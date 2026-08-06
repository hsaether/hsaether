import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import photo.photo_rename as photo_rename
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

    def test_main_renames_sidecar_thumbnail_when_requested(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root_dir = os.path.join(tmpdir, "photos")
            os.makedirs(root_dir, exist_ok=True)

            original_path = os.path.join(root_dir, "20240101_123456.jpg")
            with open(original_path, "wb") as handle:
                handle.write(b"test")

            sidecar_path = os.path.join(root_dir, "20240101_123456.thm")
            with open(sidecar_path, "wb") as handle:
                handle.write(b"thumb")

            _, rename_list = photo_rename.build_plan(root_dir, info=False)
            self.assertTrue(rename_list)
            self.assertEqual(rename_list[0]["old_file2"], sidecar_path)

            old_argv = sys.argv[:]
            sys.argv = ["photo_rename.py", root_dir, "--rename", "--no-info"]
            try:
                exit_code = photo_rename.main()
            finally:
                sys.argv = old_argv

            self.assertEqual(exit_code, 0)
            self.assertFalse(os.path.exists(original_path))
            self.assertFalse(os.path.exists(sidecar_path))
            self.assertTrue(any(name.endswith(".jpg") for name in os.listdir(root_dir)))
            self.assertTrue(any(name.endswith(".thm") for name in os.listdir(root_dir)))


if __name__ == "__main__":
    unittest.main()
