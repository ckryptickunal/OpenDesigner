---
title: What is a design system?
seo_title: What is a design system? A plain guide for any team
description: A design system is the set of rules for how a product looks and behaves. What goes into one, what tokens and DESIGN.md are, and how to make one with AI.
section: Concepts
order: 1
updated: 2026-10-15
---

A design system is the set of rules for how a product looks and behaves. It covers colors, text sizes, spacing, corners, depth, motion and the parts people use, like buttons and form fields. Writing the rules down keeps every screen consistent, even when different people, or different AI chats, build them.

{{figure:design-systems-parts}}

## Why teams write the rules down

Without written rules, each new screen makes its own small choices. One button gets 8 px corners and the next gets 6 px. A gray is typed in by hand and is a little off from the others. Over time the app looks slightly wrong, and nobody can say why.

{{figure:design-systems-hardcoded}}

A design system fixes this with a short list of agreed values and the reason for each one. Designers use the same values in their design tool. Engineers use them in code. AI coding tools read them before they change a screen.

{{figure:design-systems-one-source}}

## What goes into a design system

- **Color:** a palette in steps of shades, plus roles that say which shade is for text, backgrounds, borders and actions. Light and dark mode each get their own set of choices.
- **Typography:** the typefaces, a type scale (the fixed list of text sizes), and roles such as headings h1 to h6, body, label and caption.
- **Spacing:** a scale of steps, often on a 4 or 8 pixel grid, used for padding and gaps.
- **Shape:** the corner radius for controls, cards and dialogs.
- **Depth:** how surfaces stand apart, using shadows, borders or tones.
- **Motion:** how long movements take, how they speed up and slow down, and what happens when someone asks for less motion.
- **Components:** buttons, fields, cards and menus, with their states, such as hover, focus, pressed, disabled and error.
- **Brand assets:** the logo, icons, illustration, photos and voice. People make these. Rules can't.
- **Accessibility floors:** minimum contrast, minimum target sizes and a visible focus ring, so more people can read and use the product.

## What design tokens are

Design tokens are the rules saved as named values that code and tools can read. For example, `color.text.primary` might hold a dark gray, and `space.4` might hold 16 px.

The Design Tokens Community Group publishes an open format for tokens. Its first stable version, 2025.10, came out on 28 October 2025. One set of tokens can produce CSS variables, a Tailwind theme, Figma variables and native code for iOS and Android. See [Design tokens and DTCG](/docs/design-tokens/).

## What a DESIGN.md is

A `DESIGN.md` is the design system written in plain words, in a file at the root of a project. People read it, and AI coding agents can be told to read it before they change the interface. That way new screens follow the same rules. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Small app or large company

The idea is the same at any size. The difference is how much you write down.

- **A student project or a small app** may only need colors, a type scale, spacing, corners and one button. That is enough to look consistent.
- **A product team** adds components, states, dark mode and rules for how to use each part.
- **A design-system team at a large company** also decides who can change the system, how changes are announced, how components get versions, and how teams adopt it. The written reasons matter most here, because many people make changes over many years.

## How to make a design system with AI

1. **Start from what exists.** Read the current CSS, theme files, logo and fonts before deciding anything.
2. **Answer a few big questions first:** what you are making, who it is for, where it runs, how it should feel, and the brand color.
3. **Work out the scales with rules.** Color ramps that keep contrast, a type scale with a fixed ratio, and spacing steps on a grid. Rules give the same answer every time.
4. **Check accessibility with fixed rules.** WCAG 2.2 AA asks for at least 4.5:1 contrast for normal text, and targets of at least 24 by 24 CSS pixels.
5. **Write it down as files:** tokens in an open format, CSS and a `DESIGN.md`, plus a log of every decision and why it was made.
6. **Ask a person for what only a person should make:** the logo, illustration, photos and voice.

OpenDesigner follows these steps with the AI tool you already use. It is free and open source, and it is early: no watched user trials have happened yet. [See how it works](/docs/how-it-works/) or [install it](/docs/install/).

## Sources

- [Design Tokens Community Group: first stable version, 2025.10](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [WCAG 2.2: 1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum)
- [OpenDesigner research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md): the more than 500 Decision Cards behind the defaults, each with its sources
