#!/usr/bin/env python3
"""Build brand/showcase/index.html: every showcase piece with its direction, as one page.

  python3 brand/showcase/build_gallery.py

Makes small JPEG thumbnails in _thumbs/ so the page stays light. The full-size renders (shot*.png) stay out of git
(brand/.gitignore); each thumbnail links to the piece's live index.html.
"""
import html
import json
import pathlib
import re

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CATS = [("product", "B2B product screens", "1440 × 900"), ("styles", "Style studies", "1440 × 900"),
        ("heroes", "Hero sections", "1440 × 900"), ("components", "Web components", "1440 × 900"),
        ("app-screens", "App screens", "phone, tablet, desktop"), ("watch", "Watch screens", "49 mm class"),
        ("footers", "Footer sections", "1440 wide"), ("mockups", "Mockups", "scenes")]
THUMBS = HERE / "_thumbs"


def shown(cat, piece):
    """False for pieces that were replaced, or that the owner's review removed (audit/<cat>--<piece>.json)."""
    notes = piece / "notes.md"
    if notes.exists() and "Replaced on 2026-10-14 by" in notes.read_text():
        return False
    audit = HERE / "audit" / f"{cat}--{piece.name}.json"
    return not (audit.exists() and json.loads(audit.read_text()).get("owner", {}).get("verdict") == "remove")


def blurb(piece):
    notes = piece / "notes.md"
    title, text = piece.name, ""
    if notes.exists():
        lines = notes.read_text().splitlines()
        for ln in lines:
            if ln.startswith("# "):
                title = ln[2:].strip()
                break
        body = [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#") and not ln.startswith("|") and not ln.startswith("-")]
        if body:
            text = re.sub(r"[*_`]", "", body[0])
            text = text if len(text) < 190 else text[:187].rsplit(" ", 1)[0] + "…"
    return title, text


def thumb(src, width):
    THUMBS.mkdir(exist_ok=True)
    out = THUMBS / (src.parent.parent.name + "--" + src.parent.name + "--" + src.stem + ".jpg")
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        im = Image.open(src).convert("RGB")
        im.thumbnail((width, width * 3))
        im.save(out, "JPEG", quality=84, optimize=True, progressive=True)
    return out.relative_to(HERE).as_posix()


def main():
    sections, total = [], 0
    for cat, label, size in CATS:
        d = HERE / cat
        if not d.is_dir():
            continue
        cards = []
        for piece in sorted(p for p in d.iterdir() if p.is_dir() and (p / "shot.png").exists() and shown(cat, p)):
            title, text = blurb(piece)
            shots = sorted(piece.glob("shot*.png"))
            shots = [s for s in shots if "mobile" not in s.name] or shots
            tw = 900 if cat in ("app-screens", "watch") else 1400
            page = (piece / "index.html").relative_to(HERE).as_posix()
            imgs = "".join(f'<a href="{page}"><img loading="lazy" src="{thumb(s, tw)}" alt="{html.escape(title)}"></a>' for s in shots[:2])
            num = piece.name.split("-")[0]
            cards.append(f'<article class="card {cat}"><div class="shots">{imgs}</div><div class="cap"><span class="n">{num}</span>'
                         f'<div><h3>{html.escape(title)}</h3><p>{html.escape(text)}</p></div></div></article>')
            total += 1
        if cards:
            proc = [p.name for p in d.glob("PROCESS*.md")]
            sections.append(f'<section><header><h2>{label}</h2><span>{len(cards)} pieces · {size}</span></header>'
                            f'<div class="grid {cat}">{"".join(cards)}</div>'
                            f'<p class="proc">Process notes: {", ".join(f"<a href={cat}/{p}>{p}</a>" for p in proc) or "pending"}</p></section>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OpenDesigner showcase</title><link rel="stylesheet" href="../src/brand.css"><style>
html,body{{overflow:auto}} body{{padding:clamp(16px,5vw,72px)}}
.top{{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:64px}}
h1{{font-size:clamp(44px,7vw,104px)}} .top p{{max-width:560px;font-size:20px}}
section{{margin:0 0 96px}} section header{{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--rule);padding-top:20px;margin-bottom:28px}}
section h2{{font-size:clamp(28px,3vw,44px);font-weight:600;letter-spacing:-.04em}} section header span,.proc{{font:400 14px/1.4 var(--mono);color:var(--muted)}}
.proc a{{color:var(--accent-text)}}
.grid{{display:grid;gap:28px;grid-template-columns:repeat(auto-fill,minmax(min(100%,520px),1fr))}}
.grid.app-screens,.grid.watch{{grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr))}}
.card .shots{{display:flex;gap:10px}} .card .shots a{{flex:1;min-width:0}}
.card img{{width:100%;display:block;border-radius:14px;box-shadow:0 0 0 1px var(--rule),0 30px 60px -30px rgb(0 0 0 / .6)}}
.watch img{{border-radius:28%/24%}}
.cap{{display:flex;gap:14px;margin-top:14px}} .cap .n{{font:500 14px/1.6 var(--mono);color:var(--accent-text)}}
.cap h3{{font-size:18px;font-weight:600;letter-spacing:-.02em}} .cap p{{font-size:15px;line-height:1.45;color:var(--muted);margin-top:4px}}
</style></head><body data-theme="ink">
<div class="top"><div><div class="eyebrow"><span class="dot"></span>Made with OpenDesigner</div><h1 class="display" style="margin-top:20px">{total} pieces. <em>{total} directions.</em> One process.</h1></div>
<p class="lede">Every piece below started the same way: real references, then a design system from the OpenDesigner engine, then the build, then checks. Every brand is invented.</p></div>
{"".join(sections)}
</body></html>"""
    (HERE / "index.html").write_text(page)
    for old in THUMBS.glob("*.jpg"):  # thumbnails of pieces no longer shown
        if f"_thumbs/{old.name}" not in page:
            old.unlink()
    print(f"{total} pieces -> {HERE / 'index.html'}")


if __name__ == "__main__":
    main()
