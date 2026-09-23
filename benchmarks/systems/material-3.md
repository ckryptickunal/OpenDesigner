# Google Material Design 3 (incl. M3 Expressive)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Google, Material Design team (m3.material.io); code in AndroidX, material-components, material-foundation orgs | [S-L09-121] [S-L09-128] [S-L09-112] |
| Launch and major versions | M1 announced 2014-06-25; M2 2018; M3 / "Material You" May 2021; M3 Expressive launched 2025-05-13 (Android 16, Wear OS 6); I/O 2026 update (Expressive layout, spacing system) 2026-05-19 | [S-L09-136] (Tier C, history only) [S-L09-125] [S-L09-121] |
| Current version (Sept 2026) | Compose Material3 1.4.0 stable (2025-09-24), 1.5.0-alpha28 (2026-09-09); @material/web 2.5.0 (2026-07-15); MDC-Android 1.14.0 (2026-05-13, final line); Compose token schema v0_103, web tokens v0_192 | [S-L09-117] [S-L09-119] [S-L09-118] [S-L09-128] [S-L09-100] [S-L09-134] |
| Platforms | Android (Compose-first), Wear OS (Wear Compose Material 3), web, plus 2026 guidance for watches and immersive XR; Flutter also ships M3 [inferred, not checked this session] | [S-L09-119] [S-L09-121] [S-L09-127] |
| Open source + license | Yes. Apache-2.0 (androidx, material-web, material-color-utilities). Docs licence not checked | [S-L09-129] [S-L09-112] |
| Code frameworks | Jetpack Compose (primary; spacing tokens are Compose-only); Android Views MDC (maintenance mode since I/O 2026); Web Components MWC (maintenance mode "pending new maintainers") | [S-L09-122] [S-L09-128] [S-L09-129] |
| Figma kit | Official "Material 3 Design Kit" by @materialdesign on Figma Community, 56,661 likes, built to work with the Material Theme Builder plugin; Figma-variables status not confirmed | [S-L09-130] |
| Token tiers + naming | 3 tiers ref / sys / comp, dot grammar `md.<tier>.<group>.<name>`: `md.ref.typeface.brand` (Roboto), `md.sys.measurement.space100` (8dp), `md.sys.color.primary`; comp keys like filled-button `container-color`, `container-shape` | [S-L09-134] [S-L09-123] [S-L09-169] |
| Color model | HCT (CAM16 hue + chroma, L* tone). Tonal palettes tone 0-100; key stops 0,10,20,30,40,50,60,70,80,90,95,99,100 plus extra neutral tones (87, 90-98) for surfaces. 48 roles in Compose baseline; 53 in color-utilities (adds primaryDim/secondaryDim/tertiaryDim/errorDim). Accent: one seed color (or wallpaper) generates 5 palettes via 10 scheme variants; spec versions 2021/2025/2026 | [S-L09-116] [S-L09-108] [S-L09-104] [S-L09-115] [S-L09-112] [S-L09-114] |
| Typeface | Roboto for brand and plain roles (web tokens); Compose default maps both to FontFamily.SansSerif; Google Sans Flex open-sourced in 2025 (6 axes incl. roundedness), positioned by Google for expressive typography; no mono role in M3 tokens | [S-L09-134] [S-L09-110] [S-L09-132] [S-L09-133] |
| Type scale | 15 baseline styles (Display/Headline/Title/Body/Label x L/M/S) + 15 "Emphasized" twins in Expressive = 30. Body Large 16/24sp, Body Medium 14/20, Body Small 12/16, Display Large 57/64. Hand-tuned, weights 400/500 (700 for emphasized labels) | [S-L09-100] |
| Spacing | 8dp base, `space100 = 8dp`. Steps: 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72 dp (space0, space25, space50, space75, space100, space125, space150 confirmed; higher names follow the x100/8dp pattern [inferred]) | [S-L09-122] [S-L09-123] |
| Radius | none 0, extra-small 4, small 8, medium 12, large 16, large-increased 20, extra-large 28, extra-large-increased 32, extra-extra-large 48, full (circle). Buttons default to full (pill); square variants 12/16/28; press morphs to 12 | [S-L09-101] [S-L09-169] |
| Elevation | Two mechanisms: tonal surface-container color roles plus shadow elevation levels. Levels 0/1/3/6/8/12 dp. Light surface containers: lowest N100, low N96, container N94, high N92, highest N90; surface N98, dim N87 | [S-L09-103] [S-L09-104] |
| Motion | Durations short1-4 50/100/150/200, medium1-4 250/300/350/400, long1-4 450/500/550/600, extra-long1-4 700/800/900/1000 ms. Easing: emphasized (0.2,0,0,1), emph-decelerate (0.05,0.7,0.1,1), emph-accelerate (0.3,0,0.8,0.15), standard (0.2,0,0,1), std-decel (0,0,0,1), std-accel (0.3,0,1,1), legacy (0.4,0,0.2,1). Springs (damping ratio / stiffness): Standard scheme spatial fast 0.9/1400, default 0.9/700, slow 0.9/300; effects 1.0/3800, 1.0/1600, 1.0/800. Expressive scheme spatial fast 0.6/800, default 0.8/380, slow 0.8/200; effects same as Standard. Reduced-motion policy not verified | [S-L09-102] [S-L09-105] [S-L09-106] |
| Theming + modes | Light/dark; dynamic color from wallpaper or seed; contrast levels low -1.0, standard 0, medium 0.5, high 1.0; 10 scheme variants (TonalSpot, Neutral, Vibrant, Expressive, Fidelity, Content, Rainbow, FruitSalad, Monochrome, CMF); phone vs watch platform switch in 2025 spec; density via spacing tokens | [S-L09-167] [S-L09-112] [S-L09-113] [S-L09-122] |
| Component count | 36 component pages on m3.material.io (sitemap lastmod 2026-09-16, XR sub-pages excluded); Compose has 120 token files | [S-L09-124] [S-L09-107] |
| Component doc structure | Every component page has Overview, Specs, Guidelines, Accessibility tabs (36/36) | [S-L09-124] |
| Accessibility stance | Contrast is built into HCT: tone difference 40 guarantees >= 3:1, 50 guarantees >= 4.5:1; user-selectable contrast levels; state layers hover 0.08, focus/pressed 0.10 (Compose) or 0.12 (web), dragged 0.16. Explicit WCAG version target not verified | [S-L09-116] [S-L09-167] [S-L09-135] [S-L09-134] |
| Governance / contribution | Central Google team. 2026: "Material Android is Compose-first"; MDC-Android and MWC in maintenance mode; no public RFC process found | [S-L09-121] [S-L09-128] [S-L09-129] |
| Notable innovation | Algorithmic dynamic color (HCT + tonal palettes + contrast curves); motion as spring tokens (MotionScheme) instead of only bezier curves; shape morphing with a 35-shape library; Expressive backed by 46 studies with 18,000+ participants | [S-L09-116] [S-L09-105] [S-L09-168] [S-L09-126] |

## Visual signature: why it looks like this
- Tonal color everywhere (primary = tone 40, containers = tone 90, surfaces tinted neutrals N87-N100) -> soft, pastel, "same hue, different lightness" surfaces instead of gray cards [S-L09-104].
- Elevation expressed as five surface-container tones (N100 to N90) rather than stacked shadows -> flat, low-contrast layering with almost no drop shadow [S-L09-104] [S-L09-103].
- Large, varied radii (pill buttons, 28dp dialogs, up to 48dp, 35 morphable shapes) -> round, friendly, toy-like silhouettes [S-L09-101] [S-L09-168].
- Big type jumps (Display Large 57sp vs Body 16sp) and 500-weight titles/labels -> strong headline hierarchy on sparse screens [S-L09-100].
- Expressive springs with damping 0.6-0.8 on spatial moves -> visible overshoot and bounce; effects springs at damping 1.0 keep color/opacity changes clean [S-L09-106].
- Generous 8dp spacing grid and 40-56dp button heights -> roomy touch-first density [S-L09-123] [S-L09-169].

## Recent changes 2024-2026
- 2025-05-13: M3 Expressive announced for Android 16 and Wear OS 6, Pixel first later in 2025 [S-L09-125]. Backed by 46 studies, 18,000+ participants; key elements found up to 4x faster [S-L09-126].
- 2025: Google Sans Flex open-sourced on Google Fonts (6 variable axes) [S-L09-132]; public release covered 2025-11-18 [S-L09-133].
- 2025-09-24: Compose Material3 1.4.0 stable; material icons library dropped in favour of Material Symbols [S-L09-119].
- 2025-2026: color-utilities adds spec versions 2025 and 2026, Dim color roles and a phone/watch platform switch [S-L09-112] [S-L09-114] [S-L09-113].
- 2026-05-13: MDC-Android 1.14.0, last feature line before maintenance mode [S-L09-128].
- 2025-2026: Compose token set grows to 120 files, including Expressive-only components: button groups, connected button groups, split buttons (XS-XL), docked and floating toolbars, FAB menu, loading indicator, XS-XL buttons and icon buttons [S-L09-107].
- 2026-05-19 (Google I/O 2026): Expressive layout scaffold, new 8dp spacing system, watch and XR guidance, Expressive lists and menus, "Material Android is Compose-first"; Jetpack Compose Glimmer design system for display AI glasses mentioned [S-L09-121] [S-L09-127].
- 2026-05-19: Expressive search and search app bar shipped for Jetpack Compose [S-L09-121].
- 2026-07-15: @material/web 2.5.0, but the repo says MWC is in maintenance mode pending new maintainers [S-L09-118] [S-L09-129].
- 2026-09-09: Compose Material3 1.5.0-alpha28; Expressive list item APIs no longer experimental [S-L09-119].

## Builder takeaways
- Offer "seed color -> tonal palette -> semantic roles" as a preset, with a contrast slider (-1 to 1) and a scheme-variant picker. It is the most copied color engine in the field [S-L09-116] [S-L09-167].
- Model motion as named springs (damping + stiffness, spatial vs effects, fast/default/slow) with a "standard vs expressive" toggle, not just duration + bezier [S-L09-105] [S-L09-106].
- Ship a radius scale with "increased" in-between steps and optional shape morph on press; ask users whether they want pill or square buttons [S-L09-101] [S-L09-169].
- Warn users that web parity lags: web tokens lack the Expressive radii and spacing tokens are Compose-only [S-L09-134] [S-L09-122].

## Gaps / unverified
- Figma kit: whether the official kit uses Figma variables, and its last-update date (Figma page returned only metadata) [S-L09-130].
- Spacing token names above space150 are inferred from the pattern; values are confirmed. Browser was shared with other workers, so the full token table could not be re-read.
- M3 reduced-motion policy and an explicit WCAG version target were not found in the sources read.
- Flutter Material 3 status and docs licence were not checked.
- Material changes tied to Android releases after Android 16 (and to newer Wear OS versions) were not checked; no dated source found in this pass.
- Conflict: state-layer opacity for focus and pressed is 0.10 in Compose but 0.12 in material-web tokens [S-L09-135] [S-L09-134].
- Tracking values differ slightly between Compose (Display Large -0.2sp, Body Medium 0.2sp) and web (-0.25px, 0.25px) token builds [S-L09-100] [S-L09-134].
