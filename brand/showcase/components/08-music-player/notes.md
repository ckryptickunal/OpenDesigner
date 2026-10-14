# 08 · Music player · Pomelo Tapes

## Direction
Pomelo Tapes is a fictional indie cassette label; this is the embeddable player that sits on its release pages and artists' sites. It should feel like a piece of the record sleeve: the cover art is generated in code and its colours are sampled at runtime to paint the whole card, a record slides out from behind the sleeve while it plays, the track title is set huge in a wide display face, and the waveform is marked with the song's sections ("1:42 the drop"). Dark stage, vivid gradient, round everything.
Feel words: **vibrant, expressive, bold** (engine: vibrant → rich + bold, bold → bold, "expressive" unknown).

## References (Mobbin, cited by link only)
- Brink podcast player, https://mobbin.com/screens/0b6c0d17-7cd7-4b61-80a5-c54312e75c90 : the whole background tinted from the artwork, translucent chips for secondary actions, one big white round pause. Taught me art-tinted surfaces and the white primary disc.
- SoundCloud track page, https://mobbin.com/screens/ed654af2-e00e-4abe-9b23-6f56f5056a17 : the waveform is the scrubber, with markers placed on the timeline. Taught me to put meaning (sections) on the waveform.
- Higgsfield audio, https://mobbin.com/screens/70d08781-cbce-431c-8b11-4778b974e282 : a dense bar waveform with a crisp playhead marker over it. Taught me the bar rhythm (2px gaps) and the playhead cap.
- Once cassette player, https://mobbin.com/screens/fa0ca563-f6ce-49cb-b165-d53512821014 : a physical-object player (cassette) with the play button at the centre of attention. Taught me the record-behind-the-sleeve idea.

## System (engine)
`sketch --name "Pomelo Tapes" --brand "#ff3d81" --audience regular --platforms web --feel vibrant,expressive,bold --theme system-light-dark --delegated all --surfaces experience`, rendered with `data-theme="dark"`.

| Dial | Value | Why |
|---|---|---|
| expression | 90 | display sizes up to 90px, display weight 850 |
| brandPresence | 85 | art and pink run the card |
| density | 38 | one track at a time |
| energy | 82 | wanted springy; see findings (no effect on springs) |
| roundness | 82 | control 16, container 24, overlay 32 |
| depth | 70 | the hero card uses elevation.overlay |
| colorfulness | 92 | vibrant scheme, HCT chroma 97 accent |
| warmth | 62 | warm pinks and tangerine over violet |

Typefaces through the engine: `raw.displayFace "Unbounded"`, `raw.textFace "DM Sans"`, `raw.monoFace "DM Mono"` (SIL OFL, Google Fonts), licence recorded.

## Where I stepped outside the tokens, and why
- **Art-derived colours `--c1..--c3`** are sampled from the generated cover in the browser (vivid hue bins, three distinct hues) and paint the hero card, the page glow, the vinyl label and the scrubber fill. This is the point of the piece; the engine has no slot for content-derived colour.
- **Darkening base `--ink` (#0c0710)** mixes the art colours down so white text stays above 4.5:1 (title, artist) and secondary text at 74% white stays above 4.5:1 on the darkest mix.
- **Translucent whites** (12–26% white) for chips and unplayed waveform bars on the art; no token for "on-art" surfaces.
- The vinyl uses hard-coded near-black greys (an object, not UI).
- Display tracking −0.035em on the 51px Unbounded title (preflight M5 warns; checked at 200%, glyphs do not touch).

## Checks
- `engine.py validate`: no errors, 0 warnings, 5 notes (188 colour pairs checked).
- `preflight.py html --medium web`: 2 errors, both false positives (M9: Unbounded and DM Mono load from the Google Fonts link). 1 warning, M5 tight tracking (intentional, checked). An earlier M7 warning for `<br>` in the title is fixed with `text-wrap: balance`. An earlier 9px "1" on repeat-one is now a 12px badge.
- Contrast: white on darkened art mixes ≥ 7:1 for the title; 74% white secondary text ≥ 4.5:1; mono captions (text.secondary on the dark base) about 8:1. Unplayed waveform bars are graphical; the playhead, time code and `aria-valuetext` carry the position, so the 26% bars are not the only signal. Disabled play ("off") is exempt.
- Interaction: the waveform is a real `role="slider"` (Arrow keys ±5s, Page ±30s, Home/End, click to seek, hover shows the time); play/pause toggles the spinning record and advances time; Space plays from anywhere on the page; shuffle, repeat and save are `aria-pressed` toggles; volume is a native range. Reduced motion stops the record spin, the EQ bars and the spinner and zeroes transitions.

## Rounds
1. The record slid over the track title and hid half of it; the cover read as a generic synthwave sunset (striped sun, orbit ring); the right column ran off the bottom.
2. Moved the record behind the meta column with a wider gutter, redrew the cover as a heat-lamp coil (an Archimedean spiral in a glowing disc) to fit the album name, trimmed the rail. The play button then squashed into an oval in a flex row that was too narrow.
3. Moved volume into the chip row, gave controls `flex: none`, widened the meta column, balanced the title wrap instead of a `<br>`, restored the third queue row.

## Process findings
1. **Energy does nothing to springs or easing.** Springs, standard easing and the medium/long durations are locked by house standards; only `duration.extra` and heading weight follow the dial. Energy 20 (table) and 82 (player) produce identical spring tokens. (feedback: gap)
2. **No content-derived colour.** Art-tinted players are a standard pattern; the engine has no slot for runtime colours or a contrast rule for text on them. (feedback: gap)
3. **Hot pink named "crimson"** in the sketch output and DESIGN.md. (feedback: bug)
4. **"expressive" is not a known feel word.** (feedback: idea)
5. Helped: Expression 90 produced a real display scale (51/67/90) and display weight 850 without asking; roundness 82 gave radius roles that matched a record-like shape language; elevation.overlay at depth 70 was exactly the right lift for the card.

## Owner type and color rules (applied after the first render)
- **Two fonts:** Unbounded (display: title, label number, mini-player titles, the cover lettering) and DM Sans (everything else). DM Mono is gone: time codes, catalogue numbers and captions use DM Sans with tabular figures (`font-variant-numeric: tabular-nums`) and 0.08em caps tracking. Engine: `pick Q-type-06 system-mono` so the token no longer names DM Mono; the cover canvas also switched to DM Sans.
- **Title weight on purpose:** the hero title went from Unbounded 850 to 500. At 51px the wide face is loud enough at regular weight, and the cover art now carries the visual weight of the card instead of competing with the title. The "08." number is 500 too; mini-player titles keep 700 at 16px so they read at small size.
- **Type scale (5 sizes):** caption/label 12, body 16, title 21 (artist, brand), headline 38 (sheet number), display 51 (track title). No two within 10%.
- **Color:** dark violet stage, white and bright pink text on art darkened toward #0c0710; no brown tones. No change needed.
