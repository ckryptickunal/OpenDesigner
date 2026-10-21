#!/usr/bin/env python3
"""Capture the before-and-after demo with the review skill's own tools, so every number on the site is measured.

    python3 site/demo/before-after/capture.py        (needs Playwright for Python and a local Chrome)

For before.html and after.html at 1280 px wide: run probe.js and save its measurements (review/probe-*.json, which
`review.py check` reads), save a full-page screenshot at 2x (shots/*.png), and box each issue with __od.marks() from the
lists in marks.in.json (review/marks-*.json). Then build the report with review.py compare. The site build turns the
screenshots and marks into the home-page figure and serves the report at /demo/before-after/. The screenshots stay local
(git-ignored, like the showcase renders), so run this once before the first site build.
"""
import json
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REVIEW = ROOT / "skills" / "opendesigner-review" / "scripts"
PROBE = (REVIEW / "probe.js").read_text()
WIDTH = 1280


def main():
    marks_in = json.loads((HERE / "marks.in.json").read_text())
    (HERE / "review").mkdir(exist_ok=True)
    (HERE / "shots").mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for name in ("before", "after"):
            page = browser.new_page(viewport={"width": WIDTH, "height": 800}, device_scale_factor=2)
            page.goto((HERE / f"{name}.html").as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            page.add_script_tag(content=PROBE)
            probe = page.evaluate("__od.probe()")
            (HERE / "review" / f"probe-{name}.json").write_text(json.dumps(probe, indent=1))
            marks = page.evaluate("(l) => __od.marks(l)", marks_in[name])
            (HERE / "review" / f"marks-{name}.json").write_text(json.dumps(marks, indent=1))
            page.screenshot(path=str(HERE / "shots" / f"{name}.png"), full_page=True)
            missing = [m["n"] for m in marks["marks"] if m.get("missing")]
            print(f"{name}: page {marks['page']['w']}x{marks['page']['h']}, {len(marks['marks'])} marks" + (f", MISSING {missing}" if missing else ""))
            page.close()
        browser.close()
    subprocess.run([sys.executable, str(REVIEW / "review.py"), "compare", "--dir", str(HERE / "review"),
                    "--before", str(HERE / "shots" / "before.png"), "--after", str(HERE / "shots" / "after.png"),
                    "--marks", str(HERE / "review" / "marks-before.json"), "--after-marks", str(HERE / "review" / "marks-after.json"),
                    "--title", "Merriweft invoices: before and after"], check=True)


if __name__ == "__main__":
    main()
