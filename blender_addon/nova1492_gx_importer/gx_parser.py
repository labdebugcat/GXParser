"""Nova1492 GX parser ported from N2's verified Godot GxReader.

This module deliberately has no Blender dependency.  It is used both by the
Blender add-on and by the cross-runtime contract test.
"""

from __future__ import annotations

import math
import struct
from pathlib import Path
from typing import Any

MARKERS = (
    b"4294901766d",
    b"4294901773d{",
    b"4294901774d{",
    b"4294901777d{",
    b"4294901778d{",
    b"4294901779d{",
    b"4294901780d{",
    b"4294901781d{",
    b"4294901782d{",
    b"4294901783d{",
)
CLOSE = b"4294901766d"
TEXTURE_MARKER = b"4294901779d{"


def u16(data: bytes, offset: int) -> int:
    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def f32(data: bytes, offset: int) -> float:
    return struct.unpack_from("<f", data, offset)[0]


def decode_name(value: bytes) -> str:
    if not value:
        return ""
    for encoding in ("cp949", "utf-8", "latin-1"):
        try:
            return value.decode(encoding).rstrip("\x00")
        except UnicodeDecodeError:
            pass
    return value.decode("latin-1", errors="replace").rstrip("\x00")


def identity_matrix() -> list[list[float]]:
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def matrix_from_gx(values: list[float]) -> list[list[float]]:
    """Match GxReader._transform_from_matrix exactly."""
    return [
        [values[0], values[1], values[2], values[3]],
        [values[4], values[5], values[6], values[7]],
        [values[8], values[9], values[10], values[11]],
        [0.0, 0.0, 0.0, 1.0],
    ]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a[row][k] * b[k][column] for k in range(4)) for column in range(4)]
        for row in range(4)
    ]


def mapped_key(mapping: list[int], frame: int, count: int) -> int:
    if count <= 0:
        return 0
    key = frame
    if mapping:
        key = mapping[frame % len(mapping)]
    return max(0, min(int(key), count - 1))


def animation_transform(animation: dict[str, Any], frame: int) -> list[list[float]]:
    transforms = animation.get("transforms", [])
    if not transforms:
        return identity_matrix()
    return transforms[mapped_key(animation.get("frame_map", []), frame, len(transforms))]


def node_transform(node: dict[str, Any], frame: int | None = None) -> list[list[float]]:
    if frame is not None and node.get("animation"):
        return animation_transform(node["animation"], frame)
    return matrix_from_gx(node["matrix"])


def node_world_transform(nodes: list[dict[str, Any]], index: int, frame: int) -> list[list[float]]:
    chain: list[int] = []
    seen: set[int] = set()
    while 0 <= index < len(nodes) and index not in seen:
        seen.add(index)
        chain.insert(0, index)
        index = int(nodes[index].get("parent_index", -1))
    result = identity_matrix()
    for node_index in chain:
        result = matmul(result, node_transform(nodes[node_index], frame))
    return result


def mesh_channels_at_frame(mesh: dict[str, Any], frame: int) -> dict[str, Any]:
    mapping = mesh.get("frame_map", [])
    vertices = mesh["vertices"]
    normals = mesh["normals"]
    uvs = mesh["uvs"]
    if mesh.get("key_vertices"):
        values = mesh["key_vertices"]
        vertices = values[mapped_key(mapping, frame, len(values))]
    if mesh.get("key_normals"):
        values = mesh["key_normals"]
        normals = values[mapped_key(mapping, frame, len(values))]
    if mesh.get("key_uvs"):
        values = mesh["key_uvs"]
        uvs = values[mapped_key(mapping, frame, len(values))]
    safe_normals = []
    for normal in normals:
        length2 = sum(component * component for component in normal)
        safe_normals.append(
            normal
            if all(math.isfinite(component) for component in normal) and length2 > 1e-12
            else (0.0, 1.0, 0.0)
        )
    return {"vertices": vertices, "normals": safe_normals, "uvs": uvs}


def material_surfaces(
    mesh: dict[str, Any], material_set: dict[str, Any], frame: int = 0
) -> list[dict[str, Any]]:
    slots = material_set.get("slots", [])
    if not slots:
        return []
    indices = mesh["indices"]
    face_count = len(indices) // 3
    face_map = material_set.get("face_map", [])
    grouped: dict[int, list[int]] = {}
    for face_index in range(face_count):
        slot_index = 0
        if len(face_map) == face_count:
            slot_index = int(face_map[face_index])
        elif face_map:
            slot_index = int(face_map[frame % len(face_map)])
        slot_index = max(0, min(slot_index, len(slots) - 1))
        grouped.setdefault(slot_index, []).extend(
            indices[face_index * 3 : face_index * 3 + 3]
        )
    result = []
    for slot_index in sorted(grouped):
        slot = slots[slot_index]
        result.append(
            {
                "indices": grouped[slot_index],
                "texture_name": slot["texture_name"],
                "alpha_texture_name": slot["alpha_texture_name"],
                "diffuse_alpha": slot["diffuse_alpha"],
                "render_flags": slot["render_flags"],
                "slot_index": slot_index,
            }
        )
    return result


def read_file(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        data = source.read_bytes()
    except OSError as error:
        return {"ok": False, "error": str(error), "path": str(source)}
    records = scan_records(data)
    result: dict[str, Any] = {
        "ok": True,
        "path": str(source),
        "nodes": [],
        "meshes": [],
        "warnings": [],
    }
    stack: list[int] = []
    internal_material_closes: set[int] = set()
    current_texture: dict[str, Any] = {}
    current_render_flags = 0
    current_diffuse_alpha = 1.0
    current_material_set: dict[str, Any] = {}
    current_animation: dict[str, Any] | None = None
    for record_index, record in enumerate(records):
        offset, marker = record
        payload = offset + len(marker)
        record_end = records[record_index + 1][0] if record_index + 1 < len(records) else len(data)
        if marker == CLOSE:
            if offset in internal_material_closes:
                continue
            if stack:
                stack.pop()
            continue
        if marker == b"4294901778d{":
            node = parse_node(data, payload, offset, active_node_index(stack))
            if not node:
                result["warnings"].append(f"node parse failed: 0x{offset:X}")
                continue
            result["nodes"].append(node)
            stack.append(len(result["nodes"]) - 1)
            current_texture = {}
            current_render_flags = 0
            current_diffuse_alpha = 1.0
            current_material_set = {}
            current_animation = None
            continue
        if marker == b"4294901779d{":
            current_texture = parse_texture_record(data, payload)
            continue
        if marker in (b"4294901774d{", b"4294901783d{"):
            current_material_set = parse_material_set(data, payload)
            internal_material_closes.update(current_material_set["internal_closes"])
            slots = current_material_set["slots"]
            if slots:
                current_diffuse_alpha = float(slots[0]["diffuse_alpha"])
                current_render_flags = int(slots[0]["render_flags"])
            stack.append(-1)
            continue
        if marker in (b"4294901777d{", b"4294901782d{"):
            current_animation = parse_animation(
                data, payload, marker == b"4294901782d{"
            )
            stack.append(-1)
            continue
        if marker in (b"4294901780d{", b"4294901781d{"):
            mesh = parse_mesh(data, payload, record_end, offset)
            if not mesh.get("ok"):
                result["warnings"].append(mesh.get("error", "mesh parse failed"))
            else:
                mesh.pop("ok", None)
                mesh["node_index"] = active_node_index(stack)
                mesh["texture_name"] = current_texture.get("name", "")
                mesh["alpha_texture_name"] = current_texture.get("alpha_name", "")
                mesh["render_flags"] = current_render_flags
                mesh["diffuse_alpha"] = current_diffuse_alpha
                mesh["material_set"] = current_material_set
                mesh["surfaces"] = material_surfaces(mesh, current_material_set, 0)
                mesh["animation"] = current_animation or {}
                if current_animation is not None and mesh["node_index"] >= 0:
                    result["nodes"][mesh["node_index"]]["animation"] = current_animation
                result["meshes"].append(mesh)
                current_material_set = {}
            stack.append(-1)
    return result


def scan_records(data: bytes) -> list[tuple[int, bytes]]:
    records: list[tuple[int, bytes]] = []
    offset = 0
    while offset < len(data):
        if data[offset] != ord("4"):
            offset += 1
            continue
        marker = next((candidate for candidate in MARKERS if data.startswith(candidate, offset)), None)
        if marker is None:
            offset += 1
        else:
            records.append((offset, marker))
            offset += len(marker)
    return records


def active_node_index(stack: list[int]) -> int:
    for index in reversed(stack):
        if index >= 0:
            return index
    return -1


def parse_node(data: bytes, payload: int, offset: int, parent_index: int) -> dict[str, Any]:
    if payload + 4 > len(data):
        return {}
    name_length = u32(data, payload)
    name_start = payload + 4
    matrix_start = name_start + name_length
    if matrix_start + 68 > len(data):
        return {}
    matrix = list(struct.unpack_from("<16f", data, matrix_start))
    return {
        "offset": offset,
        "name": decode_name(data[name_start:matrix_start]),
        "matrix": matrix,
        "flags": u32(data, matrix_start + 64),
        "parent_index": parent_index,
    }


def parse_texture_record(data: bytes, payload: int) -> dict[str, Any]:
    if payload + 4 > len(data):
        return {}
    name_length = u32(data, payload)
    name_start = payload + 4
    name_end = name_start + name_length
    if name_end + 4 > len(data):
        return {}
    alpha_length = u32(data, name_end)
    alpha_start = name_end + 4
    alpha_end = alpha_start + alpha_length
    if alpha_end > len(data):
        return {}
    return {
        "name": decode_name(data[name_start:name_end]),
        "alpha_name": decode_name(data[alpha_start:alpha_end]) if alpha_length else "",
    }


def parse_material_set(data: bytes, payload: int) -> dict[str, Any]:
    if payload + 8 > len(data):
        return {"slots": [], "face_map": [], "internal_closes": []}
    slot_count = u32(data, payload)
    face_map_count = u32(data, payload + 4)
    cursor = payload + 8
    face_map = []
    for _ in range(face_map_count):
        if cursor + 4 > len(data):
            break
        face_map.append(u32(data, cursor))
        cursor += 4
    slots = []
    internal_closes = []
    for slot_index in range(slot_count):
        if cursor + 24 > len(data):
            break
        properties = list(struct.unpack_from("<6I", data, cursor))
        cursor += 24
        texture: dict[str, Any] = {}
        if data.startswith(TEXTURE_MARKER, cursor):
            cursor += len(TEXTURE_MARKER)
            texture = parse_texture_record(data, cursor)
            if cursor + 4 <= len(data):
                name_length = u32(data, cursor)
                cursor += 4 + name_length
                if cursor + 4 <= len(data):
                    alpha_length = u32(data, cursor)
                    cursor += 4 + alpha_length
        elif data.startswith(CLOSE, cursor):
            if slot_index + 1 < slot_count:
                internal_closes.append(cursor)
            cursor += len(CLOSE)
        slots.append(
            {
                "texture_name": texture.get("name", ""),
                "alpha_texture_name": texture.get("alpha_name", ""),
                "diffuse_alpha": ((properties[1] >> 24) & 0xFF) / 255.0,
                "render_flags": properties[5],
                "properties": properties,
            }
        )
    return {
        "slots": slots,
        "face_map": face_map,
        "internal_closes": internal_closes,
    }


def parse_animation(data: bytes, payload: int, has_frame_map: bool) -> dict[str, Any] | None:
    cursor = payload
    while cursor < len(data) and ord("0") <= data[cursor] <= ord("9"):
        cursor += 1
    if cursor == payload or cursor >= len(data) or data[cursor] != ord("d"):
        return None
    matrix_count = int(data[payload:cursor].decode("ascii"))
    cursor += 1
    if matrix_count <= 0 or cursor + matrix_count * 64 > len(data):
        return None
    transforms = []
    for matrix_index in range(matrix_count):
        values = list(struct.unpack_from("<16f", data, cursor + matrix_index * 64))
        transforms.append(matrix_from_gx(values))
    cursor += matrix_count * 64
    frame_map: list[int] = []
    if has_frame_map:
        count_start = cursor
        while cursor < len(data) and ord("0") <= data[cursor] <= ord("9"):
            cursor += 1
        if cursor > count_start and cursor < len(data) and data[cursor] == ord("d"):
            frame_count = int(data[count_start:cursor].decode("ascii"))
            cursor += 1
            for index in range(frame_count):
                if cursor + index * 2 + 2 > len(data):
                    break
                frame_map.append(u16(data, cursor + index * 2))
    if not frame_map:
        frame_map = list(range(matrix_count))
    return {"transforms": transforms, "frame_map": frame_map}


def parse_mesh(data: bytes, payload: int, record_end: int, offset: int) -> dict[str, Any]:
    if payload + 17 > len(data):
        return {"ok": False, "error": f"truncated mesh header: 0x{offset:X}"}
    lead = data[payload]
    key_count = 0
    frame_map: list[int] = []
    key_offsets: list[int] = []
    if lead == 0:
        vertex_count = u32(data, payload + 9)
        index_count = u32(data, payload + 13)
        vertex_offset = payload + 17
    else:
        key_count = u32(data, payload + 1)
        frame_count = u32(data, payload + 5)
        mapping_offset = payload + 9
        frame_map = [
            u32(data, mapping_offset + frame_index * 4)
            for frame_index in range(frame_count)
        ]
        first_key = mapping_offset + frame_count * 4
        if first_key + 8 > record_end:
            return {"ok": False, "error": f"truncated animation base: 0x{offset:X}"}
        vertex_count = u32(data, first_key)
        index_count = u32(data, first_key + 4)
        searched_count = key_count + 1 if lead == 1 else key_count
        found = find_key_offsets(
            data, first_key, record_end, vertex_count, index_count, searched_count
        )
        key_offsets = found
        if lead == 1 and len(found) == key_count + 1:
            key_offsets = [found[0], *found[2:]]
        if len(key_offsets) != key_count:
            return {"ok": False, "error": f"animation key count mismatch: 0x{offset:X}"}
        vertex_offset = key_offsets[0] + 8
    if vertex_count <= 0 or index_count <= 0 or vertex_count > 1_000_000:
        return {"ok": False, "error": f"invalid mesh counts: 0x{offset:X}"}
    normal_offset = vertex_offset + vertex_count * 12
    uv_offset = normal_offset + vertex_count * 12
    index_offset = uv_offset + vertex_count * 8
    if index_offset + index_count * 2 > len(data):
        return {"ok": False, "error": f"truncated mesh data: 0x{offset:X}"}
    vertices = read_vec3_array(data, vertex_offset, vertex_count)
    normals = read_vec3_array(data, normal_offset, vertex_count)
    uvs = read_vec2_array(data, uv_offset, vertex_count)
    indices = [u16(data, index_offset + index * 2) for index in range(index_count)]
    if any(index >= vertex_count for index in indices):
        return {"ok": False, "error": f"index out of range: 0x{offset:X}"}
    result: dict[str, Any] = {
        "ok": True,
        "lead": lead,
        "vertices": vertices,
        "normals": normals,
        "uvs": uvs,
        "indices": indices,
        "frame_map": frame_map,
        "key_vertices": [],
        "key_normals": [],
        "key_uvs": [],
    }
    if lead & 6:
        for key_index, key_offset in enumerate(key_offsets):
            key_end = key_offsets[key_index + 1] if key_index + 1 < len(key_offsets) else record_end
            key_normal_offset = (
                key_offset + 8 + vertex_count * 12
                if key_index == 0
                else find_normal_stream(data, key_offset, key_end, vertex_count)
            )
            if key_normal_offset < 0:
                return {"ok": False, "error": f"normal key missing: 0x{offset:X}"}
            # The vertex stream always begins after the key header. Some
            # effect keys carry additional native channels before normals;
            # deriving vertices backwards from normals misread those channels.
            result["key_vertices"].append(
                read_vec3_array(data, key_offset + 8, vertex_count)
            )
            result["key_normals"].append(
                read_vec3_array(data, key_normal_offset, vertex_count)
            )
            if lead & 1:
                result["key_uvs"].append(
                    read_vec2_array(data, key_normal_offset + vertex_count * 12, vertex_count)
                )
    elif lead == 1:
        result["key_vertices"].append(vertices)
        result["key_normals"].append(normals)
        result["key_uvs"].append(uvs)
        for key_offset in key_offsets[1:]:
            result["key_vertices"].append(vertices)
            result["key_normals"].append(normals)
            result["key_uvs"].append(read_vec2_array(data, key_offset + 8, vertex_count))
    return result


def read_vec3_array(data: bytes, offset: int, count: int) -> list[tuple[float, float, float]]:
    return [
        struct.unpack_from("<3f", data, offset + index * 12)
        for index in range(count)
    ]


def read_vec2_array(data: bytes, offset: int, count: int) -> list[tuple[float, float]]:
    return [
        struct.unpack_from("<2f", data, offset + index * 8)
        for index in range(count)
    ]


def find_key_offsets(
    data: bytes, start: int, end: int, vertex_count: int, index_count: int, count: int
) -> list[int]:
    result = []
    first_byte = bytes((vertex_count & 0xFF,))
    cursor = start
    while cursor <= end - 8 and len(result) < count:
        found = data.find(first_byte, cursor)
        if found < 0 or found >= end:
            break
        if found <= end - 8 and u32(data, found) == vertex_count and u32(data, found + 4) == index_count:
            result.append(found)
            cursor = found + 8
        else:
            cursor = found + 1
    return result


def find_normal_stream(data: bytes, start: int, end: int, vertex_count: int) -> int:
    byte_count = vertex_count * 12
    required = vertex_count if vertex_count < 20 else vertex_count - 1
    for offset in range(start + 8 + byte_count, end - byte_count + 1, 4):
        unit_vectors = 0
        valid = True
        for index in range(vertex_count):
            value = struct.unpack_from("<3f", data, offset + index * 12)
            length = math.sqrt(sum(component * component for component in value))
            if not math.isfinite(length):
                valid = False
                break
            if 0.75 <= length <= 1.25:
                unit_vectors += 1
        if valid and unit_vectors >= required:
            return offset
    return -1
