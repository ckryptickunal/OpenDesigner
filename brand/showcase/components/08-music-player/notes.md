# 08 · Music player · Calamondin Tapes

Gallery: Calamondin Tapes is a fictional cassette label; its player's scrubber is the whole of side A, track by track.

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

## Round 4 (owner review, 2026-10-15)

**What he said.** Most of the web components "look absolutely rubbish", and none should "feel like they are from a vibe coded app or a cheap Chinese app". Margin (02) is the only component he does not call ugly; the B2B product screens are the bar. In round 3 he had said this piece "needs a little more work".

**The idea in one sentence:** a cassette is heard a side at a time, so the scrubber is the whole of side A, track by track.

**What changed.** The label, artist, tape and track list stay (Calamondin Tapes, Juniper Static, *Heat Lamp Lullabies*). The release page with a player card inside it became the player itself, the label's **listening room**, now playing:
- A 520 px cover; beside it the track (side A, track 3 of 9, 1:47 of 3:53), *Sodium Summer* with its saved heart, the artist line, transport (previous, pause, next, repeat the tape) followed by volume and output, one line of liner notes, and *Then side B* (6 to 9).
- Across the foot of the frame, the whole of side A (19:54) as five blocks of waveform, one per track with a 16 px gap between them, labelled by track (labels placed by the same maths as the bars), played in orange to 9:48, with 10:06 left on the side.
- Gone: the buy box, the embed box, the "more releases" row, the drawn two-ink J-card, the shuffle button (a tape plays in side order), a caption-style sleeve lettering tried in this round, the section labels made with bars, and tracks 4 and 5 in the list (the scrubber already shows them; the list is now side B only).
- A paper J-card spine across the cover's foot was tried and removed (a third surface colour, and not how a J-card works).
- Two of the punning track titles were renamed: Thermostat Hymn is now Second Week of March, and Lullaby for a Hatchery is now Last Frost.
- Cover: a real photograph. Iván Martínez Díaz, "A young plant emerges from the darkness", Unsplash License, hotlinked from images.unsplash.com as Unsplash asks (https://unsplash.com/photos/a-young-plant-emerges-from-the-darkness-uG9Z4qrbt5c), credited in an HTML comment on the page. It replaced Hanson Lu's "gray greenhouse at night" (https://unsplash.com/photos/G6o5Xo-JVj8), a recognisable public conservatory that read as stock. The page needs the network to show it.
- Colour: the room takes a deep tint of the cover's darkest green (rgb 12 16 13), never brown. The accent moved from pink to calamondin orange (#FF9A3D), the citrus the label is named for. It has one job: what has played (and the logo). The logo is now a citrus slice.
- The waveform is drawn loudness, not decoded audio (the code says so), with each track's own level, a soft start and a fade; unplayed bars are at 46% white, so they pass 3:1.

**References (Mobbin, cited by link only).**
- TIDAL now playing, https://mobbin.com/screens/4e6a317f-e9d8-4c10-9029-59db504ec44c : a large cover beside a second column. Taught the split.
- Apple Music now playing, https://mobbin.com/screens/7bd2ef54-565a-42a6-ad5d-2fa21b98f2a3 : title, transport and scrubber in one column. Taught the order of the right column.
- Deezer queue, https://mobbin.com/screens/13820511-808c-411d-a033-65e3ca3b2e6e : the queue beside the cover. Also what to avoid: icons on every row and an accent everywhere.

**System (engine).** Re-sketched (git keeps the old state):
`sketch --name "Calamondin Tapes" --brand "#FF5577" --audience regular --platforms web --feel calm,bold,minimal --theme system-light-dark --delegated all --surfaces "listening room:experience"`, then `set raw.textFace "Manrope"`, `raw.neutralTint pure`; dials roundness 40, depth 20, warmth 10, colorfulness 30, expression 55, energy 30, density 62 (all `delegated`); later `set raw.brandColor "#FF9A3D" --set-by chosen`; `build`. Rendered with `data-theme="dark"`.
- `--theme dark-only` was refused by house standard STD-visual-details-24, so the system has both themes and the page asks for dark (recorded with `engine.py feedback`).
- Face: Manrope (SIL OFL), one family.
- Type scale, named roles (web px): caption 13, body 16, headline 25. Weights 400, 500, 600, 700.
- Outside the tokens on purpose: the room tint, the 56 px play button, the canvas waveform (112 px tall), the 4 px volume track.

**Checks (final render).**
- Totals re-added from the page: side A 3:41 + 4:20 + 3:53 + 2:58 + 5:02 = 19:54; side B 4:07 + 3:36 + 3:19 + 3:16 = 14:18; into side A 3:41 + 4:20 + 1:47 = 9:48, left 19:54 − 9:48 = 10:06; the playhead sits 107 s into track 3 (481 to 714 s of the side), as the page says.
- `check_dates.py --year 2026`: passes (no weekdays).
- `check_names.py`: no errors. One warning, a false positive: "Studio" is a product in `components/01`, but here it is the word in "Studio speakers".
- `preflight.py html`: 0 errors, 0 warnings; sizes 13, 16, 25.
- `engine.py validate`: no errors; 3 warnings, two for light mode (a light orange button is faint on white; the piece is shown dark) and one that the feel words calm and bold pull brand presence opposite ways.
- Computed contrast: 27 runs, lowest 6.4:1. No text sits on the photograph.
- Gallery size (337 px): the eye lands on the cover, then the orange blocks of the side.

**Blind pairwise test** (ours against a shipped player, sides random, fresh judges):

| Round | Version | TIDAL | Apple Music | Deezer |
|---|---|---|---|---|
| 1 | first build | ours −2 | +3 | +3 |
| 2 | room tinted, sections as gaps, full queue | +2 | +4 | +3 |
| 3 | orange accent, lettering, natural waveform | +2 | +4 | +3 |
| 4 | whole-side scrubber, no lettering or shuffle | +2 | +3 | +3 |
| 6 | J-card spine, side B list, taller scrubber; one judge, one pair | +2 | | |
| 7 | final (seedling cover, five-block side, layout gaps closed); one judge | +2 | | +3 |

Passes from round 2 on. Round 1 lost to TIDAL by 2 (flat charcoal, bars in the section labels, a queue that stopped short).

**Fresh-eyes audit:** round 1, 3 (stock-looking photo, a synthetic barcode waveform, header and content on different edges); round 2, 3 (cover left, player right reads as a template, pasted sleeve lettering, controls spread across the column); round 3, 3 (stock cover dominates, punning track names, the list repeating the scrubber; addressed); round 4, 3 (the photo wins over the component, layout holes, the side idea lost at gallery size; addressed); final, **3** (the photo is still the largest thing and reads as stock, the scrubber's 13 px labels lose to the 16 px list, the TIDAL-style split).

**Result: fails the fresh-eyes bar after four rounds, honestly reported.** It wins every blind pairing from round 2 on, but four fresh auditors in a row score it 3. The cover is a stock photograph however it is cropped, and it is the largest thing in the frame. What would move it: cover art the label owns (commissioned, painted with `opendesigner-paint`, or the owner's own photo) at a smaller size, and the side-A scrubber given the frame's weight (larger labels, the side B list demoted).

**For the owner:** `mockups/05-components-board` and `mockups/08-made-with-opendesigner` crop this shot.png with offsets set for an older layout; they need new crops.

## Round 5 (owner hid it until better, 2026-10-18)
**What Kunal did:** he hid the piece "until better": it had won its blind test in round 4, but the fresh reviewer stayed at 3.

**The idea, in one sentence:** a cassette is heard a side at a time, so the scrubber is the whole of side A, track by track.

**What changed**
- The stock photo is gone. The cover is the label's own art, drawn in code (SVG, seeded so it never changes): one row of a seed tray under a heat lamp, nine cells for nine tracks with a thicker wall between side A and side B, each seedling as tall as its track is long (2:58 to 5:02). Two inks: green, and the lamp's pale light; the seedlings turn dark green in front of the lamp. The sleeve lettering is set like a J-card (Juniper Static, Heat Lamp Lullabies, CT 014). A first drawing, a seed tray from above with an orange pool of light, read as tiled wallpaper and was replaced.
- Orange has one job again, what has played (and the logo). The cover does not use it.
- The scrubber has the frame's weight: the cover dropped from 520 to 400 px, the waveform is 176 px tall, the track labels are 25 px (the current one bold), the times 16 px. Each track has its own drawn shape (intro, swell, fade), still drawn loudness, not decoded audio.
- Removed as clutter: the liner-notes and more buttons, "41 of 150 left", the output device and the liner note. The side B list stays, at 13 px in secondary grey.

**Type scale:** 13 (side B list, kicker), 16 (body, times), 25 (title, scrubber labels). One face, Manrope; the cover lettering uses it too.

**References (Mobbin, cited by link only; used for the blind test):**
- Apple Music now playing, https://mobbin.com/screens/7bd2ef54-565a-42a6-ad5d-2fa21b98f2a3 : title, transport and progress in one column under the art.
- SoundCloud, https://mobbin.com/screens/301a21e9-d189-4959-9e06-efe024cc9c2b : the waveform as the scrubber, played part in orange.
- The New York Times podcasts, https://mobbin.com/screens/159a9f86-1a78-43b0-9a8e-cb61341b1566 : a player where the art is the stage; what to avoid: type on a busy image.

**Blind pairwise test** (ours minus shipped, 1 to 5; neutral file names, random sides, no labels; one fresh judge saw all the round's pairs):

| Round | Version | Apple | SoundCloud | The |
|---|---|---|---|---|
| 1 | drawn tray-from-above cover, 464 px | +3 | +3 | +2 |
| 2 | side-view tray row cover with lettering; heard tracks off-white | +1 | +3 | +2 |
| 3 | pale lamp, orange only for played, 400 px cover, larger scrubber, less chrome | +3 | +3 | +2 |

**Fresh-eyes audit:** round 1, 3.5 (the cover read as tiled wallpaper, two orange masses, generated-looking waveforms; addressed); round 2, 3 (the cover outshouts the component and shares the accent, the track-by-track idea lost at gallery size, competing chrome; addressed); round 3, **3.5** (the waveforms still look procedural, "Sodium Summer" set twice at display size, the cover reads as a card and its seedlings close to clip art).

**Result: did not reach 4 in three rounds, honestly reported.** The stock photo is gone and the cover is the label's own, and the piece wins every blind pairing (worst +1), but three fresh auditors scored it 3.5, 3 and 3.5. What would move it: a painted cover (`opendesigner-paint`, which needs an `npm ci` install the owner has to approve), a waveform from real audio, and one display size (drop the scrubber labels to 16 px so the title is the only display moment).

**Checks (final render):** check_dates `--year 2026` passes; check_names 0 errors (the NEW words it lists are dictionary words, key names or the typed query); preflight 0 errors, 0 warnings; engine validate no errors (light-mode warnings as before); computed contrast of every HTML text run 4.6:1 or more.
