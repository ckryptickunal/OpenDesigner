#!/usr/bin/env python3
"""Design evals: run the engine on a fixed set of briefs and check what it produces, with no AI involved.

    python3 tools/design_evals.py              run every brief, write evals/design/results/<date>.json and latest.json
    python3 tools/design_evals.py --brief yellow-brand     one brief only (by id)
    python3 tools/design_evals.py --check --no-save     exit 1 if a required check fails, write nothing (for CI)

Each brief in evals/design/briefs.json is a person's five sketch answers. For each one the engine sketches and builds a
system in a temporary folder, twice. Two tiers of checks, each scored pass or fail:

Required (WCAG 2.2 AA and the files a person relies on; every one should always pass):
    builds          sketch and build both exit 0
    no-errors       engine validate reports 0 errors
    text-contrast   the lowest text pair is at least 4.5:1 in light and in dark mode (SC 1.4.3)
    ui-contrast     the lowest input-border and focus pairs are at least 3:1 in both modes (SC 1.4.11)
    targets         pointer targets at least 24 px (SC 2.5.8); touch targets at least 44 px when a touch platform is named
    brand-kept      the brand hex the person typed is stored and appears, exactly, in the tokens and the CSS
    exports         every export (css, tailwind, figma, paper, swift, compose, dtcg) wrote files
    design-md       DESIGN.md exists and names the brand color
    same-twice      a second build from the same answers gives the same files, ignoring timestamps

Quality (house bars stricter than WCAG; a miss is a place the engine can improve, and the engine must say so):
    type-steps      every step of the type scale is at least 10% bigger than the one below, none under 12 px
                    (the 16 px input size, which stops iPhone Safari zooming, is not a scale step)
    button-visible  the primary button's fill is at least 3:1 against the page in both modes; WCAG asks for nothing here
                    when the button has a text label, but a near-white button on white reads as no button
    says-so         every quality miss above shows up as a warning in engine validate, so the person is told

Standard library only; it runs the engine as a subprocess and never touches the network.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENGINE = ROOT / "skills/opendesigner/scripts/engine.py"
DIR = ROOT / "evals/design"
TOUCH = {"ios", "android"}
EXPORTS = ["css", "tailwind", "figma", "paper", "swift", "compose", "dtcg"]
STAMP = re.compile(r'"(at|generated|created|updated|date|timestamp)"\s*:\s*"[^"]*"|\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d+)?Z?')


def engine(state, *args):
    return subprocess.run([sys.executable, str(ENGINE), "--dir", str(state), *args], capture_output=True, text=True, timeout=300)


def sketch_and_build(state, b):
    args = ["sketch", "--name", b["name"], "--brand", b["brand"], "--audience", b["audience"], "--platforms", ",".join(b["platforms"]),
            "--feel", ",".join(b["feel"]), "--delegated", "all"]
    if b.get("theme"):
        args += ["--theme", b["theme"]]
    s = engine(state, *args)
    if s.returncode:
        return False, (s.stdout + s.stderr)[-400:]
    r = engine(state, "build")
    return r.returncode == 0, (r.stdout + r.stderr)[-400:]


def ratio(text):
    m = re.match(r"([\d.]+):1", text or "")
    return float(m.group(1)) if m else 0.0


def digest(state):
    h = hashlib.sha256()
    for f in sorted((state / "tokens").rglob("*")) + sorted((state / "build").rglob("*")):
        if f.is_file():
            h.update(str(f.relative_to(state)).encode())
            h.update(STAMP.sub("", f.read_text(errors="ignore")).encode())
    return h.hexdigest()


def run_brief(b):
    checks, quality, notes = {}, {}, {}
    with tempfile.TemporaryDirectory() as tmp:
        one, two = pathlib.Path(tmp) / "a", pathlib.Path(tmp) / "b"
        t0 = time.time()
        ok, log = sketch_and_build(one, b)
        notes["seconds"] = round(time.time() - t0, 1)
        checks["builds"] = ok
        if not ok:
            notes["log"] = log
            return checks, quality, notes
        v = json.loads(engine(one, "validate", "--json").stdout)
        st = v.get("stats", {})
        low = st.get("lowest", {})
        checks["no-errors"] = v.get("errors", 1) == 0
        text = {k: ratio(x) for k, x in low.items() if k.endswith(" text")}
        ui = {k: ratio(x) for k, x in low.items() if k.endswith((" non-text", " focus"))}
        fill = {k: ratio(x) for k, x in low.items() if k.endswith(" fill-boundary")}
        checks["text-contrast"] = bool(text) and min(text.values()) >= 4.5
        checks["ui-contrast"] = bool(ui) and min(ui.values()) >= 3.0
        notes["lowest"] = low
        tg = st.get("targets", {})
        checks["targets"] = tg.get("pointer", 0) >= 24 and (not TOUCH & set(b["platforms"]) or tg.get("touch", 0) >= 44)
        css_text = (one / "build/css/tokens.css").read_text() if (one / "build/css/tokens.css").exists() else ""
        sizes = sorted({int(n) for n in re.findall(r"--ds-font-size-(\d+):", css_text)})
        quality["type-steps"] = bool(sizes) and min(sizes) >= 12 and all(b2 >= a * 1.1 for a, b2 in zip(sizes, sizes[1:]))
        notes["typeScale"] = sizes
        quality["button-visible"] = bool(fill) and min(fill.values()) >= 3.0
        warned = {i.get("message", "") for i in v.get("items", []) if i.get("severity") == "warn"}
        quality["says-so"] = (quality["button-visible"] or any("bg.action.primary" in m for m in warned)) and \
                             (quality["type-steps"] or v.get("warnings", 0) > 0)
        hexv = b["brand"].lower()
        state = json.loads((one / "state.json").read_text())
        stored = str(state.get("raw", {}).get("brandColor", "")).lower()
        prims = (one / "tokens/primitives.tokens.json").read_text().lower() if (one / "tokens/primitives.tokens.json").exists() else ""
        css = (one / "build/css/tokens.css").read_text().lower() if (one / "build/css/tokens.css").exists() else ""
        checks["brand-kept"] = stored == hexv and hexv in prims and hexv in css
        notes["brandStored"] = stored
        checks["exports"] = all((one / "build" / x).is_dir() and any((one / "build" / x).rglob("*.*")) for x in EXPORTS)
        dm = one.parent / "DESIGN.md" if (one.parent / "DESIGN.md").exists() else one / "DESIGN.md"
        checks["design-md"] = dm.exists() and hexv in dm.read_text().lower()
        ok2, _ = sketch_and_build(two, b)
        checks["same-twice"] = ok2 and digest(one) == digest(two)
        notes["tokens"] = st.get("tokens")
        notes["contrastPairs"] = st.get("contrastPairs")
    return checks, quality, notes


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--brief", help="run one brief by id")
    ap.add_argument("--check", action="store_true", help="exit 1 if a required check fails")
    ap.add_argument("--no-save", action="store_true", help="print only; write no result files")
    a = ap.parse_args()
    briefs = json.loads((DIR / "briefs.json").read_text())["briefs"]
    if a.brief:
        briefs = [b for b in briefs if b["id"] == a.brief]
    rows, total, passed, qtotal, qpassed = [], 0, 0, 0, 0
    for b in briefs:
        checks, quality, notes = run_brief(b)
        n, p, qn, qp = len(checks), sum(checks.values()), len(quality), sum(quality.values())
        total, passed, qtotal, qpassed = total + n, passed + p, qtotal + qn, qpassed + qp
        rows.append({"id": b["id"], "why": b["why"], "checks": checks, "quality": quality, "passed": p, "of": n, **notes})
        fails = [k for k, ok in checks.items() if not ok] + [f"{k} (quality)" for k, ok in quality.items() if not ok]
        print(f"{b['id']:22} required {p}/{n}  quality {qp}/{qn}" + (f"  missed: {', '.join(fails)}" if fails else ""))
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    result = {"kind": "design", "date": datetime.date.today().isoformat(), "commit": commit, "briefs": len(rows),
              "checks": total, "passed": passed, "rate": round(passed / total, 4) if total else 0,
              "qualityChecks": qtotal, "qualityPassed": qpassed, "rows": rows}
    if not a.brief and not a.no_save:
        (DIR / "results").mkdir(parents=True, exist_ok=True)
        for path in (DIR / "results" / f"{result['date']}.json", DIR / "latest.json"):
            path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nrequired: {passed} of {total} passed across {len(rows)} briefs ({result['rate']:.0%}); quality: {qpassed} of {qtotal}")
    if a.check and passed < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
