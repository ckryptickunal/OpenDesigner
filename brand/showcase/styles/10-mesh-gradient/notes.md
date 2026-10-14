# 10 · Mesh gradient · Prill

**Final self-audit score: 4 / 5** (4 rounds). Render: `shot.png`, 1440 x 900 at scale 2.

## Direction
Prill is a fictional AI evaluation platform: before a team ships a new prompt, model or retrieval change, Prill runs it against thousands of the team's real cases and shows, case by case, what improved and what broke. The hero shows one run: v14 of a support agent against v13 in production, blocked from release because two checks fell below threshold. Feel words: **technical, premium, calm**.

## The style
- **In plain words:** a mesh gradient is a soft field of colour where several colours melt into each other in two directions at once, like light on fabric, instead of a straight band from one colour to another.
- **What defines it (checkable):**
  1. Two or more colour centres blending over an area, with no visible bands or seams.
  2. A ground colour the field sits on (here deep ultramarine #1b1370), so the colours have something to glow against.
  3. Fine grain over the field, which keeps it from looking like a flat screen fill.
  4. The field is contained in a shape with a hard edge (here a plate with a 24 px corner, bleeding off the right and bottom), not washed behind the whole page.
  5. Anything that must be read sits on solid ground, not on the gradient.
- **How it goes wrong:** the aurora blob behind a hero with no job; dark ground with neon glow (the "dark + neon" family); four or more pastel hues; text and buttons placed on the brightest part; gradients on every card; banding from 8-bit steps.
- **How I made this one deliberate, owned and premium:**
  - **It is the data.** The field is drawn on a canvas from the run itself: one point per case, placed by score (across) and p95 latency (down), cyan for v13 and violet for v14, smoothed into density. The faster, better v14 rises as the violet and lilac glow at the top; v13 settles as the cyan below the card.
  - **It is labelled like a figure:** a legend ("Run #2,481 · 4,012 cases · across: score · down: latency"), score ticks on a solid strip along the bottom, and the only cases drawn one by one: the **37 regressions**, a tight cluster of white dots at low scores, with a leader to their label. The same 37 appear in the table's footer.
  - **It is owned:** two brand hues only (the brand violet and a cyan), and the same field idea becomes the logo mark (a small plate of the two colours). Every run in the product would have its own field.
  - **It is contained and quiet where it matters:** one plate on a white page, the product card flat and whole in front, all text either on the white card, on the white page or on the solid ground strip.

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| Runway, FP&A hero: https://mobbin.com/sites/sections/a3d53a6f-f985-48b8-9f8b-92d9ac3979b4 | The product flat, whole and at a readable size in front of a soft colour field |
| OFF+BRAND, gradient panel: https://mobbin.com/sites/sections/5bc9ede6-eb6d-41c3-95f5-509e61755ef2 | Contain the gradient in a hard-edged panel instead of washing the page |
| Fuser, grain gradient: https://mobbin.com/sites/sections/811a66b9-aeb0-482a-a4ff-eeedd3ac2ca5 | Grain is what makes a gradient look printed and premium rather than a screen fill |
| Adaline, eval results: https://mobbin.com/screens/f553932d-1520-42fc-952e-af797e7b798f | Eval UI anatomy: pass rate, evaluator groups, passed or failed per case |
| Braintrust, experiments: https://mobbin.com/screens/bb7a5740-36c6-4740-babf-05f053e5d8d2 | Comparison runs, failing rows called out, a diff toggle |

## System (engine)
```
sketch --name Prill --brand #6A4BFF --audience regular --platforms web --feel technical,premium,calm --theme system-light-dark --surfaces "landing page:persuade,app:operate" --delegated all
set raw.brandColor "#6A4BFF" --set-by chosen
set raw.textFace "Funnel Sans"; set raw.displayFace "Funnel Display"; set raw.fontLicence {...}
```
The violet survived the sketch this time (white text passes on it), so no swap.

| Dial | Value | Why, and what it expresses of the style |
|---|---|---|
| expression | 70 | **Mesh:** the gradient hero is the page's expressive moment |
| brandPresence | 75 | **Mesh:** the field carries the brand; the UI stays neutral |
| colorfulness | 55 | **Mesh:** two hues plus ink and white, not a rainbow |
| depth | 25 | One soft shadow (`elevation-overlay`) lifts the card off the field |
| roundness | 40 | Plate 24, card 12, controls 6 |
| density | 50 | The eval table at real density, roomy copy |
| energy | 30 | Calm and exact; nothing moves |
| warmth | 35 | Cool neutrals; the page white stays white |

**What the dials cannot express:** the gradient itself. Its ground (#1b1370), the two field colours, the lilac peak, the blur, the grain and the rule that text never sits on it all live in `index.html`. The engine has no token group for a brand gradient and `validate` cannot check text placed on one (I measured that by hand, below).

## Type
Two faces from one family: **Funnel Display** (headline, light 300) and **Funnel Sans** (everything else), both SIL OFL, Google Fonts. No highlighted phrase in the headline; the weight of the page sits in the plate and the red "Release blocked".

| Role | Size (token) | Use |
|---|---|---|
| Display | 67 (`font-size-67`) | Headline |
| Body large / title | 21 (`font-size-21`) | Lede, card title, wordmark |
| Body | 16 (`font-size-16`) | Nav, table values, buttons, facts |
| Label | 12 (`font-size-12`) | Column heads, meta, legend, ticks |

The sketch's scale has nothing between 12 and 16, so table values are 16 and meta is 12 (recorded as a gap).

## Outside the tokens, on purpose
- The field: ground #1b1370, cyan #35c9e6 (baseline), violet field and lilac peaks, generated in canvas from seeded data so every render is identical.
- White text at 82% on the plate ground; the legend dot for v14 is a lighter violet (#9b86ff) so it reads on the ground.
- 19 on-ladder spacings converted to tokens (render pixel-identical); `review` still lists 26 raw values, 11 of them the field and plate colours above.

## Checks
- `engine.py validate`: no errors, no warnings.
- `preflight.py html`: 2 errors, both M9 for the Google Fonts faces, false positives (the browser loaded Funnel Display 300/500 and Funnel Sans 400/500/600). One warning fixed (display tracking -0.035 to -0.03em).
- **Contrast on the gradient, measured from the render:** the first score ticks sat on the cyan and failed (1.75 to 2.32:1); they now sit on a solid strip in the ground colour (white on #1b1370: 15.3:1). The "37 regressions" label also failed in places on the field (1.8:1 at worst) and moved into the strip. The legend sits on the darkest part of the field (9.9:1 at worst).
- Card text: ink 15.5:1, secondary 7.2:1, tertiary 5.9:1, danger 7.2:1, success 7.3:1.
- Targets: CTA 48 px, "Review 37 cases" 36 px, nav links 32 px.

## Rounds and self-audit
Compared at 768 px width with Runway, OFF+BRAND and Adaline (scratchpad sheet, deleted). Scores for the early rounds were given afterwards from what each render showed.
1. **Round 1 (about 3):** card right, but the field was a teal glow on near-black navy with a blown-out white peak and an invisible axis label: the dark-aurora tell exactly.
2. **Round 2 (3.5):** new colour map (ultramarine ground, violet above, cyan below), axis named in the legend; the regression cluster was hidden behind the card.
3. **Round 3 (4):** cluster moved into view and drawn as 37 white dots; score ticks added.
4. **Round 4 (4):** contrast fixes (solid axis strip, label moved into it), lede shortened.

**Tells from section 11 still present:** a violet-to-cyan field is still in the family people associate with AI products, even with a job. No pill badge, one action, no logo row, the product is flat and whole.
**Why not 5:** the colour pair is not yet surprising enough to be unmistakably this brand; a stranger palette (for example a flame-test pair from assaying) could get there.

## Process findings
1. **No brand-gradient tokens**, and no contrast check for text on a gradient: both had to be done by hand. Recorded (gap).
2. **Scale gap between 12 and 16** for dense tables on a persuade-plus-operate surface. Recorded (gap).
3. **"A gradient must carry content" needs a recipe**: draw it from the product's own data, label it like a figure, keep text on solid ground. Recorded (idea).
4. Helped: the elevation-overlay shadow and the 12 px card radius looked right with no edits; the sketch kept the violet because white text passes on it.

## Polish round 2026-10-14
After the independent audit (score 3). **Renamed Assay to Prill.** Assay is already an open-source LLM-evaluation library. A prill is the bead of metal a fire assay leaves, and a web search found no AI-evaluation product by that name. Name mentions above are updated; the rest of the text above describes the version before this round. A fresh-context reviewer re-audited it twice; final score **5** (the first pass gave 4).

**What changed**
- **Palette off blue-violet.** A white page, a graphite field and one warm signal: molten orange #F0570A with an amber core, used only for cases that got worse. In the engine: brandColor #F0570A; secondaryColors graphite #3A414B and amber #FFB547; accentCount 3; `pick Q-dir-01 mesh-gradient`, which builds gradient.brand and gradient.mesh.1 to .3; colorfulness 40; depth 10.
- **The gradient is a readable chart inside the product.**
  - It places every case by its v13 and v14 answer-correctness score, on axes from 0.2 to 1.0.
  - It has a line of equal scores, labelled regions and a key ("darker grey: more cases").
  - The 117 cases that now break the refund policy are the orange cloud, and they are the only dots.
  - The plotted cases average exactly the table's 0.861 and 0.893. The script solves for this and writes the means to `data-means`.
- **Layout.** No card floats on a gradient plate. The headline and lede sit above the run, which is shown flat and whole in the grid. The facts row is gone; there is one action.
- **Facts.**
  - "1 of 6 checks below threshold": escalation now passes at 0.871.
  - 117 cases newly fail and 8 newly pass, so passes go from 3,924 to 3,815 (0.978 to 0.951).
  - v14 is "new refund prompt, smaller model", which explains the cost and latency drops.
  - The run time is 14:37; 09:41 and 10:52 are used in other pieces.
- **Mark.** A flat orange bead with one amber highlight, with no gradient.

**References used by the re-audit:** Intercom Fin (https://mobbin.com/sites/sections/7b51d1f3-dcb3-4803-a67a-b10557822ba1), Dovetail (https://mobbin.com/sites/sections/57c3f21b-b420-47cc-be74-8b45ab45aea5), Equals (https://mobbin.com/sites/sections/85da8987-9cb3-438d-9fb5-2ca3efd9ab1b).

**Left:** the field reads as a density chart first and a mesh gradient second, so a gallery visitor looking for the style sees only a little of it.
