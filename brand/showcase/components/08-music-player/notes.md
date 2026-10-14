# 08 · Music player · Calamondin Tapes

## Direction
Calamondin Tapes is a fictional indie cassette label; this is the embeddable player that sits on its release pages and artists' sites. It should feel like a piece of the record sleeve: the cover art is generated in code and its colours are sampled at runtime to paint the whole card, a record slides out from behind the sleeve while it plays, the track title is set huge in a wide display face, and the waveform is marked with the song's sections ("1:42 the drop"). Dark stage, vivid gradient, round everything.
Feel words: **vibrant, expressive, bold** (engine: vibrant → rich + bold, bold → bold, "expressive" unknown).

## References (Mobbin, cited by link only)
- Brink podcast player, https://mobbin.com/screens/0b6c0d17-7cd7-4b61-80a5-c54312e75c90 : the whole background tinted from the artwork, translucent chips for secondary actions, one big white round pause. Taught me art-tinted surfaces and the white primary disc.
- SoundCloud track page, https://mobbin.com/screens/ed654af2-e00e-4abe-9b23-6f56f5056a17 : the waveform is the scrubber, with markers placed on the timeline. Taught me to put meaning (sections) on the waveform.
- Higgsfield audio, https://mobbin.com/screens/70d08781-cbce-431c-8b11-4778b974e282 : a dense bar waveform with a crisp playhead marker over it. Taught me the bar rhythm (2px gaps) and the playhead cap.
- Once cassette player, https://mobbin.com/screens/fa0ca563-f6ce-49cb-b165-d53512821014 : a physical-object player (cassette) with the play button at the centre of attention. Taught me the record-behind-the-sleeve idea.

## System (engine)
`sketch --name "Calamondin Tapes" --brand "#ff3d81" --audience regular --platforms web --feel vibrant,expressive,bold --theme system-light-dark --delegated all --surfaces experience`, rendered with `data-theme="dark"`.

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

## Round 3 (owner review, 2026-10-14)
**What Kunal said:** "needs a little more work". The earlier audit: a generated pink-orange-violet gradient cover with a spiral (stock "AI album art") painting the card magenta to violet with a glow on the page; dark plus neon pink on every control; four surface treatments in one card; a borrowed verified badge.

**What changed:** the embeddable player now sits in its real place, the release page for "Heat Lamp Lullabies" on Calamondin Tapes' own site, at 1440 x 900.
- **One object made with care:** the J-card art is a two-ink riso print drawn in SVG: a blue lamp shade, a pink bulb (the overlap prints purple through multiply), a pink halftone light that fades from the bulb and reaches the ground line, three solid blue seedlings, the blue layer 2 px out of register, a faint print grain, letterspaced lettering. It illustrates the liner notes (songs recorded in a greenhouse under heat lamps).
- **Flat card, one job for pink:** the player is one flat navy tint taken from the blue ink (`--sleeve-ink`, outside the tokens on purpose); pink only marks what is playing (the played waveform and the playing row). The page is white with pure ink text. No glow, no gradient, no badge.
- **Hierarchy:** the album is the page heading (38 px); the player's track title is 28 px and sits just above the controls; the waveform keeps the section markers (Intro, Verse, Swell, Bridge, Outro) that the first audit liked. The embed is a fixed 740 x 400, as the "Put this player on your site" box says.
- **Facts re-added:** side A 3:41 + 4:20 + 3:53 + 2:58 + 5:02 = 19:54; side B 4:07 + 3:36 + 3:19 + 3:16 = 14:18; album 34:12; 1:47 + 2:06 = 3:53. Edition of 150, 41 left. Cassette words: "J-card", "dubbed in real time onto chrome tape".
- **Engine:** `raw.brandColor "#FF3D81"` restored as typed (it had been stored as #e2136a), `roundness 82 → 52`, `depth 70 → 30`, `colorfulness 92 → 62`, `warmth 62 → 30`, `expression 90 → 68`, rebuilt. Faces: Unbounded (display, now 600 not 850) and DM Sans; sizes 12, 16, 28, 38.
- **New names:** the tracks Low Bulb, Brooder, Thermostat Hymn, Warm Front and Lullaby for a Hatchery; the releases Tin Roof Weather (Moss Radio, CLMD-013), Cold Frame (Ondine Vale, CLMD-012) and Night Bus Hymns (Hollis Arcade, CLMD-011).
- **States, one per frame:** `shot.png` (playing at 1:47), `shot-scrub.png` (pointer at 2:31 with a time chip and the stretch it would skip), `shot-buffering.png` (about a second loaded, "1:47 · Loading…"), `shot-error.png` (the card keeps its size, the waveform dims with pink up to 1:47, the message and Retry sit in the time row).

**Checks:** rendered contrast: no live text below the floor (the two "failures" are the J-card lettering, which the script cannot hide because SVG text uses fill; it is art and reads at about 5:1 blue on paper). Unplayed bars 3.7:1 as UI parts. `check_dates.py`: pass. preflight: 0 errors. `engine.py validate`: no errors.

**Renamed (coordinator, 2026-10-15):** the label's first name sat one word away from a real record label, so it is now **Calamondin Tapes** (a calamondin is a small citrus, so the citrus-slice logo still fits), with catalogue numbers CLMD-011 to CLMD-014. Web search found no label, company or band called Calamondin Tapes; the old name is listed under "No longer on any page" in `brand/showcase/NAMES.md`. The `sketch` command above is shown with the current name; the system was renamed with `engine.py set name "Calamondin Tapes"` and rebuilt.

**Fresh-eyes audit:** 3/5, then 4/5 (low 4); its last notes (empty space under the title, the knob touching "Swell", a hidden waveform in the error frame, a broken "740 ×", the empty bottom, a light cone that stopped short, an invisible grain, a stale comment) were fixed. References: SoundCloud waveform https://mobbin.com/screens/301a21e9-d189-4959-9e06-efe024cc9c2b, TIDAL art-tinted player https://mobbin.com/screens/2e073289-7c6a-4440-b471-83bdb41de138, Spotify now playing https://mobbin.com/screens/7e88185e-30b2-4478-8185-3ada92d36934.

**Fresh score: 4.**
