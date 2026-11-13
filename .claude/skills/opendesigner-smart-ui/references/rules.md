# Smart UI rules

Seven rules. The validator enforces what a script can see; the audit and the evals check the rest. Each rule names the check that holds it.

| Rule | What it means | Held by |
|---|---|---|
| **R1 No UI when text is enough** | A short factual answer ("When does the shop open?") stays text. The selector needs a reason to show a part: a cue in the message (compare, list, chart, book, form, status) and a part that fits. When it finds none, the prompt says "answer in text only". | `select()` in `smartui.py`; evals measure over-triggering on no-UI cases |
| **R2 One surface per intent** | One part per answer. A `Column` of two to four only when the person asked for more ("show the chart and the table"). | validator `R2-one` (`--max-parts` raises the limit) |
| **R3 Changes wait for the person** | Actions marked `data-od-effect="change"` (book, pay, send, delete) are buttons. Pressing one shows the approval prompt; only Confirm sends the action, with `approved: true` set by the renderer. An answer that sets `approved` itself is refused. An approval prompt always lists what its button will send (rebuilt from the button's own context), so it can't show one thing and send another. The reference server runs a change only when it matches one this conversation offered, once, and only from its own page. | validator `R3-approval`; `od-surface.js` `askApproval` and `approvalDetails`; `live.py` `press` |
| **R4 Nothing off-system** | The catalog has no colour, size, style or URL-of-your-choice properties. Visual options are enums of the system's token families. The validator refuses `style`, `class`, `theme`, `on*` and HTML keys; HTML in text; whole-value colours, lengths and CSS functions; URLs outside the owner's allow-list (https only); unknown parts and unknown properties (refused, not dropped, so mistakes show). | validator `R4-key`, `R4-html`, `R4-style`, `R4-token`, `R4-url`, `unknown-component`, `unknown-property` |
| **R5 Accessibility floors** | WCAG 2.2 AA contrast, 24 px targets and 44 px for actions that change data, visible focus, one polite live region announcing new surfaces (never assertive), reduced motion, every image with alt text, every control with a name, and no two actions with the same name ("Book" three times fails; the renderer adds the item's name, or the answer sets `a11y_label`). | validator `R5-name`, `R5-repeat`, `empty` on alt and labels; audit floors |
| **R6 Honest data** | A chart never invents values. With `--source` (the data the model was given), every number property must come from it; numbers inside text get a warning. A value the model does not have is left out or sent as `null`, and the renderer shows it as missing (a dash), never as zero. | validator `R6-number`, `R6-text` warning; renderer `data-od-missing` |
| **R7 Host look** | Inside Claude or ChatGPT (MCP Apps), the host's CSS variables are mapped onto `--ds-*` only when the owner opts in (`smartui.py catalog --host-look`; the model cannot turn it on). In the person's own product, their tokens always win. | MCP view; `references/adapters.md` |

## How a failure comes back
Every error is an A2UI v1.0 error message plus two fields for people: `rule` and `fix`.

```json
{"code": "VALIDATION_FAILED", "rule": "R4-url", "path": "/0/createSurface/components/0/items/0/photo/src",
 "message": "evil.example is not on the allow-list for images", "surfaceId": "s1",
 "fix": "leave it out, or ask the owner to add the domain"}
```

`smartui.py validate --a2ui` prints them as `{"version": "1.0", "error": {...}}` lines, ready to send back to the agent. Send them once. If the second answer also fails, show the text answer alone.

## What the rules do not cover
- Whether the model picked the best part for the question. The evals measure it; nothing blocks it.
- Copy quality inside the parts. The audit runs the copy checks (English only) when `opendesigner-review` has them.
- Prompt injection that stays inside the allowed values (a misleading title, a wrong but allowed number without `--source`). Pass `--source` wherever the data is known.
