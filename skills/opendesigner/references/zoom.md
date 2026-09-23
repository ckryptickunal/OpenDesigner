# Zoom levels

People never pick a mode. Everyone starts with a quick sketch of the whole system. Then they zoom into only the parts they care about, and they can stop at any level with something that works. This follows BRIEF requirement 14. The question lists are in `pacing.json` → `areas[].levels`. Each question's level is in `questions.json` → `zoom` and in its stage file.

| Level | Name | What the person gets | Rough size |
|---|---|---|---|
| 0 | sketch | A complete but coarse system: every token exists, every DESIGN.md section is filled from defaults | 5 questions, about 3 minutes |
| 1 | broad | One short screen for each foundation: style, density, color use, text, corners, depth, motion, and where the files live | 8 questions, about 8 minutes |
| 2 | defined | One area at a time (for example Color: ramps, roles, contrast) | 1 to 15 questions per area |
| 3 | detailed | Blocks, components and patterns, and the fine print of each area (`stages/*.detailed.md`) | the rest |

## Level 0: sketch (5 questions, one per message)
1. **What are you making?** Take a free answer, then record it: `engine.py set context.product '"<their words>"'`. If they name surfaces (an app and a landing page), confirm Q-scope-01 in one line.
2. **Who is it for?** This is Q-aud-01. Ask: people who use it all day, regularly, or now and then on the go.
3. **Where does it run?** This is Q-plat-01. The choices are web, iPhone, Android and desktop. Web alone is fine.
4. **How should it feel?** Offer 2 or 3 words from this list: playful or serious, friendly or authoritative, minimal or rich, premium or everyday, modern or heritage, bold or quiet. Record them with `engine.py set macros '["friendly","minimal"]'`. This fills in the personality sliders (Q-brand-01), so don't ask for the sliders.
5. **Do you have a brand color or a logo?** This is Q-color-01, asked together with Q-brand-03. A hex color is recorded as the seed. A logo file becomes the source of candidate colors. With neither, suggest 3 seed colors that fit their words, and label them as a starting point.

Then run `engine.py build`. Show the result: a preview, the palette, and the type scale, on whatever visual surface the host has (see SKILL.md). Name one or two defaults they might want to change. Then make the offer (below).

## Level 1: broad (one screen per foundation)
Go in this order, using the listed templates:
- Q-dir-01, style (`option-gallery`)
- Q-dir-02, how much fits on a screen (`spacing-ruler`)
- Q-color-02, where the brand color shows (`palette`)
- Q-type-01, which font (`type-scale`)
- Q-shape-01, corners (`radius`)
- Q-depth-01, how cards separate (`elevation`)
- Q-motion-01, motion feel (`motion`)
- Q-tool-01, where the master copy lives (text)

Each screen is one message with one question. The person can say "skip" and the default stays. After the last screen, run `engine.py build` and record `engine.py set zoom.all 1`.

## Levels 2 and 3: one area at a time
Areas: overview, platforms, themes, color, type, layout, shape, depth, motion, imagery, voice, components, delivery. Their plain names are in `pacing.json`.
1. Open the area's stage files. Ask its level-2 questions in stage order, then run `engine.py generate` and show the change.
2. Record the level with `engine.py set zoom.<area> 2`.
3. Level 3 uses `NN-*.detailed.md` in the same way.
4. Components live at level 3. Build them from tokens, not from scratch.

## The offer after every level (short)
> Your system works at the **sketch** level. Stop here, or zoom in:
> **Color** (ramps and contrast, about 5 min) · **Text** (sizes and fonts, about 4 min) · **Everything, broadly** (8 quick screens)

- Offer at most 3 choices. Pick them by what matters most for this product: high fan-out areas first (`pacing.json` → `top_decisions`), then anything their answers made risky, such as a light brand color or a dense product.
- Accessibility is never an option to skip. Contrast, target size, focus and reduced motion are already locked in at level 0.
- "Stop" is a good answer. Finish with the Finish steps in SKILL.md at whatever level they reached.

## DESIGN.md at every level
DESIGN.md is refreshed after every decision you record. Run `engine.py design-md` after each confirmed answer, and after `zoom.*` changes. Each section shows its zoom level (sketch, broad, defined, detailed), so a teammate can see what was decided and what is still a default. When someone asks what a section means, point to its zoom line and offer to zoom in.
