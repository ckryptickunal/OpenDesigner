---
title: What an AI design system generator should do
seo_title: AI design system generator: what it should and shouldn't do
description: A good AI design system generator asks, recommends with reasons, checks accessibility and writes it all down. How OpenDesigner does each, and what it isn't.
section: Guides
order: 23
updated: 2026-11-07
---

A useful AI design system generator leaves you with rules you understand and files your code can use, not only a nice palette. A design system is the rules for how your app looks: colors, text sizes, spacing, corners and buttons.

OpenDesigner is a free, open-source one. It asks a few questions, recommends sourced defaults, checks accessibility with fixed rules, and writes down why each choice was made. It doesn't draw screens or make logos.

## What it should do

**Look before it asks.** It reads your CSS, Tailwind config, `package.json`, token, logo and font files first, and skips questions they answer.

**Ask only what only you can answer.** The first pass is up to five questions: what you are making, who it is for, where it runs, how it should feel, and your brand color or logo. Then you can stop, or zoom into one area such as color or type.

**Recommend one answer, with its reason.** The defaults rest on more than 500 Decision Cards, each covering one design decision with logged sources or marked as an inference. You can always answer in your own words, or say "just pick".

**Do the math in code, not in the chat.** A Python engine works out the color ramps, type and spacing scales, contrast and every export. The same answers give the same tokens: one command run twice on 2026-10-15 gave identical files.

**Check accessibility with fixed rules.** Every system gets WCAG 2.2 AA text contrast, 3:1 contrast for borders and focus rings, minimum target sizes (24 CSS px on the web, 44 pt on iOS, 48 dp on Android), a focus ring and a reduced-motion mode. OpenDesigner checks every text, border, icon and focus-ring color pair your tokens promise, in light and dark mode, including text on hover and pressed fills, and a failing pair stops the build. That is a floor, not a certificate: automated checks catch only part of WCAG, so test with real people too.

**Write down why.** `opendesigner/decisions.md` records every value and how it was set: chosen by you, a default you confirmed, delegated to the AI, assumed, or taken from a reference. Entries are only added, never edited, so a later session can't quietly undo a choice.

**Ask a person for what a person should make:** the logo, icons, illustration, photos, brand typeface and voice. Anything missing is marked "Not enough information". It never fakes a logo, and never copies another brand's name, logo, exact color or typeface.

{{figure:intent-generator-scope}}

## What OpenDesigner isn't

- **A canvas tool.** It writes the rules, and your AI builds the screens with them. Figma variables are one of its exports.
- **A logo or illustration maker.** A separate skill finds open-licence illustrations and recolors them to your tokens.
- **A hosted service.** There is no account. The engine runs on your computer, or in Claude's code sandbox in the Claude app.
- **A replacement for designers or user testing.** It does the repetitive system work, not the judgment.

## Compared with a theme generator

A theme generator turns a color or two into a theme for one component library. If that is all you need, it's a quick, good tool. OpenDesigner works one step earlier.

| | A theme generator | OpenDesigner |
|---|---|---|
| Starts from | A color or two | Who the app is for, where it runs and the accessibility level you need |
| Writes | A theme for one component library | Tool-neutral DTCG tokens, CSS variables and a Tailwind v4 theme |
| Records why | No | Every choice, with its reason |

*Where each one starts and what it leaves you with.*

If your components expect their own variable names, you point those names at the tokens once. We haven't tested that with a specific component library yet.

## Today, and not yet

Today: nine skills, the engine, every export, and an overview page of your whole system.

Not yet:

- Clicking choices inside your AI tool ([planned in issue #20](https://github.com/ckryptickunal/OpenDesigner/issues/20)). Today choices are HTML pages, artifacts, text, or your tool's own question buttons.
- More components on the overview page. It draws buttons, a text field and a card, and the [component library](/library/) has 82 you can add.
- React Native or Flutter exports.
- Watched user trials. "About 3 minutes" for the first pass is a design target, not a measurement.

## Next

- [Install OpenDesigner](/docs/install/) in Claude, ChatGPT, Codex or Cursor.
- [Your first design system](/docs/quickstart/), step by step.
- Already have an app? [Start from an existing app or brand](/docs/existing-product/).
