# 11 · Terminal · coppice

**Final self-audit score: 4 / 5** (4 rounds). Render: `shot.png`, 1440 x 900 at scale 2.

## Direction
coppice is a fictional embedded SQL database in one 4 MB binary whose branches are copy-on-write: a 2.1 GB database branches in 41 ms and stores only the pages you change. This is the top of its documentation home. The page is written like a Unix manual page (`COPPICE(1)` header and footer, NAME, SYNOPSIS with underlined arguments) beside a real terminal session and a box-drawn storage diagram. Ink on white paper with one signal red, so it is a different direction from the amber-on-black rackhound settings panel already in the showcase. Feel words: **technical, minimal, bold**.

## The style
- **In plain words:** the terminal style makes a web page look and behave like a command line: everything in a monospaced face, lines and frames drawn from text characters, real commands and their output, and a keyboard for every action.
- **What defines it (checkable):**
  1. One monospaced family carries all text, so every character sits on the same column grid.
  2. Frames, tables and diagrams are drawn with box-drawing characters (U+2500 block: `┌ ─ ┐ │ └ ┘ ├ ┼`) or with 1 px rules that behave like them.
  3. Real sessions: a prompt, a command, believable output with units and timings, and a waiting cursor.
  4. Keyboard first: every main action shows its key (`g`, `r`, `c`, `/`, `y`, `1` to `3`), and the keys work.
  5. Terminal conventions used as structure, not ornament: here the man-page header and footer, underlined arguments, `$` prompts, inverse video for the selected tab.
- **How it goes wrong:** green-on-black "hacker" clichés with scanlines and glow; ASCII art whose glyphs fall back to another font and misalign; a fake macOS window with traffic lights pasted on a marketing page; commands that do not run or output that does not add up; mono for headings only with a sans everywhere else.
- **How I kept it premium:** one face with a true light weight for the headline (Lilex 300), one red with one job (you and your branch: prompts, cursor, the branch's commits and its own pages), numbers that add up (1,084,211 + 81,273 + 38,904 = 1,204,388 rows, the same count the `alter table` reports), a diagram that carries the product's claim (98% of pages shared, 41 MB owned), and a face chosen because its box-drawing glyphs close (see findings).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| The Content Architecture, repo-as-page: https://mobbin.com/sites/sections/29bfe158-19c6-48e3-b87a-f4e5e03b0e6f | The chrome can be the page: caps mono labels, a terminal pane, a status line with true data |
| Hermes Agent, install via terminal: https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35 | The install command as the primary action, with OS tabs and a copy control |
| Cloudflare, AI Gateway code examples: https://mobbin.com/screens/f9e55e3d-7097-491f-8136-58312d972c25 | Docs that lead with a working request and its options |
| Shopify Supply, dev mode: https://mobbin.com/sites/sections/85479695-55d2-4f92-89bc-1790dda9d9d9 | A prompt line and text-drawn type as the whole hero; I took the prompt, not the ASCII banner |

## System (engine)
```
sketch --name coppice --brand #E0301E --audience dense --platforms web --feel technical,minimal,bold --theme system-light-dark --surfaces "docs:read" --delegated all
set raw.brandColor "#E0301E" --set-by chosen     (the sketch had nudged it to #df2f1d)
set raw.textFace / raw.monoFace: "Martian Mono" -> "Chivo Mono" -> "Lilex" (see findings)
```
| Dial | Value | Why, and what it expresses of the style |
|---|---|---|
| roundness | 0 | **Terminal:** square cells, square frames, square keycaps |
| depth | 0 | **Terminal:** paper has no shadows; frames are 1 px ink |
| density | 70 | **Terminal:** dense rows (14 px body, dense 12 to 35 scale) |
| colorfulness | 25 | **Terminal:** ink on white and one red, like a printed session |
| energy | 20 | Only the cursor blinks (and not under reduced motion) |
| expression | 60 | A stylised page, played straight |
| brandPresence | 40 | Red only on prompts, the cursor and the branch |
| warmth | 45 | Neutral paper, never cream |

**What the dials cannot express:** the monospace grid (every size and column width in `ch`), glyph coverage for box drawing, the man-page structure and the keyboard map. All set in `index.html`.

## Type
One family, **Lilex** (SIL OFL, Google Fonts): 300 for the headline, 400 for text, 600 for command names and labels.

| Role | Size | Use |
|---|---|---|
| Display | 40 (off-scale) | Headline: the dense scale stops at 35; at 40 the headline sits on two balanced lines in a 580 px column |
| Title | 17 (`font-size-17`) | Wordmark |
| Body | 14 (`font-size-14`) | Description, synopsis, session, diagram, install |
| Label / caption | 12 (`font-size-12`) | Man header and footer, section labels, keycaps, frame titles |

## Outside the tokens, on purpose
- The 40 px display size (above).
- The cursor blink starts after 2.4 s so the static render always shows it.
- 20 on-ladder spacings converted to tokens; `review` lists 21 raw sizes left (off-ladder gaps such as 22 and 26 px chosen to land on text baselines).

## Checks
- `engine.py validate`: no errors, no warnings.
- `preflight.py html`: 1 error, M9 for Lilex, a false positive (the browser loaded 300/400/600).
- Contrast: ink 15.5:1, dim text 7.2:1, red text (accent 11, #aa1f11) 7.2:1, the faint argument underlines 3.6:1 (decoration under text that already passes).
- Targets: nav links 28 px, keycaps 24 px, search 34 px, focus ring 2 px red.
- Keyboard: `/` focuses search and `y` copies the install line (script at the end of the page).

## Rounds and self-audit
Compared at 768 px width with The Content Architecture, Hermes Agent and Cloudflare (scratchpad sheet, deleted). Early-round scores were given afterwards from what each render showed.
1. **Round 1 (about 3):** Martian Mono, the first choice, has no box-drawing glyphs at all; I caught it with a glyph test before rendering and moved to Chivo Mono.
2. **Round 2 (3):** the page worked, but the query result table never closed: Chivo Mono's corner and tee glyphs put their vertical strokes off its plain bar.
3. **Round 3 (3.5):** tested six faces at 3x zoom; only Lilex and Geist Mono close a table. Switched to Lilex; search border made ink like every other frame.
4. **Round 4 (4):** next to Hermes the page was the quietest of the set, so the headline went to 40 px in a wider column (two lines, no widow), which also balanced the two columns.

**Tells from section 11 still present:** none of the listed ones; the risk is the opposite, a page so restrained it is easy to scroll past.
**Why not 5:** no single object only coppice could own; the storage diagram comes closest.

## Process findings
1. **No glyph-coverage check for the mono face.** Martian Mono and 10 of 24 other open monos tested (Azeret, Space, Sometype, Reddit, Fragment, Inconsolata, Ubuntu Sans Mono, Cascadia Code and Mono, Atkinson Hyperlegible Mono) lack box-drawing glyphs entirely and 2 more lack some, and some that have them (Chivo, Spline Sans Mono, Source Code Pro) do not close tables at 14 px. Recorded (gap). Rackhound hit the same problem.
2. **The dense scale has no display role** for a docs hero. Recorded (gap).
3. **preflight M9 is a false positive** for every Google Fonts `<link>`. Recorded (bug).
4. **The delegated sketch nudged the red** (#e0301e to #df2f1d): harmless here, but it is the same silent swap as 09 and 12.
5. Helped: roundness 0 and depth 0 gave exactly the square, shadowless system; the space ladder fitted a character grid.

## Polish round 2026-10-14
After the independent audit (score 4, two fact errors and a real-product name). **Renamed burrow to coppice.** Burrow is LinkedIn's open-source Kafka consumer-lag monitor. Coppicing cuts a tree so it regrows as many shoots, which is what branches are. A web search found no database or data-infrastructure project by that name; the only uses are a Mac notes app and forestry software. The domain is coppicedb.dev, which has no DNS records. Name mentions above are updated; the rest of the text above describes the version before this round. A fresh-context reviewer re-audited it twice; final score **4**, with no fact errors left.

**What changed**
- **The diagram forks where the terminal says.** It now forks at 4f2a91c, the fifth commit.
- **The branch's own pages are earned.** They come from an UPDATE of the 81,273 pending orders, not from the metadata-only ALTER. The diff reads "81,273 rows changed · 38 MB of own pages". 38 MB of 2.1 GB is 1.8%, so 98% is shared, and the own-pages mark is half a cell of 28.
- **Less chrome.** The headline cursor is gone. The man-page chrome appears once (COPPICE(1) at the left, the version at the right), and a SEE ALSO section balances the columns.
- **Red has one job:** the branch's commits and its own pages. The prompts and the wordmark block are ink.
- **Every control works.**
  - The false "96×30" is removed.
  - Every keycap works, and "/" focuses a real search input.
  - The copy button and the arrow keys on the OS tabs work.
  - The query table has a text version.
- **Engine.** `pick Q-dir-01 terminal`; the name is set; the stale build file `burrow.resolver.json` is removed.

**References used by the re-audit:** Hermes Agent (https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35), The Content Architecture (https://mobbin.com/sites/sections/29bfe158-19c6-48e3-b87a-f4e5e03b0e6f), Supabase (https://mobbin.com/sites/sections/6d6921ce-b43a-4232-9ebd-966b1338c349).

**Left:** the box-drawing joints show faint ticks at 2x, and the wordmark block still reads a little like a cursor.
