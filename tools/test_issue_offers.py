#!/usr/bin/env python3
"""Tests for issue offers (owner, 2026-11-25): a problem the person hits twice, or a note about OpenDesigner said twice,
becomes an offer to file a GitHub issue. The offer survives sessions until it is answered, is asked once per session, and
its draft carries nothing private.

    python3 tools/test_issue_offers.py
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
HOME = tempfile.mkdtemp(prefix="opendesigner-offers-home-")
BASE_ENV = {k: v for k, v in os.environ.items() if k not in ("OD_SESSION_ID", "CLAUDE_CODE_SESSION_ID", "CODEX_SESSION_ID")}
BASE_ENV.update(HOME=HOME, XDG_CONFIG_HOME=os.path.join(HOME, ".config"), GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
                OD_STANDARDS_FILE=os.path.join(HOME, "no-standards", "standards.json"))

BUG_1 = "Q-shape-01: the radius preview shows the old corners after a pick"
BUG_2 = "Q-shape-01 radius preview still shows old corners after picking"


class IssueOffers(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="opendesigner-offers-"))
        shutil.copytree(EXAMPLE, self.root / "opendesigner")
        for name in ("feedback.md", "RULES.md", "issue-offers.json"):
            p = self.root / "opendesigner" / name
            if p.exists():
                p.unlink()
        self.home = os.path.join(str(self.root), "od-home")
        self.state = json.loads((self.root / "opendesigner" / "state.json").read_text())

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def run_engine(self, *args, session="s1", ok=True):
        env = dict(BASE_ENV, OD_HOME=self.home, OD_SESSION_ID=session)
        r = subprocess.run([sys.executable, "-B", str(ENGINE), *args], cwd=self.root, capture_output=True, text=True, env=env,
                           timeout=180)
        if ok and r.returncode != 0:
            raise AssertionError(f"engine {' '.join(args)} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
        return r

    def offers(self):
        p = self.root / "opendesigner" / "issue-offers.json"
        return json.loads(p.read_text())["offers"] if p.exists() else {}

    # counting --------------------------------------------------------------------------------------------------------------
    def test_a_repeat_counts_and_opens_an_offer(self):
        first = self.run_engine("feedback", BUG_1, "--kind", "bug", "--question", "Q-shape-01")
        self.assertNotIn("Issue offer", first.stdout, "seen once is not an offer")
        self.assertEqual(self.offers()["F-001"]["status"], "none")
        second = self.run_engine("feedback", BUG_2, "--kind", "bug")
        self.assertIn("repeat of F-001", second.stdout)
        self.assertIn("Issue offer F-001", second.stdout)
        o = self.offers()["F-001"]
        self.assertEqual((o["count"], o["status"]), (2, "pending"))
        fb = (self.root / "opendesigner" / "feedback.md").read_text()
        self.assertEqual(fb.count("## F-"), 1, "a repeat adds to the entry, not a new one")
        self.assertIn("_Seen 2 times, last ", fb)
        self.run_engine("feedback", BUG_2, "--kind", "bug")
        self.assertEqual(self.offers()["F-001"]["count"], 3)
        self.assertEqual((self.root / "opendesigner" / "feedback.md").read_text().count("_Seen "), 1)

    def test_same_overrides_the_match(self):
        self.run_engine("feedback", BUG_1, "--kind", "bug")
        self.run_engine("feedback", BUG_2, "--kind", "bug", "--same", "new")
        self.assertEqual(sorted(self.offers()), ["F-001", "F-002"])
        self.run_engine("feedback", "the export step crashed on the tokens folder", "--kind", "gap", "--same", "F-001")
        self.assertEqual(self.offers()["F-001"]["status"], "pending")
        bad = self.run_engine("feedback", "x", "--kind", "bug", "--same", "F-099", ok=False)
        self.assertNotEqual(bad.returncode, 0)

    def test_different_problems_and_ideas_do_not_count(self):
        self.run_engine("feedback", BUG_1, "--kind", "bug")
        self.run_engine("feedback", "the dark mode export misses chart colours", "--kind", "gap")
        self.run_engine("feedback", "a nicer preview", "--kind", "idea")
        self.run_engine("feedback", "a nicer preview", "--kind", "idea")
        self.assertEqual({k: v["count"] for k, v in self.offers().items()}, {"F-001": 1, "F-002": 1})

    def test_notes_about_opendesigner_open_at_two_design_notes_at_three(self):
        self.run_engine("feedback", "stop asking two questions at once", "--kind", "note", "--about", "opendesigner")
        self.assertEqual(self.offers()["N-01"]["status"], "none")
        r = self.run_engine("feedback", "stop asking two questions at once", "--kind", "note")
        self.assertIn("Issue offer N-01", r.stdout)
        self.assertEqual(self.offers()["N-01"]["status"], "pending")
        for _ in range(2):
            self.run_engine("feedback", "centre every heading", "--kind", "note")
        self.assertNotIn("N-02", self.offers(), "a note about their own design said twice stays theirs")
        self.run_engine("feedback", "centre every heading", "--kind", "note")
        self.assertEqual(self.offers()["N-02"]["status"], "pending")

    # lifecycle and sessions ------------------------------------------------------------------------------------------------
    def open_offer(self):
        self.run_engine("feedback", BUG_1, "--kind", "bug")
        self.run_engine("feedback", BUG_2, "--kind", "bug")
        self.run_engine("issue-offer", "F-001", "--asked")  # the agent asked in session s1

    def test_asked_once_per_session_and_surfaced_every_session(self):
        self.run_engine("feedback", BUG_1, "--kind", "bug")
        self.run_engine("feedback", BUG_2, "--kind", "bug")
        for _ in range(2):  # not asked yet: every line keeps saying to ask
            self.assertIn("Ask once this session", self.run_engine("status").stdout)
        self.run_engine("issue-offer", "F-001", "--asked")
        for cmd in (("status",), ("review",)):
            out = self.run_engine(*cmd, ok=False).stdout
            self.assertIn("already raised this session", out, cmd)
            self.assertNotIn("Ask once this session", out, cmd)
        out = self.run_engine("status", session="s2").stdout
        self.assertEqual(out.count("Ask once this session"), 1, "a new session asks again")
        self.run_engine("issue-offer", "F-001", "--asked", session="s2")
        self.assertIn("already raised this session", self.run_engine("status", "--hook", session="s2").stdout)
        self.assertIn("Ask once this session", self.run_engine("status", "--hook", session="s3").stdout)

    def test_later_comes_back_next_session(self):
        self.open_offer()
        self.run_engine("issue-offer", "F-001", "--answer", "later", session="s1b")
        self.assertEqual(self.offers()["F-001"]["status"], "later")
        self.assertIn("already raised", self.run_engine("status", session="s1b").stdout, "an answer counts as this session's ask")
        self.assertIn("Ask once this session", self.run_engine("status", session="s2").stdout)

    def test_no_is_never_asked_again(self):
        self.open_offer()
        self.run_engine("issue-offer", "F-001", "--answer", "no")
        for s in ("s1", "s2", "s3"):
            self.assertNotIn("Issue offer", self.run_engine("status", session=s).stdout)
        self.run_engine("feedback", BUG_2, "--kind", "bug")
        self.assertEqual(self.offers()["F-001"]["status"], "no", "a later repeat does not reopen a no")

    def test_yes_drafts_then_sent_closes(self):
        self.open_offer()
        out = self.run_engine("issue-offer", "F-001", "--answer", "yes").stdout
        self.assertIn("gh issue list --repo ckryptickunal/OpenDesigner", out)
        self.assertIn("gh issue create --repo ckryptickunal/OpenDesigner", out)
        self.assertIn("--label repeated,from-engine,bug", out)
        self.assertIn("issues/new?title=", out)
        draft = self.root / "opendesigner" / "issue-drafts" / "F-001.md"
        self.assertTrue(draft.exists())
        self.assertEqual(self.offers()["F-001"]["status"], "yes")
        self.assertIn("not filed yet", self.run_engine("status", session="s2").stdout)
        draft.write_text("edited by the person\n")
        self.assertIn("edited by the person", self.run_engine("issue-offer", "F-001", "--answer", "yes").stdout)
        self.run_engine("issue-offer", "F-001", "--sent", "https://github.com/ckryptickunal/OpenDesigner/issues/999")
        o = self.offers()["F-001"]
        self.assertEqual((o["status"], o["url"]), ("sent", "https://github.com/ckryptickunal/OpenDesigner/issues/999"))
        self.assertNotIn("Issue offer", self.run_engine("status", session="s9").stdout)

    def test_answer_needs_an_open_offer(self):
        self.run_engine("feedback", BUG_1, "--kind", "bug")
        self.assertNotEqual(self.run_engine("issue-offer", "F-001", "--answer", "yes", ok=False).returncode, 0)
        self.assertNotEqual(self.run_engine("issue-offer", "F-001", ok=False).returncode, 0)

    # privacy ---------------------------------------------------------------------------------------------------------------
    def test_draft_carries_nothing_private(self):
        name = self.state["name"]
        brand = self.state["raw"].get("brandColor") or "#0f766e"
        answer = "Our internal payroll console for the finance team"
        st = json.loads((self.root / "opendesigner" / "state.json").read_text())
        st.setdefault("answers", {})["Q-scope-01"] = {"value": answer, "set_by": "chosen", "quote": "keep it calm for Dana"}
        st["context"]["product"] = "Ledgerly payroll"
        (self.root / "opendesigner" / "state.json").write_text(json.dumps(st))
        leaky = (f"Q-color-02: in {name} the brand {brand} and rgb(1, 2, 3) on src/app/Button.tsx and ~/work/{name}/x.css "
                 f"see https://ledgerly.example/app, mail dana@ledgerly.example; {answer}; Ledgerly payroll; keep it calm for Dana")
        self.run_engine("feedback", leaky, "--kind", "confusing", "--expected", f"a preview of {brand} in tokens.css")
        self.run_engine("feedback", leaky, "--kind", "confusing")
        out = self.run_engine("issue-offer", "F-001", "--answer", "yes").stdout
        draft = (self.root / "opendesigner" / "issue-drafts" / "F-001.md").read_text()
        for secret in (name, brand, "rgb(1, 2, 3)", "src/app", "Button.tsx", "tokens.css", "~/work", "ledgerly.example",
                       "dana@", answer, "Ledgerly payroll", "keep it calm", str(self.root)):
            self.assertNotIn(secret.lower(), draft.lower(), secret)
            self.assertNotIn(secret.lower(), out.lower().split("without gh")[0], secret)
        for needed in ("Q-color-02", "2 times, first ", "OpenDesigner:", "Python ", "host ", "What was expected"):
            self.assertIn(needed, draft)


if __name__ == "__main__":
    unittest.main(verbosity=1)
