# L04: Shape, Elevation, Materials, Borders, Motion, Sound, Haptics

Lane: L04. Author: orchestrator subagent L04. Started 2026-09-23.
Status: done (2026-09-23). 28 Decision Cards; comparison tables A1 (radius), C1 (elevation), D1 (materials), F1 (durations), F2 (easing), F3 (springs), G1 (haptics).

## Lane overview
This lane covers the "physical" layer of a design system: how corners are shaped, how edges and focus are drawn, how surfaces stack (elevation, shadows, z-order), which materials are translucent, how things move, and what users feel and hear.

Five findings shape the builder:
1. **Radius scales have converged.** A 2-4px first step, a 4px rhythm, 4-11 steps, and a "full" token. Even IBM Carbon, the reference square-cornered system, is adding radius tokens (0/2/4/8/16/24/max) behind its v12 feature flag (v12 is unreleased; latest release v11.117.0, Sept 2026) [S-V1b-044]. Tags are moving from pill to 2-4px [S-L04-030] [S-L04-031].
2. **Motion has split into two moods.** Carbon has productive vs expressive easing; Material 3 has standard vs expressive motion schemes, now spring-based. M3 Expressive's default spatial spring is damping 0.8 / stiffness 380, against standard's 0.9 / 700 [S-L04-004] [S-L04-014] [S-L04-060]. Motion personality should be a theme mode.
3. **Springs are mainstream but not standardized.** Apple uses duration + bounce, M3 uses damping + stiffness, and Atlassian ships a spring as a CSS `linear()` curve. DTCG 2025.10 has no spring type, so every system improvises [S-L04-003] [S-L04-018] [S-L04-037] [S-L04-052].
4. **Depth is now a strategy choice, not a shadow ramp.** Options include tonal surfaces (M3), semantic surface + paired shadow (Atlassian), materials (Apple Liquid Glass, Windows Mica/Acrylic), and layered shadows (Fluent, Polaris, Primer). Dark mode needs lighter surfaces and edge rings, not just darker shadows [S-L04-017] [S-L04-018] [S-L04-024] [S-L04-058].
5. **Translucency comes with a legibility tax.** Apple's Liquid Glass went from launch (iOS 26) to a Clear/Tinted option (iOS 26.1, confirmed on Apple's own page [S-V1b-021]) to a system transparency slider and "improved contrast" (iOS 27) [S-L04-039] [S-L04-041]. Every material token needs an opaque twin for Reduce Transparency [S-L04-011] [S-L04-032] [S-L04-065].

Accessibility bounds: WCAG 2.2 2.4.11 Focus Not Obscured (Minimum) is AA; 2.4.13 Focus Appearance (2 CSS px perimeter, 3:1 change) and 2.3.3 Animation from Interactions are AAA [S-L04-048] [S-L04-049] [S-L04-050].

Card index: Shape DC-L04-01 to 06; Borders and focus 07 to 09; Elevation 10 to 14; Materials 15 and 16; Opacity and scrims 17 and 18; Motion 19 to 25; Haptics and sound 26 and 27; Token encoding 28. A decision graph, community reconciliation, gaps, confidence and cross-lane notes follow the cards.

---

## Part A. Shape

### Comparison table A1: corner radius scales (real values)

| System | Scale (token: value) | Default for buttons | Notes | Evidence |
|---|---|---|---|---|
| Material 3 (incl. Expressive additions) | none 0, extra-small 4, small 8, medium 12, large 16, **large-increased 20**, extra-large 28, **extra-large-increased 32**, **extra-extra-large 48**, full (9999px / CircleShape). Also asymmetric variants: extra-small-top, large-top, large-start, large-end, extra-large-top | full (pill): filled and elevated buttons use corner-full; cards corner-medium 12; menus and tooltips extra-small 4; dialogs extra-large 28; bottom sheet extra-large-top [S-L04-069] | the three bold steps are the Expressive-era additions present in the current official token export (v34, April 2026) and in Compose ShapeTokens | [S-L04-003] [S-L04-004] |
| Fluent 2 (web tokens, Fluent UI React v9) | none 0, small 2, medium 4, large 6, xLarge 8, 2xLarge 12, 3xLarge 16, 4xLarge 24, 5xLarge 32, 6xLarge 40, circular 10000px | medium 4px | 2XL-6XL were added to the token package in Jan 2026. Design site maps "Large 8px / X-Large 12px", which does not match the package names (Large 6px / XLarge 8px); use the published React v9 token names for web output; the docs discrepancy remains, and its age is not established [S-L04-078] [S-L04-079] | [S-L04-006] [S-L04-007] |
| Atlassian | xsmall 2, small 4, medium 6, large 8, xlarge 12, xxlarge 16, full 9999px, tile 25% | medium 6px | `radius.focus.*` = element radius + 2px for focus rings | [S-L04-016] [S-L04-018] |
| Shopify Polaris | 0, 050 2, 100 4, 150 6, 200 8, 300 12, 400 16, 500 20, 750 30, full 9999px | not confirmed in this lane | numeric names follow the Polaris 4px-based size scale | [S-L04-022] |
| GitHub Primer | small 3, medium 6 (= default), large 12, full 9999px | default 6px | smallest, most restrained scale of the set | [S-L04-024] |
| IBM Carbon v11 (released) | no radius tokens; corners square | 0 | the canonical "square" system | [S-L04-029] [S-L04-031] |
| IBM Carbon v12 (unreleased, behind feature flag `enable-v12-release` [S-V1b-044]) | border-radius-00 0, 02 2px, 04 4px, 08 8px, 16, 24, max 999999px | proposed `$border-radius-max` (pill), PR still open | tags stop being pill (sm 2px, md/lg 4px); popover 8px, tooltip 4px; menu 8px, menu item 4px; card 8px; progress bar max | [S-L04-028] [S-L04-030] [S-L04-031] |
| Apple (iOS 26+) | no public radius scale. Radii come from the hardware: controls, sheets and windows are made concentric with the display corners; `ConcentricRectangle` computes radii from the container | capsule for many controls [S-L04-038]; exact radii not published | continuous-curvature corners (`RoundedCornerStyle.continuous`) | [S-L04-035] [S-L04-036] [S-L04-038] [S-L04-042] |

Pattern across systems [inferred from the table]: every public scale starts with a 2 to 4px step and ends with a "full" value (9999px or similar). The middle steps sit on a 4px rhythm. The number of steps ranges from 4 (Primer) to 11 (Fluent). Enterprise web systems default buttons to 4 to 6px. Material and Apple push toward pills and capsules.

### DC-L04-01: Corner radius scale (how many steps, which values)
- **Block path:** Foundations > Shape > Corner radius scale
- **Questions the designer answers:** How many radius steps do we need? What is the smallest non-zero radius and the largest? Do we include a "full" (pill) token? Do we need asymmetric (top-only, start-only) variants?
- **Options:**
  - *Minimal (3-4 steps + full):* Primer 3/6/12/full [S-L04-024].
  - *Medium (6-8 steps + full):* Atlassian 2/4/6/8/12/16/full [S-L04-016]; Carbon v12 0/2/4/8/16/24/max [S-L04-030]; Polaris 2 to 30 plus full [S-L04-022].
  - *Large (9-11 steps + full):* Material 3 0 to 48 plus full [S-L04-003]; Fluent 0 to 40 plus circular [S-L04-006].
  - *No scale, derived radii:* Apple derives radii from the container or hardware through concentricity [S-L04-035].
  - *Asymmetric variants:* Material ships `*-top`, `*-start`, `*-end` tokens for sheets and drawers [S-L04-003].
- **Visual effect:** A short scale gives a tighter, more uniform look because fewer distinct curvatures appear on screen. A long scale lets large surfaces (sheets, dialogs, hero cards) curve more than small controls, which keeps curvature looking proportional to size [inferred].
- **Depends on (upstream):** brand personality (DC-L04-02), base spacing unit (L03: radius steps usually reuse the 4px grid [inferred from the table]), platform targets (L10).
- **Affects (downstream):** every component radius (DC-L04-03), focus ring radius (DC-L04-09), nested radius math (DC-L04-05), shadow shape (shadows follow border-radius on the web [inferred]).
- **Token encoding:** DTCG `$type: dimension`, `$value: {"value": 8, "unit": "px"}` [S-L04-052]. Primitive `radius.100 = 4px` or t-shirt `radius.sm`; semantic `radius.control`, `radius.container`, `radius.full`; component `button.radius`. Carbon already publishes its radius set as DTCG JSON [S-L04-030]; Primer as DTCG json5 [S-L04-024].
- **Platform notes:** Android Compose uses `RoundedCornerShape(dp)` and `CircleShape` [S-L04-004]; iOS uses continuous corners and container-relative shapes [S-L04-035] [S-L04-036]; web uses `border-radius` in px (no continuous curvature unless `corner-shape` is used, DC-L04-04).
- **Accessibility constraints:** None directly. Very large radii on small controls can shrink the visible hit shape; keep the touch target rectangle at the platform minimum even when the visual is a circle (L03 touch targets) [inferred].
- **Default + heuristic:** 7 steps + full on a 4px rhythm: 0, 2, 4, 8, 12, 16, 24, full. Heuristic: radius should grow with component size. If you cannot name a component that uses a step, delete the step.
- **Evidence:** [S-L04-003] [S-L04-004] [S-L04-006] [S-L04-016] [S-L04-022] [S-L04-024] [S-L04-030] [S-L04-035]

### DC-L04-02: Overall roundness level (the "shape personality" dial)
- **Block path:** Foundations > Shape > Shape personality
- **Questions the designer answers:** Should the product feel precise and technical, or soft and friendly? How round is a standard button: square, slightly rounded, or pill? Will shape be a brand signature?
- **Options:**
  - *Sharp (0-2px):* Carbon v11 (0) [S-L04-029]; Fluent uses 2px under 32px [S-L04-007].
  - *Subtle (3-6px):* Primer 6px default [S-L04-024]; Fluent 4px default [S-L04-007]; Atlassian 6px interactive elements [S-L04-016].
  - *Soft (8-16px):* Atlassian containers 8-12px [S-L04-016]; Carbon v12 cards/popovers 8px [S-L04-031].
  - *Pill / capsule / expressive:* Material full-radius buttons and a 35-shape expressive library [S-L04-005]; Apple rounder, capsule-shaped controls in iOS 26 [S-L04-038]; Carbon v12 proposes pill buttons (PR open) [S-L04-028].
- **Visual effect:** Sharp corners read as serious, technical, dense and "enterprise". Round corners read as friendly, approachable and consumer. Very round or morphing shapes read as playful and expressive. This is a common design convention; the closest measured evidence is Google's M3 Expressive research (46 studies, 18,000+ participants), where expressive designs (shape, color, size, containment together, so the effect is not isolated to shape) were rated "energetic", "playful" and "friendly". Users spotted key elements up to 4x faster, and 18-24-year-olds showed up to 87% preference. The same research warns against breaking familiar patterns and says contexts like banking need restraint [S-L04-063]. Industry direction in 2025-26: even Carbon, the reference "square" system, is adding radius in v12 [S-L04-031]. This suggests the sharp end of the dial is now a deliberate brand choice rather than the default for enterprise [inferred].
- **Depends on (upstream):** brand personality and voice (L06), typography (L02: geometric, rounded typefaces pair with rounder shapes [inferred]), audience and density (L03).
- **Affects (downstream):** radius scale values (DC-L04-01), icon corner style (L05: icon strokes and terminals should echo the UI radius [inferred]), illustration style, motion personality (DC-L04-19: round shapes pair naturally with springier motion [inferred]).
- **Token encoding:** Put this dial in a single "shape theme" mode that swaps semantic radius aliases. Example: `radius.control -> {radius.100}` in the "crisp" mode and `-> {radius.full}` in the "friendly" mode. Carbon's v11/v12 flag is exactly this pattern: the same components, with radius tokens switched by a flag [S-L04-029].
- **Platform notes:** On iOS the system decides much of this: controls become capsules and concentric with the hardware whatever your brand is [S-L04-038]. Fighting it looks off-platform [inferred].
- **Accessibility constraints:** None directly.
- **Default + heuristic:** Subtle (4-6px controls, 8-12px containers) is the safest cross-audience default. Choose sharp only when density and precision are brand values (data tools, developer tools). Choose pill when the brand is consumer and playful, or when you target Material 3 or iOS 26 conventions.
- **Evidence:** [S-L04-005] [S-L04-007] [S-L04-016] [S-L04-024] [S-L04-028] [S-L04-029] [S-L04-031] [S-L04-038] [S-L04-063]

### DC-L04-03: Per-component radius mapping (semantic radius roles)
- **Block path:** Foundations > Shape > Radius roles > Component mapping
- **Questions the designer answers:** Which radius does each component family use? Are people/avatars circular? Do small elements (badges, checkboxes) get a smaller radius than buttons? Do containers get more?
- **Options (real mappings):**
  - *Atlassian (role by component family):* xsmall 2px for badges, checkboxes, avatar labels, keyboard shortcuts; small 4px for labels, lozenges, tags, tooltips, compact buttons; medium 6px for buttons, inputs, selects, nav items; large 8px for cards, floating UI, dropdown menus; xlarge 12px for modals, Kanban columns, tables; xxlarge 16px for video players; full for avatars and people UI; tile 25% [S-L04-016] [S-L04-018].
  - *Fluent 2:* None for nav bars and tab bars; Small 2px for small badges; Medium 4px for buttons and dropdowns (the default); Large for large buttons; X-Large for sheets and popovers; Circle for personas. Shapes under 32px drop to 2px [S-L04-007].
  - *Carbon v12:* small tag 2px, medium/large tag 4px, tooltip 4px, menu item 4px, menu 8px, popover 8px, card 8px, progress bar max [S-L04-031].
  - *Apple iOS 26:* sheets have a larger radius, list sections have a larger radius "to match the curvature of controls", and controls are rounder [S-L04-038].
- **Visual effect:** Scaling radius with element size keeps curvature proportional. Reserving "full" for people (avatars) makes circles carry meaning, as in Fluent and Atlassian [S-L04-007] [S-L04-016].
- **Depends on (upstream):** DC-L04-01 scale, DC-L04-02 personality, the component inventory (L08).
- **Affects (downstream):** component tokens (`button.radius`, `card.radius`), focus ring radius, nested content radius inside cards and sheets (DC-L04-05).
- **Token encoding:** semantic role tokens (`radius.control`, `radius.container`, `radius.overlay`, `radius.person`) that alias primitives. Components reference roles, never primitives [inferred best practice consistent with L07 tiering].
- **Platform notes:** Fluent and Apple both warn against rounding corners that touch the screen edge. Fluent: avoid rounded corners "at the screen's edge" and between adjacent elements [S-L04-007]. Apple: make them concentric with the device corners instead [S-L04-035].
- **Accessibility constraints:** Non-text contrast (1.4.11 AA, 3:1) applies to the boundary of the component, not its radius; rounding does not change the requirement [inferred from S-L04-048].
- **Default + heuristic:** Map 4 roles: small detail 2-4px, control 4-8px (or full), container 8-12px, overlay/sheet 12-16px or more, plus person = full. Rule of thumb: the radius steps up one level each time the element's height roughly doubles [inferred].
- **Evidence:** [S-L04-007] [S-L04-016] [S-L04-018] [S-L04-031] [S-L04-035] [S-L04-038]

### DC-L04-04: Corner geometry (circular arc vs continuous curvature / squircle)
- **Block path:** Foundations > Shape > Corner geometry
- **Questions the designer answers:** Are corners simple circular arcs, or smoothed "squircle" curves? Must the web match the iOS look?
- **Options:**
  - *Circular arc (CSS `border-radius` default):* every web system in table A1.
  - *Continuous curvature:* Apple's `RoundedCornerStyle.continuous` (iOS 13+) [S-L04-036]. Figma reproduces it with "corner smoothing"; the iOS preset is 60%, and smoothing applies to the whole shape, not per corner [S-L04-055].
  - *Web superellipse:* CSS `corner-shape: squircle` (= `superellipse(2)`), plus bevel, scoop, notch and square. Defined in CSS Borders 4, experimental and not Baseline as of 2026-08-27 [S-L04-054].
- **Visual effect:** A circular arc meets the straight edge with a visible "kink" in curvature. Continuous curves blend in gradually and read as softer and more "Apple" at the same nominal radius [S-L04-055]. Bevel and notch corners read as technical or industrial [inferred].
- **Depends on (upstream):** platform targets (L10), personality (DC-L04-02).
- **Affects (downstream):** icon masks (L05), cards, buttons, image thumbnails, Figma component setup (corner smoothing is a Figma property, not a variable [inferred from S-L04-055]).
- **Token encoding:** DTCG has no corner-shape type [S-L04-052]. Encode as `$extensions` (for example `"com.example.shape": {"cornerSmoothing": 0.6}`) or as a string token consumed only by the web (`corner-shape: squircle`) [inferred].
- **Platform notes:** iOS: continuous is native. Web: `corner-shape` with a `border-radius` fallback (it has no effect without border-radius) [S-L04-054]. Android: Compose `RoundedPolygon` in the graphics-shapes library allows smoothed polygons [S-L04-005].
- **Accessibility constraints:** none.
- **Default + heuristic:** Use circular arcs on the web today. Add `corner-shape: squircle` as progressive enhancement only if brand parity with iOS matters. In Figma, use 60% smoothing only for iOS-targeted components.
- **Evidence:** [S-L04-005] [S-L04-036] [S-L04-052] [S-L04-054] [S-L04-055]

### DC-L04-05: Nested and concentric radius rule
- **Block path:** Foundations > Shape > Nesting rule
- **Questions the designer answers:** When a rounded element sits inside another rounded element, what radius should the inner one get? Do we automate this?
- **Options:**
  - *Same radius inside and out:* this makes the gap look uneven, thick at the corners [S-L04-057].
  - *Concentric (outer = inner + padding, so inner = outer - padding):* the classic rule. When padding exceeds the outer radius, the inner radius collapses to 0, which "doesn't feel right" [S-L04-057].
  - *Concentric with a minimum:* Apple `ConcentricRectangle` computes each corner so it shares a center with the container's corner. It lets you set `concentric(minimum:)` so corners far from the container do not collapse to square [S-L04-035].
  - *Mixed:* Apple's Notes format sheet has fixed-radius top corners and concentric bottom corners [S-L04-035].
- **Visual effect:** Concentric corners keep an even gap around the curve and make nested cards, image thumbnails in cards, and buttons in sheets look "machined" and harmonious. Apple uses this to tie software to hardware corners [S-L04-042].
- **Depends on (upstream):** radius scale (DC-L04-01), spacing scale (L03, padding values).
- **Affects (downstream):** cards with media, sheets, dialogs with buttons, segmented controls, chips inside inputs, focus rings (a ring drawn outside a control is itself a nested outer shape; Atlassian's radius.focus = radius + 2px is the same rule applied to a 2px offset [S-L04-016]).
- **Token encoding:** compute, don't store. Web: `calc(var(--radius-outer) - var(--space-inset))` with `max(<min>, ...)` for the floor [inferred]. The builder can generate derived tokens such as `card.media.radius = card.radius - card.padding`. DTCG 2025.10 has no math expressions, so this belongs in the build tool [inferred from S-L04-052].
- **Platform notes:** iOS: `containerShape()` + `ConcentricRectangle` (iOS 26+) [S-L04-035]. Web/Android: manual math.
- **Accessibility constraints:** none.
- **Default + heuristic:** inner = max(outer - padding, smallest non-zero radius). The builder should auto-derive inner radii and warn when someone sets equal radii on nested elements.
- **Evidence:** [S-L04-016] [S-L04-035] [S-L04-042] [S-L04-057]

### DC-L04-06: Pill, full-round and expressive shape library (incl. shape morphing)
- **Block path:** Foundations > Shape > Full round and expressive shapes
- **Questions the designer answers:** Do buttons, chips and tags use full (pill) radius? Do we have decorative or "expressive" shapes beyond rounded rectangles? Do shapes change (morph) on interaction?
- **Options:**
  - *Pill as a token only:* `radius.full` = 9999px (Atlassian, Polaris, Primer), 10000px (Fluent), 999999px (Carbon v12) [S-L04-006] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-030].
  - *Pill reserved for people and status:* avatars and reactions get full (Atlassian) [S-L04-016]; Carbon v12 moves tags away from pill to 2-4px [S-L04-031].
  - *Expressive shape library:* M3 Expressive `MaterialShapes` defines 35 normalized `RoundedPolygon` shapes (Circle, Square, Slanted, Arch, Fan, Arrow, SemiCircle, Oval, Pill, Triangle, Diamond, ClamShell, Pentagon, Gem, Sunny, VerySunny, Cookie4/6/7/9/12Sided, Ghostish, Clover4/8Leaf, Burst, SoftBurst, Boom, SoftBoom, Flower, Puffy, PuffyDiamond, PixelCircle, PixelTriangle, Bun, Heart). They can be used alone or as endpoints of a `Morph`, and are still marked `@ExperimentalMaterial3ExpressiveApi` [S-L04-005].
  - *Morphing on interaction:* M3 Expressive morphs between shapes through `Morph.toPath(progress)` [S-L04-005]. Apple buttons "fluidly morph into menus and popovers" with Liquid Glass [S-L04-038].
- **Visual effect:** Pills read as tappable, friendly, "consumer". Expressive shapes (cookies, bursts, clovers) add brand playfulness and are best for avatars, loading indicators, image masks and FABs rather than for dense UI [inferred]. Morphing ties shape to state (pressed, selected) and feels alive [inferred].
- **Depends on (upstream):** personality (DC-L04-02), motion system (springs, DC-L04-22), platform.
- **Affects (downstream):** buttons, chips, FABs, avatars, loaders, image masks, selection states.
- **Token encoding:** radius full = dimension. Shapes have no DTCG type; encode as an SVG path or a named asset reference in `$extensions`, and morph pairs as component-level motion specs [inferred from S-L04-052].
- **Platform notes:** Compose ships the library natively [S-L04-005]; web needs SVG `clip-path: path()` or masks [inferred]; iOS morphing is system-driven through `GlassEffectContainer` [S-L04-038].
- **Accessibility constraints:** Shape must not be the only indicator of state (WCAG 1.4.1 applies to color; the same logic applies to shape by analogy) [inferred]. Morph animations fall under reduced-motion rules (DC-L04-25).
- **Default + heuristic:** Ship `radius.full`. Add expressive shapes only if the brand is playful and you target Android/Material; limit them to 1-3 signature uses.
- **Evidence:** [S-L04-005] [S-L04-006] [S-L04-016] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-030] [S-L04-031] [S-L04-038]

---

## Part B. Borders, strokes, dividers, focus

### DC-L04-07: Border and stroke width scale (and outline vs fill vs shadow-as-border)
- **Block path:** Foundations > Borders > Stroke width scale
- **Questions the designer answers:** Which stroke widths exist? Are component boundaries drawn with borders, fills, or both? Do we use inset shadows instead of borders to avoid layout shift?
- **Options (real values):**
  - Fluent web: thin 1, thick 2, thicker 3, thickest 4px. Fluent mobile: 1/2/4/6 [S-L04-006] [S-L04-007].
  - Atlassian: border.width 1px, border.width.selected 2px, border.width.focused 2px [S-L04-018].
  - Primer: thin 1px (= default), thick 2px ("MUST use for focus rings"), thicker 4px. `boxShadow.thin/thick/thicker` = `inset 0 0 0 <width>` "used instead of a border to prevent layout shift" [S-L04-024].
  - Polaris: 0, 0165 (0.66px), 025 (1px), 050 (2px), 100 (4px) [S-L04-022]. The 0.66px step is a hairline for high-density screens [inferred].
  - Polaris uses layered inset shadows (`shadow-bevel-100`, `shadow-button`) to fake a 3D bevel edge on buttons and cards [S-L04-022].
- **Visual effect:** 1px borders read as light and "outlined". Filled controls without borders read as bolder. Bevel and inset shadows give a tactile, skeuomorphic hint (Polaris's 2023+ look) [inferred]. Hairlines under 1px look crisp on retina screens but vanish on 1x screens [inferred].
- **Depends on (upstream):** color neutrals (L01: border color has to hit 3:1 against adjacent colors for component boundaries), density (L03), elevation strategy (DC-L04-10).
- **Affects (downstream):** inputs, cards, dividers, selected states (2px), focus rings, table grids.
- **Token encoding:** DTCG `dimension` for widths; DTCG `border` composite `{color, width, style}`; `strokeStyle` string (`solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `outset`, `inset`) or `{dashArray, lineCap}` [S-L04-052]. Names: `border.width.default`, `border.width.selected`, `border.width.focus`; composite `border.input.default`.
- **Platform notes:** Fluent sets thicker strokes on mobile [S-L04-007]. Figma's lack of support for `inset/outset/double` strokes means those fall back to solid [S-L04-052].
- **Accessibility constraints:** If the border is the only thing that shows a control's boundary (for example, a text input on a white background), WCAG 1.4.11 Non-text Contrast (AA) requires 3:1 against adjacent colors [S-L04-048 references 1.4.11]. This makes "outline-only" inputs depend on a darker border neutral than decorative dividers need [inferred].
- **Default + heuristic:** 1px default, 2px selected and focus, 4px emphasis. Use inset box-shadow borders for states that change width (selected, error) so layout does not jump (the Primer pattern) [S-L04-024].
- **Evidence:** [S-L04-006] [S-L04-007] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-048] [S-L04-052]

### DC-L04-08: Divider and separator usage
- **Block path:** Foundations > Borders > Dividers
- **Questions the designer answers:** Do we separate content with lines, with space, or with surface color changes? How strong are dividers?
- **Options:**
  - *Lines:* 1px low-contrast border tokens (all systems) [S-L04-024].
  - *Whitespace and surface shifts:* Atlassian recommends whitespace or borders instead of nesting sunken surfaces [S-L04-017]; Apple uses a single vibrant `separator` value that works on all materials [S-L04-032].
  - *Surface-layer separation:* Windows uses layer fills on Mica (`LayerFillColorDefaultBrush`) instead of lines [S-L04-012].
- **Visual effect:** More lines read as more structured, denser, more "spreadsheet". Space and surface shifts read as calmer and more premium [inferred].
- **Depends on (upstream):** density (L03), neutral ramp (L01), elevation strategy (DC-L04-10).
- **Affects (downstream):** lists, tables, menus, sidebars, cards.
- **Token encoding:** `color.border.subtle` (L01) + `border.width.default`; or a composite `border.divider`.
- **Platform notes:** Apple separators are vibrant (they blend with the material) [S-L04-032].
- **Accessibility constraints:** Decorative dividers are exempt from 1.4.11. Only boundaries needed to identify a component need 3:1 [inferred from S-L04-048].
- **Default + heuristic:** Prefer space first, then surface change, then 1px subtle lines. Use lines in dense data views.
- **Evidence:** [S-L04-012] [S-L04-017] [S-L04-024] [S-L04-032] [S-L04-048]

### DC-L04-09: Focus indicator (thickness, offset, color, shape)
- **Block path:** Foundations > Borders > Focus ring
- **Questions the designer answers:** How thick is the focus ring? Is it drawn outside (offset), on the edge, or inside? What color? Does it follow the component's radius? What happens in forced-colors / high contrast?
- **Options (real values):**
  - Material 3: thickness 3px, outer offset 2px, inner offset -3px (for elements where an outside ring would clip) [S-L04-003].
  - Atlassian: border.width.focused 2px; `radius.focus.*` = element radius + 2px, so the ring stays concentric [S-L04-016] [S-L04-018].
  - Primer: 2px `borderWidth.thick` is the mandated focus-ring width [S-L04-024].
  - Fluent: the ring is drawn as a pseudo-element with `outlineRadius` matching the control, and switches to the system `Highlight` color in forced-colors mode [S-L04-053].
- **Visual effect:** Thicker, offset rings are unmistakable but louder. Inner rings keep layouts tight but can fail contrast on filled controls [inferred].
- **Depends on (upstream):** brand/primary color and neutrals (L01), radius (DC-L04-05 concentric rule), stroke scale (DC-L04-07).
- **Affects (downstream):** every interactive component, `:focus-visible` styles, z-index/overflow rules (a ring can be clipped by `overflow: hidden` parents [inferred]).
- **Token encoding:** `focus.ring.width` (dimension), `focus.ring.offset` (dimension), `focus.ring.color` (color), optional composite `border.focus` (`border` type). No dedicated DTCG outline type; use `border` or separate tokens [S-L04-052].
- **Platform notes:** Web: `outline` + `outline-offset` follow `border-radius` in modern browsers [inferred]. iOS/Android: system focus on keyboard or remote (tvOS focus uses Liquid Glass on focus [S-L04-038]).
- **Accessibility constraints:** WCAG 2.4.7 Focus Visible (AA) requires a visible indicator. WCAG 2.2 SC **2.4.11 Focus Not Obscured (Minimum) is AA**: the focused component must not be entirely hidden by author content such as sticky headers. 2.4.12 (Enhanced, none hidden) is AAA [S-L04-050]. SC **2.4.13 Focus Appearance is AAA**: the indicator area must be at least a 2 CSS px thick perimeter, with a 3:1 change of contrast between focused and unfocused states [S-L04-048]. 1.4.11 (AA) separately requires 3:1 against adjacent colors [S-L04-048].
- **Default + heuristic:** 2px solid ring, 2px offset, radius = component radius + offset, color = high-contrast brand or neutral token with a light and dark mode value, plus a forced-colors fallback. The 2px ring meets the 2.4.13 area rule on its own, provided its color also gives a 3:1 change against the unfocused state [inferred from S-L04-048].
- **Evidence:** [S-L04-003] [S-L04-016] [S-L04-018] [S-L04-024] [S-L04-048] [S-L04-050] [S-L04-052] [S-L04-053]

---

## Part C. Elevation and depth

### Comparison table C1: elevation / shadow scales (real values)

| System | Levels | Values | Depth model | Evidence |
|---|---|---|---|---|
| Material 3 | level0-level5 | 0, 1, 3, 6, 8, 12 dp. Mapping: filled card and filled button level0 (hover level1); elevated card and elevated button level1 (hover level2); menu and navigation bar level2; FAB, dialog and snackbar level3; top app bar level0, rising to level2 on scroll | **Tonal first.** Elevation is shown mainly by tonal surface color; shadows are optional (`tonalElevation` vs `shadowElevation`). Token notes: surfaces moved "from opacity based surfaces to tonal surfaces"; surface-tint layers are deprecated, so use surface container roles directly | [S-L04-003] [S-L04-058] [S-L04-069] |
| Fluent 2 | shadow2, 4, 8, 16 (low); 28, 64 (high) | two layers each: ambient `0 0 2px` + key `0 1px 2px` (s2) ... ambient `0 0 8px` + key `0 32px 64px` (s64). Light colors: ambient rgba(0,0,0,.12), key .14. Brand shadows use .30/.25. Usage: s2 cards without edges; s4 cards and list items; s8 raised cards, FAB, command bars, tooltips; s16 callouts and hover cards; s28 bottom sheets and side nav; s64 dialogs | **Shadow ramp**, key + ambient. Dark mode uses higher shadow opacity. Windows swaps key shadows for strokes | [S-L04-006] [S-L04-008] |
| Atlassian | surface: sunken < default < raised < overlay | light shadow.raised = `0 1px 1px #1E1F21@25%, 0 0 1px @31%`; shadow.overlay = `0 8px 12px @15%, 0 0 1px @31%`; shadow.overflow for scroll edges. Dark surfaces get lighter with height: default #1F1F21, raised #242528, overlay #2B2C2F, sunken #18191A. The dark overlay shadow adds a 1px #BDBDBD@12% ring | **Semantic surface + paired shadow.** Rule: always pair surface.raised with shadow.raised and surface.overlay with shadow.overlay | [S-L04-017] [S-L04-018] |
| Shopify Polaris | shadow-0 ... 600 + bevel/inset/button | 100 `0 1px 0 0 rgba(26,26,26,.07)`; 200 `0 3px 1px -1px .07`; 300 `0 4px 6px -2px .20`; 400 `0 8px 16px -4px .22`; 500 `0 12px 20px -8px .24`; 600 `0 20px 20px -8px .28`; plus multi-layer inset "bevel" shadows on buttons and cards | **Numeric shadow ramp + tactile bevels** (negative spread keeps shadows tucked under the element) | [S-L04-022] |
| GitHub Primer | resting xsmall/small/medium; floating small/medium/large/xlarge; inset | resting.medium = `0 1px 1px neutral12@10%, 0 3px 6px neutral12@12%`; floating.large = `0 0 0 1px overlay.borderColor` ring (alpha 0 in light, alpha 1 in dark and light-high-contrast) + `0 40px 80px neutral12@24%`; floating.xlarge = ring + `0 56px 112px @32%`. The dark override for floating.large is ring + `0 24px 48px neutral0@100%`. Other dark overrides use neutral.0 at 0.4-1.0 alpha. Every token also carries `org.primer.llm` usage/rules metadata | **Resting vs floating** split. Floating shadows carry an outline-ring layer that is switched on only in dark and high-contrast modes | [S-L04-024] |
| Apple (iOS 26+) | none published | n/a | **Materials, not shadows.** Depth comes from the Liquid Glass functional layer over content plus standard materials inside content | [S-L04-032] |

Cross-system pattern [inferred from table]: (1) 4-6 steps is the norm. (2) Every modern ramp uses at least two shadow layers: a tight contact or edge shadow plus a soft diffuse one. (3) Dark mode leans on surface lightness, stronger shadows and edge rings, because plain shadows vanish on dark backgrounds (Atlassian says so explicitly [S-L04-017]).

### DC-L04-10: Depth strategy (flat vs shadow vs tonal vs material)
- **Block path:** Foundations > Elevation > Depth strategy
- **Questions the designer answers:** How do we show that one surface sits above another: shadows, color or tone shifts, borders, blur, or nothing (flat)? Does the answer change in dark mode?
- **Options:**
  - *Flat + borders:* Atlassian default surface "pair with borders for flat cards" [S-L04-017]; Carbon v11 is largely flat [inferred, Carbon elevation not verified in this lane].
  - *Shadow ramp:* Fluent [S-L04-008], Polaris [S-L04-022], Primer [S-L04-024].
  - *Tonal elevation:* Material 3, where higher surfaces use different tonal container colors and shadows are secondary [S-L04-058] [S-L04-069].
  - *Semantic surfaces + paired shadows:* Atlassian [S-L04-017].
  - *Materials (translucency/blur):* Apple Liquid Glass for the control layer [S-L04-032]; Fluent Acrylic for transient surfaces [S-L04-011].
- **Visual effect:** Flat reads as modern, calm, dense and "print-like". Shadows read as tactile and give clear layering. Tonal reads as soft, color-forward and Material-like. Materials read as premium and immersive but can hurt legibility [S-L04-068].
- **Depends on (upstream):** color system (L01: tonal elevation needs tonal surface ramps; dark mode), brand personality (L06), platform (L10).
- **Affects (downstream):** cards, menus, dialogs, app bars, sheets, FABs, dark-mode surface tokens, border usage (DC-L04-07).
- **Token encoding:** shadow tokens use DTCG `shadow` (object or array of layers, optional `inset`) [S-L04-052]; tonal elevation uses `color` tokens (`color.surface.container.high`) (L01); surface roles `elevation.surface.raised` (Atlassian naming) [S-L04-018].
- **Platform notes:** Android: tonal by default in M3 [S-L04-058]. iOS: materials, not shadow tokens [S-L04-032]. Windows: Mica base + layer fills + strokes [S-L04-012]. Web: any.
- **Accessibility constraints:** Elevation must not be the only cue for interactivity [inferred]. Surface color steps in dark mode must keep text contrast (L01); Atlassian says to verify contrast in dark mode [S-L04-017].
- **Default + heuristic:** Hybrid: flat surfaces with borders for in-page containers; shadows only for things that float (menus, popovers, dialogs, drag states); in dark mode, raise surface lightness and keep shadows for overlays. This is essentially the Atlassian model [S-L04-017].
- **Evidence:** [S-L04-008] [S-L04-011] [S-L04-012] [S-L04-017] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-032] [S-L04-052] [S-L04-058] [S-L04-068] [S-L04-069]

### DC-L04-11: Elevation scale (number of levels and component mapping)
- **Block path:** Foundations > Elevation > Elevation scale
- **Questions the designer answers:** How many elevation levels? Which components sit at which level? Does elevation change on hover, drag or scroll?
- **Options:** see table C1. Level counts: M3 6 [S-L04-003]; Fluent 6 [S-L04-006]; Polaris 7 + special [S-L04-022]; Primer 7 + inset [S-L04-024]; Atlassian 4 semantic surfaces + 3 shadows [S-L04-018].
- **Visual effect:** More levels make fine hierarchy possible but also muddy it. Most products visibly use 3: resting, raised, overlay [inferred from the Atlassian model S-L04-017].
- **Depends on (upstream):** depth strategy (DC-L04-10), component inventory (L08).
- **Affects (downstream):** z-index (DC-L04-14; the elevation level and the stacking layer should agree [inferred]), state changes (M3 raises elevated cards from level1 to level2 on hover and app bars from 0 to 2 on scroll [S-L04-069]).
- **Token encoding:** primitive `shadow.100..600` (DTCG shadow arrays); semantic `elevation.raised`, `elevation.overlay`, `elevation.dragged`; component `card.elevation.hover`. Material encodes levels as dp numbers (`level3: 6px`) and resolves them to platform shadows or tones [S-L04-003].
- **Platform notes:** Android elevation dp drives both the platform shadow and, in M3, tonal color [S-L04-058].
- **Accessibility constraints:** none directly.
- **Default + heuristic:** 4 semantic levels (sunken, default, raised, overlay) backed by 4-6 shadow primitives. Heuristic: if two components sit at the same level, they should never overlap each other [inferred].
- **Evidence:** [S-L04-003] [S-L04-006] [S-L04-017] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-058] [S-L04-069]

### DC-L04-12: Shadow recipe (layering, color, softness, dark mode)
- **Block path:** Foundations > Elevation > Shadow recipe
- **Questions the designer answers:** One shadow layer or several? Neutral black or tinted/colored shadows? Hard or soft? How do shadows look in dark mode?
- **Options:**
  - *Key + ambient (2 layers):* Fluent: a sharp directional key shadow defines edges and a soft ambient shadow conveys distance [S-L04-008].
  - *Multi-layer realistic:* Primer floating.medium uses 5 layers [S-L04-024].
  - *Negative spread:* Polaris tucks shadows under the element (for example `0 8px 16px -4px`) [S-L04-022].
  - *Tinted shadow color:* Polaris uses rgba(26,26,26) rather than pure black [S-L04-022]; Atlassian uses #1E1F21 [S-L04-018]; Fluent has separate brand shadow tokens (`shadow*Brand`) [S-L04-006]. Fully colored (hue-matched) shadows are not used by any Tier A system checked [inferred from these sources].
  - *Edge ring in shadow:* Primer floating shadows include a 1px border-color spread layer whose alpha is 0 in light mode and 1 in dark and high-contrast modes [S-L04-024]; the Atlassian dark overlay adds a 1px #BDBDBD@12% ring [S-L04-018]. Both systems add the ring exactly where soft shadows stop working.
  - *Dark mode:* higher opacity (Fluent 28% vs 14% [S-L04-008]; Primer alpha up to 1.0 [S-L04-024]) and lighter surfaces (Atlassian [S-L04-017]).
- **Visual effect:** Single hard shadows look dated or "material 2014". Layered soft shadows look realistic and premium. Tinted shadows avoid a "dirty grey" look on colored backgrounds [inferred]. Edge rings keep floating panels crisp on any background, especially in dark mode [inferred].
- **Depends on (upstream):** neutral color ramp (L01), depth strategy (DC-L04-10), theme modes (L07).
- **Affects (downstream):** all floating components; performance (large blur radii are costly to paint [inferred]).
- **Token encoding:** DTCG `shadow` array of layer objects `{color, offsetX, offsetY, blur, spread, inset?}` [S-L04-052]; the shadow color should reference a color token (`{color.shadow.key}`) so dark mode can swap it [inferred; Fluent does exactly this via colorNeutralShadowAmbient/Key S-L04-006].
- **Platform notes:** Android platform shadows come from elevation dp plus a light-source model, not arbitrary CSS layers [inferred]; iOS has CALayer shadows but Apple guidance favors materials [S-L04-032].
- **Accessibility constraints:** none directly. Shadows are decorative, so do not rely on them for boundaries that must meet 1.4.11 [inferred from S-L04-048].
- **Default + heuristic:** 2 layers (a 1px contact shadow + a soft blur scaled to elevation), neutral-tinted color, alpha 8-24% in light mode. In dark mode: double the alpha and add a 1px light edge ring for overlays.
- **Evidence:** [S-L04-006] [S-L04-008] [S-L04-017] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-032] [S-L04-048] [S-L04-052]

### DC-L04-13: Surface roles and dark-mode elevation
- **Block path:** Foundations > Elevation > Surface roles
- **Questions the designer answers:** Which named surfaces exist (page, card, raised, overlay, sunken)? Do higher surfaces get lighter in dark mode? Do hovered and pressed surfaces change color instead of elevation?
- **Options:**
  - *Atlassian:* `elevation.surface` (default), `.sunken`, `.raised`, `.overlay`, each with `.hovered` and `.pressed`, plus `.container` variants. Hover and press change color as an alternative to changing elevation [S-L04-017] [S-L04-018].
  - *Material 3:* tonal surface container roles (color lane L01) replace the older surface-tint overlays [S-L04-069].
  - *Windows:* Mica base + `LayerFillColorDefaultBrush` content layer (+ commanding layer on Mica Alt) [S-L04-012].
- **Visual effect:** Lighter-when-higher in dark mode mimics a front light source. Atlassian describes surfaces as "distantly lit from the front" [S-L04-017].
- **Depends on (upstream):** L01 neutral and dark ramps; DC-L04-10.
- **Affects (downstream):** every container component, dark theme, high-contrast themes.
- **Token encoding:** color tokens named by role (`elevation.surface.raised` is a color in Atlassian [S-L04-018]). The shadow is a separate token paired by naming convention.
- **Platform notes:** see DC-L04-10.
- **Accessibility constraints:** text on each surface must meet 4.5:1 (L01).
- **Default + heuristic:** 4 surfaces (sunken, default, raised, overlay) with 3-5% lightness steps in dark mode [inferred from the Atlassian hex steps #18191A, #1F1F21, #242528, #2B2C2F].
- **Evidence:** [S-L04-012] [S-L04-017] [S-L04-018] [S-L04-069]

### DC-L04-14: Z-index / layer scale
- **Block path:** Foundations > Elevation > Stacking layers
- **Questions the designer answers:** What named stacking layers exist, and in what order? Are values spaced to allow inserting new layers? Where do toasts, tooltips and skip links go?
- **Options:**
  - *Primer (semantic, spaced by 100):* behind -1, default 0, sticky 100, dropdown 200, overlay 300, modal 400, popover 500, skipLink 600 [S-L04-024].
  - *Polaris (numeric):* z-index-0 auto, 1 = 100, 2 = 400, 3-12 = 510-520 [S-L04-022 repo, zIndex.ts].
- **Visual effect:** None directly. It prevents bugs such as a tooltip rendering under a modal, or sticky headers hiding focus.
- **Depends on (upstream):** elevation scale (DC-L04-11), component inventory (L08).
- **Affects (downstream):** overlays, sticky headers (WCAG 2.4.11), toasts, popovers, and portals.
- **Token encoding:** DTCG `number` [S-L04-052] (Primer uses `$type: number` [S-L04-024]).
- **Platform notes:** web-specific concept; native platforms manage window/sheet stacking [inferred].
- **Accessibility constraints:** Sticky or fixed layers must not entirely hide a focused element (2.4.11 AA); mitigate with `scroll-padding` [S-L04-050]. Skip links must be topmost (Primer puts skipLink at 600) [S-L04-024].
- **Default + heuristic:** Semantic names, spaced by 100, in this order: base < sticky < dropdown < overlay/scrim < modal < popover/tooltip < toast < skip link. Never hard-code z-index in components.
- **Evidence:** [S-L04-022] [S-L04-024] [S-L04-050] [S-L04-052]

---

## Part D. Materials (translucency, blur, vibrancy)

### Comparison table D1: material systems

| Material | Platform | What it is | Where to use | Fallback / accessibility | Evidence |
|---|---|---|---|---|---|
| Liquid Glass (regular) | Apple, iOS/iPadOS/macOS/watchOS/tvOS 26+ | dynamic material that is translucent and "reflects and refracts its surroundings", with real-time specular highlights; blurs and adjusts the luminosity of what is behind it | the functional layer of controls and navigation (tab bars, sidebars, toolbars, alerts, popovers), never the content layer; content-layer sliders and toggles become glass only while being touched | adapts to Reduce Transparency and Increase Contrast, and to the user's preferred glass look | [S-L04-032] [S-L04-038] [S-L04-042] |
| Liquid Glass (clear) | Apple | highly translucent variant | over media (photos, video) | add a 35% dark dimming layer over bright content | [S-L04-032] |
| Liquid Glass, user-adjustable | Apple iOS 26.1 / iOS 27 | iOS 26.1: Settings > Display & Brightness > Liquid Glass: Clear vs Tinted (more opaque, more contrast) [S-V1b-021]. iOS 27: "more uniform refraction and improved contrast", and a slider "from ultraclear to fully tinted" | n/a | this was a response to legibility complaints (press reports); Apple's own page frames it as readability | [S-L04-039] [S-L04-041] |
| Standard materials | Apple | ultraThin, thin, regular (default), thick blur materials + vibrant label/fill/separator colors | inside the content layer | thicker = better contrast; avoid quaternary labels on thin/ultraThin | [S-L04-032] |
| Acrylic (background / in-app) | Windows (Fluent) | recipe: background, blur, exclusion blend, color/tint, noise | transient, light-dismiss surfaces (menus, flyouts); in-app acrylic for supporting panes | becomes solid when Transparency effects is off, in Battery Saver, on low-end hardware, and in High Contrast; avoid accent-colored text on acrylic | [S-L04-010] [S-L04-011] |
| Mica / Mica Alt | Windows 11 | opaque; samples the desktop wallpaper once, for performance; neutral when the window is inactive | app base layer (title bar + backdrop), once per app | solid fallback color (`SolidBackgroundFillColorBase`) | [S-L04-012] |
| Smoke | Fluent 2 | translucent black dimming layer, not mode-aware | behind modals/dialogs | n/a | [S-L04-010] |
| Web glass (`backdrop-filter`) | Web | blur/saturate what is behind a semi-transparent element | cards, navbars, overlays | Baseline since Sept 2024. `prefers-reduced-transparency` exists but is not Baseline. Ancestors with opacity<1, filter, etc. become "backdrop roots" and break the blur | [S-L04-065] [S-L04-066] |

### DC-L04-15: Use of translucent materials (glass, blur, vibrancy)
- **Block path:** Foundations > Materials > Translucency
- **Questions the designer answers:** Do we use translucent or blurred surfaces at all? On which layer (controls/navigation vs content)? How strong is the blur and tint?
- **Options:**
  - *None (opaque surfaces):* the most legible and cheapest option [inferred].
  - *Control layer only (Apple model):* glass for navigation and controls, standard materials in content, never glass in the content layer [S-L04-032].
  - *Transient surfaces only (Fluent model):* acrylic for menus and flyouts; Mica for the base [S-L04-011] [S-L04-012].
  - *Decorative glassmorphism (web trend):* translucent cards over busy backgrounds. NN/g lists legibility risks: prefer more blur, simple backgrounds, and low-opacity strokes for edges [S-L04-068].
- **Visual effect:** Translucency reads as premium, light, spatial and "OS-native" in 2025-26, and keeps context visible. The cost is lower and variable contrast. Apple's own history is the case study: iOS 26 launch, then the iOS 26.1 Tinted option, then the iOS 27 slider and contrast work [S-L04-039] [S-L04-041].
- **Depends on (upstream):** platform (L10: matching iOS 26+/macOS 26 means glass is inherent); brand (premium vs utilitarian); color (L01, contrast); performance budget.
- **Affects (downstream):** nav bars, tab bars, toolbars, sheets, menus, overlays, text color choices on surfaces (vibrant colors [S-L04-032]), scroll edge effects [S-L04-034].
- **Token encoding:** no DTCG material type [S-L04-052]. Encode as a group: `material.glass.background` (color with alpha), `material.glass.blur` (dimension), `material.glass.saturate` (number), `material.glass.border` (border composite), plus a reduced-transparency mode that swaps these for an opaque color [inferred].
- **Platform notes:** iOS: `glassEffect(_:in:)`, `.glass`/`.glassProminent` button styles, `GlassEffectContainer` [S-L04-038]. Windows: `SystemBackdrop` Mica/Acrylic [S-L04-011] [S-L04-012]. Web: `backdrop-filter` [S-L04-066].
- **Accessibility constraints:** text over glass must still meet 4.5:1 (normal text) against the worst-case background [inferred from WCAG 1.4.3; NN/g S-L04-068]. Honor Reduce Transparency (DC-L04-16).
- **Default + heuristic:** Opaque by default on web products. Use glass only for floating navigation or overlays, with at least 16-20px blur [inferred] plus a tint of about 70%+ opacity [inferred], and always with a reduced-transparency fallback. On Apple platforms, use system components and let them apply glass [S-L04-038].
- **Evidence:** [S-L04-011] [S-L04-012] [S-L04-032] [S-L04-034] [S-L04-038] [S-L04-039] [S-L04-041] [S-L04-052] [S-L04-066] [S-L04-068]

### DC-L04-16: Reduced transparency and legibility fallbacks
- **Block path:** Foundations > Materials > Accessibility fallbacks
- **Questions the designer answers:** What does each translucent surface become when the user asks for less transparency, more contrast, or battery saving? Do we add dimming layers behind clear glass?
- **Options:**
  - *OS-driven fallback:* Acrylic and Mica become solid under Transparency effects off, Battery Saver, low-end hardware, High Contrast [S-L04-011] [S-L04-012]; Apple materials adapt to Reduce Transparency and Increase Contrast [S-L04-032] [S-L04-038].
  - *Web media query:* `@media (prefers-reduced-transparency: reduce)` swaps in opaque colors. It maps to the Windows, macOS and iOS settings but is not Baseline [S-L04-065].
  - *Dimming layer:* 35% dark layer behind clear Liquid Glass over bright content [S-L04-032].
  - *User control inside the product:* NN/g suggests letting users adjust transparency [S-L04-068]; Apple now exposes a system slider [S-L04-041].
- **Visual effect:** The solid fallback looks flatter but reliably legible.
- **Depends on (upstream):** DC-L04-15, L01 contrast rules.
- **Affects (downstream):** every material token; theme modes (add a `reduced-transparency` mode) [inferred].
- **Token encoding:** a mode or theme axis in L07: `material.glass.background` = rgba(...) in the default mode and an opaque color in the `reduced-transparency` mode [inferred].
- **Platform notes:** On the web, provide the fallback by default for unsupported browsers (feature-detect `backdrop-filter`) [inferred from S-L04-066].
- **Accessibility constraints:** WCAG has no transparency criterion; contrast criteria (1.4.3, 1.4.11) are what fail [inferred].
- **Default + heuristic:** Every translucent token ships with an opaque twin. Test text contrast over white, black and a busy photo.
- **Evidence:** [S-L04-011] [S-L04-012] [S-L04-032] [S-L04-038] [S-L04-041] [S-L04-065] [S-L04-066] [S-L04-068]

---

## Part E. Opacity, overlays and scrims

### DC-L04-17: Opacity scale and state layers
- **Block path:** Foundations > Opacity > State and disabled opacity
- **Questions the designer answers:** Do we show hover, press, focus and drag with translucent overlays ("state layers") or with separate solid colors? What opacity marks disabled content? Loading content?
- **Options (real values):**
  - Material 3 state layers: hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled 0.38 [S-L04-003].
  - Atlassian: interaction overlays hovered black 16% / pressed 32% in light mode, white 20% / 36% in dark mode; `opacity.disabled` 0.4 (images); `opacity.loading` 0.2 (content under a spinner) [S-L04-070].
  - Solid state colors instead of overlays: Atlassian's `elevation.surface.hovered/pressed` are opaque hex values [S-L04-018].
- **Visual effect:** State layers tint any color consistently, so one rule works for every button color. Solid state colors give exact control and predictable contrast [inferred].
- **Depends on (upstream):** L01 color roles (state layers use the "on" color of the content), dark mode.
- **Affects (downstream):** buttons, list items, cards, chips, tabs, disabled states, skeleton loaders.
- **Token encoding:** DTCG `number` for opacity (0-1) [S-L04-052]: `opacity.state.hover = 0.08`, `opacity.disabled = 0.38`. Or bake alpha into color tokens (Atlassian `color.interaction.hovered = #00000029`) [S-L04-070].
- **Platform notes:** Android ripples use the state-layer model [inferred]. iOS mostly uses highlight dimming by the system [inferred].
- **Accessibility constraints:** Disabled content is exempt from contrast minimums (WCAG 1.4.3 exception for inactive components) [inferred, WCAG text not fetched in this lane]. Still, 0.38-0.4 opacity text is often unreadable, so pair it with other cues [inferred].
- **Default + heuristic:** Adopt Material's numbers as a baseline (0.08 / 0.10 / 0.10 / 0.16 / 0.38). In dark mode, raise overlay strength (Atlassian's dark values are higher [S-L04-070]).
- **Evidence:** [S-L04-003] [S-L04-018] [S-L04-052] [S-L04-070]

### DC-L04-18: Scrim / modal backdrop
- **Block path:** Foundations > Opacity > Scrims and overlays
- **Questions the designer answers:** What color and opacity dims content behind modals, drawers and sheets? Does it differ in dark mode? Do we blur it?
- **Options (real values):**
  - Fluent: `colorBackgroundOverlay` black 40% light / 50% dark [S-L04-071]; Smoke is "always translucent black" [S-L04-010].
  - Atlassian: `color.blanket` #050C1F at about 46% in light, #101214 at about 60% in dark [S-L04-070].
  - Material 3 token export: the old drawer `scrim.opacity 0.4` is deprecated with the note "Use Neutral-Variant10 at 50% for scrims instead" [S-L04-069].
  - Apple: dimming layer of 35% for clear glass [S-L04-032]; system sheets manage their own dimming [inferred].
- **Visual effect:** Darker scrims focus attention hard (modal, blocking). Lighter scrims keep context (non-blocking sheets). A blue-black tint (Atlassian) looks warmer or more on-brand than pure black [inferred].
- **Depends on (upstream):** L01 neutrals and dark mode; depth strategy.
- **Affects (downstream):** dialogs, drawers, bottom sheets, lightboxes, onboarding spotlights.
- **Token encoding:** color token with alpha (`color.scrim` / `color.blanket`) or a color + `opacity.scrim` number pair [S-L04-052].
- **Platform notes:** Android M3 uses the scrim color role (L01) [inferred]; Windows uses Smoke [S-L04-010].
- **Accessibility constraints:** The scrim must not make the modal itself low-contrast; semi-transparent overlays that partly cover focused items can still fail contrast (2.4.11 notes) [S-L04-050].
- **Default + heuristic:** 40-50% near-black in light mode and 50-60% in dark mode, tinted toward the neutral hue.
- **Evidence:** [S-L04-010] [S-L04-032] [S-L04-050] [S-L04-052] [S-L04-069] [S-L04-070] [S-L04-071]

---

## Part F. Motion

### Comparison table F1: duration tokens (ms)

| System | Tokens and values | Evidence |
|---|---|---|
| Material 3 | short1 50, short2 100, short3 150, short4 200; medium1 250, medium2 300, medium3 350, medium4 400; long1 450, long2 500, long3 550, long4 600; extra-long1 700, extra-long2 800, extra-long3 900, extra-long4 1000. Rule: "duration should increase as the area/traversal of an animation increases" | [S-L04-003] [S-L04-064] |
| IBM Carbon | fast-01 70 (button, toggle); fast-02 110 (fade); moderate-01 150 (small expansion, short moves, default); moderate-02 240 (expansion, toast); slow-01 400 (large expansion, important notifications); slow-02 700 (background dimming, hero transitions). Non-linear scale; productive is "significantly faster" than expressive | [S-L04-014] [S-L04-075] |
| Fluent 2 (web) | ultraFast 50, faster 100, fast 150, normal 200, gentle 250, slow 300, slower 400, ultraSlow 500 | [S-L04-006] |
| Windows / WinUI 3 | ControlFasterAnimationDuration 83, ControlFastAnimationDuration 167, ControlNormalAnimationDuration 250 | [S-L04-013] |
| Atlassian | instant 0, xxshort 50, xshort 100, short 150, medium 200, long 250, xlong 400, xxlong 600. Component composites: modal enter 250 / exit 200; popup enter 150 / exit 100; flag enter 250 / exit 200; list item hover 50 | [S-L04-018] |
| Shopify Polaris | 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 5000 | [S-L04-022] |
| GitHub Primer | base 0, 50, 100, 200 ... 1000; semantic micro 100 (hover, focus, color), short 200 (toggles, expand/collapse), medium 300 (modals, dropdowns entering), long 500 (complex, large layout shifts) | [S-L04-024] |
| Apple (SwiftUI) | no duration tokens. Springs are parameterized by perceptual duration: `Spring(duration: 0.5, bounce: 0)` default; `.smooth` / `.snappy` / `.bouncy` default duration 0.5s; `Animation.default` = spring response 0.55, damping 1.0 (iOS 17+) | [S-L04-037] |

Pattern [inferred]: every system packs most tokens into 50-400ms. Micro-interactions sit at 50-150ms, component enter/exit at 150-300ms, and large or full-screen moves at 300-700ms. Carbon's 70/110/240 values are deliberately off the round-number grid, which reflects its non-linear duration model [S-L04-075].

### Comparison table F2: easing curves (cubic-bezier x1, y1, x2, y2)

| System | Standard / move | Enter (decelerate) | Exit (accelerate) | Other | Evidence |
|---|---|---|---|---|---|
| Material 3 | standard (0.2, 0, 0, 1) | standard-decelerate (0, 0, 0, 1); emphasized-decelerate (0.05, 0.7, 0.1, 1) | standard-accelerate (0.3, 0, 1, 1); emphasized-accelerate (0.3, 0, 0.8, 0.15) | **emphasized is a 2-segment path** `M 0,0 C 0.05,0 0.133333,0.06 0.166666,0.4 C 0.208333,0.82 0.25,1 1,1`, which cannot be a single cubic-bezier. The token export falls back to `easing-emphasized: $easing-standard`. legacy (0.4, 0, 0.2, 1); linear | [S-L04-003] [S-L04-064] |
| Carbon productive | (0.2, 0, 0.38, 0.9) | (0, 0, 0.38, 0.9) | (0.2, 0, 1, 0.9) | subtle, efficient | [S-L04-014] [S-L04-075] |
| Carbon expressive | (0.4, 0.14, 0.3, 1) | (0, 0, 0.3, 1) | (0.4, 0.14, 1, 1) | vibrant, for important moments | [S-L04-014] [S-L04-075] |
| Fluent 2 (web) | easyEase (0.33, 0, 0.67, 1); easyEaseMax (0.8, 0, 0.2, 1) | decelerateMax (0.1, 0.9, 0.2, 1); decelerateMid (0, 0, 0, 1); decelerateMin (0.33, 0, 0.1, 1) | accelerateMax (0.9, 0.1, 1, 0.2); accelerateMid (1, 0, 1, 1); accelerateMin (0.8, 0, 0.78, 1) | linear (0, 0, 1, 1) | [S-L04-006] |
| Windows | n/a | "Fast Out, Slow In" (0, 0, 0, 1) | "Slow Out, Fast In" (1, 0, 1, 1) | n/a | [S-L04-013] |
| Atlassian | inout.bold (0.4, 0, 0, 1) | out.practical (0.4, 1, 0.6, 1); out.bold (0, 0.4, 0, 1) | in.practical (0.6, 0, 0.8, 0.6) | **spring as CSS `linear()`** (experimental) | [S-L04-018] |
| Polaris | ease (0.25, 0.1, 0.25, 1), the default for interactions; ease-in-out (0.42, 0, 0.58, 1) for system-triggered | ease-out (0.19, 0.91, 0.38, 1) "use sparingly" | ease-in (0.42, 0, 1, 1) "use sparingly" | linear for spinners | [S-L04-022] |
| Primer | hover = ease (0.25, 0.1, 0.25, 1); move = easeInOut (0.6, 0, 0.2, 1) | enter = easeOut (0.3, 0.8, 0.6, 1) | exit = easeIn (0.7, 0.1, 0.75, 0.9) | linear for progress | [S-L04-024] |

### Comparison table F3: springs

| System | Parameterization | Values | Evidence |
|---|---|---|---|
| Material 3, **standard** scheme | damping ratio + stiffness; 3 speeds x 2 types | spatial: fast 0.9/1400, default 0.9/700, slow 0.9/300. effects: fast 1.0/3800, default 1.0/1600, slow 1.0/800 | [S-L04-003] [S-L04-004] [S-L04-064] |
| Material 3, **expressive** scheme | same | spatial: fast 0.6/800, default 0.8/380, slow 0.8/200. effects: identical to standard (critically damped) | [S-L04-004] |
| Apple SwiftUI | perceptual `duration` + `bounce` (-1..1; 0 = critically damped; >0 bouncy; <0 overdamped), or mass/stiffness/damping | `Spring(duration: 0.5, bounce: 0)`; presets `.smooth` (no bounce), `.snappy` (small bounce), `.bouncy` (higher bounce); default animation = response 0.55 s, dampingFraction 1.0 | [S-L04-037] |
| Atlassian | spring sampled into CSS `linear(...)` points, with a duration | avatar hover 250ms with slight overshoot, marked experimental | [S-L04-018] |

Conversion note [inferred, standard spring physics, mass = 1]: Apple's response or duration is roughly 2π/√stiffness, and bounce is roughly 1 - damping ratio. So M3 standard default spatial (k=700, ζ=0.9) is about 237ms with bounce 0.1. M3 expressive default spatial (k=380, ζ=0.8) is about 322ms with bounce 0.2. M3 expressive fast spatial (k=800, ζ=0.6) is about 222ms with bounce 0.4. Effects springs (ζ=1) never overshoot. A builder can store springs in one form and emit the other per platform.

### DC-L04-19: Motion personality (productive vs expressive; snappy vs bouncy)
- **Block path:** Foundations > Motion > Motion personality
- **Questions the designer answers:** Should motion feel efficient and invisible, or lively and branded? Do we allow overshoot (bounce)? Is there one style or two (utility vs hero)?
- **Options:**
  - *Two-mode system (utility + hero):* Carbon productive vs expressive. Productive is for task focus (button states, dropdowns, data tables); expressive is for "significant moments" (new page, primary action, alerts) [S-L04-075]. Material standard vs expressive motion schemes: standard for "utilitarian UI elements and recurring interactions", expressive for "prominent UI elements and hero interactions" [S-L04-060].
  - *Single restrained style:* Primer and Polaris (CSS-style eases, no springs) [S-L04-022] [S-L04-024].
  - *Physics-first:* Apple springs everywhere (default animation is a spring since iOS 17) [S-L04-037]; M3 Expressive physics system [S-L04-004] [S-L04-064].
  - *Playful accents only:* Atlassian limits its overshoot spring to "small branded elements such as avatar hover" [S-L04-018].
- **Visual effect:** Productive/snappy (short durations, strong ease-out, no overshoot) reads as fast, competent, professional. Expressive/bouncy (longer durations, overshoot, damping below 1) reads as energetic, playful, friendly [S-L04-063 for the "energetic/playful" association of expressive design overall; the motion-only attribution is inferred]. Too much bounce in frequent interactions feels slow and gimmicky; Apple advises avoiding motion on frequent interactions [S-L04-033].
- **Depends on (upstream):** brand personality (L06), shape personality (DC-L04-02), audience and domain (banking needs restraint [S-L04-063]), platform (L10).
- **Affects (downstream):** duration scale (DC-L04-20), easing set (DC-L04-21), springs (DC-L04-22), choreography (DC-L04-23), haptic intensity pairing (DC-L04-26).
- **Token encoding:** a mode or theme axis `motion-scheme: standard | expressive` that swaps semantic motion aliases, as M3 does with `MotionScheme.standard()` / `.expressive()` [S-L04-060] and Carbon with the `productive` / `expressive` easing modes [S-L04-014].
- **Platform notes:** iOS: system components already carry Apple's physics, and Liquid Glass motion is stronger with touch than with a trackpad [S-L04-033]. Android: M3 components read the theme's MotionScheme [S-L04-060].
- **Accessibility constraints:** Overshoot and large spatial motion fall under reduced-motion handling (DC-L04-25).
- **Default + heuristic:** Two modes: productive for 90% of interactions, expressive for 1-3 hero moments per flow. Keep bounce at or below 0.2 (damping ratio 0.8 or higher) except for playful brands [inferred from the M3 expressive default of 0.8].
- **Evidence:** [S-L04-004] [S-L04-014] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-033] [S-L04-037] [S-L04-060] [S-L04-063] [S-L04-064] [S-L04-075]

### DC-L04-20: Duration scale
- **Block path:** Foundations > Motion > Duration scale
- **Questions the designer answers:** How many duration steps? What is the fastest and slowest? Do durations scale with distance and size? Are exits faster than entrances?
- **Options:** table F1. Granularity ranges from 4 semantic steps (Primer micro/short/medium/long [S-L04-024]) to 16 steps (M3 [S-L04-003]). Carbon uses 6 non-linear steps [S-L04-014].
- **Visual effect:** Shorter reads as snappier and more responsive; longer reads as smoother and more cinematic, but past about 500ms UI starts to feel sluggish [inferred; Carbon caps staggered sequences at 500ms total S-L04-075].
- **Depends on (upstream):** motion personality (DC-L04-19), component size and travel distance (M3 and Carbon both scale duration with area or distance [S-L04-064] [S-L04-075]).
- **Affects (downstream):** all transitions, component motion specs (Atlassian modal 250 in / 200 out [S-L04-018]).
- **Token encoding:** DTCG `duration` with `{"value": 200, "unit": "ms"}` [S-L04-052]. Carbon's DTCG motion file uses exactly this form [S-L04-014]. Primitive `duration.200`; semantic `motion.duration.short`; component `modal.enter.duration`.
- **Platform notes:** On iOS, prefer springs with a perceptual duration over fixed-duration curves [S-L04-037]. WinUI uses 83/167/250ms control defaults [S-L04-013].
- **Accessibility constraints:** WCAG 2.2.2 Pause, Stop, Hide covers auto-moving content lasting more than 5s [inferred, SC text not fetched in this lane]; see DC-L04-25.
- **Default + heuristic:** 6 semantic steps: instant 0, micro 100, short 150-200, medium 250-300, long 400-500, extra 700 (full-screen and dimming). Make exits about 20-35% shorter than entrances (Atlassian 250 vs 200, popup 150 vs 100 [S-L04-018]; Primer enter medium 300 vs exit short 200 [S-L04-024]).
- **Evidence:** [S-L04-003] [S-L04-013] [S-L04-014] [S-L04-018] [S-L04-024] [S-L04-037] [S-L04-052] [S-L04-064] [S-L04-075]

### DC-L04-21: Easing set
- **Block path:** Foundations > Motion > Easing curves
- **Questions the designer answers:** Which curves exist (standard, enter, exit, emphasized)? How aggressive is the deceleration? Is linear allowed?
- **Options:** table F2. Structures seen: *role-based* (standard/enter/exit: Carbon, Primer, Windows) [S-L04-014] [S-L04-024] [S-L04-013]; *intensity-based* (min/mid/max: Fluent) [S-L04-006]; *personality-based* (practical vs bold: Atlassian; productive vs expressive: Carbon) [S-L04-018] [S-L04-014]; *CSS keyword clones* (Polaris, Primer's ease) [S-L04-022] [S-L04-024].
- **Visual effect:** Strong decelerate curves (M3 emphasized-decelerate 0.05, 0.7, 0.1, 1; Windows 0, 0, 0, 1) make entrances feel fast and "arriving from far away" [S-L04-013]. Accelerate curves make exits get "out of the user's way" [S-L04-013]. Symmetric ease-in-out feels calm and mechanical [inferred].
- **Depends on (upstream):** motion personality (DC-L04-19).
- **Affects (downstream):** transitions (DC-L04-23), component motion composites.
- **Token encoding:** DTCG `cubicBezier` `[x1, y1, x2, y2]` with x in [0, 1] [S-L04-052]. Curves that are not a single cubic (M3 emphasized path; springs) cannot be encoded natively: M3's own export degrades emphasized to standard [S-L04-003]. Use CSS `linear()` sampling (Atlassian [S-L04-018]) or `$extensions`.
- **Platform notes:** Android interpolators can be paths [S-L04-064]; iOS prefers springs [S-L04-037]; the web supports `cubic-bezier()` and `linear()` [inferred; Atlassian ships `linear()` values S-L04-018].
- **Accessibility constraints:** none directly.
- **Default + heuristic:** 4 curves: standard (0.2, 0, 0, 1), enter/decelerate (0, 0, 0, 1) or (0.05, 0.7, 0.1, 1), exit/accelerate (0.3, 0, 1, 1), linear (only for spinners and progress). Polaris and Primer both reserve linear for continuous or mechanical motion [S-L04-022] [S-L04-024].
- **Evidence:** [S-L04-003] [S-L04-006] [S-L04-013] [S-L04-014] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-037] [S-L04-052] [S-L04-064]

### DC-L04-22: Springs vs duration-based motion
- **Block path:** Foundations > Motion > Physics (springs)
- **Questions the designer answers:** Do we animate with springs (physics) or with fixed duration + easing? Do we separate "spatial" (position, size, shape) from "effects" (color, opacity) motion? How are springs specified?
- **Options:**
  - *Duration + easing only:* Carbon, Fluent, Polaris, Primer [S-L04-006] [S-L04-014] [S-L04-022] [S-L04-024].
  - *Springs with spatial/effects split:* M3 (spatial springs for bounds and shape; effects springs, critically damped, for color and alpha) [S-L04-060] [S-L04-064]. MDC guidance: fast for small components (switches, buttons), default for partial-screen (bottom sheet, nav drawer), slow for full-screen; a pressed button uses fast-spatial for shape plus fast-effects for color [S-L04-064].
  - *Springs with perceptual parameters:* Apple duration + bounce [S-L04-037].
  - *Spring baked into an easing:* Atlassian `linear()` [S-L04-018].
- **Visual effect:** Springs feel natural, keep velocity when interrupted, and settle organically. Duration curves feel precise and predictable [inferred; Apple spring docs note velocity is preserved when springs are replaced S-L04-037].
- **Depends on (upstream):** DC-L04-19; platform animation runtimes (L10).
- **Affects (downstream):** interruptibility (DC-L04-24), gesture-driven UI, shape morphing (DC-L04-06).
- **Token encoding:** DTCG 2025.10 has **no spring type** [S-L04-052] (and none in the Sept 2026 draft [S-L04-051]). Options: (a) a group of `number` tokens `motion.spring.default-spatial.damping = 0.9`, `.stiffness = 700`; the M3 export does exactly this and marks the composite as an unsupported "custom_composite" [S-L04-003]. (b) `$extensions` on a transition token, e.g. `{"com.example.spring": {"dampingRatio": 0.9, "stiffness": 700}}`. (c) pre-sampled `linear()` string + duration for the web [S-L04-018].
- **Platform notes:** Compose `spring(dampingRatio, stiffness)` [S-L04-060]; Android Views use the AndroidX DynamicAnimation library with MaterialSpring theme attributes [S-L04-064]; SwiftUI `Spring(duration:bounce:)` [S-L04-037]; web needs a JS spring library or `linear()` [inferred].
- **Accessibility constraints:** Reduced motion should remove bounce and large spatial travel (DC-L04-25).
- **Default + heuristic:** Store springs as (dampingRatio, stiffness) plus a derived (duration, bounce) for Apple, with pre-sampled `linear()` for CSS. Use critically damped springs for effects, and underdamped ones only for spatial hero motion.
- **Evidence:** [S-L04-003] [S-L04-006] [S-L04-014] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-037] [S-L04-051] [S-L04-052] [S-L04-060] [S-L04-064]

### DC-L04-23: Choreography and transition patterns
- **Block path:** Patterns > Motion > Transitions and choreography
- **Questions the designer answers:** Which named transition patterns do we support? How do we stagger lists? What moves first? Which axis do navigations use?
- **Options:**
  - *Material's four patterns:* container transform (for transitions between elements that include a container; creates a visible connection); shared axis (x, y or z for spatial or navigational relationships: onboarding x, stepper y, parent-child z); fade through (unrelated destinations, such as bottom-nav tabs; Fade + Scale); fade (in-screen enter/exit such as dialogs, menus, snackbars, FAB; Fade + Scale) [S-L04-064].
  - *Carbon "surfaces" (2026):* named DTCG `transition` composites: disclosure (accordion, table-row expand; moderate-01 + entrance productive), contextual (icon to tooltip/popover; fast-02, entrance expressive, scale 0.96 to 1), expand (card to side panel; moderate-02, standard productive, shared element), invoke (button to modal/menu; shared element from the trigger, moderate-02, standard expressive) [S-L04-014].
  - *Carbon choreography rules:* paths follow the grid and never run diagonally; same meaning means same motion; reversed motion signals cancel; stagger table content by 20ms and keep the total within 500ms [S-L04-075].
  - *Fluent:* stagger with short offsets; important elements get more prominent motion and longer durations [S-L04-009].
  - *Atlassian component motion tokens:* popup enter slides 8px + fades in 150ms and exits 4px in 100ms; modal scales 95% to 100% in 250ms; flag slides in from 50% [S-L04-018].
  - *Apple:* buttons morph into menus and popovers; realistic, gesture-following feedback; fades when relocating objects in visionOS [S-L04-033] [S-L04-038].
- **Visual effect:** Consistent patterns make navigation legible (you can "feel" whether you went deeper or sideways). Stagger reduces cognitive load in lists [S-L04-075].
- **Depends on (upstream):** navigation model (L08 patterns), DC-L04-20/21/22.
- **Affects (downstream):** page transitions, dialogs, menus, lists, cards, the View Transitions API on the web [inferred].
- **Token encoding:** DTCG `transition` composite `{duration, delay, timingFunction}` for each pattern [S-L04-052]; Carbon stores extra keyframe data (`enter`/`exit` properties, `kind: reveal | shared-element`) in `$extensions["carbon.motion"]` [S-L04-014]. Primer ships `motion.transition.hover/stateChange/enter/exit` [S-L04-024].
- **Platform notes:** Android has transition classes for all four Material patterns [S-L04-064]; iOS uses system transitions and matched geometry [inferred]; web uses View Transitions or FLIP [inferred].
- **Accessibility constraints:** Shared-axis and container-transform are spatial motion, so reduced motion should swap them for a fade [inferred from S-L04-049 and S-L04-067].
- **Default + heuristic:** Ship 4 named transitions (fade, fade-through, shared-axis, container-transform or "invoke") + a stagger token (20-50ms, total at most 500ms).
- **Evidence:** [S-L04-009] [S-L04-014] [S-L04-018] [S-L04-024] [S-L04-033] [S-L04-038] [S-L04-049] [S-L04-052] [S-L04-064] [S-L04-067] [S-L04-075]

### DC-L04-24: Enter/exit asymmetry and interruptibility
- **Block path:** Foundations > Motion > Interruptibility
- **Questions the designer answers:** Can users act before an animation ends? Can animations reverse mid-flight? Are exits faster than entrances?
- **Options:**
  - *Interruptible (retargeting):* Apple: "Let people cancel motion... don't make people wait for an animation to complete" [S-L04-033]; springs preserve velocity when replaced [S-L04-037].
  - *Asymmetric durations:* Atlassian exits are shorter (modal 250/200, popup 150/100, panel content 150/50) [S-L04-018]; Primer exit short 200 vs enter medium 300 [S-L04-024].
  - *Asymmetric curves:* enter decelerate, exit accelerate (Windows, Carbon, Primer) [S-L04-013] [S-L04-014] [S-L04-024].
- **Visual effect:** Interruptible, fast-exit motion feels responsive and respectful of the user's time; blocking motion feels sluggish [inferred].
- **Depends on (upstream):** DC-L04-22 (springs make retargeting easy).
- **Affects (downstream):** gestures, sheets, drawers, menus, rapid toggles.
- **Token encoding:** separate `enter` / `exit` transition tokens (Atlassian `motion.modal.enter` / `.exit` [S-L04-018]).
- **Platform notes:** SwiftUI springs retarget natively [S-L04-037]; CSS transitions reverse from their current value, while CSS keyframe animations do not [inferred].
- **Accessibility constraints:** none beyond reduced motion.
- **Default + heuristic:** Exit is about 70-80% of the enter duration and uses the accelerate curve. Never block input during a transition longer than about 100ms [inferred].
- **Evidence:** [S-L04-013] [S-L04-014] [S-L04-018] [S-L04-024] [S-L04-033] [S-L04-037]

### DC-L04-25: Reduced-motion policy
- **Block path:** Foundations > Motion > Accessibility (reduced motion)
- **Questions the designer answers:** What happens when the user turns on Reduce Motion? Do we remove motion or replace it? Which animations are "essential"? Do we offer an in-app setting?
- **Options:**
  - *Replace spatial motion with gentler effects:* MDN recommends reducing rather than removing: swap scale/pan for opacity or color [S-L04-067]. WCAG's definition of motion animation excludes color, blur and opacity changes [S-L04-049].
  - *Remove non-essential motion entirely:* WCAG 2.3.3 Animation from Interactions (AAA): motion triggered by interaction can be disabled unless essential; technique C39 = `prefers-reduced-motion` [S-L04-049].
  - *In-app "no motion" setting:* Fluent recommends it [S-L04-009]; Apple: make motion optional and pair it with haptics and audio [S-L04-033].
  - *Static alternatives always:* Carbon [S-L04-075].
- **Visual effect:** A well-designed reduced mode still feels polished (crossfades) rather than broken (jumps) [inferred].
- **Depends on (upstream):** all motion decisions.
- **Affects (downstream):** transitions (swap shared-axis for fade), springs (bounce to 0), parallax and auto-play (off), shape morphs (instant), Liquid Glass morphing (system-handled [S-L04-038]).
- **Token encoding:** a `reduced-motion` mode in the motion collection: durations to 0 or short fades, spatial springs to critically damped, `transition.*` aliases to the fade variants [inferred]. Web: `@media (prefers-reduced-motion: reduce)` [S-L04-067].
- **Platform notes:** OS settings: iOS Settings > Accessibility > Motion; macOS 26 Accessibility > Motion; Windows 11 Animation effects; Android 9+ Remove animations; GNOME and KDE equivalents; widely supported on the web since January 2020 [S-L04-067].
- **Accessibility constraints:** WCAG 2.3.3 (AAA) [S-L04-049]; vestibular triggers are scaling and panning of large objects [S-L04-067]; Apple visionOS: avoid sustained oscillation around 0.2 Hz and peripheral motion [S-L04-033].
- **Default + heuristic:** Treat 2.3.3 as a requirement even though it is AAA. Build the reduced mode as a token mode, not per-component code. Keep feedback (color, opacity) and remove travel (translate, scale, parallax).
- **Evidence:** [S-L04-009] [S-L04-033] [S-L04-038] [S-L04-049] [S-L04-067] [S-L04-075]

---

## Part G. Sound and haptics

### Comparison table G1: platform haptic vocabularies

| Platform | API | Semantic types | Evidence |
|---|---|---|---|
| iOS (UIKit) | `UIFeedbackGenerator` subclasses | Impact: light, medium, heavy, rigid, soft ("mass of the objects in the collision"). Selection. Notification: success, warning, error. Canvas feedback (drawing) | [S-L04-044] |
| iOS/macOS/watchOS (SwiftUI 17+) | `SensoryFeedback` (haptic and/or audio) | start, stop; alignment, decrease, increase, levelChange, selection, pathComplete; success, warning, error; impact, impact(weight:intensity:), impact(flexibility:intensity:); press/release | [S-L04-044] |
| macOS trackpad | `NSHapticFeedbackPerformer` | alignment, level change, generic | [S-L04-043] |
| watchOS | `WKHapticType` | notification, up, down, success, failure, retry, start, stop, click | [S-L04-043] |
| Custom (Apple) | Core Haptics | transient vs continuous events, each with intensity and sharpness; optional synced audio | [S-L04-043] |
| Android | `View.performHapticFeedback(HapticFeedbackConstants.*)` | CONFIRM, REJECT, GESTURE_START/END (API 30); TOGGLE_ON/OFF, SEGMENT_TICK, SEGMENT_FREQUENT_TICK, GESTURE_THRESHOLD_ACTIVATE/DEACTIVATE, DRAG_START, NO_HAPTICS (API 34); KEYBOARD_TAP (8), LONG_PRESS (3), VIRTUAL_KEY (5), VIRTUAL_KEY_RELEASE / KEYBOARD_PRESS / KEYBOARD_RELEASE / TEXT_HANDLE_MOVE (27), CLOCK_TICK (21), CONTEXT_CLICK (23) | [S-L04-047] |

Finding: none of the web design-system token packages inspected in this lane (Material Web sys tokens, Fluent global tokens, Atlassian tokens-raw, Primer functional tokens, Carbon motion, Polaris base tokens) defines haptic or sound tokens [S-L04-003] [S-L04-006] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-014]. Haptic vocabularies live in the platform APIs, which are semantic in themselves ("success", "selection", "toggle on").

### DC-L04-26: Haptic feedback vocabulary
- **Block path:** Foundations > Haptics > Semantic haptic map
- **Questions the designer answers:** Does the product use haptics at all? Which events get which haptic? How strong? Can users turn them off?
- **Options:**
  - *System-only:* rely on standard controls (toggles, sliders, pickers), which already play Apple-designed haptics [S-L04-043].
  - *Semantic map to platform types:* success/warning/error to UINotification or CONFIRM/REJECT; selection change to UISelection or SEGMENT_TICK; toggle to TOGGLE_ON/OFF; snap or collision to UIImpact (light to heavy) [S-L04-044] [S-L04-047].
  - *Custom patterns:* Core Haptics or VibrationEffect primitives, mostly for games or brand moments; provide fallbacks, since fewer Android devices support "rich" haptics [S-L04-043] [S-L04-046].
- **Visual effect (felt effect):** Crisp, short "clear" haptics feel precise and premium. "Buzzy" long vibrations feel cheap and dated; Android says to avoid them and use no haptic instead [S-L04-046]. Matching haptic sharpness and intensity to the animation makes the UI feel physical [S-L04-043].
- **Depends on (upstream):** motion personality (DC-L04-19; pair intensity with motion intensity [S-L04-043]), platform (mobile only in practice).
- **Affects (downstream):** toggles, pull-to-refresh thresholds, pickers, drag and drop, form submission outcomes, destructive confirmations.
- **Token encoding:** no DTCG type [S-L04-052]. Encode as `string` enum tokens with per-platform `$extensions`, e.g. `haptic.feedback.success = "success"` → iOS `.success`, Android `CONFIRM` [inferred]. Keep it semantic; never store raw vibration durations.
- **Platform notes:** Android `performHapticFeedback` respects the user's touch-feedback setting and needs no VIBRATE permission; `VibrationEffect` needs the permission [S-L04-045]. Keyclick haptics should be 10-20ms [S-L04-046]. Web: no equivalent in the sources checked [gap].
- **Accessibility constraints:** Make haptics optional; never use them as the only channel (Apple) [S-L04-043]. Apple also recommends haptics and audio as alternatives when motion is reduced [S-L04-033].
- **Default + heuristic:** Map at most about 6 semantic events (success, warning, error, selection, toggle, impact-light). Use them sparingly: "less is more" [S-L04-046]; "the best haptic experience is one that people may not be conscious of, but miss when it's turned off" [S-L04-043].
- **Evidence:** [S-L04-033] [S-L04-043] [S-L04-044] [S-L04-045] [S-L04-046] [S-L04-047] [S-L04-052]

### DC-L04-27: Sound / UI audio (earcons)
- **Block path:** Foundations > Sound > UI sounds
- **Questions the designer answers:** Does the product make UI sounds? Which events? Do sounds respect silent mode and system volume? Do we pair sound with haptics?
- **Options:**
  - *Silent by default:* tvOS plays no sounds for alerts or notifications [S-L04-074]; most web design systems ship no sound tokens [finding in G1].
  - *Nonessential sounds that honor silent mode:* in silent mode, iOS users expect keyboard clicks, sound effects and other audible feedback to be silenced; system volume always governs [S-L04-074].
  - *Sound-forward (spatial computing, games):* visionOS says "prefer playing sound", design custom sounds for custom elements, and vary repetitive sounds by randomizing pitch and volume [S-L04-074].
  - *Synced audio + haptics:* Core Haptics and SensoryFeedback can pair audio with haptics [S-L04-043] [S-L04-044].
- **Visual effect (heard effect):** Sound adds delight and confirmation but can annoy in shared spaces; repeated identical sounds feel mechanical [S-L04-074].
- **Depends on (upstream):** brand (sonic identity, L06), platform, context of use.
- **Affects (downstream):** notifications, success moments, onboarding, games, voice UIs.
- **Token encoding:** asset tokens (a file reference string) + volume `number`; no DTCG type [S-L04-052] [inferred].
- **Platform notes:** choose the right iOS audio session category (ambient vs playback, etc.) so the app respects the silent switch and mixing [S-L04-074].
- **Accessibility constraints:** Never convey important information only through sound [S-L04-074].
- **Default + heuristic:** No UI sounds on web and productivity apps. Add sounds only for rare, meaningful events on mobile, games or spatial platforms, always behind a mute option.
- **Gap:** Material Design's sound guidance (M2 era) could not be retrieved (JS-only and archived pages) [S-L04-072].
- **Evidence:** [S-L04-043] [S-L04-044] [S-L04-052] [S-L04-072] [S-L04-074]

---

## Part H. Token encoding for this lane

### DC-L04-28: Encoding shape, depth and motion tokens (DTCG types, gaps, naming)
- **Block path:** Tokens > Types > Shape, elevation, motion
- **Questions the designer answers:** Which DTCG type does each decision map to? How do we encode things the spec lacks (springs, materials, corner smoothing, haptics)? How do we name them across tiers?
- **Options: DTCG 2025.10 (stable, 28 Oct 2025) native types relevant to L04 [S-L04-052]:**
  - `dimension` `{"value": 8, "unit": "px"}` (px or rem): radius, border width, blur radius, offsets.
  - `number`: opacity, z-index, spring damping and stiffness.
  - `duration` `{"value": 200, "unit": "ms"}` (ms or s).
  - `cubicBezier` `[x1, y1, x2, y2]`, x within [0, 1].
  - `strokeStyle`: `"solid" | "dashed" | "dotted" | "double" | "groove" | "ridge" | "outset" | "inset"` or `{dashArray, lineCap}`.
  - `border` `{color, width, style}`.
  - `transition` `{duration, delay, timingFunction}`.
  - `shadow`: one object or an array of layers `{color, offsetX, offsetY, blur, spread, inset?}`; array items may be references.
  - `$extensions` (reverse-domain keys; tools must preserve unknown data) and `$deprecated`.
- **Not in the spec (and how real systems cope):**
  - *Springs:* none in 2025.10 or the Sept 2026 draft [S-L04-051] [S-L04-052]. M3 exports springs as separate damping and stiffness numbers and marks the composite "custom_composite ... not supported" [S-L04-003]. Atlassian pre-samples its spring into a CSS `linear()` string [S-L04-018].
  - *Non-cubic easing (paths):* M3 emphasized is a 2-segment path; its export collapses it to standard [S-L04-003] [S-L04-064].
  - *Motion recipes with keyframes:* Carbon puts `kind`, `enter`/`exit` keyframes and easing names in `$extensions["carbon.motion"]` alongside a valid `transition` `$value` [S-L04-014]. Atlassian bundles duration + curve + keyframes + fill into one object value (not DTCG-typed) [S-L04-018].
  - *Materials / blur, corner smoothing, shapes, haptics, sounds:* no types; use groups of primitives + `$extensions` [inferred].
- **Naming patterns observed:**
  - Radius: `radius.medium` (Atlassian), `borderRadius.default` (Primer), `border-radius-08` (Carbon), `md.sys.shape.corner.medium` (Material), `borderRadiusMedium` (Fluent) [S-L04-003] [S-L04-006] [S-L04-018] [S-L04-024] [S-L04-030].
  - Elevation: `md.sys.elevation.level3`, `elevation.surface.raised` + `elevation.shadow.raised`, `shadow-400`, `shadow.floating.large`, `shadow16` [S-L04-003] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-006].
  - Motion: `md.sys.motion.duration.medium2`, `duration.moderate.02` (Carbon DTCG path), `motion.duration.medium`, `motion.easing.out.practical`, `motion.transition.enter` (Primer), `durationNormal` / `curveDecelerateMid` (Fluent) [S-L04-003] [S-L04-014] [S-L04-018] [S-L04-024] [S-L04-006].
- **Visual effect:** none directly; encoding determines whether the builder can round-trip decisions to Figma, CSS, Compose and SwiftUI without loss.
- **Depends on (upstream):** L07 token architecture (tiers, modes), every L04 decision above.
- **Affects (downstream):** exporters (CSS, Compose, SwiftUI, Figma variables), documentation, linting.
- **Token encoding (recommended tiering):**
  - Primitive: `radius.4`, `shadow.200`, `duration.200`, `easing.decelerate`, `spring.default-spatial` (number group).
  - Semantic: `radius.control`, `elevation.overlay`, `motion.duration.short`, `motion.transition.enter`.
  - Component: `button.radius`, `menu.shadow`, `modal.motion.enter`.
  - Modes: `shape: crisp | soft | round`; `motion: standard | expressive | reduced`; `transparency: default | reduced`; `color-scheme: light | dark` (dark swaps shadow colors and scrim alpha) [inferred, consistent with S-L04-018, S-L04-060, S-L04-065].
- **Platform notes:** Figma variables cannot hold shadow composites or cubic-beziers as variables (they are "effect styles" and prototype settings) [inferred, L07 should verify against help.figma.com]. Carbon and Primer already author motion and shape tokens in DTCG JSON [S-L04-014] [S-L04-024] [S-L04-030].
- **Accessibility constraints:** reduced-motion and reduced-transparency should be modes, not ad-hoc overrides [inferred].
- **Default + heuristic:** Author in DTCG 2025.10. For springs, store `{dampingRatio, stiffness}` numbers in `$extensions` on a `transition` token whose `$value` is a cubic-bezier fallback. Generate `linear()` for CSS and `(duration, bounce)` for SwiftUI in the build step.
- **Evidence:** [S-L04-003] [S-L04-006] [S-L04-014] [S-L04-018] [S-L04-022] [S-L04-024] [S-L04-030] [S-L04-051] [S-L04-052] [S-L04-060] [S-L04-064] [S-L04-065]

---

## Decision graph for L04 (what drives what)

Upstream inputs (from other lanes), then L04 decisions, then downstream effects. Tags refer to the cards above.

- **Brand personality (L06)** drives DC-L04-02 shape personality, DC-L04-19 motion personality, DC-L04-10 depth strategy, DC-L04-15 materials, and DC-L04-27 sound. [inferred linkage; the evidence for each option is in the cards]
- **Platform targets (L10)** constrain DC-L04-04 corner geometry (continuous on iOS), DC-L04-05 concentric radii (iOS 26 hardware concentricity), DC-L04-10 depth (tonal on M3, materials on Apple, Mica on Windows), DC-L04-22 springs (native on iOS and Compose, emulated on the web), and DC-L04-26 haptics (mobile only).
- **Spacing scale (L03)** feeds DC-L04-01 radius steps (4px rhythm) and DC-L04-05 nested radius (inner = outer - padding).
- **Color system (L01)** feeds DC-L04-07 border contrast (1.4.11), DC-L04-09 focus ring color, DC-L04-12 shadow colors, DC-L04-13 dark surfaces, DC-L04-17 state layers, DC-L04-18 scrim.
- **Density (L03)** pushes toward sharper radii, thinner strokes, lines over space for dividers, and productive motion. [inferred]
- **Accessibility settings (Reduce Motion, Reduce Transparency, Increase Contrast, forced colors)** become token modes in DC-L04-25, DC-L04-16, and DC-L04-09.
- Inside L04: DC-L04-02 sets the values of DC-L04-01, which DC-L04-03 maps to components, with DC-L04-05 derived. DC-L04-10 sets DC-L04-11, DC-L04-12 and DC-L04-13, which set DC-L04-14 order. DC-L04-19 sets DC-L04-20, DC-L04-21 and DC-L04-22, which feed DC-L04-23 and DC-L04-24, all overridden by DC-L04-25. DC-L04-19 also sets haptic intensity in DC-L04-26 (Apple: match haptic sharpness and intensity to the animation [S-L04-043]).

## Community signal reconciliation
- `sources/COMMUNITY-SIGNAL.md` [S-L04-076] confirms DTCG 2025.10 as the first stable spec. This lane cites 2025.10 for all type shapes and uses the Sept 2026 editor's draft only as context [S-L04-051] [S-L04-052].
- The community file has no Reddit/HN/YouTube signal on shape, elevation, motion or haptics, and X/Twitter (where Liquid Glass and M3 Expressive debate happens) was not covered. The Liquid Glass legibility backlash is therefore sourced here from press (Tier B/C, S-L04-039, S-L04-040) and confirmed only through Apple's own product changes: the iOS 26.1 Tinted option (press-reported) and the iOS 27 slider plus "improved contrast" (Apple primary, S-L04-041). MacRumors' description of iOS 27 details (darker edge, brighter specular highlights, uniform toolbar) is **not confirmed by an Apple primary source** in this lane.
- No source used here is on L00's avoid list.

## Open questions / gaps
1. **Material 3 docs site not readable.** m3.material.io is JS-rendered, so every M3 value here comes from official code and token exports: Material Web tokens v34, Compose source, MDC Android docs [S-L04-003] [S-L04-004] [S-L04-064]. M3 prose guidance was not checked against the design site. Unchecked items: how the new shape steps map to components, expressive motion usage rules, and the current scrim opacity. The token file says "Neutral-Variant10 at 50%" for scrims [S-L04-069], while older M3 guidance is often quoted as 32%. That conflict is unresolved.
2. **Carbon v12 is not released.** Radius tokens and v12 component radii are behind the `enable-v12-release` flag. The button pill radius PR is still open [S-L04-028] [S-L04-029]. Re-check when v12 ships.
3. **Fluent radius naming conflict.** The design site says "Large 8px / X-Large 12px", but the token package has Large = 6px and XLarge = 8px, with 2XL-6XL added in January 2026 [S-L04-006] [S-L04-007]. Resolved for React v9 on 2026-09-25: published `@fluentui/tokens@1.0.0-alpha.24` (used by `@fluentui/react-theme@9.2.2`) confirms Large 6px, XLarge 8px and 2XLarge 12px. Use those names/values under GOVERNANCE.md's shipped-code-over-prose rule. The live site retains Large 8px and X-Large 12px; keep both sources instead of asserting the page is older or changing the numeric value under a code token name. Figma kit values were not inspected. [S-L04-078] [S-L04-079]
4. **Liquid Glass iOS 27 specifics.** Only Apple's iOS 27 page confirms "more uniform refraction", "improved contrast" and the "ultraclear to fully tinted" slider [S-L04-041]. The HIG Materials change log still ends at 2025-09-09 [S-L04-032], so the iOS 27 HIG material guidance was not found. The iOS 26.1 Tinted toggle, first press-reported [S-L04-039], is now confirmed on Apple's "About iOS 26 Updates" page [S-V1b-021].
5. **Apple radii values.** Apple publishes no numeric radius or elevation scale. Concentric behavior is documented; exact capsule and sheet radii are not.
6. **Material sound guidance** (M2) could not be retrieved [S-L04-072]. No design system inspected ships sound or haptic tokens. Absence of evidence was checked only in the token packages listed in Part G.
7. **Web haptics** (Vibration API support, especially on iOS Safari) not checked.
8. **Carbon elevation/layering** (the `$layer` tokens and whether shadows exist) not checked. Carbon is left out of table C1.
9. **Polaris web components era.** The Polaris React token docs redirect to shopify.dev, and token values came from the GitHub source (`polaris-tokens`) [S-L04-019] [S-L04-022]. Whether the web-components Polaris uses the same token values is unconfirmed.
10. **Fluent focus ring default width and color** not confirmed from source [S-L04-053].
11. **Research on "how radius reads".** The only measured evidence is Google's M3 Expressive research, which bundles shape with color, size and containment [S-L04-063]. No study was found that isolates corner radius and perceived personality (Perplexity and WebSearch budgets were exhausted mid-lane).
12. **WCAG texts not fetched:** 1.4.3 (disabled exemption), 1.4.11 (fetched only through the 2.4.13 Understanding page), 2.2.2. Claims that depend on them are tagged [inferred].
13. **Tooling limits hit:** Perplexity quota exhausted (401); the session-wide WebSearch budget of 200 was exhausted; GitHub API rate-limited; disk-full errors for about 10 minutes. The research worked around these with raw GitHub and unpkg files, Apple DocC JSON, and MDN.

## Confidence
- **Confirmed from Tier A primary sources or official code (high):**
  - Radius values for M3, Fluent tokens, Atlassian, Polaris, Primer and Carbon v12.
  - M3 elevation dp values and component mapping.
  - Shadow recipes for Fluent, Atlassian, Polaris and Primer.
  - Duration and easing values for M3, Carbon, Fluent, WinUI, Atlassian, Polaris and Primer.
  - M3 standard and expressive spring parameters.
  - Apple Spring API semantics and defaults.
  - Liquid Glass HIG guidance (regular/clear, 35% dimming, control layer only).
  - Acrylic and Mica behavior and fallbacks.
  - WCAG 2.4.11 (AA), 2.4.12 (AAA), 2.4.13 (AAA), 2.3.3 (AAA).
  - DTCG 2025.10 type shapes, including optional shadow `inset` and no spring type.
  - Platform haptic vocabularies and Android API levels.
  - MDN baseline statuses.
- **Confirmed with caveats (medium):**
  - Carbon v12 radius (unreleased, flagged).
  - Fluent site mapping versus package mismatch.
  - iOS 26.1 Tinted option (press; now confirmed on Apple's own page [S-V1b-021]).
  - iOS 27 details beyond Apple's two sentences (press only).
  - Expressive research numbers (Google Design article, publication date not shown).
- **Inferred (explicitly tagged in the cards):**
  - Personality readings of sharp vs round and snappy vs bouncy (except the M3 research).
  - All "Default + heuristic" numbers.
  - The spring conversion formulas (response ≈ 2π/√k, bounce ≈ 1 - ζ; standard physics, not a vendor statement).
  - Token encodings for materials, haptics and corner smoothing.
  - Cross-system "patterns" summarized under each table.

## Cross-lane notes
- [L04 -> L01] Tonal elevation (M3), dark-mode surface lightness steps (Atlassian #18191A/#1F1F21/#242528/#2B2C2F), shadow color tokens, scrim alpha (Fluent 40/50%, Atlassian 46/60%), and state-layer opacities all live in color tokens. L01 should own the surface-role ramp. L04 references it.
- [L04 -> L01] M3 token export deprecates surface-tint overlays ("update from opacity based surfaces to tonal surfaces") [S-L04-069]. Check that L01 describes current M3 surface container roles, not surface tint.
- [L04 -> L03] Radius steps reuse the 4px spacing rhythm in every system checked. The nested radius rule needs padding tokens (inner = outer - padding). Carbon choreography says motion paths "never run diagonally" on the grid.
- [L04 -> L06] The shape personality and motion personality dials are the main visual outputs of brand personality in this lane. Google's M3 Expressive research (46 studies, 18k participants) is the only measured evidence found for expressive visual design; it also warns against expressiveness in banking-type contexts.
- [L04 -> L07] DTCG gaps that matter for the builder: no spring type, no non-cubic easing (M3 emphasized is a path), no material/blur, no corner smoothing, no haptics. Real workarounds:
  - Carbon: `transition` + `$extensions["carbon.motion"]` keyframes.
  - M3: springs split into number tokens.
  - Atlassian: CSS `linear()` for springs.
  - Primer: separate `alpha` field beside `color` in shadow layers, which is not DTCG 2025.10 color syntax. L07 should check.
  - Carbon's motion package moved to DTCG JSON in July-Sept 2026.
- [L04 -> L07/L11] Primer tokens carry `$extensions["org.primer.llm"]` with `usage` and `rules` strings (for example borderWidth.thick "MUST use for focus rings"). This is a live example of AI-readable token metadata, matching the "docs for agents" trend in COMMUNITY-SIGNAL.
- [L04 -> L08] Component-level tokens from M3 and Atlassian (for example `motion.modal.enter` = 250ms scale 95 to 100%; `motion.popup.exit` = 100ms, 4px) give ready-made per-component motion specs. Carbon v12 removes popover and tooltip carets and adds a 4px gap. Focus ring rules (2px, 2px offset, concentric radius) apply to every interactive component.
- [L04 -> L10] Platform splits:
  - Apple: materials and concentric radii, springs with duration and bounce, SensoryFeedback.
  - Android: tonal elevation, MotionScheme springs, HapticFeedbackConstants (API 30/34 additions).
  - Windows: Mica and Acrylic, 83/167/250ms control durations.
  - Web: `backdrop-filter` (Baseline 2024); `corner-shape` and `prefers-reduced-transparency` are not Baseline.
- [L04 -> L09] Benchmark matrix values for radius, elevation, duration and easing are in tables A1, C1, F1, F2 and F3 of this file.
