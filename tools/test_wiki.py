#!/usr/bin/env python3
"""Tests for the learning wiki (tools/wiki.py), its committed data, and the house standards file.

    python3 tools/test_wiki.py                       standard library only; OpenWiki tests are skipped
    .venv-wiki/bin/python tools/test_wiki.py         also runs the OpenWiki integration tests (ingest, lint)
"""
import importlib.util, io, json, re, shutil, sys, tempfile, unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("wiki", ROOT / "tools" / "wiki.py")
wiki = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wiki)
HAVE_OPENWIKI = importlib.util.find_spec("openwiki") is not None
TOPIC = json.loads((ROOT / "learn" / "taxonomy.json").read_text())["topics"][0]["name"]


def analysis(**over):
    a = {"summary": "s", "key_ideas": ["k"], "entities": [{"name": "Sonner", "type": "library", "description": "d"}],
         "topics": [{"name": TOPIC, "summary": "t"}], "claims": [{"claim": "c", "evidence": "e"}],
         "quotes": ["short quote here"], "tags": ["motion"], "authority": "reference",
         "rules": [{"rule": "Use ease-out to enter.", "why": "feels fast", "kind": "do", "strength": "must", "area": "motion",
                    "applies_to": "web", "values": ["ease-out"], "evidence": "tip 4"}],
         "decisions": [{"question": "Which easing?", "options": [{"name": "ease-out", "effect": "fast start", "when": "enter"}],
                        "recommendation": "ease-out", "maps_to": None, "evidence": "tip 4"}],
         "process": [{"step": "Look", "detail": "slow it down"}], "examples": [{"what": "toast", "where": "Sonner", "visual_note": "stacks"}],
         "numbers": [{"value": "300ms", "context": "max UI duration", "evidence": "tip 6"}], "caveats": []}
    a.update(over)
    return a


RAW_TXT = """Title: {title}
Video ID: {vid}
URL: https://www.youtube.com/watch?v={vid}
Channel: Test Channel
Published: 2026-09-01

============================================================
TRANSCRIPT
============================================================

A talk about easing. Use ease-out when things enter.
"""


class Sandbox(unittest.TestCase):
    """A throwaway learn/ tree: tools/wiki.py reads its paths from module globals, so they are pointed here."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = {k: getattr(wiki, k) for k in ("ROOT", "LEARN", "RAW", "ANALYSIS", "WIKI", "SOURCES", "TAXONOMY", "TRACE", "STANDARDS",
                                                    "LOCK", "MAP", "CARDS_DIR", "CITE_JSON", "REVIEW_LOG")}
        wiki.ROOT = self.tmp
        learn = self.tmp / "learn"
        wiki.LEARN, wiki.RAW, wiki.ANALYSIS, wiki.WIKI = learn, learn / "raw", learn / "analysis", learn / "wiki"
        wiki.SOURCES, wiki.TAXONOMY, wiki.TRACE = learn / "sources.json", learn / "taxonomy.json", self.tmp / "L19-trace.md"
        wiki.STANDARDS, wiki.LOCK = self.tmp / "standards.json", learn / "openwiki.lock.json"
        wiki.MAP, wiki.CARDS_DIR, wiki.CITE_JSON = learn / "MAP.md", learn / "wiki" / "synthesis" / "_cards", learn / "citation-check.json"
        for d in (wiki.RAW / "chan", wiki.RAW / "videos", wiki.RAW / "site", wiki.ANALYSIS):
            d.mkdir(parents=True)
        shutil.copy(ROOT / "learn" / "taxonomy.json", wiki.TAXONOMY)
        wiki.SOURCES.write_text(json.dumps({
            "youtube_channels": [{"name": "Chan", "query": "https://www.youtube.com/@chan", "folder": "raw/chan", "authority": "reference"}],
            "youtube_videos": [{"name": "One talk", "url": "https://www.youtube.com/watch?v=AAAAAAAAAAA", "folder": "raw/videos",
                                "authority": "non-negotiable"}],
            "pages": [{"name": "Site", "urls": ["https://example.com/a"], "folder": "raw/site", "id_prefix": "site",
                       "authority": "good-to-have"}]}))

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(wiki, k, v)
        shutil.rmtree(self.tmp)

    def raw(self, folder, vid, title="A talk"):
        p = wiki.RAW / folder / f"{vid}.txt"
        p.write_text(RAW_TXT.format(title=title, vid=vid))
        return p

    def run_cmd(self, fn, **kw):
        out = io.StringIO()
        with redirect_stdout(out):
            code = fn(type("A", (), kw)())
        return code, out.getvalue()


class Classify(unittest.TestCase):
    def test_urls(self):
        self.assertEqual(wiki.classify("https://www.youtube.com/@KoleJain"), "youtube_channels")
        self.assertEqual(wiki.classify("https://www.youtube.com/watch?v=lkKGQVHrXzE"), "youtube_videos")
        self.assertEqual(wiki.classify("https://youtu.be/lkKGQVHrXzE"), "youtube_videos")
        self.assertEqual(wiki.classify("https://github.com/emilkowalski/skills"), "github_repos")
        self.assertEqual(wiki.classify("https://emilkowal.ski/ui/7-practical-animation-tips"), "pages")

    def test_video_id(self):
        self.assertEqual(wiki.video_id("https://www.youtube.com/watch?v=lkKGQVHrXzE&t=3"), "lkKGQVHrXzE")
        self.assertEqual(wiki.video_id("https://youtu.be/lkKGQVHrXzE"), "lkKGQVHrXzE")
        self.assertIsNone(wiki.video_id("https://example.com"))

    def test_raw_folder_name(self):
        # OpenWiki turns "/" into "_", so YouTube runs with learn/raw/ as root and a one-level name.
        self.assertEqual(wiki.raw_folder_name("raw/mobbin"), "mobbin")
        with self.assertRaises(SystemExit):
            wiki.raw_folder_name("mobbin")
        with self.assertRaises(SystemExit):
            wiki.raw_folder_name("raw/a/b")


class AnalysisSchema(unittest.TestCase):
    topics = {t["name"] for t in json.loads((ROOT / "learn" / "taxonomy.json").read_text())["topics"]}

    def errs(self, a):
        return wiki.check_analysis(a, self.topics)[0]

    def test_valid(self):
        self.assertEqual(self.errs(analysis()), [])

    def test_quote_limits(self):
        self.assertTrue(any("quote over" in e for e in self.errs(analysis(quotes=["one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen"]))))
        self.assertTrue(any("quotes (max" in e for e in self.errs(analysis(quotes=["a", "b", "c", "d"]))))

    def test_topic_must_be_in_taxonomy(self):
        self.assertTrue(any("not in taxonomy" in e for e in self.errs(analysis(topics=[{"name": "Colour", "summary": "x"}]))))
        errs, notes = wiki.check_analysis(analysis(topics=[{"name": "Sound design", "summary": "x", "new": True}]), self.topics)
        self.assertEqual(errs, [])
        self.assertTrue(notes)

    def test_rule_fields(self):
        bad = analysis(rules=[{"rule": "x", "why": "", "strength": "always", "area": "motion"}])
        e = self.errs(bad)
        self.assertTrue(any("rule without why" in x for x in e))
        self.assertTrue(any("strength" in x for x in e))

    def test_authority(self):
        self.assertTrue(any("authority" in e for e in self.errs(analysis(authority="gospel"))))

    def test_missing_field(self):
        a = analysis()
        del a["decisions"]
        self.assertTrue(any("decisions" in e for e in self.errs(a)))


class Authority(Sandbox):
    def test_single_video_uses_its_own_entry(self):
        v = self.raw("videos", "AAAAAAAAAAA")
        other = self.raw("videos", "BBBBBBBBBBB")
        self.assertEqual(wiki.authority_of(v), "non-negotiable")
        self.assertEqual(wiki.authority_of(other), "reference")  # not listed: reference, never the neighbour's level
        self.assertEqual(wiki.authority_of(self.raw("chan", "CCCCCCCCCCC")), "reference")

    def test_check_flags_authority_mismatch(self):
        self.raw("videos", "AAAAAAAAAAA")
        (wiki.ANALYSIS / "AAAAAAAAAAA.json").write_text(json.dumps(analysis(authority="reference")))
        code, out = self.run_cmd(wiki.cmd_check)
        self.assertEqual(code, 1)
        self.assertIn("sources.json says 'non-negotiable'", out)

    def test_check_ok_and_counts(self):
        self.raw("chan", "CCCCCCCCCCC")
        self.raw("chan", "DDDDDDDDDDD")
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        code, out = self.run_cmd(wiki.cmd_check)
        self.assertEqual(code, 0, out)
        self.assertIn("2 raw files, 1 analysed, 1 pending", out)


class WorkItems(Sandbox):
    def test_grouping(self):
        self.raw("chan", "CCCCCCCCCCC")
        self.raw("site", "site-a")
        self.raw("site", "site-b")
        code, out = self.run_cmd(wiki.cmd_pending, json=False, work_items=True)
        items = {i["k"]: i for i in json.loads(out)}
        self.assertEqual(items["site"]["ids"], ["site-a", "site-b"])  # pages of one site go to one agent
        self.assertEqual(items["site"]["a"], "good-to-have")
        self.assertEqual(items["CCCCCCCCCCC"]["ids"], ["CCCCCCCCCCC"])  # one agent per video


class Trace(Sandbox):
    def test_append_only_and_stable(self):
        self.raw("chan", "CCCCCCCCCCC")
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        self.run_cmd(wiki.cmd_trace)
        first = wiki.TRACE.read_text()
        self.assertIn("S-L19-001", first)
        self.assertIn("<!-- CCCCCCCCCCC -->", first)
        self.run_cmd(wiki.cmd_trace)  # nothing new: unchanged
        self.assertEqual(wiki.TRACE.read_text(), first)
        self.raw("chan", "DDDDDDDDDDD")
        (wiki.ANALYSIS / "DDDDDDDDDDD.json").write_text(json.dumps(analysis()))
        self.run_cmd(wiki.cmd_trace)
        second = wiki.TRACE.read_text()
        self.assertTrue(second.startswith(first.rstrip("\n")))  # rows are appended, never rewritten
        self.assertIn("S-L19-002", second)
        sids = json.loads((wiki.LEARN / "sids.json").read_text())
        self.assertEqual(sids, {"CCCCCCCCCCC": "S-L19-001", "DDDDDDDDDDD": "S-L19-002"})

    def test_no_caption_videos_are_logged_as_rejected(self):
        (wiki.RAW / "chan" / "_extract_state.json").write_text(json.dumps({"done": [], "permanent_skip": ["EEEEEEEEEEE"]}))
        self.run_cmd(wiki.cmd_trace)
        self.assertIn("rejected: no captions available", wiki.TRACE.read_text())


class Next(Sandbox):
    def test_reports_steps_in_order(self):
        self.raw("chan", "CCCCCCCCCCC")
        self.raw("chan", "DDDDDDDDDDD")
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        steps = [t[0] for t in wiki.pipeline_state()]
        self.assertIn("fetch", steps)                         # "One talk" and "Site" have nothing on disk
        self.assertLess(steps.index("analyse"), steps.index("trace"))
        self.assertIn("standards", steps)                     # a non-negotiable analysis and no standards file
        why = dict((t[0], t[1]) for t in wiki.pipeline_state())
        self.assertIn("1 fetched sources have no analysis", why["analyse"])

    def test_standards_stale_when_inputs_change(self):
        (wiki.ANALYSIS / "ek-a.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        doc = {"version": 1, "themes": [], "standards": [], "retired": [], "built_from": wiki.standard_inputs()}
        doc["content_hash"] = wiki.standards_hash(doc)
        wiki.STANDARDS.write_text(json.dumps(doc))
        self.assertFalse([t for t in wiki.pipeline_state() if t[0] == "standards"])
        (wiki.ANALYSIS / "ek-a.json").write_text(json.dumps(analysis(authority="non-negotiable", summary="changed")))
        (wiki.ANALYSIS / "ek-b.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        why = [t[1] for t in wiki.pipeline_state() if t[0] == "standards"][0]
        self.assertIn("1 new and 1 changed", why)


class Map(Sandbox):
    def test_map_lists_areas_cards_and_questions(self):
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        (wiki.CARDS_DIR).mkdir(parents=True)
        (wiki.CARDS_DIR / "motion.md").write_text("### DC-L19-81: Press feedback\n- **Maps to:** Q-motion-01 new default\n\n"
                                                   "### DC-L19-82: Old idea\n- **Withdrawn:** not in the source\n- **Maps to:** Q-motion-07\n")
        saved = wiki.CARDS_DIR
        text = wiki.render_map()
        self.assertIn("DC-L19-81: Press feedback → Q-motion-01", text)
        self.assertIn("~~DC-L19-82: Old idea~~ (withdrawn)", text)
        self.assertIn("| Q-motion-01 | DC-L19-81 |", text)
        self.assertNotIn("| Q-motion-07 | DC-L19-82", text)          # withdrawn cards are not offered as guidance
        self.assertIn(f"{TOPIC} (1, no page yet)", text)
        code, out = self.run_cmd(wiki.cmd_map, check=True)
        self.assertEqual(code, 1)                                    # no MAP.md yet: stale
        self.run_cmd(wiki.cmd_map, check=False)
        code, out = self.run_cmd(wiki.cmd_map, check=True)
        self.assertEqual(code, 0, out)


class ReviewLog(Sandbox):
    def test_reviewed_items_leave_the_flagged_list_until_edited(self):
        wiki.REVIEW_LOG = wiki.LEARN / "citation-review.json"
        a = analysis()
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(a))
        wiki.CITE_JSON.write_text(json.dumps({"results": [{"source": "CCCCCCCCCCC", "n": 0, "rule": a["rules"][0]["rule"],
                                                           "verdict": "unsupported", "confidence": 0.4}], "standards": []}))
        flagged = lambda: json.loads(self.run_cmd(wiki.cmd_flagged, json=True)[1])["rules"]
        self.assertEqual(len(flagged()), 1)
        import sys as _sys
        saved_stdin = _sys.stdin
        _sys.stdin = io.StringIO(json.dumps([{"item": "CCCCCCCCCCC rule 0", "decision": "confirmed", "note": "verbatim in tip 4"}]))
        try:
            self.run_cmd(wiki.cmd_review_log)
        finally:
            _sys.stdin = saved_stdin
        self.assertEqual(flagged(), [])
        a["rules"][0]["rule"] = "Use ease-out to enter and exit."               # an edit re-opens the item
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(a))
        c = json.loads(wiki.CITE_JSON.read_text()); c["results"][0]["rule"] = a["rules"][0]["rule"]
        wiki.CITE_JSON.write_text(json.dumps(c))
        self.assertEqual(len(flagged()), 1)


class Standards(Sandbox):
    def doc(self):
        (wiki.ANALYSIS / "ek-tips.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        d = {"version": 1, "themes": [{"key": "easing", "title": "Easing", "summary": ""}], "standards": [
            {"id": "STD-easing-01", "theme": "easing", "area": "motion", "title": "Ease out", "rule": "Use ease-out.",
             "why": "fast", "strength": "must", "values": {"enter": "ease-out"}, "applies_to": ["web"],
             "sources": [{"id": "ek-tips", "evidence": "tip 4"}], "engine": {"path": "motion.easing.exit", "value": [0.23, 1, 0.32, 1]},
             "review": {"pattern": r"transition:\s*all", "message": "name the properties"}, "design_md": True,
             "conflicts": [], "since": 1, "changed": 1}], "retired": []}
        d["content_hash"] = wiki.standards_hash(d)
        return d

    def test_valid(self):
        self.assertEqual(wiki.check_standards(self.doc()), [])

    def test_edit_without_bump_fails(self):
        d = self.doc()
        d["standards"][0]["rule"] = "Use ease-in."
        self.assertTrue(any("without a version bump" in e for e in wiki.check_standards(d)))

    def test_problems_are_named(self):
        d = self.doc()
        s = d["standards"][0]
        s["review"]["pattern"] = "("
        s["sources"].append({"id": "missing-source"})
        s["strength"] = "consider"
        d["standards"].append(dict(s))
        d["content_hash"] = wiki.standards_hash(d)
        e = " | ".join(wiki.check_standards(d))
        for needle in ("does not compile", "missing-source", "strength must be", "duplicate ids"):
            self.assertIn(needle, e)

    def test_bump_stamps_versions(self):
        d = self.doc()
        d["standards"][0]["rule"] = "Use ease-out for enter and exit."
        wiki.STANDARDS.write_text(json.dumps(d))
        self.run_cmd(wiki.cmd_standards, bump="first release")  # no git history in the sandbox: version stays 1
        out = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual(wiki.check_standards(out), [])
        self.assertEqual(out["history"][-1]["why"], "first release")


class Upstream(Sandbox):
    def test_lock_mismatch_warns(self):
        wiki.LOCK.parent.mkdir(parents=True, exist_ok=True)
        wiki.LOCK.write_text(json.dumps({"commit": "0" * 40}))
        saved = wiki.installed_openwiki
        wiki.installed_openwiki = lambda: {"version": "9", "commit": "1" * 40}
        err = io.StringIO()
        try:
            from contextlib import redirect_stderr
            with redirect_stderr(err):
                wiki.warn_if_unlocked()
        finally:
            wiki.installed_openwiki = saved
        self.assertIn("not the tested commit", err.getvalue())


class FindPassage(unittest.TestCase):
    body = ("Intro text. " * 50 + "Easing, or the rate of change, is the most important part of any animation. "
            + "Filler. " * 80 + "Buttons should scale to 0.97 when pressed. " + "More filler. " * 60)

    def test_exact_evidence(self):
        passage, how = wiki.find_passage(self.body, "Scale buttons on press", "Buttons should scale to 0.97")
        self.assertEqual(how, "evidence found")
        self.assertIn("0.97", passage)

    def test_elided_evidence(self):
        passage, how = wiki.find_passage(self.body, "Easing matters most", "Easing ... is the most important part")
        self.assertEqual(how, "evidence found")
        self.assertIn("most important part", passage)

    def test_keyword_fallback(self):
        passage, how = wiki.find_passage(self.body, "Press scale 0.97 on buttons", "section 1")
        self.assertEqual(how, "keyword window")
        self.assertIn("0.97", passage)


class CommittedData(unittest.TestCase):
    """What is in git must pass the same checks the pipeline applies."""

    def test_sources_json(self):
        cfg = json.loads((ROOT / "learn" / "sources.json").read_text())
        for kind, e in wiki.all_sources(cfg):
            self.assertIn(e.get("authority"), wiki.AUTHORITY, e["name"])
            self.assertTrue(e["folder"].startswith("raw/") and e["folder"].count("/") == 1, e["folder"])

    def test_taxonomy_unique(self):
        names = [t["name"] for t in json.loads((ROOT / "learn" / "taxonomy.json").read_text())["topics"]]
        self.assertEqual(len(names), len(set(names)))

    def test_every_analysis_passes(self):
        topics = {t["name"] for t in json.loads((ROOT / "learn" / "taxonomy.json").read_text())["topics"]}
        for p in sorted((ROOT / "learn" / "analysis").glob("*.json")):
            with self.subTest(p.name):
                self.assertEqual(wiki.check_analysis(json.loads(p.read_text()), topics)[0], [])

    def test_no_third_party_text_committed(self):
        ignored = (ROOT / ".gitignore").read_text()
        self.assertIn("learn/raw/", ignored)
        self.assertIn("learn/raw_*/", ignored)

    def test_standards_file(self):
        p = ROOT / "synthesis" / "standards.json"
        if not p.exists():
            self.skipTest("synthesis/standards.json not written yet")
        self.assertEqual(wiki.check_standards(json.loads(p.read_text())), [])

    def test_lock_file(self):
        lock = json.loads((ROOT / "learn" / "openwiki.lock.json").read_text())
        self.assertRegex(lock["commit"], r"^[0-9a-f]{40}$")


@unittest.skipUnless(HAVE_OPENWIKI, "OpenWiki not installed (use .venv-wiki/bin/python)")
class OpenWikiIntegration(Sandbox):
    """The contract with OpenWiki: raw header parsing, ingest with analysis JSON, our section, lint."""

    def test_ingest_adds_learn_section_once(self):
        self.raw("chan", "CCCCCCCCCCC", title="Easing talk")
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        (wiki.WIKI).mkdir(parents=True, exist_ok=True)
        saved = wiki.openwiki
        wiki.openwiki = lambda *a, **k: 0  # lint runs separately below
        try:
            self.run_cmd(wiki.cmd_ingest, force=False)
            self.run_cmd(wiki.cmd_ingest, force=True)  # re-ingest must not duplicate our section
        finally:
            wiki.openwiki = saved
        pages = list((wiki.WIKI / "sources").glob("CCCCCCCCCCC-*.md"))
        self.assertEqual(len(pages), 1)
        text = pages[0].read_text()
        self.assertEqual(text.count(wiki.MARK_START), 1)
        self.assertIn("authority: reference", text)
        self.assertIn("## For OpenDesigner", text)
        self.assertIn("**must** (motion, web): Use ease-out to enter.", text)
        topic = wiki.WIKI / "topics" / (re.sub(r"[^a-z0-9]+", "-", TOPIC.lower()).strip("-") + ".md")
        self.assertTrue(topic.exists(), topic)
        from openwiki.lint import build_report
        from openwiki.workspace import Workspace
        report = build_report(Workspace.resolve(wiki.LEARN))
        self.assertEqual(report.get("missing_frontmatter", []), [])

    def test_raw_header_contract(self):
        from openwiki.textfmt import parse_source_file
        rec = parse_source_file(self.raw("chan", "CCCCCCCCCCC", title="Easing talk"))
        self.assertEqual(rec["video_id"], "CCCCCCCCCCC")
        self.assertEqual(rec["title"], "Easing talk")
        self.assertIn("ease-out", rec["transcript"])

    def test_safe_folder_name_contract(self):
        # If OpenWiki stops rewriting "/", raw_folder_name() can go; if it rewrites more, fetch must adapt.
        from openwiki.youtube import safe_folder_name
        self.assertEqual(safe_folder_name("mobbin"), "mobbin")
        self.assertEqual(safe_folder_name("raw/mobbin"), "raw_mobbin")


if __name__ == "__main__":
    unittest.main(verbosity=1)
