# 01 Brask: giant wordmark footer

## Direction
Brask is a fictional independent creative studio (identity, type, motion) in Copenhagen, Lisbon and Mexico City. The footer is the last thing a prospective client sees, so it is the studio's signature: the name set edge to edge, oversized and cropped by the bottom of the page, with one invitation above it. Monochrome warm black and bone, one signal orange used three times only (the open-slot dot, the "Send it over." line, the full stop of the wordmark).
Feel words: bold, minimal, confident.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/ddfad441-10db-4949-9baa-299e7e0edeee — a cropped wordmark only works if the rest of the footer is tiny and quiet; the crop is what makes it feel like a sign, not a heading.
- https://mobbin.com/sites/sections/98fd09b2-7134-404b-a9df-d6d91c49ec54 — the info row is set in four small columns that snap to the same grid as the mark; small caps-size labels, no link colour.
- https://mobbin.com/sites/sections/23a43fc2-e616-4b49-945c-4a0dd97df268 — office cities with local time as a human detail; hairline rules carry the structure instead of boxes.

## System (engine)
```
python3 $E --dir .../01-brask-wordmark/opendesigner sketch --name "Brask" --brand "#ff4d00" --audience regular --platforms web \
  --feel bold,minimal,confident --theme system-light-dark --delegated all --surfaces "landing page:persuade"
```
- `--theme dark-only` was refused (house standard STD-visual-details-24). Used system-light-dark and pinned `data-theme="dark"` on `<html>`.
- `--delegated all` changed the brand hex to #d63f00 ("a readable shade", called "a red"). Set it back: `set raw.brandColor '"#ff4d00"' --set-by chosen`.
- Dials: expression 85 (the footer is the signature), brandPresence 85 (the name is the composition), density 30 (few links, lots of air), energy 70 (heavy, punchy type), roundness 0 (square, typographic), depth 0 (hairlines only), colorfulness 12 (monochrome plus one accent), warmth first 62 (45 gave a blue-grey neutral at hue 264; 62 moved it to hue 58), then 50 under the owner's colour rule (neutral black and white; see below).
- Typeface: `set raw.textFace '"Archivo"'` (SIL OFL, Google Fonts). The display role follows the text face.
- Build: no errors, 0 warnings, 5 notes.

## Build
- Every colour, space, size, weight, radius, border, focus ring and duration is a `--ds-*` token. The heading is `--ds-font-size-67`, labels `--ds-text-label-sm`, links `--ds-font-size-16`, email `--ds-font-size-21`.
- Outside the tokens, on purpose:
  - The wordmark size is fitted by script so its ink runs exactly gutter to gutter (canvas scan of the real glyphs, not the advance width), then cropped at 0.6 of the font size (0.74 on phones so it still reads). It is art, not a type-scale step.
  - `font-variation-settings: "wdth" 125` for the mark and `"wdth" 100` for the heading: there is no token for a font axis.
  - Signal orange is `--ds-color-brand-seed` (the exact hex, 5.5:1 on the black) because the dark ramp's step 9 is a desaturated #e76944.
  - Mark tracking -0.035em and weight 860; an SVG noise layer at 6% opacity for grain.
- Accessibility: all meaningful text is 4.5:1 or better on #151514 (secondary #afaba8 is 8.0:1, the signal orange 5.5:1). Links are at least 32 px tall, the email link 44 px. Focus ring is the system's 2 px ring. The wordmark is decorative and `aria-hidden` (the brand name is also in the copyright line).

## Renders
- `shot.png`: 1440 wide, full height (796 px), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: the mark was centred by advance width, so the B's ink started 20 px inside the text gutter and the full stop overshot. Fixed with the ink scan.
- Round 2: on the phone the crop hid too much of the letters; raised the crop to 0.74 below 720 px.

## Checks
- `preflight.py html`: 1 error, 1 warning. The error ("Archivo has no @font-face") is a false positive: the face is loaded with a Google Fonts link. The warning is the wordmark's -0.035em tracking; at 200% no glyphs touch. The script listed only `[300]` as font sizes, because it ignores rem values.
- `engine.py validate`: passes, 0 warnings. `engine.py review`: 6 raw values left after `od-ignore` on the mark's start size: the 8 px dot, the 20 px arrow icon, the 32 px link height and the dot's halo (review wants a border token there, because depth is set to borders).
- Checklist type and layout: one scale (12, 16, 21, 67 plus the art mark), heading weight from the system, no one-word last lines (balanced), every content edge on the 12-column grid, nothing overflows at 390.

## Owner type and color rules (applied mid-run)
- Fonts: one (Archivo). No mono.
- Type scale (named roles): label 12 (uppercase, tracked), body 16, title 21 (email link), display 67 (headline; 38 on phones), plus the wordmark as art (fitted, outside the scale). Four steps, none within 10%.
- Changed: the headline was all 750 weight with "Send it over." in orange text. Now the headline is regular (400) and "Send it over." is bold in an orange fill box with black text. The visual weight sits in the wordmark at the bottom; the box gives the top half one strong accent instead of a second heavy block of type.
- Changed: warmth 62 to 50 (`set dials.warmth 50`). At 62 the neutrals leaned brown (#151514, #ebe8e6) under an orange accent, which the new rule forbids; now a neutral black (#151515) and white (#e9e9e9). Black on the orange box is 5.5:1.

## Process findings
1. `--delegated all` silently rewrote the given brand hex and called an orange "a red" (feedback: bug).
2. A dark footer band is not a dark-only product, but the only route is a pinned `data-theme` (feedback: confusing).
3. The dark accent ramp loses the exact brand hue (feedback: gap).
4. No token for a font axis such as width (feedback: gap).
5. Preflight cannot see Google Fonts links or rem sizes (feedback: bug).
- Helped: `set` prints which tokens change, and a warmth dial that moves the neutral hue made the bone and warm black a one-line change.
