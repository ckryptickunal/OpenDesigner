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

MODELS = {"anthropic": "claude-sonnet-5-5", "claude-cli": "claude-sonnet-5-5", "gemini": os.environ.get("OD_GEMINI_MODEL") or "gemini-3.1-pro-preview"}
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


def ask(provider, system, turns):
    """turns: [{"role": "user"|"assistant", "text": ...}]. Returns the model's text."""
    if provider == "anthropic":
        body = {"model": MODELS["anthropic"], "max_tokens": 2048, "system": system,
                "messages": [{"role": t["role"], "content": t["text"]} for t in turns]}
        res = _post("https://api.anthropic.com/v1/messages", body,
                    {"x-api-key": env_key("ANTHROPIC_API_KEY"), "anthropic-version": "2023-06-01"})
        u = res.get("usage", {})
        _count(MODELS["anthropic"], u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0), u.get("output_tokens", 0))
        return "".join(b.get("text", "") for b in res.get("content", []) if b.get("type") == "text")
    if provider == "gemini":
        body = {"systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "model" if t["role"] == "assistant" else "user", "parts": [{"text": t["text"]}]} for t in turns]}
        res = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{MODELS['gemini']}:generateContent", body,
                    {"x-goog-api-key": env_key("GEMINI_API_KEY")})
        u = res.get("usageMetadata", {})
        _count(MODELS["gemini"], u.get("promptTokenCount", 0), u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0))
        parts = res["candidates"][0]["content"].get("parts", [])
        return "".join(p.get("text", "") for p in parts if not p.get("thought"))
    if provider == "claude-cli":
        convo = "\n\n".join(f"{'Person' if t['role'] == 'user' else 'You (earlier)'}: {t['text']}" for t in turns[:-1])
        msg = (f"Conversation so far:\n{convo}\n\nPerson now: {turns[-1]['text']}" if convo else turns[-1]["text"])
        r = subprocess.run(["claude", "-p", "--model", MODELS["claude-cli"], "--system-prompt", system, "--tools", "",
                            "--setting-sources", "", "--output-format", "json", msg], capture_output=True, text=True, cwd="/tmp", timeout=600)
        try:
            return json.loads(r.stdout).get("result") or ""
        except ValueError:
            raise RuntimeError("claude -p failed: " + (r.stderr or r.stdout)[:200])
    raise RuntimeError(f"unknown provider {provider}")


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


def actions_text(actions, changes):
    return "\n".join(f"- {n}({', '.join(f'{k}: {v}' for k, v in a.get('params', {}).items())}): {a['description']}"
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
        self.route_parts = {}
        for name, a in app.ACTIONS.items():
            for it in (self.scope or {}).get("intents", []):
                if a.get("path") and it.get("from", "").startswith(f"{a.get('method', 'GET')} {a['path']} "):
                    self.route_parts[name] = it.get("components", [])
        self.turns = []        # [{"role", "text"}] as the model sees them
        self.data = {}         # action name -> its latest result
        self.surfaces = 0
        self.log = []          # per turn: calls, first errors, repaired, ui
        self.offered = []      # the changes an answer offered as buttons: (name, context); a press must match one (R3)

    # -- routing: which read actions to run
    def route(self, message):
        if self.provider == "recorded":
            return []
        system = ROUTE.format(reads=actions_text(self.app.ACTIONS, False), changes=actions_text(self.app.ACTIONS, True))
        raw = ask(self.provider, system, self.turns[-6:] + [{"role": "user", "text": message}])
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
    def answer(self, message, max_parts=None):
        if self.provider == "recorded":
            return self._recorded(message)
        calls = self.route(message)
        fresh = self.run(calls)
        data = {**self.data, **fresh}
        surface = f"s{self.surfaces + 1}"
        history = "\n".join(f"{'Person' if t['role'] == 'user' else 'You'}: {t['text'][:400]}" for t in self.turns[-6:])
        boost = {}
        for name, _ in calls:  # the parts this repo's scope tied to the actions just run
            for i, part in enumerate(self.route_parts.get(name, [])):
                boost[part] = boost.get(part, 0) + (3 if i == 0 else 2)
        said = " ".join([t["text"] for t in self.turns if t["role"] == "user"] + [message])
        source = {**data, "_the_person_said": said}  # numbers the person typed count as given (R6)
        always = ["ApprovalPrompt"] if any(a.get("changes") for a in self.app.ACTIONS.values()) else []
        system, sel = smartui.build_prompt(message, self.catalog, 3, self.scope, data, boost, always)
        if history:
            system += "\n\nThe conversation so far (for follow-up questions):\n" + history
        system += ("\n\nActions that change data are buttons only. When the person wants one, show an ApprovalPrompt whose approve "
                   "button carries the action as its event name, with the details from the data; never say it is done.")
        if sel["ui"]:
            system += ("\nChange actions: use the exact name as the approve button's event name, and put every argument in "
                       "its event context, filled from the data (for example {\"name\": \"pay_invoice\", \"context\": {\"number\": \"TH-1047\"}}):\n"
                       + actions_text(self.app.ACTIONS, True))
        turns = self.turns[-8:] + [{"role": "user", "text": message}]
        reply = ask(self.provider, system, turns)
        result = self._check(reply, source, surface, max_parts)
        first_errors = result["errors"]
        repaired = False
        if result["errors"]:
            fix = ("Your answer was not shown: it failed these checks. Send the corrected text and part, or text only.\n"
                   + "\n".join(f"- {e['rule']} at {e['path']}: {e['message']}" + (f" ({e['fix']})" if e.get("fix") else "") for e in result["errors"][:10]))
            reply = ask(self.provider, system, turns + [{"role": "assistant", "text": reply}, {"role": "user", "text": fix}])
            result = self._check(reply, source, surface, max_parts)
            repaired = True
            if result["errors"] and all(e["rule"] in smartui.COPY_RULES for e in result["errors"]) and result.get("draft"):
                result["answer"] = result["draft"]  # only wording is left after the repair: show it, log what's left
            elif result["errors"] and not all(e["rule"] in smartui.COPY_RULES for e in result["errors"]):
                result["answer"] = None  # still wrong after one repair: text only
        text = result["text"] or "Sorry, I couldn't show that. Here is what I found: " + json.dumps(fresh)[:300]
        self.turns += [{"role": "user", "text": message},
                       {"role": "assistant", "text": text + (f" [showed {result['part']}]" if result["answer"] else "")}]
        if result["answer"]:
            self.surfaces += 1
            self._remember_offers(result["answer"])
        entry = {"message": message, "calls": calls, "selector": sel["candidates"], "ui": bool(result["answer"]),
                 "part": result["part"], "first_errors": [f"{e['rule']} {e['path']}" for e in first_errors], "repaired": repaired,
                 "final_errors": [f"{e['rule']} {e['path']}" for e in result["errors"]]}
        self.log.append(entry)
        return {"text": text, "answer": result["answer"], "data": data, "log": entry}

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
        r = smartui.validate(msgs, self.catalog, {"source": data, "limits": {"leaves": max_parts}, "copy": True})
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
    def press(self, action):
        name, ctx = action.get("name"), dict(action.get("context") or {})
        a = self.app.ACTIONS.get(name)
        if a and a.get("changes"):
            approved = ctx.pop("approved", None) is True
            offer = (name, json.dumps(ctx, sort_keys=True))
            if not approved or offer not in self.offered:  # only a change this conversation showed, after the prompt said yes
                return {"text": "That needs your confirmation first.", "answer": None, "log": {"refused": name}}
            self.offered.remove(offer)
            args = {k: v for k, v in ctx.items() if k in a.get("params", {})}
            try:
                result = a["fn"](**args)
            except Exception as e:
                result = {"error": {"message": str(e)[:200]}}
            self.data[name] = result
            return self.answer(f"(I confirmed {name.replace('_', ' ')}. The app returned the result; tell me what happened.)")
        # not a change: what the person picked becomes their next message
        said = ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in ctx.items())
        return self.answer(f"I picked {name.replace('_', ' ')}" + (f": {said}" if said else "") + ".")

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

        def _same_site(self):
            """Loopback pages from this server only: a JSON body, our own Host, and our own Origin when the browser sends one
            (stops another site, or a DNS rebinding, from posting a press)."""
            here = f"127.0.0.1:{srv.server_address[1]}", f"localhost:{srv.server_address[1]}"
            origin = self.headers.get("Origin")
            return (self.headers.get("Host") in here and (origin is None or origin in {f"http://{h}" for h in here})
                    and (self.headers.get("Content-Type") or "").split(";")[0].strip() == "application/json")

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
