#!/usr/bin/env python3
"""Tests for tools/build_examples.py, on a copy of one example: the check writes nothing and fails on any drift, the
build date and artifact times are ignored, and writing removes only files the engine makes.

  python3 tools/test_build_examples.py
"""
import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_examples as B  # noqa: E402

NAME = "devtool-dense"


def tree(d):
    return {p.relative_to(d).as_posix(): p.read_bytes() for p in sorted(d.rglob("*")) if p.is_file()}


class BuildExamples(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "examples"
        self.ex = self.root / NAME
        shutil.copytree(B.EXAMPLES / NAME, self.ex)

    def tearDown(self):
        self.tmp.cleanup()

    def run_tool(self, *argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            code = B.main(list(argv), root=self.root)
        return code, out.getvalue()

    def test_committed_example_matches_and_check_writes_nothing(self):
        before = tree(self.ex)
        code, out = self.run_tool("--check")
        self.assertEqual(code, 0, out)
        self.assertIn("matches the engine", out)
        self.assertEqual(tree(self.ex), before)

    def test_check_names_a_changed_token_file_and_leaves_it(self):
        f = self.ex / "tokens" / "primitives.tokens.json"
        f.write_text(f.read_text().replace("#", "#0", 1))
        before = tree(self.ex)
        code, out = self.run_tool("--check")
        self.assertEqual(code, 1)
        self.assertIn(f"examples/{NAME}/tokens/primitives.tokens.json differs", out)
        self.assertEqual(tree(self.ex), before)

    def test_check_finds_a_stale_file_and_a_hand_edit(self):
        (self.ex / "build" / "css" / "old.css").write_text(":root{}\n")
        d = self.ex / "DESIGN.md"
        d.write_text(d.read_text() + "\nA note written by hand outside an od:keep block.\n")
        code, out = self.run_tool("--check")
        self.assertEqual(code, 1)
        self.assertIn("build/css/old.css is no longer made", out)
        self.assertIn("DESIGN.md.hand-edited is new", out)  # the engine keeps the edit aside; the check says so

    def test_build_date_and_artifact_times_are_ignored(self):
        ov, art = self.ex / "overview.html", self.ex / "build" / "artifact" / "project" / "design-system.json"
        ov.write_text(B.STAMPS["overview.html"][0][0].sub("· built 2020-01-01", ov.read_text()))
        doc = json.loads(art.read_text())
        doc["createdOnFiles"]["at"] = doc["lastChange"]["at"] = "2020-01-01T00:00:00Z"
        art.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
        before = tree(self.ex)
        code, out = self.run_tool("--check")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.run_tool()[0], 0)
        self.assertEqual(tree(self.ex), before)  # writing keeps a file whose only change is a stamp

    def test_write_restores_tokens_removes_stale_files_and_keeps_a_persons_files(self):
        f = self.ex / "tokens" / "primitives.tokens.json"
        good = f.read_bytes()
        f.write_text("{}\n")
        (self.ex / "build" / "css" / "old.css").write_text(":root{}\n")
        (self.ex / "notes.txt").write_text("kept\n")
        code, out = self.run_tool()
        self.assertEqual(code, 0, out)
        self.assertEqual(f.read_bytes(), good)
        self.assertFalse((self.ex / "build" / "css" / "old.css").exists())
        self.assertEqual((self.ex / "notes.txt").read_text(), "kept\n")
        self.assertEqual(self.run_tool("--check")[0], 0)

    def test_a_failed_build_changes_nothing(self):
        (self.ex / "state.json").write_text("{ not json")
        before = tree(self.ex)
        code, out = self.run_tool()
        self.assertEqual(code, 1)
        self.assertIn("engine.py build failed", out)
        self.assertEqual(tree(self.ex), before)

    def test_readme_numbers_come_from_the_tokens(self):
        meta = json.loads((self.ex / "tokens" / "opendesigner.meta.json").read_text())
        readme = (self.ex / "README.md").read_text()
        self.assertIn(f"body {meta['type']['base']}px", readme)
        self.assertIn(f"python3 tools/build_examples.py {NAME}", readme)
        self.assertNotIn("make_examples", readme)

    def test_unknown_example_is_refused(self):
        with self.assertRaises(SystemExit):
            self.run_tool("no-such-example")


if __name__ == "__main__":
    unittest.main()
