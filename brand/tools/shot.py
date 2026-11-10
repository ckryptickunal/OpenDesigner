#!/usr/bin/env python3
"""Render a local HTML file to PNG at an exact size.

  python3 brand/tools/shot.py page.html out.png --w 1440 --h 900 [--scale 2] [--full] [--wait 600] [--query "id=x"]
  python3 brand/tools/shot.py page.html out.png --w 1440 --h 900 --dark      (prefers-color-scheme: dark)

Uses Playwright with the installed Google Chrome, waits for fonts and images, then captures.
Each call gets its own browser, so several sessions can render at once.
"""
import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out")
    ap.add_argument("--w", type=int, required=True)
    ap.add_argument("--h", type=int, required=True)
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--full", action="store_true", help="capture the full scroll height")
    ap.add_argument("--wait", type=int, default=500, help="extra ms after fonts load (animations settle)")
    ap.add_argument("--query", default="", help="query string, e.g. id=x-01")
    ap.add_argument("--dark", action="store_true")
    ap.add_argument("--selector", help="capture only this element")
    a = ap.parse_args()

    src = pathlib.Path(a.html).resolve()
    if not src.exists():
        sys.exit(f"no such file: {src}")
    url = src.as_uri() + (("?" + a.query) if a.query else "")
    out = pathlib.Path(a.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome")
        except Exception:
            browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": a.w, "height": a.h}, device_scale_factor=a.scale,
                                color_scheme="dark" if a.dark else "light")
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(a.wait)
        if a.selector:
            page.locator(a.selector).first.screenshot(path=str(out))
        else:
            page.screenshot(path=str(out), full_page=a.full)
        browser.close()
    for e in errors:
        print("page error:", e, file=sys.stderr)
    print(out)


if __name__ == "__main__":
    main()
