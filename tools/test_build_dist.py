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
        with tempfile.TemporaryDirectory(dir=build_dist.ROOT) as tmp:
            with mock.patch.object(build_dist, "DIST", Path(tmp)), \
                 mock.patch("sys.argv", ["build_dist.py"]), \
                 contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as exit_status:
                    build_dist.main()
                self.assertEqual(exit_status.exception.code, 0)
            for name in ("opendesigner-extract", "opendesigner-extend", "opendesigner-export"):
                with self.subTest(skill=name), zipfile.ZipFile(Path(tmp) / f"{name}.zip") as z:
                    root = f"{name}/"
                    self.assertIn(root + "scripts/engine.py", z.namelist())
                    for template in (build_dist.SRC / "opendesigner" / "assets" / "templates").glob("*.html"):
                        self.assertIn(root + "assets/templates/" + template.name, z.namelist())


if __name__ == "__main__":
    unittest.main()
