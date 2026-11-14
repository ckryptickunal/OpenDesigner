#!/usr/bin/env python3
"""Gemini evals: run the agent eval cases (evals/<case>/) with a Gemini model, so OpenDesigner is tested outside Claude.

    python3 tools/gemini_evals.py --list                                  which cases would run (costs nothing)
    python3 tools/gemini_evals.py --case 'contrast*' --runs 1             one case, one run, while checking the runner
    python3 tools/gemini_evals.py --runs 3 --save                         every case, 3 runs (the comparison with Claude)
    python3 tools/gemini_evals.py --runs 3 --save --compare evals/agent/results/<date>-claude.json
    python3 tools/gemini_evals.py drift --example devtool-dense --runs 1  build tasks on a finished system (see DRIFT below)

`claude plugin eval` runs the Claude side (tools/agent_evals.py). This file is its Gemini twin:
- The same cases, prompts, fixtures, scaffold scripts and graders. The plugin is staged the way agent_evals.py stages it.
- A small agent loop with the tools a case allows (Read, Glob, Grep, Bash, Write, Edit, Skill, AskUserQuestion), shaped
  like Claude Code's, so the skills read the same. The Skill tool returns a SKILL.md with its folder, as Claude Code does.
  The plugin's start-of-session hook (engine.py status --hook) runs when the workspace has opendesigner/state.json.
- Bash runs in macOS sandbox-exec: no network, writes only inside the run's workspace and temp folders, no .env, ~/.ssh
  or other credentials. Read, Write and Edit refuse paths outside the workspace, the case's extra folders and the skills.
- The llm graders are judged by the same Haiku model the Claude evals use (`claude -p --model haiku`), so the judge is
  not the model under test. regex, file_exists and tool_used graders are checked here, exactly.
- Standard library HTTP only. The key is read from GEMINI_API_KEY in .env (this checkout's, else the main checkout's)
  or the environment, sent in a header, and never printed, logged or written. One call at a time (a lock file, also
  across processes), a backoff on 429 and 5xx that honours the server's retry delay, and a cost ceiling per invocation
  (--max-cost-usd) checked before every call. Spend is priced from usageMetadata and kept in dist/gemini/spend.jsonl.
- Raw transcripts stay in dist/gemini/ (git-ignored). --save writes only the summary to evals/agent/results/.

Only the "with" arm runs (OpenDesigner loaded), which is what the score column of the Claude summary is.

DRIFT: `drift` copies a finished example system (examples/<name>: DESIGN.md, tokens, build) into a workspace and asks the
model for a pricing page, a settings screen and a chat view. Then it measures what came back: engine.py review (hard-coded
values, tokens in charge), the review skill's probe.js in a real browser through capture.py (off-scale spacing, fonts and
colours outside the tokens, cut-off text) and a few copy rules from DESIGN.md. Results go to dist/gemini/drift/.
"""
import argparse
import datetime
import fcntl
import http.client
import fnmatch
import glob as globmod
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import agent_evals as ae  # noqa: E402  (case discovery, tags, staging)

WORK = ROOT / "dist" / "gemini"
STAGE = WORK / "plugin"
OUT = ROOT / "evals" / "agent" / "results"
API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
# USD per million tokens, from https://ai.google.dev/gemini-api/docs/pricing (read 2026-11-13). Prompts over 200k tokens cost more.
PRICES = {"gemini-3.1-pro-preview": {"in": (2.0, 4.0), "out": (12.0, 18.0), "cached": (0.20, 0.40)}}
DEFAULT_MODEL = "gemini-3.1-pro-preview"


# ---------------------------------------------------------------- the key and the client

def load_key():
    """GEMINI_API_KEY from the environment, this checkout's .env, or the main checkout's (worktrees have none)."""
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"]
    places = [ROOT / ".env"]
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    if common:
        places.append(pathlib.Path(common).parent / ".env")
    for p in places:
        if p.exists():
            for line in p.read_text().splitlines():
                k, _, v = line.partition("=")
                if k.strip() == "GEMINI_API_KEY" and v.strip():
                    return v.strip().strip("'\"")
    sys.exit("no GEMINI_API_KEY in the environment or .env")


class CostCap(Exception):
    pass


class Gemini:
    def __init__(self, model, cap_usd, label):
        self.model, self.cap, self.label = model, cap_usd, label
        self.key = load_key()
        self.spent, self.calls = 0.0, 0
        self.tokens = {"prompt": 0, "cached": 0, "output": 0}
        WORK.mkdir(parents=True, exist_ok=True)
        self.lock = open(WORK / "call.lock", "w")

    def price(self, usage):
        p = PRICES.get(self.model, PRICES[DEFAULT_MODEL])
        prompt = usage.get("promptTokenCount", 0)
        cached = usage.get("cachedContentTokenCount", 0)
        out = usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)
        tier = 1 if prompt > 200_000 else 0
        return ((prompt - cached) * p["in"][tier] + cached * p["cached"][tier] + out * p["out"][tier]) / 1e6

    def generate(self, body):
        if self.spent >= self.cap:
            raise CostCap(f"cost ceiling ${self.cap} reached (spent ${self.spent:.2f})")
        data = json.dumps(body).encode()
        delay = 5.0
        for attempt in range(8):
            req = urllib.request.Request(API.format(model=self.model), data=data, method="POST",
                                         headers={"Content-Type": "application/json", "x-goog-api-key": self.key})
            fcntl.flock(self.lock, fcntl.LOCK_EX)  # one call at a time, across processes too
            try:
                with urllib.request.urlopen(req, timeout=600) as r:
                    res = json.loads(r.read())
                break
            except urllib.error.HTTPError as e:
                text = e.read().decode(errors="replace")[:2000]
                if e.code in (429, 500, 502, 503, 504) and attempt < 7:
                    m = re.search(r'"retryDelay":\s*"(\d+(?:\.\d+)?)s"', text)
                    wait = max(float(m.group(1)) if m else 0, delay)
                    print(f"  gemini {e.code}; waiting {wait:.0f}s", file=sys.stderr)
                    time.sleep(wait)
                    delay = min(delay * 2, 120)
                    continue
                raise RuntimeError(f"gemini HTTP {e.code}: {text[:500]}") from None
            except (urllib.error.URLError, OSError, http.client.HTTPException) as e:  # a dropped connection is retried too
                if attempt < 7:
                    time.sleep(delay)
                    delay = min(delay * 2, 120)
                    continue
                raise RuntimeError(f"gemini network error: {e}") from None
            finally:
                fcntl.flock(self.lock, fcntl.LOCK_UN)
        u = res.get("usageMetadata", {})
        cost = self.price(u)
        self.spent += cost
        self.calls += 1
        self.tokens["prompt"] += u.get("promptTokenCount", 0)
        self.tokens["cached"] += u.get("cachedContentTokenCount", 0)
        self.tokens["output"] += u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)
        with open(WORK / "spend.jsonl", "a") as f:
            f.write(json.dumps({"t": datetime.datetime.now().isoformat(timespec="seconds"), "model": self.model,
                                "label": self.label, "usd": round(cost, 5), "usage": u}) + "\n")
        return res


# ---------------------------------------------------------------- tools the agent gets

DECLS = {
    "Read": {"description": "Read a file. Returns lines numbered like cat -n. Use offset and limit for big files.",
             "parameters": {"type": "object", "properties": {"file_path": {"type": "string", "description": "absolute path"},
                            "offset": {"type": "integer"}, "limit": {"type": "integer"}}, "required": ["file_path"]}},
    "Glob": {"description": "Find files by glob pattern (supports **). Returns matching paths.",
             "parameters": {"type": "object", "properties": {"pattern": {"type": "string"}, "path": {"type": "string"}},
                            "required": ["pattern"]}},
    "Grep": {"description": "Search file contents with a regular expression. Returns path:line:text matches.",
             "parameters": {"type": "object", "properties": {"pattern": {"type": "string"}, "path": {"type": "string"},
                            "glob": {"type": "string"}}, "required": ["pattern"]}},
    "Bash": {"description": "Run a shell command in the project folder (zsh-compatible /bin/bash). No network. "
                            "Returns stdout and stderr.",
             "parameters": {"type": "object", "properties": {"command": {"type": "string"},
                            "timeout": {"type": "integer", "description": "seconds, default 120, max 600"}},
                            "required": ["command"]}},
    "Write": {"description": "Write a file, replacing it if it exists.",
              "parameters": {"type": "object", "properties": {"file_path": {"type": "string"}, "content": {"type": "string"}},
                             "required": ["file_path", "content"]}},
    "Edit": {"description": "Replace an exact string in a file. old_string must be unique unless replace_all is true.",
             "parameters": {"type": "object", "properties": {"file_path": {"type": "string"}, "old_string": {"type": "string"},
                            "new_string": {"type": "string"}, "replace_all": {"type": "boolean"}},
                            "required": ["file_path", "old_string", "new_string"]}},
    "Skill": {"description": "Load a skill's instructions by name. Use it when a task matches a skill in the list.",
              "parameters": {"type": "object", "properties": {"skill": {"type": "string"}, "args": {"type": "string"}},
                             "required": ["skill"]}},
    "AskUserQuestion": {"description": "Ask the person a multiple-choice question in the app's question box (up to 4 "
                                       "questions per call, 2-4 options each; they can also type their own answer).",
                        "parameters": {"type": "object", "properties": {"questions": {"type": "array", "items": {
                            "type": "object", "properties": {"question": {"type": "string"}, "header": {"type": "string"},
                                                             "options": {"type": "array", "items": {"type": "object", "properties": {
                                                                 "label": {"type": "string"}, "description": {"type": "string"}},
                                                                 "required": ["label"]}},
                                                             "multiSelect": {"type": "boolean"}},
                            "required": ["question", "options"]}}}, "required": ["questions"]}},
}


def skills_index(stage):
    out = []
    for f in sorted((stage / "skills").glob("*/SKILL.md")):
        head = f.read_text().split("---")[1]
        m = re.search(r"^description:\s*(.+)$", head, re.M)
        out.append((f.parent.name, (m.group(1).strip() if m else "").strip("'\"")))
    return out


def sandbox_profile(ws):
    home = str(pathlib.Path.home())
    allow = [ws, str(pathlib.Path(ws).parent / "tmp"), "/dev"]  # the workspace and this run's own temp folder only
    allow = " ".join(f'(subpath "{os.path.realpath(p)}")' for p in allow)
    return f"""(version 1)
(allow default)
(deny network*)
(deny file-write*)
(allow file-write* {allow})
(deny file-read* (regex #"/\\.env$") (subpath "{home}/.ssh") (subpath "{home}/.aws") (subpath "{home}/.config")
  (subpath "{home}/.netrc") (subpath "{home}/Library/Keychains") (subpath "{home}/.claude"))
"""


class Workspace:
    def __init__(self, ws, extra, stage, allowed):
        self.ws, self.extra, self.stage, self.allowed = ws, extra, stage, allowed
        self.profile = ws.parent / "sandbox.sb"
        (ws.parent / "tmp").mkdir(exist_ok=True)
        self.profile.write_text(sandbox_profile(str(ws)))
        self.env = {"PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin", "HOME": str(ws),
                    "LANG": "en_US.UTF-8", "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(ws.parent / "tmp"),
                    "CLAUDE_PROJECT_DIR": str(ws), "CLAUDE_PLUGIN_ROOT": str(stage),
                    "GIT_CEILING_DIRECTORIES": str(ws.parent)}  # the run is not inside this repo's git

    def path(self, p, write=False):
        q = pathlib.Path(p)
        q = (q if q.is_absolute() else self.ws / q).resolve()
        roots = [self.ws.resolve()] + ([] if write else [x.resolve() for x in self.extra] + [(self.stage / "skills").resolve()])
        if not any(q == r or r in q.parents for r in roots):
            raise PermissionError(f"{p} is outside the folders this session can {'write' if write else 'read'}")
        return q

    def call(self, name, a):
        if name not in self.allowed:
            return f"Error: the {name} tool is not available in this session."
        try:
            return getattr(self, "t_" + name)(a)
        except PermissionError as e:
            return f"Error: {e}"
        except Exception as e:  # a tool error goes back to the model, as in Claude Code
            return f"Error: {type(e).__name__}: {e}"

    def t_Read(self, a):
        p = self.path(a["file_path"])
        if p.is_dir():
            return f"Error: {p} is a directory"
        lines = p.read_text(errors="replace").splitlines()
        off = max(int(a.get("offset") or 1), 1)
        lim = int(a.get("limit") or 2000)
        body = "\n".join(f"{i:6}\t{l[:2000]}" for i, l in enumerate(lines[off - 1:off - 1 + lim], off))
        return body or "(empty file)"

    def t_Glob(self, a):
        base = self.path(a.get("path") or str(self.ws))
        hits = sorted(globmod.glob(str(base / a["pattern"]), recursive=True))
        return "\n".join(hits[:300]) or "No files found"

    def t_Grep(self, a):
        base = self.path(a.get("path") or str(self.ws))
        rx = re.compile(a["pattern"])
        files = [base] if base.is_file() else [f for f in base.rglob(a.get("glob") or "*") if f.is_file()]
        out = []
        for f in files:
            if f.stat().st_size > 2_000_000:
                continue
            for i, line in enumerate(f.read_text(errors="replace").splitlines(), 1):
                if rx.search(line):
                    out.append(f"{f}:{i}:{line[:300]}")
                    if len(out) >= 300:
                        return "\n".join(out) + "\n(truncated)"
        return "\n".join(out) or "No matches"

    def t_Bash(self, a):
        t = min(int(a.get("timeout") or 120), 600)
        try:
            p = subprocess.run(["sandbox-exec", "-f", str(self.profile), "/bin/bash", "-c", a["command"]], cwd=self.ws,
                               env=self.env, capture_output=True, text=True, timeout=t)
        except subprocess.TimeoutExpired:
            return f"Error: command timed out after {t}s"
        out = (p.stdout + ("\n" + p.stderr if p.stderr else "")).strip()
        if len(out) > 30000:
            out = out[:15000] + "\n...(output truncated)...\n" + out[-15000:]
        return (out or "(no output)") + (f"\n[exit code {p.returncode}]" if p.returncode else "")

    def t_Write(self, a):
        p = self.path(a["file_path"], write=True)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(a["content"])
        return f"File written: {p}"

    def t_Edit(self, a):
        p = self.path(a["file_path"], write=True)
        s = p.read_text()
        n = s.count(a["old_string"])
        if n == 0:
            return "Error: old_string not found in the file"
        if n > 1 and not a.get("replace_all"):
            return f"Error: old_string appears {n} times; give more context or set replace_all"
        p.write_text(s.replace(a["old_string"], a["new_string"], -1 if a.get("replace_all") else 1))
        return f"File edited: {p}"

    def t_Skill(self, a):
        name = a["skill"].split(":")[-1].strip().lstrip("/")
        f = self.stage / "skills" / name / "SKILL.md"
        if not f.exists():
            return f"Error: no skill named {a['skill']}"
        body = f.read_text().split("---", 2)[2]
        return f"Base directory for this skill: {f.parent}\n\n{body}" + (f"\n\nARGUMENTS: {a['args']}" if a.get("args") else "")

    def t_AskUserQuestion(self, a):
        return "No answer yet: the person sees your question and will reply after this turn ends."


def system_prompt(ws, extra, skills, allowed):
    lines = [
        "You are an AI agent helping a person with their software project, in a coding tool like Claude Code. You work by",
        "calling the tools you are given; the person only sees your text replies. Keep replies readable.",
        f"Primary working directory: {ws}",
    ]
    if extra:
        lines.append("Additional working directories you can read: " + ", ".join(str(x) for x in extra))
    lines.append(f"Platform: macOS. Today's date: {datetime.date.today().isoformat()}. Tools: {', '.join(sorted(allowed))}.")
    if skills and "Skill" in allowed:
        lines += ["", "The following skills are available for use with the Skill tool. When a request matches a skill, "
                      "call the Skill tool first; its instructions load for you to follow.", ""]
        lines += [f"- {n}: {d}" for n, d in skills]
    return "\n".join(lines)


def to_text(parts):
    return "".join(p.get("text", "") for p in parts if not p.get("thought"))


def run_agent(client, prompt, ws, extra, stage, allowed, max_turns, timeout, with_skills=True, transcript=None, followup=None):
    """The agent loop. Returns (final reply, tool calls, stop reason). `followup(reply)` may return the person's next
    message when the model ends its turn (the drift tasks use it to answer a question and say "go ahead")."""
    w = Workspace(ws, extra, stage, set(allowed))
    sys_text = system_prompt(ws, extra, skills_index(stage) if with_skills else [], allowed)
    user = prompt
    if with_skills and (ws / "opendesigner" / "state.json").exists():  # the plugin's SessionStart hook
        hook = json.loads((stage / "hooks" / "hooks.json").read_text())["hooks"]["SessionStart"][0]["hooks"][0]["command"]
        h = subprocess.run(["/bin/bash", "-c", hook], cwd=ws, env=w.env, capture_output=True, text=True, timeout=20).stdout.strip()
        if h:
            user = f"<system-reminder>\nSessionStart hook additional context: {h}\n</system-reminder>\n\n{prompt}"
    contents = [{"role": "user", "parts": [{"text": user}]}]
    tools = [{"functionDeclarations": [{"name": n, **DECLS[n]} for n in allowed if n in DECLS]}]
    calls, reply, stop = [], "", "max_turns"
    start = time.time()
    for turn in range(max_turns):
        if time.time() - start > timeout:
            stop = "timeout"
            break
        try:
            res = client.generate({"systemInstruction": {"parts": [{"text": sys_text}]}, "contents": contents, "tools": tools,
                                   "generationConfig": {"temperature": 1.0}})
        except CostCap as e:
            stop = f"cost_cap: {e}"
            break
        cand = (res.get("candidates") or [{}])[0]
        content = cand.get("content") or {"role": "model", "parts": []}
        content.setdefault("role", "model")
        parts = content.get("parts", [])
        contents.append(content)  # verbatim, so Gemini 3's thought signatures go back with the function calls
        text = to_text(parts)
        if text.strip():
            reply = text
        fcs = [p["functionCall"] for p in parts if "functionCall" in p]
        if not fcs:
            stop = cand.get("finishReason", "STOP")
            nxt = followup(reply) if followup else None
            if not nxt:
                break
            calls.append({"tool": "(person replied)", "input": {"after": reply[:1500], "message": nxt}, "turn": turn, "output": ""})
            contents.append({"role": "user", "parts": [{"text": nxt}]})
            continue
        responses = []
        for fc in fcs:
            out = w.call(fc["name"], fc.get("args", {}))
            calls.append({"tool": fc["name"], "input": fc.get("args", {}), "turn": turn, "output": out[:4000]})
            responses.append({"functionResponse": {"name": fc["name"], "response": {"result": out}}})
        contents.append({"role": "user", "parts": responses})
        reply = ""  # a reply is the text of the turn that ends the session
    if transcript:
        transcript.write_text(json.dumps({"system": sys_text, "contents": contents, "stop": stop}, indent=1))
    return reply, calls, stop


# ---------------------------------------------------------------- graders

def front(path):
    s = path.read_text()
    parts = s.split("---")
    meta, body = {}, ""
    if len(parts) >= 3:
        meta = parse_yaml(parts[1])
        body = "---".join(parts[2:]).strip()
    return meta, body


def parse_yaml(text):
    """Enough YAML for the grader front matter: key: value, quoted strings, { a: b } maps and [a, b] lists."""
    out = {}
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = scalar(v.strip())
    return out


def scalar(v):
    if v.startswith("{") and v.endswith("}"):
        d = {}
        for item in v[1:-1].split(","):
            k, _, x = item.partition(":")
            d[k.strip()] = scalar(x.strip())
        return d
    if v.startswith("[") and v.endswith("]"):
        return [scalar(x.strip()) for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1].replace("''", "'") if v[0] == "'" else v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def workspace_files(ws):
    return sorted(str(p.relative_to(ws)) for p in ws.rglob("*") if p.is_file() and ".home" not in p.parts
                  and "__pycache__" not in p.parts)


def judge(rubric, prompt, reply, calls, ws, before):
    """The case's llm grader, judged by Haiku through the Claude CLI, as the Claude evals are."""
    written = [f for f in workspace_files(ws) if f not in before]
    shown = []
    for f in written[:12]:
        p = ws / f
        if p.stat().st_size < 6000 and p.suffix in {".md", ".json", ".css", ".html", ".txt", ".js", ".ts", ".tsx"}:
            shown.append(f"--- {f}\n{p.read_text(errors='replace')[:3000]}")
    tool_lines = [f"{c['tool']}: {json.dumps(c['input'])[:300]}" for c in calls][:60]
    q = (f"You grade one run of an AI agent. Apply the rubric strictly to what is shown.\n\nRUBRIC:\n{rubric}\n\n"
         f"THE PERSON'S MESSAGE:\n{prompt}\n\nTHE AGENT'S FINAL REPLY:\n{reply or '(no reply)'}\n\n"
         f"TOOL CALLS ({len(calls)}):\n" + "\n".join(tool_lines) + "\n\nFILES THE AGENT WROTE OR CHANGED:\n" +
         ("\n".join(written) or "(none)") + "\n\n" + "\n".join(shown) +
         '\n\nAnswer with one line of JSON only: {"pass": true or false, "reason": "one sentence"}')
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_CODE_") and k != "CLAUDECODE"}
    votes, reasons, cost = [], [], 0.0
    for _ in range(3):  # three votes and the majority, as `claude plugin eval` judges
        ok, why, c = judge_once(q, env)
        votes.append(ok)
        reasons.append(why)
        cost += c
        if votes.count(True) >= 2 or votes.count(False) >= 2:
            break
    ok = votes.count(True) >= 2
    return ok, f"judge votes: {' '.join('PASS' if v else 'FAIL' for v in votes)}. " + reasons[votes.index(ok)], cost


def judge_once(q, env):
    for attempt in range(3):
        p = subprocess.run(["claude", "-p", "--model", "haiku", "--output-format", "json", "--max-turns", "1",
                            "--tools", "", "--setting-sources", "", "--strict-mcp-config", "--disable-slash-commands",
                            "--system-prompt", "You grade AI agent runs against a rubric. Reply only with the JSON asked for."],
                           input=q, capture_output=True, text=True, env=env, cwd=tempfile.gettempdir(),
                           timeout=300)
        try:
            outer = json.loads(p.stdout)
            m = re.search(r"\{.*\}", outer.get("result", ""), re.S)
            verdict = json.loads(m.group(0))
            return bool(verdict.get("pass")), verdict.get("reason", ""), outer.get("total_cost_usd", 0)
        except Exception:
            time.sleep(3)
    return False, f"judge failed: {p.stderr[:200]}", 0


def grade(case_dir, prompt, reply, calls, ws, before):
    results, judge_cost = [], 0.0
    for g in sorted((case_dir / "graders").glob("*.md")):
        meta, body = front(g)
        kind = meta.get("type")
        ok, why = False, ""
        if kind == "regex":
            t = meta.get("target")
            if t == "files":
                text = "\n".join(workspace_files(ws))
            elif isinstance(t, dict) and t.get("source") == "file":
                hits = globmod.glob(str(ws / t["path"]), recursive=True)
                text = "\n".join(pathlib.Path(h).read_text(errors="replace") for h in hits if pathlib.Path(h).is_file())
            else:
                text = reply
            flags = (re.I if "i" in str(meta.get("flags", "")) else 0) | (re.M if "m" in str(meta.get("flags", "")) else 0)
            found = bool(re.search(meta["pattern"], text, flags))
            ok = not found if meta.get("match") == "not_contains" else found
            why = f"pattern {'found' if found else 'not found'}"
        elif kind == "file_exists":
            hits = [h for h in globmod.glob(str(ws / meta["path"]), recursive=True) if ".home" not in h]
            ok, why = bool(hits), (hits[0].replace(str(ws) + "/", "") if hits else "no file")
        elif kind == "tool_used":
            rx = re.compile(meta.get("input_match", ""), re.S) if meta.get("input_match") else None
            n = sum(1 for c in calls if c["tool"] == meta["tool"] and (not rx or rx.search(json.dumps(c["input"]))))
            lo, hi = int(meta.get("min", 1)), meta.get("max")
            ok = n >= lo and (hi is None or n <= int(hi))
            why = f"{n} matching calls"
        elif kind == "llm":
            ok, why, c = judge(body, prompt, reply, calls, ws, before)
            judge_cost += c
        else:
            why = f"unknown grader type {kind}"
        results.append({"grader": g.stem, "type": kind, "pass": ok, "why": why})
    return results, judge_cost


# ---------------------------------------------------------------- running the cases

def case_meta(case_dir):
    meta, prompt = front(case_dir / "prompt.md")
    cy = {}
    if (case_dir / "case.yaml").exists():
        text = (case_dir / "case.yaml").read_text()
        m = re.search(r"scaffold_script:\s*(\S+)", text)
        cy["scaffold"] = m.group(1) if m else None
        m = re.search(r"add_dirs:\s*\[([^\]]*)\]", text)
        cy["add_dirs"] = [x.strip() for x in m.group(1).split(",")] if m else []
    return meta, prompt, cy


def run_case(client, case_dir, run_no, outdir):
    meta, prompt, cy = case_meta(case_dir)
    rd = outdir / case_dir.name / f"run-{run_no}"
    if rd.exists():
        shutil.rmtree(rd)
    ws = rd / "workspace"
    ws.mkdir(parents=True)
    extra = []
    for d in cy.get("add_dirs", []):  # a copy, so a run can never change the fixture
        shutil.copytree(case_dir / d, rd / "extra" / d)
        extra.append(rd / "extra" / d)
    if cy.get("scaffold"):
        subprocess.run(["bash", str(case_dir / cy["scaffold"])], cwd=ws, check=True, capture_output=True, timeout=120,
                       env=os.environ | {"GIT_CEILING_DIRECTORIES": str(ws.parent)})
    before = set(workspace_files(ws))
    allowed = meta.get("allowed_tools") or ["Read", "Glob", "Grep", "Skill", "Bash", "Write", "Edit"]
    spent0 = client.spent
    t0 = time.time()
    try:
        reply, calls, stop = run_agent(client, prompt, ws, extra, STAGE, allowed, int(meta.get("max_turns", 30)),
                                       int(meta.get("timeout_seconds", 600)), transcript=rd / "transcript.json")
        err = None
    except RuntimeError as e:
        reply, calls, stop, err = "", [], "error", str(e)
    grades, jc = grade(case_dir, prompt, reply, calls, ws, before)
    score = sum(g["pass"] for g in grades) / len(grades) if grades else 0
    rec = {"case": case_dir.name, "run": run_no, "score": score, "stop": stop, "error": err, "turns": len({c["turn"] for c in calls}),
           "toolCalls": len(calls), "costUsd": round(client.spent - spent0, 4), "judgeCostUsd": round(jc, 4),
           "seconds": round(time.time() - t0), "grades": grades, "reply": reply, "before": sorted(before),
           "calls": [{k: c[k] for k in ("tool", "input", "turn")} | {"output": c["output"][:600]} for c in calls]}
    (rd / "result.json").write_text(json.dumps(rec, indent=1))
    return rec


def cmd_regrade(a):
    """Grade saved runs again (after a grader or judge change), from each run's reply, tool calls and workspace."""
    global STAGE
    outdir = WORK / "runs" / a.label
    STAGE = WORK / "plugin" / f"cases-{a.label}"
    recs = []
    for f in sorted(outdir.glob("*/run-*/result.json")):
        rec = json.loads(f.read_text())
        case_dir = STAGE / "evals" / rec["case"]
        if not case_dir.exists():
            case_dir = ROOT / "evals" / rec["case"]
        _, prompt, _ = case_meta(case_dir)
        full = json.loads((f.parent / "calls.json").read_text()) if (f.parent / "calls.json").exists() else rec["calls"]
        before = set(rec.get("before", []))
        rec["grades"], jc = grade(case_dir, prompt, rec["reply"], full, f.parent / "workspace", before)
        rec["score"] = sum(g["pass"] for g in rec["grades"]) / len(rec["grades"])
        rec["judgeCostUsd"] = round(jc, 4)
        f.write_text(json.dumps(rec, indent=1))
        recs.append(rec)
        print(f"{rec['case']:24} run {rec['run']}  score {rec['score']:.2f}", flush=True)
    old = json.loads((outdir / "summary.json").read_text())
    chosen = [pathlib.Path(n) for n in dict.fromkeys(r["case"] for r in recs)]

    class C:  # the spend is the original run's
        spent, cap, calls, tokens = old["costUsd"], 1e9, old["calls"], old["tokens"]
    a.model, a.runs, a.ref = old["model"], old["runsPerArm"], None if old["skillsRef"] == "working tree" else old["skillsRef"]
    s = summarise(recs, a, C, sum(r["judgeCostUsd"] for r in recs), old["durationSeconds"], chosen)
    s["regraded"] = datetime.date.today().isoformat()
    (outdir / "summary.json").write_text(json.dumps(s, indent=2))
    if a.save:
        name = f"{old['date']}-{a.label}.json"
        (OUT / name).write_text(json.dumps(s, indent=2) + "\n")
        print(f"saved {OUT.relative_to(ROOT) / name}")
    print(f"overall {s['overallScore']}")
    if a.compare:
        compare(s, json.loads(pathlib.Path(a.compare).read_text()))


def cmd_cases(a):
    cases, tags = ae.split(a.case), ae.split(a.tag)
    chosen = [d for d in ae.available() if ae.wanted(d, cases, tags)]
    if not chosen:
        sys.exit(f"no eval case matches --case {cases or 'any'} --tag {tags or 'any'}")
    if a.list:
        for d in chosen:
            print(f"{d.name:24} {', '.join(sorted(ae.case_tags(d)))}")
        return
    global STAGE
    stamp = a.label or datetime.datetime.now().strftime("%Y%m%d-%H%M")
    STAGE = ae.STAGE = WORK / "plugin" / f"cases-{stamp}"  # agent_evals.py's staging, in a folder of this run's own
    ae.stage(a.ref, cases, tags)
    outdir = WORK / "runs" / stamp
    client = Gemini(a.model, float(a.max_cost_usd), f"cases:{stamp}")
    recs, judge_total = [], 0.0
    t0 = time.time()
    for r in range(1, a.runs + 1):  # round by round, so a cost stop still leaves whole rounds
        for d in chosen:
            if client.spent >= client.cap:
                break
            done = outdir / d.name / f"run-{r}" / "result.json"
            if a.resume and done.exists():  # --resume keeps the runs a stopped invocation finished
                rec = json.loads(done.read_text())
            else:
                rec = run_case(client, STAGE / "evals" / d.name, r, outdir)
            recs.append(rec)
            judge_total += rec["judgeCostUsd"]
            fails = [g["grader"] for g in rec["grades"] if not g["pass"]]
            print(f"{d.name:24} run {r}  score {rec['score']:.2f}  {rec['stop']:10} ${rec['costUsd']:.2f}"
                  + (f"  failed: {', '.join(fails)}" if fails else ""), flush=True)
    s = summarise(recs, a, client, judge_total, time.time() - t0, chosen)
    (outdir / "summary.json").write_text(json.dumps(s, indent=2))
    print(f"overall {s['overallScore']}  Gemini ${s['costUsd']}  judge ${s['judgeCostUsd']}  {client.calls} calls  -> {outdir}")
    if a.save:
        OUT.mkdir(parents=True, exist_ok=True)
        name = f"{s['date']}-{a.label}.json" if a.label else f"{s['date']}-{a.model}.json"
        (OUT / name).write_text(json.dumps(s, indent=2) + "\n")
        print(f"saved {OUT.relative_to(ROOT) / name}")
    if a.compare:
        compare(s, json.loads(pathlib.Path(a.compare).read_text()))


def summarise(recs, a, client, judge_total, seconds, chosen):
    cases = []
    for d in chosen:
        rs = [r for r in recs if r["case"] == d.name]
        if not rs:
            continue
        per = {}
        for r in rs:
            for g in r["grades"]:
                per.setdefault(g["grader"], []).append(g["pass"])
        cases.append({"name": d.name, "score": round(sum(r["score"] for r in rs) / len(rs), 3), "runs": len(rs),
                      "runScores": [round(r["score"], 3) for r in rs],
                      "graders": {k: f"{sum(v)}/{len(v)}" for k, v in per.items()},
                      "stops": sorted({r["stop"] for r in rs}), "errors": [r["error"] for r in rs if r["error"]]})
    scores = [c["score"] for c in cases]
    return {"kind": "agent", "runner": "tools/gemini_evals.py", "date": datetime.date.today().isoformat(),
            "commit": subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip(),
            "skillsRef": a.ref or "working tree", "label": a.label, "model": a.model, "judgeModel": "haiku",
            "runsPerArm": a.runs, "arms": "with only", "overallScore": round(sum(scores) / len(scores), 3) if scores else None,
            "casesTotal": len(cases), "costUsd": round(client.spent, 2), "judgeCostUsd": round(judge_total, 2),
            "tokens": client.tokens, "calls": client.calls, "durationSeconds": round(seconds),
            "partial": client.spent >= client.cap, "cases": cases}


def compare(g, c):
    cc = {x["name"]: x for x in c.get("cases", [])}
    print(f"\n{'case':24} {'gemini':>7} {'claude':>7}   ({g['model']} vs {c.get('model')}, {g['runsPerArm']} and {c.get('runsPerArm')} runs)")
    for x in g["cases"]:
        y = cc.get(x["name"], {}).get("score")
        print(f"{x['name']:24} {x['score']:7.2f} {('%7.2f' % y) if isinstance(y, (int, float)) else '      -'}")
    print(f"{'overall':24} {g['overallScore']:7.2f} {c.get('overallScore') or 0:7.2f}")


# ---------------------------------------------------------------- drift: building on a finished system

TASKS = {
    "pricing": "Build our pricing page as pricing.html in this folder: three plans (Free, Team, Business) with monthly "
               "prices, what each includes, a comparison of features, an FAQ with four questions and a button to start "
               "each plan. Use our design system. Plain HTML and CSS, no build step.",
    "settings": "Build the account settings screen as settings.html in this folder: profile (name, email, photo), "
                "notifications (email and push toggles for five kinds of events), security (password change, two-factor "
                "on or off, active sessions with a sign-out button for each) and a danger zone to delete the account. "
                "Use our design system. Plain HTML and CSS, no build step.",
    "chat": "Build a chat view as chat.html in this folder: a list of conversations on the left with unread counts, the "
            "open conversation with messages from two people (one of them long, with a link and a code snippet), a "
            "typing indicator, and a message box with attach and send buttons at the bottom. Use our design system. "
            "Plain HTML and CSS, no build step.",
}


def run_claude(prompt, ws, stage, model, rd, followup):
    """The same build task in Claude Code (`claude -p` with the staged plugin, no user settings), for comparison."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_CODE_") and k != "CLAUDECODE"}
    env["GIT_CEILING_DIRECTORIES"] = str(rd)
    calls, reply, stop, cost, sid, msg = [], "", "", 0.0, None, prompt
    for turn in range(3):
        cmd = ["claude", "-p", "--model", model, "--plugin-dir", str(stage), "--setting-sources", "", "--strict-mcp-config",
               "--allowedTools", "Bash", "Read", "Write", "Edit", "Glob", "Grep", "Skill", "--disallowedTools", "WebFetch",
               "WebSearch", "AskUserQuestion", "--max-budget-usd", "4", "--output-format", "stream-json", "--verbose"]
        if sid:
            cmd += ["--resume", sid]
        p = subprocess.run(cmd, input=msg, capture_output=True, text=True, cwd=ws, env=env, timeout=1800)
        (rd / f"claude-{turn}.jsonl").write_text(p.stdout)
        for line in p.stdout.splitlines():
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "assistant":
                for part in ev.get("message", {}).get("content", []):
                    if part.get("type") == "tool_use":
                        calls.append({"tool": part["name"], "input": part.get("input", {}), "turn": turn, "output": ""})
            if ev.get("type") == "result":
                reply, stop, sid = ev.get("result", ""), ev.get("subtype", ""), ev.get("session_id")
                cost += ev.get("total_cost_usd", 0) or 0
        nxt = followup(reply)
        if not nxt or not sid:
            break
        calls.append({"tool": "(person replied)", "input": {"after": reply[:1500], "message": nxt}, "turn": turn, "output": ""})
        msg = nxt
    return reply, calls, stop, cost


OWNER_REPLY = ("No log and no hand-off for now, thanks. Please build it now. Wherever you would ask me something, use "
               "your recommended default and tell me afterwards what you assumed.")


def cmd_drift(a):
    ex = ROOT / "examples" / a.example
    if not (ex / "DESIGN.md").exists():
        sys.exit(f"no example at {ex}")
    global STAGE
    stamp = a.label or datetime.datetime.now().strftime("%Y%m%d-%H%M")
    STAGE = ae.STAGE = WORK / "plugin" / f"drift-{stamp}-{a.example}"
    ae.stage(None, ["__none__"], None)
    client = Gemini(a.model, float(a.max_cost_usd), f"drift:{stamp}")
    tasks = ae.split(a.task) or list(TASKS)
    for r in range(1, a.runs + 1):
        for t in tasks:
            rd = WORK / "drift" / stamp / a.example / f"{t}-{r}" if a.agent == "gemini" else WORK / "drift" / stamp / a.example / f"{t}-claude-{r}"
            if rd.exists():
                shutil.rmtree(rd)
            ws = rd / "workspace"
            ws.mkdir(parents=True)
            # The project as the example's README says a person has it: DESIGN.md and PRODUCT.md at the root, the rest in opendesigner/
            for f in ("DESIGN.md", "PRODUCT.md"):
                if (ex / f).exists():
                    shutil.copy(ex / f, ws / f)
            shutil.copytree(ex, ws / "opendesigner", ignore=shutil.ignore_patterns("DESIGN.md", "PRODUCT.md", "README.md", "*.png"))
            # An example's DESIGN.md names paths from inside the example folder (build/css/tokens.css). In a project they are
            # opendesigner/build/..., so write it again the way `engine.py build` writes it in a project.
            subprocess.run([sys.executable, "-B", str(STAGE / "skills/opendesigner/scripts/engine.py"), "design-md"], cwd=ws,
                           check=True, capture_output=True, env=os.environ | {"GIT_CEILING_DIRECTORIES": str(rd)})
            spent0 = client.spent
            target = ws / f"{t}.html"
            said = []

            def followup(reply, target=target, said=said):  # a person who wants the page and has no more to say
                if target.exists() or len(said) >= 2:
                    return None
                said.append(1)
                return OWNER_REPLY
            if a.agent == "claude":
                reply, calls, stop, cost = run_claude(TASKS[t], ws, STAGE, a.claude_model, rd, followup)
                client.spent += 0  # Claude usage is on the Claude account, reported apart
            else:
                reply, calls, stop = run_agent(client, TASKS[t], ws, [], STAGE, sorted(DECLS.keys() - {"AskUserQuestion"}),
                                               a.max_turns, 1800, transcript=rd / "transcript.json", followup=followup)
                cost = client.spent - spent0
            rec = {"example": a.example, "task": t, "run": r, "agent": a.agent, "stop": stop, "costUsd": round(cost, 4),
                   "toolCalls": len(calls), "reply": reply,
                   "calls": [{k: c[k] for k in ("tool", "input", "turn")} | {"output": c["output"][:600]} for c in calls]}
            (rd / "result.json").write_text(json.dumps(rec, indent=1))
            print(f"{a.example} {t} run {r}: {stop}, {len(calls)} tool calls, ${rec['costUsd']:.2f}", flush=True)
            if client.spent >= client.cap:
                break
    print(f"Gemini ${client.spent:.2f} in {client.calls} calls -> {WORK / 'drift' / stamp}")


# ---------------------------------------------------------------- drift: measuring what came back

HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
FUNC_COLOR = re.compile(r"\b(?:rgba?|hsla?|oklch|oklab|lab|lch)\([^)]*\)")
SPACE_PROP = re.compile(r"\b(margin|padding|gap|row-gap|column-gap|inset|top|right|bottom|left)(?:-[a-z]+)?\s*:\s*([^;}\"]+)")
PX = re.compile(r"(?<![\w.-])(-?\d+(?:\.\d+)?)px")
FONT_FAMILY = re.compile(r"font-family\s*:\s*([^;}\"]+)")
VAR = re.compile(r"var\(\s*(--[a-zA-Z0-9_-]+)")
BUTTON = re.compile(r"<(button|a)\b([^>]*)>(.*?)</\1>", re.S | re.I)


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def static_scan(ws):
    tokens_css = (ws / "opendesigner" / "build" / "css" / "tokens.css").read_text()
    defined = set(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", tokens_css))
    spaces = {float(v) for v in re.findall(r"--ds-space-[0-9]+:\s*(\d+(?:\.\d+)?)px", tokens_css)}
    files = [p for p in ws.rglob("*") if p.is_file() and p.suffix in {".html", ".css"} and "opendesigner" not in p.parts
             and ".home" not in p.parts]
    out = {"files": [str(p.relative_to(ws)) for p in files], "literalColors": [], "offScaleSpacing": [], "fontsOutsideTokens": [],
           "inventedTokens": [], "localTokens": [], "inlineStyles": 0, "copy": [], "tokenUses": 0, "tokensCssLinked": False}
    for p in files:
        s = p.read_text(errors="replace")
        rel = str(p.relative_to(ws))
        if p.suffix == ".html":
            out["tokensCssLinked"] |= "build/css/tokens.css" in s
            out["inlineStyles"] += len(re.findall(r"\sstyle=\"", s))
        # a literal colour that is not a var() fallback
        code = re.sub(r"var\([^()]*(?:\([^()]*\)[^()]*)*\)", "var()", s)
        code = re.sub(r"<!--.*?-->|/\*.*?\*/", "", code, flags=re.S)
        for m in HEX.finditer(code):
            if re.match(r"[0-9a-fA-F]{3,8}$", m.group(0)[1:]) and not re.search(r"(href|id|url)\s*=\s*[\"'][^\"']*$", code[max(0, m.start() - 80):m.start()]):
                out["literalColors"].append(f"{rel}: {m.group(0)}")
        out["literalColors"] += [f"{rel}: {m.group(0)}" for m in FUNC_COLOR.finditer(code) if "var(" not in m.group(0)]
        for prop, val in SPACE_PROP.findall(code):
            for v in PX.findall(val):
                f = abs(float(v))
                if f not in spaces and f > 2:
                    out["offScaleSpacing"].append(f"{rel}: {prop}: {v}px")
        for val in FONT_FAMILY.findall(code):
            if "var(--ds-font" not in val and val.strip() not in {"inherit", "var()"}:
                out["fontsOutsideTokens"].append(f"{rel}: {val.strip()[:80]}")
        uses = VAR.findall(s)
        out["tokenUses"] += sum(1 for u in uses if u.startswith("--ds-"))
        local = set(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", s))
        out["localTokens"] += sorted(f"{rel}: {n}" for n in local - defined)
        out["inventedTokens"] += sorted({f"{rel}: {u}" for u in uses if u not in defined and u not in local})
        if p.suffix == ".html":
            for tag, attrs, inner in BUTTON.findall(s):
                if tag.lower() == "a" and not re.search(r"class=\"[^\"]*(btn|button)", attrs):
                    continue
                text = strip_tags(inner)
                words = text.split()
                if not words:
                    continue
                why = []
                if len(words) > 4:
                    why.append("over four words")
                if len(words) > 1 and sum(w[:1].isupper() for w in words[1:]) >= max(1, len(words[1:]) // 2 + 1) and not text.isupper():
                    why.append("Title Case, not sentence case")
                if "!" in text:
                    why.append("exclamation mark")
                if re.search(r"\b(click here|submit|ok)\b", text, re.I) and len(words) <= 2:
                    why.append("does not say what it does")
                if why:
                    out["copy"].append(f"{rel}: \"{text[:60]}\" ({', '.join(why)})")
    return out


def browser_check(ws, outdir):
    """The review skill's probe in Chrome (capture.py), then review.py check against the tokens."""
    import http.server
    import socketserver
    import threading
    pages = [p for p in ws.glob("*.html")]
    if not pages:
        return {"error": "no page"}

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *x, **k):
            super().__init__(*x, directory=str(ws), **k)

        def log_message(self, *x):
            pass
    srv = socketserver.TCPServer(("127.0.0.1", 0), Quiet)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port = srv.server_address[1]
    review = ROOT / "skills" / "opendesigner-review" / "scripts"
    try:
        cap = subprocess.run([sys.executable, str(review / "capture.py"), "--url", f"http://127.0.0.1:{port}",
                              "--routes", ",".join("/" + p.name for p in pages), "--viewports", "390,1440",
                              "--themes", "light,dark", "--out", str(outdir), "--channel", "chrome", "--steps", "4"],
                             capture_output=True, text=True, timeout=900)
        chk = subprocess.run([sys.executable, str(review / "review.py"), "check", str(outdir), "--project", str(ws), "--json"],
                             capture_output=True, text=True, timeout=300)
    finally:
        srv.shutdown()
    try:
        found = json.loads(chk.stdout)
    except json.JSONDecodeError:
        return {"error": (cap.stderr or chk.stderr)[-800:]}
    return {"findings": [{k: x.get(k) for k in ("case", "severity", "title", "measured", "expected")} for x in found]}


def cmd_measure(a):
    base = WORK / "drift" / a.label
    rows = []
    for rd in sorted(base.glob("*/*-*")):
        ws = rd / "workspace"
        if not ws.exists():
            continue
        rec = json.loads((rd / "result.json").read_text()) if (rd / "result.json").exists() else {}
        eng = subprocess.run([sys.executable, "-B", str(ROOT / "skills/opendesigner/scripts/engine.py"), "--dir",
                              str(ws / "opendesigner"), "review", "--project", str(ws), "--json"], capture_output=True, text=True,
                             timeout=300, env=os.environ | {"GIT_CEILING_DIRECTORIES": str(rd)})
        try:
            e = json.loads(eng.stdout)
            engine = {k: e.get(k) for k in ("counts", "tokenUses", "tokens", "staleSections", "reasons", "ok", "broken", "untrue")}
            engine["findings"] = [f"{f.get('file')}:{f.get('line')} {f.get('value')}" for f in e.get("findings", [])][:80]
        except json.JSONDecodeError:
            engine = {"error": (eng.stderr or eng.stdout)[-500:]}
        row = {"run": str(rd.relative_to(base)), "stop": rec.get("stop"), "costUsd": rec.get("costUsd"),
               "toolCalls": rec.get("toolCalls"), "engineReview": engine, "static": static_scan(ws)}
        if not a.no_browser:
            row["browser"] = browser_check(ws, rd / "review")
        (rd / "measure.json").write_text(json.dumps(row, indent=1))
        rows.append(row)
        s, b = row["static"], row.get("browser", {})
        print(f"{row['run']:32} engine {engine.get('counts')} tokens:{engine.get('tokens')}  literal colours {len(s['literalColors'])}"
              f"  off-scale {len(s['offScaleSpacing'])}  fonts {len(s['fontsOutsideTokens'])}  invented {len(s['inventedTokens'])}"
              f"  copy {len(s['copy'])}  browser {len(b.get('findings', []))}", flush=True)
    (base / "measure.json").write_text(json.dumps(rows, indent=1))
    print(f"-> {base / 'measure.json'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd")
    rg = sub.add_parser("regrade", help="grade saved runs again (three judge votes), from their replies and workspaces")
    rg.add_argument("--label", required=True)
    rg.add_argument("--save", action="store_true")
    rg.add_argument("--compare")
    m = sub.add_parser("measure", help="measure the drift runs: engine.py review, a static scan, the review probe in Chrome")
    m.add_argument("--label", required=True)
    m.add_argument("--no-browser", action="store_true")
    for p in (ap, d := sub.add_parser("drift", help="build tasks on a finished example system")):
        p.add_argument("--model", default=DEFAULT_MODEL)
        p.add_argument("--max-cost-usd", default="20", help="stop before the next call once this much is spent (default 20)")
        p.add_argument("--label", help="a name for this run (its folder in dist/gemini and the saved file)")
        p.add_argument("--runs", type=int, default=3)
    ap.add_argument("--case", action="append")
    ap.add_argument("--tag", action="append")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--save", action="store_true", help="write the summary into evals/agent/results/")
    ap.add_argument("--resume", action="store_true", help="with --label: keep the runs already finished under that label")
    ap.add_argument("--ref", help="stage the skills from this git commit instead of the working tree")
    ap.add_argument("--compare", help="a Claude summary (evals/agent/results/*.json) to print beside the Gemini scores")
    d.add_argument("--example", default="devtool-dense")
    d.add_argument("--task", action="append", help=f"one of {', '.join(TASKS)} (default: all)")
    d.add_argument("--max-turns", type=int, default=60)
    d.add_argument("--agent", default="gemini", choices=["gemini", "claude"], help="claude: the same tasks in Claude Code")
    d.add_argument("--claude-model", default="sonnet")
    a = ap.parse_args()
    {"drift": cmd_drift, "measure": cmd_measure, "regrade": cmd_regrade}.get(a.cmd, cmd_cases)(a)


if __name__ == "__main__":
    main()
