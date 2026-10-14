# 08 · Undertow: podcast now playing (phone, 390×844 @3x, dark)

## Direction
Undertow is a fictional podcast app for long-form, late-night listening. The screen is now playing, chapters and a live transcript for "Night Cartography", episode 41, "Maps of places that moved". It should feel like a magazine at midnight: full-bleed generated cover art (a contour map lit by a moon), a large quiet serif title, a scrubber split into chapters, and chapters set like a table of contents. Feel words: **sophisticated, moody, editorial** (the engine knew only "sophisticated"; it left out "moody" and "editorial").

## References (Mobbin, structure only)
- [Brink, transcript player](https://mobbin.com/screens/dc4bf431-8eb4-45c6-aa53-fe16e0a95733): a live transcript where the current sentence is brighter than the rest.
- [Queue, chapter picker](https://mobbin.com/screens/4ac39cee-850b-4828-9e08-aa93b44c3ef3): chapters with durations and a scrubber that knows its chapters.
- [Digg, daily briefing](https://mobbin.com/screens/1855d882-66a2-4247-a138-96271580bfa3): chapter rows with start times on the right.
- [Bloomberg, audio list](https://mobbin.com/screens/a10206a4-9fb9-4545-ab53-e299fb68eb69): editorial headlines between hairline rules, with no cards.

## System (engine)
```
sketch --name "Undertow" --brand "#E8946A" --platforms ios --feel sophisticated,moody,editorial --delegated all
   (--theme dark-only was refused by STD-visual-details-24; built both modes and render the dark one)
   (the sketch replaced my apricot with #AF6037 brown; restored with set raw.brandColor --set-by chosen)
pick Q-scope-06 experience · set raw.baseSize 17 · set raw.fontLicence {...}
-- after the owner's rules --
set raw.brandColor "#A9C4FF" · set raw.secondaryColors ["#2F45C8"] · set raw.neutralBase "#141C33"
set dials.warmth 18 · set raw.displayFace Newsreader · set raw.monoFace ui-monospace
build → Passes: no errors; 2 warnings about light mode (the ice-blue action is 1.7:1 on white). Not used here, but real for a light theme.
```
| Dial | Value | Why |
|---|---|---|
| expression | 75 | editorial: the art and the title lead |
| brandPresence | 60 | the show's art leads, the app recedes |
| density | 45 | player, transcript and chapters on one screen |
| energy | 35 | late-night pace |
| roundness | 6 | print edges: every radius token is 0 |
| depth | 15 | flat, hairlines only |
| colorfulness | 30 | one duotone |
| warmth | 18 (was 65) | cool night palette |

## Fonts and type scale (two faces)
Newsreader (display, OFL, optical sizes) and Hanken Grotesk (text, OFL). Times use Hanken Grotesk with tabular figures; there is no mono. iOS roles, 4 sizes:

| Role | Size / weight | Used for |
|---|---|---|
| Large title (display) | 54 Newsreader **300**, opsz 72 | episode title |
| Title 2 | 23 Newsreader 400 | transcript line, "Chapters" |
| Body / headline | 17 Hanken 400-600 | show name, chapter titles, current chapter |
| Footnote | 13 Hanken 500-600 | caps labels, times, speed, the numbers in the skip icons |

The title is light on purpose. The engine's heading weight (650, from Energy) is too heavy for a quiet night title, and there is no way to ask for light display titles.

## Color
The page is navy near-black (`accent2-dark-2` `#1c2029`, because the neutral dark ramp stays almost grey). The text is ice white (`#e6e9ee`). The single accent, ice blue `#adc4f5`, is used for the play button, the progress and the transcript fill box, with dark text on it. The canvas duotone runs ink → ultramarine → ice, from the same tokens.

## Where I left the tokens, on purpose
- The cover art is a canvas: fractal noise posterized into 9 levels, with contour lines, grain, a moon with a glow and a dotted river route. Its colors are read from the token CSS at run time. The small coordinate label in the art is decorative.
- A 196 px top margin lets the title overlap the faded art.
- A bottom fade over the chapter list shows that it scrolls.

## Changes for the owner's type and color rules
- **Palette replaced.** Plum near-black with apricot was too close to "brown-black with orange", and piece 02 already uses peach on dark indigo. It is now night navy and ice blue.
- **Three fonts became two.** JetBrains Mono is gone; times and labels use Hanken Grotesk with tabular figures.
- **Display face changed** from Instrument Serif (used by piece 02) to Newsreader, which has a light weight.
- **Italic-word trick removed.** "moved" was italic apricot; the title is now one light roman line. Italic headings ("Chapters", the show name) are now roman.
- **Transcript highlight** is now a fill box (ice blue, dark text), the allowed form.
- **Scale:** 54, 23, 17, 13. The 12 px skip numerals became 13, so no two sizes sit within 10%.

## Checks
- `engine.py validate`: no errors; 2 light-mode warnings (above).
- `preflight.py html`: 0 errors and 0 warnings after the change. Earlier it reported a `<br>` in the title (fixed with `text-wrap: balance`) and 10 px numerals (fixed).
- Review probe: 0 errors and 0 warnings. Before the type change it caught 10 px text in the skip icons and 13 px padding off the ladder; both fixed.

## Process findings
- **Bug (important):** with `--delegated all`, `sketch` rewrites an explicit `--brand` to a white-text shade. Apricot `#E8946A` became brown `#AF6037` in `state.json`, even though apricot carries dark text perfectly on a dark player. (feedback recorded)
- **Confusing:** `--theme dark-only` is refused by a house standard with no hint about what to do instead (keep both modes and set the default theme). (feedback recorded)
- **Gap:** dark neutrals ignore most of `neutralBase`: a navy base still gives near-grey `#131519`, so the navy page uses an accent step.
- **Gap:** there is no input for a light display weight; heading weight comes only from Energy.
- **Gap:** `OPEN_FONTS` did not know Instrument Serif or Newsreader. (feedback recorded)

## Round 3 (owner review, 2026-10-14)
**What he said:** "can be a little better." The audit before it named the generated contour-map art with a glowing moon and a coordinate label (a motif repeated across the showcase), and reused invented data.

**What changed:**
- **The cover is a real photograph, made into a cover.** Dave Hoefler's "River between grass" (free Unsplash licence, checked on its photo page; `images.unsplash.com/photo-1567475360083-31f83e5e9b0e`, cropped with `rect=` so the top-right corner is plain grass), set as a duotone from navy to ice in a 132 pt square with "Night Cartography" in Newsreader on it. The river bend is the episode's subject ("The river that changed its mind"). The canvas, moon, glow, route and coordinate label are gone, and so is the full-bleed texture behind the header: the page is flat navy.
- **Accent with one job.** Ice blue marks "now" only: all played time in one fill, the phrase being spoken, and the current chapter's number and time. Play is ice white with a navy glyph.
- **Labels.** No letterspaced capitals: "Episode 41 · 52 min · 12 Oct", "Transcript · Yusra Quennell", "Chapter 3 of 6 · The river that changed its mind" on one line, "Full transcript" in sentence case.
- **Platform.** `--ds-size-target-min` is 44 in the piece (the token resolves to 24 under `pointer: fine`, which the renderer reports); the transport is a five-column grid with play centred on the screen; the nav glyphs, "1.2×" and the sleep moon sit on the 20 and 370 margins.
- **Chapters** are a table of contents under a sticky header, scrolled one row so 02 (played, dimmed), 03 (now) and 04 show; rows share a baseline and the leaders end on one line; times are m:ss to match the scrubber.
- **Data.** The fill inside chapter 3 was 54% for 18:42 (it should have been 59%); elapsed is now 17:05, remaining −34:55 (52:00 in all), fill 43% = 4:23 of 10:12. Chapter starts 0:00, 4:06, 12:42, 22:54, 32:18, 44:24; segment widths 4.1, 8.6, 10.2, 9.4, 12.1, 7.6 minutes. "Ines Valcourt" (Ines is also in `app-screens/02`) is now Yusra Quennell; "18:42" is gone.
- Type roles: Display 54 (Newsreader 300) · Title 2 22 · Body 17 · Subheadline 15 · Footnote 13, plus the cover's own 20 pt type. `overrides.font.size.15` and `.22` added through the engine.
- References this round: Neuecast https://mobbin.com/screens/c1987944-c25e-4f79-ad38-2a2d44bdd7f9 (a type-led player), Brink https://mobbin.com/screens/cf024e3b-bc8b-4981-b433-0cfbe5ae11bd (cover, chapters, 15/30 skips and sleep in one row), Spotify https://mobbin.com/screens/646eefc4-43bd-4950-8b14-11a1431f9bfd (speed, skips and timer under the scrubber; a white play button).

**Fresh-eyes audit** (fresh-context agent, against the B2B product screens and the three references): **3/5** (24 pt targets from the token, play off centre, the cover still texture, crushed bottom, two accent jobs), **3/5** after the first rework (current chapter under the fade, rows off their baselines, a pasted-on cover band), then **4/5**, with four polish items (sticky-header hairline, header spacing, leader ends, cover type contrast), all applied after it.

**Checks:** `engine.py build` passes (2 light-mode warnings, not used here). `preflight.py html`: the Google Fonts `<link>` false positive only. `check_dates.py --year 2026`: passes.
