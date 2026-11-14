#!/usr/bin/env python3
"""Smart UI, live: a real model answers, and the answer is checked, repaired once and drawn in the person's system.

One turn:  message -> route (the model may call the app's READ actions only) -> run them -> select parts -> answer
           -> validate against the data the model was given -> one repair round with the errors -> or text only.
A press:   a button the person pressed comes back here. A change (book, pay, cancel) runs only when the renderer's
           approval prompt said yes (approved: true, set by <od-surface>, never by the model); then the model reports the
           result. Anything else becomes the next user turn ("I picked the Standard fare").

Providers (picked in this order unless --provider says otherwise; keys are read from the environment or .env, sent only
in request headers, never printed or logged):
  anthropic    ANTHROPIC_API_KEY, the Messages API
  claude-cli   the `claude` command on this computer (your own Claude Code login), when there is no API key
  gemini       GEMINI_API_KEY, generateContent
  recorded     no model: the app's recorded answers, when it has them

  python3 live.py serve --app examples/smart-ui-support/server.py [--port 8000] [--provider gemini]
      loopback only; serves the app's web/ folder, POST /api/chat and POST /api/press
The app module defines NAME, CATALOG (a path), TOKENS (a path), WEB (a folder) and ACTIONS:
  {name: {"description": str, "params": {name: description}, "changes": bool, "fn": callable(**args) -> JSON}}
Standard library only.
"""
import argparse
import importlib.util
import inspect
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smartui  # noqa: E402

# Fast models by default (a turn should feel instant); a stronger one is a setting: OD_GEMINI_MODEL=gemini-3.1-pro-preview,
# gemini-4-argon or gemini-4-hydrogen; OD_CLAUDE_MODEL=claude-sonnet-5-5. OD_THINKING: none (default for flash and lite
# models), low (default for the others) or high (the model's own).
CLAUDE = os.environ.get("OD_CLAUDE_MODEL") or "claude-haiku-5-5"
MODELS = {"anthropic": CLAUDE, "claude-cli": CLAUDE, "gemini": os.environ.get("OD_GEMINI_MODEL") or "gemini-3.8-flash"}
THINKING = os.environ.get("OD_THINKING") or ("none" if re.search(r"flash|lite|haiku", MODELS["gemini"]) else "low")
_NO_THINKING, _SCHEMA_OK, _TOO_BIG = set(), {}, {}  # models that refused a thinking setting; (model, schema) -> the form that was accepted  # models that refused a thinking setting; schemas a provider called too complex
USAGE = {}  # model -> tokens used in this process: {"calls", "input", "output"} (output includes thinking)


def _count(model, inp, out):
    u = USAGE.setdefault(model, {"calls": 0, "input": 0, "output": 0})
    u["calls"] += 1
    u["input"] += inp or 0
    u["output"] += out or 0


# ----------------------------------------------------------------------------------------------- keys and providers

def env_key(name, start=None):
    """A key from the environment, else the nearest .env up from start, else the main checkout's .env. Never printed."""
    if os.environ.get(name):
        return os.environ[name]
    roots = []
    d = pathlib.Path(start or os.getcwd()).resolve()
    roots += [d, *d.parents]
    try:
        common = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=d, capture_output=True, text=True).stdout.strip()
        if common:
            roots.append((d / common).resolve().parent)
    except OSError:
        pass
    for r in roots:
        f = r / ".env"
        if f.is_file():
            for line in f.read_text().splitlines():
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'") or None
    return None


def available():
    out = []
    if env_key("ANTHROPIC_API_KEY"):
        out.append("anthropic")
    if shutil.which("claude"):
        out.append("claude-cli")
    if env_key("GEMINI_API_KEY"):
        out.append("gemini")
    return out + ["recorded"]


def ask(provider, system, turns, schema=None, on_text=None):
    """turns: [{"role": "user"|"assistant", "text": ...}]. Returns the model's text (JSON text when schema is given).
    schema: a JSON Schema the reply must follow (constrained decoding where the provider has it).
    on_text: called with the reply so far while it streams (Gemini); otherwise once at the end.
    A list of schemas means: the first, or the next when a provider finds one too complex (Gemini)."""
    if isinstance(schema, list) and provider != "gemini":
        schema = schema[0]
    if provider == "anthropic":
        body = {"model": MODELS["anthropic"], "max_tokens": 600 if schema and "calls" in schema.get("properties", {}) else 3000, "system": system,
                "messages": [{"role": t["role"], "content": t["text"]} for t in turns]}
        if schema:  # a forced tool call: its input follows the schema
            body["tools"] = [{"name": "answer", "description": "Your answer", "input_schema": schema}]
            body["tool_choice"] = {"type": "tool", "name": "answer"}
        res = _post("https://api.anthropic.com/v1/messages", body,
                    {"x-api-key": env_key("ANTHROPIC_API_KEY"), "anthropic-version": "2023-06-01"})
        u = res.get("usage", {})
        _count(MODELS["anthropic"], u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0), u.get("output_tokens", 0))
        if schema:
            out = next((json.dumps(b.get("input")) for b in res.get("content", []) if b.get("type") == "tool_use"), "")
        else:
            out = "".join(b.get("text", "") for b in res.get("content", []) if b.get("type") == "text")
        if on_text:
            on_text(out)
        return out
    if provider == "gemini":
        model = MODELS["gemini"]
        options = schema if isinstance(schema, list) else [schema] if schema else [None]
        route = bool(options[0]) and "calls" in options[0].get("properties", {})
        key = (model, json.dumps(options[0], sort_keys=True)) if options[0] else None
        # providers refuse a schema whose combined bounds are too complex: try the chosen parts, then fewer parts, then
        # plain JSON {text, part} (the validator checks the part either way); remember what worked
        tries = options + ([_loose(options[0])] if options[0] and not route else [])
        start = _SCHEMA_OK.get(key, 0)
        for attempt in range(2):
            thinking = THINKING != "high" and model not in _NO_THINKING
            for i in range(start, len(tries)):
                size = len(json.dumps(tries[i])) if tries[i] else 0
                if size >= _TOO_BIG.get(model, 10 ** 9) and i < len(tries) - 1:
                    continue  # this model refused a schema this large before: skip to a smaller form without asking
                body = {"systemInstruction": {"parts": [{"text": system}]},
                        "contents": [{"role": "model" if t["role"] == "assistant" else "user", "parts": [{"text": t["text"]}]} for t in turns],
                        "generationConfig": {"maxOutputTokens": (600 if route else 3000) + (8000 if thinking and THINKING == "low" else 0)}}
                if thinking:
                    body["generationConfig"]["thinkingConfig"] = {"thinkingLevel": "low"} if THINKING == "low" else {"thinkingBudget": 0}
                if tries[i]:
                    body["generationConfig"]["responseMimeType"] = "application/json"
                    body["generationConfig"]["responseJsonSchema"] = tries[i]
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent?alt=sse"
                try:
                    out = _gemini_stream(url, body, model, on_text)
                    if key:
                        _SCHEMA_OK[key] = i
                    return out
                except RuntimeError as e:
                    if "HTTP 400" not in str(e):
                        raise
                    if "thinking" in str(e).lower() and thinking:
                        break  # this model takes no such thinking setting: start over without one
                    if size:
                        _TOO_BIG[model] = min(size, _TOO_BIG.get(model, 10 ** 9))
            if not thinking:
                raise RuntimeError(f"{model} refused every form of this request (HTTP 400)")
            _NO_THINKING.add(model)  # a generic refusal of every form: some models take no thinking setting at all
            _TOO_BIG.pop(model, None)  # those refusals may have been about thinking, not size
            start = 0
    if provider == "claude-cli":
        convo = "\n\n".join(f"{'Person' if t['role'] == 'user' else 'You (earlier)'}: {t['text']}" for t in turns[:-1])
        msg = (f"Conversation so far:\n{convo}\n\nPerson now: {turns[-1]['text']}" if convo else turns[-1]["text"])
        cmd = ["claude", "-p", "--model", MODELS["claude-cli"], "--system-prompt", system, "--tools", "",
               "--setting-sources", "", "--output-format", "json"]
        if schema:
            cmd += ["--json-schema", json.dumps(schema)]
        r = subprocess.run(cmd + [msg], capture_output=True, text=True, cwd="/tmp", timeout=600)
        try:
            out = json.loads(r.stdout)
        except ValueError:
            raise RuntimeError("claude -p failed: " + (r.stderr or r.stdout)[:200])
        u = out.get("usage") or {}
        _count(MODELS["claude-cli"], u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0), u.get("output_tokens", 0))
        so = out.get("structured_output")
        text = json.dumps(so) if (schema and so is not None) else (out.get("result") or "")
        if on_text:
            on_text(text)
        return text
    raise RuntimeError(f"unknown provider {provider}")


def _loose(schema):
    """The same reply shape without the parts' own schemas: JSON {text, part}, the part checked by the validator."""
    names = list(((schema or {}).get("properties", {}).get("part") or {}).get("properties", {}))
    return {"type": "object", "required": ["text", "part"], "properties": {"text": {"type": "string"}, "part": {
        "type": ["object", "null"], "properties": {n: {"type": "object"} for n in names}, "additionalProperties": False}}}


def _gemini_stream(url, body, model, on_text):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"content-type": "application/json", "x-goog-api-key": env_key("GEMINI_API_KEY")})
    wait, text, usage = 2, "", {}
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                for raw in r:
                    line = raw.decode("utf-8", "replace").strip()
                    if not line.startswith("data:"):
                        continue
                    d = json.loads(line[5:])
                    usage = d.get("usageMetadata") or usage
                    for part in ((d.get("candidates") or [{}])[0].get("content") or {}).get("parts", []):
                        if part.get("text") and not part.get("thought"):
                            text += part["text"]
                            if on_text:
                                on_text(text)
            break
        except (TimeoutError, urllib.error.URLError) as e:
            if isinstance(e, urllib.error.HTTPError):
                pass
            elif attempt < 2 and not text:
                time.sleep(wait)
                continue
            else:
                raise RuntimeError("generativelanguage.googleapis.com did not answer in time") from None
            if e.code in (429, 500, 502, 503, 504) and attempt < 5 and not text:
                time.sleep(wait)
                wait = min(wait * 2, 30)
                continue
            detail = ""
            try:
                detail = json.loads(e.read()).get("error", {}).get("message", "")[:200]  # the provider's message, never the request
            except Exception:
                pass
            raise RuntimeError(f"generativelanguage.googleapis.com returned HTTP {e.code}: {detail}") from None
    _count(model, usage.get("promptTokenCount", 0), usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0))
    return text


def _post(url, body, headers):
    wait = 5
    for attempt in range(6):
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"content-type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504, 529) and attempt < 5:
                time.sleep(wait)
                wait = min(wait * 2, 60)
                continue
            raise RuntimeError(f"{url.split('/')[2]} returned HTTP {e.code}") from None  # never echo the request: it holds the key


# ----------------------------------------------------------------------------------------------- the app

def load_app(path):
    spec = importlib.util.spec_from_file_location("od_app", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _overlap(a, b, n=4):
    """Words of a found in b; a word also matches a longer one it starts (renew, renewal) when it has n letters or more."""
    return sum(1 for w in a if w in b or (len(w) >= n and any(x.startswith(w) or (len(x) >= n and w.startswith(x)) for x in b)))


def _fits(value, desc):
    """An id fills a parameter only if it has the shape of the description's example (FH40018273, not AB12 from AB12 CDE)."""
    m = re.search(r"\bsuch as ([A-Z0-9][A-Z0-9-]{2,})", desc or "")
    shape = lambda t: re.sub(r"\d", "9", re.sub(r"[A-Z]", "A", t))  # per character: AB12 is not FH40018273
    return not m or shape(value) == shape(m.group(1))


def _choices(desc):
    """The values a parameter's description lists: "resident or visitor", "hollow-lane, marsh-road or eastgate"."""
    head = re.split(r"\(|;|\bsuch as\b|\bfor example\b", desc or "")[0]
    opts = [o.strip(" .") for o in re.split(r",\s*|\s+or\s+", head)]
    return [o for o in opts if o and len(o.split()) <= 3 and len(opts) > 1] if " or " in head else []


def actions_text(actions, changes):
    return "\n".join(f"- {n}({', '.join(f'{k}: {v}' for k, v in a.get('params', {}).items())}): {a['description']}"
                      + (f" Its approval prompt must say, word for word: {' '.join(a['consequences'])}" if a.get("consequences") else "")
                      for n, a in actions.items() if bool(a.get("changes")) == changes) or "- none"


ROUTE = """You decide which of this app's read-only actions to call to answer the person's latest message.
Read actions (you may call these):
{reads}
Actions that change data (you may NOT call these; they become buttons the person presses):
{changes}

Reply with JSON only: {{"calls": [{{"action": "<name>", "args": {{...}}}}]}}. Use the conversation to fill arguments
(for example the flight they just looked at). Call nothing for small talk or when the data you already have answers it:
{{"calls": []}}. At most 3 calls."""


class Conversation:
    """One person's chat: the turns so far, and every piece of data the app returned (what later answers may use)."""

    def __init__(self, app, provider, catalog=None):
        self.app, self.provider = app, provider
        self.catalog = catalog or json.loads(pathlib.Path(app.CATALOG).read_text())
        sp = pathlib.Path(app.CATALOG).parent / "scope.json"
        self.scope = json.loads(sp.read_text()) if sp.exists() else None
        # action name -> the parts the scope step mapped to its route (GET /api/usage -> LineChart, BarChart)
        self.route_parts, self.route_words = {}, {}
        for name, a in app.ACTIONS.items():
            for it in (self.scope or {}).get("intents", []):
                if a.get("path") and it.get("from", "").startswith(f"{a.get('method', 'GET')} {a['path']} "):
                    self.route_parts[name] = it.get("components", [])
                    self.route_words[name] = [smartui.words(ph) for ph in it.get("phrases", []) if smartui.words(ph)]
        self.turns = []        # [{"role", "text"}] as the model sees them
        self.data = {}         # action name -> its latest result
        self.surfaces = 0
        self.log = []          # per turn: calls, first errors, repaired, ui
        self.offered = []      # the changes an answer offered as buttons: (name, context); a press must match one (R3)
        self.case_fixed, self.first_case_errors, self.routed_by_model, self.last_calls = 0, [], False, []

    # -- routing: which read actions to run
    def fast_route(self, message):
        """Which read actions to run, without a model: the message's words against each action's name, description,
        parameters and the phrases the scope step tied to its route; an id in the message (TH-1047) or one of a
        parameter's listed choices ("Hollow Lane", "visitor") fills a parameter. Returns (calls, sure). Not sure when
        nothing clearly matches before any data was fetched, or when the best match needs a value the message doesn't
        give ("the refunded one"): then a model routes."""
        # words that say nothing about which data ("did I get", "do I need") don't count as a match
        msg = set(smartui.words(message)) - {"get", "got", "did", "need", "have", "has", "want", "know", "see", "tell"}
        ids = re.findall(r"\b[A-Z]{1,5}[- ]?\d{2,}[A-Z0-9]*\b", message)
        negated = bool(re.search(r"\b(not|no|never|without)\b|n't\b|\bun[a-z]+", message.lower()))
        verbs = {"get", "list", "check", "find", "fetch", "read", "show", "view", "load"}

        def picks(desc):  # the parameter choices this message names; none when it says "not" (haven't paid != paid)
            if negated:
                return []
            return [o for o in _choices(desc) if o.lower() not in {"all", "any", "none", "both", "default"}
                    and set(smartui.words(o.replace("-", " "))) <= msg and smartui.words(o.replace("-", " "))]
        # a change the message names ("book an appointment") points at the reads that share its values (office, slot)
        wanted = {k for a in self.app.ACTIONS.values() if a.get("changes")
                  if set(smartui.words(a["fn"].__name__.replace("_", " "))) - verbs <= msg for k in a.get("params", {})}
        scored = []
        for name, a in self.app.ACTIONS.items():
            if a.get("changes"):
                continue
            own = set(smartui.words(name.replace("_", " "))) - verbs
            doc = set(smartui.words(a.get("description", ""))) | {w for k in a.get("params", {}) for w in smartui.words(k.replace("_", " "))}
            sc = 2 * _overlap(msg, own) + _overlap(msg, doc) + sum(3 if len(ws) > 1 else 1 for ws in self.route_words.get(name, []) if set(ws) <= msg)
            sc += sum(2 for desc in a.get("params", {}).values() if picks(desc))
            hint = 3 if wanted & set(a.get("params", {})) else 0
            if sc + hint:
                scored.append((sc + hint, hint, name))
        scored.sort(reverse=True)
        top = scored[0][0] if scored else 0
        if not scored or top < 2 and (top < 1 or len([x for x in scored if x[0] == top]) > 1):
            return [], bool(self.data) or not msg  # a follow-up or small talk answers from what is already here
        calls = []
        for i, (sc, _, name) in enumerate(scored[:3]):
            if sc < max(1, 0.5 * top):
                break
            a = self.app.ACTIONS[name]
            sig = inspect.signature(a["fn"]).parameters
            args = {k: picks(desc)[0] for k, desc in a.get("params", {}).items() if k in sig and picks(desc)}
            for k, v in sig.items():
                if v.default is inspect.Parameter.empty and k not in args and len(ids) == 1 and _fits(ids[0], a.get("params", {}).get(k, "")):
                    args[k] = ids[0]
            if any(v.default is inspect.Parameter.empty and k not in args for k, v in sig.items()):
                points_back = re.search(r"\b(the \w+ one|that one|this one|it|them|those)\b", message.lower())
                mine = set(smartui.words(name.replace("_", " "))) - verbs
                # "show me my parking fine": get_fine needs a reference, list_fines (the same thing, no value needed) answers it
                sibling = next((n2 for _, _, n2 in scored if n2 != name and _overlap(mine, set(smartui.words(n2.replace("_", " "))) - verbs, 3)
                                and not any(v.default is inspect.Parameter.empty for v in inspect.signature(self.app.ACTIONS[n2]["fn"]).parameters.values())), None)
                if i == 0 and (points_back or not sibling):
                    return [], False  # the best match needs a value the message doesn't give ("the refunded one")
                if i == 0 and sibling not in [c[0] for c in calls]:
                    calls.append((sibling, {}))
                continue
            calls.append((name, args))
        calls = [c for i, c in enumerate(calls) if c[0] not in [x[0] for x in calls[:i]]]
        return calls[:2], bool(calls)

    CHANGE_WORDS = re.compile(r"\b(pay|book|renew|switch|move|upgrade|downgrade|add|remove|cancel|upload|send|change|confirm|apply)\b", re.I)

    def names_a_change(self, message):
        """The person asks for something that changes data: a change action's own words, or a plain verb for one."""
        if re.match(r"\s*(do|does|did|is|are|was|were|have|has|what|which|when|where|why|how|any)\b", message.lower()):
            return False  # "do I need to pay a fine?" is a question; "pay it", "can I pay now?" ask for the change
        msg = set(smartui.words(message))
        verbs = {"get", "list", "check", "find", "fetch", "read", "show", "view", "load"}
        return bool(self.CHANGE_WORDS.search(message)) or any(
            (set(smartui.words(a["fn"].__name__.replace("_", " "))) - verbs) <= msg for a in self.app.ACTIONS.values() if a.get("changes"))

    def route(self, message):
        if self.provider == "recorded":
            return []
        calls, sure = self.fast_route(message)
        if sure:
            return calls
        self.routed_by_model = True
        system = ROUTE.format(reads=actions_text(self.app.ACTIONS, False), changes=actions_text(self.app.ACTIONS, True))
        schema = {"type": "object", "required": ["calls"], "properties": {"calls": {"type": "array", "items": {
            "type": "object", "required": ["action"], "properties": {"action": {"type": "string"}, "args": {"type": "object"}}}}}}
        raw = ask(self.provider, system, self.turns[-4:] + [{"role": "user", "text": message}], schema)
        m = re.search(r"\{.*\}", raw, re.S)
        try:
            calls = json.loads(m.group(0)).get("calls", []) if m else []
        except ValueError:
            calls = []
        ok = []
        for c in calls[:3]:
            a = self.app.ACTIONS.get(c.get("action"))
            if not a or a.get("changes"):
                continue  # R3: the model never runs a change; unknown names are ignored
            args = {k: v for k, v in (c.get("args") or {}).items() if k in a.get("params", {}) and isinstance(v, (str, int, float, bool))}
            ok.append((c["action"], args))
        return ok

    def run(self, calls):
        out = {}
        for name, args in calls:
            try:
                out[name] = self.app.ACTIONS[name]["fn"](**args)
            except Exception as e:  # an action's own failure is data too: the answer can show it (ErrorRetry)
                out[name] = {"error": {"message": str(e)[:200]}}
            self.data[name] = out[name]
        return out

    # -- one turn
    def answer(self, message, max_parts=None, on_event=None):
        """One turn. on_event gets {"type": "skeleton", "part"} as soon as a part is chosen (before any model call when
        routing needed none), {"type": "text", "text"} as the answer's words stream in, and the timings land in the log."""
        if self.provider == "recorded":
            return self._recorded(message)
        t0 = time.perf_counter()
        ms = {}
        emit = on_event or (lambda e: None)
        self.routed_by_model = False
        calls = self.route(message)
        fresh = self.run(calls)
        data = {**self.data, **fresh}
        surface = f"s{self.surfaces + 1}"
        history = "\n".join(f"{'Person' if t['role'] == 'user' else 'You'}: {t['text'][:400]}" for t in self.turns[-6:])
        boost = {}
        for name, _ in calls or self.last_calls:  # the parts this repo's scope tied to the actions run (a follow-up: last turn's)
            for i, part in enumerate(self.route_parts.get(name, [])):
                boost[part] = boost.get(part, 0) + (3 if i == 0 else 2) - (0 if calls or len(smartui.words(message)) >= 2 else 2)
        if calls:
            self.last_calls = calls
        if "ApprovalPrompt" in self.catalog["components"] and self.names_a_change(message):
            boost["ApprovalPrompt"] = boost.get("ApprovalPrompt", 0) + 4  # "pay the smaller one", "add 3 seats": ask first
        said = " ".join([t["text"] for t in self.turns if t["role"] == "user"] + [message])
        source = {**data, "_the_person_said": said}  # numbers the person typed count as given (R6)
        # the approval prompt is offered when the person asks for a change ("pay the smaller one"), not on every turn: a
        # bigger schema is slower, and a small model mixes its buttons into other parts
        always = ["ApprovalPrompt"] if any(a.get("changes") for a in self.app.ACTIONS.values()) and self.names_a_change(message) else []
        sel = smartui.select(message, self.catalog, 3, self.scope, data, boost)
        if not self.names_a_change(message):  # a question never gets an approval prompt (R3): the record answers it
            sel["candidates"] = [c for c in sel["candidates"] if c != "ApprovalPrompt"]
            sel["ui"] = sel["ui"] and bool(sel["candidates"])
        view = None if self.names_a_change(message) else self._view(calls, fresh, source, surface)
        if view:  # the app builds this part from its data: shown now, checked; the model writes only the sentence
            ms["skeleton"] = (time.perf_counter() - t0) * 1000
            emit({"type": "part", "answer": view, "data": data})
            sel = {"ui": False, "candidates": [], "scores": {}, "why": "the app's own view of the data"}
        elif sel["ui"] and sel["candidates"]:
            ms["skeleton"] = (time.perf_counter() - t0) * 1000
            emit({"type": "skeleton", "part": sel["candidates"][0]})
        system, sel = smartui.build_prompt(message, self.catalog, 3, self.scope, data, boost, always, structured=True, sel=sel)
        if view:
            system += ("\n\nThe person already sees this part, built by the app from the data:\n"
                       + json.dumps(view[0]["createSurface"]["components"][0], ensure_ascii=False)
                       + "\nWrite only the text: one or two plain sentences with what matters most (for a fine: the amount to pay "
                         "now and the day that ends). Don't list every detail and don't add a part.")
        names = (list(sel["candidates"]) + [a for a in always if a not in sel["candidates"] and a in self.catalog["components"]]) if sel["ui"] else []
        smaller = [names, names[:2] + [a for a in always if a in names[2:]], names[:1] + [a for a in always if a in names[1:]]]
        schema = [smartui.response_schema(self.catalog, n) for i, n in enumerate(smaller) if n and n not in smaller[:i]] \
            or smartui.response_schema(self.catalog, [])
        shown = [""]

        def on_text(raw):
            m = re.match(r'\s*\{\s*"text"\s*:\s*"((?:[^"\\]|\\.)*)', raw)
            if not m:
                return
            try:
                t = json.loads('"' + m.group(1).rstrip("\\") + '"')
            except ValueError:
                return
            if t and t != shown[0]:
                if "first_text" not in ms:
                    ms["first_text"] = (time.perf_counter() - t0) * 1000
                    ms.setdefault("skeleton", ms["first_text"])
                shown[0] = t
                emit({"type": "text", "text": t})
        if history:
            system += "\n\nThe conversation so far (for follow-up questions):\n" + history
        asks = self.names_a_change(message)
        system += ("\n\nActions that change data are buttons only. "
                   + ("The person asks for a change: show an ApprovalPrompt whose approve button carries the action as its event name, "
                      "with the details from the data (the amount, and any deadline such as the day a discount ends); never say it is done."
                      if asks else
                      "The person asked a question, not for a change: answer it and show the record. Never show an ApprovalPrompt "
                      "for a question. When one record matters most (the one unpaid fine), show it in full as key facts: every detail "
                      "the data gives, such as the amounts and the dates a price or a right ends. When it has a next step that changes "
                      "data (pay, renew, book), make that the part's action button, with the change's name as the event name and its "
                      "arguments in the context; pressing it only asks for the change."))
        if sel["ui"]:
            system += ("\nChange actions: use the exact name as the approve button's event name, and put every argument in "
                       "its event context, filled from the data (for example {\"name\": \"pay_invoice\", \"context\": {\"number\": \"TH-1047\"}}):\n"
                       + actions_text(self.app.ACTIONS, True))
        turns = self.turns[-4:] + [{"role": "user", "text": message}]
        reply = self._structured(ask(self.provider, system, turns, schema, on_text))
        self.first_case_errors = []
        result = self._check(reply, source, surface, max_parts)
        first_errors = self.first_case_errors + result["errors"]  # what the model's first answer got wrong, fixed here or not
        case_fixed = self.case_fixed
        repaired = False
        if result["errors"]:
            fix = ("Your answer was not shown: it failed these checks. Send the corrected text and part, or text only.\n"
                   + "\n".join(f"- {e['rule']} at {e['path']}: {e['message']}" + (f" ({e['fix']})" if e.get("fix") else "") for e in result["errors"][:10]))
            reply = self._structured(ask(self.provider, system, turns + [{"role": "assistant", "text": reply}, {"role": "user", "text": fix}], schema))
            result = self._check(reply, source, surface, max_parts)
            repaired = True
            if result["errors"] and all(e["rule"] in smartui.COPY_RULES for e in result["errors"]) and result.get("draft"):
                result["answer"] = result["draft"]  # only wording is left after the repair: show it, log what's left
            elif result["errors"] and not all(e["rule"] in smartui.COPY_RULES for e in result["errors"]):
                result["answer"] = None  # still wrong after one repair: text only
        if view:
            result.update(answer=view, part=view[0]["createSurface"]["components"][0].get("component"))
        text = result["text"] or "Sorry, I couldn't show that. Here is what I found: " + json.dumps(fresh)[:300]
        self.turns += [{"role": "user", "text": message},
                       {"role": "assistant", "text": text + (f" [showed {result['part']}]" if result["answer"] else "")}]
        if result["answer"]:
            self.surfaces += 1
            self._remember_offers(result["answer"])
        ms["full"] = (time.perf_counter() - t0) * 1000
        ms.setdefault("skeleton", ms["full"])
        ms.setdefault("first_text", ms["full"])
        entry = {"message": message, "calls": calls, "routed_by_model": self.routed_by_model, "ms": {k: round(v) for k, v in ms.items()},
                 "view": bool(view),
                 "case_fixed": case_fixed, "selector": sel["candidates"], "ui": bool(result["answer"]),
                 "part": result["part"], "first_errors": [f"{e['rule']} {e['path']}" for e in first_errors], "repaired": repaired,
                 "final_errors": [f"{e['rule']} {e['path']}" for e in result["errors"]]}
        self.log.append(entry)
        return {"text": text, "answer": result["answer"], "data": data, "log": entry}

    def _view(self, calls, fresh, source, surface):
        """The part an action's own view builds from its data (the app's @shows), when it passes every check; else None."""
        for name, _ in calls:
            make = self.app.ACTIONS.get(name, {}).get("view")
            if not make or name not in fresh:
                continue
            try:
                part = make(fresh[name])
            except Exception:
                continue
            if part:
                msgs = smartui.wrap(part, surface)
                if smartui.validate(msgs, self.catalog, {"source": source, "copy": True})["ok"]:
                    return msgs
        return None

    @staticmethod
    def _structured(raw):
        """A structured reply {"text", "part"} in the form _check reads: the text, then the part in an a2ui block."""
        try:
            obj = json.loads(raw)
        except ValueError:
            return raw  # not JSON after all: read it as free text
        if not isinstance(obj, dict) or "text" not in obj:
            return raw
        text = str(obj.get("text") or "")
        part = obj.get("part")
        if isinstance(part, dict) and "component" not in part and len(part) == 1 and isinstance(next(iter(part.values())), dict):
            name, props = next(iter(part.items()))  # {"KeyFacts": {...}} -> {"component": "KeyFacts", ...}
            part = {"component": name, **props}
        return text + (f"\n```a2ui\n{json.dumps(part, ensure_ascii=False)}\n```" if isinstance(part, dict) and part else "")

    def _check(self, reply, data, surface, max_parts):
        ans = smartui.extract_answer(reply)
        text = re.sub(r"```a2ui.*?```", "", reply, flags=re.S).strip()
        said = []  # the reply's own words follow the house voice too (copy rules)
        m = smartui.BANNED_WORDS.search(text)
        if m:
            said.append({"code": "VALIDATION_FAILED", "rule": "copy-word", "path": "text", "surfaceId": surface,
                         "message": f"'{m.group(0)}' in your text reads as filler", "fix": f"say it plainly without '{m.group(0)}'"})
        if ans is None:
            return {"text": text, "answer": None, "errors": said, "part": None, "draft": None}
        if isinstance(ans, dict) and "__parse_error__" in ans:
            return {"text": text, "answer": None, "part": None,
                    "errors": [{"rule": "json", "path": "", "message": "the a2ui block is not valid JSON: " + ans["__parse_error__"][:120]}]}
        msgs = smartui.normalize(ans) or []
        for m in msgs:  # each answer gets its own surface id, so the page can keep earlier ones
            for k in ("createSurface", "updateComponents", "updateDataModel", "deleteSurface"):
                if isinstance(m, dict) and isinstance(m.get(k), dict):
                    m[k]["surfaceId"] = surface
        opts = {"source": data, "limits": {"leaves": max_parts}, "copy": True,
                "consequences": {n: a["consequences"] for n, a in self.app.ACTIONS.items() if a.get("changes") and a.get("consequences")}}
        r = smartui.validate(msgs, self.catalog, opts)
        self.case_fixed = 0
        if r["errors"] and any(e["rule"] == "copy-case" for e in r["errors"]):
            # Title Case is fixed here, not by another model call: names the data or the person used keep their capitals
            fixed = smartui.fix_case(msgs, r["errors"], smartui.names_in(data))
            if fixed:
                self.first_case_errors = [e for e in r["errors"] if e["rule"] == "copy-case"]
                r = smartui.validate(msgs, self.catalog, opts)
                self.case_fixed = fixed
        part = next((c.get("component") for m in msgs for c in (m.get("createSurface") or {}).get("components", []) if c.get("id") == "root"), None)
        # copy rules (sentence case, plain words, one row per value) are repair errors; "draft" keeps an answer whose only
        # problems are those, for after the repair round
        errors = r["errors"] + said
        only_copy = bool(errors) and all(e["rule"] in smartui.COPY_RULES for e in errors)
        return {"text": text, "answer": msgs if not errors else None, "errors": errors, "part": part,
                "draft": msgs if only_copy else None}

    def _remember_offers(self, answer):
        def walk(v):
            if isinstance(v, dict):
                ev = v.get("event")
                if isinstance(ev, dict) and self.app.ACTIONS.get(ev.get("name"), {}).get("changes"):
                    self.offered.append((ev["name"], json.dumps(ev.get("context") or {}, sort_keys=True)))
                for x in v.values():
                    walk(x)
            elif isinstance(v, list):
                for x in v:
                    walk(x)
        walk(answer)

    # -- a button the person pressed
    def press(self, action, on_event=None):
        name, ctx = action.get("name"), dict(action.get("context") or {})
        a = self.app.ACTIONS.get(name)
        if a and a.get("changes"):
            approved = ctx.pop("approved", None) is True
            offer = (name, json.dumps(ctx, sort_keys=True))
            if not approved:
                # a "Pay this fine" button on a record: a request for the change, answered with its approval prompt
                said = ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in ctx.items())
                return self.answer(f"I want to {name.replace('_', ' ')}" + (f": {said}" if said else "") + ".", on_event=on_event)
            if not approved or offer not in self.offered:  # only a change this conversation showed, after the prompt said yes
                return {"text": "That needs your confirmation first.", "answer": None, "log": {"refused": name}}
            self.offered.remove(offer)
            args = {k: v for k, v in ctx.items() if k in a.get("params", {})}
            try:
                result = a["fn"](**args)
            except Exception as e:
                result = {"error": {"message": str(e)[:200]}}
            self.data[name] = result
            return self.answer(f"(I confirmed {name.replace('_', ' ')}. The app returned the result; tell me what happened.)", on_event=on_event)
        # not a change: what the person picked becomes their next message
        said = ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in ctx.items())
        return self.answer(f"I picked {name.replace('_', ' ')}" + (f": {said}" if said else "") + ".", on_event=on_event)

    def _recorded(self, message):
        rec = getattr(self.app, "RECORDED", None)
        if rec is None:
            f = pathlib.Path(getattr(self.app, "__file__", "")).parent / "recorded.json"
            rec = json.loads(f.read_text()).get("turns", {}) if f.is_file() else {}
        hit = next((v for k, v in rec.items() if k.lower() in message.lower()), None)
        if not hit:
            return {"text": "This demo is in recorded mode (no model key found). Pick one of the suggested questions.", "answer": None, "log": {}}
        self.surfaces += 1
        ans = hit.get("answer")
        if ans and not smartui.validate(ans, self.catalog, {"source": hit.get("data")})["ok"]:
            ans = None  # a recording that no longer passes today's checks is shown as text only
        return {"text": hit.get("text", ""), "answer": ans, "data": hit.get("data", {}), "log": {"recorded": True}}


# ----------------------------------------------------------------------------------------------- the reference server

def serve(app_path, port, provider):
    import functools
    import http.server
    app = load_app(app_path)
    web = pathlib.Path(app.WEB).resolve()
    sessions = {}
    prov = provider or available()[0]

    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _json(self, code, obj):
            b = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            if self.path.startswith("/api/info"):
                return self._json(200, {"name": app.NAME, "provider": prov, "available": available(),
                                        "model": MODELS.get(prov), "suggestions": getattr(app, "SUGGESTIONS", [])})
            for prefix, folder in getattr(app, "STATIC", {}).items():  # extra read-only folders the app names
                if self.path.startswith(prefix):
                    f = (pathlib.Path(folder) / self.path.split("?")[0][len(prefix):]).resolve()
                    if f.is_file() and pathlib.Path(folder).resolve() in f.parents:
                        b = f.read_bytes()
                        self.send_response(200)
                        self.send_header("content-type", "text/css" if f.suffix == ".css" else "application/octet-stream")
                        self.end_headers()
                        return self.wfile.write(b)
            if self.path.startswith("/system/"):  # the app's own system: tokens.css, smart-ui/catalog.json, od-components.js
                base = pathlib.Path(app.CATALOG).resolve().parents[1]
                rel = self.path.split("?")[0][len("/system/"):]
                f = (base / rel).resolve()
                allowed = {base / "build" / "css" / "tokens.css", base / "smart-ui" / "catalog.json", base / "smart-ui" / "od-components.js"}
                if f in allowed and f.is_file():
                    b = f.read_bytes()
                    self.send_response(200)
                    self.send_header("content-type", {".css": "text/css", ".json": "application/json", ".js": "text/javascript"}[f.suffix])
                    self.end_headers()
                    return self.wfile.write(b)
                return self._json(404, {"error": "not found"})
            if self.path.startswith(("/opendesigner-smart-ui/", "/skills/opendesigner-smart-ui/assets/")):  # the renderer, from this skill
                f = (HERE.parent / "assets" / self.path.split("?")[0].rsplit("/", 1)[1]).resolve()
                if f.is_file() and f.parent == (HERE.parent / "assets").resolve():
                    b = f.read_bytes()
                    self.send_response(200)
                    self.send_header("content-type", "text/javascript" if f.suffix == ".js" else "text/css")
                    self.end_headers()
                    return self.wfile.write(b)
            return super().do_GET()

        def send_error(self, code, message=None, explain=None):
            """The app's own not-found page (web/404.html) when it has one, instead of the server's bare error."""
            page = web / "404.html"
            if code == 404 and page.is_file():
                b = page.read_bytes()
                self.send_response(404)
                self.send_header("content-type", "text/html; charset=utf-8")
                self.send_header("content-length", str(len(b)))
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(b)
                return
            super().send_error(code, message, explain)

        def _same_site(self):
            """Loopback pages from this server only: a JSON body, our own Host, and our own Origin when the browser sends one
            (stops another site, or a DNS rebinding, from posting a press)."""
            here = f"127.0.0.1:{srv.server_address[1]}", f"localhost:{srv.server_address[1]}"
            origin = self.headers.get("Origin")
            return (self.headers.get("Host") in here and (origin is None or origin in {f"http://{h}" for h in here})
                    and (self.headers.get("Content-Type") or "").split(";")[0].strip() == "application/json")

        def _stream(self, conv, body):
            """One JSON object per line as the turn happens: {"type": "skeleton", "part"} as soon as a part is chosen,
            {"type": "text", "text"} while the words arrive, then {"type": "done", ...the turn} or {"type": "error"}."""
            self.send_response(200)
            self.send_header("content-type", "application/x-ndjson")
            self.send_header("cache-control", "no-store")
            self.end_headers()

            def line(obj):
                self.wfile.write((json.dumps(obj, ensure_ascii=False) + "\n").encode())
                self.wfile.flush()
            try:
                if self.path == "/api/chat":
                    r = conv.answer(str(body.get("message") or "")[:2000], on_event=line)
                else:
                    r = conv.press(body.get("action") or {}, on_event=line)
                line({"type": "done", **r})
            except RuntimeError as e:
                line({"type": "error", "error": str(e)})

        def do_POST(self):
            if not self._same_site():
                return self._json(403, {"error": "only this page may talk to this server"})
            n = int(self.headers.get("content-length") or 0)
            if n > 100_000:
                return self._json(413, {"error": "too large"})
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except ValueError:
                return self._json(400, {"error": "not JSON"})
            sid = str(body.get("session") or "default")[:40]
            conv = sessions.setdefault(sid, Conversation(app, prov))
            if body.get("stream") and self.path in ("/api/chat", "/api/press"):
                return self._stream(conv, body)
            try:
                if self.path == "/api/chat":
                    msg = str(body.get("message") or "")[:2000]
                    return self._json(200, conv.answer(msg))
                if self.path == "/api/press":
                    return self._json(200, conv.press(body.get("action") or {}))
                if self.path == "/api/reset":
                    sessions.pop(sid, None)
                    return self._json(200, {"ok": True})
            except RuntimeError as e:
                return self._json(502, {"error": str(e)})
            return self._json(404, {"error": "no such endpoint"})

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(H, directory=str(web)))
    print(f"{app.NAME}: http://127.0.0.1:{srv.server_address[1]}/  (provider: {prov}; available: {', '.join(available())})")
    srv.serve_forever()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("serve")
    p.add_argument("--app", required=True)
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--provider", choices=list(MODELS) + ["recorded"])
    p = sub.add_parser("ask", help="one turn in the terminal")
    p.add_argument("--app", required=True)
    p.add_argument("--provider", choices=list(MODELS) + ["recorded"])
    p.add_argument("message", nargs="+")
    p = sub.add_parser("record", help="answer the app's suggestions with a real model once, and save them as its recorded mode")
    p.add_argument("--app", required=True)
    p.add_argument("--provider", choices=list(MODELS))
    p = sub.add_parser("providers")
    a = ap.parse_args(argv)
    if a.cmd == "providers":
        print(", ".join(available()))
        return 0
    if a.cmd == "serve":
        serve(a.app, a.port, a.provider)
        return 0
    if a.cmd == "record":
        app = load_app(a.app)
        prov = a.provider or next(p for p in available() if p != "recorded")
        out = {}
        for q in getattr(app, "SUGGESTIONS", []):
            r = Conversation(app, prov).answer(q)
            out[q] = {"text": r["text"], "answer": r["answer"], "data": r["data"], "model": MODELS.get(prov)}
            print(f"{q}: {r['log'].get('part') or 'text'}")
        dest = pathlib.Path(a.app).parent / "recorded.json"
        dest.write_text(json.dumps({"about": f"Answers recorded from {MODELS.get(prov)} with live.py record; replayed when there is no model.",
                                    "turns": out}, indent=1, ensure_ascii=False) + "\n")
        print(f"wrote {dest}")
        return 0
    app = load_app(a.app)
    conv = Conversation(app, a.provider or available()[0])
    for m in " ".join(a.message).split(" || "):
        r = conv.answer(m)
        print(json.dumps({"text": r["text"], "part": r["log"].get("part"), "log": r["log"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
