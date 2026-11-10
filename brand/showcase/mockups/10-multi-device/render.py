#!/usr/bin/env python3
"""Render this mockup: first the laptop's screen (desktop.html to desktop.png, 1440 x 900 at 2x), then the scene
(index.html to shot.png, 1600 x 1200 at scale 2). Both go through brand/tools/shot.py, so the settings are the
showcase's usual ones. The phone's screen is ../../app-screens/11-approvals-mobile/shot.png, rendered by that piece.

  python3 brand/showcase/mockups/10-multi-device/render.py [--out shot.png] [--query hide-text]

--query hide-text renders the scene with the caption made transparent, for measuring its contrast on the pixels behind it.
"""
import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SHOT = HERE.parents[2] / "tools" / "shot.py"

ap = argparse.ArgumentParser()
ap.add_argument("--out", default=str(HERE / "shot.png"))
ap.add_argument("--query", default="")
a = ap.parse_args()

def shot(src, out, w, h, query=""):
    cmd = [sys.executable, str(SHOT), str(src), str(out), "--w", str(w), "--h", str(h), "--scale", "2"]
    subprocess.run(cmd + (["--query", query] if query else []), check=True)

shot(HERE / "desktop.html", HERE / "desktop.png", 1440, 900)
shot(HERE / "index.html", pathlib.Path(a.out).resolve(), 1600, 1200, a.query)
