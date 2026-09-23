---
name: opendesigner-export
description: Exports an OpenDesigner system to CSS variables, Tailwind, DTCG, Swift, Compose, Figma and Paper, and writes it into Figma or Paper through their MCP servers when connected.
license: MIT
compatibility: Python 3.10+ (standard library). Figma writes need Figma's remote MCP (signed in, Full seat); Paper writes need Paper Desktop running.
metadata:
  version: "0.1.0"
  homepage: "https://github.com/ckryptickunal/OpenDesigner"
---

# OpenDesigner: export and round trip

Use this after an OpenDesigner interview (or on an existing `opendesigner/` folder) when the person wants the system in code, in Figma, or in Paper. The DTCG files in `opendesigner/tokens/` are canonical; every other format is generated from them. Never edit an export by hand: change the decision and regenerate.

The engine is `<skills folder>/opendesigner/scripts/engine.py` (the sibling opendesigner skill). Run it from the project root.

## 1. Code exports (always available)
```
python3 <engine> generate
python3 <engine> validate                   must pass before exporting
python3 <engine> export --format all        or one of: css tailwind dtcg figma paper swift compose
python3 <engine> design-md
```
| Format | Output in `opendesigner/` | Use it |
|---|---|---|
| `dtcg` | `tokens/` (sets plus a resolver for modes) and `dtcg/<theme>.tokens.json` (flat, one mode per file) | Style Dictionary, Terrazzo, Tokens Studio, Penpot |
| `css` | `css/tokens.css` (custom properties, light and dark) | Import once at the app root |
| `tailwind` | `tailwind/theme.css` (Tailwind v4 `@theme`) | `@import` it after Tailwind in the main CSS file |
| `swift` | `swift/DesignTokens.swift` | Add to the iOS target |
| `compose` | `compose/DesignTokens.kt` | Add to the Android UI module |
| `figma` | `figma/variables.json` | Import in Figma (below) when there is no MCP |
| `paper` | `paper/tokens.json`, `paper/tokens.css` | Paper tokens (below) |

Ask before wiring an export into the person's code (editing their CSS entry, Tailwind config or build). Offer to append `<opendesigner>/assets/output/AGENTS-snippet.md` to their AGENTS.md so later agents use the tokens.

## 2. Figma
Detect what is connected before promising anything:
- **Remote Figma MCP with `use_figma`** (signed in, Full seat; canvas writes are in beta): can create variables, styles and frames. If Figma's official skills are installed (`figma-use`, `figma-generate-library`), load them and follow their rules; they know the current API.
- **Figma desktop MCP only** (`get_variable_defs`, `get_design_context`, `get_screenshot`): read-only. Use it to verify, not to write.
- **Nothing connected:** hand over `figma/variables.json` for import (Figma's variables import or Tokens Studio), and say that DTCG import into Figma is partial (one mode per file, sRGB, px, no composite tokens).

Write flow with `use_figma`:
1. Confirm the target file with the person and suggest working on a duplicate first.
2. Create collections by tier: **Primitives** (ramps, raw sizes, no modes) and **Semantic** (roles aliased to primitives, with Light and Dark modes). Modes per collection depend on the Figma plan; check before adding more themes.
3. Create variables with explicit scopes (never "all scopes"), and set code syntax to the CSS variable name so developers see `var(--...)`.
4. Add text styles for the type scale and effect styles for the elevation levels.
5. Build one specimen frame per foundation (palette, type, spacing, radius, elevation) and a component sheet, bound to the variables.
6. Read back with `get_variable_defs` and compare against `tokens/`; report any mismatch.
7. After the person or a designer edits in Figma, read the changes back and apply them as decisions (`engine.py set ... --why "changed in Figma by <name>"`), never by editing token files directly.

## 3. Paper
Paper's MCP server runs inside Paper Desktop (local, `127.0.0.1:29979/mcp`). If its tools are present:
1. Load Paper's guide first (`get_guide` with topic `paper-mcp-instructions`), then `get_basic_info` to see the file.
2. Write tokens from `paper/tokens.json` with `create_tokens` or `set_tokens`. Paper tokens are CSS variables without modes, so write light values and add dark ones as a separate, clearly named set.
3. Call `get_font_family_info` before any typography, then write specimen artboards with `write_html`, one visual group per call: palette, type ladder, spacing ruler, radius, elevation, component sheet. The HTML in `<opendesigner>/assets/templates/` (component sheet, palette) is a good starting point; use the person's tokens, not sample data.
4. Review each artboard with `get_screenshot`; fix clipping by setting the artboard height to fit content.
5. Call `finish_working_on_nodes` when done.
6. Designer comments (`list_comment_threads`) and selections (`get_selection`) come back as decisions through the engine, like Figma edits.

## 4. Before you hand over
- `engine.py validate` passes, or each remaining warning has a written waiver.
- The person knows which file is canonical (DTCG in `opendesigner/tokens/`) and that exports are regenerated, not edited.
- Record the export in the stage summary: formats, destinations (file names, Figma file, Paper file) and date.
