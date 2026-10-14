# Components 01-05: process report

Five working, interactive web components, each a 1440 × 900 component sheet rendered at scale 2 (2880 × 1800 PNG), each with its own design system made by the engine in its own folder. The other builder owns 06-10.

## The pieces

| # | Piece | Fictional brand and direction | Palette | Type (final) | Render |
|---|---|---|---|---|---|
| 01 | `01-pricing-glass/shot.png` | Gloaming, AI video studio. Dark screening room; a projector beam lights the plan most people pick; billing toggle | teal-black, frosted dark glass, one near-white lit card, amber #F2A93B | Instrument Serif 400 (titles, prices) + Geist | 1440×900 @2x |
| 02 | `02-command-palette/shot.png` | Margin, writing tool. A palette floating over a manuscript, annotated with margin notes; real fuzzy matching | paper and ink only, 1 px rules | IBM Plex Sans + Newsreader (manuscript, wordmark) | 1440×900 @2x |
| 03 | `03-date-range-picker/shot.png` | Wayfern, cabin stays. Two months, a price in every night, heat from cream to coral, fern marks best prices | cream, tan, coral, terracotta band, ink | Fraunces (soft, wonky) + Nunito | 1440×900 @2x |
| 04 | `04-upload-brutal/shot.png` | Halftone Yard, print shop. Neo-brutalist dropzone and job-ticket rows, drag, reject, progress, error with replace | newsprint, ink, process cyan / magenta / yellow | Archivo (normal and expanded) + Space Mono (data only) | 1440×900 @2x |
| 05 | `05-toast-stack/shot.png` | Chorus, team chat. A layered toast stack in context, fanned out on hover, with undo, retry and reply | lilac fog, white, ink, iris, mint | Figtree only | 1440×900 @2x |

Every piece has `index.html` (works live: hover, focus-visible, keyboard, reduced motion), `notes.md` (direction, Mobbin references by link, dials, fonts, type scale, what is outside the tokens and why, checks, findings), `opendesigner/` (state, tokens, build, `feedback.md`) and the generated `DESIGN.md` and `PRODUCT.md`. 04 and 05 read `?still` to freeze their timers for the render.

Honest quality notes: 01, 02 and 04 are the strongest. 03 is warm and clear but the calendar is a busy grid by nature. 05 is correct and calm, as briefed, and the quietest of the five. The beam in 01 still has a visible edge, kept on purpose as a spotlight.

## Process findings, most important first

### The engine or skill is wrong or missing something

1. **Sketch rewrites the brand colour.** In 3 of 5 pieces `sketch --brand` stored a different colour as `raw.brandColor` so white button text would pass: #F2A93B became #a16900 ("a brown", 01), #E4572E became #d04418 (03), #FFE500 became #847600 ("an olive", 04). Stage 08 says a light brand colour should switch its button text to dark instead, and the engine does exactly that once the hex is set back by hand (`text.on-action` became neutral 12 on yellow). Then `pick Q-color-01 keep-hex` printed "the tokens already match this answer" while the brand was in no ramp. Evidence: sketch output, `state.json` raw.brandColor before and after, decisions D-0029 (01) and D-0012 (04).
2. **Type sizes break the house's own floors.** On "operate" surfaces the engine chose a 14 px base and ratio 1.333, so `text.body-sm` and `label-sm` were 11 px (03 and 04), while stage 11 says nothing below 12 px on web and preflight errors under 12 (M8). The display end was capped at 33 px even at expression 90; poster type needed `set overrides.type.displayReach 5`, which no question or stage file mentions. In 01 (expression 85) the scale skipped 14 px entirely (12 / 16 / 21 / 28). Fixed each time through answers (`Q-type-08 16`, `Q-type-09 1.25`).
3. **The checks miss what matters most and flag what does not.** Text over glass, art and tinted cells was where every real contrast failure was, and no tool measured it: the engine checks token pairs on solid surfaces, preflight reads CSS text. My own render-based check found secondary text at 2.88:1 on 01's lit glass and prices at 4.22:1 on 03's coral heat cells. Meanwhile preflight could not see token sizes (`font sizes in px: []` on token-built pages), reported Google Fonts as missing whenever a `font-family` longhand was written but not in the shorthand, and read a `/24px` line height as a font size; `review` returned 103 findings on 01 with wrong "closest match" tokens (a backdrop colour mapped to `text-on-action`, `width: 80px` to `space-80`), told a plain HTML page to rebuild on base-ui or Radix, and called a spinner's period an over-budget transition.
4. **Typefaces are named but not understood.** `set raw.textFace / displayFace / monoFace` works (not documented in the stage files; Q-type-01 only offers classes). The weights ignore the face: Instrument Serif ships one weight, the tokens asked for 650 and 750 and the browser would fake a bold. Nothing in the system knows the owner's new limits (two faces, mono only for data, named roles, about six sizes).
5. **Colour model gaps.** Several exact brand colours can only be given through `raw.secondaryColors`, mentioned once in zoom.md; it worked perfectly for process cyan and magenta in 04. `Q-color-04 three` is called triadic but uses ±60 degrees (green and orange from yellow). The only sequential ramp is `color.chart.sequential`, unlocked by the charts question and built from the accent hue, so it collides with the selection colour in a price heat. The alpha neutral ramp exists but DESIGN.md never mentions it; there is no white veil for light overlays; a near-black brand collapses accent steps 10 to 12 into black.
6. **Depth and material gaps.** The dark glass token is 72% opaque, which hides the light a glass card exists to show (01 mixes it to 55%). There is no hard offset shadow for neo-brutalism (04 defines its own).
7. **Dark-only is awkward end to end.** `--theme dark-only` is refused by STD-visual-details-24; the override needs `init` first, which the refusal does not say. Afterwards `validate` still warns about light-mode contrast and DESIGN.md's front matter shows the light surface (#f4f4f4).
8. **"Springy" collides with locked motion.** The toast entrance is locked to 400 ms ease and spatial springs are critically damped by a standard; only `motion.spring.momentum` overshoots (1.5%). It took reading the standards to find where a spring was allowed.

### Where OpenDesigner clearly helped

- **The house standards designed the behaviour.** "No motion on 100+ times-a-day actions" and "never animate keyboard actions" settled the palette (02) and the keyboard paths in 01 and 03; thirteen toast rules gave 05 its stacking, timing, pause, queue, swipe and placement with numbers; "legible text on translucent surfaces" named the fix for 01's glass.
- **Answers reach the tokens.** Q-color-09, Q-depth-01, Q-type-08 and Q-type-09 each changed the right values at once, and the change reports ("tokens: 111 values change") made cause and effect visible.
- **On-colour text is automatic** once the brand is right: dark on yellow and cyan, white on magenta and terracotta, with no hand tuning.

### I worked around it (each recorded in the piece's notes)

- Set `raw.brandColor` back by hand (01, 04); accepted the darker brand in 03.
- Raised the body size and lowered the ratio (03, 04); `overrides.type.displayReach 5` (04).
- `raw.secondaryColors` for cyan and magenta (04), found by reading engine.py.
- Outside the tokens on purpose: the teal film grade and projector light (01), a white veil (02), the hard offset shadow (04), warm coloured shadows (03), backdrop art in all five.
- Wrote a render-based contrast check and a computed-size and loaded-face check, because the built-in checks could not see either.
- Mid-run owner rules (two fonts, named scale, no italic-serif highlight, clear tonal contrast): applied by hand to all four finished pieces and built into 05 from the start. 01 lost its mono and its italic gradient word, and its lit plan became a near-white screen with ink text instead of cream on brown; 02 lost its mono; 03's headings went lighter and the range ends stopped being brown-black on orange; 04 kept mono only for real data and dropped most of its 900 weights. Each change is listed in that piece's `notes.md`.

## Feedback recorded with `engine.py feedback`
26 items across the five `opendesigner/feedback.md` files (01: 10, 02: 4, 03: 4, 04: 5, 05: 3), each with an issue link that was printed and not posted.
