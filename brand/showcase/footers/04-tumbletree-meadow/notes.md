# 04 Tumbletree: playful illustrated footer with a meadow and a mascot

## Direction
Tumbletree is a fictional learning app for children aged 4 to 8 (reading, numbers, ten minutes a day). The footer is read by parents and teachers, but it should make a child smile if they are on the lap: a meadow at the end of the page, a rising sun, and Pip, a round tangerine creature with a sprout, waving with one hand and flying a kite with the other, saying "See you tomorrow!". Chunky rounded type, thick ink outlines, "sticker" buttons with a hard drop.
Feel words: playful, cheerful, warm.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/0cc6183c-2921-48ea-bfe9-d7c3d60bfed4 — a line-art scene along the bottom edge that the link grid sits above; the scene is the reward for scrolling to the end.
- https://mobbin.com/sites/sections/63e60bfc-1a20-41d0-a3b3-2da8a43a3723 — a landscape as the ground of the footer, with legal text standing on it.
- https://mobbin.com/sites/sections/9ee9d990-cbe1-40fe-b2ca-03ae743e3f0a — a warm footer that puts links in a rounded panel with a thick border and lets a mascot and a speech bubble carry the voice.

## System (engine)
```
python3 $E --dir .../04-tumbletree-meadow/opendesigner sketch --name "Tumbletree" --brand "#ffc83d" --audience large --platforms web \
  --feel playful,cheerful,warm --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "family site:persuade"
```
- Dials: expression 90 (a whole illustrated world), brandPresence 80 (sun yellow and the mascot are the brand), density 28 (big targets, few links), energy 80 (bouncy), roundness 100 (pills and blobs), depth 35 (chunky drop on the panel and buttons), colorfulness 95, warmth 90.
- `raw.accentCount 3`, `raw.secondaryColors '["#3fb6f2","#3fb86a"]'`: sky (accent2) and grass (accent3) ramps.
- Faces: `raw.textFace "Nunito"`, `raw.displayFace "Fredoka"` (both SIL OFL). DESIGN.md flagged Fredoka as a licence risk, so I recorded `raw.fontLicence {"web":true,"app":true,"selfHost":true}`.
- Build: no errors, 1 warning (2 after the warmth change, base and raised surface): the yellow action colour against a white surface is 1.5:1. Correct and useful; the buttons get a 3 px ink border so the edge passes.
- `--audience large` did not raise body size (still 16 px; see findings).

## Build
- Type, spacing, radii, motion, focus and all UI colours are tokens. The meadow uses the ramps: sky accent2 steps 2 and 4, hills accent3 steps 4, 6, 9 and 11, sun accent step 9, path accent step 3.
- Outside the tokens, on purpose: Pip's tangerine, belly and cheek colours (a brand character, the "illustration, characters" asset the engine lists as a designer hook); the ink outline uses the darkest neutral token; white clouds and flowers; the 56 px button height and 3 px outlines (sticker style); the hard 5 to 8 px drops.
- Art made in SVG by hand: hills, trees, path, sun, kite, birds, clouds, Pip. The speech bubble's words are inside the art, so the SVG is `aria-hidden` and nothing it says is needed.
- Accessibility: white legal text on accent3 step 11 is 5.9:1; chips' green text on white 5.9:1; the blue "big curiosity." 5.4:1 on the sky; buttons are 56 px tall; links 36 px; 3 px focus ring in sky step 11; clouds stop drifting with reduced motion.

## Renders
- `shot.png`: 1440 wide, full height (836 px after the type changes), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: clouds sat behind the logo and inside the link panel, "Lesson plans" wrapped beside its "New" pill, the speech bubble tail was a patched shape. Moved clouds into the empty sky, made links nowrap with auto columns, drew the bubble and tail as one path, added birds.
- Round 2 (mobile): the legal links sat on the bright near hill (white on #00bc5f is 2.5:1, a fail), the kite was cut off and a cloud covered a chip. Moved the legal row into its own dark green band below the scene, reframed the SVG on phones (`viewBox 600 0 520 380`) so Pip and the kite stay in view, hid two clouds.

## Checks
- `preflight.py html`: 1 error, the Google Fonts false positive (Fredoka).
- `engine.py validate`: passes with the advisory yellow-on-white warning (handled by the border).
- `engine.py review`: 25 raw values, 16 of them colours: the mascot, white art, rgb() whites for translucent panels. All in the art layer.
- Checklist: sizes 12, 16, 21, 28, 38 (phone), 51 from one scale; heading weight 600 (lighter than the system's 750, because Fredoka at 750 reads as shouting); the panel, chips and buttons stay on one line where they should.

## Owner type and color rules (applied mid-run)
- Fonts: two (Fredoka for display and the speech bubble, Nunito for text).
- Type scale (named roles): label 12 ("New" pill), body 16, title 21 (link headings, buttons, lede), headline-sm 28 (wordmark), display 51 (headline; 38 on phones). Five steps.
- Changed: "big curiosity." was highlighted by colour only (sky blue). Now it sits in a rounded sun-yellow fill box with ink text, which matches the sticker style and the yellow button. Headline leading went from 1.04 to 1.14 so the box does not touch the line above.
- Changed: warmth 90 to 55 (`set dials.warmth 55`). At 90 the ink and grey text were brown (#282321, #605551) on a sky-blue page; now a clean ink (#252423) and grey (#595756).

## Process findings
1. `--audience large` promises 17 px body in the stage file but leaves it at 16 (feedback: bug).
2. The open-font list misses common OFL faces, so DESIGN.md warns about licences that are free (feedback: bug).
3. No saturated mid-tones for illustration in the ramps (feedback: gap).
4. The illustrate skill cannot run without a person to say yes to fetching (feedback: confusing).
- Helped: the yellow-on-white warning caught a real problem with a chunky yellow button.
