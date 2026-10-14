# Components 06–10: process report

Five working, interactive web components, each presented as a 1440×900 component sheet (hero instance plus labelled states), rendered at scale 2. Every piece went through the full OpenDesigner path: Mobbin references, `engine.py sketch` + dials + typefaces + `build`, an `index.html` on the generated `tokens.css`, at least two render-and-fix rounds, `preflight.py` and `engine.py validate`, notes and `engine.py feedback`. Piece 09 also used the `opendesigner-illustrate` skill end to end. After the owner's mid-run type and colour rules, all five were revisited (changes listed at the end of each `notes.md`).

## The pieces

| # | Piece | Direction | Palette | Type (two faces) | Render |
|---|---|---|---|---|---|
| 06 | `06-data-table/shot.png` | Tarrow Freight: dense shipment table for dispatchers; sort, filter chips, row selection with a floating bulk bar, lane-progress cells, loading/empty/error | Light cool slate, near-black ink, one signal orange (#cc4b00) for selection, sort and the primary action | IBM Plex Sans + IBM Plex Mono (IDs and figures); scale 12/14/20/24/35 | 1440×900 @2 |
| 07 | `07-ai-composer/shot.png` | Oriel: research assistant's composer; source attachments (one uploading), @mention, Ask/Research/Draft mode, model menu, send/stop/streaming, error that keeps the draft, drop target | Parchment, brown-black ink (≈14:1), terracotta #b4532a | Newsreader + Instrument Sans; 13/16/20/39 | 1440×900 @2 |
| 08 | `08-music-player/shot.png` | Calamondin Tapes: indie label's embeddable player; generated cover art whose colours are sampled at runtime to paint the card, record sliding out of the sleeve, waveform scrubber with section markers, mini player, queue | Dark violet stage, art-derived pink/tangerine/violet, white text | Unbounded + DM Sans; 12/16/21/38/51 | 1440×900 @2 |
| 09 | `09-onboarding-stepper/shot.png` | Mossby: plant-care onboarding; vine progress line that sprouts a leaf per finished step, illustrated multi-select plant cards, "I'm not sure yet", phone variant, Continue states, all-set card | Warm white, near-black text, pastel sage / peach / lilac / butter, sage action #338355 | Fredoka + Nunito; 13/16/20/25/39/49 | 1440×900 @2 |
| 10 | `10-settings-terminal/shot.png` | rackhound: homelab settings in an amber-phosphor terminal; block switches, segmented controls, block-track sliders, hostname input, fan-curve preview, apply log, tmux status lines | Black #151515, grey unlit blocks, phosphor amber #ffb000, red for danger | JetBrains Mono + VT323; 12/14/20/24/29/76 | 1440×900 @2 |

All paths are under `brand/showcase/components/`. Every hero is interactive: real sorting and keyboard row selection (06), Enter to send / Esc to stop / Arrow-key mode switch / live model menu (07), keyboard-seekable waveform slider and play/pause (08), checkbox cards that update the Continue count (09), switches, radiogroups and sliders with live readouts (10). All use `:focus-visible` rings and switch motion off under `prefers-reduced-motion`. A Playwright pass confirmed every face loads and no page throws errors.

**Honest quality read.** 08 and 10 are the strongest marketing pieces (distinctive, striking at a glance). 07 is the most refined. 06 is credible and well crafted but, being a dense enterprise table, it is the least "wow". 09 is charming, but its plant drawings are third-party CC0 line doodles, not bespoke art, and their line weights vary a little.

## Process findings, most important first

### A. The engine or skill is wrong or missing something

1. **A delegated sketch silently replaces the brand colour you passed.** With `--brand` plus `--delegated all`, the engine swaps the hex for "a readable shade" so white text passes, and DESIGN.md says "Picked for you, not chosen by you". Evidence: `10-settings-terminal/opendesigner/decisions.md` D-0005 `raw.brandColor = "#9e6b00"`, reason "a readable shade of #ffb000 (an olive)". The same happened to #e8590c → #cc4b00 (06), #ff3d81 → #e2136a (08), #5fae7d → #338355 (09). A light brand (amber) never got the dark-text treatment Q-color-01 itself recommends until I re-set `raw.brandColor` with `--set-by chosen`. The hue names are also wrong: orange is called "a brown", hot pink "a crimson", amber "an olive".

2. **Preflight cannot see a tokenised page.** `preflight.py html` only reads px font sizes and literal family names. Every engine size is rem and every family arrives through `var()`, so the report says `font sizes in px: []`. The M8 minimum-size rule never fires on the engine's own 11px labels, and a fully tokenised page passes with 0 errors (09). At the same time, faces loaded from a Google Fonts `<link>` (which the brief allows) are flagged as M9 errors in 06, 07, 08 and 10.

3. **Three parts disagree on the smallest text.** `engine.py` hard-codes `min_size = 11` and the dense scale emitted 11px body-sm, label and code styles (06). Preflight errors below 12px and warns below 14px on the web. The owner's new rule follows Material (body 14–16). The documented fix exists (Q-type-08, `raw.baseSize 14`), but nothing in the dense path points to it.

4. **No component-level tokens or guidance for what I built.** The only component tokens are `component.toast.*`. A table, a composer, a player, a stepper, switches, sliders and segmented controls were all designed by hand on top of primitives. `pick Q-ai-01 chat` adds `prompt-input` to the inventory and DESIGN.md calls it "planned (tokens ready)" although no composer tokens exist. There is no state guidance for an AI turn of unknown length (send → stop → streaming → error that keeps the draft).

5. **The colour controls fight distinctive palettes.**
   - Colorfulness mixes "how many hues" with "how saturated the one hue is". The one-hue phosphor needed colorfulness 85 plus `raw.accentCount 1`; at 22 the amber became brown (10).
   - The dark ramp always desaturates the accent (#ffb000 → #eeb763), with no option to keep brand chroma for a neon or CRT look (10).
   - Three-accent harmony gives grey-teal and khaki at 24/36 of the primary chroma; pastel peach and lilac needed `raw.secondaryColors`, which no stage question asks for (09).
   - Warmth 88 tinted the greys pink toward the brand, and `pick Q-color-09 warm` then made them nearly grey. A real parchment needed `raw.neutralBase`, which appears in no stage file (07).
   - There is no slot for colour taken from content, such as a colour sampled from album art, and no rule for keeping text readable on it (08).
   - There is no divider role lighter than `border.subtle` (neutral 7 at warmth 30 is too heavy for row rules) (06).

6. **The Energy dial barely changes motion.** House standards lock the springs, the standard easing and the medium/long durations. Energy 20 (06) and energy 82 (08) produce identical spring tokens; only `duration.extra` and the heading weight move. DESIGN.md still describes energy as driving motion.

7. **Typeface handling.** Faces outside the short `OPEN_FONTS` list (IBM Plex Sans Condensed, Newsreader, Unbounded, VT323…) are listed as licence risks until `raw.fontLicence` is recorded. The heading weight (600–850) applies to serif and display faces alike, so an editorial serif came out too heavy (07).

8. **Feel vocabulary.** "editorial", "expressive", "precise" and "dense" are unknown. "retro" + "technical" raises four "playful, serious pull X in opposite directions. Pick which one wins" warnings. The warning names no command and stays after every dial is set explicitly (10).

9. **opendesigner-illustrate.**
   - Its `--dir` is the illustrations folder, while the engine's `--dir` is the state folder. Passing the same value dumped search files into `opendesigner/`, and `palette` then lost the tokens.
   - "potted house plant" matched birdhouses and houses for sale, and `--style flat` still ranked heavy line doodles first.
   - `fetch` exited 1 on success, and `apply --label` left the ledger rows "(unassigned)".
   - Recolouring only maps mono line art to neutral 1 and 12.

10. **Smaller issues.**
    - `--theme light-only` and `dark-only` are refused by a house standard, so the brief's own sketch command fails as written.
    - Depth 15 sets even `elevation.overlay` to zero, so floating bars and menus get no separation (06).
    - The light-mode contrast warning on an amber fill suggests a fix that would undo the brand pin (10).

### B. Where I worked around it (and how)

- Brand colour: re-set with `engine.py set raw.brandColor '"#ffb000"' --set-by chosen` (10). In 06, 08 and 09 I accepted the shifted shade, because it still read as the intended hue.
- Single theme: built with `system-light-dark` and rendered with `data-theme="dark"` (08, 10).
- Fonts: `raw.textFace`, `raw.displayFace` and `raw.monoFace`, plus `raw.fontLicence`; `raw.displayFace "=textFace"` and `pick Q-type-06 system-mono` to meet the two-font rule (06, 08).
- Body size: `raw.baseSize 14` (06); Q-type-08 is the documented route.
- Colour: `raw.neutralBase` (07), `raw.accentCount` + `raw.secondaryColors` (09), colorfulness 85 + `accentCount 1` (10). Where a role was missing I used ramp steps on purpose and named them in CSS, with a comment:
  - `--rule` (06)
  - pastel fills (09)
  - phosphor = light accent step 9 in the dark theme (10)
  - art-derived `--c1..--c3` at runtime (08)
- Serif weight: set by hand to 400/500 (07).
- Illustrations: moved the skill's files into `opendesigner/illustrations/`, passed `--tokens` on every call, and set `--od-illus-neutral-1` per card to tint the line art pastel (09). The skill's CSS-variable output made this easy, and it is its best feature.
- Preflight false positives: confirmed font loading with a Playwright check instead.

### C. What helped

- The density, roundness and depth dials map well to real decisions. Density gave the right control heights every time (24/32/40 dense, 40/48/56 airy), roundness gave matching radius roles (0, 12/16/24, full pills), and depth gave correct elevation.
- Validate's contrast checks (164–188 pairs per system) meant I never hand-checked a status or on-accent colour.
- The focus-ring, reduced-motion and feedback/enter transition tokens worked unchanged in five very different looks, from a CRT terminal to a pastel storybook.
- `build` is fast, and DESIGN.md says plainly what was picked and why, which is how the brand-replacement problem was found.
- Mobbin references were quick to find and taught concrete structure (filter chips, the send/stop swap, art-tinted players, escape-hatch onboarding, label-left settings rows).

## Feedback recorded

28 entries through `engine.py feedback`, written locally to each piece's `opendesigner/feedback.md` (06: 9, 07: 5, 08: 4, 09: 5, 10: 5). Nothing was posted.

## Environment note

The scratchpad directory is shared between parallel builders in one session. My first helper script (`dials.py`) was overwritten by the other builder's file with the same name mid-run. I moved my scratch files into a private subfolder (`scratchpad/c0610/`). 09's `index.html` was assembled from a template there (to inline the four recoloured SVGs); the result is self-contained and is the file to edit.
