# Why {{name}} looks the way it does

<!-- One page for teammates, managers and designers who will not read decisions.md. Written by the model
from the decision log at the end of the interview, refreshed after each extend session. Plain language;
question ids and D-numbers only in the footnotes. -->

## What we built
{{One paragraph: the product, who it is for, the direction in one line, and the one thing people should remember.}}

## The five choices that shape everything
1. **{{Personality}}:** we chose {{X}} because {{Y}}; the main alternative was {{Z}}, which would have meant {{W}}.
2. **{{Platforms}}:** ...
3. **{{Visual direction}}:** ...
4. **{{Density}}:** ...
5. **{{Brand color role}}:** ...

## What the rules guarantee
- Text contrast of at least 4.5:1 (3:1 for large text and controls) in light and dark mode.
- Touch and click targets of at least {{24 px web / 44 pt iOS / 48 dp Android}}.
- A visible focus ring on every interactive element.
- Motion that respects the reduced-motion setting.

## What is still open
- Assumed answers to confirm: {{list}}
- Assets pending, with owner and brief: {{hook, owner, opendesigner/briefs/<hook>.md}}
- Warnings waived, with reasons: {{list}}

## How to ask for a change
{{Who approves design-system changes.}} Ask your agent to use the opendesigner-extend skill; it reads this system first, shows what a change would move, and records the new decision in `opendesigner/decisions.md`.

## For designers
{{The briefs for missing assets and what is yours to own: logo, illustration, photography, custom icons, motion signature.}}

---
Footnotes: {{Q-ids and D-numbers for each choice above}}
