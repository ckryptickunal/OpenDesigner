---
title: Smart UI: answers that show your interface
seo_title: "Generative UI from your own design system components"
description: Comes with OpenDesigner: your assistant answers with a table, a comparison or a booking step made from your own components, checked before it shows.
section: Concepts
order: 8
updated: 2026-11-13
---

Smart UI makes your assistant answer by rendering your own components instead of plain text. Ask your travel app's assistant for flights to Lisbon and it can answer with a list of flights you can book, not three paragraphs. Smart UI comes with OpenDesigner and does this with your own design system: your components, your colours, your type, in any framework. There's nothing separate to install. It stays off until you ask for it, or until OpenDesigner sees an assistant or chat in your product, offers it once, and you say yes.

The model picks a part and fills in words and numbers. It never picks a colour, a size or a link. Every answer is checked before anything shows, and anything that books, pays, sends or deletes waits for the person to press a button.

## How an answer becomes interface

1. **Scope.** It reads your repo: what the product is, who uses it, where the assistant lives, your framework, your tokens, and the actions your API can take. It proposes what the assistant should answer with (for a travel app: flight results, a fare comparison, a booking confirmation) and you confirm the list. What it can't find says "not known".
2. **Catalog.** Your confirmed parts become a catalog the model reads. It holds words and numbers, and looks only from your token names.
3. **Select.** For each message, only the two or three parts that fit go to the model. A short question gets a text answer.
4. **Check.** The answer is validated before it renders. A mistake comes back to the model as an error it can fix.
5. **Show.** `<od-surface>`, a plain HTML element, draws the part from your library and your `tokens.css`. It works in React, Vue, Svelte or plain HTML.
6. **Audit.** Every part is rendered in every state at phone and desktop sizes, at 200% text, in dark mode and right to left, and checked against the accessibility floors.

## The rules it keeps

| Rule | What it means |
|---|---|
| Text when text is enough | "When does check-in open?" gets a sentence, not a card. |
| One part per answer | Unless the person asked for more. |
| Changes wait for a tap | Book, pay, send and delete are buttons. Pressing one asks first. The model can't press it. |
| Nothing off-system | No colours, sizes, styles, HTML or links outside your allow-list. Unknown parts are refused, not dropped. |
| Accessibility floors | AA contrast, 24 px targets (44 px for actions that change data), visible focus, one polite announcement, reduced motion, and no two buttons with the same name. |
| Honest numbers | A number shown must be in the data the assistant was given. Missing stays missing. |
| Your look wins | Inside Claude or ChatGPT, the host's look applies only if you turn it on. |

## What you get

- 26 parts in six jobs: answer, data, choose, act, confirm, and media. They're all in the [component library](/library/), so they work in your product with or without the assistant. The full list, by job, is on the [Smart UI page](/smart-ui/#parts).
- A catalog in the A2UI v1.0 format, an MCP Apps view for Claude and ChatGPT, and a plain-text version for anywhere that shows no interface. See [where it runs](/docs/smart-ui-adapters/).
- An audit of every part in every state, and evals of how Claude and Gemini use it.

## What has been tested

We say what we ran. The parts, the checks and the renderer are tested in Chromium, in two different systems. The catalog and messages pass A2UI's own v1.0 schemas. The MCP Apps view is tested against a simulated host that speaks the protocol. It hasn't been tried yet inside Claude Desktop, claude.ai or ChatGPT. The [evals](/docs/evals/) report how often each model picked the right part, how often its answer passed the first time, and how often it showed a part where text was enough.

[Add it to your assistant](/docs/smart-ui-quickstart/)
