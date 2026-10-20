#!/usr/bin/env python3
"""Checker evals: run OpenDesigner's own audit tools on pages with planted defects, and score what they catch.

    python3 tools/checker_evals.py                 every checker, plus check_layout.py's history; writes evals/checkers/results/<date>.json and latest.json
    python3 tools/checker_evals.py --repeat 2      run everything twice and record whether both runs found exactly the same things
    python3 tools/checker_evals.py --checker dates --no-history --no-write     one checker, nothing written

evals/checkers/manifest.json lists every fixture page in evals/checkers/fixtures/, the checker that reads it and the
findings it should produce. Clean pages expect none. The checkers under test are run as they ship, unchanged:

    layout     site/check_layout.py (Playwright, channel="chrome"), on the fixtures served from 127.0.0.1
    preflight  skills/opendesigner-preflight/scripts/preflight.py html <page> --medium web
    review     skills/opendesigner-review: probe.js in Chrome at each viewport, the Tab walk and drawn-font check from
               capture.py at the narrowest and widest, console and failed requests, then review.py check --json
    dates      brand/tools/check_dates.py --year 2026
    names      brand/tools/check_names.py --registry evals/checkers/fixtures/names/NAMES.md

Matching is strict: a finding counts for a planted defect only when it names the same check and the same element (a
selector segment, an evidence entry, or the quoted text the expectation gives), at a width where the defect was planted.
A finding with the right check on the wrong element is reported as "mislocated" and does not count as a catch.

Scores, per checker and per check: recall (planted defects caught / planted), precision (findings that match a planted
defect / all findings) and falseAlarms (findings on clean pages). A layout finding seen at several widths is one finding.
Errors and warnings count; info notes (review.py's info severity, preflight's indented lines, check_names' NEW to-do list)
are kept in the results but never scored.

History: every committed version of site/check_layout.py (from git, written to a temporary folder, never to the working
tree), plus the working-tree file when it differs, is run on the same layout fixtures.

Standard library plus Playwright (and the installed Chrome). Opens nothing but 127.0.0.1.
"""
import argparse
import datetime as dt
import functools
import http.server
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import types

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "checkers"
FIX = EVALS / "fixtures"
LAYOUT = ROOT / "site" / "check_layout.py"
PREFLIGHT = ROOT / "skills" / "opendesigner-preflight" / "scripts" / "preflight.py"
REVIEW_DIR = ROOT / "skills" / "opendesigner-review" / "scripts"
DATES = ROOT / "brand" / "tools" / "check_dates.py"
NAMES = ROOT / "brand" / "tools" / "check_names.py"
CHECKERS = ["layout", "preflight", "review", "dates", "names"]
SCRIPTS = {"layout": LAYOUT, "preflight": PREFLIGHT, "review": REVIEW_DIR / "review.py", "dates": DATES, "names": NAMES}
CHECKER_FILES = [LAYOUT, PREFLIGHT, REVIEW_DIR / "review.py", REVIEW_DIR / "probe.js", REVIEW_DIR / "capture.py", DATES, NAMES]


# ------------------------------------------------------------------------------------------------- helpers
def sh(args, timeout=900):
    return subprocess.run([str(a) for a in args], capture_output=True, text=True, timeout=timeout, cwd=ROOT)


def git(*args):
    r = sh(["git", *args])
    return r.stdout.strip() if r.returncode == 0 else ""


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


class Server:
    """The fixtures folder on 127.0.0.1, a free port, quiet."""

    def __enter__(self):
        handler = functools.partial(Quiet, directory=str(FIX))
        self.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        return self

    def __exit__(self, *exc):
        self.httpd.shutdown()
        self.httpd.server_close()


def segments(sel):
    return [s.strip() for s in sel.split(" > ")]


# ------------------------------------------------------------------------------------------------- runners
# Each runner returns findings: {"page", "check", "level", "loc", "msg", ...}. "loc" is what an expectation's element is
# looked for in: a list of selector paths for the layout and review checkers, the message itself for the others.

LAYOUT_HEAD = re.compile(r"^(/\S+): ")
LAYOUT_AT = re.compile(r"^  at (\d+) px$")
LAYOUT_ROW = re.compile(r"^    (error|warning)\s+(\S+)\s+(.*)$")


def run_layout(script, fixtures, base, work):
    """One check_layout.py run per group of pages that share a width list. Findings at several widths become one finding."""
    groups = {}
    for f in fixtures:
        groups.setdefault(tuple(f["widths"]), []).append(f)
    found, raw = {}, []
    for widths, fs in groups.items():
        pages = ",".join("/" + f["page"] for f in fs)
        r = sh([sys.executable, script, "--base", base, "--pages", pages, "--widths", ",".join(map(str, widths)), "--shots", work / "shots"])
        if r.returncode not in (0, 1) or "pages at" not in r.stdout:
            raise SystemExit(f"check_layout.py failed ({script}):\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}")
        page = width = None
        lines = r.stdout.splitlines()
        for i, line in enumerate(lines):
            if m := LAYOUT_HEAD.match(line):
                page, width = m.group(1).lstrip("/"), None
            elif m := LAYOUT_AT.match(line):
                width = int(m.group(1))
            elif (m := LAYOUT_ROW.match(line)) and page:
                sel = re.sub(r"\s+\[figure .*\]$", "", m.group(3)).strip()
                msg = lines[i + 1].strip() if i + 1 < len(lines) else ""
                raw.append({"page": page, "width": width, "check": m.group(2), "level": m.group(1), "sel": sel, "msg": msg})
                key = (page, m.group(2), sel)
                f = found.setdefault(key, {"page": page, "check": m.group(2), "level": m.group(1), "loc": [sel], "msg": msg, "widths": []})
                f["widths"].append(width)
                if m.group(1) == "error":
                    f["level"] = "error"
    return list(found.values()), {"layoutInstances": len(raw)}


PF_ROW = re.compile(r"^(ERROR|WARN)\s+(.*)$")


def run_preflight(fixtures):
    out, info = [], 0
    for f in fixtures:
        r = sh([sys.executable, PREFLIGHT, "html", FIX / f["page"], "--medium", "web"])
        for line in r.stdout.splitlines():
            if m := PF_ROW.match(line):
                t = re.search(r"\[(M\d+(?:, M\d+)*)\]\s*$", m.group(2))
                tags = re.findall(r"M\d+", t.group(1)) if t else []
                check = tags[0] if tags else ("missing-sheet" if "is linked but not found" in m.group(2) else "untagged")
                out.append({"page": f["page"], "check": check, "tags": tags, "level": m.group(1).lower(), "loc": [m.group(2)], "msg": m.group(2)})
            elif line.startswith("       "):
                info += 1
    return out, {"infoLines": info}


def load_capture():
    """capture.py from the review skill, imported as a module so the eval uses its own Tab walk and drawn-font check."""
    sys.path.insert(0, str(REVIEW_DIR))
    spec = importlib.util.spec_from_file_location("od_capture", REVIEW_DIR / "capture.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_review(fixtures, base, work):
    from playwright.sync_api import sync_playwright
    cap = load_capture()
    out, info, notes = [], 0, []
    opts = types.SimpleNamespace(tabs=20)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        for f in fixtures:
            d = work / "review" / pathlib.Path(f["page"]).stem
            vps = sorted(f["viewports"])
            for w in vps:
                h = 844 if w < 700 else 900
                phone = w < 700
                ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=2 if phone else 1, is_mobile=phone, has_touch=phone,
                                          color_scheme="light", locale="en-US")
                page = ctx.new_page()
                url = f"{base}/{f['page']}"
                console = {"kind": "console", "url": url, "viewport": {"w": w, "h": h}, "media": {"colorScheme": "light"}, "messages": []}
                page.on("console", lambda m, c=console: c["messages"].append({"type": m.type, "text": m.text[:300]}) if m.type in ("error", "warning") else None)
                page.on("pageerror", lambda e, c=console: c["messages"].append({"type": "pageerror", "text": str(e)[:300]}))
                page.on("requestfailed", lambda r, c=console: c["messages"].append({"type": "requestfailed", "text": f"{r.method} {r.url[:160]} {r.failure}"}))
                page.on("response", lambda r, c=console: c["messages"].append({"type": "http", "text": f"{r.status} {r.url[:160]}"}) if r.status >= 400 else None)
                page.goto(url, wait_until="load")
                cap.settle(page)
                tag = f"{pathlib.Path(f['page']).stem}-{w}x{h}"
                probe = page.evaluate(cap.PROBE_JS)
                cap.review.write_json(d / "probes" / f"{tag}.json", probe)
                if w in (vps[0], vps[-1]):  # capture.py's anchor cells: the narrowest and the widest
                    cap.focus_walk(page, d, tag, probe, opts)
                    try:
                        cap.rendered_fonts(page, d, tag, probe)
                    except Exception as e:  # noqa: BLE001
                        notes.append(f"{f['page']} {w}: drawn-font check skipped ({str(e).splitlines()[0]})")
                cap.review.write_json(d / "console" / f"{tag}.json", console)
                ctx.close()
            project = FIX / f["project"] if f.get("project") else work  # the work folder has no opendesigner/: floors only
            r = sh([sys.executable, REVIEW_DIR / "review.py", "check", d, "--dir", d, "--project", project, "--json"])
            if r.returncode:
                raise SystemExit(f"review.py check failed on {f['page']}:\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}")
            for x in json.loads(r.stdout.replace(base, "<fixtures>")):  # the port changes every run
                if x["severity"] == "info":
                    info += 1
                    continue
                out.append({"page": f["page"], "check": x["case"], "level": x["severity"], "title": x["title"],
                            "loc": list(x.get("evidence") or []) + [x.get("measured") or ""], "msg": x["title"] + ": " + (x.get("measured") or "")})
        browser.close()
    return out, {"infoNotes": info, "notes": notes}


DATE_ROW = re.compile(r'^(.+?): "(.+)" (is a (\w+) in (\d{4})|is not a date)$')


def run_dates(fixtures):
    out = []
    for f in fixtures:
        r = sh([sys.executable, DATES, FIX / f["page"], "--year", "2026"])
        for line in r.stdout.splitlines():
            if m := DATE_ROW.match(line):
                out.append({"page": f["page"], "check": "weekday" if m.group(4) else "not-a-date", "level": "error", "loc": [m.group(2)], "msg": line.split(": ", 1)[1]})
    return out, {}


def run_names(fixtures):
    """All name pages in one run, as the checker is meant to be used: it compares pieces checked together."""
    paths = [FIX / f["page"] for f in fixtures]
    registry = FIX / fixtures[0]["registry"]
    r = sh([sys.executable, NAMES, *paths, "--registry", registry])
    out, new, page = [], 0, None
    by_name = {pathlib.Path(f["page"]).stem: f["page"] for f in fixtures}
    for line in r.stdout.splitlines():
        if m := re.match(r"^(\S+\.html) \((.+)\)$", line):
            page = str(pathlib.Path(m.group(1)).resolve().relative_to(FIX))
        elif m := re.match(r"^  (ERROR|WARN)\s+(.*)$", line):
            out.append({"page": page, "check": names_check(m.group(2)), "level": m.group(1).lower(), "loc": [m.group(2)], "msg": m.group(2)})
        elif line.startswith("  NEW"):
            new += int(re.search(r"NEW\s+(\d+)", line).group(1))
        elif m := re.match(r"^(ERROR|WARN)\s+(.*)$", line):  # pieces checked together: the line names its pieces
            first = re.search(r"\(([^)]+)\)", m.group(2))
            out.append({"page": by_name.get(first.group(1).split(",")[0].strip(), "(several)") if first else "(several)",
                        "check": "cross-near" if "letters from" in m.group(2) else "cross-new", "level": m.group(1).lower(), "loc": [m.group(2)], "msg": m.group(2)})
    return out, {"newNames": new}


def names_check(msg):
    if "is already a" in msg:
        return "registry-name"
    if "is part of" in msg:
        return "registry-word"
    if "letters from" in msg:
        return "registry-near"
    if "dictionary word" in msg:
        return "dictionary-name"
    return "other"


# ------------------------------------------------------------------------------------------------- scoring
def checks_of(m):
    return [m["check"]] if isinstance(m["check"], str) else list(m["check"])


def element_in(e, loc):
    """e names a selector segment of loc: exactly, or followed by more classes, an id or :nth-of-type (li.tag matches li.tag:nth-of-type(2))."""
    return any(seg == e or (seg.startswith(e) and seg[len(e)] in ".:#[") for seg in segments(loc))


def one_match(m, f):
    if f["check"] not in checks_of(m):
        return False
    if m.get("level") and f["level"] != m["level"]:
        return False
    if m.get("text") and not any(re.search(m["text"], x) for x in f["loc"] + [f["msg"]]):
        return False
    if m.get("elements") and not any(element_in(e, loc) for e in m["elements"] for loc in f["loc"]):
        return False
    return True


def matches(exp, f):
    """A finding matches a planted defect: same page, a width where it was planted (layout), and one of its matchers."""
    if f["page"] != exp["page"]:
        return False
    if exp.get("widths") and not set(f.get("widths") or []) & set(exp["widths"]):
        return False
    return any(one_match(m, f) for m in exp.get("any_of") or [exp])


def main_check(exp):
    return checks_of((exp.get("any_of") or [exp])[0])[0]


def all_checks(exp):
    return {c for m in exp.get("any_of") or [exp] for c in checks_of(m)}


def score(fixtures, findings):
    exps = [dict(e, page=f["page"]) for f in fixtures for e in f.get("expect", [])]
    clean_pages = {f["page"] for f in fixtures if f.get("clean")}
    for f in findings:
        f["matched"] = [e["id"] for e in exps if matches(e, f)]
    caught = {e["id"]: [f for f in findings if e["id"] in f["matched"]] for e in exps}
    false_f = [f for f in findings if not f["matched"]]
    for f in false_f:  # the right check on the right page, but not the planted element: a mislocated finding
        f["mislocatedFor"] = [e["id"] for e in exps if e["page"] == f["page"] and f["check"] in all_checks(e) and not caught[e["id"]]] or None

    def ratio(a, b):
        return round(a / b, 3) if b else None

    per = {}
    for c in sorted({main_check(e) for e in exps} | {f["check"] for f in findings}):
        ce = [e for e in exps if main_check(e) == c]
        cf = [f for f in findings if f["check"] == c]
        n_caught, n_true = sum(1 for e in ce if caught[e["id"]]), sum(1 for f in cf if f["matched"])
        per[c] = {"planted": len(ce), "caught": n_caught, "recall": ratio(n_caught, len(ce)), "findings": len(cf), "true": n_true,
                  "precision": ratio(n_true, len(cf)), "falseAlarms": sum(1 for f in cf if f["page"] in clean_pages)}
    n_caught = sum(1 for v in caught.values() if v)
    n_true = len(findings) - len(false_f)
    return {
        "planted": len(exps), "caught": n_caught, "recall": ratio(n_caught, len(exps)),
        "findings": len(findings), "true": n_true, "false": len(false_f), "precision": ratio(n_true, len(findings)),
        "cleanPages": len(clean_pages), "falseAlarms": sum(1 for f in findings if f["page"] in clean_pages),
        "mislocated": sum(1 for f in false_f if f.get("mislocatedFor")),
        "perCheck": per,
        "missed": [{"id": e["id"], "page": e["page"], "check": main_check(e), "what": e["what"]} for e in exps if not caught[e["id"]]],
        "unexpected": [{k: f[k] for k in ("page", "check", "level", "loc", "msg", "widths", "mislocatedFor") if f.get(k) is not None} for f in false_f],
        "caughtBy": {i: [{"check": f["check"], "level": f["level"], "msg": f["msg"][:200]} for f in fs] for i, fs in caught.items() if fs},
    }


# ------------------------------------------------------------------------------------------------- the run
def fixtures_for(manifest, checker):
    return [f for f in manifest["fixtures"] if f["checker"] == checker]


def run_all(manifest, which, server, work):
    results = {}
    for c in which:
        fx = fixtures_for(manifest, c)
        if c == "layout":
            found, meta = run_layout(LAYOUT, fx, server.base, work)
        elif c == "preflight":
            found, meta = run_preflight(fx)
        elif c == "review":
            found, meta = run_review(fx, server.base, work)
        elif c == "dates":
            found, meta = run_dates(fx)
        else:
            found, meta = run_names(fx)
        results[c] = {"script": str(SCRIPTS[c].relative_to(ROOT)), **score(fx, found), **meta}
    return results


def layout_versions():
    """Every committed version of check_layout.py, oldest first, plus the working tree when it differs from the last commit."""
    rows = [l.split("|", 2) for l in git("log", "--reverse", "--format=%h|%ad|%s", "--date=iso-strict", "--", "site/check_layout.py").splitlines() if l]
    out = [{"commit": h, "date": date, "subject": subject, "source": git("show", f"{h}:site/check_layout.py") + "\n"} for h, date, subject in rows]
    wt = LAYOUT.read_text()
    if not out or wt.strip() != out[-1]["source"].strip():
        out.append({"commit": "working tree", "date": dt.datetime.now().isoformat(timespec="seconds"), "subject": "uncommitted changes", "source": wt, "current": True})
    else:
        out[-1]["current"] = True
    return out


def run_history(manifest, server, work):
    """The same layout fixtures through every version of check_layout.py: what each version catches, what it newly catches
    (with the owner feedback items those defects answer) and which clean-page false alarms it removed or added."""
    fx = fixtures_for(manifest, "layout")
    clean = {f["page"] for f in fx if f.get("clean")}
    owner_of = {e["id"]: e.get("owner_feedback", []) for f in fx for e in f.get("expect", [])}
    check_of = {e["id"]: main_check(e) for f in fx for e in f.get("expect", [])}
    hist = []
    for v in layout_versions():
        d = work / "history" / v["commit"].replace(" ", "-")
        d.mkdir(parents=True, exist_ok=True)
        script = d / "check_layout.py"
        script.write_text(v["source"])
        found, _ = run_layout(script, fx, server.base, d)
        s = score(fx, found)
        alarms = sorted({(u["page"], u["check"], u["loc"][0]) for u in s["unexpected"] if u["page"] in clean})
        hist.append({"commit": v["commit"], "date": v["date"][:10], "time": v["date"], "subject": v["subject"], "current": v.get("current", False),
                     "checkNumbers": check_numbers(v["source"]), "findingTypes": sorted(set(re.findall(r'add\("([a-z-]+)"', v["source"]))),
                     "planted": s["planted"], "caught": s["caught"], "recall": s["recall"], "findings": s["findings"], "precision": s["precision"],
                     "falseAlarms": s["falseAlarms"], "missed": [m["id"] for m in s["missed"]],
                     "perCheck": {c: {"planted": p["planted"], "caught": p["caught"], "falseAlarms": p["falseAlarms"]} for c, p in s["perCheck"].items()},
                     "falseAlarmList": [{"page": a, "check": b, "element": c} for a, b, c in alarms]})
    prev = None
    for h in hist:
        gained = sorted(set(owner_of) - set(h["missed"])) if prev is None else sorted(set(prev["missed"]) - set(h["missed"]))
        h["newlyCaught"] = gained
        h["ownerFeedback"] = sorted({i for g in gained for i in owner_of[g]})
        items = f"; they answer owner feedback items {', '.join(map(str, h['ownerFeedback']))}" if h["ownerFeedback"] else ""
        if prev is None:
            h["note"] = f"First version: {span(h['checkNumbers'])}; catches {h['caught']} of {h['planted']} planted defects{items}."
        else:
            before = {(a["page"], a["check"], a["element"]) for a in prev["falseAlarmList"]}
            now = {(a["page"], a["check"], a["element"]) for a in h["falseAlarmList"]}
            h["falseAlarmsRemoved"] = [{"page": a, "check": b, "element": c} for a, b, c in sorted(before - now)]
            h["falseAlarmsAdded"] = [{"page": a, "check": b, "element": c} for a, b, c in sorted(now - before)]
            added = [n for n in h["checkNumbers"] if n not in prev["checkNumbers"]]
            parts = [f"adds {span(added)}"] if added else []
            if gained:
                parts.append(f"newly catches {len(gained)} planted defects ({', '.join(sorted({check_of[g] for g in gained}))}){items}")
            if h["falseAlarmsRemoved"]:
                parts.append(f"removes {len(h['falseAlarmsRemoved'])} clean-page false alarms ({', '.join(sorted({a['check'] for a in h['falseAlarmsRemoved']}))})")
            if h["falseAlarmsAdded"]:
                parts.append(f"adds {len(h['falseAlarmsAdded'])} clean-page false alarms ({', '.join(sorted({a['check'] for a in h['falseAlarmsAdded']}))})")
            h["note"] = ". ".join(x[0].upper() + x[1:] for x in parts or ["no change on these fixtures"]) + "."
        prev = h
    return hist


def check_numbers(source):
    """The numbered checks in check_layout.py's MEASURE script, from its comments ("// 3 and 5. stacked groups")."""
    return sorted({int(n) for m in re.finditer(r"^\s*//\s*(\d+)(?:\s+and\s+(\d+))?\.", source, re.M) for n in m.groups() if n})


def span(ns):
    """[9, 10, 11] -> 'checks 9 to 11'; [4] -> 'check 4'."""
    if not ns:
        return "no numbered checks"
    if len(ns) == 1:
        return f"check {ns[0]}"
    return f"checks {ns[0]} to {ns[-1]}" if ns == list(range(ns[0], ns[-1] + 1)) else "checks " + ", ".join(map(str, ns))


def fingerprint(results, history):
    """What must be identical between two runs: every finding's page, check, level, place and matches."""
    keep = {c: {k: r[k] for k in ("planted", "caught", "findings", "true", "falseAlarms", "missed", "unexpected")} for c, r in results.items()}
    if history:
        keep["history"] = [{k: v[k] for k in ("commit", "caught", "findings", "falseAlarms", "missed")} for v in history]
    return json.dumps(keep, sort_keys=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--checker", action="append", choices=CHECKERS, help="only this checker (repeatable)")
    ap.add_argument("--repeat", type=int, default=1, help="run everything this many times and compare (default 1)")
    ap.add_argument("--no-history", action="store_true", help="skip the old versions of check_layout.py")
    ap.add_argument("--no-write", action="store_true", help="print the summary, write no result files")
    a = ap.parse_args(argv)
    manifest = json.loads((EVALS / "manifest.json").read_text())
    which = a.checker or CHECKERS
    runs = []
    work_root = pathlib.Path(tempfile.mkdtemp(prefix="od-checker-evals-"))
    try:
        with Server() as server:
            for n in range(max(1, a.repeat)):
                work = work_root / f"run{n + 1}"
                work.mkdir()
                results = run_all(manifest, which, server, work)
                history = None if a.no_history or "layout" not in which else run_history(manifest, server, work)
                runs.append((results, history, fingerprint(results, history)))
    finally:
        shutil.rmtree(work_root, ignore_errors=True)
    results, history, fp = runs[0]
    chrome = ""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(channel="chrome")
            chrome = b.version
            b.close()
    except Exception:  # noqa: BLE001
        pass
    now = dt.datetime.now()
    doc = {
        "kind": "checkers",
        "date": now.date().isoformat(), "time": now.isoformat(timespec="seconds"),
        "commit": git("rev-parse", "--short", "HEAD"),
        "checkersChangedSinceCommit": [str(p.relative_to(ROOT)) for p in CHECKER_FILES if git("status", "--porcelain", "--", str(p.relative_to(ROOT)))],
        "environment": {"python": sys.version.split()[0], "chrome": chrome, "platform": sys.platform},
        "runs": len(runs), "sameEveryRun": all(r[2] == fp for r in runs),
        "scoring": "recall = planted defects caught / planted; precision = findings that match a planted defect / all findings; "
                   "falseAlarms = findings on clean pages. Errors and warnings count; info notes do not. A layout finding at several widths counts once.",
        "checkers": results,
    }
    if history:
        doc["history"] = history
        doc["historyChecker"] = "site/check_layout.py"
        doc["ownerFeedback"] = manifest.get("owner_feedback", {})
    print_summary(doc)
    if not a.no_write:
        out = EVALS / "results"
        out.mkdir(parents=True, exist_ok=True)
        text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
        (out / f"{doc['date']}.json").write_text(text)
        (EVALS / "latest.json").write_text(text)
        print(f"\nwritten: {(out / (doc['date'] + '.json')).relative_to(ROOT)} and {(EVALS / 'latest.json').relative_to(ROOT)}")
    return 0 if doc["sameEveryRun"] else 1


def pct(x):
    return "n/a" if x is None else f"{x * 100:.0f}%"


def print_summary(doc):
    print(f"checker evals, {doc['time']} (commit {doc['commit']}, Chrome {doc['environment']['chrome'] or '?'}); runs: {doc['runs']}, same every run: {doc['sameEveryRun']}")
    for c, r in doc["checkers"].items():
        print(f"\n{c} ({r['script']}): recall {r['caught']}/{r['planted']} ({pct(r['recall'])}), precision {r['true']}/{r['findings']} ({pct(r['precision'])}), "
              f"false alarms on {r['cleanPages']} clean page(s): {r['falseAlarms']}" + (f", mislocated: {r['mislocated']}" if r["mislocated"] else ""))
        for m in r["missed"]:
            print(f"  missed      {m['id']}: {m['what']}")
        for u in r["unexpected"]:
            print(f"  unexpected  {u['page']}: {u['check']} {u['level']} {(u['loc'][0] if u['loc'] else '')[:90]}" + (f" (mislocated: {', '.join(u['mislocatedFor'])})" if u.get("mislocatedFor") else ""))
    if doc.get("history"):
        print(f"\n{doc['historyChecker']} history (same layout fixtures):")
        for v in doc["history"]:
            print(f"  {v['commit']:<12} {v['date']}  recall {v['caught']}/{v['planted']} ({pct(v['recall'])}), precision {pct(v['precision'])}, "
                  f"clean false alarms {v['falseAlarms']}. {v['note']}")


if __name__ == "__main__":
    sys.exit(main())
