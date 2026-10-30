#!/usr/bin/env python3
"""Draw the README's GitHub star chart from GitHub's own star list, and keep it current.

  python3 tools/star_chart.py                 redraw brand/kit/readme/stars-light.svg and stars-dark.svg here
  python3 tools/star_chart.py --push          in a clean worktree of origin/main: redraw, and commit and push only if the
                                              star count changed (what the scheduled job runs)
  python3 tools/star_chart.py --install       run --push every 3 hours on this Mac (launchd), and once now
  python3 tools/star_chart.py --uninstall     stop that
  python3 tools/star_chart.py --status        the job, the last run, the chart's count and GitHub's

Why not a hosted chart: star-history.com and GitHub's image proxy both cache for 24 hours, and GitHub Actions does not run
on this account. A file in the repo shows on GitHub within about 5 minutes of a push. Needs the GitHub CLI, signed in.
"""
import datetime as dt
import json
import os
import pathlib
import plistlib
import re
import shutil
import subprocess
import sys

REPO = "ckryptickunal/OpenDesigner"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ("brand", "kit", "readme")
LABEL = "dev.opendesigner.stars"
HOME = pathlib.Path.home()
APP = HOME / "Library" / "Application Support" / "OpenDesigner" / "stars"
PLIST = HOME / "Library" / "LaunchAgents" / f"{LABEL}.plist"
LOG = HOME / "Library" / "Logs" / "opendesigner-stars.log"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {  # OpenDesigner cobalt on cool neutrals (brand/design-system/project/tokens.json)
    "light": {"line": "#2338ff", "text": "#141517", "muted": "#5b6170", "grid": "#e6e9ee"},
    "dark": {"line": "#537eff", "text": "#e6e9ee", "muted": "#9aa1ad", "grid": "#2a2f37"},
}


def gh(path, accept=None, paginate=False):
    cmd = ["gh", "api"] + (["-H", f"Accept: {accept}"] if accept else []) + (["--paginate", "--slurp"] if paginate else []) + [path]
    out = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=True).stdout)
    return [x for page in out for x in page] if paginate else out


def series():
    """Total stars at the end of every day since the repo opened."""
    created = dt.date.fromisoformat(gh(f"repos/{REPO}")["created_at"][:10])
    per_day = {}
    for s in gh(f"repos/{REPO}/stargazers?per_page=100", "application/vnd.github.star+json", paginate=True):
        per_day[s["starred_at"][:10]] = per_day.get(s["starred_at"][:10], 0) + 1
    rows, total, day, today = [], 0, created, dt.datetime.now(dt.timezone.utc).date()
    while day <= today:
        total += per_day.get(day.isoformat(), 0)
        rows.append((day, total))
        day += dt.timedelta(days=1)
    return rows


def nice_max(v):
    for step in (5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, 5000, 10000):
        if v <= step * 4:
            return step * 4, step
    return v, v // 4


def svg(rows, theme):
    c = THEMES[theme]
    W, H, L, R, T, B = 800, 300, 44, 64, 78, 34
    total, first, last = rows[-1][1], rows[0][0], rows[-1][0]
    top, step = nice_max(max(total, 1))
    span = max(1, (last - first).days)
    x = lambda d: L + (W - L - R) * (d - first).days / span
    y = lambda v: H - B - (H - T - B) * v / top
    pts = " ".join(f"{x(d):.1f},{y(v):.1f}" for d, v in rows)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
           f'<title>OpenDesigner GitHub stars: {total}</title>',
           '<defs><linearGradient id="a" x1="0" x2="0" y1="0" y2="1">'
           + "".join(f'<stop offset="{o}" stop-color="{c["line"]}" stop-opacity="{a}"/>' for o, a in ((0, .26), (.25, .16), (.5, .08), (.75, .03), (1, 0)))
           + '</linearGradient></defs>',
           f'<text x="{L}" y="30" font-size="14" fill="{c["muted"]}">GitHub stars · updated {last.strftime("%b %-d, %Y")}</text>',
           f'<text x="{L}" y="62" font-size="30" font-weight="300" fill="{c["text"]}">{total:,}</text>']
    for v in range(0, top + 1, step):
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{c["grid"]}" stroke-width="1"/>')
        out.append(f'<text x="{L - 8}" y="{y(v) + 4:.1f}" font-size="11" fill="{c["muted"]}" text-anchor="end">{v:,}</text>')
    gap = 7 if span <= 70 else 30 if span <= 400 else 90
    d, seen = first, set()
    while d <= last:
        label = d.strftime("%b %-d") if gap < 30 else d.strftime("%b %Y")
        if label not in seen and x(d) <= W - R - 20:
            seen.add(label)
            out.append(f'<text x="{x(d):.1f}" y="{H - 12}" font-size="11" fill="{c["muted"]}" text-anchor="middle">{label}</text>')
        d += dt.timedelta(days=gap)
    out.append(f'<polygon points="{L},{y(0):.1f} {pts} {x(last):.1f},{y(0):.1f}" fill="url(#a)"/>')
    out.append(f'<polyline points="{pts}" fill="none" stroke="{c["line"]}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>')
    out.append(f'<circle cx="{x(last):.1f}" cy="{y(total):.1f}" r="4" fill="{c["line"]}"/>')
    out.append(f'<text x="{x(last) + 10:.1f}" y="{y(total) + 4:.1f}" font-size="13" fill="{c["text"]}">{total:,}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def draw(root):
    rows = series()
    folder = root.joinpath(*OUT)
    for theme in THEMES:
        (folder / f"stars-{theme}.svg").write_text(svg(rows, theme))
    return rows[-1][1]


def chart_count(root):
    m = re.search(r"GitHub stars: (\d+)", (root.joinpath(*OUT) / "stars-light.svg").read_text())
    return int(m.group(1)) if m else None


def log(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    line = f"{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    with LOG.open("a") as f:
        f.write(line + "\n")
    print(line)


def git(repo, *args, check=True):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=check)


def push(repo):
    wt = APP / "worktree"
    git(repo, "fetch", "-q", "origin")
    if wt.exists():
        git(repo, "worktree", "remove", "--force", str(wt), check=False)
        shutil.rmtree(wt, ignore_errors=True)
    git(repo, "worktree", "add", "-q", "--detach", str(wt), "origin/main")
    try:
        before = chart_count(wt)
        total = draw(wt)
        if before == total:
            log(f"no change: {total} stars")
            return
        git(wt, "add", *[str(pathlib.Path(*OUT) / f"stars-{t}.svg") for t in THEMES])
        git(wt, "commit", "-q", "-m", f"README: star chart, {total} stars\n\nRedrawn by tools/star_chart.py --push (every 3 hours on the maintainer's Mac).")
        for _ in range(3):
            if git(wt, "push", "-q", "origin", "HEAD:main", check=False).returncode == 0:
                log(f"pushed: {before} -> {total} stars")
                return
            git(wt, "fetch", "-q", "origin")
            git(wt, "rebase", "-q", "origin/main")
        log("push failed three times; will try again next run")
        sys.exit(1)
    finally:
        git(repo, "worktree", "remove", "--force", str(wt), check=False)


def install():
    APP.mkdir(parents=True, exist_ok=True)
    script = APP / "star_chart.py"
    shutil.copy2(__file__, script)
    common = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--path-format=absolute", "--git-common-dir"],
                            capture_output=True, text=True, check=True).stdout.strip()
    (APP / "repo.txt").write_text(str(pathlib.Path(common).parent))  # the main checkout, even when run from a worktree
    PLIST.parent.mkdir(parents=True, exist_ok=True)
    plistlib.dump({"Label": LABEL, "ProgramArguments": [sys.executable, str(script), "--push"], "StartInterval": 3 * 3600,
                   "RunAtLoad": True, "StandardOutPath": str(LOG), "StandardErrorPath": str(LOG),
                   "EnvironmentVariables": {"PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"}}, PLIST.open("wb"))
    subprocess.run(["launchctl", "unload", str(PLIST)], capture_output=True)
    subprocess.run(["launchctl", "load", str(PLIST)], check=True)
    print(f"installed: {LABEL} every 3 hours; log {LOG}")


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--install":
        install()
    elif arg == "--uninstall":
        subprocess.run(["launchctl", "unload", str(PLIST)], capture_output=True)
        PLIST.unlink(missing_ok=True)
        print("uninstalled")
    elif arg == "--push":
        repo = pathlib.Path((APP / "repo.txt").read_text().strip()) if (APP / "repo.txt").exists() else ROOT
        push(repo)
    elif arg == "--status":
        loaded = subprocess.run(["launchctl", "list", LABEL], capture_output=True).returncode == 0
        print(f"job        {'running every 3 hours' if loaded else 'not installed'}")
        print(f"last run   {LOG.read_text().strip().splitlines()[-1] if LOG.exists() else 'none'}")
        print(f"chart      {chart_count(ROOT)} stars (this checkout)")
        print(f"GitHub     {gh(f'repos/{REPO}')['stargazers_count']} stars")
    elif arg == "":
        print(f"drew {draw(ROOT)} stars into {pathlib.Path(*OUT)}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
