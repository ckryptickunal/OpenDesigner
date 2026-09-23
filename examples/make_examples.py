#!/usr/bin/env python3
"""Rebuild the three worked examples from scratch with the engine's own commands.

    python3 examples/make_examples.py            # all three
    python3 examples/make_examples.py devtool-dense

Each example is made only through `engine.py init / set / pick / build`, so decisions.md is the real
decision log the engine writes, and state.json is the only input the tokens depend on. The products
are fictional; no brand identity is copied from any real system.
"""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "..", "skills", "opendesigner", "scripts", "engine.py")

EXAMPLES = {
    "devtool-dense": {
        "name": "Devtool Dense",
        "steps": [
            ("set", "summary", "A dense, calm console for a fictional CI and observability tool: productive, compact, sharp, quiet.", "the one-line brief"),
            ("set", "context.product", "Build and run console for platform teams: pipelines, logs, traces.", "product brief"),
            ("set", "context.audience", "Engineers who keep it open all day on large desktop screens.", "Q-aud-01 conversation"),
            ("set", "context.surfaces", [{"name": "Pipelines table", "mode": "Operate"}, {"name": "Run detail and logs", "mode": "Read"}], "two main surfaces"),
            ("set", "context.memorable", "The run timeline: every step of a build on one line.", "Q-brand-02"),
            ("set", "context.scope", {"in": ["web app", "desktop shell"], "out": ["marketing site", "mobile apps"]}, "scope agreed at the first gate"),
            ("set", "principles", ["The task comes first: chrome recedes, data leads.", "Dense, never cramped: visuals shrink, hit areas do not.",
                                   "Quiet motion: show state changes, skip choreography."], "ranked principles"),
            ("pick", "Q-aud-01", "dense", "confirmed: people work all day in data-heavy tables"),
            ("pick", "Q-plat-01", ["web", "desktop"], "confirmed: browser plus an Electron-style desktop shell"),
            ("set", "raw.inputs", ["pointer"], "pointer-first desktop tool; touch is out of scope, so the 24px WCAG 2.5.8 floor applies"),
            ("set", "dials.expression", 20, "productive: no hero moments inside the product (DC-L06-03)"),
            ("set", "dials.brandPresence", 55, "own look on an open neutral face; platform chrome stays native"),
            ("set", "dials.density", 85, "compact band: 14px body, 32px default controls, compact spacing mode"),
            ("set", "dials.energy", 20, "calm: productive easing, no overshoot, durations x0.88"),
            ("set", "dials.roundness", 30, "4px controls: crisp but not brutal (Fluent, Radix band)"),
            ("set", "dials.depth", 22, "ring plus faint shadow: separation without heavy shadows in dense layouts"),
            ("set", "dials.colorfulness", 30, "neutral scheme: color only where it means something (status, selection, the primary action)"),
            ("set", "dials.warmth", 30, "cool, formal neutrals: slate-leaning gray"),
            ("set", "raw.brandColor", "#4a5cf0", "the product's indigo; used as the accent hue"),
            ("set", "raw.flags.brandExact", True, "keep the exact indigo on the primary action even at low colorfulness (Carbon pattern)"),
            ("set", "raw.textFace", "Inter", "open neutral face with tabular figures; OFL licence"),
            ("set", "raw.monoFace", "JetBrains Mono", "logs and code; OFL licence"),
            ("set", "raw.scripts", ["Latn"], "English-only product for now"),
            ("set", "hooks.H-logo.status", "have", "SVG logo exists"),
            ("set", "hooks.H-favicon.status", "have", "derived from the logo SVG"),
            ("set", "hooks.H-icons.status", "open-library", "Lucide (ISC licence), 1.5px strokes at 16px match the formula"),
            ("set", "hooks.H-type.status", "open-library", "Inter and JetBrains Mono under the SIL OFL"),
            ("set", "hooks.H-color.status", "have", "the indigo is fixed"),
            ("set", "hooks.H-illus.status", "not-needed", "empty states use icon plus text"),
            ("set", "hooks.H-photo.status", "not-needed", "no photography in a console"),
            ("set", "hooks.H-voice.status", "placeholder", "draft voice from the dials until a writer reviews it"),
        ],
    },
    "consumer-playful": {
        "name": "Consumer Playful",
        "steps": [
            ("set", "summary", "An expressive, rounded, colorful system for a fictional habit app shared between friends.", "the one-line brief"),
            ("set", "context.product", "A habit tracker where friends cheer each other on.", "product brief"),
            ("set", "context.audience", "Casual users on phones, a few minutes a day, many first-time visitors.", "Q-aud-01 conversation"),
            ("set", "context.surfaces", [{"name": "Today feed", "mode": "Experience"}, {"name": "Onboarding and store pages", "mode": "Persuade"},
                                         {"name": "Settings", "mode": "Operate"}], "surfaces and their modes"),
            ("set", "context.memorable", "The streak celebration.", "Q-brand-02"),
            ("set", "context.scope", {"in": ["iOS app", "Android app", "web app", "marketing pages"], "out": ["watch", "TV"]}, "scope"),
            ("set", "principles", ["Celebrate progress, never shame a miss.", "Big, friendly targets for thumbs.",
                                   "One joyful moment per screen, not ten."], "ranked principles"),
            ("set", "macros", ["playful", "friendly"], "Q-brand-01: playful and friendly; explicit dials below win where set"),
            ("pick", "Q-aud-01", "large", "confirmed: occasional, mobile users"),
            ("pick", "Q-plat-01", ["ios", "android", "web"], "confirmed: phone-first with a web companion"),
            ("set", "raw.inputs", ["touch", "pointer"], "touch first"),
            ("set", "dials.expression", 82, "expressive: hero moments, visible containers, springs throughout"),
            ("set", "dials.brandPresence", 70, "brand-led surfaces; navigation and sheets stay native"),
            ("set", "dials.density", 25, "spacious: 16px body, 48px default controls"),
            ("set", "dials.energy", 80, "energetic: springy (damping 0.76), durations x1.12, heavier headings"),
            ("set", "dials.roundness", 97, "pill controls, 24px cards"),
            ("set", "dials.depth", 62, "soft shadow ladder for cards and sheets"),
            ("set", "dials.colorfulness", 85, "expressive scheme with three accents and tinted containers"),
            ("set", "dials.warmth", 78, "warm neutrals and sentence case"),
            ("set", "raw.brandColor", "#ff5a36", "coral: warm and energetic"),
            ("set", "raw.textFace", "Nunito", "rounded open face (OFL) matching Roundness 81+"),
            ("set", "raw.productType", "content", "a content app: 16px body in the comfortable band"),
            ("set", "raw.marketingSurfaces", True, "store pages and onboarding need display sizes"),
            ("set", "hooks.H-logo.status", "have", "wordmark and symbol exist"),
            ("set", "hooks.H-appicon.status", "commissioning", "designer brief sent for layered 1024px icon"),
            ("set", "hooks.H-illus.status", "commissioning", "character illustrations for empty and success states"),
            ("set", "hooks.H-motion.status", "commissioning", "Lottie streak celebration"),
            ("set", "hooks.H-icons.status", "open-library", "Phosphor (MIT), rounded weight"),
            ("set", "hooks.H-type.status", "open-library", "Nunito under the SIL OFL"),
            ("set", "hooks.H-voice.status", "placeholder", "draft: casual, encouraging, contractions"),
        ],
    },
    "public-service-accessible": {
        "name": "Public Service Accessible",
        "steps": [
            ("set", "summary", "A plain, high-contrast system for a fictional city benefits service: AAA text, generous targets, no motion.", "the one-line brief"),
            ("set", "context.product", "Apply for and track council benefits online.", "product brief"),
            ("set", "context.audience", "Everyone, including people with low vision, low literacy, old devices and assistive technology.", "Q-aud-01"),
            ("set", "context.surfaces", [{"name": "Application form", "mode": "Operate"}, {"name": "Guidance pages", "mode": "Read"}], "surfaces"),
            ("set", "context.memorable", "Nothing to learn: one question per page.", "Q-brand-02"),
            ("set", "context.constraints", ["Legal: public-sector accessibility regulations", "Works without JavaScript"], "constraints"),
            ("set", "principles", ["Plain words, one question at a time.", "It works for everyone, on any device, with any assistive technology.",
                                   "Nothing decorative: every element earns its place."], "ranked principles"),
            ("pick", "Q-aud-01", "large", "confirmed: occasional, public users"),
            ("pick", "Q-plat-01", ["web"], "confirmed: web only"),
            ("pick", "Q-theme-01", "light-only", "confirmed: one light theme keeps testing simple; forced colors still work"),
            ("pick", "Q-motion-01", "none", "confirmed: no motion; state changes are instant"),
            ("set", "raw.inputs", ["touch", "pointer"], "phones and desktops"),
            ("set", "dials.expression", 10, "plain: no hero moments, whitespace over containers"),
            ("set", "dials.brandPresence", 85, "one fixed look everywhere; no theming"),
            ("set", "dials.density", 8, "spacious: 19px body text"),
            ("set", "dials.roundness", 0, "square corners"),
            ("set", "dials.depth", 5, "borders only; no shadows"),
            ("set", "dials.colorfulness", 35, "restrained: color for actions, links and status only"),
            ("set", "dials.warmth", 45, "near-neutral gray; formal but not cold"),
            ("set", "raw.brandColor", "#075c63", "a deep teal of our own (not another service's identity); 7.7:1 with white"),
            ("set", "raw.flags.brandExact", True, "the teal is the button fill exactly; it already carries white text at AAA"),
            ("set", "raw.contrastTarget", "AAA", "7:1 text everywhere (WCAG 2.2 SC 1.4.6)"),
            ("set", "raw.textFace", "Atkinson Hyperlegible", "open face designed for low vision (OFL) instead of any proprietary government face"),
            ("set", "raw.spaceUnit", 5, "5px unit, a raw input: gives 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120"),
            ("set", "raw.minTarget", 48, "generous targets: every hit area at least 48px"),
            ("set", "raw.focusWidth", 3, "a thicker 3px focus ring"),
            ("set", "hooks.H-logo.status", "have", "council crest supplied by the council"),
            ("set", "hooks.H-icons.status", "not-needed", "text labels instead of icons"),
            ("set", "hooks.H-illus.status", "not-needed", "no illustration"),
            ("set", "hooks.H-photo.status", "not-needed", "no photography"),
            ("set", "hooks.H-type.status", "open-library", "Atkinson Hyperlegible under the SIL OFL"),
            ("set", "hooks.H-voice.status", "have", "plain-English content guide exists"),
        ],
    },
}


def run(*args):
    out = subprocess.run([sys.executable, ENGINE, *args], capture_output=True, text=True)
    if out.returncode not in (0,) and args[0] != "build":
        sys.exit(f"engine {' '.join(args)} failed:\n{out.stdout}\n{out.stderr}")
    return out


def make(name):
    spec = EXAMPLES[name]
    d = os.path.join(HERE, name)
    for sub in ("tokens", "build"):
        shutil.rmtree(os.path.join(d, sub), ignore_errors=True)
    for f in ("state.json", "decisions.md", "DESIGN.md", "PRODUCT.md", "preview.html"):
        if os.path.exists(os.path.join(d, f)):
            os.remove(os.path.join(d, f))
    run("init", "--dir", d, "--name", spec["name"])
    for kind, path, value, why in spec["steps"]:
        if kind == "pick":
            run("pick", "--dir", d, path, json.dumps(value), "--why", why)
        else:
            run("set", "--dir", d, path, json.dumps(value), "--why", why)
    out = run("build", "--dir", d)
    print(out.stdout.strip().splitlines()[0], "|", out.stdout.strip().splitlines()[1])
    write_readme(d, spec)
    return out.returncode


def write_readme(d, spec):
    """README with numbers read back from the generated files, so it can never drift from them."""
    meta = json.load(open(os.path.join(d, "tokens", "opendesigner.meta.json"), encoding="utf-8"))
    state = json.load(open(os.path.join(d, "state.json"), encoding="utf-8"))
    val = subprocess.run([sys.executable, ENGINE, "validate", "--json", "--dir", d], capture_output=True, text=True)
    rep = json.loads(val.stdout)
    t, sp, sh, mo, el = meta["type"], meta["space"], meta["shape"], meta["motion"], meta["elevation"]
    dens = meta["density"][meta["params"]["space.densityMode"]["value"]]
    acc = meta["ramps"]["accent"]["light"]["hex"]
    dials = " · ".join(f"{k} {v}" for k, v in meta["dials"].items())
    name = os.path.basename(d)
    lines = [
        f"# {spec['name']}", "", f"![{spec['name']}: components in light and dark, generated by the engine](preview.png)", "",
        state.get("summary", ""), "",
        f"**Dials:** {dials}.", "",
        "| What | Result |", "|---|---|",
        f"| Type | body {t['base']}px, ratio {t['ratio']}, sizes {', '.join(str(x) for x in t['sizes'])}; weights "
        + ", ".join(f"{k} {v}" for k, v in t["weights"].items()) + " |",
        f"| Space | {sp['unit']}px unit; default density {meta['params']['space.densityMode']['value']} (controls "
        f"{dens['control']['sm']}/{dens['control']['md']}/{dens['control']['lg']}px); hit areas " + ", ".join(f"{k} {v}px" for k, v in sp["targets"].items()) + " |",
        f"| Shape | control radius {sh['control']}, containers {sh['container']}px, focus ring {sh['focusWidth']}px |",
        f"| Depth | {el['model']} |",
        f"| Motion | medium {mo['durations']['medium']}ms, spring damping {mo['spatial']['dampingRatio']}"
        + (", motion off (reduced everywhere)" if mo.get("motionOff") else "") + " |",
        f"| Color | {meta['color']['scheme']} scheme, accent solid `{acc[8]}`, text minimum {meta['color']['textMin']}:1, themes {', '.join(meta['modes'])} |",
        f"| Validation | {rep['errors']} errors, {rep['warnings']} warnings, {rep['advisories']} notes; {rep['stats'].get('contrastPairs')} contrast pairs checked |",
        "", "**Files:** `state.json` (the only input), `decisions.md` (why each choice), `tokens/` (DTCG 2025.10 + resolver, canonical), "
        "`build/` (css, tailwind, figma, paper, swift, compose, dtcg), `DESIGN.md`, `PRODUCT.md`, `preview.html`.", "",
        f"**Rebuild:** `python3 examples/make_examples.py {name}` replays the decisions; `python3 skills/opendesigner/scripts/engine.py build --dir examples/{name}` regenerates from `state.json`.",
        "", "The product is fictional; no real brand's identity is copied.", ""]
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    names = sys.argv[1:] or list(EXAMPLES)
    codes = [make(n) for n in names]
    sys.exit(max(codes))
