#!/usr/bin/env python3
"""Tests for engine.py (standard library unittest; no network).

    python3 skills/opendesigner/scripts/test_engine.py        (or: python3 -m unittest test_engine)
"""
import contextlib
import copy
import io
import json
import os
import re
import sys
import tempfile
import unittest
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine as e  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def quiet(fn, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **k)


def state_with(**raw):
    s = e.default_state("Test")
    for k, v in raw.items():
        if k in e.DIALS:
            s["dials"][k] = v
        else:
            s["raw"][k] = v
    return s


class ColorMath(unittest.TestCase):
    def test_wcag_contrast_known_values(self):
        self.assertAlmostEqual(e.contrast("#000000", "#ffffff"), 21.0, places=6)
        self.assertAlmostEqual(e.contrast("#ffffff", "#ffffff"), 1.0, places=6)
        self.assertAlmostEqual(e.contrast("#767676", "#ffffff"), 4.54, places=2)  # the classic lightest AA gray on white
        self.assertLess(e.contrast("#777777", "#ffffff"), 4.5)                     # one step lighter fails; no rounding
        self.assertAlmostEqual(e.contrast("#959595", "#ffffff"), 3.0, places=1)

    def test_apca_reference_values(self):
        self.assertAlmostEqual(e.apca_lc("#000000", "#ffffff"), 106.04, places=1)
        self.assertAlmostEqual(e.apca_lc("#ffffff", "#000000"), -107.88, places=1)

    def test_oklch_round_trip_and_hct_chroma(self):
        for hx in ("#5b5bd6", "#0f62fe", "#ffdd00", "#1a7f37", "#123456"):
            self.assertEqual(e.oklch_to_hex(*e.hex_to_oklch(hx)), hx)
        hue, chroma = e.cam16_hue_chroma(e.hex_to_linear("#0000ff"))  # Material HCT blue: hue 282.8, chroma 87.2
        self.assertAlmostEqual(hue, 282.76, delta=0.1)
        self.assertAlmostEqual(chroma, 87.23, delta=0.1)


class Ramps(unittest.TestCase):
    def test_lightness_monotonic(self):
        for brand in ("#5b5bd6", "#0f62fe", "#e11d48", "#1a7f37", None):
            s = state_with(brandColor=brand)
            ramps, _ = e.build_palette(e.merge_defaults(s), e.derive_params(s, e.resolve_dials(s)[0])[0])
            for (name, mode), r in ramps.items():
                # solids that carry dark text (steps 9-10, an amber for example) sit off the ramp order, as in Radix amber;
                # every other step, and every step of a ramp with white-text solids, is ordered by luminance
                order = list(range(1, 13)) if r.text_on_solid == "light" else [1, 2, 3, 4, 5, 6, 7, 8, 11, 12]
                ys = [r.y(i) for i in order]
                for a, b, i in zip(ys, ys[1:], order[1:]):
                    if mode == "light":
                        self.assertGreaterEqual(a, b, f"{name} {mode} step {i}")
                    else:
                        self.assertLessEqual(a, b, f"{name} {mode} step {i}")

    def test_contrast_targets_by_construction(self):
        s = state_with(brandColor="#5b5bd6")
        ramps, _ = e.build_palette(e.merge_defaults(s), e.derive_params(s, e.resolve_dials(s)[0])[0])
        n = ramps[("neutral", "light")]
        self.assertGreaterEqual(e.contrast(n.steps[8]["hex"], n.steps[3]["hex"]), 3.0)   # step 8: 3:1 boundaries
        self.assertGreaterEqual(e.contrast(n.steps[11]["hex"], n.steps[4]["hex"]), 4.5)  # step 11: text on 1-4
        self.assertGreaterEqual(e.contrast(n.steps[12]["hex"], n.steps[5]["hex"]), 7.0)  # step 12: 7:1
        dark1 = ramps[("neutral", "dark")].steps[1]["hex"]
        self.assertTrue(e.luminance("#121212") <= e.luminance(dark1) <= e.luminance("#1a1a1a"))  # DC-L01-19 band

    def test_dark_is_not_an_inversion(self):
        files, meta, _ = e.generate_system(state_with(brandColor="#5b5bd6"))
        light = e.resolve_all(files, {"theme": "light"})
        dark = e.resolve_all(files, {"theme": "dark"})
        inv = lambda hx: "#" + "".join(f"{255 - v:02x}" for v in e.hex_to_rgb8(hx))
        same = sum(1 for p in light if light[p]["type"] == "color" and p.startswith("color.text.")
                   and e.hex_of(dark[p]["resolved"]) == inv(e.hex_of(light[p]["resolved"])))
        self.assertEqual(same, 0)


class TypeScale(unittest.TestCase):
    SPECTRUM_DESKTOP = [10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 51, 58, 65, 73]  # S-L02-020, S-L02-021
    MATERIAL = [11, 12, 14, 16, 22, 24, 28, 32, 36, 45, 57]                                     # S-L02-005

    def test_spectrum_2_desktop_and_mobile(self):
        self.assertEqual(e.type_scale_sizes(14, 1.125, -3, 14), self.SPECTRUM_DESKTOP)
        mobile = e.type_scale_sizes(17, 1.125, 0, 14)
        self.assertEqual((mobile[0], mobile[-1]), (17, 88))

    def test_material_matches_except_24_and_57(self):
        sizes = set(e.type_scale_sizes(14, 1.125, -3, 15))
        self.assertTrue(set(self.MATERIAL) - {24, 57} <= sizes)
        self.assertIn(58, sizes)       # 14 x 1.125^12 = 57.54 rounds to 58: Material's Display Large 57 is 1px below (LEVERS B6)
        self.assertNotIn(57, sizes)
        self.assertNotIn(24, sizes)    # Material's 24 is hand-placed

    def test_emphasized_variants_from_expression_67(self):
        """levers.json: type.emphasizedVariants is on at Expression 67-100 (DC-L02-11, S-L02-006)."""
        for expr, want in ((66, False), (67, True), (90, True)):
            s = state_with(expression=expr)
            files, meta, _ = e.generate_system(s)
            flat = e.resolve_all(files, {"theme": "light"})
            emph = {k: v for k, v in flat.items() if k.startswith("text.emphasized.")}
            self.assertEqual(bool(emph), want, expr)
            for k, v in emph.items():
                base = flat["text." + k[len("text.emphasized."):]]["resolved"]
                self.assertGreater(v["resolved"]["fontWeight"], base["fontWeight"], k)
                self.assertEqual(v["resolved"]["fontSize"], base["fontSize"], k)
            rep = e.Report()
            e.validate_files(files, s, rep)
            self.assertEqual(rep.count("error"), 0)
            self.assertFalse(any("text styles" in i["message"] for i in rep.items), expr)  # variants are not extra levels
        self.assertIn(".ds-text-emphasized-body-md", e.export_css(files, meta, "ds"))

    def test_ratio_capped_by_density(self):
        s = state_with(expression=90, density=90)
        p, _ = e.derive_params(s, e.resolve_dials(s)[0])
        self.assertEqual(p["type.ratio"], 1.2)


class Scales(unittest.TestCase):
    def test_space_ladders(self):
        self.assertEqual(e.space_ladder(4), [0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96])  # Atlassian set + 96 (spec 6.2)
        self.assertTrue({0, 5, 10, 15, 20, 25, 30, 40, 50, 60} <= set(e.space_ladder(5)))            # GOV.UK (S-L09-508)
        files, _m, _c = e.generate_system(state_with())
        desc = files["primitives.tokens.json"]["space"]["$description"]
        self.assertIn(", 20, 24]", desc)                     # the $description names every multiplier, up to x24 (space.96)
        self.assertIn("96", files["primitives.tokens.json"]["space"])

    def test_spring_conversion(self):
        files, meta, _ = e.generate_system(state_with(energy=80))
        flat = e.resolve_all(files, {})
        ext = flat["motion.spring.spatial.default"]["$extensions"]["opendesigner"]
        self.assertAlmostEqual(ext["apple"]["duration"], 2 * 3.141592653589793 / 380 ** 0.5, places=3)  # 0.322s (LEVERS B11)
        self.assertTrue(ext["css"]["easing"].startswith("linear("))
        self.assertAlmostEqual(ext["apple"]["bounce"], 1 - ext["spring"]["dampingRatio"], places=3)

    def test_recipes_reproduce_their_signatures(self):
        """LEVERS C recipes are fixtures (spec 6.2). Known, documented deviations are listed, not hidden."""
        known = {("Apple HIG (iOS 26)", "controlMd"): "44pt comes from the platform, not the density bands"}
        misses = []
        for rc in e.levers()["recipes"]:
            s = e.default_state()
            s["dials"].update(rc["dials"])
            raw = rc["raw"]
            for k in ("baseSize", "spaceUnit", "productType", "marketingSurfaces", "platforms"):
                if k in raw:
                    s["raw"][k] = raw[k]
            if isinstance(raw.get("brandColor"), str) and raw["brandColor"].startswith("#"):
                s["raw"]["brandColor"] = raw["brandColor"]
            s["overrides"] = dict(rc.get("overrides") or {})
            _f, meta, _c = e.generate_system(s)
            got = {"radius": meta["shape"]["control"], "body": meta["type"]["base"], "ratio": meta["type"]["ratio"],
                   "controlMd": meta["density"][meta["params"]["space.densityMode"]["value"]]["control"]["md"]}
            for k, v in rc["expected"].items():
                if k in got and (isinstance(v, (int, float)) or v == "full") and (rc["system"], k) not in known and got[k] != v:
                    misses.append((rc["system"], k, v, got[k]))
        self.assertEqual(misses, [])


class Validate(unittest.TestCase):
    def test_generated_system_passes(self):
        files, meta, _ = e.generate_system(state_with(brandColor="#5b5bd6"))
        rep = e.Report()
        e.validate_files(files, state_with(brandColor="#5b5bd6"), rep)
        self.assertEqual([i for i in rep.items if i["severity"] == "error"], [])

    def test_catches_a_failing_pair(self):
        s = state_with(brandColor="#5b5bd6")
        s["overrides"]["light:color.text.secondary"] = "{color.neutral.light.6}"  # a detached value that breaks 4.5:1
        files, _m, _c = e.generate_system(s)
        rep = e.Report()
        e.validate_files(files, s, rep)
        errs = [i for i in rep.items if i["severity"] == "error" and i["category"] == "contrast"]
        self.assertTrue(errs)
        self.assertTrue(all(i["measured"] < i["threshold"] for i in errs))
        self.assertIn("SC 1.4.3", errs[0]["rule"])

    def test_catches_small_target_and_missing_reduced_motion(self):
        s = state_with()
        s["overrides"]["size.target.pointer"] = {"value": 20, "unit": "px"}
        files, _m, _c = e.generate_system(s)
        del files["opendesigner.resolver.json"]["modifiers"]["motion"]
        files["opendesigner.resolver.json"]["resolutionOrder"] = [x for x in files["opendesigner.resolver.json"]["resolutionOrder"]
                                                                   if "motion" not in x["$ref"]]
        rep = e.Report()
        e.validate_files(files, s, rep)
        cats = {(i["category"], i["severity"]) for i in rep.items}
        self.assertIn(("targets", "error"), cats)
        self.assertTrue(any("reduced-motion" in i["message"] for i in rep.items if i["severity"] == "error"))

    def test_examples_pass(self):
        for name in ("devtool-dense", "consumer-playful", "public-service-accessible"):
            d = os.path.join(REPO, "examples", name)
            if os.path.exists(os.path.join(d, "state.json")):
                rep = e.validate_dir(d)
                self.assertEqual(rep.count("error"), 0, name)


class Exports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.d = os.path.join(cls.tmp.name, "opendesigner")
        quiet(e.cmd_init, cls.d, name="Export test")
        quiet(e.cmd_set, cls.d, "raw.brandColor", "#0f62fe", "test")
        cls.files, cls.meta, _ = quiet(e.cmd_generate, cls.d)
        quiet(e.cmd_export, cls.d, "all", cls.files, cls.meta)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def read(self, *p):
        with open(os.path.join(self.d, *p), encoding="utf-8") as f:
            return f.read()

    def test_json_exports_parse(self):
        for p in (("build", "figma", "variables.json"), ("build", "paper", "tokens.json"), ("build", "dtcg", "export-test.resolver.json"),
                  ("build", "figma", "import", "Color.Light.tokens.json"), ("tokens", "opendesigner.resolver.json")):
            json.loads(self.read(*p))
        fig = json.loads(self.read("build", "figma", "variables.json"))
        self.assertEqual([c["name"] for c in fig["collections"]][:2], ["Primitives", "Color"])
        self.assertTrue(all(len(v.get("codeSyntax", {})) <= 3 for c in fig["collections"] for v in c["variables"]))

    def test_css_has_variables_and_modes(self):
        css = self.read("build", "css", "tokens.css")
        for needle in ("--ds-color-text-primary:", "--ds-space-inset-md:", "--ds-radius-control:", "prefers-color-scheme: dark",
                       '[data-theme="dark"]', "prefers-reduced-motion: reduce", "--ds-motion-transition-move-duration: 0ms"):
            self.assertIn(needle, css)
        self.assertEqual(css.count("{"), css.count("}"))

    def test_platform_files(self):
        self.assertIn("@theme inline", self.read("build", "tailwind", "theme.css"))
        self.assertIn("enum Colors", self.read("build", "swift", "DesignTokens.swift"))
        self.assertIn("data class DsColors(", self.read("build", "compose", "DesignTokens.kt"))

    def test_deterministic(self):
        f2, _m, _c = e.generate_system(e.read_json(os.path.join(self.d, "state.json")))
        for name, data in f2.items():
            self.assertEqual(json.dumps(data, indent=2, ensure_ascii=False) + "\n", self.read("tokens", name), name)
        self.assertEqual(e.export_css(f2, _m, "ds"), self.read("build", "css", "tokens.css"))


class TokenNames(unittest.TestCase):
    def test_path_segments_are_lowercase_kebab(self):
        """Spec 7.4 (decided 2026-09-24): every token path segment is lowercase kebab-case, e.g. color.bg.accent.bold-hover."""
        seg = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
        for dials, raw in (({}, {}), ({"expression": 90, "depth": 95}, {"platforms": ["ios", "web"], "focusColor": "#ffdd00",
                                                                          "secondaryColors": ["#e11d48"]}), ({"depth": 5}, {"contrastTarget": "AAA"})):
            s = state_with(**raw)
            s["dials"].update(dials)
            files, _m, _c = e.generate_system(s)
            for fn, data in files.items():
                if fn.endswith(".tokens.json"):
                    bad = [p for p in e.flatten(data) if not all(seg.match(x) for x in p.split("."))]
                    self.assertEqual(bad, [], fn)
        flat = e.resolve_all(files, {"theme": "light"})
        for p in ("color.bg.accent.bold-hover", "color.text.on-accent", "color.bg.action.primary-pressed", "radius.control-sm"):
            self.assertIn(p, flat)


class StateAndLog(unittest.TestCase):
    def test_set_status_supersede_and_lock(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Log test")
            quiet(e.cmd_set, d, "answers.Q-aud-01", "dense", "delegated: pick for me")
            quiet(e.cmd_set, d, "Q-aud-01", "regular", "changed my mind")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual(st["answers"]["Q-aud-01"]["value"], "regular")
            self.assertEqual(st["dials"]["density"]["value"], 50)
            with open(os.path.join(d, "decisions.md"), encoding="utf-8") as f:
                log = f.read()
            self.assertIn("set_by: delegated", log)
            self.assertRegex(log, r"## D-0003 · answers\.Q-aud-01 = \"regular\"\n- set_by: chosen · locked: no · date: [\d-]+ · supersedes: D-0002")
            quiet(e.cmd_lock, d, "dials.roundness")
            with self.assertRaises(SystemExit):
                quiet(e.cmd_set, d, "dials.roundness", 80, "should be refused")

    def test_zoom_and_sketch(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Sketch", "#5b5bd6", "regular", "web", "friendly", "system-light-dark", quiet=True)
            z = e.zoom_levels(d, e.merge_defaults(e.read_json(os.path.join(d, "state.json"))))
            self.assertEqual({v["level"] for v in z.values()}, {"sketch"})   # a sketch alone reads 'sketch' everywhere (U5 F23)
            self.assertEqual(z["color"]["next"], ["Q-color-02"])
            files, meta, _ = e.generate_system(e.read_json(os.path.join(d, "state.json")))
            rep = e.Report()
            e.validate_files(files, e.read_json(os.path.join(d, "state.json")), rep)
            self.assertEqual(rep.count("error"), 0)  # Level 0 alone gives a complete, valid system


class AnswersAndBuild(unittest.TestCase):
    """U1 consistency items 4-6, 10 and 11 (research/U1-consistency-findings.md)."""

    def test_principles_come_from_q_brand_07(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Principles")
            quiet(e.cmd_set, d, "Q-brand-07", ["Clarity over flourish", "Accessible, always"], "ranked")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual(st["principles"], ["Clarity over flourish", "Accessible, always"])
            quiet(e.cmd_set, d, "Q-brand-07", {"format": "imperatives", "principles": ["Do less, better"]}, "dict form")
            self.assertEqual(e.read_json(os.path.join(d, "state.json"))["principles"], ["Do less, better"])
            quiet(e.cmd_set, d, "Q-brand-07", "generate", "format only: principles stay")
            self.assertEqual(e.read_json(os.path.join(d, "state.json"))["principles"], ["Do less, better"])
            quiet(e.cmd_build, d)
            with open(os.path.join(t, "PRODUCT.md"), encoding="utf-8") as f:
                self.assertIn("1. Do less, better", f.read())
            with open(os.path.join(t, "DESIGN.md"), encoding="utf-8") as f:
                self.assertNotIn("Q-brand-04", f.read())

    def test_q_tool_03_sets_the_figma_plan(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Plan")
            for answer, plan in (("figma-starter", "starter"), ("figma-org", "organization"), ("figma-ent", "enterprise"),
                                 ("figma-pro", "professional")):
                quiet(e.cmd_set, d, "Q-tool-03", answer, "plan")
                self.assertEqual(e.read_json(os.path.join(d, "state.json"))["exports"]["figmaPlan"], plan)
            quiet(e.cmd_set, d, "Q-tool-03", "paper", "not Figma: the plan is left alone")
            self.assertEqual(e.read_json(os.path.join(d, "state.json"))["exports"]["figmaPlan"], "professional")

    def test_q_dir_01_default_applies_until_answered(self):
        qs = e.read_json(os.path.join(e.REFERENCES, "questions.json"))["questions"]
        self.assertEqual(next(q for q in qs if q["id"] == "Q-dir-01")["default_value"], e.DEFAULT_PRESET)
        s = e.default_state()
        dials, src, _ = e.resolve_dials(s)
        preset = next(p for p in e.levers()["presets"] if p["id"] == e.DEFAULT_PRESET)
        for k, v in preset["dials"].items():
            self.assertEqual(dials[k], v, k)
            self.assertEqual(src[k], "preset:" + e.DEFAULT_PRESET)
        s["answers"]["Q-dir-01"] = {"value": "custom", "set_by": "chosen"}   # answered with no preset: coupling rules apply
        self.assertEqual(e.resolve_dials(s)[1]["expression"], "default")
        s["preset"] = "tonal"
        self.assertEqual(e.resolve_dials(s)[0]["roundness"], 95)

    def test_starting_inventory_matches_q_comp_02(self):
        q = next(x for x in e.read_json(os.path.join(REPO, "synthesis", "questionnaire.json"))["questions"] if x["id"] == "Q-comp-02")
        core = next(o for o in q["options"] if o["value"] == "core-25")
        listed = [c.strip() for c in core["effect"].split("[")[0].rstrip(". ").split(",")]
        self.assertEqual(len(listed), 25)
        self.assertEqual(len(e.DEFAULT_COMPONENTS), len(listed))
        self.assertTrue(q["default"].startswith("core-25"))

    def test_surface_mode_q_scope_06(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Surfaces")
            quiet(e.cmd_set, d, "Q-scope-06", "read", "docs site")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual((st["raw"]["productType"], st["raw"]["marketingSurfaces"]), ("content", False))
            self.assertEqual(st["context"]["surfaces"], [])            # a bare mode names no surfaces
            _f, meta, _c = e.generate_system(st)
            self.assertEqual(meta["type"]["base"], 16)                  # Read: 16px body at middle density (DC-L02-08)
            quiet(e.cmd_set, d, "Q-scope-06", ["Console:operate", {"name": "Landing", "mode": "Persuade"}], "two surfaces")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual((st["raw"]["productType"], st["raw"]["marketingSurfaces"]), ("work-tool", True))
            self.assertEqual(st["context"]["surfaces"], [{"name": "Console", "mode": "Operate"}, {"name": "Landing", "mode": "Persuade"}])
            self.assertEqual(e.resolve_dials(st)[0], e.resolve_dials(e.default_state())[0])  # no dial moves (Q-scope-06 Dials line)
            quiet(e.cmd_build, d)
            with open(os.path.join(t, "PRODUCT.md"), encoding="utf-8") as f:
                self.assertIn("- Landing: Persuade mode (density spacious; one hero line per page", f.read())
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(SystemExit):
                quiet(e.cmd_sketch, os.path.join(t, "opendesigner"), "Bad", surfaces="app:sell")

    def test_design_md_three_voice_layout_and_asset_names(self):
        """assets/output/DESIGN.md: zoom line, one plain sentence, the 'Designers · Code' line, detail folded (THREE-VOICES)."""
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Voices", "#167874", quiet=False)
            with open(os.path.join(t, "DESIGN.md"), encoding="utf-8") as f:
                text = f.read()
            for title in ("Overview", "Colors", "Typography", "Layout", "Shapes", "Motion", "Accessibility"):
                sec = text.split(f"\n## {title}\n", 1)[1].split("\n## ", 1)[0]
                lines = [x for x in sec.split("\n") if x.strip()]
                self.assertTrue(lines[0].startswith("> Zoom:"), title)
                self.assertTrue(lines[1].startswith("<!-- od:zoom"), title)
                self.assertTrue(lines[2].startswith("**"), title)
                self.assertRegex(lines[3], r"^Designers: .+ · Code: `.+`$", title)
                self.assertEqual(lines[4], "<details><summary>More</summary>", title)
                self.assertIn("</details>", sec, title)
                if title == "Colors":
                    self.assertIn("#167874", lines[2])                     # the plain sentence names the brand color
            rep = e.validate_dir(d)
            note = next(i for i in rep.items if i["category"] == "hooks")
            self.assertNotIn("H-logo", e.plain_of(note))
            self.assertIn("logo, wordmark", e.plain_of(note))
            self.assertIn("H-logo", note["where"])                        # ids stay in the machine-readable field

    def test_build_stops_before_export_on_errors(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Stops")
            quiet(e.cmd_set, d, "size.target.pointer", {"value": 20, "unit": "px"}, "too small on purpose")
            self.assertIn("size.target.pointer", e.read_json(os.path.join(d, "state.json"))["overrides"])  # flat key, not nested
            self.assertEqual(quiet(e.cmd_build, d), 1)
            self.assertTrue(os.path.isdir(os.path.join(d, "tokens")))
            self.assertFalse(os.path.exists(os.path.join(d, "build")))
            self.assertFalse(os.path.exists(os.path.join(t, "DESIGN.md")))
            self.assertEqual(quiet(e.cmd_build, d, force=True), 1)
            self.assertTrue(os.path.exists(os.path.join(d, "build", "css", "tokens.css")))
            quiet(e.cmd_set, d, "size.target.pointer", {"value": 24, "unit": "px"}, "back to the floor")
            self.assertEqual(quiet(e.cmd_build, d), 0)


class Intake(unittest.TestCase):
    SCAN = {"method": "computed", "color": {"accents": [{"hex": "#7170ff"}], "neutralTint": {"chroma": 0.012, "hue": 260}},
            "type": {"families": ["Inter"], "scale": {"base": 14, "ratio": 1.2, "meanLogResidual": 0.01}},
            "space": {"unit": 4}, "radius": {"mostCommon": 6}, "depth": {"hint": "ring+faint-shadow", "shadows": []},
            "motion": {"median": 180, "durationMultiplier": 0.65, "easings": []}}

    def test_fits_dials_and_keeps_identity_out(self):
        fit = e.fit_reference(dict(self.SCAN, tag="inspiration"))
        got = {p["path"]: p["value"] for p in fit["proposals"]}
        self.assertEqual(got["dials.roundness"], 42)        # 6px -> band 38-47 (A5)
        self.assertEqual(got["raw.spaceUnit"], 4)
        self.assertNotIn("raw.brandColor", got)             # another brand's hue is never carried (spec 5.4)
        self.assertNotIn("raw.textFace", got)
        self.assertNotIn("dials.brandPresence", got)
        own = {p["path"] for p in e.fit_reference(dict(self.SCAN, tag="our-product"))["proposals"]}
        self.assertIn("raw.brandColor", own)
        self.assertEqual(e.fit_reference(dict(self.SCAN, tag="competitor"))["proposals"], [])


class ReviewAndFeedback(unittest.TestCase):
    def test_review_finds_bypasses_and_stale_sections(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Review test")
            quiet(e.cmd_build, d)
            os.makedirs(os.path.join(t, "src"))
            with open(os.path.join(t, "src", "a.css"), "w") as f:
                f.write(".x { color: #ff0000; padding: 12px; border-radius: 6px; }\n.y { color: #00ff00; } /* od-ignore */\n"
                        ".z { color: var(--ds-color-text-primary); gap: var(--ds-space-8); }\n")
            with open(os.path.join(t, "src", "V.swift"), "w") as f:
                f.write("let c = Color(red: 0.1, green: 0.2, blue: 0.3)\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                e.cmd_review(d, as_json=True)
            res = json.loads(out.getvalue())
            self.assertEqual(res["counts"], {"color": 2, "size": 1, "radius": 1})
            self.assertFalse(any(f_["line"] == 2 and f_["file"].endswith("a.css") for f_ in res["findings"]))
            self.assertEqual(res["staleSections"], [])
            with open(os.path.join(t, "DESIGN.md"), encoding="utf-8") as f:
                text = f.read()
            with open(os.path.join(t, "DESIGN.md"), "w", encoding="utf-8") as f:
                f.write(text.replace("## Motion\n", "## Motion\n\nold text\n"))
            self.assertEqual(quiet(e.cmd_review, d, strict=True), 1)

    def test_review_finds_shadows_and_durations(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Review shadows")
            quiet(e.cmd_set, d, "dials.depth", 68, "shadow ladder")
            quiet(e.cmd_build, d)
            os.makedirs(os.path.join(t, "src"))
            with open(os.path.join(t, "src", "b.css"), "w") as f:
                f.write(".card { box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2); }\n"        # 1 shadow (not also a color)
                        ".menu { transition: opacity .2s ease-out; }\n"                  # 2 duration 200ms
                        ".spin { animation: spin 1s linear infinite; }\n"                # 3 looping: skipped
                        ".ok { box-shadow: var(--ds-elevation-raised); transition: opacity var(--ds-motion-duration-short); }\n"
                        "  --card-box-shadow: 0 1px 2px #000;\n"                     # 5 token definition: skipped
                        ".img { filter: drop-shadow(0 2px 4px black); animation-duration: 250ms; }\n")  # 6 shadow + duration
            with open(os.path.join(t, "src", "S.swift"), "w") as f:
                f.write("view.shadow(color: .black, radius: 8)\nwithAnimation(.easeOut(duration: 0.25)) { }\n")
            with open(os.path.join(t, "src", "C.kt"), "w") as f:
                f.write("val spec = tween<Float>(durationMillis = 300)\nModifier.shadow(8.dp)\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                e.cmd_review(d, as_json=True)
            res = json.loads(out.getvalue())
            self.assertEqual(res["counts"], {"shadow": 4, "duration": 4})
            got = {(f_["file"].split(os.sep)[-1], f_["line"], f_["kind"]): f_["fix"] for f_ in res["findings"]}
            self.assertIn("--ds-elevation-overlay", got[("b.css", 1, "shadow")])      # 24px blur -> overlay role
            self.assertIn("--ds-elevation-raised", got[("b.css", 6, "shadow")])       # 4px blur -> raised role
            self.assertIn("--ds-motion-transition-feedback-duration", got[("b.css", 2, "duration")])  # a 200ms opacity change is feedback
            self.assertIn("DSMotion.duration", got[("S.swift", 2, "duration")].replace(".Motion.", "Motion."))
            self.assertTrue(got[("C.kt", 1, "duration")].endswith("Ms"))
            self.assertNotIn(("b.css", 3, "duration"), got)

    def test_feedback_records_and_builds_issue_link(self):
        with tempfile.TemporaryDirectory() as t:
            url = quiet(e.cmd_feedback, t, "Spacing step names confuse beginners & experts", "confusing")
            u = urlparse(url)
            self.assertEqual(f"{u.scheme}://{u.netloc}{u.path}", "https://github.com/ckryptickunal/OpenDesigner/issues/new")
            q = parse_qs(u.query)
            self.assertTrue(q["title"][0].startswith("[confusing] Spacing step names"))
            self.assertIn("confusing", q["labels"][0])
            self.assertIn("&", q["body"][0])  # encoded, not split
            with open(os.path.join(t, "feedback.md"), encoding="utf-8") as f:
                self.assertIn("## F-001", f.read())
            with self.assertRaises(SystemExit):
                e.cmd_feedback(t, "x", "rant")


class JourneyTracking(unittest.TestCase):
    """The engine logs its own steps to the private journey log, and only after the person's yes (journey.py)."""

    def events(self, d):
        return [(x["event"], x["step"], x["data"]) for x in e.journey.read_events(e.journey.jpath(d, "events.jsonl"))]

    def test_nothing_is_logged_without_a_yes(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Quiet")
            quiet(e.main, ["--dir", d, "pick", "Q-shape-01", "soft", "--no-doc"])
            self.assertEqual(self.events(d), [])

    def test_engine_logs_its_own_steps(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Tracked")
            e.journey.set_tracking(d, True)
            quiet(e.cmd_set, d, "context.product", "a recipe app for families", "their words")
            quiet(e.cmd_sketch, d, "Tracked", None, "regular", "web", "friendly")
            got = self.events(d)
            answered = {s: x.get("how") for ev, s, x in got if ev == "step_answered"}
            self.assertEqual(answered, {"Q-scope-01": "free", "Q-aud-01": "option", "Q-plat-01": "option", "Q-brand-01": "option"})
            self.assertIn(("export", None, {"kind": "all"}), got)
            self.assertEqual(got[-1][:2], ("level_complete", None))
            quiet(e.main, ["--dir", d, "pick", "Q-shape-01", "soft", "--no-doc"])
            quiet(e.main, ["--dir", d, "pick", "Q-shape-01", "subtle", "--set-by", "delegated", "--no-doc"])
            self.assertEqual(self.events(d)[-3:], [("step_answered", "Q-shape-01", {"how": "option"}),
                                                   ("step_changed", "Q-shape-01", {}),
                                                   ("step_answered", "Q-shape-01", {"how": "delegated"})])
            quiet(e.cmd_set, d, "size.target.pointer", {"value": 20, "unit": "px"}, "too small on purpose")
            quiet(e.main, ["--dir", d, "generate"])
            self.assertEqual(quiet(e.main, ["--dir", d, "validate"]), 1)
            self.assertEqual(self.events(d)[-1][:2], ("error", "validate"))
            self.assertEqual(json.dumps(self.events(d)).count("recipe"), 0)   # never the answer itself

    def test_feedback_from_journey_adds_hotspots(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Hot")
            with self.assertRaises(SystemExit):
                quiet(e.main, ["--dir", d, "feedback", "--from-journey"])
            e.journey.set_tracking(d, True)
            e.journey.log(d, "step_shown", step="Q-color-02")
            e.journey.log(d, "frustration", signal="said", note="Priya hates teal")
            e.journey.log(d, "frustration", signal="repeat_question")
            quiet(e.main, ["--dir", d, "feedback", "--from-journey"])
            with open(os.path.join(d, "feedback.md"), encoding="utf-8") as f:
                text = f.read()
            self.assertIn("confusing", text)
            self.assertIn("Frustration: Q-color-02 (2)", text)
            self.assertNotIn("Priya", text)
            self.assertEqual(self.events(d)[-1], ("feedback_filed", None, {"kind": "confusing"}))


def u5_state(**raw):
    s = e.default_state("U5 test")
    s["raw"]["brandColor"] = "#2563eb"
    s["raw"]["platforms"] = ["ios", "web"]
    for k, v in raw.items():
        s["raw"][k] = v
    return e.merge_defaults(s)


def token_hash(state):
    files, _m, _c = e.generate_system(state)
    return json.dumps({k: v for k, v in files.items() if k != "opendesigner.meta.json"}, sort_keys=True)


def option_value(qid, v):
    """A realistic answer value for one listed option of a question."""
    if qid == "Q-brand-01":
        return {v[:1]: 20}
    if qid == "Q-aud-02" and v == "state-*":
        return "state-anxious"
    if qid == "Q-plat-01":
        return [v]
    return v


class AnswerCoverage(unittest.TestCase):
    """U5 fix 1: every answer reaches the system, or the engine says what it shapes instead. Never silent."""

    def test_every_option_has_an_effect_or_a_stated_record(self):
        qs = e.questions()
        self.assertGreaterEqual(len(qs), 190)
        silent = []
        for qid, q in qs.items():
            for v in e.option_values(q):
                eff, kind, _note = e.answer_outcome(qid, option_value(qid, v))
                if not eff and not kind:
                    silent.append(f"{qid}={v}")
        self.assertEqual(silent, [], "options that change nothing and say nothing")

    def test_mapped_questions_change_tokens(self):
        """Every question that is not declared record-only moves tokens: its options give at least two different systems."""
        base = u5_state()
        flat_only = []
        for qid, q in e.questions().items():
            if qid in e.ANSWER_RECORDS:
                continue
            hashes = set()
            for v in e.option_values(q):
                val = option_value(qid, v)
                s2 = copy.deepcopy(base)
                s2["answers"][qid] = {"value": val, "set_by": "chosen"}
                for pth, x in e.answer_effects(qid, val, s2).items():
                    e._store(s2, pth, x, "chosen", "t", False)
                hashes.add(token_hash(s2))
            if len(hashes) < 2:
                flat_only.append(qid)
        self.assertEqual(flat_only, [])

    def test_replies_say_what_changed(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="Replies")
            quiet(e.cmd_set, d, "raw.brandColor", "#2563eb", "brand")
            for qid, v, want in (("Q-form-02", "on-blur", "shapes DESIGN.md rules, not tokens"),
                                 ("Q-type-17", "capped-chrome", "build/"),
                                 ("Q-gov-01", "strict", "owner input"),
                                 ("Q-color-03", "vivid", "tokens:"),
                                 ("Q-type-01", "open-source", "not one of the listed options")):
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    e.cmd_set(d, "answers." + qid, v, "test")
                self.assertIn(want, out.getvalue(), qid)
            with open(os.path.join(d, "decisions.md"), encoding="utf-8") as f:
                self.assertIn("also set: dials.colorfulness = 92 (from Q-color-03)", f.read())

    def test_testers_answers_move_the_right_tokens(self):
        def apply(qid, v, s=None):
            s2 = copy.deepcopy(s or u5_state())
            for pth, x in e.answer_effects(qid, v, s2).items():
                e._store(s2, pth, x, "chosen", "t", False)
            files, meta, _c = e.generate_system(s2)
            return s2, files, meta
        _s, _f, tonal = apply("Q-color-03", "tonal")
        _s, _f, vivid = apply("Q-color-03", "vivid")
        self.assertGreater(vivid["color"]["peakHct"], tonal["color"]["peakHct"])
        s2, files, meta = apply("Q-color-04", "contrasting", u5_state(secondaryColors=["#ff9900"]))
        self.assertIn("accent2", meta["color"]["ramps"])
        self.assertEqual(meta["color"]["accentCount"], 2)
        _s, files, meta = apply("Q-color-09", "cool")
        self.assertAlmostEqual(meta["color"]["neutralTint"]["h"], 255.0, delta=1)
        _s, files, meta = apply("Q-color-19", "categorical-6-8")
        flat = e.resolve_all(files, {"theme": "light"})
        self.assertIn("color.chart.categorical.8", flat)
        rep = e.Report()
        e.validate_files(files, _s, rep)
        self.assertFalse([i for i in rep.items if i["category"] == "contrast" and "chart" in i["message"]])
        _s, files, meta = apply("Q-color-20", "overlay")
        flat = e.resolve_all(files, {"theme": "light"})
        self.assertEqual(flat["color.bg.action.primary-hover"]["$value"]["colorSpace"], "srgb")  # a composited state layer
        _s, files, meta = apply("Q-color-21", "black")
        self.assertEqual(meta["ramps"]["neutral"]["dark"]["hex"][0], "#000000")
        _s, files, meta = apply("Q-dir-02", "compact")
        self.assertEqual(meta["density"]["compact"]["control"]["md"], 32)
        _s, files, meta = apply("Q-color-02", "flooded-chrome", u5_state())
        self.assertEqual(e.resolve_all(files, {"theme": "light"})["color.surface.nav"]["$value"], "{color.accent.light.9}")
        _s, files, meta = apply("Q-form-01", "filled")
        self.assertEqual(e.resolve_all(files, {"theme": "light"})["color.bg.field"]["$value"], "{color.neutral.light.3}")


class BrandColor(unittest.TestCase):
    """U5 fix 2: a person's brand hex that passes is kept exactly; feel words never gray it out."""

    def test_exact_hex_on_primary_when_it_passes(self):
        for brand, feel in (("#2563eb", ["playful"]), ("#1f6f5c", ["serious", "minimal", "premium"]), ("#2563eb", ["serious", "minimal"])):
            s = u5_state()
            s["raw"]["brandColor"] = brand
            s["macros"] = feel
            files, meta, _c = e.generate_system(s)
            flat = e.resolve_all(files, {"theme": "light"})
            self.assertEqual(e.hex_of(flat["color.bg.action.primary"]["resolved"]), brand, (brand, feel))
            self.assertGreaterEqual(meta["dials"]["colorfulness"], 36)
            self.assertNotEqual(meta["color"]["scheme"], "monochrome")
            self.assertIn("exactly", e.brand_line(meta, s))

    def test_failing_hex_is_adjusted_and_explained(self):
        s = u5_state(brandColor="#7a7a7a")
        files, meta, _c = e.generate_system(s)
        self.assertIsNone(meta["color"]["pinnedStep"])
        line = e.brand_line(meta, s)
        self.assertIn("#7A7A7A", line)
        self.assertIn("color.brand.seed", line)
        self.assertEqual(line.count("\n"), 0)

    def test_seed_and_explicit_monochrome_are_honoured(self):
        s = u5_state()
        s["raw"]["flags"]["brandExact"] = False
        _f, meta, _c = e.generate_system(s)
        self.assertIsNone(meta["color"]["pinnedStep"])
        s = u5_state()
        s["dials"]["colorfulness"] = {"value": 5, "set_by": "chosen"}
        _f, meta, _c = e.generate_system(s)
        self.assertEqual(meta["color"]["scheme"], "monochrome")


class FeelWordsAndDelegation(unittest.TestCase):
    """U5 fixes 3 and 9."""

    def test_free_words_map_and_unknown_words_never_error(self):
        macros, mapping, unknown = e.feel_words(["fun!!", "calm", "techy", "a bit cozy", "zesty"])
        self.assertEqual(mapping["fun!!"], ["playful"])
        self.assertIn("deferential", mapping["calm"])
        self.assertEqual(mapping["techy"], ["modern"])
        self.assertEqual(mapping["a bit cozy"], ["friendly"])
        self.assertEqual(unknown, ["zesty"])
        for w in ("fun", "playful", "bright", "bold", "calm", "quiet", "serious", "minimal", "friendly", "techy", "premium", "cozy"):
            self.assertTrue(e.feel_words([w])[0], w)
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(e.cmd_sketch(d, "Words", None, "regular", "web", "fun,quiet,zesty"), 0)
            self.assertIn("zesty", out.getvalue())
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual(st["macros"], ["playful", "deferential"])

    def test_sketch_delegated(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Ops", "#2563eb", "dense", "web", "serious,minimal", quiet=True, delegated="all")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual(st["answers"]["Q-aud-01"]["set_by"], "delegated")
            with open(os.path.join(d, "decisions.md"), encoding="utf-8") as f:
                log = f.read()
            self.assertRegex(log, r"## D-\d+ · macros = .*\n- set_by: delegated")
            self.assertRegex(log, r"## D-\d+ · raw.brandColor = .*\n- set_by: delegated")
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Ops", "#2563eb", "dense", "web", "serious", quiet=True, delegated="feel")
            st = e.read_json(os.path.join(d, "state.json"))
            self.assertEqual(st["answers"]["Q-aud-01"]["set_by"], "chosen")
            with self.assertRaises(SystemExit):
                e.cmd_sketch(d, "Ops", delegated="colour")


class VisibleStates(unittest.TestCase):
    """U5 fix 4: hover and pressed differ visibly from the fill, including a pinned brand solid."""

    def test_states_differ_and_keep_text(self):
        for brand in ("#1f6f5c", "#2563eb", "#0a0a0a", "#ffdd00", "#e11d48"):
            for method in ("hybrid", "overlay"):
                s = u5_state(brandColor=brand, stateMethod=method)
                files, meta, _c = e.generate_system(s)
                for mode in ("light", "dark"):
                    flat = e.resolve_all(files, {"theme": mode})
                    H = lambda p: e.hex_of(flat[p]["resolved"])
                    for base, on in (("color.bg.action.primary", "color.text.on-action"), ("color.bg.accent.bold", "color.text.on-accent"),
                                     ("color.bg.danger.bold", "color.text.on-danger")):
                        hov = base + "-hover"
                        prs = base + "-pressed"
                        self.assertGreaterEqual(e.contrast(H(hov), H(base)), e.STATE_MIN["hover"] - 0.005, (brand, method, mode, hov))
                        self.assertGreaterEqual(e.contrast(H(prs), H(base)), e.STATE_MIN["pressed"] - 0.005, (brand, method, mode, prs))
                        self.assertGreaterEqual(e.contrast(H(on), H(hov)), 4.5, (brand, method, mode))
                        self.assertGreaterEqual(e.contrast(H(on), H(prs)), 4.5, (brand, method, mode))
                rep = e.Report()
                e.validate_files(files, s, rep)
                self.assertEqual([i["message"] for i in rep.items if i["severity"] == "error"], [], (brand, method))
                self.assertFalse([i for i in rep.items if i["category"] == "states"], (brand, method))
        s = u5_state(brandColor="#1f6f5c")
        files, _m, _c = e.generate_system(s)
        s["overrides"]["light:color.bg.action.primary-hover"] = "{color.accent.light.9}"
        files, _m, _c = e.generate_system(s)
        rep = e.Report()
        e.validate_files(files, s, rep)
        self.assertTrue([i for i in rep.items if i["category"] == "states"])


class PersonalOutputs(unittest.TestCase):
    """U5 fix 5: DESIGN.md opens with a plain summary that is true; the preview is the person's project."""

    def test_summary_names_and_facts(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_init, d, name="robotics-club-site")
            quiet(e.cmd_set, d, "context.product", "A website for our school robotics club, to get new members", "their words")
            quiet(e.cmd_sketch, d, "Robotics Club", "#2563EB", "large", "web", "fun,bright", surfaces="website:persuade")
            with open(os.path.join(t, "DESIGN.md"), encoding="utf-8") as f:
                text = f.read()
            front = text.split("---", 2)[1]
            self.assertLessEqual(len(front.strip().splitlines()), 18)                    # short front matter
            body = text.split("---", 2)[2]
            summary = body.split("\n> Generated", 1)[0].strip().splitlines()
            self.assertEqual(summary[0], "# Robotics Club")                             # --name wins over init's folder name
            self.assertLessEqual(len([x for x in summary if x.strip()]), 15)
            joined = "\n".join(summary)
            for want in ("school robotics club", "now and then", "website", "playful", "#2563EB", "exactly", "Next", "Licence risks"):
                self.assertIn(want, joined)
            self.assertNotIn("not recorded yet (Q-aud-01)", text)
            self.assertNotIn("not recorded yet (Q-scope-06)", text)
            self.assertNotIn("defined (2 of 3)", text)
            with open(os.path.join(t, "PRODUCT.md"), encoding="utf-8") as f:
                prod = f.read()
            self.assertNotIn("Not recorded yet (Q-aud-01)", prod)
            self.assertNotIn("Not recorded yet (Q-scope-06)", prod)
            with open(os.path.join(d, "preview.html"), encoding="utf-8") as f:
                pv = f.read()
            self.assertIn("Robotics Club", pv)
            self.assertIn("Join us", pv)
            self.assertNotIn("acme", pv.lower())
            self.assertNotIn("Invite your team", pv)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                e.cmd_review(d)
            self.assertIn("No code yet", out.getvalue())

    def test_preview_follows_the_surface(self):
        for surf, product, want in (("app:operate", "Internal admin for users and jobs", "Add user"),
                                    ("app:operate", "Personal finance: budgets and bills", "Add transaction"),
                                    ("docs:read", "Developer guides", "Getting started")):
            with tempfile.TemporaryDirectory() as t:
                d = os.path.join(t, "opendesigner")
                quiet(e.cmd_init, d, name="P")
                quiet(e.cmd_set, d, "context.product", product, "x")
                quiet(e.cmd_sketch, d, "Pilot", None, "regular", "web", surfaces=surf)
                with open(os.path.join(d, "preview.html"), encoding="utf-8") as f:
                    self.assertIn(want, f.read(), surf)

    def test_zoom_follows_question_levels(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Z", "#2563eb", "regular", "web", "calm", quiet=True)
            quiet(e.cmd_set, d, "Q-color-02", "accent", "level 1")
            st = e.merge_defaults(e.read_json(os.path.join(d, "state.json")))
            self.assertEqual(e.zoom_levels(d, st)["color"]["level"], "broad")
            for q in ("Q-color-03", "Q-color-04", "Q-color-09", "Q-color-14", "Q-color-15"):
                quiet(e.cmd_set, d, q, e.questions()[q]["default_value"] or "tonal", "defined", set_by="delegated")
            st = e.merge_defaults(e.read_json(os.path.join(d, "state.json")))
            self.assertEqual(e.zoom_levels(d, st)["color"]["level"], "defined")
            quiet(e.cmd_set, d, "zoom.color", "broad", "the model ran level 1 only")
            st = e.merge_defaults(e.read_json(os.path.join(d, "state.json")))
            self.assertEqual(e.zoom_levels(d, st)["color"]["level"], "broad")


class PlatformsAndLicences(unittest.TestCase):
    """U5 fix 6: font licence scope per platform; iOS Dynamic Type."""

    def gen(self, lic, plats=("web", "ios")):
        s = u5_state(platforms=list(plats), textFace="Söhne", fontLicence=lic)
        files, meta, _c = e.generate_system(s)
        return s, files, meta

    def test_web_only_face_falls_back_in_apps(self):
        s, files, meta = self.gen({"web": True, "app": False, "selfHost": True})
        sw = e.export_swift(files, meta, "ds")
        kt = e.export_compose(files, meta, "ds")
        self.assertNotIn('Font.custom("Söhne"', sw)
        self.assertIn("not licensed for apps", sw)
        self.assertIn("Font.system(.body", sw)
        self.assertIn("not licensed for apps", kt)
        flat = e.resolve_all(files, {})
        self.assertEqual(flat["font.family.text"]["resolved"][0], "Söhne")        # the web keeps it
        self.assertTrue(any("not licensed for apps" in r for r in e.licence_risks(s, meta)))

    def test_app_licence_uses_dynamic_type_sizes(self):
        s, files, meta = self.gen({"web": True, "app": True, "selfHost": True})
        sw = e.export_swift(files, meta, "ds")
        self.assertIn('Font.custom("Söhne", size: 17, relativeTo: .body)', sw)
        self.assertNotIn("size: 14,", sw)
        s, files, meta = self.gen({"web": False, "app": False, "selfHost": False})
        self.assertEqual(e.resolve_all(files, {})["font.family.text"]["resolved"][0], "system-ui")
        rep = e.Report()
        s2, files2, meta2 = self.gen({})
        e.validate_files(files2, s2, rep)
        self.assertTrue([i for i in rep.items if i["category"] == "licence" and i["severity"] == "warn"])

    def test_q_type_02_web_only(self):
        eff = e.answer_effects("Q-type-02", "web-only")
        self.assertEqual(eff["raw.fontLicence"], {"web": True, "app": False, "selfHost": True})


class ReviewReactAndTailwind(unittest.TestCase):
    """U5 fix 7: review finds JSX and Tailwind drift and suggests tokens by role."""

    def test_jsx_tailwind_and_roles(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Ops", "#2563eb", "dense", "web", "serious", quiet=True)
            quiet(e.cmd_build, d)
            os.makedirs(os.path.join(t, "src"))
            with open(os.path.join(t, "src", "UserForm.jsx"), "w") as f:
                f.write("const s = { borderRadius: 10, padding: 20, fontSize: 15, boxShadow: '0 4px 12px rgba(0,0,0,0.15)', background: '#ffffff' };\n"
                        "export const B = () => <button style={{ background: '#2563eb', color: '#fff', transition: 'background 250ms' }}>Save</button>;\n"
                        "export const C = () => <div className=\"bg-[#2563eb] p-[13px] rounded-lg bg-blue-600 text-white text-lg shadow-md\">x</div>;\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                e.cmd_review(d, as_json=True)
            res = json.loads(out.getvalue())
            vals = {f_["value"]: f_["fix"] for f_ in res["findings"]}
            for want in ("borderRadius: 10", "padding: 20", "fontSize: 15", "#ffffff", "bg-[#2563eb]", "p-[13px]", "rounded-lg",
                         "bg-blue-600", "text-white", "text-lg", "shadow-md"):
                self.assertIn(want, vals, want)
            self.assertIn("action-primary", vals["#2563eb"])                     # a button fill gets the primary action, not info
            self.assertNotIn("info", vals["#2563eb"])
            self.assertIn("bg-action-primary", vals["bg-[#2563eb]"])
            self.assertIn("transition-feedback", [f_["fix"] for f_ in res["findings"] if f_["kind"] == "duration"][0])
            self.assertIn("off", vals["bg-blue-600"])                           # the reset removes default palette classes


class ExtendTokens(unittest.TestCase):
    """U5 fix 8: set adds a new token and keeps DTCG and density modes."""

    def test_new_and_changed_tokens(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Ext", "#2563eb", "dense", "web", quiet=True)
            quiet(e.cmd_set, d, "size.row.md", 36, "table rows")
            quiet(e.cmd_set, d, "compact:size.control.md", 30, "compact only")
            quiet(e.cmd_set, d, "space.inset.md", 12, "default density only")
            quiet(e.cmd_set, d, "color.bg.highlight", "#fff4c2", "new color")
            files, meta, _c = quiet(e.cmd_generate, d)
            self.assertEqual(files["semantic.tokens.json"]["size"]["row"]["md"]["$value"], {"value": 36, "unit": "px"})
            self.assertEqual(files["semantic.tokens.json"]["size"]["row"]["md"]["$type"], "dimension")
            dens = {n: files[f"semantic.density.{n}.tokens.json"] for n in e.DENSITIES}
            self.assertEqual(dens["compact"]["space"]["inset"]["md"]["$value"], {"value": 12, "unit": "px"})
            self.assertNotEqual(dens["spacious"]["space"]["inset"]["md"]["$value"], {"value": 12, "unit": "px"})
            self.assertEqual(dens["compact"]["size"]["control"]["md"]["$value"], {"value": 30, "unit": "px"})
            self.assertNotEqual(dens["comfortable"]["size"]["control"]["md"]["$value"], {"value": 30, "unit": "px"})
            for m in ("light", "dark"):
                self.assertEqual(files[f"semantic.color.{m}.tokens.json"]["color"]["bg"]["highlight"]["$value"]["hex"], "#fff4c2")
            rep = e.validate_dir(d)
            self.assertEqual(rep.count("error"), 0)
            n = len(e._decision_entries(d))
            with self.assertRaises(SystemExit):
                quiet(e.cmd_set, d, "size.row.md", "tall", "not a size")
            with self.assertRaises(SystemExit):
                quiet(e.cmd_set, d, "shape.blob", "wobbly", "type unknown")
            self.assertEqual(len(e._decision_entries(d)), n)                     # nothing logged for a refused change


class TailwindExport(unittest.TestCase):
    """U5 fix 10: one import, optional reset, class names in DESIGN.md."""

    def test_self_contained_theme(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "TW", "#2563eb", "dense", "web")
            with open(os.path.join(d, "build", "tailwind", "theme.css"), encoding="utf-8") as f:
                tw = f.read()
            code = [x for x in tw.splitlines() if x.strip() and not x.startswith(("/*", "   ")) and not x.strip().startswith(("@import \"tailwindcss\"", "@import \"<path"))]
            self.assertEqual(code[0], '@import "../css/tokens.css";')
            self.assertIn("--color-*: initial;", tw)
            self.assertIn("--spacing-control-md:", tw)
            self.assertNotIn("--spacing-size-", tw)
            with open(os.path.join(t, "DESIGN.md"), encoding="utf-8") as f:
                self.assertIn("`bg-action-primary`", f.read())
            quiet(e.cmd_set, d, "exports.tailwindReset", False, "keep Tailwind defaults")
            quiet(e.cmd_build, d)
            with open(os.path.join(d, "build", "tailwind", "theme.css"), encoding="utf-8") as f:
                self.assertNotIn("--color-*: initial;", f.read())


class ShowTemplates(unittest.TestCase):
    """U5 fix 11: engine.py show fills every template with real values."""

    def test_every_template_fills(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "opendesigner")
            quiet(e.cmd_sketch, d, "Showcase", "#1f6f5c", "regular", "web", "serious,minimal", quiet=True)
            for name in e.TEMPLATE_QUESTIONS:
                p = quiet(e.cmd_show, d, name)
                with open(p, encoding="utf-8") as f:
                    html = f.read()
                data = json.loads(re.search(r'<script type="application/json" id="od-data">(.*?)</script>', html, re.S).group(1).replace("<\\/", "</"))
                self.assertTrue(data["options"], name)
                self.assertIn("Showcase", data["title"], name)
                self.assertNotIn(">Acme<", html)
            pal = e.build_payload(e.merge_defaults(e.read_json(os.path.join(d, "state.json"))), "palette")
            accents = {o["value"]: o["ramps"][0]["light"][8] for o in pal["options"]}
            self.assertEqual(accents["tonal"], "#1f6f5c")                            # the brand stays exact in every option
            self.assertNotEqual(pal["options"][0]["ramps"][0]["light"][2], pal["options"][1]["ramps"][0]["light"][2])


class IntakeU5(unittest.TestCase):
    """Coordinator follow-ups: a tight key shadow no longer reads as deep; a face the person licenses may carry over."""

    def test_depth_weights_soft_shadows(self):
        ref = {"method": "computed", "depth": {"hint": "shadow-ladder", "shadows": ["0px 2px 2px rgba(0,0,0,0.3)"],
                                               "levels": [{"level": "low", "blur": 2, "y": 2, "alpha": 0.3, "count": 50},
                                                          {"level": "medium", "blur": 12, "y": 4, "alpha": 0.12, "count": 10}]}}
        got = {p["path"]: p["value"] for p in e.fit_reference(ref)["proposals"]}
        self.assertLessEqual(got["dials.depth"], 60)
        legacy = {"method": "computed", "depth": {"hint": "shadow-ladder", "shadows": ["0 2px 2px rgba(0,0,0,0.3)", "0 0 64px 64px rgba(255,255,255,0.75)"]}}
        self.assertLessEqual({p["path"]: p["value"] for p in e.fit_reference(legacy)["proposals"]}["dials.depth"], 60)

    def test_own_licensed_face_carries_over(self):
        ref = {"method": "computed", "tag": "inspiration", "type": {"families": ["sohne-var", "-apple-system"]}}
        fit = e.fit_reference(ref)
        self.assertNotIn("raw.textFace", {p["path"] for p in fit["proposals"]})
        self.assertFalse(any("-apple-system" in n for n in fit["notes"]))
        s = u5_state(textFace="Söhne", fontLicence={"web": True, "app": False})
        s["hooks"]["H-type"]["status"] = "have"
        got = {p["path"]: p["value"] for p in e.fit_reference(ref, s)["proposals"]}
        self.assertEqual(got["raw.textFace"], "Söhne")
        s["hooks"]["H-type"]["status"] = "pending"
        s["raw"]["fontLicence"] = {}
        self.assertNotIn("raw.textFace", {p["path"] for p in e.fit_reference(ref, s)["proposals"]})


if __name__ == "__main__":
    unittest.main(verbosity=1)
