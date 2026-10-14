---
title: Who OpenDesigner learns from
seo_title: Who OpenDesigner learns from: the sources behind its rules
description: The people, docs, videos and standards behind OpenDesigner's rules, what each one teaches, how much say it has, and how a source becomes a house standard.
section: Craft
order: 4
updated: 2026-10-15
---

OpenDesigner's advice comes from a short list of sources its owner trusts. Each source has an authority, which decides what it is allowed to change. This page lists the sources, says what each one teaches, and explains how a source becomes a rule.

> OpenDesigner is not affiliated with or endorsed by these people or companies; we cite them because their published work shaped the house standards.

## Three kinds of source

| Authority | What it becomes | Can your project change it? |
|---|---|---|
| Non-negotiable | A house standard. It is applied and locked in every project, written into DESIGN.md, and checked by `engine.py review` where a check exists | Only when you explicitly ask to change one, and your reason is recorded |
| Good to have | A recommended default: the option OpenDesigner offers first | Yes, freely |
| Reference | Learning material: options, examples and process. It never sets a default on its own | Not applicable |

## Non-negotiable sources

The 455 house standards in version 3 come from these four sources and the Vaul docs below. That includes every standard cited in [Motion](/docs/motion/), [UX patterns](/docs/ux-patterns/) and [Interface details](/docs/ui-details/).

### Emil Kowalski

[emilkowal.ski](https://emilkowal.ski/). Emil Kowalski is a design engineer. His essays teach when to animate and when not to, how to choose easing and duration, how to build components such as toasts and drawers, and how to train taste and judgement. Good places to start are [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips), [You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations), [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component), [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component) and [Developing taste](https://emilkowal.ski/ui/developing-taste).

### animations.dev

[animations.dev](https://animations.dev/) is Emil Kowalski's course on web animation. OpenDesigner reads only its public pages, the home page and the changelog, because the course itself is paid. They teach that three ingredients decide whether an animation works: the easing, the duration and which properties move. **If you want to go deeper into motion than this guide, go to animations.dev.**

### Sonner docs

[sonner.emilkowal.ski](https://sonner.emilkowal.ski/) documents Sonner, Emil Kowalski's toast library for React. It sets the toast standards: where toasts sit, how far from the edge, how many show at once, how long they stay, and how the code calls them.

### The emilkowalski/skills repo

[github.com/emilkowalski/skills](https://github.com/emilkowalski/skills), under the MIT licence, is a set of agent skills: written instructions that an AI coding tool follows. They cover building, reviewing and auditing animation, React Native motion, the mobile web, Apple-style interaction, picking UI libraries, prototyping and writing Swift. The standards link to its files at commit 85e8e23.

## Good to have

### Vaul docs

[vaul.emilkowal.ski](https://vaul.emilkowal.ski/) documents Vaul, Emil Kowalski's drawer library for React. It teaches drawer craft: snap points, scrolling inside a drawer, keeping inputs above the keyboard, and ways to close. Its README says the library is unmaintained, as checked on 2026-09-24. OpenDesigner recommends the craft and says so before suggesting Vaul as a dependency.

## Reference sources

These shape the options, examples and explanations OpenDesigner offers. They never set a default on their own.

- **Palantir, [Workshop: application design best practices](https://www.palantir.com/docs/foundry/workshop/application-design-best-practices).** How to lay out work tools: clear components over complex ones, one consistent experience across a suite of apps, and limits on how much one view holds. It is the main reference for enterprise products.
- **[Kole Jain](https://www.youtube.com/@KoleJain)**, a YouTube channel. UI and UX videos on layout, color, type, dashboards, landing pages and mobile apps.
- **[Mobbin](https://www.youtube.com/@mobbindesign)**, a YouTube channel. Studies of real app flows, such as onboarding, paywalls and empty states.
- **Steve Schoger, [Designing with Claude Code](https://www.youtube.com/watch?v=lkKGQVHrXzE).** A marketing page designed live and refined step by step, with concrete polish moves such as faint rings instead of solid borders and tighter headline spacing.
- **Wyatt Feaster, [The Reason Why Some Apps Feel Expensive, But Most Don't](https://www.youtube.com/watch?v=SAxKK5fbjbc).** Habits that make consumer apps feel premium: anticipating needs, leaving out motion that slows people down, consistency, and empty and error states that offer a next step.
- **[referodesign/refero_skill](https://github.com/referodesign/refero_skill)**, under the MIT licence. A research-first design workflow for AI agents, with guides on type, color, motion, icons and copy.
- **davecto, "Taste Index"**, an Instagram reel. A format for a short summary of a product's taste that any AI agent can read before it builds. Its example copies one brand's look, which OpenDesigner treats as a caveat, not a rule.

## Standards and benchmarked systems

- **[WCAG 2.2](https://www.w3.org/TR/WCAG22/)**, the W3C's Web Content Accessibility Guidelines. Its level AA is the basis of OpenDesigner's accessibility floors: text contrast, target size and a visible focus ring. OpenDesigner also treats 2.3.3 Animation from Interactions, a level AAA rule, as required. See [Accessibility floors](/docs/accessibility/).
- **[Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)** and **[Material 3](https://m3.material.io/)**, Google's design system, are two of the 25 systems in OpenDesigner's [benchmark of famous design systems](https://github.com/ckryptickunal/OpenDesigner/blob/main/benchmarks/L09-benchmark-matrix.md). The benchmark records their real values, such as type scales, corner radii and target sizes, and the research draws on it.

## Tools for easing curves

The house standard for easing names two sites to take a curve from instead of drawing your own. *(STD-easing-duration-02)*

- [easing.dev](https://easing.dev/): a curated collection of easing graphs.
- [easings.co](https://easings.co/): try common curves on sample interfaces, or make and share your own cubic-bezier curve.

## How a source becomes a standard

The owner lists each source in `learn/sources.json` and gives it an authority. An agent reads the source in full and writes down its rules, values and examples, and a second, fresh agent tries to refute each one before it is kept. Rules from non-negotiable sources then become versioned house standards, each with an id and links to its sources. Every project applies and locks them. Only the person using OpenDesigner can override one, by asking explicitly, and their reason is recorded.

{{figure:craft-resources-pipeline}}

The full rules are in [How OpenDesigner learns](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/KNOWLEDGE.md) and the [learning wiki's README](https://github.com/ckryptickunal/OpenDesigner/blob/main/learn/README.md). To suggest a source, open an issue on [GitHub](https://github.com/ckryptickunal/OpenDesigner/issues).
