#!/usr/bin/env python3
"""Tests for tools/growth_check.py: each check with a known-good and a known-bad case. Offline, standard library."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import growth_check as g  # noqa: E402

PAGE = '<!doctype html><html><head><title>x</title></head><body>x</body></html>'
NOINDEX = '<!doctype html><html><head><meta name="robots" content="noindex"></head><body>x</body></html>'


class Robots(unittest.TestCase):
    def test_all_allowed(self):
        self.assertEqual(g.robots_blocked("User-agent: *\nAllow: /\n"), [])

    def test_star_disallow_blocks_everyone(self):
        self.assertEqual(g.robots_blocked("User-agent: *\nDisallow: /\n"), g.MUST_ALLOW)

    def test_named_group_wins(self):
        txt = "User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nDisallow: /\n"
        self.assertEqual(g.robots_blocked(txt), ["OAI-SearchBot"])

    def test_training_bot_block_is_not_a_failure(self):
        self.assertEqual(g.robots_blocked("User-agent: GPTBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n"), [])


class Readme(unittest.TestCase):
    GOOD = "Version 0.3.1, today. 82 ready-made parts. It copies in the nine skill folders. The guide lists the other six."

    def test_good(self):
        self.assertEqual(g.readme_facts(self.GOOD, "0.3.1", 82, 9), [])

    def test_bad(self):
        bad = g.readme_facts(self.GOOD, "0.4.0", 90, 10)
        self.assertEqual(len(bad), 4)
        self.assertIn("0.4.0", bad[0])

    def test_opening_words(self):
        self.assertEqual(g.readme_opening_words("A design system for Claude Code and Cursor, written as design tokens."), [])
        self.assertEqual(g.readme_opening_words('<img alt="design system Claude Code Cursor design tokens"> Hello'),
                         ["design system", "Claude Code", "Cursor", "design tokens"])


class Site(unittest.TestCase):
    def make(self, pages, sitemap, llms="# X\n\n## Questions people ask, and the page that answers each\n", full=""):
        d = Path(tempfile.mkdtemp())
        for path, html in pages.items():
            f = d / path.strip("/") / "index.html" if path != "/" else d / "index.html"
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(html)
        (d / "sitemap.xml").write_text("<urlset>" + "".join(f"<url><loc>https://x.test{p}</loc></url>" for p in sitemap) + "</urlset>")
        (d / "robots.txt").write_text("User-agent: *\nAllow: /\n")
        (d / "llms.txt").write_text(llms)
        (d / "llms-full.txt").write_text(full)
        return d

    def test_sitemap_matches(self):
        d = self.make({"/": PAGE, "/docs/a/": PAGE, "/hidden/": NOINDEX}, ["/", "/docs/a/"])
        self.assertEqual(g.built_pages(d), {"/", "/docs/a/"})
        self.assertEqual(g.sitemap_paths(d, "https://x.test"), {"/", "/docs/a/"})

    def test_sitemap_mismatch(self):
        d = self.make({"/": PAGE, "/docs/a/": PAGE}, ["/", "/docs/gone/"])
        self.assertEqual(g.built_pages(d) - g.sitemap_paths(d, "https://x.test"), {"/docs/a/"})
        self.assertEqual(g.sitemap_paths(d, "https://x.test") - g.built_pages(d), {"/docs/gone/"})


if __name__ == "__main__":
    unittest.main()
