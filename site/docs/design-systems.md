---
title: What is a design system?
seo_title: What is a design system? A plain guide for any team
description: A design system is the set of rules for how a product looks and behaves. What goes into one, what tokens and DESIGN.md are, and how to make one with AI.
section: Concepts
order: 1
updated: 2026-11-08
---

A design system is the set of rules for how a product looks and behaves, such as its colors, spacing, corners and buttons. Written down, the rules keep every screen consistent, even when different people, or different AI chats, build them.

{{figure:design-systems-parts}}

## Why teams write the rules down

Without written rules, each new screen makes its own small choices, like 8 px corners on one button and 6 px on the next. Over time the app looks slightly wrong, and nobody can say why.

{{figure:design-systems-hardcoded}}

A design system fixes this with a short list of agreed values and the reason for each. Designers and engineers share the values, and AI tools read them before they change a screen.

{{figure:design-systems-one-source}}

## What goes into a design system

| Part | What it covers |
|---|---|
| Color | Shades in steps, and which is for text, backgrounds and actions, in light and dark mode |
| Typography | Typefaces, a type scale (the fixed list of text sizes) and roles like headings and body |
| Spacing | Steps for padding and gaps, often on a 4 or 8 pixel grid |
| Shape | Corner radius for controls, cards and dialogs |
| Depth | Shadows, borders or tones that set surfaces apart |
| Motion | How long movements take and how they speed up and slow down, with less motion for people who ask |
| Components | Buttons, fields, cards and menus, with states like hover and error |
| Brand assets | Logo, icons, illustration, photos and voice. People make these. Rules can't. |
| Accessibility floors | Minimum contrast and target size, and a visible focus ring, so more people can use it |

## What design tokens are

Design tokens are the rules saved as named values that code and tools can read. The name for the main text color holds one dark gray, and every screen uses the name. See [Design tokens and DTCG](/docs/design-tokens/).

:::dev
For example, `color.text.primary` might hold a dark gray, and `space.4` might hold 16 px. The Design Tokens Community Group publishes an open format for tokens. Its first stable version, 2025.10, came out on 28 October 2025. One set of tokens can produce CSS variables, a Tailwind theme, Figma variables and native code for iOS and Android.
:::

## What a DESIGN.md is

A `DESIGN.md` is the design system in plain words, in one file in your project. People read it, and AI agents can be told to read it before changing the interface. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Small app or large company

The idea is the same at any size. Only how much you write down changes.

| Who | What they write down |
|---|---|
| A student project or small app | Colors, a type scale, spacing, corners and one button: enough to look consistent. |
| A product team | Also components, states, dark mode and rules for using each part |
| A design-system team at a large company | Also who can change the system, how changes are announced and versioned, and how teams adopt it. Here the reasons matter most: many people change it over many years. |

## How to make a design system with AI

1. **Start from what exists:** the current CSS, theme files, logo and fonts.
2. **Answer a few big questions,** such as who it's for and how it should feel.
3. **Work out the scales with rules,** which give the same answer every time: color ramps that keep contrast, a type scale with a fixed ratio, spacing steps on a grid.
4. **Check accessibility with fixed rules.** WCAG 2.2 AA asks for at least 4.5:1 contrast for normal text, and targets of at least 24 by 24 CSS pixels.
5. **Write it down as files:** tokens, CSS and a `DESIGN.md`, plus a log of every decision and why.
6. **Ask a person for the brand assets,** such as the logo and photos.

OpenDesigner follows these steps with the AI tool you already use. It's free and open source, and early: no watched user trials have happened yet. [See how it works](/docs/how-it-works/) or [install it](/docs/install/).

## Sources

- [Design Tokens Community Group: first stable version, 2025.10](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [WCAG 2.2: 1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum)
- [OpenDesigner research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md): the more than 500 Decision Cards behind the defaults, each with its sources
