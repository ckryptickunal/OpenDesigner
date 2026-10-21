#!/usr/bin/env python3
"""Check that the site's chrome is the same on every page: the header (brand, each nav link, Book a call, GitHub) and the footer
sit at the same place and size, with the same links, at each width. Owner, 2026-10-21: "top nav changes in each and every page
... audit the complete website for inconsistencies like this and fix them all for forever".

  python3 site/check_chrome.py --base http://localhost:4174 [--widths 390,768,1440]

Compares every page in the build's sitemap with the home page. Exits 1 on any difference larger than 1 px, or a link that is
missing or extra. Needs Playwright and Chrome, like check_layout.py.
"""
import argparse
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

SITE = pathlib.Path(__file__).resolve().parent
MEASURE = """() => {
  const box = el => { const r = el.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]; };
  const shown = el => el.checkVisibility() && el.getBoundingClientRect().width > 0;
  const out = {};
  const bar = document.querySelector("header.bar");
  if (!bar) return {missing: "header"};
  out["header"] = box(bar);
  for (const el of bar.querySelectorAll("a, button")) {
    if (!shown(el)) continue;
    const key = "header " + (el.getAttribute("href") || el.textContent.trim().slice(0, 20));
    out[key] = box(el);
    out[key + " text"] = el.textContent.replace(/\\s+/g, " ").replace(/[0-9,]+$/, "#").trim();
    out[key + " current"] = el.hasAttribute("aria-current") ? "current" : "";
  }
  const foot = document.querySelector("footer.foot");
  if (foot) { out["footer links"] = [...foot.querySelectorAll("a")].filter(shown).map(a => a.getAttribute("href")).join(" "); out["footer width"] = Math.round(foot.getBoundingClientRect().width); }
  return out;
}"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="http://localhost:4173")
    ap.add_argument("--widths", default="390,768,1440")
    ap.add_argument("--dist", default=str(SITE / "dist"))
    a = ap.parse_args()
    sitemap = (pathlib.Path(a.dist) / "sitemap.xml").read_text()
    pages = sorted({re.sub(r"^https?://[^/]+", "", u) for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)})
    problems = 0
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        for w in [int(x) for x in a.widths.split(",")]:
            pg = b.new_page(viewport={"width": w, "height": 900})
            pg.goto(a.base + "/"); pg.wait_for_timeout(300)
            base = pg.evaluate(MEASURE)
            for path in pages:
                pg.goto(a.base + path); pg.wait_for_timeout(200)
                got = pg.evaluate(MEASURE)
                diffs = []
                for k in sorted(set(base) | set(got)):
                    if k.endswith(" current") or (k.startswith("header ") and k.endswith(" text") and False):
                        continue
                    x, y = base.get(k), got.get(k)
                    if isinstance(x, list) and isinstance(y, list):
                        if any(abs(i - j) > 1 for i, j in zip(x, y)):
                            diffs.append(f"{k}: {y} (home {x})")
                    elif x != y:
                        diffs.append(f"{k}: {y!r} (home {x!r})")
                if diffs:
                    problems += 1
                    print(f"{path} at {w} px:\n  " + "\n  ".join(diffs[:8]) + (f"\n  ... {len(diffs) - 8} more" if len(diffs) > 8 else ""))
            pg.close()
        b.close()
    print(f"{len(pages)} pages at {a.widths}: {problems} with chrome that differs from the home page")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
