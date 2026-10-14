#!/usr/bin/env python3
"""Outline a word in a font file to SVG path data, with the font's pair kerning (GPOS PairPos).

  python3 brand/tools/outline.py FONT.ttf "OpenDesigner" --track -0.02 > path.json

Prints JSON: {"d": "<path data, y down, baseline at 0, 1000 units per em>", "width": ..., "cap": ..., "desc": ...}
"""
import argparse
import json

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


def pair_kerning(font):
    """{(left glyph, right glyph): x advance adjustment} from GPOS PairPos lookups (formats 1 and 2)."""
    kern = {}
    if "GPOS" not in font:
        return kern
    gpos = font["GPOS"].table
    for lookup in gpos.LookupList.Lookup:
        subs = lookup.SubTable
        if lookup.LookupType == 9:  # extension
            subs = [s.ExtSubTable for s in subs]
        for st in subs:
            if getattr(st, "LookupType", 2) != 2 and lookup.LookupType != 9:
                continue
            if not hasattr(st, "Format") or not hasattr(st, "Coverage"):
                continue
            cov = st.Coverage.glyphs
            if st.Format == 1:
                for i, left in enumerate(cov):
                    for pvr in st.PairSet[i].PairValueRecord:
                        v = getattr(pvr.Value1, "XAdvance", 0) if pvr.Value1 else 0
                        if v:
                            kern.setdefault((left, pvr.SecondGlyph), v)
            elif st.Format == 2:
                c1 = st.ClassDef1.classDefs if st.ClassDef1 else {}
                c2 = st.ClassDef2.classDefs if st.ClassDef2 else {}
                for left in cov:
                    k1 = c1.get(left, 0)
                    rec = st.Class1Record[k1]
                    for right, k2 in list(c2.items()) + [(None, 0)]:
                        v1 = rec.Class2Record[k2].Value1
                        v = getattr(v1, "XAdvance", 0) if v1 else 0
                        if v and right:
                            kern.setdefault((left, right), v)
    return kern


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("font")
    ap.add_argument("text")
    ap.add_argument("--track", type=float, default=0.0, help="tracking in em")
    a = ap.parse_args()
    f = TTFont(a.font)
    upm = f["head"].unitsPerEm
    s = 1000 / upm
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    kern = pair_kerning(f)
    names = [cmap[ord(c)] for c in a.text]
    x, parts = 0.0, []
    for i, g in enumerate(names):
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
        parts.append(pen.getCommands())
        x += gs[g].width * s
        if i + 1 < len(names):
            x += kern.get((g, names[i + 1]), 0) * s + a.track * 1000
    os2 = f["OS/2"]
    print(json.dumps({"d": " ".join(parts), "width": round(x, 1), "cap": round(os2.sCapHeight * s, 1),
                      "desc": round(-os2.sTypoDescender * s, 1), "kerned_pairs": len(kern)}))


if __name__ == "__main__":
    main()
