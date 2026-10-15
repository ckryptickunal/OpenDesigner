---
title: Design styles, named
seo_title: Design styles named: from glassmorphism to brutalism
description: Glassmorphism, neumorphism, brutalism and 25 more design styles, each drawn in code with its name, the words people use for it, where it fits and how it fails.
section: Concepts
order: 7
updated: 2026-10-15
---

You don't need to know the names of design styles. Describe the look in your own words, like "frosty", "like a comic" or "soft buttons", and OpenDesigner shows you the named styles that match, side by side, so you can point at the one you mean. This page draws 28 of them in code, each with its name, the words people use for it, where it fits and how it goes wrong. The engine knows 133 named styles, and `engine.py style search` finds them from your words.

## Your words, and the styles they mean

| You say | Look at |
|---|---|
| frosty, see-through, glassy, icy | [Glassmorphism](#glassmorphism), [Frutiger Aero](#frutiger-aero), [Dark luxe](#dark-luxe) |
| soft buttons, pillowy, pressed in | [Neumorphism](#neumorphism), [Claymorphism](#claymorphism), [Playful](#playful) |
| puffy, squishy, cute, "made of clay" | [Claymorphism](#claymorphism), [Playful](#playful), [Y2K](#y2k) |
| real, knobs, leather, "like a real object" | [Skeuomorphism](#skeuomorphism) |
| simple, clean, flat, "no shadows" | [Flat design](#flat-design), [Minimal monochrome](#minimal-monochrome), [Swiss](#swiss) |
| "like Android", floating cards, a round plus button | [Material elevation](#material-elevation) |
| bold, loud, punk, "black borders" | [Neo-brutalism](#neo-brutalism), [Comic and pop art](#comic-and-pop-art), [Brutalism](#brutalism) |
| raw, ugly on purpose, "like an old website" | [Brutalism](#brutalism), [Terminal](#terminal-and-ascii) |
| grid, poster, magazine, "long reads" | [Swiss](#swiss), [Editorial](#editorial) |
| black and white, quiet, sleek dark | [Minimal monochrome](#minimal-monochrome), [Dark luxe](#dark-luxe) |
| boxes, tiles, 3D diagram, stacked layers | [Bento grid](#bento-grid), [Isometric](#isometric), each with another style |
| dreamy colors, northern lights, "gradient background" | [Mesh and aurora](#mesh-and-aurora) |
| grainy, film, zine, screen print | [Grain and noise](#grain-and-noise), [Risograph](#risograph) |
| two-color photos, "like a poster" | [Duotone](#duotone) |
| comic, dots, speech bubbles | [Comic and pop art](#comic-and-pop-art) |
| 80s, squiggles, confetti, zigzags | [Memphis](#memphis) |
| primary colors, "circles, squares and triangles" | [Bauhaus](#bauhaus) |
| Gatsby, gold, 1920s, theatre | [Art Deco](#art-deco) |
| 2000s, chrome, aqua, bubbles, glossy | [Y2K](#y2k), [Frutiger Aero](#frutiger-aero) |
| hacker, code, 8-bit, pixels | [Terminal and ASCII](#terminal-and-ascii), [Pixel art](#pixel-art) |
| for kids, chunky, bouncy | [Playful and toy-like](#playful) |
| natural, earthy, calm and warm | [Organic and natural](#organic) |

## Surfaces and depth

How surfaces are lit and stacked: see-through, molded, real or flat.

{{figure:styles-surfaces-1}}

{{figure:styles-surfaces-2}}

## Graphic and print

Ink, outlines, shapes and printing processes.

{{figure:styles-graphic-1}}

{{figure:styles-graphic-2}}

{{figure:styles-graphic-3}}

## Layout and digital

How content is arranged, and looks born on screens. Bento grid and isometric drawing are structures: they borrow their colors and surfaces from another style.

{{figure:styles-layout-1}}

{{figure:styles-layout-2}}

{{figure:styles-layout-3}}

## Tone

The mood a whole surface gives off, from quiet to loud.

{{figure:styles-tone-1}}

{{figure:styles-tone-2}}

## Gradients and surfaces, named

The smaller effects that styles are built from. They follow the same pattern: plain words first, then the name, then the code.

{{figure:styles-glossary-1}}

{{figure:styles-glossary-2}}

{{figure:styles-glossary-3}}

## A style is a direction, not decoration

A style applies to a whole surface, never to one corner of it. One glass card on a flat page, or one comic burst on a calm dashboard, reads as a mistake. Use the style on every instance of the same kind, keep one base style per surface, and spend boldness in one signature place. A product can carry two: a durable style for the app and a louder one for its marketing pages. When you pick a style in the interview, OpenDesigner records its name and sets the [dials](/docs/dials/) that build it.

The [accessibility floors](/docs/accessibility/) stay locked whatever the style: 4.5:1 text contrast, 3:1 for control edges and icons, 24 px targets, visible focus, reduced motion and reduced transparency. Some styles push against them:

- **Text on glass** changes contrast with whatever scrolls behind it, so it is checked at the worst spot, and every glass surface gets a solid twin for people who turn transparency off.
- **Neumorphism** fails the 3:1 edge contrast by design. Every control needs a visible border or a darker fill, and a pressed state needs a second signal besides the inset shadow.
- **Pastel and bright fills** often fail with white text, and fluorescent pink or yellow fails as text on white. Keep text dark on light fills and check every pair.
- **Textures** such as grain, halftone and scanlines lower contrast. Check text with the effect on, or keep text on plain fills.

To see styles applied to whole pages, browse the style studies in the [showcase](/showcase/).
