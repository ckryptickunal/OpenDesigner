# Style studies 01 to 04: process report

Four style studies of fictional B2B products, each built through the OpenDesigner engine, rendered at 1440 x 900 at scale 2, checked, and self-audited against Mobbin references (making.md sections 5 and 11). Each piece has `notes.md` (direction, references, dials, type scale, checks, audit rounds, "The style") and an audit file in `brand/showcase/audit/styles--<nn-slug>.json`.

## The pieces

| # | Brand and subject | Direction | Palette | Type | Render | Score |
|---|---|---|---|---|---|---|
| 01 glassmorphism | Corvale, subscription billing: revenue overview | Frosted panes over a real dusk photograph; the summit stands in the open band and its ridge runs on behind the glass | Teal photo, white glass at 5 to 11%, one mint for money going up, coral for money lost | Manrope only | 1440 x 900, @2x | 4 |
| 02 neumorphism | Ouvra, building management: Level 6 East climate panel | Soft extruded controls around a 16 to 28 °C dial; pressed in means on | Cool grey-blue monochrome (#e7ecf4), ink text, one cobalt | Outfit only | 1440 x 900, @2x | 4 |
| 03 claymorphism | Wayfold, people ops: a new hire's first week | One clay object (the badge on its lanyard, which is also the next task) beside a grouped checklist | Lilac-white ground, violet clay (done, progress), lemon clay (next) | Bricolage Grotesque only | 1440 x 900, @2x | 4 |
| 04 skeuomorphism | Fenmoor, audio post-production: STEM-8 console plugin | Eight stem strips and a loudness master in brushed aluminium and anodized graphite | Graphite and aluminium; cyan only on backlit LCDs; LED green, amber, red | Barlow Condensed (legends) + Barlow (values) | 1440 x 900, @2x | 5 |

Shots:
- `brand/showcase/styles/01-glassmorphism/shot.png`
- `brand/showcase/styles/02-neumorphism/shot.png`
- `brand/showcase/styles/03-claymorphism/shot.png`
- `brand/showcase/styles/04-skeuomorphism/shot.png`

Directions were written side by side before building. The four pieces differ in domain, typeface, palette and structure:
- a dark photo dashboard;
- a light monochrome control panel;
- a light two-column onboarding page with one object;
- a dark horizontal hardware strip layout.

01 and 02 both use a card grid. To keep them apart, 02 is built around a single dial with a rail, and 01 around a photograph.

**Honest weak spots:**
- 01's mountain photo behind a finance dashboard is a showcase conceit (the "workspace backdrop" setting is the excuse).
- 02 uses the same soft treatment on every panel, and a real BMS would be denser.
- In 03, the clay lives in the coloured parts; the white task cards read as soft UI.
- 04 is the only 5. Its weakness is identical knob caps, and the drag alternatives that are noted but not wired.

## Process findings, most important first

### A. The engine or a skill is wrong or missing something

1. **Named styles do not reach the tokens, even the two that have presets.**
   - Q-dir-01 offers `glass` and `soft`, but neither produces its style.
     - `glass` gives Apple's control material: `color.surface.glass` is `rgb(34 37 43 / .72)` and "never content" (`01-glassmorphism/opendesigner/build/css/tokens.css`). Glassmorphism puts content on clear glass.
     - `soft` emits the same one-way drop shadows as flat (`--ds-elevation-shadow-1..6` identical in form; `surface.raised` is white) and only adds a lint warning. Picking it also left depth at 15 (`02-neumorphism`, `engine.py resolve`).
   - Clay and skeuomorphism have no option at all; I used `tonal` for 03 and no preset for 04.
   - Result: the look of every piece was hand-built. `engine.py review` counts the hard-coded values:
     - 01: 41 (23 glass alphas).
     - 02: 28.
     - 03: 7, after moving the art colours onto tokens.
     - 04: 64 (24 of them material shadows).
   - Missing tokens:
     - content-glass fill and rim;
     - paired highlight and shade plus an inset "pressed";
     - a three-layer clay elevation with a capped highlight;
     - material tokens (metal, LCD glass, lit and unlit LED).
2. **No tool checks text against what is actually behind it.**
   - `validate` checks roles against solid surfaces, and preflight only reads CSS. Both passed every one of these real failures:
     - 01: 13 text runs, worst 2.47:1, "Active subscriptions" over the snowy ridge.
     - 03: "Add to calendar" at 4.31:1, where a 45% clay highlight lightened the violet.
     - 04: LCD captions at 4.33 to 4.41:1 and a graph label at 1.03:1.
   - I caught them with a small rendered-pixel check: hide all text, re-render, compare each run with the brightest (or darkest) 5% of pixels in its box. All four pieces now pass (119, 116, 50 and 287 runs, 0 failures).
   - For glass, clay, photos and gradients this check is the difference between passing and failing. It belongs in preflight (`opendesigner-review`'s probe could carry it).
3. **`sketch --delegated` darkens light brand colours** so white text passes, and says only "I picked a teal".
   - Mint #5CE1B4 became #008564 (01) and cyan #38D5F2 became #008195 (04). Both are recorded as D-0008 in each piece's `opendesigner/decisions.md`.
   - The same thing happened to Orbika's lime (heroes) and to Memphis's lemon (06, per `PROCESS-05-08.md`).
   - On a dark system these colours want dark on-text, not a darker brand. Fixed each time with `set raw.brandColor` plus `flags.brandExact`.
4. **Feel words push the neutrals beige, against the owner's colour rule.**
   - "soft" (02) and "friendly" (03) map to the friendly macro, which set warmth to 80.
   - Tested on a copy of 02's state, neutral step 3 at each warmth: 22 gives #e7ecf4, 40 gives #eaebee, 50 gives #ebebeb, 60 gives #edebea, 80 gives #efebe8.
   - In 02 the word was about material (soft as in pillowy), not personality.
   - Warmth had to be set by hand to 22 and 30.
5. **Warnings that cannot be answered,** which teaches people to ignore warnings:
   - A dark-only theme still writes a light block, and validate warns about light-mode contrast (01, 04).
   - Macro-conflict warnings stay after the conflicting dial is set by hand (02: roundness; 03: expression and colorfulness).
   - The neumorphic "fails 3:1 by design" lint stays after a 3.05:1 rim was added to every shape-only control (02); there is no way to record the mitigation.
6. **Inputs that are silently ignored or misread:**
   - `raw.secondaryColors` does nothing until `raw.accentCount` is 2 (03).
   - `raw.monoFace "=textFace"` is written literally into the CSS: `--ds-font-family-mono: =textFace, ui-monospace…` (01).
   - The feel word "precise" is unknown (01).
7. **Ramp and documentation slips:**
   - The lemon accent2 tints (steps 2 to 7) are cream and beige (#f7f4eb, #f1ebd9, #ece3c6) (03).
   - DESIGN.md drops alpha in the dark column (`surface.glass` shown as #22252b) (01).
   - `review` suggests `radius-container` (24 px) for 3 to 6 px radii, and spacing tokens for control sizes (02).
   - Preflight M9 still reports Google Fonts links as missing faces (all four).
8. **`skills/opendesigner/references/styles.md` exists but nothing reads it.** It is untracked and was written during this run by another session. Its ranges disagree with what worked here:
   - Clay: warmth 60 to 80 (beige, see 4) and "start from soft" (brings the neumorphic lint and colorfulness 20).
   - Neumorphism: "no borders and no outlines" as a defining trait, while accessibility needs rims, and 02 shows the look survives them.
   - Skeuomorphism: roundness 48 to 80, density 30 to 50 and brandPresence 70 to 90 describe consumer skeuo (wood, leather, a turntable). A pro hardware panel worked at 15, 85 and 30.
   - Its glass entry says "never on reading surfaces, not for card grids", which is exactly what this brief asked for. A style guide needs a "when the brief asks for it anyway" path: dimming, worst-pixel contrast, a fallback.

### B. I worked around it

- **Materials:**
  - Paired shadows, clay layers, glass fill and rim, metal, knurling, LCD and LEDs were hand-built.
  - Every flat colour still points at a ramp token: neutral, accent, accent2 and status steps through `color-mix` and `var(--ds-*)`. This includes the SVG art in 03, through `style` attributes.
- **Contrast:** a scratch Playwright script, not shipped, compared text with rendered pixels.
- **Colour fixes:**
  - Brand colours restored with `brandExact`.
  - Warmth set by hand.
  - `accentCount` set so the second colour exists.
  - `monoFace` named in full.
- **Standards:** `review` caught `100vh` and 1 to 3 px spacing in all four pieces. They were fixed with `100dvh` and `--ds-space-2` or `--ds-border-width-1`.
- **Data:** every figure was cross-checked. MRR movements add up, the loudness reading sits inside its spec, and task counts match the progress bar. Two data clashes in 02 were found and fixed in round 3: a duplicated 62%, and a peak bar that disagreed with its caption.

### C. Running many builders at once

- **The scratchpad is shared between parallel sessions,** and that broke this run twice.
  - First, another session overwrote my `scratchpad/dials.sh` with a version that reads stdin. My dial settings for 02 then silently did nothing: `resolve` still showed expression 0 and warmth 80 after the call.
  - Later the whole scratch folder I had made was deleted mid-run, taking the contrast script with it.
  - Each builder needs its own named scratch folder, and the "delete scratch" rule should apply to a builder's own folder only.

### What helped

- `pick Q-dir-01 glass` plus depth above 80 gave the blur, the 35% dimming rule and the reduced-transparency fallback. The house rule against stacking translucent panes caught the tooltip.
- The dense audience (04) and density 30 (03) produced type scales that needed no tuning. The dense scale's 12 px floor already meets preflight's web minimum.
- The status ramps gave alarm text and LED colours that pass on both light and dark grounds with no edits.
- The neumorphic lint and the stage file's advice ("every clickable part needs added borders to reach 3:1") pointed straight at the real problem in 02.
