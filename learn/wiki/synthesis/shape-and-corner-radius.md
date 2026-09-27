---
type: synthesis
title: Shape and corner radius
created: 2026-09-24
updated: 2026-09-28
sources:
  - 9WVt1CelBfg
  - AH_ugxmLeUM
  - c1TvOcKdBVE
  - eMMiLeo_UGI
  - ek-the-magic-of-clip-path
  - eks-skills-prototype-picker
  - lkKGQVHrXzE
  - pGYLZyBE32o
tags:
  - od-area-shape-depth
---

# Shape and corner radius

## In short

Corner radius is how round the corners of buttons, cards, inputs and images are. Rounder corners make a product feel friendlier, and much less rounded corners make it feel more modern and professional. The mistake the sources call out most is mixing many different radii, so pick a small set and use it everywhere, images included. When one rounded shape sits inside another, give the inner one a smaller radius so the gap between them stays even. Pills (shapes with fully round ends) are the exception: they need no correction.

## House standards

- **STD-visual-details-26** (must): build UI from the project's existing tokens, radii included, and extend them when something is missing; never add a parallel set or hand-type an approximate value.
- **STD-enter-exit-origin-42** (should): when an active tab changes color, clip a styled duplicate of the tab list with `clip-path: inset(... round <radius>)` so the clip keeps the tab's rounded shape (article example `round 17px`), instead of timing text-color transitions.
- **STD-accessibility-motion-17** (should): a visual-only duplicate layer like those clipped tabs is `aria-hidden`, with `tabIndex={-1}` on its buttons.
- **STD-springs-gestures-34** (should): when a drag drives a drawer, derive the background's corner radius (with its scale and the backdrop opacity) from the same drag progress, not from a separate animation.
- **STD-process-review-taste-45** (must): the prototype variant picker is fixed chrome with `border-radius: 999px`, and it is never restyled with the project's tokens, so its pill sits outside the project's radius scale.
- **STD-mobile-touch-09** (must): touch targets stay at least 44×44pt (iOS), 48dp (Android) or a 44px hit area (web) however round or small the visible shape is. When the visual is smaller, grow the hit area, never the visual. This applies to shape because a round or pill control can look smaller than its target [inferred].

## What the sources teach

### Roundness sets the mood
- The same layout feels friendly and welcoming with round corners and large, bubbly buttons (plus a warm background and colorful visuals). With much less rounded corners, calmer premium imagery and optional background noise, it feels modern and professional [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- For an AI product's look, one redesign pairs mesh gradients and a healthy dose of noise with fully rounded corners [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Steve Schoger switched a generated site to pill buttons on every button because the horizontal padding felt a bit much. He tried it to see what would happen and liked the result; it is his taste in one video, not a tested rule [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

### One radius family, used everywhere
- Mixed corner radii make a design feel amateur. Give all smaller components one shared radius (10 pixels in the recipe app), and make components that do the same job match in size, radius and style, such as the back and skip buttons [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]). The 10 pixels is that app's value; the lasting lesson is one shared radius.
- Images count too: sharp-edged images next to rounded buttons create a disconnect on a weak landing page [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Match the radius of a product screenshot's frame to the radius used inside the screenshot itself [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

### Nested corners
- When a rounded shape sits inside another, give the inner corner the outer radius minus the gap: a 30px outer radius with a 10px gap gives a 20px inner radius. With equal radii the gap stays even along the edges but widens at the corners [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- The subtraction breaks down once the inner corner is more than 30px away, so Kole Jain estimates by eye there. Pill shapes need none of this, because the distance is the same all the way around [S-L19-070].
- Inset screenshots tightly in their container (about 8px) with a radius concentric with the container's. When a large hero screenshot is cropped to sit on the container's bottom edge, remove its bottom corner radius [S-L19-103].
- Stacking cards inside containers inside cards ends with borders on borders and three radii stacked together. That point comes from a depth-topic source and is covered in [[synthesis/depth-shadows-and-borders|Depth, shadows and borders synthesis]].

### Corner geometry
- To make round corners look rounder, set Figma's iOS corner smoothing to the maximum on all four corners. It tapers the curve just before the corner, and the difference is visible only when the two versions are stacked side by side [S-L19-070].

### Shapes beyond rounded rectangles
- `clip-path` clips an element to a shape without changing layout: `circle(50% at 50% 50%)` for a centred circle, `ellipse`, `polygon`, `url()` for a custom SVG shape, or an `inset()` rectangle that can carry rounded corners (`round 17px` on the clipped tabs) [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- The prototype picker's container, sliding highlight and items all use `border-radius: 999px`, a full pill, as part of a fixed spec [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).

## Where they agree and disagree

- **Consistency (agree).** Three sources ask for one radius family applied everywhere, images and screenshots included [S-L19-045] [S-L19-072] [S-L19-103]. This matches DC-L04-01's heuristic (delete any radius step you cannot name a component for). It sits beside DC-L04-03, which grows the radius with size (details 2-4px, controls 4-8px, containers 8-12px, overlays 12-16px or more, full for people). The two fit if "one radius for all smaller components" is read as the control role only [inferred].
- **The 10px value is opinion.** It comes from one video and one app [S-L19-045]. It sits inside the "soft 8-12px" band of Q-shape-01, and DC-L09-01's default is 6px controls with 8-12px containers. Treat it as an example, not a default.
- **Nested radius (agree, with a different fix at the edge).** Outer minus gap [S-L19-070] is DC-L04-05's concentric rule, and the concentric screenshots [S-L19-103] apply it. Both note that the rule collapses when the padding is large. Kole Jain's fix is to eyeball it; DC-L04-05 uses a floor, inner = max(outer - padding, smallest non-zero radius), after Apple's `concentric(minimum:)`. The pill exception [S-L19-070] is not stated in DC-L04-05, but it follows from the geometry [inferred].
- **Mood (agree, different words).** Round reads friendly and less-rounded reads professional [S-L19-043], in line with DC-L04-02 and DC-L09-01 (0px official and engineered, 4-6px businesslike, 8-12px friendly, pill consumer and touch-first). The sources don't mention density. DC-L04-02 and Q-shape-01 warn that pills need taller controls and should be avoided on dense, short controls, which the pill-everywhere advice [S-L19-103] does not weigh.
- **Corner smoothing (disagree on amount and platform).** Kole Jain sets iOS smoothing to the maximum for everything [S-L19-070]. DC-L04-04 records Figma's iOS preset as 60%, keeps plain circular arcs as the web default (CSS `corner-shape: squircle` is still experimental), and uses continuous corners only on iOS-targeted parts. The "max" setting is one presenter's taste for leaning into a trend.
- **Full pills as tokens (agree).** The picker's 999px [S-L19-030] matches DC-L04-06's `radius.full` convention (9999px in Atlassian, Polaris and Primer). Under STD-process-review-taste-45 it is fixed chrome, so a radius check should not count it as drift [inferred].

## Decisions this informs

- **Q-shape-01** (how soft corners feel): friendly versus professional [S-L19-043], fully rounded for an AI look [S-L19-082] and pill buttons everywhere [S-L19-103] are evidence for the options. The analysis of [S-L19-103] maps its pill-button decision to this question.
- **Q-brand-01** (personality sliders): the analysis of [S-L19-043] maps its friendly-versus-professional choice here, so roundness should follow the slider rather than be chosen alone [inferred]. The engine already does this: Q-brand-01 answers become macros that push the roundness dial (`levers.json`: playful +30, friendly +15, serious -25, authoritative -20).
- **Q-shape-02** (how many radius steps): one shared radius for small components [S-L19-045] supports a short scale. The research heuristic of deleting unnamed steps [DC-L04-01] agrees.
- **Q-shape-03** (which components get which radius): images and screenshots belong in the radius roles too [S-L19-072] [S-L19-103], not just controls and containers.
- **Q-shape-04** (circular or smoothed corners): the analysis maps [S-L19-070] here. It is evidence for offering `continuous`, but "maximum smoothing" is opinion, not a default.
- **Concentric rule (applied automatically in stage 14 through DC-L04-05):** the sources back it [S-L19-070] [S-L19-103] and add the pill exception, so the builder should skip the warning for pills [inferred].
- **Q-img-02** (image shapes): it covers aspect ratios and text on images, not corners, so the rule that image corners come from the same radius family as the buttons beside them [S-L19-072] belongs in Q-shape-03's roles, as DC-L19-61 proposes.

## Visual examples worth showing

- One layout shown twice: friendly (round corners, big bubbly buttons, warm background) and professional (much less rounded, premium imagery, noise) [S-L19-043].
- The recipe app before and after: mixed radii and mismatched back and skip buttons, then one 10px radius on every small component [S-L19-045].
- Two nested rounded rectangles with equal radii (the gap widens at the corner), then corrected to 30px outer, 10px gap and 20px inner, with a pill beside them needing no fix [S-L19-070].
- A magnified corner with and without iOS corner smoothing, stacked [S-L19-070].
- A level-one landing page where sharp images meet rounded buttons [S-L19-072].
- Feature cards with screenshots inset 8px and concentric corners, and a hero screenshot cropped at the bottom edge with its bottom radius removed [S-L19-103].
- Clip-path tabs, where a blue rounded pill (`round 17px`) slides between Payments, Balances, Customers and Billing, plus a `circle(50% at 50% 50%)` clip [S-L19-010].
- The dark glass variant picker: a 999px pill with a pill-shaped highlight [S-L19-030].

## Open questions

- Where does "smaller component" end? One shared radius [S-L19-045] and radius growing with size [DC-L04-03] need a stated cut-off, for example at the control-to-container step [inferred].
- For nested corners past the 30px limit, should the builder use DC-L04-05's floor or leave it to the eye as Kole Jain does? If a floor, what value?
- Should Q-shape-01 warn when `pill` is picked with the compact density of Q-dir-02? The sources that recommend pills never discuss density.
- What smoothing value should a `continuous` corner token carry: Figma's 60% iOS preset (DC-L04-04) or the maximum [S-L19-070]?
- Should the image radius alias the container role or the control role? The sources only say images and buttons must not clash [S-L19-072].
