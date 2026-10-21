#!/usr/bin/env python3
"""Pull every message a person typed in a demo-trial session, so each correction can be logged in the trial ledger.

  python3 tools/trial_messages.py ~/od-trials/01-built-app            all sessions run in that folder
  python3 tools/trial_messages.py ~/od-trials/01-built-app --out notes.md

Reads Claude Code transcripts (~/.claude/projects/<folder-key>/*.jsonl) and prints the person's own messages in
order, with times. Skill bodies, system reminders and session briefs are left out. It reads only; the transcripts
stay on this machine, and nothing here is meant for the repo except the lessons drawn from it
(_coordination/TRIAL-LEDGER.md).
"""
import argparse
import json
import pathlib
import re

SKIP = ("<", "Base directory for this skill", "Caveat:", "[Request interrupted")


def folder_key(path):
    return re.sub(r"[^A-Za-z0-9]", "-", str(pathlib.Path(path).expanduser().resolve()))


def messages(transcript):
    for line in transcript.read_text().splitlines():
        try:
            o = json.loads(line)
        except ValueError:
            continue
        if o.get("type") != "user" or o.get("isMeta"):
            continue
        c = o["message"].get("content")
        texts = [c] if isinstance(c, str) else [b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text"]
        for t in texts:
            t = t.strip()
            if t and not t.startswith(SKIP) and "Background (from the session" not in t[:300]:
                yield o.get("timestamp", "")[:16].replace("T", " "), t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", help="the trial's project folder")
    ap.add_argument("--out", help="write Markdown here instead of printing")
    a = ap.parse_args()
    proj = pathlib.Path.home() / ".claude" / "projects" / folder_key(a.folder)
    out = [f"# What the person typed: {pathlib.Path(a.folder).name}\n"]
    for t in sorted(proj.glob("*.jsonl"), key=lambda p: p.stat().st_mtime):
        msgs = list(messages(t))
        if not msgs:
            continue
        out.append(f"\n## Session {t.stem[:8]} ({len(msgs)} messages)\n")
        for i, (ts, text) in enumerate(msgs, 1):
            out.append(f"\n**{i}. {ts}**\n\n{text}\n")
    text = "".join(out)
    if a.out:
        pathlib.Path(a.out).expanduser().write_text(text)
        print(a.out)
    else:
        print(text)


if __name__ == "__main__":
    main()
