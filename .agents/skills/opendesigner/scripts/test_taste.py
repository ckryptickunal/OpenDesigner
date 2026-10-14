#!/usr/bin/env python3
"""Tests for taste.py: the library is valid and covers every dial end, the page builds, results import, and the taste index
merges every signal, orders options, keeps red lines and flags drift."""
import contextlib, io, json, os, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import taste  # noqa: E402
import engine as e  # noqa: E402

LIB = taste.library(extra=False)
FLAT = [s for s in LIB if s["d"][5] < 20][:6]   # depth is the sixth dial
DEEP = [s for s in LIB if s["d"][5] > 75][:2]


def poll(loved=FLAT, hated=DEEP, extra=()):
    ratings = [[s["id"], "cracked"] for s in loved] + [[s["id"], "hate"] for s in hated] + list(extra)
    return {"v": 1, "n": len(ratings), "date": "2026-10-15", "dials": {d: {"value": 50, "conf": 0.2} for d in taste.DIALS},
            "everyday": 0.3, "hero": 0.5, "genericAllergy": 0.4, "likes": ["flat"], "dislikes": ["glow"], "redLines": [],
            "ratings": ratings}


def quiet(fn, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **k)


class Project(unittest.TestCase):
    """A sketched project in a temporary folder, with a poll on disk."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.d = os.path.join(tmp.name, "opendesigner")
        quiet(e.cmd_sketch, self.d, "Ledger", None, "regular", "web", "calm,minimal", quiet=True)

    def write_poll(self, rec):
        Path(self.d, "taste-profile.json").write_text(json.dumps(rec), encoding="utf-8")

    def reference(self, rid, tag, proposals):
        st = e.load_state(self.d)
        st["references"][rid] = {"tag": tag, "kind": "url", "file": "", "proposals": proposals, "notes": [], "status": "accepted"}
        e.dump_json(os.path.join(self.d, "state.json"), st)

    def index(self):
        return taste.build_index(self.d, e)


class Library(unittest.TestCase):
    def test_library_is_valid(self):
        self.assertEqual(taste.problems(taste.library(extra=False)), [])

    def test_every_dial_end_has_several_screens(self):
        _, _, gaps = taste.coverage(taste.library(extra=False), thin=6)
        self.assertEqual(gaps, [])

    def test_bad_entries_are_caught(self):
        bad = {"id": "Hero Figma", "app": "", "kind": "banner", "platform": "tv", "source": "mobbin",
               "d": [1, 2, 3], "tags": ["shiny"]}
        errs = " ".join(taste.problems([bad]))
        for word in ("id must", "missing app", "unknown kind", "platform", "d must", "unknown", "mobbin_url"):
            self.assertIn(word, errs)


class Build(unittest.TestCase):
    def test_build_fills_the_page_with_screens_that_have_images(self):
        with tempfile.TemporaryDirectory() as tmp:
            shots = Path(tmp) / "shots"
            shots.mkdir()
            ids = [e["id"] for e in taste.library(extra=False)[:3]]
            for i in ids:
                (shots / f"{i}.jpg").write_bytes(b"\xff\xd8\xff")
            env = dict(os.environ, OD_TASTE_SCREENS=str(shots), OD_HOME=str(Path(tmp) / "home"))
            # the repo's own taste-screens/ may exist; point the lookup at the temp folder first
            out = Path(tmp) / "poll"
            subprocess.run([sys.executable, str(HERE / "taste.py"), "build", "--project", "Acme", "--out", str(out)],
                           check=True, env=env, capture_output=True)
            html = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn('"project": "Acme"', html)
            for i in ids:
                self.assertIn(f'"img/{i}.jpg"', html)
                self.assertTrue((out / "img" / f"{i}.jpg").exists())


class Import(unittest.TestCase):
    def test_import_builds_the_index_and_recommends_only_sure_dials(self):
        with tempfile.TemporaryDirectory() as tmp:
            od = Path(tmp) / "opendesigner"
            rec = poll(extra=[[s["id"], "okay"] for s in LIB[40:44]])
            line = "Here you go:\nOD:set taste.poll=" + json.dumps(rec) + "\n"
            r = subprocess.run([sys.executable, str(HERE / "taste.py"), "import", "-", "--dir", str(od)],
                               input=line, text=True, capture_output=True, check=True)
            saved = json.loads((od / "taste-profile.json").read_text(encoding="utf-8"))
            self.assertEqual((saved["kind"], saved["poll"]["n"], saved["counts"]["poll"]), ("taste-index", 12, 12))
            sure = [d for d in taste.DIALS if saved["dials"][d]["conf"] >= taste.SURE]
            self.assertIn("depth", sure)  # six loved flat screens
            for d in taste.DIALS:
                cmd = f"dials.{d} {saved['dials'][d]['value']} --set-by assumed"
                (self.assertIn if d in sure else self.assertNotIn)(cmd, r.stdout)
            self.assertIn("Ask directly", r.stdout)
            again = subprocess.run([sys.executable, str(HERE / "taste.py"), "import", str(od / "taste-profile.json"),
                                    "--dir", str(od)], text=True, capture_output=True, check=True)
            self.assertEqual(json.loads((od / "taste-profile.json").read_text(encoding="utf-8"))["dials"], saved["dials"],
                             again.stderr)  # importing a saved index reads the poll it keeps


@unittest.skipUnless(shutil.which("node"), "needs node to run the poll page's own model")
class SameAsTheResultsCard(unittest.TestCase):
    """The index from a poll alone is the profile the person saw on the page's results card: same values, confidence and red lines."""

    def test_python_model_matches_the_page(self):
        html = taste.TEMPLATE.read_text(encoding="utf-8")
        model = (html[html.index("const DIALS=["):html.index("const RW=")] + "const RW=Object.fromEntries(RATINGS.map(r=>[r.k,r]));\n"
                 + html[html.index("/* ---------- model ---------- */"):html.index("/* ---------- adaptive picking ---------- */")])
        keys = ["cracked", "best", "crazy", "okay", "generic", "hate"]
        cases = [[[s["id"], keys[(i * 7 + j) % 6]] for j, s in enumerate(LIB[i * 11:i * 11 + 4 + i])] for i in range(12)]
        cases.append([[s["id"], "cracked"] for s in FLAT] + [[s["id"], "hate"] for s in DEEP])
        js = ("const S=" + json.dumps([{"id": s["id"], "app": s["app"], "d": s["d"], "tags": s["tags"], "common": bool(s.get("common"))}
                                        for s in LIB]) + ";const BY=Object.fromEntries(S.map(s=>[s.id,s]));\n" + model
              + "\nfor(const R of " + json.dumps(cases) + "){const P=profile(R);console.log(JSON.stringify({d:P.dials.map(d=>[d.v,"
              "+d.conf.toFixed(2)]),red:P.red.map(r=>[r.d.id,r.x>50?'high':'low',r.x])}))}")
        out = subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout.splitlines()
        for ratings, line in zip(cases, out):
            want = json.loads(line)
            with tempfile.TemporaryDirectory() as tmp:
                Path(tmp, "taste-profile.json").write_text(json.dumps(dict(poll(), ratings=ratings)), encoding="utf-8")
                ix = taste.build_index(tmp)
            self.assertEqual([[ix["dials"][d]["value"], ix["dials"][d]["conf"]] for d in taste.DIALS], want["d"], ratings)
            self.assertEqual([[r["dial"], r["side"], r["value"]] for r in ix["redLines"]], want["red"], ratings)


class Weights(unittest.TestCase):
    def test_signals_rank_in_the_agreed_order(self):
        w = taste.WEIGHTS
        strongest_ref = w["inspiration"] * max(taste.REF_CONFIDENCE.values())
        self.assertGreater(w["override"], w["cracked"])
        self.assertEqual(w["cracked"], -w["hate"])
        self.assertGreater(w["cracked"], strongest_ref)
        self.assertGreater(strongest_ref, w["style"])
        self.assertGreaterEqual(w["style"], w["feel"])
        self.assertEqual(taste.REF_TAGS["competitor"], 0)


class Merge(Project):
    def test_every_signal_lands_in_the_index_with_its_weight(self):
        self.write_poll(poll())
        self.reference("calm-site", "inspiration", [{"path": "dials.depth", "value": 10, "confidence": "high", "basis": "",
                                                     "status": "accepted"}])
        quiet(e.cmd_set, self.d, "answers.Q-dir-01", "glass", "sketch start", set_by="assumed")
        quiet(e.cmd_set, self.d, "answers.Q-dir-01", "flat2", "they picked the quiet one")
        quiet(e.cmd_set, self.d, "dials.warmth", 70, "warm greys", set_by="chosen")
        quiet(e.cmd_set, self.d, "dials.energy", 90, "our guess", set_by="assumed")
        ix = self.index()
        self.assertEqual(set(ix["counts"]), {"poll", "decision", "style", "reference", "feel"})
        depth = {(x["source"], x["kind"]): x["weight"] for x in ix["dials"]["depth"]["evidence"]}
        self.assertEqual(depth[("style", "override")], 8)          # glass was our pick; flat2 is theirs
        self.assertEqual(depth[("poll", "cracked")], 3)
        self.assertEqual(depth[("poll", "hate")], -3)
        self.assertEqual(depth[("reference", "inspiration")], 2.5)
        weights = [abs(x["weight"]) for x in ix["dials"]["depth"]["evidence"]]
        self.assertEqual(weights, sorted(weights, reverse=True))  # strongest first
        self.assertTrue(any(x["source"] == "feel" for d in taste.DIALS for x in ix["dials"][d]["evidence"]))
        warmth = ix["dials"]["warmth"]
        self.assertEqual((warmth["value"], warmth["conf"]), (70, 0.95))  # the person's own value is pinned
        self.assertTrue(warmth["decided"].startswith("D-"))
        self.assertFalse([x for x in ix["dials"]["energy"]["evidence"] if x["source"] == "decision"])  # our guess never counts
        self.assertLess(ix["dials"]["depth"]["value"], 35)

    def test_a_competitor_never_pulls(self):
        self.write_poll(poll())
        base = self.index()
        self.reference("rival", "competitor", [{"path": f"dials.{d}", "value": 100, "confidence": "high", "basis": "",
                                                "status": "pending"} for d in taste.DIALS])
        ix = self.index()
        for d in taste.DIALS:
            self.assertEqual((ix["dials"][d]["value"], ix["dials"][d]["conf"]), (base["dials"][d]["value"], base["dials"][d]["conf"]))
            self.assertEqual([x["weight"] for x in ix["dials"][d]["evidence"] if x["id"] == "rival"], [0])

    def test_confirming_a_recommendation_is_weaker_than_choosing(self):
        quiet(e.cmd_set, self.d, "dials.depth", 20, "taste index", set_by="assumed")
        quiet(e.cmd_set, self.d, "dials.depth", 20, "yes, keep it")
        quiet(e.cmd_set, self.d, "dials.roundness", 20, "taste index", set_by="assumed")
        quiet(e.cmd_set, self.d, "dials.roundness", 60, "rounder")
        ix = self.index()
        kind = lambda d: [x["kind"] for x in ix["dials"][d]["evidence"] if x["source"] == "decision"]
        self.assertEqual((kind("depth"), kind("roundness")), (["confirmed"], ["override"]))

    def test_a_red_line_goes_when_the_person_chooses_past_it(self):
        self.write_poll(poll())
        self.assertIn("depth", [r["dial"] for r in self.index()["redLines"]])
        quiet(e.cmd_set, self.d, "dials.depth", 95, "I want it deep after all")
        self.assertNotIn("depth", [r["dial"] for r in self.index()["redLines"]])


class Options(unittest.TestCase):
    INDEX = {"dials": {"depth": {"value": 10, "conf": 0.8}, "roundness": {"value": 30, "conf": 0.4}},
             "redLines": [{"dial": "depth", "side": "high", "value": 85, "limit": 70, "from": "x"}]}

    def test_rank_orders_by_fit_and_leaves_out_red_lines(self):
        opts = [{"value": "a", "dials": {"depth": 50, "roundness": 30}}, {"value": "b", "dials": {"depth": 12, "roundness": 40}},
                {"value": "c", "dials": {"depth": 90, "roundness": 30}}, {"value": "d", "dials": {"energy": 50}}]
        kept, left = taste.rank(self.INDEX, opts)
        self.assertEqual([o["value"] for o in kept], ["b", "a", "d"])  # no fit (nothing sure about energy) goes last
        self.assertEqual([o["value"] for o in left], ["c"])
        self.assertGreater(kept[0]["fit"], kept[1]["fit"])
        kept, left = taste.rank(self.INDEX, opts, keep="c")  # their current answer is theirs, not an offer
        self.assertEqual(left, [])

    def test_drift_flags_far_and_past_a_line_but_not_a_decided_dial(self):
        ix = {"dials": {d: {"value": 50, "conf": 0.1} for d in taste.DIALS}, "redLines": self.INDEX["redLines"]}
        ix["dials"]["roundness"] = {"value": 20, "conf": 0.7}
        ix["dials"]["warmth"] = {"value": 20, "conf": 0.95, "decided": "D-0009"}
        got = taste.drift(ix, dict({d: 50 for d in taste.DIALS}, roundness=60, depth=75, warmth=60))
        self.assertEqual([x["dial"] for x in got], ["roundness", "depth"])
        self.assertEqual(got[1]["redLines"][0]["limit"], 70)

    def test_fit_command_orders_a_gallery_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "taste-profile.json").write_text(json.dumps(poll()), encoding="utf-8")
            payload = {"recommended": "deep", "options": [{"value": "mid", "dials": {"depth": 50}},
                                                          {"value": "deep", "dials": {"depth": 95}},
                                                          {"value": "flat", "dials": {"depth": 5}}]}
            r = subprocess.run([sys.executable, str(HERE / "taste.py"), "fit", "-", "--dir", tmp], input=json.dumps(payload),
                               text=True, capture_output=True, check=True)
            out = json.loads(r.stdout)
            self.assertEqual([o["value"] for o in out["options"]], ["flat", "mid"])
            self.assertEqual(out["leftOut"][0]["value"], "deep")
            self.assertEqual(out["recommended"], "flat")  # never recommend an option past a red line


class Engine(Project):
    def test_the_gallery_is_ordered_by_fit_and_leaves_out_red_lines(self):
        self.write_poll(poll())
        st = e.load_state(self.d)
        payload = e.build_payload(st, "option-gallery", taste=e.taste_index(self.d, st))
        values = [o["value"] for o in payload["options"]]
        self.assertNotIn("glass", values)  # glass is deep; they hated deep screens
        self.assertIn("Left out, past a line you drew: ", payload["subtitle"])
        fits = [o["fit"] for o in payload["options"]]
        self.assertEqual(fits, sorted(fits, reverse=True))
        self.assertEqual(payload["recommended"], values[0])
        self.assertEqual(set(payload["options"][0]["dials"]), set(taste.DIALS))
        plain = e.build_payload(st, "option-gallery")
        self.assertEqual([o["value"] for o in plain["options"]], ["flat2", "tonal", "glass"])  # no index, no change

    def test_feel_words_alone_leave_the_gallery_as_it_is(self):
        st = e.load_state(self.d)
        ix = e.taste_index(self.d, st)
        self.assertEqual(set(ix["counts"]), {"feel", "decision"})  # the audience answer decided density
        self.assertFalse(taste.sure(ix))
        with_ix, plain = e.build_payload(st, "option-gallery", taste=ix), e.build_payload(st, "option-gallery")
        self.assertEqual([o["value"] for o in with_ix["options"]], [o["value"] for o in plain["options"]])
        self.assertEqual((with_ix["recommended"], with_ix["subtitle"]), (plain["recommended"], plain["subtitle"]))

    def test_review_flags_drift_until_the_person_decides(self):
        self.write_poll(poll())
        quiet(e.cmd_set, self.d, "dials.depth", 60, "pick the rest for me", set_by="delegated")
        res = json.loads(quiet_out(e.cmd_review, self.d, as_json=True))
        self.assertEqual([x["dial"] for x in res["tasteDrift"]][:1], ["depth"])
        quiet(e.cmd_set, self.d, "dials.depth", 60, "keep it, I like it")
        res = json.loads(quiet_out(e.cmd_review, self.d, as_json=True))
        self.assertNotIn("depth", [x["dial"] for x in res["tasteDrift"]])


def quiet_out(fn, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*a, **k)
    return buf.getvalue()


if __name__ == "__main__":
    unittest.main(verbosity=1)
