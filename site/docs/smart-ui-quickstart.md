---
title: Add Smart UI to your assistant
seo_title: "Add generative UI to your chatbot with your own components"
description: Add OpenDesigner Smart UI to a chatbot you already have: scope the repo, confirm the parts, write the catalog, then check and render each answer.
section: Guides
order: 9
updated: 2026-11-13
---

This guide sets up your assistant to answer by rendering your own components instead of plain text. You need an assistant in your product (or a plan for one) and an OpenDesigner system. No system yet? Run the five-question sketch first: it takes a few minutes. Smart UI comes with OpenDesigner, so there's nothing more to install. Ask your AI: "Add Smart UI to our assistant."

## 1. Let it read your repo

Your AI runs the scope step and shows you what it found:

```
python3 smartui.py scope --write
```

You'll see your product type, where the assistant lives, your framework, your tokens and the actions your API takes, then a list of answers the assistant should show as interface. For a travel app it might propose flight results, a fare comparison, a seat or time picker, a booking confirmation and a refund status. Remove what you don't need. Fewer is better: four to six parts is plenty to start.

## 2. Confirm the parts and write the catalog

```
python3 smartui.py confirm FlightResults,Comparison,TimeSlots,ApprovalPrompt,Receipt
python3 smartui.py catalog --allow-images images.your-cdn.example
```

The catalog lands in `opendesigner/smart-ui/`. Images and links are off until you name the hosts they may come from.

## 3. Send the right parts with each message

Before each call to your model, add the prompt for that message. It holds the rules and only the parts that fit:

```
python3 smartui.py prompt --for "Flights from Bristol to Lisbon on 4 December" --data flights.json
```

The model answers in text, plus one block of A2UI messages when a part helps.

## 4. Check and show the answer

In the browser, `<od-surface>` checks the answer and draws it:

```html
<od-surface id="answer"></od-surface>
<script type="module">
  const s = document.getElementById("answer");
  s.catalog = catalog;               // opendesigner/smart-ui/catalog.json
  s.source = data;                   // what the model was given: every number must come from it
  s.process(messagesFromTheModel);   // checks first, then renders
  s.addEventListener("od-error", (e) => sendBack(e.detail.a2ui));   // the model fixes and resends once
  s.addEventListener("od-action", (e) => handle(e.detail));        // a button the person pressed
</script>
```

On a server, the same check runs in Python: `smartui.py validate reply.txt --source data.json`.

## 5. Audit it

```
python3 smartui.py audit --fixtures
```

Every part you confirmed renders in every state, at 320, 375 and 1440 px, at 200% text, in dark mode, right to left and with reduced motion. The report lists what failed and what didn't run. It needs Playwright, which it never installs for you.

## In Claude or ChatGPT

The OpenDesigner MCP server adds a `show_ui` tool and a view, so the same parts show inside hosts that support MCP Apps. See [where it runs](/docs/smart-ui-adapters/).
