# Spotify Encore

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

Encore is internal and not open source. Public information comes from two places. (1) Spotify Design articles, now reachable only through the Wayback Machine, because spotify.design 301-redirects to open.spotify.com as of 2026-09-23 [S-L09-468]. (2) The `--encore-*` CSS custom properties that ship in Spotify's public web player [S-L09-470]. Values from (2) are observed product code. Token names are real; how Spotify groups them internally is inferred.

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Spotify. Distributed Encore teams (Encore Foundation, Encore Web, mobile component team, local-system teams) | [S-L09-469] [S-L09-472] |
| Launch and major versions | Before Encore: GLUE (2014-15 brand refresh, 30+ people), then about 22 grassroots systems (e.g. Tape for web). Encore project started 2018 and introduced internally November 2019. The public intro article's original URL is dated 2019-12-16; the migrated page shows "September 2020". Three-years-on update December 2022. No public version numbers | [S-L09-469] [S-L09-471] [S-L09-472] |
| Current version (Sept 2026) | Not public. Live web player CSS bundle `web-player.ef42be14.css`, fetched 2026-09-23 | [S-L09-470] |
| Platforms | Web (web player, desktop app built on web tech, websites), iOS, Android, plus TV, car, wearables and speakers (45 platforms in 2019) | [S-L09-469] [S-L09-472] |
| Open source + license | No; proprietary. 0 public Encore repos in the Spotify GitHub org | [S-L09-469] [S-L09-475] |
| Code frameworks | Encore Web: React + TypeScript, with component APIs in 3 layers (config props, slots, custom composition). Ships tokens as CSS custom properties (238 distinct `--encore-*` names) plus hashed class names. Mobile frameworks: not public | [S-L09-489] [S-L09-470] |
| Figma kit | Internal Figma toolkits kept in sync with code tokens by the "Figgy" bot across thousands of files. No public Figma file | [S-L09-472] |
| Token tiers + naming | Started non-semantic (palette, spacers, type scale). Semantic layers added after 2020. Observed web tiers: scale tokens (`--encore-spacing-looser-2`, `--encore-corner-radius-base`, `--encore-text-size-larger`), semantic color roles (`--background-elevated-base`, `--text-subdued`, `--essential-bright-accent`), component tokens (`--encore-button-min-block-size`). Grammar: base plus tighter-n / looser-n, smaller-n / larger-n | [S-L09-472] [S-L09-470] |
| Color model | Color "sets": 16 sets (base, bright-accent, muted-accent, negative, warning, positive, announcement, their subdued variants, inverted, inverted-light/dark, over-media, app-frame). Each defines the same 25 roles: background base/highlight/press, elevated x3, tinted x3, text x7, essential x7, decorative x2. Dark base set: background-base #121212, highlight #1f1f1f, elevated-highlight #2a2a2a, text-base #fff, text-subdued #b3b3b3, bright-accent #1ed760. Light base set: text-subdued #656565, bright-accent text #107434. A color-theming algorithm generates themes "with guaranteed accessible color contrast" | [S-L09-470] [S-L09-472] |
| Typeface | Spotify Mix (bespoke variable font by Dinamo Typefaces, launched 2024-05-22). Web stacks: `SpotifyMixUI` (body), `SpotifyMixUITitle` (titles), `SpotifyMixUITitleVariable`, with script cuts. CircularSp is the fallback for non-Latin scripts. Before that: Circular, adopted in the 2014-15 refresh | [S-L09-473] [S-L09-470] [S-L09-469] |
| Type scale | 10 text-size tokens, responsive. Small devices (<= 767px): .5625, .6875, .8125, 1, 1.125, 1.25, 1.5, 2, 2.5, 3 rem. Medium (>= 768px): .625, .75, .875, 1, 1.25, 1.5, 2, 3, 4, 6 rem. Base 1rem (16px). Line heights and style names not captured | [S-L09-470] |
| Spacing | 12 tokens. Fixed tighter end: tighter-5 2, tighter-4 4, tighter-3 6, tighter-2 8, tighter 12, base 16 px. Looser end on small devices: 20, 24, 32, 40, 48, 64 px; on medium: 24, 32, 48, 64, 96, 128 px. Layout margins 16/16/24 (small) and 24/32/64 (medium) | [S-L09-470] |
| Radius | corner-radius smaller 2, base 4, larger 6, larger-2 8, larger-3 16 px. A 500px pill radius is used on the green #1ed760 play/CTA button through a hashed class, not a token | [S-L09-470] |
| Elevation | Tonal, not shadow-led. Dark theme lifts surfaces by lightness: #121212 base, #1f1f1f elevated, #2a2a2a elevated-highlight. Tinted overlays at white 10%/14%/21%. Inputs, selects and text areas draw their outline with box-shadow (`--encore-input-box-shadow-color` and similar tokens). Border widths: hairline 1, thin 2, focus 2, thick 4, thicker 8 px | [S-L09-470] |
| Motion | Durations: shortest-1 50ms, shortest-2 100ms, shortest-3 150ms, shortest-4 200ms, short-1 250ms, short-2 300ms. "Productive" easings: productive (0.3,0,0,1), decelerate (0,0,0.2,1), accelerate (0.8,0,1,1). Enter = 250ms decelerate; exit = 200ms accelerate. Web CSS has 28 `prefers-reduced-motion: no-preference` gates and 2 `reduce` blocks | [S-L09-470] |
| Theming + modes | Dark (default for the player) and light themes (`.encore-dark-theme`, `.encore-light-theme`). Color sets nest inside themes. Layout themes by device size (`.encore-small-devices-theme` <= 767px, `.encore-medium-devices-theme` >= 768px). Local systems per product (e.g. Spotify for Artists) | [S-L09-470] [S-L09-469] |
| Component count | Not public. Web component families visible in CSS include button, list-row, image, icon, progress-circle, input, select, text-area, field-group, verified-badge [inferred: from token prefixes] | [S-L09-470] |
| Component doc structure | Not public. The internal Encore website shares one structure across all member systems | [S-L09-469] |
| Accessibility stance | Accessibility guidelines live in Encore Foundation. In late 2020 an accessibility drive wanted to adjust Spotify Green for contrast, but non-semantic tokens made that unsafe. The later theming algorithm guarantees contrast. Focus outline 3px. No public WCAG level | [S-L09-469] [S-L09-472] [S-L09-470] |
| Governance / contribution | Federated "system of systems". Each system has a dedicated team and anyone can contribute. An embed program put someone on an Encore team every day of 2022. Adoption tracked through daily repo queries and dashboards (usage, contribution, coverage, satisfaction). In 2022 the model was being simplified to be "experience-driven" rather than org-shaped | [S-L09-469] [S-L09-472] |
| Notable innovation | Layered family of systems (Foundation, then Web/Mobile, then local systems). Color "sets" that re-skin any subtree with the same role names. Figgy bot for code-to-Figma sync. Algorithmic color and layout themes | [S-L09-469] [S-L09-470] [S-L09-472] |

## Visual signature: why it looks like this
- Near-black #121212 canvas with 2 tonal lifts (#1f1f1f, #2a2a2a) and no shadows -> album art and content glow. Chrome recedes [S-L09-470].
- A single saturated accent, #1ed760 green, used for play, active and positive states -> a signature "one green light" brand on a monochrome UI [S-L09-470].
- Two text tiers only, #fff and #b3b3b3 -> strong hierarchy with minimal color [S-L09-470].
- Spotify Mix, a variable font blending sharp angles and curves, used in UI and title cuts -> a custom editorial voice that replaced Circular's geometric neutrality in 2024 [S-L09-473] [S-L09-470].
- Small radii (4-8px) on images and rows, 48px default control size, bold 2px-stroke icons at 24px -> touch-friendly, chunky controls with crisp tiles [S-L09-470] [S-L09-474].
- Short productive motion (50-300ms, (0.3,0,0,1)) -> snappy media controls, no bounce [S-L09-470].

## Recent changes 2024-2026
- 2022-01: icon refresh by Encore Foundation. Main 24px icons go from 1px to 2px stroke; 16px icons get 1.5px; 220+ icons in 5 sizes reduced to 2 sizes [S-L09-474].
- 2022-12: "Three years on" post. Semantic token layers, Figgy bot, a new mobile component team, and a plan to evolve the layered model in 2023 [S-L09-472].
- 2023-03 and 2023-05: Spotify Engineering posts "Encore x Accessibility" (screen-reader practice, expert-led) and "Multiple Layers of Abstraction" (config / slots / custom API pattern for Encore Web) [S-L09-490] [S-L09-489].
- 2024-05-22: Spotify Mix typeface launched (Dinamo), rolling out first to Latin scripts and Vietnamese [S-L09-473].
- By 2026-09: the web player ships `SpotifyMixUI` stacks with per-script cuts, and device-size layout themes. These look like the "layout and spacing themes" algorithm promised in 2022 [S-L09-470] [S-L09-472] [inferred: link between the two].
- By 2026-09: spotify.design redirects to open.spotify.com. The design blog is offline [S-L09-468].

## Builder takeaways
- Offer "color sets" (scoped palettes with identical role names) so a user can flip a card, banner or subtree to negative, announcement or inverted without new tokens [S-L09-470].
- Support responsive token values: the same token name with different values per device class (Encore's small vs medium spacing and type) [S-L09-470].
- Warn users early that non-semantic tokens do not scale. Encore could not safely change Spotify Green until it added semantic layers [S-L09-472].
- Ask whether the system is one system or a family. Encore's lesson: local systems drift toward org charts [S-L09-472].

## Gaps / unverified
- Everything internal is not public: the Encore docs site, component inventory, mobile tokens, version history and governance documents.
- The web-player token grouping, the component list and pill-button radius are inferred from shipped CSS, not from documentation.
- Spotify Design articles were read from Wayback copies because the live domain is gone. The Encore intro date conflicts: 2019-12-16 (original URL) vs "September 2020" (migrated page).
- Light-theme usage in the product (where Spotify shows it) was not verified.
- No 2025-2026 official Encore update was found. WebSearch quota was exhausted, so newer posts may exist on the engineering blog.
