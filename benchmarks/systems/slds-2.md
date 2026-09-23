# Salesforce Lightning Design System 2 (SLDS 2, Cosmos theme)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Salesforce (Salesforce UX; built files credit the "Design Systems Engineering team") | [S-L09-237] [S-L09-238] |
| Launch and major versions | SLDS 1: `@salesforce-ux/design-system` on npm 2015-09-09, 2.0.0 2016-06-06. SLDS Linter 0.1.0 2025-02-27, 1.0.0 2025-09-17. SLDS 2 CSS package `@salesforce-ux/design-system-2`: first alpha 2026-03-19; 1.0.0 2026-04-07; 2.0.0 2026-04-08; 2.0.1-2.0.4 June 2026; 2.264.0, the first stable of the Winter '27 line, 2026-07-21 (corrected by the L09 verification pass [S-L09-732, 733]). Beta and GA dates for SLDS 2 itself not confirmed from a primary source (see Gaps) | [S-L09-236] |
| Current version (Sept 2026) | Winter '27: `@salesforce-ux/design-system` 2.264.2 (2026-09-06) and `@salesforce-ux/design-system-2` 2.264.2 (2026-09-10), built with `@salesforce-ux/design-tokens` 4.1.0. Version numbers jumped from 2.30.4 (Summer '26) to 2.264.x, which matches Salesforce release numbering [inferred]. SLDS 2 docs default release label: "Summer '26 v3.3.3" | [S-L09-236] [S-L09-237] [S-L09-243] [S-L09-242] |
| Platforms | Web: Salesforce platform (Lightning Web Components, Aura) and any HTML via CSS | [S-L09-240] [S-L09-237] |
| Open source + license | Mixed. SLDS 1: BSD-3-Clause code, CC BY-ND 4.0 icons. SLDS 2 npm: proprietary "Terms of Use" (royalty-free license, not OSI); its GitHub repo is issues-only and "not licensed under any Open Source license". `lightning-base-components` MIT; SLDS Linter and starter kit Apache-2.0 | [S-L09-244] [S-L09-237] [S-L09-238] [S-L09-245] |
| Code frameworks | CSS blueprints + styling hooks; Lightning Web Components base components (`lightning-base-components` 1.28.19-alpha); Aura. SLDS 1 also has `@salesforce/design-system-react` 0.10.65 | [S-L09-237] [S-L09-245] [S-L09-236] |
| Figma kit | SLDS 2 docs list a "Figma Kits" page under Tools; its content is JS-only and was not read. Variables not confirmed | [S-L09-242] |
| Token tiers + naming | 4 hook tiers as CSS custom properties. Reference `--slds-r-*` (`--slds-r-color-brand-50`); global `--slds-g-*` (`--slds-g-color-accent-1`, `--slds-g-spacing-4`, `--slds-g-radius-border-2`); shared `--slds-s-*` (`--slds-s-button-radius-border`, `--slds-s-input-color-border`); component `--slds-c-*` (`--slds-c-button-destructive-color-background`). Cosmos file: 85 r, 524 g, 107 s, 16 c. Component-level hooks are Beta | [S-L09-237] [S-L09-242] |
| Color model | Reference ramps brand, info, success, error, warning: 17 steps each (5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 85, 90, 95). Global palette hooks: 13 hues x 12 steps (blue, cloud-blue, electric-blue, green, hot-orange, indigo, orange, pink, purple, red, teal, violet, yellow) + neutral 14. sRGB hex. 326 global color hooks; roles surface, surface-container, on-surface, accent, accent-container, border, error, success, warning, info, disabled (1-3 levels each). Accent: Cosmos `accent-1` = brand-50 #066afe; Lightning Blue uses `var(--lwc-brandPrimary, brand-60)`, so org branding flows in | [S-L09-237] |
| Typeface | System stack: `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif`; mono `Consolas, Menlo, Monaco, Courier`. Salesforce Sans was removed as the default in 2.15.0 (2021-03-25) | [S-L09-237] [S-L09-244] |
| Type scale | Base 13px (`font-scale-base` 0.8125rem), ratio hook 1.15. Cosmos: neg-2 10, neg-1 12, base 13, 1: 14, 2: 16, 3: 20, 4: 24, 5: 28, 6: 32, 7: 40, 8: 48px. Lightning Blue: 10, 12, 13, 14, 16, 18, 20, 24, 28, 32, 42px. Line heights 1, 1.25, 1.375, 1.5 (base), 1.75, 2. Weights 100-700. Hand-tuned steps | [S-L09-237] |
| Spacing | 4px base. `--slds-g-spacing-1..12` = 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80px (same in both themes). Sizing 1..16 = 2px to 480px | [S-L09-237] |
| Radius | Cosmos `radius-border-1..4` = 4, 8, 12, 20px; pill 15rem; circle 100%. Lightning Blue = 2, 4, 8, 16px. Defaults, Cosmos: buttons pill, inputs 8px, containers 20px, avatars and icons circular. Lightning Blue: buttons, inputs, containers 4px | [S-L09-237] |
| Elevation | Shadows + surfaces. `shadow-1..5` (5 = 4). Cosmos stacks 3 layers with `light-dark()` alpha, e.g. shadow-1 = 0 0 2px + 0 2px 2px (black 18% light / 36% dark) + 0 -1px 2px (10% / 20%). Lightning Blue uses one layer: 0 2px 2px #0000001A up to 0 2px 5px #00000027. Surfaces: surface-1 #fff, surface-2 #f3f3f3 (Cosmos dark #242424 / #181818). Focus ring 2px brand-15 (Cosmos) vs brand-40 (Lightning Blue) | [S-L09-237] |
| Motion | Duration hooks: instantly 0s, immediately 0.05s, quickly 0.1s, promptly 0.2s, slowly 0.4s, paused 3.2s; toast short 4.8s, medium 9.6s. No easing hooks in the theme files. Cosmos buttons lift on hover: brand `translateY(-2px)` with a hard `0 2px 0 0` shadow, bordered `-1.5px`. Reduced-motion policy not found | [S-L09-237] |
| Theming + modes | 2 themes over one structure file: Cosmos and Lightning Blue, swapped at runtime by changing one theme stylesheet. Cosmos has dark mode built in through CSS `light-dark()` (352 uses), switched with the body class `slds-color-scheme_dark` (SLDS 2 only). Lightning Blue is light-only. Docs include "Color Modes", "Themes" and "Display Density" pages; scoped CSS variants ship too | [S-L09-237] [S-L09-238] [S-L09-242] |
| Component count | 48 component pages in SLDS 2 docs (nav read 2026-09-22). The SLDS 2 npm package has 89 component folders (includes utilities and templates). 85 CSS blueprint docs in `design-system-md-docs`. `lightning-base-components` has 211 modules (includes private utilities) | [S-L09-242] [S-L09-237] [S-L09-239] [S-L09-245] |
| Component doc structure | Not verified (page bodies are JS-only). Docs sections: Components, Patterns, Visual Language, Accessibility, Styling API, Utility Classes, Tools, AI and SLDS 2 | [S-L09-242] |
| Accessibility stance | WCAG AA; text contrast at least 4.5:1 (small) and 3:1 (large). SLDS 2 docs have Global Focus, Text and Color Contrast, Keyboard Interaction, Mobile Design and Global Accessibility Standards pages | [S-L09-243] [S-L09-242] |
| Governance / contribution | Central Salesforce UX team; releases follow Salesforce's seasonal train (Spring / Summer / Winter). SLDS 2 repo only takes issues. Adoption is enforced with SLDS Linter (ESLint-based, LWC HTML/CSS + Aura, SARIF reports, bulk autofix) and SLDS Validator | [S-L09-236] [S-L09-238] [S-L09-240] [S-L09-242] |
| Notable innovation | Styling hooks as a public CSS custom-property API in 4 tiers; linter-driven migration from SLDS 1 to 2; one component set rendered as two very different themes (4px vs pill); AI docs section (Prompt Design Guide, Agentic Patterns, AI Development Skills, SLDS 2 AI Starter Kit) | [S-L09-237] [S-L09-240] [S-L09-242] |

## Visual signature: why it looks like this
- Cosmos: pill buttons (15rem), 20px container radius, circular icons and avatars -> soft, consumer-grade look on an enterprise product. Lightning Blue keeps 4px everywhere -> the classic squared Lightning look. [S-L09-237]
- Cosmos fixes one saturated accent, brand-50 #066afe; Lightning Blue defers to the org's `--lwc-brandPrimary` (fallback brand-60 #4992fe) -> Cosmos looks uniformly "Salesforce blue", Lightning Blue follows each customer's brand. [S-L09-237]
- 13px system-font base with a 1.15 ratio -> dense, platform-native data screens (tables, record pages). [S-L09-237]
- #f3f3f3 app surface under #fff cards with 3-layer Cosmos shadows (7-18% black in light mode) -> tactile, card-based layout. [S-L09-237]
- Brand buttons lift 2px on hover with a hard 2px bottom shadow -> physical, "pressable" controls. [S-L09-237]
- Cosmos input focus uses inset shadows (2px 2px 5px black 8% inset + 0 0.5px 2px black 35% inset) and keeps the neutral border; Lightning Blue uses a 3px accent glow and an accent border -> Cosmos fields feel recessed, not outlined. [S-L09-237]

## Recent changes 2024-2026
- 2025-02-27: SLDS Linter 0.1.0 on npm (package created 2025-01-22); 1.0.0 on 2025-09-17; 1.1.0 on 2026-01-12; 1.2.1 on 2026-03-05. [S-L09-236]
- 2025-09-04: last `@salesforce-ux/stylelint-plugin-slds` release (0.5.3); the ESLint plugin continues (1.2.1). [S-L09-236]
- 2025-10-01: SLDS 1 2.28.1, the last entry in the public release notes on `main`. [S-L09-244]
- 2026-03-19: `@salesforce-ux/design-system-2` first published (alpha); beta from 2026-03-26; 1.0.0 on 2026-04-07 and 2.0.0 on 2026-04-08; 2.264.0 (first stable of the 2.264 line) on 2026-07-21; 2.264.2 on 2026-09-10. [S-L09-236] [S-L09-732]
- 2026-03-20: `design-system-2-starter-kit` repo created (LWC + Vite, SLDS 1/2 and light/dark/system switch); it ships AGENTS.md, CLAUDE.md and an MCP config. [S-L09-238]
- 2026-05-26: SLDS 1 2.30.4, the last Summer '26 build under the old numbering. [S-L09-236]
- 2026-07 to 09: package versions realigned to 2.264.x for Winter '27 on both SLDS 1 and SLDS 2. [S-L09-236] [S-L09-243]
- 2026-08-18: `design-system-md-docs` (markdown CSS-class docs plus a Cosmos flat token file) updated. [S-L09-239]
- 2026-09-06: SLDS 1 2.264.2 published; the SLDS 1 site now shows "Current release: Winter '27 (SLDS 2.264.2)" and a banner to explore the Cosmos theme. [S-L09-236] [S-L09-243]
- 2026-09-22: SLDS 2 docs updated, with an "AI and SLDS 2" section, Agentic Patterns and Interaction Models. Component-level styling hooks and the Currency pattern are marked Beta. [S-L09-242]

## Builder takeaways
- Split "structure CSS" from "theme CSS" so a user can swap a whole visual theme by changing one file. SLDS proves one component set can go from 4px to pill.
- Offer the r / g / s / c hook grammar (reference, global, shared, component) as a naming preset. It is short and readable in CSS.
- Ship a linter with the generated system to find hardcoded values and suggest hooks. Salesforce made this the main migration path.
- Offer dark mode as `light-dark()` pairs inside one theme file, switched by a class or `color-scheme`.

## Gaps / unverified
- SLDS 2 beta and GA dates (the brief mentions Spring '25 / Summer '25) could not be confirmed. developer.salesforce.com returned HTTP 403, the SLDS 2 docs bodies are JS-only, and web search was unavailable. Evidence shows a stable npm package since 2026-07-21 and the SLDS 1 site promoting the Cosmos theme. [S-L09-241] [S-L09-242] [S-L09-243]
- Whether the Cosmos theme is GA or beta inside Salesforce orgs is not confirmed.
- The brief listed Salesforce Sans. It was removed in 2021; both SLDS 2 themes use the system font stack. [S-L09-244]
- Figma kit contents, easing curves and reduced-motion policy are not public in the sources read.
- A public count of Lightning base components was not found; the 211 modules include private utilities.
- Which theme (Cosmos or Lightning Blue) is the default for new orgs was not confirmed.
- How Cosmos handles org branding is not confirmed; only Lightning Blue reads `--lwc-brandPrimary` in the theme file. [S-L09-237]
- The Cosmos flat token JSON in `design-system-md-docs` was not parsed; values here come from the built theme CSS. [S-L09-239]
- Display density values (comfy vs compact) were not captured; the docs page exists but its body is JS-only. [S-L09-242]
- SLDS Validator, Scope Customizer and the AI Starter Kit are listed under Tools but were not examined. [S-L09-242]
- How far styling hooks reach into Aura components (beyond the linter's Aura support) was not checked. [S-L09-240]
- Lightning Blue has no dark values in its theme CSS; any plan to add them is unknown. [S-L09-237]
- Version conflict: the SLDS 2 docs label their release "Summer '26 v3.3.3" while the npm package is 2.264.2 (Winter '27). Docs and packages seem to be numbered separately [inferred]. [S-L09-242] [S-L09-236]
