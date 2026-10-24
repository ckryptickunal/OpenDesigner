#!/usr/bin/env python3
"""Build the site and publish it to Vercel (project "opendesigner", static files, no build step on Vercel).

  python3 site/deploy.py              build, upload to production without the domain, check key paths, then promote
  python3 site/deploy.py --preview    build, deploy a preview URL and check key paths

Only this script uploads the site. Pushing to main deploys through site/autodeploy.py on the maintainer's Mac, which
runs this script in .worktrees/deploy (a clean worktree of origin/main); run it by hand only when the auto-deployer
is uninstalled. Vercel's own Git builds stay off (Ignored Build Step `exit 0`): they have no Python build and served
404 on every path on 2026-10-22.

IndexNow hears only about pages whose content changed since the last accepted ping (site/.cache/indexnow.json).

Needs the Vercel CLI, signed in (`vercel whoami`). The link to the Vercel project lives in site/.vercel/ and is
copied into the build folder before each upload. Set SITE_URL in site/site-url.txt (the production address), so
canonical links, the sitemap, robots.txt and llms.txt point at the right domain.
"""
import json
import os
import re
import pathlib
import shutil
import subprocess
import sys

SITE = pathlib.Path(__file__).resolve().parent
DIST = SITE / "dist"
PROJECT = "opendesigner"


def main():
    url_file = SITE / "site-url.txt"
    env = dict(os.environ)
    if url_file.exists():
        env["SITE_URL"] = url_file.read_text().strip()
    subprocess.run([sys.executable, str(SITE / "build.py")], check=True, env=env)
    if not (SITE / ".vercel" / "project.json").exists():
        subprocess.run(["vercel", "link", "--yes", "--project", PROJECT], cwd=SITE, check=True)
    shutil.copytree(SITE / ".vercel", DIST / ".vercel", dirs_exist_ok=True)
    if not (DIST / "index.html").exists() or not (DIST / "og" / "home.jpg").exists():
        sys.exit("dist/ has no index.html or og/home.jpg: not deploying a broken build")
    preview = "--preview" in sys.argv
    # Production is uploaded without taking the domain (--skip-domain), checked, and only then promoted.
    args = ["vercel", "deploy", str(DIST), "--yes"] + ([] if preview else ["--prod", "--skip-domain"])
    for attempt in (1, 2):  # the CLI sometimes exits 1 once; a second run works
        r = subprocess.run(args, cwd=SITE, text=True, capture_output=True)
        if r.returncode == 0:
            break
    else:
        sys.exit(r.stderr.strip()[-800:])
    out = r.stdout
    try:  # newer CLIs answer in JSON
        url = json.loads(out[out.index("{"):])["deployment"]["url"]
    except (ValueError, KeyError):
        url = out.strip().splitlines()[-1].strip()
    url = url if url.startswith("http") else f"https://{url}"
    print(f"uploaded: {url} ({'preview' if preview else 'production, not live yet'})")
    bad = [p for p in CHECK_PATHS if status(p, url) != "200"]
    if bad:
        sys.exit(f"not promoting: {', '.join(bad)} did not answer 200 on {url}")
    nf = subprocess.run(["vercel", "curl", "/no-such-page-od-check/", "--deployment", url, "--", "-s", "-w", "\\n%{http_code}"],
                        cwd=SITE, text=True, capture_output=True).stdout
    if not nf.endswith("404") or "noindex" not in nf:
        sys.exit("not promoting: a missing page did not answer 404 with the noindex 404 page")
    if '"/ingest/' in (DIST / "vercel.json").read_text():  # analytics on: events must reach PostHog, not our 404
        ev = subprocess.run(["vercel", "curl", "/ingest/i/v0/e/", "--deployment", url, "--", "-s", "-o", "/dev/null", "-X", "POST",
                             "-H", "Content-Type: application/json", "-d", "{}", "-w", "%{http_code}"], cwd=SITE, text=True, capture_output=True).stdout
        if ev.strip()[-3:] in ("404", ""):
            sys.exit(f"not promoting: POST /ingest/i/v0/e/ gave {ev!r}, so analytics events would not reach PostHog")
    md = subprocess.run(["vercel", "curl", "/docs/install/", "--deployment", url, "--", "-s", "-o", "/dev/null", "-H", "Accept: text/markdown",
                         "-w", "%{content_type}"], cwd=SITE, text=True, capture_output=True).stdout
    if "text/markdown" not in md:
        sys.exit(f"not promoting: Accept: text/markdown on /docs/install/ gave {md!r}, not Markdown")
    if preview:
        return
    subprocess.run(["vercel", "promote", url, "--yes"], cwd=SITE, check=True)
    site_url = env.get("SITE_URL", "")
    import time
    for wait in (5, 10, 20):  # the domain can answer from the old deployment for a few seconds
        time.sleep(wait)
        bad = [p for p in CHECK_PATHS if live_status(site_url + p) != 200]
        if not bad:
            break
    print("live: every key path answers 200" if not bad else f"WARNING live paths not 200: {bad}")
    indexnow(site_url)


CHECK_PATHS = ["/", "/docs/", "/docs/install/", "/library/", "/sitemap.xml", "/robots.txt", "/llms.txt", "/og/home.jpg", "/_vercel/speed-insights/script.js", "/.well-known/agent-skills/index.json", "/404.webp"]


def status(path, deployment):
    """HTTP status of a path on one deployment (vercel curl passes deployment protection)."""
    r = subprocess.run(["vercel", "curl", path, "--deployment", deployment, "--", "-s", "-o", "/dev/null", "-w", "%{http_code}"],
                       cwd=SITE, text=True, capture_output=True)
    return r.stdout.strip()[-3:]


def live_status(url):
    import urllib.request
    try:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=15) as r:
            return r.status
    except Exception as e:
        return getattr(e, "code", str(e))


def page_hashes(urls, site_url):
    """A hash per page of what the page says. The GitHub star count is left out: it changes every page at once."""
    import hashlib
    out = {}
    for u in urls:
        rel = u[len(site_url):].lstrip("/")
        f = DIST / rel / "index.html" if not rel or rel.endswith("/") else DIST / rel
        if f.exists():
            text = re.sub(r"data-stars>[^<]*<", "data-stars><", f.read_text(errors="ignore"))
            out[u] = hashlib.sha256(text.encode()).hexdigest()[:16]
    return out


def indexnow(site_url):
    """Tell IndexNow engines (Bing, Yandex, Seznam, Naver...) which pages changed. Google uses the sitemap instead."""
    import urllib.request
    key_file = SITE / "indexnow-key.txt"
    if not (site_url and key_file.exists()):
        return
    key = key_file.read_text().strip()
    urls = re.findall(r"<loc>([^<]+)</loc>", (DIST / "sitemap.xml").read_text())
    sent_file = SITE / ".cache" / "indexnow.json"
    try:
        sent = json.loads(sent_file.read_text())
    except (OSError, ValueError):
        sent = {}
    now = page_hashes(urls, site_url)
    changed = [u for u in urls if now.get(u) != sent.get(u)]
    if not changed:
        print("IndexNow: no page changed, nothing sent")
        return
    body = json.dumps({"host": site_url.split("//", 1)[1], "key": key, "keyLocation": f"{site_url}/{key}.txt", "urlList": changed}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"IndexNow: {r.status} for {len(changed)} changed of {len(urls)} URLs")
            sent_file.parent.mkdir(exist_ok=True)
            sent_file.write_text(json.dumps(now, indent=0, sort_keys=True))
    except Exception as e:
        print("IndexNow not accepted:", e)


if __name__ == "__main__":
    main()
