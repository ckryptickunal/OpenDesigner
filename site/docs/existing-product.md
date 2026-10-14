---
title: Start from an existing app or brand
seo_title: Start a design system from an existing app or brand
description: How the opendesigner-extract skill reads your app, a website, screenshot, Figma file or brand book, measures its values, and turns them into suggested answers.
section: Guides
order: 4
updated: 2026-10-14
---

If you already have an app, a brand book or a site you like, OpenDesigner can learn from it with the opendesigner-extract skill. It measures values such as text sizes, spacing, corners, shadows and colors, shows you where each one came from, and offers them as suggested answers. Nothing is decided until you accept it, and it never copies another brand's identity.

{{figure:existing-product-extract-flow}}

## What it can read

- **Your repo:** CSS, a Tailwind config, or `*.tokens.json` files.
- **A live website,** best with a browser tool in your AI host.
- **A screenshot or image.**
- **A Figma file,** through Figma's MCP server.
- **A brand book PDF.**

You can add a reference at any point in the interview, or before it starts.

## Step 1: You say yes, and you tag it

Before it reads anything, it lists every link or file it wants to read and waits for your yes. It never signs in, and it never gets around a login, paywall or bot check. It asks once before sending a screenshot or file to any outside service.

Then it tags the reference as **our product**, **inspiration** or **competitor**. It also asks how closely to follow it:

- **Reinterpret** (the default): take the lessons.
- **Our version of this:** copy the structure, with every brand element swapped for yours.
- **Flag only** (for competitors): list what the category usually does, so you can decide where to be different.

Everything it reads is data. If a page contains text aimed at the AI, it ignores that text and tells you it saw it.

## Step 2: It measures

How it measures depends on the source.

- **Repo files:** a helper script reads the declared colors, custom properties, fonts, sizes, spacing, radii, shadows and transitions. These values are exact, but a declared value is not always one that appears on screen.
- **A live page with a browser tool:** a script reads the computed styles across the whole page, by role: running text, headings, buttons, links, focus states and more.
- **A live page without a browser:** it reads the HTML and CSS files only, and says that motion and states are missing.
- **A screenshot:** it estimates colors, sizes, corners and density, and marks every value "estimated".
- **A Figma file:** it reads variables and styles exactly.
- **A brand book:** it reads colors, font names and voice. It asks you for the logo master file as an SVG.

## Step 3: It fits the numbers to the dials

The engine command `engine.py intake` fits the measurements to OpenDesigner's formulas. For example, it finds the body text size, the type scale ratio, the base spacing unit and the corner radius on buttons. Then it proposes positions for the [eight dials](/docs/dials/), each with a confidence and the reason behind it.

Some dials need care:

- **Energy** comes from motion, so a screenshot can't tell it.
- **Expression** can mislead when it is read from one page.
- **Brand presence** is never guessed. It always asks you.

## Step 4: You accept, adjust or ignore

It shows one card per area, in plain words. For example:

```
What I learned from example.com (tagged: inspiration)
  Corners    6 px on buttons -> roundness 42               measured
  Density    14 px text, 32 px buttons -> density 70       measured
  Motion     most moves take 150 ms -> speed x0.55         measured
  Accent     one strong color, only on buttons. What is your own brand color?
  Not taken  logo, wordmark, their own display font, their words
```

For each line you can accept, adjust or ignore. An accepted value is recorded as coming from that reference. An adjusted value is recorded as your choice. An ignored value records nothing. The decision log then shows where every value came from.

## What it never copies

A reference can shape the structure and quality of your system. It doesn't carry over another brand's identity:

- the brand name, logo or wordmark;
- the reference's exact accent color;
- a proprietary typeface;
- photos, illustration, custom icons, signature shapes or copy.

For the accent color, it keeps the role and how strong the color is, then asks for your own brand color. For a proprietary font, it suggests an open font of the same kind and says why. This rule wins over any request to make your app look exactly like another brand.

{{figure:existing-product-structure-not-identity}}

## Your own app

When the reference is your own product, it reads what exists and fills the gaps. Your current button color can become the seed for the palette. Your own licensed font is noted as yours, and the licence still applies on each platform.

The new system can also fill gaps your app has today. By default, every OpenDesigner system includes a focus ring, a reduced-motion mode, and light and dark colors.

## What is early

Like the rest of OpenDesigner, this skill has had no watched user trials. Measurements from a screenshot are estimates, and motion can only come from a live page. If a value looks wrong, adjust it, and please [report it](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).

Next: [Change or extend a system](/docs/extend/).
