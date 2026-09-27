#!/usr/bin/env python3
"""Check that each standalone skill zip can run its bundled engine's visual command."""
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
            for name in ("opendesigner-extract", "opendesigner-extend", "opendesigner-export"):
                with self.subTest(skill=name), zipfile.ZipFile(Path(tmp) / f"{name}.zip") as z:
                    root = f"{name}/"
                    names = z.namelist()
                    self.assertIn(root + "scripts/engine.py", names)
                    bundled = [item for item in names if item.startswith(root + "assets/templates/") and item.endswith(".html")]
                    self.assertGreaterEqual(len(bundled), 8)
                    for template in templates:
                        self.assertIn(root + "assets/templates/" + template.name, names)


if __name__ == "__main__":
    unittest.main()
