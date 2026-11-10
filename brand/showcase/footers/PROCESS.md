# Footers: process report

Eight footer sections for eight fictional brands, each made through OpenDesigner (Mobbin references, an engine-made system, build, renders, checks). All renders are 1440 wide at scale 2 with `--full`, plus a 390-wide phone render (`shot-mobile.png`). The owner's type and colour rules (added mid-run) were applied to all eight; each `notes.md` has a section saying what changed.

## The pieces

| # | Folder | Brand and direction | Palette | Type (scale used) | Desktop render |
|---|---|---|---|---|---|
| 01 | `01-brask-wordmark` | Brask, creative studio. Giant wordmark set ink-to-ink across the page, cropped by the bottom edge; one invitation above it | Neutral black #151515, white #e9e9e9, signal orange #ff4d00 (used three times) | Archivo only. 12 / 16 / 21 / 67, wordmark fitted as art | 1440 x 796 |
| 02 | `02-keystrata-mega` | Keystrata, cloud security. Six-column mega footer on a strict grid, live status console (90 days of uptime bars, region latencies), certifications, disclosure, region and language picker | Cool white, graphite, deep teal #0b7a6f, status green | IBM Plex Sans + Plex Mono (data only). 12 / 14 / 24 / 29 | 1440 x 799 |
| 03 | `03-quietfield-horizon` | Quietfield, AI research lab. Newsletter-led; a planet's rim lit violet, magenta and amber at the bottom, starfield above | True black, white, violet / magenta / amber light | Sora only. 12 / 16 / 21 / 67 | 1440 x 945 |
| 04 | `04-tumbletree-meadow` | Tumbletree, learning app for ages 4 to 8. SVG meadow, rising sun, Pip the mascot flying a kite, sticker-style panel and buttons | Sky blue, meadow greens, sun yellow #ffc83d, tangerine mascot | Fredoka + Nunito. 12 / 16 / 21 / 28 / 51 | 1440 x 836 |
| 05 | `05-salt-ledger-index` | Salt Ledger, independent print quarterly. Footer set as a contents page: double rule, huge italic issue numeral, sections with roman numerals, dotted leaders and page numbers | Warm paper #efebe4, ink, oxblood #7a1f1f | Newsreader only. 12 / 16 / 21 / 28 / 38, numeral 248 as art | 1440 x 661 |
| 06 | `06-knurl-brutalist` | Knurl Supply, streetwear drops. Black marquee, 4 px bordered blocks with hard offset shadows, drop countdown, knurl-pattern block with a round stamp | Acid lime #c8ff00, black, white | Big Shoulders Display + Space Mono. 12 / 16 / 28 / 51 / 90 | 1440 x 758 |
| 07 | `07-sasame-tea` | Sasame, eight-seat tea house in Kanazawa. Hanging-scroll moment: brush ensō, vertical place names, vertical phrase 一服の、静けさを。, vermilion seal; three quiet notes on the left | Pale celadon paper #e0e4db, sumi, matcha, seal vermilion | Shippori Mincho only. 13 / 16 / 25 / 39 / 49 | 1440 x 725 |
| 08 | `08-rallo-app` | Rallo, running and strength coaching app. Cobalt panel, generic store-style badges ("Get it on your phone"), rating, a phone rising from the panel edge with a live tempo run, floating stat cards | Cobalt #2b45ff, white, mint #00e9a5 | Plus Jakarta Sans only. 12 / 16 / 21 / 28 / 51 / 67 | 1440 x 922 |

Directions were written side by side before building (domain, palette, type, layout idea, shape language, mood). The closest pair is 05 and 07: both are paper grounds with a serif and a red accent, because "editorial magazine" and "Japanese tea house" both pull that way. I moved 07 from warm washi to a pale celadon ground under the owner's colour rule, which separates them, but they remain the two most related pieces.

## Honest assessment
- Strongest: 01 (the fitted, cropped wordmark with a regular headline and one orange box), 03 (the horizon light), 05 (the contents-page idea is fresh for a footer), 06 (loud and coherent).
- 02 is competent but conventional; enterprise footers are conventional by nature, and the status console is its one memorable idea.
- 07 relies on the ensō, a familiar motif, and has a wide quiet band above the legal row that some will read as empty rather than "ma".
- 08's phone is a CSS mockup and the scan square is a decorative pattern, not a working code; believable at a glance, generic up close.
- 04's mascot is hand-drawn SVG by a non-illustrator: charming at footer size, not a character a studio would ship as a brand asset without an illustrator.

## Process findings, most important first

### The engine or a skill is wrong or missing something

1. **`sketch --delegated all` silently rewrote the brand colour.** I gave `--brand "#ff4d00"`; the state became #d63f00 ("a readable shade") and DESIGN.md called it "a red". The brief told every builder to use `--delegated all`, so every builder who gave a brand hex got a different one. Evidence: `01-brask-wordmark/opendesigner/decisions.md` (D-0004 the given hex, D-0005 the rewrite, D-0021 where I set it back), engine `cmd_sketch` (the `if sb("brand")` branch). With `--delegated feel,audience,...` (brand left out) the hex stays exact, which I used for pieces 02 to 08.
2. **Preflight cannot see what the engine produces.** In 7 of 8 pieces `preflight.py html` raised `font "<face>" is used but has no @font-face` for faces loaded with a Google Fonts `<link>`, which the brief allows (it did not flag Plus Jakarta Sans in 08, so the check is also inconsistent). Its type-scale check reads only px, so every rem size from tokens.css is invisible: it printed `font sizes in px: []` for six pieces and only the art sizes for the rest. The checks that matter most for this test (font loading, scale discipline) therefore said nothing true. Evidence: the Checks section of each notes.md.
3. **Answers silently change the type system.** A "read" surface (`--surfaces "research site:read"`, `"magazine:read"`) turns off marketing surfaces and caps the scale at 2.5 x body, so the largest size was 38 px with no notice (03, 05; fixed with `set raw.marketingSurfaces true`). `--audience large` leaves body at 16 px (`resolve` shows `type.baseSize.web 16`) while `stages/02-audience-and-commitments.md` promises "body 17px or more" (04).
4. **The type scale is bigger than the owner now wants, and nothing counts sizes.** Every build with marketing surfaces emits 8 font-size steps (for example 12, 16, 21, 28, 38, 51, 67, 90). Preflight warns only above 10, `engine.py review` does not count the sizes a page uses, and piece 06 used all 8 until I trimmed it to 5 by hand.
5. **High warmth makes neutrals brown, with no warning.** Warmth 62 gave #151514 / #ebe8e6 under an orange brand (01), warmth 90 gave brown ink #282321 and grey #605551 on a sky-blue page (04). The owner's new colour rule forbids exactly this. Warmth also drives voice (contractions, tone), so "warm voice" and "warm neutrals" cannot be set apart.
6. **Style vocabulary the showcase needed is missing.** No zero-blur hard offset shadow (neo-brutalism; `stages/15-depth-borders-and-materials.detailed.md` even says "One hard shadow looks dated"); no token for a variable-font axis (wdth for the wordmark); no figure style or small caps (editorial); no vertical writing; the fallback stack is always the system sans, even for Shippori Mincho, and adds no Japanese faces when `raw.scripts` includes Jpan; no gradient token; no hairline border role lighter than `border.subtle` (step 7 is heavy for a 40-rule mega footer); no "page tone" (paper, cream) answer, since `raw.neutralBase` only sets hue.
7. **Dark sections are awkward.** `--theme dark-only` is refused by STD-visual-details-24, yet a dark footer band is not a dark-only product; the route is system-light-dark plus a pinned `data-theme="dark"`. In dark mode, accent step 9 is a desaturated brand (#ff4d00 became #e76944), so an exact signal colour on black needs `--ds-color-brand-seed`.
8. **Warnings that do not clear.** "The feel words X, Y pull <dial> in opposite directions. Pick which one wins" stays on every build after that dial is set explicitly (03, 08).
9. **`engine.py review` suggests wrong replacements.** It maps every px to a spacing token, including a 6 px status dot, a 12 px icon and a 20 px logo height; it suggested `--ds-elevation-raised` (a soft zero-size shadow here) for a `3px 3px 0` hard shadow, and a border token for a focus-style halo.
10. **The open-font list is short.** Archivo, Fredoka, Newsreader, Big Shoulders Display and Shippori Mincho (all SIL OFL) are not in `OPEN_FONTS`, so DESIGN.md lists "Licence risks: confirm the web licence" for free fonts until `raw.fontLicence` is set by hand.
11. **Naming a typeface is hard to discover.** No `--font` on sketch; the question route picks among six built-in open faces; any other face needs `set raw.textFace '"Name"'` (JSON-quoted). `raw.fontClass` + `raw.textFace "=openClass"` works well (08) but I found it in engine.py.
12. **opendesigner-illustrate needs a person to say yes before fetching,** so an autonomous builder cannot use it; all art here is drawn in SVG, canvas or CSS instead.

### Where it helped
- `--delegated` with a list kept the brand hex exact from piece 02 on.
- `raw.accentCount` plus `raw.secondaryColors` turned extra colours into real ramps with dark steps (03's horizon light, 04's sky and grass, 07's seal, 08's mint), so most art colours stayed on tokens.
- `raw.darkBase "black"` was exactly the switch 03 needed; `raw.scripts` with Jpan added a `:lang(ja)` line-height scale.
- Contrast warnings on pale action colours (yellow 1.5:1 in 04, lime 1.1:1 in 06) caught real problems; the right fix there was a border, which the warning does not mention.
- `engine.py review` plus `od-ignore` is a fast, clean way to keep deliberate raw values and still get a clean report (05).
- `set` prints which tokens a change touches, which made dial tuning quick.

### I worked around it (recorded so the next builder knows)
- Pinned `data-theme` for dark footers (01, 03); used `--ds-color-brand-seed` for the exact orange on black (01).
- Hand-wrote the hard shadow (06), the width axis (01), old-style figures and tracked labels (05), vertical writing and a Mincho fallback stack (07), hairlines at neutral step 4 (02), gradient stops (03).
- Set `raw.fontLicence` by hand for OFL faces the engine did not know (04, 05, 06, 07).
- Mobbin: style words are weak in `search_sections` (no real neo-brutalist or editorial contents-page footers came back), and the same sites repeated across unrelated queries (Zellerfeld, BAGGU, Swap, Glossier, Notion). Structure references were still useful for 01, 02, 03 and 08.

## Feedback recorded
Every gap above is in a `feedback.md` next to the system it came from (`engine.py feedback`, written locally, nothing posted): 01 has 7 entries, 02 3, 03 3, 04 4, 05 3, 06 2, 07 2, 08 2.
