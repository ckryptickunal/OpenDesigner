---
title: How OpenDesigner builds a design system with your AI
seo_title: How OpenDesigner works: five questions to a design system
description: OpenDesigner reads your project, asks up to five plain questions, then writes design tokens, CSS, a Tailwind theme and a DESIGN.md. Every step, in order.
h1: How OpenDesigner works
updated: 2026-10-14
---

OpenDesigner is a free, open-source helper that builds a design system with the AI you already use. A design system is the set of rules for how your app looks: colors, text sizes, spacing, corners, depth, motion and the parts like buttons. OpenDesigner asks plain questions one at a time, recommends an answer with its reason, checks the result, and saves everything as files.

## The steps, from your side

1. **Add it to your AI tool.** One or two commands. See [Install](../install/).
2. **Say "Create a design system for this project."**
3. **It looks before it asks.** It reads your CSS, Tailwind config, `package.json`, token files, logo and fonts, and skips anything a file already answers.
4. **It asks once about a private log.** A step log stays on your computer, and only a clear yes turns it on.
5. **The sketch: up to five questions, one per message.** What you are making, who it is for, where it runs, how it should feel, and your brand color or logo. Each question comes with a recommended answer and its reason. Answer in your own words, or say "just pick".
6. **You get a complete first version right away.** The engine builds every token, every export, `DESIGN.md` and an overview page. On a laptop the engine part takes about two seconds.
7. **You see the whole system on one page.** `opendesigner/overview.html` shows colors with their contrast ratios, headings h1 to h6, spacing, corners, depth, motion and core components. Each area is marked Chosen, Picked for you or Default. Anything only you can give, like a logo or a voice guide, shows as "Not enough information", next to the question that fills it.
8. **Zoom in only where you care, or stop.** After each level it offers "stop here, or zoom into color, type, spacing" and more. Every level gives a working system.
9. **It checks its own work.** Contrast, target sizes, focus rings and reduced motion are checked by fixed rules before the AI gives any opinion. Errors block the build.
10. **It writes everything down.** Every decision is logged with how it was set and why, so a later session doesn't quietly undo it. It asks before adding a short note to your `AGENTS.md`.

## The four zoom levels

- **Sketch:** up to five questions. A complete system that works.
- **Broad:** one short screen per foundation (color, type, space, shape, depth, motion).
- **Defined:** one area at a time, only where you want more control.
- **Detailed:** every choice the research covers, for teams that need it.

You can stop at any level. Nobody has to pick a mode up front.

## What you get

- `DESIGN.md`: your design rules in plain words, for people and AI tools.
- `opendesigner/tokens/`: the rules as named values in the open DTCG 2025.10 format, with light, dark, three densities and reduced motion as modes.
- `opendesigner/build/`: CSS variables, a Tailwind v4 theme, Figma variables, Paper tokens, Swift and Jetpack Compose files, and Claude Design System artifact files.
- `opendesigner/overview.html`: the whole system on one page, including what is still missing. It works offline.
- `opendesigner/preview/`: the visual templates (palette, type scale, spacing, corners, depth, motion, components) filled with your own values.
- `opendesigner/decisions.md`: every decision and its reason, append-only.

## What it checks

Every system gets WCAG 2.2 AA text contrast (4.5:1 for body text, 3:1 for large text), 3:1 for borders and focus rings, minimum target sizes (24 CSS px on the web, 44 pt on iOS, 48 dp on Android), a visible focus ring and reduced motion. These are a floor, not a certificate: automated checks catch only part of WCAG, so test with real people too.

## What it asks you for

OpenDesigner makes what can be made from rules: color ramps, type and spacing scales, radius, depth, motion and component states. It asks a person for what a person should make: the logo, custom icons, illustration, photography, a brand typeface and the voice. It never fakes your logo, and it never copies another brand's identity from a reference.

## Where the defaults come from

The defaults rest on 352 Decision Cards: one design decision each, with its options, a default and its sources. A verification pass re-checked 161 claims against live sources, and the fixes are logged. The research is in the repository, and you can [read it](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).
