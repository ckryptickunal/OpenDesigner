#!/usr/bin/env python3
"""Tests for tools/check_links.py: a link that starts with / in site/docs is checked against the addresses site/build.py
makes, so a real website route passes and a made-up one still fails.

  python3 tools/test_check_links.py
"""
import contextlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_links as C  # noqa: E402


class SiteLinks(unittest.TestCase):
    def test_routes_the_build_makes_pass(self):
        for rel in ("/", "/docs/", "/docs/install/", "/changelog/", "/tour/", "/showcase/", "/book/", "/library/",
                    "/docs/install/index.md", "/index.md", "/llms.txt", "/llms-full.txt", "/sitemap.xml", "/robots.txt", "/version.json"):
            self.assertIsNone(C.site_link(rel), rel)

    def test_every_docs_page_and_library_part_is_a_route(self):
        routes, _ = C.site()
        for f in C.SITE_DOCS.glob("*.md"):
            path = {"index": "/docs/", "changelog": "/changelog/"}.get(f.stem, f"/docs/{f.stem}/")
            self.assertIn(path, routes, f.name)
        lib = C.ROOT / "skills" / "opendesigner" / "assets" / "library"
        for d in (p for p in lib.iterdir() if (p / "meta.json").exists() and (p / "component.html").exists()):
            self.assertIn(f"/library/{d.name}/", routes, d.name)

    def test_a_made_up_route_still_fails(self):
        for rel in ("/docs/no-such-page/", "/nowhere/", "/tours/", "/docs/install/missing.md", "/library/no-such-part/"):
            self.assertIn("no page or file", C.site_link(rel), rel)

    def test_a_redirect_or_a_missing_slash_names_the_address_to_use(self):
        self.assertIn("/docs/install/", C.site_link("/install/"))
        self.assertIn("trailing slash", C.site_link("/tour"))

    def test_main_checks_site_docs_by_route_and_other_files_by_path(self):
        C.site()  # load the routes from the real site/build.py before pointing the checker at a temporary repo
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "site" / "docs").mkdir(parents=True)
            (root / "docs").mkdir()
            (root / "site" / "docs" / "page.md").write_text(
                "[tour](/tour/) [log](/changelog/#latest) [gone](/docs/gone/) [file](../../docs/note.md)\n")
            (root / "docs" / "note.md").write_text("[a route is not a repo file](/tour/)\n")
            out = io.StringIO()
            with mock.patch.object(C, "ROOT", root), mock.patch.object(C, "SITE_DOCS", root / "site" / "docs"), \
                    contextlib.redirect_stdout(out):
                code = C.main([])
        text = out.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("site/docs/page.md:1: /docs/gone/", text)
        self.assertIn("docs/note.md:1: /tour/", text)
        self.assertNotIn("page.md:1: /tour/", text)
        self.assertNotIn("/changelog/", text)
        self.assertIn("5 relative links checked, 2 broken", text)

    def test_the_root_llms_txt_may_only_link_to_files_that_exist(self):
        gh = "https://raw.githubusercontent.com/ckryptickunal/OpenDesigner/main/"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "note.md").write_text("plain\n")
            (root / "llms.txt").write_text(f"- [Note]({gh}docs/note.md): here\n- [Moved]({gh}docs/moved.md): gone\n"
                                           "- [Folder](https://github.com/ckryptickunal/OpenDesigner/tree/main/docs): a folder\n"
                                           "- [Site](https://opendesigner.dev/llms.txt): not a repository file\n")
            out = io.StringIO()
            with mock.patch.object(C, "ROOT", root), mock.patch.object(C, "SITE_DOCS", root / "site" / "docs"), \
                    contextlib.redirect_stdout(out):
                code = C.main([])
        self.assertEqual(code, 1)
        self.assertIn("llms.txt:2: docs/moved.md", out.getvalue())
        self.assertIn("3 relative links checked, 1 broken", out.getvalue())

    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_a_git_checkout_reads_only_what_git_would_commit(self):     # issue 72
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            iso = mock.patch.dict(os.environ, {"HOME": tmp, "XDG_CONFIG_HOME": tmp, "GIT_CONFIG_GLOBAL": os.devnull,
                                               "GIT_CONFIG_NOSYSTEM": "1"})  # never the real home or the machine's git config
            iso.start()
            self.addCleanup(iso.stop)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("site/.cache/\n")
            (root / "site" / ".cache").mkdir(parents=True)
            (root / "site" / ".cache" / "copied.md").write_text("[gone](missing.md)\n")       # ignored: never read
            (root / "tracked.md").write_text("[ok](new.md)\n")
            (root / "new.md").write_text("[gone](nowhere.md)\n")                              # untracked, not ignored: read
            subprocess.run(["git", "-C", str(root), "add", "tracked.md"], check=True)
            out = io.StringIO()
            with mock.patch.object(C, "ROOT", root), mock.patch.object(C, "SITE_DOCS", root / "site" / "docs"), \
                    contextlib.redirect_stdout(out):
                code = C.main([])
                named = C.main(["site/.cache/copied.md"])                                     # a file named on purpose is read
        text = out.getvalue()
        self.assertEqual((code, named), (1, 1))
        self.assertIn("new.md:1: nowhere.md", text)
        self.assertIn("2 relative links checked, 1 broken", text)
        self.assertIn("site/.cache/copied.md:1: missing.md", text)
        self.assertEqual(text.count("copied.md"), 1)


if __name__ == "__main__":
    unittest.main()
