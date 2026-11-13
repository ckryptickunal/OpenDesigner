#!/usr/bin/env python3
"""Tests for the library MCP server, over real stdio: python3 server/mcp/test_server.py

Starts server.py as a subprocess the way a host does, sends JSON-RPC lines and checks the answers. Standard library only.
get_tokens_template runs the engine (a few seconds); everything else is instant.
"""
import json
import pathlib
import re
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CATALOG = json.loads((ROOT / "skills/opendesigner/assets/library/library.json").read_text())
MODERN = {"io.modelcontextprotocol/protocolVersion": "2026-07-28", "io.modelcontextprotocol/clientInfo": {"name": "test", "version": "1"},
          "io.modelcontextprotocol/clientCapabilities": {"extensions": {"io.modelcontextprotocol/ui": {"mimeTypes": ["text/html;profile=mcp-app"]}}}}


class Session:
    def __init__(self):
        self.p = subprocess.Popen([sys.executable, str(HERE / "server.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, text=True)
        self.n = 0

    def send(self, method, params=None, notify=False):
        msg = {"jsonrpc": "2.0", "method": method, **({"params": params} if params is not None else {})}
        if not notify:
            self.n += 1
            msg["id"] = self.n
        self.p.stdin.write(json.dumps(msg) + "\n")
        self.p.stdin.flush()
        if notify:
            return None
        line = self.p.stdout.readline()
        out = json.loads(line)
        assert out["id"] == self.n, out
        return out

    def raw(self, text):
        self.p.stdin.write(text + "\n")
        self.p.stdin.flush()
        return json.loads(self.p.stdout.readline())

    def close(self):
        self.p.stdin.close()
        code = self.p.wait(timeout=10)
        err = self.p.stderr.read()
        self.p.stdout.close()
        self.p.stderr.close()
        return code, err


class Legacy(unittest.TestCase):
    """The initialize handshake (what Claude Desktop and most hosts send today)."""

    @classmethod
    def setUpClass(cls):
        cls.s = Session()
        cls.init = cls.s.send("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test", "version": "1"}})
        cls.s.send("notifications/initialized", notify=True)

    @classmethod
    def tearDownClass(cls):
        code, err = cls.s.close()
        assert code == 0, err

    def test_initialize_echoes_version(self):
        r = self.init["result"]
        self.assertEqual(r["protocolVersion"], "2025-06-18")
        self.assertEqual(r["serverInfo"]["name"], "opendesigner-library")
        self.assertIn("tools", r["capabilities"])

    def test_unknown_version_gets_ours(self):
        s = Session()
        r = s.send("initialize", {"protocolVersion": "1999-01-01", "capabilities": {}, "clientInfo": {"name": "t"}})
        self.assertIn(r["result"]["protocolVersion"], ["2025-11-25", "2025-06-18", "2025-03-26"])
        s.close()

    def test_initialize_never_agrees_to_the_handshake_free_version(self):
        s = Session()
        r = s.send("initialize", {"protocolVersion": "2026-07-28", "capabilities": {}, "clientInfo": {"name": "t"}})
        self.assertEqual(r["result"]["protocolVersion"], "2025-11-25")
        s.close()

    def test_wrong_argument_types_are_tool_errors(self):
        for name, args in (("get_tokens_template", {"brand": 123}), ("suggest_components", {"screen": "a table", "limit": "abc"}),
                           ("suggest_components", {"screen": 5}), ("suggest_components", {"screen": "x" * 501}),
                           ("suggest_components", {"screen": "a table", "limit": 99}), ("get_component", {}),
                           ("get_component", {"id": "Bad Id"})):
            r = self.s.send("tools/call", {"name": name, "arguments": args})
            self.assertTrue(r["result"]["isError"], (name, args, r))

    def test_tools_are_read_only_and_described(self):
        tools = self.s.send("tools/list")["result"]["tools"]
        self.assertEqual({t["name"] for t in tools}, {"list_components", "get_component", "get_tokens_template", "suggest_components"})
        for t in tools:
            a = t["annotations"]
            self.assertTrue(a["readOnlyHint"], t["name"])
            self.assertFalse(a["destructiveHint"], t["name"])
            self.assertEqual(t["inputSchema"]["type"], "object")
            self.assertTrue(t["description"])
        lc = next(t for t in tools if t["name"] == "list_components")
        self.assertEqual(lc["_meta"]["ui"]["resourceUri"], "ui://opendesigner/library-gallery")

    def test_list_all_and_filtered(self):
        r = self.s.send("tools/call", {"name": "list_components", "arguments": {}})["result"]
        self.assertEqual(r["structuredContent"]["count"], CATALOG["count"])
        self.assertTrue(all(c["use"] == "OD:add library." + c["id"] for c in r["structuredContent"]["components"]))
        r = self.s.send("tools/call", {"name": "list_components", "arguments": {"type": "chart"}})["result"]
        self.assertTrue(r["structuredContent"]["count"] > 0)
        self.assertTrue(all(c["type"] == "chart" for c in r["structuredContent"]["components"]))

    def test_bad_filter_is_a_tool_error(self):
        r = self.s.send("tools/call", {"name": "list_components", "arguments": {"type": "spaceship"}})["result"]
        self.assertTrue(r["isError"])
        r = self.s.send("tools/call", {"name": "list_components", "arguments": {"colour": "red"}})["result"]
        self.assertTrue(r["isError"])

    def test_get_component(self):
        r = self.s.send("tools/call", {"name": "get_component", "arguments": {"id": "approval-panel"}})["result"]
        sc = r["structuredContent"]
        self.assertEqual(sc["entry"]["id"], "approval-panel")
        self.assertIn('class="odl-approval-panel', sc["html"])
        self.assertIn(".odl-approval-panel", sc["css"])
        self.assertNotIn("<style>", sc["markup"])
        self.assertEqual(set(sc["entry"]["states"]["edge"]), {"empty", "loading", "error", "disabled", "overflow", "long_text"})

    def test_get_unknown_component(self):
        r = self.s.send("tools/call", {"name": "get_component", "arguments": {"id": "../../etc/passwd"}})["result"]
        self.assertTrue(r["isError"])
        r = self.s.send("tools/call", {"name": "get_component", "arguments": {"id": "no-such-part"}})["result"]
        self.assertTrue(r["isError"])
        self.assertIn("No component", r["content"][0]["text"])

    def test_suggest(self):
        r = self.s.send("tools/call", {"name": "suggest_components", "arguments": {"screen": "a finance tool where a manager approves invoices"}})["result"]
        ids = [p["id"] for p in r["structuredContent"]["suggestions"]]
        self.assertIn("approval-panel", ids[:3])
        r = self.s.send("tools/call", {"name": "suggest_components", "arguments": {"screen": "a music player with a track list", "audience": "consumer"}})["result"]
        ids = [p["id"] for p in r["structuredContent"]["suggestions"]]
        self.assertTrue({"music-player", "track-list"} & set(ids[:3]), ids)
        r = self.s.send("tools/call", {"name": "suggest_components", "arguments": {"screen": ""}})["result"]
        self.assertTrue(r["isError"])

    def test_tokens_template(self):
        r = self.s.send("tools/call", {"name": "get_tokens_template", "arguments": {"brand": "#167874"}})["result"]
        sc = r["structuredContent"]
        self.assertEqual(sc["missing"], [], "the template must define every variable the library reads")
        self.assertIn("--ds-color-border-focus", sc["css"])
        bad = self.s.send("tools/call", {"name": "get_tokens_template", "arguments": {"brand": "red; rm -rf /"}})["result"]
        self.assertTrue(bad["isError"])
        bad = self.s.send("tools/call", {"name": "get_tokens_template", "arguments": {"feel": "calm --dir /tmp"}})["result"]
        self.assertTrue(bad["isError"])

    def test_resources(self):
        res = self.s.send("resources/list")["result"]["resources"]
        view = next(r for r in res if r["uri"] == "ui://opendesigner/library-gallery")
        self.assertEqual(view["mimeType"], "text/html;profile=mcp-app")
        r = self.s.send("resources/read", {"uri": "ui://opendesigner/library-gallery"})["result"]["contents"][0]
        self.assertEqual(r["mimeType"], "text/html;profile=mcp-app")
        self.assertEqual(r["_meta"]["ui"]["csp"]["resourceDomains"], ["https://images.unsplash.com"])
        self.assertIn("ui/message", r["text"])
        self.assertIn("OD:add library.", r["text"])
        err = self.s.send("resources/read", {"uri": "file:///etc/passwd"})
        self.assertEqual(err["error"]["code"], -32002)

    def test_errors(self):
        self.assertEqual(self.s.send("no/such/method")["error"]["code"], -32601)
        self.assertEqual(self.s.send("tools/call", {"name": "write_files", "arguments": {}})["error"]["code"], -32602)
        self.assertEqual(self.s.raw("{not json")["error"]["code"], -32700)
        self.assertEqual(self.s.raw("[]")["error"]["code"], -32600)
        self.assertEqual(self.s.send("ping")["result"], {})


class Modern(unittest.TestCase):
    """MCP 2026-07-28: no handshake, version and client info in every request's _meta."""

    def test_discover_and_call(self):
        s = Session()
        d = s.send("server/discover", {"_meta": MODERN})["result"]
        self.assertEqual(d["resultType"], "complete")
        self.assertIn("2026-07-28", d["supportedVersions"])
        self.assertIn("io.modelcontextprotocol/ui", d["capabilities"]["extensions"])
        t = s.send("tools/list", {"_meta": MODERN})["result"]
        self.assertIn("ttlMs", t)
        self.assertEqual(t["_meta"]["io.modelcontextprotocol/serverInfo"]["name"], "opendesigner-library")
        r = s.send("tools/call", {"name": "list_components", "arguments": {"width": "narrow"}, "_meta": MODERN})["result"]
        self.assertEqual(r["resultType"], "complete")
        bad = s.send("tools/list", {"_meta": {**MODERN, "io.modelcontextprotocol/protocolVersion": "2099-01-01"}})
        self.assertEqual(bad["error"]["code"], -32022)
        self.assertEqual(bad["error"]["data"]["supported"], ["2026-07-28"])
        self.assertEqual(s.send("resources/read", {"uri": "od://nothing", "_meta": MODERN})["error"]["code"], -32602)
        self.assertEqual(s.send("ping", {"_meta": MODERN})["error"]["code"], -32601)
        no_caps = {k: v for k, v in MODERN.items() if k != "io.modelcontextprotocol/clientCapabilities"}
        self.assertEqual(s.send("tools/list", {"_meta": no_caps})["error"]["code"], -32602)
        code, _ = s.close()
        self.assertEqual(code, 0)

    def test_no_view_for_a_host_without_apps(self):
        s = Session()
        meta = {**MODERN, "io.modelcontextprotocol/clientCapabilities": {"extensions": {}}}
        tools = s.send("tools/list", {"_meta": meta})["result"]["tools"]
        self.assertTrue(all("_meta" not in t for t in tools))
        s.close()


class Static(unittest.TestCase):
    def test_stdout_is_only_json(self):
        """Nothing but MCP messages on stdout: the start-up line goes to stderr."""
        p = subprocess.run([sys.executable, str(HERE / "server.py")], input="", capture_output=True, text=True, timeout=30)
        self.assertEqual(p.stdout, "")
        self.assertIn("read-only", p.stderr)

    def test_server_writes_and_fetches_nothing(self):
        src = (HERE / "server.py").read_text()
        self.assertIsNone(re.search(r"^\s*(import|from)\s+(urllib|http|socket|requests|ssl|ftplib|smtplib)\b", src, re.M))
        for bad in ("open(", "write_text", "write_bytes", "unlink", "rmtree", "os.remove", "shell=True"):
            self.assertFalse(bad in src, bad)

    def test_view_floors(self):
        """The gallery keeps the MCP Apps floors: 44 px targets, visible focus, reduced motion, dark mode, no external loads."""
        v = (HERE / "views/gallery.html").read_text()
        self.assertIn("min-height: 44px", v)
        self.assertIn(":focus-visible", v)
        self.assertIn("prefers-reduced-motion", v)
        self.assertIn("prefers-color-scheme: dark", v)
        self.assertIsNone(re.search(r"<(script|link)[^>]+(src|href)=\"https?:", v))
        self.assertNotRegex(v, r"\bfetch\(|XMLHttpRequest|WebSocket|localStorage")


if __name__ == "__main__":
    unittest.main(verbosity=1)
