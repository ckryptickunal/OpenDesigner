#!/usr/bin/env python3
"""Tests for the plugin's start-of-session hook (hooks/hooks.json).

    python3 tools/test_plugin_hook.py

The hook runs on every plugin user's machine at startup, on resume, after /clear and after compaction, so it must stay
small: silent without opendesigner/state.json, read-only, no network, fast, and quiet on any error. Each test runs the
exact command from hooks.json with `sh -c`, the way Claude Code runs a command hook, after putting the plugin root in
place of ${CLAUDE_PLUGIN_ROOT} as Claude Code does.
"""
import json
import shutil
import os
import pathlib
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
HOOKS = ROOT / "hooks" / "hooks.json"
ENGINE = ROOT / "skills" / "opendesigner" / "scripts" / "engine.py"
SCRIPTS = ENGINE.parent


def the_hook():
    entries = json.loads(HOOKS.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
    return entries[0], entries[0]["hooks"][0]


OD_HOME = tempfile.mkdtemp(prefix="od-hook-home-")  # the offer's memory lives here, never in the real home folder


def run_hook(project, plugin_root=ROOT, **extra):
    _, h = the_hook()
    cmd = h["command"].replace("${CLAUDE_PLUGIN_ROOT}", str(plugin_root))
    env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(plugin_root), CLAUDE_PROJECT_DIR=str(project), **dict({"OD_HOME": OD_HOME}, **extra))
    t = time.monotonic()
    p = subprocess.run(["sh", "-c", cmd], cwd=project, env=env, capture_output=True, text=True, timeout=30)
    return p, time.monotonic() - t


def snapshot(folder):
    """Every file under folder with its size and modification time."""
    return {str(f.relative_to(folder)): (f.stat().st_size, f.stat().st_mtime_ns) for f in pathlib.Path(folder).rglob("*") if f.is_file()}


def make_system(project):
    subprocess.run([sys.executable, str(ENGINE), "--dir", str(project / "opendesigner"), "init", "--name", "Hook Test"],
                   cwd=project, capture_output=True, check=True,
                   env=dict(os.environ, OD_STANDARDS_FILE=str(project / "no-standards.json")))


class StartOfSessionHook(unittest.TestCase):

    def test_the_file_is_one_small_session_start_hook(self):
        doc = json.loads(HOOKS.read_text(encoding="utf-8"))
        self.assertEqual(list(doc["hooks"]), ["SessionStart"])  # nothing runs on tool calls or prompts
        entry, h = the_hook()
        self.assertEqual(len(doc["hooks"]["SessionStart"]), 1)
        self.assertEqual(entry["matcher"], "startup|resume|clear|compact")
        self.assertEqual(h["type"], "command")
        self.assertLessEqual(h["timeout"], 10)
        self.assertIn("status --hook", h["command"])
        self.assertIn("opendesigner/state.json", h["command"])
        self.assertTrue(h["command"].rstrip().endswith("exit 0"))
        for word in ("curl", "wget", "pip", "npm", "http", " rm ", ">"):  # no network, installs or writes
            self.assertNotIn(word, h["command"].replace("2>/dev/null", ""), word)

    def test_silent_without_a_design_system(self):
        with tempfile.TemporaryDirectory() as t:
            p, _ = run_hook(pathlib.Path(t))
            self.assertEqual((p.returncode, p.stdout, p.stderr), (0, "", ""))
            os.makedirs(os.path.join(t, "opendesigner"))  # a folder without a system is not one
            p, _ = run_hook(pathlib.Path(t))
            self.assertEqual((p.returncode, p.stdout, p.stderr), (0, "", ""))

    def test_with_a_system_it_prints_the_now_line_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as t:
            project = pathlib.Path(t)
            make_system(project)
            before, caches = snapshot(project), set(SCRIPTS.rglob("*.pyc"))
            p, took = run_hook(project)
            self.assertEqual(p.returncode, 0)
            lines = p.stdout.strip().splitlines()
            self.assertLessEqual(len(lines), 8)
            text = p.stdout
            for bit in ("opendesigner/", "Now: step 1 Discover", "Next:", "RULES.md", "engine.py review", "DESIGN.md", "engine.py here is"):
                self.assertIn(bit, text, bit)
            self.assertEqual(snapshot(project), before)  # read-only in the project
            self.assertEqual(set(SCRIPTS.rglob("*.pyc")), caches)  # and no bytecode written next to the plugin
            self.assertLess(took, 5)  # about 0.3 s on a laptop; generous for slow machines

    def test_one_offer_in_a_ui_project_without_a_system(self):
        """Installed but unused (owner, 2026-11-13): one short note, once per project, at most once a week, never in the
        project's files; offers off or OD_CHECKINS=off keep it silent."""
        home = tempfile.mkdtemp(prefix="od-offer-home-")
        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as t2:
            project = pathlib.Path(t)
            (project / "styles.css").write_text("body{margin:0}\n")
            before = snapshot(project)
            p, took = run_hook(project, OD_HOME=home)
            self.assertEqual(p.returncode, 0)
            self.assertIn("no design system yet", p.stdout)
            self.assertEqual(len(p.stdout.strip().splitlines()), 1)
            self.assertEqual(snapshot(project), before)  # nothing written in the project
            p, _ = run_hook(project, OD_HOME=home)
            self.assertEqual(p.stdout, "", "never twice for the same project")
            other = pathlib.Path(t2)
            (other / "app.tsx").write_text("export {}\n")
            p, _ = run_hook(other, OD_HOME=home)
            self.assertEqual(p.stdout, "", "at most one offer a week across projects")
            p, _ = run_hook(other, OD_HOME=tempfile.mkdtemp(), OD_CHECKINS="off")
            self.assertEqual(p.stdout, "")
            fresh = tempfile.mkdtemp()
            subprocess.run([sys.executable, str(ENGINE), "checkin", "--offers", "off"], env=dict(os.environ, OD_HOME=fresh),
                           capture_output=True, check=True)
            p, _ = run_hook(other, OD_HOME=fresh)
            self.assertEqual(p.stdout, "")
        shutil.rmtree(home, ignore_errors=True)

    def test_quiet_on_errors(self):
        with tempfile.TemporaryDirectory() as t:
            project = pathlib.Path(t)
            (project / "opendesigner").mkdir()
            (project / "opendesigner" / "state.json").write_text("{not json", encoding="utf-8")
            p, _ = run_hook(project)
            self.assertEqual((p.returncode, p.stderr), (0, ""))
            make_system_dir = pathlib.Path(t) / "other"
            make_system_dir.mkdir()
            make_system(make_system_dir)
            p, _ = run_hook(make_system_dir, plugin_root=pathlib.Path(t) / "no-such-plugin")  # a host without the plugin root
            self.assertEqual((p.returncode, p.stdout, p.stderr), (0, "", ""))


if __name__ == "__main__":
    unittest.main(verbosity=1)
