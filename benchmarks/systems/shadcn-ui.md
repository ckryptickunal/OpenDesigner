# shadcn/ui

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | shadcn (individual maintainer), repo github.com/shadcn-ui/ui (124,449 stars, 2026-09-23). Vercel affiliation not verified | [S-L09-575] [S-L09-589]; Vercel [inferred] |
| Launch and major versions | Launched January 2023 on Radix. CLI package `shadcn` 1.0.0 2024-07-09; 2.0.0 2024-08-30; 3.0.0 2025-08-27; 4.0.0 2026-03-06. Tailwind v4 + OKLCH 2025-02-19; `shadcn create` 2025-12-12 | [S-L09-584] [S-L09-572] [S-L09-578] [S-L09-580] |
| Current version (Sept 2026) | `shadcn` CLI 4.21.0, 2026-09-04. The components themselves are unversioned code in the registry | [S-L09-572] [S-L09-589] |
| Platforms | Web (React). Templates for Next.js, Vite, Laravel, React Router, Astro, TanStack Start | [S-L09-582] |
| Open source + license | Yes, MIT | [S-L09-575] |
| Code frameworks | React + Tailwind CSS v4. Copy-in source via CLI and registry, "not a component library". Three interchangeable bases: Base UI (default since 2026-07-02), Radix (`radix-ui` package), React Aria (since 2026-07-17) | [S-L09-589] [S-L09-584] [S-L09-585] [S-L09-579] |
| Figma kit | No official kit. Docs: "The Figma files are contributed by the community". Lists 4 free kits (e.g. Obra Community Edition, shadcncraft with Figma variables for all 8 styles) and 7 paid kits | [S-L09-588] |
| Token tiers + naming | 2 tiers of CSS variables. Raw values in `:root` / `.dark` (`--primary: oklch(0.205 0 0)`), mapped to Tailwind with `@theme inline` (`--color-primary: var(--primary)`), used as utilities (`bg-primary`). Surface/foreground pairs: `primary` + `primary-foreground`, plus `border`, `input`, `ring`, `chart-1..5`, `sidebar-*` | [S-L09-587] |
| Color model | OKLCH (HSL converted Feb 2025). 31 semantic tokens per mode (background/foreground, card, popover, primary, secondary, muted, accent, destructive, border, input, ring, chart-1..5, 8 sidebar tokens). Neutral default is pure gray (chroma 0): primary oklch(0.205 0 0), border oklch(0.922 0 0); dark borders white at 10%. Destructive oklch(0.577 0.245 27.325). 7 base colors: Neutral, Stone, Zinc, Mauve, Olive, Mist, Taupe. Ramps come from Tailwind's palette (26 families) | [S-L09-587] [S-L09-578] [S-L09-593] |
| Typeface | Set per preset: Nova = Geist, Vega/Mira/Luma/Rhea = Inter, Maia = Figtree, Lyra = JetBrains Mono, Sera = Noto Sans + Playfair Display headings. Icons per preset: Lucide, Hugeicons, Phosphor | [S-L09-592] |
| Type scale | Tailwind v4 defaults: xs 12/16, sm 14/20, base 16/24, lg 18/28, xl 20/28, 2xl 24/32, 3xl 30/36, 4xl 36/40px. Controls mostly text-sm 14px (Vega button) or text-xs 12px (Lyra, Sera). shadcn/typeset (2026-07-10) adds a prose system with size, leading, flow controls | [S-L09-593] [S-L09-591] [S-L09-586] |
| Spacing | Tailwind `--spacing: 0.25rem` (4px) multiplier; utilities p-1 = 4px, p-2 = 8px, etc. Density is set by choosing a style (Nova, Mira, Rhea are compact), not by changing the multiplier | [S-L09-593] [S-L09-583] |
| Radius | `--radius: 0.625rem` (10px). Derived: sm 0.6x = 6px, md 0.8x = 8px, lg 1x = 10px, xl 1.4x = 14px, 2xl 1.8x = 18px, 3xl 2.2x = 22px, 4xl 2.6x = 26px. Vega button rounded-md (8px), cards rounded-xl (14px); Lyra/Sera rounded-none; Luma buttons rounded-4xl | [S-L09-587] [S-L09-591] |
| Elevation | Mostly borders and 1px rings, light Tailwind shadows. Vega: cards `ring-1 ring-foreground/10 shadow-xs` (0 1px 2px rgb(0 0 0 / 0.05)); overlays shadow-md/lg. Luma adds "soft elevation" | [S-L09-591] [S-L09-593] [S-L09-583] |
| Motion | tw-animate style utilities on overlays: fade-in-0 + zoom-in-95 + slide-in 2 (8px) at duration-100 (100ms); some 200-300ms with `cubic-bezier(0.22, 1, 0.36, 1)`. Tailwind default transition 150ms, ease-out `cubic-bezier(0, 0, 0.2, 1)`. No reduced-motion variants in the Vega style file | [S-L09-591] [S-L09-593]; reduced-motion absence [inferred from grep] |
| Theming + modes | Light + dark via `.dark` class overriding the same variables. Brand theming by editing variables or applying a `--preset` code (colors, theme, icons, fonts, radius in one string). 8 styles rewrite component code: Vega, Nova, Maia, Lyra, Mira, Luma, Sera, Rhea. RTL option. No high-contrast mode | [S-L09-587] [S-L09-582] [S-L09-585] [S-L09-586] |
| Component count | 64 component doc pages for Base UI, 65 for Radix (adds Sonner), 63 for React Aria; counted from the repo docs folders on 2026-09-23. Includes compositions (data-table, date-picker) and chat pieces (message, bubble, attachment) | [S-L09-577] |
| Component doc structure | Installation (CLI + manual), Usage, one section per variant/example, RTL, API Reference. Base/Radix/Aria tabs on each page | [S-L09-590] [S-L09-584] |
| Accessibility stance | Claims "accessible components"; accessibility is inherited from the chosen base (Base UI, Radix, React Aria). No WCAG level stated. Focus ring 3px `ring/50` in Vega | [S-L09-589] [S-L09-591] |
| Governance / contribution | Maintainer-led open source with GitHub PRs. Open registry schema: anyone can publish a registry; official Registry Directory lists community registries; GitHub and private GitHub registries (2026) | [S-L09-589] [S-L09-577] |
| Notable innovation | Distribute source, not a package ("Open Code"). Registry schema + CLI + MCP + agent skills make it the default UI vocabulary for AI code generators (v0, Claude, Codex, Replit named in docs). Presets as a portable design-system code. Primitive-library swapping behind one API | [S-L09-589] [S-L09-586] [S-L09-582] [S-L09-584] |

## Visual signature: why it looks like this
- Achromatic OKLCH neutrals (chroma 0) with a near-black primary oklch(0.205 0 0) -> monochrome, "no brand yet" look that users then recolor [S-L09-587].
- 10px base radius, 8px buttons, 14px cards -> soft but not bubbly corners [S-L09-587] [S-L09-591].
- 1px borders at oklch(0.922) and 10%-white in dark, `shadow-xs` only -> flat cards separated by hairlines [S-L09-587] [S-L09-591].
- 36px buttons with 14px medium text, Inter or Geist -> compact, SaaS-dashboard density [S-L09-591] [S-L09-592].
- Fast 100ms fade + 95% zoom on popovers -> overlays feel instant, little flourish [S-L09-591].
- The defaults were used so widely that shadcn wrote "all apps started looking the same", which led to 8 styles that change geometry, not only color [S-L09-580] [S-L09-583].

## Recent changes 2024-2026
- 2025-02-19: Tailwind v4 and React 19; HSL -> OKLCH; `default` style deprecated for `new-york`; toast -> Sonner; buttons use default cursor [S-L09-578].
- 2025-04-30: registry MCP; 2025-08-27: CLI 3.0 [S-L09-586] [S-L09-572].
- 2025-10-03: Spinner, Kbd, Button Group, Input Group, Field, Item, Empty; written to work with any base library [S-L09-594].
- 2025-12-12: `npx shadcn create` with 5 styles and a Radix or Base UI choice [S-L09-580].
- 2026-01-20: full Base UI docs; 2026-02-02: new-york style moves to unified `radix-ui` package [S-L09-581] [S-L09-579].
- 2026-03-06: CLI v4 with agent skills, `--preset`, `--dry-run`/`--diff` [S-L09-582].
- 2026-03-31 / 04-16 / 05-26: Luma, Sera, Rhea styles [S-L09-583]. 2026-04-25: opt-in pointer cursor [S-L09-586].
- 2026-06-26: chat components MessageScroller, Message, Bubble, Attachment, Marker [S-L09-594].
- 2026-07-02: Base UI becomes the default base; Radix still supported [S-L09-584]. 2026-07-17: React Aria base [S-L09-585]. 2026-07-10: shadcn/typeset [S-L09-586].
- 2026-09-03: components import `cn` from a new `cn` package instead of clsx + tailwind-merge [S-L09-586].

## Builder takeaways
- Export to shadcn's variable contract (`--background`, `--primary`, `--primary-foreground`, `--ring`, `--radius` ...). It is the de facto interchange format for AI code generators.
- Copy the preset idea: one short code that holds colors, fonts, icons and radius, and can re-skin an existing project.
- Treat density and shape as a "style" choice separate from color, as Vega/Lyra/Luma/Sera do; ask users for geometry, not only palette.
- Ask which primitive base (Base UI, Radix, React Aria) the user's code uses; shadcn shows one visual API can sit on any of them.

## Gaps / unverified
- Default preset: docs example `components.json` shows `base-nova` and Nova is first in the CLI preset map, but no doc sentence says "Nova is default".
- Motion: only Vega style CSS was tallied; other styles may differ.
- Accessibility: no conformance statement exists to verify.
- Maintainer's employer (Vercel) not verified this session.
- ui.shadcn.com itself was not opened; all docs values come from the repo's MDX source on main, which is what the site renders.
