# The library over MCP

A local, read-only MCP server for the OpenDesigner component library. An AI app (Claude Desktop, Claude Code, Cursor, VS Code and others) starts it on your computer and calls its tools. It reads the catalog and the component files from this repository and writes nothing. The server makes no network calls; the gallery's previews load the parts' sample photos from images.unsplash.com.

Setup for people: [site/docs/library.md](../../site/docs/library.md) (on the website at `/docs/library/`).

## Files
| File | What it is |
|---|---|
| `server.py` | The server: one Python file, standard library only, stdio |
| `views/gallery.html` | The MCP Apps view `ui://opendesigner/library-gallery`: a gallery with Preview and Use this |
| `test_server.py` | Tests over real stdio: `python3 server/mcp/test_server.py` |

## Tools
All four carry `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true` and `openWorldHint: false` (DC-L18-05).
| Tool | Returns |
|---|---|
| `list_components` | Rows from `library.json`, filtered by type, style, width, audience or industry. Linked to the gallery view |
| `get_component` | One catalog entry, the file, its CSS, markup and script |
| `get_tokens_template` | A `tokens.css` made by `engine.py` in a temporary folder from a brand colour, audience and feel words. Takes a few seconds; cached per brief while the server runs |
| `suggest_components` | Keyword matches for a described screen, with the matched words and each part's `avoid_when`. Not a model |

Resources: the gallery view, and `od://library/catalog` (the whole `library.json`).

Each result has `structuredContent` and a plain-text summary written for the model. The spec says a tool with structured content SHOULD also send the same JSON as text; this server sends the summary instead (and `get_component` puts the full entry in its text), because 82 rows of JSON would cost the model far more than the summary. Hosts that read `structuredContent` get all of it.

## How a pick comes back
Inline in a chat the view is a short card with one button, **Open the gallery** (Claude's inline cards allow at most two actions and no filters); the full gallery opens in fullscreen. The gallery's **Use this** sends one line to the chat with `ui/message`: `OD:add library.<id>`. That is the channel DC-L18-07 recommends (a visible chat line); the line itself has no `=<value>`, like `OD:lock <path>`, and is listed in `skills/opendesigner/references/rules.md` section 9. The agent confirms with the person, then runs `library.py add <id>`. A host that refuses `ui/message` gets the line on screen to copy, so there is always a text path.

## Protocol
Sources, read 2026-11-13: the MCP specification (https://modelcontextprotocol.io/specification/2026-07-28: changelog, stdio, `server/discover`, versioning; and the 2025-11-25 lifecycle), the MCP Apps extension (https://github.com/modelcontextprotocol/ext-apps, `specification/2026-01-26/apps.mdx` and `src/spec.types.ts`) and Claude's MCP Apps design guidelines (https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md). The research behind the choices is `research/L18-ai-first-distribution.md` (Part C, DC-L18-05 and -07); these protocol details postdate it.
- MCP 2026-07-28: `server/discover`, per-request `_meta` with the protocol version, `resultType`, `ttlMs` and `cacheScope` on list and read results, error -32022 for a version it doesn't speak.
- The older handshake (`initialize`, 2025-11-25, 2025-06-18 and 2025-03-26), which many hosts still send.
- MCP Apps (`io.modelcontextprotocol/ui`, ext-apps 2026-01-26): `_meta.ui.resourceUri` on `list_components` (and the older flat `ui/resourceUri`), the view as `text/html;profile=mcp-app` with `_meta.ui.csp`. Its only outside source is the parts' sample photos from `https://images.unsplash.com`. A host that says it can't show views gets the tools without the link.

## Tested so far
- `test_server.py`: both protocol versions over stdio, every tool, bad input, the view's resource and floors.
- A live Claude Code session (headless, 2026-11-13) called `suggest_components`, `get_component` and `list_components` correctly.
- The gallery in a mock MCP Apps host in a browser (handshake, tool result, Use this, Preview, focus return, light and dark).
- **Not yet:** Claude Desktop. It needs a restart after the config change; the steps are in `DEMO.md`.

## Decisions for the owner
- **Language: Python standard library**, to match the skills and the engine (the server imports `library.py` and runs `engine.py`, so one runtime and no install). The alternative was Node (the contributor proposal in PR 124, and `server/telemetry/` is a Cloudflare Worker). Node would matter for a hosted copy on Cloudflare Workers; Python fits a local stdio server and a plain host. Kunal's call; changing it later means rewriting one file of about 380 lines.
- **Hosted copy** (no sign-in, read-only, DC-L18-05 option b): not built and not deployed. It waits for Kunal's yes, and for a choice of host.
- **Not in the plugin's `.mcp.json`** yet: plugin users don't get the server started for them. Adding it is one line, but it starts a process in every session, so it is the owner's call.
