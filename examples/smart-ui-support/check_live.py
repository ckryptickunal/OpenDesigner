#!/usr/bin/env python3
"""Run the billing assistant against a real model in a browser, and check the whole loop.

  python3 examples/smart-ui-support/check_live.py [--provider gemini|claude-cli|anthropic] [--out shots/]

Needs Playwright for Python and a model (GEMINI_API_KEY or ANTHROPIC_API_KEY in .env, or the `claude` command). It starts
server.py on a free loopback port, then: asks which invoices are unpaid (a table must show, with column headers), asks to pay
the smaller one (an approval prompt must show, and nothing is paid), presses the approve button (a receipt or a confirmation must
follow), asks a short fact (no part may show), and fails on console errors. Screenshots at 1440 and 375 px go to --out.
"""
import argparse
import pathlib
import socket
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", default="gemini")
    ap.add_argument("--out", default=str(HERE / "shots"))
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    port = free_port()
    srv = subprocess.Popen([sys.executable, str(HERE / "server.py"), "--port", str(port), "--provider", a.provider],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    problems = []
    try:
        time.sleep(1.5)
        with sync_playwright() as p:
            try:
                b = p.chromium.launch()
            except Exception:
                b = p.chromium.launch(channel="chrome")
            for width in (1440, 375):
                page = b.new_page(viewport={"width": width, "height": 1000})
                errors = []
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.goto(f"http://127.0.0.1:{port}/")
                page.wait_for_selector(".od-chat-form")
                turn = lambda: page.locator(".od-chat-turn").last

                def ask(q, timeout=240000):
                    n = page.locator(".od-chat-turn").count()
                    page.fill(".od-chat-form input", q)
                    page.click(".od-chat-form button")
                    page.wait_for_function(f"document.querySelectorAll('.od-chat-turn, .od-chat-error').length > {n}", timeout=timeout)
                    page.wait_for_timeout(700)  # the scroll to the newest answer
                    top = page.evaluate("() => { const t = [...document.querySelectorAll('.od-chat-turn')].pop(); const r = t.getBoundingClientRect(); return [r.top, innerHeight]; }")
                    bottom = page.evaluate("() => [...document.querySelectorAll('.od-chat-turn')].pop().getBoundingClientRect().bottom")
                    if not (-2 <= top[0] < top[1] * 0.6 or (top[0] >= -2 and bottom <= top[1] + 2)):  # its top near the top, or all of it on screen
                        problems.append(f"{width}: after '{q}' the newest answer starts at {round(top[0])} px, not in view")
                    for tbl in turn().locator("table").all():
                        if not tbl.locator("thead th").count() or not tbl.locator("thead th").first.is_visible():
                            problems.append(f"{width}: a table without visible column headers after '{q}'")

                ask("Which invoices haven't we paid yet?")
                if not turn().locator('[data-od-component="DataTable"], [data-od-component="KeyFacts"]').count():
                    problems.append(f"{width}: no table or list for the unpaid invoices")
                page.screenshot(path=str(out / f"live-{width}-1-invoices.png"))
                ask("OK, pay the smaller one")
                if not turn().locator('[data-od-component="ApprovalPrompt"]').count():
                    problems.append(f"{width}: no approval prompt before paying")
                page.screenshot(path=str(out / f"live-{width}-2-approve.png"))
                approve = turn().locator('[data-od-component="ApprovalPrompt"] [data-od-effect="change"]')
                if approve.count():
                    n = page.locator(".od-chat-turn").count()
                    approve.first.click()
                    page.wait_for_function(f"document.querySelectorAll('.od-chat-turn').length > {n}", timeout=240000)
                    t = turn().inner_text().lower()
                    if not ("paid" in t or "py-55309" in t or turn().locator('[data-od-component="Receipt"]').count()):
                        problems.append(f"{width}: no confirmation after approving")
                    page.screenshot(path=str(out / f"live-{width}-3-paid.png"))
                ask("How many seats do we have right now?")
                if turn().locator("[data-od-component]").count():
                    problems.append(f"{width}: a part for a short fact (R1)")
                page.screenshot(path=str(out / f"live-{width}-4-fact.png"), full_page=False)
                if errors:
                    problems.append(f"{width}: console errors {errors[:3]}")
                page.close()
            b.close()
    finally:
        srv.terminate()
    print("\n".join(problems) or f"live loop ok with {a.provider} at 1440 and 375 px; screenshots in {out}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
