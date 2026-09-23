# Levers: what makes a design system look which way

Synthesis S1c. Audience: engineers building or using the design-system builder. Machine-readable twin: `synthesis/levers.json`. Causal narrative: `synthesis/DECISION-GRAPH.md`.

**How to read the tags.** `DC-Lxx-nn` points to a Decision Card in `research/` or `benchmarks/`. `S-Lxx-nnn` points to a source in that lane's trace. `[inferred]` means this synthesis made the link or chose the number; treat it as a default to test, not a finding. Most anchor values below are sourced; most interpolations between anchors are inferred.

**The design in one paragraph.** The builder asks for a few raw inputs (brand color, typeface, base size, platforms, contrast target) and exposes eight dials, each 0 to 100, where 50 is a sensible system default (the convention L06 uses for its lever matrix, section 4.2). Three dials set the overall posture and match the axes of the L09 personality map: **Expression**, **Brand presence** and **Density** (DC-L09-01 to DC-L09-07, L09 section A3). Five dials tune character and default to values implied by the first three: **Energy**, **Roundness**, **Depth**, **Colorfulness** and **Warmth**. Brand adjectives such as "playful" or "premium" are not dials; they are **macros** that nudge several dials at once (L06 lever matrix rows A to G). Style presets (flat 2.0, tonal, glass, neo-brutalist) are named dial settings (DC-L15-01).

---

## A. Input dials

### A0. Why these eight, and what was merged

| Dial (0 to 100) | Merges these research levers | Why it is its own dial |
|---|---|---|
| 1. **Expression**: productive to expressive | L06 row C (minimal/rich), DC-L06-03 hero-moment budget, L09 X axis, DC-L02-11 productive vs expressive type, DC-L15-02 hierarchy strength, DC-L15-03 emphasis budget | Carbon and Material each flip type, motion and emphasis together with one productive/expressive switch [S-L06-001][S-L06-002][S-L06-009] |
| 2. **Brand presence**: native to brand-led | L06 row G (bold/deferential), DC-L06-14, DC-L10-02, L09 Y axis, DC-L13-17 | It is the vertical axis of the L09 map and the root of platform posture (DC-L10-02, fan-out 9) |
| 3. **Density**: spacious to compact | DC-L15-04 density voice, DC-L03-10/11 density modes, DC-L02-08 body size, DC-L09-04 | L09 found density to be a second independent axis (13-14px dense, 16px regular, 17px+ large) |
| 4. **Energy**: calm to energetic | L06 row D, DC-L06-10, DC-L04-19 to DC-L04-22 | Motion bounce and saturation move together in L06 row D; Material's standard vs expressive springs are the cleanest anchors [S-L04-004] |
| 5. **Roundness**: sharp to soft | DC-L04-02 ("the shape personality dial"), DC-L06-09, DC-L09-01, DC-L05-02 | Radius is the most divergent visible lever in the benchmark (0px to pill; median 6px) |
| 6. **Depth**: flat to deep | DC-L04-10, DC-L04-12, DC-L09-02, DC-L15-01 style preset | L09 found four depth models (borders, rings, tonal, shadows, plus materials) |
| 7. **Colorfulness**: monochrome to vivid | DC-L01-10 chroma level, DC-L06-05 scheme variant, DC-L06-04 brand color role, DC-L15-06 | Material's scheme variants already form a colorfulness dial (Monochrome to Vibrant) [S-L06-083][S-L01-010] |
| 8. **Warmth**: cool/formal to warm/friendly | L06 row B, DC-L01-06 neutral temperature, DC-L06-06 (Linear's warmer gray) | Linear's 2026 "calmer interface" moved warmth and border softness together [S-L06-067]; L15 lists neutral temperature as an exposed control (P45) |

Dropped as dials and turned into macros: playful/serious (row A), premium/everyday (row E) and modern/heritage (row F). Each of these is a combination of the eight dials plus a typeface suggestion, so a separate dial would double-count [inferred].

**Dial coupling.** When a user has not touched a character dial, it follows the posture dials: Roundness, Colorfulness and Energy default to `50 + 0.5 x (Expression - 50)` and Depth to `40 + 0.5 x (Expression - 50)`, with the materials band only when Expression is above 60 and the platform supports materials; Colorfulness also moves `0.3 x (Energy - 50)`, because L06 row D ties saturation to energy; Density pulls Roundness down by up to 10 points [inferred; direction from L04's graph note that density pushes toward sharper radii and thinner strokes, and from the L09 X rubric that sums radius, surface color, motion and material into one expressiveness score]. Touching a dial detaches it from the coupling.

### A1. Expression (productive 0 to expressive 100)

Definition: how much the interface performs on everyday screens. Productive keeps attention on the task; expressive adds emphasis, variety and hero moments.

| Foundation | Parameter | Productive end (0-33) | Middle (34-66) | Expressive end (67-100) | Evidence |
|---|---|---|---|---|---|
| Type | Scale ratio (hierarchy strength) | 1.125-1.2 | 1.25 | 1.333+ | DC-L15-02, DC-L02-09 |
| Type | Emphasized style variants | off | off | on (Material's 15 emphasized styles) | DC-L02-11 [S-L02-006] |
| Type | Weight palette | 2 weights (400/600, Windows 11) | 3 weights (400/500-600/600-700) | 3-4 weights, heavier display | DC-L02-15; band cut-offs [inferred] |
| Emphasis | Hero-moment budget | none; productive only | productive plus expressive moments (new page, primary action, alerts) | 1-2 hero moments per product, expressive tactics throughout | DC-L06-03 [S-L06-002][S-L06-009] |
| Emphasis | Primary actions per view; accent use | 1; accent only on actions, selection, status | 1 primary + 1 highlighted secondary; accent on links and nav | expressive; large color areas allowed on chrome | DC-L15-03 |
| Color | Brand color role | reserved accent | reserved accent + optional signature surface | brand-flooded chrome allowed | DC-L06-04 |
| Layout | Containment | whitespace instead of containers | mixed | visible containers for emphasis (M3 tactic 4) | L06 row C [S-L06-080][S-L06-009] |
| Shape | Shape variety | one radius family | one family | mixed shapes and shape morph, hero moments only | DC-L06-09, DC-L04-06 |
| Motion | Where expressive motion is used | nowhere | significant moments | throughout, with springs | DC-L04-19 [S-L04-075][S-L04-060] |
| Icons | Style at rest | outlined | outlined, filled when selected | filled, colored or dimensional icons allowed | DC-L05-02, L06 row C [S-L06-062] |

Caveat carried from L06: Google found a strong minority prefers calm designs and warned expressive UI may not suit banking [S-L06-010]; NN/g measured tone effects of only 0.5-1 point on a 5-point scale [S-L06-013]. Extreme settings rarely help.

### A2. Brand presence (native 0 to brand-led 100)

Definition: how much the product looks like the brand versus like the platform it runs on. The dial is calibrated to the L09 Y score times 10 (typeface ownership, fixed accent, own look, re-skin lock, voice guidance).

| Foundation | Parameter | Native end | Hybrid (about 50) | Brand-led end | Evidence |
|---|---|---|---|---|---|
| Type | Typeface suggestion | OS system font per platform (Fluent uses SF Pro on Apple, Roboto on Android) | open neutral face (Inter, Roboto) | proprietary or custom face (Plex, Cereal, Spotify Mix) | L09 Y rubric, DC-L06-07, DC-L02-01 [S-L06-098] |
| Color | Brand color placement | accent only for primary actions and status; brand color in the content layer | accent plus one signature surface | brand color on large surfaces and custom components | L06 row G [S-L06-008], DC-L10-04 |
| Components | Share of native components | system components almost everywhere | native 80% of the time, 20% "signature experiences" | one custom look on every platform (CRED NeoPOP) | DC-L06-14 [S-L06-043][S-L06-112] |
| Shape, depth | Who wins on corners and materials | platform (iOS continuous and concentric corners, Liquid Glass, M3 shape scale) | platform on system chrome, brand elsewhere | brand radii and surfaces everywhere | DC-L06-09 platform note [inferred], DC-L10-12 |
| Behavior | Navigation, back, sheets, pickers | always native | always native | always native (guardrail) | DC-L10-02 rule of thumb [S-L10-009] |
| Content | Voice guidance in the system | none | short | full voice and illustration guidance | L09 Y rubric (voice point) |

### A3. Density (spacious 0 to compact 100)

Definition: how much information fits on a screen, and how airy or utilitarian it feels. Spacious reads calm and premium; compact reads serious and efficient (Material, quoted in DC-L03-24 [S-L03-028]).

| Foundation | Parameter | Spacious (0-33) | Comfortable (34-66) | Compact (67-100) | Evidence |
|---|---|---|---|---|---|
| Type | Web body size | 16 (19 at 0-10, GOV.UK level) | 16 for content products, 14 for work tools | 14; 13 at 90+ (Polaris, SLDS) | DC-L02-08, L09 density axis |
| Type | Line height of body | long-form ratio (about 1.5) | 1.5 | compact variant (Carbon 14/18 vs 14/20) | DC-L02-13 [S-L02-011] |
| Type | Ratio cap | none | none | 1.2 maximum | DC-L02-09 ("1.125-1.2 for dense apps") |
| Space | Semantic density mode | one ladder step looser | default | one ladder step tighter (about 4px per step, Material density -1 to -3) | DC-L03-10, DC-L03-11 [S-L03-029] |
| Space | Inner:outer spacing ratio | 1:3 to 1:4 | 1:2 to 1:3 | 1:2 | DC-L03-24 [inferred] |
| Components | Default control height | 48 (touch 44-48) | 40 | 32 (24 for pointer-only tools) | DC-L03-07, L09 density axis |
| Icons | Default icon size | 24 | 20 | 16 (paired with 14px text, Carbon, Atlassian) | DC-L05-05 [S-L05-016][S-L05-021] |
| Signifiers | Minimum signifier strength | minimal allowed | balanced | strong (denser layouts need stronger grouping and signifiers) | DC-L15-04, DC-L15-09 [S-L15-004] |
| Floors | Target size | unchanged | unchanged | unchanged: density shrinks visuals, never hit areas | DC-L03-12, L14 invariant I-1 |

### A4. Energy (calm 0 to energetic 100)

Definition: how lively the interface feels in motion and intensity. Calm is quiet and fast; energetic is visible, springy and saturated.

| Foundation | Parameter | Calm end | Default (50) | Energetic end | Evidence |
|---|---|---|---|---|---|
| Motion | Spring damping ratio (spatial) | 1.0 from 0 to 33, no overshoot (Apple default `dampingFraction 1.0`) | 0.9 (M3 standard) | 0.8 at 75 (M3 expressive default); 0.6 at 100 (M3 expressive fast, playful only) | F3 in L04 [S-L04-003][S-L04-004][S-L04-037]; interpolation [inferred] |
| Motion | Spring stiffness (spatial default) | 700 | 700 | 380 at 75 and above (M3 expressive default) | [S-L04-004] |
| Motion | Easing curve (web, and wherever springs are not used) | Carbon productive (0.2, 0, 0.38, 0.9) | standard (0.2, 0, 0, 1) | Carbon expressive (0.4, 0.14, 0.3, 1). When damping is below 1, the web gets the spring sampled into CSS `linear()` (Airbnb, Atlassian); overshoot beziers (Geist 1.1, Gestalt 1.25, Blade 1.5 as the y2 value) are the fallback | DC-L06-10 [S-L06-002], DC-L04-21, M8 in L09 |
| Motion | Duration multiplier on the ladder | 0.8 (Linear-style 100/180ms) | 1.0 | 1.2 for medium and long steps | anchors [S-L09-656][S-L09-102]; multiplier [inferred] |
| Color | Added saturation | lower (TonalSpot, Neutral) | none | higher (Vibrant); saturation raises perceived excitement | L06 row D [S-L06-083][S-L06-072] |
| Type | Heading weight | lighter ("calm as a whisper") | 600 | heavier ("loud and rugged") | [S-L06-031] |
| Chrome | Navigation brightness | recessive (Linear's dimmer sidebar) | neutral | colored app bars and FABs, when Expression allows brand chrome | [S-L06-067][S-L06-011] |
| Haptics | Intensity | light | medium | matched to the animation's energy | DC-L04-26 [S-L04-043] |

### A5. Roundness (sharp 0 to soft 100)

Definition: the corner radius of the default control, and everything that follows from it.

| Dial value | Control radius | Systems at this setting | Evidence |
|---|---|---|---|
| 0-12 | 0 | Carbon v11, GOV.UK | M6 in L09 |
| 13-25 | 2 | Fluent below 32px tall | [S-L04-007] |
| 26-37 | 4 | Fluent, USWDS, Radix, Chakra, Encore | M6 in L09 |
| 38-47 | 6 | Atlassian, Primer, Ant, Geist (benchmark median) | M6 in L09 |
| 48-60 | 8 | Polaris, Paste, Uber, Blade, Mantine v9, shadcn | M6 in L09 |
| 61-80 | 12 | Airbnb | M6 in L09 |
| 81-92 | 16 | (no benchmarked system uses 16 on controls; it is Atlassian's xxlarge role and a Carbon v12 token step) | L09 M6, DC-L04-03 |
| 93-100 | full (pill) | Material 3, Spectrum 2, SLDS Cosmos, Gestalt classic | M6 in L09 |

It also drives: container and overlay radii, the nested-radius rule and focus-ring radius (section B5); icon corner style and caps, rounded icons at 61+ and sharp icons at 12 or below (DC-L05-02 [S-L05-003]; caps [inferred]); and a typeface suggestion of rounded or geometric sans at 81+ (Google Sans Flex roundness "personal, playful" [S-L06-031]). The benchmark trend is rounder: Carbon 0 to 4, Mantine 4 to 8, SLDS 4 to pill, Spectrum sharp to pill [S-L09-258][S-L09-646][S-L09-237][S-L09-228].

### A6. Depth (flat 0 to deep 100)

Definition: how strongly surfaces separate in the third dimension. The scale is ordinal: each band is a different depth model, ordered by how much visual depth it shows.

| Band | Depth model | Recipe | Systems | Evidence |
|---|---|---|---|---|
| 0-15 | Borders only | 1px borders, no shadows | GOV.UK, Primer (borders first) | M7 in L09 |
| 16-35 | Ring plus faint shadow | 1px alpha ring + extra-small shadow | shadcn (`ring-1 ring-foreground/10 shadow-xs`), Geist, Radix | [S-L09-591][S-L09-618][S-L09-559] |
| 36-55 | Tonal layers | surfaces stepped by lightness; one shadow for floating UI | Carbon, Material 3, Linear, Encore | DC-L04-10, M7 |
| 56-80 | Shadow ladder | key + ambient shadows, 3-8 levels | Fluent 2, Polaris, Uber | DC-L04-12 [S-L04-008] |
| 81-100 | Materials and glass | translucent, blurred layers for controls and navigation only, with a solid fallback | Apple Liquid Glass, Fluent Acrylic | DC-L04-15 [S-L15-073] |

Within a band, the dial scales shadow opacity from 8% to 24% in light mode (DC-L04-12 default). In every band, dark mode lifts raised surfaces by lightness, because every benchmarked system with dark mode does (M7 pattern in L09).

### A7. Colorfulness (monochrome 0 to vivid 100)

Definition: how much chroma the generated palette carries and how much of the screen it covers.

| Dial | Accent chroma (HCT units) | Scheme variant emitted | Surfaces | Evidence |
|---|---|---|---|---|
| 0 | 0 | Monochrome | neutral | [S-L01-010] |
| 20 | 8-12 | Neutral | neutral | [S-L01-010] |
| 50 | 32-36 | TonalSpot (default, "low to medium colorfulness") | neutral + one accent | [S-L01-010][S-L06-083] |
| 75 | 48 light / 36 dark | Expressive | tinted containers | [S-L01-010] |
| 100 | gamut maximum | Vibrant | brand or dynamic color on surfaces | [S-L01-010] |

Also driven: accent count (one accent below 60, secondary and tertiary accents above; DC-L01-08, DC-L15-06); whether text may use the accent ramp (Radix: gray text reads "functional", accent text "colorful" [S-L01-053]). A raw flag **brand hue must be exact** switches to Material's Fidelity behavior at any colorfulness [S-L06-083]; the accent ramp then peaks at the brand color's own chroma, and the dial governs only surfaces, secondary palettes and accent count. This is how Carbon keeps a vivid IBM Blue on otherwise gray screens [inferred]. Guard: keep large areas low in chroma and spend chroma on small, high-meaning elements (DC-L01-10 [S-L01-013][S-L01-033]).

### A8. Warmth (cool/formal 0 to warm/friendly 100)

Definition: the temperature of the neutrals and the formality of the details around them.

| Foundation | Cool/formal end | Middle (50) | Warm/friendly end | Evidence |
|---|---|---|---|---|
| Neutral ramp tint (OKLCH at step 500) | slate: chroma 0.046, hue 257; gray: 0.027, 264; zinc: 0.016, 286 | pure gray, chroma 0 (or hue-matched to the brand if that flag is on) | stone: 0.013, hue 58; taupe: 0.021, 43; olive: 0.031, 107 | DC-L01-06 [S-L01-062] |
| Tint at the ramp ends | chroma 0-0.008 at steps 50 and 950 | same | same | DC-L01-06 [S-L01-062] |
| Borders | stronger rules and dividers | default | softer borders (Linear 2026) | [S-L06-067]; cool end [inferred] |
| Capitalization default | title case ("generally considered formal") | sentence case | sentence case ("more casual") | [S-L06-052] |
| Contractions in UI copy | none ("cannot", GOV.UK) | allowed | encouraged, "we/you" in errors | [S-L06-048][S-L06-056] |
| Typeface suggestion | grotesque or serif | neutral sans | humanist or rounded sans (SF "friendly", Segoe "friendly and legible") | [S-L06-113][S-L06-098]; cool end [inferred] |

Warmth never moves the brand hue, which is a raw input. When no brand color is given, the builder can suggest hues: blue reads competent and red reads exciting (Labrecque and Milne [S-L06-072]).

### A9. Macros: brand adjectives as dial moves

Each macro adds the listed offsets to the current dial values and sets the listed suggestions. Offsets are [inferred]; the directions come from the cited L06 row. When two macros push the same dial in opposite directions, the builder shows the conflict and lets the design principles decide, rather than averaging silently (L06 section 4.2 usage note).

| Macro | Dial offsets | Other settings | Direction source |
|---|---|---|---|
| Playful | Expression +20, Energy +20, Roundness +30, Colorfulness +25 | rounded display face; characters in empty and error states; casual voice | L06 row A [S-L06-009][S-L06-011][S-L06-073][S-L06-026] |
| Serious | Expression -20, Energy -20, Roundness -25, Colorfulness -25 | neo-grotesque or humanist sans; pictograms or no illustration; no bounce | L06 row A [S-L06-001][S-L06-002] |
| Friendly | Warmth +30, Roundness +15 | sentence case; people imagery | L06 row B [S-L06-062][S-L06-052] |
| Authoritative | Warmth -25, Roundness -20 | title case allowed; strong rules | L06 row B [S-L06-023][S-L06-003] |
| Minimal | Expression -25, Colorfulness -20 | fewer, smaller, outlined icons | L06 row C [S-L06-067][S-L06-088] |
| Rich | Expression +25, Colorfulness +20 | brand shapes as graphic devices | L06 row C [S-L06-009][S-L06-030] |
| Premium | Depth +25 (toward materials), Colorfulness -20, Density -20 | taller type proportions; one deep accent | L06 row E [S-L06-031][S-L06-100]; most cells [inferred] |
| Everyday | Depth -20, Colorfulness +15, Density +15 | sturdy, tall x-height face | L06 row E [S-L06-021]; most cells [inferred] |
| Modern | none | perceptual ramps (OKLCH or LCH); geometric or grotesque sans; mono companion face | L06 row F [S-L06-012][S-L06-035][S-L06-031] |
| Heritage | none | serif or slab display face; hand-picked palette | L06 row F [S-L06-028][S-L06-078]; palette [inferred] |
| Bold | Brand presence +30 | custom face everywhere | L06 row G |
| Deferential | Brand presence -30 | native type per platform; accent only | L06 row G [S-L06-008][S-L06-098] |

### A10. Style presets as named dial settings

Style presets from DC-L15-01, written as dial values [inferred placement; the levers of each style are sourced in L15 section 1.10].

| Preset | Expr | Energy | Round | Depth | Color | Notes |
|---|---|---|---|---|---|---|
| Flat 2.0 (default) | 40 | 35 | 45 | 25-40 | 40 | durable base of Carbon, Primer, Polaris, Fluent [S-L15-009] |
| Material tonal | 70 | 70 | 95 | 45 | 70 | tonal surfaces, springs, pills |
| Glass | 50 | 40 | 70 | 90 | 35 | controls and navigation only; 35% dimming layer under clear glass over bright content [S-L15-073] |
| Neo-brutalist | 70 | 60 | 0-10 | 0 + offset shadow | 80 | thick borders, solid 4px offset shadow, 2-3 bold colors, 24-32px padding [S-L15-006] |
| Soft / neumorphic | 40 | 30 | 80 | special | 20 | shown only with a contrast warning (fails 3:1 non-text by design) [S-L15-060] |
| Maximal | 95 | 85 | any | any | 95 | marketing surfaces only; too much complexity costs appeal more than too little [S-L15-047] |

---
## B. Generation formulas: from dials and raw inputs to tokens

### B0. Raw inputs

| Input | Default when missing | Why it is raw, not a dial | Evidence |
|---|---|---|---|
| Brand color (one hex) | none; builder offers hues | Blade builds a full light and dark theme from `createTheme({ brandColor })`; Material from one source color | DC-L06-06 [S-L06-094][S-L06-082] |
| Optional: primary-action color, neutral base, second accent | derived | Primer uses a green primary button with a blue accent; Linear uses base + accent + contrast | M3 in L09 [S-L09-331], [S-L06-012] |
| Contrast target | WCAG 2.2 AA; AAA in high-contrast mode | Linear's contrast input produces accessible high-contrast themes | DC-L01-22 [S-L06-012] |
| Typeface(s): text face, display face (may be the same) | platform system font | Apple, Google and Linear split display and text faces | L06 section 3 patterns, DC-L02-01 |
| Base body size | from Density and platform | 13-19px across the benchmark | DC-L02-08 |
| Base spacing unit | 4 | GOV.UK is the one system on 5 | DC-L03-01 [S-L09-508] |
| Platforms and input types | web, pointer + touch | platform posture and target sizes key off it | DC-L10-01, DC-L14-03 |
| Marketing or editorial surfaces in scope | no | controls display-size reach (see B6) | DC-L02-11 |
| Product type: work tool, content, marketing | work tool | picks 14 or 16px body in the comfortable band | DC-L02-08 |
| Focus color | derived from the accent | GOV.UK uses a fixed yellow #ffdd00 | L09 M12 |
| Flags: brand hue must be exact; tint neutrals toward brand; motion off; dark mode on | off, off, off, on | binary choices | DC-L06-05, DC-L01-06, M8/M9 in L09 |

### B1. Color ramps from one brand color

Three construction rules exist in real systems (DC-L01-03, L09 M3):

| Rule | What a step number means | Real parameters | Strength | Weakness |
|---|---|---|---|---|
| **Tone-based** (Material HCT) | equal perceived lightness across hues; tone difference drives contrast | tones 0-100; primary = tone 40 light / 80 dark; primary-container = 90 / 30; on-primary = 100 / 20; surface 98 / 6 (2021) or 4 (2025 phone); tones 50 vs 98 give 3:1 and 30 vs 98 give 7:1 | one seed makes 5 palettes and 26 roles at 3 contrast levels | contrast guarantees come from tone distance, not step names | [S-L01-006][S-L01-010] |
| **Step-purpose-based** (Radix, Primer, Geist) | each step has a job | Radix 1-2 backgrounds; 3/4/5 component background normal/hover/pressed; 6/7/8 borders subtle/interactive/strong; 9 solid (peak chroma); 10 solid hover; 11 low-contrast text; 12 high-contrast text; steps 11 and 12 guarantee APCA Lc 60 and Lc 90 on step 2 | tokens need no extra semantic layer | hand-tuned per hue; hard to regenerate from a new brand color | [S-L01-002][S-L01-027] |
| **Contrast-based** (Spectrum with Leonardo, USWDS, Stripe) | equal contrast against the background at each step, across hues | Spectrum: every 700 = 3.01:1, every 900 about 5.07:1, every 1000 about 6.7:1 against gray-100; USWDS grade difference 40 = AA large, 50 = AA, 70 = AAA; Stripe 5 levels apart = 4.5:1, 4 apart = 3:1 | any recolored accent passes the same pairings | needs a solver; hues can look uneven in chroma | [S-L01-035][S-L09-547][S-L01-044] |

**Builder default: contrast-indexed steps with purpose bands, generated in OKLCH** (HCT when the output must feed Material dynamic color). DC-L01-01 and DC-L01-03 recommend exactly this pairing for a builder that lets users recolor the accent.

Algorithm [inferred assembly of sourced rules]:
1. Convert the brand color to OKLCH (or HCT). Keep its hue H.
2. Build 12 steps with Radix's jobs. Fix three steps by contrast against the light background: step 8 (strong border, focus) at 3:1 for WCAG 1.4.11, step 11 (secondary text) at 4.5:1 and step 12 (primary text) at 7:1 (WCAG 1.4.3 and 1.4.6 thresholds, DC-L01-22). Solve lightness for each target. Space steps 1-7 evenly in lightness between the background and step 8 [inferred].
3. Set chroma per step as `accentChroma x curve(step)`: peak at step 9, falling toward both ends, clamped to the target gamut (Radix peak at 9 [S-L01-002]; HCT chroma limits at extreme tones [S-L01-006]). `accentChroma` comes from the Colorfulness dial (A7): HCT 0 / 8-12 / 32-36 / 48 / max, or in OKLCH roughly 0 up to 0.21-0.25 (Tailwind blue-500 0.214, red-600 0.245 [S-L01-062]).
4. Anchor the brand: place the brand color at the step closest in lightness. Map `bg.brand` to the nearest step that gives 4.5:1 with white or black text. If the brand color gives under 3:1 with white, use it as a fill with dark text or as a tint only (DC-L01-09). Auto-pick the on-color foreground, as Blade does [S-L06-094].
5. With the "brand hue must be exact" flag, keep the input color itself in the container role (Material Fidelity) and derive the rest around it [S-L06-083].
6. Secondary and status hues use the same solver, so step-distance guarantees hold for every hue. Harmonize static colors toward the primary hue if wanted (Material `harmonize()` [S-L01-057]).

### B2. Neutral tinting

`neutral.hue = warmth-derived hue` (A8) or the brand hue when the tint-toward-brand flag is on (Radix pairs grays to accent families; Material derives neutral palettes from the source hue) [S-L01-053][S-L01-010]. `neutral.chroma(step) = tint x curve(step)`, with tint 0.01-0.03 OKLCH at the middle steps and 0-0.008 at the ends (DC-L01-06 [S-L01-062]); Material's TonalSpot uses HCT chroma 5-6 for neutral and 8-8.5 for neutral variant [S-L01-010]. Use pure gray (chroma 0) for image- and data-critical tools, as Spectrum does to avoid misread colors [S-L01-036]. Neutrals get 12-13 steps plus alpha variants (DC-L01-02, DC-L01-07).

### B3. Roles and interaction states

Roles alias ramp steps (primitive > semantic > component; DC-L01-26, DC-L06-04): `color.bg` = neutral 1, `color.surface.subtle` = 2, component backgrounds = 3/4/5, borders = 6/7/8, `color.action.primary.bg` = brand 9, hover = 10, `color.text.secondary` = neutral 11, `color.text.primary` = neutral 12. Three text tiers with guaranteed contrast are automated (L15 P04).

States (DC-L01-17): hover = +1 step and pressed = +2 steps toward higher contrast with the surface. When the color is unknown at design time (user themes), fall back to Material state layers: hover 8%, focus 10%, pressed 10%, drag 16% of the on-color; disabled container at 12% and content at 38% [S-L01-005][S-L01-064]. Focus changes stroke, not fill (Fluent, Carbon 2px) [S-L01-033][S-L01-029].

### B4. Dark mode mapping

Dark mode is always a separate mapping, never an inversion (Apple: dark colors "aren't necessarily inversions" [S-L01-014]; no benchmarked system ships a pure inversion, DC-L01-18).
1. Generate a separate dark neutral ramp against the dark background with the same contrast targets; Spectrum's dark themes target higher ratios [S-L01-036].
2. Map by role, not by value: for each semantic token pick the dark step that keeps the light-mode contrast relationship. Shortcuts: Atlassian's mirror (700 in light becomes 400 in dark; 100 becomes 1000) [S-L01-031]; Material's tone reassignment (40 to 80, 100 to 20, 90 to 30, 98 to 6 or 4) [S-L01-010].
3. Dark base between #121212 and #1a1a1a (tone 4-6) with the warmth tint; accents one or two steps lighter and lower in chroma (Material 2025 TonalSpot primary chroma 32 in light, 26 in dark on phone) (DC-L01-19).
4. Raised surfaces get lighter: four surfaces with 3-5% lightness steps (Atlassian #18191A, #1F1F21, #242528, #2B2C2F; DC-L04-13 [inferred step size]).
5. Shadows double their opacity and overlays gain a 1px light ring (DC-L04-12).
6. Offer a "dimmed" dark theme only for long reading at night (Primer dark dimmed) [inferred audience rule].

### B5. Contrast checks

Every foreground/background pair is tested in every mode at build time (DC-L01-22):
- **Enforced:** WCAG 2.2 SC 1.4.3 text 4.5:1, large text (24px, or 18.66px bold) 3:1; SC 1.4.11 UI boundaries and meaningful graphics 3:1; no rounding (4.499:1 fails) [S-L01-022][S-L01-023].
- **High-contrast mode:** AAA 7:1 text, 4.5:1 large (Primer, Material high contrast) [S-L01-025][S-L01-027]; Material contrast levels target `on_surface` at 4.5, 7, 11 and 21 [S-L01-010].
- **Advisory only:** APCA Lc 75 body minimum, Lc 60 other text, Lc 45 large text, Lc 30 placeholder and disabled, Lc 15 non-text [S-L01-026]. WCAG 3 is still a Working Draft (10 Sep 2026) with its contrast method undetermined, so APCA is not a conformance target [S-L01-021].
- **Published guarantee:** because steps are contrast-indexed, the builder can print a step-distance table like Carbon's and Stripe's ("any text step on any background step 1-3 passes 4.5:1") [S-L01-029][S-L01-044].

### B6. Type scale

`size(n) = base x ratio^n`, for n from -2 up to N, rounded to the nearest whole pixel (DC-L02-09).
- **Check against real systems (recomputed this session):** 14 x 1.125^n rounded to the nearest pixel gives every Spectrum 2 desktop size (10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 51, 58, 65, 73) and 17 x 1.125^n gives every mobile size (17 to 88) [S-L02-020][S-L02-021]. Material's 16, 22, 28, 32, 36 and 45 also match; its 24 is hand-placed and its Display Large 57 sits 1px below the rounded value (14 x 1.125^12 = 57.54) [S-L02-005]. Ant rounds to even pixels instead [S-L09-407].
- **Ratio** comes from Expression, capped by Density (A1, A3): 1.125-1.2 productive or dense, 1.25 balanced (the L15 default), 1.333+ editorial (DC-L15-02).
- **Display reach N** comes from the marketing-surfaces input, not from Expression. In the benchmark the largest display-to-body ratios belong to productive systems that ship marketing display sets: Carbon 92/14, Uber 96/16, Fluent 68/14, Geist 72/14; product-only scales stay near 2-3x (Apple 34/17, Atlassian 32/14, Primer 40/14) (M4 and A3 in L09). Product-only: top display about 2.5x body; with marketing: 4.5-6.5x [inferred bands from those values].
- **Steps:** 8-10 sizes and 12-15 styles; merge adjacent sizes less than about 10% apart (DC-L02-10).
- **Alternatives the builder should offer:** Carbon's additive formula (`X(n) = X(n-1) + (INT((n-2)/4) + 1) x 2` from 12px) [S-L02-012]; Ant's `14 x e^(i/5)` rounded to even [S-L09-407]; fluid two-keyframe scales (Utopia: ratio 1.2 at 18px on small screens to 1.25 at 20px on large) [S-L02-040].
- **Base size by platform** when Brand presence is below 50: iOS 17pt, macOS 13pt, Android 14sp (Body Medium) or 16sp (Body Large), watchOS 16pt, tvOS 29pt (DC-L02-08, DC-L14-04).

### B7. Line height, tracking, weight and scripts

- **Line height:** ratio by size, rounded to the nearest 4px: about 1.5 for 12-16px, 1.4 for 18-24px, 1.25 for 28-40px, 1.1-1.15 for 48px and up (DC-L02-13). Compact density adds a tighter variant for short text in components (Carbon 14/18 vs 14/20) [S-L02-011].
- **Tracking in em:** 0 at body sizes; +0.02 to +0.05em at 11-12px and for all caps; -0.01 to -0.02em from about 32px (DC-L02-14). Brand-led systems go further (Geist -0.06em at 40-72px [S-L09-625]).
- **Weights:** three by default (400 body, 500-600 labels, 600-700 headings); light 300 only at 32px and up (DC-L02-15). Energy moves heading weight (A4). Adjacent hierarchy levels differ by at least about 10% in size or 200 in weight (DC-L15-02; the 200 is [inferred]).
- **Per-script adjustments** (DC-L02-25): line height +7% for Arabic, Bangla, Chinese, Hindi, Japanese, Korean, Thai, Vietnamese and most non-Latin scripts; +30% for Burmese and Telugu; +100% for Nastaliq (Material language heights [S-L02-006]). CJK line height 1.5 headings / 1.7 body against Latin 1.3 / 1.5, and CJK sizes one step smaller (Spectrum 2 [S-L02-021]). Tracking is zeroed for Arabic and Devanagari [S-L02-055][S-L02-056]. Emphasis uses weight, not italics or all caps, for scripts without case.

### B8. Spacing scale from a base unit

`space = unit x [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]`, dropping non-integer values. With unit 4 this is Atlassian's exact set (0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80), the default in DC-L03-02; with unit 5 it gives GOV.UK's 0, 5, 10, 15, 20, 25, 30, 40, 50, 60 [S-L09-508] (the multiplier list is an [inferred] generalization). It contains the nine steps 4, 8, 12, 16, 24, 32, 40, 48, 64 that 17 of 22 benchmarked scales share (M5 in L09).
- Above 8px, adjacent steps differ by at least 25% so the difference is visible (DC-L03-02 [inferred]).
- Semantic aliases (`space.inset.*`, `space.stack.*`, `space.inline.*`, `space.section.*`) point at ladder indexes; the density mode moves the pointer by one index (B13).
- The builder enforces inner < outer spacing by construction: a group's internal gap is always at least one ladder step below its external gap, and at least half of it (L15 P16; DC-L03-24).
- Optional global multiplier like Radix `scaling` 90-110% [S-L09-559].

### B9. Radius from the Roundness dial

1. `radius.control` from the A5 table.
2. Role scale [inferred ratios, checked against Atlassian]: `radius.detail = max(2, control / 2)`; `radius.container = snap(control x 1.5)`, at least 8 when control > 0; `radius.overlay = snap(container x 1.5)`; `radius.person = full`. Snap to 0, 2, 4, 6, 8, 12, 16, 20, 24, 28, 32. Atlassian check: control 6 gives container 8 and overlay 12, matching its medium, large and xlarge roles [S-L04-016]. When control is full, containers use 16-28 (Material uses 28 for large containers; SLDS Cosmos 20). Uber deliberately squares its containers (0 on cards and modals), which the builder allows as an override [S-L09-430].
3. Shapes under 32px tall drop one step (Fluent 2px under 32px) [S-L04-007]; Spectrum makes radius size-dependent [S-L09-221].
4. **Nested radius:** `inner = max(outer - padding, smallest non-zero step)`. Plain `outer - padding` collapses to square when padding exceeds the radius; Apple's `ConcentricRectangle` with `concentric(minimum:)` solves the same problem (DC-L04-05 [S-L04-057][S-L04-035]). Equal radii on nested elements trigger a warning.
5. **Focus ring radius** = element radius + ring offset (Atlassian `radius.focus` = radius + 2px) [S-L04-016].
6. On iOS, use continuous corners (DC-L04-04).

### B10. Elevation from the Depth dial

- **Band** from A6 picks the model.
- **Shadow ladder** (56-80): Fluent's formula is the cleanest to generate: level n in {2, 4, 8, 16, 28, 64} = ambient `0 0 2px` + key `0 (n/2)px (n)px`, alpha 0.12 / 0.14 in light and 0.24 / 0.28 in dark [S-L09-179][S-L04-008].
- **Default two-layer recipe** (any band with shadows): a 1px contact shadow plus a soft blur scaled to elevation, neutral-tinted (Atlassian #1E1F21, Polaris rgba(26,26,26); no Tier A system uses hue-colored shadows), alpha 8-24% in light mode; in dark mode double the alpha and add a 1px light ring on overlays (Atlassian #BDBDBD at 12%) (DC-L04-12).
- **Tonal** (36-55): surfaces sunken, default, raised, overlay (Atlassian) or five surface containers (Material); shadows only on floating UI (DC-L04-10, DC-L04-13).
- **Glass** (81-100): blur and translucency on controls and navigation only; a solid fallback under Reduce Transparency and Increase Contrast; a 35% dimming layer under clear glass over bright content; never in the content layer (DC-L04-15, DC-L04-16 [S-L15-073]).
- **Borders** at every band: 1px default, 2px selected and focus, 4px emphasis; state changes that alter width use inset box-shadow so layout does not jump (Primer) (DC-L04-07 [S-L04-024]).

### B11. Motion from the Energy dial

- **Duration ladder:** instant 0, micro 100, short 150-200, medium 250-300, long 400-500, extra 700 (DC-L04-20). Energy multiplies medium and longer steps by 0.8 to 1.2 (A4). Exits are 20-35% shorter than entrances (Atlassian 250 vs 200; Primer 300 vs 200) [S-L04-018][S-L04-024]. Duration grows with travel distance (Carbon [S-L06-002]). Standard transitions stay at or under 400ms, the Doherty threshold; over 500ms raises a warning (L13 B5 and E1, where both links are marked inferred).
- **Easing set:** standard, enter (decelerate), exit (accelerate), and linear only for spinners and progress (DC-L04-21). Curves by Energy band as in A4.
- **Springs:** store damping ratio and stiffness; emit Apple's `duration` and `bounce` and a pre-sampled CSS `linear()` (DC-L04-22). Conversion with mass 1: `duration ~ 2 pi / sqrt(stiffness)`, `bounce ~ 1 - dampingRatio` (L04 F3 note). Recomputed: stiffness 700 gives 237ms, 380 gives 322ms, 800 gives 222ms. Effects springs (color, opacity) stay critically damped at 1.0 in every setting, as in Material [S-L04-004].
- **Speeds:** fast for small components (switches, buttons), default for partial-screen surfaces (sheets, drawers), slow for full-screen. Material standard spatial stiffness 1400 / 700 / 300 at damping 0.9; expressive spatial 800 / 380 / 200 at damping 0.6 / 0.8 / 0.8; effects 3800 / 1600 / 800 at 1.0 [S-L04-003][S-L04-004][S-L04-064].
- **Where springs run:** native springs on iOS and Compose; `linear()` approximations on the web (DC-L06-10 platform note). The spring-vs-curve choice follows the platform; Energy only sets how bouncy and how long.
- **Reduced motion** is a token mode: replace travel (translate, scale, parallax) with opacity or color, keep feedback, set travel durations to 0 (Blade) (DC-L04-25 [S-L09-458]).

### B12. Icon stroke from type weight

- The icon's optical weight equals the adjacent text weight (SF Symbols weights map one-to-one to SF font weights; Material asks for "the same optical weight for your symbol and text" and matching grade) (DC-L05-03 [S-L05-010][S-L05-003]).
- Formula [inferred, fitted to sourced anchors]: `stroke = (iconSize / 12) x (textWeight / 400)`, rounded to 0.5px, minimum 1px. It gives 2px at 24px and weight 400 (Material, Lucide) and 1.5px at 16px (Atlassian, Octicons) [S-L05-001][S-L05-029][S-L05-021][S-L05-024]. It misses lighter house styles such as Heroicons (1.5px at 24) [S-L05-032], which the builder offers as a "light" icon preset.
- Size pairs with the adjacent line height: 16px icon with 14px text, 20 with 16, 24 with 20 (DC-L05-05 [inferred from S-L05-016]). Optical sizing thins strokes as icons grow (Material opsz 20-48) [S-L05-003].
- Corners and caps follow Roundness; outline versus fill follows Expression (A1, A5).

### B13. Density modes

Density is a token mode on the semantic layer, separate from color theme and breakpoint; primitives and target minimums never change (DC-L03-11). Three values:
- **Compact:** semantic insets, stacks and row heights move one ladder step down (about 4px, Material density -1 [S-L03-029]); control sizes shift one step (md 40 to 32); body can drop to 14 or 13; compact may also change layout, such as inline labels (Salesforce) [S-L03-070]. Material does not apply density to menus, snackbars or dialogs [S-L03-029].
- **Comfortable:** default.
- **Spacious:** one step up; larger inner:outer ratio.
- Primer-style modality switch: coarse pointers get wider gaps (12px) than fine pointers (8px) [S-L03-009].

---
## C. Look recipes: famous systems as dial settings plus raw inputs

Dial order: **Ex**pression, **Br**and presence, **De**nsity, **En**ergy, **Ro**undness, **Dp** depth, **Co**lorfulness, **Wa**rmth. Values were set from each system's measured levers in the L09 matrix (M3 to M8, M12) and then run through the formulas in `levers.json` with a small test engine. The engine output matched each system's default control radius, body size and depth model in every case below except the noted ones, and its computed L09 expressiveness score (X, using the L09 rubric) matched L09's score for all 13 systems. Caution: the dial values were chosen by looking at the same matrix, so the X match shows the mapping is consistent, not that it predicts unseen systems.

| System | Ex | Br | De | En | Ro | Dp | Co | Wa | Raw inputs | Generated signature | Beyond the dials | Fit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Material 3 Expressive | 90 | 10 | 40 | 80 | 96 | 45 | 75 | 50 | any seed; Roboto or Google Sans Flex; Android; tint neutrals toward seed | pill controls; 16 body; 40dp default button; tonal surfaces; Expressive scheme; spring damping 0.76 / stiffness 380 (M3 expressive default is 0.8 / 380) | type ratio 1.125 must be overridden (Expression alone gives 1.333); the 35-shape library and shape morph are assets | B |
| Apple HIG (iOS 26) | 45 | 20 | 25 | 10 | 75 | 95 | 30 | 50 | systemBlue; SF Pro; iOS | 17pt body and 44pt controls (native base because Brand < 50); Liquid Glass band; critically damped springs, bounce 0 | concentric corners and capsule controls come from the platform rule, not the radius table | A |
| IBM Carbon v11 | 25 | 90 | 70 | 15 | 5 | 45 | 25 | 50 | #0f62fe with brand-exact flag; IBM Plex Sans; 14; marketing surfaces on | 0 radius; 14 body; tonal layers; productive curve (0.2, 0, 0.38, 0.9); true grays | additive type formula chosen as the scale method; dense band gives 32px controls where Carbon's md is 40 (its sm is 32) | B |
| Fluent 2 | 35 | 10 | 68 | 25 | 30 | 68 | 30 | 50 | #0f6cbd; Segoe or platform font; web, Windows, iOS, Android | 4 radius; 14 body; 32 controls; key + ambient shadow ladder; non-bouncy motion | per-platform type ramps need platform modes | A |
| Shopify Polaris | 45 | 60 | 90 | 30 | 52 | 70 | 5 | 50 | near-black brand rgba(48,48,48); blue focus color; Inter; 13 | 8 radius; 13 body; 32 controls; shadow ladder; monochrome scheme; pure R=G=B grays | bevelled button shadows (a signature asset); body weight 450 | B |
| Atlassian | 20 | 90 | 70 | 30 | 42 | 45 | 30 | 50 | #1868DB; Atlassian Sans; 14 | 6 radius; 14 body; ratio 1.2 (its minor-third basis); semantic surfaces; spacing ladder identical to Atlassian's | heading weight 653; spring on avatar hover as a hand-placed hero moment | B |
| GitHub Primer | 20 | 80 | 70 | 30 | 42 | 10 | 30 | 25 | accent #0969da; primary-action color #1f883d; Mona Sans; 14 | 6 radius; 14 body; 32 controls; borders-first depth; cool blue-gray neutrals (OKLCH chroma 0.027, hue 264) | none, given the second color input | A |
| GOV.UK Frontend | 10 | 90 | 5 | 0 | 0 | 0 | 25 | 50 | #1d70b8; green action color; focus #ffdd00; GDS Transport + Arial; 19; space unit 5; motion off | 0 radius; 19 body; 5px spacing ladder; borders only; no motion | strong signifiers (thick black borders) set by the signifier guardrail | A |
| shadcn/ui (Vega) | 30 | 20 | 45 | 30 | 55 | 25 | 0 | 50 | no brand color; Geist or Inter; content product | 8 radius; 16 body; ring + extra-small shadow; monochrome, near-black primary; calm 100-150ms motion; warmth is exactly shadcn's base-neutral choice | card radius 14 against the formula's 12 | A |
| Linear | 20 | 50 | 88 | 20 | 45 | 45 | 20 | 60 | accent #7170ff; near-black base; contrast input; Inter + Inter Display; dark default | 14 body; tonal near-black levels; micro 100 and short 150-200 unchanged, medium steps shortened by x0.88 (Linear's site uses 100 and 180ms); slightly warm gray | in-between weights 510/590; app values not public, so this recipe is partly [inferred] | B |
| Vercel Geist | 45 | 90 | 75 | 55 | 42 | 25 | 5 | 50 | blue-700 accent; Geist Sans and Mono; 14; marketing on | 6 radius; 14 body; ring + faint shadow; achromatic; spring damping 0.88 gives a small overshoot like Geist's (0.175, 0.885, 0.32, 1.1) | -0.06em display tracking | B |
| Razorpay Blade | 55 | 50 | 70 | 70 | 52 | 30 | 45 | 30 | brandColor #1364F1; Inter + TASA Orbiter; 14; web + React Native | 8 radius; 14 body; faint tinted shadows; overshoot motion; blue-gray neutrals; one-input generation is Blade's own model | Blade raises radius to 12 on large controls, the opposite of the small-control drop | A |
| Airbnb DLS | 62 | 100 | 40 | 70 | 70 | 60 | 45 | 60 | Rausch #FF385C; Cereal; content product; photo-first | 12 radius (cards 16-20 from the container rule, Airbnb uses 20); springs damping 0.82 (Airbnb publishes stiffness 100-300 and damping 14-35 at mass 1, roughly 0.7-1.0 as a damping ratio if low damping pairs with low stiffness [inferred]) | ring + shadow + materials mix is only partly one band; imagery is content | B |

Fit grades: **A** means dials plus raw inputs reproduce the signature; **B** means one or two overrides or a signature asset are also needed. No recipe needed a change to the formulas. **What the recipes prove:** the eight dials reach every occupied cell of the L09 personality map (productive brand-led, neutral toolkit, platform-native, expressive platform) and the density axis from 13px to 19px body. **What they show is missing:** variable-font weight overrides (Polaris 450, Atlassian 653, Linear 510/590), signature assets (Material shape library, Polaris bevels), and a separate primary-action color. The builder should expose these as raw inputs or detachable overrides, not as more dials.

---

## D. Guardrails that bound the dials

Three levels, following L15's automate / guide / expose split and L13's default / lint error / warning / human-judgment levels (L15 section 3; L13 E1).

### D1. Enforced by construction (the dials cannot produce a violation)

| Guardrail | Rule | How the generator enforces it | Evidence |
|---|---|---|---|
| Text contrast | 4.5:1 body, 3:1 large text (24px, or 18.66px bold); 7:1 in high-contrast mode; no rounding | text steps are solved for contrast; colorfulness and warmth change chroma and hue only within the solved lightness | DC-L01-22 [S-L01-022][S-L01-025] |
| Non-text contrast | 3:1 for boundaries, focus rings, meaningful icons | strong border step solved at 3:1; depth bands never rely on shadow alone for a boundary (forced colors strips shadows) | [S-L01-023], L14 I-7 |
| On-color text | foreground on a brand fill is picked automatically | Blade-style light/dark flip | [S-L06-094] |
| Target size | hit area at least 24 CSS px on the web (WCAG 2.5.8 AA), 44pt iOS, 48dp Android; 56-66 for remote and gaze; 76dp in cars | `target.min` keys to input type, not density; density shrinks visuals only | DC-L03-12, DC-L14-03, L14 I-1 and I-2 |
| Focus indicator | 2px ring, 2px offset, radius = element radius + offset, 3:1 change against unfocused, forced-colors fallback; changes a physical property, not only color | generated from the radius and color tokens | DC-L04-09, L14 I-5 |
| Reduced motion | a token mode swaps travel for opacity and keeps feedback; WCAG 2.3.3 treated as required; nothing flashes more than 3 times a second | every Energy setting emits both modes | DC-L04-25, L14 I-13 |
| Reduced transparency | glass falls back to solid | the materials band always emits a solid twin | DC-L04-16 |
| Text scaling | containers grow with text to 200% (iOS Dynamic Type, Android font scale) and hierarchy stays intact | line heights and control heights are min-heights, not fixed | L14 I-6, DC-L15-02 [S-L15-055] |
| Grouping | inner spacing smaller than outer spacing | spacing aliases are derived with the ratio from Density | L15 P16, DC-L03-24 |
| Hierarchy tiers | three text colors, two or three weights, a scale with few steps, one primary button variant | the type and color generators only emit these | L15 P02-P04, P08 |
| Nested radii | concentric with a minimum | derived (B9) | DC-L04-05 |
| Script safety | per-script line height, zero tracking for Arabic and Devanagari, no italic emphasis for caseless scripts | script-aware type tokens | DC-L02-25 |
| Native behavior | back, navigation containers, sheets and pickers follow the platform at every Brand setting | Brand presence changes appearance only | DC-L10-02, L14 I-12 |
| Default behaviors | button loading state that traps repeat clicks; feedback timing tokens (50ms acknowledge, 100ms instant, 1s indicator, 10s progress); empty, error and success variants; live-region announcements | shipped in every generated system | L13 E1 level 1, L13 B5 |
| Driving mode (if cars are in scope) | no on-screen animation in templated categories, 76dp targets, 2s glance and 12s task limits | hard validator rules | DC-L14-11 |

### D2. Warnings and lint (the builder flags; the person can override)

Lint errors that block publishing unless overridden with a written reason (L13 E1 level 2): a target under 24x24 CSS px without a spacing exception; a field with no programmatic label; meaning shown by color alone; a dialog with no way to dismiss; a pre-checked consent box.

Warnings (L15 "guide" and L13 E1 level 3). The hierarchy numbers are practitioner consensus, not experiments, and the UI should say so:
- More than 3 type sizes in one view, or more than 2 large elements (NN/g) [S-L15-001][S-L15-002].
- More than one element at top emphasis, or more than one primary action per view [S-L15-067][S-L15-038].
- More than 3 text colors or more than 2 weights in one view (Refactoring UI) [S-L15-038].
- Accent covering more than about 15% of a view [inferred threshold, DC-L15-03]; 60-30-10 is available only as an optional soft check because its evidence is weak [S-L15-048].
- Spring bounce above 0.2 (damping below 0.8) without the Playful macro (DC-L04-19).
- Colorfulness above 75 together with Density above 66: too much visual complexity costs appeal far more than too little [S-L15-047].
- Minimal signifiers with Density above 33 or an unconventional layout: NN/g measured +22% task time on weak signifiers [S-L15-004].
- Expression above 66 on a finance or banking product (Google's caution) [S-L06-010].
- Equal radii on nested elements; glass in the content layer; the neumorphic preset (fails 3:1 non-text by design) [S-L15-060].
- Standard transitions over 500ms [inferred threshold, L13 E1]; placeholder-only labels; button labels over 4 words; delete with neither undo nor confirm (L13 E1).
- APCA below Lc 75 on body text, as an advisory note only [S-L01-026].

### D3. Left to the person (the builder asks and records, it does not decide)

Brand personality itself and the dial positions; information architecture and labels; which element matters most on each screen; which actions get undo and which get confirmation; convention versus novelty for the product's core differentiator; tone and celebration; logo, illustration, photography and custom icons (designer hooks in the brief). Golden-ratio scales, color-wheel harmonies and 60-30-10 are optional presets, never rules: L15 found golden-ratio effects fragile under testing [S-L15-052], wheel palettes "not very useful" for UI [S-L15-039], and 60-30-10 of unclear origin [S-L15-048].

The builder must also refuse to automate these misapplied "laws" (L13 E2): no 7-item cap on navigation (Miller does not limit menus), no automatic removal of options for Hick's law, no nag features justified by Zeigarnik, no strategic delays justified by the Doherty threshold, no attractiveness score used as a usability signal, and no hard caps on result counts justified by choice overload.

---
## E. Reference intake: starting from an example site or file

The brief asks that a person can drop in an example website, screenshot or Figma file at any point, and the builder reads what it uses and builds on it, "copying structure and quality, never another brand's identity" (`_coordination/BRIEF.md`, requirement 4). Reference intake is the formulas in section B run backwards: measure the reference's values, fit them to the formulas, and read off the dial positions. The person then adjusts from there with the same dials.

### E1. What each source type can yield

| Source | What can be read | Tools in the research | Blind spots |
|---|---|---|---|
| Live website (URL) | computed CSS: colors, font families, sizes, line heights, tracking, weights, margins, paddings, gaps, radii, box-shadows, backdrop-filter, transition durations and easings, `linear()` springs, `prefers-color-scheme` and `prefers-reduced-motion` rules | Paper MCP reads computed styles [S-L16-009] | JavaScript-driven springs; states you cannot trigger; pages behind login |
| Figma file | variables (color, number, and timing/easing types since Config 2026), styles, effects, component properties, prototype motion | Figma MCP `get_variable_defs`, `get_design_context`, `get_motion_context`, `get_screenshot` [S-L16-001]; Figma variable types noted in the BOARD cross-lane notes (L07) | files that use raw values instead of variables; only one mode per import (L07) |
| Screenshot | colors and their areas, approximate sizes and radii, depth cues, icon style; complexity and colorfulness metrics (Aalto Interface Metrics computes clutter, colorfulness, grid quality and white space from a screenshot) [S-L15-080] | vision model plus metric tools | no motion, no exact spacing, no dark mode, no hover or focus states |

### E2. Which dials can be inferred

| Dial | Inferable? | Measured from | Inverse formula | Confidence |
|---|---|---|---|---|
| Roundness | **Yes** | most common radius on buttons and inputs | look up the A5 band; container and nested radii confirm the role ratios | high on URL and Figma; medium on screenshots |
| Density | **Yes** | body size, control heights, table row heights, typical paddings | A3 bands (13-14px and 32px controls read compact; 16px and 40px comfortable; 17px+ and 44-48px spacious; L09 density axis) | high |
| Depth | **Yes** | shadow layer count and alpha, borders, surface lightness steps, backdrop blur | A6 bands: borders only, 1px ring + tiny shadow, tonal steps, key + ambient ladder, blur | high on URL and Figma; medium on screenshots |
| Colorfulness | **Yes** | chroma of the accent and of large surfaces; count of distinct accent hues; share of screen area that is chromatic | A7 anchors run backwards (surface chroma and accent count first, accent chroma second) | high |
| Warmth, color part | **Yes** | neutral hue and chroma in OKLCH | nearest A8 anchor (slate, gray, pure, stone, taupe) | high |
| Warmth, voice part | Partly | capitalization of buttons and headings, contractions | A8 content rows | medium; needs enough copy |
| Energy | **Partly** | transition durations, easing curves, overshoot (a bezier y value above 1 or an overshooting `linear()`), saturation, heading weight | duration multiplier = median medium duration / 275ms (the middle of the 250-300 medium step) [inferred]; damping from overshoot size; saturation and weight as secondary signals | medium on URLs, low on Figma unless motion is defined, **none from screenshots** |
| Expression | **Partly** | display-to-body ratio, emphasized styles, containment, icon fill, how much chrome carries color; the L09 X score is computable from these levers | fit the L09 X rubric (radius + surface color + type contrast + motion + material), subtract what the character dials already explain | medium; one page can mislead because hero moments are rare by design |
| Brand presence | **No, ask** | could detect whether the font is a system, open or proprietary face | none; this dial expresses the person's own intent (how native their product should feel), and copying a reference's brand-led posture would copy its identity | n/a |

### E3. Formulas run backwards

- **Type scale.** Collect distinct font sizes; fit `log(size) = log(base) + n x log(ratio)` by least squares over integer n. Small residuals mean a modular scale (Spectrum and Material fit 14 x 1.125^n almost exactly, section B6); a constant or stepped difference means an additive scale (Carbon); large residuals mean hand-tuned, so the builder keeps the measured sizes as overrides. Body size = the most common paragraph size; line heights give the per-size ratios in B7.
- **Spacing.** Collect margins, paddings and gaps; the base unit is the largest of 4, 5 or 8 that divides most values (GOV.UK is the 5 case [S-L09-508]); check coverage of the nine-step ladder; nested groups give the inner:outer ratio.
- **Color.** Split colors into neutrals (low chroma) and accents. For the ramp rule, test whether same-numbered steps have equal contrast across hues (contrast-based), equal lightness (tone-based) or neither (hand-tuned); DC-L01-03 lists the three. Detect dark mode and whether dark is a separate mapping.
- **Shadows.** Parse each `box-shadow` into layers: a 0-blur 1px spread is a ring; a small-blur and a large-blur pair is key + ambient; alpha values give the A6 opacity position.
- **Motion.** Read durations and curves; map curves to the nearest A4 curve by control-point distance; an overshoot sets damping below 1.
- **Icons.** Stroke width against icon size gives the implied weight through B12; `stroke-linecap` and fill versus outline feed Roundness and Expression.

### E4. What intake never copies

Following the brief, intake transfers structure and quality, not identity [inferred policy from BRIEF.md requirement 4]:
- **Brand color:** the reference's exact hue is not carried over by default. Intake keeps the measured chroma level, neutral temperature and ramp structure, then asks for the person's own brand color (or offers a hue family, clearly labeled as a suggestion).
- **Typeface:** proprietary or restricted faces (GDS Transport is limited to gov.uk; Cereal, Uber Move and Spotify Mix are proprietary; L09 M4) are replaced with an open face of the same classification and proportions, and the person is told why.
- **Logos, illustration, photography, custom icons and signature assets** (for example Material's shape library, Polaris bevels, CRED NeoPOP surfaces) go to the designer-hook list instead of being cloned.
- **Brand presence** starts at 50 regardless of the reference and is asked, not inferred.

After intake, the builder shows the inferred dial positions with a confidence badge per dial, highlights the ones it could not infer (always Brand presence; Energy when the source is a screenshot), and lets the person adjust from there.

---

## Weak evidence and open contradictions

- **Weakest mappings** (all tagged [inferred] above): the coupling coefficients (0.5, 0.3, 0.2); the Energy duration multiplier (0.8 to 1.2); the macro offsets; the radius role ratios (x1.5); the icon stroke formula (it misses Heroicons' 1.5px at 24); the 200-weight hierarchy gap; the 15% accent-area threshold; L06 row E (premium/everyday), where most cells are inferred in L06 itself.
- **Display size is not a personality lever in the benchmark.** L06 row A and L15 tie big size jumps to playful or dramatic brands, but in L09 the largest display-to-body ratios belong to productive systems with marketing display sets (Carbon 92/14, Uber 96/16, Fluent 68/14). This synthesis therefore drives display reach from the marketing-surfaces input and only the ratio from Expression.
- **Material's type scale and its expressiveness disagree.** Material is the most expressive system in L09 (X = 9) yet uses the smallest ratio (1.125). Expressiveness there comes from shape, color and motion, not the ratio, so the Material recipe needs a ratio override.
- **Material's Display Large (57) does not follow its own formula**: 14 x 1.125^12 = 57.54, which rounds to 58, and Spectrum lists 58 for the same step. L02's "rounds to 57" check is off by one pixel at that step.
- **Carbon density:** L09 groups Carbon with dense systems (14px body, 32px controls), but Carbon's ladder has md 40 and calls its 48px large button "the most common button size in software products" [S-L03-082]. Body size and control size do not always move together.
- **Energy and duration direction:** calm systems are fast (Linear 100/180ms, Carbon productive "significantly faster"), and expressive motion is slower and more visible (Carbon expressive, Material expressive springs settle in about 322ms against 237ms). So "energetic" means longer and bouncier hero motion, not faster UI; the builder should say so in the dial's tooltip.
