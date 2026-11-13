---
title: Where Smart UI runs
seo_title: "Smart UI adapters: your product, A2UI and MCP Apps"
description: Smart UI answers show in your own product with a plain HTML element, through the A2UI v1.0 format, and inside Claude and ChatGPT through MCP Apps. What has been tested in each.
section: Reference
order: 8.5
updated: 2026-11-13
---

One answer format, three places to show it. No new protocol: Smart UI writes A2UI v1.0 and speaks MCP Apps.

| Where | How | Tested |
|---|---|---|
| Your own product, any framework | `<od-surface>`, a plain custom element | Yes, in Chromium, in two systems |
| Agents that speak A2UI v1.0 | The catalog and the renderer | Messages and catalog pass A2UI's own schemas. Not tried with another A2UI renderer yet |
| Claude, ChatGPT and other MCP Apps hosts | `show_ui` in the OpenDesigner MCP server | Against a simulated host. Not tried in Claude or ChatGPT yet |
| Anywhere with no interface | The same answer as plain text | Yes |

## In your own product

`<od-surface>` needs no framework and no build step. Copy `od-surface.js`, `od-validate.js` and `od-surface.css` from the skill's `assets/` folder, and load your `tokens.css` and the `od-components.js` the catalog step wrote. In React or Vue, render the element and call `process()` on it from an effect.

- `process(messages)` checks the answer, then draws it. It fires `od-error` with errors the model can fix.
- `process(messages, {partial: true})` while an answer streams in. Missing parts show as loading blocks.
- `od-action` fires when the person presses a button. A change shows the approval prompt first.
- `setActionState(button, "pending" | "done" | "failed", note)` shows what happened and reads the note out.
- `toText()` gives the answer as plain lines.

## A2UI v1.0

The catalog follows A2UI's catalog format, so an agent built with an A2UI SDK can target it. The renderer's `capabilities()` returns the `supportedCatalogIds` A2UI expects. Errors go back as A2UI error messages, and button presses come out as A2UI action messages.

One difference from A2UI's basic catalog: Smart UI takes values, not data bindings. What renders is exactly what was checked.

## MCP Apps: inside Claude and ChatGPT

The OpenDesigner MCP server adds a `show_ui` tool and a `ui://opendesigner/surface` view. The model calls `show_ui` with its answer. The server checks it against your catalog and returns the errors when it fails. When it passes, the host draws it with your tokens, and hosts without views show the text version.

A button pressed in the view comes back to the chat as a message. Nothing runs on its own, and the server never changes anything.

Your look draws the answer by default. To blend into the host instead, the owner turns on `host_look`, which maps the host's colours and font onto a few of your roles.

## What we haven't tried

- Claude Desktop, claude.ai and ChatGPT with the MCP server. The view passes a simulated host; real hosts are known to differ.
- Other A2UI renderers (the Lit, React and Flutter ones) and CopilotKit.
- A real screen reader. The audit checks names, roles and the live region, which is what one reads, but not how it sounds.
