# Airbnb Design Language System (DLS)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

The DLS is internal. Public information comes from three places. (1) Airbnb Design articles: airbnb.design now 302-redirects to airbnb.com (404), so these were read from Wayback copies [S-L09-476]. (2) Airbnb Newsroom release notes. (3) The CSS custom properties Airbnb ships on its live website, where DLS tokens appear as `--palette-*`, `--motion-*`, `--elevation-*`, `--typography-*` and `--dls-*` [S-L09-482]. Values from (3) are observed product code for the web client. Native iOS/Android values may differ.

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Airbnb design and engineering. Design Language Systems team; Karri Saarinen was Principal Designer and later Design Lead, DLS | [S-L09-477] [S-L09-478] |
| Launch and major versions | DLS built from 2015-16 and presented in "Building a Visual Language" (first archived 2016-05-26). Airbnb Cereal typeface launched May 2018 (first archived 2018-05-15). Product redesigns via Newsroom releases: 2021-2024, then the 2025 Summer Release (2025-05-13) "all-new app". No public version numbers | [S-L09-477] [S-L09-478] [S-L09-480] |
| Current version (Sept 2026) | Not public. Latest product release: Airbnb 2026 Summer Release, 2026-05-20 (new homepage) | [S-L09-480] |
| Platforms | iOS and Android first ("native platforms" was the initial scope), then web and tablet. 4 platforms were tested for the Cereal rollout | [S-L09-477] [S-L09-479] |
| Open source + license | DLS: no; proprietary. Related open source: Lottie (lottie-android and lottie-ios created 2016-10-06, active; lottie-ios pushed 2026-09-19), react-sketchapp (last commit 2021-03-30), Lona (last push 2023-01-04), Epoxy, Showkase, visx | [S-L09-483] |
| Code frameworks | Internal "technical view framework" for native. The web uses CSS custom properties (671 in the homepage HTML). Specific frameworks are not public | [S-L09-477] [S-L09-482] [inferred: web stack unnamed] |
| Figma kit | Not public. Historically a master Sketch library, versioned through git/GitHub PRs and shared via Box | [S-L09-477] |
| Token tiers + naming | Observed on web: palette primitives (`--palette-rausch600` #FF385C, `--palette-grey1000` #222222), semantic roles (`--palette-bg-primary`, `--palette-text-primary`, `--palette-border-secondary`, `--palette-icon-brand`), component tokens (`--dls-button_border-radius` 12px). Size and value are baked into names, e.g. `--corner-radius-medium12px`, `--typography-titles-semibold_22_26`. 353 palette tokens | [S-L09-482] |
| Color model | sRGB hex plus `color-mix()` alphas. Rausch ramp 100-1000 (600 = #FF385C brand, 700 #DA1249 for text and borders). Grey ramp grey0 #FFFFFF to grey1100 #000000 (1000 #222222 primary text, 400 #DDDDDD borders). Named brand colors: Rausch, Hof #222222, Foggy #6A6A6A, Arches #C13515 (error). Sub-brand gradients: Plus #BD1E59 to #861453, Luxe #59086E to #440589 | [S-L09-482] |
| Typeface | Airbnb Cereal, custom, by Dalton Maag, 2018. Now served as a variable font, `Airbnb Cereal VF`, with Arabic, Cyrillic, Devanagari, Greek, Hebrew, Thai and Italic cuts. Fallbacks: 'Circular' (the previous typeface), -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue | [S-L09-478] [S-L09-479] [S-L09-482] |
| Type scale | Names encode size and line height, e.g. `titles-semibold_22_26`, `body-text_14_18`, `special-display-medium_72_74`. Web sizes: 10, 11, 12, 14, 16, 18, 22, 26, 32, 40, 48, 60, 72 px. Weights: Book 400, Medium 500, Semibold 600. Negative tracking on large titles (-0.0275rem at 22px, -0.06rem at 32px, -0.18rem at 72px). Base body probably 16/22 or 14/20 [inferred]. In 2018 the style `TextTitle3` = size 24, leading 32 | [S-L09-482] [S-L09-479] |
| Spacing | Two named scales. Micro: 2, 4, 8, 12, 16, 24, 32 px. Macro: 16, 24, 32, 40, 48, 64, 80 px. 8px-based with 2/4/12 fillers | [S-L09-482] |
| Radius | corner-radius tiny 4, small 8, medium 12, large 16, xlarge 20, xxlarge 24/28, xxxlarge 32 px. Button 12px; cards and media 20px; icon buttons 50% | [S-L09-482] |
| Elevation | Shadows plus a 1px hairline ring. elevation0 = inset 1px #DDDDDD. elevation1-5 = 1px black-2% ring plus a drop shadow (e.g. elevation1 `0 2px 4px` black 16%; elevation3 `0 8px 24px` black 10%). Named shadows: tertiary `0 2px 4px` .18, secondary `0 6px 16px` .12, primary `0 6px 20px` .2, high `0 8px 28px` .28. Also translucent "materials": extra-thin rgba(218,218,218,.40) to extra-thick rgba(255,255,255,.925) | [S-L09-482] |
| Motion | Curves: standard (0.2,0,0,1), enter (0.1,0.9,0.2,1), exit (0.4,0,1,1), linear. 6 springs with source physics and CSS `linear()` easing: fast (stiffness 300, damping 35, about 452ms), fast-bounce (250/22, about 449ms), standard (175/26, about 584ms), medium-bounce (175/18.5, about 574ms), slow (100/20, about 746ms), slow-bounce (100/14, about 762ms), all mass 1. The homepage HTML has 3 `prefers-reduced-motion` rules. Principle from 2016: "Conversational", motion as communication | [S-L09-482] [S-L09-477] |
| Theming + modes | Web: light only (0 `prefers-color-scheme` rules). Sub-brand themes via Plus and Luxe palettes and gradients. RTL gradient variants. Native dark mode not verified | [S-L09-482] |
| Component count | Not public. 2016 organization: Navigation, Marquees, Content, Image, Speciality. Nearly 50 screens prototyped in a day from the library | [S-L09-477] |
| Component doc structure | Not public | |
| Accessibility stance | 2016 principle "Universal: welcoming and accessible". Cereal tuned for legibility (larger x-height, open apertures, balanced Book weight). No public WCAG target for the DLS | [S-L09-477] [S-L09-478] |
| Governance / contribution | Central DLS team. Components defined with required and optional elements in both Sketch and code. Changes via PRs with changelog and PNG exports (2016). Current process not public | [S-L09-477] |
| Notable innovation | Components as a "living organism" instead of atomic design. Cross-platform tooling that shaped the industry: Lottie (After Effects to native animation), react-sketchapp (React to Sketch), Lona (design-system definitions to code). Springs shipped as tokens with physics source values and precomputed CSS `linear()` curves | [S-L09-477] [S-L09-483] [S-L09-482] |

## Visual signature: why it looks like this
- Rausch #FF385C used sparingly (logo, primary CTA gradient #E61E4D to #D70466), with near-black #222222 text on white -> a warm, friendly brand accent on a clean, photo-first canvas [S-L09-482].
- Cereal VF at 400/500/600 with tight negative tracking on big titles -> rounded, approachable, editorial headings [S-L09-482] [S-L09-478].
- Generous radii (12px buttons, 20px cards and media, 32px max) -> soft, tactile surfaces that frame listing photos [S-L09-482].
- A hairline ring plus a soft drop shadow (elevation1-5), and translucent materials -> cards lift gently. Floating bars read like iOS glass [S-L09-482].
- Spring tokens (stiffness 100-300) with bounce variants -> physical, playful transitions in the 2025 app [S-L09-482] [inferred: link to 2025 redesign].
- 8px-based spacing with an 80px macro step -> roomy, magazine-like page rhythm [S-L09-482].

## Recent changes 2024-2026
- 2024-05-01 and 2024-10-16: Summer and Winter releases (product features) [S-L09-480].
- 2025-05-13: 2025 Summer Release, "Introducing Airbnb Services and Airbnb Experiences in an all-new app". Redesigned Explore homepage, Trips itinerary, Messages and Profile [S-L09-480].
- 2025-10-21: 2025 Winter Release (social features for Experiences) [S-L09-480].
- 2026-05-20: 2026 Summer Release, "the new homepage" [S-L09-480].
- By 2026-09: airbnb.design is retired (redirects to airbnb.com). Web tokens now include springs, materials and a variable Cereal font [S-L09-476] [S-L09-482].

## Builder takeaways
- Offer spring tokens with both physics inputs (stiffness, damping, mass) and a generated CSS `linear()` easing plus duration. Airbnb ships all three per spring [S-L09-482].
- Offer a "materials" tier (translucent backgrounds, thin to extra-thick) next to elevation for glassy nav bars [S-L09-482].
- Consider value-in-name typography tokens (`semibold_22_26`). They are self-documenting for handoff, but renaming is costly when values change. Ask users which they prefer [S-L09-482].
- Ask whether the product is photo-led. Airbnb's large radii and quiet neutrals exist to frame imagery.

## Gaps / unverified
- The DLS documentation, component inventory, native tokens and governance are not public.
- Web token values were read from the live homepage HTML (Indian locale redirect, airbnb.co.in), not from documentation. Native apps may differ.
- The 2025 redesign's design language (reported 3D icons, animation format) is not described in Airbnb's own release notes. Medium (Airbnb Tech Blog) blocked access (403) and WebSearch quota was exhausted, so it stays unverified.
- The Cereal launch date comes from the first Wayback capture (2018-05-15). The brief assumed 2019; the evidence says 2018.
