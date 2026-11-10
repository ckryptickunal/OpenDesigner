---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/color.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-color
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/color.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - color
  - palette
  - neutrals
  - oklch
  - semantic-colors
  - dark-mode
  - contrast
  - tokens
  - gradients
  - indigo
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/color.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-color`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/color.md

## Summary

This Refero color guide teaches how to build a restrained UI palette: answer context questions first, work in OKLCH, and structure the palette as four layers (neutrals, one primary accent, semantic colors, and optional effects). It gives concrete scales and hex values for an 11-step neutral ramp, accent step roles for default/hover/active, semantic color sets with background, border and on-color pairs, a 60/30/10-style distribution, and a two-colors-per-component limit. It covers WCAG AA contrast minimums, why dark themes need their own neutral scale rather than inversion, browser-level dark mode settings (color-scheme and theme-color), purpose-based token naming, a four-step palette-from-scratch process, gradient rules and anti-patterns led by the indigo/violet ban. For a design system it is close to a complete color token spec with a reference implementation for light and dark.

## Key Ideas

- When in doubt use fewer colors, more neutrals and stricter purpose; restraint beats colorful.
- Product UI needs fewer colors and strict semantics; marketing can carry more emotion and gradients.
- HSL lightness is not perceptually even, so generate palettes in OKLCH and store hex for production.
- A palette needs four layers: neutrals, one primary accent, semantic colors, and effects only if needed.
- Neutrals make up 70-90% of the UI and need 10-12 steps with a slight warm or cool character.
- Semantic colors work as sets: a main color, a background, a border and an on-color for text.
- Use at most 2 colors per component, and make hover and active a predictable darker or lighter step.
- Secondary text that is too pale is the most common contrast failure.
- A dark theme gets its own neutral scale, with lighter surfaces for elevation and low-contrast borders.
- Set color-scheme and theme-color so scrollbars, form controls and browser chrome match the theme.
- Name tokens by purpose (primary, text-muted), never by color (blue, light-blue).
- Pick semantic colors that do not clash with the primary.
- Gradients must never be the only thing that makes an element visible, and must keep text contrast across the whole gradient.

## Entities

- [[entities/oklch|OKLCH]] (concept): Perceptually uniform color space recommended as the source of truth for generating scales.
- [[entities/hsl|HSL]] (concept): Intuitive color model the guide says misrepresents perceived brightness.
- [[entities/tailwind-css-colors|Tailwind CSS Colors]] (library): Curated palette suggested for MVPs and scale generation.
- [[entities/radix-colors|Radix Colors]] (library): Curated palette suggested for MVPs and scale generation.
- [[entities/open-color|Open Color]] (library): Curated palette suggested for MVPs and scale generation.
- [[entities/wcag-aa|WCAG AA]] (concept): Contrast standard whose minimum ratios the guide lists.
- [[entities/color-scheme|color-scheme]] (concept): CSS property and meta tag that makes scrollbars, inputs and system dialogs follow dark mode.

## Topics

- [[topics/color|Color]]: Four-layer palette structure, neutral and accent scales with step roles, semantic sets, 60/30/10 distribution, 2-colors-per-component limit, OKLCH workflow, gradients and the indigo ban.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Dark theme needs its own neutrals (#0f0f0f bg, #f0f0f0 text, not pure black/white), lighter elevated surfaces, rgba white borders, and color-scheme/theme-color settings.
- [[topics/accessibility|Accessibility]]: WCAG AA minimums of 4.5:1 for body text and 3:1 for large text and UI components; pale secondary text and text on tints are the common failures.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Name tokens by purpose; gives a minimum token set and a complete reference token system for light and dark.
- [[topics/gradients-blend-modes-and-texture-effects|Gradients, blend modes and texture effects]]: Gradients only when they support brand, keep readability and stay localized; subtle over dramatic; never the only means of visibility.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS custom property examples, meta color-scheme and theme-color tags, and a dark-mode fix for native select on Windows.
- [[topics/ai-assisted-design|AI-assisted design]]: Treats indigo/violet as the fingerprint of AI-generated design and asks four justification questions before using purple.

## Notable Claims

- Using fewer colors, more neutrals and stricter purpose eliminates 50% of AI slop before you start. Evidence: 0. Context First, Hard rule
- HSL poorly represents perceptual brightness: a 50% lightness yellow looks much brighter than a 50% lightness blue. Evidence: The Problem with HSL
- OKLCH provides perceptually uniform lightness, so steps from 50 to 950 look even. Evidence: The Solution: OKLCH
- Neutrals are 70-90% of a UI. Evidence: 2.1 Neutrals (Most Important)
- Secondary text that is too pale is the number one contrast issue. Evidence: Common Failures
- Mechanically inverting colors for dark mode gives eye-burning contrast and an amateur look. Evidence: 5. Light and Dark Themes, The Wrong Way
- Without color-scheme: dark, scrollbars stay light gray and form inputs and system dialogs get wrong colors. Evidence: Why this matters
- A button with brand gradient, colored border, colored shadow and colored text is almost always garbage. Evidence: Component Color Limit

## Quotes

> When in doubt — fewer colors, more neutrals, stricter purpose. Restraint beats "colorful."

> Never name tokens by color. Name by purpose.

> spacing creates breathing room, not faded text

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: The 'eliminates 50% of AI slop' figure is a rhetorical claim, not a measurement.
- Caveat: The section titled 60/30/10 actually gives ranges (60-80%, 10-20%, 5-10%) rather than exactly 60/30/10.
- Caveat: The hex values appear to match Tailwind's default palette [inferred]; they are examples, not a brand.
- Caveat: The 'acceptable' gradient example uses #667eea to #764ba2, a blue-violet pair, which sits uneasily with the guide's own indigo/violet ban [inferred].

### Rules and practices

- **should** (color, all): Before choosing colors, decide whether it is product UI or marketing, how data-dense it is, and whether a brand exists. Why: Product UI needs fewer colors and strict semantics; dashboards need muted accents and high text contrast; an existing brand should be translated into tokens, not painted everywhere. [0. Context First]
- **should** (color, all): Generate and adjust palettes in OKLCH, keep the OKLCH logic as the source of truth, and store production values as hex. Why: OKLCH lightness is perceptually uniform, so scale steps look even; HSL is not. Values: oklch(0.55 0.2 250), oklch(0.48 0.2 250), oklch(0.41 0.2 250). [Practical workflow]
- **should** (color, all): Give neutrals 10-12 steps (50 to 950) with a slight warm or cool character, consistent across light and dark themes. Why: Neutrals are 70-90% of the UI; this is where you win or lose. Values: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950. [2.1 Neutrals (Most Important)]
- **consider** (tokens, all): Map neutral steps to roles: 50 near-white backgrounds, 100-200 surfaces, 300-400 borders, 500 placeholder, 600-700 secondary text, 800-900 primary text, 950 near-black. Why: Gives each neutral a predictable job. Values: #fafafa, #f5f5f5, #e5e5e5, #d4d4d4, #a3a3a3, #737373, #525252, #404040, #262626, #171717, #0a0a0a. [Scale reference]
- **must** (color, all): Do not use pure #000 on white for body text; use near-black. Why: Listed as a red flag; near-black such as #0b0b0b is recommended. Values: #000, #0b0b0b. [Never use pure #000 on white as body text]
- **must** (color, all): Do not make text gray to create breathing room; use spacing instead. Why: Spacing creates breathing room, not faded text. [Hard rules (neutrals)]
- **should** (color, all): Use one primary accent with a full 50-950 scale and good contrast on both white and dark backgrounds; use 50-100 for tints, 500-600 default, 600-700 hover, 700-800 active. Why: One accent used sparingly and purposefully; a single hex is not enough. Values: 50-100, 500-600, 600-700, 700-800. [2.2 Primary Accent]
- **should** (tokens, all): Define each semantic color as a set: main color, background, border and on-color. Why: Semantics work through pairs, not single colors. Values: --success: #16a34a, --success-bg: #f0fdf4, --success-border: #86efac, --on-success: #ffffff. [2.3 Semantic Colors]
- **should** (color, all): Keep effects such as gradients, glows and illustration tints rare and localized in product UI. Why: Save drama for marketing. [2.4 Effects (Only If Needed)]
- **should** (color, all): Distribute color as 60-80% neutrals, 10-20% text hierarchy, 5-10% accents and semantics. Why: Distribution that works for any interface. Values: 60-80%, 10-20%, 5-10%. [3. The 60/30/10 Rule]
- **must** (components, all): Use a maximum of 2 colors per component. Why: A button with gradient, colored border, colored shadow and colored text is almost always garbage. Values: 2. [Component Color Limit]
- **must** (color, all): Make hover and active slightly darker or lighter, slightly higher contrast, with subtle shadow enhancement; do not repaint states with new colors or gradients. Why: State changes should be structure, not circus. [State Changes: Structure, Not Circus]
- **must** (accessibility, all): Meet WCAG AA: 4.5:1 for body text (16px and under), 3:1 for large text (18px+ bold, 24px+ regular) and for UI components and icons. Why: Minimum requirements for real readability. Values: 4.5:1, 3:1, ≤16px, 18px+ bold, 24px+ regular. [Minimum Requirements]
- **should** (accessibility, all): Test secondary text and text on tinted backgrounds on multiple devices; if it disappears when you squint, darken it. Why: Text that looks fine on a Retina display at noon fails on cheap monitors at 9pm. [Practical Check]
- **must** (color, all): Do not create dark mode by inverting colors; give the dark theme its own neutral scale with a near-black background and off-white text. Why: Mechanical inversion gives eye-burning contrast and an amateur look. Values: --bg: #0f0f0f, --surface: #1a1a1a, --text: #f0f0f0, --text-muted: #a1a1a1. [Dark — NOT just inverted]
- **should** (elevation, all): In dark UI show elevation with slightly lighter surfaces, subtle 1px low-contrast borders, and very soft or no shadows. Why: That is how layers communicate in dark themes. Values: --surface-elevated: #242424, --border: rgba(255, 255, 255, 0.1), 1px. [Dark Theme Elevation]
- **must** (platforms, web): Set color-scheme on the root (light, and dark under the dark theme), add <meta name="color-scheme" content="light dark">, and set theme-color meta tags per scheme to match the page background. Why: Otherwise scrollbars stay light, form inputs get wrong colors and system dialogs and autofill look broken. Values: color-scheme: light, color-scheme: dark, content="light dark", #0f0f0f, #ffffff. [Dark Mode: Technical Implementation]
- **should** (platforms, css): In dark mode, set native select background and text color explicitly from tokens. Why: Fixes a Windows issue with native selects in dark mode. Values: background-color: var(--surface-2), color: var(--text). [Native <select> fix for dark mode (Windows issue)]
- **must** (tokens, all): Name color tokens by purpose (--primary, --primary-tint, --primary-active), never by color (--blue, --light-blue). Why: The source states it as a rule and shows color names as the bad example; purpose names survive palette changes [inferred]. [6. Naming Tokens]
- **must** (tokens, all): Make components use tokens, never hardcoded hex. Why: Random hex in components is a red flag. [Components should work from tokens]
- **should** (color, all): Test a candidate primary in a button, a text link and a badge on both white and dark backgrounds; it should be strong but not fluorescent. Why: All three should feel right. [Step 2: Choose One Primary]
- **should** (color, all): Choose a success color that does not clash with the primary: green for a blue primary, teal for a green primary, green for a red primary. Why: Semantics must not clash with primary. [Step 4: Add Semantics]
- **must** (color, all): Never let a gradient be the only thing that makes an element visible, and check text contrast across the whole gradient. Why: If removing the gradient makes the element invisible, redesign. [8. Gradients, Rules]
- **must** (color, all): Do not use indigo/violet unless you can answer yes to at least one of: the brand requires purple, research references used it, there is a semantic reason, or a senior designer would not question it; otherwise use blue, teal, green, orange or a researched brand color. Why: Indigo/violet is the universal fingerprint of AI-generated design. Values: #6366f1, #8b5cf6, #2563eb, #0d9488, #16a34a, #ea580c. [THE #1 AI SLOP INDICATOR: INDIGO/VIOLET]
- **should** (color, all): Limit accent colors to 1-2. Why: Multiple competing accents are a red flag; one primary, others clearly secondary or semantic. Values: 1-2. [Quick Test]
- **should** (color, all): Usually define 3-4 semantic colors: success green, warning amber/yellow, danger red, and optionally info blue. Why: Confirmations, attention, errors/destructive actions and neutral information each need a role. Values: #16a34a, #f59e0b, #ef4444, #0ea5e9. [2.3 Semantic Colors]
- **consider** (color, all): Give the dark theme its own lighter primary and dark on-primary text, and 0.15-alpha tinted semantic backgrounds. Why: The reference dark theme shifts primary to #60a5fa with --on-primary #0f0f0f rather than reusing light values. Values: --primary: #60a5fa, --on-primary: #0f0f0f, rgba(22, 163, 74, 0.15). [Appendix: Dark theme]
- **should** (color, all): Keep gradients subtle rather than dramatic, and allow them only when they support brand identity, keep readability and stay localized (hero, illustration, small highlight). Why: Direction and angle matter more than color variety. [8. Gradients]
- **consider** (tokens, all): Start from a minimum token set: bg, surface-1/2, text, text-muted, text-subtle, border, border-strong, primary with on-primary/hover/active/tint, and success/warning/danger. Why: Components should work from tokens, not hardcoded hex values. Values: --text-muted: #5f6368, --text-subtle: #7a7f85, --border: #e6e6e6, --border-strong: #d1d1d1, --primary-hover: #1d4ed8. [Minimum Token Set]

### Decisions it informs

- Should the gray scale lean warm or cool? (`Q-color-09`)
  - Cool: Feels tech and precise. When: Tech or precision products.
  - Warm: Feels friendly and premium. When: Friendly or premium products.
  - Recommendation: Decide first; it affects the entire feel. Keep it a slight character, not colorful.
- How should palette scales be generated? (`Q-color-07`)
  - OKLCH: Perceptually even steps from 50 to 950. When: Building a lasting system.
  - Curated palettes (Tailwind, Radix, Open Color): Ready-made even scales. When: An MVP.
  - HSL: Uneven perceived brightness across hues; scales break when extended. When: Not recommended.
  - Recommendation: OKLCH as the source of truth with hex in production; curated palettes are fine for an MVP.
- How many accent colors? (`Q-color-04`)
  - One primary: Clear, purposeful accent hierarchy. When: Default.
  - Several hero colors: Competing accents; unintentional look. When: Not recommended.
  - Recommendation: One primary accent; 1-2 accents total, others secondary or semantic.
- How should dark mode be derived from light? (`Q-color-16`)
  - Mechanical inversion: Eye-burning contrast, amateur look. When: Never.
  - Separate dark neutral scale: Near-black background (#0f0f0f), off-white text, lighter elevated surfaces. When: Always.
  - Recommendation: A separate dark neutral scale.
- How dark should the dark-mode background be? (`Q-color-21`)
  - Pure black #000: Harsh contrast. When: Not recommended.
  - Near-black #0f0f0f: Softer, professional dark. When: Default.
  - Recommendation: Near-black #0f0f0f, with text #f0f0f0 instead of #fff.
- How should hover and press colors change? (`Q-color-20`)
  - Step along the shade scale: Predictable, calm darker or lighter shift. When: Default.
  - New color or gradient per state: Circus; random and noisy. When: Never.
  - Recommendation: Step along the scale: 500-600 default, 600-700 hover, 700-800 active.
- How should color roles be named? (`Q-color-12`)
  - By color: --blue, --light-blue; breaks when the palette changes [inferred]. When: Never.
  - By purpose: --primary, --primary-tint, --text-muted. When: Always.
  - Recommendation: By purpose.
- Where are gradients allowed? (`Q-color-25`)
  - Localized: Hero, illustration or a small highlight. When: They support brand identity and keep readability.
  - Across UI surfaces: Multi-hue card backgrounds look problematic. When: Not recommended.
  - Recommendation: Rare and localized; subtle over dramatic.

### Process

1. Answer context questions: Product UI or marketing, data density, and whether a brand is defined.
2. Choose neutral character: Decide warm or cool for the gray scale.
3. Choose one primary: It must work on white and dark, in buttons, links and badges, and be strong but not fluorescent.
4. Generate the scale: Use OKLCH or a curated generator such as Tailwind CSS Colors, Radix Colors or Open Color.
5. Add semantics: Pick success, warning, danger and optional info colors that do not clash with the primary, each with bg, border and on-color.
6. Build the dark theme: Write a separate dark neutral scale, lighter elevated surfaces, rgba white borders, and set color-scheme and theme-color.
7. Run the pre-ship checklist: One primary, neutrals 70-90%, readable secondary text, calm states, purpose-named tokens, no random hex, WCAG AA, rare gradients, color-scheme and theme-color set.

### Examples and visual references

- Complete light and dark token system: Cool neutral ramp #fafafa to #0a0a0a, blue primary #2563eb with hover #1d4ed8 and active #1e40af, semantic success/warning/danger/info with tinted backgrounds; dark theme with #0f0f0f background, #60a5fa primary and 0.15-alpha semantic backgrounds.
- Good vs bad hover: Good: hover just switches to a darker primary token. Bad: hover becomes a 135deg red-to-yellow gradient with a 20px colored glow.
- Acceptable vs problematic gradient: Acceptable: a hero badge with a two-stop 135deg gradient #667eea to #764ba2. Problematic: a card with a four-hue 90deg gradient.
- OKLCH primary steps: Base oklch(0.55 0.2 250), hover oklch(0.48 0.2 250), active oklch(0.41 0.2 250): only lightness changes.

### Numbers

- 50%: Share of AI slop the restraint rule eliminates, per the source. [This single rule eliminates 50% of AI-slop]
- 70–90%: Share of the UI made of neutrals. [Neutrals are 70–90% of your UI]
- 10-12: Number of neutral scale steps. [10-12 steps: 50, 100, ... 950]
- 3-4: Number of semantic colors usually needed. [2.3 Semantic Colors: Usually 3-4]
- 60-80% / 10-20% / 5-10%: Distribution of neutrals, text hierarchy, and accents plus semantics. [3. The 60/30/10 Rule]
- 2: Maximum colors per component. [Maximum 2 colors per component.]
- 4.5:1: WCAG AA minimum for body text 16px and under. [Minimum Requirements]
- 3:1: WCAG AA minimum for large text and UI components/icons. [Minimum Requirements]
- rgba(255, 255, 255, 0.1): Dark theme border color. [Dark Theme Elevation]
- 0.15: Alpha used for dark-theme tint and semantic backgrounds. [Appendix: --primary-tint: rgba(59, 130, 246, 0.15)]

<!-- /od:learn -->
