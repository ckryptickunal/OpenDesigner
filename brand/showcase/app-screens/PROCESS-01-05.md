# App screens 01-05: process report

Five iOS screens, each a fictional product made end to end through OpenDesigner: Mobbin references, `engine.py sketch`, dials and answers, `build`, an HTML screen on the generated `--ds-*` tokens, renders at 390 × 844 with `--scale 3` (1170 × 2532 PNG), then `validate`, `review`, `preflight` and the checklist. Each piece folder has `notes.md` (references, commands, scale, checks, findings) and `opendesigner/feedback.md` (23 entries in total, nothing posted).

## The pieces, side by side

| # | Brand and screen | Mood and feel words | Palette | Type (two fonts) | Shape language | Image |
|---|---|---|---|---|---|---|
| 01 | Halden Private, private-banking home | quiet wealth; premium, calm, trusted | green-black #121614 to #374d43, gold #C9A86A, ivory | Bodoni Moda (display numerals, wordmark) + Inter | 4 px tailored corners, hairlines, guilloche, a metal card | metal card and guilloche in CSS/SVG |
| 02 | Lullwater, sleep-story session | dusk over still water; calm, gentle, dreamy | indigo, rose #C77DA8, lavender #7E6CC9, peach #E8A48A | Instrument Serif (timer, title) + Instrument Sans | circles and pills, frosted glass | canvas sky, breathing orb, reflection, grain |
| 03 | Larder, recipe detail | cooking magazine; warm, editorial, rich | paper #f7f4ee, ink #262420, tomato #C8401F, olive | Fraunces + Libre Franklin | printed double rules, 2 px corners, a red ticket | Unsplash photo (Kerri Leung); first version painted in canvas |
| 04 | Voltfield, live interval run | stadium at night; energetic, bold, techy | true black, acid lime #D4FF3A, pink #FF2E63 for zone 5 | Archivo at 62-75% width + JetBrains Mono (data only) | 0 px, chamfered cuts, skewed chips, a 39 px grid | SVG heart-rate trace by zone |
| 05 | Aerlo, boarding pass | first minute of a flight; airy, crisp, trustworthy | white ticket, sky blue #2A66E8, pale sky #7CC4FF, indigo | Sora + DM Mono (codes only) | perforated ticket with punched notches, pills, dot grid | Unsplash header photo (Nicholas Szewczyk) + SVG dot-matrix route map |

All render at 390 × 844 pt, scale 3. Shots: `0N-*/shot.png` (03 also keeps `shot-painted-v1.png`, the painted version). No second screens: I spent the time on revision rounds instead.

Type scales follow Apple HIG Dynamic Type roles after the owner's mid-run rule (each piece's `notes.md` has its table): 5 or 6 sizes per screen, neighbours at least about 13% apart, nothing under 11 pt, plus one custom display size where a hero number needs it (52, 95, 169).

## Findings, most important first

### The engine or a skill is wrong or missing something

1. **The sketch overwrites an explicit brand color.** With `--brand ... --delegated all`, three of five brands were replaced by a darker "readable shade": gold #C9A86A became #8f7032 "an olive" (01, `decisions.md` D-0005), peach #E8A48A became #a4654d "a brown" (02), acid lime #D4FF3A became #677e00 "a green" (04). Only the two brands that already carried white text survived (03 red, 05 blue). All three light colors carry dark text at 7-18:1, and the Q-color-01 stage file itself says a light brand should switch its button text to dark. `pick Q-color-01 keep-hex` afterwards does not restore the hex; I had to `set raw.brandColor` again each time.
2. **keep-hex only pins the light ramp.** In dark mode the brand is dulled (`DARK_ACCENT_CHROMA`): the lime #D4FF3A is #b6d269 at dark step 9, and `bg.brand` points at it. A neon or gold brand cannot be exact where it is most visible. Workaround: `--ds-color-brand-seed` (04).
3. **No Apple HIG (or Material) named type scale, and hand-tuning is heavy.**
   - The CSS scale is a ratio formula (body.sm 14, title 21/27, headline 33).
   - The Swift export maps the same styles to Dynamic Type (.subheadline 15, .title2 22, .largeTitle 34), so the CSS and Swift outputs disagree.
   - `Q-type-10 named` only records a rule.
   - To follow the owner's rule I added 8 `font.size` steps and replaced 11 text styles with full typography JSON in every system (scratchpad script, about 20 `set` calls per system).
   - `set text.body.sm.fontSize` is refused ("not a token path").
   - Formula steps cannot be removed (`set font.size.21 null` is a no-op), so validate then warns "12-15 text sizes".
   - Overriding a step in place keeps its old name (`font-size-14` holding 15 px).
4. **iOS body text drops to 14 px when Brand presence is 50 or more** (`platform.useNativeBaseSize` turns off), with 11 px labels. This happened in 01; fixed with `pick Q-type-08 17` in all five.
5. **A dial set after an answer silently undoes it.** In 02, `pick Q-depth-01 glass` sets depth 90; my later `set dials.depth 45` removed every glass token, and DESIGN.md then said both "Materials and glass" and "No materials or glass in this system". `set` gave no warning.
6. **The neutral ramp works against tinted surfaces.** The ramp ends cap chroma at 0.008 while the text steps get the most, so:
   - "Deep green-black" (01) and "cream paper" (03) need `raw.neutralBase` hacks plus `Q-color-14 alternating`.
   - Warm neutrals turn the text brown. 03 first had brown secondary text and a brown-black timer with orange on it, which the owner's rule forbids.
   - Nothing in validate warns about it.
7. **Weights do not follow the face.** A single-weight face (Instrument Serif, 02) gets heading 600 and display 700, which asks the browser for a faux bold.
8. **Secondary hexes are not exact under keep-hex.** In 03, olive #5F6B2E became #6c7d00, much more acid, because the ramp peak takes the dial's chroma when that is higher.
9. **Vocabulary gaps:**
   - 4 of the 15 feel words were unknown: dreamy, editorial, airy, crisp. The engine asked instead of guessing, which is right.
   - `OPEN_FONTS` does not know OFL faces like Bodoni Moda, so validate gave a licence warning until Q-type-02 was answered.
   - There is no 11 pt caption step.
   - There is no accent role for inverse surfaces.
10. **No contrast check for text over art or photos.** The guarantees cover generated surfaces 1-4 only. In 02 text.tertiary was 4.15:1 on the painted sky; in 05 the first photo crop put white text at 3.66:1. I caught both by sampling pixels from the render, not with any OpenDesigner tool.
11. **Preflight does not fit app screens:**
    - It has no app or iOS medium, so 11 pt tab labels and icon numerals are "errors for web".
    - It flags Google Fonts `<link>` faces as "no @font-face", sometimes one face of two loaded the same way.
    - Checklist item 10 ("loaded from a file you ship") contradicts BRIEF.md, which allows the `<link>`.
    - Its real catches were useful: tracking -0.035 and -0.04em, and `<br>` in text (04, 05).
12. **`engine.py review` is noisy.** 01's first pass had 64 findings.
    - It maps element sizes to spacing tokens.
    - It suggests `--ds-elevation-raised` for 1 px inset rings and engraved text-shadows, and calls neon glows "shadows" in a borders-only system.
    - It proposes `--ds-space-0` for a negative hit-area margin and `--ds-color-surface-raised` for `#ffffff` inside canvas code.
    - Its "write spacing in rem" standard conflicts with the generated `--ds-space-*` tokens, which are px.
    - `od-ignore` works well for keeping art values on purpose.
13. **The paint skill has no route for an in-app image.**
    - Slots are marketing film sizes (16:9), and even a still needs a film project with `npm install` and a Chromium download.
    - The skill says to ask before installing, which a subagent cannot do.
    - Its font rule ("ship the woff2") conflicts with the brief.
    - What helped: `paint.py brief` worked offline and gave nine good palette families from the tokens.
14. **Light-mode warnings are noise for dark-led products.** `dark-only` is refused by house standard STD-visual-details-24, so 01, 02 and 04 keep a light mode they never show. Validate then warns about it (the lime primary on white is 1.14:1).

### Where I worked around it (and what helped)
- Restored brand hexes by hand (01, 02, 04). Used `--ds-color-brand-seed` for the neon (04).
- Set `raw.neutralBase` for tinted neutrals, and `Q-color-14 alternating` for paper (03). This helped.
- `overrides.type.displayReach` gave real 52, 95 and 169 px steps inside the scale. This helped a lot: every hero number is a token.
- `Q-color-04 analogous` / `contrasting` plus `raw.secondaryColors` produced full rose, lavender, pale-sky and pink ramps. The 02 dusk sky and the 05 map stayed inside the system.
- The glass tokens (`surface-glass`, its fallback, `material-glass-blur`) and `ring-shadow` were exactly right for 02 and 05.
- `set` printing how many token values change, and `feedback` writing a ready issue link, made the loop fast.

## Honest assessment
- **Strongest:** 04, a clear single idea at arm's length. 05, after the photo header. 01, with its numerals and metal card.
- **02** is lovely but quieter. Its sky sits in the mid-tones, and the readable text depends on a bright-on-dark palette I checked by sampling.
- **03** looks most like a real product now, but its plate is a borrowed photograph. The painted version (`shot-painted-v1.png`) was more original and less appetising.
- **05:** the map's coastlines are hand-traced approximations, stretched vertically, and the 2D code does not scan.
- No piece has a second screen.
- Each piece had three or more full-size review rounds; the notes list what each round fixed.

## Owner's mid-run rules, applied to all five
- Two fonts per piece. Status bars no longer use the system font. 04 and 05 use mono only for data and codes.
- HIG roles and sizes as above, nothing under 11 pt; 02's 10 px icon numerals became 11.
- The italic-word highlights are gone:
  - 01: the wordmark's italic "Private"; italic "Holdings" and "Reserve".
  - 03: the red italic "&", italic "Ingredients", masthead and notes.
  - 03's title now highlights "Burnt tomatoes" by weight.
- 03's colors moved off brown: Warmth 85 to 55, a greyer neutral base, and the timer changed from brown-black to tomato red with white.
- Unsplash photos replaced the painted plate (03) and lead the boarding pass (05). Both are free-licence images, hotlinked and credited, not Unsplash+.
