import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import photo.photo_suport as photo_suport


class PhotoSuportTests(unittest.TestCase):
    def test_extract_from_file_parses_postfix_model_tag(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "20240101_123456_EOS500.jpg")
            with open(file_path, "wb") as handle:
                handle.write(b"test")

            camera, model, dt = photo_suport.extract_from_file(file_path)

            self.assertEqual(camera, "CANON")
            self.assertEqual(model, "EOS 500D")
            self.assertIsNotNone(dt)


if __name__ == "__main__":
    unittest.main()
