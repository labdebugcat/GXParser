from __future__ import annotations

bl_info = {
    "name": "GXParser Blender Importers",
    "author": "Project N",
    "version": (0, 6, 0),
    "blender": (4, 0, 0),
    "location": "File > Import > Nova1492 GX/XFI or Nova1492 Assembled Unit",
    "description": "Imports single GX parts or assembles MP/BP/AP with the verified XFI chain",
    "category": "Import-Export",
}

import importlib
import copy
import sys
from pathlib import Path
from typing import Any

import bpy
from bpy.props import BoolProperty, IntProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from mathutils import Matrix, Vector

if __package__:
    from . import gx_parser, xfi_parser
else:
    import gx_parser
    import xfi_parser

importlib.reload(gx_parser)
importlib.reload(xfi_parser)

AXIS_TO_BLENDER = Matrix(
    (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, -1.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
)


def to_blender_vector(value) -> tuple[float, float, float]:
    return float(value[0]), -float(value[2]), float(value[1])


def to_blender_matrix(value: list[list[float]]) -> Matrix:
    native = Matrix(value)
    return AXIS_TO_BLENDER @ native @ AXIS_TO_BLENDER.inverted()


def asset_search_roots(source_path: Path) -> list[Path]:
    """Return the small set of client folders used by the native loader."""
    candidates = [
        source_path.parent,
        source_path.parent / "common",
        source_path.parent.parent / "common",
    ]
    result: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = (
            str(candidate.resolve()).lower()
            if candidate.exists()
            else str(candidate).lower()
        )
        if candidate.is_dir() and key not in seen:
            seen.add(key)
            result.append(candidate)
    return result


def asset_index(folders: Path | list[Path]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    priorities = {".tga": 0, ".bmp": 1, ".png": 2}
    roots = [folders] if isinstance(folders, Path) else folders
    for folder in roots:
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            extension = path.suffix.lower()
            if not path.is_file() or extension not in priorities:
                continue
            result.setdefault(path.name.lower(), path)
            stem_key = f"stem:{path.stem.lower()}"
            old = result.get(stem_key)
            if old is None or priorities[extension] < priorities[old.suffix.lower()]:
                result[stem_key] = path
    return result


def resolve_asset(index: dict[str, Path], name: str) -> Path | None:
    if not name:
        return None
    filename = name.replace("\\", "/").rsplit("/", 1)[-1].lower()
    return index.get(filename) or index.get(f"stem:{Path(filename).stem}")


def load_image(index: dict[str, Path], name: str, pack_image: bool = True):
    path = resolve_asset(index, name)
    if path is None:
        return None
    try:
        image = bpy.data.images.load(str(path), check_existing=True)
        if pack_image and not image.packed_file:
            image.pack()
        return image
    except RuntimeError:
        return None


def apply_legacy_same_stem_material(
    parsed: dict[str, Any],
    source_path: Path,
    folder_index: dict[str, Path],
) -> None:
    """Resolve only the identified empty-material legacy decoration family.

    Some old map decorations contain one or more empty material slots and
    store their texture as an image with the same stem as the GX. Empty slots
    in ordinary mixed-material parts remain sentinels and are not changed.
    """
    same_stem = resolve_asset(folder_index, source_path.name)
    if same_stem is None:
        return
    meshes = parsed.get("meshes", [])
    all_slots = [
        slot
        for mesh in meshes
        for slot in mesh.get("material_set", {}).get("slots", [])
    ]
    all_uvs = [uv for mesh in meshes for uv in mesh.get("uvs", [])]
    if (
        not all_slots
        or not all_uvs
        or any(str(slot.get("texture_name", "")) for slot in all_slots)
        or any(abs(float(value)) > 1.0e-9 for uv in all_uvs for value in uv)
    ):
        return
    for mesh in meshes:
        material_set = mesh.get("material_set", {})
        slots = material_set.get("slots", [])
        if not slots:
            continue
        mesh["material_set"] = copy.deepcopy(material_set)
        for slot in mesh["material_set"]["slots"]:
            slot["texture_name"] = same_stem.name
            slot["_legacy_same_stem"] = True
        mesh["texture_name"] = same_stem.name
        vertices = mesh.get("vertices", [])
        if not vertices:
            continue
        minimum_x = min(float(vertex[0]) for vertex in vertices)
        maximum_x = max(float(vertex[0]) for vertex in vertices)
        minimum_z = min(float(vertex[2]) for vertex in vertices)
        maximum_z = max(float(vertex[2]) for vertex in vertices)
        extent_x = maximum_x - minimum_x
        extent_z = maximum_z - minimum_z
        generated = [
            (
                (float(vertex[0]) - minimum_x) / extent_x
                if abs(extent_x) > 1.0e-9
                else 0.0,
                (float(vertex[2]) - minimum_z) / extent_z
                if abs(extent_z) > 1.0e-9
                else 0.0,
            )
            for vertex in vertices
        ]
        mesh["uvs"] = generated
        if mesh.get("key_uvs"):
            mesh["key_uvs"] = [generated for _ in mesh["key_uvs"]]


def build_material(
    folder_index: dict[str, Path],
    source: dict[str, Any],
    cache: dict[tuple, bpy.types.Material],
    missing_color_textures: set[str],
    missing_alpha_textures: set[str],
    pack_images: bool,
) -> bpy.types.Material:
    color_name = str(source.get("texture_name", ""))
    alpha_name = str(source.get("alpha_texture_name", ""))
    selector = int(source.get("render_flags", 0)) & 0xFF
    diffuse_alpha = float(source.get("diffuse_alpha", 1.0))
    key = (color_name.lower(), alpha_name.lower(), selector, round(diffuse_alpha, 6))
    if key in cache:
        return cache[key]
    material = bpy.data.materials.new(
        f"GX_{Path(color_name).stem or 'empty'}_{selector}"
    )
    material.use_nodes = True
    material.diffuse_color = (1.0, 1.0, 1.0, diffuse_alpha)
    material["nova_texture"] = color_name
    material["nova_alpha_texture"] = alpha_name
    material["nova_render_flags"] = selector
    material["nova_diffuse_alpha"] = diffuse_alpha
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    image = load_image(folder_index, color_name, pack_images)
    alpha_image = load_image(folder_index, alpha_name, pack_images)
    if color_name and image is None:
        missing_color_textures.add(color_name)
    if alpha_name and alpha_image is None:
        # Missing companion alpha uses the embedded color-image alpha.
        missing_alpha_textures.add(alpha_name)
    material["nova_texture_resolved"] = str(
        resolve_asset(folder_index, color_name) or ""
    )
    material["nova_alpha_texture_resolved"] = str(
        resolve_asset(folder_index, alpha_name) or ""
    )
    texture = None
    if image is not None:
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        texture.interpolation = "Closest"
    if selector in (3, 4):
        emission = nodes.new("ShaderNodeEmission")
        emission.inputs["Strength"].default_value = 1.35
        if texture is not None:
            links.new(texture.outputs["Color"], emission.inputs["Color"])
        links.new(emission.outputs["Emission"], output.inputs["Surface"])
    else:
        shader = nodes.new("ShaderNodeBsdfPrincipled")
        shader.inputs["Roughness"].default_value = 1.0
        shader.inputs["Alpha"].default_value = diffuse_alpha
        if texture is not None:
            links.new(texture.outputs["Color"], shader.inputs["Base Color"])
            if alpha_image is None:
                links.new(texture.outputs["Alpha"], shader.inputs["Alpha"])
        if alpha_image is not None:
            alpha_texture = nodes.new("ShaderNodeTexImage")
            alpha_texture.image = alpha_image
            alpha_texture.interpolation = "Closest"
            alpha_texture.image.colorspace_settings.name = "Non-Color"
            links.new(alpha_texture.outputs["Color"], shader.inputs["Alpha"])
        links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    if alpha_image is not None or diffuse_alpha < 0.999:
        if hasattr(material, "surface_render_method"):
            material.surface_render_method = "DITHERED"
        elif hasattr(material, "blend_method"):
            material.blend_method = "BLEND"
    material.use_backface_culling = False
    cache[key] = material
    return material


def face_material_indices(mesh: dict[str, Any], frame: int) -> list[int]:
    face_count = len(mesh["indices"]) // 3
    slots = mesh.get("material_set", {}).get("slots", [])
    mapping = mesh.get("material_set", {}).get("face_map", [])
    result = []
    for face_index in range(face_count):
        slot = 0
        if len(mapping) == face_count:
            slot = int(mapping[face_index])
        elif mapping:
            slot = int(mapping[frame % len(mapping)])
        result.append(max(0, min(slot, max(len(slots) - 1, 0))))
    return result


def create_mesh_object(
    collection: bpy.types.Collection,
    parsed: dict[str, Any],
    mesh_source: dict[str, Any],
    mesh_index: int,
    frame: int,
    node_objects: list[bpy.types.Object],
    folder_index: dict[str, Path],
    material_cache: dict[tuple, bpy.types.Material],
    missing_color_textures: set[str],
    missing_alpha_textures: set[str],
    pack_images: bool,
) -> bpy.types.Object:
    channels = gx_parser.mesh_channels_at_frame(mesh_source, frame)
    vertices = [to_blender_vector(value) for value in channels["vertices"]]
    indices = mesh_source["indices"]
    faces = [
        tuple(indices[index : index + 3])
        for index in range(0, len(indices) - 2, 3)
    ]
    mesh_data = bpy.data.meshes.new(f"GX_mesh_{mesh_index:03d}")
    mesh_data.from_pydata(vertices, [], faces)
    mesh_data.update()
    uv_layer = mesh_data.uv_layers.new(name="GX_UV")
    source_uvs = channels["uvs"]
    for loop in mesh_data.loops:
        uv = source_uvs[loop.vertex_index]
        uv_layer.data[loop.index].uv = (float(uv[0]), 1.0 - float(uv[1]))
    slots = mesh_source.get("material_set", {}).get("slots", [])
    if not slots:
        slots = [
            {
                "texture_name": mesh_source.get("texture_name", ""),
                "alpha_texture_name": mesh_source.get("alpha_texture_name", ""),
                "diffuse_alpha": mesh_source.get("diffuse_alpha", 1.0),
                "render_flags": mesh_source.get("render_flags", 0),
            }
        ]
    for slot in slots:
        mesh_data.materials.append(
            build_material(
                folder_index,
                slot,
                material_cache,
                missing_color_textures,
                missing_alpha_textures,
                pack_images,
            )
        )
    for polygon, material_index in zip(
        mesh_data.polygons, face_material_indices(mesh_source, frame)
    ):
        polygon.material_index = material_index
    obj = bpy.data.objects.new(f"GX_mesh_{mesh_index:03d}", mesh_data)
    collection.objects.link(obj)
    node_index = int(mesh_source.get("node_index", -1))
    if 0 <= node_index < len(node_objects):
        obj.parent = node_objects[node_index]
        obj.matrix_parent_inverse = Matrix.Identity(4)
        obj.matrix_local = Matrix.Identity(4)
    obj["nova_mesh_index"] = mesh_index
    obj["nova_node_index"] = node_index
    obj["nova_lead"] = int(mesh_source.get("lead", 0))
    obj["nova_frame_map"] = list(mesh_source.get("frame_map", []))
    obj["nova_uv_key_count"] = len(mesh_source.get("key_uvs", []))
    obj["nova_material_frame_map"] = list(
        mesh_source.get("material_set", {}).get("face_map", [])
    )
    add_shape_keys(obj, mesh_source)
    return obj


def add_shape_keys(obj: bpy.types.Object, mesh_source: dict[str, Any]) -> None:
    key_vertices = mesh_source.get("key_vertices", [])
    if len(key_vertices) <= 1:
        return
    obj.shape_key_add(name="Basis", from_mix=False)
    for index, vertices in enumerate(key_vertices):
        block = obj.shape_key_add(name=f"GX_Key_{index:03d}", from_mix=False)
        for point, coordinate in zip(block.data, vertices):
            point.co = to_blender_vector(coordinate)
        block.value = 0.0


def create_node_objects(
    collection: bpy.types.Collection,
    parsed: dict[str, Any],
    initial_frame: int,
) -> list[bpy.types.Object]:
    result: list[bpy.types.Object] = []
    for index, node in enumerate(parsed["nodes"]):
        name = str(node.get("name", "")) or f"node_{index:03d}"
        obj = bpy.data.objects.new(f"{index:03d}_{name}", None)
        obj.empty_display_type = (
            "ARROWS" if name.lower() in ("muzzle", "muzzle1") else "PLAIN_AXES"
        )
        obj.empty_display_size = 0.12 if name.lower().startswith("muzzle") else 0.05
        collection.objects.link(obj)
        obj["nova_node_index"] = index
        obj["nova_parent_index"] = int(node.get("parent_index", -1))
        obj["nova_flags"] = int(node.get("flags", 0))
        obj["nova_name"] = name
        result.append(obj)
    for index, node in enumerate(parsed["nodes"]):
        parent_index = int(node.get("parent_index", -1))
        if 0 <= parent_index < len(result):
            result[index].parent = result[parent_index]
            result[index].matrix_parent_inverse = Matrix.Identity(4)
        result[index].matrix_local = to_blender_matrix(
            gx_parser.node_transform(node, initial_frame)
        )
    return result


def key_transform(obj: bpy.types.Object, matrix: Matrix, blender_frame: int) -> None:
    location, rotation, scale = matrix.decompose()
    obj.location = location
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = rotation
    obj.scale = scale
    obj.keyframe_insert("location", frame=blender_frame)
    obj.keyframe_insert("rotation_quaternion", frame=blender_frame)
    obj.keyframe_insert("scale", frame=blender_frame)


def action_fcurves(action: bpy.types.Action):
    if hasattr(action, "fcurves"):
        yield from action.fcurves
        return
    for layer in getattr(action, "layers", []):
        for strip in getattr(layer, "strips", []):
            for channelbag in getattr(strip, "channelbags", []):
                yield from getattr(channelbag, "fcurves", [])


def create_node_actions(
    parsed: dict[str, Any],
    xfi: dict[str, Any],
    node_objects: list[bpy.types.Object],
    gx_stem: str,
) -> None:
    action_names: dict[str, list[str]] = {}
    for clip in xfi.get("clips", []):
        action_id = int(clip["animation_id"])
        start = int(clip["start_frame"])
        end = max(int(clip["end_frame"]), start + 1)
        names: list[str] = []
        for index, (node, obj) in enumerate(zip(parsed["nodes"], node_objects)):
            if not node.get("animation"):
                continue
            action = bpy.data.actions.new(
                f"{gx_stem}.ID{action_id}.{index:03d}.{obj.get('nova_name', '')}"
            )
            obj.animation_data_create()
            obj.animation_data.action = action
            for source_frame in range(start, end):
                blender_frame = 1 + (source_frame - start) * 33
                key_transform(
                    obj,
                    to_blender_matrix(
                        gx_parser.node_transform(node, source_frame)
                    ),
                    blender_frame,
                )
            # Blender 5.x uses layered/slotted Actions; Blender 4.x exposes
            # Action.fcurves directly.
            for curve in action_fcurves(action):
                for point in curve.keyframe_points:
                    point.interpolation = "CONSTANT"
            action["nova_action_id"] = action_id
            action["nova_source_start"] = start
            action["nova_source_end_exclusive"] = end
            action["nova_frame_seconds"] = xfi_parser.FRAME_SECONDS
            names.append(action.name)
        action_names[str(action_id)] = names
    for obj in node_objects:
        obj["nova_actions"] = str(action_names)


def create_shape_actions(
    parsed: dict[str, Any],
    xfi: dict[str, Any],
    mesh_objects: list[bpy.types.Object],
    gx_stem: str,
) -> None:
    for mesh_index, (source, obj) in enumerate(
        zip(parsed["meshes"], mesh_objects)
    ):
        key_data = obj.data.shape_keys
        key_count = len(source.get("key_vertices", []))
        if key_data is None or key_count <= 1:
            continue
        mapping = source.get("frame_map", [])
        action_names: dict[str, str] = {}
        for clip in xfi.get("clips", []):
            action_id = int(clip["animation_id"])
            start = int(clip["start_frame"])
            end = max(int(clip["end_frame"]), start + 1)
            action = bpy.data.actions.new(
                f"{gx_stem}.shape.ID{action_id}.mesh_{mesh_index:03d}"
            )
            key_data.animation_data_create()
            key_data.animation_data.action = action
            for block in key_data.key_blocks[1:]:
                block.value = 0.0
            previous_key = None
            for source_frame in range(start, end):
                key_index = gx_parser.mapped_key(
                    mapping, source_frame, key_count
                )
                if key_index == previous_key:
                    continue
                blender_frame = 1 + (source_frame - start) * 33
                if previous_key is not None:
                    previous_block = key_data.key_blocks[previous_key + 1]
                    previous_block.value = 0.0
                    previous_block.keyframe_insert(
                        "value", frame=blender_frame
                    )
                current_block = key_data.key_blocks[key_index + 1]
                current_block.value = 1.0
                current_block.keyframe_insert("value", frame=blender_frame)
                previous_key = key_index
            for curve in action_fcurves(action):
                for point in curve.keyframe_points:
                    point.interpolation = "CONSTANT"
            action["nova_action_id"] = action_id
            action["nova_source_start"] = start
            action["nova_source_end_exclusive"] = end
            action["nova_frame_seconds"] = xfi_parser.FRAME_SECONDS
            action_names[str(action_id)] = action.name
        obj["nova_shape_actions"] = str(action_names)


def select_action(
    parsed: dict[str, Any],
    xfi: dict[str, Any],
    node_objects: list[bpy.types.Object],
    mesh_objects: list[bpy.types.Object],
    action_id: int,
) -> tuple[int, int]:
    clip = xfi_parser.clip_for_mode(xfi, action_id)
    start = int(clip.get("start_frame", 0))
    end = max(int(clip.get("end_frame", start)), start + 1)
    token = f".ID{action_id}."
    for obj in node_objects:
        if not obj.animation_data:
            continue
        action = next(
            (
                candidate
                for candidate in bpy.data.actions
                if token in candidate.name and candidate.name.endswith(
                    f".{obj.get('nova_name', '')}"
                )
            ),
            None,
        )
        if action is not None:
            obj.animation_data.action = action
    shape_token = f".shape.ID{action_id}."
    for obj in mesh_objects:
        key_data = obj.data.shape_keys
        if key_data is None or not key_data.animation_data:
            continue
        action = next(
            (
                candidate
                for candidate in bpy.data.actions
                if shape_token in candidate.name
                and candidate.name.endswith(
                    f".mesh_{int(obj.get('nova_mesh_index', -1)):03d}"
                )
            ),
            None,
        )
        if action is not None:
            key_data.animation_data.action = action
    return start, end


def import_gx(
    context: bpy.types.Context,
    filepath: str,
    action_id: int,
    import_animations: bool,
    pack_images: bool = True,
    strict_color_textures: bool = True,
) -> dict[str, Any]:
    path = Path(filepath)
    parsed = gx_parser.read_file(path)
    if not parsed.get("ok"):
        raise RuntimeError(parsed.get("error", "GX parse failed"))
    xfi = xfi_parser.read_for_gx(path)
    clip = xfi_parser.clip_for_mode(xfi, action_id)
    initial_frame = int(clip.get("start_frame", 0))
    collection = bpy.data.collections.new(f"GX_{path.stem}")
    context.scene.collection.children.link(collection)
    collection["nova_source_gx"] = str(path)
    collection["nova_source_xfi"] = str(xfi.get("path", ""))
    collection["nova_authority"] = "Project N2 GX/XFI rules 2026-07-30"
    collection["nova_forward_axis"] = "+Z"
    collection["nova_frame_seconds"] = xfi_parser.FRAME_SECONDS
    node_objects = create_node_objects(collection, parsed, initial_frame)
    index = asset_index(asset_search_roots(path))
    apply_legacy_same_stem_material(parsed, path, index)
    material_cache: dict[tuple, bpy.types.Material] = {}
    missing_color_textures: set[str] = set()
    missing_alpha_textures: set[str] = set()
    mesh_objects = [
        create_mesh_object(
            collection,
            parsed,
            mesh,
            mesh_index,
            initial_frame,
            node_objects,
            index,
            material_cache,
            missing_color_textures,
            missing_alpha_textures,
            pack_images,
        )
        for mesh_index, mesh in enumerate(parsed["meshes"])
    ]
    if strict_color_textures and missing_color_textures:
        missing = ", ".join(sorted(missing_color_textures))
        raise RuntimeError(
            f"GX color texture could not be loaded: {missing}. "
            "Choose the GX from the installed Nova1492 data/common folder."
        )
    if import_animations and xfi.get("ok"):
        context.scene.render.fps = 1000
        context.scene.render.fps_base = 1.0
        create_node_actions(parsed, xfi, node_objects, path.stem)
        create_shape_actions(parsed, xfi, mesh_objects, path.stem)
        start, end = select_action(
            parsed, xfi, node_objects, mesh_objects, action_id
        )
        context.scene.frame_start = 1
        context.scene.frame_end = max(1, 1 + (end - start - 1) * 33)
        context.scene.frame_set(1)
    return {
        "nodes": len(node_objects),
        "meshes": len(mesh_objects),
        "materials": len(material_cache),
        "xfi": bool(xfi.get("ok")),
        "clips": len(xfi.get("clips", [])),
        "warnings": parsed.get("warnings", []),
        "collection": collection,
        "parsed": parsed,
        "xfi_data": xfi,
        "node_objects": node_objects,
        "mesh_objects": mesh_objects,
        "loaded_images": sorted(
            {
                image.name
                for image in bpy.data.images
                if image.source == "FILE"
                and int(image.size[0]) > 0
                and int(image.size[1]) > 0
            }
        ),
        "missing_color_textures": sorted(missing_color_textures),
        "missing_alpha_textures": sorted(missing_alpha_textures),
    }


def _assembly_container(
    collection: bpy.types.Collection,
    name: str,
    node_objects: list[bpy.types.Object],
    mesh_objects: list[bpy.types.Object],
) -> bpy.types.Object:
    container = bpy.data.objects.new(name, None)
    container.empty_display_type = "PLAIN_AXES"
    container.empty_display_size = 0.18
    collection.objects.link(container)
    roots = [
        obj
        for obj in [*node_objects, *mesh_objects]
        if obj.parent is None
    ]
    for obj in roots:
        local = obj.matrix_local.copy()
        obj.parent = container
        obj.matrix_parent_inverse = Matrix.Identity(4)
        obj.matrix_local = local
    return container


def _first_mesh_node(result: dict[str, Any]) -> bpy.types.Object:
    meshes = result["parsed"].get("meshes", [])
    if not meshes:
        raise RuntimeError("GX has no mesh for assembly")
    node_index = int(meshes[0].get("node_index", -1))
    nodes = result["node_objects"]
    if not 0 <= node_index < len(nodes):
        raise RuntimeError("GX first mesh node is invalid")
    return nodes[node_index]


def assemble_player_parts(
    context: bpy.types.Context,
    mp_path: str,
    bp_path: str,
    ap_path: str,
    action_id: int = 0,
    import_animations: bool = True,
    pack_images: bool = True,
    strict_color_textures: bool = True,
) -> dict[str, Any]:
    """Import and assemble MP -> BP -> AP with the verified native chain.

    BP remains a child of the animated MP first-mesh node and AP remains a
    child of the animated BP first-mesh node.  This preserves inherited
    bobbing and attack motion instead of baking a one-frame center alignment.
    """
    mp = import_gx(
        context, mp_path, action_id, import_animations,
        pack_images, strict_color_textures
    )
    bp = import_gx(
        context, bp_path, action_id, import_animations,
        pack_images, strict_color_textures
    )
    ap = import_gx(
        context, ap_path, action_id, import_animations,
        pack_images, strict_color_textures
    )
    mp_sockets = mp["xfi_data"].get("transforms", [])
    bp_sockets = bp["xfi_data"].get("transforms", [])
    if len(mp_sockets) <= 0:
        raise RuntimeError("MP XFI attachment matrix 0 missing")
    # The verified player assembly contract always attaches AP through the
    # body's third serialized transform. AP-family guessing and visual offsets
    # are intentionally not part of the release implementation.
    ap_socket_index = 2
    if len(bp_sockets) <= ap_socket_index:
        raise RuntimeError(
            "BP XFI attachment matrix 2 missing"
        )
    mp_container = _assembly_container(
        mp["collection"], "ASSEMBLY_MP", mp["node_objects"], mp["mesh_objects"]
    )
    bp_container = _assembly_container(
        bp["collection"], "ASSEMBLY_BP", bp["node_objects"], bp["mesh_objects"]
    )
    ap_container = _assembly_container(
        ap["collection"], "ASSEMBLY_AP", ap["node_objects"], ap["mesh_objects"]
    )
    bp_container.parent = _first_mesh_node(mp)
    bp_container.matrix_parent_inverse = Matrix.Identity(4)
    bp_container.matrix_local = to_blender_matrix(mp_sockets[0])
    ap_container.parent = _first_mesh_node(bp)
    ap_container.matrix_parent_inverse = Matrix.Identity(4)
    ap_container.matrix_local = to_blender_matrix(bp_sockets[ap_socket_index])
    mp_container["nova_part_role"] = "MP"
    bp_container["nova_part_role"] = "BP"
    ap_container["nova_part_role"] = "AP"
    context.view_layer.update()
    return {
        "mp": mp,
        "bp": bp,
        "ap": ap,
        "mp_container": mp_container,
        "bp_container": bp_container,
        "ap_container": ap_container,
        "action_id": action_id,
        "dynamic_inheritance": True,
        "ap_socket_index": ap_socket_index,
    }


def show_materials_in_viewport(context: bpy.types.Context) -> None:
    """Avoid Blender's default Solid mode making a valid import look white."""
    screen = getattr(context, "screen", None)
    if screen is None:
        return
    for area in screen.areas:
        if area.type == "VIEW_3D":
            area.spaces.active.shading.type = "MATERIAL"


class IMPORT_SCENE_OT_nova1492_gx(bpy.types.Operator, ImportHelper):
    bl_idname = "import_scene.nova1492_gx"
    bl_label = "Import Nova1492 GX/XFI"
    bl_options = {"UNDO", "PRESET"}

    filename_ext = ".gx"
    filter_glob: StringProperty(default="*.gx;*.GX", options={"HIDDEN"})
    action_id: IntProperty(
        name="초기 XFI Action ID",
        description="가져온 직후 활성화할 XFI 행동 ID",
        default=0,
        min=0,
        max=255,
    )
    import_animations: BoolProperty(
        name="XFI Action 생성",
        description="각 XFI ID의 노드 애니메이션을 33ms 시간축으로 생성",
        default=True,
    )
    pack_images: BoolProperty(
        name="텍스처를 .blend에 포함",
        description="원본 이미지를 Blender 파일 안에 Pack하여 이동 후에도 보존",
        default=True,
    )
    strict_color_textures: BoolProperty(
        name="색상 텍스처 누락 시 중단",
        description="흰 모델을 조용히 만들지 않고 누락 파일명을 오류로 표시",
        default=True,
    )
    def execute(self, context):
        try:
            result = import_gx(
                context,
                self.filepath,
                self.action_id,
                self.import_animations,
                self.pack_images,
                self.strict_color_textures,
            )
        except Exception as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        self.report(
            {"INFO"},
            "GX import: nodes={nodes} meshes={meshes} materials={materials} "
            "XFI={xfi} clips={clips} images={image_count}".format(
                **result, image_count=len(result["loaded_images"])
            ),
        )
        show_materials_in_viewport(context)
        return {"FINISHED"}


class IMPORT_SCENE_OT_nova1492_assembled_unit(bpy.types.Operator):
    bl_idname = "import_scene.nova1492_assembled_unit"
    bl_label = "Import Nova1492 Assembled Unit"
    bl_description = "Import MP, BP and AP using MP XFI[0] and BP XFI[2]"
    bl_options = {"UNDO", "PRESET"}

    mp_path: StringProperty(
        name="MP GX",
        description="Lower/mobile part GX file",
        subtype="FILE_PATH",
    )
    bp_path: StringProperty(
        name="BP GX",
        description="Body part GX file",
        subtype="FILE_PATH",
    )
    ap_path: StringProperty(
        name="AP GX",
        description="Weapon part GX file",
        subtype="FILE_PATH",
    )
    action_id: IntProperty(
        name="XFI Action ID",
        description="XFI action selected after import",
        default=0,
        min=0,
        max=255,
    )
    import_animations: BoolProperty(
        name="Import XFI Animations",
        description="Create available XFI actions on the 33 ms native timeline",
        default=True,
    )
    pack_images: BoolProperty(
        name="Pack textures into .blend",
        description="Keep all loaded Nova textures inside the saved Blender file",
        default=True,
    )
    strict_color_textures: BoolProperty(
        name="Fail on missing color texture",
        description="Do not silently import a white model when a color texture is missing",
        default=True,
    )
    def draw(self, _context):
        layout = self.layout
        layout.label(text="Choose the three visual parts. ACP does not change the model.")
        layout.prop(self, "mp_path")
        layout.prop(self, "bp_path")
        layout.prop(self, "ap_path")
        layout.separator()
        layout.prop(self, "action_id")
        layout.prop(self, "import_animations")
        layout.prop(self, "pack_images")
        layout.prop(self, "strict_color_textures")

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self, width=720)

    def execute(self, context):
        paths = {
            "MP": Path(bpy.path.abspath(self.mp_path)),
            "BP": Path(bpy.path.abspath(self.bp_path)),
            "AP": Path(bpy.path.abspath(self.ap_path)),
        }
        for role, path in paths.items():
            if not path.is_file():
                self.report({"ERROR"}, f"{role} GX file not found: {path}")
                return {"CANCELLED"}
            if path.suffix.lower() != ".gx":
                self.report({"ERROR"}, f"{role} must be a GX file: {path.name}")
                return {"CANCELLED"}
        try:
            assemble_player_parts(
                context,
                str(paths["MP"]),
                str(paths["BP"]),
                str(paths["AP"]),
                self.action_id,
                self.import_animations,
                self.pack_images,
                self.strict_color_textures,
            )
        except Exception as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        self.report(
            {"INFO"},
            f"Assembled MP={paths['MP'].name}, BP={paths['BP'].name}, AP={paths['AP'].name}",
        )
        show_materials_in_viewport(context)
        return {"FINISHED"}


def menu_import(self, _context):
    self.layout.operator(
        IMPORT_SCENE_OT_nova1492_gx.bl_idname,
        text="Nova1492 GX/XFI (.gx)",
    )
    self.layout.operator(
        IMPORT_SCENE_OT_nova1492_assembled_unit.bl_idname,
        text="Nova1492 Assembled Unit (MP/BP/AP)",
    )


CLASSES = (
    IMPORT_SCENE_OT_nova1492_gx,
    IMPORT_SCENE_OT_nova1492_assembled_unit,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_import)


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
