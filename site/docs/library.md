---
title: Use the component library
seo_title: Component library by fetch, curl or a local MCP server
description: Pull an OpenDesigner component into a project with one command, read its catalog entry as JSON, or browse the library in Claude Desktop over a local MCP server.
section: Guides
order: 9
updated: 2026-11-13
---

The [component library](/library/) has 82 parts built only on your design tokens. You can take one in three ways: copy a prompt from its page, fetch the file with one command, or let your AI browse the library through a small server on your computer. All three give you the same file.

## Take one file

Every component has a fixed address. This downloads the approval panel into the folder you are in:

```
curl -fsSLo approval-panel.html https://opendesigner.dev/library/approval-panel.html
```

With OpenDesigner installed, this copies it into your project and lists any token your system doesn't have yet:

```
python3 <skill>/scripts/library.py add approval-panel --from https://opendesigner.dev
```

Leave out `--from` to use the copy that came with the skill.

The file is plain HTML with one `<style>` block. Its colours, type and spacing come from `--ds-*` variables, so in a project with an OpenDesigner system it works as it is. Your AI turns it into a React, Vue or Svelte component in your own style.

## Read what a component holds

Each component also has a catalog entry in JSON. It says what the part is for and when not to use it, its parts, how much text and how many items it holds, which states it has, the tokens it reads and how it works with a keyboard.

| Address | What it is |
|---|---|
| `/library/index.json` | Every component's entry in one file |
| `/library/<id>.json` | One component's entry |
| `/library/<id>.html` | The component file |
| `/library/<id>/` | Its page, with a live preview |

The six hard states are always listed: empty, loading, error, disabled, too many items, and long text. Each says whether the file shows it, copes with it, or leaves it for you to build, with one line on how. Of the 492 across the library, 289 are left for you. The entry says so rather than guessing.

:::dev
The catalog is `skills/opendesigner/assets/library/library.json`, written by `library.py catalog` from each component's `component.html` and `meta.json`. Tokens, roles and control counts are read from the file. Purpose, limits and states are written by whoever wrote the component; the limits are what the layout holds at its width, read from the layout, not measured in a browser. `library.py check` fails when the catalog is out of date or a part names a selector the file doesn't have.
:::

## Browse it from your AI (MCP)

MCP is the way AI apps such as Claude Desktop call tools on your computer. OpenDesigner has a small MCP server for the library. It only reads: it never writes to your project and never goes online.

| Tool | What it does |
|---|---|
| `list_components` | Lists the parts, filtered by type, style, width, audience or industry. In Claude it opens a gallery |
| `get_component` | One part: its catalog entry and its file |
| `suggest_components` | Parts that fit a screen you describe. It matches words against the catalog, so check each suggestion's "avoid when" |
| `get_tokens_template` | A `tokens.css` with every variable the parts read, made from a brand colour, for a project with no system yet |

In the gallery, **Use this** puts one line in the chat, for example `OD:add library.approval-panel`. Your AI reads it, asks you, and then adds the file. Where the gallery can't send it, the line stays on screen to copy.

To add it to Claude Desktop, clone the repository, then add this to `claude_desktop_config.json` (Settings, Developer, Edit Config) with your own path, and restart Claude:

```
{
  "mcpServers": {
    "opendesigner-library": {
      "command": "python3",
      "args": ["/path/to/OpenDesigner/server/mcp/server.py"]
    }
  }
}
```

Claude Code takes the same server with `claude mcp add opendesigner-library -- python3 /path/to/OpenDesigner/server/mcp/server.py`. It needs Python 3.10 or newer and nothing else.

:::dev
The server is `server/mcp/server.py`, one Python file with only the standard library, to match the skills. It speaks MCP over stdio: the 2026-07-28 version (`server/discover`, no handshake) and the older `initialize` handshake. Every tool is marked `readOnlyHint: true` and `destructiveHint: false`. The gallery is an MCP Apps view (`ui://opendesigner/library-gallery`, `text/html;profile=mcp-app`) whose only outside source is the sample photos from `images.unsplash.com`, declared in `_meta.ui.csp`. A hosted copy that needs no sign-in is planned, not live.
:::
