# Style vocabulary: proposals for the maintainer

Most people cannot name the look they want, so OpenDesigner should name it for them, show it, and turn it into dials and tokens. `skills/opendesigner/references/styles.md` now holds the vocabulary: 28 named styles with plain words, the words people use, defining traits, code, dial ranges, fit, failure modes, accessibility and real Mobbin examples, plus a gradient and surface glossary. This file proposes the three changes that would wire it into the product. Nothing here is merged; no other file was edited.

Checked on 2026-10-14 against the repo as it stands: every engine command quoted below was run in a scratch project, and the glossary entries pass `tools/check_glossary.py`.

## 1. Twelve glossary entries

These are the twelve style terms people meet most, including the four the owner named (glassmorphism, comic style, neumorphism, gradients as `mesh gradient`).

**Merged.** The twelve terms were added to `synthesis/glossary.json` directly. Since 2026-10-21 that file is the glossary's source: the shards and `terms-input.json` named below are retired, and new terms go straight into `glossary.json` (`synthesis/glossary/WRITING-RULES.md`). The steps below are kept as written.

**How to merge (as proposed).** `synthesis/glossary.json` was generated: `tools/check_glossary.py --build` merges `synthesis/glossary/shard-*.json` and takes each term's layer from `synthesis/glossary/terms-input.json` (all 399 current terms come from shards). So:
1. Save the array below as `synthesis/glossary/shard-styles.json`.
2. Add the twelve ids to `synthesis/glossary/terms-input.json` with `"layer": "prin"`, `"kind": "style"`, a one-line `context` and `"source": ["skills/opendesigner/references/styles.md"]`.
3. Run `python3 tools/check_glossary.py --build`, then `python3 tools/build_data.py` and `python3 tools/sync_skills.py`, then the checks in AGENTS.md.

**What was checked.** `python3 tools/check_glossary.py shard-styles.json` prints `12 entries, plain voice mean grade 5.4, 0 errors` (word limits, jargon list, acronyms, grade ceiling, and every token name such as `material.glass.blur`, `color.surface.glass-fallback`, `border.width.default` and `elevation.raised` exists in the engine). No id, term or alias collides with the 399 existing terms. The ids sit in the `prin` layer next to `prin.visual.style` (the style preset). Optional `see_also` links worth adding: glassmorphism to `found.elevation.materials`, mesh gradient to `found.color.expressive`, flat design to `found.elevation.depth-model`.

```json
[
 {
  "id": "prin.style.glassmorphism",
  "term": "glassmorphism",
  "plain": "See-through panels that look like frosted glass, so you see a blur of what is behind them.",
  "designer": "Translucent fill, background blur and a thin light edge over rich content. Use it on bars, sheets and menus, never on reading surfaces, and give it a solid twin.",
  "engineer": "Q-dir-01 glass, or Depth above 80, builds the materials model: material.glass.blur (24px), color.surface.glass and color.surface.glass-fallback. Web uses backdrop-filter.",
  "designer_says": "glassmorphism, frosted glass",
  "code_name": "backdrop-filter, material.glass.blur",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-01",
   "DC-L04-15",
   "DC-L04-16"
  ],
  "layer": "prin",
  "aliases": [
   "frosted glass",
   "frosty",
   "glassy",
   "see-through",
   "backdrop blur"
  ]
 },
 {
  "id": "prin.style.neumorphism",
  "term": "neumorphism",
  "plain": "Soft buttons that look pushed up out of the page, or pressed in, all one color.",
  "designer": "Same-color surfaces with paired light and dark soft shadows. Tactile but vague: edges usually fail 3:1, so every control needs an added border or fill.",
  "engineer": "Q-dir-01 soft selects the soft preset (roundness 80, colorfulness 20) and the lint warns neumorphic-preset. Paired and inset shadows are not generated yet (proposed).",
  "designer_says": "neumorphism, soft UI",
  "code_name": "paired box-shadow, inset",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-01",
   "S-L15-060"
  ],
  "layer": "prin",
  "aliases": [
   "soft UI",
   "soft buttons",
   "pillowy",
   "new skeuomorphism"
  ]
 },
 {
  "id": "prin.style.claymorphism",
  "term": "claymorphism",
  "plain": "Puffy, round shapes that look made of soft clay or toy plastic.",
  "designer": "Large radius, a soft outer shadow plus light and dark inner shadows, pastel color and 3D clay art. Friendly and cute; keep product controls calmer.",
  "engineer": "No preset of its own: start from soft, then raise roundness above 80 and colorfulness. Inner shadows are not generated yet (proposed); 3D art is an asset (Q-img-06).",
  "designer_says": "claymorphism, clay 3D",
  "code_name": "box-shadow with inset pairs",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-01"
  ],
  "layer": "prin",
  "aliases": [
   "clay",
   "puffy",
   "squishy",
   "inflated 3D",
   "soft 3D"
  ]
 },
 {
  "id": "prin.style.skeuomorphism",
  "term": "skeuomorphism",
  "plain": "Screens that copy real objects and materials, like a record player, a tape or wood.",
  "designer": "Realistic textures, lighting and shadows that mimic physical objects. Useful as a metaphor, like a folder or trash can; as full realism it clutters screens and loads slowly.",
  "engineer": "Mostly assets, not tokens: textures and objects use the H-motif hook (Q-img-07), custom controls Q-plat-06 custom, and Depth in the shadow-ladder band (56-80).",
  "designer_says": "skeuomorphism, realism",
  "code_name": "layered gradients and box-shadow",
  "source": [
   "skills/opendesigner/references/styles.md",
   "S-L15-008",
   "DC-L15-01"
  ],
  "layer": "prin",
  "aliases": [
   "realistic",
   "real-world look",
   "physical metaphor"
  ]
 },
 {
  "id": "prin.style.flat",
  "term": "flat design",
  "plain": "Plain solid colors with no shadows, no shine and no texture.",
  "designer": "Solid fills, simple icons, hierarchy from color and size. Flat 2.0 brings subtle shadows back. Keep strong signs of what to click, or people search longer.",
  "engineer": "Depth 0-15 builds the borders model with no shadows. The default flat2 preset (Q-dir-01) sets Depth 30: a ring plus a faint shadow.",
  "designer_says": "flat design, flat 2.0",
  "code_name": "box-shadow: none",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-01",
   "S-L15-009",
   "S-L15-004"
  ],
  "layer": "prin",
  "aliases": [
   "flat",
   "flat 2.0",
   "semi-flat",
   "no shadows"
  ]
 },
 {
  "id": "prin.style.neo-brutalism",
  "term": "neo-brutalism",
  "plain": "Bright flat colors with thick black lines and hard black shadows, like stickers.",
  "designer": "Thick borders, a solid 4px offset shadow, 2-3 bold colors, 24-32px padding and a quirky display face over a neutral body face. Loud and indie.",
  "engineer": "Q-dir-01 neo-brutalist selects the neobrutal preset (roundness 5, depth 0, colorfulness 80). Thick borders and the offset shadow need overrides of border.width.default and elevation.raised.",
  "designer_says": "neo-brutalism, neubrutalism",
  "code_name": "box-shadow: 4px 4px 0",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-01",
   "S-L15-006"
  ],
  "layer": "prin",
  "aliases": [
   "neubrutalism",
   "neo brutalist",
   "black borders",
   "chunky outlines"
  ]
 },
 {
  "id": "prin.style.swiss",
  "term": "Swiss style",
  "plain": "A strict, tidy grid with plain bold letters lined up on the left and lots of space.",
  "designer": "International Typographic Style: a column grid, neo-grotesque type set flush left, big size jumps, asymmetric layouts, neutral colors plus one accent.",
  "engineer": "Q-type-03 neo-grotesque, Q-dir-05 start and the flat2 preset, with roundness 0-25 and colorfulness 11-45. The grid itself is layout, not a token.",
  "designer_says": "Swiss style, International Typographic Style",
  "code_name": "display: grid; text-align: start",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L02-02"
  ],
  "layer": "prin",
  "aliases": [
   "International Typographic Style",
   "Swiss design",
   "grid style",
   "Helvetica look"
  ]
 },
 {
  "id": "prin.style.editorial",
  "term": "editorial style",
  "plain": "Pages that read like a good magazine: big titles, calm text and large photos.",
  "designer": "Serif display headlines, dramatic size jumps (1.333 or more), 60-75 character lines, pull quotes and thin rules. For reading products and long content.",
  "engineer": "Q-type-03 serif, Q-dir-03 dramatic (type ratio 1.333) and Q-dir-04 lines. Body text stays 16px or larger; limit lines with max-width: 65ch.",
  "designer_says": "editorial, magazine layout",
  "code_name": "max-width: 65ch",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L15-02",
   "DC-L15-05"
  ],
  "layer": "prin",
  "aliases": [
   "magazine style",
   "magazine layout",
   "long-form"
  ]
 },
 {
  "id": "prin.style.bento",
  "term": "bento grid",
  "plain": "Content in neat boxes of different sizes, like the parts of a lunch box.",
  "designer": "Tiles of two or three spans in one grid with one gap; one idea per tile, the hero tile largest. A layout that borrows its look from another style.",
  "engineer": "CSS grid with grid-column and grid-row spans; Q-dir-04 containers. Keep DOM order equal to reading order (WCAG 1.3.2) and reflow to one column.",
  "designer_says": "bento grid, bento box layout",
  "code_name": "grid-column: span 2",
  "source": [
   "skills/opendesigner/references/styles.md",
   "S-L15-065",
   "S-L15-062"
  ],
  "layer": "prin",
  "aliases": [
   "bento",
   "bento box",
   "tile grid",
   "feature tiles"
  ]
 },
 {
  "id": "prin.style.mesh-gradient",
  "term": "mesh gradient",
  "plain": "Soft clouds of a few colors that melt into each other, like the northern lights.",
  "designer": "Three to five colors blending in many directions, often blurred and slowly moving. Marketing and brand moments only, never on buttons or forms.",
  "engineer": "Stacked radial-gradient layers or blurred shapes, interpolated in OKLab. DTCG gradient tokens hold stops only; the engine does not generate gradients yet (proposed).",
  "designer_says": "mesh gradient, aurora gradient",
  "code_name": "radial-gradient layers",
  "source": [
   "skills/opendesigner/references/styles.md",
   "DC-L01-25"
  ],
  "layer": "prin",
  "aliases": [
   "aurora gradient",
   "aurora",
   "gradient blur",
   "gradient background",
   "northern lights"
  ]
 },
 {
  "id": "prin.style.grain",
  "term": "grain texture",
  "plain": "A fine speckle over colors, like old film or printed paper.",
  "designer": "Fine noise at 3-8% strength over fills and gradients. It warms flat color and hides gradient banding; keep it off body text and keep it still.",
  "engineer": "An SVG feTurbulence image on a pseudo-element with mix-blend-mode: overlay. Not a token yet (proposed); record it with the H-motif hook (Q-img-07).",
  "designer_says": "grain, noise texture",
  "code_name": "feTurbulence overlay",
  "source": [
   "skills/opendesigner/references/styles.md"
  ],
  "layer": "prin",
  "aliases": [
   "grain",
   "noise",
   "film grain",
   "grainy",
   "paper texture"
  ]
 },
 {
  "id": "prin.style.comic",
  "term": "comic style",
  "plain": "Looks like a comic book, with thick ink outlines, bright flat colors, dots and speech bubbles.",
  "designer": "Black outlines, primary colors, halftone dot shading, speech balloons and burst shapes; pop art is its gallery cousin. Keep hand lettering to short labels.",
  "engineer": "Start from the neobrutal preset with colorfulness above 88. Halftone is a radial-gradient dot pattern; drawings are assets (Q-img-04, opendesigner-illustrate).",
  "designer_says": "comic style, pop art, halftone",
  "code_name": "radial-gradient dot pattern",
  "source": [
   "skills/opendesigner/references/styles.md"
  ],
  "layer": "prin",
  "aliases": [
   "comic",
   "comic book",
   "pop art",
   "cartoon",
   "halftone",
   "speech bubbles"
  ]
 }
]
```

## 2. Where the vocabulary appears in the interview

The rule for every moment below: plain words first, then the name, then the code (`rules.md` section 2), and the style is shown, not described.

| Moment | Today | Proposal |
|---|---|---|
| **Level 0, question 4: "How should it feel?"** (`sketch --feel`, fills Q-brand-01) | Look words are not understood. `engine.py feel frosty comic` prints "not known yet" for both (run 2026-10-14). | Add a `styleWords` map to `synthesis/levers.json`, next to `feelWords`, built from the "They say" table in styles.md: word to style id to preset plus dial offsets. Then `engine.py feel frosty` answers "glassmorphism (preset glass)", the sketch uses it as the starting preset recorded as `assumed`, and the first result names the style in one line ("Frosted see-through panels; designers call it glassmorphism"). |
| **Q-dir-01, the style screen** (zoom 1, weight high, changes 13 decisions) | Six presets: flat2, tonal, glass, neo-brutalist, soft, maximal. | Keep the six as families and show named styles inside them in the option gallery: flat2 for flat design, Swiss, editorial, minimal monochrome and bento; tonal for Material elevation; glass for glassmorphism and Frutiger Aero; neo-brutalist for neo-brutalism, brutalism and comic; soft for neumorphism and claymorphism; maximal for mesh and aurora, Memphis, Y2K and risograph. Pick the 2 or 3 safe choices and at least 2 risks (`rules.md` section 3, item 5) from the styles whose "Fits" line matches the audience and platform. Record the named style as well as the preset (section 3, last row). |
| **Q-depth-01, how cards stand out** (zoom 1) | Options shadow, tonal, borders, ring-shadow, glass. | Name them as styles in the option labels: borders is flat design, shadow is Material elevation, glass is glassmorphism. Offer the soft styles (neumorphism, claymorphism) only as a risk with the 3:1 warning. |
| **Q-depth-04, where glass goes** (zoom 2) | Options none, control-layer, transient, decorative. | Say "glassmorphism; Apple calls it Liquid Glass, Microsoft calls it Acrylic" on first mention. |
| **Q-shape-01, corners** (zoom 1) | Square, subtle, soft, pill. | Add one "Now" clause per option naming the styles it suits: square for Swiss and brutalism, pill for playful and toy-like. |
| **Q-color-03, how colorful** (zoom 2) | Monochrome, tonal, vivid, expressive, fidelity. | Name minimal monochrome on `monochrome`, and Memphis, comic and Y2K on `vivid`. Add a follow-up for color treatments (duotone photos, risograph spot inks), which no question covers today. |
| **Q-type-03, font style** (zoom 2) | Neo-grotesque, geometric, humanist, serif, slab, rounded. | Add options several styles need: monospace for the interface (terminal), pixel or bitmap display (pixel art), condensed display (Swiss posters, brutalism), high-contrast geometric display (Art Deco), italic serif display (editorial). |
| **Q-img-04, illustration style** (zoom 2) | None, line, flat, hand-drawn, mascot, where. | Add clay 3D, isometric, comic with halftone, and pixel art, each handing off to opendesigner-illustrate. |
| **Q-img-06 and Q-img-07, 3D and brand patterns** (zoom 3) | 3D assets; brand shapes none, expressive-only, logo-shapes. | Name the pattern styles at Q-img-07: Memphis shapes, Bauhaus shapes, grain, halftone, risograph texture. Name claymorphism at Q-img-06 `3d`. |
| **Q-brand-02, the memorable thing** (zoom 2) | Signature typeface, color, device, character. | Under `sig-device`, offer one trait from a style as the single signature (a hard offset shadow, a grain layer, a pixel logo), so a bold style is spent in one place (`rules.md` section 10). |
| **Q-theme-01, light and dark** (zoom 2) | `dark-only` and `light-only` break STD-visual-details-24; `pick Q-theme-01 dark-only` is refused (run 2026-10-14). | Dark luxe, terminal and Art Deco lead with dark: recommend `light-dark-toggle` and design dark first. styles.md already says this. |
| **Taste poll** (`references/taste.md`) | `assets/taste/library.json` tags 237 screens with style tags: glass 12, grain texture 6, thick borders 5, sticker 5, brutalist 3, bento 3, editorial 15, flat 13, monochrome 23, retro 14, mono type 18, 3D 25, chunky buttons 6, gradient 16, glow 17. | Map each tag to a styles.md id, so the poll result can name what the person loved: "You rated three glass screens highest; designers call this glassmorphism." The thin tags (brutalist 3, bento 3) tell `taste.py coverage` where to fetch more Mobbin screens. |
| **opendesigner-extract** | Measures a reference's values. | Name the reference's style in one line from styles.md, so the person learns the word, while still taking structure, never identity. |

The showcase pieces another session is building in `brand/showcase/styles/` (01-glassmorphism, 02-neumorphism, 05-comic, 06-memphis, 09-bento-grid, 10-mesh-gradient, 11-terminal, 12-pixel-art) would make good full-size option-gallery samples for these moments once they pass review; their numbering differs from styles.md.

**Wiring still needed (files this task did not touch):** a row for `references/styles.md` in the "Files in this skill" table of `skills/opendesigner/SKILL.md` ("Read it when a person describes a look in their own words, and before Q-dir-01"); a pointer from stage 06 (`synthesis/` source of `stages/06-visual-direction.md`) to styles.md; and `python3 tools/sync_skills.py`, because `sync_skills.py --check` fails until the new file is copied to `.agents/skills/` and `.claude/skills/`.

## 3. What the dials cannot express today

The eight dials and six presets cover depth model, corners, chroma, density, type scale and motion. These looks need things the engine does not build. "Evidence" is what was read or run in the repo on 2026-10-14.

| Styles affected | What is missing | Evidence | Proposal |
|---|---|---|---|
| Neo-brutalism, comic, pixel art, brutalism | Thick default borders and a hard offset shadow from the preset | `levers.json` preset `neobrutal` has `extra: {borderWidth: "thick", offsetShadow: "4px solid", colors: "2-3", padding: [24, 32]}`, but `resolve_dials` reads only `preset["dials"]`; nothing reads `extra`, `rules`, `scope` or `warning` (only the soft preset's warning exists, as a lint). `border.width.default` always aliases `border.width.1`; `raw.borderWidths` adds steps up to 8 px but never moves the default. `build_elevation` emits only blurred shadows. **Workaround that builds cleanly today:** `engine.py set border.width.default 3` and an `elevation.raised` override with blur 0 and color `{color.text.primary}` (CSS: `--ds-elevation-raised: 4px 4px 0px 0px var(--ds-color-text-primary)`). | Read preset extras. Add `raw.borderDefault` (1 to 4) and an elevation model `offset` (blur 0, x = y = 2 to 6 px, color from the strongest text color), with the press recipe in DESIGN.md. These borders go against STD-visual-details-14, so the route is a project standard with `--beats` when the person chooses this style. |
| Neumorphism, claymorphism, skeuomorphism, Y2K, Frutiger Aero, playful (ledge buttons) | Paired light and dark shadows, inner shadows, a highlight color, gloss and bevels | `shadow_layer` supports `inset`, but no elevation model uses it; there is no highlight color token. The soft preset sets no depth value. A token override with an inset layer works when every color is an alias, but **a literal hex inside a shadow override stops the build** (`ValueError: not a color: #ffffff`) and the CSS export wrote `var(--ds-fffff)` for it. | Add `color.shadow.highlight` (light mode white at about 80%, dark mode a lifted surface) and an elevation model `extruded` with raised and pressed pairs; a `clay` variant with two inner shadows; a `ledge` recipe (0 4px 0 in the pressed accent). Fix literal colors in shadow overrides, or reject them with a clear message. |
| Glassmorphism, Frutiger Aero | Tunable glass | `material.glass.blur` is fixed at 24 px and `color.surface.glass` at 72%; STD-visual-details-16 gives `saturate(180%)` and a 1 px top edge at 40% white, and STD-visual-details-19 asks for stronger blur on bigger surfaces; none of these are tokens. | `material.glass.blur.sm` and `.lg`, `material.glass.saturate`, `color.border.glass-edge`. |
| Mesh and aurora, gradient text and borders, Y2K chrome, Art Deco gold | Any gradient token | `gradient` is in `DTCG_TYPES` for reading, but the engine generates no gradient tokens; glossary `found.color.expressive` says kind, angle and interpolation belong in `$extensions`. | Generate `gradient.brand.*` (linear, radial, conic) from accent steps, interpolated in OKLab, marked marketing-only; a mesh as a list of radial layers in `$extensions`; CSS recipes for gradient text and border; a lint that flags gradients on controls. |
| Grain, halftone, scanlines, risograph, paper | Texture | No token or state field; only the H-motif hook (Q-img-07) records that a texture exists. | A `texture` group in `$extensions` (kind, strength 0.03 to 0.08, blend mode, static or moving) with a CSS export of an inline SVG noise, switched off under `prefers-contrast: more`. |
| Terminal, pixel art, Art Deco, brutalism, Swiss posters, editorial | Type classes | `Q-type-03` maps only to `neo-grotesque`, `geometric`, `humanist`, `serif`, `slab`, `rounded` (`raw.fontClass`). `raw.monoFace` feeds only the code roles; a mono interface works today only by setting `raw.textFace` to a mono face by hand (verified). | Add `mono-ui`, `pixel`, `condensed`, `high-contrast-display` and `italic-serif-display` classes, each with a licence check and a readable body fallback. |
| Duotone, risograph, Bauhaus, neo-brutalism | Palette limits and image treatment | Colorfulness sets chroma, not how many hues; Q-color-04 sets accent count only. No token for photo treatment. | `image.treatment` (none, grayscale, duotone with two ramp steps) and a `palette.maxHues` limit the validator checks. |
| Pixel art, terminal | Stepped motion and pixel rendering | The energy dial drives springs and bezier curves only. | `motion.easing.steps` and a DESIGN.md rule for `image-rendering: pixelated` and whole-number scaling. |
| Every style | A home for the style's name | The name can live only in `taste.likes` or a `--why` today; DESIGN.md says "preset glass", not "glassmorphism". | A `style` state field (a styles.md id) set by Q-dir-01 or the new styleWords map, shown in DESIGN.md and the overview as "Style: glassmorphism (frosted see-through panels)". |
| Showing styles | The option gallery template | `option-gallery.html` hard-codes 1 px borders, has no `backdrop-filter`, and uses `--t-bg` both as a background and as a text color, so a gradient value would break text. Shadows accept any `box-shadow`. | Add `border-w`, `backdrop`, `surface-image` and `texture` variables, and a separate text color variable, so every style in styles.md can be shown side by side. |
