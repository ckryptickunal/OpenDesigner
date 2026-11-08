---
title: Brand assets and asset hooks
seo_title: Brand assets: what OpenDesigner asks you for, and why
description: Which brand assets only a person should make, how OpenDesigner's 14 asset hooks ask for them, what it offers when you have none, and how it tracks licences.
section: Concepts
order: 6
updated: 2026-11-08
---

Some parts of a brand should be made by a person, such as a logo, photos or a voice guide. OpenDesigner doesn't fake these. For each one it asks whether you have it, checks the file if you do, and offers honest paths if you don't. Each of these questions is called an asset hook.

## The 14 asset hooks

1. **Logo and lockups:** the name written out, a symbol, or both.
2. **App icon**, best in separate layers.
3. **Favicon set**, made from your logo's symbol.
4. **Custom icons** that free icon sets don't have.
5. **Illustration:** a drawing style or a character.
6. **Photography**, or a photo style to follow.
7. **Brand typeface** files of your own.
8. **Fixed brand colors** that must match exactly.
9. **Motion signature:** a moving logo, loading animations or 3D.
10. **Graphic motifs:** patterns, textures, color blends or a signature shape.
11. **UI sounds**, or a short sound for your brand.
12. **Haptics:** your own vibration patterns.
13. **Voice and tone guide**, or a word list.
14. **Brand book:** your guidelines as a PDF.

## When it asks

In the sketch, it asks only about a brand color or a logo. When you zoom into brand or imagery, it asks about the rest once, in one checklist. Until then, each keeps a placeholder with a brief.

An internal tool with no brand may not need sound, haptics, photos, illustration, motion or motifs, and can mark them all not needed in one step.

## If you have it

It asks for one master file, checks it and makes the other sizes from it.

{{figure:brand-assets-master}}

- **Logo:** SVG or PDF, with the text turned into outlines.
- **App icon:** layered files for each platform, and PNG for the app stores.
- **Icons:** SVG drawn on the icon library's grid.
- **Brand typeface:** OTF or TTF masters, and WOFF2 for the web.
- **Photos:** the highest-resolution originals.

The logo also gets two rules: clear space on every side, and the smallest size it may be shown at. Both say "Default" on the brand page until you set them. That page also offers your logo files to download, with do and don't examples made from your own logo.

Give it a logo and it shows up to three of its colors, with how much of the logo each one covers. You pick the brand color from them, or type your own. Nothing is recorded until you pick.

:::dev
- The logo rules start at half the logo's height for clear space, and 16 px tall for the symbol (24 px with the wordmark). Set one: `engine.py set hooks.H-logo.clearSpace 0.75`
- Make the brand page: `engine.py export --format brand`
- Read the colors from a PNG or SVG logo: `engine.py sketch --logo logo.svg`
:::

## If you don't have it

It offers four paths, in this order:

| Path | What comes with it |
|---|---|
| 1. A designer | A written brief (below) |
| 2. An open library | Its licence. For example, Lucide or Phosphor for icons, and Google Fonts for type |
| 3. A named tool | Its caveats. For an AI tool, that tool's terms for your plan |
| 4. Nothing | For example, no illustration, and honest text in empty states |

A placeholder is always labelled, and a generated stand-in is never shown as finished work.

For a contractor's logo, it reminds you to get the copyright assigned in writing.

## The brief it writes

A logo brief looks like this. The real one lists the files and sizes needed, with your own tokens and direction.

```
Asset: logo
Needed by: launch
Files: SVG master with outlined text, one-color version
System: DESIGN.md; palette accent + neutrals; type faces; radius control/container
Direction: the chosen direction in one line; memorable thing: from your answers
Constraints: licence, platforms, dark mode, reduced motion
Rights: written copyright assignment to the owner on delivery
```

## Brand fonts and their licences

When you name a brand font, it asks where its licence lets you use it: websites, apps, and hosting the files yourself. Then it tells you in one line what that means for each platform, for example: "Your licence covers websites only, so the iPhone app will use the system font."

If you don't know what the licence covers, it records nothing and lists an open question. It never guesses a licence.

:::dev
The Swift and Compose exports then use the system font by themselves.
:::

## The licence ledger

For each asset, it records the source, the licence, the credit line, where the asset may be used and who owns it.

- It keeps the notices that open icon libraries require.
- It blocks an asset from any place its licence forbids. Some free illustration sets, for example, can't be used in a logo.
- It fetches assets for your project only, never into a shared catalog, because several licences forbid that.

## The illustration skill

With no illustrations of your own, the illustrate skill finds open-licence art, recolors it to your tokens and logs each licence. With a few icons of your own, it draws more the same way and shows them next to yours. Nothing is used until you say yes.

The engine makes no network calls. This skill does: it searches and downloads art and icons over HTTPS, and only when you use it.

:::dev
The skill is `opendesigner-illustrate`. It searches open-licence sources, ranks what it finds, recolors the art to your tokens and applies it. Its directory lists 46 sources, photo sources included. Most licences were checked on 2026-09-28, and Unsplash and Pexels on 2026-11-05.

For icons, it reads how yours are drawn: the badge or ring around each one, the box the drawing sits in, the line weight and the color. It finds the open icon set closest to that and redraws the glyphs you pick the same way. Each glyph's licence goes in the ledger.
:::

## How the status is recorded

Each hook records where it stands, from "have" to "not needed", and stays pending until it is asked. The overview page shows how many of the 14 you have provided.

{{figure:brand-assets-board}}

:::dev
The statuses are have, commissioning, tool, open library, placeholder and not needed.
:::

If you share a site you admire, its logo, art, photos and icons are never copied. They go on your own asset list instead. See [Start from an existing app or brand](/docs/existing-product/).
