import json
import unittest
from pathlib import Path


EVIDENCE = (
    Path(__file__).parents[1]
    / "research"
    / "evidence"
    / "gx_attachment_native_evidence_20260725.json"
)


class ProfileEvidenceTest(unittest.TestCase):
    def test_current_ar_ap_corpus_does_not_match_legacy_pair_signature(self):
        evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        assets = [
            asset
            for asset in evidence["corpus"]["assets"]
            if str(asset.get("category", "")).lower() == "ap"
        ]
        self.assertEqual(len(assets), 60)
        collisions = []
        for asset in assets:
            names = {
                str(node.get("name", "")).replace("\\", "/").rsplit("/", 1)[-1].lower()
                for node in asset.get("nodes", [])
            }
            legacy_signature = (
                {"merge_head", "merge_a", "merge_b"}.issubset(names)
                and any("larm" in name for name in names)
                and any("rarm" in name for name in names)
            )
            if legacy_signature:
                collisions.append(asset.get("gx"))
        self.assertEqual(collisions, [])


if __name__ == "__main__":
    unittest.main()
