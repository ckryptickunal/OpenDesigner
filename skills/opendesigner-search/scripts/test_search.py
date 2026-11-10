#!/usr/bin/env python3
"""Tests for search.py: python3 skills/opendesigner-search/scripts/test_search.py"""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import search as s  # noqa: E402

FIXTURE = HERE.parents[2] / "evals" / "search-audit" / "site"


def page(title="A page about one clear thing", h1="One clear thing", body="Words a person came for. " * 10, head="", canonical="/x"):
    can = f'<link rel="canonical" href="{canonical}">' if canonical else ""
    return (f'<!doctype html><html lang="en"><head><title>{title}</title><meta name="description" content="A short description of '
            f'this page that says what it answers for the reader.">{can}{head}</head><body><a href="/">Home</a><h1>{h1}</h1>'
            f"<p>{body}</p></body></html>")


def site(files):
    d = tempfile.mkdtemp()
    for rel, text in files.items():
        p = Path(d) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return d


def codes(result, sev=None):
    return sorted((f["code"], f["severity"]) for f in result["findings"] if sev is None or f["severity"] == sev)


BASE = {"robots.txt": "User-agent: *\nAllow: /\nSitemap: https://a.example/sitemap.xml\n",
        "sitemap.xml": "<urlset><url><loc>https://a.example/</loc></url></urlset>", "llms.txt": "# A\n",
        "index.html": page(canonical="https://a.example/")}


class Fixture(unittest.TestCase):
    def test_the_eval_site_shows_its_five_planted_problems_and_nothing_else(self):
        r = s.audit(FIXTURE, "https://ledgerly.example")
        loud = sorted((f["code"], f["where"]) for f in r["findings"] if f["severity"] != "info")
        self.assertEqual(loud, [("SE-01", "robots.txt"), ("SE-03", "pricing.html"), ("SE-05", "docs/index.html"),
                                ("SE-08", "app.html"), ("SE-09", "faq.html")])
        gpt = [f for f in r["findings"] if f["title"] == "Training crawlers blocked"]
        self.assertEqual((gpt[0]["severity"], "GPTBot" in gpt[0]["evidence"]), ("info", True))  # the owner's choice

    def test_the_trap_site_shows_only_its_two_real_problems(self):
        r = s.audit(HERE.parents[2] / "evals" / "search-traps" / "site", "https://ledgerly.example")
        loud = sorted((f["code"], f["severity"], f["where"]) for f in r["findings"] if f["severity"] != "info")
        self.assertEqual(loud, [("SE-04", "error", "old-pricing.html"), ("SE-04", "warn", "drafts/launch.html")])
        info = {f["title"] for f in r["findings"] if f["severity"] == "info"}
        self.assertEqual(info, {"Training crawlers blocked", "FAQPage: no Google rich result"})   # the owner's choice; keep the markup

    def test_read_only(self):
        before = sorted((str(p), p.stat().st_mtime) for p in FIXTURE.rglob("*"))
        s.audit(FIXTURE)
        self.assertEqual(sorted((str(p), p.stat().st_mtime) for p in FIXTURE.rglob("*")), before)


class Robots(unittest.TestCase):
    def test_search_bots_error_user_and_training_bots_inform(self):
        g, maps = s.parse_robots("User-agent: *\nDisallow: /\n\nUser-agent: Googlebot\nUser-agent: Bingbot\nAllow: /\n")
        self.assertFalse(s.blocked_everywhere(g, "Googlebot"))                 # its own group wins over '*'
        self.assertTrue(s.blocked_everywhere(g, "OAI-SearchBot"))              # falls back to '*'
        self.assertEqual(maps, [])
        found = []
        s.robots_findings("User-agent: *\nDisallow: /\n", lambda *x: found.append(x))
        sev = {}
        for x in found:
            sev.setdefault(x[1], []).append(x[2])
        self.assertEqual(len(sev["error"]), len(s.SEARCH_BOTS))
        self.assertTrue(all("robots.txt blocks" in t for t in sev["error"]))
        self.assertIn("Training crawlers blocked", sev["info"])
        self.assertIn("robots.txt names no sitemap", sev["warn"])

    def test_cli_table(self):
        d = site({"robots.txt": "User-agent: GPTBot\nDisallow: /\n"})
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(s.main(["robots", os.path.join(d, "robots.txt")]), 0)
        self.assertRegex(out.getvalue(), r"GPTBot +blocked")
        self.assertRegex(out.getvalue(), r"OAI-SearchBot +allowed")


class Pages(unittest.TestCase):
    def test_a_clean_site_has_no_warnings(self):
        self.assertEqual(codes(s.audit(site(BASE), "https://a.example"), "warn") + codes(s.audit(site(BASE)), "error"), [])

    def test_faq_and_howto_that_match_the_page_are_info_never_errors(self):
        faq = ('<script type="application/ld+json">{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Words a person '
               'came for."}]}</script><script type="application/ld+json">{"@type":"HowTo","name":"x"}</script>')
        r = s.audit(site(dict(BASE, **{"index.html": page(head=faq, canonical="https://a.example/")})), "https://a.example")
        se09 = [f for f in r["findings"] if f["code"] == "SE-09"]
        self.assertEqual(sorted(f["severity"] for f in se09), ["info", "info"])
        self.assertTrue(all("no Google rich result" in f["title"] for f in se09))
        self.assertNotIn("remove", " ".join(f["evidence"] + f["fix"] for f in se09).lower())

    def test_faq_text_split_by_inline_tags_still_matches(self):
        faq = ('<script type="application/ld+json">{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is it an '
               'AI-made app?"}]}</script>')
        html_ = page(head=faq, canonical="https://a.example/", body="Is it an <abbr>AI</abbr>-made app? No. " * 8)
        r = s.audit(site(dict(BASE, **{"index.html": html_})), "https://a.example")
        self.assertEqual([f["severity"] for f in r["findings"] if f["code"] == "SE-09"], ["info"])

    def test_fragments_are_not_pages(self):
        r = s.audit(site(dict(BASE, **{"parts/card.html": "<style>.c{}</style><div class=c>Card</div>"})))
        self.assertEqual(r["pages"], 1)
        self.assertIn(("SE-00", "info"), codes(r))

    def test_broken_json_ld_and_heading_and_title_problems(self):
        r = s.audit(site(dict(BASE, **{
            "index.html": page(head='<script type="application/ld+json">{oops</script>', canonical="https://a.example/"),
            "a.html": page(h1="One</h1><h1>Two", canonical="/a.html"), "b.html": page(h1="", canonical="/b.html").replace("<h1></h1>", ""),
            "c.html": page(title="", canonical="/c.html")})))
        got = codes(r)
        for want in [("SE-09", "error"), ("SE-07", "warn"), ("SE-07", "error"), ("SE-05", "error")]:
            self.assertIn(want, got)

    def test_noindex_conflicts(self):
        noidx = '<meta name="robots" content="noindex">'
        r = s.audit(site(dict(BASE, **{
            "sitemap.xml": "<urlset><url><loc>https://a.example/</loc></url><url><loc>https://a.example/p.html</loc></url></urlset>",
            "p.html": page(head=noidx, canonical="https://a.example/"), "index.html": page(canonical="https://a.example/") + '<a href="/p.html">p</a>'})),
            "https://a.example")
        self.assertIn(("SE-04", "error"), codes(r))
        self.assertIn(("SE-03", "error"), codes(r))

    def test_noindex_behind_a_disallow_is_named(self):
        noidx = '<meta name="robots" content="noindex">'
        r = s.audit(site(dict(BASE, **{"robots.txt": "User-agent: *\nAllow: /\nDisallow: /drafts/\nSitemap: https://a.example/sitemap.xml\n",
                                       "drafts/plan.html": page(head=noidx, canonical=None)})))
        hit = [f for f in r["findings"] if f["title"] == "noindex behind a robots.txt Disallow"]
        self.assertEqual([(f["severity"], f["where"]) for f in hit], [("warn", "drafts/plan.html")])
        self.assertFalse([f for f in r["findings"] if f["code"] == "SE-11"])     # a noindex page needs no inbound links
        g, _m = s.parse_robots("User-agent: *\nDisallow: /a\nAllow: /a/ok\n")
        self.assertTrue(s.disallowed(g, "Googlebot", "/a/x"))
        self.assertFalse(s.disallowed(g, "Googlebot", "/a/ok/page"))            # the longer Allow wins
        self.assertFalse(s.disallowed(g, "Googlebot", "/b"))

    def test_orphans_duplicates_and_sitemap_gaps(self):
        r = s.audit(site(dict(BASE, **{"lost.html": page(canonical="/lost.html"), "twin.html": page(canonical="/twin.html")})))
        warns = [(f["code"], f["title"]) for f in r["findings"] if f["severity"] == "warn"]
        self.assertIn(("SE-11", "No page links here"), warns)
        self.assertTrue(any(c == "SE-05" and "share one title" in t for c, t in warns))
        self.assertTrue(any(c == "SE-02" and "missing from the sitemap" in t for c, t in warns))

    HOME = page(h1="Invoices that chase themselves", canonical="https://a.example/",
                body="Reminders go out on day 3, 7 and 14. <h2>How reminders work</h2> Each one waits. <h2>Pricing for firms</h2> "
                     "Three plans. <h2>Data and security</h2> Your data stays in the EU. " * 2)
    PRICING = page(title="Ledgerly pricing for small firms", h1="Pricing", canonical="/pricing.html", body="Each plan and what it costs per month. " * 6)

    def llms(self, text):
        r = s.audit(site(dict(BASE, **{"index.html": self.HOME, "pricing.html": self.PRICING, "llms.txt": text})), "https://a.example")
        return {f["title"]: f for f in r["findings"] if f["code"] == "SE-10"}

    def test_llms_txt_written_for_an_earlier_page_is_named(self):
        got = self.llms("# Ledgerly\n\n> The AI operating system for dental clinics.\n\nEvery chart audited and covered.\n"
                        "Reminders go out on day 3, 7 and 14 and cut late payments by 40%.\n\n## How reminders work\n"
                        "- [Pricing](/pricing.html): what each plan costs\n- [Old tour](https://a.example/tour.html)\n")
        unsaid = got["llms.txt says what no page says"]
        self.assertEqual(unsaid["severity"], "warn")
        self.assertTrue(unsaid["evidence"].startswith("3 line(s): "), unsaid["evidence"])
        for bit in ('"The AI operating system for dental clinics."', '"Every chart audited and covered."', "(no page shows 40%)"):
            self.assertIn(bit, unsaid["evidence"])
        self.assertNotIn("what each plan costs", unsaid["evidence"])          # the pricing page says it
        self.assertEqual(got["llms.txt links pages the build does not have"]["evidence"], "https://a.example/tour.html")
        gaps = got["Home page sections llms.txt does not cover"]
        self.assertEqual(gaps["evidence"], "it covers 2 of 3; not: Data and security")

    def test_llms_txt_that_matches_the_pages_is_quiet(self):
        got = self.llms("# Ledgerly\n\n> Invoices that chase themselves: reminders go out on day 3, 7 and 14.\n\n## Docs\n"
                        "- [Pricing](/pricing.html): each plan and what it costs\n\n## Optional\n- [Home](/): how reminders work, pricing, data and security\n")
        self.assertEqual(sorted(got), [])
        short = self.llms("# Ledgerly\n\n> Invoices that chase themselves.\n")   # a short summary covers no section: not judged on them
        self.assertNotIn("Home page sections llms.txt does not cover", short)

    def test_llms_txt(self):
        self.assertIn(("SE-10", "info"), codes(s.audit(site({k: v for k, v in BASE.items() if k != "llms.txt"}))))
        self.assertIn(("SE-10", "warn"), codes(s.audit(site(dict(BASE, **{"llms.txt": "Ledgerly\n"})))))


class Cli(unittest.TestCase):
    def test_live_is_off_until_the_owner_approves_it(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(s.main(["audit", "--live", "https://a.example"]), 2)
        self.assertIn("waits for the owner's approval", out.getvalue())
        self.assertFalse(s.LIVE_APPROVED)

    def test_network_stays_in_one_https_function(self):
        src = (HERE / "search.py").read_text(encoding="utf-8")
        self.assertEqual(src.count("urlopen("), 1)
        self.assertNotIn("import urllib", src.split("def fetch_https", 1)[0])  # imported only inside the one function
        with self.assertRaises(ValueError):
            s.fetch_https("http://a.example")

    def test_json_output_and_exit_code(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = s.main(["audit", str(FIXTURE), "--json"])
        data = json.loads(out.getvalue())
        self.assertEqual((code, data["pages"]), (1, 5))


if __name__ == "__main__":
    unittest.main(verbosity=1)
