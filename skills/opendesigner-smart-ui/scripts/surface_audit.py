#!/usr/bin/env python3
"""Smart UI audit: render answers or every component's state fixtures in headless Chromium and check them.

Called by `smartui.py audit`. Needs Playwright for Python (`pip install playwright && playwright install chromium`);
this script never installs anything. It serves the files on 127.0.0.1 only, for the length of the run.

Checks on every render (measured in the page, see FLOORS_JS):
  cut-off text and sideways scroll · targets 24 px (44 px for actions that change data) · every control and image
  named · repeated names · text contrast (WCAG 2.2 AA) · one polite live region · focus visible on Tab · nothing
  moves with reduced motion · the text-only fallback says something
Plus, when opendesigner-review's probe.js has the craft checks: cut-off, breathing room, kerning and copy (review.py).
Failures can go into the audit ledger with engine.py ledger (--ledger).
"""
import contextlib
import copy
import functools
import http.server
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
ASSETS = SKILL / "assets"
LIB = SKILL.parent / "opendesigner" / "assets" / "library" / "components"
FIXTURES = ASSETS / "fixtures" / "components"  # older place; components/<slug>/fixture.json comes first


def fixture_path(slug):
    for f in (LIB / slug / "fixture.json", FIXTURES / f"{slug}.json"):
        if f.exists():
            return f
    return None
REVIEW = pathlib.Path(os.environ.get("OD_REVIEW_DIR") or SKILL.parent / "opendesigner-review" / "scripts")  # the craft checks
ENGINE = SKILL.parent / "opendesigner" / "scripts" / "engine.py"

HARNESS = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Smart UI audit</title><link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="od-surface.css">
<style>body{margin:0;padding:var(--ds-space-inset-lg);background:var(--ds-color-bg-canvas, var(--ds-color-surface-default));} od-surface{max-inline-size:44rem;margin-inline:auto}</style>
<script src="od-components.js"></script></head><body><main><od-surface id="s"></od-surface></main>
<script type="module">
import "./od-surface.js";
const cat = await (await fetch("catalog.json")).json();
const s = document.getElementById("s"); s.catalog = cat;
window.__render = (answer, o = {}) => {
  s.reset(); s.source = o.source; s.maxParts = o.maxParts;
  document.documentElement.dir = o.rtl ? "rtl" : "ltr";
  document.documentElement.style.fontSize = o.text200 ? "200%" : "";
  if (o.loading) { s.showLoading(o.loading); return {ok: true}; }
  const r = s.process(answer, {partial: !!o.partial, allowEmpty: !!o.relax});
  if (o.actionState) { const b = s.querySelector("[data-od-event]"); if (b) s.setActionState(b, o.actionState, "Saving"); }
  return {ok: r.ok, errors: r.errors, text: s.toText()};
};
window.__ready = true;
</script></body></html>"""

FLOORS_JS = r"""() => {
  const out = {cutoff: [], scroll: null, targets: [], unnamed: [], repeated: [], contrast: [], live: 0, images: []};
  const vis = (el) => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none"; };
  const sel = (el) => el.tagName.toLowerCase() + (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : "");
  const surf = document.querySelector("od-surface");
  const de = document.scrollingElement;
  if (de.scrollWidth > innerWidth + 1) out.scroll = {page: de.scrollWidth, viewport: innerWidth};
  for (const el of surf.querySelectorAll("*")) {
    if (!vis(el)) continue;
    const cs = getComputedStyle(el);
    const r0 = el.getBoundingClientRect();
    const srOnly = r0.width <= 1.5 && r0.height <= 1.5 || /inset\(50%\)/.test(cs.clipPath);  // visually hidden text for screen readers, on purpose
    const clips = !srOnly && (/(hidden|clip)/.test(cs.overflowX + cs.overflowY) || cs.textOverflow === "ellipsis");
    const text = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    if (text && clips && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 2) && !/(auto|scroll)/.test(cs.overflowX + cs.overflowY))
      out.cutoff.push({sel: sel(el), text: el.textContent.trim().slice(0, 60), sw: el.scrollWidth, cw: el.clientWidth});
    if (text && !el.closest("[aria-hidden=true]") && cs.color && el.textContent.trim().length > 1) {
      const fg = parse(cs.color); let bg = null, n = el;
      while (n && !bg) { const c = parse(getComputedStyle(n).backgroundColor); if (c && c[3] > 0.95) bg = c; if (getComputedStyle(n).backgroundImage !== "none" && !bg) { bg = "image"; } n = n.parentElement; }
      if (fg && bg && bg !== "image") {
        const op = +cs.opacity < 1 ? +cs.opacity : 1;
        const f = op < 1 ? fg.map((v, i) => i < 3 ? v * op + bg[i] * (1 - op) : 1) : fg;
        const ratio = contrast(f, bg), size = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 600;
        const need = size >= 24 || (bold && size >= 18.66) ? 3 : 4.5;
        if (ratio + 0.005 < need) out.contrast.push({sel: sel(el), text: el.textContent.trim().slice(0, 40), ratio: +ratio.toFixed(2), need});
      }
    }
  }
  const controls = [...surf.querySelectorAll("button, a[href], a[role=button], input:not([type=hidden]), select, textarea, [role=button], [role=option], [role=checkbox], [role=switch], [role=tab]")].filter((e) => vis(e) && !e.closest("[aria-hidden=true]"));
  const names = new Map();
  for (const el of controls) {
    const r = el.getBoundingClientRect();
    const main = el.matches("[data-od-effect=change]");
    const min = main ? 44 : 24;
    const box = el.closest("label") && el.matches("input") ? el.closest("label").getBoundingClientRect() : r;
    if (box.width + 0.5 < min || box.height + 0.5 < min) out.targets.push({sel: sel(el), w: Math.round(box.width), h: Math.round(box.height), min});
    let name = el.getAttribute("aria-label") || (el.getAttribute("aria-labelledby") || "").split(/\s+/).map((id) => document.getElementById(id)?.textContent || "").join(" ").trim();
    if (!name && el.labels && el.labels.length) name = [...el.labels].map((l) => l.textContent).join(" ");
    if (!name) name = el.textContent || el.getAttribute("title") || el.getAttribute("placeholder") || "";
    name = name.replace(/\s+/g, " ").trim().toLowerCase();
    if (!name) out.unnamed.push(sel(el));
    else if (el.matches("button, [role=button], a")) { names.set(name, (names.get(name) || 0) + 1); }
  }
  for (const [n, c] of names) if (c > 1) out.repeated.push({name: n, count: c});
  for (const img of surf.querySelectorAll("img")) if (!img.hasAttribute("alt")) out.images.push(sel(img));
  out.live = document.querySelectorAll("[aria-live=polite]").length;
  out.assertive = document.querySelectorAll("[aria-live=assertive]").length;
  out.text = surf.innerText.length;
  return out;
  function parse(c) { const m = /rgba?\(([^)]+)\)/.exec(c || ""); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; }
  function lum(c) { const a = c.slice(0, 3).map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2]; }
  function contrast(a, b) { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
}"""

FOCUS_JS = r"""async () => {
  const surf = document.querySelector("od-surface"), miss = [];
  const els = [...surf.querySelectorAll("button:not([disabled]), a[href], [role=button][tabindex], input:not([type=hidden]):not([disabled]), select, textarea, [tabindex='0']")].filter((e) => e.getBoundingClientRect().width > 0 && !e.closest("[aria-hidden=true], [inert]"));
  for (const el of els.slice(0, 30)) {
    el.focus({focusVisible: true});
    const cs = getComputedStyle(el), cw = getComputedStyle(el.closest("label") || el);
    const ok = (cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== "none" || (cw.outlineStyle !== "none" && parseFloat(cw.outlineWidth) > 0)
      || el.matches(":focus-visible") && [...document.styleSheets].length && (el.parentElement && getComputedStyle(el.parentElement).outlineStyle !== "none");
    if (!ok) miss.push(el.tagName.toLowerCase() + "." + (el.className || ""));
  }
  return {count: els.length, missing: miss};
}"""

MOTION_JS = r"""() => document.getAnimations().filter((a) => a.playState === "running" && a.effect && a.effect.getTiming().duration > 1 && a.effect.getTiming().iterations === Infinity).map((a) => (a.effect.target && a.effect.target.className) || "?")"""

ENVIRONMENTS = {
    "desktop": {"width": 1440, "height": 900},
    "phone": {"width": 375, "height": 812},
    "phone-320": {"width": 320, "height": 700},
    "text-200": {"width": 1440, "height": 900, "text200": True},
    "dark": {"width": 1440, "height": 900, "dark": True},
    "dark-phone": {"width": 375, "height": 812, "dark": True},
    "rtl": {"width": 375, "height": 812, "rtl": True},
    "reduced-motion": {"width": 375, "height": 812, "reduced": True},
}


# ----------------------------------------------------------------------------------------------- fixtures (section 5)

def _strings(obj, fn, schema=None):
    if isinstance(obj, str):
        return fn(obj, schema or {})
    if isinstance(obj, list):
        it = (schema or {}).get("items", {})
        return [_strings(x, fn, it) for x in obj]
    if isinstance(obj, dict):
        props = (schema or {}).get("properties", {})
        # event names, enums and URLs are not prose: leave them as they are
        return {k: (v if k in ("component", "id", "event") or k.startswith("@") or "$ref" in props.get(k, {})
                    or (isinstance(v, str) and ("enum" in props.get(k, {}) or props.get(k, {}).get("format") == "uri" or "pattern" in props.get(k, {})))
                    else _strings(v, fn, props.get(k))) for k, v in obj.items()}
    return obj


def longer(s, schema, grow=0.3):
    """A 30% longer language: every word grows, no new spaces (a German stand-in)."""
    out = re.sub(r"[A-Za-z]{3,}", lambda m: m.group(0) + ("ung" * 9)[:max(1, round(len(m.group(0)) * grow))], s)
    return out[: schema.get("maxLength", len(out))]


def longest(s, schema):
    n = schema.get("maxLength", len(s) * 3)
    base = (s + " ") * (n // max(1, len(s) + 1) + 1)
    return base[:n].strip() or s


def lists(comp, schema, fn):
    out = copy.deepcopy(comp)
    for k, p in schema.get("properties", {}).items():
        if p.get("type") == "array" and isinstance(out.get(k), list):
            out[k] = fn(out[k], p)
    return out


def fill_to_max(xs, p):
    """Repeat the items up to maxItems, each copy named apart (a list of identical names is its own error, R5)."""
    n = p.get("maxItems", 12)
    if not xs:
        return xs
    out = []
    nf = p.get("items", {}).get("x-od-name-from")
    for i in range(n):
        it = copy.deepcopy(xs[i % len(xs)])
        if i >= len(xs) and isinstance(it, dict):
            iprops = p.get("items", {}).get("properties", {})
            free = lambda k: isinstance(it.get(k), str) and "enum" not in iprops.get(k, {}) and "pattern" not in iprops.get(k, {})
            key = nf if nf and free(nf) else next((k for k in it if free(k)), None)
            if key:
                mx = p.get("items", {}).get("properties", {}).get(key, {}).get("maxLength", 200)
                suffix = f" {i + 1}"
                it[key] = it[key][: max(1, mx - len(suffix))] + suffix
            def number(node):  # a copied button would repeat its spoken name, also in nested lists: number the copies
                if isinstance(node, dict):
                    if "event" in node and isinstance(node.get("label"), str):
                        node["a11y_label"] = (node.get("a11y_label") or node["label"])[:110] + f" {i + 1}"
                    for x in node.values():
                        number(x)
                elif isinstance(node, list):
                    for x in node:
                        number(x)
            number(it)
        out.append(it)
    return out


def variants(base, schema):
    """The content and load states of section 5, made from one good fixture of the component."""
    c = base
    v = {"base": {"comp": c}}
    has_list = any(p.get("type") == "array" for p in schema.get("properties", {}).values())
    if has_list:
        v["empty"] = {"comp": lists(c, schema, lambda xs, p: []), "relax": True}
        one = lists(c, schema, lambda xs, p: xs[:1])
        if "rows" in schema.get("properties", {}) and "columns" in c:
            one["columns"] = copy.deepcopy(c["columns"])  # one row of a table still has every column, each with its header
        v["one-item"] = {"comp": one, "relax": True}
        v["max-items"] = {"comp": lists(c, schema, fill_to_max)}
    v["long-text"] = {"comp": _strings(c, longest, schema)}
    v["translate-30"] = {"comp": _strings(c, longer, schema)}
    v["partial"] = {"comp": {k: x for i, (k, x) in enumerate(c.items()) if k in ("component", "id") or i % 2 == 0}, "partial": True}
    v["loading"] = {"loading": c["component"]}
    v["stale"] = {"comp": {**c, "@metadata": {"stale_since": "10:42"}}}
    v["no-permission"] = {"comp": {**c, "@metadata": {"permission": "denied", "permission_note": "Ask an admin for access."}}}
    if re.search(r'"event"', json.dumps(c)):
        for st in ("pending", "done", "failed"):
            v["action-" + st] = {"comp": c, "actionState": st}
    if re.search(r'"src"', json.dumps(c)):
        v["missing-image"] = {"comp": json.loads(re.sub(r'"src":\s*"[^"]*"', '"src": "https://images.unsplash.com/photo-0000000000000-missing?w=10"', json.dumps(c)))}
    return v


def answer(comp):
    return [{"version": "1.0", "createSurface": {"surfaceId": "s1", "components": [{**comp, "id": "root"}]}}]


# ----------------------------------------------------------------------------------------------- serving and running

@contextlib.contextmanager
def serve(root):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=str(root))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}"
    finally:
        srv.shutdown()


def stage(catalog_dir, tokens, tmp):
    tmp = pathlib.Path(tmp)
    for f in ("od-surface.js", "od-validate.js", "od-surface.css"):
        shutil.copy(ASSETS / f, tmp / f)
    for f in ("catalog.json", "od-components.js"):
        shutil.copy(pathlib.Path(catalog_dir) / f, tmp / f)
    shutil.copy(tokens, tmp / "tokens.css")
    (tmp / "index.html").write_text(HARNESS)
    probe = REVIEW / "probe.js"
    return probe if probe.exists() else None


def run_matrix(catalog_dir, tokens, cases, out, envs=None, shots=True, craft=True):
    """cases: [(name, answer, opts)]. Returns a list of results with findings."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise SystemExit("Playwright for Python is not installed. To run the audit: pip install playwright && playwright install chromium")
    out = pathlib.Path(out)
    (out / "shots").mkdir(parents=True, exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory() as tmp, serve(tmp) as url:
        probe = stage(catalog_dir, tokens, tmp)
        probe_src = probe.read_text() if probe and craft else None
        with sync_playwright() as pw:
            browser = launch(pw)
            for env_name, env in (envs or ENVIRONMENTS).items():
                ctx = browser.new_context(viewport={"width": env["width"], "height": env["height"]},
                                          color_scheme="dark" if env.get("dark") else "light",
                                          reduced_motion="reduce" if env.get("reduced") else "no-preference")
                page = ctx.new_page()
                logs = []
                page.on("console", lambda m: logs.append(m.text) if m.type in ("error", "warning") else None)
                page.on("pageerror", lambda e: logs.append(str(e)))
                page.goto(url + "/index.html")
                page.wait_for_function("window.__ready === true")
                for name, ans, opts in cases:
                    logs.clear()
                    o = {**opts, "rtl": env.get("rtl"), "text200": env.get("text200")}
                    r = page.evaluate("([a, o]) => window.__render(a, o)", [ans, o])
                    page.wait_for_timeout(80)
                    f = page.evaluate(FLOORS_JS)
                    focus = page.evaluate(FOCUS_JS) if env_name in ("desktop", "phone") else {"missing": []}
                    moving = page.evaluate(MOTION_JS) if env.get("reduced") else []
                    findings = []
                    if not r.get("ok") and not opts.get("expect_error"):
                        findings.append({"check": "validator", "detail": r.get("errors", [])[:3]})
                    for k, label in (("cutoff", "cut-off text"), ("targets", "target too small"), ("unnamed", "control without a name"),
                                     ("repeated", "two controls with one name"), ("contrast", "contrast below AA"), ("images", "image without alt")):
                        if f.get(k):
                            findings.append({"check": label, "detail": f[k][:5]})
                    if f.get("scroll"):
                        findings.append({"check": "sideways scroll", "detail": f["scroll"]})
                    if not f.get("live") or f.get("assertive"):  # parts may have their own polite status line; never assertive
                        findings.append({"check": "live region", "detail": f"{f.get('live')} polite, {f.get('assertive')} assertive (want at least 1 polite, no assertive)"})
                    if focus.get("missing"):
                        findings.append({"check": "focus not visible", "detail": focus["missing"][:5]})
                    if moving:
                        findings.append({"check": "moves with reduced motion", "detail": moving[:5]})
                    if not opts.get("loading") and not opts.get("partial") and r.get("ok") and not (r.get("text") or "").strip():
                        findings.append({"check": "text fallback is empty", "detail": ""})
                    errs = [x for x in logs if "favicon" not in x]
                    if errs:
                        findings.append({"check": "console error", "detail": errs[:3]})
                    craft_findings = None
                    if probe_src:
                        craft_findings = run_craft(page, probe_src, out, f"{name}.{env_name}")
                        if craft_findings:
                            findings += [{"check": "craft " + c.get("case", ""), "detail": c.get("title"), "severity": c.get("severity")} for c in craft_findings]
                    shot = None
                    if shots and env_name in ("desktop", "phone", "dark-phone"):
                        shot = out / "shots" / f"{name}.{env_name}.png"
                        el = page.query_selector("od-surface")
                        try:
                            (el or page).screenshot(path=str(shot))
                        except Exception:
                            page.screenshot(path=str(shot))
                    results.append({"case": name, "env": env_name, "ok": r.get("ok"), "findings": findings,
                                    "shot": str(shot.relative_to(out)) if shot else None})
                ctx.close()
            browser.close()
    return results


def launch(pw):
    """Playwright's own Chromium, or the Chrome already on this computer (channel chrome), so nothing is downloaded."""
    try:
        return pw.chromium.launch()
    except Exception:
        return pw.chromium.launch(channel="chrome")


def run_craft(page, probe_src, out, key):
    """opendesigner-review's probe plus review.py check, when its craft checks exist (S2). None when they don't."""
    try:
        data = page.evaluate(probe_src)
    except Exception:
        return None
    if not isinstance(data, dict) or "craft" not in data:
        return None
    pdir = out / "probes"
    pdir.mkdir(exist_ok=True)
    pf = pdir / f"{key}.json"
    pf.write_text(json.dumps(data))
    try:
        r = subprocess.run([sys.executable, str(REVIEW / "review.py"), "check", str(pf), "--json"], capture_output=True, text=True, timeout=60)
        res = json.loads(r.stdout or "[]")
    except (subprocess.SubprocessError, ValueError):
        return None
    items = res.get("findings", res) if isinstance(res, dict) else res
    return [x for x in items if isinstance(x, dict) and x.get("severity") in ("high", "medium", "error", "warning", "fail")]


def fixture_cases(catalog, only=None):
    cases = []
    for name, schema in catalog["components"].items():
        slug = ((schema.get("metadata") or {}).get("extensions", {}).get("opendesigner", {})).get("slug")
        if not slug or (only and slug not in only and name not in only):
            continue
        f = fixture_path(slug)
        if not f:
            cases.append((f"{slug}.no-fixture", None, {"missing": True}))
            continue
        base = json.loads(f.read_text())
        for vname, v in variants({**base, "component": name, "id": "root"}, schema).items():
            opts = {}
            if v.get("partial"):
                opts["partial"] = True
            if v.get("loading"):
                opts["loading"] = v["loading"]
            if v.get("actionState"):
                opts["actionState"] = v["actionState"]
            if v.get("relax"):
                opts["relax"] = True
            cases.append((f"{slug}.{vname}", answer(v["comp"]) if "comp" in v else None, opts))
    return cases


def report(results, out):
    out = pathlib.Path(out)
    bad = [r for r in results if r["findings"]]
    # an empty list may be below minItems: that is the validator doing its job, not a render failure
    lines = ["# Smart UI audit", "", f"{len(results)} renders, {len(bad)} with findings.", "",
             "| Case | Where | Findings |", "|---|---|---|"]
    for r in bad:
        lines.append(f"| {r['case']} | {r['env']} | " + "; ".join(f"{x['check']}: {json.dumps(x['detail'])[:160]}" for x in r["findings"]).replace("|", "/") + " |")
    (out / "REPORT.md").write_text("\n".join(lines) + "\n")
    (out / "audit.json").write_text(json.dumps(results, indent=1) + "\n")
    return bad


def ledger(bad):
    """One ledger item per failing case and check (engine.py ledger, owned by the core skill)."""
    seen = set()
    for r in bad:
        for f in r["findings"]:
            item = "SUI-" + re.sub(r"[^a-z0-9]+", "-", f"{r['case']}-{f['check']}".lower()).strip("-")[:60]
            if item in seen:
                continue
            seen.add(item)
            note = f"{f['check']} at {r['env']}: {json.dumps(f['detail'])[:120]}"
            for args in (["ledger", "add", item, "--note", note], ["ledger", "broke", item, "--note", note]):
                subprocess.run([sys.executable, str(ENGINE), *args], capture_output=True, text=True)
    return len(seen)


def run(a):
    cat_path = pathlib.Path(a.catalog)
    catalog = json.loads(cat_path.read_text())
    cases = []
    if a.fixtures:
        cases += [c for c in fixture_cases(catalog, set(a.only.split(",")) if a.only else None) if c[1] is not None or c[2].get("loading")]
    for f in a.answer or []:
        sys.path.insert(0, str(HERE))
        import smartui
        ans = smartui.extract_answer(pathlib.Path(f).read_text())
        if ans:
            cases.append((pathlib.Path(f).stem, ans, {}))
    if not cases:
        print("Nothing to render: pass --fixtures or --answer <file>.")
        return 2
    # an empty or one-item list below minItems is refused by the validator; render those with relaxed minimums
    envs = {k: ENVIRONMENTS[k] for k in (a.envs.split(",") if getattr(a, "envs", None) else ENVIRONMENTS)}
    results = run_matrix(cat_path.parent, a.tokens, cases, a.out, envs=envs, shots=not getattr(a, "no_shots", False))
    bad = report(results, a.out)
    print(f"{len(results)} renders, {len(bad)} with findings. Report: {a.out}/REPORT.md")
    if a.ledger and bad:
        print(f"Recorded {ledger(bad)} ledger items (engine.py ledger show).")
    return 1 if bad else 0
