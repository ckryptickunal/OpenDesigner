#!/usr/bin/env python3
"""Tests for the system-states kit in the component library (type "states") and the library.py rule it needs: a
--ds-state-* variable, which only some systems write, is allowed only when every use falls back to one every system writes.

  python3 tools/test_library_states.py
"""
import json
import pathlib
import re
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/opendesigner/scripts"))
import library as L  # noqa: E402

KNOWN = {"--ds-color-bg-neutral-subtle", "--ds-motion-duration-extra", "--ds-radius-detail"}
EDGES = {"empty", "loading", "error", "disabled", "overflow", "long_text", "missing_image"}


def part(css):
    return f'<style>\n.odl-x {{ {css} }}\n</style>\n<div class="odl-x">x</div>\n'


META = {"name": "X", "summary": "s", "use": "u", "type": "states", "style": "quiet", "industries": ["any"], "tags": ["a", "b", "c"],
        "states": ["loading"], "source": None, "a11y": "a", "width": "narrow"}


class Fallback(unittest.TestCase):
    def errors(self, css):
        with tempfile.TemporaryDirectory() as t:
            d = pathlib.Path(t) / "x"
            d.mkdir()
            (d / "component.html").write_text(part(css))
            old, L.LIB = L.LIB, pathlib.Path(t)
            try:
                return [e for e in L.check_one({"slug": "x", **META}, KNOWN) if "--ds-" in e]
            finally:
                L.LIB = old

    def test_fallbacks_reads_nested_brackets(self):
        text = "a: var(--ds-state-p, calc(var(--ds-motion-duration-extra) * 2)); b: var(--ds-state-p);"
        self.assertEqual(L.fallbacks(text, "--ds-state-p"), ["calc(var(--ds-motion-duration-extra) * 2)", ""])

    def test_good_fallback_passes(self):
        self.assertEqual(self.errors("background: var(--ds-state-skeleton-base, var(--ds-color-bg-neutral-subtle)); "
                                     "border-radius: var(--ds-state-skeleton-radius, var(--ds-radius-detail));"), [])

    def test_calc_fallback_of_known_tokens_passes(self):
        self.assertEqual(self.errors("animation: odl-a var(--ds-state-skeleton-pulse, calc(var(--ds-motion-duration-extra) * 2.5)) infinite;"), [])

    def test_no_fallback_fails(self):
        self.assertEqual(len(self.errors("background: var(--ds-state-skeleton-base);")), 1)

    def test_one_bare_use_among_good_ones_fails(self):
        self.assertEqual(len(self.errors("background: var(--ds-state-skeleton-base, var(--ds-color-bg-neutral-subtle)); color: var(--ds-state-skeleton-base);")), 1)

    def test_fallback_to_unknown_token_fails(self):
        errs = self.errors("background: var(--ds-state-skeleton-base, var(--ds-color-made-up));")
        self.assertTrue(any(e.startswith("--ds-state-skeleton-base") for e in errs), errs)

    def test_literal_fallback_fails(self):
        self.assertEqual(len(self.errors("background: var(--ds-state-skeleton-base, transparent);")), 1)

    def test_other_unknown_tokens_still_fail(self):
        self.assertEqual(len(self.errors("background: var(--ds-color-made-up, var(--ds-color-bg-neutral-subtle));")), 1)


class StatesKit(unittest.TestCase):
    """Every component of type "states" carries what the kit promises: the spec block, a fixture that matches it,
    a live region when it says it has one, motion that stops when motion is reduced, and planned tokens it really uses."""

    @classmethod
    def setUpClass(cls):
        cls.kit = [c for c in L.components() if c["type"] == "states"]

    def test_kit_is_there(self):
        self.assertGreaterEqual(len(self.kit), 22)

    def test_spec_block(self):
        for c in self.kit:
            s = c.get("spec", {})
            self.assertTrue(s.get("use_when") and s.get("avoid_when") and s.get("keyboard"), c["slug"])
            self.assertEqual(set(s.get("edge", {})), EDGES, c["slug"])
            html = (L.LIB / c["slug"] / "component.html").read_text()
            for k, e in s["edge"].items():
                self.assertIn(e["status"], ("shown", "handled", "not_built", "none"), (c["slug"], k))
                self.assertTrue(e.get("how"), (c["slug"], k))
                if e["status"] in ("shown", "handled"):
                    self.assertIn(e["evidence"], html, (c["slug"], k))

    def test_fixture_matches_spec(self):
        for c in self.kit:
            fx = json.loads((L.LIB / c["slug"] / "fixture.json").read_text())
            props = c["spec"]["data"].get("properties", {})
            self.assertTrue(set(fx) <= set(props), (c["slug"], set(fx) - set(props)))
            for k in c["spec"]["data"].get("required", []):
                self.assertIn(k, fx, c["slug"])

    def test_live_region(self):
        for c in self.kit:
            html = (L.LIB / c["slug"] / "component.html").read_text()
            if c.get("live_region", "none") != "none":
                self.assertTrue(re.search(r'role="(status|alert|alertdialog)"|aria-live=', html), c["slug"])

    def test_reduced_motion(self):
        for c in self.kit:
            html = (L.LIB / c["slug"] / "component.html").read_text()
            self.assertIn("prefers-reduced-motion: reduce", html, c["slug"])

    def test_planned_tokens_are_used_with_fallbacks(self):
        for c in self.kit:
            html = (L.LIB / c["slug"] / "component.html").read_text()
            for name in c.get("tokens_planned", {}):
                self.assertIn(name, html, c["slug"])
                for fb in L.fallbacks(html, name):
                    self.assertTrue(fb, (c["slug"], name, "has no fallback"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
