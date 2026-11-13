#!/usr/bin/env python3
"""Tests for the engine fixes from S4's drift report (2026-11-13): what a second model got past review, and the text that
let it.

    python3 tools/test_review_drift.py

Each test copies the devtool-dense example into a temporary project and runs the engine as people do. Nothing reads or
writes the real home folder.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENGINE = ROOT / "skills" / "opendesigner" / "scripts" / "engine.py"
EXAMPLE = ROOT / "examples" / "devtool-dense"
HOME = tempfile.mkdtemp(prefix="opendesigner-drift-home-")
ENV = dict(os.environ, HOME=HOME, OD_HOME=os.path.join(HOME, ".opendesigner"), XDG_CONFIG_HOME=os.path.join(HOME, ".config"),
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))

PAGE = """\
<style>
.card { color: var(--ds-color-text-primary); background: var(--ds-color-surface-raised); }
.title { color: var(--ds-color-text-fg-primary); }
.mine { --ds-local-gap: 8px; gap: var(--ds-local-gap); }
.body { font-family: "Inter", system-ui, sans-serif; }
.ok { font-family: var(--ds-font-family-text); }
.inh { font-family: inherit; }
.heavy { font-weight: 800; }
.fine { font-weight: 400; }
.kept { padding: 13px; } /* od-ignore: the print grid needs it */
@font-face {
  font-family: "Inter Var";
  font-weight: 100 900;
}
code { font-family: monospace; }
.short { font: 300 16px Georgia, serif; }
</style>
<div className="font-[Georgia] font-black">x</div>
<script>const s = { fontFamily: "Comic Sans MS", fontWeight: 300 };</script>
"""


def run(*args, cwd, ok=True):
    r = subprocess.run([sys.executable, "-B", str(ENGINE), *args], cwd=cwd, capture_output=True, text=True, env=ENV, timeout=180)
    if ok and r.returncode != 0:
        raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


class DriftFixes(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-drift-"))
        shutil.copytree(EXAMPLE, self.root / "opendesigner")
        for name in ("DESIGN.md", "PRODUCT.md"):
            shutil.move(str(self.root / "opendesigner" / name), str(self.root / name))
        (self.root / "page.html").write_text(PAGE)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def review(self):
        return json.loads(run("review", "--json", "--project", ".", cwd=self.root).stdout)

    def test_unknown_token_names_fonts_and_weights(self):
        rv = self.review()
        by = {(f["kind"], f["line"]): f for f in rv["findings"]}
        unk = by[("unknown-token", 3)]
        self.assertEqual(unk["value"], "var(--ds-color-text-fg-primary)")
        self.assertIn("var(--ds-color-text-primary)", unk["fix"], "the nearest real name")
        self.assertFalse([f for f in rv["findings"] if f["kind"] == "unknown-token" and f["line"] in (2, 4)],
                         "real names and names the page defines itself are fine")
        self.assertIn(("font", 5), by)
        self.assertEqual(by[("font", 5)]["value"], 'font-family: "Inter", system-ui, sans-serif', "a stack that starts with a quote")
        self.assertIn("var(--ds-font-family-text)", by[("font", 5)]["fix"])
        self.assertFalse([k for k in by if k[0] == "font" and k[1] in (6, 7)])
        self.assertIn(("weight", 8), by)
        self.assertFalse([k for k in by if k[1] in (11, 12, 13, 15)], "@font-face declares a face; a lone generic family is fine")
        self.assertIn(("font", 16), by, "the font shorthand")
        self.assertTrue({("font", 18), ("weight", 18)} <= set(by), "Tailwind font-[...] and a weight class")
        self.assertTrue({("font", 19), ("weight", 19)} <= set(by), "JSX fontFamily and fontWeight")
        self.assertNotIn(("weight", 9), by)
        self.assertFalse(rv["ok"])
        text = run("review", "--project", ".", cwd=self.root, ok=False).stdout
        self.assertIn("token name that does not exist", text)
        self.assertNotIn("add a comment with the reason on that line", text, "review no longer offers od-ignore as the fix")

    def test_an_agents_od_ignore_stays_open_until_the_owner_approves(self):
        rv = self.review()
        self.assertEqual([k["reason"] for k in rv["ignoredByAgent"]], ["the print grid needs it"])
        self.assertEqual(rv["keptOnPurpose"], [], "not kept on purpose until the owner says so")
        self.assertIn("1 od-ignore line the owner has not approved", rv["reasons"])
        self.assertNotEqual(run("keep", "the print grid needs it", cwd=self.root, ok=False).returncode, 0, "the owner's words are required")
        run("keep", "the print grid needs it", "--quote", "yes keep that one", cwd=self.root)
        rv = self.review()
        self.assertEqual(rv["ignoredByAgent"], [])
        self.assertFalse([x for x in rv["reasons"] if "od-ignore" in x])
        self.assertIn("od-ignore: the print grid needs it", json.loads((self.root / "opendesigner" / "state.json").read_text())["waivers"])

    def test_handoff_and_guard_need_the_owners_words(self):
        r = run("handoff", "yes", cwd=self.root, ok=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--quote", r.stdout + r.stderr)
        self.assertFalse((self.root / "AGENTS.md").exists(), "nothing written")
        self.assertNotEqual(run("handoff", "yes", "--quote", "ok", cwd=self.root, ok=False).returncode, 0, "two words at least")
        run("handoff", "yes", "--quote", "yes, write the note", cwd=self.root)
        self.assertTrue((self.root / "AGENTS.md").exists())
        r = run("guard", "install", cwd=self.root, ok=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--quote", r.stdout + r.stderr)

    def test_hook_text(self):
        out = run("status", "--hook", "--dir", "opendesigner", cwd=self.root).stdout
        self.assertNotIn("log question", out, "after the sketch the log question is not asked (S4 #4)")
        self.assertIn(str(ROOT / "skills" / "opendesigner" / "references" / "rules.md"), out)
        for bit in ("engine.py ledger start", "engine.py review", "opendesigner-review", "screenshots"):
            self.assertIn(bit, out)
        fresh = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-drift-new-"))
        try:
            run("init", "--name", "New", cwd=fresh)
            self.assertIn("log question", run("status", "--hook", "--dir", "opendesigner", cwd=fresh).stdout, "before the sketch it is")
        finally:
            shutil.rmtree(fresh, ignore_errors=True)

    def test_for_agents_names_each_token_twice_and_the_build_loop(self):
        run("design-md", cwd=self.root)
        md = (self.root / "DESIGN.md").read_text()
        agents = md[md.index("## For Agents"):]
        self.assertIn("engine.py ledger start", agents)
        self.assertIn("opendesigner-review", agents)
        if "Tailwind" in agents:
            self.assertIn("| Area | Tailwind class | Plain CSS (no build step) |", agents)
            self.assertIn("`text-fg-primary` | `var(--ds-color-text-primary)`", agents)
            self.assertIn("never load Tailwind from a CDN script", agents)
            css = (self.root / "opendesigner" / "build" / "css" / "tokens.css").read_text()
            import re as _re
            for name in _re.findall(r"`var\((--ds-[a-z0-9-]+)\)`", agents):  # every name it gives exists (the audit's catch)
                self.assertIn(name + ":", css, name)


if __name__ == "__main__":
    try:
        unittest.main(verbosity=1)
    finally:
        shutil.rmtree(HOME, ignore_errors=True)
