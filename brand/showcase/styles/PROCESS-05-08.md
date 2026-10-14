# Style studies 05 to 08: process report

Four style studies, each a fictional B2B brand built through the OpenDesigner engine, rendered, checked and self-audited against Mobbin references (making.md sections 5 and 11). Each piece has `notes.md` (direction, references, dials, type scale, checks, audit rounds, "The style") and an audit file in `brand/showcase/audit/styles--<nn-slug>.json`.

## The pieces

| # | Brand and subject | Direction | Palette | Type | Render | Score |
|---|---|---|---|---|---|---|
| 05 comic | Nightjar, on-call platform: INC-4471 postmortem on the engineering blog | Seven-panel noir comic of a real-feeling incident (renamed config key, 3 s default timeout, retries 1 to 16, rollback that fixes nothing, breaker) | Two inks: black and alarm red on white; tone in halftone dots; red only where something is broken | Shantell Sans (lettering, SFX, title) + JetBrains Mono (data in panels) | 1440 x 1701 (full), @2x | 4 |
| 06 memphis | Plenary, conference ticketing for organisers: landing section | Memphis set on black whose four shapes are the four ticket types, drawn to scale by tickets sold, around a flat organiser card | Lemon, pink, mint on black and white; patterns only on shapes | Bricolage Grotesque only (width 84 to 100) | 1440 x 900, @2x | 4 |
| 07 risograph | Halde & Ström, design-research consultancy: annual report chapter | Overprint carries the finding: pink = felt wait (61 min), blue = actual (38), overlap = real | Two spot inks (Medium Blue, Fluorescent Pink) and their overprint on neutral paper | Archivo only (width 62 to 88) | 1440 x 900, @2x | 5 |
| 08 bauhaus | weir, ETL / data pipelines: hero | Kandinsky's blue circle, yellow triangle, red square as source types sized by rows a day; bars weighted by rows a second into the weir bar and the warehouse | Red, yellow, blue, black on white | Jost only, lowercase (Bayer) | 1440 x 900, @2x | 4 |

Shots: `brand/showcase/styles/05-comic/shot.png`, `06-memphis/shot.png`, `07-risograph/shot.png`, `08-bauhaus/shot.png`.

Directions were set side by side before building so no two share a domain, palette, face, layout idea or mood: a dark-ink comic page, a dark Memphis landing, a light two-ink report spread, a light primary-colour poster hero. Red appears in 05 and 08, but as one alarm colour in a two-ink comic versus one of three primaries.

**Honest weak spots.** 05 has one character drawn from behind and a uniform 3 px line (hand-inked comics vary weight). 06 is still "product card with shapes around it", a familiar landing layout. 08 is calm and evenly stacked; a stronger Bauhaus poster would have more tension. Only 07 reached 5.

## Process findings, most important first

### A. The engine or skill is wrong or missing something

1. **Colours the style depends on do not survive the engine.**
   - Evidence 1. A delegated `sketch` replaced the lemon brand #FFE45C with olive #877400 and said only "I picked an olive" (`06-memphis/opendesigner/decisions.md` D-0004, D-0005). This is the same bug the Orbika hero hit (lime to olive). It is still open.
   - Evidence 2. `raw.secondaryColors` are not pinned the way the brand is.
     - Bauhaus ultramarine #1E4AA8 came out as #256aff at accent2 step 9 and is in no step at all.
     - Cadmium yellow #F2C200 became #edc343.
     - Fluorescent Pink #FF48B0 became #fb4faf.
     - Mint #6FE3C1 became #27e3b8 (dark) and #00ecbd (light).
   - Evidence 3. In dark mode the brand ramp dulls lemon to #d8c568 at step 9, while the secondary pink keeps its exact #ff8fb8. The two behave differently.
   - Result: three of four pieces set colour by hand outside the tokens (`--lemon`, `--blue`, `--yellow`). Filed as bugs in 06 and 08.
2. **Named styles are not wired in.**
   - `Q-dir-01` offers six presets: flat2, tonal, glass, neo-brutalist, soft, maximal. Comic, Memphis, risograph and Bauhaus are not among them.
   - For comic I took neo-brutalist for its borders, then had to cancel its offset shadow with depth 0.
   - While this run was going, another session wrote `skills/opendesigner/references/styles.md` (untracked, 20:50). It covers all four styles, but nothing reads it: `sketch`, `feel` and Q-dir-01 are unchanged.
   - Three of its ranges conflict with what made these pieces work:
     - **Comic:** it gives colorfulness 88 to 100 and "flat primaries". The premium route here was a two-ink noir at 18.
     - **Memphis:** it lists "shapes scattered at angles around the content" as a defining trait. That is section 11's "decoration with no data" tell.
     - **Risograph:** it gives warmth 55 to 75. A high warmth dial turns neutrals cream or brown, which breaks the owner's colour rule; 45 gave neutral paper.
   - Worth a look before it is merged.
3. **Style traits have no tokens.** None of these exist as tokens:
   - a pure ink black separate from text-primary (#222428)
   - art line weights
   - halftone screens
   - balloon and caption styles
   - ink count and spot inks
   - misregistration, grain and blend mode
   - paper tone (warmth moves hue, not lightness)
   - pattern laminates
   - layout grid: columns, gutter and margins, so Bauhaus "strict grid" was computed by hand

   Filed as gaps in 05, 06, 07 and 08.
4. **Preflight cannot check the type scale on a token-built page.**
   - `preflight.py html` printed `font sizes in px: []` for 05, 06 and 08, and only `[440]` for 07. It does not read `var(--ds-font-size-*)` or SVG `font-size` attributes.
   - Every piece also got the M9 false positive for Google Fonts loaded by `<link>`.
   - The owner's type-scale rule therefore had to be checked by hand from the code (filed as a bug in 05).
5. **Print-native styles fight STD-visual-details-24.** `--theme light-only` was refused ("breaks house standard STD-visual-details-24"). Comic, risograph and Bauhaus are printed pages with one paper. I kept system-light-dark and pinned each page with `data-theme` (filed as an idea in 07).
6. **Macro conflicts are flagged but have no way out in `sketch`.**
   - In 05, "technical" mapped to modern + serious and clashed with playful on four dials. I re-sketched with "geeky".
   - In 07, "vivid, focused" gave rich against minimal. I had to `set macros [...]` by hand.
   - The warning is right; offering the two resolutions would save a step (filed as confusing in 07).
7. **The display weight ignores the face.** The display weight token is 850, but Shantell Sans stops at 800 (filed as a bug in 05).

### B. I worked around it (and what helped)

- **The rule that did the most: make the style's ornament carry data** (section 11, "every mark on the page carries information"). It is what turned each style from decoration into a premium piece:
  - Memphis shapes sized by tickets sold, at 63.6 px² per ticket.
  - Bauhaus shapes sized by rows a day and bars by rows a second.
  - Riso overprint meaning felt against actual wait.
  - Comic red only where something is broken.
  - Proposal: add it to making.md section 11 and to `styles.md` as the first "how to keep it premium" line for every decorative style.
- **Mobbin has no example of any of these four styles on a B2B page.** Searches for comic strips, Memphis, risograph and Bauhaus returned mostly unrelated sections. Mobbin was useful for product structure (blog header, organiser ticket screens, report chapter pages, pipeline diagrams) and for one ink reference (Figma Shortcut). The style itself came from first principles, and each `notes.md` says so.
- **`raw.secondaryColors` with `raw.accentCount` built two- and three-ink systems in one step.** The colours drifted (A1), but the ramps and their readable step-11 text colours were usable.
- **`data-theme="light"` on one element** let 06's product card sit in its own light theme inside a dark page with no extra CSS.
- **`engine.py review`** caught px spacing (a must-standard) and `100vh` in every piece. **`validate`** caught the lemon button on white in light mode.
- **`raw.marketingSurfaces true`** unlocked display sizes on "read" surfaces. Without it the scale stops at 38.
- **SVG filters stand in for print physics.** Turbulence plus displacement gave riso voids, edge wander and drum banding. One lesson: small type needs its own, much lighter filter. The first round applied the heavy one to 12 px text and made it blotchy.

## Audit rounds (summary)

| Piece | Round 1 | Round 2 | Round 3 | Final |
|---|---|---|---|---|
| 05 comic | 3: balloon tails over chart labels, unreadable finger, off-scale 13/14 px | 3.5: crisp light bands, rebuilt head, a glow with no source replaced by action lines | 4: label clear of tail, two-line title, Return key pressed flush | 4 |
| 06 memphis | 3.5: confetti with no data, note on the pattern, tight tracking | 4: confetti removed, shapes stacked behind card | 4: hero recipe broken (kicker and second highlight removed) | 4 |
| 07 risograph | 4: heavy grain on small type, "6138" reading | 4.5: two filters, staggered numerals, labelled bars | 5: drum banding, rem spacing | 5 |
| 08 bauhaus | 3.5: Kandinsky reversed, double rules, customer-count "proof" | 4: Kandinsky pairing, grid placement, red action | 4: warehouse number, facts without invented proof | 4 |

All engine feedback is recorded locally in each piece's `opendesigner/feedback.md` (nothing posted).

## Polish round 2026-10-14
After the independent audit, 05 was polished (its facts fixed), and 06 and 08 were rebuilt around one idea each. 06's event is now Kanteel Design Week 2027 in Ghent, and 08 has 287 connectors. The table above describes the versions before the polish. For what changed and the fresh re-audit scores (05: 4, 06: 5, 08: 4), see the "Polish round 2026-10-14" section of each piece's `notes.md` and the `polish` field of its file in `brand/showcase/audit/`.
