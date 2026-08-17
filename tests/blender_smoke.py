"""Headless Blender smoke test for the single-part and assembly importers."""

from __future__ import annotations

import sys
from pathlib import Path

import bpy


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "blender_addon"))

import nova1492_gx_importer as addon  # noqa: E402


def close_vector(actual, expected, tolerance=1e-4):
    return all(abs(float(a) - float(b)) <= tolerance for a, b in zip(actual, expected))


def main() -> None:
    arguments = sys.argv[sys.argv.index("--") + 1 :]
    if len(arguments) != 1:
        raise SystemExit("usage: blender --background --python tests/blender_smoke.py -- COMMON_DIR")
    root = Path(arguments[0])
    fixtures = (
        (
            ("legs24_sts.gx", "n_body44_brps.gx", "arm76_orns.gx"),
            (16, 8, 25),
            (0.0000000049, 0.0, 1.5102072746),
            (-0.0015319951, -0.483486, 1.8444242746),
        ),
        (
            ("legs50_pps.gx", "body20_prsd.gx", "arm81_rtro.GX"),
            (25, 3, 15),
            (0.0, 0.0, 1.6011675596),
            (-0.000008, -0.000472, 1.8658175596),
        ),
    )
    for names, expected_counts, expected_bp, expected_ap in fixtures:
        paths = [str(root / name) for name in names]
        single = addon.import_gx(
            bpy.context, paths[0], 0, True, False, True
        )
        if single["meshes"] != expected_counts[0]:
            raise AssertionError(f"single import mesh count: {single['meshes']}")
        bpy.ops.wm.read_factory_settings(use_empty=True)
        assembled = addon.assemble_player_parts(
            bpy.context, *paths, 0, True, False, True
        )
        counts = tuple(assembled[role]["meshes"] for role in ("mp", "bp", "ap"))
        if counts != expected_counts:
            raise AssertionError(f"assembly mesh counts: {counts}")
        bp_origin = tuple(assembled["bp_container"].matrix_world.translation)
        ap_origin = tuple(assembled["ap_container"].matrix_world.translation)
        if not close_vector(bp_origin, expected_bp):
            raise AssertionError(f"BP origin: {bp_origin}")
        if not close_vector(ap_origin, expected_ap):
            raise AssertionError(f"AP origin: {ap_origin}")
        bpy.ops.wm.read_factory_settings(use_empty=True)
    print("BLENDER_IMPORTERS_OK single=2/2 assembly=2/2 contract=MP_XFI0_BP_XFI2")


if __name__ == "__main__":
    main()
