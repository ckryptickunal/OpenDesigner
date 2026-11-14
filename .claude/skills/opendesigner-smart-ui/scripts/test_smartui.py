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
    return {"partial": o.get("partial"), "source": o.get("source"), "limits": o.get("limits"), "allow_empty": o.get("allowEmpty"), "copy": o.get("copy")}


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

    def test_renderer_dates_and_approval_rows(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        js = """
globalThis.HTMLElement = class {};
const { fmt, ODSurface } = await import(%s);
const out = { dates: [fmt("2026-11-01", "en-GB"), fmt("2026-11-01", "en-US"), fmt("TH-1043", "en-GB"), fmt("2026-11-14T09:30", "en-GB")] };
const c = { component: "ApprovalPrompt", details: [{ label: "Invoice number", value: "TH-1043" }, { label: "Number", value: "TH-1043" }, { label: "Amount", value: "€184.00" }],
            approve: { label: "Pay", event: { name: "pay_invoice", context: { number: "TH-1043", amount: "€500.00" } } } };
out.rows = ODSurface.prototype.approvalDetails.call({}, c).details;
console.log(JSON.stringify(out));
""" % json.dumps((SKILL / "assets" / "od-surface.js").as_uri())
        r = subprocess.run([node, "--input-type=module", "-e", js], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        got = json.loads(r.stdout)
        self.assertEqual(got["dates"], ["1 Nov 2026", "Nov 1, 2026", "TH-1043", "14 Nov 2026, 09:30"])
        rows = got["rows"]
        self.assertEqual([d["value"] for d in rows].count("TH-1043"), 1)  # one row per value
        self.assertEqual(rows[0], {"label": "Invoice number", "value": "TH-1043"})  # the answer's own label
        self.assertIn({"label": "Amount", "value": "€500.00"}, rows)  # what the button sends wins over what the text says
        self.assertNotIn({"label": "Amount", "value": "€184.00"}, rows)

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


class CopyRules(unittest.TestCase):
    def test_duplicate_rows_are_text_facts_only(self):
        errs = []
        smartui.duplicate_rows([{"label": "Number", "value": "TH-1043"}, {"label": "Invoice number", "value": "TH-1043"}], "/f", errs, "s1")
        self.assertEqual([e["rule"] for e in errs], ["duplicate-row"])
        errs = []  # a chart's months can have the same value
        smartui.duplicate_rows([{"label": "Jan", "value": 12}, {"label": "Feb", "value": 12}], "/p", errs, "s1")
        self.assertEqual(errs, [])

    def test_two_questions_in_one_are_not_a_short_fact(self):
        cat = json.loads((ROOT / "examples" / "smart-ui-support" / "opendesigner" / "smart-ui" / "catalog.json").read_text())
        self.assertTrue(smartui.select("What plan are we on and when does it renew?", cat, 3, None, {}, {"KeyFacts": 3})["ui"])
        self.assertFalse(smartui.select("How many seats do we have right now?", cat, 3, None, {}, {"KeyFacts": 3})["ui"])


class Selector(unittest.TestCase):
    cat = None

    @classmethod
    def setUpClass(cls):
        cls.cat, _ = smartui.build_catalog(TOKENS, "Test", ["images.unsplash.com"])

    def test_no_ui_for_short_facts(self):
        for m in ("What is the capital of Peru?", "When does the shop open?", "How many seats are left?"):
            with self.subTest(m):
                self.assertFalse(smartui.select(m, self.cat)["ui"])

    def test_fetched_data_does_not_override_r1(self):
        sel = smartui.select("How many seats do we have right now?", self.cat, 3, None, None, {"KeyFacts": 5})
        self.assertFalse(sel["ui"])

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


class Live(unittest.TestCase):
    """The live loop with a scripted model: routing, the repair round, and approvals (R3)."""

    def setUp(self):
        import live
        self.live = live
        self.app = live.load_app(ROOT / "examples" / "smart-ui-support" / "server.py")
        self.ran = []
        a = self.app.ACTIONS["pay_invoice"]
        a["fn"] = (lambda f: (lambda **kw: (self.ran.append(kw), f(**kw))[1]))(a["fn"])

    def script(self, replies, routes=()):
        """A scripted model: routing calls (a schema with "calls") take from routes, answers from replies."""
        it, rt = iter(replies), iter(routes)
        self.asked = []

        def ask(provider, system, turns, schema=None, on_text=None):
            if isinstance(schema, dict) and "calls" in schema.get("properties", {}):
                return next(rt, '{"calls": []}')
            self.asked.append(schema)
            return next(it)
        self.live.ask = ask

    def test_route_answer_repair(self):
        bad = '```a2ui\n{"component": "DataTable", "title": "<b>Open</b>", "columns": [], "rows": []}\n```'
        good = 'Two are open.\n```a2ui\n{"component": "KeyFacts", "title": "Open invoices", "facts": [{"label": "TH-1047", "value": "€1,104.00"}, {"label": "TH-1043", "value": "€184.00"}]}\n```'
        self.script([bad, good])
        conv = self.live.Conversation(self.app, "scripted")
        r = conv.answer("Show my open invoices")
        self.assertEqual([c[0] for c in r["log"]["calls"]], ["list_invoices"])  # routed by its words, no model call
        self.assertFalse(r["log"]["routed_by_model"])
        self.assertEqual(self.ran, [])
        self.assertTrue(r["log"]["first_errors"])
        self.assertTrue(r["log"]["repaired"])
        self.assertEqual(r["log"]["part"], "KeyFacts")
        self.assertIsNotNone(r["answer"])

    def test_a_model_route_never_runs_a_change(self):
        self.script(["It was refunded on 1 June."],
                    ['{"calls": [{"action": "list_invoices", "args": {}}, {"action": "pay_invoice", "args": {"number": "TH-1047"}}]}'])
        r = self.live.Conversation(self.app, "scripted").answer("What happened to the refunded one?")
        self.assertTrue(r["log"]["routed_by_model"])  # refund_status needs an invoice the message doesn't name
        self.assertEqual([c[0] for c in r["log"]["calls"]], ["list_invoices"])  # the change was dropped (R3)
        self.assertEqual(self.ran, [])

    def test_an_id_in_the_message_fills_the_action(self):
        conv = self.live.Conversation(self.app, "scripted")
        calls, sure = conv.fast_route("Can I get invoice TH-1046?")
        self.assertTrue(sure)
        self.assertEqual(calls[0], ("get_invoice", {"number": "TH-1046"}))
        self.assertEqual(conv.fast_route("Compare the plans")[0][0][0], "list_plans")
        self.assertEqual(conv.fast_route("Show my open invoices")[0][0], ("list_invoices", {"status": "open"}))  # a listed choice

    def test_a_negation_never_fills_a_choice(self):
        conv = self.live.Conversation(self.app, "scripted")
        self.assertEqual(conv.fast_route("Which invoices haven't we paid yet?")[0][0], ("list_invoices", {}))  # not status=paid
        self.assertEqual(conv.fast_route("Thanks, that's all"), ([], False))  # "all" is not a request

    def test_structured_reply_and_skeleton(self):
        reply = json.dumps({"text": "Two are open.", "part": {"component": "KeyFacts", "title": "Open invoices", "facts": [
            {"label": "TH-1047", "value": "€1,104.00"}, {"label": "TH-1043", "value": "€184.00"}]}})
        self.script([reply])
        events = []
        r = self.live.Conversation(self.app, "scripted").answer("Show my open invoices", on_event=events.append)
        self.assertEqual(events[0]["type"], "skeleton")  # drawn before the model's answer
        self.assertEqual(r["log"]["part"], "KeyFacts")
        self.assertIn("KeyFacts", json.dumps(self.asked[0]))  # the reply was constrained to the chosen parts
        self.assertIn("skeleton", r["log"]["ms"])

    def test_a_part_under_its_own_name(self):
        reply = json.dumps({"text": "Two are open.", "part": {"KeyFacts": {"title": "Open invoices", "facts": [
            {"label": "TH-1047", "value": "€1,104.00"}, {"label": "TH-1043", "value": "€184.00"}]}}})
        self.script([reply])
        r = self.live.Conversation(self.app, "scripted").answer("Show my open invoices")
        self.assertEqual(r["log"]["part"], "KeyFacts")
        sch = smartui.response_schema(self.live.Conversation(self.app, "scripted").catalog, ["KeyFacts", "DataTable"])
        self.assertEqual(sorted(sch["properties"]["part"]["properties"]), ["DataTable", "KeyFacts"])  # one key per part

    def test_change_needs_the_renderers_approval(self):
        self.script(["It's paid.", "It's paid."])
        conv = self.live.Conversation(self.app, "scripted")
        r = conv.press({"name": "pay_invoice", "context": {"number": "TH-1043"}})  # no approval
        self.assertEqual(self.ran, [])
        self.assertIn("confirmation", r["text"])
        conv.press({"name": "pay_invoice", "context": {"number": "TH-1043", "approved": True}})  # approved, but never offered
        self.assertEqual(self.ran, [])
        conv._remember_offers([{"createSurface": {"components": [{"approve": {"label": "Pay", "event": {"name": "pay_invoice", "context": {"number": "TH-1043"}}}}]}}])
        conv.press({"name": "pay_invoice", "context": {"number": "TH-1047", "approved": True}})  # offered one invoice, sent another
        self.assertEqual(self.ran, [])
        conv.press({"name": "pay_invoice", "context": {"number": "TH-1043", "approved": True}})
        self.assertEqual(self.ran, [{"number": "TH-1043"}])
        conv.press({"name": "pay_invoice", "context": {"number": "TH-1043", "approved": True}})  # an offer is used once
        self.assertEqual(len(self.ran), 1)

    def test_title_case_is_fixed_without_a_model_call(self):
        title_case = 'Two are open.\n```a2ui\n{"component": "KeyFacts", "title": "Unpaid Invoices On The Team Plan", "facts": [{"label": "TH-1047", "value": "€1,104.00"}, {"label": "TH-1043", "value": "€184.00"}]}\n```'
        self.script([title_case])
        r = self.live.Conversation(self.app, "scripted").answer("Which invoices haven't we paid?")
        self.assertIn("copy-case /0/createSurface/components/0/title", r["log"]["first_errors"])
        self.assertFalse(r["log"]["repaired"])
        self.assertEqual(r["log"]["case_fixed"], 1)
        self.assertEqual(r["answer"][0]["createSurface"]["components"][0]["title"], "Unpaid invoices on the Team plan")

    def test_only_wording_left_still_shows(self):
        filler = 'The invoice was successfully paid.\n```a2ui\n{"component": "KeyFacts", "title": "Paid", "facts": [{"label": "Invoice", "value": "TH-1043"}, {"label": "Amount", "value": "€184.00"}]}\n```'
        self.script([filler, filler])
        r = self.live.Conversation(self.app, "scripted").answer("Did it go through?")
        self.assertTrue(r["log"]["repaired"])
        self.assertIsNotNone(r["answer"])  # wording alone never costs the person the part
        self.assertEqual(r["log"]["final_errors"], ["copy-word text"])

    def test_still_wrong_after_repair_is_text_only(self):
        bad = '```a2ui\n{"component": "Nope"}\n```'
        self.script(["Here.\n" + bad, "Here again.\n" + bad])
        r = self.live.Conversation(self.app, "scripted").answer("Compare the plans")
        self.assertIsNone(r["answer"])
        self.assertTrue(r["log"]["final_errors"])


class Render(unittest.TestCase):
    def test_a_part_rendered_before_it_is_attached_still_runs_its_script(self):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            self.skipTest("Playwright for Python is not installed")
        import surface_audit as A
        with tempfile.TemporaryDirectory() as t:
            cat, bundle = smartui.build_catalog(TOKENS, "Test", ["images.unsplash.com"], only={"data-table"})
            pathlib.Path(t, "cat").mkdir()
            pathlib.Path(t, "cat", "catalog.json").write_text(json.dumps(cat))
            pathlib.Path(t, "cat", "od-components.js").write_text(smartui.bundle_js(bundle))
            fx = json.loads(A.fixture_path("data-table").read_text())
            with tempfile.TemporaryDirectory() as site, A.serve(site) as url:
                A.stage(pathlib.Path(t, "cat"), TOKENS, site)
                with sync_playwright() as p:
                    b = A.launch(p)
                    pg = b.new_page()
                    pg.goto(url + "/index.html")
                    pg.wait_for_function("window.__ready === true")
                    n = pg.evaluate("""async (fx) => {
                      const s = document.createElement("od-surface");
                      s.catalog = await (await fetch("catalog.json")).json();
                      s.process([{version: "1.0", createSurface: {surfaceId: "x", components: [{...fx, id: "root", component: "DataTable"}]}}]);
                      document.body.append(s);   // attached after rendering, as a chat that builds a turn first does
                      return s.querySelectorAll("thead th").length; }""", fx)
                    b.close()
        self.assertGreater(n, 0, "the table's own script never built its header row")


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
