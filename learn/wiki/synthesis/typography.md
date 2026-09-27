---
type: synthesis
title: Typography
created: 2026-09-24
updated: 2026-09-24
sources:
  - 7sUUzOCv47U
  - EcbgbKtOELY
  - B7k5rOgmOGY
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - P2ksReDwWkE
  - Gfsd8NNuD9g
  - Lp6ey4AyDzA
  - c1TvOcKdBVE
  - RCneB_MQ7qs
  - V3Omp1hm0Sg
  - adev-changelog
  - eMMiLeo_UGI
  - eeN7yUcIWbw
  - ek-agents-with-taste
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-prototype-picker
  - lkKGQVHrXzE
  - xHD01_Onac0
tags:
  - od-area-typography
---

# Typography

## In short

Text is most of an interface, so a few type choices shape how the whole product looks. Start from one plain font, the device's own font unless there is a reason to change it, and build importance with size, weight, line spacing and color together instead of size alone. Large text needs tighter letter spacing and tighter line spacing; small text and all-capital labels need a little more room. Keep paragraphs to a comfortable width of about 65 characters, and do not shrink text for phones. Emil Kowalski's rules on these details are locked house standards; the numbers from Kole Jain and Steve Schoger are practitioner starting points, and a number that only one video gives is an opinion.

## House standards

These apply to every system OpenDesigner builds and cannot be traded away.

- **STD-visual-details-11** (should): start from the platform's system font; switch to a custom typeface only for a stated reason.
- **STD-visual-details-07** (should): build type hierarchy from weight, size and line height set together, not from font size alone.
- **STD-visual-details-29** (should): use order, spacing and contrast so the most important thing on a screen is the most obvious.
- **STD-visual-details-05** (must): never use one letter-spacing value for every size; tighten display text and headings (for example -0.02em), give small text slightly positive tracking, leave body text near 0.
- **STD-visual-details-04** (must): give uppercase labels looser letter spacing than the same text in sentence case.
- **STD-visual-details-06** (should): line height goes down as size goes up (about 1.05 for display, 1.5 for body), higher for scripts with tall ascenders and descenders, tighter for dense UI.
- **STD-visual-details-01** (must): cap body text at about 65ch.
- **STD-visual-details-02** (must): `font-variant-numeric: tabular-nums` on price columns and on numbers that change in place (tickers, timers, counters).
- **STD-visual-details-03** (must): write the single ellipsis character (…), never three periods.
- **STD-visual-details-08** (should): emphasise interface text with weight; keep italics for citations and stress in prose.
- **STD-visual-details-09** (must): underline only links.
- **STD-visual-details-10** (must): declare a fallback font stack whose x-height and weight match the primary typeface.
- **STD-visual-details-13** (should): on blurred or translucent surfaces, avoid flat gray text; use higher contrast, a slightly heavier weight and a small letter-spacing increase.
- **STD-accessibility-motion-13** (must): respect the user's text-size setting (Dynamic Type) and scale layout with the text; on the web write spacing in rem or em.
- **STD-mobile-touch-11** (must): input, textarea and select text at 16px or larger (at least under `@media (pointer: coarse)`).
- **STD-accessibility-motion-27** (must): never disable pinch zoom; when a page zooms into an input, fix the input's font size instead.
- **STD-visual-details-25** (must): when prototyping with no project to draw tokens from, use the system font stack.
- **STD-process-review-taste-45** (must): the prototype variant picker keeps its own type (system stack, 13px, line height 1) and never takes the project's fonts.

OpenDesigner's own locked floor also applies, although it is not a STD: text contrast of at least 4.5:1 (3:1 for large text) under WCAG 2.2 AA, measured without rounding up (`skills/opendesigner/references/guardrails.md`).

## What the sources teach

### Choosing fonts

- Default to the platform's system font, because it already ships optical sizing, tracking tables and legibility tuning; use a custom face only with a reason [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). This is STD-visual-details-11.
- One font is enough for most designs. Kole says to pick a nice sans serif and not spend long on the choice [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]); elsewhere he calls one font entirely acceptable, two the limit, three a rare edge case and four a source of problems [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). He counts one font used throughout as a strength even on his lowest-graded landing page [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- If there is only one font, it is usually a sans serif [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). A second face is a display, serif or handwritten font paired with the sans [S-L19-042]. In a restaurant-software redesign, Kole kept the existing sans, dropped a monospace that did not fit and mixed in a serif for personality, "like a printed menu" [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]). The animations.dev course site added a serif to emphasise important words [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]); that is a changelog entry, not stated guidance.
- Reuse a brand face that already exists: in a skincare redesign the hero heading uses the font already on the logo and packaging (Apple's New York) [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- When the font is Inter, Schoger loads the variable version with its display cut and font features, because sites generated by Claude typically lean on plain default Inter [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]). After generating a screen with AI, fonts are one of the three biggest fixes, with alignment and color [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Check the licence before using a font found on another website [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]). Beginners tend to pair fonts badly, and a generator such as Fontjoy can suggest a pairing [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- Tool chrome keeps neutral type so it is never mistaken for the design being judged: the prototype picker uses the system stack at 13px, antialiased, never the project's fonts [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).

### Building hierarchy

- Hierarchy comes from several levers, not size alone. Emil's set is weight, size and line height [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]); Kole's is size, weight and text color, noting that most people use size only [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Rank first, then style: list every text element in order of importance, then give each a style that matches [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). Kole's preferred pattern lets size carry the heading (it need not also be bold), bolds subheadings so they scan, and keeps paragraphs at full opacity so the smallest text is not also the faintest [S-L19-042].
- Weights: avoid ultra bold and ultra thin for regular text [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]); use at most two weights, at least one weight step apart [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). With a variable font, Schoger picks an in-between 550 when medium (500) feels thin and semibold (600) feels heavy [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Emphasis: bold, not italic, and underline only for links [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]); weight adds presence without taking more space [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Text color: Kole uses two text colors, the primary at 100% and a reduced-opacity secondary, which he puts at 40-70% in one video [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]) and 45-70% in another [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). At small sizes a thinner weight and a lighter color look alike, so either can push text back [S-L19-042]. See the contrast warning under "Where they agree and disagree".
- Balance the levels: at level three of his landing-page grades the headline dominates at the expense of the sub-line [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]), and a site that puts giant headline sections next to small spec-text sections reads as two different styles [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).

### Sizes and the scale

- A ratio-based scale improves on eyeballing one page [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). Kole's method: multiply body size by the golden ratio (1.62) when there is only a heading and body text; for a full style guide use its square root, 1.27, because full 1.62 steps from a 16px base reach about 110px too fast; use the cube root for dashboards or mobile [S-L19-042]. The cube root works out to about 1.17 [inferred].
- The range depends on the product: landing pages can use up to six sizes with a large range, while dashboards normally have nothing above 24px [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). Dashboards use many small sizes with small steps between them [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Do not shrink type for phones. Mobile type stays about the size of desktop type or grows, and iOS has a 17px base font against 13px on macOS [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]). Apple states these in points; the source says pixels.
- Fluid sizes: Kole's one-line formula scales each size in a straight line between a 320px and a 1920px wide screen, wrapped in `max()` and `min()` caps [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). The apple-design skill's display sample uses `clamp(2rem, 5vw, 4rem)` [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). Only sizes change with the screen; colors, weights and pairings stay the same [S-L19-042].
- Check type on the screen it is meant for: designing zoomed out in Figma led Kole to oversized fonts and spacing [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]])[S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).

### Letter spacing

- Tracking depends on size: negative for display (for example -0.02em), slightly positive for small text, near 0 for body; one value for every size is wrong somewhere [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). Kole states the same direction: less space as text grows, more as it shrinks [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- Practitioner numbers for headings: about -2% to -3% on large header text [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]); -2% to -4% on text over about 70-80px [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]); Schoger tightens once sizes pass about 24-30px [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]). In Figma a percentage is a share of the font size, so -2% equals -0.02em [inferred].
- Uppercase needs looser tracking [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]). Schoger widens tracking whenever text is all capitals, as on his monospace uppercase eyebrows [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Over blurred or translucent surfaces use higher-contrast text, a slightly heavier weight and a small tracking increase [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Line height

- Line height goes down as size goes up: about 1.05 for display, 1.5 for body; higher for scripts with tall ascenders and descenders; tighter for dense, information-heavy UI [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Kole's rule of thumb: paragraphs around 150%, headings around 110-130% [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]); large headers about 110-120% [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). Raise line height for longer lines; Kole notes that most designers leave line height on auto, and that auto falls off for extremely large text [S-L19-042].

### Line length and line breaks

- Cap body text at about 65ch so lines stay comfortable to read [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).
- Schoger sets heading and text-block widths in `ch` (40ch for his section headings, after trying 45 and 35), and the `ch` width must sit on the same element that sets the font size, or the text comes out too narrow [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- `text-wrap: pretty` removes orphan words; when it still wraps awkwardly, try `text-wrap: balance` [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]). He also puts each sentence of a multi-sentence headline on its own line [S-L19-103].
- Use the ellipsis character … rather than three periods [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).

### Numbers and small details

- Tabular (fixed-width) digits for price columns [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]) and for tickers, timers and counters, so numbers do not jump as they change [S-L19-019] ([[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]).
- A fallback font stack whose x-height and weight match the primary face, so loading the font causes no layout shift [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).
- `font-optical-sizing: auto` on display text, because Apple designs type to change shape with size [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Respect the user's text size by writing spacing in rem or em [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Proper punctuation ("nicer commas, quotes") was a polish item on the animations.dev platform [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).

### Display type as a visual element

- Text can be a visual element that tells a story, through a distinctive or animated font [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]). A good display font can be as visually important as an image, but use giant text once or maybe twice per page [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Never set small paragraph text in a display or handwritten font [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- A giant-text hero pairs a massive headline (Oswald at 290px in his example) with very small nav text placed beneath it [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]).
- Schoger sets section titles inline with their supporting sentence at the same size, with the supporting text in a softer gray (gray 600) and medium weight, so the pair reads as one block [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

## Where they agree and disagree

**Between the sources**

- All three voices tighten large text [S-L19-020][S-L19-042][S-L19-052][S-L19-070][S-L19-103]. Emil and Kole loosen small text [S-L19-020][S-L19-042], and Emil and Schoger loosen uppercase text [S-L19-004][S-L19-103]. They disagree on where tightening starts: about 24-30px for Schoger [S-L19-103], "large header text" in one Kole video [S-L19-052] and over 70-80px in another [S-L19-070]. They also disagree on how far: Emil's example is -0.02em [S-L19-020], Kole goes to -4% [S-L19-070].
- Everyone builds hierarchy from more than size, but the third lever differs: line height for Emil [S-L19-020], text color for Kole [S-L19-057][S-L19-042].
- Font count is not a real conflict: one font is the baseline for Kole [S-L19-052][S-L19-042][S-L19-072], and a second face is added only for personality or emphasis [S-L19-062][S-L19-001].
- The house standard (system font first) outranks "pick a nice sans" [S-L19-052] and "load variable Inter" [S-L19-103]; reusing a brand face that is already on the logo and packaging [S-L19-049] is the kind of stated reason STD-visual-details-11 allows [inferred].
- Monospace depends on the brand: Schoger likes monospace eyebrows [S-L19-103], while Kole removed a monospace that did not fit a restaurant brand [S-L19-062] [inferred].
- Emil's display line height (1.05) is tighter than Kole's heading range (110-130%) [S-L19-020][S-L19-042]; both fall as size grows, and display text is larger than an ordinary heading [inferred].

**With OpenDesigner's existing research**

- Letter spacing, DC-L02-14: 0 at body sizes, +0.02 to +0.05em for 11-12px and all caps, -0.01 to -0.02em from about 32px. This agrees in direction; its 32px start sits between Schoger's 24-30px and Kole's 70-80px. `synthesis/standards.json` already records two conflicts with STD-visual-details-05: `engine.py` `tracking()` gives 0em to every size from 13px to 31px, so default headings such as title.lg (22px) and headline.sm (27px) are not tightened, and the Q-type-13 option `zero` gives one value for every size. The same `zero` option also strips the 0.05em from the uppercase label.sm style, against STD-visual-details-04.
- Line height, DC-L02-13: about 1.5 for 12-16px down to 1.1-1.15 for 48px and up. This agrees with Kole's 150% and 110-130% [S-L19-042] and with STD-visual-details-06. `standards.json` records that the engine's 4px snapping inverts leading in the default scale (title.lg at 22px gets 1.4545 while body.lg at 18px gets 1.3333).
- Weights: DC-L02-15 defaults to three weights (400, 500-600, 600-700), while Kole uses at most two [S-L19-057]. DC-L15-02's "balanced" default uses two weights and three text colors, and the Q-type-12 stage default cites a BOARD note of two weights per view. "Two per view, three in the system" would reconcile them [inferred]. DC-L02-12 (weight first, color second, italics only in running text) agrees with STD-visual-details-08.
- Scale ratio, DC-L02-09: 1.125-1.2 for dense apps, 1.25 for mixed, 1.333 and up for editorial. Kole's 1.27 sits near 1.25 and his cube root (about 1.17) sits in the dense band [S-L19-042] [inferred]. The L15 research labels golden-ratio scales as weak evidence, the Q-type-09 stage offers the golden ratio only as an optional preset, and the analysis of Kole's video calls the method his personal one.
- Number of sizes, DC-L02-10: 8-10 sizes and 12-15 styles, against Kole's cap of six sizes on landing pages [S-L19-052]. His count is per page; the card counts a whole system [inferred].
- Fluid type, DC-L02-19 and the Q-type-15 default: body and UI text stay fixed, and only display and headline styles are fluid on the web. Kole scales every size fluidly [S-L19-042]; the house skill's fluid example is a display style only [S-L19-020]. A size set purely in viewport units does not follow the user's text setting, which STD-accessibility-motion-13 requires; `clamp()` with rem ends restores that at the limits [inferred].
- Mobile sizes, DC-L02-08 and DC-L02-20: iOS body 17pt and mobile about 1.15-1.2 times desktop. This agrees with Kole's "don't shrink" [S-L19-053]. `standards.json` records that the Q-type-08 web default of a 14px UI body, also used for inputs in the engine preview, clashes with STD-mobile-touch-11 (16px inputs).
- Line length, DC-L02-17: 65-70ch, which agrees with STD-visual-details-01. `standards.json` notes that Q-type-14 `measure-45-75` and Q-layout-03 `reading` (40-80 characters) allow lines above about 65ch. No earlier card covers heading width, which is where Schoger's 40ch applies [S-L19-103]; DC-L19-29 now proposes one.
- Numerals, DC-L02-26 and DC-L02-05: tabular digits in tables and in live numbers, which agrees with STD-visual-details-02. `standards.json` notes the engine only generates `text.numeric.*` styles when Q-type-06 `numeric-face` or Q-layout-03 `data` is chosen.
- Font loading, DC-L02-06: `font-display: swap` with a metric-adjusted fallback, which agrees with STD-visual-details-10. `standards.json` notes that `engine.py` writes no `@font-face` or metric overrides. The licence warning [S-L19-050] agrees with the card; the same video's tip to save font files from other sites through developer tools does not, as its analysis caveat says.
- Typeface source, DC-L02-01, DC-L10-06 and the Q-type-01 default (`system`): this agrees with STD-visual-details-11. DC-L06-07's default (a brand face for display, a system font or text cut for body) matches the brand-font hero heading [S-L19-049] and Schoger's display cut [S-L19-103] [inferred].
- Text color, DC-L01-14: solid text tokens by default, with secondary text passing 4.5:1 on the lowest surface. Kole's opacity-based secondary text [S-L19-042][S-L19-057] is the other option, and its low end fails: black at 40% opacity on white measures about 2.85:1 and at 45% about 3.36:1, while 55% measures about 4.74:1 [inferred: WCAG 2 math on pure white]. DC-L15-02 also warns against hierarchy by color alone, which Kole's color-only demo layout [S-L19-042] would be.

## Decisions this informs

- **Q-type-01** (system, plain free font or brand font): system first (STD-visual-details-11) [S-L19-020]; brand face reuse for headings [S-L19-049]; variable Inter with display cut when Inter is chosen [S-L19-103].
- **Q-type-02** (font files and licence): check the licence of any font taken from another site [S-L19-050].
- **Q-type-03** (font style): a single font is usually a sans serif, and serif is said to read older and more authoritative (stated without evidence) [S-L19-042]; a serif can add brand personality [S-L19-062].
- **Q-type-05** (one family or a pair): one font as the baseline [S-L19-052][S-L19-042][S-L19-072]; a display, serif or handwritten second face only with a job [S-L19-042][S-L19-062][S-L19-001][S-L19-057].
- **Q-type-06** (code and numbers): tabular digits for prices and changing numbers [S-L19-004][S-L19-019].
- **Q-type-07** (variable weights and optical sizes): in-between weights such as 550 [S-L19-103]; `font-optical-sizing: auto` [S-L19-020].
- **Q-type-08** (body size): don't shrink on phones, iOS 17 versus macOS 13 [S-L19-053]; dashboards small [S-L19-052][S-L19-047]; inputs at 16px (STD-mobile-touch-11).
- **Q-type-09** (scale ratio): 1.27 for a full guide, cube root for dense screens, golden ratio only for heading plus body [S-L19-042].
- **Q-type-10** (how many styles): at most six sizes on a landing page, nothing above 24px on dashboards [S-L19-052].
- **Q-type-11** (line height): 150% body, 110-130% headings [S-L19-042]; 110-120% large headers [S-L19-052]; 1.05 display and 1.5 body, higher for tall scripts (STD-visual-details-06) [S-L19-020].
- **Q-type-12** (weights and emphasis): two weights at least one step apart [S-L19-057]; no extreme weights [S-L19-042]; bold over italic, underline only links [S-L19-004].
- **Q-type-13** (letter spacing by size): size-specific tracking is a house standard (STD-visual-details-05); the option `zero` conflicts with it; heading thresholds from [S-L19-052][S-L19-070][S-L19-103].
- **Q-type-14** (paragraph width and cut-off): 65ch body [S-L19-004]; `ch` widths on the font-size element, 40ch headings, `text-wrap: pretty` or `balance` [S-L19-103]; the ellipsis character [S-L19-004].
- **Q-type-15** (sizes change with screen width): Kole's fluid formula with caps [S-L19-042] against the fixed default; display-only `clamp()` [S-L19-020].
- **Q-type-16** (sizes by device): phone type is not smaller than desktop type [S-L19-053].
- **Q-type-17** (grow with the user's text size): scale layout with text, rem or em spacing (STD-accessibility-motion-13) [S-L19-020].
- **Q-dir-03** (how much headings stand out): wide range for landing pages, narrow for dashboards [S-L19-052]; don't let the headline swallow the sub-line [S-L19-072]; avoid a giant-versus-tiny split [S-L19-065].
- **Q-dir-02** (how much fits on a screen): denser screens take smaller sizes with smaller steps [S-L19-047][S-L19-052].
- **Q-brand-06** (bigger marketing headings): giant display text as a visual element, once or twice per page [S-L19-057][S-L19-050][S-L19-060].
- **Q-color-22** (text colors solid or see-through): Kole's 100% plus 40-70% (or 45-70%) opacity pair [S-L19-042][S-L19-057], checked against the 4.5:1 floor.

## Visual examples worth showing

- **Two ways to style a heading, subheadings and paragraphs**: a bold full-opacity heading over light paragraphs, next to a large plain heading with bold subheadings and full-opacity paragraphs [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- **Weight versus color at small sizes**: the same line made thinner, then made lighter, looking almost the same [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- **Size only versus size plus two weights and two colors**: Kole's before and after of one text block [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- **Loose versus tightened display heading**: the same large heading at 0 tracking and at -2% to -4% [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]), and a hero heading at default versus -2% to -3% tracking with 110-120% line height [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- **Landing-page scale versus dashboard scale**: up to six sizes with a wide range, against a set that stops at 24px [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]])[S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- **Phone versus desktop base size**: a 17px iOS body next to a 13px macOS body [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- **Fluid size graph**: font size against screen width from 320px to 1920px, with min and max caps [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- **Display type sample**: `clamp(2rem, 5vw, 4rem)`, line height 1.05, -0.02em, `font-optical-sizing: auto`, over a `100%/1.5 system-ui` body [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- **Giant-text hero**: a 290px display headline with very small nav text beneath it [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]).
- **Serif and sans split headline**: hero lines alternating between a serif and a sans [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- **Schoger's section treatments**: variable Inter display at weight 550 with tighter tracking, a monospace uppercase eyebrow with wide tracking, an inline title running into gray supporting text, and a 40ch heading shown with `text-wrap: pretty` and `balance` [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- **Tabular versus proportional digits**: a ticking counter and a price column in both [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]])[S-L19-019] ([[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]).
- **Font anatomy**: baseline, x-height and cap height marked on sample letters [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).

## Open questions

- Where should heading tracking start, and how tight can it go? The sources say 24-30px [S-L19-103], "large" [S-L19-052] or 70-80px [S-L19-070], the card says about 32px, and the engine currently starts above 31px. Only the direction is a house standard.
- Two weights or three? Kole's two-weight cap [S-L19-057] is one practitioner's opinion, though DC-L15-02 and a BOARD note agree with it per view; DC-L02-15 defaults to three for the system.
- Should Q-color-22 `opacity-levels` enforce a minimum opacity so secondary text passes 4.5:1 on every surface, given that Kole's 40-45% lower bound fails on white [inferred]?
- Should fluid sizing ever apply to body text, as Kole's formula does [S-L19-042], and how does a viewport-based size stay compatible with STD-accessibility-motion-13?
- Is Kole's six-size cap for landing pages [S-L19-052] a page rule worth checking in `engine.py review`, or only advice?
- Heading width has no standard. Should Q-type-14 gain a heading measure (for example Schoger's 40ch [S-L19-103]) and a `text-wrap` choice, as DC-L19-29 and DC-L19-30 propose?
- Giant display text "once or maybe twice per page" [S-L19-057] comes from one video; is it a rule for OpenDesigner's expressive styles or just taste?
- The golden-ratio method [S-L19-042] is labelled weak evidence in L15; should Q-type-09 show 1.27 as a named preset or leave it out?
