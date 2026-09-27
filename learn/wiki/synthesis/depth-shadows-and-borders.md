---
type: synthesis
title: Depth, shadows and borders
created: 2026-09-24
updated: 2026-09-28
sources:
  - 66oOi9OLMCw
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - EHwZzWd-OnQ
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - If7iCPDy2vk
  - Lp6ey4AyDzA
  - MZSm6MA8bww
  - NtZeYmTMuo4
  - c1TvOcKdBVE
  - eks-readme
  - eks-skills-apple-design-skill
  - eks-skills-prototype-picker
  - gKM6b2EnW1k
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - ulSOdTgoGeY
  - vaul-getting-started
tags:
  - od-area-shape-depth
---

# Depth, shadows and borders

## In short

Depth is how a design shows that one surface sits above another, using shadows, borders, color steps or see-through "glass". Most sources agree that shadows and borders are usually too strong: soften them, or remove the ones that don't help. In light mode, a soft shadow or a faint edge separates a card from the page; in dark mode shadows barely show, so raised surfaces get lighter instead. Many lists and sections need no lines at all, because space alone separates them. Glass (blurred, see-through surfaces) belongs on bars, toolbars and sheets, and it must turn frostier or solid when a person asks their device for less transparency.

## House standards

- **STD-visual-details-14** (should): separate surfaces with a semi-transparent shadow rather than a solid, opaque border.
- **STD-visual-details-15** (should): don't put a 1px border under a sticky header. Fade a small blur or gradient mask where content passes under floating chrome, and only where they actually overlap.
- **STD-visual-details-16** (should): build nav bars, toolbars and sheets as translucent layers (`backdrop-filter: blur()` over a semi-transparent background) with content scrolling underneath.
- **STD-visual-details-17** (should): use darker, heavier materials for structural regions such as sidebars, and lighter materials to draw attention to interactive elements.
- **STD-visual-details-18** (must): never place a light translucent surface on another light translucent surface.
- **STD-visual-details-19** (should): bigger surfaces get a stronger blur and a deeper shadow than small chips.
- **STD-visual-details-20** (should): a modal task gets a dimming scrim and pushes the background back. A parallel, non-blocking panel gets translucency and offset without a scrim. Each parent in a stack of sheets is progressively dimmed.
- **STD-visual-details-13 / -21** (should): over translucent surfaces, use higher-contrast, slightly heavier text rather than flat gray, and put color on a solid layer, not on the translucent one.
- **STD-accessibility-motion-11** (must): under `prefers-reduced-transparency: reduce`, make translucent surfaces frostier or solid (raise the background opacity, drop the blur).
- **STD-accessibility-motion-12** (must): under `prefers-contrast: more`, use near-solid backgrounds with a defined, contrasting border.
- **STD-enter-exit-origin-31** (should): a glass surface enters and exits by animating its blur and scale together, not by a plain fade. **STD-enter-exit-origin-12** (should): a modal's backdrop fades with the modal on the same timing.
- **STD-performance-properties-19** (must): in React Native, never animate Android elevation or BlurView intensity. Crossfade a pre-shadowed or static blurred layer instead.
- **STD-process-review-taste-45** (must): the prototype picker keeps its own fixed shadow and glass and is never restyled with project shadows or borders.
- `standards.json` already records the conflicts between STD-visual-details-14, -15, -16, -19 and -20 and OpenDesigner's current defaults. They are summarized below.

## What the sources teach

### Fewer and softer effects
- Overusing shadows, glows and gradients makes a design look cluttered and amateur. Figma's default drop shadow is too harsh: change the shadow color, usually to a light gray, and raise the blur a lot rather than only lowering opacity, or remove the shadow entirely [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Look at gradients and drop shadows honestly and remove them if they aren't working; that often makes a site feel more professional [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Most shadows are too strong: lower the opacity and raise the blur. If the shadow is the first thing you notice, it is being used wrong [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).

### A shadow recipe, when you keep one
- Kole Jain's basic recipe: the x offset stays at or below the y offset, the blur is 1.3-2 times the y offset, and opacity drops from Figma's 25% preset to 15-20%. Darker backgrounds need the stronger end [S-L19-057]. He calls this his own strategy.
- Match the strength to the layer: cards need less shadow, and content that sits above other content, such as popovers, needs more [S-L19-052]. The Emil Kowalski skill adds that bigger surfaces should read as thicker (stronger blur, deeper shadow), and suggests heavier shadow over busy or text content and lighter shadow over plain backgrounds [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Shadow color: pop-ups in a mostly white dashboard get a very subtle shadow in a very light gray, not a transparent black [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- A fully specified example: the picker's shadow is an inset 1px white hairline at 0.08 opacity, plus `0 8px 24px` at 0.24 and `0 2px 6px` at 0.12 in black, with no other shadows or borders allowed [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).

### Edges: border, ring or shadow
- Emil Kowalski's README gives "a solid border instead of a semi-transparent shadow" as one of the small agent mistakes that add up [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- Steve Schoger avoids solid-color borders next to a shadow because the join looks muddy. He uses an outer ring of gray 950 at 10% opacity on buttons, screenshots and the nav's bottom edge, an inset ring on top of screenshots, and a small shadow to lift a secondary button [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- On a light background, cards alone look washed out and a subtle shadow helps only a little. Don't reach for a thin black border; define the edge with roughly 85% white [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A very subtle outline around cards and nearly every element lets the palette stay pure white or near white [S-L19-059]. Inputs get an off-white fill with the stroke at 40% opacity [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Rip out strokes that aren't needed, or dim them a lot if contrast is a worry [S-L19-045]. Rather than add another colored background layer to a card, a simple border is sometimes cleaner [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).

### Separation without lines
- A good list comes down to separation by space, by lines or dividers, or by color. Stacking items into one list is less cluttered than giving each its own border [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Lose the lines: divider lines are often redundant, so space items apart, and if they must sit tight, use a subtle background on alternating rows [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- Many separators and containers feel cluttered even with little content. In multi-column layouts, space should do the separating [S-L19-057].
- Don't fill a wide canvas with containers until there are borders on borders and three radii stacked together. A single line and a column edge can do the card's job [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- Line dividers are coming back, but lines on everything look like an old slide deck, and dividers don't have to be straight; rounded ends can work [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]).
- Tints can replace lines. Examples: a pricing card's price area on a reduced-opacity primary tint [S-L19-075]; a softly tinted "well" (gray 950 at 5%, no border) behind screenshots [S-L19-103]; page sections on adjusted backgrounds [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- Under floating chrome, use a scroll-edge blur or gradient mask rather than a 1px divider [S-L19-020].

### Depth in dark mode
- Dark mode is less flexible than light mode: surfaces always get lighter as they rise, so a raised card needs a lighter color or just a border [S-L19-039].
- Dark mode has no shadows the way light mode does. Make the card lighter than the background, and lower the contrast of a light border that is too strong [S-L19-052].
- Kole Jain's step in HSB (hue, saturation, brightness): each card layer gets about 4-6 more brightness and 10-20 less saturation than the one below, repeated for every extra layer [S-L19-070].
- Don't just invert light mode. Brighten borders and the main card surfaces more than an inversion would [S-L19-051]. A darker background behind lighter cards reads as farther back, and frosted glass can help a dark design that still looks flat [S-L19-085].
- Personal preference only: outlines on dark mode, background colors on light mode [S-L19-047].

### Glass and materials
- The Apple-design skill makes nav bars, toolbars and sheets translucent layers, and says:
  - heavier materials mark structure and lighter ones mark interactive elements;
  - never put light glass on light glass;
  - text over glass must be legible and color belongs on a solid layer;
  - glass should materialize (blur and scale) rather than fade.
  Its sample toolbar is `rgba(255, 255, 255, 0.6)`, `blur(20px) saturate(180%)`, with a 1px top border at `rgba(255, 255, 255, 0.4)` read as light catching the material. It turns solid under reduced transparency and near-solid with a border under increased contrast [S-L19-020].
- The picker's dark glass (`rgba(10, 10, 10, 0.82)`, `blur(12px) saturate(1.4)`) works on light or dark pages, which is why it is not theme-aware [S-L19-030].
- The "dark soft glass" look common on AI startup sites is a semi-transparent rectangle with a subtle gradient, background blur, a 1px border and a soft inner shadow, optionally with a shimmer running along the border. The video gives no other values and doesn't discuss contrast or reduced motion [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).
- A tab bar can stay solid (the redesign's default) or be dark, see-through and blurred to look "a little fancier" [S-L19-075].

### Scrims (the dim layer behind a dialog)
- Dim to focus, separate to keep flow: a modal task gets a scrim and pushes the background back, a non-blocking panel gets translucency and offset without a scrim, and stacked sheets dim each parent in turn [S-L19-020].
- Vaul's starter example styles the drawer overlay `fixed inset-0 bg-black/40`, a full-screen black layer at 40% [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]). This is a good-to-have source, and the value is an example, not a rule.

### Tactile and decorative depth
- Combine inner and outer shadows to make raised, tactile buttons [S-L19-052].
- The clay effect uses two inner shadows on opposite edges (top-right and bottom-left) and a less saturated color, optionally with a drop shadow. The metal effect uses a gradient with a clear color change in the middle, a white radial highlight on Overlay blend and inner shadows. Clay suits isometric art and illustrations; metal suits credit cards and mockups and "not a whole lot else" [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- Stickers get depth from a hard drop shadow: a darker color at full opacity, offset a little [S-L19-075].
- Shadows are not the only depth tool. An offset layer behind a button on a background or image adds depth and animates easily on hover [S-L19-085].
- A prototype's focus state uses a bright yellow stroke over a blurred duplicate of the shape (about a 24px layer blur). The source doesn't check its contrast or keyboard use [S-L19-059].

## Where they agree and disagree

- **Soften or remove shadows (agree).** Three Kole Jain videos say this [S-L19-045] [S-L19-052] [S-L19-057]. The research agrees: DC-L04-12 calls a single hard shadow dated and prefers layered soft shadows. Kole Jain's 15-20% opacity falls inside DC-L04-12's light-mode alpha range of 8-24%.
- **Blur ratio (partly disagree).** Kole Jain's "blur 1.3-2 times y" [S-L19-057] is a single-video opinion. Several research examples come to about 2 times y: in L04 table C1, Fluent `0 1px 2px` and `0 32px 64px`, Polaris `0 8px 16px -4px` and Primer `0 3px 6px`. But the house-standard picker uses 3 times y (`0 8px 24px`, `0 2px 6px`) [S-L19-030], which is outside Kole Jain's range. The ratios are my own arithmetic [inferred]. All of these examples keep x at 0, which fits "x at or below y".
- **Shadow color (open tension).** Kole Jain recolors shadows to a light gray [S-L19-045] [S-L19-059]. The picker [S-L19-030] and the research recipes use near-black at low alpha: DC-L04-12 cites Polaris `rgba(26,26,26)` and Atlassian `#1E1F21`. STD-visual-details-14 asks for a *semi-transparent* shadow. The videos don't say whether the gray is also transparent. On colored or dark backgrounds, an opaque light gray and a transparent black look very different [inferred].
- **Border versus shadow (partly disagree).** Everyone avoids a strong, solid, dark edge. Kole Jain's 85% white border [S-L19-039] is a solid light border, and his subtle outline on everything [S-L19-059] probably is too (the video doesn't give its opacity) [inferred], but STD-visual-details-14 (house) prefers a semi-transparent shadow [S-L19-014]. Steve Schoger's gray-950 ring at 10% [S-L19-103] sits between them: a semi-transparent edge. It matches the `ring-shadow` option of Q-depth-01 and DC-L09-02's light-mode default (1px ring plus a soft shadow). `standards.json` notes that OpenDesigner's opaque `color.border.*` steps conflict with STD-visual-details-14, while its 10%-alpha `color.shadow.ring` agrees. DC-L04-07 and DC-L08-15 add that a border that is the *only* edge of an interactive element needs 3:1 contrast (WCAG 1.4.11). A very light border works for decorative card edges but would likely fail on inputs [inferred].
- **Lines last (agree).** Space first, then a surface change, then lines, as in [S-L19-047] [S-L19-057] [S-L19-070] [S-L19-080], matches DC-L04-08 and DC-L15-05 (space-first, lines for long lists and dense data). The scroll-edge standard (STD-visual-details-15) extends this to sticky headers. `standards.json` notes that `engine.py` still gives them a constant 1px ring. Two sources pull the other way on marketing pages: dividers as a returning trend [S-L19-050] and Schoger's decorative "canvas grid" of section borders [S-L19-103]. Both treat lines as decoration, not as separators.
- **Dark mode (agree on surfaces, differ on shadows).** Lighter-when-higher [S-L19-039] [S-L19-052] [S-L19-070] [S-L19-085] matches DC-L04-13, which uses 3-5% lightness steps. Kole Jain's HSB +4-6 brightness is close to that [inferred]. Kole Jain drops shadows on dark cards [S-L19-052], but DC-L04-12 keeps them for overlays in dark mode with doubled alpha and a 1px light edge ring.
- **Glass on the web (conflict with an existing default).** STD-visual-details-16 makes bars, toolbars and sheets translucent [S-L19-020]. Q-depth-04 and DC-L04-15 default the web to opaque with optional blur. `standards.json` records this conflict, and as a house standard, STD-visual-details-16 should prevail. Since standards v2 it says so formally: it supersedes DC-L04-15 and DC-L10-12, and Q-depth-04 now marks its `none` and `transient` options as breaking it, although the stage file's written default still reads "opaque on web with optional blur". Kole Jain's glass on cards [S-L19-055] [S-L19-085] is the `decorative` option that DC-L04-15 flags for legibility. It is dark glass, so it doesn't break STD-visual-details-18, but STD-accessibility-motion-11 still requires a solid fallback, and neither video mentions one.
- **Scrim strength (agree).** Vaul's `bg-black/40` [S-L19-095] matches the `scrim-fluent` option (black 40% in light mode) and the low end of DC-L04-18's 40-50% default. STD-visual-details-20 adds that scrims are for modal tasks only, and `standards.json` notes that OpenDesigner currently pairs every sheet with the scrim.
- **Decorative depth (fits existing presets).** Clay and tactile inner shadows [S-L19-052] [S-L19-058] correspond to the "soft" preset of DC-L15-01, which is offered with a contrast warning. The sticker's hard offset shadow [S-L19-075] corresponds to the "neo-brutalist" preset [inferred mapping]. The clay source itself limits clay to illustrations [S-L19-058].

## Decisions this informs

- **Q-depth-01** (how surfaces separate): `ring-shadow` [S-L19-103] [S-L19-014], `borders` [S-L19-039] [S-L19-059], `tonal` for dark mode [S-L19-052] [S-L19-070], and `shadow` softened for light mode [S-L19-052]. Several analyses map here. The current hybrid default holds, and its border wording should follow STD-visual-details-14.
- **Q-depth-02** (levels and dark mode): lighter per level, with Kole Jain's HSB step as a practitioner cross-check on DC-L04-13's 3-5% [S-L19-070] [S-L19-039].
- **Q-depth-03** (shadow look): soft, low alpha, scaled by layer and surface size [S-L19-052] [S-L19-020]. Kole Jain's x/y/blur/opacity recipe is an option to show, not a default [S-L19-057]. The shadow color question stays open.
- **Q-depth-04** (glass): STD-visual-details-16 should change the web default. The options `none` and `transient` are already flagged as breaking it, which leaves `control-layer` as the fit for bars, toolbars and sheets [inferred]. Always pair it with the reduced-transparency and increased-contrast fallbacks [S-L19-020]. The tab-bar variant [S-L19-075] maps here.
- **Q-depth-05** (borders and dividers): space first, then alternating rows when tight, then lines [S-L19-070] [S-L19-047]. Faint input strokes are evidence of taste [S-L19-075]. Replace the divider under a sticky header with a scroll edge (STD-visual-details-15).
- **Q-depth-06** (scrim and state tints): 40% black as the example [S-L19-095], scrims only for modal tasks, and progressive dimming for stacked sheets [S-L19-020].
- **Q-dir-04** (group by space, cards or lines): space first [S-L19-057] [S-L19-080].
- **Q-dir-01** (overall look): glass, soft and neo-brutalist looks are all demonstrated [S-L19-055] [S-L19-058] [S-L19-075].
- **Q-color-16, Q-color-23, Q-color-26** (dark-mode derivation, border strength, transparent colors): the analyses map brighter dark-mode borders [S-L19-039] [S-L19-051], dimming strokes [S-L19-045] and gray 950 at 10% or 5% [S-L19-103] here.
- **Q-motion-10** (device settings): reduced transparency and increased contrast are house musts (STD-accessibility-motion-11, -12).

## Visual examples worth showing

- Card edges four ways on a light page: no edge (washed out), a subtle shadow, a thin black border (don't) and an 85% white border [S-L19-039].
- Figma's default shadow next to a light-gray, high-blur shadow and next to no shadow [S-L19-045].
- A solid border beside a shadow (muddy) versus a gray-950 10% outer ring. Also a screenshot inset in a tinted well with an inset ring [S-L19-103].
- One list three ways: divided by lines, by space, and by subtle alternating rows [S-L19-070]. Bordered link items versus one stacked list [S-L19-047].
- A dark dashboard with card layers stepping up in brightness and down in saturation [S-L19-070]. A dark card fixed by a softer border and a lighter surface [S-L19-052].
- The translucent toolbar CSS sample beside its solid reduced-transparency twin [S-L19-020].
- The dark glass picker pill with its three-layer shadow [S-L19-030].
- A dark soft glass card with a shimmering border [S-L19-055]. A clay rectangle and a metallic card with a rose-gold tint [S-L19-058]. A 12-point star sticker with a hard offset shadow [S-L19-075].
- A drawer over a `bg-black/40` overlay [S-L19-095].
- Rounded-end dividers (Isomorphic Labs) [S-L19-050] and the "canvas grid" of section borders [S-L19-103].

## Open questions

- Should the default shadow color be a near-black at low alpha (house picker, research) or a light gray (Kole Jain)? How should the gray behave on colored surfaces?
- Should `borders` stay a Q-depth-01 option that uses opaque light borders, given STD-visual-details-14? Or should border tokens become semi-transparent, like `color.shadow.ring`?
- Is "blur 1.3-2 times y" worth a review warning, or is it only taste, given that the house picker uses 3 times y?
- In dark mode, should overlays keep a shadow with an edge ring (DC-L04-12), or go shadowless as Kole Jain suggests?
- How should the Q-depth-04 web default and `engine.py` (glass tokens only for the materials model, one 24px blur for every surface) change to honor STD-visual-details-16 and -19?
- None of the glass, clay or inner-shadow videos give their blur, opacity or inset values in speech; those appear only on screen. Should they be measured from the free Figma files before becoming presets?
