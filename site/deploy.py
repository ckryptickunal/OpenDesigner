#!/usr/bin/env python3
"""Build the site and publish it to Vercel (project "opendesigner", static files, no build step on Vercel).

  python3 site/deploy.py              build, upload to production without the domain, check key paths, then promote
  python3 site/deploy.py --preview    build, deploy a preview URL and check key paths

Only this script deploys the site. The Vercel project is linked to GitHub, but its Ignored Build Step is `exit 0`,
so pushes never deploy (a Git build has no Python build and served 404 on every path on 2026-10-22).
Run it from a clean worktree of origin/main, so other sessions' uncommitted edits stay out.

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


CHECK_PATHS = ["/", "/docs/", "/docs/install/", "/library/", "/sitemap.xml", "/robots.txt", "/llms.txt", "/og/home.jpg", "/_vercel/speed-insights/script.js", "/.well-known/agent-skills/index.json"]


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


def indexnow(site_url):
    """Tell IndexNow engines (Bing, Yandex, Seznam, Naver...) which pages changed. Google uses the sitemap instead."""
    import urllib.request
    key_file = SITE / "indexnow-key.txt"
    if not (site_url and key_file.exists()):
        return
    key = key_file.read_text().strip()
    urls = re.findall(r"<loc>([^<]+)</loc>", (DIST / "sitemap.xml").read_text())
    body = json.dumps({"host": site_url.split("//", 1)[1], "key": key, "keyLocation": f"{site_url}/{key}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"IndexNow: {r.status} for {len(urls)} URLs")
    except Exception as e:
        print("IndexNow not accepted:", e)


if __name__ == "__main__":
    main()
