#!/usr/bin/env python3
"""The library's scaled previews in Safari's engine (WebKit) and Chrome: every shop card and every part page shows the whole
part at a readable shape, never a sliver or a one-letter column, never past its frame.

  python3 site/check_browsers.py [--base http://localhost:4173] [--engines webkit,chromium] [--widths 1440,390]

Why (owner, 2026-10-24, screenshots from Safari): cards drew parts as thin columns with text wrapping letter by letter. Every
other check ran in Chrome only, where the shop looked right. Two causes: Safari keeps text at a minimum size inside CSS zoom,
so a zoomed part grew thousands of pixels tall; and a card measured while content-visibility skipped its contents laid the
part out at about 0 px wide. Both are fixed in site/static/library.js (scaleEl, fitItem); this check keeps them fixed.

The shop is scrolled fast to the end, as a person would, then every card is measured: the part's drawn box must be at least
60 px wide and inside its tile. Each part page is opened and its device frame measured the same way. Exits 1 on any problem.
Needs Playwright with its WebKit browser (python3 -m playwright install webkit) and Chrome.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = """() => [...document.querySelectorAll('.shelf .item:not([hidden])')].map(it => {
  const m = it.querySelector('.item-media').getBoundingClientRect(), l = it.querySelector('.item-media .lib-live').getBoundingClientRect();
  return [it.id.slice(5), m.width, m.height, l.width, l.height];
})"""
PAGE = """() => { const s = document.querySelector('.part-stage'), l = s && s.querySelector('.lib-live');
  if (!l) return null; const a = s.getBoundingClientRect(), b = l.getBoundingClientRect(); return [a.width, a.height, b.width, b.height]; }"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="http://localhost:4173")
    ap.add_argument("--engines", default="webkit,chromium")
    ap.add_argument("--widths", default="1440,390")
    ap.add_argument("--no-pages", action="store_true", help="check the shop only, not each part page")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    slugs = sorted(p.name for p in (ROOT / "skills/opendesigner/assets/library/components").iterdir() if (p / "meta.json").exists())
    problems = []
    with sync_playwright() as p:
        for eng in a.engines.split(","):
            b = p.webkit.launch() if eng == "webkit" else p.chromium.launch(channel="chrome")
            for w in [int(x) for x in a.widths.split(",")]:
                pg = b.new_page(viewport={"width": w, "height": 900})
                pg.add_init_script("try { localStorage.setItem('od-analytics', 'denied') } catch (e) {}")  # no consent card over cards
                pg.goto(a.base + "/library/", wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(2000)
                for _ in range(120):
                    pg.mouse.wheel(0, 900); pg.wait_for_timeout(80)
                pg.wait_for_timeout(1500)
                for slug, mw, mh, lw, lh in pg.evaluate(CARDS):
                    if lw < 60:
                        problems.append(f"{eng} {w}px card {slug}: the part is drawn {lw:.0f} px wide in a {mw:.0f} px tile (a sliver)")
                    elif lw > mw + 1 or lh > mh + 1:
                        problems.append(f"{eng} {w}px card {slug}: the part ({lw:.0f}x{lh:.0f}) is larger than its tile ({mw:.0f}x{mh:.0f})")
                if not a.no_pages:
                    for slug in slugs:
                        pg.goto(f"{a.base}/library/{slug}/", wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(700)
                        r = pg.evaluate(PAGE)
                        if not r:
                            problems.append(f"{eng} {w}px page {slug}: no part frame found"); continue
                        sw, sh, lw, lh = r
                        if lw < min(150, sw * 0.3):
                            problems.append(f"{eng} {w}px page {slug}: the part is drawn {lw:.0f} px wide on a {sw:.0f} px stage (a sliver)")
                        elif lw > sw + 1:
                            problems.append(f"{eng} {w}px page {slug}: the part ({lw:.0f} px) is wider than its stage ({sw:.0f} px)")
                pg.close()
            b.close()
    for line in problems:
        print("error  " + line)
    n = len(problems)
    print(f"{a.engines} at {a.widths} px: {n} problem{'s' if n != 1 else ''} in library previews")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
