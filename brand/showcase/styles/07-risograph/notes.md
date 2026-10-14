# 07 Tessin & Ström: a risograph annual report section

**Direction.** Tessin & Ström is a fictional design-research consultancy in Copenhagen. Its 2026 annual report, chapter 03, presents an invented study: 412 hours in 14 outpatient waiting rooms in Denmark and Sweden, 1,860 timed waits, 96 exit interviews. People felt they had waited 61 minutes; the clock said 38. A 2026 pilot in six clinics (a live queue board and a text ten minutes before each turn) left the real wait almost unchanged (35 min) and cut the felt wait to 37. The page is printed, in spirit, on a two-drum duplicator: Medium Blue and Fluorescent Pink. The technique carries the finding: **pink is the felt wait, blue is the actual wait, and where they overprint is the part that was real.** Feel words: **vivid, detailed, credible**.

Render: 1440 x 900, scale 2 (`shot.png`), light paper by design (`data-theme="light"`).

## References (Mobbin, cited by URL only)
Mobbin has no true risograph web page. The grain example and the report structure come from the references below; the ink behaviour (overprint, misregistration, starved solids, drum banding) is from print practice.

| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/bde9e82a-b11e-446f-9858-76c20256b468 (AI in Design Report 2026, chapter opener) | A report chapter page: chapter number and title top left, an "in this chapter" list, a large printed-looking image. Our toc row and running head come from here. |
| https://mobbin.com/sites/sections/a5ae62f7-16c6-40e0-ab62-cbef4ec73817 (AI in Design Report 2026, block chart) | Two years as overlapping blocks with the number inside. Became the overprinted felt and actual bars. |
| https://mobbin.com/sites/sections/2e102d3e-9c17-456e-af13-61468986fd1d (AI in Design Report 2026, methodology) | Method stated plainly with sample sizes, on a strict grid with rules. Our method note and n values. |
| https://mobbin.com/sites/sections/0a98e178-0bd4-427b-82af-b1289b0db60e (Dropbox, More Connected) | What real grain looks like on web: speckled solids in a few spot colours. (Its orange and brown palette was not used.) |

## System (engine)
```
sketch --name "Tessin & Ström" --brand "#3255A4" --audience regular --platforms web --feel vivid,focused,credible --theme system-light-dark --surfaces "annual report:read" --delegated all
  -> WARN rich vs minimal pull expression and colorfulness apart
set macros ["bold","rich","authoritative"]; taste.feelWords ["vivid","detailed","credible"]   (conflict resolved by hand)
set raw.secondaryColors ["#FF48B0"]; raw.accentCount 2     (Medium Blue + Fluorescent Pink, the two drums)
set answers.Q-dir-01 "flat2"; raw.textFace "Archivo"; raw.displayFace "=textFace"; raw.fontLicence all true; raw.marketingSurfaces true
build -> no errors, 0 warnings
```

| Dial | Value | How it expresses risograph |
|---|---|---|
| expression | 70 | The overprinted numerals are the art |
| brandPresence | 60 | Blue carries every word; pink marks the felt wait |
| density | 58 | A report page: two text columns, a chart, stats, method |
| energy | 35 | Calm reading pace |
| roundness | 0 | Print: square everything |
| depth | 0 | Ink on paper |
| colorfulness | 50 | Two inks and their overprint, nothing else |
| warmth | 45 | Neutral paper (25 gave a blue-white screen grey; higher would drift to cream) |

**What the dials cannot express:** the spot-ink model (two named inks, overprint by multiply), misregistration (pink drum offset 3 px right, 2 px down, 0.12°), starved-ink voids and drum banding (SVG turbulence filters), paper tooth, and the rule that small type gets a fine filter while solids get the heavy one. The engine nudged Fluorescent Pink from #FF48B0 to #fb4faf in the accent2 ramp; I used the token, but a spot ink should stay exact.

## Fonts and type scale
Archivo only (SIL OFL; width 62 to 125). Numerals at width 62 and weight 800, title at width 88 and weight 400, stats at width 80 and 700.

| Role | Size | Use |
|---|---|---|
| Art | 440 | "61" and "38" (outside the scale on purpose) |
| Headline | 51 | Chapter title, regular weight |
| Title | 38 | Stats |
| Body large | 21 | Standfirst, with 61 minutes and 38 in bold |
| Body | 16 | Columns, chart labels, legend |
| Label | 12 | Running head and foot, toc, captions, method |

## Outside the tokens, on purpose
- 440 px numerals (art); misregistration offsets; the two SVG ink filters and the paper-tooth texture (a data-URI SVG noise, no image file).
- `engine.py review`: 14 raw sizes left (fixed frame, bar heights, column widths); the px-margin standard breaks it found were moved to rem.

## Checks
- `engine.py validate`: no errors, 0 warnings.
- `preflight.py html`: 1 error, the M9 Google Fonts false positive; it read only the 440 px numeral size.
- Contrast on paper #f3f4f5: blue text 6.4:1. Pink (2.8:1) is never used for text: only for the 440 px numerals, bars and the legend swatch, each labelled in blue. The overprint violet is darker than either ink.
- The numerals are `aria-hidden`; the standfirst says the same numbers in words.

## Self-audit
Compared at 1440 with the three AI in Design Report pages.
- **Round 1, score 4.** The idea worked on first render, but the heavy ink filter on 12 and 16 px type made it blotchy and the running-head rules looked broken; "61" and "38" overlapped so much they read as "6138"; the chart labels said "61 · 38" without saying which was which.
- **Round 2, score 4.5.** Two filters: fine voids for type, heavy starvation for solids; numerals enlarged to 440 and staggered further down; labels now "61 felt · 38 actual"; track narrowed so labels fit.
- **Round 3, score 5.** Added drum banding to big solids (first try was too strong and read as video scanlines; softened to a slight density drift); spaced the arrow in "4.1 → 1.6%"; spacing moved to rem.
- **Tells checked:** grain here is the medium, not a stand-in for an asset; every printed mark is data or text; no invented proof; two inks, no third colour. **Final score: 5.**

## The style: risograph
- **Plain words.** The look of pages printed on a Risograph, a stencil duplicator: one flat, bright ink per drum, slightly off register, grainy, on uncoated paper.
- **What defines it (checkable).** Two or three spot inks, often fluorescent; colours mix only by overprinting (multiply), making a third tone; one ink slightly misaligned; solids with tiny voids and uneven density; uncoated paper texture; tints made of halftone or dither, not gradients.
- **How it goes wrong.** A grain filter over a normal design; more than three inks; gradients; perfect registration; noise so heavy small text cannot be read; using riso pink for body text; cream paper with brown and orange.
- **How I kept it premium.** Overprint carries the meaning (felt vs actual); two inks only; small text stays crisp; the report has a real method note with n values; one family in several widths does all the typography.

## Process findings
1. **No spot-ink or paper model** in the engine; a spot ink is nudged off its exact hex (feedback: gap).
2. **Macro conflict without a way out in `sketch`**: had to set `macros` by hand (feedback: confusing).
3. **Print-native styles fight the light/dark standard** (feedback: idea).
4. Helped: `raw.secondaryColors` and `accentCount 2` gave a clean two-ink system; the warmth dial found a neutral paper in one move; Archivo's width axis meant one font could do numerals, title and text.
Renamed from Halde & Ström to Tessin & Ström on 2026-10-14: 'Halde' was already the architecture hero's name (reused invented data).
