---
title: Make a vibe-coded app look professional
seo_title: How to make a vibe-coded app look professional
description: Make a vibe-coded app look professional: set the design language, choose a direction from real references, write DESIGN.md, build with tokens, check every size.
section: Guides
order: 22
updated: 2026-11-07
---

To make a vibe-coded app look professional, stop each prompt from choosing its own values. Decide the design language once, write it down where your AI reads it, and check the page as people see it, not only the code. OpenDesigner takes the repetitive part off your hands, but it doesn't rewrite your UI on its own: you or your AI make the fixes.

## Why it looks off

Each prompt picks its own values. One button gets 7 px corners, a card gets 12 px, and a gray is typed in by hand. No single value is wrong, but together they don't match.

## Five steps

| Step | What you do | What OpenDesigner does |
|---|---|---|
| 1. Set the design language | Confirm your colors, type, spacing, corners, depth and motion | Reads the values already in your code and proposes them as tokens |
| 2. Choose a direction from real references | Pick by looking at shipped products, not AI mockups | Runs a taste poll of real screens, or shows three directions on one board |
| 3. Write the rules down | Commit `DESIGN.md` | Writes `DESIGN.md`, with a section your AI reads before any UI work |
| 4. Build with the tokens | Ask your AI for the screens | `engine.py review` lists every value typed by hand, with the token to use |
| 5. Check the rendered page | Look at it at every size and theme | The opendesigner-review skill checks the page in a browser, with evidence for each finding |

*The five steps, and the part OpenDesigner takes off your hands.*

The taste poll needs your own Mobbin access. The three directions come with the optional user research step, which runs only after you say yes.

## Rules your AI can follow

OpenDesigner holds every screen to these lines from its quality bar and accessibility floors:

- **Fit the job.** A dispatch board is dense; a launch page is quiet.
- **Real content.** Real names, and numbers with units. No lorem ipsum, placeholder logo or invented proof.
- **One system.** One accent with one job, one or two typefaces, and every spacing and radius from the scale.
- **A clear first read.** One thing reads first, and each view has one primary action.
- **Every state designed:** empty, loading, error and long text, aligned at every width.
- **Restraint.** No glow, blobs, emoji icons or decoration that carries no data.
- **Motion with a job.** Things move only to explain or confirm, and reduced motion is respected.
- **The floors.** Text contrast of 4.5:1, borders and focus rings at 3:1, targets of at least 24 px, and a visible focus ring.

## The example, step by step

We wrote a six-line style sheet with that kind of drift and ran it through the engine on 2026-10-15, with Python 3.10.11. Every output below is copied from that run. Here are lines 2, 4 and 5:

```css
.btn { background: #4f46e5; color: #ffffff; border-radius: 7px; padding: 8px 16px; }
.input { border: 1px solid #d1d5db; border-radius: 7px; padding: 8px 12px; }
.card { background: #f9fafb; border-radius: 12px; padding: 24px; }
```

**It reads what is there.** The opendesigner-extract skill asks before it reads anything, and you tag the source as your own product. Then it measures the CSS and proposes values:

```
Reference our-app (our-product, code): 7 proposal(s), pending until accepted
  dials.roundness                  42  high    most common control radius 7 -> A5 band
  dials.density                    35  high    body 16.0px -> A3 bands
  raw.brandColor             "#4f46e5"  high    the person's own product: its brand color may carry over
```

Your 7 px button corners set the roundness, your 16 px body text sets the density, and your indigo stays as the brand color because the app is yours. From someone else's site, the exact color is never copied.

**You confirm.** Nothing is decided until you accept, adjust or ignore each line. Here all seven were accepted, and the decision log records each one as coming from your app. `DESIGN.md` notes that white text on the indigo reads at 6.29:1, above the 4.5:1 floor.

**Review finds the drift.** `engine.py review --project src` found 16 hard-coded values, plus 4 lines that broke a house standard because their spacing was in pixels. Part of its output:

```
  app.css:2  #4f46e5  ->  use var(--ds-color-bg-action-primary)
  app.css:2  border-radius: 7px  ->  use var(--ds-radius-control) (6px, the control radius)
  app.css:4  #d1d5db  ->  use var(--ds-color-border-separator) (closest match)
  app.css:5  border-radius: 12px  ->  use var(--ds-radius-container) (8px, the container radius)
```

"Closest match" means no token fits exactly, so you choose. For the input border, we chose `--ds-color-border-input` instead.

**You decide.** Review shows the cards' 12 px corners would become 8 px. To keep 12 px, say so. The extend skill records your reason, and the corners of dialogs move up to 16 px with it:

```
engine.py set radius.container 12 --why "cards keep the 12px corners the app has today"
```

**You fix the code.** We made the edits by hand. Your AI can make them when you ask.

{{figure:intent-vibe-before-after}}

Review again:

```
No hard-coded colors, sizes, radii, shadows or durations found: the code uses the tokens.
```

With `--strict`, review exited with an error before the edits and passed after them.

## What this can't tell you

`engine.py review` reads code, so it can't judge layout or hierarchy. The review skill checks the rendered page for those. Neither tells you whether people understand your app. Values read from a screenshot are estimates, and OpenDesigner hasn't had watched user trials yet. If a value looks wrong, adjust it, and please [report it](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).

## Next

- [Install OpenDesigner](/docs/install/) in your AI tool.
- [Start from an existing app or brand](/docs/existing-product/) for websites, screenshots, Figma files and brand books.
- No app yet? Follow [Your first design system](/docs/quickstart/).
