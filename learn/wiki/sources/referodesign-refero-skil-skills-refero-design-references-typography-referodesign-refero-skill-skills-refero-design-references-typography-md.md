---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/typography.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-typography
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/typography.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - typography
  - type-scale
  - letter-spacing
  - line-height
  - font-pairing
  - text-color
  - vertical-rhythm
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/typography.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-typography`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/typography.md

## Summary

Refero's typography guide for product and marketing UI. It starts from context questions, offers a safe SaaS preset (Inter, 16px, 1.55 line height, 1.2 scale, 65ch), and then covers type scale ratios with a ready Minor Third scale, the one-font rule and pairing strategies, a text color system by opacity, weights, line height, vertical rhythm derived from line height, letter spacing by size and case, measure, punctuation and text-polish details, fluid and stepped responsive type, and font loading. It lists AI-slop red flags with countable limits (8 sizes, 4 colors, 4 weights) and closes with a pre-ship checklist and a complete token set. For a design system it supplies concrete defaults and limits for nearly every typography decision.

## Key Ideas

- Decide context first: work tools need neutrality; when in doubt go denser, simpler and more neutral
- A safe SaaS preset already gives good typography; everything else is refinement
- Pick one scale ratio and stick to it; Minor Third 1.2 is the default
- Keep production to 6-8 font sizes
- One family with several weights is the professional default; a second font needs a real reason
- Text color comes from a few opacity levels, never pure black, and body never under 60% opacity
- Larger text can be lighter; smaller text needs more weight; body is always 400
- Line height: body 1.5-1.7, headlines 1.0-1.2, UI 1.2-1.4; longer lines need more
- Derive vertical spacing from line height: half the line height is the minimum step
- Spacing matters more than font size
- Tracking: positive for small text, labels and all caps; negative for large headings; always in em
- Keep body measure at 50-75 characters, about 65ch
- Polish details: real ellipsis, curly quotes, non-breaking spaces, tabular numbers, balanced headings
- Load at most 2 families and 3 weights with font-display: swap; system stack is fine

## Entities

- [[entities/refero|Refero]] (company): Publisher of the refero_skill repo this guide comes from
- [[entities/inter|Inter]] (product): Typeface used in the safe SaaS preset and recommended across product types
- [[entities/jetbrains-mono|JetBrains Mono]] (product): Monospace font suggested for code alongside Inter
- [[entities/instrument-serif|Instrument Serif]] (product): Serif in the example serif + sans pairing with Inter
- [[entities/cal-sans|Cal Sans]] (product): Display font in the example display + system pairing
- [[entities/ibm-plex-sans|IBM Plex Sans]] (product): Suggested for finance and enterprise
- [[entities/geist|Geist]] (product): Suggested for SaaS and tech
- [[entities/sf-pro|SF Pro]] (product): Suggested for SaaS and tech
- [[entities/dm-sans|DM Sans]] (product): Suggested for startups
- [[entities/plus-jakarta|Plus Jakarta]] (product): Suggested for startups
- [[entities/minor-third|Minor Third]] (concept): 1.200 type scale ratio, the guide's default
- [[entities/tabular-nums|tabular-nums]] (concept): font-variant-numeric value for aligned digits in tables, prices and stats
- [[entities/text-wrap-balance|text-wrap: balance]] (concept): CSS for balancing short headings and avoiding one-word last lines

## Topics

- [[topics/typography|Typography]]: Scale, pairing, weights, line height, tracking, measure, polish details, responsive type and font loading, with concrete values.
- [[topics/visual-hierarchy|Visual hierarchy]]: Weight stack of size, weight, color, case, spacing, style; squint, 5-second and scan tests; everything-bold flattens hierarchy.
- [[topics/spacing-and-layout|Spacing and layout]]: Vertical rhythm from line height (12/24/48/72px for a 24px line); spacing matters more than font size.
- [[topics/color|Color]]: Text color system by opacity (100/65/45/30%), never pure black, dark-mode inversion.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Dark text tokens: #F5F5F5 primary, 0.7 and 0.5 white for secondary and tertiary.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Complete CSS token set for families, sizes, weights, leading, tracking, text colors and spacing.
- [[topics/content-and-microcopy|Content and microcopy]]: Ellipsis character, curly quotes, non-breaking spaces, loading labels ending with an ellipsis.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: clamp() fluid type, breakpoints, truncation and line clamp, min-width: 0 for flex children, font-display: swap.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: AI-slop anti-patterns and countable limits that reveal amateur typography.
- [[topics/accessibility|Accessibility]]: WCAG AA 4.5:1 for body and 3:1 for large text; light text for an airy feel destroys readability.

## Notable Claims

- Typography is 90% of web design. Evidence: Typography Guide intro
- Most successful SaaS products use one font family. Evidence: Font Pairing
- Most bad interfaces look bad because of color, not font choice. Evidence: Text Color System
- Line height affects readability more than any other property. Evidence: Line Height
- AI-slop is almost always exposed by bad spacing between text blocks. Evidence: Vertical Rhythm
- Light weights (300) become illegible below 16px. Evidence: Font Weight Rules: Small text
- Default proportional figures make 111 narrower than 999. Evidence: Tabular Numbers: Why
- Weights 400, 500 and 600 cover 95% of needs. Evidence: Performance Typography Rules
- Full-width paragraphs on desktop are unreadable above 100 characters. Evidence: Line Length: Anti-pattern
- Sans-serif needs 0.1 more line height than serif. Evidence: Line Height Principles

## Quotes

> When in doubt — go denser, simpler, and more neutral.

> Spacing matters more than font size.

> If typography is beautiful but the page loads slow — it's bad typography.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Opinionated guide from Refero's skill; claims such as 'typography is 90% of web design' are rhetoric, not measurements.
- Caveat: The weights checklist is inconsistent: the quick test allows 4 weights while elsewhere 400/500/600 is 'enough' and ≤3 weights are loaded. [inferred]
- Caveat: The safe preset uses 1.55 line height and rgba(0,0,0,0.7)/0.5 text colors, while the text color system section uses 0.65/0.45; the two sets differ. [inferred]
- Caveat: The scale's pixel values (19, 23, 33, 57) are rounded from the 1.2 ratio. [inferred]
- Caveat: text-wrap: balance and pretty depend on modern browser support; the source says they degrade gracefully.

### Rules and practices

- **should** (typography, all): Before choosing fonts, answer: work tool or marketing, long reading or scanning, B2B, B2C or dev tool; in work products choose neutrality over personality. Why: Context changes line height, density, character and weight choices. [Context First]
- **consider** (typography, css): Start from the safe SaaS preset: Inter with system-ui fallback, 16px base, 1.55 line height, 1.2 scale, weights 400/500/600, 65ch max width. Why: If you use this preset as-is, your typography is already good. Values: 16px, 1.55, 1.2, 400, 500, 600, 65ch. [The Safe SaaS Preset]
- **should** (typography, all): Pick one type scale ratio and stick to it; use Minor Third 1.200 by default, 1.067-1.125 for dense UI, 1.250-1.333 for marketing and expressive layouts, and 1.618 only for landing page heroes. Why: A consistent scale creates visual rhythm. Values: 1.067, 1.125, 1.200, 1.250, 1.333, 1.618. [Type Scale: Common Ratios]
- **must** (typography, all): Use no more than 6-8 font sizes in production. Why: More = chaos; 10+ sizes is an AI-slop red flag. Values: 6-8. [Type Scale Rule]
- **should** (typography, all): Use one font family with multiple weights; add a second only for marketing pages, content-heavy products or real art direction, and almost never a third. Why: Two fonts adds complexity that must be justified. [The One-Font Rule]
- **should** (typography, all): When pairing, contrast structure (serif with sans, not two serifs) and match x-heights. Why: Pairing rules. [If You Must Pair]
- **must** (color, all): Never use pure black for text; use #0B0B0B to #111. Why: Listed under Rules That Actually Work: never pure black, use #0B0B0B–#111. Values: #0B0B0B, #111, #000. [Never pure black]
- **must** (color, all): Keep 3-4 text color levels (primary 100%, secondary 65%, tertiary 45%, disabled 30%) and never set readable body text below 60% opacity. Why: Fewer shades with stable usage; lighter text destroys readability. Values: rgba(0,0,0,0.65), rgba(0,0,0,0.45), rgba(0,0,0,0.3), 60%. [Text Color System]
- **must** (color, all): Do not lighten text for an airy feel; if it fails the squint test it is too light. Why: Almost always destroys readability. [Anti-pattern]
- **consider** (color, css): In dark mode use #F5F5F5 for primary text, rgba(255,255,255,0.7) for secondary and rgba(255,255,255,0.5) for tertiary. Why: Dark Mode Inversion tokens. Values: #F5F5F5, rgba(255,255,255,0.7), rgba(255,255,255,0.5). [Dark Mode Inversion]
- **should** (typography, all): Set body text at 400 and never bold whole paragraphs; use 500 for UI labels, 600 for buttons and subheadings, 400-700 for headlines depending on the font (serifs often look better at 400); use 300 only for large display text. Why: Weight creates hierarchy; bold everywhere flattens it. Values: 400, 500, 600, 400–700, 300. [Font Weight]
- **must** (typography, all): Use 400 minimum and preferably 500 for small text like 12px captions; do not use light 300 below 16px. Why: Smaller size needs heavier weight; light becomes illegible. Values: 12px, 400, 500, 300, 16px. [Weight + Size Relationship]
- **should** (typography, all): Set line height to 1.5-1.7 for body, 1.4-1.5 for short paragraphs, 1.0-1.2 for headlines, 0.9-1.1 for large display, 1.2-1.4 for UI text and 1 for buttons. Why: Line height affects readability most. Values: 1.5 – 1.7, 1.4 – 1.5, 1.0 – 1.2, 0.9 – 1.1, 1.2 – 1.4, 1. [Line Height: Quick Reference]
- **should** (typography, all): Give 80+ character lines 1.6-1.7 leading, 40-character lines about 1.4, and sans-serif about 0.1 more than serif. Why: Longer lines need more leading. Values: 80+, 1.6–1.7, 40, 1.4, 0.1. [Line Height Principles]
- **should** (layout, all): Derive the minimum vertical spacing step from line height × 0.5 (e.g. 16px/1.5 gives 24px lines, 12px step, 12/24/48 scale). Why: Bad spacing between text blocks exposes AI-slop. Values: 0.5, 12px, 24px, 48px, 72px. [Vertical Rhythm]
- **should** (layout, all): Fix spacing before tweaking fonts. Why: Same fonts with different spacing look like different products. [Golden Rule]
- **must** (typography, all): Add letter spacing of 0.06em-0.10em to all-caps text, 0.01em-0.02em to 11-13px small text, and 0.01em-0.03em to UI labels and buttons. Why: Without tracking caps look cramped and small text is harder to read. Values: 0.06em, 0.10em, 0.01em, 0.02em, 0.03em, 11–13px. [Letter Spacing: Quick Reference]
- **should** (typography, all): Tighten large headings (32px+) to 0 to -0.02em and display text (48px+) to -0.02em to -0.03em, only for non-light headlines where pairs like AV, WA, To do not collide. Why: Large headlines feel loose without tightening. Values: 32px+, -0.02em, 48px+, -0.03em. [When to Tighten]
- **must** (typography, css): Always specify letter spacing in em, never px. Why: Em scales with font size. Values: em. [Units]
- **should** (typography, all): Keep body text measure at 50-75 characters (about 65ch, minimum 45, maximum 85) and cap compact UI descriptions near 45ch. Why: Optimal reading width prevents eye fatigue. Values: 50–75, 45, 85, 65ch, 45ch. [Line Length (Measure)]
- **should** (content, all): Use the ellipsis character instead of three dots, curly quotes, and non-breaking spaces between numbers and units and in keyboard shortcuts; end loading labels with an ellipsis. Why: Polish details AI models often miss. Values: …, &hellip;, &nbsp;, Loading…. [Punctuation]
- **should** (typography, css): Use font-variant-numeric: tabular-nums for tables, prices, counters and stats. Why: Proportional figures make digits different widths. Values: font-variant-numeric: tabular-nums. [Tabular Numbers]
- **should** (typography, css): Apply text-wrap: balance to short headings, captions, pull quotes and card titles and text-wrap: pretty to lead and prose, but not to nav, buttons, tables, badges, code, form controls or dense labels. Why: Prevents one-word last lines that look accidental. Values: text-wrap: balance, text-wrap: pretty. [Text Wrapping for Headings]
- **should** (typography, css): Make text containers handle long content with truncation, line clamp or word breaking, and give flex children min-width: 0 so text can truncate. Why: Flex children otherwise will not truncate. Values: min-width: 0, -webkit-line-clamp: 2, overflow-wrap: break-word. [Content Overflow]
- **consider** (typography, css): Scale type with viewport non-linearly using clamp() or breakpoints: base 16px to 16-18px, H1 32-36px to 48-64px, keeping letter spacing the same. Why: Font size should respond to viewport, but not linearly. Values: clamp(1rem, 1.5vw + 0.5rem, 1.25rem), clamp(2rem, 5vw + 1rem, 3.5rem), 768px, 1200px. [Responsive Typography]
- **must** (typography, web): Load at most 2 font families and 3 weights per family, prefer variable fonts, and always use font-display: swap. Why: Beautiful typography on a slow page is bad typography. Values: font-display: swap, ≤2, ≤3. [Performance Typography]
- **must** (typography, all): Do not center paragraphs except short marketing copy, and do not use a decorative display font without brand intent. Why: Listed as instant red flags that reveal AI-generated or amateur design. [Instant Red Flags]
- **should** (process, all): Check that an interface has at most 8 font sizes, 4 text colors and 4 font weights. Why: More is likely AI-slop or needs editing. Values: ≤8, ≤4. [Quick Test]
- **should** (process, all): Test hierarchy with a squint test (3 clear levels), a 5-second test and a scan test. Why: Clear hierarchy guides the eye. Values: 3, 5-second. [Hierarchy Test]
- **must** (accessibility, all): Meet WCAG AA text contrast: 4.5:1 for body and 3:1 for large text; test layouts at 320px, 768px and 1440px. Why: Pre-ship checklist. Values: 4.5:1, 3:1, 320px, 768px, 1440px. [Pre-Ship Checklist]
- **should** (typography, all): Keep small text at 11px minimum, with positive tracking. Why: Pre-ship checklist item. Values: 11px. [Pre-Ship Checklist: Small text]
- **should** (color, all): Keep disabled text rare; if a screen has lots of disabled text, redesign it. Why: Rules That Actually Work: Disabled is rare. Values: rgba(0,0,0,0.3). [Text Color System: Rules]
- **should** (typography, css): After applying text-wrap, inspect the real breakpoints; if wrapping is still awkward, adjust copy, max-width, font-size or line-height instead of trusting CSS alone. Why: A single word on the last line of a hero title usually looks accidental. [Text Wrapping for Headings]
- **should** (typography, all): Build hierarchy in this order of impact: size, weight, color, case (caps for labels), spacing, then italic (rarely); do not make everything bold or use italic everywhere. Why: Everything bold means nothing is bold; italic everywhere is meaningless emphasis. [Hierarchy Checklist: Visual Weight Stack; Anti-patterns]
- **consider** (typography, css): Use the system font stack (system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif) when a custom font is not needed. Why: It loads instantly, looks native and is perfectly professional. Values: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue'. [System Font Stack]

### Decisions it informs

- How much bigger should each text size be than the one below? (`Q-type-09`)
  - Minor Second 1.067: Very small steps, dense When: Dense UI, dashboards
  - Major Second 1.125: Small steps When: Compact interfaces
  - Minor Third 1.200: Balanced rhythm When: General purpose
  - Major Third 1.250: More contrast between levels When: Marketing, editorial
  - Perfect Fourth 1.333: Bold, expressive jumps When: Expressive layouts
  - Golden Ratio 1.618: Dramatic When: Landing page heroes only
  - Recommendation: Minor Third 1.200 as the default choice.
- One font family or a pair? (`Q-type-05`)
  - One font, multiple weights: Professional, simple When: Default
  - Serif + Sans (Instrument Serif + Inter): Editorial contrast When: Marketing or content-heavy products with real art direction
  - Display + System (Cal Sans + system-ui): Branded headlines, native body When: Marketing pages
  - Mono accent (JetBrains Mono + Inter): Code set apart from UI When: Dev tools
  - Recommendation: One font, different weights unless there is a strong reason.
- Which font family fits the product type? (`Q-type-01`)
  - Inter, SF Pro, Geist: Neutral tech sans When: SaaS / Tech
  - Inter, IBM Plex Sans: Sober and enterprise-like When: Finance / Enterprise
  - Inter, DM Sans, Plus Jakarta: Friendlier startup feel When: Startup
  - System font stack: Loads instantly, looks native When: When custom fonts are not needed; the source says it is often better than custom fonts
  - Recommendation: Inter is safe across product types; the system stack is perfectly professional.
- Which font weights should the system use? (`Q-type-12`)
  - 400 / 500 / 600: Covers 95% of needs When: Default
  - Add 700: Strong headlines When: Headlines and strong emphasis
  - Add 300: Elegant light display When: Large display text only
  - Recommendation: 400, 500, 600; at most 3-4 weights.
- How should letter spacing change with size and case? (`Q-type-13`)
  - Size and case table: Positive tracking for small, labels and caps; negative for large headings When: Recommended
  - No extra tracking: Caps look cramped, small text harder to read, big headlines loose When: Not recommended
  - Recommendation: Use the tracking table and em units; skipping letter spacing entirely is called out.
- How wide can paragraphs get? (`Q-type-14`)
  - 65ch prose: Optimal 50-75 characters When: Article content
  - 45ch compact: Short descriptions When: Card descriptions, compact UI
  - Recommendation: 50-75 characters, max 85; never full-width paragraphs on desktop.
- Should text sizes change with screen width? (`Q-type-15`)
  - Fluid clamp(): Sizes interpolate between a minimum and maximum When: Base and hero text
  - Breakpoint steps: H1 36px, 48px at 768px, 56px at 1200px When: Discrete control
  - Recommendation: Respond to viewport but not linearly.
- What size should body text be? (`Q-type-08`)
  - 16px: Base of the safe preset and practical scale When: Default
  - 16-18px on desktop: Slightly larger reading text When: Responsive desktop
  - Recommendation: Body 16px+ with line height 1.5+.

### Process

1. Answer context questions: Work tool or marketing, reading or scanning, B2B/B2C/dev tool.
2. Start from the preset: Apply the safe SaaS preset before customizing.
3. Set the scale: Pick a ratio (default 1.2), generate sizes, keep 6-8 in production.
4. Choose family and weights: One family; 400/500/600; add a second family only with justification.
5. Set text colors: 3-4 opacity levels, no pure black, dark-mode inversion.
6. Set line height and rhythm: Leading by text type; spacing scale from line height × 0.5.
7. Add tracking and measure: Tracking table in em; 65ch prose.
8. Polish: Ellipsis, curly quotes, non-breaking spaces, tabular nums, text-wrap balance/pretty, overflow handling.
9. Make responsive and performant: clamp() or breakpoints; font-display: swap; ≤2 families, ≤3 weights.
10. Test: Count sizes, colors, weights; squint, 5-second and scan tests; run the pre-ship checklist at 320, 768 and 1440px.

### Examples and visual references

- Minor Third × 16px practical scale: 11, 13, 16, 19, 23, 28, 33, 40, 48, 57px from caption to hero (Practical Scale): A ten-step type ramp usable as a type-scale sample.
- Badge with text-transform: uppercase and letter-spacing: 0.08em versus without (ALL CAPS Rule): Untracked caps look cramped; tracked caps look polished.
- Caption at 12px with letter-spacing: 0.015em (Small Text Rule): Small text reads more easily with slight positive tracking.
- Text color tokens #0B0B0B / 0.65 / 0.45 / 0.3 black and dark-mode #F5F5F5 / 0.7 / 0.5 white (Text Color System): Three-to-four level text hierarchy by opacity in light and dark themes.
- Vertical rhythm from 16px / 1.5: 12 / 24 / 48 / 72px spacing (Vertical Rhythm): Spacing scale tied to the body line height.

### Numbers

- 1.200: Minor Third, default scale ratio [Common Ratios]
- 6-8: Maximum font sizes in production [Type Scale Rule]
- 1.55: Preset and token normal line height [Safe SaaS Preset; Appendix]
- 65ch: Prose max width [Safe SaaS Preset; Line Length]
- 60%: Minimum opacity for readable body text [Rules That Actually Work]
- 0.06em – 0.10em: All-caps tracking [Letter Spacing Quick Reference]
- 0.08em: --tracking-caps / --tracking-widest [CSS Tokens]
- 50–75: Optimal characters per line [Line Length Guidelines]
- 95%: Share of needs covered by 400, 500, 600 weights [Performance Typography Rules]
- ≤8 / ≤4 / ≤4: Max sizes, text colors and weights in the quick test [AI-Slop Quick Test]
- 4.5:1 / 3:1: WCAG AA contrast for body and large text [Pre-Ship Checklist]
- 90%: Share of web design the guide attributes to typography [Typography Guide intro]
- 11px: Minimum small text size [Pre-Ship Checklist]

<!-- /od:learn -->
