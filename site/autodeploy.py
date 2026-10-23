#!/usr/bin/env python3
"""Deploy opendesigner.dev by itself whenever origin/main changes. launchd runs it every 2 minutes on the maintainer's Mac.

    python3 site/autodeploy.py              one check: fetch, and deploy origin/main if it moved and has been still for 5 minutes
    python3 site/autodeploy.py --now        deploy origin/main now, even if it was just pushed or its last try failed
    python3 site/autodeploy.py --status     the commit on GitHub, the one deployed, and the last result
    python3 site/autodeploy.py --install    start the launchd job (every 2 minutes, and once at login)
    python3 site/autodeploy.py --uninstall  stop it

Why a Mac and not the cloud (owner, 2026-10-23: deploy on every push):
- GitHub Actions is disabled for the owner's account. GitHub answers "Actions has been disabled for this user", so no
  workflow runs, including ci.yml.
- Vercel's own Git build can't make the site. The build needs Python with Playwright, the full git history (the
  changelog) and files git doesn't hold: showcase screenshots and the font and card caches. A Git build once served 404 on
  every path (2026-10-22), so the project's Ignored Build Step stays `exit 0`.

So the Mac deploys, with the same steps as a deploy by hand (site/README.md, "Before every deploy"):
1. Move the clean worktree .worktrees/deploy to the exact commit. It keeps the git-ignored files between deploys.
2. Run site/build.py and site/check.py.
3. Run site/deploy.py: upload without the domain, check the key paths, promote, ping IndexNow.

Safety:
- One deploy at a time (a lock).
- Never deploy over uncommitted changes in the deploy worktree.
- Wait until pushes have stopped for 5 minutes, so a burst of pushes is one deploy.
- A commit that failed is not tried again until something new is pushed (or --now).
- A failure shows a macOS notification and is logged in ~/Library/Logs/opendesigner-autodeploy.log.

It runs from .worktrees/deploy, so the script itself is always committed code. Standard library only.
"""
import json
import os
import pathlib
import plistlib
import shutil
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=HERE,
                                   capture_output=True, text=True, check=True).stdout.strip()).parent
WT = REPO / ".worktrees" / "deploy"
STATE_DIR = pathlib.Path.home() / "Library" / "Application Support" / "OpenDesigner" / "autodeploy"
STATE = STATE_DIR / "state.json"
LOCK = STATE_DIR / "lock"
LOG = pathlib.Path.home() / "Library" / "Logs" / "opendesigner-autodeploy.log"
LABEL = "dev.opendesigner.autodeploy"
PLIST = pathlib.Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
SETTLE = 300  # seconds origin/main must stay still before it deploys
STALE_LOCK = 2 * 3600  # longer than the steps' time limits together


def log(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if LOG.exists() and LOG.stat().st_size > 5_000_000:
        LOG.replace(LOG.with_suffix(".old.log"))
    with LOG.open("a") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")
    print(msg)


def notify(msg):
    text = msg.replace('"', "'")[:200]
    subprocess.run(["osascript", "-e", f'display notification "{text}" with title "opendesigner.dev deploy"'], capture_output=True)


def git(*args, cwd=WT):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def load():
    try:
        return json.loads(STATE.read_text())
    except (OSError, ValueError):
        return {}


def save(st):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=1) + "\n")


def run(cmd, label, minutes=30):
    """Run one step in the deploy worktree, logging its output tail; True if it passed. A step that hangs is stopped."""
    try:
        r = subprocess.run(cmd, cwd=WT, capture_output=True, text=True, timeout=minutes * 60)
    except subprocess.TimeoutExpired:
        log(f"{label}: stopped after {minutes} minutes")
        return False
    tail = (r.stdout + r.stderr).strip().splitlines()[-15:]
    log(f"{label}: exit {r.returncode}\n    " + "\n    ".join(tail))
    return r.returncode == 0


def deploy(target, st):
    if git("status", "--porcelain", "--untracked-files=no").stdout.strip():
        msg = f"not deploying {target[:7]}: .worktrees/deploy has uncommitted changes"
        log(msg)
        notify(msg)
        return False
    if git("checkout", "-q", "--detach", target).returncode:
        log(f"could not check out {target[:7]} in .worktrees/deploy")
        return False
    py = sys.executable
    ok = (run([py, "site/build.py"], "build") and run([py, "site/check.py"], "site/check.py", 10)
          and run([py, "site/deploy.py"], "deploy", 40))
    st.update(last_try=target, last_result="deployed" if ok else "failed", last_time=time.strftime("%Y-%m-%d %H:%M:%S"))
    if ok:
        st["deployed"] = target
        log(f"LIVE {target[:7]} on opendesigner.dev")
    else:
        notify(f"Deploy of {target[:7]} failed. Log: ~/Library/Logs/opendesigner-autodeploy.log")
    save(st)
    return ok


def check(now=False):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        LOCK.mkdir()
    except FileExistsError:
        if time.time() - LOCK.stat().st_mtime < STALE_LOCK:
            return  # a deploy is already running
        LOCK.rmdir()
        LOCK.mkdir()
    try:
        if git("fetch", "-q", "origin", "main").returncode:
            return  # offline: try again next time
        target = git("rev-parse", "origin/main").stdout.strip()
        st = load()
        if target == st.get("deployed"):
            return
        if not now:
            if target == st.get("last_try") and st.get("last_result") == "failed":
                return  # waits for a new push, or --now
            if st.get("seen") != target:
                st.update(seen=target, seen_at=time.time())
                save(st)
                log(f"new commit {target[:7]} on origin/main; deploying once pushes stop for {SETTLE // 60} minutes")
                return
            if time.time() - st.get("seen_at", 0) < SETTLE:
                return
        log(f"deploying {target[:7]}")
        deploy(target, st)
    finally:
        LOCK.rmdir()


def status():
    st = load()
    git("fetch", "-q", "origin", "main")
    head = git("rev-parse", "--short", "origin/main").stdout.strip()
    print(f"origin/main   {head}")
    print(f"deployed      {(st.get('deployed') or '?')[:7]}")
    print(f"last try      {(st.get('last_try') or '-')[:7]} {st.get('last_result', '')} {st.get('last_time', '')}")
    loaded = subprocess.run(["launchctl", "list", LABEL], capture_output=True).returncode == 0
    print(f"launchd job   {'running every 2 minutes' if loaded else 'not installed (python3 site/autodeploy.py --install)'}")
    print(f"log           {LOG}")


def install():
    script = WT / "site" / "autodeploy.py"
    if not script.exists():
        sys.exit(f"{script} is missing: move .worktrees/deploy to a commit that has site/autodeploy.py first")
    path = os.pathsep.join(dict.fromkeys([str(pathlib.Path(sys.executable).parent), "/opt/homebrew/bin", "/usr/local/bin",
                                          "/usr/bin", "/bin", "/usr/sbin", "/sbin"]))
    PLIST.parent.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with PLIST.open("wb") as f:
        plistlib.dump({"Label": LABEL, "ProgramArguments": [sys.executable, str(script)], "StartInterval": 120,
                       "RunAtLoad": True, "WorkingDirectory": str(WT), "EnvironmentVariables": {"PATH": path},
                       "StandardOutPath": "/dev/null", "StandardErrorPath": str(LOG), "ProcessType": "Background"}, f)
    uid = str(os.getuid())
    subprocess.run(["launchctl", "bootout", f"gui/{uid}/{LABEL}"], capture_output=True)
    r = subprocess.run(["launchctl", "bootstrap", f"gui/{uid}", str(PLIST)], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"launchctl bootstrap failed: {r.stderr.strip()}")
    print(f"installed {PLIST}: checks origin/main every 2 minutes and deploys new commits")


def uninstall():
    subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}/{LABEL}"], capture_output=True)
    if PLIST.exists():
        PLIST.unlink()
    print("uninstalled: pushes no longer deploy by themselves")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--install":
        install()
    elif arg == "--uninstall":
        uninstall()
    elif arg == "--status":
        status()
    elif arg in ("", "--now"):
        if not shutil.which("vercel"):
            log("the Vercel CLI is not on PATH; not deploying")
            sys.exit(1)
        check(now=arg == "--now")
    else:
        sys.exit(__doc__)
