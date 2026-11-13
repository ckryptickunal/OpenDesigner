---
title: Design tokens for Claude Code
seo_title: A Claude Code skill for design tokens, CSS and Tailwind
description: OpenDesigner is a free Claude Code skill that writes DTCG design tokens, CSS variables, a Tailwind v4 theme and a DESIGN.md Claude follows.
section: Guides
order: 21
updated: 2026-11-07
---

OpenDesigner is a free, open-source Claude Code skill for design systems. Install the plugin, which adds OpenDesigner's skills, and answer up to five questions. You get design tokens, CSS variables, a Tailwind v4 theme and a `DESIGN.md` that tells Claude how to use them. One line in `CLAUDE.md` makes every later session read it, and a review command checks that it did.

It also checks contrast as it builds: every text, border, icon and focus-ring color pair your tokens promise, in light and dark mode, including text on hover and pressed fills. A pair under 4.5:1 for text, or 3:1 for borders, icons and focus rings, stops the build.

## Install the plugin

In Claude Code, add the repository as a plugin marketplace, then install the plugin:

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

The plugin installs nine skills. Start a new session afterwards, because skills load when a session starts. The install from GitHub was tested on 2026-10-21, and the manifest passes `claude plugin validate .` with one warning, about the repository's own `CLAUDE.md`.

In the desktop app's Code tab, `/plugin` may not run, and the Claude app installs the same Claude skill from a zip. [Install](/docs/install/) has both.

Then open your project and say: **"Create a design system for this project."** It reads your files first, then asks up to five questions, each with a recommended answer and its reason. Choices show as an artifact or a local HTML page.

## Point Claude at DESIGN.md

`DESIGN.md` ends with a section for AI agents: read this file and the tokens before changing any screen, use tokens instead of raw values, and leave locked decisions alone. OpenDesigner offers to add the same rules to `AGENTS.md`, and adds them only after you say yes.

| File | Who reads it | What it holds |
|---|---|---|
| `DESIGN.md` | You, your team and every AI tool | Your design rules in plain words, written by OpenDesigner |
| `AGENTS.md` | Claude Code, when there is no `CLAUDE.md`; Cursor, Codex and other agents | OpenDesigner's short note |
| `CLAUDE.md` | Claude Code, every session | One line, `@AGENTS.md`, if you already have a `CLAUDE.md` |

*Which file each tool reads, and what goes in it.*

If you already have a `CLAUDE.md`, Claude Code (version 2.1.277 or later) skips `AGENTS.md`. Add this line to `CLAUDE.md` so the note loads too:

```
@AGENTS.md
```

**Review is the check.** Claude Code's documentation says these files are context, not enforced configuration. So the note tells Claude to run `engine.py review` at the end of each piece of work. It lists colors, sizes, radii, shadows and durations typed straight into your code, and names the token to use instead:

```
app.css:2  #4f46e5  ->  use var(--ds-color-bg-action-primary)
app.css:2  border-radius: 7px  ->  use var(--ds-radius-control) (6px, the control radius)
```

Those lines are from a test run on 2026-10-15. [Make a vibe-coded app look professional](/docs/improve-vibe-coded-ui/) shows the whole run.

## The tokens

A design token is a named value, such as the corner radius of a button. The tokens live in `opendesigner/tokens/`, in 11 files:

- **Primitives:** the raw scales, such as every color and spacing step.
- **Semantic tokens:** roles that point to a primitive, such as `radius.control` for buttons and inputs.
- **Modes:** light and dark, three densities, and standard and reduced motion, each in its own file.
- **A resolver** that ties the modes together.

The format is DTCG 2025.10, the open format from the W3C Design Tokens Community Group. Other token tools that read DTCG can use these files, though we haven't tested one yet.

{{figure:intent-token-chain}}

## Wire it in

Import the CSS once, or add the Tailwind theme, and every color, size and corner in your app comes from the tokens. Review can also fail a script when it finds a raw value.

:::dev
**CSS variables.** `opendesigner/build/css/tokens.css` holds every token as a custom property, named `--ds-...`. Import it once at the root of your app:

```css
@import "../opendesigner/build/css/tokens.css";

.card {
  background: var(--ds-color-surface-raised);
  border-radius: var(--ds-radius-container);
}
```

Dark mode follows the system setting, and `data-theme="light"` or `data-theme="dark"` overrides it. `data-density` switches density, and reduced motion follows the system setting.

**Tailwind v4.** Add two lines to your main CSS file and adjust the path:

```css
@import "tailwindcss";
@import "../opendesigner/build/tailwind/theme.css";
```

Classes follow the token roles: `bg-action-primary`, `text-fg-primary`, `rounded-control`. By default the theme switches off Tailwind's own colors, text sizes, radii and shadows, so a stray `bg-blue-600` adds no style. `DESIGN.md` lists the classes.

**Review.** Add `--strict` to `engine.py review` to make it fail when it finds anything. Swift, Jetpack Compose, Figma variables, Paper and a DTCG resolver file come from the same build: see [For engineers](/docs/engineers/).
:::

## Not yet

- No direct React Native or Flutter export.
- The overview page draws only buttons, a text field and a card. The optional [component library](/library/) has 104 finished components built on the tokens, including empty, loading and error states.
- No watched user trials yet.

## Next

- [Install OpenDesigner](/docs/install/) in other tools.
- [Your first design system](/docs/quickstart/), step by step.
- Already have an app? [Start from an existing app or brand](/docs/existing-product/).
