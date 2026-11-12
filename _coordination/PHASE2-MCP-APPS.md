# Phase 2 — a stateless MCP server with MCP Apps views

Status: design proposal, no code yet. Seeded from `docs/SEED-ISSUES.md` issue 20.

## Shape

Stateless: every request carries everything it needs. No session store, no per-user state on the
server, so any instance can answer any request. The server renders the same visual templates the
skill already ships and returns the person's choice to the model as a tool result.

## Tools (`server/`)

- `list_templates` — no input — the template ids, names and one-line descriptions read from
  `skills/opendesigner/assets/templates/`.
- `show_choices` — `{question, options: [{id, label, template, preview}]}` — an MCP App view
  (`ui://opendesigner/choices`) showing the options as clickable cards.
- `show_template` — `{template, tokens?}` — the template rendered as an MCP App view for review.
- `get_choice` — `{choice_id}` — the recorded choice, for hosts that cannot deliver view messages.

## Views

Two static views: `ui://opendesigner/choices` and `ui://opendesigner/preview`. Both are plain HTML
built from the existing templates; the view posts `{choice_id, option_id}` back through the host's
MCP Apps message channel.

## How a choice returns to the model (DC-L18-07)

The view calls the host's `ui/message` with a structured payload; the host injects it as a user-role
message holding one compact line, `opendesigner.choice {"option_id": "..."}`. The model reads that
line and continues. Choice ids are self-describing (base64url of the option payload), so
`get_choice` is a pure decode and the server stays stateless. A host that cannot deliver view
messages still works: the view shows a short code the person can paste.

## Hosting and auth (DC-L18-05)

- 2a, local: stdio only, launched from Claude Desktop's config. No auth, no network.
- 2b, remote: streamable HTTP behind an OAuth 2.1 resource server. The MCP server is the resource;
  tokens are audience-bound to its URL, PKCE is required, and the view holds no long-lived secret.
  Statelessness means no sticky sessions and no shared cache of choices.
- Views are served from the MCP origin; CSP allows inline styles and the template assets only.

## Reusing `skills/opendesigner/assets/templates/`

The server never forks the templates. A build step copies them into `server/views/` and wraps each
in the MCP Apps view shell (the script that wires `ui/message`). The templates stay the single
source of truth; a test fails when the copy drifts.

## Local test in Claude Desktop, before any remote hosting

1. Build the views.
2. Add `{"mcpServers": {"opendesigner": {"command": "node", "args": [".../server/stdio.js"]}}}` to
   `claude_desktop_config.json`.
3. Ask for a design choice; confirm the view renders and the choice line appears in the transcript.

## Open questions

- Which host view APIs are stable across Claude, ChatGPT, VS Code and Cursor.
- Whether previews need the paint engine or static HTML is enough.
