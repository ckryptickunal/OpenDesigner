#!/usr/bin/env python3
"""Tests for the library catalog (library.json) and fetching a component: python3 tools/test_library_catalog.py

Known-good and known-bad cases for the spec checks, the drift check, and library.py add --from against a local server.
Standard library only; the server is a loopback http.server in a temporary folder.
"""
import contextlib
import copy
import functools
import http.server
import importlib.util
import io
import json
import pathlib
import subprocess
import sys
import tempfile
import threading
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills/opendesigner/scripts/library.py"
_spec = importlib.util.spec_from_file_location("od_library", SCRIPT)
library = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(library)
GOOD = next(c for c in library.components() if c["slug"] == "approval-panel")


def bad(**change):
    c = copy.deepcopy(GOOD)
    for path, value in change.items():
        node, keys = c["spec"], path.split("__")
        for k in keys[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        if value is None:
            del node[keys[-1]]
        else:
            node[int(keys[-1]) if isinstance(node, list) else keys[-1]] = value
    return library.spec_errors(c)


class Spec(unittest.TestCase):
    def test_every_component_passes(self):
        for c in library.components():
            self.assertEqual(library.spec_errors(c), [], c["slug"])

    def test_known_good(self):
        self.assertEqual(library.spec_errors(GOOD), [])

    def test_no_spec(self):
        c = {k: v for k, v in GOOD.items() if k != "spec"}
        self.assertIn("lacks spec", library.spec_errors(c)[0])

    def test_selector_not_in_file(self):
        errs = bad(parts__0__selector=".odl-nonexistent")
        self.assertTrue(any("odl-nonexistent" in e for e in errs), errs)

    def test_string_without_limit(self):
        errs = bad(data__properties__vendor={"type": "string", "part": "vendor"})
        self.assertTrue(any("without maxLength" in e for e in errs), errs)

    def test_list_without_limit(self):
        steps = copy.deepcopy(GOOD["spec"]["data"]["properties"]["steps"])
        del steps["maxItems"]
        errs = bad(data__properties__steps=steps)
        self.assertTrue(any("without maxItems" in e for e in errs), errs)

    def test_part_name_must_exist(self):
        errs = bad(data__properties__vendor={"type": "string", "maxLength": 9, "part": "ghost"})
        self.assertTrue(any("'ghost'" in e for e in errs), errs)

    def test_missing_edge_state(self):
        errs = bad(edge__loading=None)
        self.assertTrue(any("edge.loading" in e for e in errs), errs)

    def test_evidence_must_be_in_the_file(self):
        errs = bad(edge__overflow={"status": "handled", "how": "it scrolls", "evidence": "overflow: magic"})
        self.assertTrue(any("evidence" in e for e in errs), errs)

    def test_avoid_when_required(self):
        self.assertTrue(any("avoid_when" in e for e in bad(avoid_when=[])))

    def test_keyboard_required_with_controls(self):
        self.assertTrue(any("keyboard" in e for e in bad(keyboard=[])))


class Catalog(unittest.TestCase):
    def test_file_is_current(self):
        self.assertEqual(library.CATALOG.read_text(), library.catalog_text(), "run library.py catalog")

    def test_shape(self):
        cat = json.loads(library.CATALOG.read_text())
        self.assertEqual(cat["format"], "opendesigner.library/1")
        self.assertEqual(cat["count"], len(cat["components"]))
        e = next(x for x in cat["components"] if x["id"] == "approval-panel")
        self.assertIn("--ds-color-border-focus", e["tokens"])
        self.assertEqual(e["tags"]["audience"], "work")
        self.assertEqual(set(e["states"]["edge"]), set(library.EDGE))
        self.assertTrue(e["a11y"]["focus_visible"])

    def test_drift_is_caught(self):
        with tempfile.TemporaryDirectory() as t:
            stale = pathlib.Path(t) / "library.json"
            stale.write_text(library.CATALOG.read_text().replace('"Approval panel"', '"Approval panel (edited)"', 1))
            old, library.CATALOG = library.CATALOG, stale
            try:
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    code = library.cmd_catalog(type("A", (), {"check": True})())
            finally:
                library.CATALOG = old
            self.assertEqual(code, 1)
            self.assertIn("out of date", out.getvalue())

    def test_audience(self):
        c = lambda t, *ind: {"type": t, "industries": list(ind)}
        self.assertEqual(library.audience(c("data", "finance")), "work")
        self.assertEqual(library.audience(c("data", "food", "travel")), "consumer")
        self.assertEqual(library.audience(c("data", "finance", "food")), "work")
        self.assertEqual(library.audience(c("data", "any")), "work")
        self.assertEqual(library.audience(c("content", "finance")), "consumer")


class Website(unittest.TestCase):
    """What site/build.py serves for the library: addresses, the one audience rule and URL wrapping."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(ROOT / "site"))
        import library_page
        cls.lp = library_page

    def test_wrap_never_inside_scheme(self):
        out = self.lp.wrap_url("curl -fsSLo a-b.html https://opendesigner.dev/library/a-b.html")
        self.assertIn("https://opendesigner.dev/<wbr>library/<wbr>", out)
        self.assertNotIn(":/<wbr>", out)
        self.assertIn('<span class="nb">a-b.html</span>', out)

    def test_web_entry_addresses(self):
        b = type("B", (), {"SITE_URL": "https://opendesigner.dev"})()
        e = self.lp.web_entry(b, json.loads(library.CATALOG.read_text())["components"][0])
        self.assertEqual(e["urls"]["html"], f"https://opendesigner.dev/library/{e['id']}.html")
        self.assertEqual(e["urls"]["json"], f"https://opendesigner.dev/library/{e['id']}.json")
        self.assertIn("--from https://opendesigner.dev", e["get"]["opendesigner"])
        self.assertNotIn("<skill>", json.dumps(e))

    def test_one_audience_rule(self):
        for c in self.lp.components():
            self.assertEqual(self.lp.who(c) == "Consumer", library.audience(c) == "consumer", c["slug"])


class Fetch(unittest.TestCase):
    """library.py add --from, against a loopback copy of the website's /library/<id>.html."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        site = pathlib.Path(cls.tmp.name) / "site" / "library"
        site.mkdir(parents=True)
        (site / "kpi-strip.html").write_text((library.LIB / "kpi-strip/component.html").read_text())
        (site / "not-a-part.html").write_text("<html>hello</html>")
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(site.parent))
        handler.log_message = lambda *a: None
        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.tmp.cleanup()

    def add(self, *args):
        with tempfile.TemporaryDirectory() as proj:
            p = subprocess.run([sys.executable, str(SCRIPT), "add", *args], cwd=proj, capture_output=True, text=True)
            out = pathlib.Path(proj) / "components/odl" / f"{args[0]}.html"
            return p, (out.read_text() if out.exists() else None)

    def test_good_fetch(self):
        p, text = self.add("kpi-strip", "--from", self.base)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(text, (library.LIB / "kpi-strip/component.html").read_text())

    def test_missing_component(self):
        p, text = self.add("no-such-part", "--from", self.base)
        self.assertEqual(p.returncode, 1)
        self.assertIsNone(text)

    def test_not_a_component_file(self):
        p, text = self.add("not-a-part", "--from", self.base)
        self.assertEqual(p.returncode, 1)
        self.assertIn("not an OpenDesigner component", p.stdout)
        self.assertIsNone(text)

    def test_plain_http_refused(self):
        p, text = self.add("kpi-strip", "--from", "http://example.com")
        self.assertEqual(p.returncode, 1)
        self.assertIn("https", p.stdout)

    def test_bad_name_refused(self):
        p, _ = self.add("../../etc/passwd", "--from", self.base)
        self.assertEqual(p.returncode, 1)
        self.assertIn("not a component name", p.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=1)
