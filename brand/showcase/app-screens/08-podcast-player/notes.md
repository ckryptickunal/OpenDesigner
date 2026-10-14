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
