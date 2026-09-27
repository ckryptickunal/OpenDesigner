#!/usr/bin/env python3
"""The learning wiki: trusted sources -> raw text -> analysis JSON -> Markdown wiki -> OpenDesigner knowledge.

The extraction and ingest engine is OpenWiki (the `openwiki` package, https://github.com/ckryptickunal/OpenWiki).
It changes often: learn/openwiki.lock.json records the commit this repo was last tested with, and
`wiki.py upstream` compares it with GitHub (`--upgrade` installs the new commit, runs both test suites and
moves the lock only when they pass).
This tool adds what OpenDesigner needs on top: authority levels, plain web pages and GitHub files as
sources, a media list per page, an analysis schema with rules / decisions / process steps, and checks.

    python3 tools/wiki.py next                        what is out of date, in pipeline order, with the command for each step
    python3 tools/wiki.py map [--check]               learn/MAP.md: the knowledge by area, standard, card and question
    python3 tools/wiki.py proposals [--check]         list cards no question has adopted yet in synthesis/QUESTIONNAIRE.md
    python3 tools/wiki.py status [--json]             every source: analysed, in the wiki, raw text on this machine
    python3 tools/wiki.py add <url> --authority reference [--name "Name"]
    python3 tools/wiki.py remove <name or url>        take a source (or one page of it) off the list
    .venv-wiki/bin/python tools/wiki.py fetch [--only "Name"]    raw text into learn/raw/ (git-ignored); exit 1 when a source gets nothing
    python3 tools/wiki.py pending [--work-items]      raw files that have no analysis JSON yet ({"root", "items"}: the learn-analyze args)
    .venv-wiki/bin/python tools/wiki.py ingest        analysis JSON -> learn/wiki/ pages, then rebuild the index
    python3 tools/wiki.py check                       schema, types, quote length, authority, coverage; exit 1 on errors
    python3 tools/wiki.py trace                       append new sources to traces/L19-trace.md (S-L19 ids, learn/sids.json)
    .venv-wiki/bin/python tools/wiki.py upstream [--upgrade]    is OpenWiki ahead of learn/openwiki.lock.json?
    python3 tools/wiki.py standards [--bump "what changed"] [--built-from]   check synthesis/standards.json, or version a change
    python3 tools/wiki.py cite-check [ids] [--limit N]  Jev (TypeSafe) checks each rule against its source passage
    python3 tools/wiki.py flagged [--json]            what the citation check left for review (args of learn-escalate.js)
    python3 tools/wiki.py review-log < decisions.json record review decisions so settled items stop being flagged

Set up once: python3 -m venv .venv-wiki && .venv-wiki/bin/pip install "git+https://github.com/ckryptickunal/OpenWiki.git@<lock commit>" pysocks
YouTube blocks an IP after many caption requests. Run `tor` and set YOUTUBE_PROXY=socks5://127.0.0.1:9050.
Keys (YOUTUBE_API_KEY for channel listing) are read from the environment; this tool never prints them.

Analysis JSON (learn/analysis/<source id>.json) is written by an agent that read the whole raw file.
The process for doing that is in learn/README.md. Third-party text is never committed: only
learn/analysis/ and learn/wiki/ (summaries, rules, at most 3 quotes of 15 words or fewer per source).
"""
import argparse, fnmatch, html, json, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEARN = ROOT / "learn"
RAW = LEARN / "raw"
ANALYSIS = LEARN / "analysis"
WIKI = LEARN / "wiki"
SOURCES = LEARN / "sources.json"
TAXONOMY = LEARN / "taxonomy.json"
AUTHORITY = ("non-negotiable", "good-to-have", "reference")
MARK_START, MARK_END = "<!-- od:learn -->", "<!-- /od:learn -->"
QUOTE_MAX_WORDS, QUOTE_MAX = 15, 3
QUESTIONS = ROOT / "skills" / "opendesigner" / "references" / "questions.json"  # Q-ids and option values (maps_to, settles)
CARDS = ROOT / "synthesis" / "cards.json"                                        # Decision Card ids (supersedes)
WORK_ITEM_MAX = 5                 # files one learn-analyze agent reads together
# Platform and stack tags a rule or standard can apply to (a project's tags: its platforms plus its recorded stack).
TAGS = ("all", "web", "css", "react", "react-native", "ios", "swift", "android", "compose", "desktop")
RULE_AREAS = ("color", "typography", "layout", "shape", "elevation", "motion", "iconography", "components", "patterns",
              "content", "accessibility", "platforms", "process", "tokens", "tooling")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save_sources(cfg):
    SOURCES.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def all_sources(cfg):
    """Every configured source as (kind, entry)."""
    for kind in ("youtube_channels", "youtube_videos", "essay_sources", "pages", "github_repos"):
        for entry in cfg.get(kind, []):
            yield kind, entry


def some(items, n=4):
    """The first n items, with "..." only when some were left out."""
    items = list(items)
    return ", ".join(items[:n]) + ("..." if len(items) > n else "")


def question_ids():
    """{Q-id: [option values as strings]} from the skill's questions.json (list values joined with |)."""
    if not QUESTIONS.exists():
        return {}
    val = lambda v: "|".join(map(str, v)) if isinstance(v, list) else str(v)
    return {q["id"]: [val(o["v"]) for o in q.get("options", [])] for q in load(QUESTIONS).get("questions", [])}


def manifest_of_wiki():
    """learn/wiki/ingested.json: what OpenWiki ingested, plus the analysis hash each page was built from."""
    return load(WIKI / "ingested.json") if (WIKI / "ingested.json").exists() else {}


def skipped_file():
    """Pages fetch could not use, on this machine only (learn/raw/ is git-ignored)."""
    return RAW / "_skipped.json"


def authority_by_folder(cfg):
    return {e["folder"]: e.get("authority", "reference") for k, e in all_sources(cfg) if k != "youtube_videos"}


def video_id(url):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", url or "")
    return m.group(1) if m else None


def authority_of(path, cfg=None):
    """Single videos share raw/videos/, so their authority comes from their own entry, not the folder."""
    cfg = cfg or load(SOURCES)
    for e in cfg.get("youtube_videos", []):
        if video_id(e["url"]) == path.stem:
            return e.get("authority", "reference")
    return authority_by_folder(cfg).get(f"raw/{path.parent.name}", "reference")


def raw_files():
    return sorted(p for p in RAW.glob("*/*.txt") if not p.name.startswith("_"))


def header(path):
    """The Key: value header OpenWiki writes above the TRANSCRIPT marker."""
    meta = {}
    for line in path.read_text(encoding="utf-8", errors="replace").split("TRANSCRIPT", 1)[0].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip().lower().replace(" ", "_")] = v.strip()
    return meta


def source_id(path):
    return header(path).get("video_id") or path.stem


# ---------------------------------------------------------------------------------------------- add
def classify(url):
    if re.search(r"youtube\.com/(@|channel/|c/)", url):
        return "youtube_channels"
    if re.search(r"(youtube\.com/(watch|shorts)|youtu\.be/)", url):
        return "youtube_videos"
    if re.match(r"https://github\.com/[^/]+/[^/]+/?$", url):
        return "github_repos"
    return "pages"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "source"


def norm_url(url):
    """One spelling per page, so the same page is never listed twice: no scheme, no www., no trailing slash,
    a lower-case host. A YouTube video is its id, however the link is written."""
    url = (url or "").strip()
    if re.search(r"(youtube\.com/(watch|shorts)|youtu\.be/)", url) and video_id(url):
        return f"youtube:{video_id(url)}"
    u = re.sub(r"^[a-z][a-z0-9+.-]*://", "", url, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I).split("#")[0]
    host, _, path = u.partition("/")
    path = path.rstrip("/")
    return host.lower() + ("/" + path if path else "")


def entry_urls(e):
    return [u for u in (e.get("url"), e.get("query"), e.get("index_url"), *e.get("urls", [])) if u]


def cmd_add(args):
    cfg = load(SOURCES)
    kind = classify(args.url)
    key = norm_url(args.url)
    for k, e in all_sources(cfg):
        if key in {norm_url(u) for u in entry_urls(e)}:
            sys.exit(f"Already listed: {args.url} is part of \"{e['name']}\" ({k}, authority {e.get('authority', 'reference')}). "
                     "To change its authority, edit that entry in learn/sources.json; to take it off the list, run "
                     f"python3 tools/wiki.py remove \"{e['name']}\".")
    if kind == "github_repos":  # one folder and id prefix per repository, named after owner/repo
        owner, repo = re.match(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", args.url).groups()
        name, base = args.name or f"{owner}/{repo}", slug(f"{owner}-{repo}")
    else:
        name = args.name or re.sub(r"^https?://(www\.)?", "", args.url).rstrip("/")
        base = slug(name)
    folder, prefix = ("raw/videos" if kind == "youtube_videos" else f"raw/{base}"), base[:24].rstrip("-")
    for k, e in all_sources(cfg):
        if e["name"] == name:
            sys.exit(f"A source is already called \"{name}\" ({k}). Pass a different --name.")
        if kind != "youtube_videos" and e["folder"] == folder:
            sys.exit(f"The folder learn/{folder} already belongs to \"{e['name']}\" ({e.get('authority', 'reference')}). "
                     "Pass a different --name.")
        p = e.get("id_prefix")
        if kind in ("pages", "github_repos") and p and (p == prefix or prefix.startswith(p + "-") or p.startswith(prefix + "-")):
            sys.exit(f"The id prefix {prefix!r} would mix this source's ids with \"{e['name']}\" (prefix {p!r}). Pass a different --name.")
    entry = {"youtube_channels": {"name": name, "query": args.url, "channel_id": None, "folder": folder},
             "youtube_videos": {"name": name, "url": args.url, "folder": folder},
             "github_repos": {"name": name, "url": args.url, "include": ["README.md", "**/*.md"],
                              "folder": folder, "id_prefix": prefix},
             "pages": {"name": name, "urls": [args.url], "folder": folder, "id_prefix": prefix}}[kind]
    entry["authority"] = args.authority
    cfg.setdefault(kind, []).append(entry)
    save_sources(cfg)
    print(f"Added to {kind}: {name} ({args.authority}). Next: .venv-wiki/bin/python tools/wiki.py fetch --only \"{name}\"")
    if args.authority != "reference":
        print("It is a house source: follow learn/IMPROVING.md section 4, \"A new house source\".")


def cmd_remove(args):
    """Take a source off the list, or one page of a multi-page source. What was learned from it stays until removed by hand."""
    cfg, key = load(SOURCES), norm_url(args.what)
    folders = source_folders(cfg)
    for kind, e in all_sources(cfg):
        urls = [u for u in entry_urls(e) if norm_url(u) == key]
        if e["name"] != args.what and not urls:
            continue
        ids = []
        if kind == "pages" and e["name"] != args.what and len(e["urls"]) > 1:
            e["urls"] = [u for u in e["urls"] if norm_url(u) != key]
            what = f"{urls[0]} (one page of \"{e['name']}\"; {len(e['urls'])} pages stay)"
        else:
            cfg[kind].remove(e)
            what = f"\"{e['name']}\" ({kind}, {e.get('authority', 'reference')})"
            ids = sorted(i for i in source_ids(kind, e, folders) if (ANALYSIS / f"{i}.json").exists())
        save_sources(cfg)
        print(f"Removed {what} from learn/sources.json.")
        if ids:
            print(f"What was learned from it stays: {len(ids)} analysis files ({some(ids)}), their wiki pages and trace rows "
                  "(the trace is append-only). To take it out of the wiki too, delete those learn/analysis files, then run "
                  "python3 tools/wiki.py next." + (" House standards cite it: re-run the learn-standards workflow."
                                                     if e.get("authority") != "reference" else ""))
        return 0
    names = "\n  ".join(e["name"] for _, e in all_sources(cfg))
    print(f"No source is called {args.what!r} and none lists that URL. The names are:\n  {names}")
    return 1


# ---------------------------------------------------------------------------------------------- fetch
def openwiki(*argv, root=LEARN):
    cmd = [sys.executable, "-m", "openwiki", "--root", str(root), *argv]
    print("$", " ".join(cmd[1:]), flush=True)
    return subprocess.run(cmd).returncode


def raw_folder_name(folder):
    """OpenWiki turns '/' in a folder name into '_' (raw/videos -> raw_videos, outside the git-ignored raw/).
    So YouTube extraction runs with learn/raw/ as its root and a one-level folder name."""
    name = folder.removeprefix("raw/")
    if "/" in name or name == folder:
        sys.exit(f"folder must be raw/<name>, got {folder!r}")
    return name


def media_list(page_html, base):
    """Images, videos and figure captions on a page, so an agent can look at the ones that carry meaning."""
    from urllib.parse import urljoin
    out = []
    for m in re.finditer(r"<(img|video|source)\b([^>]*)>", page_html, re.I):
        attrs = dict(re.findall(r'(\w[\w-]*)="([^"]*)"', m.group(2)))
        src = attrs.get("src") or attrs.get("poster") or ""
        if not src or src.startswith("data:") or re.search(r"favicon|logo|avatar|\.svg$", src, re.I):
            continue
        out.append({"tag": m.group(1).lower(), "src": urljoin(base, html.unescape(src)),
                    "alt": html.unescape(attrs.get("alt", ""))})
    for cap in re.findall(r"<figcaption[^>]*>(.*?)</figcaption>", page_html, re.I | re.S):
        out.append({"tag": "figcaption", "text": html.unescape(re.sub(r"<[^>]+>", "", cap)).strip()})
    seen, uniq = set(), []
    for item in out:
        key = item.get("src") or item.get("text")
        if key not in seen:
            seen.add(key)
            uniq.append(item)
    return uniq


def fetch_page(url, folder, prefix, channel):
    from openwiki.essays import extract_title, fetch_url, write_article_from_html
    page = fetch_url(url)
    title = extract_title(page) or url
    tail = url.rstrip("/").split("/")[-1]
    ident = tail if "." not in tail else "home"
    path = write_article_from_html(page, folder=folder, title=f"{ident}", url=url, channel=channel,
                                   prefix=prefix, min_chars=200)
    if path is None:
        print(f"SKIP (too little text) {url}")
        return None
    text = path.read_text(encoding="utf-8").replace(f"Title: {ident}\n", f"Title: {title}\n", 1)
    path.write_text(text, encoding="utf-8")
    media = media_list(page, url)
    if media:
        path.with_suffix(".media.json").write_text(json.dumps(media, indent=1) + "\n", encoding="utf-8")
    print(f"OK {url} -> {path.relative_to(ROOT)} ({len(media)} media)")
    return path


def fetch_github(entry, folder):
    from openwiki.textfmt import write_essay_file
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["git", "clone", "--depth", "1", "-q", entry["url"], tmp], check=True)
        commit = subprocess.run(["git", "-C", tmp, "rev-parse", "--short", "HEAD"], capture_output=True,
                                text=True).stdout.strip()
        files = [p for p in Path(tmp).rglob("*") if p.is_file() and ".git" not in p.parts]
        for p in sorted(files):
            rel = p.relative_to(tmp).as_posix()
            if not any(fnmatch.fnmatch(rel, pat) for pat in entry.get("include", ["**/*.md"])):
                continue
            ident = f"{entry['id_prefix']}-{slug(rel.removesuffix('.md'))}"
            url = f"{entry['url'].rstrip('/')}/blob/{commit}/{rel}"
            write_essay_file(folder / f"{ident}.txt", ident, f"{entry['name']}: {rel}", f"commit {commit}",
                             f"{entry['name']} (GitHub, {entry.get('license', 'licence unknown')})", url,
                             p.read_text(encoding="utf-8", errors="replace"))
            print(f"OK {rel} -> {ident}.txt")


def entry_raw(kind, e):
    """The raw files one source has on this machine (a single video: only its own file in the shared folder)."""
    folder = LEARN / e["folder"]
    have = sorted(p for p in folder.glob("*.txt") if not p.name.startswith("_")) if folder.exists() else []
    return [p for p in have if p.stem == video_id(e["url"])] if kind == "youtube_videos" else have


def cmd_fetch(args):
    warn_if_unlocked()
    cfg = load(SOURCES)
    chosen = [(k, e) for k, e in all_sources(cfg) if not args.only or e["name"] == args.only]
    if not chosen:
        names = "\n  ".join(e["name"] for _, e in all_sources(cfg))
        print(f"No source is called {args.only!r}. Use one of these names exactly:\n  {names}")
        return 1
    import datetime
    skipped = load(skipped_file()) if skipped_file().exists() else {}

    def page(url, folder, e):
        try:
            got = fetch_page(url, folder, e["id_prefix"], f"{e['name']} (web)")
            why = None if got else "too little text on the page"
        except Exception as exc:  # one bad page must not stop the rest
            print(f"FAILED {url}: {exc}")
            why = f"failed: {str(exc)[:200]}"
        if why:
            skipped[url] = {"source": e["name"], "why": why, "date": datetime.date.today().isoformat()}
        else:
            skipped.pop(url, None)

    empty = []
    for kind, e in chosen:
        folder = LEARN / e["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        if kind == "youtube_channels":
            openwiki("youtube", "--channel", e["query"], "--folder", raw_folder_name(e["folder"]), root=RAW)
        elif kind == "youtube_videos":
            openwiki("youtube", e["url"], "--folder", raw_folder_name(e["folder"]), root=RAW)
        elif kind == "essay_sources":
            # OpenWiki finds the article links; ids come from the URL (not the title) so they never change.
            from openwiki.essays import fetch_url, parse_index
            links = [x["url"] for x in parse_index(fetch_url(e["index_url"]), e)]
            have = {header(f).get("source") for f in folder.glob("*.txt")}
            for url in links:
                if url not in have:
                    page(url, folder, e)
        elif kind == "pages":
            for url in e["urls"]:
                page(url, folder, e)
        elif kind == "github_repos":
            fetch_github(e, folder)
        if not entry_raw(kind, e):
            empty.append(e["name"])
    if skipped or skipped_file().exists():
        skipped_file().parent.mkdir(parents=True, exist_ok=True)
        skipped_file().write_text(json.dumps(skipped, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if empty:
        print(f"Nothing was fetched for: {'; '.join(empty)}. Skipped pages are listed in {skipped_file().relative_to(ROOT)}. "
              "Check the URL, or take the source off the list: python3 tools/wiki.py remove \"<name>\".")
        return 1
    return 0


# ---------------------------------------------------------------------------------------------- pending / status
def repo_path(raw):
    """The file's path inside its GitHub repository (fetch writes the blob URL into the header)."""
    m = re.search(r"/blob/[^/]+/(.+)$", header(raw).get("source") or header(raw).get("url") or "")
    return m.group(1) if m else raw.stem


def work_items(rows, cfg):
    """The args for .claude/workflows/learn-analyze.js. One item per video or article. The pages of one site, and the
    files of one folder of a GitHub repo, go to one agent, at most WORK_ITEM_MAX files per item."""
    by_folder = {e["folder"].split("/")[-1]: (k, e) for k, e in all_sources(cfg) if k != "youtube_videos"}
    groups = {}
    for r in rows:
        folder = r["raw"].split("/")[2]
        kind, e = by_folder.get(folder, (None, {}))
        if kind == "pages":
            key = folder
        elif kind == "github_repos":
            parent = repo_path(ROOT / r["raw"]).rpartition("/")[0]
            key = f"{e.get('id_prefix') or folder}-{slug(parent)}" if parent else f"{folder}-root"
        else:
            key = r["id"]
        groups.setdefault(key, {"a": r["authority"], "d": folder, "ids": []})["ids"].append(r["id"])
    items = []
    for key, g in groups.items():
        for n, i in enumerate(range(0, len(g["ids"]), WORK_ITEM_MAX)):
            items.append({"k": key if n == 0 else f"{key}-{n + 1}", "a": g["a"], "d": g["d"], "ids": g["ids"][i:i + WORK_ITEM_MAX]})
    return items


def cmd_pending(args):
    cfg = load(SOURCES)
    rows = []
    for p in raw_files():
        sid = source_id(p)
        if not (ANALYSIS / f"{sid}.json").exists():
            rows.append({"id": sid, "raw": str(p.relative_to(ROOT)), "authority": authority_of(p, cfg),
                         "media": str(p.with_suffix(".media.json").relative_to(ROOT)) if p.with_suffix(".media.json").exists() else None,
                         "title": header(p).get("title", sid)})
    if args.work_items:
        print(json.dumps({"root": str(ROOT), "items": work_items(rows, cfg)}, separators=(",", ":")))
        return
    print(json.dumps(rows, indent=1) if args.json else "\n".join(f"{r['id']}\t{r['authority']}\t{r['title']}" for r in rows))


def source_folders(cfg):
    """{source id: raw folder} for every id this repo knows, with or without its raw text on this machine: raw files
    first, then the wiki manifest (it records each page's raw path), then the id prefixes in sources.json."""
    out = {source_id(p): f"raw/{p.parent.name}" for p in raw_files()}
    for i, m in manifest_of_wiki().items():
        out.setdefault(i, "/".join(m.get("source_file", "").split("/")[:2]))
    prefixes = sorted(((e["id_prefix"], e["folder"]) for _, e in all_sources(cfg) if e.get("id_prefix")), key=lambda x: -len(x[0]))
    for aj in ANALYSIS.glob("*.json") if ANALYSIS.exists() else []:
        if aj.stem not in out:
            out[aj.stem] = next((f for p, f in prefixes if aj.stem.startswith(p + "-")), None)
    for e in cfg.get("youtube_videos", []):
        out[video_id(e["url"])] = e["folder"]
    return out


def source_ids(kind, e, folders):
    """The ids that belong to one source."""
    if kind == "youtube_videos":  # single videos share raw/videos: each owns only its own id
        return [video_id(e["url"])]
    return sorted(i for i, f in folders.items() if f == e["folder"])


def cmd_status(args):
    cfg = load(SOURCES)
    manifest, folders = manifest_of_wiki(), source_folders(cfg)
    rows = []
    for kind, e in all_sources(cfg):
        ids = source_ids(kind, e, folders)
        rows.append({"name": e["name"], "kind": kind, "authority": e.get("authority", "reference"), "folder": f"learn/{e['folder']}",
                     "id_prefix": e.get("id_prefix"), "urls": entry_urls(e),
                     "analysed": sum((ANALYSIS / f"{i}.json").exists() for i in ids),
                     "in_wiki": sum(i in manifest for i in ids), "raw_here": len(entry_raw(kind, e))})
    if args.json:
        print(json.dumps({"root": str(ROOT), "sources": rows}, indent=1, ensure_ascii=False))
        return 0
    print(f"{'source':44} {'authority':15} analysed  in wiki  raw here")
    for r in rows:
        print(f"{r['name'][:44]:44} {r['authority']:15} {r['analysed']:8}  {r['in_wiki']:7}  {r['raw_here']:8}")
    missing = [r["name"] for r in rows if r["analysed"] and not r["raw_here"]]
    if missing:
        print(f"\nRaw text not on this machine for {len(missing)} analysed sources ({some(missing)}). learn/raw/ is git-ignored, "
              "and the committed analyses are what the app uses. Fetch it again only to re-analyse or citation-check: "
              '.venv-wiki/bin/python tools/wiki.py fetch --only "<name>"')
    return 0


# ---------------------------------------------------------------------------------------------- ingest
def learn_section(a):
    """The OpenDesigner part of a source page: authority, rules, decisions, process, examples."""
    out = [MARK_START, "", "## For OpenDesigner", "", f"- Authority: **{a['authority']}**"]
    if a.get("caveats"):
        out += [f"- Caveat: {c}" for c in a["caveats"]]
    if a.get("rules"):
        out += ["", "### Rules and practices", ""]
        for r in a["rules"]:
            vals = f" Values: {', '.join(r['values'])}." if r.get("values") else ""
            out.append(f"- **{r['strength']}** ({r['area']}, {r.get('applies_to', 'all')}): {r['rule']} "
                       f"Why: {r['why']}{vals} [{r.get('evidence', '')}]")
    if a.get("decisions"):
        out += ["", "### Decisions it informs", ""]
        for d in a["decisions"]:
            q = f" (`{d['maps_to']}`)" if d.get("maps_to") else ""
            out.append(f"- {d['question']}{q}")
            out += [f"  - {o['name']}: {o['effect']}" + (f" When: {o['when']}" if o.get("when") else "") for o in d.get("options", [])]
            if d.get("recommendation"):
                out.append(f"  - Recommendation: {d['recommendation']}")
    if a.get("process"):
        out += ["", "### Process", ""]
        out += [f"{i}. {s['step']}: {s['detail']}" for i, s in enumerate(a["process"], 1)]
    if a.get("examples"):
        out += ["", "### Examples and visual references", ""]
        out += [f"- {x['what']}" + (f" ({x['where']})" if x.get("where") else "") + f": {x.get('visual_note', '')}" for x in a["examples"]]
    if a.get("numbers"):
        out += ["", "### Numbers", ""]
        out += [f"- {n['value']}: {n['context']} [{n.get('evidence', '')}]" for n in a["numbers"]]
    return "\n".join(out + ["", MARK_END, ""])


def analysis_changed(aj, entry):
    """True when a source's wiki page was built from a different analysis than the one on disk. Pages ingested before
    the manifest recorded analysis hashes fall back to comparing file times."""
    if not entry:
        return False
    if entry.get("analysis_hash"):
        return entry["analysis_hash"] != file_hash(aj)
    page = WIKI / entry.get("wiki_page", "x").removeprefix("wiki/")
    return not page.exists() or aj.stat().st_mtime > page.stat().st_mtime


def page_labels(text):
    """OpenWiki labels every source like a video. A web page or a repository file gets page labels instead."""
    if re.search(r"^url: https?://(www\.)?(youtube\.com|youtu\.be)/", text, re.M):
        return text
    return text.replace("\n- Video ID: `", "\n- Page ID: `", 1).replace("\n- Channel: ", "\n- Publisher: ", 1)


def cmd_ingest(args):
    warn_if_unlocked()
    from openwiki.textfmt import parse_source_file
    from openwiki.wiki import ingest_path, load_manifest, rebuild_index, save_manifest, source_stem
    from openwiki.workspace import Workspace
    ws = Workspace.resolve(LEARN)
    manifest = load_manifest(ws)
    by_id = {source_id(p): p for p in raw_files()}
    counts = {"processed": 0, "skipped": 0, "failed": 0, "no_raw": 0}
    for aj in sorted(ANALYSIS.glob("*.json")):
        a = load(aj)
        raw = by_id.get(aj.stem)
        if raw is None:
            counts["no_raw"] += 1
            continue
        # OpenWiki skips a raw file it has seen; an edited analysis must still rebuild the page.
        state = ingest_path(raw, ws, manifest, force=args.force or analysis_changed(aj, manifest.get(aj.stem)), analysis=a)
        counts[state] += 1
        if aj.stem in manifest:
            manifest[aj.stem]["analysis_hash"] = file_hash(aj)
        page = ws.sources_dir / f"{source_stem(parse_source_file(raw))}.md"
        if page.exists():
            text = page.read_text(encoding="utf-8")
            text = re.sub(re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n?", "", text, flags=re.S)
            text = text.replace("\ntags:", f"\nauthority: {a['authority']}\ntags:", 1) if "\nauthority:" not in text else text
            page.write_text(page_labels(text).rstrip("\n") + "\n\n" + learn_section(a), encoding="utf-8")
    save_manifest(ws, manifest)
    rebuild_index(ws)
    print(json.dumps(counts))
    openwiki("lint", "--fix-index")


# ---------------------------------------------------------------------------------------------- trace
TRACE = ROOT / "traces" / "L19-trace.md"
TIER = {"non-negotiable": "A (owner: non-negotiable)", "good-to-have": "A (owner: good to have)",
        "reference": "B (owner-vetted practitioner)"}
TRACE_HEAD = """# L19 (learning wiki) source trace

Append-only. One row per source analysed for the learning wiki, plus the ones that could not be read. `tools/wiki.py trace` appends new rows; S-ids never change.
Tiers: the owner marked Emil Kowalski's sources non-negotiable and Vaul good to have (both used as Tier A for the house standards), and vouched for the YouTube channels (Tier B: corroborate numbers).
Format: `| time | S-id | URL | publisher | published/updated date | tier | verdict (used/rejected/why) | what was taken |`

| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
"""


def cmd_trace(args):
    import datetime
    text = TRACE.read_text(encoding="utf-8") if TRACE.exists() else TRACE_HEAD
    logged = set(re.findall(r"\| (S-L19-\d+) \|.*<!-- (\S+) -->", text))
    by_src = {src: sid for sid, src in logged}
    nums = [int(s.split("-")[-1]) for s, _ in logged]
    nxt = max(nums, default=0) + 1
    cfg = load(SOURCES)
    now = datetime.datetime.now().isoformat(timespec="minutes")
    rows = []
    for p in raw_files():
        sid = source_id(p)
        aj = ANALYSIS / f"{sid}.json"
        if sid in by_src or not aj.exists():
            continue
        h, a = header(p), load(aj)
        url = h.get("url") or h.get("source", "")
        what = (f"{len(a['rules'])} rules, {len(a['decisions'])} decisions, {len(a['process'])} process steps, "
                f"{len(a['examples'])} examples; analysis `learn/analysis/{sid}.json`")
        pub = h.get("published", "unknown")[:10]
        rows.append(f"| {now} | S-L19-{nxt:03d} | {url} | {h.get('channel', '?').replace('|', '/')} | {pub} | "
                    f"{TIER[authority_of(p, cfg)]} | used | {what} | <!-- {sid} -->")
        by_src[sid] = f"S-L19-{nxt:03d}"
        nxt += 1
    for state in RAW.glob("*/_extract_state.json"):
        for vid in load(state).get("permanent_skip", []):
            if vid not in by_src:
                rows.append(f"| {now} | S-L19-{nxt:03d} | https://www.youtube.com/watch?v={vid} | {state.parent.name} (YouTube) | "
                            f"unknown | B (owner-vetted practitioner) | rejected: no captions available | nothing | <!-- {vid} -->")
                by_src[vid] = f"S-L19-{nxt:03d}"
                nxt += 1
    TRACE.write_text(text.rstrip("\n") + "\n" + "\n".join(rows) + ("\n" if rows else ""), encoding="utf-8")
    (LEARN / "sids.json").write_text(json.dumps(dict(sorted(by_src.items(), key=lambda kv: kv[1])), indent=1) + "\n", encoding="utf-8")
    print(f"{len(rows)} rows appended to {TRACE.relative_to(ROOT)}; learn/sids.json maps source ids to S-ids")


# ---------------------------------------------------------------------------------------------- standards
STANDARDS = ROOT / "synthesis" / "standards.json"
STD_FIELDS = {"id": str, "theme": str, "area": str, "title": str, "rule": str, "why": str, "strength": str,
              "values": dict, "applies_to": list, "sources": list, "design_md": bool, "conflicts": list}
# Optional fields: what a standard settles in the interview, and what it forbids (the shared schema in docs/KNOWLEDGE.md).
STD_OPTIONAL = {"settles": list, "breaks_options": dict, "constraints": list, "supersedes": list}
CONSTRAINT_KINDS = ("accelerating-curve", "max-duration-ms")


def standards_hash(doc):
    """Hash of what a project would feel: the standards and the retired list, not the metadata around them."""
    import hashlib
    body = json.dumps({"standards": doc.get("standards", []), "retired": doc.get("retired", [])}, sort_keys=True,
                      ensure_ascii=False, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


def constraint_kind(c):
    """(kind, params) of one constraint: {"path": P, "forbid": "accelerating-curve"}, or a kind with parameters,
    {"forbid": {"max-duration-ms": {"value": 300}}} (the parameters may also sit next to "forbid")."""
    f = c.get("forbid") if isinstance(c, dict) else None
    if isinstance(f, str):
        return f, {k: v for k, v in c.items() if k not in ("path", "forbid")}
    if isinstance(f, dict) and len(f) == 1:
        kind, params = next(iter(f.items()))
        return kind, params if isinstance(params, dict) else {"value": params}
    return None, {}


def engine_entries(s):
    eng = s.get("engine")
    return eng if isinstance(eng, list) else [eng] if eng else []


def check_standards(doc):
    errs = []
    ids = [s.get("id") for s in doc.get("standards", [])]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"duplicate ids: {sorted(dup)}")
    themes = {t["key"] for t in doc.get("themes", [])}
    retired = {r.get("id") for r in doc.get("retired", [])}
    questions = cards = None
    setters = {}
    for s in doc.get("standards", []):
        sid = s.get("id", "?")
        for f, t in STD_FIELDS.items():
            if not isinstance(s.get(f), t):
                errs.append(f"{sid}: missing or wrong type: {f}")
        for f, t in STD_OPTIONAL.items():
            if f in s and not isinstance(s[f], t):
                errs.append(f"{sid}: {f} must be a {t.__name__}")
        if s.get("strength") not in ("must", "should"):
            errs.append(f"{sid}: strength must be must or should")
        if themes and s.get("theme") not in themes:
            errs.append(f"{sid}: theme {s.get('theme')!r} not in themes")
        if sid in retired:
            errs.append(f"{sid}: listed as both active and retired")
        for tag in s.get("applies_to") or []:
            if tag not in TAGS:
                errs.append(f"{sid}: applies_to {tag!r} is not one of {', '.join(TAGS)}")
        for src in s.get("sources", []):
            if not (ANALYSIS / f"{src.get('id')}.json").exists():
                errs.append(f"{sid}: source {src.get('id')!r} has no learn/analysis file")
        for e in engine_entries(s):
            if not isinstance(e, dict) or not e.get("path") or "value" not in e:
                errs.append(f"{sid}: engine entries need path and value")
            else:
                setters.setdefault(e["path"], []).append((sid, json.dumps(e["value"], sort_keys=True)))
        rev = s.get("review")
        if rev:
            try:
                re.compile(rev.get("pattern", ""))
            except re.error as exc:
                errs.append(f"{sid}: review pattern does not compile ({exc})")
            if not rev.get("message"):
                errs.append(f"{sid}: review needs a message")
        for f in ("since", "changed"):
            if not isinstance(s.get(f), int) or s[f] > doc.get("version", 0):
                errs.append(f"{sid}: {f} must be a version number <= {doc.get('version')}")
        if isinstance(s.get("settles"), list) or isinstance(s.get("breaks_options"), dict):
            questions = question_ids() if questions is None else questions
            for q in s.get("settles") if isinstance(s.get("settles"), list) else []:
                if q not in questions:
                    errs.append(f"{sid}: settles {q!r}, which is not a question in skills/opendesigner/references/questions.json")
            for q, opts in (s.get("breaks_options") or {}).items() if isinstance(s.get("breaks_options"), dict) else []:
                if q not in questions:
                    errs.append(f"{sid}: breaks_options names {q!r}, which is not a question")
                elif not isinstance(opts, list) or not opts:
                    errs.append(f"{sid}: breaks_options[{q!r}] must be a list of option values")
                else:
                    errs += [f"{sid}: {q} has no option {o!r} (options: {', '.join(questions[q])})"
                             for o in opts if str(o) not in questions[q]]
        for c in s.get("constraints") if isinstance(s.get("constraints"), list) else []:
            kind, params = constraint_kind(c)
            if not isinstance(c, dict) or not isinstance(c.get("path"), str) or not c.get("path"):
                errs.append(f"{sid}: each constraint needs a token path, for example {{\"path\": \"motion.easing.*\", \"forbid\": \"accelerating-curve\"}}")
            elif kind not in CONSTRAINT_KINDS:
                errs.append(f"{sid}: constraint on {c['path']} forbids {c.get('forbid')!r}; the kinds are {', '.join(CONSTRAINT_KINDS)}")
            elif kind == "max-duration-ms" and (isinstance(params.get("value"), bool) or not isinstance(params.get("value"), (int, float))
                                                or params["value"] <= 0):
                errs.append(f"{sid}: constraint max-duration-ms on {c['path']} needs a positive number, "
                            "for example {\"max-duration-ms\": {\"value\": 300}}")
        if isinstance(s.get("supersedes"), list) and s["supersedes"]:
            if cards is None:
                cards = {c["id"] for c in load(CARDS)} if CARDS.exists() else set()
            for dc in s["supersedes"]:
                if dc not in cards:
                    errs.append(f"{sid}: supersedes {dc!r}, which is not a card in synthesis/cards.json")
    for path, who in setters.items():  # one token path, one value: 1 and 1.0 differ as JSON, and the engine compares JSON
        if len({v for _, v in who}) > 1:
            errs.append(f"{path} is set to different values: " + ", ".join(f"{i} {v}" for i, v in who))
    if doc.get("content_hash") != standards_hash(doc):
        errs.append("standards changed without a version bump: run python3 tools/wiki.py standards --bump \"what changed\"")
    return errs


def file_hash(path):
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def standard_substance(a):
    """What a standards synthesis reads from an analysis: rules, decisions and numbers without their evidence strings.
    A reviewer re-anchoring evidence to a verbatim phrase changes no standard, so it must not ask for a rebuild."""
    import hashlib
    strip = lambda items: [{k: v for k, v in x.items() if k != "evidence"} for x in items if isinstance(x, dict)]
    body = {"authority": a.get("authority"), "rules": strip(a.get("rules", [])), "decisions": strip(a.get("decisions", [])),
            "numbers": strip(a.get("numbers", []))}
    return "s:" + hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def standard_inputs():
    """The analyses a standards synthesis must cover: every non-negotiable and good-to-have source, with the hash of
    what the synthesis reads from it (standard_substance)."""
    out = {}
    for aj in sorted(ANALYSIS.glob("*.json")):
        try:
            a = load(aj)
        except json.JSONDecodeError:
            continue
        if a.get("authority") in ("non-negotiable", "good-to-have"):
            out[aj.stem] = standard_substance(a)
    return out


def head_standards():
    """synthesis/standards.json as committed at HEAD, or None when git or that commit cannot show it."""
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{STANDARDS.relative_to(ROOT).as_posix()}"],
                           capture_output=True, text=True)
    except OSError:
        return None
    if r.returncode:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def bump(doc, why, head):
    """Version a change to the standards, in place. Returns (message, exit code).
    - No history in the file: the first release. It keeps its version and gets one history entry; git is not needed.
    - Otherwise the change is measured against HEAD's file. Nothing changed (content hash): refused.
    - The file already has a version above HEAD's (a bump nobody committed yet): that history entry is amended,
      so two bumps before a commit record one change."""
    import datetime
    today = datetime.date.today().isoformat()
    if not doc.get("history"):
        v = max(doc.get("version") or 1, 1)
        for s in doc["standards"]:
            s["since"] = s["changed"] = v
        doc["history"] = [{"version": v, "date": today, "why": why, "added": [s["id"] for s in doc["standards"]],
                           "changed": [], "retired": [r.get("id") for r in doc.get("retired", [])]}]
        doc["version"], doc["updated"] = v, today
        doc["content_hash"] = standards_hash(doc)
        return f"standards v{v}: first release, {len(doc['standards'])} standards", 0
    if doc.get("content_hash") == standards_hash(doc):
        return (f"Nothing to bump: the standards have not changed since v{doc.get('version')} (the content hash matches). "
                "A bump records a change to a rule, a value, a check or the retired list."), 1
    if head is None:
        return ("Cannot bump: git could not show synthesis/standards.json at HEAD, and a bump measures the change against "
                "the last commit. Run it in the repository's git checkout, with git installed."), 1
    hv, cur = head.get("version", 0), doc.get("version", 0)
    if cur < hv:
        return f"Cannot bump: this file says v{cur}, but HEAD has v{hv}. Start from HEAD's file, then make the change again.", 1
    v, amend = hv + 1, cur > hv
    old = {s["id"]: s for s in head.get("standards", [])}
    strip = lambda s: {k: x for k, x in s.items() if k not in ("since", "changed")}
    added, changed = [], []
    for s in doc["standards"]:
        o = old.get(s["id"])
        if o is None:
            s["since"] = s["changed"] = v
            added.append(s["id"])
        elif strip(o) != strip(s):
            s["since"], s["changed"] = o.get("since", v), v
            changed.append(s["id"])
        else:
            s["since"], s["changed"] = o.get("since", v), o.get("changed", v)
    active = {s["id"] for s in doc["standards"]}
    gone = [i for i in old if i not in active]
    doc["retired"] = [r for r in doc.get("retired", []) if r.get("id") not in active]
    have = {r.get("id") for r in doc["retired"]}
    doc["retired"] += [{"id": i, "version": v, "why": why} for i in gone if i not in have]
    entry = {"version": v, "date": today, "why": why, "added": added, "changed": changed, "retired": gone}
    if amend:
        prev = next((h for h in doc["history"] if h.get("version") == cur), None)
        if prev and prev.get("why") and prev["why"] != why:
            entry["why"] = f"{prev['why']}; {why}"
    doc["history"] = [h for h in doc["history"] if h.get("version", 0) <= hv] + [entry]
    doc["version"], doc["updated"] = v, today
    doc["content_hash"] = standards_hash(doc)
    return (f"standards v{v}: {len(added)} added, {len(changed)} changed, {len(gone)} retired, compared with HEAD (v{hv})"
            + (f"; amended the uncommitted v{v} history entry" if amend else "")), 0


def cmd_standards(args):
    if not STANDARDS.exists():
        print("synthesis/standards.json does not exist yet")
        return 0
    doc = load(STANDARDS)
    if args.bump or args.built_from:
        code = 0
        if args.bump:
            msg, code = bump(doc, args.bump, head_standards())
            print(msg)
            if code:
                return code
        if args.built_from:  # the learn-standards merge: which analyses these standards were built from
            doc["built_from"] = standard_inputs()
            print(f"built_from: {len(doc['built_from'])} non-negotiable and good-to-have analyses recorded")
        STANDARDS.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if args.bump:
            print("Next: python3 tools/wiki.py cite-check --standards (needs JEV_API_KEY or TYPESAFE_API_KEY), then the "
                  f"learn-escalate workflow with {json.dumps({'root': str(ROOT)})} if it flags anything; python3 tools/build_data.py; "
                  "python3 tools/sync_skills.py; python3 tools/wiki.py map; a CHANGELOG line; commit.")
        return 0
    errs = check_standards(doc)
    for e in errs:
        print("ERROR", e)
    by_theme = {}
    for s in doc.get("standards", []):
        by_theme.setdefault(s["theme"], []).append(s)
    mapped = sum(1 for s in doc.get("standards", []) if s.get("engine"))
    checked = sum(1 for s in doc.get("standards", []) if s.get("review"))
    print(f"standards v{doc.get('version')}: {len(doc.get('standards', []))} in {len(by_theme)} themes, "
          f"{mapped} set tokens, {checked} have review checks, {len(doc.get('retired', []))} retired")
    print("standards: " + ("OK" if not errs else f"{len(errs)} errors"))
    return 1 if errs else 0


# ---------------------------------------------------------------------------------------------- cite-check (Jev)
JEV_API = "https://api.typesafe.ai/v1/systemone"
CITE_REPORT = WIKI / "synthesis" / "citation-check.md"
CITE_JSON = LEARN / "citation-check.json"
AUTO_ACCEPT = 0.8  # below this, a person or a reasoning model looks at the verdict


def jev_key():
    for k in ("JEV_API_KEY", "TYPESAFE_API_KEY"):
        if os.environ.get(k):
            return os.environ[k]
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.startswith(("JEV_API_KEY=", "TYPESAFE_API_KEY=")):
                return line.split("=", 1)[1].strip().strip("\"'")
    return None


def jev(state, questions):
    import urllib.request
    req = urllib.request.Request(JEV_API, method="POST",
                                 data=json.dumps({"state": state, "model": "jev-latest", "questions": questions}).encode(),
                                 headers={"Authorization": f"Bearer {jev_key()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["answers"]


CUE = re.compile(r"\[\d+:\d{2}(?::\d{2})?\]\s*")  # OpenWiki 0.3+ writes "[m:ss] text" per caption cue


def body_of(path):
    """The transcript or page text, with OpenWiki's per-cue timestamps removed so phrases that span cues still match."""
    text = path.read_text(encoding="utf-8", errors="replace")
    return CUE.sub("", text.split("TRANSCRIPT", 1)[-1])


def find_passage(body, rule, evidence, width=700):
    """Code finds the evidence; Jev only judges it. Try the evidence phrase, then the best keyword window."""
    flat = re.sub(r"\s+", " ", body)
    low = flat.lower()
    ev = re.sub(r"\s+", " ", CUE.sub("", evidence or "")).strip().strip(".").lower()
    parts = [p.strip(" .\"'") for p in re.split(r"\.\.\.|…|;|\s-\s", ev)]  # "A ... B" quotes two fragments
    for probe in [ev, ev[:60], ev[:30]] + sorted(parts, key=len, reverse=True):
        if len(probe) >= 12 and probe in low:
            i = low.index(probe)
            return flat[max(0, i - width // 3): i + width], "evidence found"
    terms = [t for t in re.findall(r"[a-z0-9.()-]{4,}", (rule + " " + (evidence or "")).lower())
             if t not in {"when", "with", "that", "this", "from", "into", "your", "they", "them", "should", "never", "always"}]
    if not terms:
        return flat[:width], "no evidence"
    step, best, at = 120, -1, 0
    for i in range(0, max(1, len(low) - width), step):
        win = low[i:i + width]
        score = sum(win.count(t) for t in set(terms))
        if score > best:
            best, at = score, i
    return flat[at:at + width], "keyword window"


def cmd_cite_check(args):
    if not jev_key():
        sys.exit("cite-check needs JEV_API_KEY or TYPESAFE_API_KEY (environment or .env)")
    by_id = {source_id(p): p for p in raw_files()}
    items = []
    if args.standards:
        # Each house standard against every source it cites: the rule a project will be held to must be in the source.
        for n, st in enumerate(load(STANDARDS).get("standards", [])):
            vals = [f"{k}: {v}" for k, v in (st.get("values") or {}).items()]
            for src in st.get("sources", []):
                raw = by_id.get(src.get("id"))
                if raw is None:
                    continue
                passage, how = find_passage(body_of(raw), st["rule"], src.get("evidence", ""))
                items.append({"source": f"{st['id']} <- {src['id']}", "n": n, "rule": st["rule"], "values": vals,
                              "strength": st["strength"], "passage": passage, "how": how})
        targets = []
    else:
        targets = [ANALYSIS / f"{i}.json" for i in args.ids] if args.ids else sorted(ANALYSIS.glob("*.json"))
    for aj in targets:
        a, raw = load(aj), by_id.get(aj.stem)
        if raw is None:
            continue
        body = body_of(raw)
        for n, r in enumerate(a.get("rules", [])):
            if r.get("strength") not in args.strength:
                continue
            passage, how = find_passage(body, r["rule"], r.get("evidence", ""))
            items.append({"source": aj.stem, "n": n, "rule": r["rule"], "values": r.get("values", []),
                          "strength": r["strength"], "passage": passage, "how": how})
    if args.limit:
        items = items[: args.limit]
    print(f"checking {len(items)} rules with Jev ({len(targets)} analysis files)", flush=True)
    criteria = {"supports": "The passage states the rule or clearly implies it, and any values in the rule match the passage",
                "contradicts": "The passage says the opposite, or gives different values",
                "unsupported": "The passage does not address the rule, or does not say enough to back it"}

    def judge(batch):
        state = {"items": [{"rule": x["rule"], "values": x["values"], "passage": x["passage"]} for x in batch]}
        qs = {f"q{j}": {"type": "choice", "instructions": f"How does `items[{j}].passage` (from a video transcript or an article) "
                        f"relate to the design rule `items[{j}].rule` and its `items[{j}].values`?", "criteria": criteria}
              for j in range(len(batch))}
        ans = jev(state, qs)
        return [dict(x, verdict=ans[f"q{j}"]["choice"], confidence=ans[f"q{j}"]["confidence"]) for j, x in enumerate(batch)]

    from concurrent.futures import ThreadPoolExecutor
    batches = [items[i:i + 8] for i in range(0, len(items), 8)]
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = [r for b in ex.map(judge, batches) for r in b]
    flagged = [r for r in results if r["verdict"] != "supports" or r["confidence"] < AUTO_ACCEPT]
    counts = {v: sum(r["verdict"] == v for r in results) for v in criteria}
    key = "standards" if args.standards else "results"
    old = load(CITE_JSON) if CITE_JSON.exists() else {}
    # A run over some ids updates those ids and keeps the rest; a full run replaces everything.
    keep = [r for r in old.get(key, []) if r["source"] not in {x["source"] for x in results}] if args.ids else []
    allres = keep + [{k: v for k, v in r.items() if k != "passage"} for r in results]  # passages are third-party text
    old.update({"model": "jev-latest", "auto_accept": AUTO_ACCEPT, key: allres})
    CITE_JSON.write_text(json.dumps(old, indent=1) + "\n", encoding="utf-8")
    if args.standards:
        bad = [r for r in allres if r["verdict"] != "supports" or r["confidence"] < AUTO_ACCEPT]
        print(json.dumps(counts), f"standards: {len(bad)} of {len(allres)} standard-source pairs flagged")
        for r in sorted(bad, key=lambda r: r["confidence"]):
            print(f"  {r['verdict']:12} {r['confidence']:.2f}  {r['source']}  ({r['how']})")
        return 0
    tot = {v: sum(r["verdict"] == v for r in allres) for v in criteria}
    fl = [r for r in allres if r["verdict"] != "supports" or r["confidence"] < AUTO_ACCEPT]
    lines = ["---", "type: synthesis", "title: Citation check", "tags:", "  - quality", "---", "",
             "# Citation check (Jev)", "",
             f"Every must/should rule in `learn/analysis/` was checked against the source passage its evidence points to. "
             f"Code finds the passage; TypeSafe's Jev judges whether it supports the rule. Verdicts below {AUTO_ACCEPT} confidence, "
             f"and every verdict other than *supports*, go to review. Run: `python3 tools/wiki.py cite-check`.", "",
             f"- Rules checked: {len(allres)}", *[f"- {k}: {v}" for k, v in tot.items()], f"- Flagged for review: {len(fl)}", "",
             "## Flagged", "", "| source | rule # | verdict | confidence | how the passage was found | rule |", "|---|---|---|---|---|---|"]
    lines += [f"| `{r['source']}` | {r['n']} | {r['verdict']} | {r['confidence']:.2f} | {r['how']} | {r['rule'].replace('|', '/')} |"
              for r in sorted(fl, key=lambda r: (r["verdict"] == "supports", r["confidence"]))]
    CITE_REPORT.parent.mkdir(parents=True, exist_ok=True)
    CITE_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(counts), f"flagged {len(flagged)} of {len(results)}; report: {CITE_REPORT.relative_to(ROOT)}")
    return 0


# ---------------------------------------------------------------------------------------------- map
MAP = LEARN / "MAP.md"
CARDS_DIR = WIKI / "synthesis" / "_cards"
AREA_TITLES = {"overview": "Direction and hierarchy", "color": "Color", "modes": "Light, dark and themes", "typography": "Text",
               "layout": "Spacing and layout", "shape": "Corners", "elevation": "Depth, shadows and effects", "motion": "Motion",
               "iconography": "Icons and imagery", "content": "Words", "components": "Components", "patterns": "Patterns and flows",
               "platforms": "Platforms and devices", "accessibility": "Accessibility", "tokens": "Tokens and code",
               "process": "Process, taste and tools"}


def topic_slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse_cards():
    """Decision Cards in learn/wiki/synthesis/_cards/*.md: id, title, area file, the Q-ids its Maps to names, withdrawn or not."""
    out = []
    for f in sorted(CARDS_DIR.glob("*.md")) if CARDS_DIR.exists() else []:
        for block in re.split(r"(?m)^(?=### DC-L19-)", f.read_text(encoding="utf-8"))[1:]:
            head = block.splitlines()[0]
            m = re.match(r"### (DC-L19-\d+):\s*(.+)", head)
            if not m:
                continue
            maps = re.search(r"\*\*Maps to:\*\*(.*)", block)
            out.append({"id": m.group(1), "title": m.group(2).strip(), "area": f.stem,
                        "q": sorted(set(re.findall(r"Q-[a-z]+-\d+", maps.group(1) if maps else ""))),
                        "withdrawn": "**Withdrawn:**" in block})
    return sorted(out, key=lambda c: int(c["id"].split("-")[-1]))


def render_map():
    cfg, tax = load(SOURCES), load(TAXONOMY)
    analyses = {aj.stem: load(aj) for aj in sorted(ANALYSIS.glob("*.json"))}
    by_auth = {}
    for a in analyses.values():
        by_auth[a["authority"]] = by_auth.get(a["authority"], 0) + 1
    topic_sources = {}
    for i, a in analyses.items():
        for t in a["topics"]:
            topic_sources.setdefault(t["name"], []).append(i)
    std = load(STANDARDS) if STANDARDS.exists() else {"standards": [], "themes": []}
    cards = parse_cards()
    impact = load(ROOT / "synthesis" / "impact.json").get("questions", {}) if (ROOT / "synthesis" / "impact.json").exists() else {}
    rules = sum(len(a["rules"]) for a in analyses.values())
    L = ["# Learning wiki map", "", "<!-- generated by python3 tools/wiki.py map; edit the sources, not this file -->", "",
         "Everything OpenDesigner has learned from the sources its owner trusts, and where each piece feeds the app. "
         "Start here when you want to understand a concept, check why the app does something, or improve an area. "
         "How the knowledge is made and updated: [README.md](README.md). How it may be used: [../docs/KNOWLEDGE.md](../docs/KNOWLEDGE.md). "
         "How to turn it into app changes: [IMPROVING.md](IMPROVING.md).", "",
         "## At a glance", "",
         f"- **Sources:** {len(analyses)} analysed ("
         + ", ".join(f"{n} {k}" for k, n in sorted(by_auth.items())) + f"), listed in [sources.json](sources.json); citations in "
         "[../traces/L19-trace.md](../traces/L19-trace.md).",
         f"- **Extracted:** {rules} rules, {sum(len(a['decisions']) for a in analyses.values())} decisions, "
         f"{sum(len(a['process']) for a in analyses.values())} process steps, {sum(len(a['examples']) for a in analyses.values())} examples "
         "([analysis/](analysis/), one file per source).",
         f"- **Wiki:** {len(list((WIKI / 'sources').glob('*.md')))} source pages, {len(list((WIKI / 'topics').glob('*.md')))} topics, "
         f"{len(list((WIKI / 'synthesis').glob('*.md')))} synthesis pages ([wiki/index.md](wiki/index.md)).",
         f"- **House standards:** {len(std['standards'])} rules in {len(std['themes'])} themes, version {std.get('version', '-')} "
         "([../synthesis/standards.json](../synthesis/standards.json)).",
         f"- **Decision Cards:** {len([c for c in cards if not c['withdrawn']])} in [wiki/synthesis/_cards/](wiki/synthesis/_cards/) "
         "(assembled into [../research/L19-learning-wiki.md](../research/L19-learning-wiki.md)).",
         f"- **Impact notes:** \"Now / As it grows\" for {len(impact)} high-impact questions ([../synthesis/impact.json](../synthesis/impact.json)).",
         "- **Process:** [Decide or ask](wiki/synthesis/decide-or-ask.md) · [Citation check](wiki/synthesis/citation-check.md) · "
         "[House standards](wiki/synthesis/house-standards.md)", "",
         "## Read by area", "",
         "Each topic page brings every source on that topic together: what they teach, where they agree and disagree, the standards "
         "that apply, and the questions it informs.", ""]
    areas = {}
    for t in tax["topics"]:
        areas.setdefault(t["od_area"], []).append(t["name"])
    std_by_area = {}
    for s_ in std["standards"]:
        std_by_area.setdefault(s_["area"], set()).add(s_["theme"])
    for area, names in areas.items():
        items = []
        for n in names:
            page = WIKI / "synthesis" / f"{topic_slug(n)}.md"
            cnt = len(topic_sources.get(n, []))
            items.append(f"[{n}](wiki/synthesis/{topic_slug(n)}.md) ({cnt})" if page.exists() else f"{n} ({cnt}, no page yet)")
        themes = sorted(std_by_area.get(area, []))
        L.append(f"- **{AREA_TITLES.get(area, area)}:** " + " · ".join(items)
                 + (f". Standards: " + ", ".join(f"[{th}](../skills/opendesigner/references/standards/{th}.md)" for th in themes) if themes else ""))
    L += ["", "## House standards", "",
          "Rules from non-negotiable sources. The app applies and locks them in every project; only the person can override one "
          "([../docs/KNOWLEDGE.md](../docs/KNOWLEDGE.md) section 2).", "",
          "| Theme | Rules | Must | Lock a value | Checked in code | Read |", "|---|---|---|---|---|---|"]
    for th in std["themes"]:
        ss = [x for x in std["standards"] if x["theme"] == th["key"]]
        L.append(f"| {th['title']} | {len(ss)} | {sum(x['strength'] == 'must' for x in ss)} | {sum(1 for x in ss if x.get('engine'))} | "
                 f"{sum(1 for x in ss if x.get('review'))} | [standards/{th['key']}.md](../skills/opendesigner/references/standards/{th['key']}.md) |")
    L += ["", "## Decision Cards", "", "Reference sources turned into decisions the interview can ask better. Each card says which question it improves.", ""]
    for area in dict.fromkeys(c["area"] for c in cards):
        cs = [c for c in cards if c["area"] == area]
        L += [f"### {area} ([_cards/{area}.md](wiki/synthesis/_cards/{area}.md))", ""]
        L += [f"- {'~~' if c['withdrawn'] else ''}{c['id']}: {c['title']}{'~~ (withdrawn)' if c['withdrawn'] else ''}"
              + (f" → {', '.join(c['q'])}" if c["q"] else "") for c in cs]
        L.append("")
    qs = {}
    for c in cards:
        if not c["withdrawn"]:
            for q in c["q"]:
                qs.setdefault(q, []).append(c["id"])
    L += ["## Questions this knowledge touches", "",
          "Before you change a question in `synthesis/QUESTIONNAIRE.md`, read the cards listed for it.", "",
          "| Question | Cards | Now / As it grows notes |", "|---|---|---|"]
    for q in sorted(set(qs) | set(impact), key=lambda q: (q.split("-")[1], int(q.split("-")[2]))):
        L.append(f"| {q} | {', '.join(qs.get(q, [])) or '-'} | {'yes' if q in impact else '-'} |")
    L += ["", "## Where each part lands in the app", "",
          "| Knowledge | Becomes | Built by | The app uses it in |", "|---|---|---|---|",
          "| Non-negotiable sources | `synthesis/standards.json` | the `learn-standards` workflow, `wiki.py standards --bump` | `engine.py init` (locked values), `review` (code checks), DESIGN.md, `references/standards/` |",
          "| Reference sources | Decision Cards, topic pages | the `learn-synthesis` workflow | `research/L19-learning-wiki.md` → `cards/L19.json` (\"why?\" answers), proposed questionnaire changes (Part B) |",
          "| Impact notes | `synthesis/impact.json` | the `learn-synthesis` workflow (process step) | `references/questions.json` and stage files: Now / As it grows under each option |",
          "| Process pages | `wiki/synthesis/decide-or-ask.md` | the `learn-synthesis` workflow | `rules.md` section 6, \"Decide or ask\" |",
          "| Everything | `learn/wiki/` | `wiki.py ingest`, `map` | people and agents reading, `jev_nav.py find` (standards) |", ""]
    return "\n".join(L)


def cmd_map(args):
    text = render_map()
    if args.check:
        ok = MAP.exists() and MAP.read_text(encoding="utf-8") == text
        print("map: " + ("up to date" if ok else "stale: run python3 tools/wiki.py map"))
        return 0 if ok else 1
    MAP.write_text(text, encoding="utf-8")
    print(f"wrote {MAP.relative_to(ROOT)}")
    return 0


# ---------------------------------------------------------------------------------------------- proposals
QUESTIONNAIRE = ROOT / "synthesis" / "QUESTIONNAIRE.md"
PROP_START, PROP_END = "<!-- od:l19-proposals -->", "<!-- /od:l19-proposals -->"


def render_proposals():
    """The 'Not asked' block for learning-wiki cards no question has adopted yet (they are proposals until reviewed)."""
    qj = ROOT / "synthesis" / "questionnaire.json"
    adopted = set()
    if qj.exists():
        for q in load(qj).get("questions", []):
            adopted |= set(q.get("decides") or [])
    pending = [c for c in parse_cards() if c["id"] not in adopted]
    rows = [f"| {c['id']} | {'Withdrawn: ' if c['withdrawn'] else ''}{c['title'].replace('|', '/')} | {', '.join(c['q']) or 'new question'} |"
            for c in pending]
    return "\n".join([PROP_START, "## Not asked: learning-wiki proposals (lane L19, pending review)", "",
                      "Decision Cards from the learning wiki (`research/L19-learning-wiki.md`) that no question has adopted yet. Each one "
                      "proposes a change to the questions it maps to; `learn/IMPROVING.md` section 3 says how to adopt one, and adopting "
                      "it (citing it in a question's cards) removes it from this table. Generated by `python3 tools/wiki.py proposals`.", "",
                      "| Card | What it proposes | Maps to |", "|---|---|---|", *rows, PROP_END])


def cmd_proposals(args):
    text = QUESTIONNAIRE.read_text(encoding="utf-8")
    block = render_proposals()
    new = (re.sub(re.escape(PROP_START) + r".*?" + re.escape(PROP_END), lambda m: block, text, flags=re.S)
           if PROP_START in text else text.rstrip("\n") + "\n\n" + block + "\n")
    if args.check:
        print("proposals: " + ("up to date" if new == text else "stale: run python3 tools/wiki.py proposals"))
        return 0 if new == text else 1
    QUESTIONNAIRE.write_text(new, encoding="utf-8")
    print(f"{block.count(chr(10) + '| DC-L19')} pending proposals listed in {QUESTIONNAIRE.relative_to(ROOT)}; "
          "next: python3 tools/build_questionnaire.py && python3 tools/build_data.py")
    return 0


# ---------------------------------------------------------------------------------------------- flagged
REVIEW_LOG = LEARN / "citation-review.json"


def text_hash(t):
    import hashlib
    return hashlib.sha256((t or "").encode("utf-8")).hexdigest()[:12]


def reviewed_keys():
    """Items a person or reasoning agent already reviewed, keyed to the exact text they reviewed: an edit re-opens them."""
    if not REVIEW_LOG.exists():
        return set()
    return {(r["kind"], r["id"], r.get("source", ""), r["hash"]) for r in load(REVIEW_LOG).get("reviewed", [])
            if r.get("decision") in ("confirmed", "fixed")}


def cmd_review_log(args):
    """Record review decisions (JSON list on stdin: [{item, decision, note}], as learn-escalate returns them)."""
    import datetime
    items = json.load(sys.stdin)
    if isinstance(items, dict):
        items = items.get("items", [])
    log = load(REVIEW_LOG) if REVIEW_LOG.exists() else {"$comment": "Citation-check items a reviewer settled (tools/wiki.py review-log). "
                                                                     "`wiki.py flagged` skips them while the reviewed text is unchanged.",
                                                         "reviewed": []}
    std = {x["id"]: x for x in load(STANDARDS).get("standards", [])} if STANDARDS.exists() else {}
    added = 0
    for it in items:
        m_std = re.match(r"(STD-[\w-]+?-\d+)\s+vs\s+(\S+)", it["item"])
        m_rule = re.match(r"(\S+)\s+rule\s+(\d+)", it["item"])
        if m_std and m_std.group(1) in std:
            rec = {"kind": "standard", "id": m_std.group(1), "source": m_std.group(2), "hash": text_hash(std[m_std.group(1)]["rule"])}
        elif m_rule and (ANALYSIS / f"{m_rule.group(1)}.json").exists():
            rules = load(ANALYSIS / f"{m_rule.group(1)}.json")["rules"]
            n = int(m_rule.group(2))
            if n >= len(rules):
                continue
            rec = {"kind": "rule", "id": m_rule.group(1), "source": str(n), "hash": text_hash(rules[n]["rule"])}
        else:
            print(f"skipped (not recognised): {it['item'][:80]}")
            continue
        rec.update({"decision": it["decision"], "note": it.get("note", "")[:300], "date": datetime.date.today().isoformat()})
        log["reviewed"] = [r for r in log["reviewed"] if (r["kind"], r["id"], r.get("source")) != (rec["kind"], rec["id"], rec["source"])] + [rec]
        added += 1
    REVIEW_LOG.write_text(json.dumps(log, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"recorded {added} review decisions in {REVIEW_LOG.relative_to(ROOT)}")


def raw_path_of(sid, folders):
    """Where a source's raw text lives, relative to the repo (it may not be on this machine: learn/raw/ is git-ignored)."""
    f = folders.get(sid)
    return f"learn/{f}/{sid}.txt" if f else None


def flagged_items():
    """What the citation check left for review: {"rules": [...], "standards": [...]}, each with the raw file to read."""
    c = load(CITE_JSON)
    done = reviewed_keys()
    folders = source_folders(load(SOURCES))
    rules = [{"source": r["source"], "n": r["n"], "rule": r["rule"][:200], "verdict": r["verdict"], "confidence": r["confidence"],
              "raw": raw_path_of(r["source"], folders)}
             for r in c.get("results", []) if (r["verdict"] != "supports" or r["confidence"] < AUTO_ACCEPT)
             and ("rule", r["source"], str(r["n"]), text_hash(r["rule"])) not in done]
    std_rule = {x["id"]: x["rule"] for x in load(STANDARDS).get("standards", [])} if STANDARDS.exists() else {}
    by = {}
    for x in c.get("standards", []):
        by.setdefault(x["source"].split(" <- ")[0], []).append(x)
    std = []
    for sid, xs in by.items():  # a standard stands if one cited source confidently supports it; any contradiction is reviewed
        if not any(x["verdict"] == "supports" and x["confidence"] >= AUTO_ACCEPT for x in xs) or any(x["verdict"] == "contradicts" for x in xs):
            w = sorted(xs, key=lambda x: (x["verdict"] == "supports", x["confidence"]))[0]
            if ("standard", sid, w["source"].split(" <- ")[1], text_hash(std_rule.get(sid))) in done:
                continue
            src = w["source"].split(" <- ")[1]
            std.append({"std": sid, "source": src, "verdict": w["verdict"], "confidence": w["confidence"], "raw": raw_path_of(src, folders)})
    return {"rules": rules, "standards": std}


def cmd_flagged(args):
    """What the citation check left for review, as the args of .claude/workflows/learn-escalate.js."""
    if not CITE_JSON.exists():
        sys.exit("no learn/citation-check.json yet: run python3 tools/wiki.py cite-check first")
    f = flagged_items()
    print(json.dumps(f, separators=(",", ":")) if args.json
          else f"{len(f['rules'])} analysis rules and {len(f['standards'])} standards need review (python3 tools/wiki.py flagged --json)")


# ---------------------------------------------------------------------------------------------- next
def synthesis_areas():
    """{area key: topic names} of the learn-synthesis workflow (its AREAS list is the one place that mapping lives)."""
    js = ROOT / ".claude" / "workflows" / "learn-synthesis.js"
    text = js.read_text(encoding="utf-8") if js.exists() else ""
    return {k: re.findall(r"'([^']*)'", topics)
            for k, topics in re.findall(r"\{ key: '([\w-]+)', start: \d+, topics: \[([^\]]*)\]", text)}


def workflow(name, args):
    return f"run the saved workflow {name} (.claude/workflows/{name}.js) with args {json.dumps(args, separators=(',', ':'))}"


def pipeline_state():
    """What is out of date, in pipeline order. Each item: (step, why, command). Real work comes first; the last item,
    step "raw", only notes analysed sources whose raw text is not on this machine."""
    cfg, todo = load(SOURCES), []
    root = {"root": str(ROOT)}
    problems, _, _ = analysis_problems(cfg)
    for name, err, fix in problems:  # a broken analysis poisons every later step, so it comes first
        todo.append(("check", f"learn/analysis/{name}: {err}", fix))
    by_id = {source_id(p): p for p in raw_files()}
    folders = source_folders(cfg)
    analyses = {}
    for aj in sorted(ANALYSIS.glob("*.json")):
        try:
            analyses[aj.stem] = (aj, load(aj))
        except json.JSONDecodeError:
            continue
    skipped = load(skipped_file()) if skipped_file().exists() else {}
    no_raw = []
    for kind, e in all_sources(cfg):
        if entry_raw(kind, e):
            continue
        if any(i in analyses for i in source_ids(kind, e, folders)):
            no_raw.append(e["name"])  # already learned from; the raw text is only needed to redo or re-check it
            continue
        bad = [f"{u} ({skipped[u]['why']}, {skipped[u].get('date', '')})" for u in entry_urls(e) if u in skipped]
        if bad:
            todo.append(("fetch", f"{e['name']}: fetched, but nothing usable came back: {some(bad, 3)}",
                         f'check the URL; to drop it: python3 tools/wiki.py remove "{e["name"]}"'))
        else:
            todo.append(("fetch", f"{e['name']}: nothing fetched yet", f'.venv-wiki/bin/python tools/wiki.py fetch --only "{e["name"]}"'))
    pending = [i for i in by_id if not (ANALYSIS / f"{i}.json").exists()]
    if pending:
        todo.append(("analyse", f"{len(pending)} fetched sources have no analysis ({some(pending, 5)})",
                     "run the saved workflow learn-analyze (.claude/workflows/learn-analyze.js) with args = the output of: "
                     "python3 tools/wiki.py pending --work-items"))
    manifest = manifest_of_wiki()
    not_ingested = [i for i in analyses if i in by_id and i not in manifest]
    stale_pages = [i for i, (aj, _) in analyses.items() if i in by_id and analysis_changed(aj, manifest.get(i))]
    if not_ingested or stale_pages:
        todo.append(("ingest", f"{len(not_ingested)} analyses not in the wiki, {len(stale_pages)} wiki pages built from an older analysis",
                     ".venv-wiki/bin/python tools/wiki.py ingest"))
    sids = load(LEARN / "sids.json") if (LEARN / "sids.json").exists() else {}
    untraced = [i for i in analyses if i not in sids]
    if untraced:
        todo.append(("trace", f"{len(untraced)} analyses have no S-L19 id yet", "python3 tools/wiki.py trace"))
    if STANDARDS.exists():
        doc = load(STANDARDS)
        built, now = doc.get("built_from", {}), standard_inputs()
        new = [i for i in now if i not in built]
        changed = [i for i in now if i in built and built[i] != now[i]]
        if new or changed:
            todo.append(("standards", f"standards were built before {len(new)} new and {len(changed)} changed non-negotiable/good-to-have "
                         f"analyses ({some(new + changed)})", workflow("learn-standards", root) + '; it ends with python3 tools/wiki.py '
                         'standards --built-from. Then: python3 tools/wiki.py standards --bump "<what changed>"'))
        if doc.get("content_hash") != standards_hash(doc):
            todo.append(("standards", "synthesis/standards.json was edited without a version bump",
                         'python3 tools/wiki.py standards --bump "<what changed>"'))
    elif standard_inputs():
        todo.append(("standards", "non-negotiable sources are analysed but synthesis/standards.json does not exist",
                     workflow("learn-standards", root)))
    used = set()
    l19 = ROOT / "research" / "L19-learning-wiki.md"
    cited = set(re.findall(r"S-L19-\d+", l19.read_text(encoding="utf-8"))) if l19.exists() else set()
    for page in (WIKI / "synthesis").glob("*.md"):
        m = re.search(r"^sources:\n((?:\s+- .+\n)+)", page.read_text(encoding="utf-8"), re.M)
        used |= set(re.findall(r"- (\S+)", m.group(1))) if m else set()
    unused = [i for i, (_, a) in analyses.items() if a.get("authority") == "reference" and i not in used and sids.get(i) not in cited]
    if unused:
        topics = {t.get("name") for i in unused for t in analyses[i][1].get("topics", []) if isinstance(t, dict)}
        areas = [k for k, names in synthesis_areas().items() if topics & set(names)] or "all"
        todo.append(("synthesis", f"{len(unused)} reference sources feed no Decision Card or topic page yet ({some(unused)})",
                     workflow("learn-synthesis", {**root, "topics": areas, "cards": areas, "verify": areas, "process": False, "merge": True})))
    if CITE_JSON.exists():
        # A rule needs a (new) check when its text is not the text Jev judged: an edit elsewhere in the file does not.
        checked = {(r["source"], r["n"]): r["rule"] for r in load(CITE_JSON).get("results", [])}
        unchecked = lambda i, a: any(isinstance(r, dict) and r.get("strength") in ("must", "should") and checked.get((i, n)) != r.get("rule")
                                     for n, r in enumerate(a.get("rules", [])))
        newer = [i for i, (aj, a) in analyses.items() if i in by_id and unchecked(i, a)]
        if newer:
            key = "" if jev_key() else " (it needs JEV_API_KEY or TYPESAFE_API_KEY in the environment or .env; none is set here)"
            todo.append(("cite-check", f"{len(newer)} analyses not citation-checked since they changed",
                         "python3 tools/wiki.py cite-check " + " ".join(newer[:20]) + key))
        f = flagged_items()
        if f["rules"] or f["standards"]:
            todo.append(("escalate", f"the citation check flagged {len(f['rules'])} analysis rules and {len(f['standards'])} standards "
                         "for review", workflow("learn-escalate", root)))
    if CARDS_DIR.exists() and QUESTIONNAIRE.exists():
        q = QUESTIONNAIRE.read_text(encoding="utf-8")
        cur = re.search(re.escape(PROP_START) + r".*?" + re.escape(PROP_END), q, re.S)
        if not cur or cur.group(0) != render_proposals():
            todo.append(("proposals", "the pending-proposals table in synthesis/QUESTIONNAIRE.md is out of date",
                         "python3 tools/wiki.py proposals && python3 tools/build_questionnaire.py && python3 tools/build_data.py"))
    if MAP.exists() and MAP.read_text(encoding="utf-8") != render_map():
        todo.append(("map", "learn/MAP.md is out of date", "python3 tools/wiki.py map"))
    for tool, why in (("build_data.py", "the skills' references are older than synthesis/"), ("sync_skills.py", "the skill copies differ from skills/")):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / tool), "--check"], capture_output=True, text=True)
        if r.returncode:
            said = (r.stdout.strip().splitlines() or r.stderr.strip().splitlines() or [""])[0][:160]
            todo.append(("build", why + (f" ({said})" if said else ""), f"python3 tools/{tool}"))
    if LOCK.exists():
        inst = installed_openwiki()
        if inst and inst.get("commit") != load(LOCK)["commit"]:
            todo.append(("openwiki", "the installed OpenWiki is not the tested commit", ".venv-wiki/bin/python tools/wiki.py upstream --upgrade"))
    if no_raw:
        todo.append(("raw", f"raw text is not on this machine for {len(no_raw)} analysed sources ({some(no_raw, 3)}). Nothing to do unless "
                     "you re-analyse or citation-check them: learn/raw/ is git-ignored",
                     '.venv-wiki/bin/python tools/wiki.py fetch --only "<name>"'))
    return todo


def cmd_next(args):
    todo = pipeline_state()
    work = [t for t in todo if t[0] != "raw"]
    if not work:
        print("Everything is up to date: sources fetched, analysed, in the wiki, traced, synthesised and built.")
    for step, why, cmd in todo:
        print(f"[{step}] {why}\n    -> {cmd}")
    return 1 if args.strict and work else 0


# ---------------------------------------------------------------------------------------------- upstream (OpenWiki)
LOCK = LEARN / "openwiki.lock.json"
OPENWIKI_REPO = "https://github.com/ckryptickunal/OpenWiki"
# The OpenWiki modules this tool calls. A change to one of them is worth reading before upgrading.
USED_MODULES = ("openwiki/essays.py", "openwiki/textfmt.py", "openwiki/wiki.py", "openwiki/workspace.py",
                "openwiki/cli.py", "openwiki/youtube.py", "openwiki/lint.py")


def installed_openwiki():
    from importlib import metadata
    try:
        dist = metadata.distribution("openwiki-cli")
    except metadata.PackageNotFoundError:
        return None
    direct = dist.read_text("direct_url.json")
    return {"version": dist.version, "commit": json.loads(direct).get("vcs_info", {}).get("commit_id") if direct else None}


def remote_head():
    out = subprocess.run(["git", "ls-remote", OPENWIKI_REPO + ".git", "HEAD"], capture_output=True, text=True, timeout=60)
    return out.stdout.split()[0] if out.returncode == 0 and out.stdout else None


def compare(base, head):
    """New commits and changed files between two OpenWiki commits (GitHub API; best effort)."""
    import urllib.request
    api = OPENWIKI_REPO.replace("https://github.com/", "https://api.github.com/repos/") + f"/compare/{base}...{head}"
    try:
        with urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": "opendesigner-wiki"}), timeout=30) as r:
            data = json.load(r)
    except Exception as exc:
        return {"error": str(exc), "commits": [], "files": []}
    return {"commits": [f"{c['sha'][:7]} {c['commit']['message'].splitlines()[0]}" for c in data.get("commits", [])],
            "files": [f["filename"] for f in data.get("files", [])]}


def warn_if_unlocked():
    """fetch and ingest call this: the installed OpenWiki should be the tested one."""
    if not LOCK.exists():
        return
    inst, lock = installed_openwiki(), load(LOCK)
    if inst is None:
        sys.exit(f"OpenWiki is not installed here. Run: {sys.executable} -m pip install "
                 f"\"git+{OPENWIKI_REPO}.git@{lock['commit']}\" (or use .venv-wiki/bin/python)")
    if inst.get("commit") != lock["commit"]:
        print(f"note: installed OpenWiki {str(inst.get('commit'))[:7]} is not the tested commit {lock['commit'][:7]} "
              f"(learn/openwiki.lock.json). Run: tools/wiki.py upstream --upgrade", file=sys.stderr)


def run_tests(openwiki_commit):
    """OpenWiki's own suite at that commit, then ours with the integration tests enabled."""
    results = {}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["git", "clone", "-q", OPENWIKI_REPO + ".git", tmp], check=True)
        subprocess.run(["git", "-C", tmp, "checkout", "-q", openwiki_commit], check=True)
        r = subprocess.run([sys.executable, "-m", "pytest", "-o", "addopts=", "-q", "-m", "not live"], cwd=tmp, capture_output=True, text=True)
        results["openwiki"] = (r.returncode == 0, (r.stdout.strip().splitlines() or ["no output"])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "test_wiki.py")], capture_output=True, text=True)
    results["opendesigner"] = (r.returncode == 0, (r.stderr.strip().splitlines() or ["no output"])[-1])
    return results


def cmd_upstream(args):
    import datetime
    lock = load(LOCK) if LOCK.exists() else {"commit": None}
    inst, head = installed_openwiki(), remote_head()
    print(f"tested (learn/openwiki.lock.json): {str(lock.get('commit'))[:7]}  {lock.get('version', '')}  {lock.get('tested', '')}")
    print(f"installed here:                    {str((inst or {}).get('commit'))[:7]}  {(inst or {}).get('version', 'not installed')}")
    print(f"OpenWiki on GitHub (HEAD):         {str(head)[:7]}")
    if head is None:
        sys.exit("could not reach GitHub")
    if head == lock.get("commit"):
        print("up to date")
        return 0
    diff = compare(lock["commit"], head) if lock.get("commit") else {"commits": [], "files": []}
    for c in diff["commits"]:
        print(f"  new: {c}")
    touched = [f for f in diff["files"] if f in USED_MODULES]
    if touched:
        print("  changed modules this repo calls: " + ", ".join(touched))
    if not args.upgrade:
        print("OpenWiki moved. To test and adopt it: .venv-wiki/bin/python tools/wiki.py upstream --upgrade")
        return 1 if args.strict else 0
    pip = [sys.executable, "-m", "pip", "install", "-q", "--upgrade"]
    subprocess.run(pip + [f"git+{OPENWIKI_REPO}.git@{head}", "pytest"], check=True)
    results = run_tests(head)
    for name, (ok, last) in results.items():
        print(f"  tests {name}: {'pass' if ok else 'FAIL'} ({last})")
    if all(ok for ok, _ in results.values()):
        ver = installed_openwiki()["version"]
        LOCK.write_text(json.dumps({"repo": OPENWIKI_REPO, "commit": head, "version": ver,
                                    "tested": datetime.date.today().isoformat(),
                                    "tests": {k: v[1] for k, v in results.items()},
                                    "commits_adopted": diff["commits"]}, indent=2) + "\n", encoding="utf-8")
        print(f"adopted OpenWiki {head[:7]} ({ver}); learn/openwiki.lock.json updated. Commit it with a note on what changed.")
        return 0
    if lock.get("commit"):
        subprocess.run(pip + [f"git+{OPENWIKI_REPO}.git@{lock['commit']}"], check=True)
    print("tests failed: reinstalled the tested commit. Fix tools/wiki.py for the new OpenWiki, then run --upgrade again.")
    return 1


# ---------------------------------------------------------------------------------------------- check
REQUIRED = {"summary": str, "key_ideas": list, "entities": list, "topics": list, "claims": list, "quotes": list,
            "tags": list, "authority": str, "rules": list, "decisions": list, "process": list, "examples": list}
OPTIONAL = {"numbers": list, "caveats": list}   # a string here would be rendered one line per character


def check_analysis(a, topics, questions=None):
    """(errors, notes) for one analysis. questions: {Q-id: option values}, for maps_to (default: the skill's questions.json)."""
    errs, notes = [], []
    for k, t in REQUIRED.items():
        if not isinstance(a.get(k), t):
            errs.append(f"missing or wrong type: {k}")
    for k, t in OPTIONAL.items():
        if k in a and not isinstance(a[k], t):
            errs.append(f"{k} must be a list, not a {type(a[k]).__name__}")
    if errs:
        return errs, notes
    questions = question_ids() if questions is None else questions
    if a["authority"] not in AUTHORITY:
        errs.append(f"authority {a['authority']!r}")
    if len(a["quotes"]) > QUOTE_MAX:
        errs.append(f"{len(a['quotes'])} quotes (max {QUOTE_MAX})")
    for q in a["quotes"]:
        if not isinstance(q, str):
            errs.append(f"quotes must be strings: {str(q)[:40]}")
        elif len(q.split()) > QUOTE_MAX_WORDS:
            errs.append(f"quote over {QUOTE_MAX_WORDS} words: {q[:40]}...")
    for t in a["topics"]:
        if not isinstance(t, dict):
            errs.append(f"topics must be objects with a name: {str(t)[:40]}")
        elif t.get("name") not in topics and not t.get("new"):
            errs.append(f"topic not in taxonomy: {t.get('name')!r} (copy a name exactly, or mark it new)")
        elif t.get("new"):
            notes.append(f"proposed topic: {t.get('name')}")
    for c in a.get("caveats", []):
        if not isinstance(c, str):
            errs.append(f"caveats must be strings: {str(c)[:40]}")
    for n in a.get("numbers", []):
        if not isinstance(n, dict) or not isinstance(n.get("value"), (str, int, float)) or not isinstance(n.get("context"), str):
            errs.append(f"numbers need a value and a context: {str(n)[:60]}")
    for r in a["rules"]:
        if not isinstance(r, dict):
            errs.append(f"rules must be objects: {str(r)[:60]}")
            continue
        for f in ("rule", "why", "strength", "area"):
            if not r.get(f):
                errs.append(f"rule without {f}: {str(r)[:60]}")
        if r.get("strength") not in ("must", "should", "consider"):
            errs.append(f"rule strength {r.get('strength')!r}")
        if r.get("area") and r["area"] not in RULE_AREAS:
            errs.append(f"rule area {r['area']!r} is not one of {', '.join(RULE_AREAS)}")
        if r.get("kind") is not None and r["kind"] not in ("do", "dont"):
            errs.append(f"rule kind {r['kind']!r} (do or dont)")
        tags = r.get("applies_to", "all")
        for tag in tags if isinstance(tags, list) else [tags]:
            if tag not in TAGS:
                errs.append(f"rule applies_to {tag!r} is not one of {', '.join(TAGS)}")
        if "values" in r and (not isinstance(r["values"], list) or not all(isinstance(v, (str, int, float)) for v in r["values"])):
            errs.append(f"rule values must be a list of strings: {str(r.get('values'))[:60]}")
    for d in a["decisions"]:
        if not isinstance(d, dict):
            errs.append(f"decisions must be objects: {str(d)[:60]}")
            continue
        if not d.get("question") or not d.get("options"):
            errs.append(f"decision without question/options: {str(d)[:60]}")
        elif not isinstance(d["options"], list) or not all(isinstance(o, dict) and o.get("name") for o in d["options"]):
            errs.append(f"decision options must be objects with a name: {str(d['options'])[:60]}")
        m = d.get("maps_to")
        if m is not None and (not isinstance(m, str) or (questions and m not in questions)):
            errs.append(f"maps_to {m!r} is not a question id in skills/opendesigner/references/questions.json")
    return errs, notes


def authority_of_id(sid, cfg, folders):
    """What sources.json says a source id's authority is, with or without its raw text on this machine."""
    for e in cfg.get("youtube_videos", []):
        if video_id(e["url"]) == sid:
            return e.get("authority", "reference")
    return authority_by_folder(cfg).get(folders.get(sid), "reference") if folders.get(sid) else None


def name_of_folder(cfg, folder):
    return next((e["name"] for k, e in all_sources(cfg) if k != "youtube_videos" and e["folder"] == folder), None)


def analysis_problems(cfg=None):
    """Every error in learn/analysis/, each with the command or edit that fixes it: [(file, error, fix)], notes, raw count."""
    cfg = cfg or load(SOURCES)
    topics = {t["name"] for t in load(TAXONOMY)["topics"]}
    questions, folders = question_ids(), source_folders(cfg)
    raw_ids = {source_id(p) for p in raw_files()}
    problems, notes = [], []
    for aj in sorted(ANALYSIS.glob("*.json")):
        edit = f"fix learn/analysis/{aj.name} (learn/README.md, \"The analysis schema\"), then python3 tools/wiki.py check"
        try:
            a = load(aj)
        except json.JSONDecodeError as exc:
            problems.append((aj.name, f"bad JSON ({exc})", f"fix the JSON syntax in learn/analysis/{aj.name}"))
            continue
        errs, ns = check_analysis(a, topics, questions)
        notes += [(aj.name, n) for n in ns]
        for e in errs:
            fix = edit
            if e.startswith("topic not in taxonomy"):
                fix = f"copy a topic name exactly from learn/taxonomy.json, or add \"new\": true, in learn/analysis/{aj.name}"
            elif e.startswith("maps_to"):
                fix = f"set maps_to to a question id from skills/opendesigner/references/questions.json, or null, in learn/analysis/{aj.name}"
            elif "quote" in e:
                fix = f"shorten or drop quotes in learn/analysis/{aj.name} (at most {QUOTE_MAX}, each {QUOTE_MAX_WORDS} words or fewer)"
            problems.append((aj.name, e, fix))
        want = authority_of_id(aj.stem, cfg, folders)
        if want and a.get("authority") != want:
            # The authority decides how completely rules are extracted, so the analysis is redone, not relabelled.
            item = {"k": aj.stem, "a": want, "d": folders[aj.stem].removeprefix("raw/"), "ids": [aj.stem]}
            fix = ("re-run the learn-analyze workflow for it (the authority decides how completely rules are extracted), with args "
                   + json.dumps({"root": str(ROOT), "items": [item]}, separators=(",", ":")))
            if aj.stem not in raw_ids:
                fix = (f"fetch its raw text first (.venv-wiki/bin/python tools/wiki.py fetch --only "
                       f"\"{name_of_folder(cfg, folders[aj.stem]) or aj.stem}\"), then " + fix)
            problems.append((aj.name, f"authority {a.get('authority')!r} but sources.json says {want!r}", fix))
    return problems, notes, raw_ids


def cmd_check(args):
    problems, notes, raw_ids = analysis_problems()
    for name, e, _ in problems:
        print(f"ERROR {name}: {e}")
    for name, n in notes:
        print(f"note  {name}: {n}")
    missing = [i for i in raw_ids if not (ANALYSIS / f"{i}.json").exists()]
    if RAW.exists():
        print(f"{len(raw_ids)} raw files, {len(raw_ids) - len(missing)} analysed, {len(missing)} pending")
    print("check: " + ("OK" if not problems else f"{len(problems)} errors (python3 tools/wiki.py next gives the fix for each)"))
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True, metavar="command")
    a = sub.add_parser("add", help="add a source to learn/sources.json",
                       description="Add a source: a YouTube channel or video, a web page, or a GitHub repo. The same page is never "
                                   "listed twice (links are compared without scheme, www. or a trailing slash).")
    a.add_argument("url", help="the channel, video, page or https://github.com/<owner>/<repo> link")
    a.add_argument("--authority", required=True, choices=AUTHORITY,
                   help="non-negotiable: house standards, locked in every project; good-to-have: recommended defaults; "
                        "reference: learning material (docs/KNOWLEDGE.md section 1)")
    a.add_argument("--name", help="the name fetch --only uses; it also names the raw folder and id prefix "
                                  "(default: the link, or owner/repo for GitHub)")
    rm = sub.add_parser("remove", help="take a source, or one page of it, off the list")
    rm.add_argument("what", help="the source's exact name, or one of its links")
    f = sub.add_parser("fetch", help="raw text into learn/raw/ (run with .venv-wiki/bin/python)")
    f.add_argument("--only", metavar="NAME", help="fetch one source, by its exact name in learn/sources.json")
    p = sub.add_parser("pending", help="raw files that have no analysis yet")
    p.add_argument("--json", action="store_true", help="one row per file, as JSON")
    p.add_argument("--work-items", action="store_true", help='the learn-analyze workflow args: {"root": ..., "items": [...]}')
    stt = sub.add_parser("status", help="every source: analysed, in the wiki, raw text on this machine")
    stt.add_argument("--json", action="store_true", help="the same, with each source's folder, id prefix and links")
    i = sub.add_parser("ingest", help="analysis JSON into learn/wiki/ pages (run with .venv-wiki/bin/python)")
    i.add_argument("--force", action="store_true", help="rebuild every page, even when its analysis did not change")
    sub.add_parser("check", help="check every analysis file; exit 1 on errors")
    sub.add_parser("trace", help="append new sources to traces/L19-trace.md")
    nx = sub.add_parser("next", help="what is out of date, in order, with the command for each step")
    nx.add_argument("--strict", action="store_true", help="exit 1 when anything needs doing")
    fg = sub.add_parser("flagged", help="what the citation check left for review")
    fg.add_argument("--json", action="store_true", help="the learn-escalate workflow's input")
    sub.add_parser("review-log", help="record review decisions (a JSON list on stdin)")
    mp = sub.add_parser("map", help="write learn/MAP.md")
    mp.add_argument("--check", action="store_true", help="exit 1 when learn/MAP.md is out of date")
    pp = sub.add_parser("proposals", help="refresh the pending-proposals table in synthesis/QUESTIONNAIRE.md")
    pp.add_argument("--check", action="store_true", help="exit 1 when the table is out of date")
    cc = sub.add_parser("cite-check", help="Jev checks each rule against its source passage (needs JEV_API_KEY)")
    cc.add_argument("ids", nargs="*", help="analysis ids (default: all)")
    cc.add_argument("--limit", type=int, help="check at most this many rules")
    cc.add_argument("--strength", nargs="+", default=["must", "should"], help="rule strengths to check")
    cc.add_argument("--standards", action="store_true", help="check synthesis/standards.json against its cited sources")
    st = sub.add_parser("standards", help="check synthesis/standards.json, or version a change")
    st.add_argument("--bump", metavar="WHY", help="version a change: stamp since/changed, record history, retire removed ids")
    st.add_argument("--built-from", action="store_true", dest="built_from",
                    help="record which analyses the standards were built from (the learn-standards merge runs this)")
    u = sub.add_parser("upstream", help="is OpenWiki ahead of learn/openwiki.lock.json?")
    u.add_argument("--upgrade", action="store_true", help="install the new commit, run both test suites, move the lock if they pass")
    u.add_argument("--strict", action="store_true", help="exit 1 when OpenWiki moved")
    args = ap.parse_args()
    sys.exit({"add": cmd_add, "remove": cmd_remove, "fetch": cmd_fetch, "pending": cmd_pending, "status": cmd_status,
              "ingest": cmd_ingest, "check": cmd_check, "trace": cmd_trace, "upstream": cmd_upstream, "standards": cmd_standards,
              "cite-check": cmd_cite_check, "next": cmd_next, "flagged": cmd_flagged, "map": cmd_map, "review-log": cmd_review_log,
              "proposals": cmd_proposals}[args.cmd](args) or 0)


if __name__ == "__main__":
    main()
