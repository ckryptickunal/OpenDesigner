# Painting brief: Kumo Kobo · hero

Made 2026-10-14 by opendesigner-paint from the design system (/Users/Kunal/Desktop/Design-System/brand/showcase/heroes/09-japanese-ceramics/opendesigner/build/css/tokens.css). The painting skill reads this file before planning.

- **Message:** Bowls made slowly, fired in wood
- **Slot:** hero: film or still, 16:9, plates 1920x864 inside 1920x1080, at most 24 s; marketing pages and the top of onboarding
- **Style:** sketch. One style for the whole piece (mixing needs Expression 75+ and a hero or launch film).
- **Accent mark:** the brand accent will read as the style's red accent mark

## Style recommendations (from the dials)
1. **sketch**: calm notes and diagrams in graphite or pen; quiet tools (close on energy 10, colorfulness 10)
2. **watercolour**: delicate, archival, calm; pale paper under text (close on warmth 80, expression 55)
3. **charcoal**: weight and tension in value plus one accent (close on colorfulness 10, expression 55)

## Palette families (only these colours; one family per plate)
Scenes import them from `src/brand.js`. Pigment mixing makes in-between colours; that is expected.

| Family | Ground | Keys | Ink | Text on it |
|---|---|---|---|---|
| brand-paper | `#fffdf7` | `#a23a2a` `#534a48` | `#262420` | charcoal (15.23:1) |
| brand-tint | `#edebea` | `#a23a2a` `#534a48` | `#262420` | charcoal (13.04:1) |
| brand-night | `#171511` | `#8c8280` `#b4aaa8` | `#ebe9e3` | ivory (17.92:1) |
| saturated-field | `#a23a2a` | `#fffdf7` `#e6e2e1` | `#262420` | ivory (6.5:1) |
| archival-ink | `#f9f4ea` | `#534a48` `#dcd1ba` `#827455` | `#262420` | charcoal (14.13:1) |
| almost-nothing | `#fffdf7` | `#a23a2a` `#eae2d2` | `#716345` | charcoal (15.23:1) |
| monument | `#171511` | `#8c8280` `#b4aaa8` `#ebe9e3` | `#ebe9e3` | ivory (17.92:1) |

## Rules from the design system
- **Font:** Shippori Mincho: confirm it is OFL or Apache on its source page, then ship the woff2 with its licence and a SHA-256 (widescreen-and-titles.md).
- **Text:** Words go in a fixed-anchor phrase track over the plates, never painted in. Only families whose 'text' is not 'none' may carry words; measure 4.5:1 under the glyph mask (widescreen-and-titles.md). WCAG 2.2 AA is a locked OpenDesigner floor.
- **Motion:** Films and loops only in marketing, onboarding and celebration (DC-L05-21; STD-when-to-animate-11 keeps decorative motion off functional screens; STD-easing-duration-09 allows over 1 s only for illustrative motion). In the app: muted, a still for prefers-reduced-motion, and a pause control when it plays over 5 s (WCAG 2.2.2).
- **Sound:** Muted in the product. The soft score is only for the downloadable film or a page where the person presses play.
- **Identity:** The engine's scene library recreates one earlier film ('reconstructed'; the three 'supplied' ports of unnamed sketches are left out). Use it for structure only (composition, rhythm, archetypes); every shipped plate needs this product's subject and palette. References give structure, never identity (guardrails.md).
- **Paper:** charcoal and sketch materials take `PLATES[id].material.paper = '#f9f4ea'`.
