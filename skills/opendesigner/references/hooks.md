# Designer hooks and tool hooks

Some blocks need a human creator or a named tool. OpenDesigner asks for them instead of faking them. Source: `research/L17-how-systems-get-made.md` Part H (formats, fallbacks and checks verified against 81 Tier A pages). Full per-hook detail, including exact sizes, licence terms and evidence ids, is in `hooks.json`.

## Rules for every hook
1. **Ask once, as one checklist** (Q-brand-08 in Stage 03): "Which of these do you already have?" In Quick mode ask nothing: apply each fallback and leave a briefed placeholder.
2. **One vector master, generated derivatives.** Ask for the master (SVG, or PDF with outlined text; layered files for app icons) and derive the platform sizes from it, with size and safe-zone checks.
3. **Keep a licence ledger per asset:** source, licence, attribution string, allowed slots, owner. Keep MIT/ISC/Apache notices for icon libraries; add required credits; block assets from slots their licence forbids (for example some free illustration sets cannot be used in logos).
4. **Fetch per project; never pool assets** into a shared catalog. Several licences forbid offering their assets as a selectable library inside a tool.
5. **State AI-tool terms for the person's plan.** Ownership of AI output varies by tool and plan; in the US purely AI-generated work is not copyrightable (human selection and modification can be); the EU AI Act requires machine-readable marking of synthetic media. Say so when you suggest an AI tool.
6. **The commission path ships a brief** (required files and sizes from `hooks.json`, the system's tokens and direction) plus a reminder that a contractor's logo needs a written copyright assignment.
7. **A generated stand-in is never presented as final.** Placeholders are labelled as placeholders.

Record each hook: `engine.py set hooks.<H-id>.status '"<status>"' --why "..."` with status `have`, `commissioning`, `tool`, `open-library`, `placeholder` or `not-needed`.

## Asset hooks
| Hook | Ask | Master format | If no (in order) |
|---|---|---|---|
| `H-logo` (Q-brand-03) | Logo, wordmark, symbol, lockups? One-color version? | SVG or PDF, text outlined | Commission (brief + assignment reminder); AI logo tools with caveats and a trademark search; wordmark in the chosen typeface |
| `H-appicon` (Q-icon-06) | App icon artwork, ideally layered? | Layered SVG/PDF (Apple Icon Composer), adaptive layers (Android), PNG for stores | Designer; Icon Composer; Android Studio Image Asset; Maskable.app |
| `H-favicon` (with the logo) | Asked with the logo | Master SVG | Generated from the symbol: favicon.ico 32, icon.svg with dark-mode query, apple-touch 180, manifest 192/512 + maskable |
| `H-icons` (Q-icon-01) | An icon set, or icons libraries lack? | SVG on the library grid, SF Symbol templates, Android vector drawables | Lucide, Phosphor, Tabler, Heroicons, Material Symbols (keep notices); custom icons on the 24 px keyline; commission pictograms |
| `H-illus` (Q-img-04) | Illustrations or a character style? | Master SVG, Lottie for animation | Commission; open sets with their exact terms; AI vector tools with plan terms; or no illustration and honest text empty states |
| `H-photo` (Q-img-01) | Photography or a photo style? | Highest-resolution originals | Commission; Unsplash or Pexels under their licences; AI images with ownership caveats and synthetic-media marking |
| `H-type` (Q-type-02) | A brand typeface? Which licences: web, app embedding, self-hosting? | OTF/TTF masters, WOFF2 for web | Google Fonts (OFL/Apache, self-host OK); Fontshare (no subsetting or conversion, not offerable in a design tool's picker); Adobe Fonts (web embed only, no self-hosting or app embedding); buy the needed licences |
| `H-color` (Q-color-01) | Brand colors that must be exact? | Hex, RGB, OKLCH, Pantone refs, Figma variables | Candidates from the logo or brand book; otherwise seeds from the personality dials, labelled a starting point |
| `H-motion` (Q-img-06) | Logo animation, loaders, animated illustration, 3D? | Lottie / dotLottie, Rive, glTF/GLB, USDZ | Commission a motion designer; otherwise motion tokens only, no signature animation |
| `H-motif` (Q-img-07, Q-shape-05) | Brand patterns, textures, gradients, a signature shape? | SVG patterns, gradient definitions | Commission; or none (decoration standing in for content reads generic) |
| `H-sound` (Q-motion-08) | UI sounds or a sonic logo? | Apple: .aiff/.wav/.caf under 30 s; Android: Ogg, WAV, MP3, AAC, FLAC | Commission; platform system sounds; or no sound |
| `H-haptic` (Q-motion-09) | Custom haptic patterns? | Apple AHAP, Android VibrationEffect | System patterns first |
| `H-voice` (Q-voice-01) | A voice and tone guide or word list? | PDF, Markdown, existing product copy | Model drafts voice from the personality answers, marked draft until a content designer or owner reviews it |
| `H-brandbook` (Q-ref-01) | A brand book? | PDF | Hand to opendesigner-extract: colors, font names, embedded logos; ask for the SVG master of any logo found |

## Tool hooks
| Hook | Question | Named tools | Caveat |
|---|---|---|---|
| `H-tokens` | Which platforms consume tokens, and how do you ship packages? | Style Dictionary, Terrazzo, Tokens Studio | Only about 40% of teams automate token sync; Figma imports DTCG only partly |
| `H-figma` | Which design tool and plan? (Q-tool-03) | Figma remote MCP `use_figma`, Tokens Studio, Paper MCP, Penpot (native DTCG) | Figma modes per collection depend on plan; Code Connect is plan-gated |
| `H-comp` | Which component library or stack? | Radix, Base UI, React Aria, shadcn registry | Review against the WAI-ARIA Authoring Practices |
| `H-dataviz` | Do you show charts? Which library? | Chart libraries per L05 | Library defaults override tokens unless themed |
| `H-a11y` | Who tests with assistive technology? | axe-core and lint rules, plus human screen-reader passes | Automated tools catch only part of WCAG |

## Brief for a missing asset (fill and hand to the person)
```
Asset: <hook name>            Needed by: <date or milestone>
Files: <formats and sizes from hooks.json>
System: <link to opendesigner/DESIGN.md>; palette <accent + neutrals>; type <faces>; radius <control/container>
Direction: <the chosen direction in one line>; memorable thing: <from Stage 0>
Constraints: <licence, platforms, dark mode, reduced motion>
Rights: written copyright assignment to <owner> on delivery
```
