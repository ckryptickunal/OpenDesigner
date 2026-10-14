# Heroes 01-05: process summary

Builder for pieces 01 to 05 (another builder owns 06-10 and writes PROCESS.md). Every hero renders at 1440 x 900, scale 2 (`shot.png`, 2880 x 1800). Every piece went through: Mobbin references, `engine.py sketch`, dial and typeface changes through the engine, `build`, a page on the generated tokens, at least three look-and-fix renders, `review`, `validate`, `preflight.py html`, and notes plus `engine.py feedback`. The owner's mid-run type and colour rules were applied to all five after they arrived (each `notes.md` has a "Changes for the owner's type and colour rules" section).

## Directions, side by side (written before building)

| # | Brand (fictional) | Domain | Palette | Type | Layout idea | Shape language | Mood |
|---|---|---|---|---|---|---|---|
| 01 | Halde Architekten | Zurich architecture studio | warm off-white paper, black, one signal red | Inter Tight only | 12-column grid shown as hairlines; numbered project index; generated building section with a sun study; giant headline on the baseline | square, ruled lines, no radius, no shadow | precise, calm, authoritative |
| 02 | Nearmost (was Orrery; renamed in round 3) | vector database for developers | black, aqua light, indigo and violet halo | Geist and Geist Mono | headline and install command left; a canvas "embedding galaxy" behind three product panels at different depths | glassy panels, 6-12 px radii, glow | luminous, technical, fast |
| 03 | Lullwort | herbal sleep tea | cream, clay, sage, ink | Fraunces and Instrument Sans | soft serif headline left; a watercolour dusk with a tin and a cup in a chamomile meadow, painted in SVG | blobs, pills, hand-drawn lines | slow, warm, hushed |
| 04 | Howl Hill Weekender | indie music festival | poster yellow, ultramarine, black | Big Shoulders Display and Space Grotesk | gig poster: huge condensed type with a hard shadow, bordered nav cells, stickers, crossing lineup tickers | thick borders, hard offset shadows, rotated stickers | loud, joyful, DIY |
| 05 | Maison Auberval | fashion maison | ivory and near-black | Bodoni Moda and Jost | empty ivory page, tiny tracked caps, a tall painted plate of black silk; the headline turns ivory where it crosses the plate | hairlines, no radius, no shadow | hushed, couture, editorial |

No two share a domain, palette family, typeface, shape language or mood.

## The pieces

| # | Shot | Palette (key tokens) | Type scale used | Verdict |
|---|---|---|---|---|
| 01 | `01-swiss-architecture/shot.png` | ground #eeebe9, ink #272421, red #e8361e | 168 / 20 / 16 / 13 / 11 | Strongest of the five. The generated section drawing (winter sun reaching in, summer sun held off) gives it a real idea. |
| 02 | `02-luminous-devtool/shot.png` | #000, aqua #46e0d3, violet #a291ff, indigo #759aff | 67 / 28 / 21 / 16 / 12 | Polished and luminous, but the structure (copy left, tilted panels right) is the familiar dev-tool hero; the light field is what makes it ours. |
| 03 | `03-organic-wellness/shot.png` | cream #f1ebe1, clay #b8643f, muted sage, ink #262420 | 120 / 28 / 21 / 16 / 12 | Charming and warm; the painting is the point. Its dark mode breaks the new colour rule (brown-black with terracotta), so only the light render counts. |
| 04 | `04-neobrutalist-festival/shot.png` | yellow #ffd60a, ultramarine #2433ff, ink #252423 | 283 / 90 / 67 / 38 / 21 / 16 | Loud and fun; dense, with stickers placed close to collisions on purpose. All weights 800-900, which is the genre. |
| 05 | `05-luxury-maison/shot.png` | ivory #f6f4ef, ink #262420, black silk | 160 / 28 / 16 / 12 | The most "gallery" piece. The silk plate is a convincing painted study but still a little regular, like a pleated curtain. |

## Process findings, most important first

### A. The engine or a skill is wrong or missing something

1. **Colours the person gives are not kept.** Four of five pieces needed a fix.
   - `sketch --brand ... --delegated all` treats the given hex as model-picked and replaces it with a darker "readable" shade: 01 `#E8361E` became `#e02c13`; 02 `#46E0D3` (a luminous aqua for a dark UI) became `#00837b`. `color.brand.seed` is described as "the brand color exactly as given" but holds the changed hex. Without `--delegated` (piece 03) the exact colour is kept and only the button shade moves, which is the right behaviour. Code: `cmd_sketch`, the `readable_shade` call under `if sb("brand")`.
   - Secondary colours are pulled to the brand's chroma: 03's dried-herb sage `#7E9475` came back as `#6c9c57` (bright grass); 04's poster yellow `#FFD60A` came back as `#f8d756`. There is no seed token for them.
   - Fixed with `set raw.brandColor ... --set-by chosen` and `set color.accent2.light.9 {srgb ...}`; validation still passed.

2. **There is no palette for art, and art bound to UI roles breaks.** Ramps are built for contrast steps: a terracotta's light steps drift pink and jump from `#f2bea9` (step 7) to `#b6775d` (step 8); a very dark seed (05's espresso) gives plain greys for steps 1-8; there are no mid-tones to paint with. Art that used `surface.base` and `text.primary` inverted in dark mode (03's white petals turned black). Three pieces mixed their own art colours with `color-mix()`. The paint skill's brief already computes palette families; emitting them as theme-independent tokens would fix it.

3. **preflight cannot see a token-based page.**
   - It printed `font sizes in px: []` for four of five pages, because the generated `tokens.css` writes sizes in rem and the parser only reads px, so the scale and minimum-size checks (M6, M8) pass silently. On 02 it reported `[22]`: the line height in `font: 400 var(--ds-font-size-12)/22px` was read as the font size.
   - It raised a false ERROR (M9, "no @font-face") for every Google Fonts face on all five pages.
   - It does not notice an infinite CSS animation without a pause control (04's ticker). I added the pause button by hand.

4. **House standards fight legitimate art direction.**
   - `sketch --theme light-only` is refused by STD-visual-details-24, so 02 (dark-only) and 04 (light-only poster) needed `standard override`.
   - After dark-only, `validate` still warns about the unused light mode, and `tokens.css` still ships a light theme.
   - The depth stage tells people to avoid single hard shadows, and no option makes them, though hard shadows are what neo-brutalism is (04).
   - STD-accessibility-motion-13 requires rem spacing, and `review` flags every px gap, yet `tokens.css` writes the whole space ladder in px (`--ds-space-8: 8px`). The system breaks its own rule.

5. **The light page ground cannot be off-white.** `surface.base` is always step 1 (#fefcfb even at Warmth 70), and `raw.neutralBase` sets only hue and chroma. All four light pieces borrowed another role for paper or poster grounds (`bg.neutral.subtle`, `surface.sunken`, `bg.accent2.bold`). A `color.light.baseY` override, the light-mode twin of `color.dark.baseY`, would fix it.

6. **Dark depth is shadow-only.** `raw.darkBase black` collapses the surface ladder (base #000000, raised #010101, overlay #050608), and Depth 85 only adds black drop shadows, which are invisible on black. 02's glow, rim light and panel fills were all hand-built.

7. **`set` accepts values that crash `build`.** An elevation override written with string dimensions was accepted, then `build` died with a Python traceback (`TypeError: string indices must be integers` in `css_dim`). The DTCG shape (`{"value": 6, "unit": "px"}`) worked.

8. **Typefaces are hard to set and wrongly flagged.** The path (`raw.textFace`, `raw.displayFace`, `raw.monoFace`) is not in the typeface stage file; I found it in `engine.py`. Open Google faces outside a 40-name list (Inter Tight, Fraunces, Bodoni Moda, Big Shoulders) show as "licence risks" until `raw.fontLicence` is set. `paint.py brief` still says "confirm Fraunces is OFL" after the licence was recorded.

9. **`review` is very useful but sometimes suggests the wrong token.**
   - It suggested `space-24` for a 24 px min-height (should be `size.target.min`), `space-0` for a -4 px margin, an elevation token for a `text-shadow` (invalid there), `elevation.raised` for 1 px inset borders, and two different radius tokens for the same 2 px.
   - It flagged mask stop colours as off-palette.
   - It does not look inside `clamp()` or the `font` shorthand.

10. **Dials and options that do more than their names say.** Density changes text size: 05 at Density 5 got 19 px body and 14 px labels, the opposite of a fine luxury page. High Warmth with a warm brand silently produces the brown-black-with-orange dark mode the owner bans (03). `--audience large` means "people who use it now and then, often on a phone", not large type (04).

11. **The paint skill cannot paint unattended.** Painting needs `npm install` and Chromium per film project, which needs the person's yes. Only the offline brief was usable, so 03's and 05's art was painted by hand-written code following that brief.

12. **Feel words missing:** "natural", "organic" and "precise" were not understood. The engine asked about each, as designed.

### B. What I worked around (and how)
- Exact colours: `set raw.brandColor` with `--set-by chosen`, plus a token override for the yellow (01, 02, 04).
- Off-white grounds: borrowed `bg.neutral.subtle` or `surface.sunken` (01, 03, 05).
- Hard shadows: overrode `elevation.raised` and `elevation.floating` with DTCG shadows through `set` (04).
- Glow and dark depth: page-level custom properties built from token colours and sizes, marked `od-ignore` (02).
- Art palettes: `color-mix()` in OKLab from tokens; fixed `--art-paper` and `--art-ink` so pigments do not flip with the theme (03, 05).
- Poster type: `set type.displayReach` (14, 5, 7, 20, 9.5) and `set type.headingWeight 400` (03, 05); 01's headline is still a clamp because its grid width falls between two steps (149 and 233).
- Pause control and reduced motion for the ticker added by hand (04).

### C. What helped
- `type.displayReach` and `type.headingWeight` make poster-scale and light display type a real part of the system, not a hack.
- Token overrides through `set <token path> <DTCG value>` are logged, rebuilt and re-validated. That is a safe escape hatch.
- `engine.py review` caught real drift fast (22 hard-coded values on 01, 37 on 02) and ended every piece at "the code uses the tokens".
- Built on tokens, dark mode came almost for free: 01 and 05 render correctly in dark with no extra work.
- `raw.secondaryColors` plus `raw.accentCount` gave real ramps that the canvas art and syntax colours read at run time (02).

### D. Outside OpenDesigner
- Mobbin had little true neo-brutalism; two searches mostly returned polished SaaS heroes (04).
- The two builders shared one scratchpad folder, and the other builder's helper scripts overwrote mine (`dials.py`, `cr.py`). I moved mine to `scratchpad/h15/`. Parallel builders need their own subfolders.

All gaps are recorded with `engine.py feedback` in each piece's `opendesigner/feedback.md`: 8 for 01 (including two preflight bugs), 6 for 02, 5 each for 03 and 04, and 3 for 05. One entry in 04 was corrected after reading DESIGN.md.
