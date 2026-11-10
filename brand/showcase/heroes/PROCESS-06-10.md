# Heroes 06-10: process notes (builder B)

## Directions, side by side (written before building)

| # | Brand (fictional) | Domain | Palette | Type | Layout idea | Shape language | Mood |
|---|---|---|---|---|---|---|---|
| 06 | Plumpot | Money app for teens | Candy pastels on cream, with a plum ink | Chunky rounded display, plain rounded body | Headline with a coin inside the words; a floating stack of tilted 3D cards and coins | Pills, big radii, soft inflated shadows | Playful, tidy, bouncy |
| 07 | Isobath Ocean Observatory | Ocean and climate data institute | Deep navy, cold cyan contours, one warm signal | Light display, mono for data | Full-bleed generated contour map; headline low left; a rail of live readouts | Hairlines, no radius, crosshairs | Scientific, calm, precise |
| 08 | Orbika | Satellite radio hardware | Chrome greys and acid lime | Very wide extended display | A chrome receiver built in CSS; full-width headline; pixel radio waves | Pill bezels, knurled knobs, pixels | Playful-tech, glossy, retro-future |
| 09 | Kumo Kōbō | Small ceramics workshop | Washi paper, sumi ink, one iron-red seal | Mincho serif (Japanese and Latin), quiet sans | Asymmetric: an ink bowl off-centre, vertical Japanese text, a small headline, lots of air | Brush edges, no boxes | Quiet, crafted, still |
| 10 | Orvita | Clinical AI platform for hospitals | White, clinical teal and blue, soft grey | Crisp grotesk, tabular figures | Headline left; a composed HTML dashboard bleeding off the right; a customer wordmark row | 4-12 px radii, 1 px borders | Trustworthy, crisp, credible |

No two share a domain, palette family, typeface, layout idea or shape language.

## The pieces

| # | Shot | Palette (from the engine) | Type (two faces each, final) | Sizes used | Render |
|---|---|---|---|---|---|
| 06 | `06-playful-fintech/shot.png` | Brand #7B3FE4; secondaries #FF6FB0, #FFC83D; cream neutral, plum ink at step 12 | Fredoka 700 (wide) / Figtree | 124 · 38 · 28 · 21 · 16 · 12 | 1440 × 900 @2x |
| 07 | `07-climate-observatory/shot.png` | Brand #3FC1D9, action #3FC1D9, dark-only; navy background by hand; coral `danger-dark-11` signal | IBM Plex Sans Light / IBM Plex Mono (data only) | 95 · 25 · 20 · 16 · 13 | 1440 × 900 @2x |
| 08 | `08-y2k-retrofuture/shot.png` | Brand #B8F400 (restored after sketch swapped it), chrome from cool neutrals | Michroma / Space Grotesk; the LCD is drawn dot-matrix art | 104 · 28 · 21 · 16 · 12 | 1440 × 900 @2x |
| 09 | `09-japanese-ceramics/shot.png` | Brand #A23A2A (seal only), washi neutrals via `neutralBase` | Shippori Mincho 400 / Zen Kaku Gothic New | 39 · 25 · 20 · 16 · 13 | 1440 × 900 @2x |
| 10 | `10-enterprise-health/shot.png` | Brand #0B7A85, secondary blue (needed `accentCount 2`), status ramps | Instrument Sans 400 and 650 / Geist Mono (data only) | 76 · 25 · 20 · 16 · 13 | 1440 × 900 @2x |

**Honest ranking:**
1. **07** is the strongest: generated bathymetry, a live-instrument feel, and nothing like a template.
2. **08** is a close second: the CSS receiver reads as a real object.
3. **09** is quiet and distinctive, though the bowl is ink-wash rendering rather than visible brushwork.
4. **06** is polished and joyful but closer to familiar fintech hero grammar.
5. **10** is the most conventional layout (headline left, product right, logos below). The product fragment is good, but it would not stand out in a gallery.

Every piece went through at least three look-and-fix rounds at full size, plus one more round after the owner's mid-run type and color rules. Each piece's `notes.md` has its references (Mobbin URLs), dials, departures from the tokens, checks and type scale.

## Process findings, most important first

### The engine or skill is wrong or missing something

1. **The generated type system can't produce what a hero needs, or what the owner now requires.**
   - The scale stops at 90 or 95px, even for `landing page:persuade` with expression 85–90. Every hero needed 104–124px set by hand (06, 08).
   - Heading weight bands are 600/650/750, so a light or regular display (07 at 300, 09 at 400, 10 at 400) always departs from the tokens. Owner rule: "Titles don't have to be bold".
   - The display weight token ignores the face's real range: 850 is asked for, but Fredoka and Michroma stop at 700 and 400.
   - Every build emits three face roles and eight sizes, with 14+ named styles and no "caption" role. The owner rule is two fonts and about six sizes with HIG/Material roles.

   Evidence: `--ds-font-size-90` is the top step in `06-playful-fintech/opendesigner/build/css/tokens.css`; levers.json `type.headingWeight` bands `[[0,33,600],[34,66,650],[67,100,750]]`; `--ds-font-weight-display: 850`.

2. **Brand colors get changed or lost without a clear message.**
   - `sketch --delegated all` replaced acid lime #B8F400 with olive #5f8000 (`readable_shade`, R44) so white text would pass. Lime carries ink at 11.8:1. The output only said "I picked a green" (08).
   - `raw.secondaryColors` was silently ignored at colorfulness 40, because accentCount was 1 (10).
   - With low colorfulness and an exact brand, the steps around the pinned red are grey. Hover (#5a504d) and link (#534a48) lose the hue (09).
   - The colorfulness dial doesn't touch a brand-seeded ramp. The dark-mode button became a muddy #418e9d until `primaryActionColor` was set (07).

3. **Tinted grounds and candy tints can't be made.**
   - Neutral ramp ends are capped at chroma 0.008, so a deep navy page is impossible. `neutralBase` #0E2A4A still gives #131519 (07).
   - Yellow tint steps lose chroma: seed #FFC83D gives tan #ebd9b3. A candy pastel butter is unreachable (06).
   - There is no chrome or metal material: `soft`/neumorphic is the nearest (08).
   - Shadows are always neutral, with no tinted option (06).

   `neutralBase` works well in light mode, though (washi in 09).

4. **The checks give false or blind results on a token-built page.**
   - `preflight.py html` M9 reports "no @font-face" as an ERROR for every Google Fonts `<link>`, which the brief allows: 1-3 false errors on all five pieces.
   - It counts only px sizes, so token rem sizes are invisible to M6 and M8 ("font sizes in px: []" on 07, 09 and 10).
   - Its M8 warns at 13px while the engine's smallest step is 13px.
   - `engine.py validate` checks light-mode pairs on a dark-only system (07: 2 warnings).
   - `engine.py review` suggests tokens by numeric coincidence: a 40px height becomes `space-40` instead of `size-control-sm`; an inset border becomes `elevation-raised`; a 280px blob radius becomes `radius-overlay`.
   - The rem-spacing standard (STD-accessibility-motion-13) flags 2px while `--ds-space-*` tokens are emitted in px.

5. **The CLI hides how to do basic things.**
   - Typefaces have no flag. `set textFace` fails; `set raw.textFace '"Figtree"'` works, but you only learn that from reading engine.py.
   - `sketch --theme light-only` is refused by a house standard, and the suggested `standard override` fails until `init` has run. The working order is init, then override, then sketch: three commands with no hint of the order (all five pieces).
   - Feel words: "tidy" maps to minimal and conflicts with playful, and `set raw.feel` silently does nothing (the fix is `set macros`). "precise" was dropped without a word (07).
   - `raw.monoFace "ui-monospace"` duplicates the generic in the stack.

6. **The open-font allowlist is too short.** Fredoka and Shippori Mincho (OFL, Google Fonts) are flagged as licence risks in DESIGN.md and the paint brief.

7. **opendesigner-paint has no light path for one painted still.**
   - It needs Node, npm, Playwright and ffmpeg installed with the owner's yes.
   - It has no ink-wash (sumi-e) style.
   - Its "brand-tint" family used the grey accent tint instead of the washi neutral.

   The brief itself was useful: palette families and the "one accent mark" idea shaped 09.

### Where I worked around it, and what helped
- **Worked around:**
  - Hand-set display sizes and weights.
  - The navy background and art washes by hand, marked `od-ignore`.
  - The lime brand restored with `set raw.brandColor`.
  - `accentCount 2` for the blue.
  - `primaryActionColor` for the dark-mode button.
  - Canvas painting instead of the paint engine.
  - LCD text as drawn dot-matrix art after the two-font rule.
- **Helped:**
  - The ramps are well balanced: purple, pink, plum ink, dark navy readouts, status pills at steps 3/11.
  - `surfaces app:operate` gave proper ring-plus-shadow elevations for product UI.
  - `raw.scripts Jpan` produced a `:lang(ja)` line-height rule.
  - `engine.py review` was the most useful check. It caught `100vh`, ambient infinite loops, raw px paddings and hard-coded colors.
  - The validate warning about a lime button on a light surface led to a better ink-outlined button.

Feedback was recorded with `engine.py feedback` (27 entries, local only) in each piece's `opendesigner/feedback.md`.

## Owner rules applied mid-run
- **Fonts:** 07 dropped Source Serif 4, 08 dropped Silkscreen and 10 dropped Instrument Serif. Each piece now uses two faces.
- **Highlights:** the one-italic-word highlight (07) and color-only highlights (06, 10) are gone. 06 uses a fill box, 08 kept its fill box, and 10 uses weight.
- **Type scales:** each piece's scale is written in its notes, with at most 6 sizes and none within 10%.
- **Color:** the 09 neutrals were pulled away from brown-olive (warmth 80 to 60, new `neutralBase`).
