# Adapters: where Smart UI answers can show

One answer format (A2UI v1.0 messages against the project's catalog) and three places to draw it. No new protocol.

## 1. In the person's own product (any framework)
`<od-surface>` is a plain custom element. It works in plain HTML, React, Vue, Svelte, Angular or anything that renders HTML.

```html
<link rel="stylesheet" href="/opendesigner/build/css/tokens.css">
<link rel="stylesheet" href="/smart-ui/od-surface.css">
<script src="/opendesigner/smart-ui/od-components.js"></script>
<script type="module" src="/smart-ui/od-surface.js"></script>   <!-- imports ./od-validate.js beside it -->

<od-surface id="answer"></od-surface>
<script type="module">
  const s = document.getElementById("answer");
  s.catalog = await (await fetch("/opendesigner/smart-ui/catalog.json")).json();
  s.source = dataTheModelHad;            // optional: numbers must come from it (R6)
  const r = s.process(messagesFromTheModel);   // validates first; renders only when it passes
  s.addEventListener("od-error", (e) => sendBackToModel(e.detail.a2ui));   // repairable A2UI errors
  s.addEventListener("od-action", (e) => sendToAssistant(e.detail));        // an A2UI action message
</script>
```

Copy `od-surface.js`, `od-validate.js` and `od-surface.css` from this skill's `assets/` into the project; `smartui.py catalog` writes `catalog.json` and `od-components.js`. In React, render `<od-surface ref={ref} />` and call `ref.current.process(...)` in an effect; in Vue, the same with a template ref. No bindings to install.

Streaming: call `process(messages, {partial: true})` as messages arrive; missing slots draw as loading blocks and actions stay disabled until the final `process(messages)`.

A host that shows no interface (a voice assistant, an email digest, a plain-text API) uses `smartui.py text` or `s.toText()`: the same answer as plain lines.

## 2. A2UI v1.0
OpenDesigner is a catalog and renderer provider:
- The catalog (`catalog.json`) follows A2UI's `catalog_definition.json`: `$id` equals `catalogId`, `protocolVersion` "1.0", `$defs.anyComponent` and `$defs.anyFunction`, and our facts in `metadata.extensions.opendesigner`.
- The renderer advertises it: `s.capabilities()` returns `{"1.0": {"supportedCatalogIds": [catalogId]}}`, the shape of A2UI's `a2uiRendererCapabilities`. Send it with each request, the way your transport carries metadata.
- Errors go back as A2UI `error` messages (`smartui.py validate --a2ui`, or `e.detail.a2ui` in the browser). Actions come out as A2UI `action` messages.
- Values only: this catalog takes literal values, not `{"@path": ...}` data bindings, so what renders is exactly what was checked. `updateDataModel` is accepted and ignored.
- Agents built with an A2UI agent SDK, CopilotKit's declarative mode or an AG-UI transport can target the catalog as they would any other.

## 3. MCP Apps (inside Claude, ChatGPT and other hosts)
The OpenDesigner MCP server (`server/mcp/`) adds:
- **`show_ui`**: takes `answer` (A2UI messages), optional `source` and `max_parts`. `source` is what the model says it was given, so the R6 number check is only as good as that; where the server has the data itself, check against it there. It validates against the project's catalog; a failure returns the A2UI errors as a tool error the model can fix. A pass returns `structuredContent` for the view and the plain-text version as `content` (what a host without views shows). Read-only: data in, view out.
- **`ui://opendesigner/surface`**: one HTML file with the project's tokens, the renderer, the confirmed parts and the catalog (`smartui.py view` writes the same file). Its CSP allows images only from the owner's image hosts.
- A button pressed in the view comes back as a chat message: `OD:action <name> <context>`. A change goes through the approval prompt in the view first.
- **R7:** the host's CSS variables are mapped onto a few `--ds-*` roles only when the owner built the catalog with `--host-look`; a model cannot turn it on. By default the person's own system draws the answer.

## What has been tested, by host
Tested means: run, looked at, and the result recorded here with its date. Anything not in this table has not been tried.

| Host or tool | What was checked | Result | Date |
|---|---|---|---|
| Chromium (Playwright), plain HTML | every part's fixtures in every state of `states.md`, in two systems | see the audit report in the PR | 2026-11-13 |
| A2UI v1.0 JSON Schemas (a2ui-project/a2ui, `specification/v1_0/json`) | catalog, part fixtures, actions, errors and capabilities with `scripts/a2ui_check.py` | all conform | 2026-11-13 |
| MCP Apps view, simulated host (a test page that speaks the 2026-01-26 postMessage protocol) | initialize, tool-result draws the answer, an action becomes ui/message | to be recorded | |
| Claude Desktop, claude.ai | not tried yet | | |
| ChatGPT | not tried yet | | |
| A2UI Lit renderer, CopilotKit | not tried yet | | |
