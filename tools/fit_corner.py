#!/usr/bin/env python3
"""Measure Apple's continuous corner and find the CSS corner-shape that draws it (levers formulas.radius.continuous).

    python3 tools/fit_corner.py            sample SwiftUI's path, fit, print the table
    python3 tools/fit_corner.py --check    also fail if the numbers in synthesis/levers.json no longer match

Needs macOS with Xcode's command-line tools: the reference curve is SwiftUI's own RoundedRectangle(style: .continuous) path,
sampled for a 1000 x 1000 rect with corner radius 100 [S-L04-036]. In CSS Borders 4, superellipse(K) is the curve
x^(2^K) + y^(2^K) = 1 fitted to the corner box that border-radius sets [S-L04-080]; K = 1 is a circle and squircle is K = 2.
The error is the farthest distance between the two curves, either way round, in units of the radius.
"""
import json
import math
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
SWIFT = r"""
import SwiftUI
let r: CGFloat = 100
let path = RoundedRectangle(cornerRadius: r, style: .continuous).path(in: CGRect(x: 0, y: 0, width: 1000, height: 1000))
var cur = CGPoint.zero
func out(_ p: CGPoint) { if p.x < 400 && p.y < 400 { print(String(format: "%.5f %.5f", p.x / r, p.y / r)) } }
path.cgPath.applyWithBlock { el in
    let e = el.pointee
    switch e.type {
    case .moveToPoint, .addLineToPoint: cur = e.points[0]; out(cur)
    case .addQuadCurveToPoint:
        let c = e.points[0], p = e.points[1]
        for i in 1...100 { let t = CGFloat(i) / 100, u = 1 - t; out(CGPoint(x: u*u*cur.x + 2*u*t*c.x + t*t*p.x, y: u*u*cur.y + 2*u*t*c.y + t*t*p.y)) }
        cur = p
    case .addCurveToPoint:
        let c1 = e.points[0], c2 = e.points[1], p = e.points[2]
        for i in 1...100 { let t = CGFloat(i) / 100, u = 1 - t
            out(CGPoint(x: u*u*u*cur.x + 3*u*u*t*c1.x + 3*u*t*t*c2.x + t*t*t*p.x, y: u*u*u*cur.y + 3*u*u*t*c1.y + 3*u*t*t*c2.y + t*t*t*p.y)) }
        cur = p
    default: break
    }
}
"""


def apple_corner():
    with tempfile.TemporaryDirectory() as d:
        src, exe = pathlib.Path(d) / "corner.swift", pathlib.Path(d) / "corner"
        src.write_text(SWIFT)
        subprocess.run(["xcrun", "--sdk", "macosx", "swiftc", "-O", str(src), "-o", str(exe)], check=True, capture_output=True)
        pts = [tuple(map(float, line.split())) for line in subprocess.run([str(exe)], check=True, capture_output=True, text=True).stdout.split("\n") if line]
    return sorted(set(pts), key=lambda p: p[1] - p[0])  # from the top edge round to the left edge


def css_corner(radius, k, edge, n=300):
    """The CSS corner, in units of the token radius: straight edge, superellipse(k) at `radius`, straight edge."""
    e = 2 ** k
    curve = [(radius * (1 - math.cos(math.pi / 2 * i / n) ** (2 / e)), radius * (1 - math.sin(math.pi / 2 * i / n) ** (2 / e))) for i in range(n + 1)]
    pad = radius < edge
    return ([(0.0, edge)] if pad else []) + curve + ([(edge, 0.0)] if pad else [])


def _dist(p, line):
    best = 9.0
    for a, b in zip(line, line[1:]):
        ax, ay = b[0] - a[0], b[1] - a[1]
        size = ax * ax + ay * ay
        t = 0.0 if size == 0 else max(0.0, min(1.0, ((p[0] - a[0]) * ax + (p[1] - a[1]) * ay) / size))
        best = min(best, math.hypot(p[0] - a[0] - t * ax, p[1] - a[1] - t * ay))
    return best


def error(apple, radius, k):
    edge = max(p[0] for p in apple)
    css = css_corner(radius, k, edge)
    return max(max(_dist(p, css) for p in apple[::4]), max(_dist(q, apple) for q in css[::4] if q[0] <= edge and q[1] <= edge))


def fit(apple):
    best = min((error(apple, r / 100, k / 100), r, k) for r in range(100, 161, 6) for k in range(100, 201, 10))
    _, r0, k0 = best
    best = min((error(apple, r / 100, k / 100), r, k) for r in range(r0 - 6, r0 + 7) for k in range(k0 - 10, k0 + 11, 5))
    return best[1] / 100, best[2] / 100, best[0]


def main():
    apple = apple_corner()
    edge, diag = max(p[0] for p in apple), min(apple, key=lambda p: abs(p[0] - p[1]))
    radius, k, err = fit(apple)
    rows = [("plain circle at r (border-radius only)", 1, 1), ("squircle at r", 1, 2), (f"superellipse({k}) at {radius} r (the fit)", radius, k)]
    print(f"Apple's continuous corner meets the straight edge at {edge:.3f} r; its middle is at ({diag[0]:.4f}, {diag[1]:.4f}) r")
    print(f"(a circle's middle is at {1 - math.sqrt(0.5):.4f} r)")
    for label, r_, k_ in rows:
        print(f"  {label:44} farthest from Apple's curve: {error(apple, r_, k_):.4f} r")
    if "--check" in sys.argv:
        lv = json.loads((ROOT / "synthesis" / "levers.json").read_text())["formulas"]["radius"]["continuous"]
        ok = abs(lv["radiusScale"] - radius) <= 0.02 and abs(lv["superellipse"] - k) <= 0.05 and error(apple, lv["radiusScale"], lv["superellipse"]) <= lv["maxError"]
        print("levers.json matches" if ok else f"levers.json says superellipse({lv['superellipse']}) at {lv['radiusScale']} r: refit and update it")
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
