"""Local Blender smoke test for the v0.7 legacy merged-arm preview."""

from __future__ import annotations

import sys
from pathlib import Path

import bpy


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "blender_addon"))
import nova1492_gx_importer as addon  # noqa: E402


def close_matrix(actual, expected, tolerance=1e-5):
    return all(
        abs(float(actual[row][column]) - float(expected[row][column])) <= tolerance
        for row in range(4)
        for column in range(4)
    )


def main() -> None:
    arguments = sys.argv[sys.argv.index("--") + 1 :]
    if len(arguments) != 1:
        raise SystemExit("usage: blender --background --python SCRIPT -- CLASSIC_COMMON")
    root = Path(arguments[0])
    result = addon.assemble_player_parts(
        bpy.context,
        str(root / "n_legs41_tdr.gx"),
        str(root / "body2_prt.gx"),
        str(root / "arm2_hbbr.gx"),
        action_id=0,
        import_animations=True,
        assembly_profile="AUTO",
    )
    if result["assembly_profile"] != "LEGACY_MERGED_ARM":
        raise AssertionError(result["assembly_profile"])
    if result["attachment_summary"] != "merge_a/larm -> BP XFI[0], merge_b/rarm -> BP XFI[1]":
        raise AssertionError(result["attachment_summary"])
    nodes = result["ap"]["node_objects"]
    bp_visual = addon._first_mesh_node(result["bp"])
    sockets = result["bp"]["xfi_data"]["transforms"]
    for branch, socket_index in ((nodes[1], 0), (nodes[8], 1)):
        if branch.parent != bp_visual:
            raise AssertionError(f"{branch.name} parent")
        if not close_matrix(branch.matrix_local, addon.to_blender_matrix(sockets[socket_index])):
            raise AssertionError(f"{branch.name} socket {socket_index}")
    counts = tuple(result[role]["meshes"] for role in ("mp", "bp", "ap"))
    if counts != (12, 1, 10):
        raise AssertionError(counts)
    print("LEGACY_PREVIEW_OK profile=LEGACY_MERGED_ARM sockets=0/1 counts=12/1/10")


if __name__ == "__main__":
    main()
