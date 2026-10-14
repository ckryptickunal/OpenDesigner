#!/usr/bin/env python3
"""Tests for preflight.py (standard library only)."""
import subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("preflight.py")

BAD = """<!doctype html><html><head><style>
:root { --t-big: 150px; --track: -0.06em; }
h1 { font: 800 var(--t-big)/1 "Missing Display", sans-serif; letter-spacing: var(--track); }
p { font-family: "Inter Tight", sans-serif; font-size: 18px; }
</style></head><body><h1>Hello<br>world</h1><p>x</p>
<script>tl.to("#a", { left: 10 });</script></body></html>"""

GOOD = """<!doctype html><html><head><style>
@font-face { font-family: "Inter Tight"; src: url("a.woff2"); }
h1 { font: 650 122px/1.1 "Inter Tight", sans-serif; letter-spacing: -0.02em; }
p { font: 400 56px/1.4 "Inter Tight", sans-serif; }
</style></head><body><h1>Hello world</h1><p>x</p></body></html>"""

# A page built the way the engine builds one: rem tokens in tokens.css, a composite `font` token with a calc()
# line height, families through var(), a Google Fonts <link> with href before rel, and utility classes it never uses.
TOKENS = """:root {
  --ds-font-size-11: 0.6875rem; --ds-font-size-14: 0.875rem; --ds-font-size-18: 1.125rem; --ds-font-size-9: 0.5625rem;
  --ds-font-family-text: Manrope, system-ui, sans-serif;
  --ds-font-family-mono: "Geist Mono", ui-monospace, monospace;
  --ds-text-body-sm: 400 var(--ds-font-size-11)/calc(1.4545 * var(--ds-script-line-height-scale, 1)) var(--ds-font-family-text);
  --ds-text-tiny: 400 var(--ds-font-size-9)/1 var(--ds-font-family-text);
}
.ds-text-body-sm { font: var(--ds-text-body-sm); }
.ds-text-tiny { font: var(--ds-text-tiny); }
"""
TOKEN_PAGE = """<!doctype html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600&amp;family=Geist+Mono&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="tokens.css">
<style>
body { font-family: var(--ds-font-family-text); font-size: var(--ds-font-size-14); }
.meta { font: var(--ds-text-body-sm); }
code { font: 400 var(--ds-font-size-14)/22px var(--ds-font-family-mono); }
</style></head><body><p>x <span class="meta">y</span> <code>z</code></p></body></html>"""


def run(html, *args, files=None, name="i.html"):
    with tempfile.TemporaryDirectory() as d:
        for rel, text in (files or {}).items():
            (Path(d) / rel).parent.mkdir(parents=True, exist_ok=True)
            (Path(d) / rel).write_text(text)
        f = Path(d) / name
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html)
        return subprocess.run([sys.executable, str(SCRIPT), "html", str(f), *args], capture_output=True, text=True)


class TestHtml(unittest.TestCase):
    def test_bad_page_is_caught(self):
        r = run(BAD, "--medium", "video")
        self.assertEqual(r.returncode, 1, r.stdout)
        for needle in ('"Missing Display"', '"Inter Tight"', "under 40px", "-0.06", "<br>", "animates left"):
            self.assertIn(needle, r.stdout)

    def test_good_page_passes(self):
        r = run(GOOD, "--medium", "video")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("WARN", r.stdout)

    def test_token_page_is_read(self):
        r = run(TOKEN_PAGE, files={"tokens.css": TOKENS})
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("ERROR", r.stdout)                            # Google Fonts faces count as loaded
        self.assertIn("loaded from Google Fonts: Geist Mono, Manrope", r.stdout)
        self.assertIn("font sizes in px: [11, 14]", r.stdout)          # rem read; 22px line height and unused 9px class not
        self.assertIn("text under 12px for web: [11]", r.stdout)       # web: 11 px warns, it does not fail

    def test_media_floors(self):
        self.assertNotIn("under", run(TOKEN_PAGE, "--medium", "app", files={"tokens.css": TOKENS}).stdout)
        r = run(TOKEN_PAGE, "--medium", "watch", files={"tokens.css": TOKENS})
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("text under 12px for watch: [11]", r.stdout)
        r = run(TOKEN_PAGE, "--medium", "video", files={"tokens.css": TOKENS})
        self.assertIn("WARN   loaded from Google Fonts", r.stdout)       # a renderer may not wait for web fonts

    def test_web_error_below_11(self):
        r = run('<html><head><style>p{font-size:10px}</style></head><body><p>x</p></body></html>')
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("text under 11px for web: [10]", r.stdout)

    def test_root_relative_sheet_inline_style_and_scale(self):
        css = ("@font-face{font-family:'Hanken Grotesk';src:url(/f.woff2)}"
               ":root{--font-size-sm:12px;--font-size-md:16px;--font-size-lg:24px}body{font:400 16px/1.5 'Hanken Grotesk',sans-serif}")
        page = '<html><head><link rel="stylesheet" href="/site.css?v=2"></head><body><p style="font-size:13px">x</p></body></html>'
        r = run(page, files={"site.css": css}, name="docs/a/index.html")
        self.assertNotIn("ERROR", r.stdout)
        self.assertIn("font sizes in px: [13, 16]", r.stdout)
        self.assertIn("sizes outside the token scale [12, 16, 24]: [13]", r.stdout)

    def test_unread_remote_sheet_warns_instead_of_failing(self):
        page = ('<html><head><link rel="stylesheet" href="https://use.typekit.net/abc.css">'
                '<style>body{font:400 16px/1.5 "Proxima Nova",sans-serif}</style></head><body>x</body></html>')
        r = run(page)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn('WARN   font "Proxima Nova"', r.stdout)


if __name__ == "__main__":
    unittest.main()
