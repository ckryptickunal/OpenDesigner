# L05: Iconography, imagery, illustration, data visualization

Lane: L05. Author: orchestrator subagent L05. Started 2026-09-23.
Status: complete (25 Decision Cards). Sources: 96 trace rows (about 70 used, the rest rejected or tool failures), all in `traces/L05-trace.md`.

## Lane overview

This lane covers the "pictorial" layer of a design system: interface icons, brand marks inside the product (app icons, logos, favicons), photography, illustration and rich media (emoji, 3D, animated assets), and data visualization. Most of these blocks are **downstream** of the core foundations: they borrow their stroke from typography, their corners from the shape scale, their colors from the palette, and their mood from the brand personality. A builder should therefore ask the L05 questions after type, color and shape are set, and pre-fill answers from those choices.

**Ontology (building blocks in this lane)**
- Iconography: library source; style (outline, filled, duotone, rounded, sharp); stroke, corner and terminal metrics; construction grid (master size, live area, padding, keylines); size scale and optical sizing; state conventions; icon + label rules; icon color and rendering modes; metaphor, naming and localization; delivery format; icon tiers (UI icon, pictogram, spot icon); icon motion.
- Brand in product: app icon per platform (Apple layered Liquid Glass with six appearances, Android adaptive + themed, PWA maskable); logo component (symbol vs lockup, sizes, appearances); favicon set.
- Imagery: photography brief (types, perspective, light, color treatment, casting); aspect-ratio set; text-on-image protection; loading placeholders and fallbacks; avatars (sizes, shapes incl. AI-agent shape, presence).
- Illustration: style (line, flat, isometric/3D, character, surreal, logo-derived, abstract patterns); construction rules; tiers (hero, spot, mini, empty state, low-fi UI, ambient pattern); rich media (emoji sets, 3D assets, symbol animations, Lottie/dotLottie).
- Data visualization: scope and library; chart-type guidance by purpose; palettes (single brand color, categorical sequence, sequential, diverging, status); chart anatomy tokens; legends and tooltips; accessibility (redundant encoding, separators, text alternatives, data tables).

**Causality: what drives what (summary of the decision graph)**
- Typeface stem weight and terminals drive icon stroke weight and cap style (IBM derives icons from IBM Plex; SF Symbols' 9 weights map to SF font weights; Material matches grade and weight to text) [S-L05-017] [S-L05-010] [S-L05-003]. Icon stroke then drives pictogram and line-illustration stroke [S-L05-049].
- Corner radius family drives icon style (rounded vs sharp) [S-L05-003], avatar shape radius, and illustration shape language (Slack and Duolingo rounded geometry) [S-L05-060] [S-L05-059].
- Type scale and line height drive icon size pairing (16/20px icons with 14/16px text) [S-L05-016], which drives button, input and list-row heights (L03, L08).
- Color palette drives icon color tokens, illustration palette, photo color treatment, and the data-viz palettes, which must also satisfy 3:1 against surfaces and need separators between marks [S-L05-083] [S-L05-034].
- Brand personality drives icon style, photography brief, illustration style and how much animation or 3D is allowed [S-L05-047] [S-L05-049] [S-L05-061].
- Platform choice drives the icon library (SF Symbols vs Material Symbols), app-icon deliverables, and asset formats [S-L05-010] [S-L05-011] [S-L05-039].
- Accessibility rules bound almost every block: 3:1 for standalone icons and essential chart parts, 4.5:1 for text on images and chart labels, never color alone, text alternatives for complex images [S-L05-034] [S-L05-035] [S-L05-036] [S-L05-072].

**Questionnaire (the designer's questions, in the order a builder should ask them)**
1. Which platforms? Use native symbols there, or one cross-platform set? (DC-01)
2. Outline or filled by default? Rounded or sharp? (DC-02) — pre-fill from radius scale.
3. How heavy are icon strokes, and round or square caps? (DC-03) — pre-fill from typeface.
4. Which icon sizes, and which text size does each pair with? (DC-05) — pre-fill from type scale.
5. How does "selected" look? (DC-06) Which icons may go unlabelled? (DC-07)
6. Are icons monochrome, or layered/multicolor? (DC-08)
7. How will icons ship to engineers? (DC-10) Do we need pictograms/spot icons? (DC-11)
8. What single idea does the app icon express, and in which appearances? (DC-12) How does the logo appear in the product? (DC-13)
9. What is our photo brief? (DC-14) Which aspect ratios? (DC-15) Text on images or beside them? (DC-16)
10. What placeholder shows while images load? (DC-17) What avatar shapes and sizes? (DC-18)
11. What is our illustration style and personality, and where is illustration allowed? (DC-19, DC-20) How much animation, 3D, emoji? (DC-21)
12. Do we have charts? Which types, which library? (DC-22) Which palettes? (DC-23) How is chart chrome tokenized? (DC-24) How do we make charts accessible? (DC-25)

## Decision Cards

### Part A: Iconography

#### Reference table: icon systems at a glance (values from official docs)

| System | Grid / sizes | Stroke | Corners and terminals | Styles | Count | Source |
|---|---|---|---|---|---|---|
| Material Symbols (Google) | 24dp standard; optical sizes 20, 24, 40, 48; 20x20 live area + 2dp padding | 2dp = weight 400; variable 100-700 | 2dp exterior radius; outlined has square interiors; rounded style rounds both; sharp style 0dp; squared terminals | Outlined, Rounded, Sharp; FILL axis 0-1 | 2,500+ glyphs per font | [S-L05-001] [S-L05-002] [S-L05-003] |
| SF Symbols 8 (Apple, WWDC26) | 3 scales (small, medium, large) relative to SF cap height; point size follows text | 9 weights, ultralight to black, each matched to an SF font weight | follows SF letterforms | outline (default), fill, slash, enclosed variants | 7,000+ | [S-L05-006] [S-L05-008] [S-L05-010] |
| Fluent System Icons (Microsoft) | 12, 16, 20, 24, 28, 32, 48 | not published on the page | not published | Regular, Filled, Color | n/a | [S-L05-014] [S-L05-020] |
| IBM / Carbon | drawn on 32px grid, scaled linearly; 16px default in components, 20/24/32 allowed; 2px padding | 2px (at 32px) | 2px radius (multiples of 2), rounded exteriors + 90 degree interiors, square caps, 45/15 degree angles | single line style, derived from IBM Plex | n/a | [S-L05-016] [S-L05-017] |
| Atlassian | 16px medium (default), 12px small | 1.5px | rounded exteriors, sharp interiors, square terminals | single style | n/a | [S-L05-021] |
| Primer Octicons (GitHub) | designed at 16 and 24 (12 only when needed); library ships 12/16/24/48/96 | 1.5px at both 16 and 24 | 1px radius, round caps and joins | outline + fill where applicable | 400+ | [S-L05-022] [S-L05-024] |
| Polaris (Shopify) | `s-icon` size `small` or `base` | n/a | n/a | fixed set; custom SVG not supported | n/a | [S-L05-027] |
| Lucide | 24x24, at least 1px padding | 2px centered | 2px radius on 90 degree corners (1px for small parts), round caps and joins | outline | n/a | [S-L05-029] |
| Heroicons | Outline 24, Solid 24, Mini 20, Micro 16 | 1.5px (outline) | n/a | outline, solid | 316 (v2.1.5) | [S-L05-032] |
| Phosphor | designed at 16x16 | varies by weight | n/a | Thin, Light, Regular, Bold, Fill, Duotone | 1,248 | [S-L05-031] |
| Tabler | 24x24 | 2px default, adjustable | n/a | outline, filled | 6,220 (v3.48.0) | [S-L05-033] |

Derived ratio (stroke / canvas), useful as a builder parameter [inferred, computed from the values above]: Material and Lucide 2/24 = 8.3%; Heroicons outline and Octicons-24 1.5/24 = 6.25%; IBM 2/32 = 6.25% (so 1px at 16px); Atlassian and Octicons-16 1.5/16 = 9.4%. Lower ratios read lighter and more refined; higher ratios read bolder and survive small sizes better.

### DC-L05-01: Icon library strategy (adopt, extend, or draw your own)
- **Block path:** Foundations > Iconography > Icon library source
- **Questions the designer answers:** Will we use the platform's native symbols, an open-source set, or a custom set? Do we need icons that no library has (domain objects, brand concepts)? Is one set required across web, iOS and Android? What licence do we need?
- **Options:**
  - *Platform-native set:* SF Symbols on Apple platforms (7,000+ symbols, auto weight matching with SF, animations, localization for 20+ scripts) [S-L05-006] [S-L05-010]; Material Symbols on Android and web (variable font, 2,500+ glyphs) [S-L05-002]. Note that Apple's terms prohibit using SF Symbols, or look-alikes, in app icons, logos or trademarked use [S-L05-010].
  - *Open-source set:* Lucide (ISC licence) [S-L05-029], Heroicons (MIT, 316 icons) [S-L05-032], Phosphor (MIT, 1,248 icons, 6 weights) [S-L05-031], Tabler (6,220 icons) [S-L05-033], Fluent System Icons (MIT) [S-L05-014] [S-L05-018].
  - *Custom brand set:* IBM UI icons (drawn from IBM Plex details) [S-L05-017], Atlassian (1.5px, 16px) [S-L05-021], Octicons [S-L05-024]. Usually built by extending a template: Material ships a 24dp keyline template (Apache 2.0) [S-L05-001]; Apple lets you export a symbol template and draw a custom symbol [S-L05-010].
  - *Closed component set:* Polaris web components restrict you to the built-in set; custom SVGs and icon fonts are not supported in `s-icon` [S-L05-027].
- **Visual effect:** Native sets make the product feel "of the platform" and inherit system behaviours (weight matching, Dynamic Type, animations). Open-source sets give a neutral, contemporary look that many products share, so brand distinctiveness comes from color and type instead [inferred]. A custom set is the strongest brand signal but costs the most to maintain [inferred].
- **Depends on (upstream):** platform strategy (L10), brand personality (L06), typeface choice (L02), licence constraints.
- **Affects (downstream):** every icon-bearing component (buttons, nav, tabs, inputs, menus, alerts), icon tokens, the delivery pipeline (DC-L05-10), contribution process (L11).
- **Token encoding:** not a token; record as a system-level setting, e.g. `icon.library = "material-symbols-rounded" | "sf-symbols" | "lucide" | "custom"` [inferred].
- **Platform notes:** Cross-platform products often use SF Symbols on iOS and a matching set elsewhere; Fluent ships one set to Android (Maven), iOS/macOS (CocoaPods), Flutter and SVG [S-L05-018].
- **Accessibility constraints:** whichever library, each meaningful icon needs a text alternative [S-L05-012] and 3:1 contrast when it stands alone (WCAG 1.4.11) [S-L05-034].
- **Default + heuristic:** Default to the platform-native set on native apps and one open-source set on web. Draw custom icons only for domain concepts the library lacks, using the library's own template so stroke, radius and keylines match [inferred from S-L05-001, S-L05-010].
- **Evidence:** [S-L05-001] [S-L05-002] [S-L05-006] [S-L05-010] [S-L05-014] [S-L05-017] [S-L05-018] [S-L05-021] [S-L05-024] [S-L05-027] [S-L05-029] [S-L05-031] [S-L05-032] [S-L05-033]

### DC-L05-02: Icon style (outline, filled, duotone; rounded, sharp)
- **Block path:** Foundations > Iconography > Style
- **Questions the designer answers:** Should default icons be outlined or filled? Rounded or sharp corners? Do we need a two-tone or duotone style for marketing or empty states? Should one style mean "selected"?
- **Options:**
  - *Outlined (default in most systems):* Material says outlined symbols give "a light, clean style that works well in dense UIs" [S-L05-003]; Apple: outline "resembl[es] the appearance of text" and suits toolbars and lists [S-L05-010]; Fluent Regular is the primary wayfinding style [S-L05-014].
  - *Filled:* more visual emphasis; Apple recommends fill for iOS tab bars, swipe actions and accent-color selection [S-L05-010]; Fluent Filled "highlights selected states" [S-L05-014]; Material keeps some symbols always filled (full-body human figures, proprietary marks) [S-L05-003].
  - *Rounded vs sharp:* Material Rounded "pairs well with brands that use heavier typography, curved logos, or circular elements"; Sharp gives "a crisp style that remains legible even at smaller scales" and suits rectangular brands (0dp corners) [S-L05-003].
  - *Duotone / two-tone / hierarchical:* Phosphor Duotone weight [S-L05-031]; SF Symbols Hierarchical mode (one color at several opacities) and Palette mode (one color per layer) [S-L05-010]; Fluent Color style [S-L05-020]. Legacy Material Icons remain available but lack the variable axes of Material Symbols [S-L05-003]; that legacy set also had a two-tone theme [inferred, from memory, not re-verified].
- **Visual effect:** Outline reads lighter, quieter and more modern and blends with text; filled reads bolder, is easier to spot at small sizes and on busy surfaces, and signals emphasis or selection [S-L05-003] [S-L05-010]. Rounded reads friendly and soft; sharp reads precise, technical or editorial [S-L05-003]. Duotone reads illustrative and is best for larger sizes [inferred].
- **Depends on (upstream):** corner radius scale (L04 shape), typeface weight and terminals (L02), brand personality (L06).
- **Affects (downstream):** selected-state convention (DC-L05-06), nav bar/tab bar components, icon buttons, empty states.
- **Token encoding:** `icon.style.default = outlined`, `icon.style.selected = filled`; with Material Symbols, `icon.fill.rest = 0`, `icon.fill.selected = 1` as `number` tokens [inferred; axis values from S-L05-002].
- **Platform notes:** On iOS the component chooses: tab bar prefers fill, toolbar outline, so you often don't specify it [S-L05-010].
- **Accessibility constraints:** WCAG 1.4.11 3:1 non-text contrast for standalone icons [S-L05-034]; thin outline icons lose contrast faster when anti-aliased at small sizes, which favours filled or heavier styles at 12-16px [inferred].
- **Default + heuristic:** Outlined at rest, filled for selected. Match corner style to the component radius family: pill/rounded buttons pair with rounded icons, 0-2px radius UIs pair with sharp icons [S-L05-003].
- **Evidence:** [S-L05-003] [S-L05-010] [S-L05-014] [S-L05-020] [S-L05-031] [S-L05-034]

### DC-L05-03: Stroke weight, corners and terminals (matching type)
- **Block path:** Foundations > Iconography > Stroke and corner metrics
- **Questions the designer answers:** How thick are icon strokes? Round or square caps? What corner radius? Should icon weight track text weight?
- **Options:**
  - *Stroke:* 2px at 24 (Material default = weight 400 [S-L05-001]; Lucide [S-L05-029]; Tabler adjustable [S-L05-033]); 1.5px at 24 (Heroicons [S-L05-032]); 1.5px at 16 (Atlassian [S-L05-021]; Octicons at both 16 and 24 [S-L05-024]); 2px on a 32px master scaled linearly (IBM [S-L05-017]). Variable: Material wght 100-700, with a minimum of 200 at 24dp [S-L05-003]; SF Symbols 9 weights [S-L05-010].
  - *Corners:* 2dp exterior with square interiors (Material outlined) [S-L05-001]; rounded exteriors with 90 degree interiors (IBM, Atlassian) [S-L05-017] [S-L05-021]; 1px radius (Octicons) [S-L05-024]; 2px radius on 90 degree turns (Lucide) [S-L05-029].
  - *Terminals:* square caps (Material, IBM, Atlassian) [S-L05-001] [S-L05-017] [S-L05-021]; round caps and joins (Octicons, Lucide) [S-L05-024] [S-L05-029].
  - *Tie to type:* IBM draws icons from IBM Plex details (slab characteristics, distinctive tips, square caps) [S-L05-017]; SF Symbols weights correspond one-to-one to SF font weights [S-L05-010]; Material says to use "the same optical weight for your symbol and text" and to match Grade values between text font and symbols (e.g. both -25) [S-L05-003]; Apple: "match the weights of interface icons and adjacent text" [S-L05-012].
- **Visual effect:** Thin strokes (1-1.5px, weight 200-300) look elegant, airy and premium but get fragile below 20px; heavier strokes (2px+, weight 500-700) look confident and legible but can feel clunky in dense UIs [S-L05-003] [inferred]. Round caps and joins feel friendly and humanist; square caps feel precise and engineered [inferred]. Mixed stroke weights in one set "look like a mistake" (IBM) [S-L05-017].
- **Depends on (upstream):** typeface and its stem weight at body size (L02), corner radius scale (L04), density (L03).
- **Affects (downstream):** all icons, custom icon template, illustration line weight (DC-L05-19), chart line widths (DC-L05-24) [inferred].
- **Token encoding:** `icon.stroke.width` (`dimension`, e.g. `1.5px`), `icon.weight` (`fontWeight`, e.g. 400 for Material Symbols), `icon.grade` (`number`), `icon.corner.radius` (`dimension`, `2px`) [inferred].
- **Platform notes:** SF Symbols weight follows the adjacent font weight automatically when set via the text style [S-L05-010]. Material Symbols expose weight via CSS `font-variation-settings` [S-L05-002].
- **Accessibility constraints:** Material forbids weight 100 at 24dp (minimum 200) [S-L05-003]; thin strokes risk failing 3:1 non-text contrast perceptually even if the color passes [inferred].
- **Default + heuristic:** Set icon stroke so that icon weight visually equals your body text weight at the paired size: roughly 1.5px for 14-16px text with a regular-weight sans, 2px at 24px [inferred from S-L05-016, S-L05-021, S-L05-024]. Pick caps to echo the typeface: geometric or rounded sans leads to round caps, grotesk or slab leads to square caps [inferred].
- **Evidence:** [S-L05-001] [S-L05-003] [S-L05-010] [S-L05-012] [S-L05-016] [S-L05-017] [S-L05-021] [S-L05-024] [S-L05-029] [S-L05-032] [S-L05-033]

### DC-L05-04: Icon grid, keylines, live area and padding
- **Block path:** Foundations > Iconography > Construction grid
- **Questions the designer answers:** What master grid do we draw on? How much padding surrounds the drawing? What keyline shapes keep circles, squares and rectangles optically equal? Do we allow content into the padding?
- **Options:**
  - *24dp master with 20x20 live area and 2dp padding (Material):* keyline square 18dp, circle 20dp diameter, portrait rectangle 16w x 20h, landscape rectangle 20w x 16h; content may extend into padding only for extra visual weight; nothing outside the trim area; position "on pixel" [S-L05-001].
  - *32px master scaled down linearly with 2px padding (IBM):* key shapes; align points to the pixel grid; 45 degree angles for clean anti-aliasing, 15 degree increments otherwise [S-L05-017].
  - *16px master (Atlassian 16x16 bounding box [S-L05-021]; Phosphor designed at 16 [S-L05-031]).*
  - *24px with at least 1px padding and 2px minimum gaps (Lucide) [S-L05-029]; 1px gap between overlapping shapes, 1.5px around modifiers, reference circle/square/rectangle sizes (Octicons) [S-L05-024].*
- **Visual effect:** A consistent keyline system makes a circle icon and a square icon look the same size, so rows of icons feel even [S-L05-001] [S-L05-024]. Smaller live areas (more padding) make icons look smaller and airier next to text; larger live areas look heavier [inferred].
- **Depends on (upstream):** icon size scale (DC-L05-05), base spacing unit (L03: 4/8pt grids align with 16/20/24/32 masters) [inferred].
- **Affects (downstream):** custom icon template, contribution checklist (L11), icon-button padding, optical alignment of icons in components.
- **Token encoding:** usually documented, not tokenized. If needed: `icon.grid.size` (`dimension` 24px), `icon.liveArea` (20px), `icon.padding` (2px) [inferred].
- **Platform notes:** SF Symbols custom symbols use Apple's template with margins; negative side margins (named like `left-margin-Regular-M`) aid optical horizontal alignment of badged symbols [S-L05-010].
- **Accessibility constraints:** none directly; pixel alignment improves crispness at 1x, which helps low-vision users on low-DPI screens [inferred].
- **Default + heuristic:** Use the Material 24/20/2 construction unless your master size is 16 or 32. Always pixel-align at the smallest shipped size, since that is where blur shows first [S-L05-001] [S-L05-017].
- **Evidence:** [S-L05-001] [S-L05-010] [S-L05-017] [S-L05-021] [S-L05-024] [S-L05-029] [S-L05-031]

### DC-L05-05: Icon size scale and optical sizing
- **Block path:** Foundations > Iconography > Sizes
- **Questions the designer answers:** Which icon sizes do we ship? Which size pairs with which text size? Do we draw separate artwork per size, or scale one master? What touch target surrounds each size?
- **Options:**
  - *Material:* 24dp standard; 20dp for desktop/dense; 40 and 48dp for display/headline and large screens; opsz axis 20-48 thins strokes as the icon grows so large icons don't look heavy [S-L05-001] [S-L05-003].
  - *Carbon:* 16px default in components, 20/24/32 also; 16 and 20 are tuned to pair with 14 and 16px IBM Plex [S-L05-016].
  - *Fluent:* 12, 16, 20, 24, 28, 32, 48; 12px only for information, too small for interaction [S-L05-014] [S-L05-020].
  - *Atlassian:* 16px default, 12px sparingly (chevrons, validation, compact) [S-L05-021].
  - *Octicons:* separate drawings at 16 and 24 [S-L05-024]. *Heroicons:* separate 16, 20, 24 sets [S-L05-032].
  - *SF Symbols:* no fixed icon sizes; symbols take the point size of the text style and one of three scales (small, medium, large) relative to cap height [S-L05-010].
- **Visual effect:** Pixel-hinted per-size drawings (Octicons, Heroicons, Fluent) look crisp at every size; one master scaled linearly (IBM) is consistent but can look heavy when enlarged, which is exactly what Material's optical-size axis corrects [S-L05-003] [S-L05-017].
- **Depends on (upstream):** type scale (L02), density modes (L03), touch target rules (L03).
- **Affects (downstream):** button and input heights, icon-button hit areas, nav bars, list rows, badge placement.
- **Token encoding:** `dimension` tokens: `icon.size.xs = 12px`, `icon.size.sm = 16px`, `icon.size.md = 20px`, `icon.size.lg = 24px`, `icon.size.xl = 32px`; component tokens such as `button.icon.size = {icon.size.sm}` [inferred]. Material Symbols add `icon.opticalSize` (`number`, 20-48) [S-L05-002].
- **Platform notes:** Material target 48dp for a 24dp icon (40dp for a 20dp icon when mouse and keyboard are primary) [S-L05-003]; Carbon touch targets at least 44px [S-L05-016]; SF Symbols scale with Dynamic Type automatically when bound to a text style [S-L05-010].
- **Accessibility constraints:** Touch targets 44-48 regardless of glyph size [S-L05-003] [S-L05-016]; below 20dp complex or key-action icons need a text label [S-L05-003].
- **Default + heuristic:** Ship 16, 20, 24 (plus 12 and 32 if needed). Pair icon size to the line height of adjacent text rather than to font size: 16px icon with 14px text, 20px with 16px, 24px with 20px titles [inferred from S-L05-016].
- **Evidence:** [S-L05-001] [S-L05-002] [S-L05-003] [S-L05-010] [S-L05-014] [S-L05-016] [S-L05-017] [S-L05-020] [S-L05-021] [S-L05-024] [S-L05-032]

### DC-L05-06: Icon state conventions (selected, active, disabled, emphasis)
- **Block path:** Foundations > Iconography > States
- **Questions the designer answers:** How does an icon show that its nav item or toggle is selected? Do we swap artwork, change fill, change weight, or only change color? Do icons carry their own hover/pressed states?
- **Options:**
  - *Outline to filled swap on selection:* Material FILL axis 0 to 1, shown with bottom navigation selected/unselected [S-L05-003]; Fluent Filled for selected [S-L05-014]; Apple fill variant for accent-color selection, handled automatically in tab bars [S-L05-010] [S-L05-012].
  - *Weight or grade bump:* Material positive grade (e.g. 200) for an active state, as a finer change than weight [S-L05-002] [S-L05-003].
  - *Color only:* Carbon icons "do not have interaction states, only their backgrounds do" [S-L05-016]; Polaris `tone` and `color=subdued` [S-L05-027].
  - *Animated change:* SF Symbols Replace / Magic Replace between related symbols (e.g. a slash drawing on) [S-L05-010].
- **Visual effect:** Fill swaps give a strong, glanceable selected state and make the active tab pop even in grayscale; color-only changes are subtler and depend entirely on color perception [inferred; see WCAG 1.4.1 in S-L05-035]. Animated replacement adds continuity and personality [S-L05-010].
- **Depends on (upstream):** icon style (DC-L05-02), whether the library offers filled pairs or a FILL axis (DC-L05-01), color roles (L01).
- **Affects (downstream):** navigation bar, tab bar, segmented control, toggle icon buttons, favorites/bookmark toggles.
- **Token encoding:** `icon.fill.selected = 1` (`number`), `icon.grade.emphasis = 200` (`number`), `color.icon.selected`, `color.icon.default`, `color.icon.disabled` (`color`) [inferred; axis ranges from S-L05-002].
- **Platform notes:** On iOS you usually do not ship selected artwork; the system updates standard components [S-L05-012]. On web, a FILL-axis variable font animates the swap with CSS transitions [inferred from S-L05-002].
- **Accessibility constraints:** Selected state must not rely on color alone (WCAG 1.4.1) [S-L05-035]; the selection indicator is a graphical object needing 3:1 contrast (WCAG 1.4.11) [S-L05-034]. Disabled icons are exempt from 1.4.11 [S-L05-034].
- **Default + heuristic:** Outline at rest, filled plus accent color when selected (two cues, so it survives color-blindness). Keep hover/pressed feedback on the container, not the glyph, as Carbon does [S-L05-016].
- **Evidence:** [S-L05-002] [S-L05-003] [S-L05-010] [S-L05-012] [S-L05-014] [S-L05-016] [S-L05-027] [S-L05-034] [S-L05-035]

### DC-L05-07: Icon and label pairing (when icons need text, alignment, spacing)
- **Block path:** Foundations > Iconography > Icon with text
- **Questions the designer answers:** Which icons may appear without a visible label? How is an icon aligned to adjacent text (center or baseline)? What gap separates icon and label? Does icon color follow text color?
- **Options:**
  - *Labels by default:* Material: navigation items must have labels; below 20dp, complex or key-action icons need a label [S-L05-003]; Atlassian "use text labels to support icons wherever possible" [S-L05-021]; Polaris "pair icons with text labels whenever possible" [S-L05-027]; NN/g: only a handful of icons (home, print, search magnifier) are near-universal and labels should be visible, not hover-only [S-L05-037].
  - *Icon-only allowed for universal, space-constrained actions*, with an accessible name (tooltip + aria-label) [S-L05-012] [S-L05-027].
  - *Vertical alignment:* Carbon center-aligns icons with text and says not to baseline-align [S-L05-016]; Material shifts the symbol baseline down by about 11.5% of the text size [S-L05-003]; SF Symbols align to text automatically via their scales relative to cap height [S-L05-010].
  - *Color and size coupling:* Carbon: match icon color to text color; don't alter the icon-to-text size ratio [S-L05-016]; Material: same size and same optical weight as text [S-L05-003].
- **Visual effect:** Labelled icons read calmer and more explicit; icon-only toolbars read denser and more expert but raise ambiguity [S-L05-037] [inferred]. Correct optical alignment is invisible when right and looks "off by a pixel" when wrong [S-L05-012].
- **Depends on (upstream):** size scale (DC-L05-05), type scale and line heights (L02), spacing scale (L03).
- **Affects (downstream):** buttons with icons, nav items, menu items, chips, list items, tooltips on icon buttons.
- **Token encoding:** `space.icon.gap` (`dimension`, e.g. 4px at 16px icons, 8px at 24px) and component tokens like `button.icon.gap` [inferred]; `color.icon.default` aliased to `color.text.default` where the system couples them [inferred from S-L05-016, S-L05-021].
- **Platform notes:** Apple's HIG gives a table of standard SF Symbols for common actions (e.g. `trash` Delete, `xmark` Cancel/Close, `checkmark` Done) that can go unlabelled in toolbars [S-L05-012].
- **Accessibility constraints:** Icon-only controls need an accessible name [S-L05-012]; if a visible label conveys the same meaning, the icon itself is exempt from 3:1 contrast [S-L05-034].
- **Default + heuristic:** Label everything in navigation. Allow icon-only for about a dozen universal actions (search, close, more, add, delete, edit, share, settings) with a tooltip and accessible name. Center-align icons to the text line box [S-L05-016] [S-L05-037] [inferred list].
- **Evidence:** [S-L05-003] [S-L05-010] [S-L05-012] [S-L05-016] [S-L05-021] [S-L05-027] [S-L05-034] [S-L05-037]

### DC-L05-08: Icon color and rendering mode
- **Block path:** Foundations > Iconography > Color
- **Questions the designer answers:** Are icons single-color or multi-color? Do icons use their own color tokens or inherit text color? When do icons take semantic colors (success, warning, critical)? What contrast must they meet?
- **Options:**
  - *Monochrome, inherit or match text color:* Carbon: always solid monochrome, 4.5:1 contrast like typography, match text color [S-L05-016]; Fluent: only solid colors on system icons [S-L05-014]; Atlassian: color via icon tokens or text tokens [S-L05-021].
  - *Semantic tone:* Polaris `tone` info/success/warning/critical/caution/neutral [S-L05-027].
  - *Layered color:* SF Symbols Hierarchical (one color, several opacities), Palette (one color per layer), Multicolor (intrinsic meaning colors, e.g. green leaf, red trash.slash), plus optional gradient rendering from SF Symbols 7 [S-L05-006] [S-L05-010]; Fluent Color style [S-L05-020]; Phosphor Duotone [S-L05-031].
- **Visual effect:** Monochrome icons recede and let content lead; hierarchical and palette modes add depth and brand color without extra artwork; multicolor draws the eye and should be reserved for meaning (status, category) [S-L05-010] [inferred].
- **Depends on (upstream):** color roles and neutrals (L01), dark mode strategy (L01), icon style (DC-L05-02).
- **Affects (downstream):** alerts/banners, status badges, nav, empty states, file-type icons.
- **Token encoding:** semantic `color` tokens `color.icon.default`, `color.icon.subtle`, `color.icon.inverse`, `color.icon.brand`, `color.icon.success|warning|danger|info`, `color.icon.disabled`; component tokens `banner.icon.color` [inferred naming; Atlassian confirms icon-specific tokens exist, S-L05-021].
- **Platform notes:** Using system colors lets SF Symbols adapt to Dark Mode, vibrancy and accessibility settings automatically [S-L05-010]. Material recommends grade -25 for light icons on dark backgrounds to offset visual bleed [S-L05-003].
- **Accessibility constraints:** WCAG requires 3:1 for standalone meaningful icons (1.4.11) [S-L05-034]; Carbon chooses the stricter 4.5:1 [S-L05-016]. Status must not be color-only (1.4.1) [S-L05-035], so status icons need distinct shapes, not just distinct colors [inferred].
- **Default + heuristic:** One neutral icon color aliased to the secondary text color, semantic colors only on status icons, and no decorative multicolor in UI chrome. Test icons at the 3:1 floor, 4.5:1 if they sit on the same line as body text [S-L05-016] [S-L05-034].
- **Evidence:** [S-L05-003] [S-L05-006] [S-L05-010] [S-L05-014] [S-L05-016] [S-L05-020] [S-L05-021] [S-L05-027] [S-L05-031] [S-L05-034] [S-L05-035]

### DC-L05-09: Icon metaphors, naming and localization
- **Block path:** Foundations > Iconography > Metaphor, naming, localization
- **Questions the designer answers:** Do we name icons by what they depict or by what they do? How do we pick a metaphor? Which icons flip in right-to-left languages? Which metaphors change by market?
- **Options:**
  - *Name by shape (literal):* Fluent: icons "are named for the shape or object they represent, not the functionality they provide", e.g. "Shield, not security" [S-L05-014]; SF Symbols names describe drawings (`document.on.clipboard`, `arrow.uturn.backward`) [S-L05-012].
  - *Name by function (semantic alias layer):* a second map such as `action.delete -> trash` [inferred]. Apple's standard-actions table is effectively this map [S-L05-012].
  - *RTL handling:* Fluent metadata `directionType` = `unique` (separate LTR/RTL drawings) or `mirror` [S-L05-018]; SF Symbols adapt automatically to reading direction and ship script-specific variants for 20+ scripts [S-L05-006] [S-L05-010].
  - *Market-specific metaphors:* Material: cart vs bag vs basket for checkout; owls mean wisdom in some cultures and bad omens in others [S-L05-003].
- **Visual effect:** Literal names keep the library reusable across contexts (one "shield" icon serves security, protection, insurance); function names make product code readable but multiply duplicates [S-L05-014] [inferred].
- **Depends on (upstream):** content strategy and locales (L06), library source (DC-L05-01).
- **Affects (downstream):** icon search in Figma and code, component APIs (`icon="trash"`), localization QA.
- **Token encoding:** not a style token; an asset manifest (JSON) with `name`, `aliases`, `directionType`, `categories` [inferred from S-L05-018 metadata].
- **Platform notes:** SF Symbols 8 adds semantic "Enhanced Search", so designers can find symbols by describing them [S-L05-006] [S-L05-009].
- **Accessibility constraints:** Apple: prefer gender-neutral figures and culturally recognizable images; localize characters in icons [S-L05-012]. NN/g "5-second rule": if a good icon for a concept takes more than 5 seconds to think of, use a word instead [S-L05-037].
- **Default + heuristic:** Name assets by shape, expose a function-alias layer in the component API, record RTL behavior per icon, and test metaphors in each launch market [S-L05-003] [S-L05-014] [S-L05-018].
- **Evidence:** [S-L05-003] [S-L05-006] [S-L05-010] [S-L05-012] [S-L05-014] [S-L05-018] [S-L05-037]

### DC-L05-10: Icon delivery and encoding (how icons ship)
- **Block path:** Foundations > Iconography > Delivery; Tokens > Assets
- **Questions the designer answers:** Do engineers get icons as SVG files, a sprite, React/Vue components, an icon font, a variable font, or native symbols? How are files named? Do size and color come from tokens?
- **Options:**
  - *Inline SVG or per-icon components:* GitHub moved Octicons from an icon font to inline SVG because the font rendered blurry (sub-pixel anti-aliasing), flashed while loading, showed empty boxes for users who override fonts, and could only serve one glyph size [S-L05-038]; Octicons now ship npm `@primer/octicons` + React [S-L05-022]; Heroicons React/Vue [S-L05-032]; Phosphor React/Vue/Flutter/web [S-L05-031].
  - *Variable icon font:* Material Symbols (one font per style with FILL, wght, GRAD, opsz axes) plus SVG and PNG downloads [S-L05-002].
  - *Webfont option alongside SVG:* Tabler [S-L05-033].
  - *Native packages:* Fluent System Icons for Android (Maven), iOS/macOS (CocoaPods/Carthage), Flutter, and plain SVG [S-L05-018]; SF Symbols referenced by name, custom symbols exported from the SF Symbols app [S-L05-010].
  - *Closed component:* Polaris `s-icon type="..."` with no custom SVG [S-L05-027].
- **Visual effect:** SVG and native symbols render crisp at every size and can have per-size drawings; icon fonts can blur and can't change drawing per size, but variable fonts recover weight/fill/optical-size control [S-L05-002] [S-L05-038].
- **Depends on (upstream):** platform targets (L10), library choice (DC-L05-01), token pipeline (L07).
- **Affects (downstream):** bundle size, theming (CSS `currentColor` vs font color), Figma-to-code mapping (Code Connect in L07).
- **Token encoding:** DTCG Format 2025.10 (stable Final Community Group Report, 2025-10-28) has no icon, image or file `$type`; "File" is only listed as a future candidate [S-L05-043] [S-L05-095]. So size and color are tokens (`dimension`, `color`, `number` for axes) while the glyph itself is an asset referenced by name, e.g. `$extensions` or a separate manifest [inferred]. Naming pattern example: Fluent `ic_fluent_<name>_<size>_<style>.svg` (e.g. `ic_fluent_home_24_filled.svg`) [S-L05-020].
- **Platform notes:** iOS: vector PDF/SVG or custom SF Symbol; PNG needs @2x and @3x [S-L05-012] [S-L05-013]. Android: vector drawables [inferred]. Web: inline SVG with `fill="currentColor"` [inferred from S-L05-038].
- **Accessibility constraints:** Decorative icons hidden from assistive tech (`aria-hidden`), meaningful ones given a name; icon fonts fail for users who override fonts [S-L05-038] [S-L05-012].
- **Default + heuristic:** Ship SVG source of truth, generate per-framework components and native packages from it, name files `<name>_<size>_<style>`, and keep size and color as tokens. Use a variable icon font only if you need live weight/fill interpolation [S-L05-002] [S-L05-018] [S-L05-038].
- **Evidence:** [S-L05-002] [S-L05-010] [S-L05-012] [S-L05-013] [S-L05-018] [S-L05-020] [S-L05-022] [S-L05-027] [S-L05-031] [S-L05-032] [S-L05-033] [S-L05-038] [S-L05-043] [S-L05-095]

### DC-L05-11: Icon tiers beyond UI icons (pictograms and spot icons)
- **Block path:** Foundations > Iconography > Tiers (UI icon, pictogram, spot icon)
- **Questions the designer answers:** Do we need larger, more detailed symbols for marketing, onboarding or feature explanations? How do they relate to UI icons and to illustration?
- **Options:**
  - *Three tiers (Dropbox):* UI icons 24x24 (minimal), pictograms 64x64 (more detail, contextual), spot icons 120x120 (product benefits) [S-L05-058].
  - *UI icons + pictograms (IBM):* pictograms are a separate library; line-style illustration is "a continuation of pictogram logic" [S-L05-049].
  - *UI icons only*, with illustrations covering everything larger (Atlassian spot illustrations) [S-L05-050] [S-L05-021].
- **Visual effect:** A pictogram tier bridges the gap between austere UI icons and full illustration, so feature grids and onboarding look richer but still systematic [S-L05-049] [S-L05-058] [inferred].
- **Depends on (upstream):** UI icon style (DC-L05-02, DC-L05-03), illustration style (DC-L05-19), marketing needs (L06).
- **Affects (downstream):** feature lists, pricing pages, onboarding, empty states, help center.
- **Token encoding:** `icon.size.pictogram = 64px`, `icon.size.spot = 120px` (`dimension`) [inferred from S-L05-058].
- **Platform notes:** mostly web/marketing; in native apps SF Symbols at large scales or custom symbols fill this role [inferred].
- **Accessibility constraints:** decorative pictograms get empty alt text; informative ones need alt text [S-L05-036] [inferred].
- **Default + heuristic:** Add a pictogram tier only if you have marketing surfaces; draw it with the UI icon's stroke logic scaled up so the two feel related (IBM and Dropbox both derive icon tiers from the same typeface details) [S-L05-017] [S-L05-058].
- **Evidence:** [S-L05-017] [S-L05-021] [S-L05-036] [S-L05-049] [S-L05-050] [S-L05-058]

### Part B: Logos, app icons, favicons

### DC-L05-12: App icon system (iOS/macOS layered Liquid Glass, Android adaptive + themed, PWA)
- **Block path:** Brand in product > App icon
- **Questions the designer answers:** What single concept does the app icon express? Which platform formats and appearance variants must we produce? Who owns updates each OS cycle?
- **Options:**
  - *Apple (iOS, iPadOS, macOS, watchOS):* layered icons (background + one or more foreground layers) assembled in Icon Composer, which applies Liquid Glass specular highlights, refraction and translucency; 1024x1024 px square layout (watchOS 1088x1088, circular mask); appearances default, dark, clear light, clear dark, tinted light, tinted dark; system generates variants you don't provide; provide unmasked square layers; prefer vector (SVG/PDF) layers, PNG for raster/mesh gradients [S-L05-011]. Icon Composer 2 (beta June 2026) adds per-layer refraction strength, specular-highlight alignment and preview across OS versions [S-L05-007] [S-L05-008]. tvOS: 800x480, 2-5 parallax layers; visionOS: circular 3D, background + 1-2 layers [S-L05-011].
  - *Android adaptive icon:* foreground + background layers, each 108x108dp; 66x66dp safe zone; 18dp reserved per side for masks and motion; logo 48-66dp; optional `monochrome` layer for themed icons (Android 13, API 33+); Android 16 QPR2 auto-themes apps that lack a monochrome layer [S-L05-039].
  - *Web/PWA:* manifest icons at least 192x192 and 512x512 [S-L05-040]; maskable icons keep key content inside a circle of radius 40% of width [S-L05-041].
- **Visual effect:** Layered, simple, filled overlapping shapes pick up system lighting and look native; photos, fine lines, text and baked-in shadows look muddy under system effects and at small sizes [S-L05-011]. Dark, clear and tinted variants are progressively more subdued, so brand recognition must come from shape, not color [S-L05-011].
- **Depends on (upstream):** logo/brand mark (L06), brand color (L01), platform strategy (L10).
- **Affects (downstream):** store listings, notifications, settings, share sheets, splash screens, favicons (DC-L05-13).
- **Token encoding:** assets, not tokens; background color/gradient can reference brand color primitives (`color.brand.primary`) [inferred].
- **Platform notes:** Apple: "include text only when it's essential", "prefer illustrations to photos", don't replicate UI or Apple hardware, and keep features consistent across appearances [S-L05-011]. Android: no pre-applied masks or shadows [S-L05-039].
- **Accessibility constraints:** Logos are exempt from WCAG 1.4.11 [S-L05-034], but the icon must stay recognizable in tinted/monochrome modes users pick for comfort [S-L05-011] [S-L05-039].
- **Default + heuristic:** Design one glyph built from 1-3 filled shapes on a solid or gradient background, and export it as Apple layers, Android foreground/background/monochrome, and a maskable PWA icon. Check it in tinted/monochrome first, since that is the hardest mode [S-L05-011] [S-L05-039] [inferred order].
- **Evidence:** [S-L05-007] [S-L05-008] [S-L05-011] [S-L05-034] [S-L05-039] [S-L05-040] [S-L05-041]

### DC-L05-13: Logo in product and favicons
- **Block path:** Brand in product > Logo usage; Brand in product > Favicon
- **Questions the designer answers:** Where does the logo appear inside the product (nav, login, footer, emails)? Symbol only or lockup? Which color appearances? What favicon files do we ship?
- **Options:**
  - *Logo as a component:* Atlassian `Logo` offers Icon (symbol only) or Lockup (wordmark + icon); sizes xxsmall 16, xsmall 20, small 24, medium 32 (default), large 40, xlarge 48; appearance `brand`, `neutral` (recedes; check contrast), `inverse` (dark backgrounds); don't rely on inherited color [S-L05-044].
  - *Fixed-color product marks:* Fluent: never change the color of product launch icons; launch icons come in 48, 64, 96 and 192px [S-L05-014].
  - *Favicon minimal set (Tier B practice):* `favicon.ico` 32x32 for legacy, `icon.svg` (can carry a `prefers-color-scheme: dark` style inside the SVG), `apple-touch-icon.png` 180x180, plus manifest PNGs 192 and 512 and a 512 maskable [S-L05-042] [S-L05-040] [S-L05-041].
- **Visual effect:** A small symbol-only logo in the nav keeps chrome quiet and product-led; a full lockup reads marketing-led [inferred]. A neutral (monochrome) logo lets the product color scheme lead; brand color logos add identity but compete with primary actions [S-L05-044] [inferred].
- **Depends on (upstream):** logo system (L06), neutral and inverse surfaces (L01), app icon (DC-L05-12).
- **Affects (downstream):** top nav/app bar, sign-in screens, email templates, loading/splash screens, browser tab.
- **Token encoding:** logo sizes as `dimension` tokens mirroring the icon scale (`logo.size.md = 32px`), appearance as a component prop, not a color token [inferred from S-L05-044].
- **Platform notes:** SVG favicons are supported in modern browsers while `.ico` remains for legacy [S-L05-042].
- **Accessibility constraints:** logos are exempt from contrast minimums [S-L05-034], but a logo that acts as a link needs an accessible name [inferred].
- **Default + heuristic:** Symbol-only logo at 24-32px in the app bar, full lockup on sign-in and marketing, neutral appearance inside dense tools. Ship the favicon set from one SVG master [S-L05-042] [S-L05-044].
- **Evidence:** [S-L05-014] [S-L05-034] [S-L05-040] [S-L05-041] [S-L05-042] [S-L05-044]

### Part C: Imagery

### DC-L05-14: Photography art direction (subjects, perspective, light, color treatment, inclusion)
- **Block path:** Foundations > Imagery > Photography style
- **Questions the designer answers:** What kinds of photos do we use (people at work, portraits, products, content)? Staged or documentary? Natural or stylized light and color? How do we make casting inclusive? When do we use photos instead of illustration?
- **Options:**
  - *Documentary / reportage:* IBM's bulk photography is "lifestyle, cinematic and colorful", editorial like documentary film, "images that feel like frames from a film" [S-L05-046].
  - *Portraiture:* IBM treats every subject with equal photographic stature ("democratic") [S-L05-046]; Dropbox "People" category [S-L05-057].
  - *Still life / product / content:* IBM still-life for hardware, software and concepts [S-L05-046]; Dropbox "Content" (artwork, fabric, sketches) and "Teams" categories [S-L05-057].
  - *Perspective and composition rules:* IBM uses eye level (authentic, "eye-to-eye") or aerial, with clear focal points placed on its 2x Grid [S-L05-047].
  - *Light and color treatment:* IBM: natural light, no "golden hour" warmth, no color washes or grading, everything in sharp focus, no overlays or filters [S-L05-047]. The opposite pole (graded, duotone, brand-tinted, shallow depth of field) is a legitimate choice for lifestyle or fashion brands [inferred].
  - *Role split with illustration:* Dropbox uses photography for real-world proof and customer stories, illustration for abstract or dry concepts [S-L05-057]; Apple prefers illustration over photos inside app icons [S-L05-011].
- **Visual effect:** Natural light, deep focus and ungraded color read factual, trustworthy and enterprise-grade (IBM's stated intent: "we're a fact-based company") [S-L05-047]. Graded color, shallow focus and warm light read emotional, aspirational and consumer [inferred]. Eye-level framing reads respectful and human; unusual angles read dramatic [S-L05-047].
- **Depends on (upstream):** brand personality and voice (L06), brand color palette (L01), grid (L03; IBM ties framing to its 2x Grid) [S-L05-047].
- **Affects (downstream):** marketing heroes, onboarding, cards with media, empty states, image overlays (DC-L05-16), avatars (DC-L05-18).
- **Token encoding:** mostly guidance, not tokens. If a color treatment is used, encode it as tokens: `image.overlay.color`, `image.overlay.opacity` (`color`, `number`) [inferred].
- **Platform notes:** Photos ship as JPEG or HEIC on Apple platforms, with a color profile embedded [S-L05-013].
- **Accessibility constraints:** photographs are exempt from WCAG 1.4.11 [S-L05-034], but informative photos need alt text [S-L05-036]. Inclusion: IBM names gender, cultural and geographic diversity as a principle for imagery [S-L05-049]; Apple asks for inclusive, gender-neutral depictions [S-L05-012].
- **Default + heuristic:** Write a one-paragraph photo brief (subject types, perspective, light, color treatment, casting) before commissioning or buying stock. IBM's test is useful for any brand: if an image "could have been created by any other organization", reject it [S-L05-047].
- **Evidence:** [S-L05-011] [S-L05-012] [S-L05-013] [S-L05-034] [S-L05-036] [S-L05-046] [S-L05-047] [S-L05-049] [S-L05-057]

### DC-L05-15: Aspect ratios and cropping
- **Block path:** Foundations > Imagery > Aspect ratios
- **Questions the designer answers:** Which aspect ratios are allowed for media in cards, heroes and galleries? How do crops adapt across breakpoints? Where is the focal point?
- **Options:**
  - *A small fixed ratio set:* IBM crops to 16:9, 4:3, 3:2, 2:1 or 1:1, chosen because they align with its 2x Grid and create rhythm "from UI components to signage" [S-L05-047].
  - *Ratio per component:* e.g. 16:9 hero, 4:3 or 3:2 card media, 1:1 avatar and thumbnails [inferred].
  - *Art-directed crops per breakpoint* (different crop for mobile portrait vs desktop landscape) [inferred].
- **Visual effect:** A small ratio set gives galleries and card grids a calm, aligned rhythm; wide ratios (16:9, 2:1) feel cinematic, square feels social and product-focused, portrait feels editorial and mobile-native [S-L05-047] [inferred].
- **Depends on (upstream):** grid and breakpoints (L03), photography style (DC-L05-14).
- **Affects (downstream):** card, media, carousel, hero, avatar, image placeholder (DC-L05-17).
- **Token encoding:** DTCG 2025.10 has no ratio or asset type [S-L05-095]. Encode as `number` (`aspect.video = 1.7778`) or a string in `$extensions` (`"16 / 9"`) that maps to CSS `aspect-ratio` [inferred]; flag to L07.
- **Platform notes:** Web: set `width`/`height` attributes or CSS `aspect-ratio` so the browser reserves space before load [S-L05-068]. Apple bitmap assets need @2x/@3x (iOS) or @1x/@2x (macOS) [S-L05-013].
- **Accessibility constraints:** cropping must not remove the information an alt text describes [inferred].
- **Default + heuristic:** Allow 3-5 ratios (16:9, 3:2, 4:3, 1:1, and optionally 2:1) and assign one per component slot [S-L05-047] [inferred].
- **Evidence:** [S-L05-013] [S-L05-095] [S-L05-047] [S-L05-068]

### DC-L05-16: Text and UI on images (overlays, scrims, protection)
- **Block path:** Foundations > Imagery > Text on images
- **Questions the designer answers:** Will we place text or buttons over photos? If so, how do we guarantee contrast: a gradient scrim, a solid panel, a blur material, or text beside the image? Do we tint images with brand color?
- **Options:**
  - *Avoid text on images:* place text next to the media; IBM avoids color and image overlays on photos entirely [S-L05-047]; Atlassian applies the same logic to chart colors ("don't place text on chart colors") [S-L05-083].
  - *Gradient scrim* under the text region [inferred; common practice, no official page found in this session].
  - *Solid or translucent panel* behind the text [inferred].
  - *Blur / system material* behind text (platform materials, see L04) [inferred].
- **Visual effect:** Text beside images reads clean and editorial and keeps photos honest; scrims read cinematic but darken the image; brand-tinted overlays read bold and campaign-like and flatten photo variety into one mood [S-L05-047] [inferred].
- **Depends on (upstream):** photography style (DC-L05-14), color tokens for overlays (L01), materials/elevation (L04).
- **Affects (downstream):** hero banners, media cards, carousels, video players, story/feature tiles.
- **Token encoding:** `color.overlay.scrim` (`color` with alpha), `gradient.scrim.bottom` (`gradient`), `text.onImage.color` [inferred].
- **Platform notes:** none verified in this session.
- **Accessibility constraints:** text over images still needs 4.5:1 (3:1 for large text: 18pt, or 14pt bold) [S-L05-072]. Because image content varies, contrast has to hold at the lightest (or darkest) region behind the text, which is why a scrim or panel is usually needed [inferred].
- **Default + heuristic:** Default to text beside images. When overlay is required (heroes), use a scrim token and test contrast against the worst-case region [S-L05-072] [inferred].
- **Evidence:** [S-L05-047] [S-L05-072] [S-L05-083]

### DC-L05-17: Image loading, placeholders and fallbacks
- **Block path:** Foundations > Imagery > Loading and placeholders
- **Questions the designer answers:** What shows while an image loads: empty reserved space, a skeleton block, a dominant-color fill, or a blurred preview? What shows if the image fails?
- **Options:**
  - *Reserved empty space:* Carbon: a 600x600 image can be shown as 600x600 white space until it loads; images come in a later batch after page structure [S-L05-071].
  - *Skeleton:* Carbon uses skeletons only on container and data components (tiles, lists, tables, cards) and never on toasts, menus, modals or loaders [S-L05-071].
  - *Dominant color or blurred low-res preview* [inferred; not documented in sources read].
  - *Fallback image:* Atlassian Avatar shows a default image when no source is available [S-L05-066].
- **Visual effect:** Reserved space and skeletons keep layout still and feel fast; blurred previews feel richer and photo-forward; sudden pop-in with layout shift feels broken [S-L05-068] [S-L05-071] [inferred].
- **Depends on (upstream):** aspect ratios (DC-L05-15), neutral surface colors (L01), motion (L04, skeleton shimmer).
- **Affects (downstream):** cards, galleries, avatars, product tiles, feeds.
- **Token encoding:** `color.skeleton` / `color.background.placeholder` (`color`), `duration.skeleton.pulse` (`duration`) [inferred].
- **Platform notes:** Web: reserve space with width/height or `aspect-ratio`; CLS must stay at or below 0.1 for 75% of visits [S-L05-068].
- **Accessibility constraints:** a screen reader should be told when content is loading or fails [S-L05-071].
- **Default + heuristic:** Always reserve the final box; use a neutral placeholder fill for images and skeletons only for container components [S-L05-068] [S-L05-071].
- **Evidence:** [S-L05-066] [S-L05-068] [S-L05-071]

### DC-L05-18: Avatars (sizes, shapes, fallbacks, presence)
- **Block path:** Components > Avatar (imagery-driven component)
- **Questions the designer answers:** Which avatar sizes do we support? What shape means a person, a team or org, and an AI agent? What is the fallback when there is no photo? How is presence shown?
- **Options:**
  - *Size scale:* Primer 16, 20 (default), 24, 28, 32, 40, 48, 64 ("base-4 until 32 ... base-8 up to 48") [S-L05-069]; Atlassian xxsmall (16px) through xxlarge [S-L05-066].
  - *Shape semantics:* circle = person, square = team/org/project (Primer, Fluent, Atlassian) [S-L05-066] [S-L05-067] [S-L05-069]; AI agents as square (Primer: "bots, AI agents, teams, or organizations") [S-L05-069] or as a distinct hexagon (Atlassian, e.g. Rovo Dev) [S-L05-066].
  - *Presence and status:* Atlassian presence (online, offline, busy, focus) and status (approved, declined, locked, warning; status wins) [S-L05-066]; Fluent presence badges and activity rings [S-L05-067].
  - *Fallback:* default image (Atlassian) [S-L05-066]; initials on a generated color [inferred; not in sources read].
- **Visual effect:** Circular avatars read personal and social; square avatars read institutional; a distinct agent shape makes AI actors instantly recognizable in mixed human-AI lists [S-L05-066] [inferred].
- **Depends on (upstream):** radius scale (L04), icon/size scale (DC-L05-05), photography style (DC-L05-14).
- **Affects (downstream):** avatar group, comments, mentions, user menu, assignee fields, chat.
- **Token encoding:** `avatar.size.16 ... avatar.size.64` (`dimension`), `avatar.radius.person = 9999px`, `avatar.radius.entity = {radius.sm}` [inferred naming; values from S-L05-069].
- **Platform notes:** none specific beyond component libraries.
- **Accessibility constraints:** Fluent notes presence badges on 32px and smaller avatars are hard to perceive, so add text or tooltip [S-L05-067]; Primer: provide alt text when no name sits beside the avatar [S-L05-069]; Atlassian: drop the name on decorative avatars [S-L05-066].
- **Default + heuristic:** 16-64 scale on a 4/8 rhythm; circle = person, square = entity, a third shape for AI agents if the product mixes human and AI actors [S-L05-066] [S-L05-069].
- **Evidence:** [S-L05-066] [S-L05-067] [S-L05-069]

### Part D: Illustration and rich media

### DC-L05-19: Illustration style and brand personality
- **Block path:** Foundations > Illustration > Style
- **Questions the designer answers:** What does our illustration look like: line, flat, isometric/3D, character-based, textured, abstract? What personality should it carry? What are the construction rules so different illustrators produce one look?
- **Options (with benchmarks):**
  - *Line style:* IBM, "precision, honesty and authority"; built on a 4px grid for every canvas, no more than 4 line weights, spacing at least equal to line weight, angles in 15 degree steps, circular curves, opaque strokes, gradients that follow the stroke [S-L05-048] [S-L05-049].
  - *Flat style:* IBM, "colorful, bold, graphic statements" [S-L05-049].
  - *Isometric / dimensional:* IBM isometric adds depth to explain complex processes [S-L05-049]; Airbnb's May 2025 redesign moved to clay-like, animated 3D icons (Tier C reports; Bloomberg headline corroborates the flat-to-3D shift) [S-L05-063] [S-L05-064].
  - *Character-based and rounded:* Duolingo moved in 2018 from "flat, pointy shapes and muted colors" to "brighter, rounder, friendlier" illustration built from the fewest shapes [S-L05-059]. (A widely repeated rule, "three basic shapes: rounded rectangle, circle, rounded triangle", comes from Duolingo's retired guideline site and could not be verified live [S-L05-055].)
  - *Expressive / surreal:* Mailchimp's 2018 Collins identity favours personal expression over realism, "playful surrealism" [S-L05-061].
  - *Logo-derived geometry:* Slack's speech-bubble and lozenge shapes extend into icons, illustrations and patterns with rounded corners [S-L05-060].
  - *Simple metaphor scenes:* Dropbox uses "simple, charming scenes and metaphors" to explain abstract ideas and soften errors [S-L05-057].
  - *3D emoji-like assets:* Fluent Emoji ship 3D, Color, Flat and High Contrast styles per emoji [S-L05-062].
- **Visual effect:** Line reads precise, calm and technical; flat reads bold and energetic; isometric/3D reads tactile, premium or playful and draws attention; rounded characters read warm, young and forgiving; surreal/expressive reads creative and distinctive; abstract patterns add brand texture without narrative [S-L05-049] [S-L05-059] [S-L05-061] [inferred for 3D/abstract].
- **Depends on (upstream):** brand personality (L06), color palette (L01), icon stroke and corner logic (DC-L05-03; IBM calls line style "a continuation of pictogram logic") [S-L05-049], radius/shape language (L04).
- **Affects (downstream):** empty states, onboarding, error pages, marketing, spot icons, emoji/reactions, motion (animated illustrations).
- **Token encoding:** mostly guidance; the reusable parts are tokens: illustration palette as aliases of brand primitives (`illustration.color.primary = {color.brand.500}`), `illustration.stroke.width` (`dimension`), `illustration.grid = 4px` [inferred; grid value from S-L05-048].
- **Platform notes:** Apple app icons prefer illustration to photos [S-L05-011]; high-contrast variants exist in Fluent Emoji for Windows contrast themes [S-L05-062] [inferred purpose].
- **Accessibility constraints:** IBM: diversity (gender, culture, geography) is a principle [S-L05-049]; informative illustrations need alt text, decorative ones none [S-L05-036] [inferred].
- **Default + heuristic:** Derive illustration geometry from things you already have: the icon stroke, the corner radius and the brand palette. Pick one primary style and at most one secondary (IBM runs three, but for a very large brand) [S-L05-049] [inferred].
- **Evidence:** [S-L05-011] [S-L05-036] [S-L05-048] [S-L05-049] [S-L05-055] [S-L05-057] [S-L05-059] [S-L05-060] [S-L05-061] [S-L05-062] [S-L05-063] [S-L05-064]

### DC-L05-20: Illustration tiers and where they appear (hero, spot, empty state, patterns)
- **Block path:** Foundations > Illustration > Types and usage
- **Questions the designer answers:** Which illustration sizes and types exist? Which ones are allowed inside the product vs only in marketing? Does every empty state get an illustration?
- **Options:**
  - *Dropbox:* hero, spot, mini, plus "AI boxes" for AI features [S-L05-057].
  - *Atlassian (in product):* spot illustrations (one concept; empty, error, celebration; colorful for emphasis, neutral for routine), low-fidelity UI (gray basic shapes for onboarding, never real screenshots), ambient patterns (background texture); collage only on marketing pages [S-L05-050].
  - *IBM:* illustration must "have a job to do"; only essential, non-decorative elements [S-L05-049].
- **Visual effect:** Colorful spots celebrate and draw focus; neutral spots stay calm for frequent states; overusing illustration increases cognitive load and makes a tool feel childish [S-L05-050] [inferred for the last clause].
- **Depends on (upstream):** illustration style (DC-L05-19), product type (tool vs consumer, L06).
- **Affects (downstream):** empty state component, error pages, onboarding/feature tours, success/celebration moments, banners.
- **Token encoding:** size slots as `dimension` tokens, e.g. `illustration.size.spot`, `illustration.size.hero` [inferred]; empty-state component token `emptyState.image.maxWidth` [inferred].
- **Platform notes:** none verified.
- **Accessibility constraints:** illustrations support copy and never replace it [S-L05-050]; decorative ones are hidden from assistive tech [inferred].
- **Default + heuristic:** In product, use neutral spots for routine empty states and colorful spots only for first-run and celebration; keep hero and collage work in marketing [S-L05-050].
- **Evidence:** [S-L05-049] [S-L05-050] [S-L05-057]

### DC-L05-21: Emoji, stickers, 3D assets, animated icons and Lottie (summary)
- **Block path:** Foundations > Rich media > Emoji, 3D, animated assets
- **Questions the designer answers:** Do we use the OS emoji or a branded set? Do we allow 3D assets? Which icons animate, and in what format do animations ship?
- **Options:**
  - *Symbol animation built into the icon system:* SF Symbols Appear, Disappear, Bounce, Scale, Pulse, Variable Color, Replace (down-up, up-up, off-up), Magic Replace, Wiggle, Breathe, Rotate, and Draw On/Off (SF Symbols 7+) [S-L05-010]; the current SF Symbols page also lists Variable Draw for expressing progress (version of introduction not stated there) [S-L05-006]. Carbon lists an "Animated Icons Collection" among its icon resources [S-L05-016].
  - *Branded emoji sets:* Fluent Emoji with 3D, Color, Flat and High Contrast per emoji, MIT licensed [S-L05-062].
  - *3D animated UI icons:* Airbnb 2025 (reported custom "Lava" format; Tier C) [S-L05-063].
  - *Lottie / dotLottie:* dotLottie v2.0 packages multiple animations, shared assets, themes (dark mode, brand) and interactive state machines in one compressed file with native players [S-L05-090].
- **Visual effect:** Animated symbols confirm actions and show status with little space; 3D and animated illustration makes a product feel alive and playful but is heavy and can distract [S-L05-010] [S-L05-063] [inferred].
- **Depends on (upstream):** motion system and reduced-motion rules (L04), illustration style (DC-L05-19), brand tone (L06).
- **Affects (downstream):** reactions, success states, onboarding, loading indicators, nav/category icons.
- **Token encoding:** animation timing via motion tokens (`duration`, `cubicBezier`, L04); assets via manifest [inferred].
- **Platform notes:** Apple: "apply symbol animations judiciously" and "consider your app's tone" [S-L05-010].
- **Accessibility constraints:** respect reduced-motion settings (cross-lane L04) [inferred]; High Contrast emoji variants help contrast themes [S-L05-062].
- **Default + heuristic:** Animate icons only to confirm an action or show ongoing status; keep 3D and Lottie for onboarding, celebration and marketing moments [S-L05-010] [inferred].
- **Evidence:** [S-L05-006] [S-L05-010] [S-L05-016] [S-L05-062] [S-L05-063] [S-L05-090]

### Part E: Data visualization

### DC-L05-22: Data-viz scope, chart library and chart-type guidance
- **Block path:** Foundations > Data visualization > Chart types and library
- **Questions the designer answers:** Does our product need charts at all, and how many kinds? Do we adopt an existing chart library, build a thin themed wrapper, or build our own? How do designers pick a chart type?
- **Options:**
  - *Guidance by purpose:* Carbon groups chart types by the question asked: comparisons (simple/grouped/floating bar, lollipop, bubble, radar), trends (line, area, boxplot, histogram, stream), part-to-whole (donut, pie, stacked bar, bullet, stacked area, meter, gauge, treemap, circle pack), correlations (scatter, heat map, parallel coordinates), connections (alluvial, network, tree), geospatial (choropleth, proportional symbol, connection map; some "design only") [S-L05-078]. IBM: "choose the visual model that best conveys the message" and keep proportions true to the numbers [S-L05-093] [S-L05-094].
  - *Rules that change how charts look:* bars and areas start at zero; lines and scatter may crop the axis; never interpolate gaps; axis breaks drawn as a sinusoidal line 16px wide; keep tick increments constant [S-L05-076].
  - *Library strategy:* an open system library (Carbon Charts; Carbon notes its guidance is "a work in progress" tracked in carbon-charts) [S-L05-075]; a general grammar library such as Observable Plot [S-L05-088]; third-party (Atlassian points to Highcharts for accessible examples) [S-L05-083]; in-house. Shopify deprecated its public Polaris Viz package and archived the repo on 2026-07-29 "due to the lack of external use and cost to support", moving to an internal-only library [S-L05-080].
- **Visual effect:** Fewer chart types make dashboards look consistent and learnable; exotic types (radar, stream, alluvial) look impressive but need more reading [inferred]. Zero-based bars look honest; cropped bars exaggerate differences [S-L05-076].
- **Depends on (upstream):** product type (analytics-heavy vs occasional charts), data-viz color (DC-L05-23), typography (L02), platform (L10).
- **Affects (downstream):** dashboards, KPI tiles, reports, empty/loading states for charts, export features.
- **Token encoding:** not a token; a system decision recorded in the builder, with chart components consuming the tokens in DC-L05-23 and DC-L05-24 [inferred].
- **Platform notes:** web-first in most systems; native apps use platform chart frameworks themed with the same tokens [inferred].
- **Accessibility constraints:** see DC-L05-25.
- **Default + heuristic:** Start with 5-6 chart types (bar, line, area, stacked bar, donut or meter, scatter) plus a KPI "big number". Theme an existing library rather than building one; Polaris Viz shows the maintenance cost of a public chart library [S-L05-077] [S-L05-080] [inferred list].
- **Evidence:** [S-L05-075] [S-L05-076] [S-L05-077] [S-L05-078] [S-L05-080] [S-L05-083] [S-L05-088] [S-L05-093] [S-L05-094]

### DC-L05-23: Data-viz color palettes (categorical, sequential, diverging, status)
- **Block path:** Foundations > Color > Data visualization palettes (shared with L01)
- **Questions the designer answers:** What is the default color for a one-series chart? How many categorical colors, in what order? Do we need sequential and diverging ramps? Are status colors allowed in charts? How do palettes switch in dark mode?
- **Options:**
  - *Carbon (IBM):* 14-color categorical sequence applied strictly in order to maximize contrast between neighbours: Purple 70 #6929c4, Cyan 50 #1192e8, Teal 70 #005d5d, Magenta 70 #9f1853, Red 50 #fa4d56, Red 90 #570408, Green 60 #198038, Blue 80 #002d9c, Magenta 50 #ee538b, Yellow 50 #b28600, Teal 50 #009d9a, Cyan 90 #012749, Orange 70 #8a3800, Purple 50 #a56eff (light theme); fixed small-group overrides when the count is known; monochromatic sequential ramps 10-100 (darkest = largest in light theme, lightest = largest in dark theme); diverging red-cyan for temperature and purple-teal for non-temperature data (same in both themes); alert palette Red 60 #da1e28, Orange 40 #ff832b, Yellow 30 #f1c21b, Green 60 #198038; gradients discouraged and never a substitute for sequential [S-L05-075].
  - *Atlassian:* `color.chart.brand` as the single-series default, `color.chart.neutral` for de-emphasized data; `color.chart.categorical.1`-`.8` in numbered order, limit charts to 5-6 colors by grouping; status tokens `color.chart.success|warning|danger|information|discovery` each with `.bold`; custom chart tokens in every hue with three emphasis levels; hovered tokens; light and dark values per token; sequential and divergent palettes "not currently supported" [S-L05-083].
  - *Practitioner rules:* 3-10 categorical colors for small orgs; sequential/diverging ramps should span a wide lightness range (about 69 points) and shift hue as they darken; avoid red-green; "grey is the most important color" [S-L05-086]. IBM: shades of grey for context, color only where it has a reason [S-L05-094].
  - *Library defaults:* Observable Plot categorical `observable10`, quantitative `turbo`, diverging `rdbu`, threshold/quantile `rdylbu`; ColorBrewer, viridis and cividis available [S-L05-088].
- **Visual effect:** Single-color charts with grey context read calm, branded and focused; many-hued categorical charts read busy and need a legend; sequential ramps read as "more vs less", diverging as "above vs below a midpoint"; warm-to-cool diverging implies temperature, so Carbon reserves red-cyan for temperature [S-L05-075] [S-L05-083] [S-L05-086].
- **Depends on (upstream):** core color palette and ramps (L01), dark mode strategy (L01), surface/elevation colors (L04).
- **Affects (downstream):** all chart components, legends, KPI tiles, heat maps, maps, status charts.
- **Token encoding:** `color` tokens: primitives from the core ramps, semantic `color.chart.categorical.1..n`, `color.chart.sequential.<hue>.<step>`, `color.chart.diverging.<pair>.<step>`, `color.chart.status.*`, `color.chart.brand`, `color.chart.neutral`, `color.chart.*.hovered`; each with light/dark mode values [S-L05-083] [inferred naming beyond Atlassian's].
- **Platform notes:** the same tokens must reach web chart libraries and native chart frameworks; Carbon flips sequential lightness direction by theme [S-L05-075].
- **Accessibility constraints:** chart marks need 3:1 against the surface (WCAG 1.4.11) [S-L05-034]; Atlassian's chart colors pass 3:1 on its surfaces but not against each other, so adjacent marks need a gap or separator [S-L05-083]; color cannot be the only cue (WCAG 1.4.1) [S-L05-035]; test with color-vision-deficiency simulators [S-L05-086].
- **Default + heuristic:** One brand chart color plus grey by default; a 6-8 step categorical sequence used in fixed order; add one sequential ramp per primary hue and one diverging pair only if the product shows above/below-target data [S-L05-075] [S-L05-083] [S-L05-086].
- **Evidence:** [S-L05-034] [S-L05-035] [S-L05-075] [S-L05-083] [S-L05-086] [S-L05-088] [S-L05-094]

### DC-L05-24: Chart anatomy and chart tokens (axes, gridlines, labels, legends, tooltips)
- **Block path:** Foundations > Data visualization > Chart anatomy
- **Questions the designer answers:** Which parts does every chart have? Which existing tokens style axes, gridlines, labels and reference lines? Where do legends go and how do they behave? What does a tooltip show?
- **Options:**
  - *Carbon anatomy:* rectangular charts = chart title, axes, ticks, axis title, legend, toolbar, zoom bar, graph frame, tooltip; circular charts = title, label, tooltip, legend, graph frame, big number (KPI); title states the main insight; tooltips repeat the values on both axes; slice labels use a callout under 3 degrees [S-L05-077].
  - *Atlassian token mapping:* title `color.text`, tick label `color.text.subtle`, legend `color.text`, gridline `color.border`, threshold/reference line `color.chart.neutral`, marks `color.chart.brand`; chart tokens for marks, border and text tokens for chart chrome [S-L05-083].
  - *Legend rules (Carbon):* prefer direct labels; no legend for a single category; default at bottom (top, left or right allowed); at most 2 lines then "View more"; never taller than 30% of the chart; hover dims other series to 30% opacity; click isolates a series [S-L05-091].
  - *Axis details (Carbon):* 16px axis break, 0.5px stroke inside breaks, semibold "landmark" labels when time crosses into a new day, month or year, localized date formats [S-L05-076].
- **Visual effect:** Reusing text and border tokens for chart chrome makes charts look like part of the UI rather than pasted-in images; light gridlines and subtle tick labels push attention to the data; direct labels read editorial and cleaner than legends [S-L05-083] [S-L05-091] [S-L05-094].
- **Depends on (upstream):** text and border color tokens (L01), type scale (L02), spacing (L03), data-viz palettes (DC-L05-23).
- **Affects (downstream):** every chart component, dashboards, KPI tiles, tooltips (L08 tooltip component).
- **Token encoding:** component-tier aliases: `chart.title.color = {color.text}`, `chart.tick.label.color = {color.text.subtle}`, `chart.gridline.color = {color.border}`, `chart.reference.color = {color.chart.neutral}`, `chart.legend.maxHeight = 30%` (store as `number` 0.3), `chart.series.dimmed.opacity = 0.3` (`number`), `chart.axis.break.width = 16px` (`dimension`), `chart.label.landmark.fontWeight = 600` (`fontWeight`) [S-L05-076] [S-L05-083] [S-L05-091]; token names [inferred].
- **Platform notes:** on mobile, Carbon allows a hidden legend behind a "View legends" button, though hiding legends is otherwise discouraged [S-L05-091].
- **Accessibility constraints:** tick labels and legends are text and need 4.5:1 [S-L05-072]; gridlines are usually supportive, not essential, so 1.4.11 applies only if the chart can't be read without them [S-L05-034] [inferred application].
- **Default + heuristic:** Map chart chrome to existing text/border tokens and add chart-specific tokens only for marks and interaction states [S-L05-083].
- **Evidence:** [S-L05-034] [S-L05-072] [S-L05-076] [S-L05-077] [S-L05-083] [S-L05-091] [S-L05-094]

### DC-L05-25: Chart accessibility (not color alone, text alternatives, data tables)
- **Block path:** Foundations > Data visualization > Accessibility
- **Questions the designer answers:** How does someone who can't distinguish our colors read the chart? What does a screen reader user get? Can keyboard users reach data points? What if a value is too small to draw?
- **Options:**
  - *Redundant encoding:* shapes, line textures, patterns, markers and direct labels (Atlassian) [S-L05-083]; texture instead of or with color, shades of black with patterns and markers (Carbon, IBM) [S-L05-091] [S-L05-094]; WCAG sufficient technique "using color and pattern" [S-L05-035].
  - *Separation:* gaps or `color.border.inverse` separators between adjacent marks; no text on chart colors [S-L05-083].
  - *Text alternatives:* complex images need a short description plus a long description via adjacent link, alt text pointing to the description, `figure`/`figcaption`, or `aria-describedby` (W3C tutorial, updated 2026-04-08) [S-L05-036]; data tables as an alternative format [S-L05-083]. Carbon notes slices under 1 degree are not rendered, keyboard accessible, or in the tooltip, and can only be exposed through a data table [S-L05-077].
  - *Interaction:* "overview first, zoom and filter, then details on demand"; don't hide important information behind interaction [S-L05-094].
- **Visual effect:** Patterns and markers add texture and can look busy if overused; direct labels and separators make charts look crisper and more editorial as a side effect [S-L05-083] [inferred].
- **Depends on (upstream):** data-viz palette (DC-L05-23), chart library capabilities (DC-L05-22), motion/reduced motion (L04).
- **Affects (downstream):** all charts, legends, tooltips, dashboards, export/print.
- **Token encoding:** pattern and marker definitions as assets, plus `chart.separator.color = {color.border.inverse}` and `chart.separator.width` (`dimension`) [S-L05-083]; names [inferred].
- **Platform notes:** none verified in this session.
- **Accessibility constraints:** WCAG 1.4.1 (not color alone) [S-L05-035]; 1.4.11 (3:1 for essential chart parts such as lines and pie slice boundaries; charts pass if they are still understandable when low-contrast parts are ignored, or if labels carry the values) [S-L05-034]; 1.1.1 via short and long descriptions [S-L05-036].
- **Default + heuristic:** Every chart ships with a title that states the insight, direct labels or a legend with shape cues, a text summary, and a "view as table" option [S-L05-036] [S-L05-077] [S-L05-083].
- **Evidence:** [S-L05-034] [S-L05-035] [S-L05-036] [S-L05-077] [S-L05-083] [S-L05-091] [S-L05-094]

## Open questions / gaps
- **Salesforce Lightning data-viz guidance not captured.** The SLDS 2 site has no charts page and the SLDS 1 URL errors [S-L05-084] [S-L05-085]; the session's web-search budget ran out before I could find the new location [S-L05-087].
- **Material data-viz guidance not captured.** Material 2 (which had data-viz and imagery pages) is marked "no longer maintained" [S-L05-065]; I did not find or verify an M3 equivalent. Treat "M3 has no data-viz page" as unverified.
- **Mailchimp and Duolingo official guideline sites are gone.** Mailchimp's brand page is now product marketing [S-L05-056]; design.duolingo.com redirects to a blog hub [S-L05-055]. Their illustration descriptions here come from design press (Tier B) and Duolingo's own blog, and the popular "three basic shapes" Duolingo rule is unverified.
- **Airbnb's 2025 3D "Lava" icons** are described only by Tier C posts; no Airbnb primary source was read [S-L05-063].
- **Google illustration (Material 3 Expressive)** was not covered; L04 or L10 may have it via the M3 Expressive community file.
- **Text-on-image scrim values** (gradient stops, opacity) have no official source in this lane; DC-L05-16 options beyond "avoid" are [inferred].
- **Image placeholder techniques** (dominant color, blur-up/LQIP) and **avatar initials fallback** are [inferred]; no official page was read for them.
- **Fluent icon stroke and grid values** are not on the Fluent 2 iconography page [S-L05-014]; only sizes and styles were confirmed [S-L05-020].
- **Carbon data-viz "approved textures" page** 404s [S-L05-092], so no pattern set with real values was captured.
- **Polaris icon sizes in px** are not published on the `s-icon` page (only `small`/`base`) [S-L05-027].
- Disk-full errors (ENOSPC) interrupted Bash during the run; one GitHub API check was re-done through WebFetch [S-L05-019] [S-L05-020].

## Confidence
- **Confirmed from Tier A pages read live today (high):** Material Symbols grid, keylines, corners, stroke, axes and typography pairing [S-L05-001] [S-L05-002] [S-L05-003]; SF Symbols rendering modes, weights, scales, variants, animations and the SF Symbols 8 / OS 27 cycle [S-L05-006] [S-L05-008] [S-L05-010]; Apple app-icon specs and appearances (HIG change log 2026-06-08) [S-L05-011]; Android adaptive/themed icon specs (updated 2026-08-13) [S-L05-039]; IBM/Carbon icon, photography, illustration and data-viz values (pages updated 2026-09-09/10) [S-L05-016] [S-L05-017] [S-L05-046] [S-L05-047] [S-L05-048] [S-L05-075] [S-L05-076] [S-L05-077] [S-L05-091]; Atlassian icon, logo, avatar, illustration and chart-token guidance [S-L05-021] [S-L05-044] [S-L05-050] [S-L05-066] [S-L05-083]; Primer icon and avatar values [S-L05-024] [S-L05-069]; WCAG 1.4.1, 1.4.3, 1.4.11 and the W3C complex-images tutorial [S-L05-034] [S-L05-035] [S-L05-036] [S-L05-072]; DTCG 2025.10 has no asset type [S-L05-095]; Polaris Viz archived 2026-07-29 [S-L05-080].
- **Tier B, corroborated or low-risk (medium-high):** Icon Composer 2 naming and features (9to5Mac, consistent with Apple pages) [S-L05-007]; GitHub's icon-font-to-SVG rationale [S-L05-038]; NN/g icon labelling (2014 but consistent with Material, Atlassian, Polaris) [S-L05-037]; Datawrapper palette advice [S-L05-086]; favicon set (Evil Martians) [S-L05-042]; open-source library specs from their own sites [S-L05-029] [S-L05-031] [S-L05-032] [S-L05-033].
- **Inferred (labelled in the cards):** all "visual effect" statements not attributed to a source; proposed token names beyond those Atlassian publishes; the stroke-to-canvas ratio table (computed from sourced values); default recommendations and the questionnaire order; scrim/placeholder/initials techniques.
- **Community pulse:** COMMUNITY-SIGNAL.md has no signal on icons, imagery, illustration or data viz, so nothing here is community-disputed [S-L05-096]. I reconciled one item: DTCG is cited as the stable 2025.10 report, not a draft [S-L05-095].

## Cross-lane notes
- [L05 -> L01] Data-viz palettes belong to both lanes. Real values: Carbon 14-step categorical sequence plus sequential, diverging and alert palettes (DC-L05-23) [S-L05-075]; Atlassian `color.chart.*` tokens pass 3:1 on surfaces but not against each other, so charts need separators; Atlassian does not ship sequential or diverging chart tokens [S-L05-083]. Material Symbols recommend grade -25 for light icons on dark backgrounds, which matters for dark-mode icon tokens [S-L05-003].
- [L05 -> L02] Icon weight should follow text weight: SF Symbols' 9 weights map to SF font weights and 3 scales key off cap height [S-L05-010]; Material says to match grade and optical weight between text and symbols and to shift symbols about 11.5% of text size below the baseline [S-L05-003]; Carbon pairs 16/20px icons with 14/16px IBM Plex and center-aligns them [S-L05-016]. The builder can pre-fill icon stroke from the chosen typeface.
- [L05 -> L03] Touch targets: 48dp around a 24dp icon (40dp for 20dp when mouse and keyboard are primary) in Material, at least 44px in Carbon [S-L05-003] [S-L05-016]. Avatar scale in Primer is base-4 to 32, then base-8 [S-L05-069].
- [L05 -> L04] The corner-radius family should drive icon style (Material Rounded vs Sharp) [S-L05-003] and illustration shape language. Symbol animations (SF Symbols) and animated illustrations (dotLottie) need the motion and reduced-motion rules from L04 [S-L05-010] [S-L05-090]. Apple's app icons now take Liquid Glass effects from the system; designers should not bake in highlights or shadows [S-L05-011].
- [L05 -> L06] Brand personality drives icon style, photo brief and illustration style. Useful exemplars: IBM (engineered, fact-based photography with no grading or filters) [S-L05-047] [S-L05-049]; Duolingo (rounder, friendlier since 2018) [S-L05-059]; Slack (logo geometry extended into icons and patterns) [S-L05-060]; Mailchimp ("playful surrealism") [S-L05-061]; Dropbox (icons borrow Sharp Grotesk corners) [S-L05-058].
- [L05 -> L07] DTCG 2025.10 has no icon, image, file or aspect-ratio `$type` ("File" is only a future candidate) [S-L05-095]. The builder needs a convention for asset references (a manifest or `$extensions`) and for ratios (`number` or string). Icon axes (fill, weight, grade, optical size) fit `number`/`fontWeight` tokens [S-L05-002].
- [L05 -> L08] Components that consume L05 decisions: icon button, nav/tab bar (filled-for-selected), avatar and avatar group (circle person, square entity, hexagon or square for AI agents), empty state (spot illustration), skeleton (containers only, per Carbon), chart components, legend, tooltip [S-L05-066] [S-L05-069] [S-L05-071] [S-L05-091].
- [L05 -> L09] Benchmark facts to reuse: Polaris Viz was deprecated and its repo archived 2026-07-29 [S-L05-080]; Polaris `s-icon` blocks custom SVGs [S-L05-027]; old polaris-react and polaris-icons sites now redirect to shopify.dev [S-L05-023] [S-L05-026].
- [L05 -> L10] Current platform versions: SF Symbols 8 (7,000+ symbols; symbols for iOS 27 and the other 27-series OSes) and Icon Composer 2 from WWDC26 [S-L05-006] [S-L05-007] [S-L05-008]; Apple app icons ship in six appearances (default, dark, clear light, clear dark, tinted light, tinted dark) [S-L05-011]; Android 16 QPR2 auto-themes launcher icons for apps without a monochrome layer [S-L05-039].
- [L05 -> L11] Icon contribution needs a checklist (template, keylines, stroke, naming, RTL metadata); Atlassian asks whether an icon is truly needed before adding one [S-L05-021]; Fluent names icons by shape, not function [S-L05-014].
