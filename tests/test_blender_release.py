import re
import unittest
from pathlib import Path


SOURCE = Path(__file__).parents[1] / "blender_addon" / "nova1492_gx_importer" / "__init__.py"


class BlenderReleaseContractTest(unittest.TestCase):
    def test_release_uses_verified_socket_chain(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("ap_socket_index = 2", text)
        self.assertIn("mp_sockets[0]", text)
        self.assertNotIn("AP_MOUNT_SOCKET", text)
        self.assertNotIn("detect_ap_mount_type", text)

    def test_release_version_is_0_6(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertRegex(text, re.compile(r'"version": \(0, 6, 0\)'))


if __name__ == "__main__":
    unittest.main()
