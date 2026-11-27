#!/usr/bin/env python3
"""Tests that a `set` records only what was asked (issue #115).

    python3 tools/test_profile_handover.py

On a dense work tool, setting a dial that a work-tool default covers (roundness covers "corners") hands that default
over to the person. The handover is noted on the person's own decision; it is not a second decision. Starting or
stopping the profile (the audience changes) is still its own entry. Each test copies the extend-rounder eval fixture
into a temporary project with a temporary home folder.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENGINE = ROOT / "skills" / "opendesigner" / "scripts" / "engine.py"
FIXTURE = ROOT / "evals" / "extend-rounder" / "system"
HOME = tempfile.mkdtemp(prefix="opendesigner-handover-home-")
ENV = dict(os.environ, HOME=HOME, OD_HOME=os.path.join(HOME, ".opendesigner"), XDG_CONFIG_HOME=os.path.join(HOME, ".config"),
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))


def run(*args, cwd):
    r = subprocess.run([sys.executable, "-B", str(ENGINE), *args], cwd=cwd, capture_output=True, text=True, env=ENV, timeout=180)
    if r.returncode != 0:
        raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


def entries(project):
    return re.findall(r"^## (D-\d{4}) · (\S+)", (pathlib.Path(project) / "opendesigner" / "decisions.md").read_text(), re.M)


class ProfileHandover(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="opendesigner-handover-")
        shutil.copytree(FIXTURE, os.path.join(self.dir, "opendesigner"))

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_set_on_work_tool_adds_exactly_one_decision(self):
        before = entries(self.dir)
        r = run("set", "dials.roundness", "55", "--set-by", "chosen", "--quote", "make it rounder", cwd=self.dir)
        after = entries(self.dir)
        self.assertEqual(len(after), len(before) + 1, after[len(before):])
        self.assertEqual(after[-1][1], "dials.roundness")
        log = (pathlib.Path(self.dir) / "opendesigner" / "decisions.md").read_text()
        last = log[log.rindex("## " + after[-1][0]):]
        self.assertIn("no longer a dense work tool default: corners", last)
        self.assertNotIn("auto_default; see decisions.md", r.stdout)

    def test_dry_run_shows_no_profile_decision(self):
        r = run("set", "dials.roundness", "55", "--set-by", "chosen", "--quote", "rounder", "--dry-run", cwd=self.dir)
        self.assertIn("corners", r.stdout)
        self.assertNotIn("auto_default; see decisions.md", r.stdout)

    def test_audience_change_still_records_the_profile(self):
        before = entries(self.dir)
        run("set", "answers.Q-aud-01", "regular", "--set-by", "chosen", "--quote", "regular people use it", cwd=self.dir)
        new = [p for _, p in entries(self.dir)[len(before):]]
        self.assertEqual(new[0], "answers.Q-aud-01")
        self.assertIn("defaults.work-tool", new)


if __name__ == "__main__":
    unittest.main(verbosity=2)
