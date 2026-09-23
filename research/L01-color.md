# L01: Color

Lane: L01 (Color). Author: orchestrator subagent L01. Written 2026-09-23. Status: complete (27 Decision Cards).
Trace: `traces/L01-trace.md` (every source, including rejected ones). Schema: `_coordination/SCHEMA.md`.

## Lane overview

Color is the foundation with the most interlocking decisions in a design system. For the builder, it splits into four layers that must be decided in order:

1. **Raw material (primitives).** Which color space the ramps are built in, how many steps each ramp has, what a step number means, which hues exist, how tinted the neutrals are, and which gamut is targeted. These decisions are almost invisible to end users but set the ceiling on everything else.
2. **Meaning (semantic roles).** Which roles exist (surface, text, border, brand, status, inverse), how many emphasis levels each role has, and how foreground/background pairs are guaranteed to contrast.
3. **Behavior (states and modes).** How hover, pressed, focus, selected and disabled change color; how light, dark, dimmed, high-contrast, colorblind and forced-colors modes remap roles; whether color is static or personalized (Material You, macOS accent, iOS tinted icons, Liquid Glass).
4. **Encoding (tokens).** How the above is written as tokens (DTCG 2025.10 color objects, three tiers, mode handling via the DTCG Resolver or Figma modes).

Five findings shape the builder more than any others:

- **What a step number means is a real decision, and systems disagree.** In Tailwind, the same step number has a different lightness per hue (blue-500 is L 62.3%, amber-500 is L 76.9%) [S-L01-062]. In Spectrum, each step index has the same contrast against the background across all hues (every 700 is 3.01:1, every 900 is about 5.07:1) [S-L01-035]. In Material, the step is the HCT tone, a perceptual lightness value where tone 0 is black and tone 100 is white [S-L01-006]. Radix gives each of its 12 steps a job (1-2 backgrounds, 3-5 component fills, 6-8 borders, 9-10 solids, 11-12 text) [S-L01-002]. Contrast-indexed or tone-indexed steps let the builder guarantee contrast from step distance alone. Carbon and Stripe publish step-distance rules of this kind [S-L01-029, S-L01-044].
- **Semantic role taxonomies converge on the same grammar:** property (bg/fg/border) x role (neutral, brand, success, ...) x emphasis (subtle to bold) x state (hover, pressed). Primer, Atlassian, Carbon, Fluent and Polaris all follow a variant of it [S-L01-027, S-L01-032, S-L01-029, S-L01-034, S-L01-039]. Material 3 is the outlier. It uses paired container/on-container roles rather than a property axis [S-L01-004].
- **Dark mode is a separate mapping, not an inversion.** Apple says so outright [S-L01-014]. Atlassian mirrors its ramp (700 in light maps to 400 in dark) [S-L01-031]. Material reassigns tones (primary 40 becomes 80) [S-L01-010]. Carbon lightens one step per layer in dark themes [S-L01-029]. Nobody uses pure black as the default dark surface. Values range from Material 2025's tone 4 to #121212, #161616, #0D1117 and #292929 [S-L01-010, S-L01-055, S-L01-029, S-L01-050, S-L01-034].
- **Standards status (verified today):** DTCG 2025.10 is stable and requires a structured color object ({colorSpace, components, alpha, hex}), not a hex string [S-L01-018]. WCAG 3 is still a Working Draft (10 Sep 2026) and its contrast method is "to be determined", with APCA not named [S-L01-021]. So WCAG 2.2 ratios remain the only enforceable target. APCA is a useful secondary check that Radix already uses [S-L01-002].
- **Personalized color is now mainstream on both mobile platforms.** Material dynamic color has scheme variants and a 2025 spec that raises chroma [S-L01-010, S-L01-011]. Apple's Liquid Glass "has no inherent color" and takes color from content, and icons have default, dark, clear and tinted appearances [S-L01-013, S-L01-015]. A builder has to decide whether brand color is fixed or can yield to the user.

## Decision Cards

### DC-L01-01: Color space used to build ramps
- **Block path:** Foundations > Color > Palette generation > Color space
- **Questions the designer answers:** Do I want steps that look evenly spaced across every hue? Do I need contrast to be predictable from the step number? Am I targeting web only, or Android/Material too?
- **Options:**
  - **HSL/HSV (sRGB).** The legacy default. Stripe dropped it because "at the same level of mathematical lightness, yellow appears lighter than blue" [S-L01-044]. Material warns that HSL lightness does not match HCT tone [S-L01-006].
  - **CIELAB / LCH.** Stripe's 2019 system used Lab to make hues equally bright [S-L01-044]. DTCG supports `lab` and `lch` [S-L01-018].
  - **OKLab / OKLCH.** Tailwind v4 moved its whole palette from rgb to oklch in Jan 2025 [S-L01-045]. The current Tailwind 4.3.3 values are OKLCH, e.g. `--color-blue-500: oklch(62.3% 0.214 259.815)` [S-L01-062]. CSS `oklch()` has been Baseline widely available since May 2023 [S-L01-046].
  - **HCT (hue, chroma, tone; CAM16 hue/chroma plus L* tone).** Material 3 and Material Color Utilities (MCU) use it [S-L01-008]. Tone runs 0-100 and "determines contrast", and chroma tops out near 120 [S-L01-006].
  - **Contrast-targeted generation (CAM02/LCH/OKLCH interpolation with target contrast ratios).** Used by Adobe Leonardo [S-L01-040] and by Spectrum, whose colors follow "a perceptually linear progression of lightness" converted into target contrast ratios [S-L01-036].
- **Visual effect:** Perceptual spaces (OKLCH, Lab, HCT) make, say, blue-600 and green-600 look equally heavy. The palette reads as calm and balanced, and color swaps do not change hierarchy. HSL ramps look uneven: yellows and cyans wash out while blues and purples go muddy or dark [S-L01-044] [inferred for the "calm" reading]. OKLCH also exposes more vivid P3 colors [S-L01-045].
- **Depends on (upstream):** target platforms (Material/Android favors HCT through MCU); gamut target (DC-L01-05); tooling choice (DC-L01-04).
- **Affects (downstream):** every primitive ramp; how state shifts are computed (DC-L01-17); dark-mode mapping (DC-L01-18); whether contrast can be derived from step distance (DC-L01-22).
- **Token encoding:** DTCG `$type: "color"` with `colorSpace` set to `"oklch"`, `"lab"`, `"srgb"`, etc. [S-L01-018]. The builder's internal space is separate from the storage space: primitives can be authored in OKLCH and stored with a `hex` fallback.
- **Platform notes:** Web accepts `oklch()`, `lab()` and `color(display-p3 ...)` natively [S-L01-046, S-L01-049]. Android/Material tooling expects HCT through MCU (C++, Dart, Java, Kotlin, Swift, TypeScript) [S-L01-008]. iOS asset catalogs take sRGB or Display P3 components [S-L01-013].
- **Accessibility constraints:** WCAG 2.x contrast uses relative luminance, `(L1+0.05)/(L2+0.05)`, not OKLCH L [S-L01-022]. Equal OKLCH L therefore does not guarantee an equal WCAG ratio. Always check the ratio after generation [inferred].
- **Default + heuristic:** Default to OKLCH for web-first systems and HCT when the system must also feed Material dynamic color. Rule of thumb: if you need guaranteed contrast by step number, generate with contrast targets (the Leonardo/Spectrum approach) rather than equal lightness.
- **Evidence:** [S-L01-006, S-L01-008, S-L01-018, S-L01-022, S-L01-036, S-L01-040, S-L01-044, S-L01-045, S-L01-046, S-L01-062]

### DC-L01-02: Ramp step count and naming convention
- **Block path:** Foundations > Color > Palette generation > Ramp scale
- **Questions the designer answers:** How many shades does each color need? What do we call them? Should names leave room to insert steps later?
- **Options (real systems):**
  - **Tailwind:** 11 steps, 50, 100-900, 950 [S-L01-001].
  - **Radix:** 12 steps, 1-12, each with a defined job [S-L01-002].
  - **Material 3:** tonal palette tones 0-100 in increments of 10, plus 95, 98 and 99 ("some palettes include more values") [S-L01-006]. The 2021 surface roles also use tones 4, 6, 12, 17, 22, 24, 87, 92, 94 and 96 [S-L01-010].
  - **Carbon:** 10 grades per hue (10-100) plus Black and White, 12 grades in all, with hover "half steps" held outside the core palette [S-L01-029].
  - **Spectrum (v6 colors):** gray 50, 75, 100, 200-900 (11 grays) and hues 100-1300. The docs say "14 tints and shades per color" [S-L01-035, S-L01-036].
  - **Atlassian:** hues 100, 200, 250, 300, 400, 500, 600, 700, 800, 850, 900, 1000. Light neutrals run Neutral0-Neutral1200 and dark neutrals DarkNeutral-100 to DarkNeutral1200. Both have alpha variants (e.g. Neutral100A) [S-L01-031].
  - **Primer:** base hues 0-9 (e.g. `blue.5`) and neutrals 0-13 [S-L01-027, S-L01-050].
  - **Fluent 2:** brand ramp of 16 steps, 10-160, with 10 the darkest (brandWeb 80 = #0f6cbd) [S-L01-034].
  - **Polaris (legacy React tokens):** 16-step scale, 1-16 with 1 the lightest [S-L01-039].
- **Visual effect:** More steps give finer control over subtle surfaces and hover shifts and allow quieter, more layered UIs. Fewer steps force bolder jumps and a flatter, more graphic look [inferred]. The naming convention has no visual effect but decides whether new steps can be inserted. Atlassian's 250 and 850 are later insertions between existing steps [S-L01-031].
- **Depends on (upstream):** color space (DC-L01-01); whether steps carry a fixed purpose (DC-L01-03); dark-mode strategy (mirrored ramps need an even, symmetric count, DC-L01-18).
- **Affects (downstream):** primitive token names; semantic mapping tables; state-shift rules (e.g. Carbon's active state is "two full steps" [S-L01-029]).
- **Token encoding:** primitives such as `color.blue.500` (Tailwind-like), `blue.9` (Radix-like) or `blue.40` (tone-like); DTCG groups by hue, e.g. `{ "color": { "blue": { "500": { "$type": "color", "$value": {...} } } } }` [S-L01-018].
- **Platform notes:** Material's tone numbering is baked into MCU and Android dynamic color, so if you target it, keep tone names available as aliases [S-L01-008, S-L01-058]. Apple exposes no public numbered ramps. System colors are semantic and "may fluctuate from release to release" [S-L01-013].
- **Accessibility constraints:** none directly. Step count limits how many contrast-distinct pairs exist.
- **Default + heuristic:** Default to 11-12 steps for hues and 12-13 for neutrals. Use 100-based numbering (50-950 or 100-1000) if you expect to insert steps later, and 1-12 if every step has a fixed job. Heuristic: one step per distinct UI job plus two hover/pressed shifts.
- **Evidence:** [S-L01-001, S-L01-002, S-L01-006, S-L01-010, S-L01-027, S-L01-029, S-L01-031, S-L01-034, S-L01-035, S-L01-036, S-L01-039, S-L01-050]

### DC-L01-03: What a step means (ramp construction rule)
- **Block path:** Foundations > Color > Palette generation > Step semantics
- **Questions the designer answers:** Should "600" mean the same lightness in every hue, the same contrast, or just "looks right"? Should each step have a fixed job (background, border, text)? How does chroma behave along the ramp?
- **Options:**
  - **Hand-tuned per hue (visual equivalence).** Tailwind: at step 500, blue is L 62.3%, red 63.7%, green 72.3% and amber 76.9% [S-L01-062]. Designers tune by eye.
  - **Equal perceptual lightness per step (tone-indexed).** Material tonal palettes: the same tone gives the same perceived brightness across hues, and tone difference drives contrast (tones 50 vs 98 give 3:1, tones 30 vs 98 give 7:1) [S-L01-006].
  - **Equal contrast per step (contrast-indexed).** Spectrum v6: each index has the same contrast against gray-100 across hues (every 700 is 3.01:1, every 900 about 5.07-5.09:1, every 1000 about 6.7:1) [S-L01-035]. Grays are generated from target contrast ratios on a polynomial curve, and dark themes target higher ratios [S-L01-036]. Leonardo generates any ramp this way [S-L01-040].
  - **Purpose-indexed steps.** Radix: 1-2 app and subtle backgrounds; 3, 4, 5 component background (normal, hover, pressed/selected); 6, 7, 8 borders (subtle, interactive, strong/focus); 9 solid (highest chroma), 10 solid hover; 11 low-contrast text and 12 high-contrast text, guaranteed APCA Lc 60 and Lc 90 on step 2 [S-L01-002]. Primer neutrals: 0-5 backgrounds, 7-8 borders, 9-10 text [S-L01-027]. Spectrum grays: 50-200 backgrounds, 200-300 decorative borders, 400 field borders, 600 control borders, 700-900 text, 500 disabled text [S-L01-036].
  - **Chroma curve.** In HCT, maximum chroma depends on hue and tone, so chroma drops at extreme tones ("bright light blue ... not quite possible") [S-L01-006]. Radix puts peak chroma at step 9 [S-L01-002]. ColorBox models hue, saturation and luminosity as separate eased curves (22 easing functions) [S-L01-043].
- **Visual effect:** Contrast- or tone-indexed ramps make swapping the accent (blue to green) keep the same visual weight and legibility, so the system feels even and engineered. Hand-tuned ramps allow more character (warmer yellows, richer mid-greens) but a hue swap can make buttons suddenly lighter or darker [inferred]. Purpose-indexed ramps make UIs look consistent because borders are always one of three steps [inferred].
- **Depends on (upstream):** color space (DC-L01-01); contrast target (DC-L01-22).
- **Affects (downstream):** semantic mapping (roles point to fixed steps); interaction state shifts (DC-L01-17); dark mapping (DC-L01-18); data-viz sequential palettes (DC-L01-24).
- **Token encoding:** step purpose can be recorded in `$description` or `$extensions` per primitive [inferred]. Semantic tokens then alias steps, e.g. `color.border.interactive` = `{color.blue.7}`.
- **Platform notes:** platform-neutral.
- **Accessibility constraints:** contrast-indexed ramps let the builder publish step-distance guarantees. Carbon: from grade 100, 50 through White meets 4.5:1 and 60 through White meets 3:1 [S-L01-029]. Stripe: 5 levels apart meets 4.5:1 and 4 levels apart meets 3:1 [S-L01-044].
- **Default + heuristic:** Default to tone- or contrast-indexed steps with purpose bands documented. Heuristic: if the builder lets users recolor the accent, use contrast-indexing so every accent passes the same pairings.
- **Evidence:** [S-L01-002, S-L01-006, S-L01-027, S-L01-029, S-L01-035, S-L01-036, S-L01-040, S-L01-043, S-L01-044, S-L01-062]

### DC-L01-04: Palette generation tool and source of truth
- **Block path:** Foundations > Color > Palette generation > Tooling
- **Questions the designer answers:** Do I start from a preset palette or from my brand color? Do I need Material/Android compatibility? Do I need contrast guarantees out of the box?
- **Options:**
  - **Adopt a preset palette:** Tailwind default (26 families, 11 steps, OKLCH) [S-L01-001]; Radix Colors (light, dark, alpha and P3 variants, "not intended to be customised") [S-L01-052, S-L01-053].
  - **Material Theme Builder / Material Color Utilities:** one source color becomes 5 key colors (primary, secondary, tertiary, neutral, neutral variant), then tonal palettes, then 26 roles, in light and dark and at three contrast levels [S-L01-006]. Brand inputs can be given per key color, with "color fidelity" to match the input tone [S-L01-057]. MCU scheme variants: Monochrome, Neutral, Tonal Spot, Vibrant, Expressive, Fidelity, Content, Rainbow, Fruit Salad and CMF, with spec versions 2021 (default), 2025 and 2026 [S-L01-010].
  - **Adobe Leonardo:** key colors plus background plus target ratios. Available as a web app, as `@adobe/leonardo-contrast-colors` 1.1.0 (Feb 2026) and as `@adobe/leonardo-mcp` 0.1.0 (Feb 2026) for agent use [S-L01-040].
  - **Huetone:** LCH/APCA grid editor for "accessible color systems with predictable contrast ratios". Last pushed Nov 2023 [S-L01-042].
  - **Lyft ColorBox:** eased hue/saturation/luminosity curves. Last pushed Oct 2023; historical [S-L01-043].
  - **Hand-built in a perceptual editor** following Stripe's 2019 method [S-L01-044].
- **Visual effect:** Presets give a recognizable "stock" look: Tailwind's vivid OKLCH hues, Radix's soft, even steps. Generators give a brand-specific look. MCU output feels "Material": tinted neutrals and harmonized secondary/tertiary colors [inferred from S-L01-010 palette recipes].
- **Depends on (upstream):** brand color availability (DC-L01-09); platform (Material/Android); contrast target.
- **Affects (downstream):** all primitives; whether the builder must store generator parameters (seed, variant, contrast) as tokens.
- **Token encoding:** store the generator inputs as source tokens (e.g. `color.seed`, `$extensions.generator = {tool, variant, contrastLevel}`) and the generated ramps as primitives [inferred].
- **Platform notes:** MCU is cross-platform [S-L01-008]; Leonardo is JS [S-L01-040].
- **Accessibility constraints:** Leonardo and Spectrum-style generation encode WCAG ratios directly [S-L01-040]. Radix guarantees APCA Lc for its text steps [S-L01-002].
- **Default + heuristic:** For the builder, offer three generator modes: preset, seed-based (MCU-like) and contrast-targeted (Leonardo-like). Heuristic: pick MCU if Android dynamic color matters, Leonardo if contrast guarantees across many themes matter, and a preset if speed matters.
- **Evidence:** [S-L01-001, S-L01-002, S-L01-006, S-L01-008, S-L01-010, S-L01-040, S-L01-042, S-L01-043, S-L01-044, S-L01-052, S-L01-053, S-L01-057]

### DC-L01-05: Gamut target and color syntax (sRGB vs Display P3)
- **Block path:** Foundations > Color > Color spaces and gamut
- **Questions the designer answers:** Should colors look more vivid on modern screens? Do we need identical color on every screen? How do we ship fallbacks?
- **Options:**
  - **sRGB only (hex).** Accurate "on most displays" [S-L01-013]. The simplest pipeline.
  - **P3 as progressive enhancement.** Radix ships each scale twice: hex, then `color(display-p3 ...)` inside `@supports (color: color(display-p3 1 1 1))` and `@media (color-gamut: p3)` [S-L01-052]. MDN documents `color-gamut: srgb | p3 | rec2020`, widely available since Feb 2023 [S-L01-049].
  - **OKLCH values that may exceed sRGB.** Tailwind v4 uses the wider gamut "to make the colors more vivid" [S-L01-045]. Browsers gamut-map out-of-range oklch automatically [S-L01-046].
  - **Native P3 assets on Apple platforms.** Display P3 at 16 bits per channel, PNG. Supply separate sRGB/P3 variants when similar P3 colors blur together or P3 gradients clip on sRGB [S-L01-013].
- **Real-world check:** Tailwind v4 blue-500 (oklch 62.3% 0.214 259.815) is already slightly outside sRGB. Its linear blue channel is about 1.05, so on sRGB screens it is gamut-mapped (clipped hex approx #2b7fff) [S-L01-062, S-L01-069]. Any OKLCH palette with high chroma needs a defined gamut-mapping and fallback policy.
- **Visual effect:** P3 gives richer, more saturated accents, especially reds, greens and oranges. Brand and status colors feel more luminous on Apple and modern laptop and phone screens. sRGB-only looks slightly flatter on those devices but is identical everywhere [S-L01-013] [inferred for per-hue emphasis].
- **Depends on (upstream):** color space (DC-L01-01); brand guidelines (is exact brand match required?).
- **Affects (downstream):** token value format, the export pipeline, and gradient rendering (DC-L01-25).
- **Token encoding:** DTCG 2025.10 supports `"display-p3"`, `"rec2020"`, `"oklch"` etc., with an optional `hex` fallback: `{"colorSpace":"display-p3","components":[0.247,0.556,0.969],"hex":"#0090ff"}` [S-L01-018] (values from Radix blue-9 [S-L01-052]).
- **Platform notes:** Web: `color(display-p3 ...)`, `oklch()`, plus `@media (color-gamut)` [S-L01-049]. iOS/macOS: asset catalogs per color space [S-L01-013]. Android: support for wide-gamut UI colors was not verified in this lane (gap).
- **Accessibility constraints:** check contrast on both the P3 and sRGB fallback values, since gamut mapping can shift luminance [inferred].
- **Default + heuristic:** Default to sRGB hex primitives with optional P3 overrides for accents only. Heuristic: use P3 where saturation carries brand or status meaning; keep neutrals sRGB, since P3 adds nothing to near-grays [inferred].
- **Evidence:** [S-L01-013, S-L01-018, S-L01-045, S-L01-046, S-L01-049, S-L01-052, S-L01-062, S-L01-069]

### DC-L01-06: Neutral temperature (pure vs tinted gray, warm vs cool)
- **Block path:** Foundations > Color > Neutrals > Temperature
- **Questions the designer answers:** Should grays be truly neutral, or carry a hint of the brand hue? Warm (paper, earthy) or cool (tech, crisp)? Is color-critical content (photos, editing) shown in the product?
- **Options (with real values):**
  - **Pure neutral (zero chroma).** Tailwind `neutral` (oklch 55.6% 0 none at 500) [S-L01-062]. Radix `gray` ("pure gray") [S-L01-053]. Spectrum grays are "fully desaturated" to avoid misread colors "due to chromatic adaptation or simultaneous contrast" in image workflows [S-L01-036]. Fluent's neutral backgrounds are pure grays (#ffffff, #f5f5f5, #292929) [S-L01-034]. Polaris gray is neutral (rgba 250,250,250 ...) [S-L01-039].
  - **Cool tint (blue/cyan/violet).** Tailwind `slate` (chroma 0.046, hue 257), `gray` (0.027, hue 264), `zinc` (0.016, hue 286), `mist` (0.021, hue 213.5) [S-L01-062]. Radix `slate` [S-L01-053]. Primer light neutral1 #F6F8FA and dark #0D1117 are blue-tinted [S-L01-050].
  - **Warm tint (yellow/brown/olive).** Tailwind `stone` (0.013, hue 58), `taupe` (0.021, hue 43), `olive` (0.031, hue 107) [S-L01-062]. Radix `sand` and `olive` [S-L01-053].
  - **Hue-matched tint (neutral derived from brand hue).** Radix pairs grays to accents: mauve with tomato/red/ruby/crimson/pink/plum/purple/violet, slate with iris/indigo/blue/sky/cyan, sage with mint/teal/jade/green, olive with grass/lime, sand with yellow/amber/orange/brown. Pure gray gives "a neutral vibe"; natural pairing gives "a more colorful and harmonius vibe" (sic) [S-L01-053]. Material generates neutral and neutral-variant palettes from the source hue. TonalSpot 2021 uses chroma 6 (neutral) and 8 (neutral variant); the 2025 spec uses 5 and 8.5 on phone [S-L01-010].
- **Visual effect:** Pure gray reads as neutral, technical and "tool-like" and never competes with content color. It suits editors, photo and data apps [S-L01-036]. Cool tints read as crisp, digital and trustworthy (a SaaS/developer feel). Warm tints read as friendly, organic and editorial. Hue-matched tints make the whole UI feel "of one piece" with the brand, even in the gray areas [inferred for the personality readings; the Radix pairing rationale is harmony [S-L01-053]]. Chroma above about 0.03 OKLCH becomes visibly colored (e.g. Tailwind slate at 0.046) [inferred from S-L01-062].
- **Depends on (upstream):** brand hue (DC-L01-09); product type (content-critical apps favor pure gray); overall chroma level (DC-L01-10).
- **Affects (downstream):** every surface, border and text token; perceived temperature of dark mode (tinted darks such as #0D1117 read "blue-black") [S-L01-050]; data-viz neutrals.
- **Token encoding:** primitives `color.neutral.{step}` or `color.slate.{step}`. Semantic tokens should reference a neutral alias (`color.gray.*` -> `color.slate.*`) so the tint can be swapped in one place [inferred].
- **Platform notes:** Apple system grays (systemGray-systemGray6) are defined per appearance and should not be hard-coded [S-L01-013].
- **Accessibility constraints:** a tint shifts luminance only slightly, but check text steps after tinting. Neutral tint must not be the only carrier of meaning [S-L01-024].
- **Default + heuristic:** Default to a slight hue-matched tint (OKLCH chroma of about 0.01-0.03 at mid steps) for branded products, and pure gray for image/data-critical tools. Heuristic: tint neutrals toward the accent hue; keep chroma lowest at the extremes [inferred from S-L01-062 values, where 50/950 steps have chroma 0-0.008].
- **Evidence:** [S-L01-010, S-L01-013, S-L01-024, S-L01-034, S-L01-036, S-L01-039, S-L01-050, S-L01-053, S-L01-062]

### DC-L01-07: Neutral ramp resolution, usage bands and alpha neutrals
- **Block path:** Foundations > Color > Neutrals > Ramp and usage
- **Questions the designer answers:** How many grays? Which gray is for backgrounds, borders, text? Do we need translucent grays for overlays on imagery?
- **Options:**
  - **Solid neutrals with fixed bands.** Primer 0-13 (0-5 backgrounds, 7-8 borders, 9-10 text) [S-L01-027]. Spectrum 11 grays (50-200 background layers, 200-300 decorative borders, 400 field border, 600 control border, 700-900 text, 500 disabled text) [S-L01-036]. Carbon light UI uses White to Gray 20 for enabled fills and Gray 100 to Gray 60 for text; dark uses Gray 100 to Gray 70 fills and White to Gray 50 text [S-L01-029].
  - **Separate light and dark neutral ramps.** Atlassian Neutral0-1200 plus DarkNeutral-100 to DarkNeutral1200, with Neutral100 mapping to DarkNeutral100 [S-L01-031]. Primer light and dark neutral scales run in opposite directions [S-L01-027].
  - **Alpha (translucent) neutrals.** Atlassian Neutral100A-500A and DarkNeutral-100A-500A [S-L01-031]. Radix blackA/whiteA and per-hue alpha scales (e.g. `--blue-a1: #0080ff04`) [S-L01-052]. Spectrum's 8 transparent white/black values, white on backgrounds darker than 50% lightness and black above [S-L01-036]. (See DC-L01-27.)
- **Visual effect:** More near-white steps allow subtle zoning of cards, sidebars and wells without borders, giving a soft, layered look (Carbon: "subtle shifts in value to organize content into distinct zones" [S-L01-029]). Fewer steps push toward border-defined, flatter layouts [inferred]. Alpha neutrals keep hover and borders consistent over colored or image backgrounds [S-L01-031].
- **Depends on (upstream):** neutral temperature (DC-L01-06); step semantics (DC-L01-03); surface model (DC-L01-13).
- **Affects (downstream):** surface, border, divider, text-secondary/tertiary and disabled tokens; skeleton and blanket (scrim) colors (Atlassian `color.skeleton`, `color.blanket`) [S-L01-032].
- **Token encoding:** `color.neutral.0..13` primitives and `color.neutral.100A` alpha primitives. DTCG `alpha` component: `{"colorSpace":"srgb","components":[0,0.5,1],"alpha":0.016}` [S-L01-018].
- **Platform notes:** Apple uses four semantic label levels (label, secondaryLabel, tertiaryLabel, quaternaryLabel) plus separator/opaqueSeparator instead of exposing a ramp [S-L01-013].
- **Accessibility constraints:** text steps must hit 4.5:1 against every background band they sit on [S-L01-022]. Interactive borders need 3:1 [S-L01-023]. Primer uses step 8 as the minimum interactive-border contrast on `bgColor-muted` [S-L01-027].
- **Default + heuristic:** Default to 12-13 solid neutrals plus 4-5 alpha neutrals, with bands documented (backgrounds, borders, text). Heuristic: reserve at least three near-white steps for surfaces in light mode and at least four dark steps for layering in dark mode (Carbon's dark layering uses Gray 100, 90, 80 and 70 [S-L01-029]).
- **Evidence:** [S-L01-013, S-L01-018, S-L01-022, S-L01-023, S-L01-027, S-L01-029, S-L01-031, S-L01-032, S-L01-036, S-L01-052]

### DC-L01-08: Number of accent (brand/UI) colors
- **Block path:** Foundations > Color > Brand vs UI color > Accent count
- **Questions the designer answers:** One accent or several? Do secondary and tertiary accents carry meaning, or only variety? Are there multiple products or brands sharing one system?
- **Options:**
  - **Single accent plus neutrals.** Carbon: "The core blue family serves as the primary action color across all IBM products"; other colors "used sparingly" [S-L01-029]. Apple: one app accent color, applied to the background of prominent buttons; "refrain from adding color to the background of multiple controls" [S-L01-013]. Spectrum: colors "used sparingly and intentionally" [S-L01-036].
  - **Primary + secondary + tertiary (plus error).** Material 3: primary for key actions (FAB, filled buttons), secondary for less prominent elements (filter chips, tonal buttons), tertiary for "contrasting accents" (badges, input fields), applied "at the designer's discretion" [S-L01-004].
  - **Brand + discovery + categorical accents.** Atlassian: `brand`, `discovery` (new features, onboarding) and 10 meaning-free accents (gray, red, green, blue, yellow, orange, teal, purple, magenta, lime) that should be interchangeable [S-L01-030].
  - **Brand + shared (suite) colors + product colors.** Fluent 2: a brand palette per product (Word, Excel, Teams, ...), a shared palette for avatars, badges and calendars, and semantic colors [S-L01-033].
  - **Monochrome "brand" with a separate emphasis color.** Polaris legacy tokens: `color-bg-fill-brand` = gray 15 (near-black) while `color-bg-fill-emphasis` = blue 13 [S-L01-039].
- **Visual effect:** One accent gives a focused, calm, enterprise feel and makes every colored element read as "actionable". Three accents (Material) give a more expressive, playful, personalized feel but need discipline to keep hierarchy [S-L01-004]. A black primary action (Polaris) reads premium, minimal and editorial, and lets merchant content provide the color [inferred]. Many interchangeable accents (Atlassian) support user-categorized content such as labels and tags without implying meaning [S-L01-030].
- **Depends on (upstream):** brand guidelines (L06); product type (content vs tool); dynamic color requirement (DC-L01-21).
- **Affects (downstream):** role taxonomy (DC-L01-11); component variants (button hierarchy, chips, badges); data-viz categorical palette (DC-L01-24).
- **Token encoding:** `color.brand.*` or `color.primary.*`, `color.secondary.*`, `color.tertiary.*`; accents as `color.accent.{hue}.*` (Atlassian `color.background.accent.blue.subtler`) [S-L01-032].
- **Platform notes:** on macOS, a user-chosen accent replaces the app accent unless the setting is "multicolor" [S-L01-013].
- **Accessibility constraints:** each accent used for text or UI boundaries must independently pass 4.5:1 / 3:1 [S-L01-022, S-L01-023]. Accent-only differences violate 1.4.1 when they carry meaning [S-L01-024].
- **Default + heuristic:** Default to one brand accent plus neutrals plus status colors, and optionally a secondary. Heuristic: add an accent only when it has a job (a second action tier, discovery, categories), not for decoration.
- **Evidence:** [S-L01-004, S-L01-013, S-L01-022, S-L01-023, S-L01-024, S-L01-029, S-L01-030, S-L01-032, S-L01-033, S-L01-036, S-L01-039]

### DC-L01-09: Adapting brand color for UI use
- **Block path:** Foundations > Color > Brand vs UI color > Brand-to-UI translation
- **Questions the designer answers:** Can the exact brand hex be the button color? What if it fails contrast? Should the brand color live on fills, text, or both?
- **Options:**
  - **Use the brand hex as a ramp anchor, and pick the UI step by contrast.** Stripe found none of its brand text colors (except black) met 4.5:1 and that simply darkening them looked "dark and muddy", so it rebuilt the ramps perceptually [S-L01-044]. Leonardo and Spectrum pick the step that meets the target ratio [S-L01-040, S-L01-036].
  - **Material custom baseline scheme with color fidelity.** Brand colors go into primary/secondary/tertiary/neutral/neutral variant. "Color fidelity" adjusts role tones toward the input color without breaking pairings [S-L01-057]. Material also offers a content-based algorithm and custom colors that "closely match the chosen input colors" [S-L01-006].
  - **Harmonize secondary brand/static colors.** `harmonize()` shifts static colors' hue toward the primary [S-L01-057]. On Android use `HarmonizedColors.applyToContextIfAvailable()` [S-L01-058].
  - **Brand on fills only; text uses neutral or a darker step.** Spectrum allows colored text only for accent and negative semantics (color 900) [S-L01-036]. Apple: to emphasize primary actions, "apply color to the background rather than to symbols or text" [S-L01-013].
  - **Brand kept out of large surfaces.** Fluent: "avoid ... using them on large surfaces" [S-L01-033].
- **Visual effect:** Exact-hex fills give maximum brand recognition but, with a light brand color (yellow, cyan, lime), force dark text on buttons. Spectrum handles yellow/orange/cyan/chartreuse with black text [S-L01-036]. Darkened steps keep contrast but can drift from the brand's feel unless rebuilt perceptually [S-L01-044]. Harmonized secondaries look more cohesive but less "exact" [S-L01-057].
- **Depends on (upstream):** brand identity (L06); contrast target (DC-L01-22); accent count (DC-L01-08).
- **Affects (downstream):** `on-primary` / text-on-brand color (white or black); button, link and focus colors; dark-mode brand step (DC-L01-18).
- **Token encoding:** keep the brand primitive separate from the semantic role: `color.brand.raw` (exact hex, for logos and marketing) vs `color.bg.brand` -> `{color.blue.600}` (UI step) [inferred]. Material's `primary_fixed` roles keep the same tone in light and dark when a constant brand fill is needed [S-L01-004].
- **Platform notes:** macOS/iOS app accent color is set once and applied by the system; on macOS it can be overridden by the user [S-L01-013].
- **Accessibility constraints:** logos and brand names are exempt from 1.4.3/1.4.11, but UI uses of brand color are not [S-L01-022, S-L01-023].
- **Default + heuristic:** Default: anchor a ramp on the brand hex, then map `bg.brand` to the nearest step that gives 4.5:1 with white (or black) text. Heuristic: if the brand color's WCAG ratio with white is below 3:1, use it as a fill with dark text, or as a tint/accent only, never for small text.
- **Evidence:** [S-L01-004, S-L01-006, S-L01-013, S-L01-022, S-L01-023, S-L01-033, S-L01-036, S-L01-040, S-L01-044, S-L01-057, S-L01-058]

### DC-L01-10: Overall chroma level (muted vs vivid palette)
- **Block path:** Foundations > Color > Palette character > Vibrancy
- **Questions the designer answers:** Should the UI feel calm and muted, or bold and saturated? How much color should the non-brand parts carry? Does the product need to feel "expressive"?
- **Options:**
  - **Monochrome / near-monochrome.** MCU Monochrome variant (chroma 0 on all palettes); Neutral variant (primary chroma 12 in 2021; 8-12 in 2025 on phone) [S-L01-010]. Polaris black brand [S-L01-039].
  - **Tonal / moderate.** MCU TonalSpot, the Android 12-13 default "low to medium colorfulness": primary chroma 36 (2021) or 32 (2025, 26 in dark on phone) [S-L01-010, S-L01-058].
  - **Vivid.** MCU Vibrant (primary chroma 200, i.e. maximum available) [S-L01-010]. Tailwind v4's P3-leaning OKLCH palette (blue-500 chroma 0.214, red-600 0.245) [S-L01-045, S-L01-062].
  - **Expressive / hue-rotated.** MCU Expressive rotates primary hue (+240 in 2021) and in the 2025 spec uses primary chroma 48 light / 36 dark on phone [S-L01-010]. Google describes Material 3 Expressive dynamic color as unlocking "more variation and higher chroma across all hues", from "soft neutrals" to "juicy vibrance" [S-L01-011].
  - **Accent text vs gray text.** Radix: using the accent scale for text gives "a more colorful vibe"; using the gray scale gives "a more functional vibe" [S-L01-053].
- **Visual effect:** Low chroma reads calm, serious, professional and content-first. Moderate chroma reads friendly and approachable. High chroma reads energetic, youthful and consumer-grade, but risks fatigue and weakens status colors (everything shouts). Hue-rotated expressive schemes feel surprising and playful [inferred personality mapping; chroma values from S-L01-010].
- **Depends on (upstream):** brand personality (L06); content type; dynamic color use (DC-L01-21).
- **Affects (downstream):** neutral tint strength (DC-L01-06); status color distinctness (DC-L01-15); data-viz palette saturation (DC-L01-24).
- **Token encoding:** a builder-level parameter (e.g. `$extensions.generator.chroma = "tonal"`) feeding the generator; no DTCG type of its own [inferred].
- **Platform notes:** on Android, user-chosen color styles map to MCU variants [S-L01-058]; apps using dynamic color get the 2025 spec's higher-chroma palettes automatically [S-L01-011].
- **Accessibility constraints:** very high chroma at mid-lightness can fail 4.5:1 with both black and white text (e.g. saturated orange). Check pairs [inferred]. Vivid palettes need non-color cues for status [S-L01-024].
- **Default + heuristic:** Default to tonal (moderate) for productivity products and vivid for consumer and marketing. Heuristic: keep large-area colors (surfaces) low chroma and spend chroma on small, high-meaning elements (primary action, status, selection) [S-L01-013, S-L01-033].
- **Evidence:** [S-L01-010, S-L01-011, S-L01-013, S-L01-024, S-L01-033, S-L01-039, S-L01-045, S-L01-053, S-L01-058, S-L01-062]

### DC-L01-11: Semantic role taxonomy (naming grammar for color roles)
- **Block path:** Foundations > Color > Semantic roles > Taxonomy
- **Questions the designer answers:** Do we name colors by what they are painted on (background, text, border), by pairing (container and on-container), or by component? How many roles do we need? Where do status and brand live?
- **Options (compared):**

| System | Grammar | Example tokens | Role set |
|---|---|---|---|
| Material 3 | role + container/on pairing; 26 standard roles in 6 groups | `primary`, `on-primary`, `primary-container`, `on-primary-container`, `surface-container-high`, `outline-variant`, `inverse-primary` | primary, secondary, tertiary, error, surface, outline, plus add-ons (fixed, fixed-dim, surface dim/bright) [S-L01-004]; 2025 spec adds `primary_dim`, `secondary_dim`, `tertiary_dim`, `error_dim` [S-L01-010] |
| Primer | `[category]-[role]-[variant]` | `bgColor-accent-muted`, `fgColor-onEmphasis`, `borderColor-danger-emphasis` | default, muted, emphasis, accent, success, attention, severe, danger, open, closed, done, draft, upsell, sponsors, neutral [S-L01-027, S-L01-050] |
| Atlassian | `color.[property].[role].[emphasis].[state]` | `color.background.brand.bold.hovered`, `color.text.subtle`, `elevation.surface.raised` | neutral, brand, information, success, warning, danger, discovery, accent (10 hues), inverse, input [S-L01-030, S-L01-032] |
| Carbon | `$[element]-[role]-[state]` in 10 groups | `$layer-01`, `$text-secondary`, `$border-subtle`, `$support-error`, `$background-hover`, `$focus` | background, layer, field, border, text, link, icon, support, focus, skeleton [S-L01-029] |
| Fluent 2 | `color[Palette][Role][Level][State]` | `colorNeutralBackground1Hover`, `colorBrandBackground`, `colorStatusDangerForeground1`, `colorPaletteBerryBackground2` | neutral, brand, status (danger, success, warning), shared palette hues [S-L01-033, S-L01-034] |
| Polaris (legacy) | `color-[element]-[type]-[role]-[state]` | `color-bg-fill-brand-hover`, `color-bg-surface-secondary`, `color-text-secondary` | brand, emphasis, success, critical, caution, warning, info, magic, inverse (all present as `color-bg-fill-*` tokens in source) [S-L01-039] |
| Apple | purpose-named dynamic system colors | `label`, `secondaryLabel`, `systemBackground`, `secondarySystemGroupedBackground`, `separator`, `link`, macOS `controlAccentColor` | foreground label levels, background levels (system/grouped), separators, links, accent [S-L01-013] |

- **Visual effect:** The taxonomy is not visible to users, but it drives consistency. Property-first grammars (Primer, Atlassian, Carbon) make it hard to put a border color on text, so UIs stay coherent. Pairing grammars (Material) guarantee legible foreground/background combinations when colors change dynamically ("apply colors only in the intended pairs") [S-L01-004].
- **Depends on (upstream):** accent count (DC-L01-08); status set (DC-L01-15); dynamic color (pairing grammars suit it, DC-L01-21).
- **Affects (downstream):** every component token (L08); Figma variable collections (L07); how the builder's questionnaire is structured.
- **Token encoding:** semantic tier aliases primitives, e.g. `color.bg.accent.emphasis` -> `{color.blue.5}` (Primer's `bgColor-accent-emphasis` = `{base.color.blue.5}` [S-L01-050]).
- **Platform notes:** Apple and Android expose system semantic colors (UIKit/AppKit/SwiftUI; Android `colorPrimary`, `colorOnPrimary`, ...) [S-L01-013, S-L01-058]. A cross-platform system maps its roles onto them.
- **Accessibility constraints:** the taxonomy should encode pairs (bg + fg) so contrast can be tested per pair. Material pairs guarantee at least 3:1 [S-L01-004].
- **Default + heuristic:** Default to the property x role x emphasis x state grammar (Atlassian/Primer style) with explicit on-colors for bold fills (`fg.onEmphasis`, `text.inverse`). Heuristic: if the product must support Material dynamic color, also emit Material role aliases.
- **Evidence:** [S-L01-004, S-L01-010, S-L01-013, S-L01-027, S-L01-029, S-L01-030, S-L01-032, S-L01-033, S-L01-034, S-L01-039, S-L01-050, S-L01-058]

### DC-L01-12: Emphasis levels per role
- **Block path:** Foundations > Color > Semantic roles > Emphasis
- **Questions the designer answers:** How many strengths does each role need (subtle tint, solid fill, strong)? What is the default strength for a status banner vs a button?
- **Options:**
  - **Two levels (muted / emphasis).** Primer: `bgColor-success-muted` (`green.0`) vs `bgColor-success-emphasis` (#1f883d), plus `fgColor-onEmphasis` [S-L01-050].
  - **Container vs base (Material).** `primary` (tone 40 light) for high-emphasis fills and text; `primary-container` (tone 90 light) for "standout fill" such as FAB, with `on-primary-container` [S-L01-004, S-L01-010].
  - **Up to six levels (Atlassian).** subtlest, subtler, subtle, (default), bold, bolder, boldest. "Bolder colors have more contrast against the default surface" [S-L01-030]. E.g. `color.background.brand.subtlest` ... `color.background.brand.boldest` [S-L01-032].
  - **Numbered levels (Fluent).** `colorNeutralForeground1-5`, `colorNeutralBackground1-8` [S-L01-034].
  - **Label hierarchy (Apple).** Primary, secondary, tertiary, quaternary labels [S-L01-013].
- **Visual effect:** More levels allow soft, tinted status panels and quiet selection states, giving a gentler, more refined UI. Two levels give a punchier look (tint or solid) with less nuance [inferred]. Subtle levels on large areas keep status visible without alarm (Atlassian "subtlest" backgrounds for section messages) [inferred from S-L01-032 naming].
- **Depends on (upstream):** step count (DC-L01-02); role taxonomy (DC-L01-11).
- **Affects (downstream):** badges, banners, tags, buttons (primary/secondary/tertiary), selected states.
- **Token encoding:** emphasis as a name segment: `color.bg.danger.subtle`, `color.bg.danger.bold`; foreground-on-bold as `color.text.inverse` or `fg.onEmphasis`.
- **Platform notes:** platform-neutral.
- **Accessibility constraints:** text on subtle tints must still meet 4.5:1; bold fills need an on-color at 4.5:1. Atlassian adds special `warning.inverse` tokens because white text fails on yellow [S-L01-030].
- **Default + heuristic:** Default to three levels (subtle, default, bold) plus an on-bold foreground. Heuristic: add subtlest/boldest only when you have both page-level and component-level uses of the same role.
- **Evidence:** [S-L01-004, S-L01-010, S-L01-013, S-L01-030, S-L01-032, S-L01-034, S-L01-050]

### DC-L01-13: Surface and layering model
- **Block path:** Foundations > Color > Semantic roles > Surfaces
- **Questions the designer answers:** How do stacked areas (page, card, popover, sidebar) differ in color? Do surfaces get lighter or darker as they stack? Does color express elevation, or do shadows?
- **Options:**
  - **Named container tiers not tied to elevation (Material 3).** `surface`, then `surface-container-lowest`, `-low`, `-container`, `-high`, `-highest`, plus `surface-dim` and `surface-bright` [S-L01-004]. 2021 tones: light 98 / 100 / 96 / 94 / 92 / 90; dark 6 / 4 / 10 / 12 / 17 / 22 (dim 87 light, bright 24 dark) [S-L01-010]. Roles "are not tied to elevation"; tonal difference is the default separator [S-L01-054].
  - **Alternating vs stepping layers (Carbon).** Light themes alternate White and Gray 10 per layer. Dark themes go one step lighter per layer (Gray 100, then 90, 80, 70). Tokens `$layer-01..03` [S-L01-029].
  - **Elevation-named surfaces (Atlassian).** `elevation.surface`, `.sunken`, `.raised`, `.overlay`, each with hovered/pressed, plus matching `elevation.shadow.*` [S-L01-032].
  - **Base vs elevated (Apple iOS dark).** Base backgrounds are dimmer and elevated backgrounds brighter for foreground interfaces (popovers, sheets); the system switches automatically [S-L01-014]. System vs grouped background sets, each primary/secondary/tertiary [S-L01-013].
  - **White overlays by dp (Material 2, legacy).** 0dp 0% up to 24dp 16% white overlay on #121212 [S-L01-055].
- **Visual effect:** Tonal layering (no shadows) gives a flat, calm, modern look. Carbon's alternating light layers give a crisp, grid-like enterprise look. Lighter-when-higher dark surfaces mimic light falling on raised objects, making dark UIs feel dimensional without glowing shadows [S-L01-055] [inferred for the aesthetic readings].
- **Depends on (upstream):** neutral ramp (DC-L01-07); dark-mode strategy (DC-L01-18); elevation/shadow decisions (L04).
- **Affects (downstream):** cards, sheets, dialogs, menus, navigation bars (Material maps them to specific surface-container roles by default [S-L01-004]); hover colors on surfaces.
- **Token encoding:** `color.surface.{base|raised|overlay|sunken}` or `color.surface.container.{lowest..highest}`, aliasing neutral primitives per mode.
- **Platform notes:** iOS switches base to elevated automatically, so custom backgrounds can break it [S-L01-014]. On macOS, desktop tinting (graphite accent) tints window backgrounds [S-L01-014].
- **Accessibility constraints:** adjacent surfaces with interactive meaning need visible edges. For interactive components Material asks for sufficient contrast between surfaces [S-L01-054]. 1.4.11 applies to component boundaries [S-L01-023].
- **Default + heuristic:** Default to 4-5 surface tiers named by role (base, raised, overlay, sunken) and mapped separately for light and dark. Heuristic: in light mode separate layers with shadow or border plus a subtle tone; in dark mode separate them with lighter tones.
- **Evidence:** [S-L01-004, S-L01-010, S-L01-013, S-L01-014, S-L01-023, S-L01-029, S-L01-032, S-L01-054, S-L01-055]

### DC-L01-14: Foreground ("on") colors and text hierarchy
- **Block path:** Foundations > Color > Semantic roles > Foreground
- **Questions the designer answers:** How many text colors (primary, secondary, disabled)? Are they solid colors or opacities of one color? What goes on top of a colored fill?
- **Options:**
  - **Solid tokens per level.** Carbon `$text-primary` / `$text-secondary` (e.g. `$text-secondary` maps to Gray 70 or Gray 30 by theme) [S-L01-029]. Material `on-surface` (tone 10 light / 90 dark) and `on-surface-variant` (30 / 80) [S-L01-010]. Fluent `colorNeutralForeground1` = #242424 light / #ffffff dark [S-L01-034].
  - **Opacity-based levels.** Material 2 dark: 87% / 60% / 38% white for high, medium and disabled [S-L01-055]. Material 3 disabled content = `on-surface` at 38% [S-L01-064].
  - **On-colors per fill.** Material `on-primary`, `on-primary-container`, ... [S-L01-004]. Primer `fgColor-onEmphasis` [S-L01-027]. Atlassian `inverse` role [S-L01-030].
  - **Accent-colored text.** Radix: accent text step 11/12 for a colorful vibe, gray for a functional vibe [S-L01-053]. Spectrum allows colored text only for accent and negative [S-L01-036].
- **Visual effect:** Solid colors keep text crisp and predictable over any background. Opacity-based text blends with tinted surfaces for a harmonious but less predictable result [inferred]. High-contrast primary text with low-contrast secondary text creates strong hierarchy; Material's standard contrast level "emphasizes visual hierarchy using high and low contrast elements" [S-L01-006].
- **Depends on (upstream):** surface model (DC-L01-13); contrast target (DC-L01-22).
- **Affects (downstream):** typography tokens (L02 text styles reference color tokens); icon colors; link color.
- **Token encoding:** `color.text.{primary|secondary|tertiary|disabled|inverse|onBrand}`, `color.icon.*`. DTCG supports `alpha` if opacity-based [S-L01-018].
- **Platform notes:** Apple label colors are vibrancy-aware and adapt automatically; prefer them over custom text colors [S-L01-014].
- **Accessibility constraints:** text 4.5:1 (3:1 at 24px+/18.66px bold) [S-L01-022]; disabled text is exempt [S-L01-022, S-L01-063]; placeholder text is not exempt under WCAG, and APCA treats Lc 30 as the absolute minimum for placeholder/disabled [S-L01-026].
- **Default + heuristic:** Default to solid tokens: primary, secondary, tertiary/placeholder, disabled, inverse, plus an on-color for each bold fill. Heuristic: secondary text should still pass 4.5:1 on the lowest surface it appears on.
- **Evidence:** [S-L01-004, S-L01-006, S-L01-010, S-L01-014, S-L01-018, S-L01-022, S-L01-026, S-L01-027, S-L01-029, S-L01-030, S-L01-034, S-L01-036, S-L01-053, S-L01-055, S-L01-063, S-L01-064]

### DC-L01-15: Status and feedback colors
- **Block path:** Foundations > Color > Semantic roles > Status
- **Questions the designer answers:** Which statuses exist (success, warning, error, info, and more)? Which hue for each? Can the brand color double as a status color? How do statuses survive color blindness and dark mode?
- **Options (status sets):**
  - **Four classic:** success, warning, error/danger, info. Radix recommends error = red/ruby/tomato/crimson, success = green/teal/jade/grass/mint, warning = yellow/amber/orange, info = blue/indigo/sky/cyan [S-L01-053].
  - **Extended:** Atlassian adds discovery (purple, new things) [S-L01-030]. Primer adds attention (yellow), severe (orange), done (purple), open/closed/draft (workflow) and sponsors [S-L01-050]. Spectrum uses informative, accent, negative, notice and positive [S-L01-036]. Carbon's alert palette: Red 60 danger, Orange 40 serious warning, Yellow 30 warning, Green 60 success [S-L01-056].
  - **Static vs dynamic.** Material error roles "are made static by default with any dynamic color scheme" but still adapt to light and dark [S-L01-004].
  - **Brand = success.** Primer's green primary button is also its success color [S-L01-027]; an unusual coupling.
- **Visual effect:** Few statuses keep the UI calm and each alert unmistakable. Many statuses (Primer's workflow colors) make dense developer UIs scannable but raise the learning cost [inferred]. Warm warning colors (yellow/amber) are inherently light, so warning fills look different in weight from error fills unless text color adapts [S-L01-030, S-L01-036].
- **Depends on (upstream):** accent hue (avoid a brand hue that collides with a status hue, e.g. a red brand vs error) [inferred]; emphasis levels (DC-L01-12); colorblind strategy (DC-L01-23).
- **Affects (downstream):** banners, toasts, inline validation, badges, form field error borders, charts (Carbon alert palette in data viz [S-L01-056]).
- **Token encoding:** `color.{bg|text|border|icon}.{success|warning|danger|info}.{subtle|bold}`; Fluent `colorStatusDangerBackground1..3` [S-L01-034]; Atlassian `color.background.danger.subtler.hovered` [S-L01-032].
- **Platform notes:** Apple warns that color meaning is cultural (red is positive in Chinese stock apps) [S-L01-013].
- **Accessibility constraints (pitfalls):** (1) Yellow/amber fails 4.5:1 with white text, so use dark text on warning fills (Atlassian `warning.inverse` [S-L01-030]; Spectrum yellow/orange/cyan/chartreuse with black text [S-L01-036]). (2) Red vs green is the most common deficiency (about 1 in 12 men) [S-L01-060], so pair status color with an icon and text [S-L01-024] or ship colorblind themes (Primer remaps success to blue and danger to orange for protanopia/deuteranopia [S-L01-050]). (3) Status color used for text needs 4.5:1, and status icons and borders need 3:1 [S-L01-022, S-L01-023].
- **Default + heuristic:** Default to four statuses (success, warning, danger, info), each with subtle and bold levels plus text and icon, and always with an icon. Heuristic: pick status hues at least 60 degrees apart from the brand hue, or accept that the brand is also a status [inferred].
- **Evidence:** [S-L01-004, S-L01-013, S-L01-022, S-L01-023, S-L01-024, S-L01-027, S-L01-030, S-L01-032, S-L01-034, S-L01-036, S-L01-050, S-L01-053, S-L01-056, S-L01-060]

### DC-L01-16: Borders, outlines and focus color
- **Block path:** Foundations > Color > Semantic roles > Borders and focus
- **Questions the designer answers:** Do component boundaries need to be visible (inputs, checkboxes)? Which border is decorative only? What color is the focus ring, and does it change per theme?
- **Options:**
  - **Two-tier outline.** Material `outline` (tone 50 light / 60 dark) for important boundaries such as text fields, and `outline-variant` (80 / 30) for dividers and decoration. Don't use `outline-variant` to define target boundaries unless the inner content provides contrast [S-L01-004, S-L01-010].
  - **Border-by-purpose steps.** Spectrum gray 200-300 decorative, 400 field borders, 600 control borders [S-L01-036]. Radix steps 6 (non-interactive), 7 (interactive), 8 (strong/focus) [S-L01-002].
  - **Single focus color per theme.** Carbon `$focus` is a 2px Blue 60 border in light and White in dark, with `$focus-inset` to guarantee 3:1 [S-L01-029]. Atlassian `color.border.focused` [S-L01-032]. Fluent keeps the control color and uses a thicker stroke for focus (`colorStrokeFocus2` black in light) [S-L01-033, S-L01-034].
- **Visual effect:** Strong outlines give an explicit, form-heavy, utilitarian feel. Subtle borders plus tonal fills give a softer, modern feel. A brand-colored focus ring feels branded; a black/white ring feels neutral and is always visible [inferred].
- **Depends on (upstream):** neutral ramp (DC-L01-07); surface model (DC-L01-13); contrast target (DC-L01-22).
- **Affects (downstream):** inputs, checkboxes, radios, switches, cards, dividers, tables, focus rings on all interactive components (L08).
- **Token encoding:** `color.border.{subtle|default|strong|interactive|focused}`, `color.divider`, `color.focus.ring`, `color.focus.inset`.
- **Platform notes:** macOS `keyboardFocusIndicatorColor` [S-L01-013]; in forced-colors mode the browser forces border and outline colors to system colors [S-L01-048].
- **Accessibility constraints:** 1.4.11: component boundaries needed to identify the control, and focus indicators, need 3:1 against adjacent colors; disabled is exempt [S-L01-023]. 2.4.13 (AAA): focus indicator area at least a 2 CSS px perimeter, and 3:1 between focused and unfocused pixels [S-L01-059].
- **Default + heuristic:** Default to three border strengths (subtle decorative, default interactive at 3:1, strong) plus one focus color per mode with an inset/offset ring. Heuristic: if an input's only boundary is its border, that border must be the 3:1 token.
- **Evidence:** [S-L01-002, S-L01-004, S-L01-010, S-L01-013, S-L01-023, S-L01-029, S-L01-032, S-L01-033, S-L01-034, S-L01-036, S-L01-048, S-L01-059]

### DC-L01-17: Interaction state color method
- **Block path:** Foundations > Color > States > Interaction states
- **Questions the designer answers:** How does a component change color on hover, press, focus, selection, drag and disabled? One rule for every color, or tokens per state? Do things get darker or lighter when pressed?
- **Options:**
  - **State layers (opacity overlays of the content color).** Material 3: hover +8%, focus +10%, press +10%, drag +16%. The layer "uses the same color as the content" (the on-color), is 40dp inside a 48dp target, and only one state layer applies at a time [S-L01-005]. Compose tokens match (0.08 / 0.1 / 0.1 / 0.16) [S-L01-065]. The material-web v0.192 tokens still list focus and pressed at 0.12, an implementation lag worth noting [S-L01-064]. Disabled: container `on-surface` at 12%, content `on-surface` at 38% [S-L01-064].
  - **Step shift on the ramp.** Carbon: hover = a "half step" (its own off-palette values), active = two full steps, selected = one full step. Values in 100-70 get lighter and values in 60-10 get darker. Disabled is always gray [S-L01-029]. Radix: step 3 normal, 4 hover, 5 pressed/selected; step 9 solid, 10 solid hover [S-L01-002]. Fluent light: brand background brand80, hover brand70, pressed brand40 (darker); dark: brand70, hover brand80 (lighter) [S-L01-034].
  - **Dedicated state tokens per role.** Atlassian `.hovered`, `.pressed` on most background tokens, plus generic `color.interaction.hovered` / `.pressed` overlays and `opacity.disabled` [S-L01-032]. Polaris `-hover`, `-active`, `-selected`, `-disabled` [S-L01-039].
  - **Direction conventions.** Fluent: components get darker as you interact (rest, hover, pressed/selected), but Windows reverses this (lighter on interaction) [S-L01-033]. Carbon: direction depends on the base value's lightness [S-L01-029].
  - **Focus by stroke, not fill.** Fluent keeps the fill and thickens the stroke [S-L01-033]; Carbon uses a 2px `$focus` border [S-L01-029].
- **Visual effect:** Overlays give consistent, subtle, "material" feedback on any color, including dynamic ones, with a soft tactile feel. Step shifts give crisper, more deliberate color changes and exact control in each theme. Darker-on-press feels like pressing into paper; lighter-on-press (Windows, dark themes) feels like lighting up [inferred].
- **Depends on (upstream):** step semantics (DC-L01-03: purpose-indexed ramps provide hover/pressed steps); dynamic color (overlays suit unknown colors, DC-L01-21); dark mode (direction flips, DC-L01-18).
- **Affects (downstream):** every interactive component's state tokens (L08); motion of state transitions (L04).
- **Token encoding:** either an opacity token set (`state.hover.opacity = 0.08`, DTCG `$type: "number"`) applied to the on-color, or per-role state tokens (`color.bg.brand.bold.hovered`). Figma variables can hold both [inferred; L07 to confirm].
- **Platform notes:** Android/Compose uses state layers natively [S-L01-065]; web implementations often use `color-mix()` for overlays (Tailwind uses `color-mix(in oklab, ...)` for opacity) [S-L01-045]; Windows reverses direction [S-L01-033].
- **Accessibility constraints:** hover styles need not meet contrast [S-L01-023]; focus indicators must meet 3:1 against adjacent colors (1.4.11) [S-L01-023] and at AAA 3:1 between focused and unfocused states (2.4.13) [S-L01-059]; disabled is exempt [S-L01-023, S-L01-063]; selected states must not be shown by color alone [S-L01-024].
- **Default + heuristic:** Default to per-role state tokens generated from a ramp step shift (hover = +1 step, pressed = +2 steps, toward higher contrast with the surface), with a documented overlay fallback for dynamic or user colors. Heuristic: use overlays when the color is unknown at design time; use step shifts when every color is known.
- **Evidence:** [S-L01-002, S-L01-005, S-L01-023, S-L01-024, S-L01-029, S-L01-032, S-L01-033, S-L01-034, S-L01-039, S-L01-045, S-L01-059, S-L01-063, S-L01-064, S-L01-065]

### DC-L01-18: Dark mode mapping strategy
- **Block path:** Foundations > Color > Modes > Dark mode mapping
- **Questions the designer answers:** Is dark mode required? Do we reuse the light ramps with a new mapping, build separate dark ramps, or just invert? Does the brand color stay the same in dark?
- **Options:**
  - **Tone reassignment on shared palettes (Material).** Same tonal palettes, different tones per role: primary 40 becomes 80, on-primary 100 becomes 20, primary-container 90 becomes 30, surface 98 becomes 6 (2021) or 4 (2025, phone) [S-L01-010]. "The same color roles are used in light and dark themes" [S-L01-006].
  - **Mirrored ramp by symmetry (Atlassian).** "If a button color is 700 in light theme, it will be 400 in dark theme"; 100 maps to 1000. Separate light and dark neutral ramps (Neutral100 maps to DarkNeutral100) [S-L01-031].
  - **Separate dark scales (Radix, Primer, Spectrum).** Radix ships `blue-dark` 1-12 with the same step jobs. The solid step 9 stays #0090ff in both modes while step 10 (hover) gets lighter in dark (#3b9eff) [S-L01-052]. Primer base colors are defined separately for dark and dark dimmed [S-L01-050]. Spectrum generates each theme's grays against its own gray-100, and dark themes target higher contrast ratios [S-L01-036].
  - **Theme files per background (Carbon).** White, Gray 10, Gray 90, Gray 100 themes; token names stay and values change [S-L01-029].
  - **Naive inversion.** Apple: dark colors "aren't necessarily inversions of their light counterparts: while many colors are inverted, some are not" [S-L01-014]. No major system ships a pure inversion [inferred from all sources above].
- **Visual effect:** Mirrored or tone-reassigned mappings keep hierarchy identical across modes, so the product feels like the same app. Separate hand-tuned dark ramps can look richer (e.g. deeper blue-tinted darks) but drift more. Keeping the brand solid step identical in both modes (Radix step 9) preserves brand recognition; lighter accents in dark (Material primary 80) look softer and reduce glare [S-L01-010, S-L01-052] [inferred for the perception].
- **Depends on (upstream):** step semantics (DC-L01-03: symmetric ramps suit mirroring); neutral ramps (DC-L01-07); platform (Apple expects both appearances "even if your app ships in a single appearance", for Liquid Glass adaptivity [S-L01-013]).
- **Affects (downstream):** every semantic token gets a per-mode value; images and illustrations may need dark variants (Apple advises separate assets or darkening white-background images [S-L01-014]); shadows (L04).
- **Token encoding:** semantic tokens resolve per mode. DTCG Resolver: a `theme` modifier with `light` and `dark` contexts pointing at different token sources [S-L01-019]. Primer: per-theme overrides in `$extensions["org.primer.overrides"]` [S-L01-050]. CSS: `light-dark()` with `color-scheme: light dark` (Baseline newly available since May 2024) [S-L01-047].
- **Platform notes:** Apple: avoid app-specific appearance settings; follow the system setting [S-L01-014]. Android: Material light/dark from the same roles [S-L01-006]. Web: `prefers-color-scheme` or `light-dark()` [S-L01-047].
- **Accessibility constraints:** re-check every pair in dark mode. Apple asks for at least 4.5:1 and strives for 7:1 for custom colors, especially small text [S-L01-014]. Increase Contrast in dark can reduce contrast between dark text and dark backgrounds; test it [S-L01-014].
- **Default + heuristic:** Default to shared hue ramps with a mirrored mapping plus separate dark neutral ramps. Heuristic: map by role, not by value. For each semantic token pick the dark step that gives the same contrast relationship as in light.
- **Evidence:** [S-L01-006, S-L01-010, S-L01-013, S-L01-014, S-L01-019, S-L01-029, S-L01-031, S-L01-036, S-L01-047, S-L01-050, S-L01-052]

### DC-L01-19: Dark surface darkness, chroma in dark, and dimmed themes
- **Block path:** Foundations > Color > Modes > Dark base and dimmed
- **Questions the designer answers:** How dark is the darkest background: pure black, near-black, or charcoal? Should accents be desaturated in dark? Do we offer a softer "dimmed" dark?
- **Options (real values):**
  - **Pure black (#000).** Allowed for OLED battery savings, but "turning pixels on and off can cause a delay when the screen is scrolled, making the pixels blur" (Material 2) [S-L01-055]. Apple: avoid a bright object on a very dark or black background in immersive visionOS [S-L01-013].
  - **Near-black.** Material 2025 spec dark surface tone 4 on phone [S-L01-010]; Carbon Gray 100 #161616 [S-L01-029]; Primer dark #0D1117 (blue-tinted) [S-L01-050]; Material 2 #121212 [S-L01-055].
  - **Charcoal / softer dark.** Material 2021 dark surface tone 6 [S-L01-010]; Carbon Gray 90 #262626 [S-L01-029]; Fluent `colorNeutralBackground1` dark #292929 (with Background2 #1f1f1f, Background3 #141414) [S-L01-034].
  - **Dimmed dark theme.** Primer dark dimmed raises `bgColor-default` to neutral.3 and softens "white" to #cdd9e5 [S-L01-050]. Spectrum's "darkest" theme is a further step darker; its dark themes target higher contrast ratios [S-L01-036].
  - **Accent desaturation / lightening in dark.** Material 2: primaries desaturated to pass 4.5:1 at all elevations, with 15.8:1 white text on surface [S-L01-055]. Material 3: accent roles use lighter tones (80) in dark [S-L01-010]. Fluent's shared palette "shift[s] in saturation and brightness to reduce eye strain" in dark [S-L01-033]. Material 2025 TonalSpot lowers primary chroma in dark on phone (26 vs 32) [S-L01-010].
- **Visual effect:** Pure black is dramatic, high-contrast and cinematic, but creates halation and smear on OLED. Near-black (#0D1117 to #161616) looks sleek and modern. Charcoal (#262626 to #292929) looks soft and comfortable for long sessions but less "true dark". Dimmed themes reduce glare for low-light reading. Desaturated accents in dark avoid neon vibration [S-L01-055] [inferred for the aesthetic readings].
- **Depends on (upstream):** dark mapping (DC-L01-18); neutral temperature (tinted darks, DC-L01-06); surface model (dark layers need room to step lighter, DC-L01-13).
- **Affects (downstream):** all dark surface tokens; elevation expression; the dark brand step.
- **Token encoding:** a separate mode (`dark`, `dark-dimmed`, `darkest`) in the Resolver or Figma modes [S-L01-019]; Primer names themes `dark`, `dark-dimmed`, `dark-high-contrast` [S-L01-050].
- **Platform notes:** Dark Mode is not supported in visionOS or watchOS; watchOS icons should avoid black backgrounds [S-L01-014, S-L01-015].
- **Accessibility constraints:** very high contrast (white on pure black) can cause visual discomfort, which is why Material's medium contrast level exists for people who "may experience visual discomfort with higher contrasts from effects like halation" [S-L01-006]. Body text still needs 4.5:1 [S-L01-022].
- **Default + heuristic:** Default dark base between #121212 and #1a1a1a (or tone 4-6) with a slight neutral tint, accents one or two steps lighter and lower in chroma than in light. Heuristic: offer "dimmed" only if the audience reads long-form text at night (developer tools, reading apps) [inferred].
- **Evidence:** [S-L01-006, S-L01-010, S-L01-013, S-L01-014, S-L01-015, S-L01-019, S-L01-022, S-L01-029, S-L01-033, S-L01-034, S-L01-036, S-L01-050, S-L01-055]

### DC-L01-20: Accessibility theme set (contrast levels, high contrast, forced colors, colorblind themes)
- **Block path:** Foundations > Color > Modes > Accessibility modes
- **Questions the designer answers:** Beyond light and dark, which modes do we support? Do we follow OS contrast settings? Do we survive Windows forced colors?
- **Options:**
  - **Contrast levels.** Material standard, medium (3:1 minimum) and high (7:1) in both light and dark, applied through roles [S-L01-006]. MCU implements them with contrast curves, e.g. `on_surface` targets (4.5, 7, 11, 21) [S-L01-010].
  - **Increased-contrast variants.** Apple: every custom color should supply light, dark and increased-contrast variants for each [S-L01-013].
  - **High-contrast themes.** Primer `light-high-contrast`, `dark-high-contrast`, `dark-dimmed-high-contrast`, targeting at least 7:1 for most text and interactive elements [S-L01-027, S-L01-050].
  - **Colorblind themes.** Primer `light/dark-protanopia-deuteranopia` and `light/dark-tritanopia` (plus high-contrast versions): success becomes blue.5, danger becomes orange.5 for protan/deutan [S-L01-050].
  - **Forced colors (Windows contrast themes, web).** `@media (forced-colors: active)` forces color, background, border and outline to system colors (Canvas, CanvasText, LinkText, ButtonFace, ButtonText, Highlight, HighlightText, GrayText, Field, FieldText), sets box-shadow/text-shadow to none, and can be opted out per element with `forced-color-adjust: none` [S-L01-048].
- **Visual effect:** High-contrast modes flatten subtle tints into stark black/white and strong accent contrast, losing some brand nuance but greatly improving legibility. Forced colors reduce the UI to the user's palette, so any meaning carried only by background color or shadow disappears [S-L01-048] [inferred for the aesthetic readings].
- **Depends on (upstream):** role taxonomy (roles make remapping possible, DC-L01-11); contrast target (DC-L01-22).
- **Affects (downstream):** every semantic token gets additional modes; components need forced-colors fallbacks such as borders instead of shadows (the MDN example replaces box-shadow with a `2px ButtonText` border [S-L01-048]).
- **Token encoding:** additional Resolver modifier contexts (e.g. `contrast: standard|high`, `vision: default|protan-deutan|tritan`) combined with `theme` [S-L01-019]; Primer uses a flat theme list with overrides [S-L01-050].
- **Platform notes:** Android offers Material contrast levels [S-L01-006]; Apple has Increase Contrast and Reduce Transparency [S-L01-014]; web has forced-colors (widely available since Sep 2022) [S-L01-048].
- **Accessibility constraints:** 1.4.6 AAA 7:1 / 4.5:1 large is the natural target for high-contrast modes [S-L01-025].
- **Default + heuristic:** Default to light and dark, plus a forced-colors-safe component layer (borders, not only fills or shadows). Add high contrast as the first extra mode and colorblind themes for data-dense or status-heavy products. Heuristic: if a status or selection is conveyed by fill color, add a border or icon so it survives forced colors [S-L01-048, S-L01-024].
- **Evidence:** [S-L01-006, S-L01-010, S-L01-013, S-L01-014, S-L01-019, S-L01-024, S-L01-025, S-L01-027, S-L01-048, S-L01-050]

### DC-L01-21: Dynamic and personalized color
- **Block path:** Foundations > Color > Modes > Dynamic color
- **Questions the designer answers:** Can the user's wallpaper, accent choice or content change our colors? Which colors must stay fixed (brand, error)? How do we look inside system materials (Liquid Glass) and tinted icon modes?
- **Options:**
  - **Static only.** Hand-picked roles; Material calls this a static or baseline scheme [S-L01-006].
  - **Material dynamic color (Android 12+).** The wallpaper is quantized to a source color, which becomes 5 key colors, then tonal palettes, then 26 roles [S-L01-006]. Android 12 shipped Tonal Spot; Android 13 added Neutral, Vibrant and Expressive [S-L01-058]. Content-based color derives the scheme from in-app imagery (album art, video preview) [S-L01-006]. Error stays static by default [S-L01-004].
  - **Material 3 Expressive (2025).** Google: dynamic color upgraded "to unlock more variation and higher chroma across all hues"; apps using dynamic color get it automatically [S-L01-011]. In MCU this is spec version 2025: e.g. Expressive primary chroma 48 light / 36 dark on phone; new `primary_dim`, `secondary_dim`, `tertiary_dim`, `error_dim` roles; dark surface tone 4 on phone. A 2026 spec also exists in code [S-L01-010]. The M3 roles page (checked today) still documents 26 standard roles and does not list the `*_dim` roles [S-L01-004]. That is a documentation gap to watch.
  - **User accent color (macOS).** An app accent applies when the system setting is "multicolor"; otherwise the user's chosen accent replaces it, except fixed-color sidebar icons [S-L01-013].
  - **Content-tinted materials (Apple Liquid Glass, 2025).** "By default, Liquid Glass has no inherent color, and instead takes on colors from the content directly behind it." Color can be applied as a tint for emphasis (prominent buttons get the app accent in the background); apply color sparingly; symbols and text on small glass elements switch light/dark monochrome automatically [S-L01-013] (HIG color page change log: Liquid Glass guidance updated 16 Dec 2025).
  - **Icon appearance modes (Apple).** Default, dark, clear light, clear dark, tinted light, tinted dark on iOS, iPadOS and macOS. The system generates missing variants; clear and tinted are "even more" subdued [S-L01-015]. On Android, adaptive icons (13+) and widgets (12+) follow dynamic color [S-L01-058].
- **Visual effect:** Dynamic color makes the app feel personal and native to the device but dilutes brand recognition (the brand hue may not appear at all; MCU Expressive rotates hue [S-L01-010]). Static color maximizes brand consistency. Glass tinting yields a lighter, content-forward UI where the brand shows mainly on the primary action [S-L01-013] [inferred for the brand-dilution reading].
- **Depends on (upstream):** brand strictness (L06); platform (Android/iOS); role taxonomy (pairing roles are required for dynamic schemes, DC-L01-11).
- **Affects (downstream):** which tokens are "fixed" (brand, error, Material `*-fixed` roles) vs dynamic; harmonization of static colors (DC-L01-09); icon assets (L05); materials and translucency (L04).
- **Token encoding:** dynamic roles resolve at runtime, so the token set stores roles plus the generator recipe (source, variant, spec version, contrast level). Fixed colors are separate tokens. Harmonized statics are flagged, e.g. `$extensions.harmonize: true` [inferred].
- **Platform notes:** Android: `DynamicColors.applyToActivitiesIfAvailable()` and the `ThemeOverlay.Material3.DynamicColors.DayNight` theme [S-L01-058]. iOS/macOS: provide light and dark variants even for single-appearance apps so Liquid Glass can adapt [S-L01-013]. Web: no OS wallpaper API; runtime MCU (TypeScript) can generate schemes from an image or user color [S-L01-008].
- **Accessibility constraints:** dynamic schemes keep contrast only if components use the intended role pairs; mismatched pairs break legibility "when colors are adjusted through dynamic color features such as user-controlled contrast" [S-L01-004]. On glass, avoid similar colors in control labels over colorful backgrounds [S-L01-013].
- **Default + heuristic:** Default to static brand color with optional dynamic color on Android (behind a user setting) and accent-only tinting on Apple glass. Heuristic: let dynamic color own surfaces and secondary accents; keep brand-critical and status colors fixed and harmonized.
- **Evidence:** [S-L01-004, S-L01-006, S-L01-008, S-L01-010, S-L01-011, S-L01-013, S-L01-015, S-L01-058]

### DC-L01-22: Contrast standard, target level and enforcement method
- **Block path:** Foundations > Color > Accessibility > Contrast
- **Questions the designer answers:** Which standard do we promise (WCAG 2.2 AA, AAA, APCA)? How do we guarantee it: per-pair tests, step-distance rules, or generator targets? Which elements are exempt?
- **Options:**
  - **WCAG 2.2 AA (the enforceable baseline).** 1.4.3 text 4.5:1, large text (18pt, or 14pt bold, about 24px / 18.66px) 3:1; no rounding (4.499:1 fails); logos, decorative and inactive text exempt [S-L01-022]. 1.4.11 UI components and meaningful graphics 3:1 against adjacent colors [S-L01-023]. Atlassian and Carbon state these rules in their color docs (4.5:1 below 24px, 3:1 at 24px and above and for UI) [S-L01-030, S-L01-029].
  - **WCAG 2.2 AAA.** 1.4.6 text 7:1, large text 4.5:1 [S-L01-025]. Used as the target for high-contrast themes (Primer 7:1 [S-L01-027]; Material high contrast 7:1 [S-L01-006]); Apple asks to "strive for" 7:1 for custom colors, especially small text [S-L01-014].
  - **APCA (secondary check).** Lc 90 preferred body text, Lc 75 body minimum, Lc 60 other content text, Lc 45 headlines and large text, Lc 30 absolute minimum (placeholder, disabled), Lc 15 non-text minimum [S-L01-026]. Radix guarantees Lc 60 (step 11) and Lc 90 (step 12) on step 2 [S-L01-002]. Status: WCAG 3.0 is a Working Draft (10 Sep 2026); its text contrast requirement reads "@@[contrast measure to be determined]", APCA is not named, and the group expects "several years of work" [S-L01-021]. APCA is therefore not a conformance target today.
  - **Enforcement by construction.** Step-distance rules (Carbon's table: e.g. from 100, grades 50 through White pass 4.5:1; Stripe: 5 levels apart = 4.5:1, 4 apart = 3:1) [S-L01-029, S-L01-044]; contrast-targeted generation (Leonardo, Spectrum) [S-L01-040, S-L01-036]; role pairing with contrast curves (Material; `on_surface` contrast targets 4.5 / 7 / 11 / 21 by contrast level) [S-L01-010].
- **Visual effect:** AA allows mid-gray secondary text and softer brand tints, giving a lighter, airier feel. AAA forces darker secondary text and deeper accents, which feels heavier and starker. Designing to APCA tends to allow lighter body text on white at large sizes and demands more contrast for thin small text [S-L01-026] [inferred for the aesthetic readings].
- **Depends on (upstream):** legal market (EU/US typically reference WCAG 2.x AA) [inferred]; audience; typography weights and sizes (L02: large-text thresholds depend on size and weight).
- **Affects (downstream):** every text/background and UI/background token pair; ramp generation (DC-L01-03); brand adaptation (DC-L01-09); disabled and placeholder styling.
- **Token encoding:** record intended pairs so CI can test them, e.g. `$extensions.contrast = { against: "{color.bg.default}", min: 4.5 }` [inferred]; no DTCG-native contrast field exists [S-L01-018].
- **Platform notes:** Apple: minimum 4.5:1, strive for 7:1 [S-L01-014]. Material role pairs guarantee at least 3:1, with medium and high contrast levels available [S-L01-004, S-L01-006].
- **Accessibility constraints:** these are the constraints. Disabled components are exempt from both 1.4.3 and 1.4.11 [S-L01-022, S-L01-023].
- **Default + heuristic:** Default to WCAG 2.2 AA for all pairs, AAA for high-contrast modes, and APCA as an advisory lint on body text. Heuristic: test tokens as pairs, in every mode, at build time. Never "eyeball" a single color.
- **Evidence:** [S-L01-002, S-L01-004, S-L01-006, S-L01-010, S-L01-014, S-L01-018, S-L01-021, S-L01-022, S-L01-023, S-L01-025, S-L01-026, S-L01-027, S-L01-029, S-L01-030, S-L01-036, S-L01-040, S-L01-044]

### DC-L01-23: Color independence and color-vision-deficiency safety
- **Block path:** Foundations > Color > Accessibility > Not color alone
- **Questions the designer answers:** Where does color carry meaning (links, errors, status, charts, selection)? What is the redundant cue? Do we ship colorblind-specific themes?
- **Options:**
  - **Redundant cues everywhere.** 1.4.1: color must not be "the only visual means of conveying information" [S-L01-024]. Links distinguished by color alone need 3:1 against surrounding text plus a non-color cue on hover/focus (technique G183) [S-L01-024]. Apple: use text labels or glyph shapes [S-L01-013]. Spectrum: semantic color must be accompanied by text or an icon [S-L01-036].
  - **Colorblind-safe hue choices.** Spectrum's categorical palette "ensures the highest degree of identifiability of colors for various color vision deficiencies" [S-L01-036]. Carbon orders categorical colors to "maximize contrast between neighboring colors" [S-L01-056].
  - **Dedicated CVD themes.** Primer protanopia-deuteranopia and tritanopia themes remap success/danger hues [S-L01-050].
- **Visual effect:** Redundant cues (icons, underlines, patterns) add visual density but make meaning robust; underlined links look more "document-like" and less minimal [inferred]. CVD themes change the brand look (e.g. blue success buttons) only for users who opt in [S-L01-050].
- **Depends on (upstream):** status set (DC-L01-15); data-viz palettes (DC-L01-24); link styling (L02/L08).
- **Affects (downstream):** link styles, form validation, status badges, charts (patterns, direct labels), selected states in lists and tables.
- **Token encoding:** CVD modes as Resolver contexts (`vision: protan-deutan`) [S-L01-019]; icon tokens paired with status colors (L05).
- **Platform notes:** Apple notes cultural color meaning (red/green in stock apps varies by locale) [S-L01-013].
- **Accessibility constraints:** about 1 in 12 men have a color vision deficiency, red-green most commonly [S-L01-060]; 1.4.1 is Level A [S-L01-024].
- **Default + heuristic:** Default: every color-coded meaning gets an icon, text or shape; links in body text are underlined. Heuristic: test with red-green and blue-yellow simulation; if two meanings differ only in hue, add a second channel.
- **Evidence:** [S-L01-013, S-L01-019, S-L01-024, S-L01-036, S-L01-050, S-L01-056, S-L01-060]

### DC-L01-24: Data-visualization color (summary; L05 owns depth)
- **Block path:** Foundations > Color > Data visualization
- **Questions the designer answers:** How many distinct series colors? Are they drawn from the UI palette? Which sequential and diverging ramps? Do chart colors change in dark mode?
- **Options:**
  - **Categorical, ordered sequence.** Carbon: 14 colors applied strictly in order (Purple 70 #6929c4, Cyan 50 #1192e8, Teal 70 #005d5d, Magenta 70 #9f1853, Red 50 #fa4d56, Red 90 #570408, Green 60 #198038, Blue 80 #002d9c, Magenta 50 #ee538b, Yellow 50 #b28600, Teal 50 #009d9a, Cyan 90 #012749, Orange 70 #8a3800, Purple 50 #a56eff), with fixed small-group palettes when the count is known [S-L01-056]. Atlassian `color.chart.categorical.1-8` with `.hovered` [S-L01-032]. Primer 17 data hues x emphasis/muted [S-L01-067]. Spectrum's categorical palette is a subset of its colors [S-L01-036].
  - **Sequential (monochromatic).** Carbon Blue/Purple/Cyan/Teal 10-100; in light themes the darkest is the largest value, in dark themes the lightest [S-L01-056].
  - **Diverging.** Carbon red-cyan (temperature) and purple-teal (no temperature association); these do not change between light and dark [S-L01-056].
  - **Alert palette.** Carbon Red 60, Orange 40, Yellow 30, Green 60 for status in charts [S-L01-056].
- **Visual effect:** Chart palettes drawn from the UI ramps look native to the product. Separate, higher-chroma chart palettes make dashboards pop but can clash with the UI. Long categorical sequences (14 colors) invite illegible charts; a small group palette looks cleaner [inferred].
- **Depends on (upstream):** hue set and ramps (DC-L01-02/03); CVD safety (DC-L01-23); dark mode (DC-L01-18).
- **Affects (downstream):** chart components, legends, maps, heatmaps (L05).
- **Token encoding:** `color.chart.categorical.{1..n}`, `color.chart.sequential.{name}.{step}`, `color.chart.diverging.{name}.{step}`, each with per-mode values [S-L01-032].
- **Platform notes:** platform-neutral; Apple suggests wide color for data and status indicators on P3 displays [S-L01-013].
- **Accessibility constraints:** chart lines and marks needed for understanding require 3:1 against adjacent colors (1.4.11) [S-L01-023]; color must not be the only encoding (1.4.1) [S-L01-024].
- **Default + heuristic:** Default to 6-8 categorical colors ordered for neighbor contrast, one sequential and one diverging ramp per mode. Heuristic: if you need more than 8 categories, switch to direct labeling or grouping rather than more hues.
- **Evidence:** [S-L01-013, S-L01-023, S-L01-024, S-L01-032, S-L01-036, S-L01-056, S-L01-067]

### DC-L01-25: Gradients and expressive/brand color use (summary)
- **Block path:** Foundations > Color > Expressive color > Gradients and illustration
- **Questions the designer answers:** Are gradients part of the brand language or banned from the UI? In which color space are gradients interpolated? Do illustrations use the UI palette?
- **Options:**
  - **No gradients in functional UI; gradients reserved for brand moments** [inferred as common practice]. Carbon permits gradients in data viz only for single-category extremes, "never ... in place of a sequential palette" [S-L01-056].
  - **Perceptual interpolation.** Tailwind v4 interpolates gradients in `oklab` by default, with `/srgb`, `/hsl`, `/oklch`, `/longer` etc. modifiers [S-L01-066]. Interpolating in sRGB between complementary hues produces a gray "dead zone" midway; OKLab avoids it [inferred].
  - **Wide-gamut gradients.** P3 gradients can clip on sRGB displays; supply per-gamut variants [S-L01-013].
  - **Icon and illustration backgrounds.** Apple Icon Composer supports solid colors and gradients for icon background layers, and gradients should "respond well to system lighting effects" [S-L01-015].
- **Visual effect:** Gradients add energy, depth and "brand moment" warmth (consumer, AI and creative products), but in dense UIs they reduce clarity and compete with status color [inferred]. OKLab/OKLCH gradients look smoother and more vivid midway than sRGB [inferred].
- **Depends on (upstream):** brand identity (L06); chroma level (DC-L01-10); gamut (DC-L01-05).
- **Affects (downstream):** hero sections, marketing surfaces, illustrations, empty states, app icons (L05).
- **Token encoding:** DTCG 2025.10 defines a composite `gradient` type, an array of stops each with `color` and `position` [S-L01-068]. Stops should alias color primitives. DTCG has no field for the interpolation color space, so record it in `$extensions` [inferred].
- **Platform notes:** CSS supports `in oklab` / `in oklch` interpolation in gradients (Tailwind exposes these) [S-L01-066]; Apple icons use gradient backgrounds in Icon Composer [S-L01-015].
- **Accessibility constraints:** text over a gradient must meet 4.5:1 at its lowest-contrast point [inferred from S-L01-022].
- **Default + heuristic:** Default: no gradients on interactive components; allow brand gradients on marketing and illustration surfaces, interpolated in OKLab. Heuristic: if a gradient carries data meaning, use a sequential palette instead [S-L01-056].
- **Evidence:** [S-L01-013, S-L01-015, S-L01-022, S-L01-056, S-L01-066, S-L01-068]

### DC-L01-26: Color token architecture, tiers and mode handling
- **Block path:** Foundations > Color > Tokens > Architecture
- **Questions the designer answers:** How many token tiers? Can product teams use primitives directly? How are light, dark and other modes expressed? Which file format?
- **Options:**
  - **Three tiers: base, functional, component (Primer).** "Base tokens ... never used directly in code or design"; functional tokens respect color modes; component tokens (e.g. `focus-outlineColor`) are for specific cases [S-L01-027].
  - **Two tiers: global and alias (Fluent).** Each palette value is a "context-agnostic global token"; alias tokens add context [S-L01-033]. E.g. `colorBrandBackground` -> brand80 in light and brand70 in dark [S-L01-034].
  - **Core and component tokens (Carbon).** 10 core groups plus component tokens (button, tag, notification) that "should never be used for anything other than their own component"; roles never change between themes, values do [S-L01-029].
  - **Semantic-only public API (Atlassian, Apple).** Designers pick tokens, not palette values [S-L01-030]; Apple says don't hard-code system color values [S-L01-013].
  - **Tier chain example (builder default):** `color.blue.500` (primitive) -> `color.bg.accent.bold` (semantic) -> `button.primary.bg` (component) [inferred; mirrors Primer `bgColor-accent-emphasis` = `{base.color.blue.5}` [S-L01-050]].
- **Mode handling options:**
  - **DTCG Resolver (stable 2025.10).** Sets plus modifiers with named contexts (e.g. `theme: light|dark`) and a resolution order [S-L01-019]. The Format module itself defines no modes [S-L01-068].
  - **Per-token overrides in `$extensions`.** Primer `org.primer.overrides` with keys such as `dark`, `dark-dimmed`, `light-high-contrast` [S-L01-050].
  - **Separate theme files per mode.** Carbon themes; Radix light/dark CSS files [S-L01-029, S-L01-052].
  - **CSS runtime.** Tailwind `@theme` custom properties, with a `[data-theme="dark"]` override example [S-L01-001]; `light-dark()` [S-L01-047].
- **Value format:** DTCG 2025.10 color `$value` is an object `{colorSpace, components, alpha?, hex?}` with 14 color spaces; plain hex strings are not valid `$value`s [S-L01-018]. Primer already stores `{colorSpace: 'hsl', components: [137.1, 62.9, 32.7], hex: '#1f883d'}` [S-L01-050]. A newer DTCG draft (8 Sep 2026) is in progress and marked "do not implement" [S-L01-016].
- **Visual effect:** none directly; tiers decide how safely the look can change (rebrand, new mode) without regressions [inferred].
- **Depends on (upstream):** all color decisions above; tooling (Style Dictionary, Tokens Studio, Terrazzo named as DTCG reference implementations [S-L01-017]).
- **Affects (downstream):** Figma variables and collections (L07); code outputs; governance (L11).
- **Token encoding:** example DTCG primitive:
  `{"color":{"blue":{"500":{"$type":"color","$value":{"colorSpace":"oklch","components":[0.623,0.214,259.815],"hex":"#2b7fff"}}}}}` (OKLCH components from Tailwind blue-500 [S-L01-062]; hex computed in this lane, where the blue channel exceeds sRGB and is clipped, so the hex is an approximation [S-L01-069])
  and semantic alias `{"color":{"bg":{"accent":{"bold":{"$type":"color","$value":"{color.blue.500}"}}}}}` [S-L01-018].
- **Platform notes:** DTCG output targets iOS, Android, web and Flutter via generators [S-L01-017].
- **Accessibility constraints:** mode coverage must include every accessibility mode offered (DC-L01-20).
- **Default + heuristic:** Default to three tiers, with primitives private, semantics public and component tokens optional, stored as DTCG 2025.10 with the Resolver for modes. Heuristic: create a component token only when a component must diverge from its semantic role.
- **Evidence:** [S-L01-001, S-L01-013, S-L01-016, S-L01-017, S-L01-018, S-L01-019, S-L01-027, S-L01-029, S-L01-030, S-L01-033, S-L01-034, S-L01-047, S-L01-050, S-L01-052, S-L01-062, S-L01-068, S-L01-069]

### DC-L01-27: Transparent (alpha) colors
- **Block path:** Foundations > Color > Primitives > Alpha colors
- **Questions the designer answers:** Do hover fills, borders and overlays need to work on any background (images, colored panels)? Do we define translucent tokens, or compute opacity at runtime?
- **Options:**
  - **Alpha ramps mirroring solid ramps.** Radix `--blue-a1..a12` (e.g. `#0080ff04`) plus `blackA` and `whiteA` [S-L01-052].
  - **Alpha neutrals only.** Atlassian Neutral100A-500A and DarkNeutral alpha steps; "transparency helps UI adapt to different background colors and elevations" [S-L01-031, S-L01-030].
  - **Transparent white/black sets for use over media.** Spectrum's 8 values; white on backgrounds under 50% lightness, black above; only for components that support a transparent option [S-L01-036].
  - **Runtime opacity.** Tailwind `bg-blue-500/50` compiles to `color-mix(in oklab, var(--color-blue-500) 50%, transparent)` [S-L01-045]; Material state layers are content color at fixed opacity [S-L01-005].
- **Visual effect:** Alpha colors let hover, selection and borders pick up the underlying surface, so they look integrated on tinted or elevated surfaces and over photos; the overall look is softer and more "glassy". Solid colors look crisper and are more predictable [S-L01-030] [inferred for the aesthetic readings].
- **Depends on (upstream):** surface model (DC-L01-13); state method (DC-L01-17); materials/translucency (L04).
- **Affects (downstream):** hover and pressed fills, dividers, scrims (`color.blanket`), skeletons, overlays on media, avatars.
- **Token encoding:** DTCG `alpha` field: `{"colorSpace":"srgb","components":[0,0.5,1],"alpha":0.016}` [S-L01-018]; naming `color.blue.a3` or `color.neutral.200A`.
- **Platform notes:** macOS: add some transparency to custom component backgrounds in neutral states so they pick up desktop tinting [S-L01-014]; Liquid Glass supplies its own translucency [S-L01-013].
- **Accessibility constraints:** contrast of translucent text or borders depends on what is behind them; test against every surface they can appear on, or avoid alpha for text [inferred from S-L01-022, S-L01-023].
- **Default + heuristic:** Default to alpha neutrals (4-5 steps) for hover, borders and scrims, and solid colors for text. Heuristic: use alpha when the background is variable; use solid when the pair must be contrast-certified.
- **Evidence:** [S-L01-005, S-L01-013, S-L01-014, S-L01-018, S-L01-022, S-L01-023, S-L01-030, S-L01-031, S-L01-036, S-L01-045, S-L01-052]

## Decision graph (what drives what, for S1)

Order of decisions, upstream first. Each arrow names the card that carries the dependency.

1. **Brand inputs (L06)** feed accent count (DC-08), brand-to-UI adaptation (DC-09), chroma level (DC-10) and neutral tint (DC-06).
2. **Platform targets (L10)** decide the color space and tooling (DC-01, DC-04: HCT/MCU if Android dynamic color matters), dynamic color (DC-21) and the gamut (DC-05).
3. **Contrast target (DC-22)** constrains step semantics (DC-03), brand adaptation (DC-09), text hierarchy (DC-14), borders and focus (DC-16) and every mode (DC-18 to DC-20).
4. **Color space (DC-01)**, together with the contrast target, decides **step semantics (DC-03)**. Step semantics decide **step count and naming (DC-02)**, which then set the primitive token names (DC-26).
5. **Primitives (DC-02/03/06/07/27)** feed the **semantic roles (DC-11)**, which set the **emphasis levels (DC-12)**, **surfaces (DC-13)**, **foregrounds (DC-14)**, **status colors (DC-15)** and **borders and focus (DC-16)**.
6. **Semantic roles** drive the **state method (DC-17)** (overlays if colors are unknown, step shifts if known), the **dark mapping (DC-18)** and **dark base (DC-19)**, and the **accessibility modes (DC-20)**.
7. **Status colors and data viz (DC-15, DC-24)** both depend on **CVD safety (DC-23)**.
8. **Everything** ends in **token architecture (DC-26)**: DTCG 2025.10 objects, Resolver modifiers for modes, then Figma variables and code (L07).

**High-leverage visual levers** (the few inputs that change the look the most, for the builder's questionnaire):

| Lever | Low setting looks like | High setting looks like | Cards |
|---|---|---|---|
| Accent chroma | calm, serious, enterprise | energetic, consumer, playful | DC-10 |
| Neutral tint | technical, content-first | warm or cool branded atmosphere | DC-06 |
| Accent count | focused, single-action clarity | expressive, categorical richness | DC-08 |
| Surface layering | flat, border-defined | soft zones, tonal depth | DC-07, DC-13 |
| Dark base darkness | charcoal comfort (#262626-#292929) | near-black drama (#0D1117-#161616, tone 4) | DC-19 |
| Emphasis levels | punchy two-level (tint/solid) | nuanced subtlest-to-boldest | DC-12 |
| Dynamic color | brand-locked | device-personal | DC-21 |

The "looks like" readings in this table are [inferred] from the card evidence; the value ranges are sourced in the cards.

## Community reconciliation (L00)

- `sources/COMMUNITY-SIGNAL.md` (read 2026-09-23) has no color-specific section yet. It confirms DTCG 2025.10 is stable and flags "draft" DTCG articles as stale, which matches DC-26 [S-L01-070, S-L01-017].
- L00's raw Material 3 Expressive pull (Tier C) has practitioners recommending Material Theme Builder for palettes, and a single-source claim that web, Flutter and React Native lack M3 Expressive support [S-L01-071]. That claim fits a verifiable fact: the material-web token set (v0.192) still ships pre-revision state-layer values (focus/pressed 0.12) while Compose uses 0.1 [S-L01-064, S-L01-065]. Builder implication: M3 Expressive color behavior is reliably available only through MCU (spec 2025) and native Android/Compose today [inferred].
- No community source disputed any value used here. A MaterialKolor README claim that "creating low contrast themes is no longer possible" under the 2025 spec was not independently verified and is not used [S-L01-009].

## Open questions / gaps

1. **Spectrum 2** color (the successor to the Spectrum v6 palette cited here) was not reachable (s2.spectrum.adobe.com returned 403 / AccessDenied at the URL tried) [S-L01-037]. The contrast-indexed approach is confirmed for Spectrum v6 colors only.
2. **Polaris current docs:** Polaris React is archived and its design docs redirect to shopify.dev web-component references. Polaris color values here come from the archived token source (historical) [S-L01-038, S-L01-039]. The current Polaris web-component color tokens were not examined.
3. **Material 3 Expressive documentation:** the `*_dim` roles and the 2025/2026 spec behaviors exist in MCU code [S-L01-010] but are not on the M3 roles page [S-L01-004]. What the 2026 spec changes versus 2025 was not analyzed (the file exists; its diff was not studied).
4. **Android wide-gamut UI color** (Compose `ColorSpaces.DisplayP3`) was not verified.
5. **Figma support** for DTCG color objects and color spaces (e.g. whether Figma variables store OKLCH or P3) is L07's to verify.
6. **Apple exact system color values** are shown only as swatches on the HIG page and "may fluctuate" [S-L01-013]; no hex values were taken.
7. **Personality mappings** (e.g. "warm neutrals feel friendly") are practitioner consensus, not experimentally sourced here; all are tagged [inferred]. A research-backed source on color-emotion associations in UI would strengthen DC-06, DC-10 and DC-19 (L06 may have one).
8. **Material Theme Builder feature and export list** could not be read (the app renders client-side) [S-L01-072].
9. **Primer dark-dimmed neutral hex values** were not extracted (only that `bgColor-default` maps to `neutral.3` and that white softens to #cdd9e5) [S-L01-050].

## Confidence

**Confirmed against live Tier A sources today (2026-09-23):**
- Tailwind 4.3.3: 11 steps, 26 families, 9 neutrals with exact OKLCH values [S-L01-001, S-L01-062].
- Radix: 12-step purposes, APCA Lc 60/90 guarantees, P3 and alpha files, 6 grays [S-L01-002, S-L01-052, S-L01-053].
- Material 3: 26 roles, tonal palettes, contrast levels, HCT; state layers 8/10/10/16% (site and Compose); 2021/2025 spec tones and chroma from MCU source [S-L01-004, S-L01-005, S-L01-006, S-L01-010, S-L01-065].
- Carbon: themes, hex values, layering, state step rules, contrast step table, data-viz palettes [S-L01-029, S-L01-056].
- Atlassian: token grammar, ramps, dark symmetry, 464 token names [S-L01-030, S-L01-031, S-L01-032].
- Spectrum v6: contrast-indexed steps and gray usage bands [S-L01-035, S-L01-036].
- Fluent 2: palettes, brand ramp 10-160, alias mappings [S-L01-033, S-L01-034].
- Primer: token grammar, neutral usage bands, theme list, colorblind remaps, DTCG storage [S-L01-050, S-L01-067, S-L01-073]. The docs say "nine themes"; the primitives source carries override keys for 14 variants, including high-contrast versions of the colorblind themes, which suggests the nine are the user-facing set [S-L01-073, S-L01-050] [inferred for the reconciliation].
- Radix step purposes, APCA guarantees and gray pairings were re-verified in a browser after a WebFetch summary added an unsupported gloss, which was removed [S-L01-074, S-L01-075].
- Apple HIG: color (Liquid Glass, updated 16 Dec 2025), dark mode, app icon appearances (updated 8 Jun 2026) [S-L01-013, S-L01-014, S-L01-015].
- DTCG 2025.10 stable (color, format, resolver) [S-L01-017, S-L01-018, S-L01-019, S-L01-068].
- WCAG 2.2 SC values [S-L01-022 to S-L01-025, S-L01-059]; WCAG 3 Working Draft of 10 Sep 2026 [S-L01-021].
- MDN baseline dates for oklch, light-dark, forced-colors, color-gamut [S-L01-046 to S-L01-049].

**Tier B, used with corroboration:** APCA thresholds (method author; not a W3C standard) [S-L01-026]; the Stripe 2019 step rule (corroborated by Carbon's table) [S-L01-044]; the Android Authority M3E quote (corroborated by MCU code) [S-L01-011].

**Inferred (tagged in text):** all personality and "looks like" readings; recommended defaults and heuristics; the builder-specific token examples (`$extensions.contrast`, generator metadata); the claim that no major system ships pure inversion (based on the systems surveyed); the gradient dead-zone explanation.

**Known inconsistency surfaced:** Material state-layer focus/pressed values differ between the M3 site and Compose (0.10) and material-web tokens (0.12) [S-L01-005, S-L01-064, S-L01-065]. The site and Compose are treated as current.

## Cross-lane notes

- [L01 -> L04] Material 3 surface roles are "not tied to elevation"; tonal difference is the default separator. Dark-mode depth: Carbon lightens one step per layer; M2 used white overlays of 0-16% by dp; Apple uses base vs elevated backgrounds. Liquid Glass "has no inherent color" and takes color from content behind it [S-L01-054, S-L01-029, S-L01-055, S-L01-014, S-L01-013].
- [L01 -> L05] Data-viz palettes are summarized in DC-L01-24 (Carbon 14-color categorical order, sequential/diverging, alert palette; Atlassian chart.categorical 1-8; Primer 17 data hues). Apple icon appearances: default, dark, clear light/dark, tinted light/dark [S-L01-056, S-L01-032, S-L01-067, S-L01-015].
- [L01 -> L06] The brand-to-UI color translation is DC-L01-09 (brand hex as ramp anchor; Material color fidelity and harmonize; Polaris uses near-black as "brand" fill). L06's personality attributes should map to DC-L01-10 (chroma), DC-L01-06 (neutral tint) and DC-L01-08 (accent count).
- [L01 -> L07] DTCG 2025.10 color `$value` must be an object {colorSpace, components, alpha?, hex?} (14 spaces), not a hex string. Primer already stores tokens this way and uses `$extensions["org.primer.overrides"]` for per-theme values. The Resolver module (sets, modifiers, contexts) is the stable way to express light/dark/high-contrast/CVD modes. A newer DTCG color draft (8 Sep 2026) exists, marked "do not implement". Tailwind v4 blue-500 is outside sRGB, so exporters need a gamut-mapping policy [S-L01-018, S-L01-050, S-L01-019, S-L01-016, S-L01-069].
- [L01 -> L08] Component state colors: Material state layers (hover 8%, focus 10%, pressed 10%, dragged 16%; disabled container 12%, content 38%) vs Carbon step shifts (hover half step, active two steps, selected one step) vs Fluent (darker on interaction; Windows reverses) [S-L01-005, S-L01-064, S-L01-029, S-L01-033]. The focus indicator must be 3:1 (1.4.11) [S-L01-023].
- [L01 -> L09] Benchmark values for the matrix: ramp steps (Tailwind 11, Radix 12, Carbon 10+B/W, Spectrum grays 11 and hues 100-1300 on the palette page (the docs say 14 tints and shades), Atlassian 12 hue steps, Fluent brand 16, Polaris 16, Primer 10 hue/14 neutral); dark bases (Carbon #161616/#262626, Primer #0D1117, Fluent #292929, M2 #121212, M3 tone 6 or 4).
- [L01 -> L10] Platform color APIs: Apple dynamic system colors (label, secondaryLabel, systemBackground, ...), macOS user accent override, Liquid Glass tinting; Android dynamic color since Android 12 (variants added in 13), `DynamicColors.applyToActivitiesIfAvailable()`, HarmonizedColors; web `light-dark()`, `forced-colors`, `color-gamut` [S-L01-013, S-L01-058, S-L01-047, S-L01-048, S-L01-049].
- [L01 -> L02] Contrast thresholds depend on type size and weight (WCAG large text: 18pt, or 14pt bold, about 24px / 18.66px; APCA Lc tables vary by px and weight). Typography tokens need the size/weight data for contrast checks [S-L01-022, S-L01-026].
- [L01 -> L11] Tooling trend: Adobe published `@adobe/leonardo-mcp` (0.1.0, Feb 2026), an MCP server for contrast-based color generation. Relevant to AI/MCP-driven design-system workflows [S-L01-040].
