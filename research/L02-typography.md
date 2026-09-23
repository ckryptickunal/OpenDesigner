# L02: Typography

Lane: L02 (Typography). Author: orchestrator subagent L02. Started 2026-09-23.
Status: complete (28 Decision Cards). Trace: `traces/L02-trace.md` (every source, including rejected ones). Schema: `_coordination/SCHEMA.md`.

## Lane overview

Typography breaks into six layers that a builder should ask about in this order. Each layer constrains the next.

1. **Typeface** (DC-01 to DC-06): where the font comes from (system, brand, open source), what class it is (neo-grotesque, geometric, humanist, serif, slab, mono), how many families, whether it is variable (weight, optical size, grade), and how it is licensed and loaded.
2. **Roles and scale** (DC-07 to DC-12): how styles are named (role x size, t-shirt, numbered), the base body size, the method that generates sizes (ratio, formula, hand-tuned), how many steps, whether there is a separate expressive set, and how emphasis works.
3. **Metrics** (DC-13 to DC-18): line height and grid snapping, tracking, weights, paragraph spacing, line length, alignment/casing/truncation.
4. **Responsive and platform** (DC-19, DC-20): fixed vs stepped vs fluid sizes, and per-platform scales and minimums.
5. **Accessibility** (DC-21 to DC-23): text scaling (Dynamic Type, Android 200%, browser zoom), text-spacing robustness and legibility, and contrast linkage with color.
6. **Internationalization and encoding** (DC-24 to DC-28): script coverage and fallbacks (Indic, CJK, Arabic), script-specific metrics, numerals, the token architecture (DTCG typography composite) and the Figma encoding.

Five findings matter most for the builder:

- **The two ratio-based systems really are ratio-based, and it shows what "scale contrast" means.** Material's sizes are 14 x 1.125^n rounded (16, 22, 28, 32, 36, 45, 58; Material ships 57, and 24, each off-formula by 1 [S-V1b-025]), and Spectrum 2's desktop and mobile ramps are exactly 14 x 1.125^n and 17 x 1.125^n rounded [computed from S-L02-005, S-L02-021]. Carbon uses an additive formula, and everyone else hand-tunes on a 2px or 4px grid. A builder can therefore generate a credible scale from three inputs (base, ratio, rounding grid) and let people hand-adjust afterwards.
- **Body size encodes density.** Dense web products converge on 14px body with 20px line height (Material, Fluent, Carbon productive, Atlassian, Primer, Spectrum desktop). Reading and mobile surfaces use 16-17 (Apple Body 17pt, Spectrum mobile 17px, Carbon expressive 16px) [S-L02-001] [S-L02-005] [S-L02-007] [S-L02-011] [S-L02-015] [S-L02-017] [S-L02-021]. "Density" in L03 and "base size" here should be one linked control.
- **Expressive vs productive is a real, documented split.** Carbon has two type sets (14px fixed vs 16px fluid) [S-L02-011]. Material 3 Expressive added 15 "emphasized" styles, which use heavier weights on the same sizes [S-L02-006]. Apple's HIG added emphasized weights to its Dynamic Type specifications for every platform in December 2025 [S-L02-001]. The builder's "personality" slider should drive scale ratio, display weights, display tracking and line-height tightness together.
- **The DTCG 2025.10 typography composite is small.** It has only fontFamily, fontSize, fontWeight, letterSpacing and lineHeight (a number multiplier) [S-L02-032]. Paragraph spacing, text transform, font features (tabular numbers), variable axes (opsz, GRAD), per-breakpoint values and per-locale line heights all need `$extensions` or parallel tokens. Figma variables can bind size, weight, line height (number only), letter spacing (px only), paragraph spacing and family, but there is no composite typography variable [S-L02-036].
- **Script coverage decides whether a font can ship in India.** Google Sans Flex and Roboto Flex have no Devanagari or other Indic subsets [S-L02-026]. Material defines "language height" categories: Hindi, Bangla, Tamil and other Indic scripts need about 7% taller lines, Telugu about 30%, and Nastaliq about 100% [S-L02-006]. Letter spacing breaks Devanagari conjuncts and connected Arabic [S-L02-056] [S-L02-055]. An India-facing builder must check coverage, set a Noto/Kohinoor/Nirmala fallback, and use per-locale line heights with zero tracking for these scripts.

## Type scale comparison across systems

All values below come from each system's official docs or its official token source code, fetched 2026-09-23. Size/line-height in px (web), pt (Apple) or sp (Android); these are equivalent at 1x.

### Table 1: system-level parameters

| System | Default typeface(s) | Body default (size/line height) | Smallest style | Largest style | # named styles | How the scale was built | Weights used | Unit | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| Material 3 (baseline) | "Brand" + "Plain" typeface tokens; Roboto is the documented default for both; the m3.material.io token module shows Google Sans (display to title large) and Google Sans Text (title medium and below) | Body Medium 14/20 (Body Large 16/24) | Label Small 11/16 | Display Large 57/64 | 15 baseline + 15 emphasized (M3 Expressive) | Major Second (1.125) from base 14, then hand-rounded | 400 Regular, 500 Medium, 700 Bold (emphasized labels/titles) | sp (Android), rem = sp/16 (web) | [S-L02-005] [S-L02-006] |
| Apple iOS/iPadOS (Large = default Dynamic Type size) | SF Pro (variable, dynamic optical sizes), New York serif, SF Pro Rounded, SF Mono | Body 17/22 | Caption 2 11/13 | Large Title 34/41 | 11 text styles x 12 Dynamic Type sizes (xSmall..xxxLarge + AX1..AX5) | Hand-tuned per size; tracking varies per point size | Regular + Semibold (Headline); emphasized = Bold or Semibold | pt | [S-L02-001] |
| Fluent 2 Web | Segoe UI (web), Segoe UI Variable (Windows) | Body 1 14/20 | Caption 2 10/14 | Display 68/92 | 16 named styles (10 sizes x Regular/Strong/Stronger) | Hand-tuned: "Base" tokens 100-600 (10-24px) and "Hero" tokens 700-1000 (28-68px) | 400, 600 (Strong), 700 (Stronger); 500 exists as a token | px | [S-L02-007] [S-L02-008] |
| IBM Carbon (productive set) | IBM Plex Sans / Serif / Mono (open source) | body-01 14/20 (body-compact-01 14/18) | label-01 / legal-01 12/16 | heading-07 54/64 (fixed); fluid-display-04 reaches 156px at max breakpoint | about 30 tokens across utility, body, fixed heading, fluid heading, fluid display | Formula: Xn = Xn-1 + {INT[(n-2)/4]+1} x 2, starting at 12px; 23 steps 12..156 | 300 Light (large display), 400, 600 SemiBold | rem | [S-L02-009] [S-L02-011] [S-L02-012] |
| Shopify Polaris (tokens) | Inter, then system stack | text-body-md 13/20 | text-body-xs 11/12 | text-heading-3xl 36/48 | 11 (7 heading + 4 body) | Hand-tuned on a 4px-based size map (size-275 = 11px ... size-1200 = 48px) | 450 / 550 / 650 / 700 (variable Inter "in-between" weights) | px tokens | [S-L02-014] |
| Atlassian | Atlassian Sans + Atlassian Mono (app); Charlie Sans (brand/marketing) | font.body 14/20 | font.heading.xxsmall / font.body.small 12/16 | font.heading.xxlarge 32/36 | 7 heading + 3 body + 3 metric + 1 code | Hand-tuned; 2px/4px steps | Regular, Medium, Bold (all headings Bold) | rem | [S-L02-015] |
| GitHub Primer | Mona Sans VF first, then -apple-system, Segoe UI, Noto Sans, Helvetica, Arial | body medium 14 / 1.5 | caption 12 / 1.25 | display 40 / 1.375 | 9 roles (display, title L/M/S, subtitle, body L/M/S, caption) + codeBlock | 6 base sizes (12, 14, 16, 20, 32, 40) with 5 named unitless line heights (tight 1.25 ... loose 1.75) | 300, 400, 500 (display), 600 (titles) | rem | [S-L02-016] [S-L02-017] |
| Adobe Spectrum 2 | Adobe Clean Spectrum VF; Adobe Clean Serif; Adobe Clean Han (CJK) | body M 16/1.5 desktop (component base font-size-100 = 14px desktop / 17px mobile) | font-size-25 10px desktop / 12px mobile | font-size-1500 73px desktop / 88px mobile | 9 heading sizes (XXS..XXXXL), 7 body, 5 detail, code | Major Second (1.125), rounded; separate desktop and mobile "scale" sets (mobile about 1.2x desktop) | heading extra-bold; body regular, strong = bold; detail medium | px tokens per platform scale | [S-L02-020] [S-L02-021] |
| Fluent 2 Windows (Win 11) | Segoe UI Variable (wght 100-700, auto opsz 8-36pt) | Body 14/20 | Caption 12/16 | Display 68/92 | 9 | Hand-tuned; optical cuts "Small / Text / Display" | Regular, Semibold (no Bold, no Italic in ramp) | epx | [S-L02-022] [S-L02-007] |

### Table 2: the size ladder (font size / line height) for each system

Rows are grouped by role band. "-" means that system has no style in that band.

| Role band | Material 3 baseline [S-L02-005] | Apple iOS Large [S-L02-001] | Fluent 2 Web [S-L02-007] [S-L02-008] | Carbon productive [S-L02-011] | Polaris [S-L02-014] | Atlassian [S-L02-015] | Primer [S-L02-017] | Spectrum 2 desktop [S-L02-021] |
|---|---|---|---|---|---|---|---|---|
| Display / hero | Display L 57/64, M 45/52, S 36/44 | Large Title 34/41 | Display 68/92, Large Title 40/52 | heading-07 54/64, heading-06 42/50 (Light 300) | heading-3xl 36/48 | - | display 40/1.375 | heading XXXXL 73, XXXL 58, XXL 45 (line height 1.3) |
| Page heading | Headline L 32/40, M 28/36, S 24/32 | Title 1 28/34 | Title 1 32/40, Title 2 28/36, Title 3 24/32 | heading-05 32/40, heading-04 28/36 | heading-2xl 30/40, heading-xl 24/32 | xxlarge 32/36, xlarge 28/32, large 24/28 | title large 32/1.5 | heading XL 36, L 28 |
| Section heading | Title L 22/28 | Title 2 22/28, Title 3 20/25 | Subtitle 1 20/26 (site; token lineHeightBase500 = 28) | heading-03 20/28 | heading-lg 20/24 | medium 20/24 | title medium 20/1.625, subtitle 20/1.625 | heading M 22, S 20, XS 18 |
| Small heading / strong text | Title M 16/24 (500), Title S 14/20 (500) | Headline 17/22 (Semibold) | Subtitle 2 16/22 (600) | heading-02 16/24, heading-01 14/20 (600) | heading-md 14/20, heading-sm 13/20, heading-xs 12/16 (650) | small 16/20, xsmall 14/20, xxsmall 12/16 (Bold) | title small 16/1.5 (600) | heading XXS 14 |
| Body large | Body L 16/24 | Body 17/22 | Body 2 16/22 (token) | body-02 16/24 (expressive) | body-lg 14/20 | body.large 16/24 | body large 16/1.5 | body L 18, M 16 (line height 1.5) |
| Body default | Body M 14/20 | Callout 16/21, Subhead 15/20 | Body 1 14/20 | body-01 14/20, body-compact-01 14/18 | body-md 13/20 | body 14/20 | body medium 14/1.5 | body S 14 |
| Small / caption | Body S 12/16 | Footnote 13/18, Caption 1 12/16 | Caption 1 12/16 | label-01, helper-text-01, legal-01 12/16 | body-sm 12/16 | body.small 12/16 | body small 12/1.625, caption 12/1.25 | body XS 12 |
| Smallest / label | Label L 14/20, M 12/16, S 11/16 (all 500) | Caption 2 11/13 | Caption 2 10/14 | - | body-xs 11/12 | - | - | detail S 12, XS 11; font-size-25 10 |

### Table 3: what the comparison shows (patterns for the builder)

- **Body default clusters at 14px for dense web products** (Material Body Medium, Fluent Body 1, Carbon body-01, Atlassian font.body, Primer body medium, Spectrum 2 component base) and **16-17 for reading or mobile** (Material Body Large, Carbon expressive body-02, Spectrum 2 body M and mobile 17px, Apple Body 17pt) [S-L02-005] [S-L02-007] [S-L02-011] [S-L02-015] [S-L02-017] [S-L02-021] [S-L02-001]. Polaris's 13px body is the densest [S-L02-014].
- **Line heights snap to a grid**: every Material, Atlassian and Polaris line height is a multiple of 4 (12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 64); Fluent and Carbon snap to multiples of 2 (Fluent 14, 22, 26; Carbon 18, 22, 50). Apple uses odd leadings (13, 21, 25, 41) because it tunes per size rather than to a grid [S-L02-005] [S-L02-014] [S-L02-015] [S-L02-007] [S-L02-011] [S-L02-001]. Primer and Spectrum 2 express line height as unitless ratios (1.25-1.75; 1.3 headings / 1.5 body) [S-L02-017] [S-L02-021].
- **Line-height ratio shrinks as size grows**: roughly 1.4-1.5 at body sizes and 1.1-1.2 at display sizes (Material 57/64 = 1.12; Carbon fluid-display-04 92/102 = 1.11 and 1.05 at the max breakpoint; Fluent 68/92 = 1.35 is the outlier) [S-L02-005] [S-L02-009] [S-L02-007].
- **Only two published systems name a mathematical ratio**: Material (Major Second, 1.125) and Spectrum 2 (1.125, rounded). Carbon uses an additive formula. Everyone else hand-tunes [S-L02-006] [S-L02-020] [S-L02-012]. In practice every system rounds to whole pixels and usually to even numbers.
- **Number of sizes**: 8-11 distinct font sizes is the norm for a product UI (Material 11, Apple 10, Fluent 10, Polaris 8, Atlassian 7 + metric, Primer 6, Spectrum 2 up to 18 size tokens per platform) [inferred from the tables above].
- **Weight strategy splits into two camps**: size-led hierarchy with regular-weight headings (Material baseline, Carbon large headings at 300-400) versus weight-led hierarchy with bold/semibold headings at modest sizes (Atlassian all-Bold headings, Polaris 650, Spectrum 2 extra-bold, Fluent Semibold) [S-L02-005] [S-L02-011] [S-L02-015] [S-L02-014] [S-L02-021] [S-L02-007].

## Decision Cards

### DC-L02-01: Typeface sourcing strategy (system vs brand vs open-source)
- **Block path:** Foundations > Typography > Typeface > Sourcing
- **Questions the designer answers:** Should the product look native to each platform, or look like our brand everywhere? Can we afford to license and ship a custom font? Do we need the font on every platform, including Android, iOS, web and email?
- **Options:**
  - **Platform system fonts (native on each OS).** Apple: SF Pro (iOS/iPadOS/macOS/tvOS/visionOS), SF Compact (watchOS), New York (serif), SF Mono; Apple says use the system font constants and "don't embed system fonts in your app" [S-L02-001]. Android: Roboto is "the default typeface for Android" and the M3 default [S-L02-053]. Windows: Segoe UI Variable is "the new system font for Windows" [S-L02-022]. Fluent 2 deliberately uses native fonts per platform (Segoe UI on web and Windows, SF Pro on iOS/macOS, Roboto on Android) [S-L02-007]. On the web this is a stack such as `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...` (Fluent `fontFamilyBase`, Primer, Polaris fallbacks) [S-L02-008] [S-L02-017] [S-L02-014].
  - **Proprietary brand font.** Atlassian Sans + Atlassian Mono in-product, Charlie Sans for brand [S-L02-015]; Adobe Clean Spectrum VF [S-L02-021]; Google Sans / Google Sans Text in Google's own M3 token module [S-L02-006].
  - **Open-source brand or neutral font.** IBM Plex (Carbon, open source, downloadable from GitHub) [S-L02-012]; Mona Sans VF (Primer, first in stack) [S-L02-017]; Inter (Polaris) [S-L02-014]; Google Sans Flex, released as open source in 2025 (OFL) [S-L02-024] [S-L02-026]; Roboto Flex [S-L02-053].
- **Visual effect:** System fonts make the product feel native, neutral and "part of the OS"; the brand recedes and content leads. A brand font makes every screen recognizably yours, even in screenshots, but can feel slightly foreign next to OS chrome [inferred]. Open-source brand fonts (Plex, Inter, Mona Sans) give a consistent cross-platform look without license friction [inferred].
- **Depends on (upstream):** brand personality and how much distinctiveness is wanted (L06); platforms targeted (L10); languages/scripts required (DC-L02-24); budget and licensing.
- **Affects (downstream):** font-family tokens; fallback stacks; metric adjustments (line height, tracking) for every text style; Dynamic Type/font-scaling behaviour (custom fonts must re-implement it, see DC-L02-21); web performance budget (DC-L02-06); Figma library setup (fonts must be installed or available to every designer).
- **Token encoding:** DTCG `$type: "fontFamily"`, value is a string or an array (fallback stack) [S-L02-032] [S-L02-030]. Primitive: `font.family.brand = ["Mona Sans VF", "-apple-system", ...]`, `font.family.mono`. Semantic: `font.family.display`, `font.family.body`, `font.family.code` (Primer has `fontStack.sansSerifDisplay` which is "same as sansSerif but semantically distinct") [S-L02-017]. Material splits at the role level: `md.ref.typeface.brand` (display/headline/title large) and `md.ref.typeface.plain` (body/label) [S-L02-006].
- **Platform notes:** iOS/macOS: system fonts come with dynamic optical sizes, automatic tracking and Dynamic Type for free [S-L02-001]. Android: Roboto static is applied to all M3 components; Roboto Flex is "not yet part of the M3 typescale" [S-L02-053]. Windows: Segoe UI Variable's optical size is automatic in XAML; in HTML you must name Segoe UI Variable explicitly [S-L02-022]. Web: a brand font costs download time (DC-L02-06).
- **Accessibility constraints:** HIG: custom fonts must implement Dynamic Type and Bold Text behaviour themselves [S-L02-001]. Legibility checks for any font: distinct 1/I/l and 0/O/o [S-L02-049].
- **Default + heuristic:** Default to the platform system stack for productivity tools and internal apps; use one brand face (ideally open-source and variable) when brand recognition is a stated goal. Rule of thumb: if the product lives mostly inside another OS's chrome (native apps), go system; if it is mostly web and marketing-led, go brand.
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-007] [S-L02-008] [S-L02-012] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-024] [S-L02-026] [S-L02-030] [S-L02-032] [S-L02-049] [S-L02-053]

### DC-L02-02: Primary typeface classification (the personality choice)
- **Block path:** Foundations > Typography > Typeface > Classification
- **Questions the designer answers:** What should the product feel like: neutral and efficient, friendly and modern, warm and human, editorial and trustworthy, technical? Will the face be used for long reading or mostly short UI labels?
- **Options (genre/historical classes per Google Fonts Knowledge [S-L02-048]):**
  - **Neo-grotesque sans** (Helvetica lineage; Work Sans, Space Grotesk [S-L02-049]; Inter, SF Pro, Roboto are commonly described this way [inferred]). Used by Apple, Material, Polaris.
  - **Geometric sans** (circles, triangles, straight lines; DM Sans, Poppins, Raleway). Google warns the "repeating, similar shapes ... can hinder readability, making them less ideal for body text" [S-L02-049]. Google Sans descends from the geometric Product Sans [S-L02-024].
  - **Humanist sans** (pen-stroke influence; Merriweather Sans, Cabin [S-L02-049]; Segoe and IBM Plex Sans are often grouped here or as "grotesque-humanist hybrids" [inferred]).
  - **Serif**: humanist/old style (EB Garamond, Spectral), transitional/neoclassical [S-L02-049]. In systems: New York (Apple), Roboto Serif, IBM Plex Serif (Carbon quotations), Adobe Clean Serif [S-L02-001] [S-L02-053] [S-L02-011] [S-L02-021].
  - **Slab serif** (low contrast, serifs matching stroke weight) [S-L02-049]; rarely a primary UI face in the systems studied [inferred].
  - **Monospace** as a personality face (developer tools) rather than only for code [inferred].
- **Visual effect (conventional associations; these are cultural, change over time and vary by audience [S-L02-047]):** neo-grotesque = neutral, efficient, "invisible", corporate-modern; geometric = modern, friendly, optimistic, a bit fashionable, weaker in long text; humanist sans = warm, approachable, very legible at small sizes; serif = editorial, literary, trustworthy, established; slab = sturdy, confident, retro-industrial; mono = technical, raw, "for builders" [inferred from common practice; Google's own guidance only establishes that readers react emotionally first and that era/genre carries associations [S-L02-047] [S-L02-048]]. Spiekermann's example: people trust a sans-set skydiving notice more than a casual face [S-L02-047].
- **Depends on (upstream):** brand personality attributes (L06); primary use (reading vs scanning vs data); script coverage needed (DC-L02-24).
- **Affects (downstream):** pairing choice (DC-L02-03); tracking and line-height tuning (geometric faces with small x-heights need more size or leading) [S-L02-051]; icon style match (L05: geometric faces pair with geometric icon sets [inferred]); corner radius and shape language (L04: rounded faces such as SF Pro Rounded "coordinate text with the appearance of soft or rounded UI elements" [S-L02-001]).
- **Token encoding:** not a token itself; it selects the value of `font.family.*`. The builder should store it as metadata (e.g. `$extensions.classification: "neo-grotesque"`) to drive recommendations [inferred].
- **Platform notes:** Only the system faces are guaranteed per platform; everything else ships with the app or loads over the web.
- **Accessibility constraints:** Prefer open counters and distinct confusable pairs (il1I, 0O, rn/m, b/d, 6/9) [S-L02-051]. Google flags geometric faces for body text [S-L02-049].
- **Default + heuristic:** Default to a neo-grotesque or humanist sans with a large x-height for UI. Rule of thumb: pick the class from the brand adjectives, then veto it if it fails the confusable-pairs test at 12-14px or lacks your scripts.
- **Evidence:** [S-L02-001] [S-L02-011] [S-L02-021] [S-L02-024] [S-L02-047] [S-L02-048] [S-L02-049] [S-L02-051] [S-L02-053]

### DC-L02-03: Number of families and pairing
- **Block path:** Foundations > Typography > Typeface > Families and pairing
- **Questions the designer answers:** Do we need more than one typeface? If two, what does each one do? Should headings and body differ?
- **Options:**
  - **One family for everything** (weights, widths and optical sizes create contrast). Windows: "use one font throughout your app's UI" [S-L02-022]. Apple: "Minimize the number of typefaces you use, even in a highly customized interface" [S-L02-001]. Fluent, Polaris, Atlassian (in-product) are single-family plus mono [S-L02-008] [S-L02-014] [S-L02-015].
  - **One family split into display and text cuts** (superfamily): Material's brand vs plain typeface tokens (Google Sans for display/headline/title large, Google Sans Text below) [S-L02-006]; Segoe UI Variable's Display/Text/Small optical cuts [S-L02-022].
  - **Sans + serif pair** (Carbon: Plex Sans for UI, Plex Serif for quotations; Spectrum 2: Adobe Clean + Adobe Clean Serif; Apple: SF + New York, "designed to work well by itself and alongside the SF fonts") [S-L02-011] [S-L02-021] [S-L02-001].
  - **Sans + mono** (almost universal: Carbon Plex Mono, Atlassian Mono, Primer monospace stack, Fluent Consolas) [S-L02-009] [S-L02-015] [S-L02-017] [S-L02-008].
  - **Three families** (e.g. sans + serif + mono, as in Carbon) [S-L02-009].
- **Visual effect:** One family = calm, coherent, efficient. A display/text split within one family = the same voice but crisper headlines. Serif + sans = editorial contrast, "magazine" feel. A distinct display face = strong brand moments at the cost of coherence [inferred]. Pairing too-similar faces reads as a mistake ("dissonance"); pairing needs distinction and harmony [S-L02-046].
- **Depends on (upstream):** DC-L02-01, DC-L02-02; expressive vs productive balance (DC-L02-11).
- **Affects (downstream):** `font.family.*` token count; which roles use which family (usually display/headline vs body/label); loading budget (every family adds files).
- **Token encoding:** `font.family.sans`, `font.family.serif`, `font.family.mono` (primitives); `font.family.heading`, `font.family.body`, `font.family.code` (semantic) [inferred naming, patterned on Carbon/Primer [S-L02-009] [S-L02-017]].
- **Platform notes:** Native apps can bundle fonts; web pays per family in download time [S-L02-042].
- **Accessibility constraints:** Each extra family must meet the same legibility and script coverage bar [inferred].
- **Default + heuristic:** Default to 1 UI family + 1 mono (2 total), with an optional serif or display face for marketing. Pairing rules from Google Fonts Knowledge: first check whether the primary family's weights, widths and optical sizes already give enough contrast; add a second face only for a change of context, brand augmentation, missing weights/italics or missing scripts; pair "siblings" that share x-height, contrast and width; when in doubt pair a serif with a sans; keep the historical era consistent unless contrast is the point [S-L02-046] [S-L02-048].
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-008] [S-L02-009] [S-L02-011] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-042] [S-L02-046] [S-L02-048]

### DC-L02-04: Variable fonts, optical sizing and grade
- **Block path:** Foundations > Typography > Typeface > Variable axes
- **Questions the designer answers:** Do we want one variable file or several static weights? Should small text get a sturdier, looser design and large text a tighter, more refined one automatically? Do we want in-between weights (e.g. 450, 550)? Should text look equally heavy in light and dark mode?
- **Options:**
  - **Static fonts, discrete weights.** Roboto is static and is what M3 components apply by default [S-L02-053].
  - **Variable font, weight axis only.** Noto Sans Devanagari (wdth 62.5-100, wght 100-900) [S-L02-026]; Polaris uses in-between variable weights 450/550/650 [S-L02-014].
  - **Variable with automatic optical size (opsz).** SF Pro and New York have "dynamic optical sizes" that merge Text and Display designs and interpolate per point size [S-L02-001]; Segoe UI Variable's opsz is "automatic and on by default", scaling from 8pt to 36pt [S-L02-022]; Inter opsz 14-32 [S-L02-026]; Material's token module sets `'opsz'` equal to the font size for every style (e.g. Display Large opsz 57) [S-L02-006].
  - **Rich variable (width, grade, roundness, slant, parametric axes).** Google Sans Flex: GRAD 0-100, ROND 0-100, opsz 6-144, slnt -10-0, wdth 25-151, wght 1-1000 [S-L02-026]. Roboto Flex adds parametric axes (XOPQ, YOPQ, XTRA, YTUC, YTLC, YTAS, YTDE, YTFI) [S-L02-053].
- **Visual effect:** Optical sizing makes small text sturdier and more open (less contrast, looser spacing, taller x-height) and large text sleeker and tighter; without it, display text set in a text cut looks clunky and small text set in a display cut looks spindly [S-L02-049]. In-between weights give finer hierarchy steps (Polaris 450 body reads slightly darker than 400) [S-L02-014] [inferred for the reading]. Grade changes stroke thickness without changing width, so it can compensate for light-on-dark text looking bolder, with no reflow [S-L02-049]. Roundness (ROND) softens the brand voice, echoing rounded corners [S-L02-001] [inferred link to shape].
- **Depends on (upstream):** DC-L02-01 (the chosen face must actually have the axes); platform support.
- **Affects (downstream):** weight tokens (numeric values not limited to 100 steps); tracking tokens (automatic opsz reduces the need for size-specific tracking, but Apple still recommends adjusting tracking in mockups [S-L02-001]); dark-mode text tokens (grade per mode, cross-lane L01); file size and loading (DC-L02-06).
- **Token encoding:** DTCG `fontWeight` accepts any number 1-1000 [S-L02-030]. The DTCG 2025.10 typography composite has no slot for other axes (only fontFamily, fontSize, fontWeight, letterSpacing, lineHeight) [S-L02-032], so opsz/GRAD/wdth must live in `$extensions` or a custom type. Material tokenizes axes per style (`wght`, `GRAD`, `wdth`, `ROND`, `opsz`, `CRSV`, `slnt`, `FILL`, `HEXP`) [S-L02-006].
- **Platform notes:** iOS/macOS apply optical size automatically for the system fonts [S-L02-001]. Windows XAML matches opsz to font size automatically; CSS `font-optical-sizing: auto` does the same on the web when the font has an opsz axis [S-L02-022] [inferred for the CSS property default]. Figma exposes variable axes for installed variable fonts [inferred; not verified this session].
- **Accessibility constraints:** HIG: avoid Ultralight, Thin and Light weights, especially at small sizes [S-L02-001]. Any weight range must still pass contrast (thin strokes lower perceived contrast) [inferred].
- **Default + heuristic:** Default to a variable font with wght + opsz when available, with opsz tied to font size. Rule of thumb: if your chosen face has no opsz axis, create separate "display" tracking/line-height values for sizes above ~24px instead (DC-L02-14).
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-014] [S-L02-022] [S-L02-026] [S-L02-030] [S-L02-032] [S-L02-049] [S-L02-053]

### DC-L02-05: Monospace and numeric faces
- **Block path:** Foundations > Typography > Typeface > Monospace / numerals
- **Questions the designer answers:** Does the product show code, IDs, logs or tables of numbers? Should numbers in dashboards line up in columns? Do we want a special face for big metrics?
- **Options:**
  - **System mono stack**: Primer `ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace`; Polaris similar [S-L02-017] [S-L02-014].
  - **Brand mono**: IBM Plex Mono (Carbon code-01 12/16, code-02 14/20, tracking 0.32px) [S-L02-011]; Atlassian Mono (font.code 12/20) [S-L02-015]; Roboto Mono [S-L02-053].
  - **Dedicated numeric face**: Fluent `fontFamilyNumeric` starts with Bahnschrift [S-L02-008]; Atlassian has `font.metric.large/medium/small` (Bold 28/32, 24/28, 16/20) for KPI numbers [S-L02-015].
  - **Tabular figures from the main face** (no second family): Material recommends tabular figures in tables and anything that changes, like clocks [S-L02-052].
- **Visual effect:** Mono reads technical and precise; used widely it gives a "developer tool" personality. Tabular figures keep columns aligned and stop numbers jittering when they update [S-L02-052].
- **Depends on (upstream):** product type (data-heavy, developer, finance); DC-L02-03.
- **Affects (downstream):** code block, inline code, table cells, data-viz axis labels (L05), counters, timers.
- **Token encoding:** `font.family.mono` (fontFamily); composite `text.code.inline`, `text.code.block` (Primer `text.codeBlock` 13px / 1.5) [S-L02-017]; `text.metric.*` [S-L02-015].
- **Platform notes:** Web gets tabular figures via `font-variant-numeric: tabular-nums` (OpenType `tnum`) [S-L02-043].
- **Accessibility constraints:** Mono faces must still distinguish 0/O and 1/l/I; a slashed zero (`zero` feature) helps for codes and IDs [S-L02-043] [S-L02-049].
- **Default + heuristic:** Default to the system mono stack plus `tabular-nums` on numeric table cells. Rule of thumb: add a numeric/metric style only if the product has dashboards.
- **Evidence:** [S-L02-008] [S-L02-011] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-043] [S-L02-049] [S-L02-052] [S-L02-053]

### DC-L02-06: Font licensing, loading and performance (web)
- **Block path:** Foundations > Typography > Typeface > Delivery
- **Questions the designer answers:** Are we allowed to self-host or embed this font in apps? How much font data can the page afford? Is a flash of fallback text acceptable, or a layout shift?
- **Options:**
  - **License:** open source (SIL OFL: Google Sans Flex, Roboto Flex, Noto, Inter, per Google Fonts metadata [S-L02-026]; IBM Plex from GitHub [S-L02-012]) vs commercial license (per-domain, per-app or per-pageview terms) [inferred] vs OS-licensed system fonts that must not be embedded (Apple) [S-L02-001].
  - **Delivery:** self-host (needs CDN + HTTP/2 to beat third parties) or third-party service [S-L02-042].
  - **font-display:** `optional` (best performance, web font may not show), `swap` (fast text, possible layout shift), `block` (web font priority, invisible text delay) [S-L02-042].
  - **Payload control:** WOFF2 only; subset with `unicode-range`; variable fonts pay off when several weights are used; limit the number of fonts [S-L02-042].
  - **Fallback metric matching:** `size-adjust` on the fallback @font-face to reduce CLS [S-L02-042]; `font-size-adjust` (Baseline 2024) to normalize x-height or cap height across fallback fonts [S-L02-045].
- **Visual effect:** `swap` shows text immediately in the fallback, then visibly re-flows when the brand font arrives; `optional` looks stable but first-time visitors may never see the brand font; `block` gives a brief blank [S-L02-042]. Good fallback metric matching makes the swap nearly invisible [S-L02-045] [inferred].
- **Depends on (upstream):** DC-L02-01, DC-L02-03, DC-L02-04, script coverage (Indic/CJK fonts are large) [inferred].
- **Affects (downstream):** `font.family` fallback order; @font-face declarations; perceived performance and Core Web Vitals (CLS) [S-L02-042].
- **Token encoding:** Not usually tokenized beyond the fallback array in `fontFamily` [S-L02-032]; the builder should output @font-face CSS alongside tokens [inferred].
- **Platform notes:** Native apps bundle fonts at build time; the web downloads them at runtime [inferred].
- **Accessibility constraints:** A fallback must cover the same scripts; otherwise text becomes tofu boxes for some users [inferred].
- **Default + heuristic:** Default to WOFF2, one variable file per family, `font-display: swap` plus metric-adjusted fallback, and subsets per script. Rule of thumb: budget no more than 2 families and 1 variable file each on first load [inferred from S-L02-042].
- **Evidence:** [S-L02-001] [S-L02-012] [S-L02-026] [S-L02-032] [S-L02-042] [S-L02-045]

### DC-L02-07: Type role taxonomy and naming
- **Block path:** Foundations > Typography > Type roles
- **Questions the designer answers:** How do people pick a text style: by purpose (headline, body, label), by rank (h1-h6), by size (sm/md/lg) or by number (100-1000)? How many levels of each?
- **Options:**
  - **Role x size matrix**: Material's 5 roles (display, headline, title, body, label) x 3 sizes (large, medium, small) = 15 styles, named for purpose [S-L02-052]. Label is for text inside components (buttons use Label Large) [S-L02-052].
  - **Named semantic styles**: Apple's 11 text styles (Large Title, Title 1-3, Headline, Body, Callout, Subhead, Footnote, Caption 1-2) [S-L02-001]; Fluent (Caption 2 ... Display, plus Strong/Stronger) [S-L02-007]; Primer (display, title L/M/S, subtitle, body L/M/S, caption) [S-L02-017].
  - **Category + t-shirt size**: Atlassian `font.heading.xxlarge ... xxsmall`, `font.body.large/small`, `font.metric.*`, `font.code` [S-L02-015]; Polaris `text-heading-3xl ... xs`, `text-body-lg ... xs` [S-L02-014]; Spectrum 2 heading XXS..XXXXL, body XS..XXXL, detail S..XL, code [S-L02-021].
  - **Category + numbered level with set suffix**: Carbon `heading-01..07`, `body-01/02`, `-01` = productive, `-02` = expressive [S-L02-011].
  - **Numeric primitives underneath**: Fluent `fontSizeBase100..600`, `fontSizeHero700..1000` [S-L02-008]; Polaris `font-size-275..1200` [S-L02-014]; Spectrum `font-size-25..1500` [S-L02-021]; Carbon `scale01..23` [S-L02-009].
- **Visual effect:** Not visual in itself, but taxonomy drives consistency: purpose-named roles make designers pick by job and stop ad-hoc sizes; t-shirt sizes are easy to extend; numbered primitives leave room to insert steps [inferred].
- **Depends on (upstream):** team size and how the system is consumed (L07 token architecture, L11 governance).
- **Affects (downstream):** every component's text tokens (button label, field label, helper text, table cell, card title); docs; Figma text style names.
- **Token encoding:** Two tiers are typical: primitives (`font.size.200`, `font.weight.semibold`, `font.lineHeight.normal`) and semantic composites (`text.body.medium` of `$type: "typography"`) [S-L02-032]. Material: `md.sys.typescale.body-medium` plus `md.sys.typescale.emphasized.body-medium` [S-L02-006]. Component tier: `button.label.typography` aliasing `text.label.large` [inferred naming].
- **Platform notes:** Apple's names map to `UIFont.TextStyle` / SwiftUI `Font.TextStyle`, so using Apple's names on iOS gets Dynamic Type for free [S-L02-001].
- **Accessibility constraints:** Visual role must not replace semantic HTML headings; Primer says combine heading tags with the right style rather than choosing tags for looks [S-L02-016].
- **Default + heuristic:** Default to a role x size matrix (display, headline, title, body, label, plus code) with a numeric size ramp underneath. Rule of thumb: name semantic styles by job, primitives by number.
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-007] [S-L02-008] [S-L02-009] [S-L02-011] [S-L02-014] [S-L02-015] [S-L02-016] [S-L02-017] [S-L02-021] [S-L02-032] [S-L02-052]

### DC-L02-08: Base body size
- **Block path:** Foundations > Typography > Type scale > Base size
- **Questions the designer answers:** What size is the default paragraph and UI text? Is the product dense (many controls, tables) or reading-oriented? Which platform is primary?
- **Options (real defaults):**
  - **13px**: Polaris text-body-md 13/20 [S-L02-014].
  - **14px**: Material Body Medium 14/20 (M3's scale "key base size" is 14) [S-L02-006] [S-L02-005]; Fluent Body 1 14/20 [S-L02-007]; Windows Body 14/20 epx [S-L02-022]; Carbon productive base 14px [S-L02-011]; Atlassian font.body 14/20 [S-L02-015]; Primer body medium ("Default UI font") [S-L02-017]; Spectrum 2 desktop font-size-100 = 14px [S-L02-021].
  - **16px**: Carbon expressive base 16px [S-L02-011]; Material Body Large 16/24 [S-L02-005]; Primer body large ("user-generated content, markdown rendering") [S-L02-017]; Spectrum 2 body M = font-size-200 = 16px desktop [S-L02-021]; the browser default root size is 16px and M3 converts sp to rem at /16 [S-L02-006].
  - **17pt**: Apple iOS Body at the default Large size; HIG default text size for iOS/iPadOS and visionOS is 17pt [S-L02-001]; Spectrum 2 mobile font-size-100 = 17px [S-L02-021].
  - **Other platforms**: macOS 13pt default, tvOS 29pt, watchOS 16pt [S-L02-001].
- **Visual effect:** 13-14px = dense, efficient, "pro tool" (more data per screen, smaller targets); 16-17 = comfortable, consumer, reading-friendly, airier [inferred]. Moving base from 14 to 16 enlarges every derived style if the scale is ratio-based [inferred].
- **Depends on (upstream):** density choice (L03), platform (L10), audience age/vision, content type (reading vs scanning).
- **Affects (downstream):** the whole scale (ratio-based scales multiply from it); component heights where text drives height (buttons, inputs, list rows); line length (DC-L02-17); spacing scale if spacing is derived from type [inferred].
- **Token encoding:** `font.size.100` or `font.size.base` (dimension, rem preferred on web: Atlassian and Primer use rem "to enhance accessibility" [S-L02-015] [S-L02-016]); semantic `text.body.medium`.
- **Platform notes:** HIG minimums: iOS/iPadOS 11pt, macOS 10pt, tvOS 23pt, visionOS 12pt, watchOS 12pt [S-L02-001]. Windows minimums: 14px Semibold or 12px Regular ("text smaller than these ... are illegible in some languages") [S-L02-022]. Android text in sp; Material's smallest style is Label Small 11sp [S-L02-005].
- **Accessibility constraints:** Keep body in rem/sp/Dynamic Type units so user settings scale it (DC-L02-21). Dyslexia-friendly guidance: 12-14pt or larger [S-L02-059].
- **Default + heuristic:** Web app: 14px UI body with 16px for long-form reading; iOS: 17pt (use Apple's Body); Android: 14sp Body Medium / 16sp Body Large. Rule of thumb: if users mostly read paragraphs, use 16+; if they mostly operate controls and tables, 14 is the norm.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-007] [S-L02-011] [S-L02-014] [S-L02-015] [S-L02-016] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-059]

### DC-L02-09: Scale method and ratio
- **Block path:** Foundations > Typography > Type scale > Generation method
- **Questions the designer answers:** Should sizes come from a formula or be picked by hand? How big a jump between neighbouring sizes? Should the jump grow at large sizes?
- **Options:**
  - **Modular (geometric) scale**: size(n) = base x ratio^n. A modular scale is "a prearranged set of harmonious proportions"; start from body size and choose a ratio with meaning (Tim Brown's golden-section example with an 18px base) [S-L02-060]. Common named ratios: 1.125 (major second), 1.2 (minor third), 1.25 (major third), 1.333 (perfect fourth), 1.5 (perfect fifth), 1.618 (golden) [inferred naming convention; ratios as listed in the brief].
    - Material: "Major Second type scale with 14 as its key base size" [S-L02-006]. Check: 14 x 1.125^n rounds to 16, 22, 28, 32, 36, 45, 58 for n = 1, 4, 6, 7, 8, 10, 12 (14 x 1.125^12 = 57.54), so Material's 57 is off-formula by 1, like its hand-placed 24 [computed from S-L02-005] [S-V1b-025].
    - Spectrum 2: ratio 1.125 [S-L02-020]. Check: 14 x 1.125^n rounds to every desktop value 10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 51, 58, 65, 73, and 17 x 1.125^n rounds to every mobile value (17, 19, 22, 24, 27, 31, 34, 39, 44, 49, 55, 62, 70, 79, 88) [computed from S-L02-021].
  - **Additive / stepped formula**: Carbon Xn = Xn-1 + {INT[(n-2)/4] + 1} x 2 from 12px: +2 for four steps (12-20), then +4 (24-36), +6 (42-60), +8 (68-92), +10 (102-132), +12 (144, 156) [S-L02-012] [S-L02-009].
  - **Hand-tuned on a grid**: Apple, Fluent, Atlassian, Polaris, Primer (sizes on 2px/4px steps, chosen per role) [S-L02-001] [S-L02-008] [S-L02-015] [S-L02-014] [S-L02-017].
  - **Two ratios (fluid)**: Utopia interpolates between a small-screen ratio (default 1.2 at 18px) and a large-screen ratio (default 1.25 at 20px) [S-L02-040].
- **Visual effect (computed from a 16px base):** 1.125 gives 16, 18, 20, 23, 26, 29 (subtle steps, productive, dense apps); 1.2 gives 16, 19, 23, 28, 33, 40 (balanced); 1.25 gives 16, 20, 25, 31, 39, 49 (clear hierarchy, common for marketing-plus-app); 1.333 gives 16, 21, 28, 38, 51 (strong, editorial); 1.5 gives 16, 24, 36, 54, 81 and 1.618 gives 16, 26, 42, 68 (dramatic, poster-like, few usable steps) [computed]. Low ratios = calm, dense, productive; high ratios = expressive, editorial, high contrast [inferred]. Material notes sizes should "provide impactful contrast between sizes by avoiding small differences" [S-L02-006].
- **Depends on (upstream):** DC-L02-08 base size; expressive vs productive intent (DC-L02-11); viewport range (DC-L02-19).
- **Affects (downstream):** every `font.size.*` primitive; heading hierarchy; how many steps fit before sizes become unusable (DC-L02-10).
- **Token encoding:** Primitive size tokens (dimension). The builder should store the generator (base, ratio, rounding rule) as metadata so the ramp can be regenerated [inferred]. Spectrum stores two value sets per token (`desktop`, `mobile`) [S-L02-021].
- **Platform notes:** Rounding to whole px/pt (and usually even numbers) is universal in shipped systems [computed from tables above].
- **Accessibility constraints:** For fluid scales, the largest-to-smallest ratio of any single clamped size should stay at or below 2.5x to keep WCAG 1.4.4 (DC-L02-19) [S-L02-041].
- **Default + heuristic:** Default to a ratio-generated ramp rounded to even pixels, then hand-adjust. Ratio rule of thumb: 1.125-1.2 for dense apps, 1.25 for mixed product + marketing, 1.333+ for editorial or marketing sites.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-008] [S-L02-009] [S-L02-012] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-020] [S-L02-021] [S-L02-040] [S-L02-041] [S-L02-060]

### DC-L02-10: Number of steps and styles
- **Block path:** Foundations > Typography > Type scale > Step count
- **Questions the designer answers:** How many distinct sizes? How many named styles (size x weight x line-height combinations)? Should every product use them all?
- **Options:** Primer 6 base sizes / 9 roles [S-L02-017]; Atlassian 7 heading + 3 body [S-L02-015]; Polaris 8 sizes / 11 styles [S-L02-014]; Apple 10 sizes / 11 styles [S-L02-001]; Fluent web 10 sizes / 16 styles [S-L02-007]; Material 11 sizes / 15 baseline + 15 emphasized [S-L02-005]; Carbon 23-step size scale with about 30 styles [S-L02-009]; Spectrum 2 up to 18 size tokens per platform [S-L02-021].
- **Visual effect:** Few steps = strong, consistent rhythm and simpler decisions; many steps = more nuance but risk of near-duplicate sizes that blur hierarchy [inferred]. Material: "No single product will use all the styles"; its example picks 5 [S-L02-006].
- **Depends on (upstream):** DC-L02-09 ratio (high ratios run out of usable steps quickly); product surface breadth (app only vs app + marketing).
- **Affects (downstream):** number of text styles in Figma; documentation load; component text choices.
- **Token encoding:** a primitive size ramp (8-12 values) plus 10-16 semantic composites [inferred from the systems above].
- **Platform notes:** None specific.
- **Accessibility constraints:** None directly; fewer, clearly different steps help people who rely on visual hierarchy [inferred].
- **Default + heuristic:** Default to 8-10 sizes and 12-15 semantic styles. Rule of thumb: if two adjacent sizes differ by less than about 10%, merge them [inferred from Material's "avoid small differences" S-L02-006].
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-007] [S-L02-009] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-021]

### DC-L02-11: Productive vs expressive typography (scale contrast)
- **Block path:** Foundations > Typography > Type sets
- **Questions the designer answers:** Is the surface a task-focused product screen or a marketing/editorial page? Do we need one scale or two? Can expressive styles appear inside product containers?
- **Options:**
  - **Two sets (Carbon)**: productive set, base 14px, fixed headings, "more condensed treatment of content to maintain focus on tasks"; expressive set, base 16px, fluid headings for "a more dramatic, graphic use of type in editorial and marketing design" that "would be distracting if used in product" [S-L02-012] [S-L02-011]. Fluid styles: "Do not use these styles inside a container" [S-L02-011].
  - **One scale with emphasized variants (Material 3 Expressive)**: one scale, 15 baseline + 15 emphasized styles; emphasized is heavier and meant for selection, actions, headlines and editorial moments [S-L02-006].
  - **One scale plus a separate brand/marketing typeface**: Atlassian (Charlie Sans for brand) [S-L02-015]; Apple visionOS adds Extra Large Title 1/2 "for wide, editorial-style layouts" [S-L02-001].
  - **Single productive scale only** (Polaris, Primer's display is only for "brand to product transition pages") [S-L02-014] [S-L02-017].
- **Visual effect:** Productive = tight scale contrast (sizes 12-32), regular/semibold weights, compact line heights; dense, calm, efficient. Expressive = large jumps (Carbon fluid-display-04 from 42px to 156px across breakpoints), light weights at huge sizes (Carbon display 300), tight line heights (1.05-1.2) and negative tracking (-0.64 to -0.96px); dramatic, editorial, brand-forward [S-L02-009] [S-L02-011].
- **Depends on (upstream):** brand personality (L06); surface types in scope (app, docs, marketing).
- **Affects (downstream):** heading tokens; responsive behaviour (expressive is usually fluid); line-height and tracking tokens for display sizes; layout (L03) for hero sections.
- **Token encoding:** Carbon suffix convention (`-01` productive, `-02` expressive; `fluid-*` prefix) [S-L02-011]; Material namespace (`md.sys.typescale.emphasized.*`) [S-L02-006]. Builder option: a `mode` or `set` axis on type tokens [inferred].
- **Platform notes:** Expressive fluid type is web-centric; native apps usually rely on fixed styles plus Dynamic Type [inferred].
- **Accessibility constraints:** Very large display text still has to scale (WCAG 1.4.4) and fluid ranges should respect the 2.5x rule [S-L02-028] [S-L02-041].
- **Default + heuristic:** Default to one productive scale plus 3-4 expressive display styles for marketing. Rule of thumb: if more than a third of the product's pages are marketing/editorial, define a full second set.
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-009] [S-L02-011] [S-L02-012] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-028] [S-L02-041]

### DC-L02-12: Emphasis variants within a style
- **Block path:** Foundations > Typography > Type roles > Emphasis
- **Questions the designer answers:** How do we show importance inside the same size: heavier weight, color, italics? Should components have "selected/unread" typographic states?
- **Options:**
  - **Emphasized twin for every style**: Material Expressive (baseline 400 -> emphasized 500; baseline 500 -> emphasized 700) [S-L02-005] [S-L02-006]; Apple emphasized weights via symbolic traits, "medium, semibold, bold, or heavy" (e.g. Body Regular -> Semibold, Large Title Regular -> Bold) [S-L02-001].
  - **Strong / Stronger variants**: Fluent Body 1 (400), Body 1 Strong (600), Body 1 Stronger (700) [S-L02-007].
  - **Weight-named sub-styles**: Spectrum 2 default/strong/emphasized (italic)/heavy/light for headings and body [S-L02-021].
  - **Color only**: Carbon/Material use primary color for links and actions and lighter neutrals to de-emphasize [S-L02-012] [S-L02-052]; Fluent: primary color elevates, lighter neutral reduces [S-L02-007].
  - **Italic**: Carbon allows italics only for in-sentence emphasis (titles of works, technical terms) [S-L02-012]; Windows excludes italics from the ramp because they can reduce readability, "particularly for people with dyslexia" [S-L02-022].
- **Visual effect:** Weight emphasis adds punch without changing layout (if the font's widths are stable) and is the M3 Expressive signature: bolder selected chips, unread items and primary buttons [S-L02-006]. Color emphasis is quieter. Italic adds a literary/editorial tone [inferred].
- **Depends on (upstream):** DC-L02-15 weight palette; DC-L02-04 (variable fonts make in-between weights possible).
- **Affects (downstream):** selected/unread states in lists, menus, chips, tabs, badges, primary buttons [S-L02-006]; link styling (L01 color).
- **Token encoding:** a parallel composite per style (`text.body.medium.emphasized`) or a weight override token (`font.weight.body.strong`) [inferred]; Material's `md.sys.typescale.emphasized.body-medium` [S-L02-006].
- **Platform notes:** iOS: SwiftUI `.bold()` / UIKit symbolic traits produce the emphasized weight while keeping Dynamic Type [S-L02-001].
- **Accessibility constraints:** Don't rely on color alone for meaning (links underlined in Material) [S-L02-052]. Dyslexia guidance: use bold for emphasis, avoid italics and underline [S-L02-059].
- **Default + heuristic:** Default to one emphasized weight per style (regular to semibold, medium to bold). Rule of thumb: emphasis = weight first, color second, italics only inside running text.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-007] [S-L02-012] [S-L02-021] [S-L02-022] [S-L02-052] [S-L02-059]

### DC-L02-13: Line height system (and 4pt baseline snapping)
- **Block path:** Foundations > Typography > Metrics > Line height
- **Questions the designer answers:** Do line heights come from a ratio or fixed values? Should they snap to a 4pt grid? Tighter for headings, looser for paragraphs? Do we need a "compact" variant for components?
- **Options:**
  - **Fixed values snapped to 4pt**: Material (every line height a multiple of 4, e.g. Body Large 16/24, Display Large 57/64) [S-L02-005]; Atlassian (36, 32, 28, 24, 20, 16) [S-L02-015]; Polaris (12-48 in 4px steps) [S-L02-014].
  - **Fixed values on a 2pt grid**: Fluent (14, 16, 20, 22, 26/28, 32, 36, 40, 52, 92) [S-L02-007] [S-L02-008]; Carbon (16, 18, 20, 22, 24, 28, 36, 40, 50, 64) [S-L02-011].
  - **Named unitless ratios**: Primer tight 1.25, snug 1.375, normal 1.5, relaxed 1.625, loose 1.75, "aligned to a 4px grid" per style [S-L02-017] [S-L02-016]; Spectrum 2 line-height-100 = 1.3 (headings, detail) and line-height-200 = 1.5 (body), plus CJK 1.5 / 1.7 [S-L02-021].
  - **Per-size tuned leading**: Apple (Body 17/22, Title 3 20/25, Large Title 34/41; leading grows with each Dynamic Type size) [S-L02-001].
  - **Compact vs long-form variants of the same size**: Carbon body-compact-01 14/18 (short text, up to four lines, in components) vs body-01 14/20 (long paragraphs) [S-L02-011]; Apple "loose" and "tight" leading symbolic traits, with a rule to avoid tight leading for three or more lines [S-L02-001].
- **Visual effect:** Tight leading (1.1-1.25) makes headings feel solid and punchy; 1.4-1.6 makes paragraphs open and easy to track; too tight "undermines the flow", too loose and "lines won't feel cohesive" [S-L02-052]. Material recommends about 1.2x for title/headline/display and about 1.5x for body/label [S-L02-052]. Google Fonts Knowledge: 115-150% for Latin body; display can go 90-100%; longer measures need more leading; mobile body can be tighter (e.g. 130%) than desktop (150%) [S-L02-051]. Snapping to 4pt makes text blocks line up with a 4/8pt spacing grid, giving a tidy, engineered rhythm [inferred].
- **Depends on (upstream):** DC-L02-08 base size; spacing grid (L03: 4pt or 8pt); script mix (tall/dense scripts need more, DC-L02-25); x-height of the chosen face (larger x-height looks tighter and needs more leading) [S-L02-051].
- **Affects (downstream):** component heights (Primer notes title medium's 32px-equivalent line height "matches with button and other medium control heights") [S-L02-017]; list row heights; vertical rhythm; text-spacing robustness (DC-L02-22).
- **Token encoding:** DTCG lineHeight inside typography is a `number` interpreted as a multiplier of fontSize [S-L02-032]; the spec keeps typography open for feedback (Issue 102, "Typography type feedback", covers the whole typography type, not lineHeight alone [S-V1b-002]) [S-L02-032]. Figma's line-height variable is a number (no percent unit in variables) [S-L02-036] [S-L02-037]. Primitive: `font.lineHeight.tight/normal/relaxed` (number) or `font.lineHeight.300 = 20px` (Fluent/Polaris style dimension) [S-L02-008] [S-L02-014].
- **Platform notes:** Web and iOS place half-leading above and below the text; Android historically clips the first and last line to the font's default height, which makes the same spec render differently [S-L02-051]. Material therefore specs web/iOS with bounding boxes and Android with baselines [S-L02-052]. Android: define lineHeight in sp so it scales with text [S-L02-039]. Web: `text-box-trim` / `text-box-edge: cap alphabetic` (Baseline 2026) trims the half-leading so text can sit exactly on a grid [S-L02-044].
- **Accessibility constraints:** WCAG 1.4.12 (AA): layouts must survive user overrides to 1.5x line height with no clipping [S-L02-027]. WCAG 1.4.8 (AAA): at least 1.5 within paragraphs [S-L02-029].
- **Default + heuristic:** Default to ratio-derived line heights rounded to the nearest 4px: about 1.5 for 12-16px, 1.4 for 18-24px, 1.25 for 28-40px, 1.1-1.15 for 48px+. Rule of thumb: the larger the text, the smaller the ratio; the longer the line, the larger the ratio.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-007] [S-L02-008] [S-L02-011] [S-L02-014] [S-L02-015] [S-L02-016] [S-L02-017] [S-L02-021] [S-L02-027] [S-L02-029] [S-L02-032] [S-L02-036] [S-L02-037] [S-L02-039] [S-L02-044] [S-L02-051] [S-L02-052]

### DC-L02-14: Letter spacing (tracking) strategy
- **Block path:** Foundations > Typography > Metrics > Letter spacing
- **Questions the designer answers:** Keep the font's default spacing, or tighten big text and loosen small text? Do all-caps labels get extra spacing? Is tracking a fixed value or proportional to size?
- **Options:**
  - **Size-specific tracking table (Apple)**: SF Pro tracking goes from +41/1000 em at 6pt, to 0 at 12pt, to -26/1000 em (-0.43pt) at 17pt, back to positive (+14/1000 em) around 28-30pt and down to 0 at 80pt+. SF Pro Rounded is positive at every size; New York goes from +40 at 6pt to -16/1000 em at 70-160pt and -18 at 220pt+ [S-L02-001]. The system applies this automatically at runtime; designers mimic it in mockups [S-L02-001].
  - **Per-style tracking tokens (Material)**: in shipped Compose tokens: Display Large -0.2sp, Body Large 0.5sp, Body Medium 0.2sp, Body Small 0.4sp, Label Medium/Small 0.5sp, Title Medium 0.2sp [S-L02-005]. The M3 site's token module (Google Sans context) shows 0 for most styles and 0.1pt for Body Small and Label Medium/Small [S-L02-006].
  - **Small-size loosening only**: Carbon 0.32px at 12px, 0.16px at 14px, 0 at 16px+, then negative only at huge display sizes (-0.64px at lg, -0.96px at max) [S-L02-009] [S-L02-011].
  - **Large-size tightening only**: Polaris letter-spacing densest -0.54px (3xl), denser -0.3px (2xl), dense -0.2px (xl, lg), normal 0 below [S-L02-014].
  - **Zero everywhere, except caps/detail**: Spectrum 2 letter-spacing 0em, but detail (uppercase) style 0.06em [S-L02-021].
- **Visual effect:** Negative tracking at display sizes makes headlines dense, confident and "designed"; positive tracking at small sizes improves legibility; generous tracking on all-caps labels makes them look refined and readable [S-L02-049]. Google: negative tracking "is usually not encouraged unless the type is being set at very large (i.e., display) sizes" [S-L02-049].
- **Depends on (upstream):** the typeface (fonts with opsz already adjust spacing per size, DC-L02-04); weight (heavier fonts may need wider spacing, per M3's customization note) [S-L02-006]; script (never letter-space Arabic or Devanagari, DC-L02-25).
- **Affects (downstream):** every composite type style; all-caps components (overlines, tabs, badges); buttons.
- **Token encoding:** DTCG `letterSpacing` is a dimension (px or rem) inside the typography composite [S-L02-032]. Em is the natural unit but DTCG dimension allows only px and rem [S-L02-030]; Material documents letter spacing on the web as tracking/fontSize (e.g. 0.2 / 16 = 0.0125) [S-L02-006]. Figma letter-spacing variables are interpreted as px, not % [S-L02-036]. Polaris names by density (`font-letter-spacing-dense`) rather than by size [S-L02-014].
- **Platform notes:** iOS applies SF tracking automatically for system fonts; custom fonts need explicit kerning values [S-L02-001] [inferred for custom fonts]. Android letterSpacing is in em [S-L02-006].
- **Accessibility constraints:** WCAG 1.4.12: layout must survive letter spacing of 0.12x font size [S-L02-027]. Very large positive or negative values make words unreadable [S-L02-055].
- **Default + heuristic:** Default: 0 at body sizes, +0.02-0.05em for 11-12px and all-caps, -0.01 to -0.02em from about 32px up (tuned per font). Rule of thumb: track in em so the value scales with size, and let optical-size fonts do most of the work.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-009] [S-L02-011] [S-L02-014] [S-L02-021] [S-L02-027] [S-L02-030] [S-L02-032] [S-L02-036] [S-L02-049] [S-L02-055]

### DC-L02-15: Weight palette and the job of each weight
- **Block path:** Foundations > Typography > Metrics > Weights
- **Questions the designer answers:** Which weights are allowed? Is hierarchy carried by weight (bold headings) or by size (large regular headings)? Are light weights allowed?
- **Options:**
  - **Two weights**: Windows 11 Regular + Semibold ("use regular weight for most text, use Semibold for titles"; Bold and Italic are not in the ramp) [S-L02-022].
  - **Three weights**: Carbon Light 300 / Regular 400 / SemiBold 600 (semibold for section headers, not long text; light only for large display) [S-L02-012]; Material 400 / 500 / 700 [S-L02-005]; Atlassian Regular / Medium / Bold (all headings Bold) [S-L02-015].
  - **Four weights**: Fluent 400 / 500 / 600 / 700 [S-L02-008]; Primer 300 / 400 / 500 / 600 [S-L02-017]; Polaris variable 450 / 550 / 650 / 700 [S-L02-014].
  - **Wide range**: Spectrum 2 light through black, with extra-bold as the default heading weight (Latin and CJK) and black for CJK strong/emphasized headings [S-L02-021].
- **Visual effect:** Size-led hierarchy with regular or light headings (Material baseline Display 400, Carbon display 300) looks elegant, airy, editorial; weight-led hierarchy with bold headings at modest sizes (Atlassian Bold, Spectrum extra-bold, Polaris 650) looks punchy, compact and utilitarian [S-L02-005] [S-L02-011] [S-L02-015] [S-L02-021] [S-L02-014] [inferred for the readings]. Carbon: "a lighter weight font can rank hierarchically higher than a bold font if the lighter weight type size is significantly larger" [S-L02-012].
- **Depends on (upstream):** DC-L02-02 classification (some faces look heavy at 400); DC-L02-04 (variable weight availability); DC-L02-11 expressive vs productive.
- **Affects (downstream):** heading tokens, button labels (usually medium/semibold), emphasis variants (DC-L02-12), file count/size for static fonts.
- **Token encoding:** DTCG `fontWeight`: number 1-1000 or aliases (thin/hairline 100, extra-light 200, light 300, normal/regular/book 400, medium 500, semi-bold/demi-bold 600, bold 700, extra-bold 800, black/heavy 900, extra-black 950) [S-L02-030]. Primitive `font.weight.regular = 400`; semantic `font.weight.heading`, `font.weight.strong` [inferred naming].
- **Platform notes:** iOS "Bold Text" accessibility setting increases weights system-wide; custom fonts must honour it [S-L02-001]. Figma binds font weight as a number variable or as a style-name string [S-L02-036].
- **Accessibility constraints:** HIG: avoid Ultralight, Thin and Light, especially at small sizes [S-L02-001]. Windows minimums pair size and weight (14px Semibold, 12px Regular) [S-L02-022].
- **Default + heuristic:** Default to 3 weights: 400 body, 500-600 labels/subheads, 600-700 headings. Rule of thumb: light (300) only at 32px+, never for body.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-008] [S-L02-011] [S-L02-012] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-030] [S-L02-036]

### DC-L02-16: Paragraph spacing and vertical rhythm
- **Block path:** Foundations > Typography > Metrics > Paragraph spacing / rhythm
- **Questions the designer answers:** How much space between paragraphs, and between a heading and its text? Is text spacing measured from baselines or from text boxes? Do we trim the extra space above caps?
- **Options:**
  - **Paragraph spacing as part of the style**: Atlassian font.body.large 16px spacing, font.body 12px, font.body.small 8px (about 0.67-1x the font size) [S-L02-015].
  - **Spacing from the spacing scale (L03)** applied by layout components [inferred].
  - **Baseline-to-baseline spec** (Material for Android and platform-agnostic specs) vs **bounding box + padding** (Material for web and iOS) [S-L02-052].
  - **Trimmed text boxes**: CSS `text-box: trim-both cap alphabetic` removes half-leading so spacing tokens measure from cap height to baseline [S-L02-044].
- **Visual effect:** Generous paragraph spacing (about 1x font size or more) gives an airy, scannable page; tight spacing gives dense documents. Baseline alignment gives "a consistent visual rhythm" (Fluent) [S-L02-007]. Trimmed text makes padding look optically even around buttons and cards [inferred].
- **Depends on (upstream):** line height (DC-L02-13); spacing scale (L03).
- **Affects (downstream):** prose/markdown components, cards, dialogs, form groups.
- **Token encoding:** DTCG typography has no paragraphSpacing sub-value [S-L02-032]; Figma does support paragraph spacing as a number variable [S-L02-036]. Store as a separate dimension token (`text.body.paragraphSpacing`) or in `$extensions` [inferred].
- **Platform notes:** Android and web/iOS place text in the line box differently (DC-L02-13) [S-L02-051].
- **Accessibility constraints:** WCAG 1.4.12: survive paragraph spacing of 2x font size [S-L02-027]; WCAG 1.4.8 AAA: paragraph spacing at least 1.5x the line spacing [S-L02-029]. Dyslexia guidance: extra space around headings and between paragraphs [S-L02-059].
- **Default + heuristic:** Default paragraph spacing = 1x body font size (rounded to the spacing grid); heading-to-body gap smaller than body-to-next-heading gap. Rule of thumb: space above a heading should be about 2x the space below it, so it binds to its own text [inferred].
- **Evidence:** [S-L02-007] [S-L02-015] [S-L02-027] [S-L02-029] [S-L02-032] [S-L02-036] [S-L02-044] [S-L02-051] [S-L02-052] [S-L02-059]

### DC-L02-17: Line length (measure)
- **Block path:** Foundations > Typography > Layout of text > Measure
- **Questions the designer answers:** How wide should a paragraph get? Do we cap text column width on large screens? Different rules for CJK?
- **Options:**
  - **45-75 characters** (Bringhurst, for single-column serif text) [S-L02-051].
  - **40-60 characters** (Material guidance as quoted by Google Fonts Knowledge) [S-L02-051].
  - **50-60 characters** (Windows: "Keep to 50-60 letters per line"; don't use fewer than 20 or more than 60) [S-L02-022].
  - **Up to about 80 characters** (Primer, citing W3C) [S-L02-016]; WCAG 1.4.8 AAA: no more than 80 characters, 40 for CJK [S-L02-029].
- **Visual effect:** Too narrow lines break reading rhythm with constant line jumps; too wide lines make it hard to find the next line, so lines get skipped or repeated [S-L02-049]. Narrow measures look editorial and bookish; wide ones look like dashboards or legal text [inferred].
- **Depends on (upstream):** base size (DC-L02-08); layout grid and container widths (L03); script (CJK halves the count) [S-L02-029].
- **Affects (downstream):** max-width tokens for prose containers; line height (longer lines need more leading) [S-L02-049] [S-L02-051]; responsive type steps (Trent Walton's 45/75 asterisk technique adds a breakpoint when the measure drifts) [S-L02-051].
- **Token encoding:** a size token such as `size.measure.prose = 65ch` (CSS `ch` unit) [inferred; DTCG dimension only allows px/rem [S-L02-030], so `ch` needs `$extensions` or a px/rem approximation].
- **Platform notes:** Mostly a web/tablet/desktop concern; phones naturally sit at 30-45 characters [inferred].
- **Accessibility constraints:** WCAG 1.4.8 (AAA) 80 / 40 CJK [S-L02-029]; reflow at 200% without horizontal scrolling [S-L02-029].
- **Default + heuristic:** Default max prose width about 65-70ch for Latin text, 35-40 characters for CJK. Rule of thumb: if a paragraph is wider than about 10-12 English words per line, constrain the container before touching font size.
- **Evidence:** [S-L02-016] [S-L02-022] [S-L02-029] [S-L02-030] [S-L02-049] [S-L02-051]

### DC-L02-18: Alignment, casing and truncation
- **Block path:** Foundations > Typography > Layout of text > Alignment, case, overflow
- **Questions the designer answers:** Left-aligned or centered? Title Case, sentence case or ALL CAPS in UI? What happens when text doesn't fit: wrap, ellipsis, clip, or fade?
- **Options:**
  - **Alignment**: flush-left / ragged-right by default (Fluent, Windows, Primer); center only for short text such as under icons; right-align for RTL languages [S-L02-007] [S-L02-022] [S-L02-016]. Full justification is excluded by WCAG 1.4.8 AAA [S-L02-029].
  - **Casing**: sentence case for all UI text (Fluent, Windows) and avoid all caps [S-L02-007] [S-L02-022]; all caps kept only for small "detail"/overline labels with added tracking (Spectrum 2 detail 0.06em) [S-L02-021]; Material exposes a text-transform token on Label Medium (value None) [S-L02-006].
  - **Truncation**: Windows uses ellipses in most cases, clipping rarely; clip and wrap when multiple lines are allowed; use ellipses when containers aren't well defined or there is a "see more" link [S-L02-022]. HIG: keep truncation to a minimum as text size grows, let labels use as many lines as needed, and avoid truncating in scrollable regions unless people can open the full text [S-L02-001].
- **Visual effect:** Left-aligned sentence case reads modern, calm and conversational; centered text looks formal or promotional but slows reading of more than a few lines; all caps looks loud or formal, and in long runs is "difficult to read" [S-L02-007] [inferred for the tone readings]. Heavy truncation looks tidy but hides content.
- **Depends on (upstream):** voice and tone (L06: casing is a content decision); script direction (DC-L02-24).
- **Affects (downstream):** buttons, tabs, table cells, list items, cards, navigation; `text-align: start` rather than `left` so RTL mirrors automatically [inferred].
- **Token encoding:** textTransform and textDecoration are not part of the DTCG typography composite [S-L02-032]; store in `$extensions` or component tokens [inferred].
- **Platform notes:** Windows text controls default to ellipsis trimming [S-L02-022]; iOS labels can set unlimited lines to avoid truncation [S-L02-001].
- **Accessibility constraints:** Truncated text needs a way to reach the full content (tooltip, expand, detail view) [S-L02-001]. Dyslexia guidance: avoid all caps for whole words and headings; left align, no justification [S-L02-059] [S-L02-058].
- **Default + heuristic:** Default: start-aligned, sentence case, wrap first, then ellipsis with access to the full text. Rule of thumb: all caps only at 11-12px labels with extra tracking, never for sentences.
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-007] [S-L02-016] [S-L02-021] [S-L02-022] [S-L02-029] [S-L02-032] [S-L02-058] [S-L02-059]

### DC-L02-19: Responsive strategy (fixed, per-breakpoint or fluid)
- **Block path:** Foundations > Typography > Responsive type > Strategy
- **Questions the designer answers:** Should text sizes change with screen width? In steps at breakpoints, or smoothly? Which styles change: only headlines, or body too?
- **Options:**
  - **Fixed sizes everywhere** (rely on the OS text-size setting instead): Carbon's productive set uses fixed headings because product pages put text in containers where "fixed type styles are a must" [S-L02-011]; Windows: design in effective pixels and "you shouldn't have to alter font sizes for different screens sizes" [S-L02-022]; iOS Dynamic Type sizes are user-chosen, not width-driven [S-L02-001].
  - **Per-breakpoint steps**: Carbon expressive styles define values at md, lg, xlg and max breakpoints (e.g. fluid-display-04: 42px default, 68px md, 92px lg, 122px xlg, 156px max) [S-L02-009]; Primer: use title large on wide viewports but title medium on narrow ones, display falls back to title large [S-L02-017]; Trent Walton's measure-driven breakpoints [S-L02-051].
  - **Fluid interpolation between breakpoints**: Carbon's fluid styles change "incrementally (almost imperceptibly) between the different breakpoints" [S-L02-011]; Carbon computes the size between breakpoints in code (`fluid.ts`) [S-L02-009].
  - **Fluid scale with CSS clamp()**: Utopia generates `--step-n: clamp(min rem, rem + vw, max rem)` from a min viewport (default 360px, 18px base, 1.2 ratio) and a max viewport (default 1240px, 20px base, 1.25 ratio) [S-L02-040].
- **Visual effect:** Fixed sizes look consistent and "app-like"; per-breakpoint steps make headlines jump at thresholds; fluid type gives smooth, poster-like hero headlines that fill wide screens and shrink gracefully on phones [S-L02-011] [inferred for the readings]. Two-ratio fluid scales raise contrast on large screens (bigger jumps) and flatten it on phones [S-L02-040].
- **Depends on (upstream):** breakpoints and containers (L03); productive vs expressive (DC-L02-11); platform (native apps rarely use width-based type).
- **Affects (downstream):** heading/display tokens (need min/max or per-breakpoint values); layout of hero sections; line length (DC-L02-17).
- **Token encoding:** DTCG has no native fluid or breakpoint value type; options are one token per breakpoint (`text.display.large.md`), a mode per breakpoint (Figma modes / DTCG resolver-style sets, cf. Spectrum's `desktop`/`mobile` sets) [S-L02-021], or storing the clamp() string in `$extensions` [inferred]. Carbon stores `breakpoints: { md: {...}, lg: {...} }` inside each style object in code [S-L02-009].
- **Platform notes:** Web only for vw-based fluid type. Figma cannot express clamp(); designers mock the min and max frames [inferred].
- **Accessibility constraints:** vw units do not grow with browser zoom, so fluid type can fail WCAG 1.4.4 [S-L02-028] [S-L02-041]; keep each clamp's max at or below 2.5x its min and test at 500% zoom [S-L02-041]; always include a rem component in the preferred value (Utopia's `rem + vw` form does) [S-L02-040] [inferred rationale].
- **Default + heuristic:** Default: fixed body and UI text; fluid (or stepped) only for display and headline styles on the web. Rule of thumb: if a style appears inside a card, table or form, keep it fixed (Carbon: "Do not use these styles inside a container") [S-L02-011].
- **Evidence:** [S-L02-001] [S-L02-009] [S-L02-011] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-028] [S-L02-040] [S-L02-041] [S-L02-051]

### DC-L02-20: Platform scales and minimum sizes (mobile vs desktop)
- **Block path:** Foundations > Typography > Responsive type > Platform scales
- **Questions the designer answers:** Should the same style be bigger on phones than on desktop? What is the smallest text we allow on each platform? Do we ship one scale or one per platform?
- **Options:**
  - **Separate desktop and mobile scales**: Spectrum 2 has two value sets for every size token, mobile about 1.2x desktop (font-size-100: 14px desktop, 17px mobile; font-size-1500: 73px vs 88px), same 1.125 ratio [S-L02-021] [computed].
  - **Per-platform ramps**: Fluent 2 publishes different ramps per platform: web Body 1 14/20, iOS Body 1 17/22 (Display 60/70), Android Body 1 16/24 (Display 60/72), macOS Body 1 13/16, Windows Body 14/20 [S-L02-007].
  - **One scale, native units**: Material uses one scale in sp (Android) and rem (web), converting sp/16 = rem [S-L02-006].
  - **Adopt native text styles on each platform**: Apple's iOS text styles at Large (Body 17pt) and macOS styles (Body 13pt) [S-L02-001].
- **Minimum sizes (official):** iOS/iPadOS default 17pt, minimum 11pt; macOS 13 / 10; tvOS 29 / 23; visionOS 17 / 12; watchOS 16 / 12 [S-L02-001]. Windows 14px Semibold or 12px Regular [S-L02-022]. Material's smallest style is Label Small 11sp; body is 12-16sp [S-L02-005]. Web: many systems' smallest text is 10-12px (Fluent Caption 2 10px; Carbon 12px; Polaris 11px) [S-L02-007] [S-L02-011] [S-L02-014]. The common "16px minimum body on mobile web" rule (partly because iOS Safari zooms into form fields set below 16px) is practitioner knowledge that this session could not verify against a primary source [inferred].
- **Visual effect:** Larger mobile type compensates for distance, touch and small viewports and makes mobile screens look bolder and roomier; desktop type at 13-14px looks denser and more "pro" [S-L02-021] [inferred].
- **Depends on (upstream):** platforms in scope (L10); density (L03).
- **Affects (downstream):** tokens per platform; component heights on touch vs pointer; Figma libraries (often one per platform).
- **Token encoding:** a platform or scale mode on size and line-height tokens (Spectrum `sets: { desktop, mobile }`) [S-L02-021]; in Figma, a "platform" or "density" mode on number variables for font size/line height [S-L02-036] [inferred mapping].
- **Platform notes:** Units: pt (Apple), sp (Android text, scales with user settings), dp (Android non-text), epx (Windows), px/rem (web) [S-L02-001] [S-L02-039] [S-L02-022] [S-L02-006].
- **Accessibility constraints:** Minimums are floors, not targets; thin weights need larger sizes than the minimum [S-L02-001].
- **Default + heuristic:** Default: one semantic scale with platform modes (mobile values about 1.15-1.2x desktop for body and UI). Rule of thumb: never below 11pt/sp on mobile or 12px on the web for anything people must read.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-007] [S-L02-011] [S-L02-014] [S-L02-021] [S-L02-022] [S-L02-036] [S-L02-039]

### DC-L02-21: Text scaling support (Dynamic Type, Android font scale, browser zoom)
- **Block path:** Foundations > Typography > Accessibility > Text scaling
- **Questions the designer answers:** What happens when a user sets text to 200% or to the largest accessibility size? Which text scales and which stays put? How do layouts adapt?
- **Options / platform behaviours:**
  - **iOS/iPadOS Dynamic Type**: 7 standard sizes (xSmall to xxxLarge, default Large) plus 5 accessibility sizes (AX1-AX5). Body goes 14pt (xSmall) to 17 (Large) to 23 (xxxLarge) to 53pt at AX5; Large Title goes 31 to 34 to 40 to 60pt at AX5, so large styles scale much less than body [S-L02-001]. macOS doesn't support Dynamic Type [S-L02-001].
  - **Android 14+ nonlinear font scaling to 200%**: large text scales less than small text; text in sp; lineHeight in sp; don't use sp for padding; use `TypedValue.applyDimension()` / `deriveDimension()` rather than `fontScale` math [S-L02-039].
  - **Web**: WCAG 1.4.4 (AA) requires text resizable to 200% without loss of content or function; browser zoom satisfies it; failures include clipped containers and viewport-unit font sizes [S-L02-028]. rem units help (Atlassian, Primer) [S-L02-015] [S-L02-016].
  - **Selective scaling**: HIG says prioritize content: tab titles need not grow, character dialog should [S-L02-001].
- **Visual effect:** At the largest sizes, the hierarchy compresses (headings and body converge, AX5 Body 53pt vs Large Title 60pt) and layouts must restack: HIG recommends stacked layouts (text above secondary items), fewer columns, bigger icons, and minimal truncation [S-L02-001]. Nonlinear scaling on both platforms preserves some hierarchy while avoiding giant headings [S-L02-039] [S-L02-001].
- **Depends on (upstream):** DC-L02-01 (system fonts scale for free; custom fonts must implement it) [S-L02-001]; layout system (L03) must support reflow.
- **Affects (downstream):** every component with fixed heights (buttons, list rows, chips, tabs, nav bars); icon sizing (SF Symbols scale with Dynamic Type) [S-L02-001]; truncation rules (DC-L02-18).
- **Token encoding:** Apple exposes one token per text style with a table per size category; a builder can model Dynamic Type sizes as modes on type tokens [inferred]. On Android and the web, tokens stay in sp/rem and the platform scales them [S-L02-039] [S-L02-006].
- **Platform notes:** Use `UIFont.preferredFont(forTextStyle:)` / SwiftUI text styles, or `UIFontMetrics` for custom fonts [S-L02-001] [inferred API names]. Android: never compute sizes with `scaledDensity` [S-L02-039].
- **Accessibility constraints:** WCAG 1.4.4 AA [S-L02-028]; WCAG 1.4.10 reflow (related; owned by L03) [inferred]; HIG: aim to show as much useful text at AX sizes as at the largest standard size [S-L02-001].
- **Default + heuristic:** Default: every text token in scalable units, no fixed-height text containers, test at iOS AX5, Android 200% and browser 200% zoom. Rule of thumb: containers grow with text; nothing that holds text gets a fixed height.
- **Evidence:** [S-L02-001] [S-L02-006] [S-L02-015] [S-L02-016] [S-L02-028] [S-L02-039]

### DC-L02-22: Text spacing robustness, legibility and dyslexia considerations
- **Block path:** Foundations > Typography > Accessibility > Legibility and spacing
- **Questions the designer answers:** Will the layout survive users forcing wider spacing? Is the chosen face easy to decode for people with dyslexia or low vision? Should we offer a legibility-first font option?
- **Options:**
  - **Pass WCAG 1.4.12 (AA)**: content must survive line height 1.5x, paragraph spacing 2x, letter spacing 0.12x and word spacing 0.16x the font size, without clipping or overlap; avoid fixed-height containers, size containers in em [S-L02-027].
  - **Legibility-first face choice**: open counters, distinct confusable pairs (il1I, 0O, qp, db, nu, 69, rn/m); Lexend and Atkinson Hyperlegible were designed for easier reading [S-L02-051] [S-L02-049].
  - **Dyslexia-friendly presentation**: sans serif, 12-14pt or larger, headings at least 20% larger than body and bold, avoid italics, underline and all caps, line spacing 1.5, extra space around headings and paragraphs, plain backgrounds [S-L02-059]; left align, no justification [S-L02-058] [S-L02-029].
  - **User-selectable font setting** (offer a hyperlegible face as an option) [inferred].
- **Visual effect:** Designing for 1.4.12 means slightly roomier, flexible containers; legibility-first faces look friendlier and more open, sometimes less sleek [inferred].
- **Depends on (upstream):** DC-L02-02, DC-L02-13, DC-L02-14; component sizing rules (L08).
- **Affects (downstream):** every text container; the builder's lint rules (no fixed height on text boxes).
- **Token encoding:** no special tokens; optional theme or mode "legibility" swapping `font.family.body` and loosening line height and tracking [inferred].
- **Platform notes:** iOS Bold Text and Larger Text settings; Windows excludes italics from its ramp partly for dyslexic readers [S-L02-001] [S-L02-022].
- **Accessibility constraints:** WCAG 1.4.12 AA [S-L02-027]; WCAG 1.4.8 AAA (no justification, line spacing 1.5, paragraph spacing 1.5x line spacing) [S-L02-029].
- **Default + heuristic:** Default: body line height at least 1.4-1.5, no fixed-height text boxes, and a confusable-pairs check in the typeface picker. Rule of thumb: run the 1.4.12 bookmarklet-style override on every component before release [inferred].
- **Evidence:** [S-L02-001] [S-L02-022] [S-L02-027] [S-L02-029] [S-L02-049] [S-L02-051] [S-L02-058] [S-L02-059]

### DC-L02-23: Text color and contrast pairing (link with L01)
- **Block path:** Foundations > Typography > Accessibility > Contrast (shared with Color)
- **Questions the designer answers:** Which color roles can text use? What contrast does each text size need? How do we de-emphasize text without failing contrast?
- **Options:**
  - **Size-dependent contrast (WCAG 2.x)**: Material aims for 4.5:1 for small text and 3:1 for large text [S-L02-052]; Fluent defines large text as above 18.5px bold or 24px regular [S-L02-007].
  - **Text color roles**: Material default text color on-surface, with on-surface-variant as the alternative; links in primary (or tertiary for quieter links) and underlined [S-L02-052]. Carbon keeps running text neutral and uses primary blue for primary actions and links [S-L02-012]. Fluent emphasizes with primary color, de-emphasizes with lighter neutrals [S-L02-007].
  - **Weight/grade compensation in dark mode**: light text on dark backgrounds looks bolder; variable fonts with a grade axis can compensate without reflow [S-L02-049].
- **Visual effect:** Low-contrast secondary text looks refined but risks failing; bold small text can reach "large text" status under WCAG thresholds only at 18.5px+ bold [S-L02-007].
- **Depends on (upstream):** L01 color roles and contrast method; DC-L02-15 (weight affects which threshold applies).
- **Affects (downstream):** text color tokens per role (primary, secondary, disabled, link, inverse), per mode.
- **Token encoding:** color tokens are separate from typography composites (DTCG typography has no color sub-value) [S-L02-032]; pair them in component tokens (`text.body.color = color.text.primary`) [inferred].
- **Platform notes:** Apple and Material both lean on semantic color roles for text (L01 owns detail) [S-L02-052].
- **Accessibility constraints:** 4.5:1 normal text, 3:1 large text (18.5px bold / 24px regular per Fluent) [S-L02-052] [S-L02-007]. Disabled text is exempt under WCAG but should still be distinguishable [inferred].
- **Default + heuristic:** Default: 3 text emphasis levels (primary, secondary, disabled), each verified for contrast in every mode. Rule of thumb: when a style's size drops below 18.5px bold / 24px regular, it needs 4.5:1.
- **Evidence:** [S-L02-007] [S-L02-012] [S-L02-032] [S-L02-049] [S-L02-052]

### DC-L02-24: Script coverage and font fallback stacks (incl. Indic, CJK, Arabic)
- **Block path:** Foundations > Typography > Internationalization > Scripts and fallback
- **Questions the designer answers:** Which languages and scripts must the product support now and later (for India: Hindi/Marathi in Devanagari, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Punjabi/Gurmukhi, Odia, Urdu in Nastaliq/Arabic)? Does the brand font cover them? What renders when it doesn't?
- **Options:**
  - **Brand Latin font + per-script Noto fallback**: Material: Noto Sans is the fallback "when a language is unsupported", Roboto-compatible, 150+ scripts; fallback order Roboto Flex > Roboto > Noto [S-L02-053]. On Android, Noto is the default for every language Roboto doesn't cover [S-L02-051]. Noto Sans Devanagari is variable (wdth 62.5-100, wght 100-900) [S-L02-026].
  - **OS script fonts via the system stack**: iOS/macOS Kohinoor Devanagari (5 weights, system font), Kohinoor Bangla, Kohinoor Telugu, Kohinoor Gujarati, Tamil Sangam MN [S-L02-062]; Windows Nirmala UI covers Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Odia, Sinhala, Tamil, Telugu and more; Microsoft YaHei UI / JhengHei UI (Chinese), Yu Gothic UI (Japanese), Malgun Gothic (Korean), Segoe UI (Arabic, Hebrew) [S-L02-022]; Windows `LanguageFont` API returns the recommended font per language [S-L02-022].
  - **A brand family with its own script companions**: Adobe Clean Han for CJK in Spectrum 2 [S-L02-021]; IBM Plex Sans Hebrew in Carbon's stacks [S-L02-009]; Indic-inclusive open families such as Mukta and Hind (Devanagari + Latin, static weights) [S-L02-026].
  - **Latin-only brand font with no plan** (anti-pattern): Google Sans Flex's subsets are Latin, Latin Extended, Vietnamese and a few others, with no Devanagari or other Indic script; Roboto Flex also has no Indic subset [S-L02-026]. Such fonts silently fall back to whatever the OS has.
- **Visual effect:** Without a matched fallback, Hindi text next to a brand Latin face can look a different size and weight, and misaligned on the baseline, because "differences in physical size for fonts affects baseline alignment" in headline (shirorekha) scripts [S-L02-056]. Matched families (Noto harmonized with Roboto; Kohinoor on Apple) keep weight and height consistent [S-L02-051] [S-L02-053]. Noto tall-script families lack a Medium weight, so Medium styles may render Regular [S-L02-051].
- **Depends on (upstream):** market and language list (for an India-first product, Devanagari at minimum) [inferred]; DC-L02-01; DC-L02-06 (Indic and CJK fonts are large, so subsetting matters) [inferred].
- **Affects (downstream):** `font.family.*` stacks per locale; weight tokens (map 500 to 600/400 where a script lacks Medium) [inferred]; line heights (DC-L02-25); QA matrix.
- **Token encoding:** DTCG fontFamily arrays [S-L02-032]; per-locale overrides as token sets or modes (`font.family.body` in a `hi-IN` mode = ["Brand Sans", "Noto Sans Devanagari", "Kohinoor Devanagari", "Nirmala UI", sans-serif]) [inferred]. Primer's default stack already includes Noto Sans [S-L02-017].
- **Platform notes:** Web: `unicode-range` subsets let one family name resolve to several script files [S-L02-042]; `font-size-adjust` can normalize x-height or cap height across fallbacks (Baseline 2024) [S-L02-045].
- **Accessibility constraints:** Missing glyphs (tofu) are a hard failure for users of that language [inferred]. Windows notes text below its minimums is "illegible in some languages" [S-L02-022].
- **Default + heuristic:** Default for an India-facing product: brand Latin face + Noto Sans for each target Indic script (fallback also to Kohinoor on Apple and Nirmala UI on Windows), with a script-specific size or x-height adjustment. Rule of thumb: pick the brand font only after checking its Unicode coverage against your language list.
- **Evidence:** [S-L02-009] [S-L02-017] [S-L02-021] [S-L02-022] [S-L02-026] [S-L02-032] [S-L02-042] [S-L02-045] [S-L02-051] [S-L02-053] [S-L02-056] [S-L02-062]

### DC-L02-25: Script-specific metrics (line height, size, spacing, emphasis, direction)
- **Block path:** Foundations > Typography > Internationalization > Script metrics
- **Questions the designer answers:** Do Hindi, Telugu, Arabic or Chinese text need more line height or a different size than English? Can we apply letter spacing, italics and all caps to every script? What changes for right-to-left?
- **Options (official values):**
  - **Material 3 language height categories** (line height adapts automatically): Small (base): Latin (except Vietnamese), Cyrillic, Greek, Hebrew. Medium (~7% taller): Arabic, Bangla, Chinese, Gujarati, Hindi, Japanese, Kannada, Korean, Malayalam, Odia, Punjabi, Tamil, Thai, Vietnamese and most others. Large (~30% taller): Burmese, Telugu. Extra large (~100% taller): Nastaliq (Urdu). Default to Medium and switch by detected language; "ignoring language height can lead to overlapping text and broken UI" [S-L02-006].
  - **Tall vs dense script groups** (Google Fonts Knowledge / Material language support): tall = South/Southeast Asian and Middle Eastern (Arabic, Hindi, Telugu, Thai, Vietnamese) need extra line height; dense = CJK need extra line height plus higher character density [S-L02-051].
  - **Spectrum 2 CJK rules**: CJK line height 1.5 (headings) / 1.7 (body) vs Latin 1.3 / 1.5; CJK headings and body one size step smaller than Latin at the same t-shirt size (except heading XXS); CJK emphasis uses weight (black) instead of italic [S-L02-021].
  - **Letter spacing**: do not letter-space Arabic, which "may lead to the text looking broken" [S-L02-055]; letter spacing "splits conjuncts" in Devanagari in all major engines [S-L02-056]. So tracking tokens must be zeroed for these scripts [inferred from both].
  - **Emphasis and decoration**: underline/overline must account for Devanagari matras above and below [S-L02-056]; italics and all caps have no native meaning in Devanagari, Arabic or CJK (no case) [inferred]; Spectrum 2 maps CJK "emphasized" to heavier weights, not italics [S-L02-021].
  - **Direction**: RTL text right-aligned with RTL directionality; emails, URLs and phone numbers keep LTR order; Persian/Urdu charts stay LTR; media controls always LTR [S-L02-061]. Tokens and components use leading/trailing, not left/right [S-L02-061].
  - **Measure**: 40 characters for CJK vs 80 for others (WCAG 1.4.8) [S-L02-029].
- **Visual effect:** Using Latin line heights for Hindi or Telugu clips matras and stacked conjuncts or makes lines collide; too-small Devanagari looks lighter and harder to read than the Latin beside it [S-L02-006] [S-L02-056] [inferred for the "lighter" reading]. Correct metrics make multilingual screens look evenly spaced.
- **Depends on (upstream):** DC-L02-24; DC-L02-13 (line-height system must allow per-locale values).
- **Affects (downstream):** line-height tokens per locale; fixed-height components (Material: "Components with fixed heights are built for small values and may not adapt by default") [S-L02-006]; tracking and text-transform tokens; icon mirroring (L05).
- **Token encoding:** a `language-height` or locale mode on line-height tokens (Material's token module has a language height context selector) [S-L02-006]; Spectrum-style parallel `*-cjk-*` tokens [S-L02-021]; `letterSpacing: 0` override per script [inferred].
- **Platform notes:** Android renders first/last line clipping differently from web/iOS, which is riskier for tall scripts [S-L02-051] [inferred for the risk].
- **Accessibility constraints:** WCAG 1.4.12 exception: scripts that don't use a spacing property may conform using only the applicable ones [S-L02-027].
- **Default + heuristic:** Default: Medium language height for Indic and CJK (about +7% line height), Large (+30%) for Telugu and Burmese, zero tracking and no italics or all caps for non-Latin scripts. Rule of thumb: any component whose height is fixed must be tested in Hindi, Telugu, Arabic and Japanese.
- **Evidence:** [S-L02-006] [S-L02-021] [S-L02-027] [S-L02-029] [S-L02-051] [S-L02-055] [S-L02-056] [S-L02-061]

### DC-L02-26: Numerals (tabular vs proportional, lining vs oldstyle, native digits)
- **Block path:** Foundations > Typography > Details > Numerals
- **Questions the designer answers:** Should numbers line up in columns? Should digits in running text blend with lowercase (oldstyle) or stand tall (lining)? Do we show native script digits (e.g. Devanagari digits) or Western digits?
- **Options:**
  - **Tabular lining** (`tabular-nums lining-nums`; OpenType `tnum` + `lnum`): tables, prices, timers, clocks, dashboards. Material: use tabular figures in tables or where values change often, like clocks [S-L02-052] [S-L02-043].
  - **Proportional lining** (`pnum`): default in most UI fonts for general text [S-L02-043] [inferred for "default"].
  - **Oldstyle** (`onum`): digits with descenders that blend into editorial body text [S-L02-043] [S-L02-049].
  - **Slashed zero** (`zero`) for codes and IDs; fractions (`frac`, `afrc`); ordinals (`ordn`) [S-L02-043].
  - **Native digits**: native Devanagari digit counter styles are now supported in browsers, though many users prefer Latin numerals [S-L02-056].
- **Visual effect:** Tabular figures make data look orderly and stop "jitter" when numbers update [S-L02-052]; oldstyle figures look literary and warm; lining figures look modern and uniform [inferred].
- **Depends on (upstream):** DC-L02-01/05 (the font must include these OpenType features); product type.
- **Affects (downstream):** table cells, stat tiles, charts' axis labels (L05), input fields for amounts, timers.
- **Token encoding:** not in the DTCG typography composite [S-L02-032]; store as `$extensions` (e.g. `fontFeatureSettings: "tnum"`) or as component-level CSS [inferred].
- **Platform notes:** Web `font-variant-numeric` [S-L02-043]; iOS/Android expose monospaced-digit font features [inferred; not verified this session].
- **Accessibility constraints:** None beyond legibility (distinguish 0/O, 1/l) [S-L02-049].
- **Default + heuristic:** Default: proportional lining in text, tabular lining in any table or live-updating number. Rule of thumb: if a number can change while the user watches, make it tabular.
- **Evidence:** [S-L02-032] [S-L02-043] [S-L02-049] [S-L02-052] [S-L02-056]

### DC-L02-27: Typography token architecture and naming
- **Block path:** Foundations > Typography > Tokens
- **Questions the designer answers:** Do we tokenize each property separately, or bundle them into composite text styles? How many tiers? How are tokens named?
- **Options:**
  - **Property primitives only** (size, weight, line height, letter spacing, family as separate tokens): Fluent `fontSizeBase300`, `lineHeightBase300`, `fontWeightSemibold`, `fontFamilyBase` [S-L02-008]; Polaris `font-size-325`, `font-line-height-500`, `font-weight-regular`, `font-letter-spacing-dense` [S-L02-014].
  - **Primitives + composite semantic styles**: Fluent `typographyStyles.body1 = { fontFamily, fontSize, fontWeight, lineHeight }` [S-L02-008]; Polaris `text-body-md` [S-L02-014]; Primer `text.body.shorthand.medium` with DTCG `$type: 'typography'` referencing base tokens [S-L02-017]; Material `md.sys.typescale.body-medium` (one token per style) plus per-property tokens (`...-font`, `-line-height`, `-size`, `-tracking`, `-weight`) [S-L02-006].
  - **Composite with per-breakpoint or per-platform values**: Carbon style objects with `breakpoints` [S-L02-009]; Spectrum `sets: { desktop, mobile }` [S-L02-021].
  - **Naming patterns seen**: numeric scale (`font.size.200`, `fontSizeBase300`, `font-size-325`, `scale05`) vs semantic role (`text.body.medium`, `font.heading.large`, `md.sys.typescale.title-small`) [S-L02-008] [S-L02-014] [S-L02-009] [S-L02-017] [S-L02-015] [S-L02-006].
- **Visual effect:** none directly; composites keep size, line height and tracking in sync so text never ends up with mismatched leading [inferred].
- **Depends on (upstream):** overall token architecture (L07); DC-L02-07.
- **Affects (downstream):** component tokens (e.g. `button.label` aliases `text.label.large`), Figma text styles, code output (CSS classes, Compose `Typography`, SwiftUI `Font`).
- **Token encoding (DTCG 2025.10, stable):** `$type: "typography"` with `fontFamily` (fontFamily or alias), `fontSize` (dimension), `fontWeight` (fontWeight), `letterSpacing` (dimension), `lineHeight` (number, a multiplier of fontSize) [S-L02-032]. `fontFamily`: string or array [S-L02-030]. `fontWeight`: 1-1000 or aliases (thin/hairline 100 ... extra-black/ultra-black 950), other strings invalid [S-L02-032]. Dimension units: only px and rem [S-L02-032]. Not in the composite: paragraph spacing, text transform, text decoration, font features, variable axes, color [S-L02-032]. Example:
  ```json
  { "text": { "body": { "medium": { "$type": "typography", "$value": {
      "fontFamily": "{font.family.sans}",
      "fontSize": "{font.size.300}",
      "fontWeight": "{font.weight.regular}",
      "letterSpacing": { "value": 0, "unit": "px" },
      "lineHeight": 1.43 } } } } }
  ```
- **Platform notes:** Compose `Typography` and Material `TypeScaleTokens` map one-to-one to the 15 (+15 emphasized) styles [S-L02-005]; iOS should map semantic styles onto `Font.TextStyle` to keep Dynamic Type [S-L02-001].
- **Accessibility constraints:** export sizes as rem (web) and sp (Android) so user scaling works [S-L02-006] [S-L02-039]; the lineHeight multiplier survives scaling better than fixed px [inferred].
- **Default + heuristic:** Default to three tiers: primitives (family, size ramp, weight, lineHeight, letterSpacing) > semantic composites (`text.{role}.{size}`) > component aliases. Rule of thumb: name primitives by number and semantics by job; never let a component reference a raw size.
- **Evidence:** [S-L02-001] [S-L02-005] [S-L02-006] [S-L02-008] [S-L02-009] [S-L02-014] [S-L02-015] [S-L02-017] [S-L02-021] [S-L02-030] [S-L02-032] [S-L02-039]

### DC-L02-28: Figma encoding: text styles vs typography variables
- **Block path:** Foundations > Typography > Tokens > Figma
- **Questions the designer answers:** Do we define text styles only, or back them with variables so modes (brand, platform, density, locale) can switch values? Which properties can be variables?
- **Options:**
  - **Text styles only** (classic): one style per semantic role; values hard-coded [inferred].
  - **Text styles bound to variables**: number variables can drive font size, font weight (numeric), line height, letter spacing (interpreted as px, not %), paragraph indent and paragraph spacing; string variables drive font family and font style/weight name [S-L02-036]. The plugin API gained get/set bound variables for text properties on 2024-04-16 [S-L02-035].
  - **Variables with modes** for platform (desktop/mobile), brand, density or locale, switching all bound text styles at once [S-L02-036] [inferred application].
- **Visual effect:** none directly; variables let one library re-skin typography across brands and platforms without duplicating styles [inferred].
- **Depends on (upstream):** DC-L02-27; L07 Figma architecture.
- **Affects (downstream):** handoff (Dev Mode shows variable names), token export to code.
- **Token encoding:** Map DTCG primitives to Figma number/string variables and DTCG composites to text styles; Figma has no composite typography variable type [S-L02-036] [inferred from the variable types listed]. Line height in variables is a number; community reports that percent line heights are still not supported in variables (Tier C, unconfirmed) [S-L02-037]. Letter-spacing variables are px, so em-based tracking must be converted per size [S-L02-036].
- **Platform notes:** Fonts must be available to every editor for string font-family variables to resolve [S-L02-034] (Tier C, consistent with how Figma fonts work [inferred]).
- **Accessibility constraints:** Figma cannot preview Dynamic Type or Android font scaling directly; use modes to simulate large sizes [inferred].
- **Default + heuristic:** Default: primitives as variables, semantic text styles bound to them, a platform mode for size and line height. Rule of thumb: if you have more than one brand or platform, bind; if one brand on one platform, plain text styles are enough.
- **Evidence:** [S-L02-034] [S-L02-035] [S-L02-036] [S-L02-037]

## Decision graph summary (what drives what in typography)

Upstream to downstream edges for S1. "->" means "constrains or changes".

- Brand personality (L06) -> typeface classification (DC-02) -> pairing (DC-03), tracking (DC-14), weight palette (DC-15), icon style (L05), corner radius feel (L04, via rounded faces).
- Brand personality (L06) -> expressive vs productive balance (DC-11) -> scale ratio (DC-09), display weights (DC-15), display line height (DC-13), display tracking (DC-14), responsive strategy (DC-19).
- Platforms (L10) -> sourcing (DC-01) -> Dynamic Type/font-scaling behaviour (DC-21), fallback stacks (DC-24), loading budget (DC-06).
- Density (L03) -> base body size (DC-08) -> entire size ramp (DC-09) -> component heights (buttons, inputs, rows; L08) and line length (DC-17).
- Spacing grid (L03: 4pt/8pt) -> line-height snapping (DC-13) -> vertical rhythm and paragraph spacing (DC-16).
- Languages/markets -> script coverage (DC-24) -> typeface veto (DC-01/02), per-locale line heights (DC-25), tracking = 0 for Arabic/Devanagari (DC-14), fixed-height component bans (L08).
- Variable font availability (DC-04) -> in-between weights (DC-15), automatic optical sizing (reduces manual tracking, DC-14), grade per color mode (L01 dark mode).
- Accessibility targets (WCAG 1.4.4, 1.4.12, 1.4.8; HIG; Android 200%) -> scalable units in tokens (DC-27), no fixed text heights (DC-21, DC-22), fluid clamp limits (DC-19), line height floor (DC-13).
- Color roles and contrast (L01) <-> text sizes and weights (DC-23): the size/weight decides whether 4.5:1 or 3:1 applies.
- Token architecture (L07) -> type token naming and tiers (DC-07, DC-27) -> Figma text styles and variables (DC-28).

## Cross-lane notes
- [L02 -> L01] Text size and weight decide the contrast threshold: Fluent defines large text as 18.5px+ bold or 24px+ regular; Material targets 4.5:1 small / 3:1 large; Material's default text color is on-surface, links primary and underlined [S-L02-007] [S-L02-052]. Grade axis (GRAD) can offset light-on-dark text looking bolder in dark mode without reflow [S-L02-049].
- [L02 -> L03] Base body size and density should be one linked control (14px dense web vs 16-17 reading/mobile). Line heights snap to 4pt in Material/Atlassian/Polaris and 2pt in Fluent/Carbon. Primer ties title-medium's 32px line height to medium control height [S-L02-017]. Prose max width 65-70ch Latin / 35-40 chars CJK (WCAG 1.4.8: 80 / 40) [S-L02-029]. Fluid type limits: max <= 2.5x min per clamp [S-L02-041].
- [L02 -> L04] SF Pro Rounded exists to "coordinate text with the appearance of soft or rounded UI elements"; Google Sans Flex has a ROND (roundness) axis 0-100. Shape roundness and type roundness should be offered together [S-L02-001] [S-L02-026].
- [L02 -> L05] SF Symbols match SF text weights and scale with Dynamic Type; HIG says increase meaningful icon size as font size grows. Tabular figures for chart axes and data tables [S-L02-001] [S-L02-052].
- [L02 -> L06] Casing (sentence case vs title/all caps) is a voice decision: Fluent and Windows mandate sentence case [S-L02-007] [S-L02-022]. Typeface class associations (serif = editorial/trust, geometric = modern/friendly) are cultural conventions, flagged [inferred] in DC-02.
- [L02 -> L07] DTCG 2025.10 typography composite = fontFamily, fontSize, fontWeight, letterSpacing, lineHeight (number multiplier); dimension units only px/rem; open Issue 102 ("Typography type feedback") on the whole typography type, not lineHeight alone [S-V1b-002]. Paragraph spacing, text-transform, font features, variable axes, breakpoints and locale variants need `$extensions` or parallel tokens. Figma: number variables bind size/weight/line height/letter spacing (px)/paragraph spacing; string variables bind family and style [S-L02-032] [S-L02-036].
- [L02 -> L08] Components with fixed heights break under Dynamic Type AX sizes, Android 200% scaling, WCAG 1.4.12 overrides and tall scripts (Material: fixed-height components "are built for small values and may not adapt") [S-L02-001] [S-L02-006] [S-L02-027]. Buttons use Label Large in M3; emphasized styles for selected chips, unread list items, primary buttons [S-L02-006] [S-L02-052].
- [L02 -> L10] Per-platform ramps: Fluent publishes separate web/Windows/macOS/iOS/Android ramps; Spectrum 2 ships desktop vs mobile sets (mobile about 1.2x). Minimum sizes: iOS 11pt, macOS 10pt, watchOS/visionOS 12pt, tvOS 23pt, Windows 12px Regular / 14px Semibold [S-L02-007] [S-L02-021] [S-L02-001] [S-L02-022].
- [L02 -> L13/L15] Line length 45-75 (Bringhurst), 40-60 (Material), 50-60 (Windows), max 80 (Primer/WCAG AAA); hierarchy via size and weight (Carbon: a much larger light heading can outrank a smaller bold one) [S-L02-051] [S-L02-022] [S-L02-016] [S-L02-012].

## Open questions / gaps
- **Material tracking values disagree between sources.** Shipped Compose tokens (v0_103) use Roboto-era tracking (Body Large 0.5sp, Body Medium 0.2sp, Display Large -0.2sp), while the m3.material.io token module shows Google Sans / Google Sans Text with 0 tracking on most styles and 0.1pt on small ones [S-L02-005] [S-L02-006]. Which set is canonical for a non-Google product using Roboto is unclear; V1 should re-check.
- **Fluent web Subtitle 1 line height**: the Fluent 2 site says 20/26, the tokens package says lineHeightBase500 = 28px [S-L02-007] [S-L02-008].
- **Google Sans Flex in Material 3 Expressive / Android**: confirmed open-sourced (OFL) in 2025 with six axes, but I found no official statement that M3 components or Android now default to it; M3 still says Roboto is the default and Roboto Flex is not yet in the typescale [S-L02-024] [S-L02-053]. The exact release date (2025-11-18) comes only from Tier C press.
- **Spectrum 2 docs site** (s2.spectrum.adobe.com) returned 403/AccessDenied, so Spectrum guidance comes from its token source only; usage rules (e.g. when to use detail vs body) are not verified.
- **Polaris**: Polaris React docs now redirect to shopify.dev web components; values come from the polaris-tokens source on main, which may be legacy for the new web components [S-L02-013] [S-L02-014].
- **Figma**: percent line height in variables still appears unsupported (Tier C forum evidence only); variable-font axis control in Figma was not verified; Figma MCP was unavailable to this lane [S-L02-037].
- **Mobile web 16px minimum / iOS Safari input zoom** could not be verified against a primary source (web-search budget exhausted) [S-L02-064].
- **Indic specifics are thin in standards**: W3C ilreq is a 2020 working draft with little on metrics; Material's language height categories are the best quantitative source. No official per-script size-adjustment values (e.g. how much larger Devanagari should be than Latin at the same nominal size) were found.
- **Dyslexia**: BDA's own 2023 guide was blocked (403/404); the Ako Aotearoa 2023 derivative was used. Research on dyslexia-specific fonts (e.g. whether OpenDyslexic helps) was not reviewed.
- **Classification-to-personality mapping** (geometric = friendly, serif = trust, etc.) is conventional practice; the only Tier B evidence found says associations are cultural and time-bound, not a fixed mapping [S-L02-047].
- Not covered in depth: hyphenation and widows/orphans, hanging punctuation, vertical CJK typesetting, text on images, and email-client font support.

## Confidence
- **Confirmed from Tier A primary sources (high):** all Apple Dynamic Type sizes, minimums and SF/NY tracking tables [S-L02-001]; Material 3 baseline and emphasized sizes, line heights, weights, the Major Second statement, brand/plain typefaces, language height categories [S-L02-005] [S-L02-006] [S-L02-052] [S-L02-053]; Fluent 2 ramps for five platforms and token values [S-L02-007] [S-L02-008]; Windows Segoe UI Variable axes, ramp, minimums, 50-60 characters [S-L02-022]; Carbon scale formula, all style values and the productive/expressive definitions [S-L02-009] [S-L02-011] [S-L02-012]; Polaris, Primer and Spectrum 2 token values from their official repositories [S-L02-014] [S-L02-017] [S-L02-021]; Atlassian tokens [S-L02-015]; WCAG 1.4.4, 1.4.8, 1.4.12 [S-L02-027] [S-L02-028] [S-L02-029]; DTCG 2025.10 typography, fontWeight and dimension definitions [S-L02-032]; Figma variable-to-text-property bindings [S-L02-036]; Android 14 nonlinear scaling [S-L02-039]; MDN CSS features and Baseline status [S-L02-043] [S-L02-044] [S-L02-045] [S-L02-055]; Google Fonts metadata (axes, subsets) [S-L02-026].
- **Computed (high, arithmetic on confirmed values):** Material and Spectrum 2 sizes match base x 1.125^n rounding; the ratio examples in DC-09; Spectrum mobile/desktop about 1.2x.
- **Tier B (medium-high):** Google Fonts Knowledge guidance on pairing, measure, line height, tracking, grade, legibility, language support [S-L02-046] to [S-L02-051]; Utopia defaults [S-L02-040]; Smashing's 2.5x fluid-type rule [S-L02-041]; web.dev font loading [S-L02-042]; Ako dyslexia guide [S-L02-059]; Tim Brown modular scales [S-L02-060].
- **Inferred (medium-low, labelled [inferred] in the cards):** the visual-effect readings of typeface classes, ratios and weights; default heuristics and rules of thumb; token naming suggestions for locale/breakpoint modes; the mobile-web 16px rule.
