# Zoom levels

People never pick a mode. Everyone starts with a quick sketch of the whole system. Then they zoom into only the parts they care about. They can stop at any level with something that works (BRIEF requirement 14). Each level's questions are in `pacing.json` → `areas[].levels`. Each question's level is in `questions.json` → `zoom`, and in its stage file.

| Level | Name | What the person gets | Rough size |
|---|---|---|---|
| 0 | sketch | A complete but coarse system: every token exists, every DESIGN.md section is filled from defaults | 5 questions, about 3 minutes |
| 1 | broad | One short screen for each foundation: style, density, color use, text, corners, depth, motion, and where the files live | 8 questions, about 8 minutes |
| 2 | defined | One area at a time (for example Color: ramps, roles, contrast) | 1 to 15 questions per area |
| 3 | detailed | Blocks, components and patterns, and the fine print of each area (`stages/*.detailed.md`) | the rest |

## Level 0: sketch (5 questions, one per message)
1. **What are you making?** Take a free answer and record it: `engine.py set context.product '"<their words>"'`. If they name surfaces (an app and a landing page), confirm Q-scope-01 in one line.
2. **Who is it for?** This is Q-aud-01. Ask whether people use it all day (`dense`), regularly (`regular`), or now and then on the go (`large`).
3. **Where does it run?** This is Q-plat-01. The choices are web, iPhone (`ios`), Android and desktop. Web alone is fine.
4. **How should it feel?** Ask them to pick 2 or 3 words from these pairs:
   - playful or serious
   - friendly or authoritative
   - minimal or rich
   - premium or everyday
   - modern or heritage
   - bold or quiet

   The words fill in the personality sliders (Q-brand-01), so don't ask for the sliders.
5. **Do you have a brand color or a logo?** This is Q-color-01, asked together with Q-brand-03.
   - A hex color becomes the seed (`--brand`). The engine keeps its hue and sets strength and lightness for contrast. If the exact hex must appear on buttons, also run `engine.py set Q-color-01 keep-hex`.
   - A logo file becomes the source of candidate colors.
   - With neither, suggest 3 seed colors that fit their words, and label them as a starting point.

Then run one command. It records the answers and builds everything.
```
engine.py sketch --name "<product>" --audience regular --platforms web,ios --feel friendly,minimal [--brand "#167874"]
```
Show the result on the best visual surface the host has (SKILL.md, visual ladder): a preview, the palette and the type scale. Name one or two defaults they might want to change. Then make the offer (below).

## Level 1: broad (one screen per foundation)
Go in this order, with the listed templates:
- Q-dir-01, style (`option-gallery`)
- Q-dir-02, how much fits on a screen (`spacing-ruler`)
- Q-color-02, where the brand color shows (`palette`)
- Q-type-01, which font (`type-scale`)
- Q-shape-01, corners (`radius`)
- Q-depth-01, how cards separate (`elevation`)
- Q-motion-01, motion feel (`motion`)
- Q-tool-01, where the master copy lives (text)

Each screen is one message with one question. The person can say "skip", and the default stays. After the last screen, run `engine.py build`. The engine marks each area it touched as `broad` by itself.

## Levels 2 and 3: one area at a time
There are 14 areas: overview, accessibility, platforms, modes, color, typography, layout, shape, elevation, motion, iconography, content, components and delivery. Their plain names are in `pacing.json`. The ids match the engine's, except `delivery`: the engine does not track its zoom level.
1. Open the area's stage files. Ask its level-2 questions in stage order. Then run `engine.py generate` and show the change.
2. Record the level: `engine.py set zoom.color '"defined"'` (level names: `sketch`, `broad`, `defined`, `detailed`). The engine also infers the level from the decisions made in an area.
3. Level 3 uses `NN-*.detailed.md` in the same way.
4. Components live at level 3. Build them from tokens, not from scratch.

## The offer after every level
Keep it short:
> Your first version is ready. It is a **sketch**: every part works, and most choices are still defaults.
> Stop here, or zoom into one area:
> **Color** (shades and contrast, about 5 min) · **Text** (sizes and fonts, about 4 min) · **Everything, broadly** (8 quick screens)

- Offer at most 3 choices, each with its rough minutes from `pacing.json`. Pick what matters most for this product. First come areas whose choices change the most (`pacing.json` → `top_decisions`). Then come areas their answers made risky, such as a light brand color or a dense product.
- Accessibility is never an option to skip. Its floors (`guardrails.md` section 4) are already set at level 0.
- "Stop" is a good answer. Finish with the Finish steps in SKILL.md, at whatever level they reached.
- DESIGN.md shows each section's zoom level. A teammate can see what was decided and what is still a default (SKILL.md, "DESIGN.md stays alive"). When someone asks what a section means, point to its zoom line and offer to zoom in.
