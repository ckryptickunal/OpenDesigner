#!/usr/bin/env python3
"""Render watch pieces at 205 x 251 CSS px, scale 3, then clip the PNG to the rounded display shape.

  python3 brand/showcase/watch/render.py 01-ridgeline-trail [02-...]     (no names: all pieces)

shot.py has no transparent-background option, so the corners are cut here with an anti-aliased alpha mask.
"""
import pathlib, subprocess, sys
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
W, H, SCALE, R = 205, 251, 3, 48  # R matches --display-r in each index.html


def mask(png):
    im = Image.open(png).convert("RGBA")
    ss = 4
    m = Image.new("L", (im.width * ss, im.height * ss), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width * ss - 1, im.height * ss - 1), radius=R * SCALE * ss, fill=255)
    im.putalpha(m.resize(im.size, Image.LANCZOS))
    im.save(png)


def main(names):
    for n in names or sorted(p.name for p in HERE.iterdir() if p.is_dir() and p.name[:2].isdigit()):
        page = HERE / n / "index.html"
        out = HERE / n / "shot.png"
        subprocess.run([sys.executable, str(ROOT / "brand/tools/shot.py"), str(page), str(out),
                        "--w", str(W), "--h", str(H), "--scale", str(SCALE), "--wait", "900"], check=True, cwd=ROOT)
        mask(out)


if __name__ == "__main__":
    main(sys.argv[1:])
