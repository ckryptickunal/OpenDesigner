#!/usr/bin/env python3
"""Tests for status colours and feedback as rules (owner, 2026-11-14): build/status.json, DESIGN.md's Status and Feedback
section, and review's judgment notes.

    python3 tools/test_status_feedback.py
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
HOME = tempfile.mkdtemp(prefix="opendesigner-status-home-")
ENV = dict(os.environ, HOME=HOME, OD_HOME=os.path.join(HOME, ".opendesigner"), XDG_CONFIG_HOME=os.path.join(HOME, ".config"),
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))

PAGE = """\
<style>
.btn-primary { background: var(--ds-color-bg-success-bold); }
.toast-error { color: var(--ds-color-text-danger); }
.price-ok { color: var(--ds-color-text-danger); }
</style>
<span class="badge" style="color: var(--ds-color-text-danger)">Payment</span>
<span style="color: var(--ds-color-text-danger)"><svg></svg> Failed</span>
"""


def run(*args, cwd, ok=True):
    r = subprocess.run([sys.executable, "-B", str(ENGINE), *args], cwd=cwd, capture_output=True, text=True, env=ENV, timeout=180)
    if ok and r.returncode != 0:
        raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


class StatusAndFeedback(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-status-"))
        shutil.copytree(EXAMPLE, self.root / "opendesigner")
        for name in ("DESIGN.md", "PRODUCT.md"):
            shutil.move(str(self.root / "opendesigner" / name), str(self.root / name))
        (self.root / "page.html").write_text(PAGE)
        (self.root / "form.html").write_text('<form method="post" action="/save"><button>Save</button></form>\n')
        (self.root / "ok.html").write_text('<form method="post"><button>Save</button><p role="status"></p></form>\n')
        src = self.root / "src"
        src.mkdir()
        (src / "Save.jsx").write_text('export const Save = () => {\n  const go = () => fetch("/api", {method: "POST"}).catch((error) => console.log(error));\n'
                                      '  return <header role="banner"><button onClick={go}>Save</button></header>;\n};\n')
        (src / "api.ts").write_text('export const users = () => fetch("/api/users").then((r) => r.json());\n')
        (src / "Multi.jsx").write_text('export const M = () => (\n  <div>\n    <p className="text-danger">\n      Payment failed\n    </p>\n  </div>\n);\n')
        (src / "cta.css").write_text(".cta { background: var(--ds-color-danger-dark-9); }\n")
        (self.root / "hand.html").write_text('<style>\n.badge-ok{color:#16a34a}\n.brand{color:#2338ff}\n</style>\n'
                                             '<div class="text-red-600">Payment</div>\n<div class="text-red-600">Error: failed</div>\n')

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def status(self):
        return json.loads((self.root / "opendesigner" / "build" / "status.json").read_text())

    def test_the_map_is_exported(self):
        run("build", cwd=self.root)
        sm = self.status()
        self.assertEqual(sm["v"], 1)
        self.assertTrue({"success", "warning", "danger", "info"} <= set(sm["statuses"]))
        d = sm["statuses"]["danger"]
        self.assertEqual(d["tokens"]["text"], "color.text.danger")
        self.assertEqual(d["css"]["bg"], "--ds-color-bg-danger-subtle")
        css = (self.root / "opendesigner" / "build" / "css" / "tokens.css").read_text()
        for st in sm["statuses"].values():
            for name in st["css"].values():
                self.assertIn(name + ":", css, name)  # every name the map gives exists
        self.assertRegex(d["values"]["light"]["text"], r"^#[0-9a-f]{6}$")
        self.assertTrue(sm["rules"]["neverColourAlone"])
        for st in sm["statuses"].values():  # agreed with Smart UI: lower-case words, which its tone rule matches against data
            self.assertTrue(st["words"] and all(w == w.lower() for w in st["words"]))
        self.assertEqual((sm["aliases"]["good"], sm["aliases"]["bad"], sm["aliases"]["pending"]), ("success", "danger", "warning"))
        self.assertIn("unpaid", sm["statuses"]["danger"]["words"])
        fb = sm["feedback"]
        self.assertEqual((fb["confirm"], fb["confirmSetBy"], fb["undo"], fb["errorsStay"]), ("inline-banner", "default", "both", True))
        self.assertEqual((fb["usesToasts"], fb["toastsFor"]), (True, "low-stakes confirmations with Undo"), "as Q-form-04's default says")
        self.assertEqual(fb["toastMs"]["success"], 4000)
        run("export", "--format", "status", cwd=self.root)

    def test_answers_change_the_rules(self):
        run("pick", "Q-form-04", "toasts-widely", "--set-by", "assumed", cwd=self.root)
        run("pick", "Q-form-05", "undo-first", "--set-by", "assumed", cwd=self.root)
        run("build", cwd=self.root)
        fb = self.status()["feedback"]
        self.assertEqual((fb["confirm"], fb["confirmSetBy"], fb["undo"]), ("toasts-widely", "answer", "undo-first"))
        md = (self.root / "DESIGN.md").read_text()
        sec = md[md.index("## Status and Feedback"):]
        sec = sec[:sec.index("\n## ", 5)]
        self.assertIn("Never colour alone", sec)
        self.assertIn("| Danger |", sec)
        self.assertIn("Toasts:", sec)
        self.assertIn("an error stays until the person dismisses it", sec)
        self.assertIn("(Q-form-05)", sec)
        run("pick", "Q-form-05", "undo-first", "--set-by", "assumed", cwd=self.root)
        self.assertIn("cannot be undone still asks first", (self.root / "DESIGN.md").read_text())

    def test_review_notes_are_judgment_and_not_counted(self):
        rv = json.loads(run("review", "--json", "--project", ".", cwd=self.root).stdout)
        notes = {(n["file"], n["line"], n["kind"]) for n in rv["statusNotes"]}
        self.assertIn(("page.html", 2, "status-meaning"), notes, "success colour on a primary button")
        self.assertIn(("page.html", 4, "status-meaning"), notes, "danger on something that says ok")
        self.assertIn(("page.html", 6, "status-colour-only"), notes)
        self.assertIn(("form.html", 1, "no-feedback"), notes)
        self.assertNotIn(("page.html", 3, "status-meaning"), notes, "danger on an error toast is right")
        self.assertFalse([n for n in notes if n[1] == 7], "an icon and a word beside the colour")
        self.assertFalse([n for n in notes if n[0] == "ok.html"], "a form with a status region")
        self.assertFalse([x for x in rv["reasons"] if "status" in x.lower() and "out of date" not in x], "judgment is never counted")
        self.assertIn((os.path.join("src", "Save.jsx"), 2, "no-feedback"), notes, "a POST with only a console.log is no feedback")
        self.assertFalse([n for n in notes if n[0].endswith("api.ts")], "a GET helper in .ts is not an action")
        self.assertFalse([n for n in notes if n[0].endswith("Multi.jsx")], "text on the next lines: one line cannot judge it")
        self.assertIn((os.path.join("src", "cta.css"), 1, "status-meaning"), notes, "a danger primitive on a call to action")
        self.assertIn(("hand.html", 2, "status-by-hand"), notes, "a hex in the success hue")
        self.assertNotIn(("hand.html", 3, "status-by-hand"), notes, "a brand blue is not a status")
        self.assertIn(("hand.html", 5, "status-by-hand"), notes, "a Tailwind red")
        self.assertIn(("hand.html", 5, "status-colour-only"), notes)
        self.assertNotIn(("hand.html", 6, "status-colour-only"), notes, "with a word beside it")
        text = run("review", "--project", ".", cwd=self.root, ok=False).stdout
        self.assertIn("For a person to judge (status and feedback; not counted", text)


if __name__ == "__main__":
    try:
        unittest.main(verbosity=1)
    finally:
        shutil.rmtree(HOME, ignore_errors=True)
