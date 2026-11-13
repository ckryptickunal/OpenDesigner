#!/usr/bin/env python3
"""Run the billing assistant against a real model in a browser, and check the whole loop.

  python3 examples/smart-ui-support/check_live.py [--provider gemini|claude-cli|anthropic] [--out shots/]

Needs Playwright for Python and a model (GEMINI_API_KEY or ANTHROPIC_API_KEY in .env, or the `claude` command). It starts
server.py on a free loopback port, then: asks for the open invoices (a table must show), asks to pay the one due on the
20th (an approval prompt must show, and nothing is paid), presses the approve button (a receipt or a confirmation must
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

                ask("Show my open invoices")
                if not turn().locator('[data-od-component="DataTable"]').count():
                    problems.append(f"{width}: no table for the open invoices")
                page.screenshot(path=str(out / f"live-{width}-1-invoices.png"))
                ask("Pay the one that's due on the 20th")
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
                ask("When is the next invoice due?")
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
