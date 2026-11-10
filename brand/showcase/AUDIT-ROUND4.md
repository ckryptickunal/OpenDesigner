# Showcase audit, round 4 (15 October 2026)

Most of the showcase is not yet at the level of the B2B product screens. Of the 71 pieces the gallery shows:
- 13 are worth keeping as they are;
- 28 need a specific polish;
- 24 need rebuilding;
- 6 should come off the gallery.

The biggest single reason is the one you named: the pieces are **cluttered**. Every region carries its own legend, note, chip row or mini-panel. In the blind tests, judges who had never seen our work kept saying the same thing. Our pieces are "much denser than shipped pages", with "everything labelled" and "microcopy explaining every row".

## How this was judged
- **What was looked at.** Every piece the gallery shows (71), from its full-size `shot.png`, at 1x and in 2x crops. Pieces replaced on 14 October and the four heroes you removed were skipped.
- **Pieces rebuilt during the audit.** Eight web components were rebuilt while this audit ran (01, 03, 05, 06, 07, 08, 09 and 10). Each was scored on its newest shot, as of 06:03 on 15 October.
- **App screens.** The pages of six shown app screens (01, 03, 06, 07, 09 and 10) were rebuilt after their shots were taken. The gallery still shows the old shots, so those shots are what was scored.
- **The scale.** 1 to 10, set by your eye:
  - the B2B product screens, Orbika, the live workout, the boarding pass, Margin and footers 01, 02 and 08 are 8 or 9;
  - the private banking home is 3;
  - shipped products such as Linear, Stripe and Revolut are 9 or 10.
- **The actions.** Keep is 8 or more, polish is 6 or 7, and rebuild is 5 or less. Remove means a piece is not worth rebuilding, or it repeats a better one.
- **References.** 35 shipped screens and sections from Mobbin, covering every category; the links are at the end.
- **A blind check on my own scores.** 37 side-by-side pairs went to fresh judges with no labels: our piece against a shipped screen of the same kind, sides chosen at random. The results are below the patterns.

## The five patterns that make our pieces look cheap
1. **Too much on one screen (30 pieces).** Each panel brings its own legend, meta line, footnote, icon tile or chip row, so the eye has nowhere to rest. Examples:
   - the Ackwire settings modal has an icon on every row, a timeline, a callout and a save footer;
   - the Gridlark date picker shows two ranges, ten presets, two time fields and a legend at once;
   - the Salt Ledger footer holds an issue promo, a contents list, a newsletter, nav columns and a 24-spine chart.

   Shipped pages show one moment and leave the rest out.
2. **Decoration doing the work (26 pieces).** Examples:
   - glow on numbers and lines;
   - a blurred orange blob (Prill);
   - painted sky texture (Tidemark);
   - clip-art flowers (Lullwort) and a stock-looking clay avatar (Arrivant);
   - tilted floating cards and stickers (Plenary, Rallo, Orbika);
   - crop marks and halftone corners (Halftone Yard);
   - brown, orange and cream palettes (Larder, Wardlight).
3. **Dead space next to cramped edges (23 pieces).** A large empty hole sits in one place while things press against an edge elsewhere. Examples:
   - about 230 px of black under the Nearmost button;
   - a blank top third above the Oriel composer;
   - Bauhaus shapes cut off at the bottom;
   - a holdings row running under the tab bar (Halden);
   - watch buttons pressed against the bezel.
4. **Type that fights (20 pieces).** Examples:
   - a Didone total beside system text (Halden);
   - three faces on one watch screen (Fellrise) or one comic page (Nightjar);
   - monospace for everything (coppice, Leeward);
   - a display number that overlaps its neighbour (61 and 38 reading as "6138");
   - oversized rows that make a screen look zoomed in (the new Panelwise toast).
5. **Imitation and repetition (15 pieces).**
   - A viewer can name the product a piece copies: Duolingo (Parlo), Linear (Kestrel), Gusto (Sedge), Apple Home (Nook), dark Vercel-style pricing (Gloaming), Claude Projects (Oriel), incident.io (Ackwire).
   - The gallery shows the same thing twice. Three B2B heroes reuse the product screens. Five mockups show pieces you removed or replaced, or versions that have since been rebuilt.

Two more patterns are close behind. Weak hierarchy (grey on grey, or everything boxed) shows in 13 pieces. Spec-sheet framing (state grids, numbered callouts, caption plates) shows in 5, including Margin's right half.

**The gallery page adds clutter too.** It sits outside this audit's scope (`site/`), so I am only reporting it:
- many thumbnails carry a rotated rubber-stamp label ("+2 FRAMES", "BEING REBUILT") over their corner;
- every card carries three chips in three different styles (a filled pill, a mono outline and a dashed outline);
- there are 15 filter pills and a five-chip LABELS legend above the grid;
- titles carry device specs, such as "(phone, 390×844 @3x)";
- several captions name the old brand. "Orrery" is shown above a page that says Nearmost, and the same happens with "Wayfern" (now Gridlark), "Mossby" (Sedge), "rackhound" (Ackwire) and "Quarry" (the shot says Kestrel).

## Blind test: how often ours lost
- **Overall.** Of 37 pairs, ours lost 30 and won 7.
- **By how much.** Among the 30 losses:
  - 2 were obvious (4 of 5): the Sasame footer and the new Panelwise toast;
  - 12 were clear (3 of 5);
  - 14 were slight (2 of 5);
  - 2 were near-ties (1 of 5): the new Calamondin player and the new Gridlark picker.
- **The seven wins** were all by 2 or 3: Holdfast bento, Lampwright pixel, and the heroes Halde, Nearmost, Isobath, Purlin and Fennick.
- **The control.** Quoin, which you love, lost to Stripe by 2. So a loss by 2 is still consistent with a score of 7 or 8. Every piece that lost by 3 or 4 is scored 6 or lower.
- **Caveats.** Judges often recognised the shipped brand's logo:
  - in all seven of our wins, the judge said it recognised the logo and picked ours on craft anyway;
  - in the two near-ties, the judges said ours was equal on craft and they picked the shipped side only because they recognised it.

  Three pairs (the old Kinroom toast, the Wayfern picker and an earlier Tarrow) tested versions that have since been rebuilt. The new versions were tested again.

## Things to fix that are not about taste
- The Aerlo boarding pass says "Wed 22 Oct", which is a Thursday in 2026.
- The Knurl ticker says "Thu 24.10", which is a Saturday. `check_dates.py` does not catch the day.month format.
- Some invented data is reused across pieces:
  - 4'52" appears on both the Fellrise watch and the Rallo phone;
  - 41,208 appears in both Knurl and Fennick;
  - 18:24 on the Onething watch is the number `making.md` already warns about.
- Two invented domains look real: api.millrace.dev (on the Millrace footer) and id.ferrule.cloud (in the Ferrule page). The brief asks for .example.
- The gallery images are older than the page for:
  - product/04 and styles/11 (the coppice image still shows the banned install line that pipes a download straight into a shell);
  - mockups/06;
  - the six app screens above, whose pages are being rebuilt now.

## What needs your decision
1. **Take six pieces off the gallery now.**
   - Mockups 04, 06 and 08 show heroes you removed.
   - Heroes 12 and 13 repeat product/04 and product/06. I would keep hero 14 (Fennick) as the one B2B hero, because it won its blind pair by a clear margin.
   - Watch 08 is a generic timer.
2. **Re-render mockups 01, 05 and 07 only after their app screens and components are rebuilt.** Until then they advertise the weakest work. They could also come off the gallery.
3. **Parlo (app 07).** You called it "good to go". It is a near-copy of Duolingo, and a judge named Duolingo at once. Keep it, or rebuild it with its own structure?
4. **Halftone Yard (component 04).** You said "okay-ish, you can keep it". I score it 4, because half the frame is a spec sheet. Keep it, or rebuild it?
5. **Margin (component 02)** stays a keep, but its right half is a spec sheet. Should it be cropped to the palette in its app?
6. **The gallery page's stamps, chips and spec captions** are the page-level clutter. Should whoever owns `site/` simplify them?
7. **The web components are still being rebuilt.** Their scores and order should be re-run once the rebuild lands.

## Each category, worst first

### B2B product screens (average 8.7)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 06-ferrule-security | 8 | keep | The main frame is mostly rows of toggles, so it has less to look at than the audit-log frame. The SAML address uses id.ferrule.cloud, a real-looking domain; the brief asks for .example. | – |
| 04-sounding-observability | 8 | keep | The Requests chart is a perfect sine wave with a dashed twin, so the data looks generated. The Upstream timeouts card is empty and takes a quarter of the chart row. The gallery image is older than the last page edit (shot 14 Oct 21:46, page 15 Oct 02:41). | – |
| 05-kilnworks-billing | 9 | keep | Nothing a viewer notices in a second. | – |
| 03-corvane-record | 9 | keep | Nothing a viewer notices in a second. | – |
| 02-fennick-approvals | 9 | keep | Nothing a viewer notices in a second. | – |
| 01-quoin-payments | 9 | keep | Nothing a viewer notices in a second. Even so, a fresh judge put Stripe's payments list slightly ahead (2 of 5), citing the floating selection bar that covers two rows. | control: lost 2 to Stripe |

### Hero sections (average 6.6)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 13-ferrule-security | 5 | remove | 'When. Who. What. Where.' is spaced to sit over the table columns, so the gaps (about 30, 100 and 350 px) read as a broken justify. The audit-log card is product/06's frame again and is cut at the fold; a white button on flat plum looks templated. | – |
| 03-organic-wellness | 5 | rebuild | The vector daisies and leaves look like clip-art and the tin has a fake cylinder gradient. About 450 by 420 px of the lower left is empty apart from a tiny valerian dish. Clutter: a spec table, three callouts and a 50/30/20 bar on the tin all repeat the same blend. | – |
| 12-sounding-observability | 6 | remove | The product card is product/04's screen again. The 110 px headline runs nearly edge to edge, and the white card glares on the black page. The Requests chart is a perfect sine wave. | lost 3 to incident.io |
| 07-climate-observatory | 7 | polish | Contour lines run behind the headline and body, so the left half is busy texture. Clutter: lat/long labels, a dashed anomaly ring, float track dots, a profile card with three stat cells and a coordinates footer. | won 2 vs Linear |
| 01-swiss-architecture | 7 | polish | Clutter: dimension lines, level marks, two legends, a title block with a scale bar, and coordinates plus sunrise in the nav. The headline sits tight to the bottom edge, and the red full stop is a cliche. | won 2 vs Mouthwash Studio |
| 02-luminous-devtool | 7 | polish | About 230 px of dead black in the left column between the button and the stats. Clutter: the console packs four panels (search with three chips, map, eight results, query plan); '8.7 ms' at about 150 px is the familiar big-stat dev-tool recipe. The gallery caption says 'Orrery' but the page says Nearmost. | won 2 vs Better Stack |
| 11-spend-platform | 7 | polish | Weekend bars are 2 px slivers that look like dust, and the 'Books lock, Tue 3 Nov' label collides with the last bar. Clutter: a paragraph, a button and an aside note in the header, then a chart with three legend items, four filter tabs, a table and a journal-entry panel. | won 2 vs Front |
| 14-fennick-approvals | 7 | polish | The ledger figures at about 30 px compete with the headline. The product frame is product/02's screen, so the gallery shows it twice. | won 3 vs Coda |
| 08-y2k-retrofuture | 8 | keep | Clutter to watch: pixel signal arcs, a round '2,400 stations' sticker, a spec strip and a scrolling ticker all compete with the radio. | – |

### Web components (average 6.2)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 04-upload-brutal | 4 | rebuild | The right half is a spec sheet (dropzone in 4 states, button states, progress, file types) with tag chips '04 · FILE UPLOAD · NEO-BRUTAL · CMYK'. Crop marks, a halftone corner and a CMYK strip are decoration, and offset shadows box every element. The error row says it four ways (red rule, pink fill, red text, stripes). | – |
| 05-toast-stack | 5 | rebuild | Three expanded dark toasts sit over the right of the table, and row text shows through the gaps between them ('Scorecard from Gaurav…', 'Interview today'). The type and rows are oversized, so the screen looks zoomed in, with no app navigation; the close button hangs off the third toast's corner. Clutter: the three-toast stack, the clipped 'of 3' scorecard numbers under it, and three initials chips on every row. | lost 4 to Stripe (the earlier Slack-style version lost 3 to Slack) |
| 10-settings-terminal | 6 | polish | Clutter: an icon tile on every row, a quiet-hours timeline, an info callout and a save footer in one modal. The incident dates column shows through at the right edge of the dimmed page, and the open dropdown covers the Text message and Email controls. The gallery caption still says 'rackhound'. | lost 3 to hilos |
| 01-pricing-glass | 6 | polish | Clutter: a slider panel, a note line under each button and a footnote all stack up before the feature lists. It reads as a copy of the dark Linear or Vercel pricing style; slider tick labels are tiny and low contrast. | lost 2 to Recraft |
| 06-data-table | 6 | polish | The rows are too uniform: tidy city pairs, evenly grey text, and 'Late' in a muddy ochre is the only status colour. Clutter: a 'Times in CDT · tracking updated 14:06' line, two filter chips, date-group headers and a bulk bar compete around a nine-column table; the bulk bar covers a half-cut row. Three identical outlined buttons in the selection bar. | lost 2 to Stripe (an earlier version also lost 2) |
| 03-date-range-picker | 6 | polish | Clutter: two ranges at once (blue selection and grey comparison), ten presets, two time fields, a three-item legend and amber dots on Oct 6 and 7. The popover hides the KPI row and most of the chart; the grey comparison shading breaks into uneven week blocks. The gallery caption still says 'Wayfern'. | lost 1 to Gumloop (the earlier Wayfern version lost 2 to Airbnb) |
| 09-onboarding-stepper | 7 | polish | Nearly every element carries a grey second line (each step, radio card, field and table row), so nothing leads. Clutter: a holiday-notes column, a struck-through 'Fri, Dec 25' and a 'Book a call' block. The gallery caption still says 'Mossby'. | lost 2 to Snowflake |
| 07-ai-composer | 7 | polish | The top third above 'Ask across 14 sources' is blank, so the composer floats. Clutter: three attachment chips with cut-off names plus an inline chip in the prompt, and the model menu covers half the Recent list. A serif heading beside an all-sans interface. | lost 2 to Gumloop |
| 08-music-player | 7 | polish | The waveform is a uniform barcode, and its section labels are built from pipe characters with 'Intro' and 'Verse' jammed together. The player column floats high, leaving a dead band under it; the cover is a stock photo with no artwork treatment. | lost 1 to SoundCloud |
| 02-command-palette | 8 | keep | The right half is a spec sheet: a state grid (ROW, QUERY, KEYCAPS, DARK), numbered callouts 1 to 5 with leader lines, and a '02 · Command palette' label. The palette is about 640 px wide in a 1440 frame. | – |

### Footer sections (average 6.1)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 06-knurl-brutalist | 4 | rebuild | Clutter: a countdown, a crosshatch panel, a rotating seal and a ticker compete, and every element is boxed with an offset shadow. The ticker says 'Thu 24.10' but 24 Oct 2026 is a Saturday (check_dates.py misses this format); '41,208 on it' reuses product/02's $41,208.17. | – |
| 04-tumbletree-meadow | 5 | rebuild | A children's learning brand set on corporate navy. Clutter: four link columns with lesson counts, two paragraphs, and a letter-formation diagram with numbered yellow arrows and dotted guides. | – |
| 07-sasame-tea | 5 | rebuild | Clutter: a 5-row by 12-month Gantt fills the footer; '2–15 Jan' sits outside its tiny bar and the Feb gridline cuts it. The red seal sits on the baseline over the Matcha bar, and the today line vanishes behind the black 'from 1 Oct' bar. | lost 4 to Legora |
| 05-salt-ledger-index | 5 | rebuild | Clutter: an issue promo, contents, a newsletter, nav columns and a 24-spine chart, so nothing leads. The black spines are heavy, and the year ticks under them look like debug marks. | lost 3 to Notion |
| 09-b2b-platform | 6 | polish | The amber monospace date ('Fri 13 Nov 2026 15:43 UTC') is the loudest thing, louder than the brand. Clutter: three mini-tables in the lower band (status with a curl command, five regions, a compliance list). api.millrace.dev is a real-looking domain; use .example. | lost 2 to Railway |
| 08-rallo-app | 8 | keep | Invented proof: five stars and '4.9 from 38,200 ratings'. Clutter: a tilted phone, a floating VO2 card, a 'New' pill and concentric rings. 4'52" on the phone repeats the Fellrise watch's pace. | – |
| 01-brask-wordmark | 8 | keep | The orange highlight block on the headline is the hero-recipe tell; the wordmark is cut at the bottom on purpose. | – |
| 02-keystrata-mega | 8 | keep | Nothing a viewer notices in a second; a mega footer is dense by nature. | – |

### Style studies (average 5.8)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 03-claymorphism | 5 | rebuild | The 3D clay avatar on a lanyard badge, and the 3D avatar in the header, look like stock AI renders. The badge card leaves a large empty pastel area; the checklist beside it is generic. | – |
| 02-neumorphism | 5 | rebuild | Clutter: hundreds of tiny desk boxes with V-6.0x tags; every room is boxed and none leads. The thermostat dial is grey on grey and low contrast; pink over-temperature cells add a second colour story. | – |
| 06-memphis | 5 | rebuild | A tilted badge and a floating striped triangle overlap the hero. The headline 'The workshop room lets in triangles' needs the paragraph to make sense. Clutter: three shape textures (dots, zigzags, stripes) plus a stats list beside the chart. | – |
| 08-bauhaus | 5 | rebuild | The circle, triangle and square run off the bottom edge and overlap at awkward slivers. The black data panel on the right is a second design bolted on; the all-lowercase headline and nav feel affected. | – |
| 05-comic | 5 | rebuild | Three faces: a chunky comic headline, a handwritten body and monospace labels; the facts table mixes mono and handwriting. Clutter: every panel carries three or four text elements (captions, speech bubbles, a log, a chart, two 'BZZZT's) on dense halftone. At 3,402 px tall, the gallery tile crops it. | lost 3 to Equals |
| 10-mesh-gradient | 6 | polish | The orange blurred blob in the scatter plot is the glow tell even though it encodes density; a grey smudge at its top right looks like a render artifact. Clutter: an eight-row evaluator table with five numeric columns and a red value sits beside it. | – |
| 01-glassmorphism | 6 | polish | Grey placeholder bars and an empty pill pasted on the photo under 'Headline zone' look like a wireframe left in. Clutter: a tool rail on top of the crop frame, numbered pins, a rights table, five comment threads and a placements strip with a dead gap after Story. | lost 3 to DoorDash Merchant |
| 11-terminal | 6 | polish | One monospace face for everything, so hierarchy rests on tiny caps labels (NAME, SYNOPSIS) and light grey body text. The gallery image is stale: it still shows a curl command piped straight into sh, pointing at coppicedb.dev, which BRIEF bans. The page itself was fixed at 01:49; re-render. | lost 2 to Better Stack |
| 04-skeuomorphism | 6 | polish | Clutter: eight channel strips with about ten knobs each, plus meters and faders, labelled at 9 to 10 px. A metallic header gradient, brushed strips and corner screws are decoration; nothing on the screen leads except -24.1. | lost 2 to Snowflake |
| 07-risograph | 6 | polish | The giant pink 61 and blue 38 overlap so they read as one number, 6138. Clutter: about eight text sizes on one page (running heads, lead, two body columns, chart labels, three stat numbers, captions, a method note). | lost 2 to Zipline |
| 12-pixel-art | 7 | polish | Clutter: pixel lantern stacks plus a step line in the chart, six KPI rows each with its own sparkline, and an offers table with icons and bar meters. The pixel display face for 'Lantern Festival' sits beside a clean sans, so the pixel theme looks pasted on. | won 2 vs SoundCloud |
| 09-bento-grid | 7 | polish | Clutter: five mini-interfaces in one section (an 8-row inbox with SLA chips and initials, a macros card with template variables, a bar chart, a shortcut list), so the eye has nowhere to rest. The saturated yellow SLA tile is the only coloured block and pulls focus from the headline. | won 2 vs Windsurf |

### App screens (average 5.6)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 01-private-banking | 3 | rebuild | The £4,862,310.54 total is set in a high-contrast Didone at about 64 pt beside SF-style 17 pt text, so the two faces fight; the wordmark repeats the Didone. Secondary text is sage grey on charcoal, and the chart is a bare polyline with a dotted baseline and no values. A gold pill and gold tab give the brown-and-gold luxury cliche; the last holding row runs under the tab bar. | lost 3 to Revolut |
| 10-clinical-vitals | 4 | rebuild | Every observation sits in a caramel or beige rounded box, so the table looks like conditional formatting in brown and cream. Slashed zeros in the times (00:00, 02:15) read as a code font in a clinical UI. Clutter: three bordered boxes stacked at the top (allergy, emergency response, observations header). | – |
| 09-project-workspace | 5 | rebuild | IDs like FLD-231, cycles, priority bars and a ⌘K footer copy Linear. The cycle Gantt is heavy slate bars with grey tails, so the top third is grey on grey; every card is boxed with one to three bordered tag chips. Orange-red marks the button, urgent items, due dates and the today line. | lost 3 to Linear |
| 06-plant-care | 5 | rebuild | Three type voices: a serif title, serif italic Latin names and a sans body; 18% is set in a light 64 pt. Clutter: a week strip with drop counts under the days, a meta line ('Most urgent first · 800 ml in all · sensors read at 08:10'), a card with a segmented moisture bar and legend, then two rows with their own pill buttons. | – |
| 03-recipe-editorial | 5 | rebuild | Terracotta button, brown woven mat and cream page: the brown, orange and cream mix the rules ban. The photo credit sits as a body line under the title; the segmented time bar and its legend are cryptic. Only three ingredients fit above a full-width pill. | – |
| 07-language-lesson | 6 | polish | Mascot, word tiles with thick bottom edges, hearts, a 'Perfetto!' sheet and +15 XP: Duolingo's structure tile for tile. Clutter: every element has the same heavy navy outline, plus a dotted background and confetti dashes. | lost 2 to Duolingo |
| 08-podcast-player | 6 | polish | The episode title is a serif at about 64 pt that dominates the screen. The pause button is a flat light-grey square beside round skip icons. Clutter: a transcript quote with a highlight, chapter progress, five controls and a chapter list with dotted leaders in one view. | – |
| 11-approvals-mobile | 6 | polish | Stock iOS grouped lists with no type or colour voice; the budget bar is a flat grey and black strip. An orphan 'Details' label is cut off just above the Decline and Approve bar; the header block sits tight (the owner asked for better spacing). | lost 2 to Copilot |
| 04-fitness-neon | 8 | keep | The neon glow on 172 and on the heart-rate line is the glow tell, though here it carries live data. | – |
| 05-travel-boarding | 8 | keep | 'Wed 22 Oct' is a Thursday in 2026 (check_dates.py flags it). | – |

### Watch screens (average 5.2)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 08-onething-focus | 4 | remove | A generic ring timer with a tick ring. 18:24 is the reused number making.md section 11 already calls out. | – |
| 03-tidemark-face | 5 | rebuild | A painted night sky and sea gradient with stars is texture standing in for a real asset. The dotted tide curve and '9:42 HIGH' sit on the busy sea. | – |
| 02-thrum-heart | 5 | rebuild | 162 is set in an ultra-heavy face jammed against the heart icon and BPM. A gradient zone bar and a gradient polyline at the bottom are decoration. | – |
| 04-headway-transit | 5 | rebuild | A default-looking condensed face at three number sizes, and a rotated 'MIN' label. Clutter: yellow route squares, a stop line with nodes and a rule on a 49 mm screen. | – |
| 05-nook-home | 5 | rebuild | The orange gradient on the 'Wind down' tile has a white glare that reads as a smudge. '1 lamp' and 'All on' sit almost on the tile bottoms in low-contrast grey; 'Wind down' runs edge to edge. | lost 3 to Jomo |
| 07-leeward-sail | 6 | polish | One monospace face for everything (clock, HDG · MAG, AWS KN) reads like a terminal mock-up. The compass dial is cut by the screen edges, with 210 and both arcs clipped. | lost 3 to Copilot |
| 01-ridgeline-trail | 6 | polish | Three faces: a wide heavy grotesk for labels, a slanted heavy face for 4'52" and a light face for +312 m. Clutter: a tilted lime 'KM 14.2' tag, hatched elevation fill, grey contour lines and a halo on the position dot. 4'52" is reused on the Rallo footer's phone. | lost 3 to Future |
| 09-oncall-incident | 6 | polish | One condensed face at nearly the same size for four lines, so 'Declines 31%' and 'Noor, Bastian on it' weigh the same. Two oversized pill buttons fill the lower half and press against the bottom edge. | lost 2 to Shopify |

### Mockups (average 3.8)

| Piece | Score | Action | Most visible problems | Blind test |
|---|---|---|---|---|
| 04-browser-cascade | 2 | remove | Kumo Kōbō (removed) and Plumpot (replaced) are two of the five windows. A numbered 01 to 05 list with leader lines is documentation framing. | – |
| 06-poster-street | 2 | remove | The board shows Howl Hill. The flat yellow board is not lit like the golden-hour photo. | – |
| 08-made-with-opendesigner | 3 | remove | Maison Auberval and Howl Hill (removed) and Quietfield (replaced) are in the grid. | – |
| 05-components-board | 3 | rebuild | Old Gloaming, Wayfern and Calamondin components, a cropped pricing card and an empty composer box. | – |
| 01-phone-trio | 3 | rebuild | Lullwater (replaced, with a glowing orb) and Halden Private (hated) fill two of the three phones. A 'Three dark interfaces' title over tilted phones in lilac mist: a presentation plate, not a scene. | – |
| 07-tablet-clinic | 5 | rebuild | The screen is the caramel-boxed vitals table. A cropped glass bowl prop. | – |
| 09-laptop-dashboard | 6 | polish | The Quoin screen's text is illegible at this size, so the mockup hides what makes it good. Generic desk props. | – |
| 10-multi-device | 6 | polish | A portfolio-style plate with a caption strip; the phone covers the laptop's sidebar so only three nav items show. A band of dead white above the laptop's Decline and Approve footer. | lost 3 to Toggl Track |

## Proposed gallery order
People see the strongest work first. B2B product screens lead because you love them. The other categories follow by their average score. Inside each category, the best pieces lead, weak pieces sit at the end, and the six marked remove come last until they are taken off. The same order is in `brand/showcase/order.json`. Re-run it after the current rebuilds land.

1. **B2B product screens:** 01-quoin-payments, 02-fennick-approvals, 03-corvane-record, 05-kilnworks-billing, 04-sounding-observability, 06-ferrule-security.
2. **Hero sections:** 08-y2k-retrofuture, 14-fennick-approvals, 11-spend-platform, 02-luminous-devtool, 01-swiss-architecture, 07-climate-observatory, 03-organic-wellness, 12-sounding-observability, 13-ferrule-security.
3. **Web components:** 02-command-palette, 08-music-player, 07-ai-composer, 09-onboarding-stepper, 03-date-range-picker, 06-data-table, 01-pricing-glass, 10-settings-terminal, 05-toast-stack, 04-upload-brutal.
4. **Footer sections:** 02-keystrata-mega, 01-brask-wordmark, 08-rallo-app, 09-b2b-platform, 05-salt-ledger-index, 07-sasame-tea, 04-tumbletree-meadow, 06-knurl-brutalist.
5. **Style studies:** 09-bento-grid, 12-pixel-art, 07-risograph, 04-skeuomorphism, 11-terminal, 01-glassmorphism, 10-mesh-gradient, 05-comic, 08-bauhaus, 06-memphis, 02-neumorphism, 03-claymorphism.
6. **App screens:** 05-travel-boarding, 04-fitness-neon, 11-approvals-mobile, 08-podcast-player, 07-language-lesson, 03-recipe-editorial, 06-plant-care, 09-project-workspace, 10-clinical-vitals, 01-private-banking.
7. **Watch screens:** 09-oncall-incident, 01-ridgeline-trail, 07-leeward-sail, 05-nook-home, 04-headway-transit, 02-thrum-heart, 03-tidemark-face, 08-onething-focus.
8. **Mockups:** 10-multi-device, 09-laptop-dashboard, 07-tablet-clinic, 01-phone-trio, 05-components-board, 08-made-with-opendesigner, 04-browser-cascade, 06-poster-street.

## References (Mobbin, links only)
- **Product and data tables:** [Stripe payments](https://mobbin.com/screens/f576b06e-b290-4864-a0be-2d753324fd1d), [Stripe customers](https://mobbin.com/screens/eade1912-e11c-4d70-9556-1527dbd9837c), [Linear board](https://mobbin.com/screens/fc208a44-dbf9-4f79-b9b0-db57f9840964).
- **Style studies:**
  - [DoorDash Merchant photo adjust](https://mobbin.com/screens/2afdeed5-654d-490d-b0f8-add960425f22)
  - [Snowflake performance explorer](https://mobbin.com/screens/a9762712-40bb-4500-8809-956a391aaef7)
  - [Zipline highlights](https://mobbin.com/sites/sections/baf31b25-1858-463c-bf15-611d9c669092)
  - [Windsurf bento](https://mobbin.com/sites/sections/578c6a44-919f-4628-8573-42ba22a389d7)
  - [Better Stack docs](https://mobbin.com/sites/sections/d367b862-f8ac-44e5-b6c7-140cae9f2c2e)
  - [SoundCloud insights](https://mobbin.com/screens/81f4a402-c167-4470-ab5d-23a892be6a5a)
  - [Equals article](https://mobbin.com/sites/sections/ffa049eb-0dc2-4a16-b18f-d67b128806d1)
- **Heroes:**
  - [Mouthwash Studio](https://mobbin.com/sites/sections/0e035b6e-f0ab-416e-9ade-af96d4542658)
  - [Better Stack](https://mobbin.com/sites/sections/56c3bc9d-a358-4878-ba6b-0989d6eef012)
  - [Linear](https://mobbin.com/sites/sections/91b1d7ce-42f5-45bb-a46d-d639dc04f9f4)
  - [Front](https://mobbin.com/sites/sections/ba4ff47e-3460-4256-b2fb-0e0948cd8eb9)
  - [incident.io](https://mobbin.com/sites/sections/1f8c9d4b-9f7f-4bfa-aed3-9a849b84831e)
  - [Coda](https://mobbin.com/sites/sections/b519327c-fbb5-43a2-9516-1755e4083b5f)
- **Components:**
  - [Slack channel](https://mobbin.com/screens/f36795d0-b1cc-4056-b5fd-f816d27ecc68)
  - [Airbnb host calendar](https://mobbin.com/screens/f2bec6af-0e59-484a-b100-10bee1d42527)
  - [Gumloop date picker](https://mobbin.com/screens/95548930-658d-49e0-bf4d-6436f9aaadf6)
  - [Recraft pricing](https://mobbin.com/screens/3119e576-b1b3-47c5-a168-9c60ebd41ec8)
  - [Snowflake wizard](https://mobbin.com/screens/77cdb670-9074-4efa-9d86-d85301606776)
  - [Gumloop new chat](https://mobbin.com/screens/a3f8b130-cfc5-4ddc-8fd9-b95a4a6927bf)
  - [hilos notification settings](https://mobbin.com/screens/1c8bda14-0c9e-4cbc-b6b3-ab20412a4c94)
  - [SoundCloud track](https://mobbin.com/screens/0877f312-5984-4563-87a5-c44cdd0d6746)
- **App screens:** [Revolut performance](https://mobbin.com/screens/fa3f6ffd-c4d0-416d-ae5d-cdcfa24fc91b), [Copilot transaction](https://mobbin.com/screens/452d5f68-b2df-4bdc-8785-d241c5e074e0), [Duolingo lesson](https://mobbin.com/screens/faf99c88-e9a5-44ef-8e7d-3335018c4781).
- **Watch (phone references, no watch screens on Mobbin):** [Future Pro run](https://mobbin.com/screens/bc19a069-c416-4f95-9955-a34b5d7dbd90), [Copilot cash flow](https://mobbin.com/screens/18ab4866-ea3d-4df7-9f41-f2b8e706300c), [Shopify alerts](https://mobbin.com/screens/b1bd4556-d2f2-4e50-91d4-eea279f21206), [Jomo rules](https://mobbin.com/screens/dd1cc854-dcec-4abe-ac7e-6571b745a712).
- **Footers:** [Notion](https://mobbin.com/sites/sections/58bd399e-ff14-4dac-9378-cb8b97b06977), [Legora](https://mobbin.com/sites/sections/74f66481-04ab-4abc-bf99-7878c607e1f6), [Railway](https://mobbin.com/sites/sections/59cdf49d-e039-4904-a90e-aebfb09a9771).
- **Mockups:** [Toggl Track](https://mobbin.com/sites/sections/60d20670-e53e-4426-a9ec-2a2c8ea852c3).

No Mobbin image is saved in the repo. The downloads used for the blind pairs were kept in a scratch folder and deleted.
