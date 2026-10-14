#!/usr/bin/env python3
"""Find invented names in a page's text that are already used by another piece, or one or two letters from one.

  python3 brand/tools/check_names.py <file or folder> ... [--piece <cat>/<folder>] [--gallery] [--quiet] [--registry NAMES.md]

Reads .html and .md files: the visible text, alt, title, aria-label and placeholder text, and the strings in scripts (pieces
often render their data from a script). Finds capitalised, name-like words and runs ("Coldwater Bay Hotel", "Tellwick") and
checks them against the name registry, brand/showcase/NAMES.md, where every invented name belongs to one piece.

  ERROR  a registry name, or a distinctive word of one ("Calder" in "41 Calder Street"), that belongs to another piece
  ERROR  a name one or two letters from another piece's name (Tellwick and Stellwick), or the same new name in two pieces
  WARN   another piece's one-word name that is also a dictionary word (Craft, Dispatch): check it is not used as a name here
  NEW    names that are not in the registry: search the web for each one, then add it to NAMES.md (append only)

The piece comes from the path (brand/showcase/<cat>/<folder>/...; anything under site/ is "site") or from --piece; a registry
row belongs to a piece when the piece appears in its Pieces cell. A folder is checked one .html page at a time, skipping
opendesigner/ folders and gallery pages that sit beside the pieces; --gallery checks a page that shows other pieces on purpose. "Dictionary word" means a lowercase entry in
/usr/share/dict/words when that file exists; without it every capitalised word counts as name-like, so the lists grow.
This is a candidate finder like check_dates.py, not a verdict: a real place or a UI word can appear in the lists. It never
searches the web; that step is yours. Standard library only. Exits 1 when it finds an error.
"""
import argparse
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "brand" / "showcase" / "NAMES.md"
WORDS = pathlib.Path("/usr/share/dict/words")
# Words that start sentences and labels everywhere; never names on their own.
STOP = set("""a an and or but if in on at to for of with by from as into over under up down out off about after before
this that these those it its we you your our their my his her they them he she i is are was were be been not no yes all any
each every new more most less some one two three four five six seven eight nine ten first last next back home here there
what when where why how who which then than so do does did done can will just only also very ok okay hi hello please thanks
mon tue wed thu fri sat sun monday tuesday wednesday thursday friday saturday sunday jan feb mar apr may jun jul aug sep sept
oct nov dec january february march april june july august september october november december today tomorrow yesterday""".split())
# Common parts of company names: never distinctive on their own.
GENERIC = set("""street road lane avenue square yard bay hill park house hotel inn bar cafe kitchen kitchens studio studios
labs lab group co company inc ltd llc aps gmbh partners systems foods services service supply supplies works report
review team club bank cloud data health care center centre city north south east west harbour telecom maison atelier
mutual capital holdings ventures media""".split())
NAME_RE = re.compile(r"[^\W\d_][\w'’\-]*")
ATTR_RE = re.compile(r'\s(?:alt|title|aria-label|placeholder)="([^"]*)"', re.I)
STR_RE = re.compile(r'"((?:[^"\\\n]|\\.){2,300})"|\'((?:[^\'\\\n]|\\.){2,300})\'|`([^`\\]{2,300})`')


def load_words(path):
    if not path.exists():
        return set()
    return {w.strip() for w in path.read_text(errors="replace").splitlines() if w[:1].islower()}


def nodes_of(path):
    """Text nodes, one per element run of text, so a run of capitalised words never spans two elements."""
    s = path.read_text(errors="replace")
    if path.suffix not in (".html", ".htm"):
        return [line for line in s.splitlines() if line.strip()]
    s = re.sub(r"<style\b.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<script\b[^>]*application/ld\+json[^>]*>.*?</script>", " ", s, flags=re.S | re.I)  # structured data
    out = []
    for blk in re.findall(r"<script\b[^>]*>(.*?)</script>", s, flags=re.S | re.I):
        for m in STR_RE.finditer(blk):  # strings in scripts, which may hold markup of their own
            out += re.split(r"<[^>]*>?|^[^<]*>|\$\{[^}]*\}", html.unescape(next(g for g in m.groups() if g is not None)))
    s = re.sub(r"<script\b.*?</script>", " ", s, flags=re.S | re.I)
    out += [html.unescape(a) for a in ATTR_RE.findall(s)]
    out += [html.unescape(t) for t in re.split(r"<[^>]+>", s)]
    return [re.sub(r"\s+", " ", t).strip() for t in out if t.strip()]


def in_dict(tok, words):
    """A dictionary word, or a plural or past form of one (the system word list has no inflections)."""
    w = tok.lower()
    forms = {w}
    for suf, add in (("s", ""), ("es", ""), ("ies", "y"), ("ed", ""), ("ed", "e"), ("ied", "y"), ("ing", ""), ("ing", "e"), ("er", ""),
                     ("est", ""), ("ly", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            forms.add(w[:-len(suf)] + add)
    if len(w) > 4 and w[-3] == w[-4] and w.endswith(("ed", "er")):
        forms.add(w[:-3])  # stopped -> stop
    return bool(forms & words)


def clean(tok):
    return re.sub(r"(['’]s|['’\-]+)$", "", tok)


def is_cap(tok):
    return tok[:1].isupper() and any(c.islower() for c in tok)


def names_in(nodes):
    """Capitalised runs ("Coldwater Bay Hotel") and single capitalised tokens, with whether each sat mid-sentence."""
    runs, toks = set(), {}
    for node in nodes:
        run, prev_end = [], None  # run: (start, end) of each token in the current run of capitalised words
        for m in NAME_RE.finditer(node):
            tok = clean(m.group(0))
            gap = node[prev_end:m.start()] if prev_end is not None else ""
            initial = prev_end is None or re.search(r"[.!?:;•|·—–]\s*$", node[:m.start()]) is not None
            joins = run and gap.strip() in ("", "&")
            if is_cap(tok) and tok.lower() not in STOP:
                before = NAME_RE.findall(node[:m.start()])
                mid = not initial and bool(before) and before[-1][:1].islower()
                toks[tok] = toks.get(tok, False) or mid
                if not joins and len(run) > 1:
                    runs.add(node[run[0][0]:run[-1][1]])
                run = run + [(m.start(), m.start() + len(tok))] if joins else [(m.start(), m.start() + len(tok))]
            elif joins and tok.isupper() and 2 <= len(tok) <= 4:  # "BV", "LLC" end a company name
                run = run + [(m.start(), m.end())]
            else:
                if len(run) > 1:
                    runs.add(node[run[0][0]:run[-1][1]])
                run = []
            prev_end = m.end()
        if len(run) > 1:
            runs.add(node[run[0][0]:run[-1][1]])
    return runs, toks


def registry(path):
    rows = []
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and line.startswith("| ") and cells[0] not in ("Name", "") and not set(cells[0]) <= set("-: "):
            rows.append((cells[0], cells[1], cells[2]))
    return rows


def distance(a, b, cap=2):
    """Edit distance with swaps (optimal string alignment), case-insensitive; stops early above cap."""
    a, b = a.lower(), b.lower()
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev2, prev = None, list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                cur[j] = min(cur[j], prev2[j - 2] + 1)
        if min(cur) > cap:
            return cap + 1
        prev2, prev = prev, cur
    return prev[-1]


def near(a, b):
    """One or two letters apart (two only for names of 7 letters or more); plurals and numbered ids don't count."""
    x, y = sorted((a.lower(), b.lower()), key=len)
    if x == y or any(c.isdigit() or c in "'’" for c in x + y) or y in (x + "s", x + "es"):
        return False
    n, d = len(x), distance(x, y)
    return n >= 5 and (d == 1 or (d == 2 and n >= 7))


def piece_of(path, given):
    """The piece a file belongs to: <cat>/<folder> in the showcase, "site" for the website, None for a gallery page."""
    if given:
        return given
    parts = path.resolve().parts
    for i in range(len(parts) - 2):
        if parts[i] == "brand" and parts[i + 1] == "showcase":
            return f"{parts[i + 2]}/{parts[i + 3]}" if i + 4 < len(parts) else None
    return "site" if "site" in parts else path.stem


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--registry", type=pathlib.Path, default=REGISTRY)
    ap.add_argument("--piece", help="the piece these files belong to, as written in NAMES.md (default: from the path)")
    ap.add_argument("--words", type=pathlib.Path, default=WORDS, help="a word list; lowercase entries count as dictionary words")
    ap.add_argument("--gallery", action="store_true",
                    help="the page shows other pieces on purpose (a gallery, the site's home page): check near names and new names only")
    ap.add_argument("--quiet", action="store_true", help="print errors and warnings only")
    a = ap.parse_args(argv)
    words = load_words(a.words)
    rows = registry(a.registry)
    files = []
    for p in map(pathlib.Path, a.paths):
        files += [p] if p.is_file() else sorted(f for f in p.rglob("*.html") if "/opendesigner/" not in str(f) and "_thumbs" not in f.parts)
    known = {r[0].rstrip(".") for r in rows}
    # distinctive words of each registry name, with the pieces that own them
    owned, people = {}, set()
    for name, kind, pieces in rows:
        for w in NAME_RE.findall(name):
            w = clean(w)
            if is_cap(w) and len(w) >= 4 and w.lower() not in STOP | GENERIC:
                owned.setdefault(w, set()).add((name, pieces))
                if kind.startswith(("person", "people")):
                    people.add(w)  # surnames: Brennan and Brenner are both real, so no near-name check
    errors, seen_new, out = 0, {}, []
    explicit = {pathlib.Path(x).resolve() for x in a.paths}
    for f in files:
        piece = piece_of(f, a.piece)
        if piece is None:
            if f.resolve() not in explicit:
                continue  # a gallery or contact sheet names every piece on purpose
            piece = f.stem
        nodes = nodes_of(f)
        text = " \n ".join(nodes)
        runs, toks = names_in(nodes)
        mine = lambda pieces: piece in pieces
        err, warn, matched = [], [], set()
        for name, kind, pieces in rows:
            if a.gallery or mine(pieces) or not re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", text):
                continue
            matched.add(name)
            if " " not in name and in_dict(name, words):
                warn.append(f'WARN   "{name}" is a {kind} in {pieces}; it is also a dictionary word, so check it is not used as a name here')
            else:
                err.append(f'ERROR  "{name}" is already a {kind} in {pieces}')
        for tok in toks:
            if in_dict(tok, words) or tok.lower() in GENERIC:
                continue  # "Freight" or "Press" in two names is no collision; "Calder" is
            for name, pieces in owned.get(tok, ()):
                if not a.gallery and not mine(pieces) and name not in matched and name != tok:
                    err.append(f'ERROR  "{tok}" is part of "{name}" in {pieces}')
            for other, owners in owned.items():
                if other not in people and near(tok, other):
                    for name, pieces in owners:
                        if not mine(pieces):
                            err.append(f'ERROR  "{tok}" is one or two letters from "{other}" ("{name}", {pieces})')
        new = sorted({r for r in runs if r not in known and any(not in_dict(clean(w), words) for w in r.split())} |
                     {t for t, mid in toks.items() if t not in known and t not in owned and (not in_dict(t, words) or mid)
                      and t.lower() not in GENERIC and not any(t in r.split() for r in runs if r not in known)})
        for n in new:
            seen_new.setdefault(n, set()).add(piece)
        err = sorted(set(err))
        errors += len(err)
        out.append((f, piece, err, sorted(set(warn)), new))
    # pieces checked together: a new name in two or three of them, or two new names one or two letters apart. A name in
    # more pieces than that is shared vocabulary (a font, a place, a platform word), not an invented name.
    cross, cross_errors = [], 0
    names = sorted(n for n in seen_new if len(seen_new[n]) <= 3 and not in_dict(n, words))
    for i, n in enumerate(names):
        if len(seen_new[n]) > 1:
            cross.append(f'WARN   "{n}" is new in {len(seen_new[n])} pieces: {", ".join(sorted(seen_new[n]))}. One name, one piece')
        for m in names[i + 1:]:
            if " " not in n + m and near(n, m) and seen_new[n] != seen_new[m]:
                cross_errors += 1
                cross.append(f'ERROR  "{n}" ({", ".join(sorted(seen_new[n]))}) is one or two letters from "{m}" ({", ".join(sorted(seen_new[m]))})')
    errors += cross_errors
    for f, piece, err, warn, new in out:
        if a.quiet and not (err or warn):
            continue
        print(f"{f} ({piece})")
        for line in err + warn:
            print("  " + line)
        if new and not a.quiet:
            print(f"  NEW    {len(new)} not in NAMES.md (web-search each, then add it): " + ", ".join(new))
    for line in cross:
        print(line)
    print(f"{len(out)} files, {errors} errors" + ("" if words else f" (no word list at {a.words}: every capitalised word counted)"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
