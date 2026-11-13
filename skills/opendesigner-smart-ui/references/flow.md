# The Smart UI flow, step by step

Six steps. Each has a gate where the person decides, and a file it leaves behind in `opendesigner/smart-ui/`.

```
scope ──► confirm ──► catalog ──► (each message) select ─► model ─► validate ─► render ─► audit
 reads     person      catalog.json              prompt     A2UI     errors back    <od-surface>  floors + craft
 the repo  says yes    od-components.js          top-k      answer   to the model   tokens.css    ledger
```

## 1. Scope: work out what the assistant must answer
`smartui.py scope --write` reads, and writes nothing else:

| It looks for | Where | When it can't find it |
|---|---|---|
| What the product is | `Q-scope-01` in `opendesigner/state.json`, then the Product section of PRODUCT.md, then `raw.productType` | "not known": ask what the assistant must answer |
| Who uses it | `Q-aud-01` | "not known" |
| Where the assistant lives | files named chat, assistant, copilot, conversation, ai-panel | "not known": ask where it is, or whether it exists yet |
| The framework and AI SDKs | `package.json` (and one level down), `pyproject.toml`, `requirements.txt` | "not known" |
| The tokens | `opendesigner/build/css/tokens.css`, else the project's own CSS variables | offer the opendesigner skill, or a `--ds-*` map |
| The actions | API routes (Express, Flask, FastAPI, Next.js route handlers) and tool definitions | none: the assistant only shows things |

From the product type it proposes intents (`assets/intents.json`: travel, commerce, work tools, developer tools, health, education, content) and one intent per route that changes data (approval, receipt, error). Show the proposal as a short list: intent, the part, where it came from. The person removes, adds and renames. **Nothing about their product is invented**: a product type the list does not know gives one intent, "not known", and you ask.

## 2. Confirm
`smartui.py confirm Comparison,ResultList,...` records the parts the person kept, with the date. Recommend fewer: every part in the catalog is a part the model might pick wrongly, and each costs prompt space. For a first round, four to six parts is plenty.

## 3. Catalog
`smartui.py catalog` writes:
- `catalog.json`: an A2UI v1.0 catalog (`$schema`, `$id` = `catalogId`, `protocolVersion` "1.0", `components`, `functions`, `$defs` with `anyComponent` and `anyFunction`). Each part's properties come from its slot marks and the library's `spec.data`; visual enums are filtered to the system's token families. Our extra facts sit in `metadata.extensions.opendesigner`, the place A2UI keeps for extensions (property-level hints use `x-od-*` keywords, which JSON Schema tools ignore).
- `od-components.js`: each part's own markup and script, for the renderer.

Ask once for the image hosts and link domains the assistant may use (`--allow-images`, `--allow-links`). The default is none: images and links are off until the owner names a host.

## 4. Select and prompt (each message)
`smartui.py prompt --for "<message>" [--data data.json]` (or `build_prompt()` from Python) does two things:
- **Select.** Scores every part against the message (its intents, tags and "use when"), adds the confirmed scope phrases, and keeps the top three. It also decides whether the message gives any reason for UI (R1). No reason: the prompt says "answer in text only".
- **Prompt.** The rules, the output format (one fenced `a2ui` block of A2UI messages after the text), and only the selected parts' properties in a compact form. With `--data`, the data the model may use, so R6 can be checked.

## 5. Validate
Before anything renders: `smartui.py validate reply.txt --source data.json` (or `validate()` from `od-validate.js`, which `<od-surface>` calls itself). The two validators share one fixture suite (`assets/fixtures/validator/`), so a rule cannot exist in one and not the other. Send failures back once as A2UI errors (`--a2ui`); then fall back to text.

Streaming: validate with `--partial` (or `process(messages, {partial: true})`) while the answer arrives. Missing required properties are allowed; everything else (HTML, styles, outside URLs) is still refused. The renderer shows each missing slot as a loading block.

## 6. Render and audit
`<od-surface>` renders the answer from the part's own markup, filling slots with text only. `smartui.py audit --fixtures` renders every confirmed part in every state of `states.md` and reports to `opendesigner/smart-ui/audit/REPORT.md`, with screenshots. With `--ledger`, each failure becomes an item in the audit ledger (`engine.py ledger`, owned by the core skill). The verdict is never "looks good": say how many renders were checked, which environments, and which checks did not run (for example, the craft checks when `opendesigner-review` lacks them).
