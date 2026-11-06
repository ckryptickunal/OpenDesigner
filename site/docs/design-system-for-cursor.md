---
title: A design system for Cursor
seo_title: Give Cursor your design tokens so every screen matches
description: Cursor needs three things to keep every screen consistent: design tokens, components built on them, and a rule that points at DESIGN.md. Here is each one.
section: Guides
order: 20
updated: 2026-11-07
---

To make every screen match, give Cursor three things:

1. **Design tokens:** your colors, text sizes, spacing, corners and shadows as named values, so no screen invents its own.
2. **Components built only on those tokens:** your own, or ones from OpenDesigner's optional [component library](/library/).
3. **A project rule** that tells Cursor to read `DESIGN.md` and use the tokens before any UI work.

OpenDesigner writes the first part for you: the tokens, a `DESIGN.md` with your rules in plain words, and a design system playground page that shows it all. You add the rule file below once. OpenDesigner is free and open source (MIT).

One honest note first: the packaging for Cursor is in the repository, but nobody has recorded a test run inside Cursor yet.

```
your-app/
├── .cursor/
│   └── rules/opendesigner.mdc
├── .agents/skills/opendesigner*
├── DESIGN.md
├── PRODUCT.md
├── opendesigner/
│   ├── tokens/
│   ├── build/css/tokens.css
│   ├── build/tailwind/theme.css
│   ├── decisions.md
│   └── overview.html
└── src/components/
```

*Where each file sits. You add the rule in `.cursor/rules/`. OpenDesigner writes `DESIGN.md`, `PRODUCT.md` and everything in `opendesigner/`: the tokens, CSS and Tailwind files, the decision log and `overview.html`, your design system playground. Your components use only the tokens.*

## Set it up

**1. Copy the skills into your project.** Cursor loads skills from `.agents/skills/`:

```
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

The skills come with a small Python engine that does the math. You need Python 3.10 or newer. The engine uses only Python's standard library and makes no network calls.

**2. Ask for the system.** In Cursor's agent chat, say: **"Create a design system for this project."** It reads your CSS, Tailwind config, `package.json` and token files first, and doesn't ask what they already answer. Then it asks up to five questions, each with a recommended answer and its reason. Answer in your own words, or say "just pick". Choices show as text, or as a local HTML page you open in your browser.

**3. Add the rule.** Save this as `.cursor/rules/opendesigner.mdc`:

```
---
alwaysApply: true
---

# Design system (OpenDesigner)

Before any UI, styling or visual work:
- Read @DESIGN.md and @PRODUCT.md.
- Style with the tokens in @opendesigner/build/css/tokens.css, or the Tailwind classes from @opendesigner/build/tailwind/theme.css.
- Never hard-code colors, font sizes, spacing, radii, shadows or durations.
- Reuse existing components before you make a new one. A new component uses tokens only.
- Leave locked decisions alone. If you need a value the system lacks, add it with the opendesigner-extend skill and a reason.

When you finish:
- Run `python3 .agents/skills/opendesigner/scripts/engine.py review --project src` and fix what it lists.
- Open the page in a browser at phone and desktop width, and fix what looks wrong.
```

`alwaysApply: true` puts the rule in every chat. Each `@` line points Cursor at a file instead of copying it, so the rule never goes out of date. At the end of a session, OpenDesigner also offers to add the same rules to `AGENTS.md`, which Cursor reads too. It adds them only after you say yes.

**4. Check the code.** A rule guides Cursor, but it doesn't force it. The review command checks:

```
python3 .agents/skills/opendesigner/scripts/engine.py review --project src
```

It lists every color, size, radius, shadow and duration typed straight into your code, and names the token to use instead.

{{figure:intent-cursor-loop}}

## Already have screens? Audit first

Don't let an agent restyle a working app in one go. Paste this instead:

```
Create a design system from this project's existing styles.
Audit first: read the CSS, Tailwind config and components, and list the colors,
text sizes, spacing, radii and shadows in use, with where each one comes from.
Show me the values you propose before you change any file.
Then run engine.py review and list every hard-coded value with the token to use.
Don't restyle any screen until I say yes.
```

OpenDesigner shows each proposed value with where it was measured, and nothing is decided until you accept it. [Make a vibe-coded app look professional](/docs/improve-vibe-coded-ui/) shows a full run.

## Your design system playground

`opendesigner/overview.html` is the design system playground people otherwise build by hand. It shows every color in light and dark with its contrast ratio, every text style, spacing, corners, depth, motion and the core components, all on one page. Every build rewrites it, and it works offline. Components in their states are in `opendesigner/preview/`.

Contrast is checked for you. OpenDesigner checks every text, border, icon and focus-ring color pair your tokens promise, in light and dark mode, including text on hover and pressed fills, and a failing pair stops the build.

To change the system later, just ask: "make the buttons a bit rounder". The extend skill reads the decision log first, then records the change and its reason.

## What was checked, and what wasn't

- The skill folders are in the public repository under `.agents/skills/` (checked 2026-10-15).
- Cursor's documentation lists `.agents/skills/` as a project skill folder and says Cursor reads `AGENTS.md` (checked 2026-10-15). Its rules page documents `.cursor/rules/*.mdc` files with `alwaysApply` and `@` file references (checked 2026-11-07).
- The engine on its own was tested with Python 3.10.11.
- A run inside Cursor has not been recorded yet. If you try it, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and tell us what happened.

## Next

- [Install OpenDesigner](/docs/install/) in other tools.
- [Your first design system](/docs/quickstart/), step by step.
- Already have an app? [Start from an existing app or brand](/docs/existing-product/).
