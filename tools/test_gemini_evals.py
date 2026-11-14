#!/usr/bin/env python3
"""Tests for tools/gemini_evals.py. Offline: no Gemini call, no judge call, no browser.

    python3 tools/test_gemini_evals.py
"""
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gemini_evals as ge  # noqa: E402


def case(tmp, graders, prompt="---\ntags: [smoke]\n---\n\nHello"):
    d = pathlib.Path(tmp) / "case"
    (d / "graders").mkdir(parents=True)
    (d / "prompt.md").write_text(prompt)
    for name, text in graders.items():
        (d / "graders" / f"{name}.md").write_text(text)
    return d


class Graders(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.ws = pathlib.Path(self.tmp) / "ws"
        (self.ws / "opendesigner" / "build" / "css").mkdir(parents=True)
        (self.ws / "opendesigner" / "build" / "css" / "tokens.css").write_text(":root{--ds-x:#15803d}")

    def test_regex_on_reply_and_file(self):
        d = case(self.tmp, {"r": "---\ntype: regex\npattern: '4\\.5'\n---\n",
                            "f": "---\ntype: regex\ntarget: { source: file, path: opendesigner/build/css/tokens.css }\npattern: '#15803D'\nflags: i\n---\n"})
        good, _ = ge.grade(d, "p", "the floor is 4.5:1", [], self.ws, set())
        bad, _ = ge.grade(d, "p", "it is fine", [], self.ws, set())
        self.assertEqual([g["pass"] for g in good], [True, True])
        self.assertEqual([g["pass"] for g in bad], [True, False])  # f stays true: the file did not change

    def test_not_contains_on_files(self):
        d = case(self.tmp, {"n": "---\ntype: regex\ntarget: files\npattern: '\\.(css|html)$'\nflags: m\nmatch: not_contains\n---\n"})
        res, _ = ge.grade(d, "p", "", [], self.ws, set())
        self.assertFalse(res[0]["pass"])  # tokens.css is a .css file
        (self.ws / "opendesigner" / "build" / "css" / "tokens.css").unlink()
        res, _ = ge.grade(d, "p", "", [], self.ws, set())
        self.assertTrue(res[0]["pass"])

    def test_file_exists_glob(self):
        d = case(self.tmp, {"e": "---\ntype: file_exists\npath: \"**/*.css\"\n---\n",
                            "m": "---\ntype: file_exists\npath: \"**/DESIGN.md\"\n---\n"})
        res, _ = ge.grade(d, "p", "", [], self.ws, set())
        self.assertEqual([g["pass"] for g in res], [True, False])

    def test_tool_used_counts_and_max(self):
        d = case(self.tmp, {"s": "---\ntype: tool_used\ntool: Skill\ninput_match: 'opendesigner'\narm: with-only\n---\n",
                            "b": "---\ntype: tool_used\ntool: AskUserQuestion\ninput_match: '\"question\"\\s*:[\\s\\S]*\"question\"\\s*:'\nmin: 0\nmax: 0\n---\n"})
        one = [{"tool": "AskUserQuestion", "input": {"questions": [{"question": "a?"}]}}]
        two = [{"tool": "AskUserQuestion", "input": {"questions": [{"question": "a?"}, {"question": "b?"}]}}]
        skill = [{"tool": "Skill", "input": {"skill": "opendesigner"}}]
        res = {g["grader"]: g["pass"] for g in ge.grade(d, "p", "", skill + one, self.ws, set())[0]}
        self.assertEqual(res, {"b": True, "s": True})
        res = {g["grader"]: g["pass"] for g in ge.grade(d, "p", "", two, self.ws, set())[0]}
        self.assertEqual(res, {"b": False, "s": False})

    def test_llm_grader_majority(self):
        d = case(self.tmp, {"j": "---\ntype: llm\n---\nPASS if it says no."})
        with mock.patch.object(ge, "judge_once", side_effect=[(True, "a", 0.001), (False, "b", 0.001), (True, "c", 0.001)]):
            res, cost = ge.grade(d, "p", "no", [], self.ws, set())
        self.assertTrue(res[0]["pass"])
        self.assertIn("PASS FAIL PASS", res[0]["why"])
        with mock.patch.object(ge, "judge_once", side_effect=[(False, "a", 0), (False, "b", 0)]):
            res, _ = ge.grade(d, "p", "no", [], self.ws, set())
        self.assertFalse(res[0]["pass"])  # two votes settle it; the third is not asked


class Parsing(unittest.TestCase):
    def test_front_matter(self):
        self.assertEqual(ge.scalar("{ source: file, path: a/b.css }"), {"source": "file", "path": "a/b.css"})
        self.assertEqual(ge.scalar("[Read, Glob, Skill]"), ["Read", "Glob", "Skill"])
        self.assertEqual(ge.scalar("'it''s'"), "it's")
        self.assertEqual(ge.scalar("40"), 40)


class Workspace(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.ws = self.tmp / "run" / "workspace"
        self.ws.mkdir(parents=True)
        self.stage = self.tmp / "stage"
        (self.stage / "skills" / "opendesigner").mkdir(parents=True)
        (self.stage / "skills" / "opendesigner" / "SKILL.md").write_text("---\nname: opendesigner\ndescription: d\n---\n\nBody")
        self.w = ge.Workspace(self.ws, [], self.stage, {"Read", "Write", "Edit", "Bash", "Skill", "Glob", "Grep"})

    def test_paths_outside_are_refused(self):
        self.assertIn("outside", self.w.call("Read", {"file_path": "/etc/hosts"}))
        self.assertIn("outside", self.w.call("Write", {"file_path": str(self.tmp / "x.txt"), "content": "x"}))
        self.assertIn("outside", self.w.call("Write", {"file_path": str(self.stage / "skills" / "y.md"), "content": "x"}))
        self.assertIn("written", self.w.call("Write", {"file_path": "a/b.txt", "content": "hello"}))
        self.assertIn("hello", self.w.call("Read", {"file_path": str(self.ws / "a/b.txt")}))
        self.assertIn("Body", self.w.call("Skill", {"skill": "opendesigner:opendesigner"}))
        self.assertIn("not available", ge.Workspace(self.ws, [], self.stage, {"Read"}).call("Bash", {"command": "ls"}))

    def test_edit_needs_a_unique_match(self):
        self.w.call("Write", {"file_path": "f.css", "content": "a a"})
        self.assertIn("2 times", self.w.call("Edit", {"file_path": "f.css", "old_string": "a", "new_string": "b"}))
        self.w.call("Edit", {"file_path": "f.css", "old_string": "a", "new_string": "b", "replace_all": True})
        self.assertEqual((self.ws / "f.css").read_text(), "b b")

    @unittest.skipUnless(sys.platform == "darwin" and os.path.exists("/usr/bin/sandbox-exec"), "macOS sandbox-exec")
    def test_bash_sandbox(self):
        self.assertIn("ok", self.w.call("Bash", {"command": "echo ok > in.txt && cat in.txt"}))
        self.assertIn("t", self.w.call("Bash", {"command": "python3 -c \"import tempfile;print(tempfile.mkstemp()[1])\""}))
        out = self.w.call("Bash", {"command": f"echo x > {self.tmp / 'outside.txt'}"})
        self.assertFalse((self.tmp / "outside.txt").exists(), out)
        env = self.tmp / ".env"
        env.write_text("SECRET=1")
        self.assertNotIn("SECRET", self.w.call("Bash", {"command": f"cat {env}"}))
        net = self.w.call("Bash", {"command": "python3 -c \"import socket;socket.create_connection(('1.1.1.1',443),3)\""})
        self.assertIn("exit code", net)


class Client(unittest.TestCase):
    def client(self, cap=1.0):
        with mock.patch.dict(os.environ, {"GEMINI_API_KEY": "test-key-not-real"}), \
                mock.patch.object(ge, "WORK", pathlib.Path(tempfile.mkdtemp())):
            g = ge.Gemini("gemini-3.1-pro-preview", cap, "test")
        self.addCleanup(g.lock.close)
        return g

    def test_price(self):
        g = self.client()
        usd = g.price({"promptTokenCount": 100_000, "cachedContentTokenCount": 50_000, "candidatesTokenCount": 10_000,
                       "thoughtsTokenCount": 10_000})
        self.assertAlmostEqual(usd, (50_000 * 2.0 + 50_000 * 0.20 + 20_000 * 12.0) / 1e6)
        big = g.price({"promptTokenCount": 300_000, "candidatesTokenCount": 0})  # over 200k tokens: the higher price
        self.assertAlmostEqual(big, 300_000 * 4.0 / 1e6)

    def test_cost_cap_stops_before_the_call(self):
        g = self.client(cap=0.0)
        with mock.patch("urllib.request.urlopen") as op:
            with self.assertRaises(ge.CostCap):
                g.generate({})
            op.assert_not_called()

    def test_backoff_on_429_then_ok_and_key_in_header_only(self):
        g = self.client()
        err = urllib.error.HTTPError("u", 429, "busy", {}, io.BytesIO(b'{"error":{"details":[{"retryDelay":"1s"}]}}'))
        ok = mock.MagicMock()
        ok.__enter__.return_value.read.return_value = json.dumps({"candidates": [], "usageMetadata": {"promptTokenCount": 10}}).encode()
        seen = []

        def fake(req, timeout):
            seen.append(req)
            if len(seen) == 1:
                raise err
            return ok
        with mock.patch("urllib.request.urlopen", side_effect=fake), mock.patch("time.sleep") as sl, \
                mock.patch.object(ge, "WORK", pathlib.Path(tempfile.mkdtemp())):
            g.lock = open(os.devnull, "w")
            g.generate({"contents": []})
        self.assertEqual(len(seen), 2)
        self.assertGreaterEqual(sl.call_args[0][0], 1)
        self.assertNotIn("test-key", seen[0].full_url)
        self.assertEqual(seen[0].get_header("X-goog-api-key"), "test-key-not-real")


class StaticScan(unittest.TestCase):
    def ws(self, page):
        ws = pathlib.Path(tempfile.mkdtemp())
        (ws / "opendesigner" / "build" / "css").mkdir(parents=True)
        (ws / "opendesigner" / "build" / "css" / "tokens.css").write_text(
            ":root{--ds-space-8: 8px; --ds-space-16: 16px; --ds-color-text: #222; --ds-font-family-text: Inter}")
        (ws / "page.html").write_text(page)
        return ge.static_scan(ws)

    def test_known_good(self):
        s = self.ws('<link href="opendesigner/build/css/tokens.css"><style>body{font-family:var(--ds-font-family-text);'
                    'color:var(--ds-color-text);padding:var(--ds-space-16);margin:8px}</style><button>Save changes</button>')
        self.assertEqual((s["literalColors"], s["offScaleSpacing"], s["fontsOutsideTokens"], s["inventedTokens"], s["copy"]),
                         ([], [], [], [], []))
        self.assertTrue(s["tokensCssLinked"])

    def test_known_bad(self):
        s = self.ws('<style>body{font-family:Arial;color:#333;padding:13px;background:var(--ds-color-made-up)}</style>'
                    '<button>Start Your Free Trial Now!</button>')
        self.assertEqual(len(s["literalColors"]), 1)
        self.assertEqual(s["offScaleSpacing"], ["page.html: padding: 13px"])
        self.assertEqual(len(s["fontsOutsideTokens"]), 1)
        self.assertEqual(s["inventedTokens"], ["page.html: --ds-color-made-up"])
        self.assertIn("exclamation mark", s["copy"][0])
        self.assertIn("over four words", s["copy"][0])


if __name__ == "__main__":
    unittest.main(verbosity=1)
