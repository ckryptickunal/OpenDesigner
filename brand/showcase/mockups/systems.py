#!/usr/bin/env python3
"""Run the OpenDesigner engine for mockup scenes 01-07, the way a user's agent would.
Every command and its output goes to <piece>/engine-log.txt.

WARNING: re-running a piece deletes and rebuilds its opendesigner/ folder (and feedback.md inside it).

  python3 brand/showcase/mockups/systems.py [01-phone-trio ...]
"""
import json, shutil, subprocess, sys, pathlib

ROOT = pathlib.Path("/Users/Kunal/Desktop/Design-System")
E = "skills/opendesigner/scripts/engine.py"

PIECES = {
    "01-phone-trio": dict(name="Evening Apps Case Study", brand="#5B4FC4", feel="calm,premium,minimal", text="Manrope",
        extra=[("raw.neutralTint", '"brand"', "the field is a lilac mist taken from the brand, not a grey")],
        dials=dict(expression=(45, "the work is the show; the scene stays quiet"), brandPresence=(35, "violet only tints the field"),
                   density=(10, "three objects and one line of text"), energy=(20, "floating, still"),
                   roundness=(80, "phones have big soft corners"), depth=(85, "the whole idea is objects at different depths"),
                   colorfulness=(30, "one tinted field; the screens bring the colour"), warmth=(35, "cool mist so the dusk screens glow"))),
    "02-laptop-desk": dict(name="Halde Studio Desk", brand="#D7351F", feel="calm,sober,understated", text="Inter",
        dials=dict(expression=(35, "a photograph does the mood; type is a credit line"), brandPresence=(20, "red appears only as one dot"),
                   density=(10, "one object on a table"), energy=(15, "afternoon light"),
                   roundness=(20, "machined aluminium, tight radii"), depth=(60, "a real object casting a real shadow"),
                   colorfulness=(15, "plaster grey, oak, aluminium"), warmth=(30, "cool grade on the photo"))),
    "03-watch-trio": dict(name="Wrist Studio", brand="#5CC8FF", feel="premium,sleek,bold", text="Sora", dark=True,
        dials=dict(expression=(60, "product photography: light is the drama"), brandPresence=(25, "blue only as a caption dot"),
                   density=(10, "three objects"), energy=(35, "still, but crisp highlights"),
                   roundness=(70, "watch cases are rounded squares"), depth=(90, "specular light, reflections, contact shadow"),
                   colorfulness=(25, "graphite; the screens bring colour"), warmth=(20, "cool studio grey"))),
    "04-browser-cascade": dict(name="Index of Heroes", brand="#FF4F00", feel="minimal,technical,refined", text="Geist",
        dials=dict(expression=(55, "editorial: a numbered index and exact steps"), brandPresence=(30, "one orange index mark"),
                   density=(35, "five windows, five labels"), energy=(25, "precise, not lively"),
                   roundness=(25, "browser chrome with small radii"), depth=(55, "stacked windows need shadow to separate"),
                   colorfulness=(15, "paper and ink; the heroes bring colour"), warmth=(20, "cool paper white"))),
    "05-components-board": dict(name="Components Board", brand="#C6F432", feel="techy,minimal,bold", text="Instrument Sans", dark=True,
        dials=dict(expression=(50, "a studio's components page"), brandPresence=(25, "lime only marks scale"),
                   density=(40, "five tiles in a bento"), energy=(30, "calm board"),
                   roundness=(55, "tiles with medium corners"), depth=(20, "flat tiles on black, hairline borders"),
                   colorfulness=(20, "black board; components bring colour"), warmth=(35, "neutral black, no brown"))),
    "06-poster-street": dict(name="Howl Hill Billboard", brand="#FFD400", feel="bold,energetic,playful", text="Archivo",
        dials=dict(expression=(70, "a festival billboard at golden hour"), brandPresence=(60, "festival yellow on the board"),
                   density=(10, "one billboard"), energy=(55, "summer evening"),
                   roundness=(10, "billboard edges are square"), depth=(40, "a real photo; shadows come from the sun"),
                   colorfulness=(55, "golden hour sky and yellow print"), warmth=(45, "warm light lives in the photo, not the neutrals"))),
    "07-tablet-clinic": dict(name="Vigil Ward Tablet", brand="#127C7C", feel="calm,trustworthy,clean", text="Source Sans 3",
        dials=dict(expression=(35, "clinical calm"), brandPresence=(30, "teal only in the caption mark"),
                   density=(15, "one tablet on a table"), energy=(15, "night shift quiet"),
                   roundness=(60, "tablet corners"), depth=(55, "a device lying on a surface with window light"),
                   colorfulness=(20, "white table, teal accent"), warmth=(25, "clean daylight white"))),
}


def run(log, *args):
    cmd = ["python3", E] + list(args)
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    log.write("$ " + " ".join(json.dumps(a) if (" " in a or not a) else a for a in cmd) + f"\n{out}\n(exit {p.returncode})\n\n")
    return p.returncode, out


def main(slug):
    c = PIECES[slug]
    folder = ROOT / "brand/showcase/mockups" / slug
    folder.mkdir(parents=True, exist_ok=True)
    for x in ("opendesigner", "DESIGN.md", "PRODUCT.md"):
        t = folder / x
        if t.is_dir():
            shutil.rmtree(t)
        elif t.exists():
            t.unlink()
    d = f"brand/showcase/mockups/{slug}/opendesigner"
    with open(folder / "engine-log.txt", "w") as log:
        run(log, "--dir", d, "sketch", "--name", c["name"], "--brand", c["brand"], "--audience", "regular",
            "--platforms", "web", "--feel", c["feel"], "--surfaces", "case study:experience",
            "--delegated", "feel,audience,platforms")
        run(log, "--dir", d, "set", "raw.textFace", json.dumps(c["text"]), "--set-by", "chosen",
            "--why", "open-licence face (SIL OFL) picked for this scene; one family per scene")
        run(log, "--dir", d, "set", "raw.fontLicence", json.dumps({"web": True, "app": True, "selfHost": True}),
            "--set-by", "chosen", "--why", f"{c['text']} is SIL OFL, loaded from Google Fonts")
        if c.get("dark"):
            run(log, "--dir", d, "pick", "Q-color-21", "near-black", "--set-by", "chosen", "--why", "dark studio scene")
        for k, v, why in c.get("extra", []):
            run(log, "--dir", d, "set", k, v, "--set-by", "delegated", "--why", why)
        for k, (v, why) in c["dials"].items():
            run(log, "--dir", d, "set", f"dials.{k}", str(v), "--set-by", "delegated", "--why", why)
        rc, out = run(log, "--dir", d, "build")
    print(f"{slug}: build exit {rc}")
    print("\n".join(l for l in out.splitlines() if l.strip().startswith(("WARN", "ERROR", "Passes", "Fails", "built", "warning", "error"))))


if __name__ == "__main__":
    for s in (sys.argv[1:] or PIECES):
        main(s)
