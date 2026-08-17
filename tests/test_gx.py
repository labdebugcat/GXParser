import unittest

from gxparser.gx import decode_name, mapped_key, matrix_from_gx, mesh_channels_at_frame


class GxHelpersTest(unittest.TestCase):
    def test_cp949_name(self):
        self.assertEqual(decode_name("테스트".encode("cp949") + b"\0"), "테스트")

    def test_matrix_uses_first_three_rows(self):
        values = [float(value) for value in range(16)]
        self.assertEqual(
            matrix_from_gx(values),
            [values[0:4], values[4:8], values[8:12], [0.0, 0.0, 0.0, 1.0]],
        )

    def test_frame_map_is_clamped(self):
        self.assertEqual(mapped_key([9], 0, 3), 2)
        self.assertEqual(mapped_key([], 7, 3), 2)

    def test_static_mesh_channels(self):
        mesh = {
            "vertices": [(1.0, 2.0, 3.0)],
            "normals": [(0.0, 1.0, 0.0)],
            "uvs": [(0.25, 0.75)],
            "frame_map": [],
            "key_vertices": [],
            "key_normals": [],
            "key_uvs": [],
        }
        channels = mesh_channels_at_frame(mesh, 0)
        self.assertEqual(channels["vertices"], mesh["vertices"])
        self.assertEqual(channels["normals"], mesh["normals"])
        self.assertEqual(channels["uvs"], mesh["uvs"])


if __name__ == "__main__":
    unittest.main()
