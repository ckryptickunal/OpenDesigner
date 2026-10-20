# 03 · Claymorphism · Arrivant new-hire first week

Gallery: Arrivant is a fictional onboarding tool; a new hire's first week is six clay capsules, one bead per task.

Arrivant, a people-ops onboarding page: clay on one object, the new hire's badge with a clay portrait drawn in SVG (a real person's photo until Round 3), beside a flat first-week list in one green. Fresh audit after the polish round: 4 of 5.

The "Round 4 (owner review, 2026-10-18)" section, the last one, describes this page; the sections before it record earlier versions. The polish round of 2026-10-14 before it describes the version that round started from. The sections between record the first build, the Wayfold page that the independent audit scored 3.

Round 3 ended at 4 of 5; the round-4 audit then scored it 5 of 10 and it was rebuilt (last section).

## Direction
Wayfold is a fictional people-ops platform. The screen is the onboarding page a new hire sees six days before starting: Tomás Reyes, Product Designer, joining Northcote Labs on Monday 20 October (2025 calendar; wrong for 2026, fixed in the polish round). On the left is the one object that matters on day one, his badge, drawn in clay. On the right is the first-week checklist: done, next, and later. The audience is a new employee, nervous and keen. Mood: kind, clear, a little playful, never childish.
Feel words: **friendly, playful, calm**.

## References (Mobbin, cited by link only)
| Reference | What it taught |
|---|---|
| Remote self-enrollment, https://mobbin.com/screens/156170a2-7331-438f-9a0a-e7eba294b489 | The new-hire task list: one row per task with a short reason line, "tasks remaining" and a percentage. The base structure. |
| Vanta starter guide, https://mobbin.com/screens/d6c8a960-3253-4ca4-b4aa-06e902fa0e4e | Grouped tasks with "4 of 4 complete" on each group, and finished groups collapsed to one line. Became "Before day one: 5 of 5 done". |
| Tabby setup (iOS), https://mobbin.com/screens/c9bb4207-f92e-4dfe-9609-1dcba416b626 | Clay in a real flow: one 3D object at the top, then a linked checklist with puffy filled checks. The nearest shipped claymorphism. |
| Glow wallet (iOS), https://mobbin.com/screens/b92dfcad-1b54-46fd-ba7f-fb6ab7223b57 | One saturated soft 3D object on a pale ground, lit from the top left, with a soft cast shadow. The bar for the badge. |

Mobbin has clay illustrations in consumer onboarding but no B2B HR product in the style. The UI half of claymorphism (puffy controls) came from first principles.

## System (engine)
```
init; standard override STD-visual-details-24 --why "claymorphism shown in one light appearance"
sketch --name Wayfold --brand #6D4AFF --audience regular --platforms web --feel friendly,playful,calm --theme light-only --surfaces "new-hire portal:operate" --delegated all
pick Q-dir-01 tonal          (no clay option; tonal is the nearest: colour on surfaces, big radii)
set raw.secondaryColors ["#FFD43B"]; set raw.accentCount 2   (the second colour was ignored until accentCount was 2)
set raw.textFace "Bricolage Grotesque"; displayFace "=textFace"; monoFace "Bricolage Grotesque"; fontLicence (all true)
build
```

| Dial | Value | Why | Expresses the style? |
|---|---|---|---|
| roundness | 96 | Inflated shapes: full-radius controls, 20 to 28 px cards, circles | Yes |
| depth | 80 | Clay is volume | Only in name: the tokens are drop shadows, not inner light and shade |
| colorfulness | 55 | Two clay hues, violet and lemon, on lilac-white; never four pastels | Yes |
| density | 30 | One task at a time, roomy. This also raised the scale to 12/16/21/28/38 | Yes, indirectly |
| expression | 70 | A welcome flow; personality is the point | Yes |
| brandPresence | 55 | Violet carries progress, done and the primary action | Yes |
| energy | 50 | Friendly but not bouncy | No |
| warmth | 30 | The feel word friendly pushed warmth to 80 (beige). Kept cool so the violet stays clean | Yes, protects the colour rule |

**What the dials cannot express:**
- Clay's three layers: inner light top-left, inner shade bottom-right, soft cast shadow.
- Coloured clay whose highlight must stay subtle so white text keeps 4.5:1.
- The inset "dimple" of an empty checkbox.
- The 3D object itself.

**Fonts.** Bricolage Grotesque only (SIL OFL, Google Fonts), using its optical-size axis. 400 for the welcome headline, 500 for the date, 600 for the logo and checks.

**Type scale (5 sizes, all from the engine's scale).**

| Role | Size | Use |
|---|---|---|
| Display | 38 | "Welcome to Northcote, Tomás" |
| Headline | 28 | First-day date; the name on the badge |
| Title | 21 | Wordmark |
| Body | 16 | Tasks, lede, buttons |
| Caption | 12 | Task details, counts, badge line |

(The badge initials are 38 px, the display size.)

## The object
The badge on its lanyard is drawn in SVG:
- an SVG filter (offset + blur + composite "out") paints inner shade bottom-right and inner light top-left, clipped to each shape;
- a blurred ellipse is its shadow on the stage;
- gradients from the accent ramp shape the strap and the avatar disc;
- the clip uses the lemon accent.

All its colours point at `--ds-*` tokens through `style` attributes (round 3). It shows initials, not a photo, and only true data: name, role, company, floor. It is also the next task: "Collect your badge and laptop".

## Where I stepped outside the tokens, and why
- The clay shadow recipes (`--clay-white`, `--clay-color`, `--clay-lemon`, `--dimple`) are built from accent step 12 and white with `color-mix`.
- The stage panel's inset light.
- `review` counts 7 hard-coded values (radii and shadow lengths).

## Checks
- `engine.py validate`: no errors. Two warnings, both macro conflicts ("playful, minimal pull expression and colorfulness") that stay after both dials were set by hand.
- `preflight.py html`: 1 error, M9 for Bricolage Grotesque (false: Google Fonts link).
- `engine.py review`: no standard breaks.
- **Contrast as rendered.**
  - Round 2 found "Add to calendar" at 4.31:1, because the 45% white highlight on violet clay lightened its top-left.
  - Round 3 lowered the highlight to 28%, which gives 4.62:1.
  - Final: 50 runs, 0 failures. The badge initials are 3.81:1 at 38 px (large text, 3:1).
- **Facts:**
  - Today is Tue 14 Oct, so Mon 20 Oct is 6 days away (2025 calendar; wrong for 2026, fixed in the polish round).
  - 12 tasks = 5 + 4 + 3, and 6 are done (5 + lunch), which matches the 50% bar.
  - "Due Wednesday" and "Wed 14:00" are both 22 Oct.

## Self-audit
Each round compared the render with Remote, Vanta and Tabby at the same width.
1. **Round 1 (3.5).** The badge already held the page. But:
   - The checklist ran off the bottom of the screen.
   - The next task said its status three ways: a lemon border, a lemon-rimmed check and a "Next" tag (a section 11 tell).
   - The lede ran to two lines.
2. **Round 2 (4).**
   - The rest of the week became a row of three clay tiles. This keeps the page in one view and breaks the list rhythm.
   - The next task says it once: a "Next" tag, plus a higher lift.
   - Shorter lede.
3. **Round 3 (4).**
   - Fixed the white-on-violet contrast.
   - Moved every colour of the badge art onto tokens.
   - Spacing pass.

**Tells, final state:**
- One object with craft, and it carries data.
- Lemon has one meaning (next and soon): the "Next" tag, the countdown, and the badge clip, since the badge is the next task.
- No confetti or sparkles, and no clay icon on every row.

**Remaining weakness:** the white task cards read more "soft UI" than clay. Clay lives in the coloured parts (checks, button, tags, badge). A stronger version would give the next task a coloured clay body.

## The style
- **Plain words:** things look puffy and soft, as if made of modeling clay. They bulge, catch light on top and sit on a soft shadow.
- **What defines it (checkable):**
  1. Big radii (24 to 40 px) or full circles.
  2. Three shadow layers per shape: inner light top-left, inner shade bottom-right, soft outer cast shadow.
  3. Saturated but soft colour, with a slight gradient on each shape.
  4. Usually one or more 3D clay objects, not only puffy controls.
- **How it goes wrong:**
  - A clay icon on every row.
  - Four or more pastel hues.
  - White text on pastel clay.
  - Beige backgrounds from a warm palette.
  - Toy-like art with no link to the product.
  - The same bubbly radius on everything.
- **How I kept it premium:**
  - One object, drawn with care, that is also the next task.
  - Two clay hues, each with one job: violet for done and progress, lemon for next.
  - Dark ink text everywhere except on violet, measured at the worst pixel.
  - A real first-week plan with names, rooms and times.
  - Cool lilac-white ground instead of beige.

## Process findings
Each was recorded in `opendesigner/feedback.md`.
1. **(gap) No clay or skeuomorphic option in Q-dir-01;** tonal was the nearest. Clay needs a three-layer elevation token, a coloured-clay variant with a capped highlight (a 45% highlight dropped white text to 4.31:1), and an inset dimple.
2. **(confusing) `raw.secondaryColors` is silently ignored** until `raw.accentCount` is 2.
3. **(bug) The lemon accent2 ramp's tint steps 2 to 7 are cream and beige** (#f7f4eb, #f1ebd9, #ece3c6), not pale lemon. Only step 9 was usable.
4. **(bug) Macro-conflict warnings stay** after the conflicting dials are set by hand.
5. **(repeat) "friendly" pushed warmth to 80** (beige neutrals; neutral step 3 was #efebe8 before the fix).
6. **(conflict) `references/styles.md` (untracked, written this run by another session) gives clay warmth 60 to 80 and "start from pick Q-dir-01 soft".**
   - Warmth 80 gives #efebe8 neutrals, the cream the owner rejects.
   - The soft preset brings the neumorphic contrast lint and colorfulness 20.
   - Tonal plus warmth 30 worked better.
7. **What helped:**
   - Density 30 produced a 16 px body and a 12/16/21/28/38 scale with no hand-tuning.
   - The accent ramp's step 12 made a good clay shadow colour (violet-tinted, not grey).
   - The secondary-colour ramp gave a lemon with dark on-text (`text.on-accent2`), exactly right for lemon chips.

## Polish round 2026-10-14
**Fresh audit: 4 of 5.** Two fresh-context reviews both scored it 4. The independent audit had given the first build 3. Render: `shot.png`, 1440 x 900 at scale 2.

### What the audit asked for
- Violet on lilac with a lemon second accent, a known default palette.
- Initials on the badge where a real badge has a photo.
- White task rows that were soft UI, not clay.
- Stock chips ("Next", "6 days to go").
- Weekdays from the 2025 calendar: it put Monday on 20 October, which is a Tuesday in 2026.
- Tomás and Calder were reused.

### What changed
- **The palette.** One deep green (`#0E7C5A` and its accent ramp) does done, progress and the single action. It sits on cool greys (page neutral 2 `#f2f4f9`, ink `#222428`). There is no violet, lemon or cream.
- **Clay on the one object that carries the story:** the badge on its lanyard, which is also the next task.
  - The card uses the engine's clay elevation (cast shadow, inner shade, inner light), with a deeper inner light and shade so it bulges.
  - The green band at the bottom is puffy.
  - The strap is woven with the company name. White on green measures at least 5.18:1 along the strap.
  - A steel crimp, connector and clip hold the badge.
- **A real portrait.** The photo is by Andre Styles on Unsplash (photo-1609436132311, "Woman in gray and black scarf", Unsplash Licence, source page https://unsplash.com/photos/woman-in-gray-and-black-scarf-pq9npYMirk8). It is credited and linked on the page. The badge shows only true data: photo, name, role and access ("Staff · Floors 3 and 4").
- **The checklist is flat.**
  - Hairline rows and flat checks.
  - One button, on the next task.
  - No "Next" chip and no countdown pill: "in 5 days" is plain text.
- **Dates.** Today is Wed 14 Oct 2026. The first day is Monday 19 October. The week continues Wed 21, Thu 22 and Fri 23 Oct; earlier dates are Fri 9 and Mon 12 Oct.
- **Names.**
  - Tomás Reyes is now Imani Clarke, and Ama Owusu is now Tove Nyström.
  - 41 Calder Street is now 41 Ropewalk Lane. Rye & Fennel is dropped.
  - Wayfold read close to Wayfern (`components/03`). It became Joinery, which the first fresh audit found is a real AI hiring product (teamjoinery). The name is now **Arrivant**, which returned no HR or onboarding product.
  - "Elin" was dropped because it is one letter from Elif, a name in another piece.
- **Fixes after the first fresh audit (4):**
  - Stronger clay.
  - Before day one now says "laptop choice", since the laptop itself is collected on day one.
  - The security course moved to the rest of week one. The counts are now 5 + 3 + 4 = 12, with 6 done.
- **Fixes after the second fresh audit (4):**
  - The summary row says "5 tasks".
  - The credit moved into the text block and links to its source page.

### System (engine)
```
set raw.brandColor "#0E7C5A"; set raw.flags.brandExact true; set raw.accentCount 1; set raw.secondaryColors []
pick Q-dir-01 claymorphism        (soft preset, style claymorphism, clay elevation model)
set name "Arrivant"; build
```
The dials were already the claymorphism ones: roundness 96, depth 80, colorfulness 55, warmth 30.

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Gusto, https://mobbin.com/screens/030224c2-2326-4e00-938c-d6d90b7a087d | The "Before Day 1" and "On Day 1" grouping in flat rows. |
| Workable, https://mobbin.com/screens/32528886-f7f1-4e0c-96ad-ccf5e05bd78f | A start date, a progress bar, and dated Done and To do rows. |
| Slack onboarding template, https://mobbin.com/screens/1dbdaef3-604a-4b37-9266-0632cbeb3adb | First-week tasks, meetings and a buddy on one employee-facing page. |

### Checks
- **Contrast as rendered:** 53 runs, 0 below the floor.
  - The lowest is 4.94:1, "Your first day, in 5 days" in green on the stage grey.
  - White on the green button is 5.19:1, and on the band 5.21:1.
  - The woven strap is 5.18:1. For text set along a path, the check samples small boxes along the path and skips the part hidden under the crimp.
- **Weekdays.** `check_dates.py --year 2026`: every weekday matches. 14 to 19 October is 5 days.
- **Tools.**
  - `validate`: no errors and no warnings.
  - `review`: 20 hard-coded values, mostly badge radii and the stronger clay shadows.
  - Preflight: no errors.

### Remaining weaknesses
- The badge reads as soft 3D plastic more than modelling clay.
- The stage gives about 40% of the width to one object. That is the point of the piece, but a shipped onboarding page would give the list more room.

## Round 3 (polish) 2026-10-15
**Fresh audit: 4 of 5** against the B2B product screens (`product/01`, `02`, `04`, `06`). Render: `shot.png`, 1440 x 900 at scale 2.

### Why this round
The piece still carried "Being rebuilt" on the public showcase, against the bar of the B2B product screens. One rule was also broken: the badge showed an Unsplash photograph of a real person, captioned as the invented Imani Clarke. The showcase brief allows Unsplash photos but not "photographs of fake people", and not real faces standing in for invented people.

### What changed
- **A clay portrait drawn in SVG replaces the photograph,** on the badge and in the header avatar. Head, hair, ears, neck and jumper are each a shape shaded like the engine's clay elevation (an inner shade bottom-right, an inner light top-left), written as an SVG filter because a CSS box-shadow cannot reach inside SVG shapes, over a soft fill gradient. Features are kept plain: brows, eyes with one highlight, a soft nose shadow, a closed smile. Claymorphism is defined by its 3D clay figures (`styles.md`, section 3, point 4), so the badge now teaches the style twice: the clay card and the clay figure on it.
- **The photo credit line is gone,** with the photograph. No image on the page now comes from outside the file.
- **After the first fresh audit (3):**
  - **The portrait, redrawn.** The first SVG figure read as a default avatar. Now: eye whites, irises, pupils, a highlight and upper lids; filled brows; a raised nose tip that catches the light, with soft nostrils and a shadow under it; a jaw and chin; the left ear showing, with the hair tucked behind it; a side-swept fringe with its shadow on the forehead; a lock over the right shoulder; a shirt collar under the jumper's V.
  - **Edges.** The stage and the last task row both end at y 868 (they were 30 px apart); the space went into the list's group gaps, on the 4 px grid.
  - **Rows on a 60 px rhythm** (they were 59).
  - **Times at body size in ink,** in their own column. The next task keeps "09:30" in that column; its button says "Add to calendar".
  - **The lanyard shows the name whole:** one "NORTHCOTE LABS" per strap, placed by measuring the path between the frame's top and the crimp.
  - **No repeated directions:** the address line says the badge and laptop wait at reception; the task says "At reception · Tove meets you"; coffee is "Kitchen · 30 min".
  - **"In 4 days":** today is Thu 15 Oct 2026, and Monday 19 October is 4 days away (the page said 5, true on the 14th).
- **After the second fresh audit (4, "only just"):**
  - **Green has one job,** done and progress (the employer's lanyard and badge band stay green: they are the badge). "Add day one to calendar" is ink, and the first-day line is ink-2.
  - **The panel and the list no longer repeat each other:** the panel gives the date, the address and the way in ("Side door, open from 08:30"); the time stays in the list.
  - **The welcome lunch is a day-one event,** not yet done: "Welcome lunch with the design team, 12:30 · Vegetarian, picked Fri 9 Oct". Totals: before day one 5 of 5, day one 0 of 3, the rest 0 of 4, so 5 of 12 and a bar at 41.7%.
  - **One calendar action for the whole day:** "Add day one to calendar".
  - **The portrait:** smaller irises (no stare), a part line, and two shaded strands following the fringe's sweep, plus a sheen on the shoulder lock.
- **After the final fresh audit (4):**
  - The render was stale (it still showed the old side-door line); it is re-rendered from the current page.
  - The eyes no longer stare: the whites sit under lowered lids, and the brows are 1.5 px lower.
  - The clay reads: the badge face is a pale mint gradient with a deeper shade bottom-right (claymorphism's pastel, `styles.md` point 3).
  - The day-level action sits with the day: "Add day one to your calendar" is a link under the address; the first task keeps only its time. The group header is "Day one", since the date is in the panel.

- **After a last regression check (holds at 4):** the lids are raised halfway again (at 32 px in the header avatar, the lowered lids read as drowsy).

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| GoDaddy, https://mobbin.com/screens/66d1dcdf-73d4-4364-9549-1629c474c326 | A shipped 3D clay person: lids, nose, hair with volume. |
| Pipedrive, https://mobbin.com/screens/e7f636d0-1d6f-4a07-a5fa-9baaffea7734 | Quiet task rows with the accent only on done. |
| Revolut Business, https://mobbin.com/screens/480acc51-97cd-45f9-b0dc-8feb37488e77 | One soft 3D object beside a flat list. |

### Checks
- **Contrast as rendered:** 52 runs, 0 below the floor; lowest 5.21:1 ("Staff · Floors 3 and 4" on the green band).
- **Weekdays:** `check_dates.py --year 2026` passes (Fri 9, Mon 12, Mon 19, Wed 21, Thu 22, Fri 23 Oct 2026); Thu 15 to Mon 19 October is 4 days.
- **Facts re-added:** 5 + 3 + 4 = 12 tasks; 5 + 0 + 0 = 5 done; the bar fills 41.7%. The panel and the last task row end within 1 px of each other.
- Preflight: no type or font errors.

## Round 4 (owner review, 2026-10-18)
**This section describes the page now.** Rebuilt after the round-4 audit scored it 5 of 10 (rebuild). Render: `shot.png`, 1440 x 900 at scale 2.

**One idea:** Imani's first week is six clay capsules, one per day and as long as its tasks, with five beads already green before day one.

**Why:** The round-4 audit: a clean checklist, but the clay avatar and the lanyard badge looked like stock AI renders.

### What changed
- **No person, no badge, no lanyard.** The clay object is the week: one raised clay capsule per day (before day one, then Mon 19 to Fri 23 Oct), as long as that day's tasks, with one bead per task, green with a check when done. The next task's bead has a green ring. The header avatar is initials.
- **The decoration carries data:** 5 + 3 + 1 + 1 + 1 + 1 = 12 beads, the same 12 tasks as the list; 5 are green, matching '5 of 12 done'. 'Security and privacy basics' moved to Tue 20 Oct so every day has a task, and the list is in date order.
- **Calm type:** Nunito, set through the engine (Bricolage Grotesque stays only in `styles/06`), two weights (400 and 600), the large titles regular.
- **One surface:** the mint panel is gone; the capsules sit on the page under 'Your first week', and the first-day block is bottom-aligned with the last rule of the list.
- After the fresh audits: the beads matte (soft shading, no gloss), 'One bead per task' and '12 tasks' deleted, the tubes sized to their counts. **After the third audit (unscored):** the white plate, two-thirds empty, was removed and the capsules turned into one row per day, so the object fills the column; this version was checked by the blind pairwise test only. Last, the capsules went one step deeper in mint (accent 4 to 6) so the white beads read at 337 px.

### Type scale
Nunito only. 12 captions, 16 body and task titles, 21 group and section titles, 28 'Monday 19 October', 38 the welcome headline.

### Blind pairwise test
Three shipped references (Mobbin, cited by link only; images were kept in scratch and deleted). Each pair at the same height, sides random, no labels; fresh judges saw several pairs at once (four sets: 15, 9, 6 and 6 pairs, a new judge each time) and were told to weigh craft, not content. The table gives the result for the final render.

| Reference | Result |
|---|---|
| Aboard, https://mobbin.com/screens/4f90f332-e4d8-4201-b341-da664b1fdfe8 | ours better by 3 |
| Remote, https://mobbin.com/screens/156170a2-7331-438f-9a0a-e7eba294b489 | ours better by 3 |
| Deputy, https://mobbin.com/screens/555bcc50-9f56-4a55-a8cd-272c3f6f6dd6 | ours better by 4 |

**Pass rule:** never lose by 3 or more, and equal or better in at least 2 of 3. Passes. Every judge named the same flaw for ours: the soft, puffy 3D week tracker looks dated or gimmicky.

### Fresh-eyes audit
Round 1 was a fresh-context auditor given PRESENTATION.md, ROUND3-BRIEF.md, the owner's note, the B2B product screens (product/01, 02, 04, 06), Orbika, Holdfast and Lampwright as the bar, and the three references below. Rounds 2 and 3 went to the same auditor, so they check its own fixes rather than being fresh eyes. Scores: 3, 3, 3 ('close to 4' in round 3). It did not reach 4 in three rounds. Its round-3 notes (the empty plate, the empty bottom left) were then fixed, but that version has not been audited.

### Checks
- `check_dates.py --year 2026` passes (Fri 9, Mon 12, Mon 19, Tue 20, Wed 21, Thu 22, Fri 23 Oct 2026).
- `check_names.py`: 2 flags, both false positives: 'Fischer' (Lena Fischer) is two letters from 'Fishers', a common word in a `components/07` thread title; 'Northcote' is two letters from 'Northgate', which `watch/04` has already replaced with Saltgrove (only the old `mockups/03` render still shows it). New words (Good, Onboarding, People) are UI words.
- `engine.py validate`: no errors, 0 warnings. Preflight: no type or font errors.
- Re-added from the page: 5 + 3 + 1 + 1 + 1 + 1 = 12 beads; 5 + 3 + 4 = 12 tasks in the list; 5 of 12 = 41.7%, the bar's fill. Thu 15 Oct to Mon 19 Oct is 4 days.

### Left
Fresh audit 3, not 4. The judges call the puffy clay capsules dated; the empty space right of the short capsules is the data, not a hole.
