# Tailwind CSS (as a token/utility system)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Tailwind Labs (founder Adam Wathan). Acquisition by Shopify announced 2026-09-09; the team keeps maintaining the OSS projects | [S-L09-606] |
| Launch and major versions | 0.1.0 2017-11-01; 1.0.0 2019-05-13; 2.0.0 2020-11-18; 3.0.0 2021-12-09; 4.0.0 2025-01-21 (blog post 2025-01-22). v4 minors: 4.1.0 2025-04-01, 4.2.0 2026-02-18, 4.3.0 2026-05-08 | [S-L09-600] [S-L09-605] |
| Current version (Sept 2026) | tailwindcss 4.3.3, 2026-07-16. A `v3-lts` npm tag still ships 3.4.19 | [S-L09-600] [S-L09-608] |
| Platforms | Web (CSS). Build integrations for Vite, PostCSS and a CLI, plus a first-party webpack loader since 4.2 | [S-L09-607]; Vite/PostCSS/CLI [inferred] |
| Open source + license | Yes, MIT (~97.6k GitHub stars). Shopify post: "Everything will always be MIT-licensed". Tailwind Plus (paid) is a separate commercial product | [S-L09-608] [S-L09-606] |
| Code frameworks | Framework-agnostic CSS utilities. Tailwind Plus ships React, Vue and HTML (formats per a Tier C page); vanilla JS support added 2025-07-25. Catalyst is a React UI kit inside Tailwind Plus | [S-L09-605] [S-L09-611] [S-L09-615]; Catalyst = React [inferred] |
| Figma kit | No official free Figma kit found on the docs or blog. Not verified further | [inferred] |
| Token tiers + naming | 1 built-in tier: flat primitives declared in `@theme`, grammar `--{namespace}-{key}` plus `--{token}--{sub-property}`. Examples: `--color-blue-500`, `--radius-lg`, `--text-sm--line-height`. 20 namespaces (color, font, text, font-weight, tracking, leading, tab-size, breakpoint, container, spacing, radius, shadow, inset-shadow, drop-shadow, blur, perspective, zoom, aspect, ease, animate). A semantic tier is user-defined (`@theme inline` or `:root` vars) | [S-L09-609] [S-L09-604] |
| Color model | 26 families x 11 steps (50, 100-900, 950) = 286 OKLCH values, plus black #000 and white #fff. 17 hues (red to rose) and 9 neutrals: slate, gray, zinc, neutral, stone, plus mauve, olive, mist, taupe (added in 4.2). Sample: blue-500 `oklch(62.3% 0.214 259.815)`, neutral-500 `oklch(55.6% 0 none)`. 0 semantic roles. Accent is picked, not generated | [S-L09-604] [S-L09-607] [S-L09-613] |
| Typeface | No brand face. System stacks. 4.3.3 `--font-sans`: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif + emoji (was `ui-sans-serif, system-ui` through 4.3.0). Mono: ui-monospace, SFMono-Regular, Menlo... Serif: ui-serif, Georgia... | [S-L09-604] [S-L09-608] |
| Type scale | 13 sizes, each with a paired line height: xs 12/16, sm 14/20, base 16/24, lg 18/28, xl 20/28, 2xl 24/32, 3xl 30/36, 4xl 36/40, 5xl 48, 6xl 60, 7xl 72, 8xl 96, 9xl 128 (5xl up at line-height 1). Hand-tuned. 9 weights thin 100 to black 900. Tracking tighter -0.05em to widest 0.1em. Leading tight 1.25 to loose 2 | [S-L09-604] |
| Spacing | One base token `--spacing: 0.25rem` (4px). Every spacing/sizing utility is `calc(var(--spacing) * n)` for any number n (e.g. `w-17`). Since 4.3.1, `m-1` emits `var(--spacing)` and `m-0` emits `0`. Breakpoints sm 40rem, md 48rem, lg 64rem, xl 80rem, 2xl 96rem. Containers 3xs 16rem to 7xl 80rem | [S-L09-604] [S-L09-613] [S-L09-608] |
| Radius | xs 2px, sm 4px, md 6px, lg 8px, xl 12px, 2xl 16px, 3xl 24px, 4xl 32px (+ `rounded-full`). No default control radius because core has no components | [S-L09-604]; full [inferred] |
| Elevation | Shadows only, all black-alpha: 2xs `0 1px rgb(0 0 0/.05)`; xs `0 1px 2px 0 /.05`; sm `0 1px 3px 0 /.1, 0 1px 2px -1px /.1`; md `0 4px 6px -1px, 0 2px 4px -2px` (/.1); lg `0 10px 15px -3px, 0 4px 6px -4px`; xl `0 20px 25px -5px, 0 8px 10px -6px`; 2xl `0 25px 50px -12px /.25`. Plus inset-shadow 2xs-sm, drop-shadow xs-2xl, text-shadow 2xs-lg (4.1) | [S-L09-604] |
| Motion | Default transition 150ms `cubic-bezier(0.4, 0, 0.2, 1)`. `--ease-in` (0.4, 0, 1, 1), `--ease-out` (0, 0, 0.2, 1), `--ease-in-out` (0.4, 0, 0.2, 1). Animations: spin 1s linear, ping 1s (0,0,0.2,1), pulse 2s (0.4,0,0.6,1), bounce 1s. No springs. Reduced motion is opt-in per element via `motion-safe:` / `motion-reduce:` | [S-L09-604] [S-L09-661] |
| Theming + modes | `dark:` variant follows `prefers-color-scheme` by default; switch to class or data attribute with `@custom-variant dark (&:where(.dark, .dark *))`. `contrast-more:`, `contrast-less:`, `forced-colors:` variants. Themes = overriding CSS variables; `--color-*: initial` wipes a namespace. No density mode | [S-L09-612] [S-L09-661] [S-L09-609] |
| Component count | 0 in core (utilities only). Tailwind Plus: "500+" UI blocks per a third-party page; the official storefront now shows only a sign-in page, so the count is unconfirmed | [S-L09-615] [S-L09-610] [S-L09-614] |
| Component doc structure | Per utility page: Quick reference (class -> CSS table), Examples, Customizing your theme | [S-L09-660] |
| Accessibility stance | No stated WCAG target for the framework or palette. Provides media-query variants (motion, contrast, forced colors); `sr-only` utility | [S-L09-661]; no target found [inferred]; sr-only [inferred] |
| Governance / contribution | Company-led core team, public GitHub repo; from 2026-09 inside Shopify. No public RFC process found | [S-L09-606] [S-L09-608]; RFC absence [inferred] |
| Notable innovation | Tokens that generate their own utilities (`@theme`), exposed as native CSS variables at runtime. One `--spacing` multiplier instead of a fixed scale. OKLCH default palette (first mainstream framework to ship one) | [S-L09-609] [S-L09-613]; "first" [inferred] |

## Visual signature: why it looks like this
Tailwind has no fixed look. It has a very recognisable default look, because most sites keep the defaults.
- 4px spacing multiplier with any-integer steps (`p-4` = 16px) -> tight, even rhythm; layouts land on a 4px grid without a designer choosing it [S-L09-604].
- System font stack, 14/20 and 16/24 body sizes, 600-700 headings -> the neutral "every SaaS" text look. Nothing brand-specific comes from the type layer [S-L09-604].
- Soft black-alpha shadows (`0 1px 3px /.1`) + 6-12px radius (`rounded-md` to `rounded-xl`) + `ring-1` borders -> the familiar "Tailwind UI card": white panel, faint border, small blur [S-L09-604]; ring usage [inferred].
- OKLCH palette with high chroma at 500-600 (blue-500 C=0.214) -> saturated accents that look vivid on P3 screens; indigo/blue buttons on zinc or slate neutrals is the default combination [S-L09-604] [S-L09-613]; combination [inferred].
- Five cool-to-neutral grays (slate is blue-tinted, zinc slightly cool, stone warm), plus four tinted neutrals since 4.2 -> the gray you pick sets the temperature of the whole UI [S-L09-604] [S-L09-607].
- 150ms default transitions with Material-style curves -> quick, understated state changes; no springs or overshoot [S-L09-604].

## Recent changes 2024-2026
- 2024-11-21: v4.0 beta 1 [S-L09-605].
- 2025-01-22: v4.0. CSS-first `@theme` config replaces `tailwind.config.js`, palette moves from rgb to OKLCH, single `--spacing` variable. Full builds 3.78x faster, incremental up to 182x [S-L09-613].
- 2025-03-04: Tailwind UI renamed Tailwind Plus (one-time purchase, includes Catalyst) [S-L09-611].
- 2025-04-03: v4.1 adds text shadows and masks [S-L09-605].
- 2026-02-18: v4.2 adds mauve, olive, mist, taupe neutrals, logical-property utilities (`pbs-*`, `mbe-*`, `inset-s-*`), `font-features-*`, webpack plugin [S-L09-607] [S-L09-600].
- 2026-05-08: v4.3 adds scrollbar utilities, `@container-size`, `zoom-*`, `tab-*`, stacked `@variant`, `--default()` for functional utilities [S-L09-607].
- 2026-07-16: 4.3.3 swaps `system-ui`/`ui-sans-serif` for explicit platform fonts so CJK text respects `lang` on Windows [S-L09-608].
- 2026-09-09: Tailwind Labs joins Shopify. Tailwind Plus and ui.sh close sign-ups for new customers [S-L09-606].

## Builder takeaways
- Offer "Tailwind v4 `@theme`" as an export target. It is the most common place a generated token set will land. Map builder tokens onto the 20 namespaces and emit `--{namespace}-{key}` names [S-L09-609].
- Copy the single-multiplier spacing model (`--spacing` x n) as a preset. Ask the user for the base (4px default) rather than a list of steps [S-L09-613].
- Ship a semantic layer on top. Tailwind has 0 semantic color roles, so a builder adds value by generating `bg`, `fg`, `border` roles that point at Tailwind primitives [S-L09-604].
- Default to OKLCH 11-step ramps (50-950) for interoperability, and let the user pick a neutral temperature from 9 options [S-L09-604].

## Gaps / unverified
- Tailwind Plus component and template counts: the official page now redirects to sign-in. "500+" comes from a Tier C page only.
- Whether an official Figma kit exists: none found; not confirmed either way.
- No accessibility target or governance/RFC process was found in the pages opened.
- What the Shopify acquisition changes for roadmap and Catalyst: the announcement does not mention Catalyst.
