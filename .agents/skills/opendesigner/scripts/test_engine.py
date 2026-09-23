#!/usr/bin/env python3
"""Tests for engine.py (standard library unittest; no network).

    python3 skills/opendesigner/scripts/test_engine.py        (or: python3 -m unittest test_engine)
"""
import contextlib
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

    def test_ratio_capped_by_density(self):
        s = state_with(expression=90, density=90)
        p, _ = e.derive_params(s, e.resolve_dials(s)[0])
        self.assertEqual(p["type.ratio"], 1.2)


class Scales(unittest.TestCase):
    def test_space_ladders(self):
        self.assertEqual(e.space_ladder(4), [0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96])  # Atlassian set + 96 (spec 6.2)
        self.assertTrue({0, 5, 10, 15, 20, 25, 30, 40, 50, 60} <= set(e.space_ladder(5)))            # GOV.UK (S-L09-508)

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
            self.assertEqual(z["color"]["level"], "broad")
            self.assertEqual(z["motion"]["level"], "sketch")
            files, meta, _ = e.generate_system(e.read_json(os.path.join(d, "state.json")))
            rep = e.Report()
            e.validate_files(files, e.read_json(os.path.join(d, "state.json")), rep)
            self.assertEqual(rep.count("error"), 0)  # Level 0 alone gives a complete, valid system


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


if __name__ == "__main__":
    unittest.main(verbosity=1)
