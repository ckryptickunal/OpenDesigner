# 05 Nightjar: an incident postmortem told as a comic

Gallery: Nightjar is a fictional incident platform; its engineering blog tells a postmortem in three comic panels drawn from the data.

**Direction.** Nightjar is a fictional on-call and incident-management platform. Its engineering blog publishes blameless postmortems; this one, INC-4471, is drawn as a seven-panel noir comic. The incident is a believable one: a gateway release (v4.18) renamed a config key, the 30-second ledger timeout was silently ignored, the HTTP client fell back to a 3-second default, the nightly settlement batch pushed ledger latency past 3 s, and two retry layers (app ×4, gateway ×4) turned one checkout call into 16. The rollback fixed nothing because 1.9 M queued retries kept hammering the ledger; opening the retry worker's breaker and draining the queue did. Audience: engineers and engineering managers who buy incident tooling. Feel words: **playful, bold, geeky**.

Render: 1440 wide, full height (1701 px), scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
Mobbin has no comic-strip pages at all (searched "comic strip with panels, speech balloons and halftone"). The comic grammar (panels, gutters, captions, balloons, SFX, Ben-Day dots) comes from print comics, designed from first principles. Mobbin gave the ink quality and the blog frame.

| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/d89d3841-aea4-4bc6-a310-075eb53e19db (Figma, Shortcut) | Editorial ink illustration: black outlines, flat spot colors, dot patterns used as tone, not decoration. Set the bar for ink weight and the dots-as-tint idea. |
| https://mobbin.com/sites/sections/08d5d4d3-7404-4c85-acb7-ab34b8b22fe3 (SIGMA, FAQ) | A solid black figure next to an outlined one: a silhouette can be the character. That is why Ilse is drawn from behind, rim-lit, with no face. |
| https://mobbin.com/sites/sections/b7000804-e14d-4dcf-958c-1c4320eaf4e7 (Mailchimp Engineering) | An engineering blog where the art carries the page and the chrome stays small. |
| https://mobbin.com/sites/sections/dc58e1c0-2cf6-4031-b9e4-cd8d852aabb1 (Notion blog article) | Article header structure: kicker, large title, byline sentence; the facts table on the right is the postmortem version of its side rail. |

## System (engine)
```
sketch --name Nightjar --brand "#E3201B" --audience regular --platforms web --feel playful,bold,geeky --theme system-light-dark --surfaces "engineering blog:read" --delegated all
pick Q-dir-01 neo-brutalist     (nearest preset to comic ink: thick borders; its offset shadow is cancelled by depth 0)
set raw.textFace "Shantell Sans"; raw.displayFace "=textFace"; raw.monoFace "JetBrains Mono"; raw.fontLicence all true
set raw.marketingSurfaces true  (a "read" surface caps type at 38 px; the title needed 67)
build  -> no errors, 0 warnings
```
- First try used `--feel playful,bold,technical`: "technical" maps to modern + serious, and the engine warned that playful and serious pull four dials in opposite directions. Re-sketched with "geeky" (modern + playful). The warning was right.
- `light-only` was refused by house standard STD-visual-details-24. I kept system-light-dark and render light.

| Dial | Value | How it expresses the comic |
|---|---|---|
| expression | 85 | The strip is the page; type ratio 1.333 gives the 67 px title and 90 px SFX steps |
| brandPresence | 40 | Red is an alarm in the story, not brand wallpaper |
| density | 60 | Panels packed with lettering and data like a printed page |
| energy | 70 | Hard cuts between panels |
| roundness | 8 | Square panels and frames (control radius 0) |
| depth | 0 | Printed ink: flat, borders only |
| colorfulness | 18 | Two inks: black and one red |
| warmth | 30 | Cool white paper, never cream |

**What the dials cannot express** (all hand-made in the page): halftone screens (dot step 5 to 7 px, 45° angle, radius by tone), ink line weights (4 px panel rule, 3 px outlines, 2 px details), speech balloons as one closed path with the tail, caption boxes, SFX lettering with a paper outline, the panel grid and gutters, and the two-ink rule (red only where something is broken). There is no "ink" token either: text-primary is #222428, comic ink is #000 (`--ds-color-black`).

## Fonts and type scale
Shantell Sans (SIL OFL, Arrow Type; hand-lettered, with Informal and Bounce axes) for all lettering, title, body and SFX. JetBrains Mono (SIL OFL) only for real data: terminal output, chart labels, timestamps, config names, the facts labels. Two fonts.

| Role | Size | Use |
|---|---|---|
| Display | 90 | "31%" SFX |
| Headline | 67 | Title, "BZZZT" |
| Title | 38 | "What we changed", "TAK!", "KA-CHUNK" |
| Body large | 21 | Standfirst, action items, retry counter |
| Body | 16 | Balloons, captions, nav, facts |
| Label | 12 | Mono labels in the art and the page |
All from the token scale (12, 16, 21, 38, 67, 90). Title weight 700, lettering 600 uppercase (comic convention), everything else 400.

## Outside the tokens, on purpose
- Panel sizes (560/400/320 and 288/520/232/224 by 460) and `--ink`, `--paper`, `--red` aliases (the aliases point at tokens).
- The art: every SVG coordinate, halftone, stroke width.
- Accessibility: every panel has a full text version (`figcaption`, visually hidden) and the SVG art is `aria-hidden`.

## Checks
- `engine.py validate`: no errors, 0 warnings.
- `preflight.py html`: 2 errors, both M9 false positives (Google Fonts via `<link>`); it read **no** font sizes (`font sizes in px: []`) because sizes are tokens and SVG attributes, so it could not check the scale (filed as a bug).
- `engine.py review`: 5 standard breaks (px spacing) fixed to tokens; 3 raw sizes left (layout widths).
- Contrast: ink on paper 20.6:1; white on red tag 4.68:1; red text (#af1310) on paper 7.1:1; red SFX on black 4.49:1 with a paper outline (large display, 3:1 applies).

## Self-audit (making.md section 5 and 11)
Compared at 1440 wide with the Figma Shortcut illustration, the Mailchimp engineering blog and the Notion article header.

- **Round 1 (first render), score 3.** Balloon tail covered the chart title in panel 2; panel 3's finger read as a remote control; the panel 5 balloon hid the retry counter; panel 7's balloon hid the mug; the blind light in panel 1 was ragged dot "caterpillars"; art text at 13 and 14 px broke the scale.
- **Round 2, score 3.5.** Crisp blind bands with a dotted falloff; hooded head redrawn with headphones (now reads as an engineer); finger removed; counter and balloon re-laid; a glow behind the breaker with no bulb replaced by action lines (section 11: a glow must have a job); background tint in panel 5 removed (decoration with no data); sizes snapped to 12/16/21.
- **Round 3, score 4.** Balloon tail moved off the deploy marker; title kept on two lines with a non-breaking hyphen; Return key redrawn pushed flush while the other keys stand proud; action items to regular weight (bold was everywhere in lettering already).
- **Tells still present:** uniform 3 px vector line (real comic ink varies thick to thin); one character, drawn without a face. It passes as a careful in-house engineering-blog comic, not as a hired illustrator's. **Final score: 4.**

## The style: comic
- **Plain words.** A story told in drawn boxes read in order, with words in speech balloons and caption boxes, printed in a few inks.
- **What defines it (checkable).** Panels with a ruled border and white gutters; reading order left to right, top to bottom; captions (rectangles, narration, time) and balloons (ovals with a tail to the speaker); lettering in uppercase hand-drawn type; sound effects drawn as big outlined words; tone made of halftone dots, not gradients; solid blacks; a small number of inks.
- **How it goes wrong.** Clip-art characters with dead faces; Comic-Sans-style lettering; Bangers on everything; a "POW!" burst for decoration; gradients instead of dots; balloons whose tails point nowhere; jokes instead of a real story; every panel the same shot.
- **How I kept it premium.** A real incident with real numbers and units in every panel; two inks with a rule (red only where something is broken, so panel 7 has none); varied shots (establishing, over-the-shoulder, close-up, diagram, action, callback); a character drawn as a silhouette instead of a weak face; the light from panel 1 returns inverted in panel 7; a text version of every panel; postmortem actions with owners and ship dates under the strip.

## Process findings
1. **No named-style answer.** Q-dir-01 offers six presets; comic is none of them. Neo-brutalist was nearest but brings an offset shadow I had to cancel (feedback: gap).
2. **Comic traits have no tokens:** ink, art line weights, halftone screen, balloon and caption styles, ink count (feedback: gap).
3. **Preflight cannot read token or SVG font sizes** and flags Google Fonts as missing (feedback: bug).
4. **Display weight 850 ignores the face's range** (Shantell stops at 800) (feedback: bug).
5. Helped: the macro-conflict warning caught "technical" fighting "playful"; `marketingSurfaces` unlocked display sizes; `review` caught px spacing.

## Polish round 2026-10-14
After the independent audit (score 4, two fact errors). A fresh-context reviewer re-audited it three times; final score **4**, with no fact errors left.

**What changed**
- **The drain fits the clock.** The ledger's retry queue (all callers, now said under the counter) is about 2.0 M at 02:36 and drains at 4,000 calls a second, so it is empty at 02:44, before "02:47. Resolved." It was 2,000 a second, which would have taken 16 minutes.
- **The charts agree.** Panels 1, 2 and 4 read 38% at 02:13, minute by minute. The rollback marker sits at 02:24; it was drawn at 02:20. After it the line falls only to 29%, and Kwame says "Errors 29%. Not fixed." instead of "haven't moved".
- **The story closes.** Panel 2 marks the 02:00 settlement batch, and the Cause row names it. Panel 4's caption says the queued retries kept the ledger down.
- **Reused data replaced.** The page time 02:14 became 02:13 and 31% became 29%; both were used by other showcase pieces.
- **The breaker panel is an object.** It has no hand, is labelled once ("Retry worker breaker", then "OPEN" by the lever), and shows the queue draining. KA-CHUNK and OPEN are no longer red, because red is only for what is broken.
- **Better drawing.**
  - The head has hair from the crown and a rim light, with real headphones.
  - The mug has an elliptical rim and a handle.
  - The keys have legends, and four arrows leave the app.
- **Text versions match the drawings.** Return was pressed at 02:19, and panel 7 has no lamp. Quotes are curly, and the body lettering is calmer (Informality 0).
- **It reflows.**
  - From 1,280 to 1,375 px, each row keeps its drawn proportions.
  - Below 1,280 px, one centred panel per line.
  - Below 720 px, the text versions show under the three widest panels.
- **Engine.** `pick Q-dir-01 comic` replaced the neo-brutalist preset; build passes with no errors.

**References used by the re-audit (Mobbin, by URL):** Mailchimp Engineering (https://mobbin.com/sites/sections/b7000804-e14d-4dcf-958c-1c4320eaf4e7), Dollar Shave Club (https://mobbin.com/sites/sections/ae5d023c-3b8e-4d49-8a0b-204608c24649), Ragged Edge (https://mobbin.com/sites/sections/951aaab5-9615-49f5-85b1-f753090e9c83).

**Left:** one 3 px vector line everywhere and simple props (the glass, mug and breaker). That is the gap to a 5.

## Round 4 (owner review, 2026-10-18)
**This section describes the page now.** Rebuilt after the round-4 audit scored it 5 of 10 (rebuild). Render: `shot.png`, 1440 x 900 at scale 2.

**One idea:** A postmortem's lead illustration is a three-panel strip: the page at 02:13, the rollback that fixed nothing, the breaker that did.

**Why:** The round-4 audit: three typefaces and dense halftone panels looked busy and amateur; every panel carried three or four text elements; at 3,402 px tall the gallery tile cropped it; it lost by 3 to Equals.

### What changed
- **One screen, 1440 x 900:** an engineering-blog article header (kicker, title, standfirst, byline, a four-row facts list) and one strip of three equal panels under it, the way Mailchimp, Linear and Dovetail put one lead illustration under a post title. The 3,402 px seven-panel page is gone.
- **Two faces:** Inter for the page (the engine's text face), Shantell Sans only for the lettering inside the strip (the engine's display face). JetBrains Mono is gone; both set through the engine.
- **Each panel holds one caption and one drawing, drawn from the data:** 02:13, the paged phone in ink outline with its SEV-2 notification (5xx at 38%); 02:24, the error rate with the rollback marked, falling only to 29%; 02:36, the retry queue from 02:13, 2.0 M at the breaker, empty at 02:44. Halftone only fills the area under a measured line, at a coarse 10 px pitch. Red only where something is broken.
- **Removed:** the speech balloons, SFX (BZZZT, TAK!, KA-CHUNK), the keyboard, glass, mug, headphones figure and breaker drawing, the terminal, the retry counter, the action-items row and the footer.
- After the fresh audits: five sizes and three weights; all panels white; no balloon and no tag; the phone as an outline, not the heaviest mass; the queue axis from 02:13 so the build-up is drawn; '2.0 M retries queued, from every ledger caller' (the queue is all callers, not only checkout, so it is not 16 x 33,712). **After the third audit (unscored):** the caption boxes lost their borders, the panels became equal widths and the lettering went from 700 to 600, after a blind judge called the unequal boxed panels home-made.

### Type scale
Page in Inter, lettering in Shantell Sans. 12 meta, axis labels; 16 body, chart notes; 21 standfirst, captions; 28 the big readings (38%, 29%, 5xx at 38%); 51 the title and the phone's clock. Weights: Inter 400 and 600, lettering 600.

### Blind pairwise test
Three shipped references (Mobbin, cited by link only; images were kept in scratch and deleted). Each pair at the same height, sides random, no labels; fresh judges saw several pairs at once (four sets: 15, 9, 6 and 6 pairs, a new judge each time) and were told to weigh craft, not content. The table gives the result for the final render.

| Reference | Result |
|---|---|
| Mailchimp Engineering, https://mobbin.com/sites/sections/b7000804-e14d-4dcf-958c-1c4320eaf4e7 | ours better by 2 |
| Linear blog, https://mobbin.com/sites/sections/5e1fc30a-f780-41cd-b546-f16b263ebf3b | ours worse by 1 (near tie) |
| Dovetail blog, https://mobbin.com/sites/sections/dc74d364-db70-40a1-ac64-1fb5e73133df | ours better by 2 |

**Pass rule:** never lose by 3 or more, and equal or better in at least 2 of 3. Passes. The judges' flaw for ours each time: the hand-lettered comic font reads as a novelty next to the article's type.

### Fresh-eyes audit
Round 1 was a fresh-context auditor given PRESENTATION.md, ROUND3-BRIEF.md, the owner's note, the B2B product screens (product/01, 02, 04, 06), Orbika, Holdfast and Lampwright as the bar, and the three references below. Rounds 2 and 3 went to the same auditor, so they check its own fixes rather than being fresh eyes. Scores: 3, 3, 4. Its round-3 note (remove the caption-box borders) was then done.

### Checks
- `check_dates.py --year 2026` passes (Tuesday 6 October 2026).
- `check_names.py`: 0 errors; new words (Blog, On-call, Postmortem, Postmortems, Runbooks) are UI words.
- `engine.py validate`: no errors, 0 warnings. Preflight: no type or font errors.
- Re-added from the page: 4,180 / 33,712 = 12.4%; 02:06 to 02:47 = 41 min; 2.0 M at 4,000 a second = 500 s, so 02:36 + 8 min 20 s = 02:44; each chart's time scale is even.

### Left
The comic lettering still reads as a novelty to blind judges; it is the style, and it is confined to the strip.
