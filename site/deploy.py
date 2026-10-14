#!/usr/bin/env python3
"""Build the site and publish it to Vercel (project "opendesigner", static files, no build step on Vercel).

  python3 site/deploy.py              build and deploy to production
  python3 site/deploy.py --preview    build and deploy a preview URL only

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
    args = ["vercel", "deploy", str(DIST), "--yes"] + ([] if "--preview" in sys.argv else ["--prod"])
    out = subprocess.run(args, cwd=SITE, check=True, text=True, capture_output=True).stdout
    try:  # newer CLIs answer in JSON
        dep = json.loads(out[out.index("{"):])["deployment"]
        print(f"{dep['readyState']}: {dep['url']} ({dep['target'] or 'preview'})")
    except (ValueError, KeyError):
        print(out.strip().splitlines()[-1])
    if "--preview" not in sys.argv:
        indexnow(env.get("SITE_URL", ""))


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
