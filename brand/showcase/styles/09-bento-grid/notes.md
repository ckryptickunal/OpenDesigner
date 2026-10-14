# 09 · Bento grid · Holdfast

**Final self-audit score: 4 / 5** (3 rounds). Render: `shot.png`, 1440 x 900 at scale 2.

## Direction
Holdfast is a fictional help desk for B2B support teams that have contracts to keep. Every ticket carries its SLA (service-level agreement: how fast you promised to answer), so the queue sorts itself by the next promise about to break. This piece is the product's feature section: a bento grid of five tiles, each showing a real piece of the product. Feel words: **clean, confident, practical**.

## The style
- **In plain words:** a bento grid is a page section made of rounded tiles of different sizes that lock together like the compartments of a lunch box. Each tile holds one idea, and the sizes tell you which idea matters most.
- **What defines it (checkable):**
  1. One grid with a single gap (here 16 px) between all tiles, and one outer radius (24 px) on every tile.
  2. At least three different tile sizes; the largest tile holds the main idea (here the inbox, 5 columns by 2 rows).
  3. A tile colour hierarchy: most tiles share one surface, one or two are inverted or filled to set the rhythm (here one sun-yellow tile and one ink tile).
  4. Each tile is a whole thought: a short caption plus one object, with no tile depending on another.
  5. The objects are real product UI at a readable size, not icons.
- **How it goes wrong:** identical cards in a uniform 3 x 2 grid (that is a card grid, not a bento); an icon plus an adjective per tile; floating, tilted UI fragments with soft shadows; every tile a different pastel; text so small the UI is decoration.
- **How I kept it premium:** every tile shows working product with believable, internally consistent data (ticket #48207 is the selected inbox row, the SLA clock and the snooze menu); one typeface carries everything through size and weight; colour does one job (yellow means "time is running", ink means "keyboard"); one tile's UI bleeds off its edge to break the box-in-box rhythm; no shadows, no gradients.

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| Linear, Asks features: https://mobbin.com/sites/sections/2bf6ad95-a30f-4623-9d10-b243918e1a9b | Unequal tile widths in a 2 x 2, a real form as the hero of a tile, and the caption as a short bold-plus-regular sentence |
| Cycle, feature mosaic: https://mobbin.com/sites/sections/cec6d26c-c967-4aff-bc76-7e5e5cce4699 | A true bento: one tall tile beside smaller ones, objects cropped by the tile edge |
| Plain, "and so much more": https://mobbin.com/sites/sections/d84b60ea-df64-48e5-a209-b2b6ce9cc79a | A support product's features shown as UI fragments (issue, chat, command menu) rather than icons |
| Plain, support thread: https://mobbin.com/screens/bfd38f18-8817-4724-a0e3-8d2abdfde0fa | The anatomy of a modern support queue: priority, status, timeline, Reply R and Note N key hints |

Mobbin's section search mostly returned uniform card grids for "bento"; true asymmetric bentos were rare (Cycle was the clearest). The structure therefore comes partly from first principles (above).

## System (engine)
```
sketch --name Holdfast --brand #FFD23F --audience regular --platforms web --feel clean,confident,practical --theme system-light-dark --surfaces "landing page:persuade" --delegated all
set raw.brandColor "#FFD23F" --set-by chosen      (the sketch had swapped it for olive #8f7200)
set raw.textFace "Schibsted Grotesk"; set raw.fontLicence {...}
```
`--theme light-only` was refused by house standard STD-visual-details-24, so the system has a dark mode the piece never shows.

| Dial | Value | Why, and what it expresses of the style |
|---|---|---|
| roundness | 62 | **Bento:** gives radius-24 for tiles and 12 for nested UI |
| depth | 8 | **Bento:** flat tiles separated by gap and tone, no shadows |
| colorfulness | 30 | **Bento:** ink, greys and one yellow, so the tile hierarchy reads by fill, not by hue |
| expression | 45 | A composed marketing section with some character |
| brandPresence | 45 | Yellow on one tile and the SLA moments only |
| density | 45 | Roomy tiles holding dense real UI |
| energy | 30 | Calm; the timer is the only live thing |
| warmth | 40 | 20 made the greys blue-lavender (#e7ecf4); 40 is a true neutral grey (#eaebee) |

**What the dials cannot express:** the grid itself (column spans, row heights, one gap), the tile colour hierarchy (which tile is filled or inverted), and the "UI bleeds off the tile" crop. All three were set by hand in CSS. There is no tile role in the radius tokens; I used `radius-24` (outer) and `radius-12` (inner).

## Type
One family: **Schibsted Grotesk** (SIL OFL, Google Fonts). Weight does the highlighting (600 for the tile name, 400 for its sentence); the headline is regular 400 with no highlighted phrase.

| Role | Size (token) | Use |
|---|---|---|
| Display | 76 (`font-size-76`) | SLA clock "14:32" |
| Headline | 49 (`font-size-49`) | Section headline |
| Title | 39 (`font-size-39`) | CSAT score |
| Body large | 20 (`font-size-20`) | "%" beside the score |
| Body | 16 (`font-size-16`) | Captions, intro paragraph |
| Label | 13 (`font-size-13`) | All UI inside the tiles |

Tabular figures are set only on the SLA chips and tab counts: in this face `tnum` also widens `.` `,` `:` (first render showed "keep ." and "14 : 32").

## Outside the tokens, on purpose
- Grid geometry (12 columns, rows of 322 px) and the macro card's negative margins for the bleed.
- Every on-ladder spacing now uses `--ds-space-*` (22 values converted; the render is pixel-identical). `engine.py review` still lists 31 raw values: 21 sizes (off-ladder row paddings of 9 to 11 px and icon sizes, chosen to match shipped support tools' row heights), 7 small radii, the yellow-tile track colour and the selected row's inset bar.

## Checks
- `engine.py validate`: no errors. Warnings: yellow action fill on light surfaces is 1.4:1 (advisory; no button relies on it, the only yellow control text is ink on yellow at 10.8:1) and one macro conflict that never clears.
- `preflight.py html`: 1 error, M9 for the Google Fonts face, a false positive (the browser's font list shows 400/500/600 loaded). Earlier real errors fixed: 11 px text raised to 13, display tracking eased to -0.03em.
- Contrast (measured from tokens.css): ink #232427 on white 15.5:1; secondary 7.3:1; tertiary 5.9:1; "Late 4m" danger text 7.2:1; "+1.8 pts" success 7.3:1; ink on yellow 10.8:1; ink tile captions 6.7:1.
- Targets: the only link is 24 px tall; key caps are illustrations inside `role="img"` regions.

## Rounds and self-audit
Compared at 768 px width with Linear Asks, Cycle and Plain (a side-by-side sheet made in the scratchpad, then deleted). The scores for rounds 1 and 2 were given afterwards, from what each render showed; the final score was given against the sheet.
1. **Round 1 (score 2):** spaced punctuation from `tnum` on body text, a four-line headline pushing the grid off the frame, the bold-last-word headline highlight (an audited tell).
2. **Round 2 (score 3.5):** fixed those; the inbox's last row was clipped, the CSAT tile had a dead middle, the "Goal 92%" label sat on the bars, the page grey was lavender.
3. **Round 3 (score 4):** inbox trimmed to 8 rows with its footer, taller chart and a legend, warmth 40 for true grey, the macro card bleeds off the tile's right and bottom edges, shorter keyboard caption.

**Tells from making.md section 11 still present:** initials avatars in the inbox (a real assignee pattern in support tools, but generic). None of glow, decoration, invented proof, the hero recipe, or floating UI.
**Why not 5:** the section head (headline left, paragraph and link right) is conventional, and only the yellow clock tile is truly ownable.

## Process findings
1. **`--delegated all` swapped the brand colour again** (sun yellow to olive). Recorded as a bug.
2. **Warmth's neutral point is near 40-50, not where "cool" suggests**: 20 gave lavender greys. Recorded (confusing).
3. **No tile or bento vocabulary** in the system: grid spans, tile radius versus nested radius, tile fill hierarchy. Recorded (gap).
4. **Tabular figures widen punctuation** in some faces; guidance should limit `tnum` to columns of numbers. Recorded (idea).
5. **light-only is refused** by a house standard even for a light marketing section. Recorded (confusing).
6. Helped: the radius and space ladders were right for bento without edits; validate's yellow-on-light warning was correct.
