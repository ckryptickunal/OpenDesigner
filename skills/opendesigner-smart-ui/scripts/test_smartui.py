#!/usr/bin/env python3
"""Tests for Smart UI: the shared validator fixtures (Python and JavaScript must agree exactly), the slot marks, the
catalog generator, the selector, the text fallback and the scope step. Standard library; node runs the JS half when it
is installed (skipped with a note when it is not).

  python3 skills/opendesigner-smart-ui/scripts/test_smartui.py
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
ROOT = SKILL.parent.parent
sys.path.insert(0, str(HERE))
import smartui  # noqa: E402
import slots  # noqa: E402  (smartui put the core scripts on the path)

FIX = SKILL / "assets" / "fixtures" / "validator"
CASES = json.loads((FIX / "cases.json").read_text())["cases"]
CAT = json.loads((FIX / "catalog.json").read_text())
TOKENS = ROOT / "examples" / "devtool-dense" / "build" / "css" / "tokens.css"


def keys(errors):
    return sorted(f"{e['rule']}@{e['path']}" for e in errors)


def py_opts(o):
    return {"partial": o.get("partial"), "source": o.get("source"), "limits": o.get("limits"), "allow_empty": o.get("allowEmpty")}


class Validator(unittest.TestCase):
    def test_python_fixtures(self):
        for c in CASES:
            with self.subTest(c["name"]):
                r = smartui.validate(c["answer"], CAT, py_opts(c["opts"]))
                self.assertEqual(keys(r["errors"]), sorted(c["expect"]), json.dumps(r["errors"], indent=1))

    def test_js_matches_python(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed: the JavaScript validator was not run")
        js = """
import { validate } from %s;
import fs from "node:fs";
const cat = JSON.parse(fs.readFileSync(%s, "utf8"));
const cases = JSON.parse(fs.readFileSync(%s, "utf8")).cases;
const out = {};
for (const c of cases) out[c.name] = validate(c.answer, cat, c.opts).errors.map((e) => `${e.rule}@${e.path}`).sort();
console.log(JSON.stringify(out));
""" % (json.dumps((SKILL / "assets" / "od-validate.js").as_uri()), json.dumps(str(FIX / "catalog.json")), json.dumps(str(FIX / "cases.json")))
        r = subprocess.run([node, "--input-type=module", "-e", js], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        got = json.loads(r.stdout)
        for c in CASES:
            with self.subTest(c["name"]):
                self.assertEqual(got[c["name"]], sorted(c["expect"]))

    def test_extract(self):
        self.assertIsNone(smartui.extract_answer("Paris is the capital of France."))
        self.assertEqual(smartui.extract_answer('Here:\n```a2ui\n[{"version": "1.0"}]\n```'), [{"version": "1.0"}])
        self.assertIn("__parse_error__", smartui.extract_answer("```a2ui\n[{oops\n```"))

    def test_text_fallback(self):
        ans = [c for c in CASES if c["name"] == "ok-results-named"][0]["answer"]
        r = smartui.validate(ans, CAT)
        t = smartui.to_text(r["surfaces"], CAT)
        self.assertIn("Harbour room", t)
        self.assertNotIn("book_room", t)


class Marks(unittest.TestCase):
    def test_every_marked_component_passes(self):
        lib = smartui.LIB
        for d in sorted(p for p in lib.iterdir() if (p / "component.html").exists()):
            src = (d / "component.html").read_text()
            if not slots.has_marks(src):
                continue
            with self.subTest(d.name):
                self.assertEqual(slots.check_marks(src), [])
                spec = json.loads((d / "meta.json").read_text()).get("spec", {})
                if spec.get("data"):
                    self.assertEqual(slots.check_against_spec(src, spec["data"]), [])

    def test_bad_marks_are_caught(self):
        bad = """<style>.odl-x [data-tone="a"]{}</style><div class="odl-x">
<p data-od-slot="Title">x</p><p data-od-slot="t"><b>no</b></p><span data-od-media="m"></span>
<ul data-od-list="items"><li>no item mark</li></ul><p data-od-var="tone" data-tone="a"></p><p data-od-bogus="1"></p></div>"""
        errs = " ".join(slots.check_marks(bad))
        for want in ("is not a name", "holds elements", "goes on an <img>", "no data-od-item", "at least two", "unknown mark"):
            self.assertIn(want, errs)


class Catalog(unittest.TestCase):
    def test_set_components_exist_and_are_marked(self):
        missing = []
        for c in smartui.load_set()["components"]:
            p = smartui.LIB / c["slug"] / "component.html"
            if not p.exists() or not slots.has_marks(p.read_text()):
                missing.append(c["slug"])
        self.assertEqual(missing, [], "in set.json but not in the library with marks")

    def test_components_md_is_current(self):
        self.assertEqual((smartui.SKILL / "references" / "components.md").read_text(), smartui.components_md(),
                         "run: smartui.py components --write")

    def test_catalog_shape(self):
        cat, bundle = smartui.build_catalog(TOKENS, "Test system", ["images.unsplash.com"])
        self.assertEqual(cat["protocolVersion"], "1.0")
        self.assertEqual(cat["$id"], cat["catalogId"])
        self.assertIn("anyComponent", cat["$defs"])
        self.assertIn("anyFunction", cat["$defs"])
        for name, s in cat["components"].items():
            with self.subTest(name):
                self.assertEqual(s["properties"]["component"], {"const": name})
                self.assertFalse(s.get("additionalProperties", True))
                flat = json.dumps(s)
                for word in ('"style"', '"class"', '"color"', '"theme"'):
                    self.assertNotIn(word + ":", flat.replace(" ", ""))
        self.assertTrue(set(bundle) <= set(cat["components"]))

    def test_visual_enums_are_token_names(self):
        cat, _ = smartui.build_catalog(TOKENS, "Test")
        names = smartui.token_names(TOKENS)

        def walk(s):
            if isinstance(s, dict):
                if s.get("x-od-token"):
                    for v in s["enum"]:
                        self.assertTrue(smartui.token_backed(v, names), v)
                for x in s.values():
                    walk(x)
            elif isinstance(s, list):
                for x in s:
                    walk(x)
        walk(cat["components"])


class Selector(unittest.TestCase):
    cat = None

    @classmethod
    def setUpClass(cls):
        cls.cat, _ = smartui.build_catalog(TOKENS, "Test", ["images.unsplash.com"])

    def test_no_ui_for_short_facts(self):
        for m in ("What is the capital of Peru?", "When does the shop open?", "How many seats are left?"):
            with self.subTest(m):
                self.assertFalse(smartui.select(m, self.cat)["ui"])

    def test_prompt_lists_only_candidates(self):
        text, sel = smartui.build_prompt("Compare the three fare types side by side", self.cat, k=3)
        self.assertTrue(sel["ui"])
        self.assertLessEqual(len(sel["candidates"]), 3)
        others = [n for n in self.cat["components"] if n not in sel["candidates"] and n != "Column"]
        for n in others:
            self.assertNotIn(f"- {n}:", text)


class Scope(unittest.TestCase):
    def test_scope_reads_a_repo_and_marks_gaps(self):
        with tempfile.TemporaryDirectory() as t:
            root = pathlib.Path(t)
            (root / "package.json").write_text(json.dumps({"dependencies": {"next": "15", "ai": "5"}}))
            (root / "app" / "api" / "bookings").mkdir(parents=True)
            (root / "app" / "api" / "bookings" / "route.ts").write_text("export async function POST(req) { return Response.json({}) }")
            (root / "components").mkdir()
            (root / "components" / "ChatPanel.tsx").write_text("export function ChatPanel() { return null }")
            s = smartui.scope(root)
            self.assertEqual(s["framework"], "Next.js")
            self.assertIn("Vercel AI SDK", s["ai_sdks"])
            self.assertIn("components/ChatPanel.tsx", s["chat_surface"])
            self.assertTrue(any(a.get("method") == "POST" and a["changes_data"] for a in s["actions"]))
            self.assertTrue(any("product type" in n for n in s["not_known"]))
            self.assertEqual(s["intents"][0]["intent"], "not known")


class Routes(unittest.TestCase):
    def test_read_routes_become_parts(self):
        cases = [({"path": "/api/invoices", "name": "list_invoices", "doc": "with number, status and due date"}, ["DataTable"]),
                 ({"path": "/api/invoices/<number>", "name": "get_invoice", "doc": "one invoice and its PDF file"}, ["FileCard", "KeyFacts"]),
                 ({"path": "/api/usage", "name": "get_usage", "doc": "calls per month"}, ["LineChart", "BarChart"]),
                 ({"path": "/api/plans", "name": "list_plans", "doc": ""}, ["Comparison"]),
                 ({"path": "/api/subscription", "name": "get_subscription", "doc": "plan, seats"}, ["KeyFacts"]),
                 ({"path": "/api/refunds/:id", "name": "refund_status", "doc": ""}, ["ProgressStatus"]),
                 ({"path": "/api/ping", "name": "ping", "doc": ""}, [])]
        for a, want in cases:
            with self.subTest(a["path"]):
                self.assertEqual(smartui.route_parts(a), want)

    def test_example_app_scope(self):
        s = smartui.scope(ROOT / "examples" / "smart-ui-support")
        gets = {i["from"].split()[1]: i["components"] for i in s["intents"] if i["from"].startswith("GET")}
        self.assertEqual(gets["/api/usage"], ["LineChart", "BarChart"])
        self.assertEqual(sum(1 for a in s["actions"] if a.get("changes_data")), 3)
        self.assertIn("web/assistant.js", s["chat_surface"])


class Offer(unittest.TestCase):
    def test_offer_on_a_chat_and_not_without(self):
        with tempfile.TemporaryDirectory() as t:
            root = pathlib.Path(t)
            (root / "index.html").write_text("<h1>Shop</h1>")
            self.assertIsNone(smartui.offer_reason(root))
            (root / "src").mkdir()
            (root / "src" / "SupportChat.tsx").write_text("export const SupportChat = () => null")
            self.assertIn("SupportChat.tsx", smartui.offer_reason(root))

    def test_no_second_offer_after_an_answer(self):
        with tempfile.TemporaryDirectory() as t:
            root = pathlib.Path(t)
            (root / "assistant.js").write_text("")
            (root / "opendesigner").mkdir()
            (root / "opendesigner" / "state.json").write_text(json.dumps({"profile": {"smart_ui": "declined"}}))
            self.assertIsNone(smartui.offer_reason(root))


if __name__ == "__main__":
    unittest.main()
