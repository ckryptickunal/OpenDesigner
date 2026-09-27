---
type: synthesis
title: Gradients, blend modes and texture effects
created: 2026-09-27
updated: 2026-09-27
sources:
  - MZSm6MA8bww
tags:
  - od-area-shape-depth
---

# Gradients, blend modes and texture effects

## In short

These are decorative surface effects: smooth blends between colors (gradients), layers that mix their colors with the layers underneath (blend modes such as Screen or Overlay), and blur or grain that give a surface texture. The only source on this topic is a short Figma tutorial that builds four effects from those pieces (a kaleidoscope, clay, metal and a mesh gradient) and names where each one fits: mostly cards, stickers, illustrations, mockups and backgrounds, with buttons the only everyday control on the list. Its presenter admits that one of them looks good but is poor for usability, and says mesh gradients are more art than science. This page rests on that single reference video, so its recipes and use cases are opinion until another source agrees. OpenDesigner's research keeps gradients to brand and marketing surfaces by default, and any text placed on these surfaces still has to pass the locked contrast floor.

## House standards

No house standard comes from this source, which is a reference video. These standards from the non-negotiable sources apply when a surface uses gradients, blending, blur or grain:

- `STD-visual-details-21` (should): put color on a solid layer, not on a translucent foreground surface.
- `STD-visual-details-13` (should): over blurred or translucent surfaces, avoid flat gray text; use higher-contrast text, a slightly heavier weight and a little more letter spacing.
- `STD-visual-details-18` (must): never place a light translucent surface on top of another light translucent surface.
- `STD-visual-details-15` (should, web): where content meets floating chrome, fade a small blur or gradient mask instead of drawing a 1px border, and only where the floating UI overlaps content. This is the one place the standards ask for a gradient.
- `STD-accessibility-motion-11` (must, web): under `prefers-reduced-transparency: reduce`, translucent surfaces become frostier or solid.
- `STD-accessibility-motion-12` (must, web): under `prefers-contrast: more`, surfaces get near-solid backgrounds with a defined, contrasting border.
- `STD-when-to-animate-11` (must): if one of these effects is animated, that decorative motion stays on marketing pages and illustrations, never on functional, information-dense UI.
- `STD-visual-details-25` (must): when prototyping with no project tokens, use a restrained look (neutral grays, one accent color, the system font), which leaves these effects out until someone chooses them [inferred].

Also locked, as an OpenDesigner accessibility floor rather than an STD: text 4.5:1 (large text 3:1) and UI parts 3:1, measured with WCAG 2 math and no rounding up (`skills/opendesigner/references/guardrails.md`, section 4).

## What the sources teach

### Four effects, each with a named place

- **Kaleidoscope:** best for credit cards, stickers and buttons. The presenter admits that the finished effect, with text laid over it, is poor for usability even though it looks good [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- **Clay:** for isometric drawings and illustrations that need some depth [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- **Metallic:** for credit cards and metal mockups and, in his words, not much else [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- **Mesh gradient:** he calls it probably the most useful of the four and uses it on websites, posters, slideshows and almost everything else he can [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

### Blend modes and layer order do the work

- The kaleidoscope starts from a circle with a radial gradient in any colors. A second layer holds an angular gradient that alternates black and white an even number of times (eight in the video; ten or six also work) and is set to the Difference blend mode. A copy of that layer is set to Screen, and the Screen layer has to sit on top of every other layer or the effect does not work [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]). The auto-captions spell the mode "differ"; it is Figma's Difference mode.
- The metallic card is a rounded rectangle with a linear gradient of mostly grays and dark blues. The colors at the edges matter less; what makes it read as metal is a noticeable change of color in the middle. A white radial gradient set to Overlay adds depth and thickness, and two inner shadows finish it [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- A tint layer changes the metal: one more layer with a 20% fill in a red, orange or blue gives a rose gold, gold, bronze or even titanium feel [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- A mesh gradient needs no plugin: a blurred, semi-transparent circle as the background, then more blurred, semi-transparent circles on top set to Overlay, repeated until a mesh comes together. The more layers overlap, the brighter and more vibrant it gets, so 8 to 10 layers or more are fine; then adjust colors, blurs and transparency until it looks right, because making one is "more of an art than a science" [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

### Depth from paired inner shadows

- Clay is a rectangle in a color that is not saturated, because saturated colors don't work well for this effect, with one inner shadow covering the top and right edges and a second covering the bottom and left edges. An optional drop shadow improves it [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

### Texture

- Noise appears once: when the kaleidoscope works, the presenter improves it by first adding noise with the Noise & Texture plugin, then thicker text set to Overlay. It is the only step in the video that needs a plugin [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

### What the video leaves out

- The inner-shadow, blur and transparency values are only shown on screen, so none of the recipes can be rebuilt exactly from what is said; the kaleidoscope's recap is also on screen only [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- It covers Figma only, with no CSS or native code, and it dates from April 2024, so Figma's interface and the plugin may have changed [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- The use cases are the presenter's opinion, not tested guidance, and the effects are decorative showcase pieces rather than advice for core UI [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

## Where they agree and disagree

With a single source, the comparisons are with OpenDesigner's research, the other learning-wiki cards and the house standards.

- **Where gradients belong (partly agree).** DC-L01-25 and Q-color-25's default `brand-only` keep gradients on brand and marketing surfaces and off interactive components. A mesh gradient behind a website section, poster or slideshow fits that default [inferred]. The kaleidoscope on a button does not: it would need the `components` option, and the presenter himself says its usability is poor [S-L19-058].
- **How many hues (differs from other videos).** DC-L19-12 records other practitioners. One is stricter: no gradient is usually cleaner, and a gradient that is really needed uses shades of one color [S-L19-045]. Another says mesh gradients with noise now read as "AI" and keeps noise sparing [S-L19-082]. The mesh and the kaleidoscope here use any colors, so under DC-L19-12's one-hue heuristic they stay decoration on brand surfaces [inferred].
- **Color space (not covered).** DC-L01-25 blends gradients in OKLab and notes, as its own inference, that sRGB blends between complementary hues pass through a gray middle. The video mixes by eye in Figma and names no color space [S-L19-058].
- **Clay and soft styles (agree, with a limit).** DC-L15-01 offers the soft (neumorphic) style only with a contrast warning, and DC-L19-67 adds that an effect drawn only with inner shadows cannot be a control's only boundary (3:1, WCAG 1.4.11). The clay recipe is made of inner shadows, but the video uses it for illustrations, not controls [S-L19-058], which keeps it clear of that limit [inferred].
- **Clay as an illustration style (agree).** DC-L05-19 lists isometric and dimensional illustration as a style (IBM's isometric drawings, Airbnb's move to clay-like 3D icons), and DC-L19-75 already offers clay and isometric illustration as an option. The clay recipe is one way to draw that style in Figma [inferred].
- **Metal (agree).** DC-L19-67 keeps metal to card and mockup visuals, as the video does [S-L19-058].
- **Text on effects (conflicts with the locked floor).** The kaleidoscope's Overlay text is accepted as poor for usability [S-L19-058]. OpenDesigner locks text contrast at 4.5:1, and DC-L01-25 asks for that ratio at the lowest-contrast point of a gradient. Text blended over a striped pattern changes contrast from point to point, so it can only be decoration beside a real, readable label [inferred].
- **Noise (agree).** DC-L19-12 treats noise as an image asset rather than a token and keeps it sparing; the video adds it as a finishing step on one effect only [S-L19-058].
- **Tokens (a gap).** DTCG has a `gradient` type (DC-L01-25) and shadow layers with `inset`, which DC-L19-67 proposes for effects such as clay. No research card gives a token for a blend mode, so blend-mode recipes stay design assets or component code rather than tokens [inferred].

## Decisions this informs

- **Q-color-25** (where gradients are allowed): mesh gradients on marketing surfaces fit `brand-only`; a kaleidoscope button would need `components` [S-L19-058].
- **Q-dir-01** (overall look): the clay rectangle is a visual sample for `soft`, as DC-L19-67 proposes.
- **Proposed Q-depth-07** (special surface effects, DC-L19-67): this source supplies the `clay` and `metal` options and their limits (illustrations; cards and mockups) [S-L19-058].
- **Q-img-04** (illustrations): clay for isometric drawings and illustrations that need depth (DC-L19-75) [S-L19-058].
- **Q-color-03** (how colorful): clay needs muted rather than saturated colors [S-L19-058]; a `vivid` palette would need a separate muted set for clay illustrations [inferred].
- **Q-img-07** (where brand shapes and patterns show up): mesh-gradient backgrounds are a candidate for its default `expressive-only`, special screens only [inferred].

## Visual examples worth showing

- The four effects side by side on the surfaces the presenter names: a kaleidoscope sticker or card, a clay isometric illustration, a metallic credit card with its rose-gold variant, and a mesh-gradient poster or hero background [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- A mesh gradient with a few overlapping layers beside one with 8 to 10 or more, brighter and more vibrant [S-L19-058].
- The kaleidoscope with the Screen layer on top, beside the broken version where it sits lower [S-L19-058].
- A metallic gradient with and without the color change in the middle [S-L19-058].
- Clay in a saturated color beside clay in a muted one [S-L19-058].

## Open questions

- The shadow, blur and transparency values are only on screen. Should someone read them from the video or its linked Figma file before these recipes become templates, and does that file carry a licence that allows it?
- Should OpenDesigner translate the recipes into code (CSS blend modes, blur filters and inset shadows, or their SwiftUI equivalents)? The source is Figma-only and says nothing about performance or dark mode.
- Is text on a blended, patterned surface ever acceptable, for example as decoration beside a readable label, and how would `engine.py validate` measure it?
- No second source covers blend modes or noise directly. The neighbouring advice is in the [[synthesis/color|Color synthesis]] (gradients and texture) and the [[synthesis/depth-shadows-and-borders|Depth, shadows and borders synthesis]] (inner shadows and glass); another source would confirm or correct these use cases.
