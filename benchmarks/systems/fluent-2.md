# Microsoft Fluent 2

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Microsoft (Fluent design system, fluent2.microsoft.design; code in github.com/microsoft/fluentui*) | [S-L09-192] [S-L09-198] |
| Launch and major versions | Fluent Design System announced 2017-05-11 (Build); Fluent UI React v9 GA 9.0.0 on 2022-06-28; fluent2.microsoft.design first archived 2023-05-23; Fluent Web Components 3.0.0 stable 2026-06-29 | [S-L09-165] (Tier C) [S-L09-183] [S-L09-166] |
| Current version (Sept 2026) | @fluentui/react-components 9.74.8 (2026-09-21); @fluentui/web-components 3.1.3 (2026-08-25); @fluentui/tokens 1.0.0-alpha.24 (2026-08-11); legacy v8 @fluentui/react 8.125.7 (2026-06-30) | [S-L09-183] |
| Platforms | Web (React v9, Web Components v3, Blazor), iOS and macOS (fluentui-apple, UIKit/AppKit), Android (fluentui-android), Windows (WinUI 3), Figma | [S-L09-198] [S-L09-196] |
| Open source + license | Yes. MIT (fluentui LICENSE file and npm; fluentui-apple, -android, -blazor, -contrib, system icons, WinUI all MIT) | [S-L09-183] [S-L09-198] |
| Code frameworks | React (v9 primary, v8 maintained), Web Components v3, Blazor, UIKit/AppKit, Android, WinUI/XAML; motion via Web Animations API (@fluentui/react-motion) | [S-L09-198] [S-L09-139] |
| Figma kit | Official Fluent 2 Web, iOS and Android UI kits by @microsoft. 4 tiers: Fluent 2 design language (Figma variables for color, stroke, radius, spacing, size; light/dark; Fluent + Copilot), Core kits, Copilot UI kits, Labs kits. Variables: yes | [S-L09-197] |
| Token tiers + naming | 2 tiers: global (raw) and alias (semantic); camelCase, roughly `category + role + variant + state` [inferred from names]. Global: `borderRadiusMedium` 4px, `fontSizeBase300` 14px, `durationNormal` 200ms, `curveEasyEase`. Alias: `colorNeutralBackground1`, `colorBrandBackground`, `colorNeutralForeground1`, `shadow16` | [S-L09-192] [S-L09-171] [S-L09-173] [S-L09-187] |
| Color model | sRGB hex. Brand ramp 16 steps 10-160 (brandWeb 80 = #0f6cbd); neutral grey ramp 50 steps (2-98 by 2, plus 99); ~52 shared named colors, each shade50..primary..tint60. 184 alias color tokens in the light theme (117 Neutral, 36 Brand, 11 Subtle, 9 Compound, 7 Transparent, others). Accent: pass one 16-step brand ramp to `createLightTheme` / `createDarkTheme` | [S-L09-178] [S-L09-188] [S-L09-187] [S-L09-170] |
| Typeface | Segoe UI (web), Segoe UI Variable (Windows), SF Pro (iOS, macOS), Roboto (Android); mono Consolas; numeric Bahnschrift; Teams stack starts with -apple-system / system-ui. All system fonts | [S-L09-185] [S-L09-173] [S-L09-170] |
| Type scale | Web tokens: 17 styles, caption2 10/14 to display 68/92; body1 = 14/20 (fontSizeBase300 / lineHeightBase300). Sizes 10, 12, 14, 16, 20, 24, 28, 32, 40, 68; line heights 14, 16, 20, 22, 28, 32, 36, 40, 52, 92. Weights 400/500/600/700. Windows ramp: 8 styles (Caption 12/16 .. Display 68/92). Hand-tuned, per-platform ramps (iOS body 17/22pt, Android body 16/24sp) | [S-L09-177] [S-L09-173] [S-L09-185] |
| Spacing | 4px base. React tokens: none 0, XXS 2, XS 4, SNudge 6, S 8, MNudge 10, M 12, L 16, XL 20, XXL 24, XXXL 32 (separate horizontal and vertical sets). Design-language size ramp: size20..size560 = 2, 4, 6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 48, 52, 56 | [S-L09-172] [S-L09-190] |
| Radius | Tokens: None 0, Small 2, Medium 4, Large 6, XLarge 8, 2XLarge 12, 3XLarge 16, 4XLarge 24, 5XLarge 32, 6XLarge 40, Circular 10000px. Default control radius 4px; elements under 32px use 2px. Windows 11: 4px controls, 8px windows/flyouts/dialogs, 0 when snapped | [S-L09-171] [S-L09-191] [S-L09-137] |
| Elevation | Dual shadows. shadow2/4/8/16/28/64 = ambient `0 0 2px` (8px for 28 and 64) + key `0 {n/2}px {n}px`. Light: ambient rgba(0,0,0,.12), key .14; dark: .24 / .28; brand shadows .30 / .25. Windows swaps key shadows for strokes and uses Mica, Acrylic, Smoke materials | [S-L09-179] [S-L09-187] [S-L09-186] [S-L09-138] |
| Motion | Durations: ultraFast 50, faster 100, fast 150, normal 200, gentle 250, slow 300, slower 400, ultraSlow 500 ms. Curves: easyEase (0.33,0,0.67,1), easyEaseMax (0.8,0,0.2,1), decelerateMax (0.1,0.9,0.2,1), decelerateMid (0,0,0,1), decelerateMin (0.33,0,0.1,1), accelerateMax (0.9,0.1,1,0.2), accelerateMid (1,0,1,1), accelerateMin (0.8,0,0.78,1), linear. No spring tokens. Reduced motion: react-motion honours prefers-reduced-motion with per-animation overrides; guidance asks for a "no motion" setting | [S-L09-175] [S-L09-174] [S-L09-139] [S-L09-189] |
| Theming + modes | webLightTheme, webDarkTheme, teamsLightTheme, teamsDarkTheme, teamsHighContrastTheme, teamsLightV21Theme, teamsDarkV21Theme; brand ramps Web, Teams, Office, TeamsV21; generators for light, dark, high contrast, Teams dark. Applied via FluentProvider [inferred from package list] | [S-L09-170] [S-L09-178] [S-L09-181] [S-L09-184] |
| Component count | 47 component packages in @fluentui/react-components (57 re-exports minus 10 infra packages), matching 47 web React pages on fluent2.microsoft.design; plus 5 preview packages. Site also lists 12 iOS and 5 Android component pages (2026-09-23) | [S-L09-184] [S-L09-196] |
| Component doc structure | Preview (live, CodeSandbox), Resources (Storybook, React and Web Components guidance, WAI pattern), Behavior, Layout, Accessibility, Content; API docs in Storybook | [S-L09-196] |
| Accessibility stance | Components "meet or surpass WCAG 2.1 AA": 4.5:1 text, 3:1 large text (18.5px bold / 24px regular) and non-text; global palette includes high-contrast system colors (hcCanvas, hcHighlight, hcButtonFace, hcHyperlink) for HC themes; touch targets 44x44 web/iOS, 48x48 Android | [S-L09-193] [S-L09-188] [S-L09-190] |
| Governance / contribution | Open monorepo with per-PR change files; fluentui-contrib monorepo for contributor extension packages; "-preview" packages before stable; partner-led Labs UI kits in Figma | [S-L09-180] [S-L09-198] [S-L09-197] |
| Notable innovation | One design language with native ramps per platform (web, Windows, iOS, macOS, Android); key + ambient dual shadow ramp; one brand ramp generates full light/dark/HC themes; 2026 headless React primitives for teams building their own design systems | [S-L09-185] [S-L09-179] [S-L09-170] [S-L09-199] |

## Visual signature: why it looks like this
- 4px default radius (2px under 32px, 8px on overlays) -> tight, businesslike, "productivity app" corners [S-L09-171] [S-L09-191].
- Segoe UI at 14/20 body with semibold (600) titles -> compact, dense Office/Teams text rhythm [S-L09-177] [S-L09-173].
- Near-neutral surfaces (white, #fafafa, #f5f5f5; dark #292929) with one blue brand (#0f6cbd) -> mostly gray canvas with a single cool accent [S-L09-187] [S-L09-178].
- Two-part shadows (2px ambient halo + directional key) at low opacity (.12 / .14) -> soft lift that reads well on light gray [S-L09-179] [S-L09-187].
- Short durations (100-300ms) on easyEase and decelerate curves, no springs -> quick, restrained, non-bouncy motion [S-L09-175] [S-L09-174].
- On Windows, Mica and Acrylic plus strokes instead of key shadows -> wallpaper-tinted, layered desktop look [S-L09-138] [S-L09-186].

## Recent changes 2024-2026
- 2025-07-29: new Teams brand ramp (brandTeamsV21) and teamsLightV21 / teamsDarkV21 themes, described as the v3 variant of Teams themes [S-L09-181] [S-L09-178].
- 2026-01-22: "CAP DR" token update: radius 2XLarge-6XLarge (12-40px) added and rest/hover/pressed/selected state color tokens across web light, dark, high contrast and Teams dark [S-L09-180] [S-L09-171].
- 2026-02-19: Windows 11 geometry guidance updated (4px / 8px / 0px radii, ControlCornerRadius, OverlayCornerRadius) [S-L09-137].
- 2026-04-27: @fluentui/react-headless-components-preview first published: unstyled v9 primitives with a data-* state contract for custom design systems [S-L09-199].
- 2026-06-29: Fluent Web Components 3.0.0 stable; 3.1.3 by 2026-08-25 [S-L09-183].
- Undated (live 2026): Figma kits reorganised into design language, Core, Copilot and Labs tiers; variables now style Fluent and Copilot assets [S-L09-197].
- 2026-08-11: @fluentui/tokens reaches 1.0.0-alpha.24 as a standalone token package [S-L09-183].
- 2026-09-21: @fluentui/react-components 9.74.8 [S-L09-183].

## Builder takeaways
- Copy the "one brand ramp in, full theme out" API: 16 brand steps generate light, dark and high-contrast alias sets [S-L09-170] [S-L09-178].
- Offer a dual-shadow elevation preset (ambient + key, 6 levels) with separate light and dark opacities [S-L09-179] [S-L09-187].
- Support per-platform type ramps under shared role names (Body 1 is 14px on web, 17pt on iOS, 16sp on Android) [S-L09-185].
- Offer a headless tier so teams can keep behaviour and accessibility while replacing visuals, as Fluent now does [S-L09-199].

## Gaps / unverified
- Conflict: the Fluent 2 shapes page lists Large 8px and X-Large 12px, but code tokens are Large 6px, XLarge 8px, 2XLarge 12px [S-L09-191] [S-L09-171].
- Conflict: the typography page shows Subtitle 1 at 20/26, but tokens give 20/28 (lineHeightBase500) [S-L09-185] [S-L09-173].
- Stale comments in lightColor.ts say brand[80] is #0078d4; the actual brandWeb[80] value is #0f6cbd [S-L09-187] [S-L09-178].
- "CAP DR" is not defined in the public PR; the source repo (fluentui-design-tokens) is private [S-L09-180] [S-L09-182].
- Fluent 2 site launch date is inferred from the first web-archive capture (2023-05-23), not an announcement [S-L09-166].
- iOS and Android component coverage on the Fluent 2 site (12 and 5 pages) is far smaller than web (47); native libraries may contain more controls than the site documents [S-L09-196].
- Stroke widths differ by platform on the shapes page: web 1/2/3/4 px, mobile 1/2/4/6; code tokens only carry the web set [S-L09-191] [S-L09-176].
- Figma kit dates and exact component counts in the Figma files were not checked; web search budget ran out.
