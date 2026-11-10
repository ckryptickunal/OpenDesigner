#!/usr/bin/env python3
"""Run the OpenDesigner engine for the watch pieces, the way a user's agent would. Logs every command to <piece>/engine-log.txt.

WARNING: re-running deletes and rebuilds <piece>/opendesigner, which also removes feedback.md and any later
engine changes (07 had a colorfulness 15 -> 45 -> 15 test after this ran; see its decisions.md).

  python3 brand/showcase/watch/systems.py [01-ridgeline-trail ...]
"""
import json, shutil, subprocess, sys, pathlib

ROOT = pathlib.Path("/Users/Kunal/Desktop/Design-System")
E = "skills/opendesigner/scripts/engine.py"
WHY_DARK = "Brief: smartwatch app, black background edge-to-edge (watch platform convention, OLED); no light mode"

PIECES = {
    "01-ridgeline-trail": dict(name="Ridgeline", brand="#C8FF2E", feel="energetic,bold,futuristic", text="Archivo", display=None, mono=None,
        dials=dict(expression=(80, "bold mid-run energy"), brandPresence=(85, "the acid green is the identity"),
                   density=(25, "glanceable at arm's length; few items"), energy=(90, "race-day urgency"),
                   roundness=(15, "angular, cut corners like rock strata"), depth=(10, "flat OLED; no shadows on black"),
                   colorfulness=(60, "one loud accent plus status"), warmth=(35, "cool-neutral so the green burns"))),
    "02-thrum-heart": dict(name="Thrum", brand="#FF5436", feel="bold,warm,strong", text="Bricolage Grotesque", display=None, mono=None,
        dials=dict(expression=(70, "big numerals are the show"), brandPresence=(70, "warm red owns the screen"),
                   density=(25, "one number, one bar"), energy=(75, "live, beating data"),
                   roundness=(55, "soft but not bubbly"), depth=(20, "flat with a warm glow"),
                   colorfulness=(70, "five zone colors in one warm family"), warmth=(50, "owner rule: high warmth turns the neutrals brown; the warmth lives in the zone colors, not the greys"))),
    "03-tidemark-face": dict(name="Tidemark", brand="#5CC8FF", feel="calm,fresh,sleek", text="Sora", display=None, mono=None,
        dials=dict(expression=(60, "the sky is the art"), brandPresence=(50, "blue lives in the sky, not the chrome"),
                   density=(45, "a face carries several complications"), energy=(30, "slow tides"),
                   roundness=(70, "circular complications"), depth=(35, "layered sky"),
                   colorfulness=(55, "a cool family of blues"), warmth=(15, "cold sea air"))),
    "04-headway-transit": dict(name="Headway", brand="#FFCC1A", feel="bold,practical,authoritative", text="Overpass", display=None, mono=None,
        dials=dict(expression=(55, "signage, not decoration"), brandPresence=(75, "yellow is wayfinding"),
                   density=(50, "a departure board needs rows"), energy=(50, "countdown urgency without panic"),
                   roundness=(0, "hard signage edges"), depth=(0, "flat enamel signs"),
                   colorfulness=(30, "yellow, white, one alert"), warmth=(55, "sodium-lamp yellow"))),
    "05-nook-home": dict(name="Nook", brand="#FFB54A", feel="warm,cozy,gentle", text="Nunito", display=None, mono=None,
        dials=dict(expression=(45, "calm controls"), brandPresence=(55, "amber is lamp light"),
                   density=(20, "three big tiles per screen"), energy=(25, "evening, unhurried"),
                   roundness=(95, "pillowy tiles"), depth=(55, "soft glow lifts active tiles"),
                   colorfulness=(50, "amber plus warm neutrals"), warmth=(50, "owner rule: high warmth made brown-black tiles; amber carries the warmth, neutrals stay neutral"))),
    "06-hush-breathe": dict(name="Hush", brand="#B9A6FF", feel="calm,gentle,elegant", text="Fraunces", display=None, mono=None,
        dials=dict(expression=(65, "the orb is the interface"), brandPresence=(40, "quiet presence"),
                   density=(10, "one word on screen"), energy=(10, "slow breath"),
                   roundness=(100, "everything is a circle"), depth=(30, "glow, not shadow"),
                   colorfulness=(35, "lavender only"), warmth=(55, "soft dusk"))),
    "07-leeward-sail": dict(name="Leeward", brand="#EDE4CC", feel="technical,classic,sober", text="IBM Plex Sans", display=None, mono="IBM Plex Mono",
        dials=dict(expression=(35, "an instrument, not a poster"), brandPresence=(30, "bone linework, no brand color fills"),
                   density=(60, "an instrument shows several readings"), energy=(20, "steady helm"),
                   roundness=(30, "hairlines and ticks"), depth=(0, "flat chart"),
                   colorfulness=(15, "bone plus port red and starboard green only"), warmth=(45, "chart paper"))),
    "08-onething-focus": dict(name="Onething", brand="#FF4F9A", feel="minimal,focused,understated", text="Geist", display=None, mono="Geist Mono",
        dials=dict(expression=(30, "nothing extra"), brandPresence=(35, "one accent ring only"),
                   density=(20, "one task, one timer"), energy=(30, "steady focus"),
                   roundness=(60, "round ring, soft buttons"), depth=(0, "flat black"),
                   colorfulness=(15, "monochrome plus one pink"), warmth=(40, "neutral"))),
}


def run(log, *args):
    cmd = ["python3", E] + list(args)
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    log.write("$ " + " ".join(json.dumps(a) if " " in a else a for a in cmd) + f"\n{out}\n(exit {p.returncode})\n\n")
    return p.returncode, out


def main(slug):
    c = PIECES[slug]
    folder = ROOT / "brand/showcase/watch" / slug
    folder.mkdir(parents=True, exist_ok=True)
    for x in ("opendesigner", "DESIGN.md", "PRODUCT.md"):
        t = folder / x
        if t.is_dir():
            shutil.rmtree(t)
        elif t.exists():
            t.unlink()
    d = f"brand/showcase/watch/{slug}/opendesigner"
    logp = folder / "engine-log.txt"
    with open(logp, "w") as log:
        run(log, "--dir", d, "sketch", "--name", c["name"], "--brand", c["brand"], "--audience", "large",
            "--platforms", "watch", "--feel", c["feel"], "--delegated", "feel,audience,platforms")
        run(log, "--dir", d, "standard", "override", "STD-visual-details-24", "--why", WHY_DARK)
        run(log, "--dir", d, "pick", "Q-theme-01", "dark-only", "--set-by", "chosen", "--why", "watch app: black edge-to-edge, per the brief")
        run(log, "--dir", d, "pick", "Q-color-21", "black", "--set-by", "chosen", "--why", "watch: pure black OLED edge-to-edge")
        run(log, "--dir", d, "pick", "Q-plat-02", "watch", "--set-by", "chosen", "--why", "the product is a watch app")
        run(log, "--dir", d, "pick", "Q-plat-04", "watch", "--set-by", "chosen", "--why", "used on the wrist, in seconds")
        run(log, "--dir", d, "set", "raw.textFace", json.dumps(c["text"]), "--set-by", "chosen", "--why", "open-licence face picked for the direction")
        if c.get("display"):
            run(log, "--dir", d, "set", "raw.displayFace", json.dumps(c["display"]), "--set-by", "chosen", "--why", "display face")
        if c.get("mono"):
            run(log, "--dir", d, "set", "raw.monoFace", json.dumps(c["mono"]), "--set-by", "chosen", "--why", "tabular readouts")
        run(log, "--dir", d, "set", "raw.baseSize", "17", "--set-by", "chosen", "--why", "watchOS Body at the xLarge default for 44/45/49 mm is 17 pt (HIG typography, watchOS Dynamic Type)")
        for k, (v, why) in c["dials"].items():
            run(log, "--dir", d, "set", f"dials.{k}", str(v), "--set-by", "delegated", "--why", why)
        rc, out = run(log, "--dir", d, "build")
    print(f"{slug}: build exit {rc}")
    print("\n".join(l for l in out.splitlines() if l.startswith(("WARN", "ERROR", "Passes", "Fails", "built"))))


if __name__ == "__main__":
    for s in (sys.argv[1:] or PIECES):
        main(s)
