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
                                                    "LOCK", "MAP", "CARDS_DIR", "CITE_JSON", "REVIEW_LOG", "head_standards",
                                                    "fetch_page", "jev_key")}
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

    def exits(self, fn, **kw):
        """The message a command stops with (sys.exit with a string)."""
        with self.assertRaises(SystemExit) as cm:
            self.run_cmd(fn, **kw)
        return str(cm.exception.code)

    def sources(self, **extra):
        cfg = json.loads(wiki.SOURCES.read_text())
        cfg.update(extra)
        wiki.SOURCES.write_text(json.dumps(cfg))
        return cfg

    def manifest(self, entries):
        wiki.WIKI.mkdir(parents=True, exist_ok=True)
        (wiki.WIKI / "ingested.json").write_text(json.dumps(entries))


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

    def test_types_and_enums(self):
        # A string where a list belongs would be rendered one line per character by ingest.
        self.assertTrue(any("caveats must be a list" in e for e in self.errs(analysis(caveats="sponsored"))))
        self.assertTrue(any("numbers must be a list" in e for e in self.errs(analysis(numbers="300ms"))))
        rule = analysis()["rules"][0]
        for bad, needle in (({"values": "ease-out"}, "values must be a list"), ({"area": "sound"}, "rule area 'sound'"),
                            ({"applies_to": "vue"}, "applies_to 'vue'"), ({"kind": "maybe"}, "rule kind 'maybe'")):
            with self.subTest(bad):
                self.assertTrue(any(needle in e for e in self.errs(analysis(rules=[dict(rule, **bad)]))))
        self.assertEqual(self.errs(analysis(rules=[dict(rule, applies_to=["react-native", "compose"])])), [])
        dec = analysis()["decisions"][0]
        self.assertTrue(any("maps_to 'Q-nope-01'" in e for e in self.errs(analysis(decisions=[dict(dec, maps_to="Q-nope-01")]))))
        self.assertEqual(self.errs(analysis(decisions=[dict(dec, maps_to="Q-motion-01")])), [])


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
    def items(self):
        code, out = self.run_cmd(wiki.cmd_pending, json=False, work_items=True)
        doc = json.loads(out)
        self.assertEqual(doc["root"], str(wiki.ROOT))  # the workflows need the checkout they run against
        return {i["k"]: i for i in doc["items"]}

    def test_grouping(self):
        self.raw("chan", "CCCCCCCCCCC")
        self.raw("site", "site-a")
        self.raw("site", "site-b")
        items = self.items()
        self.assertEqual(items["site"]["ids"], ["site-a", "site-b"])  # pages of one site go to one agent
        self.assertEqual(items["site"]["a"], "good-to-have")
        self.assertEqual(items["CCCCCCCCCCC"]["ids"], ["CCCCCCCCCCC"])  # one agent per video

    def test_github_files_group_by_folder_and_items_are_capped(self):
        self.sources(github_repos=[{"name": "o/r", "url": "https://github.com/o/r", "folder": "raw/gh", "id_prefix": "gh",
                                    "authority": "reference"}])
        (wiki.RAW / "gh").mkdir()

        def repo_file(rel):
            ident = "gh-" + wiki.slug(rel.removesuffix(".md"))
            (wiki.RAW / "gh" / f"{ident}.txt").write_text(
                f"Title: o/r: {rel}\nVideo ID: {ident}\nSource: https://github.com/o/r/blob/abc123/{rel}\n\nTRANSCRIPT\n\ntext\n")
        for n in range(7):
            repo_file(f"skills/animate/part-{n}.md")
        repo_file("README.md")
        repo_file("notes.md")
        for n in range(7):
            self.raw("site", f"site-{n}")
        items = self.items()
        self.assertEqual(len(items["gh-skills-animate"]["ids"]), wiki.WORK_ITEM_MAX)  # one folder, at most 5 files per agent
        self.assertEqual(len(items["gh-skills-animate-2"]["ids"]), 2)
        self.assertEqual(sorted(items["gh-root"]["ids"]), ["gh-notes", "gh-readme"])  # files at the repo root
        self.assertEqual((len(items["site"]["ids"]), len(items["site-2"]["ids"])), (5, 2))


class Trace(Sandbox):
    def test_append_only_and_stable(self):
        self.raw("chan", "CCCCCCCCCCC")
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        self.run_cmd(wiki.cmd_trace)
        first = wiki.TRACE.read_text()
        self.assertRegex(first, r"\| \d{4}-\d\d-\d\dT\d\d:\d\d \| S-L19-001 \|")  # a date and a time, not a bare time
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

    def test_check_comes_first_with_a_fix(self):
        self.raw("videos", "AAAAAAAAAAA")
        (wiki.ANALYSIS / "AAAAAAAAAAA.json").write_text(json.dumps(analysis(authority="reference")))
        step, why, fix = wiki.pipeline_state()[0]
        self.assertEqual(step, "check")
        self.assertIn("sources.json says 'non-negotiable'", why)
        args = json.loads(fix.split("with args ", 1)[1])  # the exact args to redo the analysis at the right depth
        self.assertEqual(args["items"], [{"k": "AAAAAAAAAAA", "a": "non-negotiable", "d": "videos", "ids": ["AAAAAAAAAAA"]}])
        self.assertEqual(args["root"], str(wiki.ROOT))

    def test_edited_analysis_marks_its_page_stale(self):
        self.raw("chan", "CCCCCCCCCCC")
        aj = wiki.ANALYSIS / "CCCCCCCCCCC.json"
        aj.write_text(json.dumps(analysis()))
        (wiki.WIKI / "sources").mkdir(parents=True)
        (wiki.WIKI / "sources" / "CCCCCCCCCCC-a-talk.md").write_text("page")
        entry = {"wiki_page": "wiki/sources/CCCCCCCCCCC-a-talk.md", "source_file": "raw/chan/CCCCCCCCCCC.txt",
                 "analysis_hash": wiki.file_hash(aj)}
        self.manifest({"CCCCCCCCCCC": entry})
        steps = lambda: [t for t in wiki.pipeline_state() if t[0] == "ingest"]
        self.assertEqual(steps(), [])
        aj.write_text(json.dumps(analysis(summary="edited")))  # the page is newer on disk, but built from the old analysis
        self.assertIn("1 wiki pages built from an older analysis", steps()[0][1])
        self.assertEqual(steps()[0][2], ".venv-wiki/bin/python tools/wiki.py ingest")  # ingest re-ingests it by itself

    def test_fresh_clone_counts_committed_work(self):
        # learn/raw/ is git-ignored: a fresh clone has analyses and a wiki manifest, but no raw text.
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis()))
        (wiki.ANALYSIS / "site-a.json").write_text(json.dumps(analysis(authority="good-to-have")))
        self.manifest({"CCCCCCCCCCC": {"source_file": "raw/chan/CCCCCCCCCCC.txt", "wiki_page": "wiki/sources/x.md"}})
        rows = {r["name"]: r for r in json.loads(self.run_cmd(wiki.cmd_status, json=True)[1])["sources"]}
        self.assertEqual((rows["Chan"]["analysed"], rows["Chan"]["in_wiki"], rows["Chan"]["raw_here"]), (1, 1, 0))
        self.assertEqual(rows["Site"]["analysed"], 1)
        todo = wiki.pipeline_state()
        fetch = [t[1] for t in todo if t[0] == "fetch"]
        self.assertEqual(fetch, ["One talk: nothing fetched yet"])  # only the source nothing was learned from
        self.assertEqual(todo[-1][0], "raw")  # the missing raw text is a note after the real work
        self.assertIn("Chan", todo[-1][1])

    def test_skipped_pages_are_reported(self):
        wiki.fetch_page = lambda *a, **k: None  # the page had too little text
        code, out = self.run_cmd(wiki.cmd_fetch, only="Site")
        self.assertEqual(code, 1)
        self.assertIn("Nothing was fetched for: Site", out)
        self.assertEqual(json.loads(wiki.skipped_file().read_text())["https://example.com/a"]["why"], "too little text on the page")
        why = [t[1] for t in wiki.pipeline_state() if t[0] == "fetch" and t[1].startswith("Site")][0]
        self.assertIn("nothing usable came back", why)

    def test_fetch_only_with_an_unknown_name(self):
        code, out = self.run_cmd(wiki.cmd_fetch, only="Sight")
        self.assertEqual(code, 1)
        self.assertIn("No source is called 'Sight'", out)
        self.assertIn("  One talk", out)

    def test_synthesis_step_names_the_workflow_and_areas(self):
        (wiki.ANALYSIS / "CCCCCCCCCCC.json").write_text(json.dumps(analysis(topics=[{"name": "Easing and timing", "summary": "t"}])))
        js = wiki.ROOT / ".claude" / "workflows"
        js.mkdir(parents=True)
        shutil.copy(ROOT / ".claude" / "workflows" / "learn-synthesis.js", js)
        cmd = [t[2] for t in wiki.pipeline_state() if t[0] == "synthesis"][0]
        args = json.loads(cmd.split("with args ", 1)[1])
        self.assertIn("learn-synthesis", cmd)
        self.assertEqual((args["topics"], args["merge"]), (["motion"], True))

    def test_standards_stale_when_inputs_change(self):
        (wiki.ANALYSIS / "ek-a.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        doc = {"version": 1, "themes": [], "standards": [], "retired": [], "built_from": wiki.standard_inputs()}
        doc["content_hash"] = wiki.standards_hash(doc)
        wiki.STANDARDS.write_text(json.dumps(doc))
        self.assertFalse([t for t in wiki.pipeline_state() if t[0] == "standards"])
        a = analysis(authority="non-negotiable", summary="changed")
        a["rules"][0]["evidence"] = "a verbatim phrase from the source"           # evidence and summary feed no standard
        (wiki.ANALYSIS / "ek-a.json").write_text(json.dumps(a))
        self.assertFalse([t for t in wiki.pipeline_state() if t[0] == "standards"])
        a["rules"][0]["values"] = ["ease-out", "200ms"]                           # a rule's substance does
        (wiki.ANALYSIS / "ek-a.json").write_text(json.dumps(a))
        (wiki.ANALYSIS / "ek-b.json").write_text(json.dumps(analysis(authority="non-negotiable")))
        why = [t[1] for t in wiki.pipeline_state() if t[0] == "standards"][0]
        self.assertIn("1 new and 1 changed", why)


class AddRemove(Sandbox):
    def add(self, url, authority="reference", name=None):
        return self.run_cmd(wiki.cmd_add, url=url, authority=authority, name=name)

    def test_same_page_is_never_listed_twice(self):
        for url in ("http://www.example.com/a/", "https://example.com/a#top", "https://EXAMPLE.com/a"):
            with self.subTest(url):
                msg = self.exits(wiki.cmd_add, url=url, authority="reference", name=None)
                self.assertIn('part of "Site"', msg)
                self.assertIn("authority good-to-have", msg)  # the owner and the authority it already has
        msg = self.exits(wiki.cmd_add, url="https://youtu.be/AAAAAAAAAAA", authority="reference", name=None)
        self.assertIn('"One talk"', msg)

    def test_folder_and_prefix_are_never_shared(self):
        self.assertIn("already called", self.exits(wiki.cmd_add, url="https://other.org", authority="reference", name="Site"))
        self.assertIn("learn/raw/site already belongs", self.exits(wiki.cmd_add, url="https://other.org", authority="reference", name="SITE!"))
        self.assertIn("would mix", self.exits(wiki.cmd_add, url="https://other.org", authority="reference", name="site-x"))
        self.assertEqual(json.loads(wiki.SOURCES.read_text())["pages"][0]["name"], "Site")  # nothing written

    def test_github_names_come_from_owner_and_repo(self):
        code, out = self.add("https://github.com/acme/ui-kit", "non-negotiable")
        self.assertIn("learn/IMPROVING.md section 4", out)  # a new house source has a checklist
        self.add("https://github.com/other/tokens.git/")
        repos = {e["name"]: e for e in json.loads(wiki.SOURCES.read_text())["github_repos"]}
        self.assertEqual((repos["acme/ui-kit"]["folder"], repos["acme/ui-kit"]["id_prefix"]), ("raw/acme-ui-kit", "acme-ui-kit"))
        self.assertEqual(repos["other/tokens"]["id_prefix"], "other-tokens")

    def test_remove(self):
        self.sources(pages=[{"name": "Site", "urls": ["https://example.com/a", "https://example.com/b"], "folder": "raw/site",
                             "id_prefix": "site", "authority": "good-to-have"}])
        (wiki.ANALYSIS / "site-a.json").write_text(json.dumps(analysis(authority="good-to-have")))
        code, out = self.run_cmd(wiki.cmd_remove, what="https://www.example.com/b/")
        self.assertEqual(code, 0, out)
        self.assertEqual(json.loads(wiki.SOURCES.read_text())["pages"][0]["urls"], ["https://example.com/a"])  # one page of it
        code, out = self.run_cmd(wiki.cmd_remove, what="Site")
        self.assertEqual(json.loads(wiki.SOURCES.read_text())["pages"], [])
        self.assertIn("1 analysis files (site-a)", out)  # what was learned stays until removed by hand
        self.assertIn("learn-standards", out)
        code, out = self.run_cmd(wiki.cmd_remove, what="Nope")
        self.assertEqual(code, 1)
        self.assertIn("Chan", out)


class Flagged(Sandbox):
    def test_items_name_their_raw_file(self):
        self.raw("chan", "CCCCCCCCCCC")
        wiki.CITE_JSON.write_text(json.dumps({"results": [{"source": "CCCCCCCCCCC", "n": 0, "rule": "r", "verdict": "unsupported",
                                                           "confidence": 0.3}], "standards": []}))
        wiki.REVIEW_LOG = wiki.LEARN / "citation-review.json"
        self.assertEqual(wiki.flagged_items()["rules"][0]["raw"], "learn/raw/chan/CCCCCCCCCCC.txt")


class PageLabels(unittest.TestCase):
    def test_web_pages_get_page_labels(self):
        web = "---\nurl: https://sonner.emilkowal.ski/toast\n---\n\n## Metadata\n\n- Video ID: `sonner-toast`\n- Channel: Sonner docs (web)\n"
        out = wiki.page_labels(web)
        self.assertIn("- Page ID: `sonner-toast`", out)
        self.assertIn("- Publisher: Sonner docs (web)", out)
        video = web.replace("https://sonner.emilkowal.ski/toast", "https://www.youtube.com/watch?v=AAAAAAAAAAA")
        self.assertEqual(wiki.page_labels(video), video)

    def test_norm_url(self):
        self.assertEqual(wiki.norm_url("HTTP://www.Example.com/a/"), "example.com/a")
        self.assertEqual(wiki.norm_url("https://youtu.be/lkKGQVHrXzE"), wiki.norm_url("https://www.youtube.com/watch?v=lkKGQVHrXzE&t=3"))

    def test_synthesis_areas_come_from_the_workflow(self):
        areas = wiki.synthesis_areas()
        self.assertIn("Easing and timing", areas["motion"])
        self.assertEqual(len(areas), 10)


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

    def bump(self, why, head=None, built_from=False):
        wiki.head_standards = lambda: head
        return self.run_cmd(wiki.cmd_standards, bump=why, built_from=built_from)

    def test_first_release_is_decided_from_the_file(self):
        d = self.doc()
        d["standards"][0]["rule"] = "Use ease-out for enter and exit."
        wiki.STANDARDS.write_text(json.dumps(d))
        code, out = self.bump("first release")  # no history in the file: the first release, git not needed
        self.assertEqual(code, 0, out)
        doc = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual(wiki.check_standards(doc), [])
        self.assertEqual((doc["version"], [h["why"] for h in doc["history"]]), (1, ["first release"]))
        self.assertNotIn("built_from", doc)  # only the learn-standards merge stamps it (--built-from)

    def released(self):
        """v1, committed: the file and HEAD agree."""
        d = self.doc()
        wiki.bump(d, "v1", None)
        wiki.STANDARDS.write_text(json.dumps(d))
        return json.loads(json.dumps(d))

    def test_unchanged_standards_are_not_bumped(self):
        head = self.released()
        code, out = self.bump("again", head)
        self.assertEqual(code, 1)
        self.assertIn("Nothing to bump", out)
        self.assertEqual(json.loads(wiki.STANDARDS.read_text())["version"], 1)

    def test_bump_without_git_fails(self):
        self.released()
        d = json.loads(wiki.STANDARDS.read_text())
        d["standards"][0]["rule"] = "Use ease-out, always."
        wiki.STANDARDS.write_text(json.dumps(d))
        code, out = self.bump("edit", head=None)  # git cannot show HEAD: refuse, never rewrite history
        self.assertEqual(code, 1)
        self.assertIn("git", out)
        self.assertEqual(len(json.loads(wiki.STANDARDS.read_text())["history"]), 1)

    def test_v1_to_v2_and_a_second_bump_amends(self):
        head = self.released()
        d = json.loads(wiki.STANDARDS.read_text())
        d["standards"][0]["rule"] = "Use ease-out, always."
        new = dict(d["standards"][0], id="STD-easing-02", rule="Keep UI motion under 300ms.")
        d["standards"].append(new)
        wiki.STANDARDS.write_text(json.dumps(d))
        code, out = self.bump("sharper rule", head)
        self.assertEqual(code, 0, out)
        doc = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual(wiki.check_standards(doc), [])
        self.assertEqual(doc["version"], 2)
        s1, s2 = doc["standards"]
        self.assertEqual((s1["since"], s1["changed"], s2["since"]), (1, 2, 2))
        self.assertEqual(doc["history"][-1] | {"date": "-"}, {"version": 2, "date": "-", "why": "sharper rule",
                                                            "added": ["STD-easing-02"], "changed": ["STD-easing-01"], "retired": []})
        # Before the commit, another change: HEAD is still v1, so the uncommitted v2 entry is amended, not repeated.
        doc["standards"] = doc["standards"][:1]
        wiki.STANDARDS.write_text(json.dumps(doc))
        code, out = self.bump("drop the 300ms rule again", head)
        self.assertEqual(code, 0, out)
        self.assertIn("amended", out)
        doc = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual((doc["version"], len(doc["history"])), (2, 2))
        self.assertEqual(doc["history"][-1]["added"], [])  # measured against HEAD: STD-easing-02 never shipped
        self.assertEqual(doc["history"][-1]["why"], "sharper rule; drop the 300ms rule again")
        self.assertEqual(doc["retired"], [])
        self.assertEqual(wiki.check_standards(doc), [])

    def test_removed_standard_is_retired(self):
        head = self.released()
        d = json.loads(wiki.STANDARDS.read_text())
        d["standards"] = []
        wiki.STANDARDS.write_text(json.dumps(d))
        self.assertEqual(self.bump("the source withdrew it", head)[0], 0)
        doc = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual(doc["retired"], [{"id": "STD-easing-01", "version": 2, "why": "the source withdrew it"}])

    def test_built_from_only_on_request(self):
        self.released()
        code, out = self.run_cmd(wiki.cmd_standards, bump=None, built_from=True)
        self.assertEqual(code, 0, out)
        doc = json.loads(wiki.STANDARDS.read_text())
        self.assertEqual(doc["built_from"], wiki.standard_inputs())
        self.assertEqual((doc["version"], wiki.check_standards(doc)), (1, []))  # no bump, hash unchanged

    def test_new_fields_are_checked(self):
        d = self.doc()
        s = d["standards"][0]
        s.update({"settles": ["Q-motion-02"], "breaks_options": {"Q-motion-02": ["16-steps"]},
                  "constraints": [{"path": "motion.easing.*", "forbid": "accelerating-curve"},
                                  {"path": "motion.duration.*", "forbid": {"max-duration-ms": {"value": 300}}}],
                  "supersedes": ["DC-L04-20"], "applies_to": ["web", "css", "react"]})
        d["content_hash"] = wiki.standards_hash(d)
        self.assertEqual(wiki.check_standards(d), [])
        s.update({"settles": ["Q-motion-99"], "breaks_options": {"Q-motion-02": ["17-steps"]},
                  "constraints": [{"path": "motion.easing.*", "forbid": "slow"}, {"path": "motion.duration.*", "forbid": "max-duration-ms"}],
                  "supersedes": ["DC-L99-01"], "applies_to": ["web", "vue"]})
        d["content_hash"] = wiki.standards_hash(d)
        e = " | ".join(wiki.check_standards(d))
        for needle in ("settles 'Q-motion-99'", "no option '17-steps'", "forbids 'slow'", "needs a positive number",
                       "supersedes 'DC-L99-01'", "applies_to 'vue'"):
            self.assertIn(needle, e)
        s["settles"] = "Q-motion-02"
        d["content_hash"] = wiki.standards_hash(d)
        self.assertIn("settles must be a list", " | ".join(wiki.check_standards(d)))

    def test_one_path_one_value(self):
        d = self.doc()
        other = dict(d["standards"][0], id="STD-easing-02", engine={"path": "motion.easing.exit", "value": [0.23, 1.0, 0.32, 1]})
        d["standards"].append(other)
        d["content_hash"] = wiki.standards_hash(d)
        self.assertTrue(any("motion.easing.exit is set to different values" in e for e in wiki.check_standards(d)))
        other["engine"]["value"] = [0.23, 1, 0.32, 1]  # the same JSON: fine
        d["content_hash"] = wiki.standards_hash(d)
        self.assertEqual(wiki.check_standards(d), [])


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

    def test_sources_json_is_canonical(self):
        # wiki.py add and remove rewrite the file; canonical formatting keeps their diffs to the lines they change.
        text = (ROOT / "learn" / "sources.json").read_text(encoding="utf-8")
        self.assertEqual(text, json.dumps(json.loads(text), indent=2, ensure_ascii=False) + "\n")

    def test_wiki_pages_have_front_matter(self):
        # OpenWiki's lint expects front matter on every page but its index, log and schema.
        for p in sorted((ROOT / "learn" / "wiki").rglob("*.md")):
            if p.name not in ("index.md", "log.md", "schema.md"):
                with self.subTest(str(p.relative_to(ROOT))):
                    text = p.read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("---\n") and "\n---\n" in text[4:])

    def test_lock_file(self):
        lock = json.loads((ROOT / "learn" / "openwiki.lock.json").read_text())
        self.assertRegex(lock["commit"], r"^[0-9a-f]{40}$")


class BuildData(unittest.TestCase):
    """tools/build_data.py: what the house standards do to the stage files and questions.json (D02), and the bump guard."""

    def setUp(self):
        spec_bd = importlib.util.spec_from_file_location("build_data", ROOT / "tools" / "build_data.py")
        self.bd = importlib.util.module_from_spec(spec_bd)
        spec_bd.loader.exec_module(self.bd)
        self.tmp = Path(tempfile.mkdtemp())
        self.bd.SYN = self.tmp
        doc = {"version": 1, "standards": [
            {"id": "STD-easing-duration-11", "rule": "Exits are about 20% shorter than entrances.", "settles": ["Q-motion-02"]},
            {"id": "STD-easing-duration-01", "rule": "Use ease-out.", "breaks_options": {"Q-motion-02": ["16-steps"]}}], "retired": []}
        doc["content_hash"] = wiki.standards_hash(doc)
        (self.tmp / "standards.json").write_text(json.dumps(doc))
        self.q = {"id": "Q-motion-02", "stage": "S16", "question": "How many lengths?", "mode": "Expert", "time_weight": "low",
                  "fan_out": 1, "block_class": "G", "decides": [], "show_if": None, "ask": "How many?", "why": "w",
                  "options": [{"value": "4-semantic", "label": "4 steps", "effect": ""},
                              {"value": "16-steps", "label": "16 steps", "effect": "Material"}],
                  "default": "4-semantic", "default_source": "", "preview": "p", "use_avoid": None, "hook": None, "skip": "s",
                  "kind": "decision", "changes": []}

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_settled_questions_and_breaking_options_are_marked(self):
        marks = self.bd.standard_marks()
        md = self.bd.stage_md({"id": "S16", "n": 16, "title": "Motion", "screen": "s"}, [self.q], 1, marks=marks)
        self.assertIn("- **Settled by:** STD-easing-duration-11: Exits are about 20% shorter than entrances. Don't ask; the value "
                      "is locked. Change it only through engine.py standard override when the person explicitly asks.", md)
        self.assertIn("`16-steps` 16 steps (breaks STD-easing-duration-01): Material", md)
        self.assertIn("**Planned** or **Settled by**", md)
        q = self.bd.build_questions({"questions": [self.q]}, marks)["questions"][0]
        self.assertEqual(q["settled_by"], ["STD-easing-duration-11"])
        self.assertEqual([o.get("breaks") for o in q["options"]], [None, ["STD-easing-duration-01"]])

    def test_unbumped_standards_stop_the_build(self):
        self.assertFalse(self.bd.standards_unbumped())
        doc = json.loads((self.tmp / "standards.json").read_text())
        doc["standards"][1]["rule"] = "Use ease-in."
        (self.tmp / "standards.json").write_text(json.dumps(doc))
        self.assertTrue(self.bd.standards_unbumped())


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

    def test_edited_analysis_is_reingested_without_force(self):
        self.raw("chan", "CCCCCCCCCCC", title="Easing talk")
        aj = wiki.ANALYSIS / "CCCCCCCCCCC.json"
        aj.write_text(json.dumps(analysis()))
        wiki.WIKI.mkdir(parents=True, exist_ok=True)
        saved = wiki.openwiki
        wiki.openwiki = lambda *a, **k: 0
        try:
            self.run_cmd(wiki.cmd_ingest, force=False)
            self.assertEqual(wiki.manifest_of_wiki()["CCCCCCCCCCC"]["analysis_hash"], wiki.file_hash(aj))
            a = analysis(summary="A new summary after the analysis was fixed.")
            aj.write_text(json.dumps(a))  # the raw file did not change, so OpenWiki alone would skip it
            code, out = self.run_cmd(wiki.cmd_ingest, force=False)
        finally:
            wiki.openwiki = saved
        self.assertIn('"processed": 1', out)
        page = next((wiki.WIKI / "sources").glob("CCCCCCCCCCC-*.md")).read_text()
        self.assertIn("A new summary after the analysis was fixed.", page)
        self.assertEqual(wiki.manifest_of_wiki()["CCCCCCCCCCC"]["analysis_hash"], wiki.file_hash(aj))
        self.assertEqual([t for t in wiki.pipeline_state() if t[0] == "ingest"], [])

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
