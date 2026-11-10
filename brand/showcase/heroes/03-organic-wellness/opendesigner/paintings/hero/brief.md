# Painting brief: Lullwort · hero

Made 2026-10-14 by opendesigner-paint from the design system (/Users/Kunal/Desktop/Design-System/brand/showcase/heroes/03-organic-wellness/opendesigner/build/css/tokens.css). The painting skill reads this file before planning.

- **Message:** Let the day steep out of you
- **Slot:** hero: film or still, 16:9, plates 1920x864 inside 1920x1080, at most 24 s; marketing pages and the top of onboarding
- **Style:** watercolour. One style for the whole piece (mixing needs Expression 75+ and a hero or launch film).


## Style recommendations (from the dials)
1. **watercolour**: delicate, archival, calm; pale paper under text (close on energy 15, colorfulness 42, expression 70)
2. **sketch**: calm notes and diagrams in graphite or pen; quiet tools (close on energy 15)
3. **cel**: flat 2D animation; mechanisms, impacts, friendly characters (close on expression 70)

## Palette families (only these colours; one family per plate)
Scenes import them from `src/brand.js`. Pigment mixing makes in-between colours; that is expected.

| Family | Ground | Keys | Ink | Text on it |
|---|---|---|---|---|
| brand-paper | `#fffcf8` | `#b15f3b` `#6c9c57` `#874528` | `#262420` | charcoal (15.15:1) |
| brand-tint | `#f9e8e2` | `#b15f3b` `#874528` `#6c9c57` | `#262420` | charcoal (13.03:1) |
| brand-night | `#171512` | `#b77457` `#739962` `#df9d81` | `#ece9e3` | ivory (17.82:1) |
| saturated-field | `#b15f3b` | `#6c9c57` `#fffcf8` `#f7ded3` | `#262420` | none (4.49:1) |
| archival-ink | `#f8f3ed` | `#874528` `#dbd1c1` `#81745f` | `#262420` | charcoal (14.04:1) |
| almost-nothing | `#fffcf8` | `#b15f3b` `#e9e2d6` | `#6f624e` | charcoal (15.15:1) |
| monument | `#171512` | `#b77457` `#df9d81` `#ece9e3` | `#ece9e3` | ivory (17.82:1) |
| accent2-paper | `#f1f5ef` | `#6c9c57` `#486e36` `#b15f3b` | `#262420` | charcoal (14.05:1) |

## Rules from the design system
- **Font:** Fraunces: confirm it is OFL or Apache on its source page, then ship the woff2 with its licence and a SHA-256 (widescreen-and-titles.md).
- **Text:** Words go in a fixed-anchor phrase track over the plates, never painted in. Only families whose 'text' is not 'none' may carry words; measure 4.5:1 under the glyph mask (widescreen-and-titles.md). WCAG 2.2 AA is a locked OpenDesigner floor.
- **Motion:** Films and loops only in marketing, onboarding and celebration (DC-L05-21; STD-when-to-animate-11 keeps decorative motion off functional screens; STD-easing-duration-09 allows over 1 s only for illustrative motion). In the app: muted, a still for prefers-reduced-motion, and a pause control when it plays over 5 s (WCAG 2.2.2).
- **Sound:** Muted in the product. The soft score is only for the downloadable film or a page where the person presses play.
- **Identity:** The engine's scene library recreates one earlier film ('reconstructed'; the three 'supplied' ports of unnamed sketches are left out). Use it for structure only (composition, rhythm, archetypes); every shipped plate needs this product's subject and palette. References give structure, never identity (guardrails.md).
- **Paper:** charcoal and sketch materials take `PLATES[id].material.paper = '#f8f3ed'`.
