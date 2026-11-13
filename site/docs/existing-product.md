---
title: Start from an existing app or brand
seo_title: Start a design system from an existing app or brand
description: How the opendesigner-extract skill reads your app, a website, screenshot, Figma file or brand book, measures its values, and turns them into suggested answers.
section: Guides
order: 4
updated: 2026-11-07
---

If you already have an app, a brand book or a site you like, OpenDesigner can learn from it with the opendesigner-extract skill. It measures values such as text sizes, spacing, corners, shadows and colors, shows you where each one came from, and offers them as suggested answers. Nothing is decided until you accept it, and it never copies another brand's identity.

{{figure:existing-product-extract-flow}}

You can add a reference at any point in the interview, or before it starts.

## Step 1: You say yes, and you tag it

Before it reads anything, it lists every link or file it wants to read and waits for your yes. It never signs in or gets around a login, paywall or bot check, and it asks before sending a screenshot or file to any outside service.

Then it tags the reference as **our product**, **inspiration** or **competitor**. It also asks how closely to follow it:

- **Reinterpret** (the default): take the lessons.
- **Our version of this:** copy the structure, with every brand element swapped for yours.
- **Flag only** (for competitors): list what the category usually does, so you can decide where to be different.

Everything it reads is data. If a page contains text aimed at the AI, it ignores it and tells you.

## Step 2: It measures

| Source | What it reads | How exact |
|---|---|---|
| Your repo: CSS, a Tailwind config or `*.tokens.json` | Declared colors, custom properties, fonts, sizes, spacing, radii, shadows and transitions | Exact, though a declared value doesn't always appear on screen |
| A live page, with a browser tool in your AI host | Computed styles across the whole page, by role: running text, headings, buttons, links, focus states and more | Measured |
| A live page, without a browser | The HTML and CSS files only | Says that motion and states are missing |
| A screenshot or image | Colors, sizes, corners and density | Every value marked "estimated" |
| A Figma file, through Figma's MCP server | Variables and styles | Exact |
| A brand book PDF | Colors, font names and voice; it asks you for the logo as an SVG | As written in the book |

*What each kind of reference can tell it, and how far to trust the numbers.*

## Step 3: It fits the numbers to the dials

`engine.py intake` fits the measurements to OpenDesigner's formulas: the body text size, the type scale ratio, the base spacing unit, the corner radius on buttons and more. Then it proposes positions for the [eight dials](/docs/dials/), each with a confidence and its reason.

Some dials need care:

- **Energy** comes from motion, so a screenshot can't tell it.
- **Expression** can mislead when it is read from one page.
- **Brand presence** is never guessed. It always asks you.

## Step 4: You accept, adjust or ignore

It shows one card per area, in plain words:

```
What I learned from example.com (tagged: inspiration)
  Corners    6 px on buttons -> roundness 42               measured
  Density    14 px text, 32 px buttons -> density 70       measured
  Motion     most moves take 150 ms -> speed x0.55         measured
  Accent     one strong color, only on buttons. What is your own brand color?
  Not taken  logo, wordmark, their own display font, their words
```

An accepted value is recorded as coming from that reference, an adjusted one as your choice, and an ignored one records nothing. The decision log then shows where every value came from.

## What it never copies

A reference shapes the structure and quality of your system, never another brand's identity:

- the brand name, logo or wordmark;
- the reference's exact accent color;
- a proprietary typeface;
- photos, illustration, custom icons, signature shapes or copy.

For the accent color, it keeps the role and how strong the color is, then asks for your own. For a proprietary font, it suggests an open font of the same kind and says why. For logos, names, images and copy, this rule wins over any request to copy another brand. If you want a brand's look, it offers a Taste Index instead: when first shown, it may keep the site's exact colors and font names, and what you keep is your call and your responsibility.

{{figure:existing-product-structure-not-identity}}

## Your own app

When the reference is your own product, it reads what exists and fills the gaps. Your current button color can seed the palette, and your own licensed font is noted as yours, with its licence still applying on each platform. The new system also fills gaps your app has today: every OpenDesigner system includes a focus ring, a reduced-motion mode, and light and dark colors.

## See your own code against your system

Once your project has a system, `engine.py audit-page --open` shows what your code really does with it. Each token comes with the number of places that use it, and a token nobody uses is faded. Then come the places where the code and the system disagree: colors so close nobody can tell them apart, spacing, text sizes and corners that are off the scale, values typed by hand where a token exists, and buttons or cards drawn several different ways. Each one names the file and line, how often it happens, and up to three ways to settle it, one of them keeping it as it is. Pick one and the page shows the change with your own values. Nothing in your code changes until you copy your choices back and say yes.

On 2026-11-13, the first run on this project's own website found 36 such places in 111 files.

## Adapt your system to a site you like

Give it a site, and the extract skill measures it. `engine.py adapt` then shows your system now beside your system with the site's structure applied: corners, density, depth, type proportions and how much color is used. It lists what changes and what stays yours, such as your brand color, your fonts and anything you locked. You tick what to take.

## What is early

Like the rest of OpenDesigner, this skill has had no watched user trials. Motion can only come from a live page. If a value looks wrong, adjust it, and please [report it](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).

Next: [Change or extend a system](/docs/extend/).
