# Painting brief: Larder · hero

Made 2026-10-14 by opendesigner-paint from the design system (/Users/Kunal/Desktop/Design-System/brand/showcase/app-screens/03-recipe-editorial/opendesigner/build/css/tokens.css). The painting skill reads this file before planning.

- **Message:** a bowl of charred tomato and butter bean stew, seen from above
- **Slot:** hero: film or still, 16:9, plates 1920x864 inside 1920x1080, at most 24 s; marketing pages and the top of onboarding
- **Style:** watercolour. One style for the whole piece (mixing needs Expression 75+ and a hero or launch film).


## Style recommendations (from the dials)
1. **watercolour**: delicate, archival, calm; pale paper under text (close on energy 35, colorfulness 65, expression 70)
2. **pointillism**: luminous, saturated, textured; forms that dissolve into dots (close on colorfulness 65, expression 70)
3. **cel**: flat 2D animation; mechanisms, impacts, friendly characters (close on colorfulness 65, expression 70)

## Palette families (only these colours; one family per plate)
Scenes import them from `src/brand.js`. Pigment mixing makes in-between colours; that is expected.

| Family | Ground | Keys | Ink | Text on it |
|---|---|---|---|---|
| brand-paper | `#fffcf9` | `#c8401f` `#6c7d00` `#e6b339` `#9f3117` | `#272420` | charcoal (15.11:1) |
| brand-tint | `#ffe6e0` | `#c8401f` `#9f3117` `#6c7d00` `#e6b339` | `#272420` | charcoal (12.98:1) |
| brand-night | `#171511` | `#d1644b` `#7a8c21` `#deb55d` `#f99077` | `#ece8e3` | ivory (17.84:1) |
| saturated-field | `#c8401f` | `#6c7d00` `#e6b339` `#fffcf9` `#ffdbd2` | `#272420` | ivory (4.88:1) |
| archival-ink | `#faf3e9` | `#9f3117` `#e0d0b9` `#877255` | `#272420` | charcoal (14.02:1) |
| almost-nothing | `#fffcf9` | `#c8401f` `#ede1d1` | `#766144` | charcoal (15.11:1) |
| monument | `#171511` | `#d1644b` `#f99077` `#ece8e3` | `#ece8e3` | ivory (17.84:1) |
| accent2-paper | `#f3f5ec` | `#6c7d00` `#505d00` `#c8401f` | `#272420` | charcoal (14.04:1) |
| accent3-paper | `#f8f4ec` | `#e6b339` `#805f00` `#c8401f` | `#272420` | charcoal (14.08:1) |

## Rules from the design system
- **Font:** Fraunces: confirm it is OFL or Apache on its source page, then ship the woff2 with its licence and a SHA-256 (widescreen-and-titles.md).
- **Text:** Words go in a fixed-anchor phrase track over the plates, never painted in. Only families whose 'text' is not 'none' may carry words; measure 4.5:1 under the glyph mask (widescreen-and-titles.md). WCAG 2.2 AA is a locked OpenDesigner floor.
- **Motion:** Films and loops only in marketing, onboarding and celebration (DC-L05-21; STD-when-to-animate-11 keeps decorative motion off functional screens; STD-easing-duration-09 allows over 1 s only for illustrative motion). In the app: muted, a still for prefers-reduced-motion, and a pause control when it plays over 5 s (WCAG 2.2.2).
- **Sound:** Muted in the product. The soft score is only for the downloadable film or a page where the person presses play.
- **Identity:** The engine's scene library recreates one earlier film ('reconstructed'; the three 'supplied' ports of unnamed sketches are left out). Use it for structure only (composition, rhythm, archetypes); every shipped plate needs this product's subject and palette. References give structure, never identity (guardrails.md).
- **Paper:** charcoal and sketch materials take `PLATES[id].material.paper = '#faf3e9'`.
