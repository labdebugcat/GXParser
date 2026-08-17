"""Pure Python reader for XFI transforms and animation ranges."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

FRAME_SECONDS = 0.033
NUMBER = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def matrix_from_xfi(values: list[float], offset: int) -> list[list[float]]:
    """Transpose the stored Direct3D row-vector layout."""
    return [
        [values[offset], values[offset + 4], values[offset + 8], values[offset + 12]],
        [values[offset + 1], values[offset + 5], values[offset + 9], values[offset + 13]],
        [values[offset + 2], values[offset + 6], values[offset + 10], values[offset + 14]],
        [0.0, 0.0, 0.0, 1.0],
    ]


def read_for_gx(gx_path: str | Path) -> dict[str, Any]:
    source = Path(gx_path)
    candidates = (source.with_suffix(".xfi"), source.with_suffix(".XFI"))
    path = next((candidate for candidate in candidates if candidate.is_file()), None)
    if path is None:
        return {"ok": False, "transforms": [], "clips": []}
    return read_file(path)


def read_file(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        text = source.read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        return {"ok": False, "error": str(error), "transforms": [], "clips": []}
    values = [float(match.group(0)) for match in NUMBER.finditer(text)]
    if not values:
        return {"ok": False, "transforms": [], "clips": []}
    first_token = text.split(",", 1)[0].strip()
    named_layout = not re.fullmatch(r"[-+]?\d+", first_token)
    layout_code = int(values[0])
    if len(values) == 1:
        return {
            "ok": True,
            "path": str(source),
            "layout_code": layout_code,
            "layout_name": first_token if named_layout else "",
            "transforms": [],
            "declared_clip_count": 0,
            "clips": [],
        }
    if named_layout:
        candidates = [layout_code]
    elif layout_code == -1:
        candidates = [0]
    elif layout_code == 0:
        candidates = [0, 1]
    elif layout_code == 1:
        candidates = [1, 5, 6]
    else:
        candidates = [0]
    for matrix_count in candidates:
        count_offset = 1 + matrix_count * 16
        if count_offset >= len(values):
            continue
        remaining = len(values) - count_offset - 1
        if remaining < 0 or remaining % 3:
            continue
        transforms = [
            matrix_from_xfi(values, 1 + index * 16)
            for index in range(matrix_count)
        ]
        clip_count = int(values[count_offset])
        clips = []
        cursor = count_offset + 1
        valid = True
        while cursor + 2 < len(values):
            triple = values[cursor : cursor + 3]
            if any(value != round(value) for value in triple):
                valid = False
                break
            clips.append(
                {
                    "animation_id": int(triple[0]),
                    "start_frame": int(triple[1]),
                    "end_frame": int(triple[2]),
                }
            )
            cursor += 3
        if valid and len(clips) >= clip_count:
            return {
                "ok": True,
                "path": str(source),
                "layout_code": layout_code,
                "layout_name": first_token if named_layout else "",
                "transforms": transforms,
                "declared_clip_count": clip_count,
                "clips": clips,
            }
    return {"ok": False, "transforms": [], "clips": []}


def clip_for_mode(xfi: dict[str, Any], action_id: int) -> dict[str, int]:
    for clip in xfi.get("clips", []):
        if int(clip.get("animation_id", -1)) == action_id:
            return clip
    clips = xfi.get("clips", [])
    return clips[0] if clips else {
        "animation_id": action_id,
        "start_frame": 0,
        "end_frame": 0,
    }
