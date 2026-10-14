---
title: Introduction
seo_title: OpenDesigner docs: make a design system with your AI tool
description: What OpenDesigner is, who it helps, and what it does not do. A free, open-source add-on that builds a design system with the AI tool you already use.
section: Getting started
order: 1
updated: 2026-10-14
---

OpenDesigner is a free, open-source (MIT) add-on that helps you make a design system with the AI tool you already use, such as Claude, ChatGPT, Codex or Cursor. A design system is the set of rules for how your app looks: colors, text sizes, spacing, corners, depth, motion and parts like buttons. OpenDesigner asks a few plain questions, suggests an answer for each with a reason, checks the result, and saves the rules as files in your project.

## What it does

- **It reads your project first.** It looks at your CSS, Tailwind config, `package.json`, token files, logo and font files. It doesn't ask what a file already answers.
- **It starts with a sketch.** Up to five questions give you a complete first version.
- **You zoom in only where you care.** Go deeper on color, text, spacing or motion, or stop. See [Zoom levels](/docs/zoom-levels/).
- **It checks its own work.** Fixed rules check contrast, target sizes, focus rings and reduced motion. Errors block the build.
- **It writes files you keep.** Design tokens in the open DTCG 2025.10 format, CSS variables, a Tailwind v4 theme, Figma variables, Paper tokens, and Swift and Jetpack Compose files.
- **It writes down every decision and its reason,** in a log and in a `DESIGN.md` that people and AI tools can read.
- **It asks you for what a person should make,** such as a logo, icons, illustration, photos or a brand typeface.

## Who it is for

### Students and beginners

You don't need to know design words. It asks one question at a time, suggests an answer, and explains each new term in one line.

### Product designers

The engine does the repetitive work: scales, tokens, states and contrast checks. You keep direction, taste and the assets only a person should make. See [For product designers](/docs/designers/).

### Engineers

You get token files and code to import, a `DESIGN.md` your coding agents can follow, and a command that finds hard-coded values. See [For engineers](/docs/engineers/).

### Design-system teams

You get a decision log with reasons, locked decisions, house and project standards, and open token files. It is early for teams: nobody has run a team pilot yet. See [For enterprise design-system teams](/docs/enterprise/).

### People with an app already built

It reads what exists, fills the gaps, and leaves a system that later changes can follow. See [Start from an existing app or brand](/docs/existing-product/).

## What it is not

- **A canvas design tool.** It doesn't draw screens the way Figma does. It writes the rules, and your AI builds with them.
- **A logo, icon, illustration or photo maker.** It asks you for these. The illustration skill can find and recolor open-licence art. It never fakes a logo.
- **A replacement for designers or for user testing.** The accessibility checks set a minimum. Automated checks catch only part of WCAG, so people who use assistive technology should still test your app.
- **A hosted service.** There is no account, web app or server. It runs inside your AI tool, and the engine runs on your computer. In the Claude app, it runs in Claude's code-execution sandbox.

## What you need

- Your own AI tool and plan. OpenDesigner is free, but the AI is not part of it. Your chat goes to your AI provider, as with any prompt.
- Python 3.10 or newer for the engine. In the Claude app, code execution must be on.

## The five skills

A skill is a set of instructions your AI tool loads when a task needs it.

- **opendesigner** creates a design system with you.
- **opendesigner-extract** learns from a website, screenshot, Figma file, repo or brand book.
- **opendesigner-extend** changes or extends a system you already made.
- **opendesigner-export** gets the system into code, Figma or Paper.
- **opendesigner-illustrate** finds open-licence illustrations, ranks them and recolors them to your tokens.

## How early it is

- The repository was created on 2026-09-23. Version 0.1.0 is planned, and there is no tagged release yet.
- No watched user trials have happened yet. The usability tests so far were role-played by AI testers.
- The packaging for each AI tool is in the repository, but a recorded test run in each tool is still to do.
- If something breaks or confuses you, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose). That is the most useful help right now.

## Where to go next

- [Install OpenDesigner](/docs/install/) in your AI tool.
- Make [your first design system](/docs/quickstart/).
- Read [how it works](/docs/how-it-works/), step by step.
- Find quick answers in the [FAQ](/docs/faq/).
