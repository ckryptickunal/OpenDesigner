#!/usr/bin/env python3
"""Check that each standalone skill zip can run its bundled engine's visual command, and that the ChatGPT bundle holds
the knowledge files and only the text people paste.

  python3 tools/test_build_dist.py
"""
import contextlib
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

import build_dist


class StandaloneSkills(unittest.TestCase):
    def test_bundled_engine_has_visual_templates(self):
        templates = sorted((build_dist.SRC / "opendesigner" / "assets" / "templates").glob("*.html"))
        self.assertGreaterEqual(len(templates), 8)
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(build_dist, "DIST", Path(tmp)), \
                 mock.patch("sys.argv", ["build_dist.py"]), \
                 contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as exit_status:
                    build_dist.main()
                self.assertEqual(exit_status.exception.code, 0)
            for name in ("opendesigner-extract", "opendesigner-extend", "opendesigner-export", "opendesigner-illustrate", "opendesigner-review", "opendesigner-paint"):
                with self.subTest(skill=name), zipfile.ZipFile(Path(tmp) / f"{name}.zip") as z:
                    root = f"{name}/"
                    names = z.namelist()
                    self.assertIn(root + "scripts/engine.py", names)
                    bundled = [item for item in names if item.startswith(root + "assets/templates/") and item.endswith(".html")]
                    self.assertGreaterEqual(len(bundled), 8)
                    for template in templates:
                        self.assertIn(root + "assets/templates/" + template.name, names)


class ChatGPTBundle(unittest.TestCase):
    def run_main(self, tmp, *args):
        with mock.patch.object(build_dist, "DIST", Path(tmp)), mock.patch("sys.argv", ["build_dist.py", *args]), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as exit_status:
                build_dist.main()
        self.assertEqual(exit_status.exception.code, 0)

    def test_one_download_with_the_knowledge_files_and_only_the_paste_text(self):
        knowledge = sorted(f for f in (build_dist.GPT / "knowledge").iterdir() if f.is_file())
        self.assertTrue(knowledge)
        with tempfile.TemporaryDirectory() as tmp:
            self.run_main(tmp)
            with zipfile.ZipFile(Path(tmp) / "opendesigner-chatgpt.zip") as z:
                root = "opendesigner-chatgpt/"
                self.assertEqual(sorted(z.namelist()), sorted([root + "README.txt", root + "instructions.txt"]
                                                              + [root + "knowledge/" + f.name for f in knowledge]))
                for f in knowledge:
                    self.assertEqual(z.read(root + "knowledge/" + f.name), f.read_bytes(), f.name)
                paste = z.read(root + "instructions.txt").decode("utf-8")
                readme = z.read(root + "README.txt").decode("utf-8")
        source = (build_dist.GPT / "instructions.md").read_text(encoding="utf-8")
        self.assertTrue(source.endswith(paste), "instructions.txt is the end of instructions.md, word for word")
        self.assertTrue(paste.startswith("You are OpenDesigner"), paste[:60])
        for note in ("# OpenDesigner for ChatGPT Projects", "tools/build_data.py", "\n---\n"):
            self.assertIn(note, source)
            self.assertNotIn(note, paste)  # the notes above the line are for people reading the repository
        self.assertIn(f"Upload the {len(knowledge)} files", readme)
        for f in knowledge:
            self.assertIn(f.name, readme)

    def test_check_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.run_main(tmp, "--check")
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
