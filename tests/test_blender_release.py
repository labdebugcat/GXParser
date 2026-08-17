import re
import unittest
from pathlib import Path


SOURCE = Path(__file__).parents[1] / "blender_addon" / "nova1492_gx_importer" / "__init__.py"


class BlenderReleaseContractTest(unittest.TestCase):
    def test_preview_keeps_ar_and_adds_legacy_pair_profiles(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("ap_socket_index = 2", text)
        self.assertIn("mp_sockets[0]", text)
        self.assertIn('"LEGACY_MERGED_ARM"', text)
        self.assertIn('(left, 0, "larm")', text)
        self.assertIn('(right, 1, "rarm")', text)
        self.assertIn("detect_assembly_profile", text)

    def test_preview_version_is_0_7(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertRegex(text, re.compile(r'"version": \(0, 7, 0\)'))


if __name__ == "__main__":
    unittest.main()
