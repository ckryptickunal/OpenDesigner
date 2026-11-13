#!/usr/bin/env python3
"""The Smart UI MCP Apps view against a simulated host: a page that speaks the MCP Apps 2026-01-26 postMessage protocol.

  python3 server/mcp/test_smartui_view.py      (needs Playwright for Python and Chromium or Chrome; skipped without)

It builds a catalog for the example travel system in a temporary project, calls show_ui like a model would, loads the
ui://opendesigner/surface HTML in a sandboxed iframe, and checks: the view sends ui/initialize and then
ui/notifications/initialized, draws the tool result, reports its size, and turns a pressed button into ui/message. A bad
answer must come back from show_ui as a tool error with A2UI errors, and never reach the view.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SMART = ROOT / "skills" / "opendesigner-smart-ui"
TOKENS = ROOT / "examples" / "smart-ui-chat" / "opendesigner" / "build" / "css" / "tokens.css"

HOST = """<!doctype html><meta charset="utf-8"><title>host</title><body>
<iframe id="v" sandbox="allow-scripts" style="width:720px;height:600px;border:0"></iframe>
<script>
window.log = [];
const f = document.getElementById("v");
window.addEventListener("message", (e) => {
  const m = e.data; if (!m || m.jsonrpc !== "2.0") return;
  window.log.push(m.method || "reply");
  if (m.method === "ui/initialize") f.contentWindow.postMessage({jsonrpc: "2.0", id: m.id, result: {protocolVersion: "2026-01-26",
    hostInfo: {name: "test-host", version: "1"}, hostCapabilities: {}, hostContext: {theme: "light", displayMode: "inline"}}}, "*");
  if (m.method === "ui/notifications/initialized") f.contentWindow.postMessage({jsonrpc: "2.0", method: "ui/notifications/tool-result",
    params: {content: [{type: "text", text: "fallback"}], structuredContent: window.RESULT}}, "*");
  if (m.method === "ui/message") { window.message = m.params; f.contentWindow.postMessage({jsonrpc: "2.0", id: m.id, result: {}}, "*"); }
  if (m.method === "ui/notifications/size-changed") window.size = m.params;
});
window.load = (html, result) => { window.RESULT = result; f.srcdoc = html; };
</script>"""


class ToolErr(Exception):
    pass


class View(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        proj = pathlib.Path(cls.tmp.name)
        (proj / "opendesigner" / "build" / "css").mkdir(parents=True)
        shutil.copy(TOKENS, proj / "opendesigner" / "build" / "css" / "tokens.css")
        subprocess.run([sys.executable, str(SMART / "scripts" / "smartui.py"), "catalog", "--all", "--system", "Orvell Travel",
                        "--allow-images", "images.unsplash.com"], cwd=proj, check=True, capture_output=True)
        os.environ["OD_PROJECT"] = str(proj)
        sys.path.insert(0, str(HERE))
        import smartui_tool
        cls.tool = smartui_tool
        cls.catalog = json.loads((proj / "opendesigner" / "smart-ui" / "catalog.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def answer(self):
        sys.path.insert(0, str(SMART / "scripts"))
        import audit
        fx = json.loads(audit.fixture_path("quick-replies").read_text())
        return [{"version": "1.0", "createSurface": {"surfaceId": "s1", "catalogId": self.catalog["catalogId"],
                                                     "components": [{**fx, "id": "root", "component": "QuickReplies"}]}}]

    def test_bad_answer_is_a_tool_error(self):
        bad = [{"version": "1.0", "createSurface": {"surfaceId": "s1", "components": [{"id": "root", "component": "Marquee", "style": "color:red"}]}}]
        with self.assertRaises(ToolErr) as e:
            self.tool.show_ui({"answer": bad}, ToolErr)
        self.assertIn("VALIDATION_FAILED", str(e.exception))

    def test_text_fallback_in_content(self):
        sc, text = self.tool.show_ui({"answer": self.answer()}, ToolErr)
        self.assertTrue(text.strip())
        self.assertEqual(sc["catalogId"], self.catalog["catalogId"])

    def test_view_in_a_host(self):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            self.skipTest("Playwright for Python is not installed")
        sc, _ = self.tool.show_ui({"answer": self.answer()}, ToolErr)
        html = self.tool.view_text()
        with sync_playwright() as p:
            try:
                b = p.chromium.launch()
            except Exception:
                b = p.chromium.launch(channel="chrome")
            page = b.new_page()
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.set_content(HOST)
            page.evaluate("([h, r]) => window.load(h, r)", [html, sc])
            page.wait_for_function("window.log.includes('ui/notifications/initialized')", timeout=5000)
            frame = page.frame_locator("#v")
            frame.locator("[data-od-component]").first.wait_for(timeout=5000)
            frame.locator("[data-od-event]").first.click()
            page.wait_for_function("!!window.message", timeout=5000)
            msg = page.evaluate("window.message")
            size = page.evaluate("window.size")
            log = page.evaluate("window.log")
            b.close()
        self.assertEqual(log[0], "ui/initialize")
        self.assertIn("OD:action ", msg["content"][0]["text"])
        self.assertTrue(size and size["height"] > 0)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
