#!/usr/bin/env python3
"""Static red-flag scan of a pull request's diff, for OpenDesigner maintainers. It never runs PR code.

    python3 scan_pr.py origin/main refs/od-review/pr-36          scan base...head
    python3 scan_pr.py origin/main refs/od-review/pr-36 --json   machine-readable

Findings are BLOCK (do not run or merge until a human has read it), REVIEW (read the lines and decide) or
NOTE (convention drift). A clean scan is not a pass: it only means no known pattern matched. Read the diff.
Standard library only. Run from the repository root.
"""
import argparse, json, re, subprocess, sys

HIGH_RISK = [  # (path regex, why a human must read every changed line)
    (r"^\.github/workflows/", "CI workflow: can run code with repository permissions"),
    (r"^\.github/(FUNDING\.yml|CODEOWNERS)$|^funding\.json$", "money or ownership routing"),
    (r"^\.(claude|agents)/skills/opendesigner", "generated copy of skills/: sync_skills.py --check proves it matches"),
    (r"^\.claude/|^\.agents/|^\.mcp\.json$|^\.cursor/|^\.vscode/", "agent config: hooks, settings, MCP servers or skills run on the maintainer's machine"),
    (r"^\.claude-plugin/|^plugin\.json$", "plugin manifest: what every user installs"),
    (r"(^|/)(AGENTS|CLAUDE|GEMINI)\.md$|^llms\.txt$|SKILL\.md$|^chatgpt-project/instructions\.md$"
     r"|references/(rules|guardrails|hooks|improve)\.md$", "instructions that other people's AI models follow"),
    (r"journey\.py$|^server/|^docs/PRIVACY\.md$", "telemetry and consent: what may leave a user's machine"),
    (r"^(LICENSE|LICENSE-CONTENT|CITATION\.cff|GOVERNANCE\.md|SECURITY\.md)$", "licence, governance or security policy"),
    (r"^\.gitignore$", "ignore rules: removing a line can expose secrets"),
    (r"^tools/.*\.py$|^skills/.*\.py$", "code maintainers and users run"),
    (r"\.html?$", "page that runs in a browser or artifact"),
]
GENERATED = [(r"^\.agents/skills/opendesigner|^\.claude/skills/opendesigner", r"^skills/", "sync_skills.py"),
             (r"^data/|^skills/[^/]+/references/.*\.json$|^skills/opendesigner/references/(stages|cards)/"
              r"|^chatgpt-project/knowledge/", r"^synthesis/", "build_data.py")]
LINE_RULES = [  # (severity, label, regex, file regex it applies to or None for all)
    ("BLOCK", "workflow trigger that runs fork code with secrets", r"pull_request_target|workflow_run", r"^\.github/"),
    ("BLOCK", "workflow write permission or secret use", r"permissions:\s*write-all|:\s*write\b|\$\{\{\s*secrets\.", r"^\.github/"),
    ("REVIEW", "third-party action not pinned to a commit SHA", r"uses:\s*(?!actions/)[\w.-]+/[\w.-]+@(?![0-9a-f]{40})", r"^\.github/"),
    ("BLOCK", "pipe from the network into a shell", r"(curl|wget|iwr|Invoke-WebRequest)[^\n|]*\|\s*(ba|z)?sh|\|\s*iex", None),
    ("BLOCK", "decode-and-run pattern", r"(exec|eval)\s*\(\s*(base64|codecs|bytes\.fromhex|zlib|marshal)|b64decode\([^)]*\)\s*\)|atob\(", None),
    ("BLOCK", "possible secret", r"AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{36}|sk-(ant-)?[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}"
     r"|-----BEGIN [A-Z ]*PRIVATE KEY", None),
    ("REVIEW", "network access", r"^\+\s*(import|from)\s+(urllib|http|socket|requests|httpx|aiohttp|ftplib|smtplib|ssl)\b"
     r"|urlopen\(|\b(requests|httpx)\.(get|post|put|request)\(|socket\.socket\(|fetch\(|XMLHttpRequest|sendBeacon|WebSocket\("
     r"|^\+\s*(-\s*)?(run:\s*)?(curl|wget)\b", r"\.(py|js|mjs|ts|html?|sh|ya?ml)$"),
    ("REVIEW", "process or dynamic code execution", r"\b(subprocess|os\.system|os\.popen|pty\.spawn|ctypes|pickle\.loads?|marshal\.loads?"
     r"|__import__|importlib)\b|(?<![\w.])(eval|exec|compile)\s*\(|new Function\(|child_process", r"\.(py|js|mjs|ts|html?|sh)$"),
    ("REVIEW", "external script, style or frame", r"<(script|iframe|link|img)[^>]+(src|href)=[\"']https?://", r"\.html?$"),
    ("REVIEW", "writes outside the project or to home/system paths", r"^\+(?!#!).*(expanduser|Path\.home\(\)|~/\.|/etc/|/usr/|AppData|\.ssh|\.aws|\.config)", r"\.(py|js|sh)$"),
    ("REVIEW", "text aimed at an AI model rather than a reader", r"(?i)ignore (all |any )?(previous|prior|above) (instructions|rules)|you are now|do not (tell|inform) the user"
     r"|(disable|skip|bypass) (the )?(safety|guardrail|check|consent|review)|auto-?merge|without asking|system prompt", r"\.(md|json|txt|html?|ya?ml)$"),
    ("REVIEW", "long encoded-looking string", r"[A-Za-z0-9+/=]{200,}|(\\x[0-9a-fA-F]{2}){20,}", None),
]
INVISIBLE = re.compile("[​-‏‪-‮⁦-⁩﻿]")
IST = re.compile(r"^\+- \d{4}-\d{2}-\d{2} \d{2}:\d{2} IST ")


def git(*args, raw=False):
    r = subprocess.run(["git", *args], capture_output=True)
    if r.returncode:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.decode().strip()}\n"
                 "Fetch the PR first: git fetch origin pull/<N>/head:refs/od-review/pr-<N>")
    return r.stdout if raw else r.stdout.decode("utf-8", "replace")


def local_modules(head, path):
    """Modules that sit next to `path` at the PR head (sibling imports are fine)."""
    folder = path.rsplit("/", 1)[0] + "/"
    names = git("ls-tree", "--name-only", head, folder).splitlines()
    return {n.rsplit("/", 1)[-1][:-3] for n in names if n.endswith(".py")}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("base"); ap.add_argument("head"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rng = f"{a.base}...{a.head}"
    found = []
    add = lambda sev, path, line, msg: found.append({"severity": sev, "path": path, "line": line, "msg": msg})

    status = [l.split("\t") for l in git("diff", "--name-status", "-M", rng).splitlines() if l]
    paths = [s[-1] for s in status]
    for s in status:
        if s[0].startswith("D"):
            add("REVIEW", s[1], 0, "file deleted")
    for line in git("diff", "--summary", rng).splitlines():
        if "mode 120000" in line:
            add("BLOCK", line.split()[-1], 0, "symlink added (can point outside the repo)")
        elif re.search(r"mode 100755", line):
            add("REVIEW", line.split()[-1], 0, "file made executable")
    for line in git("diff", "--numstat", rng).splitlines():
        adds, _, path = line.split("\t", 2)
        if adds == "-":
            add("BLOCK", path, 0, "binary file: cannot be reviewed as text")
    for path in paths:
        for rx, why in HIGH_RISK:
            if re.search(rx, path):
                add("REVIEW", path, 0, f"high-risk path, read every line: {why}")
                break
        if re.search(r"(^|/)(setup\.py|pyproject\.toml|requirements[^/]*\.txt|package(-lock)?\.json|Pipfile|[^/]+\.pth)$", path):
            add("BLOCK", path, 0, "dependency or install hook: skills and tools must stay standard-library only")
    for gen_rx, src_rx, tool in GENERATED:
        if any(re.search(gen_rx, p) for p in paths) and not any(re.search(src_rx, p) for p in paths):
            add("NOTE", "-", 0, f"generated copies changed without their source; rebuild with {tool} instead")

    patch = git("diff", "-U0", "--no-color", rng, raw=True)
    path, lineno = None, 0
    for rawline in patch.split(b"\n"):
        if rawline.startswith(b"+++ "):
            path = rawline[6:].decode("utf-8", "replace") if rawline[4:6] == b"b/" else None
            continue
        if rawline.startswith(b"@@"):
            m = re.search(rb"\+(\d+)", rawline)
            lineno = int(m.group(1)) if m else 0
            continue
        if path is None or re.match(r"\.(claude|agents)/skills/opendesigner", path) and \
                re.sub(r"^\.(claude|agents)/", "", path) in paths:
            continue
        if rawline.startswith(b"-") and not rawline.startswith(b"---"):
            if path.startswith("traces/"):
                add("REVIEW", path, lineno, "line removed from an append-only trace")
            if path == ".gitignore":
                add("REVIEW", path, lineno, "ignore rule removed: " + rawline[1:].decode("utf-8", "replace"))
            continue
        if not rawline.startswith(b"+"):
            continue
        try:
            text = rawline.decode("utf-8")
        except UnicodeDecodeError:
            add("REVIEW", path, lineno, "not valid UTF-8 (tools that read it as UTF-8 will crash)")
            text = rawline.decode("utf-8", "replace")
        if INVISIBLE.search(text):
            add("BLOCK", path, lineno, "invisible or bidirectional control character (can hide code)")
        for sev, label, rx, file_rx in LINE_RULES:
            if (file_rx is None or re.search(file_rx, path)) and re.search(rx, text):
                add(sev, path, lineno, f"{label}: {text[1:].strip()[:140]}")
        if path == "_coordination/DECISIONS.md" and text.startswith("+- ") and not IST.match(text):
            add("NOTE", path, lineno, "decision line is not in the 'YYYY-MM-DD HH:MM IST' format")
        if path.startswith("skills/") and path.endswith(".py"):
            m = re.match(r"\+\s*(?:from|import)\s+([A-Za-z_]\w*)", text)
            if m and m.group(1) not in sys.stdlib_module_names and m.group(1) not in local_modules(a.head, path):
                add("BLOCK", path, lineno, f"non-standard-library import '{m.group(1)}' in a skill (skills ship offline)")
        lineno += 1

    order = {"BLOCK": 0, "REVIEW": 1, "NOTE": 2}
    found.sort(key=lambda f: (order[f["severity"]], f["path"], f["line"]))
    if a.json:
        print(json.dumps({"range": rng, "files": len(paths), "findings": found}, indent=2))
    else:
        print(f"{rng}: {len(paths)} files changed")
        for f in found:
            loc = f"{f['path']}:{f['line']}" if f["line"] else f["path"]
            print(f"{f['severity']:6} {loc}  {f['msg']}")
        counts = {s: sum(f["severity"] == s for f in found) for s in order}
        print(f"\n{counts['BLOCK']} block, {counts['REVIEW']} review, {counts['NOTE']} note. A clean scan is not a pass; read the diff.")
    sys.exit(1 if any(f["severity"] == "BLOCK" for f in found) else 0)


if __name__ == "__main__":
    main()
