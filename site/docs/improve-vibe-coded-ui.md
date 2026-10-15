---
title: Improve a vibe-coded UI
seo_title: Improve a vibe-coded UI with a design system you confirm
description: How OpenDesigner reads the values in an app built fast with AI, lets you confirm the rules, and lists every hard-coded value that still skips them.
section: Guides
order: 22
updated: 2026-10-15
---

If you built an app quickly by prompting an AI, it probably works but looks a little off. OpenDesigner can help in three steps. It reads the values already in your code. You confirm which ones become the rules. Then it lists every place your code still skips those rules, with the token to use instead.

It doesn't rewrite your UI by itself. You, or your AI, make the fixes, and a review command shows what is left.

## Why it looks off

Each prompt picks its own values. One button gets 7 px corners, a card gets 12 px, and a gray is typed in by hand. No single value is wrong, but together they don't match. A design system puts the rules in one place, so every screen uses the same ones.

## The example on this page

We wrote a six-line style sheet with that kind of drift and ran it through the real engine on 2026-10-15, with Python 3.10.11. Every output below is copied from that run. Here are three of its lines, numbers 2, 4 and 5:

```css
.btn { background: #4f46e5; color: #ffffff; border-radius: 7px; padding: 8px 16px; }
.input { border: 1px solid #d1d5db; border-radius: 7px; padding: 8px 12px; }
.card { background: #f9fafb; border-radius: 12px; padding: 24px; }
```

## Step 1: It reads what is there

The opendesigner-extract skill asks before it reads anything, and asks you to tag the source. Here it is tagged as your own product. A helper script measures the CSS, then the engine turns the measurements into proposals:

```
Reference our-app (our-product, code): 7 proposal(s), pending until accepted
  dials.roundness                  42  high    most common control radius 7 -> A5 band
  dials.density                    35  high    body 16.0px -> A3 bands
  raw.brandColor             "#4f46e5"  high    the person's own product: its brand color may carry over
```

In plain words: your 7 px button corners set the roundness, your 16 px body text sets the density, and your indigo stays as the brand color because the app is yours. When the source is someone else's site, the exact color is never copied. See [Start from an existing app or brand](/docs/existing-product/).

## Step 2: You confirm

Nothing is decided until you accept, adjust or ignore each line. In the example, all seven were accepted. The decision log records each one as coming from your app, with its reason. The brand color stayed exact on the buttons. `DESIGN.md` notes that white text on it reads at 6.29:1, above the 4.5:1 floor.

## Step 3: Review finds the drift

Run `engine.py review --project src`. Here is part of its output:

```
  app.css:2  #4f46e5  ->  use var(--ds-color-bg-action-primary)
  app.css:2  border-radius: 7px  ->  use var(--ds-radius-control) (6px, the control radius)
  app.css:4  #d1d5db  ->  use var(--ds-color-border-separator) (closest match)
  app.css:5  border-radius: 12px  ->  use var(--ds-radius-container) (8px, the container radius)
```

In all, it found 16 hard-coded values. It also found 4 lines that break a house standard, because their spacing was in pixels.

Each suggestion names a role and its value, so you can see what would change. "Closest match" means no token fits exactly, so you choose. For the input border, we chose `--ds-color-border-input` instead.

## Step 4: You decide, and extend records it

The review shows that the cards' 12 px corners would become 8 px. If you'd rather keep 12 px, say so. The extend skill records the change, with your reason, and rebuilds:

```
engine.py set radius.container 12 --why "cards keep the 12px corners the app has today"
```

```
D-0015 set overrides.radius.container = 12 (chosen)
  tokens: 2 values change (radius.container, radius.overlay). Run `engine.py build` to refresh the tokens, exports and preview.
```

The radius for overlays, such as dialogs, moved up to 16 px with it.

## Step 5: You fix the code

{{figure:intent-vibe-before-after}}

We made these edits by hand, following the suggestions. Your AI agent can make the same edits when you ask it to. Then review again:

```
No hard-coded colors, sizes, radii, shadows or durations found: the code uses the tokens.
```

With `--strict`, review exited with an error before the edits and passed after them.

## What review can't tell you

Review reads code. It can't see the rendered page, so it can't judge layout, hierarchy or whether people understand your app. Values read from a screenshot are estimates. OpenDesigner hasn't had watched user trials yet. If a value looks wrong, adjust it, and please [report it](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).

## Next

- [Install OpenDesigner](/docs/install/) in your AI tool.
- [Start from an existing app or brand](/docs/existing-product/) for websites, screenshots, Figma files and brand books.
- No app yet? Follow [Your first design system](/docs/quickstart/).
