---
title: The eight dials
seo_title: The eight design dials in OpenDesigner and what each sets
description: OpenDesigner's eight dials, from Expression to Warmth: what each end means, the values each dial drives, how feel words move them, and their limits.
section: Reference
order: 4
updated: 2026-11-08
---

Eight sliders, each from 0 to 100, set most of how your design system looks. Your answers and feel words move them for you, and each position becomes real values, such as a type scale ratio or a corner radius. Read this page to see what a dial changes before you move one yourself.

{{figure:dials-sliders}}

## How the dials work

- **50 is the middle** for most dials. Depth starts at 40.
- **Feel words move them.** "Playful" or "serious" shifts several dials at once, and plain words count too: "fun" reads as playful.
- **Some dials follow others until you move them.** Four follow Expression. Roundness also follows Density, and Colorfulness also follows Energy. Once you set a dial yourself, it stays where you put it.
- **Raw inputs sit beside the dials:** your brand color, typeface, base text size, platforms and contrast target.
- **Style presets are named dial settings,** such as flat, tonal, glass and neo-brutalist.

{{figure:dials-coupling}}

:::dev
Set a dial yourself, then rebuild:

```
engine.py set dials.roundness 60 --why "softer corners for a friendlier feel"
engine.py build
```

The formulas, their sources and their weak spots are in [the levers document](https://github.com/ckryptickunal/OpenDesigner/blob/main/synthesis/LEVERS.md).
:::

## The three posture dials

These set the overall stance. Each range runs from the left end to the right.

### Expression: productive to expressive

How much the interface performs on everyday screens. It drives:

- the type scale ratio, 1.2 to 1.333;
- how many font weights are used;
- hero moments, none to one or two per product;
- expressive motion, nowhere to throughout;
- the brand color's role, a reserved accent to brand-colored chrome;
- containment, whitespace to visible containers;
- icons at rest, outline to filled or colored.

At every position, each view gets one primary action.

### Brand presence: native to brand-led

How much the product looks like your brand rather than its platform. It drives:

- the suggested typeface: the platform's system font, then open typefaces, then your own brand typeface;
- where the brand color appears, accents only to large surfaces;
- how many components are the platform's own, all of them to none;
- whether the platform's base text size and shapes win;
- how much voice guidance to write.

Navigation always follows the platform's own patterns. The engine never guesses this dial from a reference: it always asks you.

### Density: spacious to compact

How much information fits on a screen. It drives:

- the base text size on the web, 19 px down to 13 px;
- the control height: 48, 40 or 32 px;
- the density mode: spacious, comfortable or compact;
- the ratio of inner to outer spacing;
- the default icon size: 24, 20 or 16 px;
- a cap on the type scale ratio in dense layouts.

Density never shrinks tap and click targets.

## The five character dials

These tune the details.

### Energy: calm to energetic

How lively the interface feels in motion and intensity. It drives spring damping and stiffness, the standard easing curve, a duration multiplier from 0.8 to 1.2, heading weight, how navigation is treated, and haptic strength.

### Roundness: sharp to soft

The corner radius of the default control and everything made from it: 0, 2, 4, 6, 8, 12 or 16 px, or fully round. It also sets icon corners and line caps, and whether to suggest a rounded display face.

Until someone chooses the corners, with the corner question, this dial or a style, buttons and fields stay between 6 and 12 px: feel words alone never make square or pill buttons. The Roundness line in `DESIGN.md` shows the radius your tokens hold.

### Depth: flat to deep

How strongly surfaces stand apart. From flat to deep, the model runs from borders to a ring with a faint shadow, tonal layers, a ladder of shadows, and materials. It also sets shadow strength in light mode; in dark mode, raised surfaces get lighter instead.

Some styles bring their own depth, such as the solid offset shadows of neo-brutalism. The Depth line in `DESIGN.md` then names that model.

### Colorfulness: monochrome to vivid

How much color the palette carries and how much of the screen it covers. It drives the accent's chroma, the scheme from monochrome through neutral and tonal to vibrant, whether surfaces are tinted, how many accent colors there are, and whether text may use the accent.

### Warmth: cool and formal to warm and friendly

The temperature of the neutral grays and the formality of the details around them. It drives the gray tint (cool blue-gray to warm stone), how soft the borders are, title or sentence case, how freely the copy uses contractions, and the kind of typeface suggested.

## Where the dials come from

The dials were tested against 13 real systems, such as Material 3 Expressive, Carbon and GOV.UK. Dials plus raw inputs reproduce the signature look of 6 of them; the other 7 need one or two overrides or a signature asset.

But the dial values were set by reading that same benchmark. So this shows they agree with those systems, not that they predict systems they haven't seen. Some mappings are marked as inferred in the source file.

## What you decide

The dials do the arithmetic. You decide the brand personality and the dial positions, and OpenDesigner records your answer. [How it works](/docs/how-it-works/) shows how your answers reach the dials.
