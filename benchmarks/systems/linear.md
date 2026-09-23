# Linear (public information only)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

Linear has no published design system. This file uses Linear's own blog posts and the production CSS of the public marketing site (linear.app). Marketing-site values may differ from the product app; they are labeled "site".

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Linear (the company). Redesign posts by Karri Saarinen (co-founder) and team; 2026 refresh by Charlie Aufmann and Maxime Heckel | [S-L09-652] [S-L09-654]; "co-founder" [inferred] |
| Launch and major versions | No versioned system. Public milestones: UI redesign 2024-03-28; iOS "Liquid Glass" post 2025-10-21; "calmer interface" refresh 2026-03-12; StyleX migration finished 2026-08-06 | [S-L09-652] [S-L09-653] [S-L09-654] [S-L09-655] |
| Current version (Sept 2026) | Not versioned. Current look = the March 2026 refresh, now styled with StyleX | [S-L09-654] [S-L09-655] |
| Platforms | Web app plus native apps; iOS confirmed by the Liquid Glass post. Desktop and Android not checked | [S-L09-653]; rest [inferred] |
| Open source + license | No. Proprietary; no public component library or token package | [S-L09-655]; no package [inferred] |
| Code frameworks | React. Styling moved from styled-components to StyleX (100% StyleX on 2026-08-06, 1,000+ PRs) | [S-L09-655] |
| Figma kit | Not public. Internally, token values are exported as JSON and imported into Figma with a plugin | [S-L09-654] |
| Token tiers + naming | App: themes generated from 3 inputs (base color, accent color, contrast) into "more than a hundred color variables in LCH space"; the old system needed 98 hand-set variables per theme. Site names: `--color-bg-level-0..3`, `--color-bg-primary`, `--color-border-primary`, `--color-accent` | [S-L09-652] [S-L09-655] [S-L09-656] |
| Color model | App: LCH, generated, 100+ variables; token hue, chroma and lightness tuned in an internal tool. Site dark: bg-level-0 #08090a, 1 #0f1011, 2 #141516, 3 #191a1b; border-primary #23252a; accent #7170ff (hover #828fff). 2026: grays moved from "cool, blue-ish" to "warmer", "less saturated" | [S-L09-652] [S-L09-654] [S-L09-656] |
| Typeface | App (2024): Inter Display for headings, Inter for everything else. Site: "Inter Variable" + "Berkeley Mono"; weights 400, 510, 590, 680 | [S-L09-652] [S-L09-656] |
| Type scale | App: not public. Site: text tiny 10px, micro 12, mini 13, small 14, regular 15, large 17; titles 1-9 = 17, 20, 24, 32, 40, 48, 56, 64, 72px. Regular line height 1.6; tracking -0.01em to -0.015em on small sizes | [S-L09-656] |
| Spacing | Not public. Site page padding 24px inline, 64px block | [S-L09-656] |
| Radius | App: not public (2026 tabs got "rounded corners", borders "rounding out their edges"). Site: 4, 6, 8, 12, 16, 24, 32px, 9999px | [S-L09-654] [S-L09-656] |
| Elevation | Tonal: 4 background levels in dark (#08090a to #191a1b). Site shadows low `0 1px 4px -1px #00000017`, medium `0 3px 12px #00000017`, high `0 7px 24px #0000000f` (light values) | [S-L09-656]; light/dark assignment [inferred] |
| Motion | App: not public. Site: Penner easing set, e.g. ease-out-quad (.25, .46, .45, .94), ease-out-expo (.19, 1, .22, 1); `--duration: .18s`, `--transition-duration: .1s` | [S-L09-656] |
| Theming + modes | Light, dark and custom themes from base/accent/contrast; raising contrast gives "super high-contrast themes". Nested `ThemeProvider` regenerates themes for selected rows, focus states and elevated surfaces | [S-L09-652] [S-L09-655] |
| Component count | Not public | none |
| Component doc structure | Not public (no docs site) | none |
| Accessibility stance | Contrast input exists "for accessibility reasons". No WCAG statement found | [S-L09-652] |
| Governance / contribution | In-house. The 2026 refresh was done by a two-person design team using coding agents | [S-L09-654] |
| Notable innovation | Whole themes generated from 3 inputs in a perceptual space (LCH), with contrast as a user control. Its look became a web trend ("Linear design": dark UI, gradients, glass, bold type) | [S-L09-652] [S-L09-657] |

## Visual signature: why it looks like this
- 4 near-black tonal levels (#08090a to #191a1b) instead of shadows -> deep, quiet dark UI where depth comes from lightness steps [S-L09-656].
- Inter Variable at in-between weights 510 and 590 -> crisp text that never looks bold or heavy [S-L09-656].
- Little "chrome": less blue in the theme math (2024), warmer and less saturated grays (2026) -> calm, content-first screens [S-L09-652] [S-L09-654].
- One violet-blue accent (site #7170ff) on near-black -> the signature highlight other SaaS sites copy [S-L09-656] [S-L09-657].
- Small body sizes (13-15px) with slight negative tracking -> dense, keyboard-tool feel [S-L09-656].
- Short transitions (100-180ms) with ease-out curves -> fast, quiet feedback [S-L09-656].

## Recent changes 2024-2026
- 2024-03-28: UI redesign. LCH theme generation from base/accent/contrast; Inter Display headings; denser, quieter sidebar, tabs and headers [S-L09-652].
- 2025-10-21: "A Linear Spin on Liquid Glass" (iOS; post opened only in the listing) [S-L09-653].
- 2026-03-12: "A calmer interface". Warmer, less saturated grays; dimmer sidebar; compact rounded tabs; fewer and smaller icons; softer borders [S-L09-654].
- 2026-03-08 to 2026-08-06: styled-components to StyleX; 20-35% less main-thread CPU on view-heavy pages (post 2026-08-26) [S-L09-655].

## Builder takeaways
- Offer a "generate from 3 inputs" theme mode (base, accent, contrast) in a perceptual space. The contrast control gives a high-contrast theme for free [S-L09-652].
- Offer tonal elevation (lightness steps per level) as the default dark-mode elevation preset [S-L09-656].
- Allow variable-font in-between weights (510/590) in type presets [S-L09-656].

## Gaps / unverified
- Product-app tokens (type scale, spacing, radius, motion) are not public. Site CSS is a proxy only.
- The Liquid Glass post was seen only as a title in the blog listing.
- Component count, docs structure, and any internal design system name are not public.
