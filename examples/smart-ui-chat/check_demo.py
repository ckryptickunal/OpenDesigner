#!/usr/bin/env python3
"""Play the whole Smart UI demo in a browser and check it, in two systems, at 1440 and 375 px.

  python3 examples/smart-ui-chat/check_demo.py [--out shots/]     (needs Playwright for Python; never installs it)

It serves the repository on 127.0.0.1 for the run, then for each system: plays every question, presses Choose on the
Standard fare, confirms the booking (the receipt must appear), sends the broken answer (it must be refused and nothing
drawn), switches to text only, and fails on any console error or on an answer the page did not check. Screenshots of
each step go to --out.
"""
import argparse
import contextlib
import functools
import http.server
import pathlib
import sys
import threading

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SYSTEMS = {"orvell": "opendesigner/build/css/tokens.css", "devtool-dense": "../devtool-dense/build/css/tokens.css"}


@contextlib.contextmanager
def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}/examples/smart-ui-chat/index.html"
    finally:
        srv.shutdown()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(HERE / "shots"))
    a = ap.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright for Python is not installed: pip install playwright && playwright install chromium")
        return 2
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    problems = []
    with serve() as url, sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        for width in (1440, 375):
            for name, href in SYSTEMS.items():
                page = b.new_page(viewport={"width": width, "height": 900})
                errors = []
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" and "favicon" not in m.text else None)
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.goto(url)
                page.select_option("#system", href)
                page.wait_for_selector("od-surface [data-od-component]")
                shot = lambda step: page.screenshot(path=str(out / f"{name}-{width}-{step}.png"), full_page=False)
                shot("1-flights")
                page.get_by_role("button", name="Compare the fares on the 08:40").click()
                page.wait_for_selector('[data-od-component="Comparison"]')
                page.locator('[data-od-component="Comparison"] [data-od-event="choose_fare"]').nth(1).click()
                page.wait_for_selector('[data-od-component="ApprovalPrompt"]')
                page.locator('[data-od-component="ApprovalPrompt"]').scroll_into_view_if_needed()
                shot("2-approve")
                page.locator('[data-od-component="ApprovalPrompt"] [data-od-event="book_flight"]').click()
                page.wait_for_selector('[data-od-component="Receipt"]', timeout=5000)
                page.locator('[data-od-component="Receipt"]').scroll_into_view_if_needed()
                shot("3-receipt")
                for q in ("When does check-in open?", "Where's my hotel?", "Book a transfer for when I land", "What are the key details of my hotel booking?"):
                    page.get_by_role("button", name=q).click()
                page.wait_for_selector('[data-od-component="KeyFacts"]')
                shot("4-more")
                n_before = page.locator("od-surface [data-od-component]").count()
                page.get_by_role("button", name="Send a broken answer").click()
                page.wait_for_selector(".errors li")
                n_after = page.locator("od-surface [data-od-component]").count()
                if n_after != n_before:
                    problems.append(f"{name} {width}: the broken answer drew something")
                page.locator(".errors").scroll_into_view_if_needed()
                shot("5-refused")
                checked = page.locator(".checked").all_inner_texts()
                if any("failed" in c for c in checked):
                    problems.append(f"{name} {width}: a recorded answer failed its checks")
                page.get_by_role("button", name="Text only").click()
                page.wait_for_selector("pre.fallback")
                shot("6-text-only")
                if errors:
                    problems.append(f"{name} {width}: console errors: {errors[:3]}")
                page.close()
        b.close()
    print("\n".join(problems) or f"demo ok in {len(SYSTEMS)} systems at 1440 and 375 px; screenshots in {out}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
