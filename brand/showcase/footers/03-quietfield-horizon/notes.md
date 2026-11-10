# 03 Quietfield: newsletter-led dark footer with a glowing horizon

## Direction
Quietfield is a fictional AI research lab in Oslo that studies how models think (interpretability, evaluations). Its footer exists for one action: subscribe to the monthly research letter. The picture is a sunrise seen from orbit: a planet's dark edge at the bottom, its atmosphere lit violet, magenta and amber, a thin starfield above. Light, quiet type (Sora 300) and a single white pill button.
Feel words: futuristic, calm, sophisticated.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/2c33a0e6-3add-4a11-b4b8-d8b66ba00597 — warm light bleeding in from the edges of a dark footer, and a pill email field with the button inside it.
- https://mobbin.com/sites/sections/59c36bb2-2898-4e00-8481-892fa6c8520c — one centred newsletter ask, nothing competing with it; the legal row stays tiny.
- https://mobbin.com/sites/sections/010b6e4d-1e73-4698-9e32-e4396c7d9357 — a single light source in a dark scene does all the art direction; links stay small and mono at the top.

## System (engine)
```
python3 $E --dir .../03-quietfield-horizon/opendesigner sketch --name "Quietfield" --brand "#8b6cff" --audience regular --platforms web \
  --feel futuristic,calm,sophisticated --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "research site:read"
```
- Dials: expression 78 (the horizon is the site's signature), brandPresence 60 (brand lives in the light), density 25 (one ask, lots of sky), energy 35 (slow, luminous), roundness 90 (pill field and button), depth 70 (glow and layered light), colorfulness 60 (three-colour light), warmth 45 (cool night, warm rim).
- `set raw.accentCount 3` and `set raw.secondaryColors '["#e04fb8","#ffb35c"]'`: the engine made accent2 (magenta) and accent3 (amber) ramps, so the horizon colours are tokens (`--ds-color-accent-dark-10`, `accent2-dark-10`, `accent3-dark-10`, `accent3-dark-12`).
- `set raw.darkBase '"black"'` for a true black sky.
- `set raw.marketingSurfaces true`: with "read" surfaces the type scale stopped at 38 px. This brought back 51, 67 and 90.
- Faces: `raw.textFace "Sora"`, `raw.monoFace "JetBrains Mono"` (both SIL OFL); after the owner's two-font rule the page no longer uses the mono.
- Build: no errors, 1 warning (the feel-word conflict, which stays after I set brandPresence myself).

## Build
- Tokens for every colour, size, space, radius, focus, duration and easing. The headline is `--ds-font-size-67`, line one at weight 300 and line two at 600 (the system's heading weight is 650; a light display line is the voice), tracking -0.03em.
- Outside the tokens, on purpose: the planet's diameter (3600 px, 1500 px on phones) and arc position; the gradient stops of the rim, glow and sun (there is no gradient token); the star colour in the canvas script; blur radii.
- Accessibility: the field and button are 44 px tall, the field has a real label (visually hidden), the focus ring is the system's, all text is 4.5:1 or more on black (tertiary #7e8083 is 5.3:1, secondary 7.3:1). The art is decorative.

## Renders
- `shot.png`: 1440 wide, full height (945 px after the type changes), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: the legal row was invisible (my `.horizon > div` rule turned it into a 3600 px circle), the page was 1092 px tall, and the light was dim. Fixed the selector, tightened spacing, added a sun bloom.
- Round 2: the planet's rim crossed the legal links at both ends. Centred the legal row inside the planet's dark body, where the arc is highest.
- Round 3 (mobile): placeholder truncated, "fine-tuning" broke at its hyphen, "Terms" was orphaned. Shorter placeholder, non-breaking hyphen, legal links as a 2 by 2 grid.

## Checks
- `preflight.py html`: 1 error, the Google Fonts false positive (Sora; JetBrains Mono no longer used). No sizes read (all rem).
- `engine.py validate`: passes with the feel-word warning. `engine.py review`: 7 raw values (1 colour, 2 shadows, 4 sizes), all in the art layer.
- Checklist: sizes 12, 16, 21, 38 (phone), 67 from one scale; no one-word last lines on desktop; the content block sits in a centred 860 px box; nothing overflows at 390.

## Owner type and color rules (applied mid-run)
- Fonts: one (Sora). Changed: JetBrains Mono was used for eyebrows, column labels, fine print and the legal row, none of which is code or data; all of it is now Sora, and the mono link was removed.
- Type scale (named roles): label 12 (uppercase, tracked), body 16, title 21 (wordmark), display 67 (headline; 38 on phones). Four steps.
- Changed: the headline's second line was set apart by a grey colour at the same light weight. Now line one is light (300) and "before it becomes a paper." is semibold (600), both in the same colour. The glow carries the bottom of the frame, so the heavy line sits above the form where the eye should land.
- Color: black sky, bright text, a violet-magenta-amber light. No change.

## Process findings
1. The feel-word conflict warning does not clear after the dial is set (feedback: bug).
2. A "read" surface silently caps display type at 38 px (feedback: confusing).
3. No gradient token; secondary colours worked well as ramps (feedback: gap).
- Helped: `raw.secondaryColors` plus `accentCount 3` made the three light colours real ramps with dark-mode steps, and `raw.darkBase "black"` was exactly the right switch.

Replaced on 2026-10-14 by footers/09-b2b-platform after the Mobbin audit (score 2).
