# 08 · Made with OpenDesigner: launch post

Render: `shot.png`, 1600 × 900 at scale 2. Page: `index.html`.

## Direction
A launch post in OpenDesigner's own brand system (`brand/design-system/project/`: `tokens.json`, `README.md`, the component previews). Light theme. One headline, "Every piece has its own design system.", over a mosaic of showcase work that bleeds off the right and bottom edges. Generous space, nothing loud except the work.

How it follows the README:
- Hanken Grotesk only (Source Code Pro is not loaded: no code on the post).
- Four styles at most: `social-label` (32/40, 500, `ink-muted`) and `social-headline` (108/112, 300), with the lockup.
- Highlight: the weight method (the second line at 650), the README's default. No fill box.
- Cobalt once: the circle in `lockup-light`. A tile whose own blue sits close to cobalt (the Howl Hill hero) was swapped for Halde Architekten so the accent stays single.
- Margins `space-80`, gaps `space-16`, tiles `radius-container` with a 1 px `line` and no shadow ("nothing else gets a shadow").

Tokens: `tokens.css` is compiled from `tokens.json` by `build_tokens.py` in this folder (same format as `brand/design-system/build_previews.py`, whose `_local/` copy is git-ignored). `bundle.css` and the lockup SVG are linked from the project folder, read-only.

Mosaic (real renders): heroes 07, 05, 01; app screens 08, 04; watch 03, 01; components 08, 03; footer 03.

## References (Mobbin, cited by link only)
- Squarespace, made with: https://mobbin.com/sites/sections/5749aa40-d43e-4d7c-865d-f899f7b066b2 . The work itself is the proof; one short line names it.
- Intercom, results grid: https://mobbin.com/sites/sections/f9204160-0727-4c99-9b0d-ab5f3bd3c4ce . A headline above a tight grid that keeps going past the frame.

## Look and fix
1. First render: the Howl Hill tile's blue competed with the cobalt circle in the lockup (two cobalt-like things on one screen, which the README calls wrong).
2. Second render: tile swapped; checked the headline at 200% (tracking -0.03em holds, no touching glyphs).

## Checks
- `preflight.py html`: 2 errors, 5 warnings, all false or from declarations, not use: M9 for Hanken Grotesk (Google Fonts link; loaded in the browser check) and for Source Code Pro (declared in `tokens.css`, never used); "13 distinct font sizes" and "sizes within 10%" (48/51, 67/72) are the whole style list in `tokens.css`, while the page renders two sizes (32 and 108, measured in the browser); the 12 px and -0.035em warnings are also unused styles. The `<br>` is deliberate: the two lines are the two weights.
- No engine system here (the brand system is the source), so no `validate`; `opendesigner/feedback.md` holds the preflight finding.
- Contrast: headline `ink` on `surface` 15:1; label `ink-muted` on `surface` 7.14:1.

## Process findings
- The brand README is precise enough to follow without guessing (styles, highlight methods, one-accent rule, lockup variants). Two gaps: no rule for image tiles (radius, border, shadow) in a mosaic, and nothing on colours inside showcased work that compete with cobalt.
- The project folder ships no compiled `tokens.css`; a builder has to write one.

## Round 3 (2026-10-15)
Rendered last, after the heroes (01, 02, 03, 07, 11), the app screens, the components and the renames were final. `shot.png`, 1600 × 900 at 2×.
- **Every tile is the current render** of its piece: the rebuilt Isobath and Halde heroes, Undertow's square river-photo cover, Tidemark's WED 14, Calamondin Tapes (was Pomelo Tapes), Voltfield's "Pace now", and the trail watch renamed **Fellrise** (Ridgeline is a real product name).
- **Alt texts:** the fitness tile names the product, Voltfield ("Tempo 6 × 800" is the workout); the music tile says Calamondin Tapes; the trail watch says Fellrise.
- **Phone crops start and end on whole elements:** Undertow from its chevron row to above its play controls (`object-position` 12.3%), Voltfield from just above its workout row and lock button (15.4%).
- **Both rows end at the same point.** The trail watch tile, which sat entirely off the canvas, is back: both rows have the same tile widths from the fourth tile on, and their last tiles start at x 1479 and are cut by the canvas edge at the same place. The two watch tiles were swapped so the edge cuts Tidemark through its sea, not the trail watch's "+312 m".

**Fresh audit: 4 of 5**, against Squarespace (https://mobbin.com/sites/sections/5749aa40-d43e-4d7c-865d-f899f7b066b2), Intercom (https://mobbin.com/sites/sections/f9204160-0727-4c99-9b0d-ab5f3bd3c4ce) and Mixpanel (https://mobbin.com/sites/sections/229af221-2f6b-48be-81f3-093001c5b3c8); both earlier must-fixes are fixed. Headline 15.3:1, label 7.1:1. Small items left: the mosaic's `aria-label` sits on a plain div, the Voltfield alt text is longer than the others, and Fellrise's "2.1 km" sits right above Tidemark's "2.1 m rising".
