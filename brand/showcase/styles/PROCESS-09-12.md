# Style studies 09 to 12: process report

Four style studies, each a fictional B2B brand built through the OpenDesigner engine, rendered at 1440 x 900 (scale 2), checked, and self-audited against Mobbin references at the same width (making.md sections 5 and 11). Each piece has `notes.md` (direction, references, dials and what they cannot express, type scale, checks, audit rounds, "The style") and an audit file `brand/showcase/audit/styles--<nn-slug>.json`.

## The pieces

| # | Brand and subject | Direction | Palette | Type | Render | Score |
|---|---|---|---|---|---|---|
| 09 bento grid | Holdfast, help desk for B2B support teams: feature section | Five tiles of real product: a 5 x 2 inbox sorted by SLA, a yellow SLA clock (14:32), a macro with variables, CSAT by week, a keyboard snooze menu | Neutral grey page, white tiles, ink, one sun yellow (#FFD23F) for "time is running" | Schibsted Grotesk only; 13/16/20/39/49/76 | 1440 x 900, @2x | 4 |
| 10 mesh gradient | Prill (named Assay until the polish round), AI evaluation platform: hero | A contained gradient plate drawn from the eval run's own 4,012 cases (score across, latency down, cyan v13, violet v14), labelled like a figure, with the 37 regressions drawn as dots; the run table flat in front | White page, ultramarine plate (#1b1370), brand violet (#6A4BFF) and cyan; red only for "Release blocked" | Funnel Display (300) + Funnel Sans; 12/16/21/67 | 1440 x 900, @2x | 4 |
| 11 terminal | coppice (named burrow until the polish round), branchable embedded SQL database: docs hero | A man page (COPPICE(1), NAME, SYNOPSIS with underlined arguments) beside a real session whose numbers add up and a box-drawn storage diagram; keys on every action | Ink on white paper, one signal red (#E0301E) for prompts, cursor and the branch | Lilex only (300/400/600); 12/14/17 + 40 display | 1440 x 900, @2x | 4 |
| 12 pixel art | Lampwright (named Signalfire until the polish round), a studio's live-ops console for its game Mossbank: dashboard header and KPI strip | The game's pixel key art (lanterns rising from a pier at night, 328 x 70 at 4x) as the event header; pixel type for the event title only; six KPIs, revenue per hour against last year, offers with item sprites | Slate shell (#191d23), night-indigo art, lantern gold (#FFC24B) for the event only, semantic green and red | Onest + Silkscreen (pixel, 16 and 32 only); 14/27 | 1440 x 900, @2x, dark | 4 |

Shots: `brand/showcase/styles/09-bento-grid/shot.png`, `10-mesh-gradient/shot.png`, `11-terminal/shot.png`, `12-pixel-art/shot.png`.

The four directions were written side by side before building: a light grey bento with one yellow, a white page with one deep gradient plate, a black-and-white man page with one red, a dark dashboard with gold. Different domains (support, AI evals, databases, games), different faces, different shape languages (24 px tiles, one plate, square frames, a pixel grid). 11 is deliberately the opposite of the existing amber-on-black rackhound terminal panel.

**Honest weak spots.** None reached 5. 09's section head (headline left, paragraph and link right) is conventional, and only the yellow clock tile is truly ownable. 10's violet and cyan field still sits in the colour family people read as "AI product", even though it is drawn from data. 11 is the quietest piece and has no single object only coppice could own. 12's pixel scene is clean but procedurally shaded, poorer than shipped pixel key art.

## Process findings, most important first

### A. The engine or skill is wrong or missing something

1. **A delegated sketch still swaps the brand colour, and in 12 it produced the exact colour family the owner bans.**
   - Evidence: `09-bento-grid/opendesigner/decisions.md` D-0005 `raw.brandColor = "#8f7200"` (from #ffd23f, "I picked an olive"); `12-pixel-art/.../decisions.md` D-0005 `"#996d00"` (lantern gold to a brown olive); `11-terminal/.../decisions.md` D-0005 `"#df2f1d"` (from #e0301e, harmless). Only violet (10) survived, because white text already passes on it.
   - Three of four pieces here, after Orbika, rackhound and 05 to 08. Fix in every case: `engine.py set raw.brandColor '"#…"' --set-by chosen`.

2. **The engine has no vocabulary for a named style, so every defining trait was hand-built.** Each `notes.md` has a "What the dials cannot express" paragraph:
   - bento: grid spans, one gap, tile fill hierarchy, a tile radius role (09)
   - mesh gradient: the gradient itself, its ground, grain, and where text may sit (10)
   - terminal: the character grid and glyph coverage of the face (11)
   - pixel art: the integer-scaled grid and a size grid for the pixel face (12)
   - The dials did carry the surrounding system well (roundness 0 / depth 0 for the terminal, roundness 62 / depth 8 for bento). A per-style checklist (traits, failure modes, which dials express it) is the missing piece. `engine.py feedback` recorded as an idea; `STYLE-VOCAB-PROPOSALS.md` in this folder (another builder's) covers the same need.

3. **No glyph-coverage check for a monospaced face, and it decides whether a terminal page works.**
   - Evidence: a Playwright width test (scratchpad, deleted): Martian Mono, the first choice, has no box-drawing, block or arrow glyphs; they fall back to another face at a different advance (24.08 vs 28.0 px at 40 px).
   - Of 24 other open monos, 10 lack them entirely and 2 partly.
   - Having the glyphs is not enough: at 3x zoom, Chivo Mono, Spline Sans Mono and Source Code Pro do not close a table at 14 px. Only Lilex and Geist Mono did.
   - Rackhound hit the same problem.

4. **No brand-gradient tokens, and nothing checks text on a gradient.**
   - The field in 10 (ground, two hues, peak, blur, grain) lives only in `index.html`.
   - `validate` passed with 0 warnings while the first score ticks sat at 1.75 to 2.32:1 on the cyan. That was measured from the render with PIL, then fixed with a solid axis strip.
   - "Brand gradients" is listed as a designer hook but has no token group or rule.

5. **The colour ramps fight saturated and tinted brands in dark mode.**
   - The dark accent ramp turns lantern gold #FFC24B into beige #e6bd77 at step 9 (12), as it turned rackhound's amber; I pinned `--ds-color-brand-seed` by hand.
   - The warmth dial runs from slate (#191d23 at 0) to grey (40). It cannot reach an indigo shell.
   - Its neutral point is also not where a person expects: warmth 20 ("cool") gave lavender page greys (#e7ecf4) in 09, and 40 gave true grey.

6. **The type scales miss the roles these styles need.**
   - 10: nothing between 12 and 16 for a dense eval table.
   - 11: the dense scale has no display size for a docs hero (headline set at 40 px, off-scale).
   - 12: no 8 px grid for the pixel face (Silkscreen at 16 and 32, off-scale).
   - 09: Schibsted Grotesk's tabular figures also widen `.` `,` `:`, which spaced the punctuation in body text ("keep .", "14 : 32") until `tnum` was limited to number columns.

7. **The checkers contradict each other or misfire.**
   - `preflight.py html` raised M9 "no @font-face" for every Google Fonts face in all four pieces, while `document.fonts` showed every used weight loaded.
   - `engine.py review` reads pixel-sprite strings such as `'...w....w...'` as "three periods in UI text" (12).
   - `review` flags every px spacing under STD-accessibility-motion-13 ("write spacing in rem"), then suggests `var(--ds-space-8)`, which `tokens.css` defines in px. After tokenising, the rule still reports 13, 8, 15 and 10 lines.
   - `sketch --theme light-only` is refused by STD-visual-details-24 even for a light marketing section, so 09 to 11 carry dark modes they never show.

### B. I worked around it (and what helped)

- **Brand swaps:** re-pinned with `--set-by chosen` in 09, 11 and 12.
- **Glyph coverage:** a 20-line Playwright script measured glyph advances and rendered test tables at 3x before committing to a face. That is two face changes (Martian Mono, then Chivo Mono, then Lilex) recorded through `engine.py set raw.textFace` with the reason.
- **Gradient contrast:** sampled the rendered plate with PIL around each label, then moved the labels onto solid ground.
- **Raw spacing:** converted every on-ladder spacing to `--ds-space-*` mechanically (22, 19, 20 and 38 values), then pixel-diffed the renders. They were identical except 11's blinking cursor.
- **Same-width audit:** making.md asks for the render beside three shipped references at the same width, but there is no tool for it. I composited each render with three Mobbin previews at 768 px in the scratchpad, judged, then deleted the sheets. A small `audit-sheet` helper would make this step routine.
- **Mobbin:**
  - Searches for the product type (support inbox, eval results, CLI docs, KPI strips) were productive.
  - Searches for the style word were not: "bento" returned mostly uniform card grids, and real asymmetric bentos were rare (Cycle was the clearest).
  - Mobbin reported high AI usage for this account during these searches.
- **What helped:**
  - The radius and space ladders fitted bento and a character grid without edits.
  - `elevation-overlay` gave the right card shadow over the gradient.
  - Semantic green and red in dark mode passed contrast first time (12).
  - Onest on the generated 14/27 steps made the KPI strip look shipped with no tuning.
  - validate's yellow-on-light warning (09) was a real catch.

## Audit rounds (summary)

Early-round scores were given afterwards from what each render showed; final scores were given against a same-width sheet with three references.

| Piece | Rounds | Scores | What changed most |
|---|---|---|---|
| 09 bento | 3 | about 2, then 3.5, then 4 | `tnum` limited to number columns; two-line regular headline (no bold last word); inbox trimmed so its footer shows; warmth 40 for true grey; macro card bleeds off its tile |
| 10 mesh | 4 | about 3, then 3.5, then 4, then 4 | Colour map rebuilt from navy-and-teal glow to an ultramarine ground with violet above and cyan below; 37 regressions drawn as dots; ticks and label moved onto a solid strip after contrast failures |
| 11 terminal | 4 | about 3, then 3, then 3.5, then 4 | Face changed twice for box-drawing (Martian, then Chivo, then Lilex); 40 px headline in a wider column for presence |
| 12 pixel | 3 | about 3, then 3.5, then 4 | Lanterns rebuilt as a rising plume in four sizes (was confetti); olive area fill and duplicate event border removed; actions moved off the moon's reflection |

## Polish round 2026-10-14
After the independent audit, 10, 11 and 12 were polished and renamed: Assay is an LLM-evaluation library, Burrow is LinkedIn's Kafka monitor and SignalFire is a venture capital firm. The table above describes the versions before the polish. For what changed and the fresh re-audit scores (10: 5, 11: 4, 12: 4), see the "Polish round 2026-10-14" section of each piece's `notes.md` and the `polish` field of its file in `brand/showcase/audit/`.
