#!/usr/bin/env python3
"""Tests for css_scan.py and read_page.js (reference measurement). Standard library only, no network.
The read_page.js tests need Node and are skipped without it. Fixtures are small pages written here.

    python3 skills/opendesigner-extract/scripts/test_extract.py
"""
import importlib.util, json, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import css_scan  # noqa: E402

NODE = shutil.which("node")
ENGINE = next((p for p in (HERE / "engine.py", HERE.parent.parent / "opendesigner" / "scripts" / "engine.py") if p.exists()), None)

# A docs-like page: many short nav and caption rules, headings, one body size, slate text colors,
# a decorative chromatic blob, 1 px radius on inline links, pills as badges, a white fade "shadow".
SITE_CSS = """
:root { --brand: #5469d4; --radius-control: 6px; --shadow-card: 0 2px 5px rgba(60,66,87,.08), 0 1px 1px rgba(0,0,0,.12); }
html { font-size: 16px; }
body { font-size: 16px; color: #3c4257; font-family: "Sohne", -apple-system, sans-serif; }
p { font-size: 1rem; color: #3c4257; }
li { font-size: 16px; }
h1 { font-size: 48px; text-shadow: 0 1px 2px #000; }
h2 { font-size: 32px; } h3 { font-size: 24px; } h4 { font-size: 20px; }
nav a { font-size: 14px; color: #414552; border-radius: 1px; }
.nav-item { font-size: 14px; } .nav-link { font-size: 14px; } .menu-item { font-size: 14px; }
.sidebar-link { font-size: 14px; } .breadcrumb { font-size: 14px; }
.caption { font-size: 12px; } .legal { font-size: 12px; } small { font-size: 12px; } footer p { font-size: 12px; }
a { color: var(--brand); border-radius: 1px; }
a.inline { border-radius: 1px; } .prose a { border-radius: 1px; }
.btn { border-radius: var(--radius-control); background: var(--brand); color: #fff;
       transition: opacity .2s cubic-bezier(0.25, 0.1, 0.25, 1), transform 300ms linear(0, 0.5 50%, 1); }
.btn-secondary { border-radius: 6px; background: #fff; color: #3c4257; border: 1px solid #d4dee9; }
input, select { border-radius: 6px; border: 1px solid #d4dee9; }
:focus-visible { outline: 2px solid #5469d4; }
[aria-selected="true"] { background: #5469d4; color: #fff; }
.badge { border-radius: 9999px; background: #e5edf5; } .pill { border-radius: 9999px; } .tag { border-radius: 9999px; }
.avatar { border-radius: 50%; }
.card { border-radius: 12px; box-shadow: var(--shadow-card); background: #fff; }
.modal { border-radius: 12px; box-shadow: 0 15px 35px rgba(50,50,93,.1), 0 5px 15px rgba(0,0,0,.07); }
.fade-edge { box-shadow: 0 0 64px 64px rgba(255,255,255,.75); }
.hidden-ring { box-shadow: 0 0 0 0 rgba(0,0,0,0); }
.hero-blob { background: #ff5996; } .hero-blob-2 { background: #ffc043; }
.heading-slate { color: #0a2540; }
"""

SYSTEM_ONLY_CSS = "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; }"


def scan(css, name="site.css"):
    d = Path(tempfile.mkdtemp())
    (d / name).write_text(css, encoding="utf-8")
    try:
        return css_scan.analyse(css_scan.scan_files([str(d)]))
    finally:
        shutil.rmtree(d)


class Helpers(unittest.TestCase):
    def test_split_top_keeps_function_commas(self):
        v = "opacity .2s cubic-bezier(0.25, 0.1, 0.25, 1), transform 300ms linear(0, 0.5 50%, 1), color 1s ease"
        self.assertEqual(len(css_scan.split_top(v)), 3)
        self.assertIn("cubic-bezier(0.25, 0.1, 0.25, 1)", css_scan.split_top(v)[0])

    def test_parse_color_forms(self):
        self.assertEqual(css_scan.parse_color("#abc"), ("#aabbcc", 1.0))
        self.assertEqual(css_scan.parse_color("rgba(84, 105, 212, 0.5)"), ("#5469d4", 0.5))
        self.assertEqual(css_scan.parse_color("rgb(84 105 212 / 50%)"), ("#5469d4", 0.5))
        self.assertEqual(css_scan.parse_color("hsl(0, 100%, 50%)")[0], "#ff0000")
        L, C, H = css_scan.oklch("#5469d4")
        back = css_scan.parse_color(f"oklch({L} {C} {H})")[0]  # oklch() rounds to 3 decimals
        self.assertTrue(all(abs(int(back[i:i + 2], 16) - int("5469d4"[i - 1:i + 1], 16)) <= 2 for i in (1, 3, 5)), back)
        self.assertEqual(css_scan.parse_color("transparent")[1], 0.0)

    def test_shadow_classification(self):
        cls = lambda s: css_scan.classify_layer(css_scan.parse_shadow_layer(s))
        self.assertEqual(cls("0 0 64px 64px rgba(255,255,255,.75)"), "fade")
        self.assertEqual(cls("rgba(0, 0, 0, 0) 0px 0px 0px 1px"), "transparent")
        self.assertEqual(cls("rgb(84, 105, 212) 0px 0px 0px 1px"), "ring")
        self.assertEqual(cls("inset 0 1px 0 rgba(0,0,0,.1)"), "inset")
        self.assertEqual(cls("0 1px 1px rgba(0,0,0,.12)"), "low")
        self.assertEqual(cls("rgba(50, 50, 93, 0.12) 0px 16px 32px 0px"), "high")
        self.assertEqual(cls("0 30px 60px -12px rgba(50,50,93,.25)"), "overlay")


class DeclaredScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = scan(SITE_CSS)

    def test_body_size_is_running_text_not_nav_or_captions(self):
        t = self.a["type"]
        self.assertEqual(t["body"]["px"], 16)
        self.assertEqual(self.a["bodySize"], 16)
        self.assertEqual(t["scale"]["base"], 16)
        self.assertEqual(t["largestHeading"]["px"], 48)
        self.assertEqual(t["headingRatio"]["value"], 3.0)

    def test_accent_from_interactive_skips_neutrals(self):
        c = self.a["color"]
        self.assertEqual(c["accents"][0]["hex"], "#5469d4")
        hexes = [x["hex"] for x in c["accents"]]
        for gray in ("#3c4257", "#414552", "#ffffff", "#000000", "#d4dee9"):
            self.assertNotIn(gray, hexes)
        self.assertNotIn("#ff5996", hexes)  # decorative, not interactive
        self.assertIn(c["confidence"], ("high", "medium"))
        self.assertTrue({"button", "focus", "selected", "link"} <= set(c["accents"][0]["sources"]))

    def test_radius_control_and_container_apart(self):
        r = self.a["radius"]
        self.assertEqual(r["control"]["px"], 6)
        self.assertEqual(r["container"]["px"], 12)
        self.assertEqual(r["mostCommon"], 6)
        self.assertGreaterEqual(r["ignored"].get("link", 0), 3)
        self.assertGreaterEqual(r["ignored"].get("decor", 0), 3)

    def test_shadows_ignore_fades_and_text_shadows(self):
        d = self.a["depth"]
        self.assertEqual(d["hint"], "shadow-ladder")
        joined = " ".join(d["shadows"])
        self.assertNotIn("255, 255, 255", joined)
        self.assertNotIn("64px", joined)
        self.assertIn("fade", d["ignored"])
        self.assertEqual({l["level"] for l in d["levels"]}, {"low", "medium", "overlay"})  # 35 px modal blur = overlay
        self.assertEqual(d["count"], 3)  # .card (via var), --shadow-card token, .modal

    def test_motion_keeps_easing_commas(self):
        m = self.a["motion"]
        self.assertIn("cubic-bezier(0.25, 0.1, 0.25, 1)", m["easings"])
        self.assertIn("linear(0, 0.5 50%, 1)", m["easings"])
        self.assertEqual(sorted(m["durations"]), [200.0, 300.0])

    def test_identity_and_confidence(self):
        t = self.a["type"]
        self.assertEqual(t["families"], ["Sohne"])
        self.assertFalse(t["primaryIsSystem"])
        s = self.a["summary"]
        for k in ("bodySize", "headingRatio", "accent", "radiusControl", "radiusContainer", "depth", "motionMedianMs"):
            self.assertIn(k, s)
            self.assertIn(s[k]["confidence"], ("high", "medium", "low"))
            self.assertIsInstance(s[k]["count"], int)
        self.assertNotIn("#5469d4", json.dumps(s))  # the summary never offers the hue as a value
        self.assertEqual(self.a["identity"]["accentHue"], "#5469d4")
        self.assertIn("never values to adopt", self.a["identity"]["rule"])

    def test_system_faces_are_not_identity(self):
        a = scan(SYSTEM_ONLY_CSS)
        self.assertEqual(a["type"]["families"], [])
        self.assertTrue(a["type"]["primaryIsSystem"])
        self.assertIn("-apple-system", a["type"]["systemFaces"])

    def test_html_inline_styles_and_style_blocks(self):
        html = """<html><head><style>.card{border-radius:10px} p{font-size:17px}</style></head>
        <body><button class="cta" style="border-radius: 4px; background: #1f6f5c">Go</button>
        <a href="#" style="border-radius:1px">link</a></body></html>"""
        a = scan(html, "index.html")
        self.assertEqual(a["radius"]["control"]["px"], 4)
        self.assertEqual(a["radius"]["container"]["px"], 10)
        self.assertEqual(a["bodySize"], 17)
        self.assertEqual(a["color"]["accents"][0]["hex"], "#1f6f5c")

    def test_resets_vars_and_unknown_class_names(self):
        css = """:root { --font-text: "Inter", sans-serif; }
        button, input, select { border-radius: 0; font-family: inherit; }
        body { font-family: var(--font-text); }
        .TransactionRow { border-radius: 10px; } .surface { border-radius: 10px; } .avatar { border-radius: 50%; }"""
        a = scan(css)
        self.assertEqual(a["type"]["families"], ["Inter"])
        self.assertEqual(a["radius"]["control"]["px"], 10)
        self.assertEqual(a["radius"]["control"]["confidence"], "low")

    def test_report_is_readable(self):
        text = css_scan.report(self.a)
        self.assertIn("Body size: 16 px", text)
        self.assertIn("Control radius: 6 px", text)
        self.assertIn("[", text)


def capture(**values):
    base = {k: {} for k in ("colors", "fontFamilies", "fontSizes", "lineHeights", "fontWeights", "spacing",
                            "radii", "shadows", "durations", "easings")}
    base.update(values)
    return {"source": "fixture", "method": "computed", "elements": 400, "values": base}


class ComputedCapture(unittest.TestCase):
    def test_old_capture_without_roles_falls_back_with_low_confidence(self):
        # the shape the designer tester saved: counts only, header nav first in DOM order
        a = css_scan.analyse(capture(fontSizes={"16": 460, "12": 18, "20": 10, "11": 5, "34": 4, "14": 1},
                                     radii={"1": 31, "5": 10, "6": 8, "100": 3},
                                     colors={"#3c4257": 300, "#5469d4": 113, "#ffffff": 23},
                                     easings={"cubic-bezier(0.25": 150}))
        self.assertEqual(a["bodySize"], 16)
        self.assertEqual(a["type"]["body"]["confidence"], "low")
        self.assertEqual(a["radius"]["mostCommon"], 5)  # 1 px corners dropped
        self.assertEqual(a["color"]["accents"][0]["hex"], "#5469d4")
        self.assertEqual(a["color"]["confidence"], "low")

    def test_ring_colors_count_toward_accent(self):
        a = css_scan.analyse(capture(shadows={"rgb(84, 105, 212) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 1px 1px 0px": 4}))
        self.assertEqual(a["depth"]["hint"], "ring+faint-shadow")
        self.assertEqual(a["color"]["accents"][0]["hex"], "#5469d4")
        self.assertNotIn("84, 105, 212", " ".join(a["depth"]["shadows"]))


@unittest.skipUnless(NODE, "node not installed")
class ReadPageJs(unittest.TestCase):
    """read_page.js core (collect) on synthetic element descriptions, then css_scan on its output."""

    def node(self, script):
        r = subprocess.run([NODE, "-e", script], capture_output=True, text=True, timeout=30,
                           env={"RP": str(HERE / "read_page.js"), "PATH": ""})
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def collect(self, items):
        return self.node("const a=require(process.env.RP);const r=a.collect(" + json.dumps(items) + ",1280);"
                         "console.log(JSON.stringify({source:'fixture',method:'computed',elements:" + str(len(items)) +
                         ",values:r.values,targetsUnder24:r.targetsUnder24}))")

    def test_directory_page_reads_card_copy(self):
        # a docs hub: 16 px product names and link lists, 14 px one-line descriptions, no paragraphs
        base = {"w": 200, "h": 20, "ctx": None, "prose": False, "linkText": False, "fontFamily": "-apple-system",
                "fontWeight": "400", "lineHeight": "20px", "radius": "0px", "boxShadow": "none", "spacing": []}
        items = [{**base, "own": 30, "fontSize": 14} for _ in range(30)]
        items += [{**base, "own": 10, "fontSize": 16, "linkText": True} for _ in range(20)]
        items += [{**base, "own": 22, "fontSize": 16, "prose": True, "linkText": True} for _ in range(10)]
        items += [{**base, "own": 24, "fontSize": 32, "ctx": "heading"}]
        a = css_scan.analyse(self.collect(items))
        self.assertEqual(a["bodySize"], 14)
        self.assertEqual(a["type"]["body"]["confidence"], "medium")
        self.assertIn("mostly short text", a["type"]["body"]["basis"])
        self.assertEqual(a["type"]["families"], [])
        self.assertTrue(a["type"]["primaryIsSystem"])

    def test_split_and_durations(self):
        out = self.node("const a=require(process.env.RP);console.log(JSON.stringify(["
                        "a.splitTop('cubic-bezier(0.25, 0.1, 0.25, 1), linear(0, 0.25 25%, 1), ease'),"
                        "a.toMs('0.3s'), a.toMs('150ms'), a.radiusValue('50%', 40, 40), a.radiusValue('9999px', 80, 32),"
                        "a.radiusValue('6px', 80, 32), a.parseRgb('rgba(84, 105, 212, 0.5)')]))")
        self.assertEqual(out[0], ["cubic-bezier(0.25, 0.1, 0.25, 1)", "linear(0, 0.25 25%, 1)", "ease"])
        self.assertEqual(out[1:6], [300, 150, "full", "full", 6])
        self.assertEqual(out[6], {"hex": "#5469d4", "a": 0.5})
        vis = self.node("const a=require(process.env.RP);console.log(JSON.stringify(["
                        "a.shadowVisible('rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px'),"
                        "a.shadowVisible('rgba(0, 0, 0, 0.12) 0px 1px 1px 0px'), a.shadowVisible('none'),"
                        "a.shadowVisible('rgb(227, 232, 238) 0px -1px 0px 0px inset')]))")
        self.assertEqual(vis, [False, True, False, False])

    def test_collect_then_scan(self):
        items = []
        white, ink, accent, slate = ({"hex": h, "a": 1} for h in ("#ffffff", "#0a2540", "#533afd", "#50617a"))
        none = {"hex": "#000000", "a": 0}
        base = {"w": 100, "h": 20, "own": 0, "ctx": None, "prose": False, "buttonLike": False, "link": False,
                "formField": False, "selected": False, "media": False, "containerHint": False, "fontSize": 16,
                "fontFamily": "sohne-var", "fontWeight": "400", "lineHeight": "normal", "color": slate, "bg": none,
                "border": None, "accentColor": None, "radius": "0px", "boxShadow": "none", "spacing": [],
                "transition": ["all", "0s", "ease"], "animation": None}
        el = lambda **k: items.append({**base, **k})
        for _ in range(60):  # header nav: many short 14 px labels
            el(own=8, ctx="nav", fontSize=14)
        for _ in range(12):  # running text at 16 px (fewer elements, more characters)
            el(own=220, prose=True, fontSize=16)
        for _ in range(6):   # short 16 px card labels
            el(own=12, fontSize=16)
        el(own=30, ctx="heading", fontSize=56, color=ink)
        el(own=20, ctx="heading", fontSize=32, color=ink)
        for _ in range(3):   # small print
            el(own=90, ctx="caption", fontSize=12, prose=True)
        for _ in range(30):  # inline links with a 1 px radius
            el(own=10, prose=True, link=True, radius="1px", color=accent)
        for _ in range(4):   # pill buttons
            el(own=10, ctx="control", buttonLike=True, w=120, h=36, radius="9999px", bg=accent, color=white,
               transition=["opacity, transform", "0.3s, 150ms", "cubic-bezier(0.25, 0.1, 0.25, 1), linear(0, 0.5 50%, 1)"])
        for _ in range(3):   # cards
            el(w=320, h=200, radius="8px", bg=white,
               boxShadow="rgba(50, 50, 93, 0.12) 0px 16px 32px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px")
        el(w=900, h=40, radius="0px", boxShadow="rgba(255, 255, 255, 0.75) 0px 0px 64px 64px")  # fade glow
        el(w=40, h=20, radius="9999px", bg={"hex": "#e5edf5", "a": 1})  # badge
        for _ in range(10):  # transparent accordion buttons (shadow reset to transparent): no visible corner
            el(own=30, ctx="control", buttonLike=True, w=450, h=60, radius="0px",
               boxShadow="rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px")
        for _ in range(20):  # a link list at 14 px inside li: labels, not running text
            el(own=25, prose=True, linkText=True, link=True, fontSize=14, color=accent)
        cap = self.collect(items)
        v = cap["values"]
        self.assertEqual(v["radiiByRole"]["control"], {"full": 4})
        self.assertEqual(v["textSizes"]["label"]["14"], 500)
        self.assertIn("cubic-bezier(0.25, 0.1, 0.25, 1)", v["easings"])
        self.assertIn("linear(0, 0.5 50%, 1)", v["easings"])
        a = css_scan.analyse(cap)
        self.assertEqual(a["bodySize"], 16)
        self.assertEqual(a["type"]["body"]["confidence"], "high")
        self.assertEqual(a["type"]["headingRatio"]["value"], 3.5)
        self.assertEqual(a["radius"]["control"]["px"], "full")
        self.assertEqual(a["radius"]["container"]["px"], 8)
        self.assertEqual(a["radius"]["ignored"]["link"], 30)
        self.assertEqual(a["color"]["accents"][0]["hex"], "#533afd")
        self.assertNotIn("#50617a", [x["hex"] for x in a["color"]["accents"]])
        self.assertEqual(a["depth"]["hint"], "shadow-ladder")
        self.assertEqual(a["depth"]["ignored"].get("fade"), 1)
        self.assertEqual(sorted(a["motion"]["durations"]), [150.0, 300.0])
        self.assertEqual(a["type"]["families"], ["sohne-var"])
        cap["values"]["fontFamilies"] = {"-apple-system": 1966, "Menlo": 1003, "Source Code Pro": 20}
        t = css_scan.analyse(cap)["type"]
        self.assertEqual((t["families"], t["minorFaces"], t["primaryIsSystem"]), ([], ["Source Code Pro"], True))


@unittest.skipUnless(ENGINE, "engine.py not found")
class EngineIntakeCompat(unittest.TestCase):
    """engine.py intake reads css_scan --json output unchanged (read-only use of the engine)."""

    def test_intake_reads_body_radius_accent(self):
        spec = importlib.util.spec_from_file_location("od_engine", ENGINE)
        eng = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(eng)
        a = scan(SITE_CSS)
        a["tag"] = "inspiration"
        fit = eng.fit_reference(json.loads(json.dumps(a)))
        by = {p["path"]: p for p in fit["proposals"]}
        self.assertIn("dials.roundness", by)
        self.assertIn("6", by["dials.roundness"]["basis"])
        self.assertIn("dials.density", by)
        self.assertIn("16", by["dials.density"]["basis"])
        self.assertIn("dials.colorfulness", by)
        self.assertNotIn("raw.brandColor", by)  # inspiration: the accent hue is never proposed


if __name__ == "__main__":
    unittest.main(verbosity=1)
