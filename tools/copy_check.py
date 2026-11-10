#!/usr/bin/env python3
"""Flag the words and shapes that make public copy read as AI-written (docs/COPY.md).

  python3 tools/copy_check.py FILE ...       check Markdown, HTML, JSON, text or composition files
  echo "some copy" | python3 tools/copy_check.py -
  python3 tools/copy_check.py --strict FILE  exit 1 when anything is found (for CI or a pre-render step)

It reports; it never edits. One hit proves little. Several in one paragraph is what readers notice.
Code blocks, inline code, HTML tags, URLs and CSS/JS are skipped. Standard library only.
"""
import re
import sys
from pathlib import Path

WORDS = """delve delves delving tapestry testament pivotal crucial vibrant showcase showcases showcasing landscape realm
foster fosters underscore underscores intricate multifaceted holistic robust seamless seamlessly effortless effortlessly
elevate elevates unlock unlocks unleash supercharge supercharged leverage leverages leveraging harness streamline
streamlines revolutionize revolutionise revolutionary transformative game-changer game-changing cutting-edge next-level
world-class best-in-class embark meticulous meticulously nuanced ever-evolving empower empowers empowering
synergy paradigm unparalleled elevated boost boosts enhance enhances ensure ensures""".split()

PHRASES = [
    (r"\bin today'?s (fast-paced|digital|modern|ever)", "warm-up opener"),
    (r"\bin a world where\b", "warm-up opener"),
    (r"^\s*imagine\b", "warm-up opener"),
    (r"\bwhether you'?re an? \w+ or an? \w+", "'whether you're X or Y'"),
    (r"\blook no further\b|\bsay goodbye to\b|\bhere'?s the thing\b|\blet'?s dive\b|\bdive (in|into)\b", "stock phrase"),
    (r"^\s*(overall|in conclusion|in summary|ultimately|to sum up),", "summary closer"),
    (r"\bthe (result|best part|catch|secret|answer)\?", "question answered at once"),
    (r"\b(it'?s|this is|that'?s) not (just )?(a |an |about )?[^.?!]{1,40}[.,;] (it'?s|this is|that'?s)\b", "'it's not X, it's Y'"),
    (r"\bnot (just|only|merely) [^.?!]{1,40}, but\b", "'not just X, but Y'"),
    (r"\bno [^.?!]{1,25}\. no [^.?!]{1,25}\. just\b", "'No X. No Y. Just Z.'"),
    (r"\bfrom [^.,;]{2,30} to [^.,;]{2,30}, (and )?(from|everything)\b", "false range"),
    (r", (highlighting|underscoring|emphasizing|emphasising|showcasing|reflecting|making it|ensuring|demonstrating) ", "trailing '-ing' clause"),
    (r"\b(easier|faster|better) than ever\b", "empty comparison"),
    (r"\bjourney\b|\bnavigate the\b", "journey/navigate metaphor"),
    (r"\b(stunning|beautiful|gorgeous|premium|delightful|powerful|comprehensive)\b", "self-praise adjective: show it instead"),
    (r"\b(thousands|millions) of (users|designers|developers|teams|happy)\b", "traction claim: check FACTS.md"),
]

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
TRIAD = re.compile(r"\b([a-z-]{4,}), ([a-z-]{4,}),? and ([a-z-]{4,})\b")
ADJ = re.compile(r"(ive|ful|less|ous|al|ic|able|ible|ent|ant|ed|ing|ly|y)$")


def prose(text, suffix):
    if suffix in {".html", ".htm", ".tsx", ".jsx", ".vue", ".svelte"}:
        text = re.sub(r"<(script|style)\b.*?</\1>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", "\n", text)
        text = re.sub(r"\{[^{}\n]*\}", " ", text)
    if suffix in {".js", ".ts", ".json", ".tsx", ".jsx"}:
        # keep only string literals that look like sentences or labels
        strings = re.findall(r"([\"'`])((?:(?!\1).){8,}?)\1", text)
        return "\n".join(s for _, s in strings if " " in s and not re.search(r"[{}();=<>]|^\s*[\w.-]+/", s))
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "`…`", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def check(text, name):
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        for w in WORDS:
            if re.search(rf"(?<![\w-]){re.escape(w)}(?![\w-])", low):
                hits.append((n, f"word '{w}'", line))
        for pat, why in PHRASES:
            if re.search(pat, low):
                hits.append((n, why, line))
        if "—" in line:
            hits.append((n, "em dash", line))
        if EMOJI.search(line):
            hits.append((n, "emoji", line))
        if line.count("!") and not re.search(r"!\[|!=|<!", line):
            hits.append((n, "exclamation mark", line))
        m = TRIAD.search(line)
        if m and sum(bool(ADJ.search(w)) for w in m.groups()) >= 2:
            hits.append((n, f"list of three ('{m.group(0)}'): use the real count", line))
    return hits


def rhythm(text):
    """Most AI copy keeps every sentence about the same length."""
    sents = [s for s in re.split(r"(?<=[.?!])\s+", re.sub(r"\s+", " ", text)) if len(s.split()) >= 3]
    if len(sents) < 8:
        return None
    lens = [len(s.split()) for s in sents]
    mean = sum(lens) / len(lens)
    sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
    return mean, sd


def main(argv):
    strict = "--strict" in argv
    paths = [a for a in argv if a != "--strict"]
    if not paths:
        print(__doc__)
        return 2
    total = 0
    for p in paths:
        if p == "-":
            raw, name, suffix = sys.stdin.read(), "stdin", ".txt"
        else:
            path = Path(p)
            raw, name, suffix = path.read_text(errors="replace"), p, path.suffix.lower()
        text = prose(raw, suffix)
        hits = check(text, name)
        total += len(hits)
        for n, why, line in hits:
            print(f"{name}:{n}: {why}: {line.strip()[:110]}")
        r = rhythm(text)
        if r and r[1] < 0.35 * r[0]:
            print(f"{name}: sentence lengths are even (mean {r[0]:.0f} words, spread {r[1]:.1f}): mix short and long")
            total += 1
    print(f"{total} hit(s). Fix each, or keep it on purpose. Then read it out loud (docs/COPY.md).")
    return 1 if strict and total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
