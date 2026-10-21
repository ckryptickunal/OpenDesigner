#!/usr/bin/env python3
"""Check every library component's own layout, unscaled, at all 13 widths of site/check_layout.py.

The shop shows components zoomed down to cards, which the layout checker cannot measure, so this makes one plain test page per
component (in three looks: Billerwick dense, Pebbleday regular, Fernhollow large), serves them on a loopback port and runs
site/check_layout.py on them.

  python3 site/library_layout.py [slug ...] [--widths 320,390,768]

Needs Playwright and Chrome, like check_layout.py. Writes nothing to the repo (a temporary folder is served and removed).
"""
import functools
import http.server
import pathlib
import re
import socketserver
import subprocess
import sys
import tempfile
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "skills/opendesigner/assets/library/components"
LOOKS = ["billerwick", "pebbleday", "fernhollow"]


REFS = r'(id|for|aria-controls|aria-labelledby|aria-describedby|aria-activedescendant|name)="([^"]+)"'


def suffix(markup, k):
    return re.sub(REFS, lambda m: f'{m.group(1)}="{m.group(2)}-{k}"', markup)


def page(slug, src, css):
    markup = re.sub(r"<style>.*?</style>|<script>.*?</script>", "", src, flags=re.S)
    style = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    script = "".join(re.findall(r"<script>(.*?)</script>", src, re.S))
    # Each look's copy keeps ids unique and radio groups apart, as a page with one copy would have them.
    copies = "".join(f'<section class="look odl-sys-{k}">{suffix(markup, k)}</section>' for k in LOOKS)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{slug}</title><style>{css}\n{style}\nbody{{margin:0;background:#f4f5f7}} .look{{box-sizing:border-box;padding:16px;'
            f'background:var(--ds-color-surface-base);color:var(--ds-color-text-primary);font:var(--ds-text-body-md);display:grid}}'
            f'.look>*{{margin-inline:auto}}</style></head><body><main>{copies}</main><script>{script}</script></body></html>')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    extra = [a for a in sys.argv[1:] if a.startswith("--")]
    css = (ROOT / "site/static/library-systems.css").read_text()
    slugs = args or sorted(p.name for p in LIB.iterdir() if (p / "meta.json").exists())
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        for s in slugs:
            (root / s).mkdir()
            (root / s / "index.html").write_text(page(s, (LIB / s / "component.html").read_text(), css))
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=d)
        handler.log_message = lambda *a: None
        with socketserver.TCPServer(("127.0.0.1", 0), handler) as srv:
            port = srv.server_address[1]
            threading.Thread(target=srv.serve_forever, daemon=True).start()
            r = subprocess.run([sys.executable, str(ROOT / "site/check_layout.py"), "--base", f"http://127.0.0.1:{port}",
                                "--pages", ",".join(f"/{s}/" for s in slugs), *extra])
            srv.shutdown()
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
