# L15: Visual design principles (what makes an interface look good, and why)

Lane: L15. Author: orchestrator subagent L15. Written 2026-09-23. Status: complete (first pass).
Trace: `traces/L15-trace.md` (81 source ids, S-L15-000 to S-L15-080, plus 2 correction rows; rejected sources included). Schema: `_coordination/SCHEMA.md`.
Related lanes (linked, not repeated): L01 color (`research/L01-color.md`), L02 typography (`research/L02-typography.md`), L03 space and layout (`research/L03-space-layout.md`), L04 shape, depth and motion (`research/L04-shape-depth-motion.md`), L06 brand and voice (`research/L06-brand-voice.md`), L13 UX laws (`research/L13-ux-laws-heuristics.md`, written in parallel; behavioral laws such as von Restorff, Hick, Fitts and Jakob live there).

## Lane overview

This lane answers "what would make it look which way" at the level of principles rather than token values. The builder's users are engineers and technical people who often lack visual-design training, so for every principle this file decides one of three stances:

- **Automate**: enforce by construction. The user cannot easily break it because the generated tokens and components already obey it (for example, a spacing scale where inner gaps are always smaller than outer gaps).
- **Guide**: detect and warn, or suggest a fix, but let the user override (for example, "three elements on this screen compete for first place").
- **Expose**: give the user a control, because the principle encodes a taste or brand choice with more than one good answer (for example, how dramatic the size jump between heading levels is).

Evidence strength uses a four-step scale throughout: **Strong** (peer-reviewed experiments, replicated), **Moderate** (a single controlled study or eyetracking experiment, or peer-reviewed work with mixed replication), **Consensus** (several Tier A/B guidelines agree, no experiment), **Weak/folk** (a rule of thumb with unclear origin, or one contradicted by evidence).

**What "futur" resolved to.** Kunal's "futur" is **The Futur** (thefutur.com and youtube.com/@thefutur), the education company founded by Chris Do [S-L15-019]. It is mainly a business-of-design and branding channel: of 1,187 channel videos, a keyword count of titles finds about 650 on business, sales, pricing, marketing and branding topics and only about 100 on design craft (typography, layout, color, UI, critique, logos); the visual-design content is a smaller track of typography rules, layout critiques, color lessons (Greg Gunn) and composition tips (Matthew Encina) [S-L15-023]. Its visual teaching is practitioner opinion (Tier B/C), useful as teachable heuristics, not as evidence. Other plausible matches considered: the **Futura** typeface (which The Futur itself uses in its credits [S-L15-023]) and generic "future of design" trend content; neither fits "a source that teaches visual design" as well as The Futur.

**Five findings that shape the builder most:**

1. **Hierarchy is the principle to automate first, and its levers are countable.** Independent sources converge on small numbers: no more than three type sizes and at most two "big" elements per view (NN/g) [S-L15-001, S-L15-002], three levels of dominance with one dominant element (Smashing) [S-L15-067], "1 really BIG object", "1–2 medium sized objects" and "Tons of very tiny objects" (The Futur) [S-L15-028], two or three text colors and two weights (Refactoring UI) [S-L15-038], and one true primary action per page [S-L15-038]. These are consensus, not experiments, but they are concrete enough to lint.
2. **Grouping is the best-evidenced visual principle, and it has a strength order.** Gestalt grouping has a century of vision science behind it [S-L15-016]. In UI terms, common region (a boundary) overpowers proximity, and proximity overpowers similarity [S-L15-012, S-L15-010, S-L15-011]. The builder can enforce proximity by construction (inner spacing always smaller than outer spacing) and offer containers only where space alone fails.
3. **"Looks good" has measurable components: low-to-moderate visual complexity, familiar layout, moderate colorfulness.** Users judge aesthetics within 17-50 ms, and simple, prototypical sites score as most beautiful [S-L15-044, S-L15-045]. Across 2.4 million ratings, appeal peaks at moderate complexity, and too much complexity hurts far more than too little (Cohen's d 2.0 for high complexity vs 0.6 for low, each compared with the peak) [S-L15-047]. This argues for a restrained default and for a computed "complexity" readout in the builder, since tools like Aalto Interface Metrics already compute clutter, colorfulness, grid quality and white space from a screenshot [S-L15-080].
4. **The aesthetic-usability effect is real but narrower than its popular version.** Attractive UIs are perceived as more usable and forgive minor problems [S-L15-003], but a controlled 80-person study found aesthetics did *not* raise perceived usability, while poor usability *lowered* perceived beauty after use [S-L15-042]. The builder should present polish as a multiplier on a usable base, never as a substitute, and should warn that pretty prototypes hide problems in testing [S-L15-003].
5. **Several popular "rules" are weak.** The 60-30-10 color rule is an interior-decorating heuristic with unclear origin and no study behind it [S-L15-048]; The Futur's own worked example does not follow it exactly (60/25/10/5) [S-L15-026]. Color-harmony wheels (complementary, triad) are called "not very useful" for UIs by Refactoring UI [S-L15-039], and lab data show people rate *similar*-hue pairs as more harmonious than contrasting ones [S-L15-017]. Golden-ratio aesthetics are fragile under careful testing [S-L15-052] even though NN/g presents them uncritically [S-L15-066]. The builder should expose these as optional presets, never enforce them.

---

## 1. Principle catalog

Each row gives: what the principle is, evidence strength, the concrete levers or tokens it maps to, and the builder stance. Principles are numbered P01-P72 for cross-reference.

### 1.1 Hierarchy and emphasis

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P01 | Visual hierarchy | "Guiding the eye on the page so that it attends to different design elements in the order of their importance" [S-L15-001]. Apple: "Order content by relative importance" [S-L15-053]. The Futur frames it as primary, secondary and tertiary "reads" [S-L15-033]. | Consensus (eyetracking supports scanning order, P09) | Type scale steps, weight, text color tier, spacing around an element, position | **Automate** the tiers (text roles, 3 text colors, button levels); **guide** per screen |
| P02 | Scale | Relative size signals rank; a visually pleasing design "generally uses no more than 3 different sizes" [S-L15-001]; "Limit how many elements are big to a maximum of 2" [S-L15-002]. The Futur: one big, one or two medium, many tiny [S-L15-028]. | Consensus | `font.size.*` roles, component size props, image/hero size | **Automate** a scale with few steps (L02 DC-L02-09/10); **guide** when a view uses more than 3 sizes or more than 2 large elements |
| P03 | Weight contrast ("skip a weight") | Adjacent weights are too similar to read as different; jump from light to bold or medium to extra bold [S-L15-033, S-L15-034]. Refactoring UI: two weights are usually enough in UI (400/500 and 600/700); avoid weights under 400 for UI text [S-L15-038]. Apple: avoid Ultralight, Thin and Light [S-L15-055]. | Consensus | `font.weight.regular/strong` (L02 DC-L02-15) | **Automate** a two- or three-weight palette with a minimum gap of 200 [inferred numeric from S-L15-033/038] |
| P04 | Color and value as hierarchy | Use color and weight before size: "Is this text secondary? Let's use a lighter color" [S-L15-038]. Bright or saturated for important, muted for less important [S-L15-002]. Do not rely on color alone [S-L15-002]. | Consensus | `color.text.primary/secondary/tertiary` (L01 DC-L01-14) | **Automate** three text tiers with guaranteed contrast |
| P05 | De-emphasis as a tool | To make one thing stand out, turn others down rather than turning it up. Refactoring UI chapter "De-emphasize to emphasize" [S-L15-037]; Smashing: "You can't emphasize everything" [S-L15-067]. | Consensus | Secondary/tertiary text tokens, ghost and link button variants, reduced-opacity icons | **Guide**: when the user enlarges or colors an element, suggest demoting its neighbors instead |
| P06 | Single dominant element, three levels | Emphasis is relative; ideally one dominant element; people perceive about three levels (dominant, sub-dominant, subordinate), which should be distinct steps, not a continuum [S-L15-067]. Figma's Miguel Cardona: "If everything looks the same, then you see nothing" [S-L15-051]. | Consensus | Count of elements at top emphasis per view; size and contrast gaps between levels | **Guide** (lint: more than one element at top emphasis) |
| P07 | Contrast (difference must be obvious) | "The juxtaposition of visually dissimilar elements in order to convey the fact that these elements are different" [S-L15-001]. Williams frames weak difference as "conflict" rather than contrast [S-L15-070]. The Futur: fonts that are too similar muddy hierarchy [S-L15-030]. | Consensus | Minimum ratio between adjacent type steps, weight gap, color-step distance | **Automate** minimum gaps between tiers; **expose** strength (DC-L15-02) |
| P08 | Button and action hierarchy | "Most pages only have one true primary action"; primary = solid high-contrast; secondary = outline or low-contrast fill; tertiary = link style; destructive is not always red unless it is the primary action [S-L15-038]. Apple: color the background of the prominent button, and do not color many controls [S-L15-054]. | Consensus | Button variants `primary/secondary/tertiary`, `danger` as a modifier not a level | **Automate** variants; **guide** (lint: more than one primary per view) |
| P09 | Scanning order | Eyetracking shows four text-scanning patterns (F, spotted, layer-cake, commitment); the F-pattern appears when there are no subheadings; RTL mirrors it [S-L15-079]. Apple: people start top-leading, so place the most important items there [S-L15-053]. | Moderate (eyetracking) | Heading and subheading styles, left alignment, position of primary content | **Automate** RTL mirroring and heading styles; **guide** placement |
| P10 | Separate visual from document hierarchy | An H2 does not have to look like a big heading; visual weight follows importance, not HTML tag. Refactoring UI chapters "Separate visual hierarchy from document hierarchy" and "Semantics are secondary" [S-L15-037]. | Consensus | Decouple `font.role` tokens from semantic tags in generated code | **Automate** (role tokens independent of tag) |
| P11 | Labels are a last resort | Where data formats are self-explanatory, drop "Label: value" pairs and let format and hierarchy carry meaning [inferred from the chapter title S-L15-037]. | Consensus (single source) | Display patterns for key-value data | **Guide** |
| P12 | Squint (blur) test | Blur the design to check whether hierarchy and groups still read without text [S-L15-002]. | Consensus (method) | A blur preview mode | **Automate** as a builder view; pairs with computed saliency heatmaps such as AIM's UMSI and MD-EAM models [S-L15-080] |

### 1.2 Contrast, alignment, repetition, proximity (CRAP) and the classic principles

Robin Williams' four principles (proximity, alignment, repetition, contrast) come from *The Non-Designer's Design Book*, now in its 4th edition [S-L15-070]. Her premise fits the builder exactly: "Once you can name the problem, you can find the solution" [S-L15-070]. The Futur lists a near-identical set as the fundamentals of typography and design: contrast, repetition, balance, scale, composition (or hierarchy) [S-L15-021, S-L15-029].

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P13 | Contrast | See P07. | Consensus | Tier gaps | Automate + expose |
| P14 | Alignment | Every element aligns to something. Apple: alignment "makes an app look neat and organized", aligned items read as related and indented items as subordinate [S-L15-053]. The Futur: "Align to One Axis" and justify left for Western reading [S-L15-033]. | Consensus | Grid columns, shared left edge, indentation step token | **Automate** (snap to grid and to a small set of edges); **guide** on stray edges (AIM "grid quality" metric computes this [S-L15-080]) |
| P15 | Repetition / consistency | "Repeat some aspect of the design throughout the entire piece" [S-L15-070]. NN/g: consistent visual rules per element type build expectations [S-L15-011]. | Consensus | Tokens and components themselves | **Automate** (this is what a design system is) |
| P16 | Proximity | See Gestalt P23; Williams' first principle [S-L15-070]. | Strong | Spacing scale semantics | **Automate** |
| P17 | Balance | "A satisfying arrangement or proportion of design elements"; symmetrical, asymmetrical or radial; "Asymmetry is dynamic and engaging. It creates a sense of energy and movement. Symmetry is quiet and static" [S-L15-001]. Visual weight (P55) is what gets balanced [S-L15-068]. | Consensus | Layout templates (centered vs left-aligned), hero composition | **Expose** (DC-L15-08) |
| P18 | Rhythm | Regular, repeated intervals (spacing, type baseline, component heights) read as order. | Consensus [inferred from S-L15-070 repetition + L03 DC-L03-25] | Spacing scale, 4pt baseline, consistent control heights (L03 DC-L03-02, DC-L03-07, DC-L03-25) | **Automate** |
| P19 | Unity | All parts look like one family: limited palette, one or two typefaces, one shape language. NN/g: 2 primary + 2 secondary colors [S-L15-002]; Apple: minimize typefaces [S-L15-055]. | Consensus | Palette size, font family count, radius scale | **Automate** small sets; **guide** when the user adds families or hues |
| P20 | Scale (proportion system) | Sizes relate by a ratio (modular scale). | Consensus that a system helps; specific ratios are taste | Type scale ratio (L02 DC-L02-09), spacing progression (L03 DC-L03-02) | **Expose** the ratio; **automate** the system |
| P21 | Golden ratio | Proportions of 1:1.618 for type scale, layout splits, crops. NN/g presents it as a usable reference (16 px x 1.618 ≈ 26 px) [S-L15-066]. Peer-reviewed reviews find real but fragile effects, "relatively sensitive to careless methodological practices" [S-L15-052]; paintings show no golden-section preference [S-L15-052]. | **Weak/folk** | One option among type-scale ratios | **Expose** as a preset only; never claim it is "more beautiful" |
| P22 | Negative space | Space is an active element; a crowded design "often looks harsh"; "If you have a small room, buy small furniture" (Chris Do) [S-L15-020]. The Futur: avoid the corners and edges; "Let your design breathe" [S-L15-033]. Refactoring UI: "Start with too much white space" [S-L15-037]. | Consensus | Section spacing tokens, container max widths, margins | **Automate** generous defaults; **expose** density (DC-L15-04) |

### 1.3 Gestalt principles in UI

Gestalt psychology started with Wertheimer in 1912. The modern review by Wagemans and colleagues (Psychological Bulletin, 2012) lists the classical grouping principles (proximity, similarity, common fate, good continuation, closure, symmetry, parallelism) and newer ones (synchrony, common region, element and uniform connectedness), and treats Prägnanz as the tendency toward "the simplest possible organization" [S-L15-016]. This is the best-evidenced area in the lane. What is *less* established is the exact strength order in real interfaces; the order below comes from NN/g's applied articles [S-L15-010, S-L15-011, S-L15-012]. Figma's list adds "focal point", which is not a classical Gestalt principle (it is emphasis, see P06, and von Restorff in L13) [S-L15-049].

| # | Principle | UI meaning | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P23 | Proximity | "Items that are visually closer together are perceived as part of the same group" [S-L15-001]; proximity "can overpower competing visual cues such as similarity of color or shape"; distant elements get overlooked [S-L15-010]. | Strong (vision science) + applied consensus | Inner vs outer spacing (label-to-field < field-to-next-field); L03 DC-L03-24 sets the ratio (at least 1:2) | **Automate**: semantic spacing tokens where `space.inner < space.outer` always holds; **guide** on "ambiguous spacing" (Refactoring UI chapter title [S-L15-037]) |
| P24 | Similarity | Shared color, shape or size implies relation; weaker than proximity and common region but "the most resilient" because it works across distance [S-L15-011]. Links must look different from text [S-L15-013]. | Strong + consensus | One style per element type; link style; icon style consistency | **Automate** (component variants); **guide** when two elements with different functions share a style, or one function has two styles |
| P25 | Common region | "Items within a boundary are perceived as a group"; a boundary "can overpower other grouping principles such as proximity or similarity"; cards fix proximity failures; zebra stripes group rows; overuse creates clutter [S-L15-012]. | Strong (listed among the newer grouping principles in S-L15-016) + applied | Card, panel, section background tokens; borders; row striping | **Expose** containment level (DC-L15-05); **guide** on nested boxes-in-boxes |
| P26 | Uniform connectedness | Elements joined by lines, colors or frames read as more related than unconnected ones [S-L15-013]. | Strong (listed among the newer grouping principles in S-L15-016) | Connector lines (steppers, timelines, trees), shared backgrounds | **Automate** in components that need it (stepper, tree) |
| P27 | Continuity (good continuation) | Items on a line or curve read as related; alignment guides the eye [S-L15-049, S-L15-016]. | Strong (classical) | Alignment edges, list flow, carousels that bleed off the edge to signal "more" [inferred] | **Automate** via grid alignment |
| P28 | Closure | People complete incomplete shapes [S-L15-049, S-L15-016]. | Strong (classical) | Icon design, cropped cards signaling scroll | **Guide** (icon review) |
| P29 | Figure-ground | The eye separates foreground objects from background; the 2012 review covers both classic and newer image-based figure-ground principles and how past experience and attention affect them [S-L15-016]. In UI: surfaces, overlays and scrims must separate clearly [S-L15-049]. | Strong | Surface layering (L01 DC-L01-13), elevation (L04 DC-L04-11), scrim opacity (L04 DC-L04-18), AIM "figure-ground contrast" metric [S-L15-080] | **Automate** surface steps; **guide** when a surface differs from its parent by too little |
| P30 | Prägnanz (simplicity) | The brain settles on the simplest organization [S-L15-016]; ambiguous images get simplified [S-L15-049]. In UI: simple, regular shapes and layouts are processed faster; this links to the low-complexity preference in P70 [S-L15-045]. | Strong (theory) | Fewer shapes, regular geometry, consistent radii | **Automate** restraint by default |
| P31 | Symmetry and order | Symmetrical arrangements read as a unit and as orderly [S-L15-001, S-L15-049]. | Strong (classical) | Centered layouts, balanced columns | **Expose** (DC-L15-08) |
| P32 | Common fate | Elements that move together read as a group [S-L15-016, S-L15-049]. | Strong (classical) | Motion choreography: grouped items animate together (L04 DC-L04-23) | **Automate** in motion presets |

### 1.4 Whitespace, density, grids and composition

Token-level detail for spacing scales, density modes, grids and breakpoints lives in L03 (DC-L03-01 to DC-L03-26). This section covers the principle-level choices.

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P33 | Whitespace as voice | How much empty space a product uses is a personality choice: airy reads calm, premium and confident; dense reads serious, focused and utilitarian (Material, per L03 DC-L03-24). NN/g's aesthetic-usability example shows the limit: a participant first loved a site's huge photos, then found the low information density "annoying the second time" [S-L15-003]. | Consensus | Section spacing, container width, items per screen, density mode (L03 DC-L03-10/11/24) | **Expose** (DC-L15-04) |
| P34 | Density must match task | Dense layouts suit expert, repeated, data-heavy work; sparse layouts suit first-time, marketing and emotional moments. Flat, low-signifier UIs only work when density is low [S-L15-004]. | Moderate (S-L15-004 eyetracking) + consensus | Density mode per surface (app vs marketing) | **Expose** per surface; **guide** when a dense view also uses weak signifiers |
| P35 | Grid | "A visual made up of columns, gutters, and margins"; three UI grid types: column, modular, hierarchical (the most important content takes the biggest modules) [S-L15-065]. Müller-Brockmann's *Grid Systems in Graphic Design* (1981) codified grids of 8 to 32 fields as a tool to design "more reliably and quickly" [S-L15-072]. | Consensus (NN/g: grids improve scannability; no experiment cited) | Column count, gutter, margin tokens (L03 DC-L03-15) | **Automate** grid snapping; **expose** grid type (DC-L15-07) |
| P36 | Break the grid deliberately | Breaking the grid draws attention; without a reason it produces a "chaotic browsing experience" [S-L15-065]. Refactoring UI has a chapter titled "Grids are overrated" [S-L15-037]; the likely point is that fixed widths often beat percentage columns inside components [inferred]. | Consensus | Full-bleed and offset variants | **Guide** (warn on off-grid elements that are not marked as intentional) |
| P37 | Don't fill the screen | Content should have an intended width; stretching to fill wide screens hurts reading and composition. Refactoring UI chapter "You don't have to fill the whole screen"; "Everything has an intended size" [S-L15-037]. | Consensus | Max content width, measure (L03 DC-L03-16; L02 DC-L02-17) | **Automate** max widths |
| P38 | Composition by contrast | The Futur's composition method: push contrast in value, weight, size and color; "start extreme" (the video description says "Start drastically, then pull it back"); give the most important object the strongest contrast [S-L15-028, S-L15-023]. | Practitioner opinion (Tier B/C) | Hero templates, image-text ratios | **Guide** (template presets that already follow 1 big / 1-2 medium / many small) |

### 1.5 Color at the principle level

L01 owns color spaces, ramps, roles, dark mode and contrast enforcement (DC-L01-01 to DC-L01-27). The principles below are about *how much* and *which kind* of color.

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P39 | Restraint (color budget) | Almost everything in a UI is grey; color is spent on a few high-meaning elements. Refactoring UI: "almost everything in an interface is grey" and needs 8-10 grey shades, one or two primaries, a few accents [S-L15-039]. Apple: apply color "sparingly", reserve it for status and primary actions, do not color the background of multiple controls [S-L15-054]. NN/g: 2 primary and 2 secondary colors [S-L15-002]. The Futur: too many colors or too much saturation make a design "hard to look at" [S-L15-025]. | Consensus (strong agreement across Tier A/B) | Accent share of screen area; number of hues in use; L01 DC-L01-08 (accent count), DC-L01-10 (chroma level) | **Automate** a neutral-first palette; **guide** on accent overuse |
| P40 | Role-based palettes beat harmony wheels | Wheel harmonies (complementary, triadic, "major fourth") give "five perfect color swatches" that are "not very useful" because a UI needs shades, greys and semantic colors [S-L15-039]. | Consensus (practitioner) + evidence below | Ramps per role (L01 DC-L01-02/03) | **Automate** role ramps; **expose** harmony only as an accent-picking aid |
| P41 | Harmony evidence | Lab studies separate three judgments. Pair preference and pair harmony both *increase* with hue similarity (analogous feels harmonious); preference also depends on lightness contrast; highly contrastive hue pairs are judged neither preferable nor harmonious, but a figure color is liked more when it contrasts in hue with its background [S-L15-017]. | Strong (peer-reviewed experiment) | Analogous neutrals + one contrasting accent; lightness contrast for legibility | **Automate** the pattern "low-chroma analogous surfaces, one contrasting accent for figures"; **expose** accent hue |
| P42 | 60-30-10 rule | Dominant 60%, secondary 30%, accent 10% of area. Taught by The Futur (Greg Gunn) as "a recipe" [S-L15-026]. Origin is unclear (interior decorating); some claim a golden-section basis; no empirical study found [S-L15-048]. The Futur's own Paul Rand example decomposes as 60/25/10/5 [S-L15-026]. | **Weak/folk** | Area share of neutral, brand surface, accent | **Guide** only, as a soft check that accent area stays small; never enforce exact percentages |
| P43 | Consistent saturation | Keep saturation consistent across the palette; mixed brightness of the same color across pages "can start to look too busy" [S-L15-027]. Refactoring UI: "Don't let lightness kill your saturation" and "Greys don't have to be grey" (chapter titles) [S-L15-037]. | Consensus | Chroma curve per ramp; tinted neutrals (L01 DC-L01-06) | **Automate** (perceptual ramps with controlled chroma) |
| P44 | Value contrast first | Check color pairs in grayscale; hue differences without value differences disappear [S-L15-025]. | Consensus (and consistent with contrast standards) | Contrast checks (L01 DC-L01-22) | **Automate** |
| P45 | Temperature | Warm colors advance and weigh more; cool colors recede; saturated colors weigh more than desaturated [S-L15-068]. Warm vs cool neutrals set friendliness vs authority (L06 lever matrix row B). | Consensus (practitioner synthesis; not tested here) | Neutral hue tint (L01 DC-L01-06); accent hue | **Expose** (neutral temperature) |
| P46 | Colorfulness sweet spot | Across ~40,000 people, appeal rises then falls with colorfulness (peak 6.1 of 9), with a weaker effect than complexity; preferred colorfulness varies by gender, education and country [S-L15-047]. | Strong (very large sample; one research group) | Palette chroma level (L01 DC-L01-10) | **Expose**, with a moderate default |
| P47 | No grey text on colored backgrounds | Grey on white works because it lowers contrast; on a colored surface, lower contrast with white at reduced opacity or a same-hue tint instead [S-L15-038]. | Consensus | "On-color" text tokens per surface (L01 DC-L01-14) | **Automate** (generate on-color secondary text per surface) |

### 1.6 Type pairing and typographic hierarchy (principle level)

L02 owns families, scales, line height, tracking and pairing tokens (DC-L02-01 to DC-L02-28, pairing in DC-L02-03). The principles below explain *why* those defaults look right.

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P48 | Fewer typefaces | Apple: "Minimize the number of typefaces you use"; mixing too many "can obscure your information hierarchy" [S-L15-055]. The Futur: start with one font; more than two is "unnecessary and unadvisable" for beginners [S-L15-033, S-L15-030]. | Consensus | Family count (L02 DC-L02-03) | **Automate** one family by default; **guide** at three or more |
| P49 | Pair by contrast, not similarity | Two fonts that are "too similar" confuse hierarchy; pairs should contrast and not compete [S-L15-030, S-L15-034]. | Consensus | Display vs text family classification | **Expose** pairing presets; **guide** against near-identical pairs [inferred check: same classification and similar x-height] |
| P50 | Size ratio: double or halve | The Futur's rule of thumb: headline 2x body (30 pt over 15 pt), 3x-4x "for drama" [S-L15-033]. This is a coarse version of a modular scale. | Practitioner opinion | Scale ratio and step count (L02 DC-L02-09/11) | **Expose** as hierarchy strength (DC-L15-02) |
| P51 | Hierarchy with weight, size and color together | Apple: "Adjust font weight, size, and color" to show hierarchy, and keep the relative hierarchy when text is resized [S-L15-055]. Refactoring UI: size is not everything; use weight and color [S-L15-038]. | Consensus | Text role tokens combining size, weight, color | **Automate** |
| P52 | Headings enable scanning | Layer-cake scanning, one of the more effective patterns, depends on clear headings; the F-pattern appears when they are missing [S-L15-079]. | Moderate (eyetracking) | Heading styles distinct from body | **Automate** |
| P53 | Left-align reading text | "In Western culture, people read top to bottom, left to right, so justify your text left" [S-L15-033]; mirror for RTL [S-L15-053]. | Consensus | Text alignment defaults (L02 DC-L02-18) | **Automate** |
| P54 | Widows and orphans | Avoid a single word on the last line and a paragraph's last line starting a new column [S-L15-033]. | Consensus (craft) | `text-wrap: pretty` / balance on web [inferred implementation] | **Automate** where the platform supports it |

### 1.7 Visual weight, optical adjustments, depth cues and polish

| # | Principle | What it is | Evidence | Levers and tokens | Stance |
|---|---|---|---|---|---|
| P55 | Visual weight | The combined pull of an element. Heavier: larger, darker, warmer, more saturated, textured, regular-shaped, vertical or diagonal, higher on the page, isolated by white space, or simply different from its neighbors (a circle among rectangles) [S-L15-068]. | Consensus (practitioner synthesis) | Every visual token; the input to balance (P17) and dominance (P06) | **Guide** (compute a weight map; flag unintended heavy elements) |
| P56 | Optical size matching | Equal bounding boxes do not look equal: a circle next to a same-size square looks smaller. Matching areas means scaling the circle to 112.84%; for complex shapes use the convex-hull area [S-L15-058]. Material's icon keylines encode the same idea: square 18 dp, circle 20 dp diameter, rectangles 20 x 16 dp inside a 24 dp grid with a 20 dp live area, so icons "maintain consistent visual proportions across system icons" [S-L15-059]. | Consensus with a formula (geometry, not experiment) | Icon keylines, avatar vs logo sizing, shape tokens | **Automate** (normalize icon and shape sizes by area) |
| P57 | Optical centering | Align triangles (play icons) by centroid, not bounding box; the bounding-box center looks off [S-L15-058]. | Consensus with a formula | Icon-in-button centering offsets | **Automate** for known glyphs; **guide** for custom icons |
| P58 | Overshoot | Round and pointed letters extend slightly past baseline and cap height so they look the same size as flat letters (type-design convention) [inferred; general typographic knowledge, not sourced this session]. For UI, the same logic applies to circular icons exceeding square keylines [S-L15-059]. | Consensus (craft) | Icon keylines | **Automate** via keylines |
| P59 | Optical sizing of type | Variable system fonts adjust letterforms to point size ("dynamic optical sizes") [S-L15-055]; thin weights need larger sizes [S-L15-055]. | Consensus (platform spec) | `opsz` axis, size-dependent tracking (L02 DC-L02-04, DC-L02-14) | **Automate** |
| P60 | Icons have an intended size | Icons drawn for 16-24 px look "chunky" at 3-4x; if a large icon slot is needed, put a small icon inside a colored shape [S-L15-038]. Pixel-snap icon coordinates to avoid blur [S-L15-059]. | Consensus | Icon size scale (L03 DC-L03-08), icon container component | **Automate** (icon sizes locked to the drawn sizes; container variant) |
| P61 | Nested radii | Inner radius should equal outer radius minus the padding between them (concentric corners). L04 owns this rule and its values (DC-L04-05). | Consensus (geometry) | `radius.*` derived from padding | **Automate** (compute, see L04 DC-L04-05) |
| P62 | Emulate one light source | Shadows offset downward look natural because light comes from above; insets for wells and inputs; "Shadows can have two parts" (chapter title) [S-L15-038, S-L15-037]; the usual reading is a tight dark shadow plus a soft large one [inferred]. | Consensus | Shadow recipe (L04 DC-L04-12) | **Automate** |
| P63 | Depth signals interactivity | Raised looks pressable, sunken looks fillable [S-L15-009]. Weak signifiers cost 22% more time and 25% more fixations in findability tasks [S-L15-004]. | Moderate (controlled eyetracking, 71 users) | Button fill vs ghost, input field affordance, focus rings | **Automate** strong signifiers on primary actions; **expose** overall signifier strength (DC-L15-09) |
| P64 | Fewer borders | Borders everywhere feel "busy and cluttered"; separate with a shadow, a background change, or more space [S-L15-037, S-L15-038]. | Consensus | Divider usage (L04 DC-L04-08), surface steps | **Guide** (flag nested borders and border-on-border) |
| P65 | Polish details | Refactoring UI's finishing touches: "Supercharge the defaults" (e.g. custom bullets, styled quotes [inferred]), accent borders, decorated backgrounds, designed empty states, "Think outside the box" (chapter titles) [S-L15-037]; accent borders add color to a bland UI without illustration skills [S-L15-038]. | Consensus | Component variants, empty-state templates | **Expose** as optional polish packs |
| P66 | Consistent contrast on images | "Text needs consistent contrast" over photos (chapter title) [S-L15-037], typically via overlay, scrim or text shadow [inferred]; the same failure is at the center of the Liquid Glass critique [S-L15-007]. | Consensus + accessibility standard | Scrim and overlay tokens (L04 DC-L04-18) | **Automate** scrim on text-over-image components |

### 1.8 Refactoring UI tactics, with rationale

Refactoring UI (Adam Wathan and Steve Schoger, 2018; 50 chapters, "over 30,000 copies sold") is written for exactly the builder's audience: "Make your ideas look awesome, without relying on a designer" and "Design with tactics, not talent" [S-L15-037]. The book itself is paid, so this table uses the full public table of contents [S-L15-037], the authors' free article "7 Practical Tips for Cheating at Design" (2018) [S-L15-038] and the free color-palette chapter [S-L15-039]. Rationale marked [inferred] is this lane's reading of a chapter title, not the book's text.

| Tactic (chapter title) | Rationale | Builder mapping | Stance |
|---|---|---|---|
| Start with a feature, not a layout; Detail comes later; Don't design too much | Design the smallest real piece first, low fidelity before polish [inferred] | Builder starts from a component or screen, not an empty page shell | Guide |
| Choose a personality | Typeface, color, radius and copy tone together set personality [inferred from the chapter title S-L15-037; L06 lever matrix gives the mappings] | One brand/personality step before tokens (L06 DC-L06-02) | Expose |
| Limit your choices | Pick from predefined scales instead of free values [inferred from the chapter title S-L15-037]; "you might as well have no color system at all" if the palette grows unchecked [S-L15-039] | Every property is a token picker, free values behind an escape hatch | Automate |
| Use color and weight to create hierarchy instead of size | Size alone overloads the scale; two or three text colors (dark-not-black, grey, lighter grey) and two weights do the job [S-L15-038] | Text role tokens | Automate |
| Don't use grey text on colored backgrounds | The effect of grey on white is reduced contrast; on color, use white at lower opacity or a same-hue tint [S-L15-038] | Per-surface on-color text | Automate |
| De-emphasize to emphasize; Balance weight and contrast | Turn down competitors; heavy icons next to text can be balanced with a softer color [inferred from titles] | Suggestion when user enlarges an element | Guide |
| Labels are a last resort; Separate visual hierarchy from document hierarchy; Semantics are secondary | Hierarchy follows importance, not markup or button semantics [S-L15-037, S-L15-038] | Role tokens decoupled from tags; danger as modifier | Automate |
| Not every button needs a background color | One primary (solid), secondary (outline or low-contrast), tertiary (link); destructive only red when it is the primary action [S-L15-038] | Button variants and per-view lint | Automate + guide |
| Start with too much white space | It is easier to remove space than to add it [inferred] | Generous default density | Automate default |
| Establish a spacing and sizing system; Relative sizing doesn't scale | Fixed scale steps, and do not derive every size from one ratio (large and small elements scale differently) [inferred from titles] | Spacing scale (L03 DC-L03-02) | Automate |
| You don't have to fill the whole screen; Grids are overrated | Intended widths beat stretching; fixed-width sidebars beat percentage columns [inferred from titles] | Max widths, fixed panes | Automate |
| Avoid ambiguous spacing | Space between groups must be clearly larger than space within them (proximity) [inferred from title; matches S-L15-010] | inner < outer constraint | Automate |
| Establish a type scale; Use good fonts; Keep your line length in check; Line-height is proportional; Use letter-spacing effectively; Baseline, not center; Align with readability in mind; Not every link needs a color | Typography craft; L02 holds the values | L02 DC-L02-09, -13, -14, -17, -18 | Automate |
| Ditch hex for HSL; You need more colors than you think; Define your shades up front; Don't let lightness kill your saturation; Greys don't have to be grey | Palettes need 8-10 greys and 5-10 shades per color, defined up front (no `lighten()` on the fly, which yields "35 slightly different blues"); up to ~10 colors x 5-10 shades for complex UIs; "Trust your eyes, not the numbers" [S-L15-039] | Ramp generator (L01 DC-L01-01 to -04; the builder should use OKLCH rather than HSL, per L01) | Automate |
| Accessible doesn't have to mean ugly; Don't rely on color alone | Meet contrast by adjusting lightness within the brand hue; add icons or text for status [inferred from titles; matches L01 DC-L01-23] | Contrast solver | Automate |
| Emulate a light source; Use shadows to convey elevation; Shadows can have two parts; Even flat designs can have depth; Overlap elements to create layers | Offset shadows downward (light from above) [S-L15-038]; depth without shadows via lighter surfaces and overlap [inferred from titles, S-L15-037] | Elevation and shadow tokens (L04 DC-L04-10 to -12) | Automate |
| Use good photos; Text needs consistent contrast; Everything has an intended size; Beware user-uploaded content | Images need scrims, fixed aspect ratios and crop rules [inferred from titles, S-L15-037]; small icons must not be blown up [S-L15-038] | Image component with aspect-ratio and overlay tokens | Automate |
| Supercharge the defaults; Add color with accent borders; Decorate your backgrounds; Don't overlook empty states; Use fewer borders; Think outside the box | Cheap polish: accent borders, patterned backgrounds, designed empty states; replace borders with shadow, background or space [S-L15-037, S-L15-038] | Optional polish pack; border lint | Expose + guide |

### 1.9 The aesthetic-usability effect and what "beautiful" means empirically

| # | Finding | Detail | Evidence | Builder implication |
|---|---|---|---|---|
| P67 | Aesthetic-usability effect (perceived) | Users perceive attractive products as more usable and tolerate minor issues. Origin: Kurosu and Kashimura (Hitachi, 1995), 252 participants rating 26 ATM layouts; aesthetics correlated more with *perceived* than with actual usability [S-L15-003]. Tractinsky et al. (2000) found the same, and later work both replicated it (Hartmann 2008, Lavie and Tractinsky 2004, Quinn and Tran 2010) and failed to (Hassenzahl 2004, van Schaik and Ling 2009) [S-L15-042]. L13 covers it as a UX law [S-L13-010 in L13's trace]. | **Moderate** (mixed replication) | Polish matters for first use and forgiveness; do not market it as usability |
| P68 | Reverse direction | In an 80-person 2x2 study (aesthetics x usability, online shop), aesthetics did not affect perceived usability, but usability affected post-use perceived aesthetics; frustration was the mediator [S-L15-042]. | Moderate (one controlled study) | Usability problems make the product look worse after use. The builder's guide checks for usability (L13) come before its beauty checks |
| P69 | Limits and testing bias | Beauty forgives minor problems, not major ones; in usability tests participants praise visuals and under-report problems, so watch what they do, not what they say [S-L15-003]. | Consensus (NN/g field observation) | When the builder exports a polished prototype for testing, remind the user of the masking effect |
| P70 | First impressions in 17-50 ms | Visual complexity and prototypicality affect aesthetic ratings within 17-50 ms; complexity is processed first; low complexity + high prototypicality is most appealing [S-L15-045, S-L15-044]. The Google Research summary ends: "Go for simple and familiar if you want to appeal to your users' sense of beauty" [S-L15-044]. | **Strong** (two studies, 119 real sites) | Default templates should be conventional; brand expression goes into content, color and type, not novel layouts. Links to Jakob's law in L13 |
| P71 | Complexity and colorfulness curves | 2.4 million ratings from ~40,000 people: appeal is an inverted U over complexity, peaking at 4.2 of 10 (group peaks 2.5-4.8); too complex hurts more than too simple (d 2.0 vs 0.6 relative to the peak); colorfulness peaks at 6.1 of 9 with smaller effects (d 0.3 and 0.8); preferences vary by demographic and country [S-L15-047]. A computational model of complexity and colorfulness plus demographics explains about half the variance in appeal after 500 ms [S-L15-046]. | **Strong** (large sample; one research group) | The builder can compute complexity and colorfulness on every screen and show where the design sits relative to the peak; target audience can shift the target [inferred] |
| P72 | Computable aesthetics already exist | Aalto Interface Metrics computes, from a screenshot: contour density, figure-ground contrast, feature congestion (clutter), subband entropy, attention heatmaps (UMSI, MD-EAM), colorfulness, color-harmony distance, grid quality, white-space proportion and color-blindness simulation, each with an evidence and relevance rating [S-L15-080]. | Tooling (metrics cite peer-reviewed work) | The **guide** layer does not need to be invented: reuse these metric families. The repo was last pushed in June 2023, so treat it as reference, not a maintained dependency |

### 1.10 Visual styles and trends

Each style is really a bundle of token settings. The builder can offer these as **style presets** that set many tokens at once (see DC-L15-01), then let users tune. "Durable" means the style's core levers have survived at least one trend cycle and appear in current Tier A systems; "fashionable" means its look is tied to a period and likely to date. Trend status was checked against live sources today: Figma's "Top Web design trends for 2026" [S-L15-050], NN/g articles dated 2024-2025 [S-L15-005, S-L15-006, S-L15-007], Apple's HIG [S-L15-073] and L00's community pulse for Liquid Glass and Material 3 Expressive (`sources/COMMUNITY-SIGNAL.md`).

| Style | Defining levers (token settings) | Era and 2026 status | Durable or fashionable | Accessibility and usability risks |
|---|---|---|---|---|
| **Flat** | No shadows, gradients or textures; solid fills; glyph icons; type and color carry all hierarchy. Microsoft Metro (2011) called it "authentically digital"; Apple flattened around 2013 [S-L15-009]. | Base layer of most systems today | Durable as a base; "ultraflat" is dated | Weak signifiers: +22% task time and +25% fixations when finding targets [S-L15-004]; ghost buttons and links styled as text. Works only with low density, conventional layout and standout key actions [S-L15-004] |
| **Flat 2.0 / semi-flat** | Mostly flat plus subtle shadows, highlights and layers; Material cited as flat 2.0 "with the right priorities"; long shadows cited as flat 2.0 "gone wrong" [S-L15-009]. | Current mainstream (Carbon, Primer, Polaris, Fluent; see L04 DC-L04-10) | Durable | Low if shadows and fills keep boundaries at 3:1 non-text contrast (WCAG 2.2 SC 1.4.11; see L01 DC-L01-22) |
| **Material (M2 → M3 → M3 Expressive)** | M2: elevation shadows; M3: tonal surfaces and dynamic color; M3 Expressive (May 2025): shape library, springs, higher chroma, "hero moments" (L04 DC-L04-06, -19; L06 DC-L06-03). | M3 stable; Expressive APIs still graduating in Compose 1.5.0 alphas, not in a stable release (L00, section d) | Durable (M3), Expressive still settling | Vivid schemes can fail contrast; motion needs reduced-motion handling (L01 DC-L01-10; L04 DC-L04-25) |
| **Skeuomorphism** | Realistic textures, shadows and gradients imitating physical objects; as a *learning aid* (folder, trash icons) it "has never been truly dead" [S-L15-008]. Peak early 2010s; led to "cluttered interfaces and slower load times" [S-L15-008]. | Functional metaphors survive; claims of a 2025-26 "tactile return" are Tier C only [S-L15-077] | Metaphor durable; realism fashionable | Textures reduce text contrast and add GPU cost [inferred from S-L15-008] |
| **Neumorphism (soft UI)** | Elements the same color as the background, extruded or inset with paired light and dark soft shadows; muted, low-saturation palette; rounded corners [S-L15-060]. Late 2010s, from a viral Dribbble concept [S-L15-060]. | IxDF calls it more "stylistic experiment" than lasting trend [S-L15-060]; Figma still lists it as a 2026 web trend [S-L15-050] (disagreement; the brand examples Figma gives were not verified) | Fashionable | Low contrast by design: control boundaries and states are hard to see, likely failing 3:1 non-text contrast [S-L15-060; SC mapping inferred] |
| **Glassmorphism** | Translucent fill (opacity), background blur, optional thin light stroke and gradient; best over rich backgrounds [S-L15-005]. Fluent Acrylic, macOS Big Sur, Windows 11 [S-L15-005, S-L15-078]. | Since 2020; now absorbed into platform "materials" | Durable as a platform material; fashionable as decoration | Text contrast varies with what is behind; background clutter; blur and motion sensitivity; GPU cost; weak high-contrast fallbacks [S-L15-078]. Mitigate with more blur, solid overlays behind text, and honoring Reduce Transparency [S-L15-005] |
| **Liquid Glass (Apple)** | Translucent material that refracts surroundings with specular highlights; a functional layer for controls and navigation above content; regular and clear variants; for clear over bright content consider a 35% dark dimming layer; "Use Liquid Glass effects sparingly"; never in the content layer [S-L15-073]. | Introduced June 2025 (iOS 26); iOS 26.1 added Clear/Tinted; iOS 27 (released around 14 Sep 2026) added a transparency slider and darker edges, per L00 (section e). The HIG change log still shows 9 Sep 2025 as the last materials update [S-L15-073] | Durable on Apple platforms (it is the OS); fashionable when imitated on the web | iOS 26-era critique: text over busy backgrounds, text on text, motion without meaning, smaller and more crowded targets, unpredictable controls [S-L15-007]. Designs must hold from fully clear to fully tinted and with Reduce Transparency on (L00) |
| **Neo-brutalism** | High contrast, bold primary colors, thick borders, blocky layout, solid offset shadow (e.g. a 4 px black shadow), oversized or quirky type, retro UI bits; Figma and Gumroad brand refreshes cited [S-L15-006]. | NN/g article April 2025 [S-L15-006]; in Figma's 2026 list as "neo-brutalism / anti-design" [S-L15-050] | Fashionable look; its high-contrast core ages better [inferred] | Bright pairs such as yellow and cyan fail text contrast; visual noise; NN/g advice: 2-3 colors, neutral body font, 24-32 px padding, clear hover and state changes [S-L15-006] |
| **Bento grid** | Tiles of different spans in a tight grid with one consistent gap; one idea per tile; the hero tile is largest. It is a hierarchical/modular grid in NN/g's terms [S-L15-065]. The popular origin story (Apple keynote and product-page grids around 2023, with Windows Metro tiles as precursor) is Tier C only [S-L15-062]. | Widespread on marketing pages 2024-2026 (Tier C) [S-L15-062]; not in Figma's 2026 list [S-L15-050] | Layout pattern durable; the specific look fashionable [inferred] | Visual order can diverge from DOM and reading order (WCAG 1.3.2 meaningful sequence) [inferred]; equal-weight tiles remove the dominant element (P06); reflow on narrow screens |
| **Maximalism, collage, retrofuturism, "dopamine" palettes** | Rich saturated colors, overlapping visuals, bold type, dense compositions, stickers and textures, neon and chrome [S-L15-050]. | Figma 2026 trends list [S-L15-050] | Fashionable | Conflicts with the complexity evidence: too much complexity costs more appeal than too little [S-L15-047]. Keep to marketing and brand moments, never dense app UI [inferred] |
| **Swiss / International style (minimal grid)** | Strict grids, sans-serif type, asymmetric layouts, generous white space; Müller-Brockmann's grid systems [S-L15-072]. | Underlies most product UI and design systems today [inferred] | Durable | Low; risk is blandness and weak signifiers if taken to "ultraflat" (see Flat) |

**Pattern across styles** [inferred]: durable styles change *surface treatment* (depth, material, texture) but keep hierarchy, grouping and contrast intact; styles that date quickly are the ones that sacrifice a principle for a look (neumorphism gives up contrast, ultraflat gives up signifiers, heavy glass gives up legibility, maximalism gives up simplicity). The builder can state this in its UI: every preset shows which principles it strains.

### 1.11 Critique vocabulary the builder can use for feedback

NN/g's rule for critique is to tie feedback to the design's objective and turn opinion ("This is too red!") into goal-linked observations [S-L15-075]. Williams' promise, "Once you can name the problem, you can find the solution" [S-L15-070], is the reason to give engineers the vocabulary. Each term below is phrased as a builder message template: **observation → principle → why it matters → one-click fix**.

| Designer's phrase | What is actually wrong | Detectable signal | Builder message and fix | Principle | Source |
|---|---|---|---|---|---|
| "Everything is shouting" / "no entry point" | Several elements share top emphasis | More than one element at the largest size or strongest contrast in a view | "3 elements compete for first look. Demote two to the secondary level?" | P06, P05 | [S-L15-067] |
| "Type soup" | Too many sizes, weights or families | More than 3 sizes, more than 3 weights, or more than 2 families in a view | "This view uses 6 text sizes. Snap to the 3 nearest roles?" | P02, P48 | [S-L15-001, S-L15-055] |
| "It's conflict, not contrast" / "too similar" | Two levels differ, but not enough to read as different | Adjacent size ratio under the scale minimum; weights 100 apart; similar pairing | "Heading and body are too close in size. Increase the step or the weight gap." | P07 | [S-L15-070, S-L15-030] |
| "Busy" / "cluttered" / "noisy" | Too many borders, colors or elements | Border count, distinct colors, feature-congestion or contour-density score | "12 borders on this card. Replace inner borders with spacing?" | P64, P71 | [S-L15-038, S-L15-080] |
| "Cramped" / "needs to breathe" | Not enough negative space | White-space proportion below the density target; elements touching edges | "Content touches the container edge. Apply the default inset." | P22, P33 | [S-L15-020, S-L15-033] |
| "Floating" / "ambiguous spacing" | A label or element is as close to the wrong group as to its own | Gap to own group not smaller than gap to neighboring group | "This label is equidistant from two fields. Tighten it to its field." | P23 | [S-L15-010, S-L15-037] |
| "Ragged" / "misaligned" | Too many distinct left edges | Count of unique x-positions; AIM-style grid-quality score | "5 different left edges. Snap to the column grid?" | P14 | [S-L15-053, S-L15-080] |
| "Muddy" | Colors differ in hue but not in value | Low luminance difference between adjacent colors | "These two colors look the same in grayscale." | P44 | [S-L15-025] |
| "Rainbow" / "too colorful" | Accent spread across many elements | Accent-colored area share; number of hues | "Accent color is on 9 elements. Keep it for the primary action and status?" | P39, P42 | [S-L15-025, S-L15-054] |
| "Washed out" | Grey text on a colored surface | Secondary text token used on a non-neutral surface | "Use the on-color secondary text for this surface." | P47 | [S-L15-038] |
| "Heavy" / "lopsided" / "unbalanced" | Visual weight concentrated on one side unintentionally | Weight map from size, value, saturation and position | "The left column carries most of the visual weight." | P55, P17 | [S-L15-068, S-L15-001] |
| "Doesn't look clickable" | Weak signifiers | Ghost or text-styled primary actions; links same style as text | "Primary action is a ghost button. Use the solid variant?" | P63, P24 | [S-L15-004, S-L15-013] |
| "Boxes in boxes" | Common region overused | Nested containers deeper than 2 | "3 levels of nested cards. Replace the inner card with spacing?" | P25 | [S-L15-012] |
| "Chunky icons" | Small-drawn icons scaled up | Icon rendered above its drawn size | "This 20 px icon is shown at 64 px. Use the icon-in-shape variant." | P60 | [S-L15-038] |
| "Optically off" | Geometric but not optical centering or sizing | Triangle glyph centered by bounding box; circle and square same box size | Auto-correct (centroid alignment; area matching) | P56, P57 | [S-L15-058] |
| "Doesn't feel like one family" | Inconsistent styles for the same function | Two styles for one component role, or off-token values | "2 button styles do the same job. Merge?" | P15, P24 | [S-L15-011, S-L15-070] |
| "Widow" | A single word on a paragraph's last line | Text layout check | Apply balanced or pretty wrapping | P54 | [S-L15-033] |
| "Tangent" / "trapped white space" | Edges that nearly touch, or awkward enclosed gaps | Near-coincident edges under 4 px; enclosed empty regions | "These edges almost touch. Align them or separate them." | P14, P22 | [inferred; common studio vocabulary, no source found] |
| "Looks dated" / "looks like 2020" | A style preset whose look is tied to a period | Preset label (e.g. neumorphic shadows) | Point to the style card and its durability note | 1.10 | [inferred] |

---

## 2. Decision Cards

These cover the places where visual-design principles leave a real choice. Token-level cards in L01-L04 and L06 are referenced, not repeated.

### DC-L15-01: Visual style direction (style preset)
- **Block path:** Foundations > Visual language > Style preset
- **Questions the designer answers:** What overall look should the product have? How much depth, material or decoration? Are we native-first on Apple or Android? How much trend risk can we take?
- **Options:**
  - **Flat 2.0 / semi-flat** (the mainstream of Carbon, Primer, Polaris and Fluent; values in L04 DC-L04-10 and DC-L04-12). Mostly flat surfaces, subtle shadows or tonal steps, clear signifiers [S-L15-009].
  - **Material tonal (M3)**: tonal surface steps and dynamic color; M3 Expressive adds shape library, springs and higher chroma (L04 DC-L04-06, DC-L06-03; still alpha in Compose per L00).
  - **Glass / material**: Apple Liquid Glass for controls and navigation only, regular variant by default, a 35% dimming layer under clear glass over bright content [S-L15-073]; Fluent Acrylic for menus over varied backgrounds [S-L15-005].
  - **Neo-brutalist**: thick borders, solid offset shadow (e.g. 4 px black), 2-3 bold colors, 24-32 px padding, quirky display face with neutral body face; Figma and Gumroad brands cited [S-L15-006].
  - **Soft / neumorphic**: same-color extruded surfaces with paired soft shadows [S-L15-060]. Offered only with a contrast warning.
  - **Expressive / maximal** (marketing only): vibrant palettes, overlapping visuals, bold type [S-L15-050].
- **Visual effect:** Flat 2.0 reads neutral, efficient and timeless; Material tonal reads friendly and systematic; glass reads premium and native on Apple but can obscure content [S-L15-007]; neo-brutalist reads bold, indie and irreverent; neumorphic reads soft and tactile but vague; maximal reads energetic and youthful but busy [inferred from S-L15-006, S-L15-060, S-L15-050].
- **Depends on (upstream):** brand personality (L06 DC-L06-02), expressiveness and hero-moment budget (L06 DC-L06-03), platform deference (L06 DC-L06-14), audience and density (DC-L15-04).
- **Affects (downstream):** depth strategy and shadow recipe (L04 DC-L04-10, -12), materials (L04 DC-L04-15, -16), roundness (L04 DC-L04-02), border widths (L03 DC-L03-09), chroma level (L01 DC-L01-10), type classification (L02 DC-L02-02), signifier strength (DC-L15-09).
- **Token encoding:** a preset is not a DTCG type. Store it as builder metadata (`$extensions.builder.stylePreset: "flat2" | "tonal" | "glass" | "neobrutal" | "soft" | "maximal"`) that writes primitives such as `shadow.raised` ($type shadow), `border.width.default` ($type dimension), `color.surface.glass` (color with alpha) and `blur.backdrop.md` (dimension, a DTCG gap noted in L04 DC-L04-28) [inferred].
- **Platform notes:** On iOS 26 and later, standard components get Liquid Glass automatically; custom glass should be sparing [S-L15-073]. M3 Expressive is Android/Compose-first (L00). Web glass needs `backdrop-filter` and a solid fallback [inferred].
- **Accessibility constraints:** WCAG 2.2 text contrast 4.5:1 and non-text contrast 3:1 (L01 DC-L01-22) rule out default neumorphism and uncontrolled glass; Reduce Transparency and Increase Contrast must swap glass for solid (L04 DC-L04-16; [S-L15-005]); preset motion must honor reduced motion (L04 DC-L04-25).
- **Default + heuristic:** Default to Flat 2.0 with strong signifiers. Heuristic: pick the style whose strained principle (see section 1.10) your product can afford; reserve fashionable styles for marketing surfaces and keep the app surface on a durable base.
- **Evidence:** [S-L15-004, S-L15-005, S-L15-006, S-L15-007, S-L15-009, S-L15-050, S-L15-060, S-L15-073]

### DC-L15-02: Hierarchy strength (how dramatic the contrast between levels is)
- **Block path:** Foundations > Visual language > Hierarchy > Strength
- **Questions the designer answers:** How big is the jump between a heading and body text? Do we create emphasis mainly with size, weight or color? How many levels does a typical screen need?
- **Options:**
  - **Subtle / productive**: type ratio about 1.125-1.2 (16, 18, 20, 23 px at 1.125, computed in L02 DC-L02-09); weights 400 and 600; emphasis mostly through color tier and weight [S-L15-038]. Carbon productive set (L02 DC-L02-11).
  - **Balanced**: ratio 1.25 (16, 20, 25, 31, 39 px); weights 400/600/700.
  - **Dramatic / expressive**: ratio 1.333 or more, or The Futur's "double point size", with 3x-4x "for drama" [S-L15-033]; display styles with large jumps (Carbon fluid display, L02 DC-L02-11); the Futur composition formula of one very big object [S-L15-028].
  - **Lead lever**: size-led (editorial), weight-led, or color-led (dense apps) [S-L15-038, S-L15-055].
- **Visual effect:** Subtle reads calm, dense, professional and "quiet"; dramatic reads editorial, confident, marketing-grade. Too subtle produces "conflict" (levels that almost match) [S-L15-070]; too dramatic leaves few usable steps (L02 DC-L02-09).
- **Depends on (upstream):** brand personality (L06 row A and D), density voice (DC-L15-04), surface type (app vs marketing, L02 DC-L02-11).
- **Affects (downstream):** type scale ratio and step count (L02 DC-L02-09, -10), weight palette (L02 DC-L02-15), text color tiers (L01 DC-L01-14), button prominence (P08), section spacing (L03 DC-L03-24).
- **Token encoding:** generator metadata `$extensions.builder.hierarchy = { ratio: 1.25, weights: [400, 600], textTiers: 3 }` feeding `font.size.*` (dimension), `font.weight.*` (fontWeight), `color.text.*` (color) [inferred].
- **Platform notes:** Hierarchy must survive Dynamic Type and Android font scaling: "maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes" [S-L15-055].
- **Accessibility constraints:** Color-only hierarchy fails people with low vision or color deficiency; NN/g: "Do not rely only on color" [S-L15-002]. Secondary text tiers still need 4.5:1 (L01 DC-L01-14).
- **Default + heuristic:** Default balanced (1.25, two weights, three text colors). Heuristic: the builder should keep adjacent levels at least about 10% apart in size (L02 DC-L02-10) *or* 200 apart in weight [inferred], so levels never read as "almost the same".
- **Evidence:** [S-L15-002, S-L15-028, S-L15-033, S-L15-038, S-L15-055, S-L15-070]

### DC-L15-03: Emphasis budget (focal points, primary actions, accent area)
- **Block path:** Foundations > Visual language > Hierarchy > Emphasis budget
- **Questions the designer answers:** How many things may compete for first look on one screen? How many primary buttons per view? How much of the screen may carry the accent color? How many "hero moments" does the product get?
- **Options:**
  - **Strict**: one dominant element and one primary action per view [S-L15-067, S-L15-038]; accent color only on primary actions, selection and status (Apple: "Refrain from adding color to the background of multiple controls") [S-L15-054]; accent area kept small (60-30-10 as a soft check, not a rule) [S-L15-026, S-L15-048].
  - **Moderate**: one primary plus one highlighted secondary; accent also on links and active navigation; accent borders for flair [S-L15-038].
  - **Expressive**: Material 3 Expressive's budget of one or two "hero moments" per product (L06 DC-L06-03); large color areas on chrome for playfulness (L06 row A).
- **Visual effect:** Strict reads calm, clear and premium; moderate reads friendly; expressive reads energetic but risks "everything is shouting" [S-L15-067].
- **Depends on (upstream):** brand expressiveness (L06 DC-L06-03), role of brand color (L06 DC-L06-04), style preset (DC-L15-01).
- **Affects (downstream):** button variants (P08), accent token usage, lint rules, status color distinctness (L01 DC-L01-15).
- **Token encoding:** lint configuration rather than tokens: `$extensions.builder.lint = { maxPrimaryPerView: 1, maxTopEmphasis: 1, accentAreaWarn: 0.15 }` [inferred; 0.15 is a proposed soft threshold, not a sourced number].
- **Platform notes:** Apple colors the background of the prominent button, not symbols or text, on Liquid Glass [S-L15-054].
- **Accessibility constraints:** Emphasis cannot rely on color alone (L01 DC-L01-23); motion-based emphasis must respect reduced motion (L04 DC-L04-25).
- **Default + heuristic:** Default strict for app surfaces, moderate for marketing. Heuristic: if you need two primaries, one of them is secondary.
- **Evidence:** [S-L15-026, S-L15-038, S-L15-048, S-L15-054, S-L15-067]

### DC-L15-04: Density voice (compact, comfortable, spacious)
- **Block path:** Foundations > Visual language > Density voice
- **Questions the designer answers:** Should the product feel airy and premium or dense and utilitarian? Does density change between app, docs and marketing? Can users choose?
- **Options:** Compact, comfortable, spacious, or user-selectable (L03 DC-L03-10 lists real implementations: Material density steps of about 4 dp, Salesforce comfy/cozy/compact, Carbon and Fluent size props). This card adds the *voice* view: spacious = calm, premium, focused message; compact = serious, efficient, expert (L03 DC-L03-10 quoting Material).
- **Visual effect:** Spacious layouts look confident but can frustrate repeat users with low information density [S-L15-003]; compact layouts look efficient but need strong grouping and signifiers to stay readable [S-L15-004].
- **Depends on (upstream):** audience and task frequency; brand personality (L06 row C and E); style preset (DC-L15-01).
- **Affects (downstream):** spacing semantics and density modes (L03 DC-L03-10, -11), whitespace ratio (L03 DC-L03-24), control heights (L03 DC-L03-07), type size in compact modes (L02), signifier strength (DC-L15-09).
- **Token encoding:** a `density` mode on the semantic spacing layer (L03 DC-L03-11).
- **Platform notes:** Touch surfaces cannot go as dense as pointer surfaces; target minimums stay fixed (L03 DC-L03-12).
- **Accessibility constraints:** Target size floors (WCAG 2.5.8 24 px; Material 48 dp) never shrink with density (L03 DC-L03-10).
- **Default + heuristic:** Comfortable for app surfaces, spacious for marketing, compact as a user option for data-heavy tools. Heuristic: the denser the layout, the stronger the grouping and signifiers must be [inferred from S-L15-004].
- **Evidence:** [S-L15-003, S-L15-004] plus L03 DC-L03-10, -11, -24

### DC-L15-05: Grouping strategy (space, containers or lines)
- **Block path:** Foundations > Visual language > Grouping
- **Questions the designer answers:** Do we separate groups with white space alone, with cards and backgrounds, or with divider lines? How deep may containers nest?
- **Options:**
  - **Space-first (implicit grouping)**: proximity alone, larger outer than inner gaps; Carbon and Fluent note space can replace dividers (L03 DC-L03-24); Refactoring UI "Use fewer borders" [S-L15-037].
  - **Container-first (common region)**: cards and tinted panels; strongest grouping cue, fixes proximity failures (the Food Network card example) and supports multi-type content [S-L15-012].
  - **Line-first (rules and separators)**: The Futur "Group by Using Rules" [S-L15-033]; Apple lists separators alongside negative space and container shapes [S-L15-053]; best for long homogeneous lists [inferred].
  - **Connectedness** for sequences (steppers, timelines, trees) [S-L15-013].
- **Visual effect:** Space-first looks lighter, calmer and more modern; container-first looks structured and "enterprise", and becomes "boxes in boxes" when overused [S-L15-012]; line-first looks orderly and editorial but busy if lines multiply [S-L15-038].
- **Depends on (upstream):** density voice (DC-L15-04), style preset (DC-L15-01), content heterogeneity.
- **Affects (downstream):** card component usage, divider tokens (L04 DC-L04-08), surface steps (L01 DC-L01-13), inner/outer spacing ratio (L03 DC-L03-24).
- **Token encoding:** `space.inset.*`, `space.stack.inner/outer` (dimension); `color.surface.container` (color); `border.width.divider` (dimension); builder lint `maxContainerDepth: 2` [inferred].
- **Platform notes:** iOS grouped table style uses grouped background colors (primary/secondary/tertiary) for regions [S-L15-054].
- **Accessibility constraints:** Container boundaries that carry meaning need 3:1 non-text contrast (L01 DC-L01-22); zebra striping must not be the only row cue for tables [inferred].
- **Default + heuristic:** Space first; add a container only when content types mix, items sit in a grid, or spacing cannot be controlled; use lines for long lists. Keep inner:outer spacing at 1:2 or more (L03 DC-L03-24).
- **Evidence:** [S-L15-010, S-L15-012, S-L15-013, S-L15-033, S-L15-037, S-L15-038, S-L15-053, S-L15-054]

### DC-L15-06: Color scheme strategy and accent proportion
- **Block path:** Foundations > Color > Scheme strategy (principle level; L01 owns ramps and roles)
- **Questions the designer answers:** One accent or several? Should accents harmonize with the brand hue or contrast with it? How much of the screen should be colored?
- **Options:**
  - **Neutral + one accent** (Linear, Notion per L06 row C): most harmonious and calm; the pattern Apple recommends when content is monochrome [S-L15-054].
  - **Analogous family**: neighboring hues for surfaces and illustrations; lab data show hue similarity raises both harmony and pair preference [S-L15-017].
  - **Contrasting (complementary-ish) accent on analogous neutrals**: figure colors are liked more when they contrast in hue with their background [S-L15-017]; this is the strongest "pop" for primary actions.
  - **Multi-accent** (Mailchimp per L06 row A): playful, but needs strict role rules.
  - **Wheel presets** (complementary, triadic, split-complementary): Refactoring UI calls wheel-generated five-swatch palettes "not very useful" for UI [S-L15-039]; offer them only for choosing accent hues.
  - **Proportion guide**: 60-30-10 [S-L15-026], treated as folk wisdom [S-L15-048].
- **Visual effect:** neutral + one accent reads focused and premium; analogous reads harmonious and soft; contrasting accent reads energetic and directs the eye; multi-accent reads playful and consumer [inferred, consistent with L06 lever matrix].
- **Depends on (upstream):** brand color and its role (L06 DC-L06-04, DC-L06-05), chroma level (L01 DC-L01-10), neutral temperature (L01 DC-L01-06).
- **Affects (downstream):** accent count (L01 DC-L01-08), status color distinctness (L01 DC-L01-15), data-viz palette (L01 DC-L01-24), emphasis budget (DC-L15-03).
- **Token encoding:** generator metadata `$extensions.builder.scheme = { strategy: "neutral+1", accentHue: 262 }` producing `color.brand.*`, `color.accent.*` ramps ($type color, DTCG 2025.10 color objects per L01) [inferred].
- **Platform notes:** Android dynamic color may override the scheme (L01 DC-L01-21); Apple accent colors can be replaced by the user's system accent on macOS [S-L15-054].
- **Accessibility constraints:** Complementary pairs at similar lightness vibrate and fail contrast; lightness contrast, not hue contrast, carries legibility [S-L15-017, S-L15-025]; never encode meaning in hue alone (L01 DC-L01-23).
- **Default + heuristic:** Neutral + one accent, with analogous tints for surfaces. Heuristic: harmonize the large areas, contrast the small important ones.
- **Evidence:** [S-L15-017, S-L15-025, S-L15-026, S-L15-039, S-L15-048, S-L15-054]

### DC-L15-07: Composition and grid model
- **Block path:** Foundations > Layout > Composition model (principle level; L03 owns columns, gutters, breakpoints)
- **Questions the designer answers:** Do pages follow a strict column grid, a repeating module grid, a hierarchy of big and small tiles, or a free editorial layout? When may the grid be broken?
- **Options (NN/g's three grid types plus free layout)** [S-L15-065]:
  - **Column grid**: 4 columns on mobile, 12 on desktop is the common pattern [S-L15-065]; product UI default.
  - **Modular grid**: columns plus rows; suits catalogs and galleries (Behance example) [S-L15-065].
  - **Hierarchical grid**: the most important content takes the largest area (New York Times example) [S-L15-065]; the "bento" look is a hierarchical grid of rounded tiles [S-L15-062 (Tier C) + S-L15-065].
  - **Free / broken grid**: editorial and marketing; breaking the grid "calls more attention" and needs "a valid reason" [S-L15-065].
- **Visual effect:** column = orderly and neutral; modular = browsable and even; hierarchical/bento = curated, product-launch feel with a clear hero; free = expressive, magazine-like, riskier to scan [S-L15-065; bento feel inferred].
- **Depends on (upstream):** style preset (DC-L15-01), content type, surface (app vs marketing).
- **Affects (downstream):** column tokens and container widths (L03 DC-L03-15, -16), card sizes, responsive reflow rules (L03 DC-L03-21/22), reading order in code.
- **Token encoding:** `grid.columns.*` (number), `grid.gutter.*`, `grid.margin.*` (dimension); bento tile spans as layout-component props, not tokens [inferred].
- **Platform notes:** Apple: base layout on size classes, not device type; keep layout changes "recognizable and familiar" across sizes [S-L15-053].
- **Accessibility constraints:** DOM order must match visual reading order in bento and broken grids (WCAG 1.3.2) [inferred]; reflow at 320 CSS px (WCAG 1.4.10, L03).
- **Default + heuristic:** Column grid for app surfaces; hierarchical or bento for marketing feature sections. Heuristic: every grid break should be nameable ("this hero breaks the grid to signal X").
- **Evidence:** [S-L15-053, S-L15-062, S-L15-065, S-L15-072]

### DC-L15-08: Balance and alignment axis
- **Block path:** Foundations > Layout > Balance
- **Questions the designer answers:** Do layouts hang on a left edge (asymmetric) or a center axis (symmetric)? Where is centering allowed?
- **Options:**
  - **Left-aligned asymmetric** (Swiss tradition; product UI default): matches reading order and Apple's "top and leading side" guidance [S-L15-053, S-L15-072]; The Futur "Justify Left" and "Align to One Axis" [S-L15-033]. Asymmetry "creates a sense of energy and movement" [S-L15-001].
  - **Centered symmetric**: marketing heroes, empty states, dialogs, sign-in screens; "Symmetry is quiet and static" [S-L15-001]; symmetry reads as orderly [S-L15-049].
  - **Radial**: rare in UI (gauges, radial menus) [S-L15-001; Figma lists radial menus under experimental navigation S-L15-050].
- **Visual effect:** left-aligned reads efficient, modern and scannable; centered reads calm, ceremonial and "landing page"; long centered text reads poorly [inferred from S-L15-033].
- **Depends on (upstream):** style preset (DC-L15-01), writing direction (RTL).
- **Affects (downstream):** text alignment defaults (L02 DC-L02-18), hero and empty-state templates, dialog layout.
- **Token encoding:** component and template props (`align: start | center`), mirrored automatically for RTL (`start/end`, not `left/right`) [inferred].
- **Platform notes:** Use logical start/end so RTL mirrors correctly [S-L15-053].
- **Accessibility constraints:** Centered multi-line body text is harder to read (ragged left edge) [inferred]; keep centered text to short lines.
- **Default + heuristic:** Start-aligned everywhere; center only single-focus moments with short text.
- **Evidence:** [S-L15-001, S-L15-033, S-L15-049, S-L15-050, S-L15-053, S-L15-072]

### DC-L15-09: Interactive signifier strength
- **Block path:** Foundations > Visual language > Signifiers
- **Questions the designer answers:** How obviously should clickable things look clickable? Can secondary actions be ghost buttons? Are links underlined or only colored? Do inputs have visible borders?
- **Options:**
  - **Strong**: filled or slightly raised primary buttons, colored and underlined links, bordered inputs, color reserved for interactive elements. NN/g's strong variants used "slightly 3D style buttons" and a color used only on interactive elements [S-L15-004].
  - **Balanced**: filled primary, outline secondary, link-style tertiary [S-L15-038]; links colored, underlined on hover [S-L15-006 recommends underline on hover].
  - **Minimal**: ghost buttons, links styled like text, borderless inputs.
- **Visual effect:** strong reads obvious and slightly traditional; minimal reads sleek but costs 22% more time and 25% more fixations to find targets [S-L15-004].
- **Depends on (upstream):** style preset (DC-L15-01), density (DC-L15-04), audience familiarity.
- **Affects (downstream):** button variants, link style (L02 "Not every link needs a color" nuance), input field style, focus indicator (L04 DC-L04-09), depth tokens.
- **Token encoding:** component tokens `button.primary.background`, `link.text-decoration` (string), `input.border.width` (dimension) [inferred].
- **Platform notes:** Apple uses tint on the button background for prominent actions [S-L15-054]; Liquid Glass controls float above content and can lose affordance over busy content [S-L15-007].
- **Accessibility constraints:** Input and button boundaries need 3:1 non-text contrast (L01 DC-L01-22); links distinguished from text by more than color (L01 DC-L01-23).
- **Default + heuristic:** Balanced, with strong signifiers forced for primary actions. Heuristic from NN/g: go minimal only when density is low, layouts are conventional and key actions already stand out; all three must hold [S-L15-004].
- **Evidence:** [S-L15-004, S-L15-006, S-L15-007, S-L15-038, S-L15-054]

### DC-L15-10: Optical correction policy (polish automation)
- **Block path:** Foundations > Visual language > Polish
- **Questions the designer answers:** Should the builder silently correct optical issues (icon sizes, centering, nested radii, type optical sizing), suggest them, or leave geometry exact?
- **Options:**
  - **Geometric only**: exact values, no corrections.
  - **Auto-correct known cases**: area-matched icon and shape sizes (circle scaled to 112.84% of a square's box; convex-hull area for complex shapes) [S-L15-058]; Material-style keylines (square 18, circle 20, rectangles 20 x 16 in a 24 grid) [S-L15-059]; centroid centering for triangles [S-L15-058]; concentric nested radii (L04 DC-L04-05); dynamic optical sizes and heavier weights at small sizes [S-L15-055]; pixel-snapped icon coordinates [S-L15-059].
  - **Auto + suggest for custom assets**: apply the above to system parts, flag user-imported icons that break keylines.
- **Visual effect:** corrected designs look "right" without users knowing why; uncorrected designs look subtly off (play icons drift, circular avatars look small next to square logos) [S-L15-058].
- **Depends on (upstream):** icon set choice (L05), radius scale (L04 DC-L04-01), type family and variable-font support (L02 DC-L02-04).
- **Affects (downstream):** icon component, avatar and logo sizing, button icon offsets, card radius derivation.
- **Token encoding:** keyline sizes as `icon.keyline.square/circle` (dimension); radius derived as `radius.inner = radius.outer - space.inset` (computed alias, L04 DC-L04-05) [inferred].
- **Platform notes:** SF Symbols already match text weights and align with the system font [S-L15-055]; Material icons ship with keylines [S-L15-059]; custom web icon sets vary [inferred].
- **Accessibility constraints:** None directly; keep icon hit targets at platform minimums regardless of optical size (L03 DC-L03-12).
- **Default + heuristic:** Auto-correct known cases, suggest for custom assets. Heuristic from Bjango: prefer a formula to eyeballing when one exists, "No matter what, you're still going to have to use your best judgement" [S-L15-058].
- **Evidence:** [S-L15-055, S-L15-058, S-L15-059]

### DC-L15-11: Builder feedback mode (critique strictness)
- **Block path:** Builder > Guidance > Feedback mode
- **Questions the designer answers:** Should the builder stay quiet and just enforce, coach with named principles, or block export on violations? Should it show computed scores?
- **Options:**
  - **Silent**: only automate-stance rules apply; no messages.
  - **Coach**: inline messages using the critique vocabulary of section 1.11, each tied to a goal and a one-click fix, following NN/g's goal-linked critique rule [S-L15-075].
  - **Strict**: block export on hard failures (contrast, more than one primary, targets below minimum); warnings for the rest.
  - **Metrics panel**: AIM-style scores (clutter, colorfulness, grid quality, white space, attention heatmap) with the target band from the complexity research [S-L15-080, S-L15-047].
- **Visual effect:** not visual in the product; changes how quickly non-designers converge on a clean result [inferred].
- **Depends on (upstream):** user skill level; team governance (L11).
- **Affects (downstream):** lint configuration, onboarding, review workflow (L11), exported documentation.
- **Token encoding:** builder config, not tokens (`$extensions.builder.feedback = "coach"`) [inferred].
- **Platform notes:** Metrics computed on screenshots work for any platform; structural lints need the builder's own component tree [inferred].
- **Accessibility constraints:** Accessibility failures (contrast, target size) should be at least warnings in every mode, and blocking in strict mode [inferred, consistent with L01 DC-L01-22 enforcement].
- **Default + heuristic:** Coach by default for engineers; strict for teams shipping to production; metrics panel as an advanced view. Heuristic: every message names the principle, so users learn the vocabulary (Williams: "Once you can name the problem, you can find the solution" [S-L15-070]).
- **Evidence:** [S-L15-047, S-L15-070, S-L15-075, S-L15-080]

---

## 3. Automate, guide, expose: the builder policy in one table

| Stance | Principles (catalog numbers) | How the builder does it |
|---|---|---|
| **Automate** (by construction) | Text tiers and weights (P01, P03, P04, P51), few type sizes (P02), minimum tier gaps (P07), button variants (P08), RTL mirroring and headings (P09, P52, P53), role tokens decoupled from tags (P10), alignment snapping and grids (P14, P35), repetition and consistency (P15), proximity via inner < outer spacing (P16, P23), rhythm (P18), small palettes and family counts (P19, P48), scale systems (P20), generous default space and max widths (P22, P37), similarity through variants (P24), connectors in sequence components (P26), surface steps for figure-ground (P29), restraint by default (P30), common-fate motion (P32), neutral-first role ramps with controlled chroma (P39, P40, P43), value-contrast checks (P44), on-color text (P47), optical corrections (P56, P57, P58, P59, P60, P61), one light source (P62), strong primary signifiers (P63), scrims on text over images (P66) | Generated tokens and components already obey the rule; free values sit behind an escape hatch |
| **Guide** (warn and suggest) | Per-screen hierarchy (P01, P02, P06), de-emphasis suggestions (P05), more than one primary (P08), labels (P11), off-grid and stray edges (P14, P36), ambiguous spacing (P23), style collisions (P24), nested containers (P25), weak surface separation (P29), closure in icons (P28), accent overuse and 60-30-10 soft check (P39, P42), near-identical font pairs (P49), visual-weight imbalance (P55), border clutter (P64), dense + weak signifiers (P34), composition templates (P38), complexity and colorfulness readouts (P71, P72), prototype-testing reminder (P69) | Critique vocabulary messages (section 1.11), each with a one-click fix; metrics panel optional (DC-L15-11) |
| **Expose** (user control) | Balance and symmetry (P17, P31), scale ratio including golden ratio (P20, P21), density and whitespace voice (P22, P33, P34), containment level (P25), grid type (P35), accent hue and colorfulness (P41, P46), neutral temperature (P45), pairing presets (P49), size ratio as hierarchy strength (P50), polish packs (P65), style preset, hierarchy strength, emphasis budget, scheme strategy, signifier strength, optical policy and feedback mode (DC-L15-01 to DC-L15-11) | A small number of high-level dials that each move many tokens (consistent with L06's "one brand dial" finding) |

**The most important split** [inferred]: automate the principles with strong or consensus evidence and one right answer (grouping, alignment, consistency, contrast minimums, optical corrections); expose the ones that encode personality (density, hierarchy strength, style, color strategy); guide everything that depends on the specific screen's content, because only the user knows which element matters most.

## 4. Decision graph (what drives what)

```
Brand personality (L06 DC-L06-02) ──┬─> DC-L15-01 Style preset ──> depth, materials, radius, borders (L04), chroma (L01)
                                    ├─> DC-L15-04 Density voice ──> spacing modes (L03), type size in compact (L02)
                                    ├─> DC-L15-02 Hierarchy strength ──> type ratio and weights (L02), text tiers (L01)
                                    └─> DC-L15-06 Scheme strategy ──> accent count, ramps (L01)
Audience and task frequency ────────> DC-L15-04 Density voice ──> DC-L15-09 Signifier strength (denser needs stronger)
DC-L15-01 + DC-L15-04 ──────────────> DC-L15-05 Grouping strategy ──> cards, dividers, surface steps (L01, L04)
Surface type (app vs marketing) ────> DC-L15-07 Grid model, DC-L15-08 Balance, DC-L15-03 Emphasis budget
DC-L15-02 + DC-L15-03 ──────────────> per-screen lint thresholds (DC-L15-11 feedback mode)
Icon set, radius scale, font ───────> DC-L15-10 Optical policy
```

Causal notes for the builder [inferred unless tagged]:
- Raising **hierarchy strength** without lowering the **emphasis budget** makes screens louder, not clearer; the two should move together (strong hierarchy works best with one dominant element [S-L15-067]).
- Choosing a **minimal signifier** style forces **low density** and **conventional layouts** to stay usable [S-L15-004].
- Choosing **glass** forces **solid fallbacks** and **contrast overlays** [S-L15-005, S-L15-073, S-L15-078].
- Choosing **space-first grouping** requires a spacing scale with a clear inner:outer ratio (L03 DC-L03-24); otherwise the builder must fall back to containers [S-L15-012].
- Choosing **vivid or multi-accent color** raises visual complexity, which the research says costs appeal faster than simplicity does [S-L15-047].

## Community reconciliation (L00)

Checked `sources/COMMUNITY-SIGNAL.md` before finalizing.
- **Liquid Glass**: L00 confirms the iOS 26 readability backlash, the iOS 26.1 Clear/Tinted option and iOS 27's transparency slider (released around 14 Sep 2026), plus a new complaint that iOS 27 toned glass down too much. This lane's NN/g critique [S-L15-007] is iOS 26-era and is labeled as such. The Apple HIG materials change log still shows 9 Sep 2025 as the latest update [S-L15-073], so the HIG may lag the shipped OS; L10 should re-check.
- **Material 3 Expressive**: L00 says no stable Compose release ships the full Expressive API; this lane treats Expressive as "still settling" in the styles table.
- **Style mixing** ("Expressive Glass" libraries) is read by the community as AI-generated promotion (L00 section d); not used here.
- **No community signal found** (in L00's Reddit/HN/YouTube pulse) on 60-30-10, golden ratio, bento or neo-brutalism; this lane's verdicts on those rest on the Tier A/B sources cited, and on absence of evidence for 60-30-10 [S-L15-048].
- **Disagreement flagged**: Figma lists neumorphism as a 2026 web trend [S-L15-050]; IxDF treats it as a past "stylistic experiment" [S-L15-060]. The lane sides with IxDF for app UI because of the contrast problem, and notes that Figma's page is vendor editorial with unverified brand attributions.

## Cross-lane notes

- **L01**: P41 (Schloss and Palmer 2011: hue similarity raises harmony; figure colors benefit from hue contrast against the background) supports L01's default of low-chroma analogous surfaces with one contrasting accent [S-L15-017]. The 60-30-10 rule should not appear in L01 as a rule [S-L15-048].
- **L02**: DC-L15-02 uses L02's computed ratio ladders; The Futur's "double point size" rule (2x, or 3x-4x) is a coarse expressive option [S-L15-033]. Golden-ratio type scales should carry the "weak evidence" label [S-L15-052].
- **L03**: DC-L15-04 and DC-L15-05 are the voice layer on top of L03 DC-L03-10, -11, -24; the inner < outer spacing constraint is the single most valuable automate rule from Gestalt [S-L15-010, S-L15-012].
- **L04**: optical policy (DC-L15-10) depends on L04 DC-L04-05 (nested radii); glass presets depend on L04 DC-L04-15/16; Material keylines and Bjango's area formula belong in any icon-sizing work [S-L15-058, S-L15-059].
- **L05**: icon keylines (square 18, circle 20, rectangles 20 x 16 in 24 dp) and "don't blow up small icons" are icon-system rules [S-L15-059, S-L15-038].
- **L06**: section 1.10 styles map onto L06's lever matrix; neo-brutalism and maximalism sit at the "playful/energetic/rich" corners.
- **L13**: the aesthetic-usability effect is shared; L15 adds the reverse-direction finding (Tuch et al. 2012) and the first-impression and complexity studies [S-L15-042, S-L15-045, S-L15-047]. Prototypicality (P70) is the visual evidence for Jakob's law.
- **L16 (visual tooling)**: the critique vocabulary (section 1.11) and AIM's metric families [S-L15-080] are candidate features for the builder's feedback UI.

## Open questions / gaps

- **Refactoring UI book text** is paid; only the table of contents, one free chapter and the 2018 tips article were read. Chapter rationales marked [inferred] should be checked against the book.
- **The Futur's "Grids and Layout" course and "Visual Vocabulary Worksheet"** now redirect to the homepage; their content could not be reviewed. The 3-part "average to great designer" masterclass descriptions do not name skill 1; YouTube auto-captions were deliberately not quoted.
- **No experiment found** for NN/g's numeric hierarchy limits (3 sizes, 2 big elements, 2+2 colors) or for the "three levels of dominance" rule; they are consensus only.
- **Strength order of Gestalt cues in real UIs** (common region > proximity > similarity) comes from NN/g's applied articles, not from a UI experiment located this session.
- **Bento grid origin** rests on Tier C sources only.
- **Liquid Glass after iOS 27**: no Tier B usability evaluation of the iOS 27 changes was found; NN/g's critique predates them.
- **"Tangents" and "trapped white space"** are common studio terms with no source found.
- **Overshoot** in type design is stated from general typographic knowledge, not a source read this session.
- **Cultural variation**: Reinecke and Gajos show preferred complexity and colorfulness vary by country and demographic [S-L15-047]; the builder's default target band may need regional tuning, which this lane did not specify.
- **Perplexity was unavailable** (quota), so broad literature sweeps (e.g., newer aesthetics meta-analyses after 2014) were not run.

## Confidence

- **Confirmed from primary or peer-reviewed sources today:** Gestalt principle list and Prägnanz definition [S-L15-016]; color-pair harmony results [S-L15-017]; aesthetic-usability reverse finding [S-L15-042]; first-impression complexity and prototypicality results [S-L15-045]; complexity and colorfulness curves [S-L15-046, S-L15-047]; golden-section fragility [S-L15-052]; Apple HIG hierarchy, color and typography guidance with change-log dates [S-L15-053, S-L15-054, S-L15-055, S-L15-073]; Material 2 icon keylines [S-L15-059]; NN/g flat-UI eyetracking numbers [S-L15-004].
- **Confirmed practitioner guidance (Tier B), not experimentally tested:** NN/g numeric hierarchy limits [S-L15-001, S-L15-002]; Smashing dominance levels and visual-weight factors [S-L15-067, S-L15-068]; Refactoring UI tactics as published [S-L15-037, S-L15-038, S-L15-039]; Bjango optical formulas (geometric, not perceptual experiments) [S-L15-058]; NN/g style articles [S-L15-005, S-L15-006, S-L15-008, S-L15-009].
- **Practitioner opinion (Tier B/C):** all The Futur material [S-L15-020 to S-L15-036]; Figma trend list [S-L15-050].
- **Inferred by this lane:** the automate/guide/expose assignments, all style "durable vs fashionable" verdicts, token encodings under `$extensions.builder`, the 0.15 accent-area threshold, the 200-weight gap, WCAG SC mappings for neumorphism and bento reading order, and the causal notes in section 4.
- **Weakest claims:** bento origin, "skeuomorphism is returning" (Tier C only), and any statement about which 2026 trends will last.
