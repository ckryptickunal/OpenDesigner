#!/usr/bin/env python3
"""Render the README images in brand/kit/readme/ from the HTML templates in this folder.

  python3 site/build.py                          once, to fetch the site's fonts into site/.cache (git-ignored)
  python3 brand/kit/readme/src/render.py         every image
  python3 brand/kit/readme/src/render.py banner  only the images whose names start with these

Each template draws one image at GitHub's README column width (1012 CSS px) and is rendered at 2x, so it stays sharp on
retina screens. With the class html.narrow, the same template draws a phone version (358 CSS px, *-narrow.png) that the
README picks with <picture> on screens up to 600 px wide. The social preview is the banner again at GitHub's size
(1280 x 640), full-bleed with square corners.
Photos are free Unsplash photos, hotlinked as on the site and credited in the README. Every PNG is kept under about
600 KB: when a render is larger, it is reduced to 256 colours with dithering.

Two images draw from local, git-ignored captures, like examples.html does from the showcase renders:
  before-after   site/demo/before-after/shots/ and review/marks-*.json (python3 site/demo/before-after/capture.py)
  library        part previews from the built site's /library/ page, saved in src/shots/ by
                 python3 brand/kit/readme/src/render.py --library-from http://127.0.0.1:4174 library
                 (serve a SITE_DIST build of the site there first)
"""
import io
import json
import pathlib
import sys
import tempfile

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
ROOT = HERE.parents[3]
LOGOS = json.loads((ROOT / "site/logos.json").read_text())["icons"]  # Simple Icons (CC0)
LOGO_DIR = ROOT / "brand/design-system/project/assets/Logos"
LIMIT = 600_000
SHOTS = HERE / "shots"  # git-ignored captures (see above)
DEMO = ROOT / "site/demo/before-after"
LIB_PARTS = [("approval-panel", "Approval panel", "Data"), ("bar-chart", "Monthly spend chart", "Charts"),
             ("command-menu", "Command menu", "Navigation"), ("chat-answer", "Answer with citations", "AI"),
             ("order-summary", "Order summary", "Commerce"), ("settings-toggles", "Settings switches", "Forms")]
# (output name, template, viewport width, device scale, mode: "" wide, "narrow" for phones, "full" for the social preview)
JOBS = [("banner.png", "banner.html", 1012, 2, ""),
        ("banner-narrow.png", "banner.html", 358, 2, "narrow"),
        ("social-preview.png", "banner.html", 1280, 1, "full"),
        ("works-in.png", "works-in.html", 1012, 2, ""),
        ("works-in-narrow.png", "works-in.html", 358, 2, "narrow"),
        ("how-it-works.png", "how-it-works.html", 1012, 2, ""),
        ("how-it-works-narrow.png", "how-it-works.html", 358, 2, "narrow"),
        ("examples.png", "examples.html", 1012, 2, ""),
        ("examples-narrow.png", "examples.html", 358, 2, "narrow"),
        ("before-after.png", "before-after.html", 1012, 2, ""),
        ("before-after-narrow.png", "before-after.html", 358, 2, "narrow"),
        ("library.png", "library.html", 1012, 2, ""),
        ("library-narrow.png", "library.html", 358, 2, "narrow")]


def logo(slug, size=20):
    return (f'<svg class="logo" viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">'
            f'<path fill="currentColor" d="{LOGOS[slug]["path"]}"/></svg>')


def page_html(template):
    css = (HERE / "readme.css").read_text()
    html = (HERE / template).read_text().replace("{{CSS}}", css)
    html = html.replace("{{ROOT}}", ROOT.as_uri()).replace("{{LOCKUP}}", (LOGO_DIR / "lockup-light.svg").read_text())
    for slug in LOGOS:
        html = html.replace("{{LOGO:%s}}" % slug, logo(slug))
    if "{{BA_" in html:
        html = html.replace("{{BA_BEFORE}}", demo_marks("before")).replace("{{BA_AFTER}}", demo_marks("after"))
    if "{{LIB_PARTS}}" in html:
        html = html.replace("{{LIB_PARTS}}", "".join(
            f'<figure class="part{" more" if i >= 4 else ""}"><img src="{(SHOTS / f"lib-{key}.png").as_uri()}" alt="">'
            f'<figcaption><strong>{name}</strong><span>{aisle}</span></figcaption></figure>' for i, (key, name, aisle) in enumerate(LIB_PARTS)))
    return html


CHECK = ('<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.3 5 8.7l4.6-5.2" fill="none" stroke="currentColor" stroke-width="1.8" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def demo_marks(side):
    """The audit's boxes on today's page (a dashed box and its number), or a check where each fix landed on the fixed page,
    as shares of the page that capture.py measured. The fixed page is shown cut to today's height, so a check below it is
    left out."""
    page = json.loads((DEMO / "review/marks-before.json").read_text())["page"]
    w, h = page["w"], page["h"]
    out = []
    for m in json.loads((DEMO / f"review/marks-{side}.json").read_text())["marks"]:
        x, y, bw, bh = m["rect"]
        if y >= h:
            continue
        pos = f"left:{x / w * 100:.2f}%;top:{y / h * 100:.2f}%"
        out.append(f'<span class="mk" style="{pos};width:{bw / w * 100:.2f}%;height:{min(bh, h - y) / h * 100:.2f}%"><b>{m["n"]}</b></span>'
                   if side == "before" else f'<span class="ok" style="{pos}"><b>{CHECK}</b></span>')
    return "".join(out)


def capture_library(base):
    """Each part's preview, as the library page shows it, at 2x."""
    SHOTS.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        pg.goto(base.rstrip("/") + "/library/", wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        for key, name, _ in LIB_PARTS:
            el = pg.locator(f"#item-{key} .item-media")
            el.scroll_into_view_if_needed()
            pg.wait_for_timeout(250)
            el.screenshot(path=str(SHOTS / f"lib-{key}.png"), animations="disabled")
            print(f"captured {name}")
        b.close()


def shrink(png_bytes):
    """Over the limit, reduce to 256 colours: a median-cut palette refined by k-means, with Floyd-Steinberg dithering.
    The canvas's rounded corners keep soft edges: 16 palette entries hold the edge colour at 16 levels of transparency."""
    if len(png_bytes) <= LIMIT:
        return png_bytes, "full colour"
    im = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    alpha = im.getchannel("A")
    see_through = alpha.getextrema()[0] < 255
    flat = Image.new("RGBA", im.size, (252, 253, 255, 255))
    flat.alpha_composite(im)
    n = 240 if see_through else 256
    q = flat.convert("RGB").quantize(n, method=Image.Quantize.MEDIANCUT, kmeans=2, dither=Image.Dither.FLOYDSTEINBERG)
    palette = q.getpalette()[:n * 3]
    palette += [0] * (n * 3 - len(palette))
    extra = {}
    if see_through:
        palette += [227, 230, 238] * 16  # the canvas's hairline edge, #e3e6ee
        idx = Image.frombytes("L", im.size, q.tobytes())
        idx.paste(alpha.point(lambda v: n + min(15, round(v / 17))), mask=alpha.point(lambda v: 255 if v < 255 else 0))
        q = Image.frombytes("P", im.size, idx.tobytes())
        extra["transparency"] = bytes([255] * n + [min(255, 17 * i) for i in range(16)])
    q.putpalette(palette)
    buf = io.BytesIO()
    q.save(buf, "PNG", optimize=True, **extra)
    return buf.getvalue(), "256 colours"


def main(prefixes):
    jobs = [j for j in JOBS if not prefixes or any(j[0].startswith(p) for p in prefixes)]
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        browser = p.chromium.launch(channel="chrome")
        for name, template, width, scale, mode in jobs:
            full = mode == "full"
            src = pathlib.Path(tmp) / template
            src.write_text(page_html(template))
            page = browser.new_page(viewport={"width": width, "height": 640 if full else 900}, device_scale_factor=scale)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on("requestfailed", lambda r: errors.append(f"failed: {r.url}"))
            page.goto(src.as_uri(), wait_until="networkidle")
            if mode == "narrow":
                page.evaluate("document.documentElement.classList.add('narrow')")
            if full:  # the social preview: the same drawing, scaled to fill GitHub's 1280 x 640 with square corners
                page.evaluate(f"document.documentElement.classList.add('full'); document.documentElement.style.zoom = {width / 1012}")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(400)
            png = page.locator("#canvas").screenshot(omit_background=not full, animations="disabled")
            data, how = shrink(png)
            (OUT / name).write_bytes(data)
            with Image.open(io.BytesIO(data)) as im:
                print(f"{name}: {im.size[0]} x {im.size[1]}, {len(data) // 1024} KB ({how})" + (f"  ERRORS: {errors}" if errors else ""))
            page.close()
        browser.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--library-from" in args:
        i = args.index("--library-from")
        capture_library(args[i + 1])
        args = args[:i] + args[i + 2:]
    main(args)
