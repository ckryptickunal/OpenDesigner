---
title: What is a design system? A plain guide, with AI
seo_title: What is a design system? A plain guide (with AI)
description: A design system is the rules for how your app looks: color, type, spacing, corners, depth, motion and components. What goes in one and how to make one with AI.
h1: What is a design system?
updated: 2026-10-14
type: article
---

**A design system is the set of rules for how a product looks and behaves.** It covers colors, text sizes, spacing, corners, depth, motion and the parts people use, like buttons and form fields. Writing the rules down keeps every screen consistent, even when different people, or different AI chats, build them.

## What goes into a design system

- **Color:** a palette in ramps of shades, plus roles that say which shade is for text, backgrounds, borders and actions, in light and dark mode.
- **Typography:** the typefaces, a type scale (the fixed list of sizes), and roles like display, headings h1 to h6, body, label and caption.
- **Spacing:** a scale of steps, often on a 4 or 8 pixel grid, used for padding and gaps.
- **Shape:** corner radius for controls, cards and dialogs.
- **Depth:** how surfaces separate, with shadows, borders or tones.
- **Motion:** durations and easing curves, and what happens when someone asks for reduced motion.
- **Components:** buttons, fields, cards, menus and their states (hover, focus, pressed, disabled, error).
- **Brand assets:** the logo, icons, illustration, photography and voice. People make these; rules can't.
- **Accessibility floors:** minimum contrast, target sizes and visible focus, so everyone can read and use the product.

## What design tokens are

Design tokens are the rules saved as named values that code and tools can read, for example `color.text.primary = #222428` or `space.16 = 16px`. The Design Tokens Community Group publishes an open format for them; its first stable version, 2025.10, was released in October 2025. One set of tokens can generate CSS variables, a Tailwind theme, Figma variables and native code for iOS and Android.

## What a DESIGN.md is

A `DESIGN.md` is the design system written in plain words at the root of a project. People read it, and AI coding agents read it before they change the interface, so new screens follow the same rules instead of inventing new ones.

## How to make a design system with AI

1. **Start from what exists.** Read the current CSS, theme files, logo and fonts before deciding anything.
2. **Answer a few big questions first:** what you are making, who it is for, where it runs, how it should feel, and the brand color.
3. **Generate the scales from rules,** not by hand: color ramps that keep contrast, a type scale with a fixed ratio, spacing steps on a grid.
4. **Check accessibility with fixed rules:** WCAG 2.2 AA asks for at least 4.5:1 contrast for normal text and targets of at least 24 by 24 CSS pixels.
5. **Write it down as files:** tokens in an open format, CSS and a `DESIGN.md`, plus a log of every decision and why it was made.
6. **Ask a person for what only a person should make:** the logo, illustration, photography and voice.

OpenDesigner does these steps with the AI you already use. It is free and open source. [See how it works](../how-it-works/) or [install it](../install/).

## Sources

- [Design Tokens Community Group: first stable version, 2025.10](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [WCAG 2.2: 1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum)
- [OpenDesigner research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md): 352 Decision Cards behind the defaults, each with cited sources
