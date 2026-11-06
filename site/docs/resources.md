---
title: Who OpenDesigner learns from
seo_title: Who OpenDesigner learns from: the sources behind its rules
description: The people, docs, videos and standards behind OpenDesigner's rules, what each one teaches, how much say it has, and how a source becomes a house standard.
section: Craft
order: 4
updated: 2026-11-07
---

OpenDesigner's advice comes from a short list of trusted sources. Each has an authority, which decides what it is allowed to change.

> OpenDesigner is not affiliated with or endorsed by these people or companies; we cite them because their published work shaped the house standards.

## Three kinds of source

| Authority | What it becomes | Can your project change it? |
|---|---|---|
| Non-negotiable | A house standard: applied and locked in every project, written into DESIGN.md, and checked by `engine.py review` where a check exists | Only when you explicitly ask, and your reason is recorded |
| Good to have | A recommended default: the option OpenDesigner offers first | Yes, freely |
| Reference | Learning material: options, examples and process. It never sets a default on its own | Not applicable |

## Non-negotiable sources

The 457 house standards in version 4 come from these four sources, the Vaul docs below and two rules of OpenDesigner's own: a color with a known meaning keeps it, and a product never pairs pure white with pure black. They include every standard cited in [Motion](/docs/motion/), [UX patterns](/docs/ux-patterns/) and [Interface details](/docs/ui-details/).

### Emil Kowalski

[emilkowal.ski](https://emilkowal.ski/). A design engineer whose essays teach when to animate, how to choose easing and duration, how to build toasts and drawers, and how to train taste. Start with [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips), [You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations), [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component), [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component) and [Developing taste](https://emilkowal.ski/ui/developing-taste).

### animations.dev

[animations.dev](https://animations.dev/) is his paid course on web animation; OpenDesigner reads only its public pages. **To go deeper into motion than this guide, go there.**

### Sonner docs

[sonner.emilkowal.ski](https://sonner.emilkowal.ski/) documents Sonner, his toast library for React, and sets the toast standards: placement, edge distance, how many show, how long they stay and how code calls them.

### The emilkowalski/skills repo

[github.com/emilkowalski/skills](https://github.com/emilkowalski/skills), under the MIT licence: agent skills, written instructions an AI coding tool follows, for animation, mobile, Apple-style interaction, UI libraries, prototyping and Swift.

## Good to have

### Vaul docs

[vaul.emilkowal.ski](https://vaul.emilkowal.ski/) documents Vaul, his drawer library for React: snap points, scrolling inside a drawer, keeping inputs above the keyboard, and ways to close. Its README says the library is unmaintained (checked on 2026-09-24), so OpenDesigner recommends the craft and says so before suggesting Vaul as a dependency.

## Reference sources

These shape the options, examples and explanations OpenDesigner offers. They never set a default on their own.

- **Palantir, [Workshop: application design best practices](https://www.palantir.com/docs/foundry/workshop/application-design-best-practices).** The main reference for work tools: clear components, one consistent experience across apps, and limits on how much one view holds.
- **[Kole Jain](https://www.youtube.com/@KoleJain)**, a YouTube channel: UI and UX videos on layout, color, type, dashboards, landing pages and mobile apps.
- **[Mobbin](https://www.youtube.com/@mobbindesign)**, a YouTube channel: studies of real app flows, such as onboarding, paywalls and empty states.
- **Steve Schoger, [Designing with Claude Code](https://www.youtube.com/watch?v=lkKGQVHrXzE).** A marketing page refined live, with polish moves such as faint rings instead of solid borders and tighter headline spacing.
- **Wyatt Feaster, [The Reason Why Some Apps Feel Expensive, But Most Don't](https://www.youtube.com/watch?v=SAxKK5fbjbc).** What makes consumer apps feel premium: anticipating needs, no motion that slows people down, consistency, and empty and error states with a next step.
- **[referodesign/refero_skill](https://github.com/referodesign/refero_skill)**, under the MIT licence: a research-first design workflow for AI agents.
- **davecto, "Taste Index"**, an Instagram reel: a short summary of a product's taste that any AI agent can read before it builds. Its example copies one brand's look, which OpenDesigner treats as a caveat, not a rule.

## Standards and benchmarked systems

- **[WCAG 2.2](https://www.w3.org/TR/WCAG22/)**, the W3C's accessibility guidelines. Level AA is the basis of the [accessibility floors](/docs/accessibility/): text contrast, target size and a visible focus ring. OpenDesigner also requires 2.3.3 Animation from Interactions, a level AAA rule.
- **[Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)** and Google's **[Material 3](https://m3.material.io/)** are two of the 32 systems in OpenDesigner's [benchmark](https://github.com/ckryptickunal/OpenDesigner/blob/main/benchmarks/L09-benchmark-matrix.md), which records their real type scales, corner radii and target sizes.

The house standard for easing (STD-easing-duration-02) names two sites to take a curve from: [easing.dev](https://easing.dev/) and [easings.co](https://easings.co/).

## How a source becomes a standard

{{figure:craft-resources-pipeline}}

Sources and their authority are listed in `learn/sources.json`. Only you can override a standard, by asking explicitly, and your reason is recorded.

The full rules are in [How OpenDesigner learns](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/KNOWLEDGE.md) and the [learning wiki's README](https://github.com/ckryptickunal/OpenDesigner/blob/main/learn/README.md). To suggest a source, open an issue on [GitHub](https://github.com/ckryptickunal/OpenDesigner/issues).
