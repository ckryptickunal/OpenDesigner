---
type: synthesis
title: Dark mode and themes
created: 2026-09-24
updated: 2026-09-24
sources:
  - 66oOi9OLMCw
  - B7k5rOgmOGY
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - Lp6ey4AyDzA
  - Vy0KKvZJRH8
  - c1TvOcKdBVE
  - ek-the-magic-of-clip-path
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-prototype-picker
  - jSxxAFxjxbU
  - pGYLZyBE32o
  - sonner-toaster
  - ulSOdTgoGeY
tags:
  - od-area-modes
  - od-area-color
---

# Dark mode and themes

## In short

Dark mode is not light mode turned inside out: dark colors look more alike, so the gaps between background shades must be bigger, raised cards get lighter instead of relying on shadows, and bright accent colors move to a lighter, calmer shade. Text in dark mode is usually a light gray with pure white saved for the most important things, and the darkest background is a near-black, often tinted slightly blue or toward the brand, not pure black. The app should follow the device's light or dark setting, and whatever a library or the device paints has to be told the theme too, such as toasts and the phone's status bar color; a few pieces of chrome, like the prototype variant picker, deliberately stay the same in both themes. When the theme changes, the brightness should ease over instead of jumping. The house standards (from Emil Kowalski's sources) lock this wiring, while the visual numbers come from practitioner videos and are starting points.

## House standards

- `STD-visual-details-24` (should): give every color role a light value and a dark value.
- `STD-accessibility-motion-09` (should): ease the switch between dark and light themes instead of letting brightness jump.
- `STD-easing-duration-01` (must): a color change animates with `ease`.
- `STD-accessibility-motion-02` (must): under reduced motion, remove movement but keep the opacity and color changes that explain a state change.
- `STD-enter-exit-origin-44` (should): build a theme-switch reveal (one theme uncovering the other through an animated clip-path) with the View Transitions API, not by duplicating the page.
- `STD-visual-details-55` (must): pick libraries from the curated list; for theme switching and dark mode that is next-themes (no flash on load).
- `STD-components-toasts-drawers-22` (must): in an app with a dark theme, set the Toaster theme to `'system'` or pass the theme provider's resolved theme (Sonner defaults to `'light'`).
- `STD-components-toasts-drawers-23` (should): start from Sonner's defaults and use `invert` only to flip toasts against the theme.
- `STD-mobile-touch-20` (must): ship one `theme-color` meta tag per `prefers-color-scheme` plus `<meta name="color-scheme" content="light dark">`, set to the color at the very top of the page (the header background, not the brand color); update it from JavaScript when the theme switches by class; an installed PWA's status bar and manifest colors are the same decision.
- `STD-mobile-touch-21` (must): the mobile baseline, shipped before the first component, includes one `theme-color` per scheme.
- `STD-components-toasts-drawers-65` (should): sync Safari's `theme-color` with a drawer overlay only if it stays in step with the overlay.
- `STD-easing-duration-19` (should): a script-driven theme color that accompanies a drawer transition follows the drawer's own curve.
- `STD-accessibility-motion-11` (must): under `prefers-reduced-transparency: reduce`, translucent surfaces become frostier or solid.
- `STD-accessibility-motion-12` (must): under `prefers-contrast: more`, surfaces get near-solid backgrounds with a defined, contrasting border.
- `STD-visual-details-21` and `STD-visual-details-13` (should): color sits on solid layers, and text over glass gets higher contrast, a slightly heavier weight and a little more letter spacing.
- `STD-process-review-taste-45` (must): the prototype variant picker is fixed dark-glass chrome and never follows the project's theme.

Also locked, as an OpenDesigner accessibility floor rather than an STD: every color pair passes WCAG 2.2 AA in every mode (`skills/opendesigner/references/guardrails.md`, section 4).

## What the sources teach

### Design dark mode on purpose instead of inverting

- Dark colors look more alike, so a light palette reflected into dark loses its distinctions. Rule of thumb: double the distance between neutral steps, from about 2% apart in light to 4 to 6% in dark [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Inverting the light palette gives a result that is not awful but not ideal. Build the dark palette with its own goals: brighten borders and the main cards, because dark colors must differ more to be seen [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- Light and dark mode should feel different but consistent, not exact opposites, because dark mode needs its colors further apart [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]). The captions of this passage are muddled; this is the analysis's most consistent reading.
- Dark mode is more than a new background: text flips to white and over-saturated primary and accent colors need lighter versions [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).

### Surfaces and depth

- In dark mode, surfaces always get lighter as they rise. A raised card gets a lighter color or just a border, like a search bar; light mode is flexible here, dark mode is not [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Dark mode doesn't have shadows the way light mode does, so a card shows depth by being lighter than the background [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). The same neutral-balance idea holds as in light mode: darker background, slightly lighter foreground [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). A dark background reads as farther back than lighter cards [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- For layered dashboards: from the dark background, make each card layer about 4 to 6 brighter and 10 to 20 less saturated in HSB, and repeat for each extra layer [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]). One video's numbers, though the size of the step lines up with the 4 to 6% gap in [S-L19-039] [inferred].
- One designer prefers outlined cards in dark mode and filled cards in light mode, as a personal taste that is "totally up to you" [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- If a dark design still looks like it is missing something, frosted glass on the cards and on the colored background can lift it [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]). For shadows, borders and glass in both modes, see [[synthesis/depth-shadows-and-borders|Depth, shadows and borders synthesis]].

### How dark, and how tinted

- Use bluish blacks in dark mode instead of pure black [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Use a really dark version of the accent as the background (GitHub uses a really dark blue), or take Tailwind's 950 as the background with its 300 as the primary [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- Dark mode has room for deep purples, reds or greens, not only navy blue or gray [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- If you struggle to get color into a dark mode, set the background to a gradient of two primary colors (Gemini's baby blue and pink) and darken both, adding a little noise if you like, but not so much that it looks like TV static [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### Accents, text, borders and chips in dark mode

- Move the primary brand color to step 300 or 400 with hover at 400 or 500, dim the text and brighten the borders [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Primary and accent colors are often far too saturated for dark mode; the example blue had to become a lighter blue [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]). Bright chips should be dimmed in saturation and brightness, with that flipped for the chip text to keep hierarchy [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). Desaturate the logo a touch [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- Use light grays for text because they are easier on the eyes than white, and brighten only the most important text, such as the logo and the storage-used figure, to pure white. Lower gray brightness more aggressively than in light mode, because dark modes focus on eye strain [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- One card fix goes the other way on borders: a light card border had too much contrast in dark mode, so it was lowered [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- A light gray button with white text reads as disabled in both modes [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).

### Themes beyond light and dark

- To make a color-themed version of any design (red, green or blue), convert each neutral to OKLCH, lower the lightness slightly (captioned "003", probably 0.03), raise chroma by 0.02 and set the hue to the theme color; the source says it works as well or better in dark mode [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). One video's recipe.
- Whether to go dark at all: dark mode won't suit every site but should work on most modern-themed ones, and it changes the whole look and feel [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]). One designer switched a design to dark mode the day after starting, giving no reason beyond it looking good [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]). For color videos that push back on dark themes, see [[synthesis/color|Color synthesis]].

### Following the system and wiring the theme

- Respect the device's light and dark setting as much as possible, since every Mac lets people switch. The example macOS app also puts light and dark settings in its settings popover [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- Interface colors should adapt to light and dark, and theme changes between dark and light should be eased to avoid abrupt brightness jumps [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- next-themes is the curated pick for theme switching and dark mode because it avoids a flash on load [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- Sonner's Toaster theme defaults to `'light'` and does not follow the OS, so a dark app shows light toasts unless it passes `theme="system"` or the provider's resolved theme [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]). The Sonner docs show a `'use client'` wrapper that passes `resolvedTheme` from next-themes to the Toaster [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]). `theme` accepts `'light'`, `'dark'` or `'system'`, and `invert` shows dark toasts in light mode and light toasts in dark mode [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).
- The phone's status bar and browser chrome take their color from `theme-color`. One value gives light mode a dark bar or dark mode a white one, so ship one tag per color scheme (the samples are `#ffffff` and `#0a0a0a`), match it to the header background rather than the brand color, and update it from JavaScript when the theme switches by class [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Some chrome should not follow the theme: the prototype variant picker is a dark glass pill (`rgba(10, 10, 10, 0.82)` with a 12px blur) that works on light and dark pages alike, so it is deliberately not theme-aware [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- A theme switch can reveal the other theme with an animated clip-path, from `inset(0 0 100% 0)` to `inset(0 0 0 0)` over 1s with `cubic-bezier(0.77, 0, 0.175, 1)`. Duplicating the page to do it is hacky and fine only for a prototype; the View Transitions API gives the same effect without duplication [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).

## Where they agree and disagree

Between the sources:

- **Agree:** don't invert; spread dark neutrals further apart; make raised surfaces lighter [S-L19-039] [S-L19-051] [S-L19-052] [S-L19-067] [S-L19-070] [S-L19-085]. Accents get lighter or less saturated in dark [S-L19-039] [S-L19-052] [S-L19-070] [S-L19-085]. No source recommends pure black as the background [S-L19-052] [S-L19-057] [S-L19-070].
- **Borders:** brighten them [S-L19-039] [S-L19-051], against lowering a light card border that had too much contrast [S-L19-052]. Both can hold if borders are brighter than an inverted palette would give but not bright enough to overpower the card [inferred].
- **Text:** light gray with white saved for the key items [S-L19-051], against flipping text to white [S-L19-085]; [S-L19-039] says dim the text.
- **Cards:** a lighter fill [S-L19-052] [S-L19-070] [S-L19-085], against outlines as a personal preference [S-L19-047]; [S-L19-039] allows either.
- **How tinted the base is:** a hint of brand hue in a neutral [S-L19-051] or bluish black [S-L19-057], against strongly colored darks (deep purples, reds or greens [S-L19-052], the accent's own darkest shade [S-L19-070], a darkened two-color gradient [S-L19-082]).
- **Theme setting:** [S-L19-067] respects the system setting and also adds an in-app setting.

Against OpenDesigner's existing research:

- **Not an inversion agrees** with DC-L01-18 (Apple says dark colors aren't necessarily inversions; no major system ships a pure inversion) and DC-L10-17. Q-color-16's default (shared hue ramps with a mirrored mapping, separate dark neutral ramps, mapping by role) fits the "double the distance" rule of [S-L19-039], because the wider steps can live in the separate dark neutral ramp [inferred].
- **Lighter accents agree** with DC-L01-18 and DC-L01-19 (Material moves primary from tone 40 to 80; Atlassian's 700 in light is 400 in dark; accents one or two steps lighter and lower in chroma in dark), matching the 300 or 400 primary of [S-L19-039], the Tailwind 300 of [S-L19-070] and the lighter blue of [S-L19-085]. DC-L01-18 also records a counter-example: Radix keeps its solid step the same in both modes.
- **Hover in dark mode conflicts:** [S-L19-039] moves hover to a darker step (400 or 500 from a 300 or 400 main). DC-L01-17 records that Fluent makes dark-mode hover lighter (DC-L01-18 shows the same for Radix's hover step), and DC-L01-17's default steps toward more contrast with the surface, which on a dark surface means lighter [inferred].
- **Surface steps agree in size:** DC-L01-13 (dark layers separated by lighter tones) and DC-L04-13 (3 to 5% lightness steps in dark, inferred there from Atlassian's hex values) sit close to the 4 to 6% of [S-L19-039] and the 4 to 6 brightness steps of [S-L19-070], though each uses a different color model [inferred]. Q-color-14's `alternating` option (Carbon: alternating layers in light, stepping lighter in dark) is the closest match to "flexible light mode, strict dark mode" in [S-L19-039] [inferred].
- **Shadows:** DC-L04-12 keeps shadows in dark mode (double the alpha, add a 1px light edge ring on overlays), while the videos lean on lighter surfaces because shadows barely read in dark [S-L19-052] [S-L19-070]. The "just a border" option in [S-L19-039] is the closest to that edge ring [inferred].
- **Darkness mostly agrees:** Q-color-21's default `near-black` (a base between #121212 and #1a1a1a with a slight neutral tint, accents one or two steps lighter and lower in chroma) and DC-L01-19 (no system uses pure black by default; Primer's #0D1117 is blue-tinted) agree with the bluish blacks of [S-L19-057]. The strongly colored darks in [S-L19-052] [S-L19-070] [S-L19-082] go further than "slight", and Q-color-09 warns that strong tints can make status colors look off [inferred].
- **Text:** DC-L01-19 notes that very high contrast (white on pure black) can cause visual discomfort from halation, which fits the eye-strain reason [S-L19-051] gives for light gray text; Material 2 also desaturated its dark-mode primaries to pass 4.5:1 (DC-L01-19), like the dimmed chips of [S-L19-052].
- **Following the system mostly agrees:** Q-theme-01's default `system-light-dark` and DC-L10-17 match [S-L19-067], but DC-L10-17 advises against an app-only appearance setting on Apple platforms and allows an in-app override only on web, in addition to following the system; the macOS example in [S-L19-067] adds one anyway.
- **One mode only conflicts with a house standard:** `STD-visual-details-24` wants a light and a dark value for every color role, and its recorded conflict is that Q-theme-01 still offers `light-only` and `dark-only` (its default agrees).
- **Theme generation mostly agrees:** on pure grays, the +0.02 chroma shift of [S-L19-039] lands inside Q-color-09's hue-matched range (OKLCH chroma about 0.01 to 0.03 at mid steps), but on grays that are already hue-matched it reaches about 0.03 to 0.05, past the point where DC-L01-06 says grays read as visibly colored [inferred]. It fits Q-theme-03's `generator-ready` default (semantic tier, brand-color generator, contrast check) [inferred]. DC-L01-01 warns that equal OKLCH lightness does not guarantee WCAG contrast, so every themed variant still needs the pair check.
- **Accessibility modes are missing from the videos:** `STD-accessibility-motion-11` and `STD-accessibility-motion-12` require reduced-transparency and increased-contrast handling, and Q-color-24 defaults to a forced-colors-safe layer with high contrast as the first extra mode. No video covers these, and the conflict note on `STD-accessibility-motion-12` says the engine does not yet emit a `prefers-contrast: more` rule.
- **Toasts:** the conflict note on `STD-components-toasts-drawers-23` says OpenDesigner's engine describes `color.bg.inverse` as the inverted surface for tooltips and toasts, while Sonner's default is `invert: false`, so toasts follow the theme.
- **Theme-switch timing:** the reveal in [S-L19-010] runs 1s, while `STD-easing-duration-06` keeps UI motion under 300ms unless a reason is stated, so a 1s theme reveal needs a stated reason or a shorter duration [inferred].

## Decisions this informs

- **Q-theme-01** (which modes): follow the system [S-L19-067]; dark suits most modern sites but not all [S-L19-085]; `STD-visual-details-24` wants both modes defined.
- **Q-theme-03** and **Q-token-10** (theming and generator inputs): the OKLCH neutral shift in [S-L19-039] is a ready recipe for generating themed variants.
- **Q-color-16** (deriving dark from light): don't invert, double the neutral distance, lighter primary step [S-L19-039] [S-L19-051] [S-L19-067].
- **Q-color-21** (how dark): bluish or accent-tinted near-black; none of these sources recommends pure black [S-L19-052] [S-L19-057] [S-L19-070] [S-L19-082].
- **Q-color-14** and **Q-depth-01** (layers and card separation): lighter cards [S-L19-039] [S-L19-052] [S-L19-070] [S-L19-085], or outlines [S-L19-047].
- **Q-color-20** (hover and pressed): the dark-mode hover direction is disputed ([S-L19-039] against DC-L01-17).
- **Q-color-22** (text colors): light gray text with white for key items [S-L19-051].
- **Q-depth-04** (glass): frosted glass in dark mode [S-L19-085], with the `STD-accessibility-motion-11` fallback.
- **Q-color-24**, **Q-motion-10** and **Q-aud-04** (contrast and transparency settings): `STD-accessibility-motion-11` and `STD-accessibility-motion-12`.
- **Q-form-04** (where messages appear): if toasts are used, they follow the app theme (`STD-components-toasts-drawers-22`, [S-L19-022]).

## Visual examples worth showing

- A light palette reflected straight into dark, where the surfaces lose their distinction, beside one with the neutral steps doubled [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Inverted light mode against a designed dark mode for the same file manager: weak borders and all-light-purple text, then brighter borders and cards, light gray text, a pure white logo and storage figure, and a slightly desaturated logo [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- A dark card fix: a too-bright border lowered, the card lifted lighter than the background, a bright chip dimmed [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- A dark dashboard with several card layers, each slightly brighter and less saturated than the one below, and GitHub's very dark blue background [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- A dark-mode search bar defined only by a border [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- One design themed red, green and blue in light and dark mode through the OKLCH neutral shift [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A light site switched to dark: text to white, a saturated blue lightened, then frosted glass on the cards [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- A dark hero on a darkened baby-blue-to-pink gradient with light noise [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- A status bar that clashes because of a single `theme-color`, fixed with one tag per scheme [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- The clip-path theme-switch reveal [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Toasts in a dark app: light by default, matching once `theme="system"` is set [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- The dark glass variant picker sitting on a light page and on a dark page [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).

## Open questions

- In dark mode, should hover step darker [S-L19-039] or lighter (DC-L01-17)? No source tested it.
- Should dark-mode borders be brightened [S-L19-039] [S-L19-051] or softened [S-L19-052], and by how much?
- How strongly should the dark base be tinted? Q-color-21 says slightly; several videos go much further. At what chroma do status colors start to look off?
- Should Q-theme-01 keep `light-only` and `dark-only` options given `STD-visual-details-24`?
- Should macOS apps offer an in-app theme switch [S-L19-067], against DC-L10-17?
- Is a theme switch a justified long animation under `STD-easing-duration-06` (the reveal in [S-L19-010] runs 1s), and should it fall back to a cross-fade under reduced motion (`STD-accessibility-motion-02`) [inferred]?
- How far can gray text be dimmed in dark mode [S-L19-051] before it drops below 4.5:1? No source gives values.
- When will the engine emit `prefers-contrast: more` and reduced-transparency styles (the conflict note on `STD-accessibility-motion-12`)?
