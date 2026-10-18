#!/usr/bin/env python3
"""Render a mockup scene with prefers-reduced-motion: reduce, so animated work inside an iframe
(the Howl Hill marquee) is captured at its still frame instead of wherever the animation happens to be.
Same output as brand/tools/shot.py, which has no reduced-motion option (see PROCESS.md).

  python3 brand/showcase/mockups/render_still.py <page.html> <out.png> --w 1600 --h 1200 [--scale 2]
"""
import argparse, pathlib
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("html"); ap.add_argument("out")
ap.add_argument("--w", type=int, required=True); ap.add_argument("--h", type=int, required=True)
ap.add_argument("--scale", type=float, default=2); ap.add_argument("--wait", type=int, default=1500)
a = ap.parse_args()
with sync_playwright() as p:
    try:
        b = p.chromium.launch(channel="chrome")
    except Exception:
        b = p.chromium.launch()
    pg = b.new_page(viewport={"width": a.w, "height": a.h}, device_scale_factor=a.scale, reduced_motion="reduce")
    pg.goto(pathlib.Path(a.html).resolve().as_uri(), wait_until="networkidle", timeout=60000)
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(a.wait)
    pg.screenshot(path=str(pathlib.Path(a.out).resolve()))
    b.close()
print(a.out)
