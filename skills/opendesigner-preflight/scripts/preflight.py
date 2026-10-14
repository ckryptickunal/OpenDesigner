#!/usr/bin/env python3
"""OpenDesigner preflight: catch the silly mistakes before an export. Read-only.

  preflight.py html  <file.html> [--medium web|app|watch|video]   type and font checks from the page's CSS
  preflight.py video <file.mp4> [--ignore 0-17]         frozen time with timestamps, black frames, audio, length
  preflight.py frames <file.mp4> [--every 0.5] [--out DIR]   full-size frames plus 390 px phone copies
  preflight.py audio <clip.wav> [...]                     noise bursts or clicks at the start or end of each clip

Exit code 1 when an error is found. Standard library only, no network; video modes need ffmpeg and ffprobe.
The html check reads CSS, not the rendered page. See ../references/checklist.md for the checks a script cannot make.
"""
import argparse, html as htmllib, json, re, shutil, subprocess, sys
from pathlib import Path

GENERIC = {"serif", "sans-serif", "monospace", "system-ui", "ui-monospace", "ui-sans-serif", "ui-serif", "ui-rounded",
           "-apple-system", "blinkmacsystemfont", "inherit", "initial", "unset", "cursive", "fantasy", "emoji", "math"}
# Smallest text, as (error below, warn below) in CSS px. On app and watch pages laid out at the device's width in
# points, 1 CSS px = 1 pt. Sources: Apple HIG Typography (iOS 11 pt, watchOS 12 pt minimum), Material 3 (label-small
# 11, body-small 12), and stage 11 of the opendesigner skill (12 px on the web, 11 pt on mobile).
MIN = {"web": (11, 12), "app": (11, 11), "watch": (12, 12), "video": (40, 54)}
WHY = {"web": "below 11 px is under every platform minimum; 12 px is the web floor for text people read, and 11 px "
              "fits only short labels (stage 11, Material label-small)",
       "app": "11 pt is the iOS and Android minimum (Apple HIG, Material label-small)",
       "watch": "12 pt is the watchOS minimum (Apple HIG)",
       "video": "a 1920 px frame watched 390 pt wide on a phone needs about 54 px for 11 pt; check it on a 390 px wide frame"}
SIZE_WORDS = {"xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large", "xxx-large", "smaller", "larger"}


class Report:
    def __init__(self):
        self.errors = 0
        self.warns = 0

    def err(self, msg):
        self.errors += 1
        print(f"ERROR  {msg}")

    def warn(self, msg):
        self.warns += 1
        print(f"WARN   {msg}")

    def info(self, msg):
        print(f"       {msg}")


def split_top(s: str, seps: str) -> list:
    """Split on any character in `seps` outside parentheses and quotes."""
    parts, cur, depth, quote = [], [], 0, None
    for ch in s:
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif depth == 0 and ch in seps:
            parts.append("".join(cur))
            cur = []
            continue
        cur.append(ch)
    parts.append("".join(cur))
    return [p.strip() for p in parts if p.strip()]


def unquote_url(s: str) -> str:
    return re.sub(r"%([0-9A-Fa-f]{2})", lambda m: chr(int(m.group(1), 16)), s.replace("+", " "))


def google_families(url: str) -> list:
    """Families named in a Google Fonts stylesheet URL (css and css2 APIs). No request is made."""
    fams = []
    for value in re.findall(r"[?&]family=([^&]+)", htmllib.unescape(url)):
        for part in unquote_url(value).split("|"):
            name = part.split(":")[0].strip()
            if name:
                fams.append(name)
    return fams


def find_local(href: str, base: Path, html_dir: Path):
    """A stylesheet path on disk: relative to the file that links it, or root-relative (searched upward)."""
    href = href.split("#")[0].split("?")[0]
    if not href.startswith("/"):
        p = (base / href).resolve()
        return p if p.is_file() else None
    for d in [html_dir, *html_dir.parents]:
        p = d / href.lstrip("/")
        if p.is_file():
            return p
    return None


class Sheets:
    """Every stylesheet a page loads, in document order: <style>, <link rel=stylesheet> and @import."""

    def __init__(self, html_path: Path, html: str):
        self.html_dir = html_path.parent.resolve()
        self.css, self.google, self.remote, self.missing = [], {}, [], []
        for m in re.finditer(r"<style[^>]*>(.*?)</style>|<link\b[^>]*>", html, re.S | re.I):
            if m.group(1) is not None:
                self.add_css(m.group(1), self.html_dir, 0)
                continue
            attrs = {k.lower(): v for k, v in re.findall(r'([\w-]+)\s*=\s*["\']([^"\']*)["\']', m.group(0))}
            rel = attrs.get("rel", "").lower().split()
            if "stylesheet" in rel or ("preload" in rel and attrs.get("as", "").lower() == "style"):
                self.add_href(attrs.get("href", ""), self.html_dir, 0)

    def add_href(self, href: str, base: Path, depth: int):
        href = htmllib.unescape(href.strip())
        if not href or depth > 4:
            return
        if re.match(r"(https?:)?//", href, re.I):
            if re.search(r"//fonts\.googleapis\.com/css", href, re.I):
                for f in google_families(href):
                    self.google.setdefault(f, href)
            elif href not in self.remote:
                self.remote.append(href)
            return
        p = find_local(href, base, self.html_dir)
        if p is None:
            self.missing.append(href)
        else:
            self.add_css(p.read_text(encoding="utf-8", errors="replace"), p.parent, depth + 1)

    def add_css(self, css: str, base: Path, depth: int):
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        for imp in re.findall(r"@import\s+(?:url\(\s*)?[\"']?([^\"')\s;]+)", css, re.I):
            self.add_href(imp, base, depth)
        self.css.append(css)


def css_blocks(css: str) -> list:
    """(prelude, body, enclosing at-rules) for every innermost block, in order."""
    out, stack, start, leaf, i, n = [], [], 0, False, 0, len(css)
    while i < n:
        c = css[i]
        if c in "\"'":
            j = css.find(c, i + 1)
            i = n if j < 0 else j + 1
            continue
        if c == "{":
            stack.append(css[start:i].rsplit(";", 1)[-1].strip())
            start, leaf = i + 1, True
        elif c == "}":
            if stack:
                pre = stack.pop()
                if leaf:
                    out.append((pre, css[start:i], list(stack)))
            start, leaf = i + 1, False
        i += 1
    return out


def decls(body: str) -> list:
    out = []
    for d in split_top(body, ";"):
        if ":" in d:
            prop, val = d.split(":", 1)
            out.append((prop.strip().lower() if not prop.strip().startswith("--") else prop.strip(),
                        re.sub(r"\s*!important\s*$", "", val.strip(), flags=re.I)))
    return out


def length_px(tok: str, root: float):
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem|pt|pc)", tok.strip(), re.I)
    if not m:
        return None
    v, unit = float(m.group(1)), m.group(2).lower()
    return v * {"px": 1, "rem": root, "pt": 4 / 3, "pc": 16}[unit]


def size_px(val: str, root: float):
    """Font sizes a value can render at, in CSS px. None when it depends on the parent or the window."""
    val = val.strip()
    m = re.fullmatch(r"(clamp|min|max)\((.*)\)", val, re.I | re.S)
    if m:
        args = split_top(m.group(2), ",")
        if m.group(1).lower() == "clamp" and len(args) == 3:
            args = [args[0], args[2]]
        got = [x for x in (length_px(a, root) for a in args) if x is not None]
        return got or None
    x = length_px(val, root)
    return None if x is None else [x]


def first_family(stack: str):
    names = split_top(stack, ",")
    if not names or names[0].startswith("var("):
        return None
    name = names[0].strip("'\"").strip()
    return None if name.lower() in GENERIC else name


def parse_font(val: str):
    """The `font` shorthand, `[style] [variant] [weight] [stretch] size[/line-height] family`, as (size, family)."""
    toks = split_top(val, " \t\r\n")
    for i, t in enumerate(toks):
        head = split_top(t, "/")[0] if "/" in t and not t.startswith("/") else t
        if re.fullmatch(r"-?\d*\.?\d+(px|rem|em|pt|pc|%|vw|vh|vmin|vmax|cqi|ch|ex)", head, re.I) \
                or re.match(r"(clamp|min|max|calc)\(", head, re.I) or head.lower() in SIZE_WORDS:
            rest = i + 1
            if t.endswith("/"):
                rest = i + 2
            elif "/" not in t and rest < len(toks) and toks[rest].startswith("/"):
                rest += 2 if toks[rest] == "/" else 1
            return head, " ".join(toks[rest:])
    return None, None


def check_html(path: Path, medium: str) -> Report:
    r = Report()
    page = path.read_text(encoding="utf-8", errors="replace")
    sheets = Sheets(path, page)
    blocks = [b for css in sheets.css for b in css_blocks(css)]
    no_style = re.sub(r"<style[^>]*>.*?</style>", "", page, flags=re.S | re.I)
    words = set(re.findall(r"[\w-]+", no_style))
    for attr in re.findall(r"\sstyle\s*=\s*(?:\"([^\"]*)\"|'([^']*)')", no_style):
        blocks.append(("[style]", htmllib.unescape(attr[0] or attr[1]), []))

    def is_root(sel, at):
        return not any(a.startswith("@") and not a.lower().startswith("@layer") for a in at) and \
            any(s in (":root", "html") for s in split_top(sel, ","))

    def used(sel):  # a rule counts when every class and id it names appears in the page (markup or script)
        if sel == "[style]":
            return True
        for item in split_top(sel, ","):
            item = re.sub(r"\[[^\]]*\]|:(not|has)\([^)]*\)", "", item)
            if all(n in words for n in re.findall(r"[.#](-?[A-Za-z_][\w-]*)", item)):
                return True
        return False

    root_props, any_props, faces, scale = {}, {}, set(), set()
    for sel, body, at in blocks:
        ds = decls(body)
        if sel.lower().startswith("@font-face"):
            faces |= {v.strip("'\" ") for p, v in ds if p == "font-family"}
            continue
        for p, v in ds:
            if p.startswith("--"):
                any_props.setdefault(p, v)
                if is_root(sel, at):
                    root_props[p] = v

    def resolve(value, local, depth=0):
        if depth > 8 or "var(" not in value:
            return value

        def sub(m):
            name, fb = m.group(1), m.group(2)
            v = local.get(name, root_props.get(name, any_props.get(name)))
            return resolve(v, local, depth + 1) if v is not None else (resolve(fb.strip(), local, depth + 1) if fb else m.group(0))
        return re.sub(r"var\(\s*(--[\w-]+)\s*(?:,((?:[^()]|\([^()]*\))*))?\)", sub, value)

    root_px = 16.0
    for sel, body, at in blocks:
        if is_root(sel, at):
            for p, v in decls(body):
                if p == "font-size":
                    v = resolve(v, {})
                    pct = re.fullmatch(r"(\d*\.?\d+)%", v.strip())
                    root_px = 16 * float(pct.group(1)) / 100 if pct else (length_px(v, 16) or root_px)
    for name, v in any_props.items():
        if re.search(r"font-?size", name, re.I):
            for x in size_px(resolve(v, {}), root_px) or []:
                scale.add(round(x, 1))

    sizes, families, tracking, loose = [], set(), [], 0
    for sel, body, at in blocks:
        if sel.startswith("@") or not used(sel):
            continue
        ds = decls(body)
        local = {p: v for p, v in ds if p.startswith("--")}
        for prop, raw in ds:
            if prop.startswith("--"):
                continue
            val = resolve(raw, local)
            size_val = None
            if prop == "font-size":
                size_val = val
            elif prop == "font":
                size_val, fam = parse_font(val)
                f = first_family(fam) if fam else None
                if f:
                    families.add(f)
            elif prop == "font-family":
                f = first_family(val)
                if f:
                    families.add(f)
            elif prop == "letter-spacing":
                tracking += [float(x) for x in re.findall(r"(-?\d*\.?\d+)em\b", val)]
            if size_val is not None and size_val.lower() not in ("inherit", "initial", "unset", "revert"):
                got = size_px(size_val, root_px)
                if got:
                    sizes += got
                else:
                    loose += 1
    # families set from scripts (for example GSAP fontFamily)
    for f in re.findall(r"fontFamily\s*:\s*[\"']([^\"']+)[\"']", page):
        ff = first_family(f)
        if ff:
            families.add(ff)

    lower = lambda names: {n.lower() for n in names}
    google = sorted(f for f in families if f.lower() in lower(sheets.google))
    for f in sorted(families):
        if f.lower() in lower(faces) or f.lower() in lower(sheets.google):
            continue
        if sheets.remote:
            r.warn(f'font "{f}" has no @font-face here; it may come from {", ".join(sheets.remote)}, which this '
                   f"script does not fetch. Check document.fonts in a browser  [M9]")
        else:
            r.err(f'font "{f}" is used but has no @font-face, so another face may render  [M9]')
    if google:
        msg = f"loaded from Google Fonts: {', '.join(google)}"
        if medium == "video":
            r.warn(msg + "; a renderer can capture frames before a web font arrives. Ship the font file, or wait "
                         "for document.fonts.ready before the first frame  [M9]")
        else:
            r.info(msg + " (needs the network when the page loads)")
    for href in sheets.missing:
        r.warn(f"stylesheet {href} is linked but not found next to the page, so its sizes and fonts were not read")

    distinct = sorted(set(round(s, 1) for s in sizes))
    fmt = lambda xs: "[" + ", ".join(f"{x:g}" for x in xs) + "]"
    r.info(f"font sizes in px: {fmt(distinct)}" + (f" (1rem = {root_px:g}px)" if root_px != 16 else ""))
    if loose:
        r.info(f"{loose} font size(s) depend on the parent or the window (em, %, vw, calc) and were not counted; "
               "measure them rendered")
    if not distinct:
        r.warn("no font sizes found; measure type in the rendered page instead  [M6]")
    if len(distinct) > 10:
        r.warn(f"{len(distinct)} distinct font sizes; a scale has about 8  [M6]")
    close = [(a, b) for a, b in zip(distinct, distinct[1:]) if a and (b - a) / a < 0.10]
    if close:
        r.warn(f"sizes within 10% of each other: {', '.join(f'{a:g}/{b:g}' for a, b in close)}  [M6]")
    if len(scale) >= 3 and medium == "video":
        r.info("video sizes map the token scale to the frame; compare them with the mapping you wrote down  [M2]")
    elif len(scale) >= 3:
        off = [s for s in distinct if not any(abs(s - t) <= 0.5 for t in scale)]
        if off:
            r.warn(f"sizes outside the token scale {fmt(sorted(scale))}: {fmt(off)}  [M2, M6]")
    lo_err, lo_warn = MIN[medium]
    if [s for s in distinct if s < lo_err]:
        r.err(f"text under {lo_err}px for {medium}: {fmt([s for s in distinct if s < lo_err])}; {WHY[medium]}  [M8]")
    elif [s for s in distinct if s < lo_warn]:
        r.warn(f"text under {lo_warn}px for {medium}: {fmt([s for s in distinct if s < lo_warn])}; {WHY[medium]}  [M8]")
    r.info("sizes are as written; text inside a scaled container (transform: scale) is smaller on screen  [M31]")
    tight = sorted(set(t for t in tracking if t < -0.03))
    if tight:
        r.warn(f"letter-spacing tighter than -0.03em: {tight}; check glyphs and word spaces at 200%  [M5]")
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", page, flags=re.S | re.I)
    breaks = body if medium == "video" else " ".join(re.findall(r"<h[1-6][^>]*>.*?</h[1-6]>", body, re.S | re.I))
    if re.search(r"<br\s*/?>", breaks, re.I):
        r.warn(f"<br> in {'text' if medium == 'video' else 'a heading'}; let it wrap with text-wrap: balance  [M7]")
    for prop in ("left", "top", "width", "height", "fontSize", "letterSpacing"):
        if re.search(r"\.(to|fromTo|from)\([^;]*\{[^}]*\b" + prop + r"\s*:", page):
            r.warn(f"a tween animates {prop}; layout properties snap to whole pixels, use x, y or scale  [M18]")
    return r


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def need_ffmpeg():
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        sys.exit("ffmpeg and ffprobe are needed for this check")


def check_video(path: Path, ignore=()) -> Report:
    need_ffmpeg()
    r = Report()
    info = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)]).stdout)
    dur = float(info["format"]["duration"])
    v = [s for s in info["streams"] if s["codec_type"] == "video"]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"]
    if v:
        r.info(f"{v[0]['width']}x{v[0]['height']} at {v[0]['r_frame_rate']} fps, {dur:.1f} s")
    if not a:
        r.warn("no audio track; an explainer needs a voice or captions  [M25]")
    else:
        lo = run(["ffmpeg", "-hide_banner", "-i", str(path), "-map", "0:a:0", "-af", "ebur128", "-f", "null", "-"]).stderr
        m = re.findall(r"I:\s*(-?[\d.]+) LUFS", lo)
        if m:
            lufs = float(m[-1])
            r.info(f"loudness {lufs} LUFS (online video sits near -14 to -16)")
            if lufs < -24:
                r.warn("audio is very quiet")
    fr = run(["ffmpeg", "-hide_banner", "-i", str(path), "-map", "0:v:0", "-vf", "freezedetect=n=0.003:d=1.5", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"freeze_start:\s*([\d.]+)", fr)]
    lens = [float(x) for x in re.findall(r"freeze_duration:\s*([\d.]+)", fr)]
    if len(lens) < len(starts):  # a freeze that runs to the end has no duration line
        lens.append(dur - starts[-1])
    def outside(a, b):  # seconds of [a, b] not inside an ignored range
        cut = sum(max(0.0, min(b, y) - max(a, x)) for x, y in ignore)
        return max(0.0, (b - a) - cut)
    holds = [(a, outside(a, a + d)) for a, d in zip(starts, lens)]
    holds = [(a, d) for a, d in holds if d > 0]
    frozen = sum(d for _, d in holds)
    span = dur - sum(max(0.0, min(dur, y) - max(0.0, x)) for x, y in ignore)
    share = frozen / span if span else 0
    note = f" outside the ignored {', '.join(f'{x:g}-{y:g}' for x, y in ignore)} s" if ignore else ""
    r.info(f"frozen for {frozen:.1f} s in holds of 1.5 s or more ({share:.0%}){note}")
    if holds:
        longest = sorted(holds, key=lambda h: -h[1])[:6]
        r.info("longest holds: " + ", ".join(f"{a:.1f} s ({d:.1f} s)" for a, d in longest))
    if share > 0.15:
        r.warn("more than 15% of the runtime is frozen  [M14]")
    bl = run(["ffmpeg", "-hide_banner", "-i", str(path), "-map", "0:v:0", "-vf", "blackdetect=d=0.05:pix_th=0.05", "-f", "null", "-"]).stderr
    blacks = re.findall(r"black_start:([\d.]+)", bl)
    if blacks:
        r.warn(f"black frames at {blacks[:8]} s  [M15]")
    return r


def rms_db(path: Path, start=None, length=None, from_end=None) -> float:
    cmd = ["ffmpeg", "-hide_banner"]
    if from_end is not None:
        cmd += ["-sseof", f"-{from_end}"]
    elif start is not None:
        cmd += ["-ss", str(start)]
    cmd += ["-i", str(path)]
    if length is not None:
        cmd += ["-t", str(length)]
    out = run(cmd + ["-af", "astats", "-f", "null", "-"]).stderr
    m = re.findall(r"RMS level dB:\s*(-?[\d.]+|-inf)", out)
    return float(m[0]) if m and m[0] != "-inf" else -120.0


def check_audio(paths) -> Report:
    need_ffmpeg()
    r = Report()
    for p in paths:
        head, tail = rms_db(p, start=0, length=0.04), rms_db(p, from_end=0.12)
        gap = rms_db(p, from_end=0.45, length=0.3)
        body = rms_db(p)
        if tail > -35 and gap < -45:
            r.err(f"{p.name}: a {tail:.0f} dB burst in the last 0.12 s after silence; often a container (WAV header or metadata) decoded as raw samples  [M34]")
        elif tail > body + 3:
            r.err(f"{p.name}: the last 0.12 s is louder than the speech ({tail:.0f} vs {body:.0f} dB): a noise burst or a cut-off sound  [M34]")
        if head > -30:
            r.warn(f"{p.name}: the first 40 ms is at {head:.0f} dB; check for a click  [M34]")
    r.info(f"{len(paths)} clip(s) checked")
    return r


def extract_frames(path: Path, every: float, out: Path) -> Report:
    need_ffmpeg()
    r = Report()
    (out / "full").mkdir(parents=True, exist_ok=True)
    (out / "phone").mkdir(parents=True, exist_ok=True)
    sel = f"select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,{every})'"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-vf", sel, "-fps_mode", "vfr", str(out / "full" / "%04d.png")])
    run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-vf", sel + ",scale=390:-2", "-fps_mode", "vfr", str(out / "phone" / "%04d.png")])
    n = len(list((out / "full").glob("*.png")))
    r.info(f"{n} frames in {out}/full, with 390 px copies in {out}/phone. Frame k is at (k-1) x {every} s.")
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    h = sub.add_parser("html"); h.add_argument("file")
    h.add_argument("--medium", choices=list(MIN), default="web", help="where it is seen: web page, app or watch screen (laid out in points), or video frame")
    v = sub.add_parser("video"); v.add_argument("file")
    v.add_argument("--ignore", action="append", default=[], metavar="START-END", help="seconds to leave out, such as a deliberate 'before' act; repeatable")
    au = sub.add_parser("audio"); au.add_argument("files", nargs="+")
    f = sub.add_parser("frames"); f.add_argument("file"); f.add_argument("--every", type=float, default=0.5); f.add_argument("--out", default="preflight-frames")
    a = ap.parse_args()
    if a.cmd == "audio":
        r = check_audio([Path(x) for x in a.files])
        print(f"{r.errors} error(s), {r.warns} warning(s). The checklist covers what this script cannot see: references/checklist.md")
        sys.exit(1 if r.errors else 0)
    p = Path(a.file)
    if not p.exists():
        sys.exit(f"not found: {p}")
    if a.cmd == "html":
        r = check_html(p, a.medium)
    elif a.cmd == "video":
        r = check_video(p, [tuple(float(x) for x in g.split("-", 1)) for g in a.ignore])
    else:
        r = extract_frames(p, a.every, Path(a.out))
    print(f"{r.errors} error(s), {r.warns} warning(s). The checklist covers what this script cannot see: references/checklist.md")
    sys.exit(1 if r.errors else 0)


if __name__ == "__main__":
    main()
