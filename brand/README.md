# OpenDesigner brand

OpenDesigner's own design system, made with OpenDesigner, plus the images we post on GitHub, X and Threads.

## Where things are

| Path | What it holds |
|---|---|
| `opendesigner/`, `DESIGN.md`, `PRODUCT.md` | The brand's design system, built by the engine. Open `opendesigner/overview.html` to see all of it, including what is still missing |
| `design-system/project/` | The brand system as a Claude Design System artifact: tokens, brand book, logos and the post templates. This folder is the source; the artifact is a copy |
| `design-system/build_previews.py` | Writes the artifact's preview cards (the post templates) from `tokens.json` |
| `TYPE-RULES.md` | Apple's and Google's type rules, checked against their live docs, plus measurements of two reference sites |
| `TYPE-REVIEW.md` | What went wrong with the first kit's type, and what good type needs |
| `showcase/` | 46 pieces made through OpenDesigner as a stress test, with the findings in `showcase/STRESS-TEST.md` |
| `export/` | The first kit (warm black, ember, Geist). It's been replaced, and it stays until the new kit is approved and exported |

## The system in one paragraph

Cobalt (`#2338FF`) on cool neutrals, in three themes: Light, Dark and Cobalt. Hanken Grotesk sets every word, with light titles. Source Code Pro is used only for real code. Each screen gets one loud thing: a cobalt highlight box, a primary button or the circle in the mark. The full rules are in the artifact's brand book (`design-system/project/README.md`).

## Republish the artifact

The live artifact is <https://claude.ai/artifact/KnazbYyqmgHzut46upccBv>. It is private until shared from its Share menu. After changing anything in `design-system/project/`:

```
python3 brand/design-system/build_previews.py --shots
```

Then ask Claude Code to publish `brand/design-system/project/` to that artifact. The index goes last, after the logos, which are uploads.

## Rebuild the system

```
cd brand
python3 ../skills/opendesigner/scripts/engine.py build
```

This refreshes the tokens, `DESIGN.md`, `opendesigner/overview.html`, the filled templates in `opendesigner/preview/`, and the artifact files in `opendesigner/build/artifact/`.

## Rules

- Never put another company's name or logo in any image.
- Use at most two fonts in any one thing.
- Keep tonal contrast clear: dark text on light grounds and light text on dark grounds.
- Show the system in the artifact before rendering any exports.
