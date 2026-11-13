# Demo: the component library by fetch and over MCP

Under five minutes, from a clean scratch folder, on a Mac or Linux machine with Python 3.10+ and a clone of this repository. Nothing here goes online: the website is built and served on your own computer.

## 0. A clean scratch folder
```bash
export REPO="$PWD"                       # run from the root of your OpenDesigner clone
export DEMO="$(mktemp -d)" HOME="$(mktemp -d)" OD_HOME="$(mktemp -d)" XDG_CONFIG_HOME="$(mktemp -d)" GIT_CONFIG_GLOBAL=/dev/null
```

## 1. Read the catalog (no website needed)
```bash
python3 "$REPO/skills/opendesigner/scripts/library.py" check | tail -1
python3 -c "import json,sys; e=[c for c in json.load(open(sys.argv[1]))['components'] if c['id']=='approval-panel'][0]; print(e['avoid_when'][0]); print(e['data']['properties']['vendor']); print({k: v['status'] for k, v in e['states']['edge'].items()})" "$REPO/skills/opendesigner/assets/library/library.json"
```
You should see `82 components, 0 with problems`, then the first case where the approval panel is the wrong part, the vendor name's limit (`maxLength 40`), and which of the six hard states the file shows, copes with or leaves to you.

## 2. Fetch a component by its address
Build the website once and serve it on your computer (needs the git-ignored screenshots the maintainer's checkout has; skip to step 3 without them):
```bash
python3 "$REPO/site/build.py" >/dev/null && (python3 -m http.server 8765 --bind 127.0.0.1 --directory "$REPO/site/dist" >/dev/null 2>&1 &)
cd "$DEMO" && python3 "$REPO/skills/opendesigner/scripts/library.py" add kpi-strip --from http://127.0.0.1:8765
curl -fsSLo approval-panel.html http://127.0.0.1:8765/library/approval-panel.html && curl -fsS http://127.0.0.1:8765/library/approval-panel.json | head -c 300
```
The first command copies `components/odl/kpi-strip.html`; `curl` downloads a second part and shows the start of its catalog entry. On the real site the address is `https://opendesigner.dev`; `--from` refuses anything but https outside your own computer.

## 3. Ask the MCP server, as an AI app would
```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"demo"}}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"suggest_components","arguments":{"screen":"a finance tool where a manager approves invoices","limit":3}}}' \
 | python3 "$REPO/server/mcp/server.py" 2>/dev/null | tail -1 | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"
```
You should see three suggestions with `approval-panel` first and the words that matched.

## 4. In Claude Code (optional, uses your Claude account)
Run this in a real terminal, not the scratch `HOME` above, so `claude` finds your sign-in:
```bash
claude mcp add opendesigner-library -- python3 "$REPO/server/mcp/server.py"
```
Then ask Claude Code: "Suggest library components for a finance approvals screen, then get the top one." Remove it again with `claude mcp remove opendesigner-library`.

## 5. The gallery in Claude Desktop
See `site/docs/library.md` ("Browse it from your AI"). It needs a Claude Desktop restart after the config change.
