#!/usr/bin/env python3
"""Tests for the audit page, the adapt page, exempt folders and the audit ledger.

    python3 tools/test_audit_page.py

Each test copies a worked example from examples/ into a temporary project, writes a little code beside it, and runs the
engine as people do (a subprocess). Nothing reads or writes the real home folder.
"""
import hashlib
import json
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
EXAMPLE = ROOT / "examples" / "devtool-dense"
HOME = tempfile.mkdtemp(prefix="opendesigner-audit-home-")
ENV = dict(os.environ, HOME=HOME, OD_HOME=os.path.join(HOME, ".opendesigner"), XDG_CONFIG_HOME=os.path.join(HOME, ".config"),
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
           OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))

APP_CSS = """\
.page { background: #f3f4f6; padding: 13px; }
.panel { background: #f4f4f5; margin: 13px; }
.aside { background: #f2f3f5; gap: 13px; }
.title { font-size: 19px; }
.btn { border-radius: 7px; padding: 6px 10px; font-size: 13px; }
.btn-big { border-radius: 9px; padding: 10px 18px; font-size: 15px; }
.cta-button { border-radius: 3px; padding: 8px 12px; font-size: 14px; }
.btn:hover { border-radius: 2px; padding: 1px; }
.keep { padding: 13px; } /* od-ignore: print styles need exact points */
.pill { border-radius: 999px; padding: 4px 12px; }
.bento-card h3 { font-size: 13px; padding: 2px; }
"""
DEMO_CSS = ".bad { color: #ff0000; padding: 11px; }\n"


def run(*args, cwd, ok=True):
    r = subprocess.run([sys.executable, str(ENGINE), *args], cwd=cwd, capture_output=True, text=True, env=ENV, timeout=120)
    if ok and r.returncode != 0:
        raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


class Project:
    """A temporary project: the devtool-dense example as its system, and a little CSS with planted inconsistencies."""

    def __init__(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-audit-"))
        shutil.copytree(EXAMPLE, self.root / "opendesigner")
        for name in ("DESIGN.md", "PRODUCT.md"):
            shutil.move(str(self.root / "opendesigner" / name), str(self.root / name))
        (self.root / "src").mkdir()
        (self.root / "src" / "app.css").write_text(APP_CSS)
        (self.root / "demo").mkdir()
        (self.root / "demo" / "mistakes.css").write_text(DEMO_CSS)

    def state(self):
        return json.loads((self.root / "opendesigner" / "state.json").read_text())

    def close(self):
        shutil.rmtree(self.root, ignore_errors=True)


class AuditPage(unittest.TestCase):
    def setUp(self):
        self.p = Project()

    def tearDown(self):
        self.p.close()

    def data(self):
        return json.loads(run("audit-page", "--json", "--project", ".", cwd=self.p.root).stdout)

    def test_finds_each_kind_with_file_and_line(self):
        d = self.data()
        ids = {i["id"]: i for i in d["issues"]}
        kinds = {i["kind"] for i in d["issues"]}
        self.assertTrue({"color", "space", "type", "radius", "component"} <= kinds, kinds)
        color = next(i for i in d["issues"] if i["kind"] == "color")
        self.assertEqual({v["value"] for v in color["preview"]["values"]}, {"#f3f4f6", "#f4f4f5", "#f2f3f5"})
        self.assertIn({"file": os.path.join("src", "app.css"), "line": 1, "value": "#f3f4f6"}, color["evidence"])
        space = ids["A-space-13px"]  # named after the value, so a ledger item keeps pointing at the same thing
        self.assertEqual(space["count"], 3, "the od-ignore line is kept on purpose, not counted")
        self.assertTrue(any(o["id"] == "keep" and o["od"] == [f"OD:waive {space['id']}"] for o in space["options"]))
        self.assertGreaterEqual(len([o for o in space["options"] if o["id"] != "keep"]), 1)
        comp = next(i for i in d["issues"] if i["kind"] == "component")
        self.assertEqual(comp["title"], "3 different buttons", "a :hover rule is a state, not a variant")
        self.assertIn("A-color-f3f4f6", ids)
        self.assertNotIn("A-radius-999px", ids, "a pill radius is not a scale step")
        self.assertEqual(d["keptCount"], 1)
        self.assertTrue(all(i["id"].startswith("A-") for i in d["issues"]))

    def test_writes_the_page_and_changes_nothing(self):
        before = {f: hashlib.sha256((self.p.root / f).read_bytes()).hexdigest() for f in ("src/app.css", "opendesigner/state.json", "DESIGN.md")}
        r = run("audit-page", "--project", ".", cwd=self.p.root)
        self.assertIn("Nothing in the code changed", r.stdout)
        html = (self.p.root / "opendesigner" / "audit.html").read_text()
        blob = re.search(r'<script type="application/json" id="od-data">(.*?)</script>', html, re.S).group(1)
        self.assertTrue(json.loads(blob.replace("<\\/", "</"))["issues"])
        self.assertIn("Copy my choice", html)
        after = {f: hashlib.sha256((self.p.root / f).read_bytes()).hexdigest() for f in before}
        self.assertEqual(before, after)

    def test_template_sample_payload_parses(self):
        html = (ROOT / "skills" / "opendesigner" / "assets" / "templates" / "audit.html").read_text()
        blob = re.search(r'<script type="application/json" id="od-data">(.*?)</script>', html, re.S).group(1)
        self.assertIn("issues", json.loads(blob))
        html = (ROOT / "skills" / "opendesigner" / "assets" / "templates" / "adapt.html").read_text()
        blob = re.search(r'<script type="application/json" id="od-data">(.*?)</script>', html, re.S).group(1)
        self.assertIn("changes", json.loads(blob))


class Exempt(unittest.TestCase):
    def setUp(self):
        self.p = Project()

    def tearDown(self):
        self.p.close()

    def test_marked_examples_leave_review_and_are_listed(self):
        before = json.loads(run("review", "--json", "--project", ".", cwd=self.p.root).stdout)
        self.assertTrue(any(f["file"].startswith("demo") for f in before["findings"]))
        r = run("exempt", "demo", cwd=self.p.root, ok=False)
        self.assertNotEqual(r.returncode, 0, "a reason is required")
        run("exempt", "demo", "--why", "a page of mistakes on purpose", cwd=self.p.root)
        after = json.loads(run("review", "--json", "--project", ".", cwd=self.p.root).stdout)
        self.assertFalse(any(f["file"].startswith("demo") for f in after["findings"]))
        self.assertEqual(after["exempt"][0]["glob"], "demo")
        self.assertEqual(after["exempt"][0]["files"], 1)
        text = run("review", "--project", ".", cwd=self.p.root, ok=False).stdout
        self.assertIn("Left out on purpose: 1 file under demo", text)
        d = json.loads(run("audit-page", "--json", "--project", ".", cwd=self.p.root).stdout)
        self.assertEqual(d["exempt"][0]["files"], 1)
        run("exempt", "demo", "--remove", cwd=self.p.root)
        self.assertEqual(self.p.state()["exempt"], [])


class Ledger(unittest.TestCase):
    def setUp(self):
        self.p = Project()

    def tearDown(self):
        self.p.close()

    def test_round_until_nothing_is_missed(self):
        root = self.p.root
        r = run("ledger", "start", "Settings page", "--items", "comp.action.button,A-space-01,empty-state", cwd=root)
        self.assertIn("3 items planned (1 of them building blocks", r.stdout)
        st = self.p.state()
        self.assertEqual(st["blocks"]["comp.action.button"]["status"], "pending")
        rev = json.loads(run("review", "--json", "--project", "src", cwd=root).stdout)
        self.assertEqual(len(rev["ledgerOpen"]), 3)
        self.assertIn("3 ledger items neither done nor waived", rev["reasons"])
        self.assertEqual(run("ledger", "close", cwd=root, ok=False).returncode, 1)
        run("ledger", "done", "comp.action.button", "--files", "src/app.css", cwd=root)
        run("ledger", "broke", "A-space-01", "--note", "the card padding jumped on mobile", cwd=root)
        self.assertNotEqual(run("ledger", "waive", "empty-state", "--why", "later", cwd=root, ok=False).returncode, 0)
        self.assertNotEqual(run("ledger", "waive", "empty-state", "--why", "no empty lists on this page", "--by", "owner",
                                cwd=root, ok=False).returncode, 0, "owner needs their words")
        run("ledger", "waive", "empty-state", "--why", "no empty lists on this page", "--by", "agent", cwd=root)
        run("ledger", "done", "A-space-01", cwd=root)
        r = run("ledger", "close", cwd=root, ok=False)
        self.assertEqual(r.returncode, 1, "an agent's waiver waits for the owner")
        self.assertIn("the owner has not agreed yet", r.stdout)
        run("ledger", "broke", "A-space-01", "--note", "the card padding jumped on mobile", cwd=root)
        run("ledger", "waive", "empty-state", "--why", "no empty lists on this page", "--by", "owner", "--quote", "skip it", cwd=root)
        st = self.p.state()
        self.assertEqual(st["blocks"]["comp.action.button"]["status"], "done")
        self.assertIn("R1/empty-state", st["waivers"])
        rev = json.loads(run("review", "--json", "--project", "src", cwd=root).stdout)
        self.assertEqual([o["item"] for o in rev["ledgerOpen"]], ["A-space-01"], "broken stays open until fixed")
        run("ledger", "done", "A-space-01", "--note", "padding back on the 12px step", cwd=root)
        rev = json.loads(run("review", "--json", "--project", "src", cwd=root).stdout)
        self.assertEqual(rev["ledgerOpen"], [])
        self.assertFalse(any("ledger" in x for x in rev["reasons"]))
        run("ledger", "close", cwd=root)
        self.assertTrue(self.p.state()["ledger"]["rounds"][0]["closed"])
        design = (root / "DESIGN.md").read_text()
        self.assertIn("## Audit Ledger", design)
        self.assertIn("| R1 Settings page | empty-state | Skipped on purpose | no empty lists on this page (owner) |", design)
        self.assertIn("R1/empty-state: no empty lists on this page", design)
        rev = json.loads(run("review", "--json", "--project", "src", cwd=root).stdout)
        self.assertNotIn("Audit Ledger", rev["staleSections"])

    def test_no_ledger_no_section(self):
        run("design-md", cwd=self.p.root)
        self.assertNotIn("Audit Ledger", (self.p.root / "DESIGN.md").read_text())


class States(unittest.TestCase):
    """Q-state-08, Q-pattern-04 and Q-form-03 change real output: state.* tokens, DESIGN.md's States section, the overview."""

    def setUp(self):
        self.p = Project()

    def tearDown(self):
        self.p.close()

    def tokens(self):
        return json.loads((self.p.root / "opendesigner" / "tokens" / "semantic.tokens.json").read_text())

    def test_no_answer_no_tokens_but_the_section_shows_defaults(self):
        run("build", cwd=self.p.root)
        self.assertNotIn("state", self.tokens())
        design = (self.p.root / "DESIGN.md").read_text()
        self.assertIn("## States", design)
        self.assertIn("Q-state-08, not decided yet", design)
        self.assertIn('id="states"', (self.p.root / "opendesigner" / "overview.html").read_text())

    def test_answers_make_tokens(self):
        r = run("pick", "Q-state-08", "skeleton-first", "--set-by", "assumed", cwd=self.p.root)
        self.assertIn("tokens:", r.stdout)
        self.assertNotIn("not tokens", r.stdout)
        run("pick", "Q-form-03", "inline", "--set-by", "assumed", cwd=self.p.root)
        run("build", cwd=self.p.root)
        st = self.tokens()["state"]
        self.assertEqual(st["wait"]["indicator-after"]["$value"], {"value": 0, "unit": "ms"})
        self.assertEqual(st["skeleton"]["base"]["$value"], "{color.bg.neutral.subtle}")
        self.assertEqual(st["error"]["text"]["$value"], "{color.text.danger}")
        self.assertNotIn("empty", st, "Q-pattern-04 is not answered")
        css = (self.p.root / "opendesigner" / "build" / "css" / "tokens.css").read_text()
        self.assertIn("--ds-state-skeleton-base: var(--ds-color-bg-neutral-subtle)", css)
        self.assertIn("Q-state-08, decided", (self.p.root / "DESIGN.md").read_text())
        v = json.loads(run("validate", "--json", cwd=self.p.root, ok=False).stdout)
        self.assertFalse([i for i in v.get("items", []) if i.get("severity") == "error"])


class Adapt(unittest.TestCase):
    def setUp(self):
        self.p = Project()
        self.ref = self.p.root / "ref.json"
        self.ref.write_text(json.dumps({
            "id": "calm-site", "kind": "url", "tag": "inspiration",
            "measurements": {"controlRadius": 12, "bodySize": 16, "controlHeight": 44,
                             "color": {"accents": [{"hex": "#5469d4"}], "chromaticShare": 0.05}, "depth": {"hint": "shadow-ladder"}}}))

    def tearDown(self):
        self.p.close()

    def test_changes_and_what_stays_without_recording(self):
        sp = self.p.root / "opendesigner" / "state.json"
        before = hashlib.sha256(sp.read_bytes()).hexdigest()
        run("lock", "dials.depth", cwd=self.p.root)
        locked = hashlib.sha256(sp.read_bytes()).hexdigest()
        d = json.loads(run("adapt", str(self.ref), "--json", cwd=self.p.root).stdout)
        paths = {c["path"] for c in d["changes"]}
        self.assertIn("dials.roundness", paths)
        self.assertTrue(all(re.fullmatch(r"OD:accept calm-site:[\w.]+=.+", c["od"]) for c in d["changes"]), "the line carries the value")
        st = json.loads(sp.read_text())
        for c in d["changes"]:
            rec = st
            for k in c["path"].split("."):
                rec = (rec or {}).get(k) if isinstance(rec, dict) else None
            self.assertEqual(c["chosen"], isinstance(rec, dict) and rec.get("set_by") == "chosen", c["path"])
        self.assertNotIn("dials.depth", paths)
        self.assertTrue(any(s["path"] == "dials.depth" and s["why"] == "you locked it" for s in d["stays"]))
        self.assertTrue(any(s["path"] == "raw.brandColor" for s in d["stays"]))
        self.assertNotIn("#5469d4", json.dumps(d["changes"]), "a reference's hue never carries over")
        corner = next(r for r in d["table"] if r["key"] == "radius.control")
        self.assertTrue(corner["changed"])
        run("adapt", str(self.ref), cwd=self.p.root)
        self.assertTrue((self.p.root / "opendesigner" / "adapt.html").exists())
        self.assertEqual(hashlib.sha256(sp.read_bytes()).hexdigest(), locked)
        self.assertNotEqual(before, locked)


if __name__ == "__main__":
    try:
        unittest.main(verbosity=1)
    finally:
        shutil.rmtree(HOME, ignore_errors=True)
