"""Run one read-only page script in the installed Chrome (headless) and save what it returns.

    python3 capture.py <url> <script.js> <out.json> [focus-colour]

Used for OpenDesigner's read_page.js and for truth.js. The page is loaded, scrolled once so lazy
sections load, then read at 1440 x 900. A focus colour (for example #0377ff) is passed to truth.js.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

url, script, out = sys.argv[1], pathlib.Path(sys.argv[2]).read_text(), pathlib.Path(sys.argv[3])
script = script.replace("__FOCUS__", sys.argv[4] if len(sys.argv) > 4 else "")
with sync_playwright() as p:
    br = p.chromium.launch(channel="chrome")
    pg = br.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(url, wait_until="load", timeout=60000)  # not "networkidle": some sites keep a connection open
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(2000)
    h = pg.evaluate("document.documentElement.scrollHeight")
    for y in range(0, h, 700):
        pg.evaluate(f"window.scrollTo(0, {y})"); pg.wait_for_timeout(120)
    pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(400)
    out.write_text(pg.evaluate(script)); br.close()
print("wrote", out)
