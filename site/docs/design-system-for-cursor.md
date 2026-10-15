---
title: A design system for Cursor
seo_title: Design system for Cursor: tokens, Tailwind and DESIGN.md
description: Add OpenDesigner's skills to a Cursor project, ask for a design system, and get tokens, CSS, a Tailwind theme and a DESIGN.md the agent keeps following.
section: Guides
order: 20
updated: 2026-10-15
---

Copy OpenDesigner's skills into your project, ask Cursor's agent for a design system, and you get files it can follow in every later chat. You get tokens, CSS variables, a Tailwind v4 theme and a `DESIGN.md` with the rules in plain words. OpenDesigner is free and open source (MIT).

One honest note first. The packaging for Cursor is in the repository, but nobody has recorded a test run inside Cursor yet. The end of this page says what was checked.

{{figure:intent-cursor-loop}}

## Install it in your project

Cursor loads skills from a folder called `.agents/skills/` in your project. Copy the OpenDesigner skills there:

```
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

That copies eight skill folders. The main one, `opendesigner`, runs the interview. Others learn from your existing code, change the system later, or export it.

The skill comes with a small Python engine that does the math. Cursor's agent runs it in your terminal, so you need Python 3.10 or newer. The engine uses only Python's standard library and makes no network calls.

## What you ask

In Cursor's agent chat, say: **"Create a design system for this project."** Cursor picks a skill by its description. You can also type `/` and choose `opendesigner` yourself.

It looks before it asks. It reads your CSS, Tailwind config, `package.json` and any token files, and it doesn't ask what a file already answers. Then it asks up to five questions, one per message: what you are making, who it is for, where it runs, how it should feel, and your brand color or logo. Each comes with a recommended answer and its reason. Answer in your own words, or say "just pick".

OpenDesigner can't show its picture choices inside Cursor's chat yet. Instead, it shows choices as text, or writes a local HTML page you open in your browser.

## What you get

- `DESIGN.md`: your design rules in plain words, with a section written for AI agents.
- `PRODUCT.md`: what the product is and who it is for.
- `opendesigner/tokens/`: the rules as named values in the open DTCG 2025.10 format.
- `opendesigner/build/css/tokens.css` and `opendesigner/build/tailwind/theme.css`, plus Swift, Jetpack Compose and Figma files.
- `opendesigner/decisions.md`: every choice and why it was made.
- `opendesigner/overview.html`: the whole system on one page.

On 2026-10-15, a fresh run of the engine wrote 50 files. It checked the contrast of 164 color pairs across 12 combinations of light and dark, density and motion. A contrast error stops the build.

## How Cursor keeps following it

Two things carry the system into later chats.

**DESIGN.md.** Its last section tells AI agents to read the file and the tokens before changing any screen. It also tells them to use tokens instead of raw values, and to leave locked decisions alone.

**A note in AGENTS.md.** At the end, OpenDesigner asks whether to add a short note to your `AGENTS.md`. It adds it only after you say yes. Cursor reads `AGENTS.md` at your project root. The note tells the agent to:

- read `DESIGN.md` and `PRODUCT.md` before any visual work;
- never hard-code colors, sizes, spacing, radii, shadows or durations;
- run `engine.py review` at the end of every piece of work and fix what it finds.

Instructions guide an agent, but they don't force it. So the real check is a command:

```
python3 .agents/skills/opendesigner/scripts/engine.py review --project src
```

It lists every color, size, radius, shadow and duration typed straight into your code, and names the token to use instead. With `--strict`, it exits with an error when it finds anything. A script can stop on that.

To change the system later, just ask: "make the buttons a bit rounder". The extend skill reads the decision log first, then records the change and its reason.

## What was checked, and what wasn't

- The eight skill folders are in the public repository under `.agents/skills/` (checked 2026-10-15).
- Cursor's documentation lists `.agents/skills/` as a project skill folder and says Cursor supports `AGENTS.md` (checked 2026-10-15).
- The engine on its own was tested with Python 3.10.11.
- A run inside Cursor has not been recorded yet. If you try it, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and tell us what happened.

## Next

- [Install OpenDesigner](/docs/install/) in other tools.
- [Your first design system](/docs/quickstart/), step by step.
- Already have an app? [Start from an existing app or brand](/docs/existing-product/).
