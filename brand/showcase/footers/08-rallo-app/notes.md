# 08 Rallo: app-download footer with a phone peeking up

## Direction
Rallo is a fictional running and strength coaching app ("for people who run before work and lift after it"). The footer's job is one install. A full cobalt panel carries a big italic promise, two generic store-style badges ("Get it on your phone", "Also on your watch"), a decorative scan square and a rating line; on the right a phone rises from the panel's bottom edge, tilted, showing a live tempo run (distance ring, pace, heart rate), with two floating cards (VO₂ max trend, an 18-day streak) for depth, over faint running-track lanes. Normal link columns sit calmly below the panel.
Feel words: energetic, modern, confident.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/0c19121c-1011-49e4-99b7-9569cc45fd0a — a dark panel with the headline and download options on the left and phones cropped by the panel's bottom edge on the right.
- https://mobbin.com/sites/sections/27b0a2d5-011a-4cc3-bd34-a9165892b739 — the rating as a number plus stars plus a count, next to the store badge, as the proof.
- https://mobbin.com/sites/sections/86b57046-171c-45b5-80e5-61e86bc6747c — a scan square beside the badges, and the standard link columns kept separate from the install pitch.

## System (engine)
```
python3 $E --dir .../08-rallo-app/opendesigner sketch --name "Rallo" --brand "#2b45ff" --audience regular --platforms web,ios \
  --feel energetic,modern,confident --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "marketing site:persuade,app:operate"
```
- Dials: expression 80 (a product shot sells it), brandPresence 85 (a full cobalt panel), density 40, energy 90 (sporty, punchy numbers), roundness 75 (device-like corners, pills), depth 60 (the phone floats), colorfulness 65 (cobalt plus mint), warmth 55 (encouraging coach voice).
- `raw.accentCount 2` + `raw.secondaryColors ["#3ee6a8"]` gave a mint ramp (step 9 #00e9a5).
- Typeface through the engine's own route: `set raw.fontClass '"geometric"'` and `set raw.textFace '"=openClass"'` resolved to Plus Jakarta Sans (SIL OFL). This is the cleanest typeface path I found.
- Build: no errors, 1 warning (feel-word conflict on roundness, which stays after setting the dial).

## Build
- Panel, type sizes (12, 16, 21, 28, 51, 67), spacing, radii (32 panel, 16 cards, 12 badges), focus and motion are tokens. The phone's screen uses the dark neutral ramp, the ring and chart use cobalt and mint ramps.
- Outside the tokens, on purpose: the device bezel gradient, its shadows and the dynamic-island pill (product-shot art); translucent whites on cobalt (`rgb(255 255 255 / .86)` and friends); the track lanes; the scan square is a seeded pattern drawn on canvas, not a real code, and is `aria-hidden`. `engine.py review` counts 41 raw values, nearly all in the device mockup.
- Accessibility: white on cobalt 6.2:1; lede at 86% white about 4.9:1; the mint "counting on you." is 3.9:1, which passes only as large text (it is 67 px bold); mint ramp step 11 on white 5.9:1. Badges are 60 px tall, links 36 px; the whole phone stage is decorative and `aria-hidden`; the rating is plain text.

## Renders
- `shot.png`: 1440 wide, natural height (922 px), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: the stars rendered white (a `.rating span` rule beat the star colour), and the phone sat too high to read as "peeking up". Fixed the selector and lowered the phone so the panel edge crops it.
- Round 2: the streak pill covered the phone's status bar; moved it above the corner. On phones, the VO₂ card covered the distance, the rating's divider was orphaned, and the track lanes became straight lines; all three are hidden below 900 px.

## Checks
- `preflight.py html`: 0 errors, 2 warnings: -0.04em on the ring's distance number (glyphs do not touch at 200%), and `<br>` in "Scan to / install" (a two-line label, not a heading). It did not flag Plus Jakarta Sans as unloaded, while it flagged every other Google Fonts face in this set, so the font check is inconsistent.
- `engine.py validate`: passes with the feel-word warning.
- Checklist: one scale; the panel's two halves each hold one idea; badges and pills stay on one line; nothing overflows at 390.

## Owner type and color rules (applied mid-run)
- Fonts: one (Plus Jakarta Sans).
- Type scale (named roles): label 12, body 16, title 21 (lede, badge names), headline-sm 28 (wordmark, card figure), headline 51 (the ring's distance), display 67 (panel headline; 38 on phones). Six steps.
- Changed: "counting on you." was italic and mint (the italic-word trick in a sans). Now the headline is medium (500) and "counting on you." is extra bold (800), all white. Mint stays on the stars, dots, ring and chart, where it means "live" or "progress".
- Color: cobalt with white text (6.2:1). No change.

## Process findings
1. The feel-word conflict warning again ignores an explicitly set dial (same bug as piece 03).
2. Typeface through `raw.fontClass` + `=openClass` worked well and should be the documented route in DESIGN.md's Typography section.
- Missing but out of scope for the engine: device mockup and product-shot primitives. Every app footer needs one, and it was the slowest part to build.
