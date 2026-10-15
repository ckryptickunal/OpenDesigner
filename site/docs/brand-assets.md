---
title: Brand assets and asset hooks
seo_title: Brand assets: what OpenDesigner asks you for, and why
description: Which brand assets only a person should make, how OpenDesigner's 14 asset hooks ask for them, what it offers when you have none, and how it tracks licences.
section: Concepts
order: 6
updated: 2026-10-14
---

Some parts of a brand should be made by a person: a logo, an app icon, custom icons, illustration, photos, a brand typeface and a voice guide. OpenDesigner doesn't fake these. For each one it opens an asset hook: it asks whether you have it, checks the file if you do, and offers honest paths if you don't.

## The 14 asset hooks

1. **Logo and lockups:** the name written out, a symbol, or both.
2. **App icon:** separate layers are best.
3. **Favicon set:** made from your logo's symbol.
4. **Custom icons:** icons that free icon sets don't have.
5. **Illustration:** a drawing style or a character.
6. **Photography:** photos, or a photo style to follow.
7. **Brand typeface:** your own font files.
8. **Fixed brand colors:** colors that must match exactly.
9. **Motion signature:** a moving logo, loading animations or 3D.
10. **Graphic motifs:** patterns, textures, color blends or a signature shape.
11. **UI sounds:** app sounds, or a short sound for your brand.
12. **Haptics:** your own vibration patterns.
13. **Voice and tone guide:** how your product writes, or a word list.
14. **Brand book:** your brand guidelines as a PDF.

## When it asks

In the sketch, it asks only about a brand color or a logo. When you zoom into brand or imagery, it asks about the rest once, as one checklist: "Which of these do you already have?" Until then, the others keep a placeholder with a brief.

An internal tool with no brand may not need sound, haptics, photos, illustration, motion or motifs. It can mark those as not needed in one step.

## If you have it

It asks for one master file and makes the other sizes from it.

{{figure:brand-assets-master}}

- **Logo:** SVG or PDF, with the text turned into outlines.
- **App icon:** layered files for each platform, and PNG for the app stores.
- **Icons:** SVG drawn on the icon library's grid.
- **Brand typeface:** OTF or TTF masters, and WOFF2 for the web.
- **Photos:** the highest-resolution originals.

It checks each file. A logo, for example, should still work at 16 px on light and dark backgrounds.

If you give it a logo file, it can use the logo's main color as your brand color seed.

## If you don't have it

It offers these paths, in this order:

1. **A designer, with a written brief.** The brief lists the files and sizes needed, your tokens and your direction.
2. **An open library, with its licence.** For example, Lucide or Phosphor for icons, and Google Fonts for type.
3. **A named tool, with its caveats.** When it suggests an AI tool, it states that tool's terms for your plan.
4. **Nothing.** For example, no illustration, and honest text in empty states.

A placeholder is always labelled as a placeholder. A generated stand-in is never shown as finished work.

For a logo made by a contractor, it reminds you to get a written copyright assignment.

## The brief it writes

```
Asset: logo
Needed by: launch
Files: SVG master with outlined text, one-color version
System: DESIGN.md; palette accent + neutrals; type faces; radius control/container
Direction: the chosen direction in one line; memorable thing: from your answers
Constraints: licence, platforms, dark mode, reduced motion
Rights: written copyright assignment to the owner on delivery
```

The real brief carries your own tokens and direction.

## Brand fonts and their licences

When you name a brand font, it asks where its licence lets you use it: websites, apps, and hosting the files yourself. Then it says in one line what that means for each platform. For example: "Your licence covers websites only, so the iPhone app will use the system font." The Swift and Compose exports then use the system font by themselves.

If you don't know what the licence covers, it records nothing and lists it as an open question. It never guesses a licence.

## The licence ledger

For each asset, it keeps a record of the source, the licence, the credit line, where the asset may be used and who owns it.

- It keeps the notices that open icon libraries require.
- It blocks an asset from any place its licence forbids. Some free illustration sets, for example, can't be used in a logo.
- It fetches assets for your project only. It never pools them into a shared catalog, because several licences forbid that.

## The illustration skill

If you have no illustrations and want open-licence art, the opendesigner-illustrate skill can help. It searches open-licence sources, ranks what it finds, recolors the art to your tokens, applies it, and keeps the licence ledger. Its directory lists 44 illustration sources, each with its licence checked on 2026-09-28.

The engine makes no network calls. This skill does: it searches and downloads art over HTTPS, and only when you use it.

## How the status is recorded

Each hook gets a status: have, commissioning, tool, open library, placeholder or not needed. It stays pending until it is asked. The overview page shows how many of the 14 you have provided, and anything missing shows as "Not enough information".

{{figure:brand-assets-board}}

If you share a site you admire as a reference, its logo, art, photos and icons are never copied. They go on your own asset list instead. See [Start from an existing app or brand](/docs/existing-product/).
