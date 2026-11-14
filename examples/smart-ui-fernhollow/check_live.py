#!/usr/bin/env python3
"""Run the Fernhollow council assistant against a real model in a browser, check the whole loop, and time it.

  python3 examples/smart-ui-fernhollow/check_live.py [--provider gemini|claude-cli|anthropic] [--model gemini-3.1-flash-lite] [--out shots/]

Needs Playwright for Python and a model (GEMINI_API_KEY in .env, or the `claude` command). It starts server.py on a free
loopback port, then asks about fines (the fine shows, with the day the discount ends, and no payment prompt), presses the
card's Pay button or asks to pay (an approval prompt must show that paying ends the right to challenge, and nothing is paid
until it is approved), approves (a receipt, without "successful"), asks where the application is (the steps, with the wait
for a document as the current one), asks which documents are still needed (no raw dates, and no sideways scroll on a phone),
and asks a short fact (no part may show). For every turn it measures, in
the page, the time from pressing Send to the first thing on screen (the part's skeleton or the first words) and to the
checked answer. Fails on console errors. Screenshots at 1440 and 375 px go to --out.
"""
import argparse
import os
import pathlib
import re
import socket
import statistics
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
    ap.add_argument("--model", help="sets OD_GEMINI_MODEL or OD_CLAUDE_MODEL for the server")
    ap.add_argument("--out", default=str(HERE / "shots"))
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    if a.model:
        env["OD_CLAUDE_MODEL" if "claude" in a.model else "OD_GEMINI_MODEL"] = a.model
    port = free_port()
    srv = subprocess.Popen([sys.executable, str(HERE / "server.py"), "--port", str(port), "--provider", a.provider],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
    problems, first, full = [], [], []
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
                turn = lambda: page.locator(".od-chat-turn:not(.od-chat-pending)").last

                def timed(start_click):
                    """Press, then wait for the first sign of an answer and for the checked answer; both times in ms, from the page's clock."""
                    n = page.locator(".od-chat-turn:not(.od-chat-pending), .od-chat-error").count()
                    page.evaluate("""(n) => { window.__t0 = performance.now(); window.__first = null;
                      const log = document.querySelector('.od-chat-log');
                      const seen = () => log.querySelector('.od-chat-pending [data-od-component], .od-chat-pending .od-chat-bot')
                        || log.querySelectorAll('.od-chat-turn:not(.od-chat-pending), .od-chat-error').length > n;
                      const mo = new MutationObserver(() => { if (window.__first === null && seen()) window.__first = performance.now() - window.__t0; });
                      mo.observe(log, { childList: true, subtree: true, characterData: true }); window.__mo = mo; }""", n)
                    start_click()
                    page.wait_for_function(f"document.querySelectorAll('.od-chat-turn:not(.od-chat-pending), .od-chat-error').length > {n}", timeout=240000)
                    t = page.evaluate("() => { window.__mo.disconnect(); return [window.__first, performance.now() - window.__t0]; }")
                    first.append(t[0] if t[0] is not None else t[1])
                    full.append(t[1])
                    page.wait_for_timeout(600)  # the scroll to the newest answer

                def ask(q):
                    page.fill(".od-chat-form input", q)
                    timed(lambda: page.click(".od-chat-form button"))
                    top, bottom, h = page.evaluate("() => { const t = [...document.querySelectorAll('.od-chat-turn')].pop().getBoundingClientRect(); return [t.top, t.bottom, innerHeight]; }")
                    if not (-2 <= top < h * 0.6 or (top >= -2 and bottom <= h + 2)):
                        problems.append(f"{width}: after '{q}' the newest answer starts at {round(top)} px, not in view")
                    for tbl in turn().locator("table").all():
                        if not tbl.locator("thead th").count() or not tbl.locator("thead th").first.is_visible():
                            problems.append(f"{width}: a table without visible column headers after '{q}'")

                ask("have I got any parking fines?")
                t = turn().inner_text()
                if turn().locator('[data-od-component="ApprovalPrompt"]').count():
                    problems.append(f"{width}: a question about fines went straight to a payment approval")
                if not turn().locator('[data-od-component]').count():
                    problems.append(f"{width}: no part for the fines")
                if "19 Nov" not in t:
                    problems.append(f"{width}: the fines answer doesn't say when the discount ends (19 November)")
                page.screenshot(path=str(out / f"live-{width}-1-fines.png"))
                pay = turn().locator('[data-od-component] [data-od-event="pay_fine"]')
                if pay.count():  # the card's own "Pay" button asks for the change; it never pays
                    timed(lambda: pay.first.click())
                else:
                    ask("Pay the unpaid one")
                prompt = turn().locator('[data-od-component="ApprovalPrompt"]')
                if not prompt.count():
                    problems.append(f"{width}: no approval prompt before paying")
                elif "no longer challenge" not in prompt.first.inner_text().lower():
                    problems.append(f"{width}: the approval prompt doesn't say that paying ends the right to challenge")
                page.screenshot(path=str(out / f"live-{width}-2-approve.png"))
                approve = turn().locator('[data-od-component="ApprovalPrompt"] [data-od-effect="change"]')
                if approve.count():
                    timed(lambda: approve.first.click())
                    t = turn().inner_text().lower()
                    if not ("paid" in t or "pay-771905" in t or turn().locator('[data-od-component="Receipt"]').count()):
                        problems.append(f"{width}: no confirmation after paying")
                    if "successful" in t:
                        problems.append(f"{width}: the receipt says 'successful'")
                    page.screenshot(path=str(out / f"live-{width}-3-paid.png"))
                ask("Where is my application?")
                steps = turn().locator('[data-od-component="ProgressStatus"]')
                if not steps.count():
                    problems.append(f"{width}: no steps for the application")
                elif "waiting for your document" not in steps.first.inner_text().lower():
                    problems.append(f"{width}: the steps don't show the wait for the document the text talks about")
                page.screenshot(path=str(out / f"live-{width}-4-status.png"))
                ask("What documents do I still need to send?")
                t = turn().inner_text()
                if re.search(r"\b\d{4}-\d{2}-\d{2}\b", t):
                    problems.append(f"{width}: a raw date in the documents answer")
                for box in turn().locator(".odl-scroll").all():
                    if box.evaluate("b => b.scrollWidth > b.clientWidth + 1") and width < 600:
                        problems.append(f"{width}: the documents table scrolls sideways on a phone")
                page.screenshot(path=str(out / f"live-{width}-5-documents.png"))
                ask("Which zone am I in?")
                if turn().locator("[data-od-component]").count():
                    problems.append(f"{width}: a part for a short fact (R1)")
                page.screenshot(path=str(out / f"live-{width}-6-fact.png"))
                if errors:
                    problems.append(f"{width}: console errors {errors[:3]}")
                page.close()
            b.close()
    finally:
        srv.terminate()
    q = lambda xs, p: round(sorted(xs)[min(len(xs) - 1, int(round(p * (len(xs) - 1))))]) if xs else None
    print(f"in the page, {len(full)} turns: first thing on screen p50 {q(first, .5)} ms, p95 {q(first, .95)} ms; "
          f"checked answer p50 {q(full, .5)} ms, p95 {q(full, .95)} ms")
    print("\n".join(problems) or f"live loop ok with {a.provider} {a.model or ''} at 1440 and 375 px; screenshots in {out}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
