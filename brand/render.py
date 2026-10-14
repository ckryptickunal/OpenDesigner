#!/usr/bin/env python3
"""Render every brand asset in src/assets.js to export/ at its exact size.

  python3 brand/render.py              all assets
  python3 brand/render.py x-02 avatar  only ids that start with these
"""
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE / "export"


def assets():
    text = (SRC / "assets.js").read_text()
    body = text[text.index("[", text.index("window.ASSETS")):text.rstrip().rstrip(";").rindex("]") + 1]
    return json.loads(body)


def main(prefixes):
    todo = [a for a in assets() if not prefixes or any(a["id"].startswith(p) for p in prefixes)]
    page_url = (SRC / "asset.html").as_uri()
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome")
        except Exception:
            browser = p.chromium.launch()
        for a in todo:
            page = browser.new_page(viewport={"width": a["w"], "height": a["h"]}, device_scale_factor=1)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(f"{page_url}?id={a['id']}", wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(150)
            out = OUT / a["out"]
            out.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(out))
            page.close()
            print(("ERROR " + "; ".join(errors) + " ") if errors else "", out.relative_to(HERE))
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1:])
