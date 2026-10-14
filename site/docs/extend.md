---
title: Change or extend a system
seo_title: Change or extend a design system with OpenDesigner
description: How the opendesigner-extend skill changes a design system safely: it reads past decisions and locks first, asks only about what is new, and checks the result.
section: Guides
order: 5
updated: 2026-10-14
---

To change a design system you made with OpenDesigner, ask your AI for the change. The opendesigner-extend skill takes over when your project already has an `opendesigner/` folder. It reads your past decisions and locks first, asks only about what is new, records the change with its reason, and rebuilds every file.

## When it runs

It runs when `opendesigner/state.json` exists, or when the root `DESIGN.md` was made by OpenDesigner. Common requests:

- "Add a date picker" or "build the settings page."
- "Make the buttons a bit rounder."
- "Let's define the colors properly."
- "Add dark mode" or "we need Android too."
- "Why is this blue?"

## What it reads first

Before it touches anything, it reads, in order:

1. `DESIGN.md` and `PRODUCT.md`, including how far each area was zoomed.
2. `opendesigner/state.json`: your answers, the zoom levels and the locks.
3. `opendesigner/decisions.md`, newest entries last.
4. The token files in `opendesigner/tokens/`.
5. Recent git history for these files, if the project uses git.

Then it runs the checks. `engine.py validate` checks the system, and `engine.py review` looks for drift in your code. If either finds a problem, it tells you first, because fixing it may be the real task.

It then sums up in three lines or fewer: the direction, the zoom level of the area you care about, and anything locked or still open. It never re-runs the whole interview.

In a chat-only tool, it asks you to upload `state.json`, `decisions.md` and `DESIGN.md` before it changes anything.

## How it sorts a request

- **A new component or page.** It builds it from existing tokens only, lists the tokens it used, and adds states and keyboard behavior.
- **One decision,** such as rounder buttons. It finds the matching question, shows the current value and the options, and records your pick.
- **Zooming in,** such as defining colors properly. It runs the next zoom level for that area. See [Zoom levels](/docs/zoom-levels/).
- **A reopened area,** such as a new brand color or a new platform. It asks that area's questions at its current zoom level.
- **A new direction,** such as "make it more playful". This touches most decisions. It says what would move, offers safe choices and risky ones, and changes nothing without a clear yes.
- **A question,** such as "why is this blue?" It answers from the decision log and the standards, and changes nothing.
- **A value the system lacks.** It adds a new token through the engine with a reason, and never hard-codes it.

## Locks and conflicts

- A locked value changes only with the owner's explicit OK. The skill names the lock and asks.
- If a request clashes with an earlier decision, it shows both and you choose. The new decision replaces the old one in the log, and nothing is deleted.
- A value set by a standard changes only when you explicitly ask to change that standard. You can change one value, or add your own project standard that wins over it. See [For enterprise design-system teams](/docs/enterprise/).

## Making the change

1. **It shows the change first:** the current value, the new value, and what else moves.
2. **It records it** with `engine.py set` and your reason. It adds a lock if you want one.
3. **It rebuilds** with `engine.py build`, which checks the system and rewrites the exports, `DESIGN.md` and the preview. It fixes errors before showing you anything.
4. **It shows what changed:** a short list of the values that moved.

### Adding a token

When the work needs a value the system doesn't have, it first checks that no existing token fits. Reusing a token is better than making a near-copy. Then it adds the new one with a plain name for its role:

```
engine.py set color.bg.highlight '"#fff4c2"' --why "highlighted search matches"
engine.py set dark:color.bg.highlight '"#3a3000"' --why "the same highlight in dark mode"
engine.py build
```

A new color still has to pass the contrast check.

## After building anything

At the end of any page, component or refactor, it:

1. runs `engine.py review`;
2. re-reads the `DESIGN.md` sections it touched;
3. adds a decision for every new value the work needed;
4. fixes the drift that review lists, with your OK.

The review reads code. It can't see the page, so the skill also checks the page as it renders.

## A note for your team

It ends with a change note that takes about 20 seconds to read:

```
Design system change, 2026-10-14
What changed: control corner radius, 6px -> 8px
Why: buttons felt too sharp next to the cards
Affects: radius.control, buttons, inputs
Validation: pass
Decision log: opendesigner/decisions.md, D-0012
```

The values above are an example.

## Using a different AI tool later

You can make the change in a different AI tool from the one you started in. The engine gives the same result for the same `state.json`, and the extend skill reads the same files. This is meant to keep the system consistent across sessions and tools. We have not recorded a test of it in each tool yet.

## What is early

The extend skill has had no watched user trials yet. If a step was missing or confusing, tell your AI. It saves a note and gives you a ready-to-file GitHub link, and nothing is posted unless you submit it.
