---
title: Design tokens for Claude Code
seo_title: Design tokens for Claude Code: DTCG, CSS and Tailwind v4
description: Install the OpenDesigner plugin in Claude Code and get DTCG 2025.10 design tokens, CSS variables and a Tailwind v4 theme, plus a DESIGN.md Claude follows.
section: Guides
order: 21
updated: 2026-10-15
---

Install OpenDesigner as a Claude Code plugin, answer up to five questions, and you get design tokens in the open DTCG 2025.10 format. You also get CSS variables and a Tailwind v4 theme made from them. A `DESIGN.md` and an optional note in `AGENTS.md` tell Claude Code to use those tokens in later sessions, and a review command checks that it did.

## Install the plugin

In Claude Code, add the repository as a plugin marketplace, then install the plugin:

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

The plugin has eight skills. Its manifest passes Claude Code's own check, `claude plugin validate .`, with one warning: the repository's `CLAUDE.md` isn't loaded as plugin context (checked 2026-10-15). An install in a fresh Claude Code session has not been recorded yet.

Then open your project and say: **"Create a design system for this project."** OpenDesigner reads your files first, then asks up to five questions. Each comes with a recommended answer and its reason. In Claude Code it can show choices as an artifact or as a local HTML page.

## The tokens

A design token is a named value, such as the corner radius of a button. The tokens live in `opendesigner/tokens/`, in 11 files:

- **Primitives:** the raw scales, such as every color step, spacing step and radius.
- **Semantic tokens:** roles that point to a primitive, such as `radius.control` for buttons, inputs and selects.
- **Modes:** light and dark colors, three densities, and standard and reduced motion, each in its own file.
- **A resolver,** `opendesigner.resolver.json`, that ties the modes together.

The format is DTCG 2025.10, the open format from the W3C Design Tokens Community Group. Other token tools that read DTCG can use these files, though we haven't tested one yet.

{{figure:intent-token-chain}}

Never edit an export by hand. Change the decision and rebuild, and every export updates together.

## CSS variables

`opendesigner/build/css/tokens.css` holds every token as a CSS custom property, named `--ds-...`. Import it once at the root of your app:

```css
@import "../opendesigner/build/css/tokens.css";

.card {
  background: var(--ds-color-surface-raised);
  border-radius: var(--ds-radius-container);
}
```

Dark mode follows the system setting, and `data-theme="light"` or `data-theme="dark"` overrides it. `data-density` switches density, and reduced motion follows the system setting.

## Tailwind v4

Add two lines to your main CSS file and adjust the path:

```css
@import "tailwindcss";
@import "../opendesigner/build/tailwind/theme.css";
```

Classes follow the token roles: `bg-action-primary`, `text-fg-primary`, `rounded-control`. By default the theme switches off Tailwind's own colors, text sizes, radii and shadows, so a stray `bg-blue-600` adds no style. `DESIGN.md` lists the classes.

Other exports come from the same build: Swift, Jetpack Compose, Figma variables, Paper and a DTCG resolver file. See [For engineers](/docs/engineers/).

## How Claude Code keeps using them

**DESIGN.md** has a section for AI agents. It says to read the file and the tokens before changing any screen, to use tokens instead of raw values, and to leave locked decisions alone.

**The AGENTS.md note** repeats those rules for every later session. OpenDesigner asks before adding it. One detail matters here. Claude Code (version 2.1.277 or later) reads `AGENTS.md` on its own only when your project has no `CLAUDE.md`. If you have one, add this line to your `CLAUDE.md`, so the note loads too:

```
@AGENTS.md
```

OpenDesigner's own repository works this way.

**Review is the check.** Claude Code's documentation says these files are context, not enforced configuration. So at the end of a piece of work, the note tells Claude to run `engine.py review`. It lists colors, sizes, radii, shadows and durations typed straight into your code, and names the token to use instead:

```
app.css:2  #4f46e5  ->  use var(--ds-color-bg-action-primary)
app.css:2  border-radius: 7px  ->  use var(--ds-radius-control) (6px, the control radius)
```

Those two lines are from a test run on 2026-10-15. Add `--strict` to make the command fail when it finds anything. [Improve a vibe-coded UI](/docs/improve-vibe-coded-ui/) shows the whole run.

## Not yet

- No direct React Native or Flutter export.
- Only buttons, a text field and a card are previewed as components.
- No watched user trials yet.

## Next

- [Install OpenDesigner](/docs/install/) in other tools.
- [Your first design system](/docs/quickstart/), step by step.
- Already have an app? [Start from an existing app or brand](/docs/existing-product/).
