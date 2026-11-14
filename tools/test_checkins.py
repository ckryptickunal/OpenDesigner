#!/usr/bin/env python3
"""Tests for check-ins (engine.py checkin): at session start, after every N decisions and after each closed ledger round.

    python3 tools/test_checkins.py

Each test copies a worked example into a temporary project and runs the engine as people do. The home folder is a
temporary one, so nothing touches the real ~/.opendesigner.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENGINE = ROOT / "skills" / "opendesigner" / "scripts" / "engine.py"
EXAMPLE = ROOT / "examples" / "devtool-dense"
HOME = tempfile.mkdtemp(prefix="opendesigner-checkin-home-")
ENV = dict(os.environ, HOME=HOME, OD_HOME=os.path.join(HOME, ".opendesigner"), XDG_CONFIG_HOME=os.path.join(HOME, ".config"),
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))
ENV.pop("OD_CHECKINS", None)


def run(*args, cwd, ok=True, env=None):
    r = subprocess.run([sys.executable, "-B", str(ENGINE), *args], cwd=cwd, capture_output=True, text=True, env=env or ENV, timeout=180)
    if ok and r.returncode != 0:
        raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


def snapshot(folder):
    return {str(f.relative_to(folder)): (f.stat().st_size, f.stat().st_mtime_ns) for f in pathlib.Path(folder).rglob("*") if f.is_file()}


class CheckIns(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-checkin-"))
        shutil.copytree(EXAMPLE, self.root / "opendesigner")
        for name in ("DESIGN.md", "PRODUCT.md"):
            shutil.move(str(self.root / "opendesigner" / name), str(self.root / name))
        (self.root / "src").mkdir()
        (self.root / "src" / "app.css").write_text(".a { padding: 13px; color: #f3f4f6; }\n")
        run("design-md", cwd=self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def state(self):
        return json.loads((self.root / "opendesigner" / "state.json").read_text())

    def decide(self, n, start=30):
        return [run("set", "dials.roundness", str(start + i), "--set-by", "assumed", "--why", "test", cwd=self.root).stdout for i in range(n)]

    def test_after_every_n_decisions_once(self):
        run("checkin", cwd=self.root)  # the first check-in sets the baseline
        outs = self.decide(4)
        self.assertFalse(any("Check-in" in o for o in outs), "not before the fifth decision")
        out = self.decide(1, start=40)[0]
        self.assertIn("Check-in, since the last check-in", out)
        self.assertIn("5 decisions", out)
        self.assertIn("Next:", out)
        self.assertIn("ask at most one question", out)
        self.assertFalse(any("Check-in" in o for o in self.decide(2, start=50)), "the counter restarted")

    def test_the_first_check_in_is_a_silent_baseline(self):
        self.assertNotIn("checkins", self.state())
        first = self.decide(1)[0]
        self.assertNotIn("Check-in", first, "the first decision after the first result only sets the baseline")
        self.assertIn("last", self.state()["checkins"])
        self.assertFalse(any("Check-in" in o for o in self.decide(4, start=40)))
        self.assertIn("Check-in", self.decide(1, start=50)[0])

    def test_review_count_matches_the_grouped_review(self):
        out = json.loads(run("checkin", "--json", cwd=self.root).stdout)
        self.assertGreaterEqual(out["review"]["groups"], 1)
        text = run("checkin", cwd=self.root).stdout
        self.assertRegex(text, r"Review: \d+ groups? of hard-coded values \([\d,]+ values\)")
        self.assertNotRegex(text, r"Review: \d+ to fix")

    def test_the_hook_names_one_next_step(self):
        run("checkin", cwd=self.root)
        out = run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout
        self.assertEqual(out.count("Next:"), 1, out)

    def test_every_and_off(self):
        run("checkin", "--every", "2", cwd=self.root)
        run("checkin", cwd=self.root)
        self.assertIn("Check-in", self.decide(2)[1])
        run("checkin", "--off", cwd=self.root)
        self.assertFalse(any("Check-in" in o for o in self.decide(3, start=60)))
        self.assertEqual(run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout.count("Check-in"), 0)
        self.assertEqual(run("checkin", "--every", "0", cwd=self.root, ok=False).returncode != 0, True)
        env = dict(ENV, OD_CHECKINS="off")
        run("checkin", "--on", cwd=self.root)
        self.assertNotIn("Check-in", run("status", "--hook", "--dir", "opendesigner", cwd=self.root, env=env).stdout)

    def test_closed_round_and_open_ledger_item_lead(self):
        run("checkin", cwd=self.root)
        run("ledger", "start", "Settings", "--items", "a,b", cwd=self.root)
        out = run("checkin", "--json", cwd=self.root).stdout
        self.assertIn("settle ledger item R1/a", json.loads(out)["next"])
        run("ledger", "done", "a", cwd=self.root)
        run("ledger", "done", "b", cwd=self.root)
        out = run("ledger", "close", cwd=self.root).stdout
        self.assertIn("1 closed round", out)

    def test_session_start_is_read_only_and_short(self):
        run("checkin", cwd=self.root)
        self.decide(2)
        before = snapshot(self.root)
        t = time.monotonic()
        out = run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout
        took = time.monotonic() - t
        self.assertIn("Check-in, since the last check-in", out)
        self.assertIn("2 decisions", out)
        self.assertIn("Review at the last check-in", out, "no code scan at session start")
        self.assertLessEqual(len(out.strip().splitlines()), 12)
        self.assertEqual(snapshot(self.root), before)
        self.assertLess(took, 20)

    def test_nothing_before_the_first_result(self):
        fresh = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-checkin-new-"))
        try:
            run("init", "--name", "New", cwd=fresh)
            outs = [run("set", "dials.roundness", str(30 + i), "--set-by", "assumed", "--why", "t", cwd=fresh).stdout for i in range(6)]
            self.assertFalse(any("Check-in" in o for o in outs), "no housekeeping before the first result (rules.md)")
            self.assertNotIn("Check-in", run("status", "--hook", "--dir", "opendesigner", cwd=fresh).stdout)
        finally:
            shutil.rmtree(fresh, ignore_errors=True)

    def test_idle_offer_once(self):
        run("checkin", cwd=self.root)
        old = time.time() - 40 * 86400
        os.utime(self.root / "opendesigner" / "decisions.md", (old, old))
        first = run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout
        self.assertIn("Nothing in the design system changed for 40 days", first)
        again = run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout
        self.assertNotIn("Nothing in the design system changed", again)


if __name__ == "__main__":
    try:
        unittest.main(verbosity=1)
    finally:
        shutil.rmtree(HOME, ignore_errors=True)
