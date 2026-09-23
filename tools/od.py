#!/usr/bin/env python3
"""OpenDesigner coordination: lets parallel sessions (Claude, Codex, ChatGPT, humans) work in one repo.

Everything lives in files under _coordination/, so any agent that can read and write the repo can take part.
Git is the transport between machines; a lock directory prevents races between sessions on one machine.

  python3 tools/od.py status                          board, active sessions, unread messages
  python3 tools/od.py add U6 "scope" "output file" --by "Session name"   add a lane (fails if the id exists)
  python3 tools/od.py claim L19 --by "Session name"   claim an open lane (fails if someone else holds it)
  python3 tools/od.py done L19 --by "Session name" --summary "12 cards"
  python3 tools/od.py heartbeat --by "Session name" "what I am doing now"
  python3 tools/od.py note --by "Session name" "L19 -> L07: finding other lanes need"
  python3 tools/od.py send "To session" --by "From session" "message"
  python3 tools/od.py inbox "Session name" [--ack]    read (and archive) messages addressed to you
  python3 tools/od.py log --by "Session name" "decision and why"   append to the decision log
  python3 tools/od.py sync --by "Session name" -m "L19: what changed"   pull, commit, push

Set OD_SESSION to skip --by.
"""
import argparse, os, re, subprocess, sys, time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CO = ROOT / "_coordination"
BOARD, NOTES_MARK = CO / "BOARD.md", "## Cross-lane notes"
ACTIVE_MINUTES = 45


def now():
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "anonymous"


@contextmanager
def lock():
    """mkdir is atomic, so only one local session edits shared files at a time."""
    path = CO / ".lock"
    for _ in range(100):
        try:
            path.mkdir()
            break
        except FileExistsError:
            if time.time() - path.stat().st_mtime > 60:  # stale lock from a crashed session
                path.rmdir()
            time.sleep(0.2)
    else:
        sys.exit("Could not get the coordination lock; try again.")
    try:
        yield
    finally:
        path.rmdir()


def git(*args, check=True):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=check)


def lane_rows(text):
    return [(m.start(), m.end(), m) for m in re.finditer(r"^\| ([A-Z]\d+\w*) \| (.+?) \| (.+?) \| (.+?) \|$", text, re.M)]


def duplicates(text):
    ids = [m[1] for _, _, m in lane_rows(text)]
    return sorted({i for i in ids if ids.count(i) > 1})


def set_status(lane, new, expect_open, by):
    with lock():
        text = BOARD.read_text()
        if lane in duplicates(text):
            sys.exit(f"{lane} appears more than once on the board. Merge its rows into one, then try again.")
        for start, end, m in lane_rows(text):
            if m[1] != lane:
                continue
            status = m[4]
            if expect_open and not (status.startswith("open") or by in status):
                sys.exit(f"{lane} is not open: {status}")
            row = f"| {m[1]} | {m[2]} | {m[3]} | {new} |"
            BOARD.write_text(text[:start] + row + text[end:])
            return
        sys.exit(f"No lane {lane} on the board. Add it first: od.py add {lane} \"scope\" \"output\"")


def heartbeat_line(by, text):
    path = CO / "sessions" / f"{slug(by)}.md"
    path.parent.mkdir(exist_ok=True)
    if not path.exists():
        path.write_text(f"# Session: {by}\n\nAppend-only heartbeat. Newest last.\n\n")
    with path.open("a") as f:
        f.write(f"- {now()}: {text}\n")


def cmd_status(_):
    text = BOARD.read_text()
    print("Lanes")
    for _, _, m in lane_rows(text):
        print(f"  {m[1]:4} {m[4][:90]}")
    for lane in duplicates(text):
        print(f"  ! {lane} appears more than once; merge its rows before claiming it")
    print("\nSessions (heartbeat in the last %d minutes marked *)" % ACTIVE_MINUTES)
    for p in sorted((CO / "sessions").glob("*.md")):
        last = [l for l in p.read_text().splitlines() if l.startswith("- ")][-1:] or ["(no heartbeat)"]
        age = (time.time() - p.stat().st_mtime) / 60
        print(f"  {'*' if age < ACTIVE_MINUTES else ' '} {p.stem}: {last[0][2:][:100]}")
    inbox = CO / "inbox"
    unread = {d.name: len(list(d.glob("*.md"))) for d in inbox.iterdir() if d.is_dir()} if inbox.exists() else {}
    print("\nUnread messages: " + (", ".join(f"{k} {v}" for k, v in unread.items() if v) or "none"))


def cmd_add(a):
    """Create a lane row under the lock, so two sessions cannot create the same lane at once."""
    with lock():
        text = BOARD.read_text()
        if a.lane in {m[1] for _, _, m in lane_rows(text)}:
            sys.exit(f"{a.lane} is already on the board. Pick another id, or claim the existing lane.")
        rows = lane_rows(text)
        at = rows[-1][1] if rows else text.index(NOTES_MARK)
        BOARD.write_text(text[:at] + f"\n| {a.lane} | {a.scope} | {a.output} | {a.status} |" + text[at:])
    heartbeat_line(a.by, f"added lane {a.lane}")
    print(f"{a.lane} added ({a.status})")


def cmd_claim(a):
    set_status(a.lane, f"claimed by {a.by} ({now()})", True, a.by)
    heartbeat_line(a.by, f"claimed {a.lane}")
    print(f"{a.lane} claimed by {a.by}")


def cmd_done(a):
    set_status(a.lane, f"done ({a.summary})" if a.summary else "done", False, a.by)
    heartbeat_line(a.by, f"finished {a.lane}: {a.summary or ''}")
    print(f"{a.lane} marked done")


def cmd_heartbeat(a):
    heartbeat_line(a.by, a.text)


def cmd_note(a):
    with lock():
        with BOARD.open("a") as f:
            f.write(f"- [{a.by}, {now()}] {a.text}\n")


def cmd_send(a):
    box = CO / "inbox" / slug(a.to)
    box.mkdir(parents=True, exist_ok=True)
    path = box / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{slug(a.by)}.md"
    path.write_text(f"From: {a.by}\nTo: {a.to}\nSent: {now()}\n\n{a.text}\n")
    print(f"Queued for {a.to}: {path.relative_to(ROOT)}")


def cmd_inbox(a):
    box = CO / "inbox" / slug(a.name)
    msgs = sorted(box.glob("*.md")) if box.exists() else []
    for p in msgs:
        print(f"--- {p.name}\n{p.read_text().strip()}\n")
        if a.ack:
            (box / "read").mkdir(exist_ok=True)
            p.rename(box / "read" / p.name)
    if not msgs:
        print("No unread messages.")


def cmd_log(a):
    with lock():
        with (CO / "DECISIONS.md").open("a") as f:
            f.write(f"- {now()} [{a.by}] {a.text}\n")


def cmd_sync(a):
    """Commit everything under the repo (secrets are git-ignored), rebase on the remote, push."""
    heartbeat_line(a.by, f"synced: {a.m.splitlines()[0]}")
    git("add", "-A")
    if git("diff", "--cached", "--quiet", check=False).returncode:
        git("commit", "-q", "-m", f"{a.m}\n\nSession: {a.by}")
    if git("remote", check=False).stdout.strip():
        pulled = git("pull", "--rebase", "--autostash", "-q", check=False)
        if pulled.returncode:
            sys.exit("Rebase hit a conflict. Resolve it (lane files are single-owner, so conflicts are usually in "
                     "BOARD.md: keep both sides' rows), then run `git rebase --continue` and sync again.\n" + pulled.stderr)
        pushed = git("push", "-q", check=False)
        print("Pushed." if pushed.returncode == 0 else "Push failed:\n" + pushed.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    by = dict(default=os.environ.get("OD_SESSION"), required=not os.environ.get("OD_SESSION"))

    sub.add_parser("status").set_defaults(fn=cmd_status)
    p = sub.add_parser("add"); p.add_argument("lane"); p.add_argument("scope"); p.add_argument("output")
    p.add_argument("--status", default="open"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_add)
    p = sub.add_parser("claim"); p.add_argument("lane"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_claim)
    p = sub.add_parser("done"); p.add_argument("lane"); p.add_argument("--by", **by); p.add_argument("--summary", default="")
    p.set_defaults(fn=cmd_done)
    p = sub.add_parser("heartbeat"); p.add_argument("text"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_heartbeat)
    p = sub.add_parser("note"); p.add_argument("text"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_note)
    p = sub.add_parser("send"); p.add_argument("to"); p.add_argument("text"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_send)
    p = sub.add_parser("inbox"); p.add_argument("name"); p.add_argument("--ack", action="store_true"); p.set_defaults(fn=cmd_inbox)
    p = sub.add_parser("log"); p.add_argument("text"); p.add_argument("--by", **by); p.set_defaults(fn=cmd_log)
    p = sub.add_parser("sync"); p.add_argument("-m", required=True); p.add_argument("--by", **by); p.set_defaults(fn=cmd_sync)
    a = ap.parse_args()
    a.fn(a)
