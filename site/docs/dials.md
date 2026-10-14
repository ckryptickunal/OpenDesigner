---
title: The eight dials
seo_title: The eight design dials in OpenDesigner and what each sets
description: OpenDesigner's eight dials, from Expression to Warmth: what each end means, the values each dial drives, how feel words move them, and their limits.
section: Reference
order: 4
updated: 2026-10-14
---

OpenDesigner sets most of a design system's look with eight dials. Each dial is a slider from 0 to 100, and each position maps to concrete values, such as a type scale ratio or a corner radius. Three posture dials set the overall stance, and five character dials tune the details.

{{figure:dials-sliders}}

## How the dials work

- **50 is a sensible middle** for most dials. Depth starts at 40.
- **Your feel words move them.** Words like "playful", "serious", "friendly" or "premium" each shift several dials at once. The engine reads plain words too: "fun" counts as playful.
- **Some dials follow others until you move them.** Energy, Roundness, Colorfulness and Depth follow Expression. Roundness also follows Density, and Colorfulness also follows Energy. Once you set a dial yourself, it stays where you put it.
- **A few raw inputs sit beside the dials:** your brand color, typeface, base text size, platforms and contrast target.
- **Style presets are named dial settings.** Examples are flat, tonal, glass and neo-brutalist.

{{figure:dials-coupling}}

You can set a dial directly:

```
engine.py set dials.roundness 60 --why "softer corners for a friendlier feel"
engine.py build
```

## The three posture dials

### Expression: productive to expressive

How much the interface performs on everyday screens. It drives:

- the type scale ratio, from 1.2 at the productive end to 1.333 at the expressive end;
- how many font weights are used;
- hero moments, from none to one or two per product;
- where expressive motion appears, from nowhere to throughout;
- the brand color's role, from a reserved accent to brand-colored chrome;
- containment, from whitespace to visible containers;
- the icon style at rest, from outline to filled or colored.

At every position, each view gets one primary action.

### Brand presence: native to brand-led

How much the product looks like the brand, compared with the platform it runs on. It drives:

- the typeface suggestion, from the system font on each platform, through open typefaces, to your own brand typeface;
- where the brand color appears, from accents only to large surfaces;
- how many components are the platform's own, from all of them to none;
- whether the platform's base text size and shapes win;
- how much voice guidance to write.

Navigation always follows the platform's own patterns, whatever this dial says. The engine never guesses this dial from a reference. It always asks you.

### Density: spacious to compact

How much information fits on a screen. It drives:

- the base text size on the web, from 19 px down to 13 px;
- the control height, 48, 40 or 32 px;
- the density mode: spacious, comfortable or compact;
- the ratio of inner to outer spacing;
- the default icon size, 24, 20 or 16 px;
- a cap on the type scale ratio in dense layouts.

Density never shrinks tap and click targets.

## The five character dials

### Energy: calm to energetic

How lively the interface feels in motion and intensity. It drives spring damping and stiffness, the standard easing curve, a duration multiplier from 0.8 to 1.2, heading weight, how navigation is treated, and haptic strength.

### Roundness: sharp to soft

The corner radius of the default control, and everything made from it. It runs from 0 px through 2, 4, 6, 8, 12 and 16 px to fully round. It also sets icon corners and line caps, and whether a rounded display face is suggested.

### Depth: flat to deep

How strongly surfaces stand apart. From the flat end, the model goes from borders, to a ring with a faint shadow, to tonal layers, to a ladder of shadows, to materials. It also sets how strong the shadows are in light mode. In dark mode, raised surfaces get lighter instead.

### Colorfulness: monochrome to vivid

How much color the palette carries and how much of the screen it covers. It drives the accent's chroma, the color scheme from monochrome through neutral and tonal to vibrant, whether surfaces are tinted, how many accent colors there are, and whether text may use the accent.

### Warmth: cool and formal to warm and friendly

The temperature of the neutral grays and the formality of the details around them. It drives the gray tint, from cool blue-gray to warm stone, how soft the borders are, title case or sentence case, how freely the copy uses contractions, and the kind of typeface suggested.

## Where the dials come from

The dials were tested against 13 real systems, including Material 3 Expressive, Apple HIG, Carbon, Fluent 2, Polaris, Primer, GOV.UK and shadcn/ui. Dials plus raw inputs reproduce the signature look of 6 of them. The other 7 need one or two overrides or a signature asset.

The dial values were set by reading that same benchmark. So this shows the mapping is consistent with those systems. It does not show that the dials predict systems they haven't seen. Some mappings are marked as inferred in the source file.

## What you decide

The dials do the arithmetic. You decide the brand personality and the dial positions, and OpenDesigner records your answer. The formulas, their sources and their weak spots are in [the levers document](https://github.com/ckryptickunal/OpenDesigner/blob/main/synthesis/LEVERS.md).

See [How it works](/docs/how-it-works/) for how your answers reach the dials.
