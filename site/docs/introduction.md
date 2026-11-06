---
title: Introduction
seo_title: OpenDesigner docs: make a design system with your AI tool
description: What OpenDesigner is, who it helps, and what it does not do. A free, open-source add-on that builds a design system with the AI tool you already use.
section: Getting started
order: 1
updated: 2026-11-07
---

OpenDesigner is a free, open-source (MIT) add-on that helps you make a design system with the AI tool you already use, such as Claude, ChatGPT, Codex or Cursor. A design system is the set of rules for how your app looks: colors, text sizes, spacing, corners, motion and parts like buttons. OpenDesigner asks a few plain questions, suggests an answer for each with a reason, checks the result, and saves the rules as files in your project.

To see the whole system drawn on one page, open [How OpenDesigner works](/tour/).

{{figure:index-how-it-works}}

## What it does

- **It reads your project first,** and doesn't ask what a file already answers.
- **It starts with a sketch.** Up to five questions give you a complete first version. Then you [zoom in](/docs/zoom-levels/) only where you care, or stop.
- **It checks its own work.** Fixed rules check contrast, target sizes, focus rings and reduced motion. Errors block the build.
- **It writes files you keep:** design tokens in the open DTCG format, Figma variables, and code for the platforms you use ([Export](/docs/export/)).
- **It writes down every decision and its reason,** in a log and in a `DESIGN.md` that people and AI tools can read.
- **It asks you for what a person should make,** such as a logo, icons, photos or a brand typeface.

## Who it is for

- **Students and beginners.** You don't need to know design words. It asks one question at a time, suggests an answer, and explains each new term in one line.
- **Product designers.** The engine does the repetitive work: scales, tokens, states and contrast. You keep direction, taste and the assets only a person should make. See [For product designers](/docs/designers/).
- **Engineers.** Token files and code to import, a `DESIGN.md` your coding agents follow, and a command that finds hard-coded values. See [For engineers](/docs/engineers/).
- **Design-system teams.** A decision log with reasons, locked decisions, and house and project standards. It's early for teams: nobody has run a team pilot yet. See [For enterprise design-system teams](/docs/enterprise/).
- **People with an app already built.** It reads what exists and fills the gaps. See [Start from an existing app or brand](/docs/existing-product/).

{{figure:index-question-card}}

## What it is not

- **A canvas design tool.** It writes the rules, and your AI builds with them.
- **A logo, icon or photo maker.** It asks you for these and never fakes a logo. The illustrate skill can find open-licence art.
- **A replacement for designers or user testing.** Automated checks catch only part of WCAG, so people who use assistive technology should still test your app.
- **A hosted service.** There is no account or server. It runs inside your AI tool, and the engine runs on your computer.

## What you need

- Your own AI tool and plan. Your chat goes to your AI provider, as with any prompt.
- Python 3.10 or newer for the engine. In the Claude app, turn code execution on.

## The eight skills

A skill is a set of instructions your AI tool loads when a task needs it.

- **opendesigner** creates a design system with you.
- **opendesigner-extract** learns from a website, screenshot, Figma file, repo or brand book.
- **opendesigner-extend** changes a system you already made.
- **opendesigner-export** gets it into code, Figma or Paper.
- **opendesigner-illustrate** finds open-licence art and photos, recolors art to your tokens, and draws more icons like the few you have.
- **opendesigner-review** checks a built interface at every screen size and theme, with evidence for each finding.
- **opendesigner-paint** paints original art in code, in your palette: hero films, loops and stills.
- **opendesigner-preflight** checks anything visual before you share it, for the small mistakes that make it look cheap.

## How early it is

- Version 0.2.0, the first tagged release, came out on 5 November 2026.
- No watched user trials yet: the usability tests so far were role-played by AI testers. A recorded run in each AI tool is still to do.
- If something breaks or confuses you, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose). It's the most useful help right now.

## Where to go next

[Install OpenDesigner](/docs/install/), then make [your first design system](/docs/quickstart/). For the detail, read [how it works](/docs/how-it-works/) or the [FAQ](/docs/faq/).
