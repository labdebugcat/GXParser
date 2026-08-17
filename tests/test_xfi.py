import tempfile
import unittest
from pathlib import Path

from gxparser.xfi import clip_for_mode, matrix_from_xfi, read_file


class XfiParserTest(unittest.TestCase):
    def test_matrix_transposes_stored_values(self):
        values = [float(value) for value in range(16)]
        self.assertEqual(
            matrix_from_xfi(values, 0),
            [
                [0.0, 4.0, 8.0, 12.0],
                [1.0, 5.0, 9.0, 13.0],
                [2.0, 6.0, 10.0, 14.0],
                [0.0, 0.0, 0.0, 1.0],
            ],
        )

    def test_numeric_clip_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "sample.xfi")
            path.write_text("-1,1,7,10,20", encoding="utf-8")
            parsed = read_file(path)
        self.assertTrue(parsed["ok"])
        self.assertEqual(parsed["clips"], [{"animation_id": 7, "start_frame": 10, "end_frame": 20}])

    def test_clip_falls_back_to_first_entry(self):
        xfi = {"clips": [{"animation_id": 3, "start_frame": 5, "end_frame": 9}]}
        self.assertEqual(clip_for_mode(xfi, 99), xfi["clips"][0])


if __name__ == "__main__":
    unittest.main()
