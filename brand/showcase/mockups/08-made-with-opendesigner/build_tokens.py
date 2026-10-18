#!/usr/bin/env python3
"""Compile OpenDesigner's own brand tokens (brand/design-system/project/tokens.json) to tokens.css for this scene.
Same output format as brand/design-system/build_previews.py, whose _local/ copy is git-ignored.

  python3 brand/showcase/mockups/08-made-with-opendesigner/build_tokens.py
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
T = json.loads((HERE.parents[2] / "design-system/project/tokens.json").read_text())
themes = [t["id"] for t in T["color"]["themes"]]
out = [f"/* {T['name']} brand tokens, compiled from brand/design-system/project/tokens.json by build_tokens.py */"]
for i, th in enumerate(themes):
    sel = f':root, [data-theme="{th}"]' if i == 0 else f'[data-theme="{th}"]'
    decl = [f"--{c['name']}: {c['value'][th] if isinstance(c['value'], dict) else c['value']};" for c in T["color"]["tokens"]]
    decl += [f"--{s['name']}: {s['value'][th]};" for s in T["shadow"]["tokens"]]
    out.append(sel + " { " + " ".join(decl) + " }")
root = [f"--{t['name']}: {t['value']};" for fam in ("spacing", "radius") for t in T[fam]["tokens"]]
root += [f"--font-{k}: {v};" for k, v in T["type"]["families"].items()]
out.append(":root { " + " ".join(root) + " }")
for g in T["type"]["groups"]:
    for s in g["styles"]:
        fam = s.get("family", g["family"])
        out.append(f".{s['name']} {{ font-family: var(--font-{fam}); font-size: {s['fontSize']}; line-height: {s['lineHeight']}; "
                   f"font-weight: {s['fontWeight']}; letter-spacing: {s['letterSpacing']}; }}")
(HERE / "tokens.css").write_text("\n".join(out) + "\n")
print(HERE / "tokens.css")
