---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/icons.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-icons
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/icons.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - icons
  - iconography
  - stroke-weight
  - optical-correction
  - icon-libraries
  - accessibility
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/icons.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-icons`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/icons.md

## Summary

A short reference from the Refero design skill on icons in product UI. It argues icons should be treated like typography: functional, consistent, and drawn from one set. It gives display sizes by context, stroke weight trade-offs, icon-to-text size pairings, color and contrast rules, accessibility requirements, optical corrections, and a pre-ship checklist. It closes with a table of when to pick Lucide, Heroicons, Phosphor, Material Symbols or SF Symbols. For a design system it supplies concrete defaults for the icon size, stroke and library decisions.

## Key Ideas

- In product UI icons are functional, like type, not decoration
- Marketing may use duotone, gradients and illustrative icons, but that style must not leak into the product
- Display size depends on context: 16px dense/inline, 20-24px controls, 28-32px feature cards and empty states
- Thinner strokes suit larger sizes; thicker strokes hold up better at small sizes
- Round caps and joins read friendlier; square ones read technical and precise
- Consistency across one library matters more than the specific values
- Geometric center is not visual center; play triangles and chevrons need nudging
- Aim for equal visual mass across shapes, not equal measurements
- Icons default to currentColor so they follow text color and themes
- Semantic colors on icons are for status only
- Meaningful icons need 3:1 contrast; decorative ones are hidden from assistive tech
- Variable glyph systems (Material Symbols, SF Symbols) can match icon weight to text weight

## Entities

- [[entities/refero|Refero]] (company): Publisher of the refero_skill repository this guide comes from
- [[entities/lucide|Lucide]] (library): Outline-only icon set, 24x24 with 2px stroke; suggested SaaS default
- [[entities/heroicons|Heroicons]] (library): Outline and solid icon set; suggested for Tailwind projects
- [[entities/phosphor|Phosphor]] (library): Icon set with 6 weights, for weight flexibility without variable fonts
- [[entities/material-symbols|Material Symbols]] (library): Variable icon font with FILL, wght and opsz axes, for syncing icon weight with text on the web
- [[entities/sf-symbols|SF Symbols]] (library): Apple's glyph system that matches San Francisco weight; for native apps, not web
- [[entities/currentcolor|currentColor]] (concept): CSS keyword recommended as the default icon color so icons inherit text color

## Topics

- [[topics/icons-and-imagery|Icons and imagery]]: Icon sizing, stroke, style consistency, optical corrections, pairing with text, color and library choice for product UI.
- [[topics/accessibility|Accessibility]]: Icons carrying meaning need 3:1 contrast, action icons need aria-label or visible text, decorative icons get aria-hidden, and icon buttons need 44x44px touch or 32x32px desktop hit areas.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Pick one icon library or define your own spec so icons stay consistent; variable glyph systems fit design systems.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows font-variation-settings for Material Symbols and align-items: center for icon and text alignment.

## Notable Claims

- Most icon libraries use a 24x24px canvas, but this is convention, not law. Evidence: Icon Sizing: Most libraries use 24×24px as base
- A 2px stroke is the common default in Lucide and Heroicons. Evidence: Stroke weight: Standard (2px): common default in Lucide, Heroicons
- Circles look lighter than squares and diagonals look thinner than horizontals at the same stroke. Evidence: Optical Corrections: Weight
- Mixing icon libraries such as Lucide and Heroicons produces a collage effect. Evidence: Style Consistency: Don'ts
- Semibold text next to a thin icon looks like it comes from different systems. Evidence: Icon + Text Pairing: Weight harmony
- Optical corrections are what separate adequate icon work from premium. Evidence: Optical Corrections: What separates "adequate" from "premium."
- SF Symbols automatically match San Francisco font weight. Evidence: SF Symbols (Apple/Native)

## Quotes

> In product UI, treat icons as typography — functional, not decorative.

> Consistency matters more than specific values.

> Geometric center ≠ visual center.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Part of Refero's own design skill; library recommendations are opinion rather than measured findings.
- Caveat: Size, pairing and stroke values are framed by the source as starting points to adjust by visual testing.
- Caveat: Source pinned at commit a9b54a3; library features (e.g. Phosphor weights, Material Symbols axes) may change.

### Rules and practices

- **must** (iconography, all): Use one icon style and one library across the whole product; do not mix outline in nav with solid in buttons and duotone in cards. Why: Mixing styles or libraries reads as a collage. [Style Consistency: One language per product. No exceptions.]
- **must** (iconography, all): Keep duotone, gradient and illustrative icons in marketing surfaces only, never in product UI. Why: Product icons must be predictable, scalable and themeable. [Two Contexts: Never leaks into product]
- **should** (iconography, all): Size icons by context: 16px inline with body text, in table cells and dense UI; 20-24px in buttons, nav items and form inputs; 28-32px in feature cards, empty states and marketing. Why: Display size depends on context. Values: 16px, 20–24px, 28–32px. [Icon Sizing: Display sizes]
- **consider** (iconography, all): Use a thinner stroke (1.5px) for larger icons and a thicker stroke (2.5px+) for small icons; 2px is the standard default. Why: Thinner feels lighter and works better large; thicker has more presence and holds up small. Values: 1.5px, 2px, 2.5px+. [Stroke weight varies by library and style]
- **consider** (iconography, all): Choose round caps and joins for a friendly, modern tone, or square ones for a technical, precise tone, to match the product. Why: Caps and joins change the felt tone of the icons. [Round vs square caps/joins]
- **must** (iconography, all): Do not draw custom icons that ignore the chosen system's grid and stroke. Why: They break the one-language consistency. [Style Consistency: Don'ts]
- **should** (iconography, all): Optically center asymmetric icons: shift play triangles right by 0.5-1px and chevrons or arrows toward their point; check by placing the icon in a circle. Why: Geometric center is not visual center. Values: 0.5–1px. [Optical Corrections: Centering]
- **should** (iconography, all): Balance icons for equal visual mass rather than equal measurements. Why: Circles appear lighter than squares and diagonals thinner than horizontals at the same stroke. [Optical Corrections: Weight]
- **should** (iconography, all): Pair icon size with text size: 16px icons with 14-16px text, 18-20px icons with 16-18px text, 20-24px icons with headings, then adjust by visual testing. Why: Given as a starting point for icon and text pairing. Values: 14–16px, 16px, 16–18px, 18–20px, 20–24px. [Icon + Text Pairing]
- **should** (iconography, css): Align icons with text using align-items: center plus a 0.5-1px manual tweak where needed. Why: The source says icons often need a 0.5-1px manual tweak beyond align-items: center. Values: align-items: center, 0.5–1px. [Icon + Text Pairing: Alignment]
- **should** (iconography, all): Match icon weight to adjacent text weight, or use solid icons next to heavy text. Why: Semibold text with a thin icon looks like it comes from different systems. [Weight harmony]
- **should** (iconography, css): Color icons with currentColor by default. Why: It inherits text color and syncs with themes automatically. Values: currentColor. [Color: Default]
- **must** (color, all): Use red, green and amber on icons only to signal error, success and warning status, never as decoration. Why: Semantic colors are for status. [Color: Semantic]
- **must** (accessibility, all): Give meaningful icons, including icon buttons, toggles and status indicators, at least 3:1 contrast. Why: WCAG non-text contrast; applies to icon buttons, toggles and status indicators. Values: 3:1. [Color: Contrast]
- **must** (accessibility, web): Put an aria-label on icon-only action buttons (or show visible text nearby) and mark decorative icons aria-hidden="true". Why: Accessibility requirements for action vs decorative icons. Values: aria-label, aria-hidden="true". [Accessibility table]
- **must** (accessibility, all): Give icon buttons a hit area of 44x44px on touch and 32x32px on desktop, even if the visible icon is smaller. Why: Hit area requirement for icon buttons. Values: 44×44px, 32×32px. [Accessibility: Icon buttons]
- **should** (process, all): Before shipping, check icons at 50% scale, in grayscale, in dark theme, in table rows, for 3:1 contrast, 44px+ touch targets and same style everywhere. Why: Pre-ship checklist. Values: 50%, 3:1, 44px+. [Pre-Ship Checklist]
- **consider** (iconography, css): With Material Symbols, sync the wght axis with text weight, raise opsz for smaller icons, and toggle FILL between outline (0) and solid (1). Why: Variable glyphs can match text weight dynamically. Values: 'FILL' 0, 'wght' 500, 'opsz' 24, 400, 500, 600. [Material Symbols (Web)]
- **should** (platforms, ios): Use SF Symbols in SwiftUI/UIKit apps, not on the web. Why: They match San Francisco weight and are a native system. [SF Symbols (Apple/Native)]
- **should** (iconography, all): Pick one icon library or define your own icon spec (canvas, stroke, caps) and hold to it. Why: Consistency matters more than specific values. [Icon Sizing: Key principle]
- **consider** (iconography, all): If an icon does not read instantly, simplify it. Why: Icons are typography: consistent, optical, accessible. [Closing line]

### Decisions it informs

- Which icon library should the product start from? (`Q-icon-01`)
  - Lucide: Clean, consistent outline icons on 24x24 with 2px stroke When: Web SaaS, quick start
  - Heroicons: Outline and solid variant per icon When: Tailwind projects
  - Material Symbols: Variable glyphs whose weight, fill and optical size can follow the text When: Need weight sync with text
  - SF Symbols: Glyphs that match San Francisco weight, with a scale axis When: Apple native app
  - Phosphor: Six weights of the same icon When: Multiple weights without variable fonts
  - Recommendation: Lucide as the SaaS default; otherwise choose by scenario per the When to Use What table.
- Should product icons be outline, solid or variable glyphs? (`Q-icon-02`)
  - Outline: Lighter, less dominant icons When: Dense UIs, data-heavy products
  - Solid: Bolder, clearer action icons When: Consumer apps, clear actions
  - Variable glyphs: Icons whose weight and fill follow tokens When: Design systems (SF Symbols, Material Symbols)
  - Recommendation: Pick one style for the whole product; no mixing.
- How thick should icon strokes be? (`Q-icon-03`)
  - Thinner (1.5px): Lighter feel When: Works better at larger sizes
  - Standard (2px): Common default look of Lucide and Heroicons When: Default
  - Thicker (2.5px+): Bolder presence When: Better at small sizes
  - Recommendation: Pick one library or define your own spec; consistency matters more than the value.
- Round or square caps and joins on icons? (`Q-icon-02`)
  - Round: Friendlier, modern feel When: Friendly product tone
  - Square: More technical, precise feel When: Technical product tone
  - Recommendation: Match the product's tone.
- Which icon display sizes does the product need? (`Q-icon-04`)
  - Small (16px): Fits inline with body text, table cells, dense UI When: Dense UI
  - Medium (20–24px): Buttons, nav items, form inputs When: Controls
  - Large (28–32px): Feature cards, empty states, marketing When: Feature and empty-state surfaces
  - Recommendation: Use all three by context on a 24×24px canvas convention; adjust by visual testing.

### Process

1. Separate contexts: Decide product UI icon style (clean outline or solid, one set) separately from marketing illustration style, and keep the marketing style out of the product.
2. Pick library or spec: Choose one library from the When to Use What table, or define your own canvas, stroke and cap spec.
3. Set sizes and pairing: Use context sizes (16 / 20-24 / 28-32px) and the icon-to-text pairing table as a starting point, then adjust visually.
4. Apply optical corrections: Nudge asymmetric glyphs toward visual center and balance visual mass; test centering inside a circle.
5. Wire color and accessibility: Default to currentColor, reserve semantic colors for status, check 3:1 contrast, add aria-label or aria-hidden, and give hit areas of 44px touch / 32px desktop.
6. Run the pre-ship checklist: Check 50% scale, grayscale, dark theme, table rows, contrast, touch targets and consistency.

### Examples and visual references

- Material Symbols CSS with font-variation-settings 'FILL' 0, 'wght' 500, 'opsz' 24 (Material Symbols (Web)): An outline icon whose weight is set to match medium-weight text; FILL 1 would make it solid.
- Anti-pattern: outline icons in nav, solid in buttons, duotone in cards: Three icon styles on one screen read as icons from different systems.
- Test: put the icon in a circle and check whether it looks centered; shift a play triangle right 0.5-1px if not: Demonstrates optical centering: the nudged triangle looks centered while the geometric one looks left-heavy [inferred].

### Numbers

- 24×24px: Common icon canvas base [Icon Sizing]
- 16px / 20–24px / 28–32px: Small, medium and large icon display sizes [Display sizes]
- 1.5px / 2px / 2.5px+: Thin, standard and thick stroke weights [Stroke weight]
- 0.5–1px: Optical shift for play triangles and alignment tweak [Optical Corrections; Alignment]
- 3:1: Minimum contrast for meaningful icons (WCAG non-text) [Color: Contrast]
- 44×44px / 32×32px: Icon button hit area on touch / desktop [Accessibility]
- 6 weights: Phosphor weight count [Libraries]
- 20, 24, 40, 48: Material Symbols optical size values [Material Symbols (Web)]

<!-- /od:learn -->
