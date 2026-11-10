#!/usr/bin/env python3
"""Check the built site in site/dist before a deploy: one h1 per page, a self canonical, title and description lengths,
structured data that parses, no duplicate ids, and every internal link, anchor and asset present.

  python3 site/check.py            check site/dist
  python3 site/check.py <folder>   check another build (for example a SITE_DIST build)

Exits 1 when it finds a problem.
"""
import html
import json
import pathlib
import re
import sys

SITE = pathlib.Path(__file__).resolve().parent
D = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SITE / "dist"
_url = SITE / "site-url.txt"
SITE_URL = (_url.read_text().strip() if _url.exists() else "https://opendesigner.dev").rstrip("/")


def main():
    redirects = {r["source"] for r in json.loads((D / "vercel.json").read_text())["redirects"]}
    problems, n = [], 0
    for f in sorted(D.rglob("*.html")):
        if f.parts[len(D.parts):len(D.parts) + 2] == ("library", "r"):  # raw component files for agents to fetch, not pages
            continue
        n += 1
        h = f.read_text()
        rel = "/" + str(f.relative_to(D)).replace("index.html", "")
        t = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
        d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
        h1 = len(re.findall(r"<h1[\s>]", h))
        if h1 != 1:
            problems.append(f"{rel}: {h1} h1")
        if f.name != "404.html":
            if not 30 <= len(t) <= 65:
                problems.append(f"{rel}: title is {len(t)} characters: {t}")
            if not 110 <= len(d) <= 160:
                problems.append(f"{rel}: description is {len(d)} characters")
            c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
            if not c or c.group(1) != SITE_URL + rel:
                problems.append(f"{rel}: canonical {c and c.group(1)}")
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h):
            try:
                json.loads(blk)
            except ValueError as e:
                problems.append(f"{rel}: structured data does not parse: {e}")
        ids = re.findall(r'\sid="([^"]+)"', h)
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup:
            problems.append(f"{rel}: duplicate ids {dup}")
        for href in set(re.findall(r'href="([^"]+)"', h)):
            if href.startswith(("http", "mailto:")):
                continue
            if href.startswith("#"):
                if href[1:] and href[1:] not in ids:
                    problems.append(f"{rel}: missing anchor {href}")
                continue
            path = href.split("#")[0].split("?")[0]  # a ?v= version on a stylesheet is not part of the file name
            if not path.startswith("/"):
                problems.append(f"{rel}: relative link {href}")
                continue
            target = D / path.lstrip("/")
            if path.endswith("/"):
                target = target / "index.html"
            if not target.exists() and path not in redirects:
                problems.append(f"{rel}: broken link {href}")
        for src in set(re.findall(r'src="(/[^"]+)"', h)):
            if not src.startswith("/_vercel/") and not (D / src.split("?")[0].lstrip("/")).exists():  # /_vercel/ is served by Vercel
                problems.append(f"{rel}: missing asset {src}")
    print(f"{n} pages checked")
    print("\n".join(problems) or "no problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
