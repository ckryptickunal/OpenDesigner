# L10: Platforms (mobile vs web vs unified design systems)

Lane: L10 (Platforms). Author: orchestrator subagent L10. Written 2026-09-23.
Trace: `traces/L10-trace.md` (every source, including rejected ones). Schema: `_coordination/SCHEMA.md`.
Status: complete. 25 Decision Cards, 3 comparison tables, identical-vs-adapt synthesis, questionnaire, decision graph, baked-in platform rules.

## Lane overview

A design-system builder has to ask "which platforms?" before almost anything else, because the answer changes units, type ramps, navigation components, target sizes, materials, motion, the token pipeline, and even whether the brand is allowed to restyle standard controls. This lane covers:

1. **The platforms and their 2026 design languages**: Apple's Liquid Glass across iOS, iPadOS, macOS, watchOS, tvOS and visionOS (26 in 2025, refined in 27 in 2026); Google's Material 3 and M3 Expressive across Android phones, large screens, Wear OS, TV, cars and XR; the web (no native language, but a rich set of user-preference hooks); Windows (Fluent 2 / WinUI).
2. **Platform mandates that are no longer optional**: iOS 27 SDK ignores the Liquid Glass opt-out key; Android 15 enforces edge-to-edge; Android 16 enables predictive back and ignores orientation locks on large screens; Android 17 removes that opt-out.
3. **The unified-system question**: native look vs consistent brand look, and what famous multi-platform systems actually share (tokens, components, or only principles).
4. **Delivery**: units and conversions, framework theming (SwiftUI, Compose, Flutter, React Native, Compose Multiplatform, .NET MAUI, Electron), and how tokens reach each platform (Style Dictionary formats).
5. **Platform accessibility**: text scaling, screen readers, contrast and transparency settings, target minimums, keyboard and switch access.

### Top findings (what changes the builder most)

- **Apple has closed the escape hatch.** The `UIDesignRequiresCompatibility` key kept apps on the pre-Liquid-Glass look, but "the system ignores this key when you build for iOS 27 or later" (also iPadOS, Mac Catalyst, macOS and tvOS 27) [S-L10-076]. Any system that ships native Apple apps must now design for Liquid Glass bars, controls and sheets. Apple's September 2026 branding guidance tells apps to use the accent color sparingly and to "consider moving it into the content layer, where it scrolls beneath Liquid Glass controls" [S-L10-009]. Brand expression on Apple is moving out of the chrome and into content.
- **Android is now Compose-first and adaptive by force.** Google says "Android is now Compose First; Views are now in maintenance mode" [S-L10-002]. Edge-to-edge is enforced at target SDK 35 and the opt-out is disabled at 36 [S-L10-023, S-L10-020]. Orientation and resizability locks are ignored on displays 600dp or wider at 36, with no opt-out at 37 [S-L10-020, S-L10-021]. M3 Expressive components are graduating to stable inside the Compose Material 3 1.5.0 alphas (1.4.0 is still the latest stable) [S-L10-018].
- **Unified systems converge on "shared foundations, native chrome".** Fluent reuses "native platform components and patterns 80% of the time" and spends its effort on "signature experiences" (color, sound, illustration, icons) [S-L10-038]. Spotify calls cohesion "the middle path between perfect consistency and total platform independence" [S-L10-040]. Airbnb wants to be "clearly recognizable as Airbnb, no matter the platform" while following conventions for "navigation, system iconography, contextual actions, and interactions" [S-L10-044]. Fluent's type ramp shows the pattern concretely: the role names are shared, but the values and typefaces differ. Body 1 is 14/20px Segoe UI on web, 17/22pt SF Pro on iOS and 16/24sp Roboto on Android [S-L10-039].
- **Units look alike but scale differently.** Apple pt, Android dp and Windows epx all normalize for density [S-L10-087, S-L10-070, S-L10-069]. Text scaling is where they diverge. iOS Dynamic Type takes Body from 17pt to 53pt at AX5 [S-L10-011]. Android sp scales nonlinearly up to 200%, so 4sp + 20sp does not equal 24sp [S-L10-071]. Web rem follows the user's browser font size, while px does not [S-L10-074]. macOS has no Dynamic Type [S-L10-011]. A single "font size" token therefore needs a scaling policy per platform, not only a value.
- **Target minimums differ per platform and must be tokens, not constants.** iOS/iPadOS 44x44pt default (28 minimum), macOS 28x28 (20), tvOS 66x66 (56), visionOS 60x60 (28), watchOS 44x44 (28) [S-L10-012]. Android 48x48dp [S-L10-072]. Web 24x24 CSS px at WCAG 2.2 AA, 44x44 at AAA [S-L10-036].

### Comparison table A: platforms at a glance (2026)

| Platform | Design language (Sept 2026) | Default / min text | Default target | Unit | Text scaling | Primary navigation | Surfaces / materials | Appearance modes | What makes an app feel native |
|---|---|---|---|---|---|---|---|---|---|
| iOS | Liquid Glass (iOS 26, refined in 27: better diffusion, darkened edges, transparency slider) [S-L10-005, S-L10-003, S-L10-004] | 17pt / 11pt [S-L10-011] | 44x44pt (min 28) [S-L10-012] | pt (@2x, @3x) [S-L10-087] | Dynamic Type xSmall to xxxLarge plus AX1-AX5 [S-L10-011] | Floating glass tab bar that can minimize on scroll; navigation stack; sheets with medium/large detents [S-L10-014] | Liquid Glass (regular, clear) for controls; 4 standard materials for content [S-L10-008] | Light, dark, increased contrast; icons default/dark/clear/tinted [S-L10-010, S-L10-075] | Standard components, safe areas, swipe back, Dynamic Type, SF Symbols, controls mid/bottom for reach [S-L10-015] |
| iPadOS | Liquid Glass; iPadOS 26 adds a windowing system and a menu bar [S-L10-085] | 17pt / 11pt [S-L10-011] | 44x44pt [S-L10-012] | pt (@2x) [S-L10-087] | Dynamic Type [S-L10-011] | Tab bar near the top, convertible to a sidebar (`sidebarAdaptable`) [S-L10-014] | Glass sidebars float over content [S-L10-014] | As iOS | Size classes not device type; pointer, keyboard, Pencil; resizable windows [S-L10-013, S-L10-015] |
| macOS | Liquid Glass (Tahoe 26, then 27); transparent menu bar [S-L10-005] | 13pt / 10pt [S-L10-011] | 28x28pt (min 20) [S-L10-012] | pt (@1x, @2x) [S-L10-087] | None (no Dynamic Type) [S-L10-011] | Menu bar + toolbar + sidebar [S-L10-015] | Liquid Glass + vibrancy materials, behind-window blending [S-L10-008] | Light, dark; user accent overrides app accent unless set to multicolor [S-L10-010] | Menu bar holds every command; keyboard shortcuts; resizable windows; customizable toolbars [S-L10-015] |
| watchOS | Liquid Glass, minimal changes [S-L10-075] | 16pt / 12pt [S-L10-011] | 44x44pt (min 28) [S-L10-012] | pt (@2x) [S-L10-087] | Dynamic Type; enlarge 140% [S-L10-012] | Shallow hierarchy, Digital Crown vertical navigation [S-L10-015] | Materials in full-screen modals [S-L10-008] | Tinted complications option [S-L10-010] | Glanceable single screens, complications, notifications [S-L10-015] |
| visionOS | Unmodifiable window "glass" [S-L10-008] | 17pt / 12pt [S-L10-011] | 60x60pt (min 28) [S-L10-012] | pt as an angular unit [S-L10-087] | Dynamic Type [S-L10-011] | Windows, volumes, ornaments; immersion levels [S-L10-015] | Glass that adapts to surroundings [S-L10-008] | No Dark Mode setting [S-L10-008] | Minimum immersion needed, content in field of view, indirect gestures [S-L10-015] |
| tvOS | Liquid Glass on focused elements and navigation [S-L10-008] | 29pt / 23pt [S-L10-011] | 66x66pt (min 56) [S-L10-012] | pt (@1x, @2x) [S-L10-087] | Dynamic Type [S-L10-011] | Focus system, Siri Remote [S-L10-015] | Standard materials ultraThin to thick by use [S-L10-008] | Light, dark [S-L10-010] | Safe area 60pt top/bottom, 80pt sides; 8+ ft viewing [S-L10-013, S-L10-015] |
| Android phone | Material 3; M3 Expressive rolling into Compose (1.5.0 alphas) [S-L10-018] | bodyLarge 16sp, bodyMedium 14sp [S-L10-019] | 48x48dp [S-L10-072] | dp and sp (px = dp x dpi/160) [S-L10-070] | Font scale to 200%, nonlinear (Android 14+) [S-L10-071] | Navigation bar (bottom) at compact width [S-L10-025] | Tonal surfaces (color roles), not blur [S-L10-019] | Light, dark, dynamic color (Android 12+), contrast levels [S-L10-019] | Edge-to-edge, predictive back, dynamic color, Material components [S-L10-023, S-L10-020] |
| Android large screen / foldable / desktop | Material breakpoints (renamed from window size classes) [S-L10-025] | as phone | 48x48dp | dp | as phone | Collapsed or expanded navigation rail; 1-3 panes [S-L10-025] | as phone | as phone | Fill any window; locks ignored at 600dp+ [S-L10-020, S-L10-021] |
| Wear OS | M3 Expressive via Wear Compose Material 3 [S-L10-026] | Wear type scale incl. arc text [S-L10-027] | not stated on page read | dp | not stated on page read | Scrolling lists, edge buttons [S-L10-026] | Black backgrounds [S-L10-027] | Dynamic color from watch face [S-L10-027] | EdgeButton, round-screen containers, shape morphing [S-L10-026, S-L10-027] |
| Web | No native language; user-preference media features [S-L10-031, S-L10-033] | 16px browser default root, user-changeable [S-L10-074] | 24x24 CSS px AA, 44x44 AAA [S-L10-036] | CSS px (1/96 in), rem, em [S-L10-074] | Browser font size (rem) and zoom [S-L10-074] | Site-defined | Site-defined; `prefers-reduced-transparency` not Baseline [S-L10-032] | `prefers-color-scheme`, `prefers-contrast`, `forced-colors` [S-L10-031, S-L10-033] | Keyboard access, visible and unobscured focus, responsive reflow [S-L10-083] |
| Windows | Fluent 2 / WinUI [S-L10-037] | Body 14/20 epx, Segoe UI Variable [S-L10-039] | not stated on pages read | epx, multiples of 4 [S-L10-069] | OS scale 100-400% [S-L10-069] | App-defined; NavigationView [inferred] | Mica (window base), Acrylic (transient), Smoke (modal dim) [S-L10-066] | Light, dark, high contrast [S-L10-039] | 4px control radius, 8px overlay radius; 0 when snapped [S-L10-067] |

### Comparison table B: units and conversions

| Unit | Platform | Definition | Scales with user text size? | Notes |
|---|---|---|---|---|
| pt (point) | Apple | Abstract unit. @1x = 1px per pt; @2x and @3x on high-density screens [S-L10-087] | Only through Dynamic Type text styles [S-L10-011] | In visionOS a point is an angular value, so size depends on distance [S-L10-087] |
| dp | Android | Density-independent pixel; px = dp x (dpi / 160); mdpi 160 dpi baseline; buckets ldpi 120, hdpi 240, xhdpi 320, xxhdpi 480, xxxhdpi 640 [S-L10-070] | No | Use for layout only [S-L10-070] |
| sp | Android | Same as dp by default, resized by the user's text size [S-L10-070] | Yes, nonlinear to 200% [S-L10-071] | Never use sp for layout; line height should be in sp too [S-L10-070, S-L10-071] |
| epx | Windows | Effective pixel accounting for density and viewing distance; plateaus 100%-400% [S-L10-069] | Through OS scale | A 1080p TV is about 540 epx [S-L10-069] |
| CSS px | Web | 1/96 inch reference pixel [S-L10-074] | No (zoom only) | Fixed; avoid for font-size [S-L10-074] |
| rem | Web | Root font size, 16px in most browsers by default [S-L10-074] | Yes | Tailwind v4 base spacing is 0.25rem (L03 [S-L03-017]) |

Conversion rule the builder can use [inferred from S-L10-057, S-L10-074, S-L10-087, S-L10-070]: author dimension tokens once in a platform-neutral number, then emit 1 unit = 1pt = 1dp = 1epx = 1 CSS px, and 16 units = 1rem on web. Style Dictionary's built-in transforms assume a base font size of 16 when converting rem to dp, sp, pt or CGFloat [S-L10-057]. The fact that 1pt, 1dp and 1 CSS px are "the same number" is a convention rather than a physical identity, but every multi-platform system checked uses it. Fluent states its spacing ramp "abide[s] by the native platform scaling": pt on iOS, dp on Android, px on web, with the same numbers [S-L10-039].

### Comparison table C: text defaults and text scaling

| Platform | Body default | Scale mechanism | Largest setting | Custom font requirement |
|---|---|---|---|---|
| iOS / iPadOS | Body 17/22pt (Large, the default) [S-L10-011] | Dynamic Type text styles (Large Title 34 ... Caption 2 11 at default) [S-L10-011] | AX5: Body 53/62pt, Large Title 60/70 [S-L10-011] | Must implement Dynamic Type and Bold Text [S-L10-011]; aim to support 200% enlargement [S-L10-012] |
| macOS | Body 13/16pt [S-L10-011] | None [S-L10-011] | n/a | Legible at 10pt minimum [S-L10-011] |
| watchOS | 16pt [S-L10-011] | Dynamic Type | 140% target [S-L10-012] | As iOS |
| Android | bodyLarge 16/24sp (M3 Compose defaults) [S-L10-019] | sp x user font scale, nonlinear [S-L10-071] | 200% [S-L10-071] | Text sizes in sp; don't hard-code fontScale math [S-L10-071] |
| Web | 16px root [S-L10-074] | rem/em follow the browser setting [S-L10-074] | WCAG 1.4.4 asks for 200% text resize [inferred; L02 owns] | Use rem for font-size [S-L10-074] |
| Windows | Body 14/20 epx [S-L10-039] | OS text and display scale [S-L10-069] | 400% display plateau [S-L10-069] | n/a |

## Decision Cards

### DC-L10-01: Target platforms and form factors
- **Block path:** Platforms > Scope > Target platforms
- **Questions the designer answers:** Which platforms ship first: web, iOS, Android, desktop, or all? Phones only, or tablets, foldables and desktops too? Do watches, TVs, cars or headsets matter now or later?
- **Options:**
  - **Web only.** One delivery layer (CSS custom properties). Responsive plus user-preference media features [S-L10-031, S-L10-033]. Examples: Polaris, which calls Shopify's platform "the web platform" [S-L10-047].
  - **Mobile native (iOS + Android).** Two design languages (Liquid Glass, Material 3), two units (pt, dp/sp), two text-scaling models [S-L10-011, S-L10-071].
  - **Web + mobile native.** The common case for consumer products. Uber Base ships to 7 stacks: UIKit, SwiftUI, Android XML, Compose, Web React, Go, and server-driven UI [S-L10-046].
  - **Everything, including desktop and secondary form factors.** Spotify's Encore spans mobile, web, desktop, TV and watch through a shared foundation and platform subsystems [S-L10-040]. Fluent covers Web, Windows, iOS and Android [S-L10-037].
  - **Size coverage within a platform.** Android now forces large-screen support: at target SDK 36, orientation, resizability and aspect-ratio restrictions are ignored on displays 600dp or wider, and the opt-out goes away at SDK 37 [S-L10-020, S-L10-021]. Apple asks apps to support arbitrary window sizes on iPad and Mac [S-L10-075].
- **Visual effect:** Each added platform adds a set of conventions the brand must coexist with. Web-only systems can express the brand through every pixel. Native systems give up bar, control and sheet styling to the OS [S-L10-008, S-L10-075]. Adding large screens adds panes, navigation rails and sidebars, which change the product's silhouette [S-L10-025].
- **Depends on (upstream):** business model and audience (outside the design system); team skills and framework choice (DC-L10-21).
- **Affects (downstream):** every other card in this lane; unit transforms (DC-L10-08); navigation set (DC-L10-09); breakpoint set (DC-L10-10); token pipeline outputs (DC-L10-22).
- **Token encoding:** a platform dimension in the token resolver, e.g. DTCG modifier or Figma mode `platform = web | ios | android | windows` [inferred; L07 owns resolver syntax]. Tokens that vary by platform: `font.family.*`, `size.target.min`, `type.*.size`, `motion.*`, `radius.control` [inferred].
- **Platform notes:** Android's large-screen mandate means "phone-only Android" is no longer a real option for new apps [S-L10-021]. Apple still distinguishes idiom (device type) from size class, and asks layouts to follow size class [S-L10-013].
- **Accessibility constraints:** each platform brings its own assistive technology set (VoiceOver, TalkBack, Switch Control, Switch Access, Full Keyboard Access, forced colors), so each added platform adds a test matrix [S-L10-012, S-L10-072, S-L10-031].
- **Default + heuristic:** Default to web + iOS + Android phones, with Android and iPad large-screen layouts from day one. Add desktop, watch or TV only with a named use case. Rule of thumb: list platforms by where users spend time, then add any form factor the OS forces on you (Android 600dp+, resizable iPad windows).
- **Evidence:** [S-L10-020, S-L10-021, S-L10-025, S-L10-037, S-L10-040, S-L10-046, S-L10-047, S-L10-075]

### DC-L10-02: Platform posture: native-first, brand-first, or coherent hybrid
- **Block path:** Platforms > Strategy > Native vs brand posture
- **Questions the designer answers:** Should our iOS app look like an iOS app, or like our brand? Where may the brand override platform conventions? How recognizable must we be across platforms?
- **Options:**
  - **Native-first.** Use system components and styling almost everywhere. Brand shows in content, color accents, imagery and voice. Apple's guidance: "Express your brand with familiar components", keep "sizing, placement, and behavior" familiar, and don't show your logo throughout [S-L10-009]. Google told iOS developers to use UIKit/SwiftUI rather than Material components on iOS, since MDC-iOS entered maintenance mode on 2021-07-15 [S-L10-082].
  - **Coherent hybrid (most multi-platform systems).** Shared foundations and signature moments, native navigation and controls. Fluent: reuse native patterns "80% of the time" and focus on "signature experiences" [S-L10-038]. Spotify: cohesion as "the middle path" [S-L10-040]. Airbnb: recognizable everywhere, but follows conventions on navigation, system iconography, contextual actions and interactions [S-L10-044].
  - **Brand-first (one look everywhere).** The same custom components on every platform, typically through Flutter or a custom React Native kit [inferred]. Airbnb leaned this way on some structural choices, for example replacing Android's left navigation drawer with the bottom bar used on iOS [S-L10-044].
- **Visual effect:** Native-first apps feel "at home" and inherit OS updates for free: rebuilding with the latest Xcode adopts Liquid Glass automatically [S-L10-075]. But they look more like other apps on the device. Brand-first apps look identical across devices and can feel foreign: wrong back gestures, wrong sheet shapes, bars that don't blur [inferred]. They also must re-implement every OS change themselves. The hybrid looks branded in color, type, imagery, iconography and motion personality, and native in chrome.
- **Depends on (upstream):** DC-L10-01 (platforms); brand strength and distinctiveness (L06).
- **Affects (downstream):** DC-L10-03 (what to share), DC-L10-04 (brand color placement), DC-L10-06 (typefaces), DC-L10-12 (controls), DC-L10-13 (motion), DC-L10-21 (framework).
- **Token encoding:** posture is a system-level setting, not a token. It decides which tokens have platform overrides. A native-first system maps semantic tokens to platform semantics, e.g. `color.text.primary` becomes `label` on iOS and `onSurface` on Android [inferred from S-L10-010, S-L10-019]. A brand-first system emits literal values everywhere.
- **Platform notes:** Apple has removed the opt-out from the new design at the 27 SDKs [S-L10-076], so "brand-first" chrome on iOS now means building custom bars and controls, which Apple warns can "interfere with Liquid Glass" and scroll edge effects [S-L10-075]. Android has no equivalent mandate for Material styling, but platform behaviors (edge-to-edge, predictive back) are mandatory regardless of look [S-L10-020].
- **Accessibility constraints:** system components carry VoiceOver/TalkBack semantics, Dynamic Type and contrast adaptations by default [S-L10-015, S-L10-072]. Custom components must re-implement them.
- **Default + heuristic:** Default to the coherent hybrid. Rule of thumb: share anything the user perceives as "the brand" (color accents, type personality in headlines, illustration, iconography style, voice, sound), and adopt the platform's version of anything the user perceives as "how the phone works" (navigation, back, sheets, pickers, text fields, system icons).
- **Evidence:** [S-L10-009, S-L10-020, S-L10-038, S-L10-040, S-L10-044, S-L10-075, S-L10-076, S-L10-082]

### DC-L10-03: What is shared across platforms: tokens, components, or principles
- **Block path:** Platforms > Architecture > Sharing layer
- **Questions the designer answers:** Do platforms share only design tokens, or the same component specs, or the same component code? Is there one spec per component or one per platform?
- **Options (real systems):**
  - **Shared principles only.** Loosest. Each platform has its own system aligned by principles (Fluent's four principles apply across products) [S-L10-038].
  - **Shared foundation tokens, platform component subsystems.** Spotify Encore: the Foundation holds color, type styles, motion and spacing tokens and is "the minimum bar" for every product; Web and Mobile subsystems build their own components on it [S-L10-040, S-L10-041]. Fluent: global and alias tokens, with components per platform [S-L10-039].
  - **Shared component specs, per-platform implementations.** Uber Base: "each component spec serves as the single reference" for all 7 stacks, including VoiceOver, TalkBack and ARIA specs [S-L10-046].
  - **Shared component API, host-rendered.** Shopify Polaris web components keep "familiar APIs, props, and values" across Admin, Checkout and Customer Accounts, using "a different design system when needed" [S-L10-047]. In the POS app on iOS and Android they render as "native UI elements" [S-L10-048].
  - **Shared component code.** Flutter, Compose Multiplatform, React Native with a custom kit: one implementation renders on every platform [S-L10-055, S-L10-059] [inferred for RN].
- **Visual effect:** The more is shared, the more identical the product looks across platforms, and the less it looks native. Token-only sharing gives same colors, type personality and spacing rhythm with platform-shaped components. Shared code gives identical components [inferred].
- **Depends on (upstream):** DC-L10-02 (posture), DC-L10-21 (framework).
- **Affects (downstream):** documentation structure (L11), token tiers (L07), the component inventory (L08), DC-L10-22 (pipeline).
- **Token encoding:** a three-tier token set where primitives and most semantics are shared, and platform overrides live at the semantic or component tier [inferred]. Fluent names its two tiers "global" (raw values) and "alias" (semantic) [S-L10-039]. Atlassian's naming is foundation + property + modifier [S-L10-050].
- **Platform notes:** Salesforce coined "design tokens" around 2014 precisely to push one set of decisions to web and native [S-L10-053]. On web it has since moved to CSS custom properties ("global styling hooks") in SLDS 2 [S-L10-052].
- **Accessibility constraints:** a shared component spec should carry per-platform screen-reader specs, as Uber's does [S-L10-046].
- **Default + heuristic:** Default to shared tokens and shared component specs (anatomy, variants, states, content rules), with per-platform implementation and per-platform accessibility notes. Rule of thumb: share the "what" (decision, name, intent) everywhere; let the "how" (control rendering, gesture) be platform code.
- **Evidence:** [S-L10-039, S-L10-040, S-L10-041, S-L10-046, S-L10-047, S-L10-048, S-L10-050, S-L10-052, S-L10-053, S-L10-055, S-L10-059]

### DC-L10-04: Brand color placement per platform
- **Block path:** Foundations > Color > Brand accent > Platform application
- **Questions the designer answers:** Where does our brand color appear on each platform: controls, bars, backgrounds, or content? Does it tint the navigation chrome?
- **Options:**
  - **Apple (Liquid Glass era).** Accent "judiciously": primary actions, status indicators, the selected tab icon, unread badges. Or move brand color "into the content layer, where it scrolls beneath Liquid Glass controls and gets picked up dynamically" [S-L10-009]. Liquid Glass "has no inherent color". Tinting it gives a "stained glass" look reserved for the primary call to action, and the accent goes on the background of prominent buttons, not on glyphs [S-L10-010]. Small bars (toolbars, tab bars) turn light or dark monochrome depending on content beneath [S-L10-010].
  - **macOS.** The app accent applies only when the user's system accent is "multicolor". Otherwise the user's accent replaces yours, except fixed-color sidebar icons [S-L10-010].
  - **Android / Material 3.** Brand color is a source color that generates tonal palettes and roles (primary, secondary, tertiary, containers) [S-L10-019]. With dynamic color on (Android 12+), the wallpaper replaces it [S-L10-019].
  - **Windows.** Mica tints surfaces with the user's desktop color [S-L10-066]. Fluent tokens support "branded" themes alongside light, dark and high contrast [S-L10-039].
  - **Web.** No platform constraint. The brand can tint anything, bounded only by contrast rules (L01).
- **Visual effect:** On iOS 26/27 a heavily tinted nav bar now reads as dated or "fighting the glass". The Apple-endorsed look is neutral glass chrome over colorful content [S-L10-009, S-L10-010]. On Android a brand-colored top app bar and FAB remain idiomatic Material [inferred]. On web the brand can fill headers.
- **Depends on (upstream):** DC-L10-02 (posture), L01 brand palette, DC-L10-05 (dynamic color policy).
- **Affects (downstream):** button fill tokens, tab/nav indicator tokens, app bar tokens, badge tokens, link color.
- **Token encoding:** `color.brand.accent` (shared) mapped to `color.action.primary.bg` with platform overrides; on iOS set as the asset-catalog AccentColor; on Android as the `primary` seed; on macOS as app accent with a "respect user accent" flag [inferred from S-L10-010, S-L10-019].
- **Platform notes:** see options. On visionOS, glass windows limit background color information [S-L10-008].
- **Accessibility constraints:** Apple's minimum contrast is 4.5:1 up to 17pt and 3:1 at 18pt or bold [S-L10-012]; Android's is 4.5:1 for small text and 3:1 for large [S-L10-072]. A 35% dark dimming layer behind clear glass over bright content is recommended [S-L10-008].
- **Default + heuristic:** Default to accent-on-actions and brand-in-content on Apple, a brand seed on Android (with a dynamic-color decision), and freer use on web. Rule of thumb: if the brand color would sit behind navigation text on Apple, move it into the content instead.
- **Evidence:** [S-L10-008, S-L10-009, S-L10-010, S-L10-012, S-L10-019, S-L10-039, S-L10-066, S-L10-072]

### DC-L10-05: User personalization vs fixed brand (dynamic color, accent, glass look)
- **Block path:** Foundations > Color > Personalization policy
- **Questions the designer answers:** If the OS offers user-chosen colors or looks, do we follow them, ignore them, or offer our own? Is our brand color allowed to yield?
- **Options:**
  - **Follow the OS.** Android dynamic color: `dynamicLightColorScheme` / `dynamicDarkColorScheme` on API 31+ [S-L10-019]. Wear OS derives color from the watch face [S-L10-027]. macOS user accent color [S-L10-010]. iOS/iPadOS/macOS icon looks (default, dark, clear, tinted) [S-L10-075, S-L10-085]. iOS 27 Liquid Glass transparency slider from "ultra clear" to "fully tinted", plus Reduce Transparency and Increase Contrast [S-L10-003, S-L10-004]. Windows Mica wallpaper tint [S-L10-066].
  - **Fixed brand.** Supply your own color scheme and skip dynamic color. On Apple you cannot opt out of user glass settings or icon looks; you can only provide good icon layers and colors [S-L10-075] [inferred for "cannot opt out"].
  - **Hybrid.** Dynamic color for surfaces and neutrals, fixed brand for the primary action or logo moments [inferred]. Material's "fixed" roles exist for colors that stay the same across light and dark (L01 covers them).
- **Visual effect:** Following the OS makes the app feel personal and native, but screenshots differ per user and brand recognition weakens. Fixed brand keeps marketing screenshots and brand recall consistent [inferred].
- **Depends on (upstream):** DC-L10-04, L01 palette generation (HCT on Material).
- **Affects (downstream):** every color role on Android; app icon layers on Apple; QA matrix (N wallpapers x light/dark).
- **Token encoding:** a `colorSource = brand | dynamic | hybrid` setting per platform; brand tokens still exist as the fallback when dynamic color is unavailable (pre-Android 12, web) [inferred from S-L10-019].
- **Platform notes:** Web has no dynamic color hook [inferred]. Windows has an accent but it's outside what the pages read here cover.
- **Accessibility constraints:** generated schemes must still meet 4.5:1 / 3:1 [S-L10-072]. Apple's transparency slider and Reduce Transparency change glass legibility, so test the extremes [S-L10-003, S-L10-008].
- **Default + heuristic:** Default to dynamic color on Android for utility apps and fixed brand for brand-led consumer apps; on Apple, design icon layers for all four looks. Rule of thumb: the stronger the brand color's recall value, the less of it should yield to the wallpaper.
- **Evidence:** [S-L10-003, S-L10-004, S-L10-008, S-L10-010, S-L10-019, S-L10-027, S-L10-066, S-L10-072, S-L10-075, S-L10-085]

### DC-L10-06: Typeface strategy per platform (system font vs brand font)
- **Block path:** Foundations > Typography > Typeface > Platform mapping
- **Questions the designer answers:** Do we use the platform font (SF Pro, Roboto, Segoe UI Variable) or our brand font? Everywhere, or only for headlines?
- **Options:**
  - **System font everywhere.** SF Pro on Apple (plus SF Compact, SF Mono, rounded variants, New York serif); don't embed system fonts [S-L10-011]. Roboto on Android (Fluent's Android ramp uses it) [S-L10-039]. Segoe UI Variable on Windows [S-L10-039].
  - **Brand font for display, system for text.** Apple recommends exactly this: "use a custom font for headlines and subheadings while using system fonts for body copy and captions" [S-L10-009].
  - **Brand font everywhere.** Allowed, but on Apple a custom font must support Dynamic Type and Bold Text [S-L10-011]. Fluent's stance: Segoe is the signature face, but "the system defaults to native system fonts" on other platforms [S-L10-039].
  - **Shared role names, per-platform values.** Fluent keeps names (Caption, Body, Subtitle, Title, Large Title, Display) and changes sizes per platform: Body 1 is 14/20px on web, 17/22pt on iOS, 16/24sp on Android [S-L10-039].
- **Visual effect:** System fonts make the app look native and optimize small-size legibility (SF's optical sizes and automatic tracking) [S-L10-011]. A brand font in headlines gives instant recognition with native-feeling body text. A brand font everywhere gives the strongest identity but risks legibility at 11-13pt and extra work for Dynamic Type [inferred].
- **Depends on (upstream):** DC-L10-02 (posture), L02 typeface choice, L06 brand.
- **Affects (downstream):** all `type.*` tokens, line heights, text truncation behavior at AX sizes, font licensing and app size.
- **Token encoding:** `font.family.brand`, `font.family.text` with platform values, e.g. `font.family.text = { ios: "system", android: "Roboto", web: "system-ui, ...", windows: "Segoe UI Variable" }` [inferred]. Type roles like `type.body.md` with platform-specific `fontSize`/`lineHeight` [S-L10-039].
- **Platform notes:** Apple exposes system fonts through `Font.Design` constants rather than font files [S-L10-011]. Android 16 ignores `elegantTextHeight`, so layouts must handle tall scripts (Arabic, Thai, Tamil and others) without the old "UI fonts" [S-L10-020].
- **Accessibility constraints:** minimum text sizes per platform (iOS 11pt, macOS 10pt, watchOS/visionOS 12pt, tvOS 23pt) apply to custom fonts too [S-L10-011].
- **Default + heuristic:** Default to brand font for display and headline roles and system font for body, label and caption on native platforms; brand font throughout on web if its small sizes pass. Rule of thumb: if the brand font needs size bumps to look as legible as the system font at 13pt, keep it out of body text.
- **Evidence:** [S-L10-009, S-L10-011, S-L10-020, S-L10-039]

### DC-L10-07: Text scaling policy (Dynamic Type, sp, rem)
- **Block path:** Foundations > Typography > Scaling > Platform text scaling
- **Questions the designer answers:** How far must our layouts stretch when users enlarge text? Do we cap scaling anywhere? Which text follows the setting and which doesn't?
- **Options:**
  - **Full support (recommended by every platform).** iOS text styles cover xSmall to xxxLarge plus five accessibility sizes; at AX5 Body is 53/62pt and Caption 2 is 40/48pt [S-L10-011]. Apple asks for at least 200% enlargement (140% on watchOS) and minimal truncation at the largest size [S-L10-012, S-L10-011]. Android scales sp nonlinearly to 200% (Android 14+) [S-L10-071]. Web: rem-based font sizes follow the user's browser setting [S-L10-074].
  - **Capped scaling.** React Native exposes `maxFontSizeMultiplier` (e.g. 1.5) [S-L10-064]. Capping is a compromise for fixed-height chrome, not for body text [inferred].
  - **No scaling (fixed px/pt).** Breaks accessibility expectations. macOS is the one platform without Dynamic Type [S-L10-011].
- **Visual effect:** Supporting AX sizes forces layouts to reflow: horizontal rows become stacked, icons grow with text (SF Symbols scale automatically), truncation is replaced by wrapping [S-L10-011]. Material's nonlinear curve keeps headings from growing as fast as body text, preserving hierarchy at 200% [S-L10-071]. Designs that assume fixed text heights look broken at large sizes [inferred].
- **Depends on (upstream):** DC-L10-06 (typeface), L02 type scale.
- **Affects (downstream):** component min-heights (should be min, not fixed), list row layouts, button label wrapping, icon sizing tokens, line-height tokens (in sp on Android) [S-L10-071].
- **Token encoding:** type tokens should reference a platform text style rather than only a number: `type.body = { ios: textStyle "body", android: 16sp/24sp, web: 1rem/1.5rem }` [inferred from S-L10-011, S-L10-019, S-L10-074]. Never mix sp into spacing tokens [S-L10-070].
- **Platform notes:** RN respects Dynamic Type through `dynamicTypeRamp` (default `body`) and Android font scale when `allowFontScaling` is true (default) [S-L10-064]. Compose Multiplatform 1.8 respects iOS font size settings [S-L10-059].
- **Accessibility constraints:** HIG 200% guidance [S-L10-012]; WCAG 1.4.4 resize text [inferred; L02 owns].
- **Default + heuristic:** Default to full scaling with no cap on body text, and a documented cap (about 1.5x) only for fixed chrome like tab labels. Rule of thumb: test every screen at the platform's largest setting before calling a component done.
- **Evidence:** [S-L10-011, S-L10-012, S-L10-019, S-L10-059, S-L10-064, S-L10-070, S-L10-071, S-L10-074]

### DC-L10-08: Unit system and value translation
- **Block path:** Tokens > Encoding > Units per platform
- **Questions the designer answers:** In what unit do we author sizes? How do they become pt, dp, sp, epx, px and rem? Do we round?
- **Options:**
  - **Author unitless numbers, emit per platform (1:1).** 1 = 1pt = 1dp = 1epx = 1 CSS px; divide by 16 for rem [inferred; see table B]. Fluent's spacing ramp uses the same numbers in pt, dp and px [S-L10-039].
  - **Author in rem, convert down.** Style Dictionary's built-in transforms convert rem to dp/sp (Android, Compose), CGFloat (Swift) and double (Flutter), with base font size 16 [S-L10-057].
  - **Author in px, convert up to rem on web.** Common in Figma-first workflows, since Figma works in px [inferred; L07 owns Figma].
  - **Grid discipline.** Windows asks for multiples of 4 epx so UI lands on whole pixels at 125%, 150% and other plateaus [S-L10-069]. Apple suggests placing vector control points on whole values at @1x so they stay crisp at @2x/@3x [S-L10-087].
- **Visual effect:** Consistent translation keeps proportions identical across platforms. Non-4 values produce blurry 1px edges on Windows at fractional scales [S-L10-069].
- **Depends on (upstream):** DC-L10-01; L03 base unit (4 vs 8).
- **Affects (downstream):** every dimension token; DC-L10-22 transforms.
- **Token encoding:** DTCG `$type: "dimension"` with `{ "value": 16, "unit": "px" }` or `rem` (L07 owns the exact 2025.10 shape). Text sizes carry a "scalable" flag so Android emits sp and web emits rem, while spacing emits dp and px [inferred from S-L10-057, S-L10-070].
- **Platform notes:** visionOS points are angular, so a fixed pt size looks smaller as a window moves away, and the system scales windows to stay legible [S-L10-087, S-L10-013].
- **Accessibility constraints:** font sizes on web should be relative units [S-L10-074]; Android text in sp [S-L10-070].
- **Default + heuristic:** Default to unitless 4-based numbers in the source of truth, emitted as pt/dp/epx/px 1:1 and rem for web font sizes (and optionally spacing). Rule of thumb: if a value isn't divisible by 4 (except 2, 6, 10 for icon nudges), question it [S-L10-039, S-L10-069].
- **Evidence:** [S-L10-013, S-L10-039, S-L10-057, S-L10-069, S-L10-070, S-L10-074, S-L10-087]

### DC-L10-09: Primary navigation model per platform and size
- **Block path:** Patterns > Navigation > Top-level navigation
- **Questions the designer answers:** What carries top-level navigation on phones, tablets and desktops? Does it change by window size? Do we use the same pattern on iOS and Android?
- **Options:**
  - **iOS.** Tab bar floating on Liquid Glass at the bottom; can minimize on scroll with an accessory (like Music's MiniPlayer); a dedicated search tab sits at the trailing end [S-L10-014, S-L10-075]. Hierarchy uses a navigation stack with swipe-back [S-L10-015].
  - **iPadOS.** Tab bar near the top, fixed or convertible to a sidebar (`sidebarAdaptable`); `NavigationSplitView` for sidebar-only; max two levels in a sidebar, then a split view [S-L10-014]. iPadOS 26 adds a menu bar reached by swiping down or moving the pointer to the top [S-L10-085].
  - **macOS.** Menu bar for "all the commands", toolbar, sidebar [S-L10-015].
  - **Android.** Material breakpoints swap components: navigation bar at compact width; collapsed navigation rail at medium/expanded; standard expanded rail at large and extra-large [S-L10-025].
  - **watchOS.** Shallow hierarchy with Digital Crown vertical navigation [S-L10-015]. **tvOS**: focus-driven [S-L10-015].
  - **Cross-platform unification.** Airbnb moved Android from a left drawer to the bottom bar shared with iOS [S-L10-044].
- **Visual effect:** A bottom bar (both phones) puts navigation in the thumb zone; the iOS version floats and shrinks, the Material version is a solid bar with a pill indicator [S-L10-014] [inferred for Material visuals; L08 owns component anatomy]. Rails and sidebars reveal labels and more destinations at larger widths and change the app's silhouette from "stack" to "workspace" [S-L10-025].
- **Depends on (upstream):** DC-L10-01, DC-L10-02, DC-L10-10 (breakpoints), information architecture (L08).
- **Affects (downstream):** app-shell template, safe-area and inset handling, FAB placement, search placement, number of top-level destinations.
- **Token encoding:** component tokens per navigation component (`nav.bar.height`, `nav.rail.width.collapsed/expanded`, `tabbar.icon.size`), plus a layout rule table "breakpoint to navigation component" [inferred].
- **Platform notes:** Apple warns against overflow tabs; the trailing tab becomes "More" when space runs out [S-L10-014]. Material says only swap components that are functionally equivalent [S-L10-025].
- **Accessibility constraints:** controls mid/bottom are easier to reach [S-L10-015]; tab icons should use SF Symbols so they scale [S-L10-014]; each icon needs an accessibility label [S-L10-075].
- **Default + heuristic:** Default to bottom tab/navigation bar on phones (3-5 destinations), navigation rail (Android) or sidebar-adaptable tab bar (iPad) from 600dp / regular width, sidebar plus menu bar on desktop. Rule of thumb: keep the destinations identical across platforms and let the container change.
- **Evidence:** [S-L10-014, S-L10-015, S-L10-025, S-L10-044, S-L10-075, S-L10-085]

### DC-L10-10: Adaptive layout strategy (size classes, breakpoints, panes, foldables)
- **Block path:** Foundations > Layout > Adaptive strategy
- **Questions the designer answers:** Do we lay out by device type or by available window space? How many panes at each size? What happens when the window resizes or a foldable opens?
- **Options:**
  - **Apple size classes.** Compact or regular per axis, set by device, window configuration and multitasking; "determine layout based on size classes, not device type or orientation" [S-L10-013].
  - **Material breakpoints** (Android and web): compact <600dp, medium 600-839, expanded 840-1199, large 1200-1599, extra-large 1600+ [S-L10-025]. Panes: 1, 1-2, 2, 2, 1-3 [S-L10-025]. Height classes compact <480, medium 480-899, expanded 900+ [S-L10-022]. Large/XL need `supportLargeAndXLargeWidth = true` in Compose [S-L10-022].
  - **Windows breakpoints** in epx: small up to 640 (includes TVs, because of viewing distance), medium 641-1007, large 1008+ [S-L10-069].
  - **Web.** Responsive (fluid, media queries) plus component-level container queries (`container-type: inline-size`; `cqi` units) [S-L10-034]. L03 covers breakpoint values.
  - **Adapt moves** (Material): reveal, divide, resize, reposition, swap [S-L10-025].
- **Visual effect:** Window-based layouts let the same app look like a phone app in split view and a two-pane workspace full screen. Device-based layouts break in split screen, Slide Over, iPhone Mirroring and desktop windowing [S-L10-013, S-L10-022]. Material recommends 40-60 characters per line at every breakpoint [S-L10-025].
- **Depends on (upstream):** DC-L10-01 (form factors), L03 grid.
- **Affects (downstream):** DC-L10-09 navigation swaps; list-detail and supporting-pane templates; dialog vs full-screen dialog; bottom sheet vs menu [S-L10-025].
- **Token encoding:** `breakpoint.*` dimension tokens per platform family (Material set for Android + web, size class for Apple), plus layout templates keyed by breakpoint [inferred]. Keep "layout by window" semantics: never name tokens `tablet`/`phone` [S-L10-013, S-L10-022].
- **Platform notes:** Android 16+ ignores orientation/resizability locks at sw600dp+, and 17 removes the opt-out [S-L10-020, S-L10-021]. iPadOS 26's windowing system makes arbitrary window sizes common on iPad [S-L10-085]. Google's Googlebook desktop and Desktop Emulator extend the same adaptive model to laptops [S-L10-002].
- **Accessibility constraints:** reflow must still work at large text sizes (DC-L10-07); WCAG reflow at 320 CSS px (L03 [S-L03-060]).
- **Default + heuristic:** Default to Material breakpoints for Android and web, size classes for Apple, and a canonical list-detail template that becomes two panes at expanded. Rule of thumb: design compact first, then answer the five questions (reveal, divide, resize, reposition, swap) at each larger size.
- **Evidence:** [S-L10-002, S-L10-013, S-L10-020, S-L10-021, S-L10-022, S-L10-025, S-L10-034, S-L10-069, S-L10-085]

### DC-L10-11: Edge-to-edge, safe areas, insets and system bars
- **Block path:** Foundations > Layout > Safe areas and insets
- **Questions the designer answers:** Does content draw behind the status bar, navigation bar and home indicator? How do controls avoid cutouts and gesture areas? What sits behind system bars?
- **Options:**
  - **Android edge-to-edge (mandatory).** Enforced when targeting SDK 35 on Android 15+; the opt-out is disabled at SDK 36 [S-L10-023, S-L10-020]. Status bar and gesture navigation are transparent; 3-button navigation gets a translucent scrim [S-L10-023]. Handle `systemBars`, `displayCutout` and `systemGestures` insets [S-L10-023].
  - **Apple safe areas.** Respect safe areas so the Dynamic Island, bars and hardware don't cover content [S-L10-013]. Use a scroll edge effect instead of solid bar backgrounds [S-L10-013]. A background extension effect can mirror and blur imagery under sidebars and inspectors [S-L10-013].
  - **tvOS overscan.** Inset primary content 60pt top/bottom, 80pt sides [S-L10-013].
  - **Web.** `env(safe-area-inset-*)` and viewport units (`svh`, `lvh`, `dvh`) for mobile browsers [S-L10-074] [inferred for env()].
- **Visual effect:** Full-bleed content under translucent bars makes apps feel immersive and modern on both platforms. Solid-color system bar backgrounds now look legacy on Android 15+ and fight Liquid Glass on iOS [S-L10-023, S-L10-013] [inferred for "legacy"].
- **Depends on (upstream):** DC-L10-01, DC-L10-09 (bars), DC-L10-12 (materials).
- **Affects (downstream):** app bar, bottom bar, FAB and sheet padding; hero imagery; scroll edge treatments; immersive/media screens.
- **Token encoding:** insets are runtime values, not tokens. Tokens cover the treatment: `surface.scrim.systemBar`, `effect.scrollEdge`, and min margins [inferred].
- **Platform notes:** Material components like BottomAppBar and NavigationRailView handle insets automatically [S-L10-023]. Predictive back previews keep at least 8dp from screen edges [S-L10-030].
- **Accessibility constraints:** don't place touch targets under system gesture areas [S-L10-030]; WCAG 2.4.11 requires focused items not to be fully obscured by sticky bars [S-L10-083].
- **Default + heuristic:** Default to edge-to-edge everywhere with inset-aware components. Rule of thumb: backgrounds extend to the edge, interactive content respects the safe area.
- **Evidence:** [S-L10-013, S-L10-020, S-L10-023, S-L10-030, S-L10-074, S-L10-083]

### DC-L10-12: Materials, translucency and surface treatment per platform
- **Block path:** Foundations > Depth > Materials (platform)
- **Questions the designer answers:** Do our bars and panels blur what's behind them, or are they solid? Do we use the platform's material or our own? What happens when the user reduces transparency?
- **Options:**
  - **Apple Liquid Glass (functional layer only).** Controls and navigation float on glass above content; "don't use Liquid Glass in the content layer"; use it sparingly on custom controls [S-L10-008]. Two variants: regular (blurs and adjusts luminosity; for text-heavy components like alerts, sidebars, popovers) and clear (highly translucent, for components over photos and video, with a 35% dark dimming layer over bright content) [S-L10-008]. APIs: `glassEffect(_:in:)`, `UIGlassEffect`, `NSGlassEffectView`, `GlassEffectContainer` [S-L10-075]. iOS 27 adds a darkened edge, brighter specular highlights and better diffusion [S-L10-003].
  - **Apple standard materials (content layer).** ultraThin, thin, regular, thick with vibrant label and fill levels [S-L10-008].
  - **Windows.** Mica (opaque, wallpaper-tinted window base), Acrylic (frosted, only for transient light-dismiss surfaces), Smoke (modal dim) [S-L10-066].
  - **Material 3.** Tonal surface roles rather than blur (L01/L04 cover surface containers) [S-L10-019].
  - **Web.** `backdrop-filter` or solid surfaces; `prefers-reduced-transparency` exists but is not Baseline [S-L10-032]; forced colors strip shadows and non-URL background images [S-L10-031].
- **Visual effect:** Glass chrome gives depth, dynamism and "content first"; solid chrome gives calm and predictability. Overused glass distracts and hurts legibility [S-L10-008]. Mica gives Windows apps a subtle personal tint; Acrylic signals "temporary" [S-L10-066].
- **Depends on (upstream):** DC-L10-02, DC-L10-11; L04 elevation model.
- **Affects (downstream):** bar, sheet, popover, sidebar and menu tokens; icon/label colors on bars (monochrome vs tinted) [S-L10-010]; dark-mode surfaces.
- **Token encoding:** a `material` token type isn't in DTCG; encode as composite component tokens (`surface.chrome = { ios: "glass.regular", windows: "mica", android: "surfaceContainer", web: { bg, blur, opacityFallback } }`) [inferred; L04/L07 own].
- **Platform notes:** visionOS window glass is unmodifiable and adapts to surroundings [S-L10-008]. Liquid Glass responds to the user's preferred look (iOS 27 slider), Reduce Transparency and Increase Contrast [S-L10-008, S-L10-003].
- **Accessibility constraints:** provide an opaque fallback for reduced transparency on web and Apple [S-L10-032, S-L10-008]; maintain legibility at the resting state (top of scroll) [S-L10-010].
- **Default + heuristic:** Default to the platform material for chrome (glass on Apple, Mica on Windows, tonal surfaces on Android) and solid surfaces on web with an optional blur plus opaque fallback. Rule of thumb: translucency belongs on navigation and transient layers, never on reading surfaces.
- **Evidence:** [S-L10-003, S-L10-008, S-L10-010, S-L10-019, S-L10-031, S-L10-032, S-L10-066, S-L10-075]

### DC-L10-13: Controls: system controls vs custom-branded controls (and shape)
- **Block path:** Components > Controls > Platform rendering
- **Questions the designer answers:** Do buttons, switches, sliders, pickers and text fields use the OS control, a restyled OS control, or our own? Do corner radii follow the platform?
- **Options:**
  - **System controls.** On Apple, standard controls "come to life" in Liquid Glass: slider and toggle knobs turn into glass while dragged, buttons morph into menus and popovers, and controls take rounder forms concentric with hardware and window corners [S-L10-075]. If you don't hard-code metrics, you get shape and size changes by rebuilding [S-L10-075]. Material components in Compose enforce 48dp targets and use the motion scheme by default [S-L10-072, S-L10-024].
  - **Restyled system controls.** Apple permits brand customization if "sizing, placement, and behavior continue to preserve a familiar experience" [S-L10-009]. Toolbar items should keep corner radii concentric with the bar [S-L10-014].
  - **Fully custom controls.** Needed for brand-first posture or web. Must rebuild states, haptics, accessibility, and on Apple avoid custom backgrounds that "interfere with Liquid Glass" [S-L10-075].
  - **Platform shape defaults.** Windows: 4px for in-page controls and bars, 8px for windows, flyouts and dialogs, 0 when touching or snapped; configurable via `ControlCornerRadius` and `OverlayCornerRadius` [S-L10-067]. Material shapes: extraSmall 4, small 8, medium 12, large 16, extraLarge 24dp [S-L10-019]. Apple: concentric radii derived from the container and hardware [S-L10-075, S-L10-014].
- **Visual effect:** System controls make the app feel native and update with the OS. On iOS 26+ they are rounder and more capsule-like [S-L10-075]. Custom controls keep brand shape language (e.g. square brutalist buttons) but can look out of place next to system sheets, keyboards and menus [inferred].
- **Depends on (upstream):** DC-L10-02 (posture), L04 shape scale.
- **Affects (downstream):** radius tokens, control height tokens, state layers, haptic tokens (DC-L10-14), component variants per platform.
- **Token encoding:** `radius.control`, `radius.overlay`, `radius.container` with platform values (Windows 4/8; Material scale; Apple "concentric/system") [S-L10-067, S-L10-019] [inferred for the Apple value being a flag, not a number].
- **Platform notes:** the pre-Liquid-Glass look can't be preserved past the 27 SDKs [S-L10-076]. Material Components for iOS are in maintenance mode [S-L10-082]; Material Web Components are in maintenance mode since June 2024 [S-L10-079].
- **Accessibility constraints:** system controls carry roles, traits and state announcements (VoiceOver, TalkBack) [S-L10-015, S-L10-072]. Custom controls must supply them.
- **Default + heuristic:** Default to system controls tinted with the accent on native platforms, custom controls on web. Rule of thumb: restyle color and label; don't restyle shape, size or behavior of controls the OS users touch in every app (switches, pickers, text fields, sheets).
- **Evidence:** [S-L10-009, S-L10-014, S-L10-015, S-L10-019, S-L10-024, S-L10-067, S-L10-072, S-L10-075, S-L10-076, S-L10-079, S-L10-082]

### DC-L10-14: Motion, back navigation and haptics per platform
- **Block path:** Foundations > Motion > Platform motion
- **Questions the designer answers:** Do we use one motion language everywhere or the platform's? How does "back" look and feel? Do we use haptics?
- **Options:**
  - **Material motion physics.** Springs (stiffness, damping, initial velocity) replace easing and duration. Two schemes: expressive (overshoot and bounce, Material's default for most products) and standard (minimal bounce, for utilitarian products) [S-L10-024]. Tokens `md.sys.motion.spring.{fast,default,slow}.{spatial,effects}`; spatial springs may overshoot, effects springs (color, opacity) must not [S-L10-024]. Token values differ by device class (wearable, phone, tablet) [S-L10-024]. Available in Compose (`MaterialTheme.motionScheme`), MDC-Android, unavailable in Flutter, "compatible with Compose springs" on web [S-L10-024, S-L10-018].
  - **Apple.** System components include motion that adapts to accessibility settings and input; custom motion should be purposeful, brief, cancelable, optional, and avoided on frequent interactions [S-L10-088]. visionOS: avoid peripheral motion and ~0.2 Hz oscillation [S-L10-088].
  - **Back navigation.** Android 16 turns on predictive back system animations (back-to-home, cross-task, cross-activity) for apps targeting 36; custom full-screen transitions scale the exiting screen 100 to 90% and entering 110 to 100%, crossfading at 35% progress [S-L10-020, S-L10-030]. iOS uses swipe-back in navigation stacks [S-L10-015].
  - **Haptics.** Apple standard controls play haptics automatically on iPhone; use system patterns per documented meaning, consistently [S-L10-090].
  - **Shared brand motion.** Spotify keeps motion in its cross-platform Foundation tokens [S-L10-040].
- **Visual effect:** Expressive springs feel playful and alive; standard feels functional [S-L10-024]. Predictive back gives Android a "peek behind" preview that custom full-screen transitions must mimic [S-L10-030]. Mismatched back animations make a cross-platform app feel foreign [inferred].
- **Depends on (upstream):** DC-L10-02, L04 motion principles, L06 personality.
- **Affects (downstream):** transition specs, sheet and dialog enter/exit, button press feedback, navigation transitions, haptic tokens.
- **Token encoding:** brand motion personality shared as spring parameters (stiffness, damping) or duration + easing (L04/L07 own DTCG `duration`/`cubicBezier`); platform transitions (back, sheets) not tokenized, delegated to the OS [inferred].
- **Platform notes:** watchOS layout animations have built-in easing you can't turn off [S-L10-088]. Flutter lacks the M3 motion physics system for now [S-L10-024].
- **Accessibility constraints:** honor Reduce Motion (Apple) and `prefers-reduced-motion` (web) [S-L10-012] [inferred for web media query naming, L04 owns]; never make motion the only signal [S-L10-088].
- **Default + heuristic:** Default to OS-owned navigation transitions and back behavior, shared brand motion for in-content micro-interactions (as springs), and system haptics only. Rule of thumb: the OS owns how screens come and go; the brand owns how things inside a screen react.
- **Evidence:** [S-L10-012, S-L10-015, S-L10-018, S-L10-020, S-L10-024, S-L10-030, S-L10-040, S-L10-088, S-L10-090]

### DC-L10-15: Input modalities, density and target sizes
- **Block path:** Foundations > Interaction > Input modality and targets
- **Questions the designer answers:** Which inputs must we support: touch, mouse/trackpad, keyboard, pen, remote, Digital Crown, eyes and hands? How dense can the UI be for each? What's our minimum target?
- **Options:**
  - **Touch-first (phones).** iOS 44x44pt, Android 48x48dp [S-L10-012, S-L10-072].
  - **Pointer-first (desktop).** macOS 28x28pt default, 20 minimum [S-L10-012]. Android says smaller targets are acceptable for precise input [S-L10-072]. Windows spacing: 8epx between buttons, 12epx between control and label [S-L10-068].
  - **Remote / focus (TV).** tvOS 66x66pt default [S-L10-012]; focus system highlights and expands items [S-L10-015]. Google TV added pointer-remote support [S-L10-002].
  - **Spatial.** visionOS 60x60pt, button centers 60pt apart [S-L10-012, S-L10-013].
  - **Web, multi-modal.** WCAG 2.5.8 24x24 CSS px (AA) with a spacing exception; 44x44 at AAA [S-L10-036]. Detect modality with `pointer: coarse | fine`, `hover`, `any-pointer` (Baseline since 2018) [S-L10-073].
  - **Mixed input on tablets.** iPad users combine touch, keyboard, trackpad and Pencil [S-L10-015]; Compose added trackpad improvements [S-L10-080].
- **Visual effect:** Touch targets make layouts airier with larger rows; pointer layouts can be denser and show hover states [inferred]. Coarse-pointer CSS can enlarge controls only where needed [S-L10-073].
- **Depends on (upstream):** DC-L10-01, L03 density decision.
- **Affects (downstream):** control heights, list row heights, icon button padding, hover and focus states, density modes.
- **Token encoding:** `size.target.min` per platform (44 ios, 48 android, 24/44 web, 28 macos, 66 tvos, 60 visionos) and density modes keyed by input (`density = touch | pointer`) [inferred from S-L10-012, S-L10-072, S-L10-036].
- **Platform notes:** Fluent states 44x44 for iOS and web, 48x48 for Android [S-L10-039]. Compose Material components enforce 48dp automatically [S-L10-072].
- **Accessibility constraints:** the numbers above are the constraints; WCAG 2.5.7 requires a non-drag alternative [S-L10-083].
- **Default + heuristic:** Default to touch targets on all mobile and web surfaces (44 CSS px on web even though AA is 24) and a pointer density mode for desktop. Rule of thumb: the visible control can be small, the hit area can't.
- **Evidence:** [S-L10-002, S-L10-012, S-L10-013, S-L10-015, S-L10-036, S-L10-039, S-L10-068, S-L10-072, S-L10-073, S-L10-080, S-L10-083]

### DC-L10-16: Platform accessibility settings the system must honor
- **Block path:** Foundations > Accessibility > Platform settings
- **Questions the designer answers:** Which OS accessibility settings change our visuals, and what does each token do when they're on?
- **Options (settings to support):**
  - **Screen readers.** VoiceOver (Apple) and TalkBack (Android) need labels for every icon; Android's `contentDescription` should state purpose, not appearance, and use `Role` semantics [S-L10-075, S-L10-072]. Web uses ARIA (L08 owns APG patterns).
  - **Text size.** Dynamic Type, Android font scale, browser font size (DC-L10-07).
  - **Contrast.** Apple Increase Contrast (system colors have increased-contrast variants) [S-L10-010, S-L10-012]; Android High Contrast and Material contrast levels (L01); web `prefers-contrast: more | less | custom` [S-L10-033].
  - **Forced colors.** Windows High Contrast drives `forced-colors: active`, which overrides color, background, border and SVG fill/stroke with system colors (Canvas, CanvasText, LinkText, ButtonFace, ButtonText, Highlight, HighlightText, GrayText) and removes box-shadow [S-L10-031].
  - **Transparency.** Apple Reduce Transparency; web `prefers-reduced-transparency` (not Baseline) [S-L10-008, S-L10-032].
  - **Motion.** Reduce Motion / `prefers-reduced-motion` [S-L10-012].
  - **Motor.** Switch Control, AssistiveTouch, Full Keyboard Access, Pointer Control (Apple) [S-L10-012]; Switch Access (Android) [S-L10-072]; keyboard-only on web with visible, unobscured focus (WCAG 2.4.7, 2.4.11) [S-L10-083].
  - **Cognitive.** Apple Assistive Access provides a streamlined layout [S-L10-012].
- **Visual effect:** A system that honors these settings changes appearance for the user: thicker borders and solid outlines in high contrast, opaque bars instead of glass, no parallax, larger text with reflowed layouts, and system colors in forced-colors mode [S-L10-031, S-L10-033, S-L10-008].
- **Depends on (upstream):** L01 contrast strategy, DC-L10-12 materials.
- **Affects (downstream):** focus ring tokens, border tokens (shadows alone disappear in forced colors) [S-L10-031], material fallbacks, motion tokens.
- **Token encoding:** accessibility modes as token modes: `contrast = standard | more`, `transparency = full | reduced`, `motion = full | reduced`, plus a forced-colors mapping of semantic roles to CSS system colors [inferred from S-L10-031, S-L10-033; Atlassian treats reduced motion and high contrast as themes S-L10-050].
- **Platform notes:** Apple's system colors ship light, dark and increased-contrast values in both modes [S-L10-010]. React Native `PlatformColor` picks up theme and high-contrast changes from native colors [S-L10-063]. Compose Multiplatform supports VoiceOver, AssistiveTouch and Full Keyboard Access on iOS [S-L10-059].
- **Accessibility constraints:** WCAG 2.2 AA (2.4.11, 2.5.7, 2.5.8) [S-L10-083]; Apple and Android contrast minimums [S-L10-012, S-L10-072].
- **Default + heuristic:** Default to honoring every listed setting, with high contrast and reduced transparency as first-class token modes. Rule of thumb: never convey a boundary or focus state with shadow or translucency alone; forced colors and reduced transparency will remove it.
- **Evidence:** [S-L10-008, S-L10-010, S-L10-012, S-L10-031, S-L10-032, S-L10-033, S-L10-050, S-L10-059, S-L10-063, S-L10-072, S-L10-075, S-L10-083]

### DC-L10-17: Dark mode and appearance modes per platform
- **Block path:** Foundations > Color > Appearance modes (platform)
- **Questions the designer answers:** Do we support dark mode on every platform? Do we follow the system setting or offer our own toggle? Which platforms have no dark mode or are always dark?
- **Options:**
  - **Follow system appearance (Apple).** Users "expect all apps and games to respect their preference"; avoid an app-specific appearance setting [S-L10-089]. Dark palette isn't an inversion; base vs elevated backgrounds convey layering [S-L10-089].
  - **No dark mode / always dark.** "Dark Mode isn't supported in visionOS or watchOS" [S-L10-089]; visionOS glass adapts to luminance instead [S-L10-008]. Wear OS uses black backgrounds as standard [S-L10-027].
  - **Android.** Light/dark color schemes, plus dynamic dark schemes [S-L10-019]. React Native Paper offers "exact" vs "adaptive" dark themes [S-L10-065].
  - **Web.** `prefers-color-scheme` plus an optional site toggle (L01 covers); forced colors sets `color-scheme: light dark` [S-L10-031].
  - **Windows.** Light, dark, high contrast via Fluent tokens; Mica and Acrylic are mode-aware, Smoke isn't [S-L10-039, S-L10-066].
- **Visual effect:** Following the system makes the app blend with the OS at night. An app-only toggle creates mismatches and "broken" perception on Apple [S-L10-089]. Watch and headset designs start dark-first [S-L10-089, S-L10-027].
- **Depends on (upstream):** L01 dark palette mapping; DC-L10-01.
- **Affects (downstream):** every color role; imagery (soften white image backgrounds in dark mode) [S-L10-089]; elevation (base vs elevated).
- **Token encoding:** `appearance = light | dark` mode on the semantic tier; watchOS/Wear use the dark set only; visionOS uses system glass and "default dark" system color values [S-L10-010] [inferred for token structure].
- **Platform notes:** Liquid Glass bars flip light/dark with the content underneath regardless of app mode [S-L10-010].
- **Accessibility constraints:** test dark mode with Increase Contrast and Reduce Transparency, separately and together [S-L10-089].
- **Default + heuristic:** Default to system-following light and dark on phones, tablets, desktop and web, dark-only on watches. Rule of thumb: offer an in-app override only on web and only in addition to system-follow.
- **Evidence:** [S-L10-008, S-L10-010, S-L10-019, S-L10-027, S-L10-031, S-L10-039, S-L10-065, S-L10-066, S-L10-089]

### DC-L10-18: Web delivery layer (CSS custom properties, preference queries, container queries, rem)
- **Block path:** Tokens > Delivery > Web
- **Questions the designer answers:** How do tokens reach the browser? How do themes and user preferences switch values? Do components respond to their container or the viewport?
- **Options:**
  - **CSS custom properties as the runtime token layer.** Salesforce SLDS 2 replaced design tokens on web with "global styling hooks", i.e. CSS custom properties [S-L10-052]. Style Dictionary emits `css/variables` [S-L10-056].
  - **Preference hooks.** `prefers-color-scheme`, `prefers-contrast` (widely available since May 2022), `forced-colors` (widely available since Sept 2022), `prefers-reduced-motion`, `prefers-reduced-transparency` (not Baseline) [S-L10-033, S-L10-031, S-L10-032].
  - **Container queries.** `container-type: inline-size` and `cqi`/`cqw` units let components adapt to their slot; size queries are Baseline widely available (about Aug 2025, per a secondary source) [S-L10-034, S-L10-035].
  - **Relative sizing.** rem for type (follows user font size); px is fixed [S-L10-074].
  - **Input queries.** `pointer`, `hover`, `any-pointer` [S-L10-073].
- **Visual effect:** Custom properties let a single stylesheet switch light/dark/brand/high-contrast by swapping a class or media query. Container queries let the same card look compact in a sidebar and rich in a main column [S-L10-034] [inferred for "same card"].
- **Depends on (upstream):** DC-L10-08 (units), L07 tokens.
- **Affects (downstream):** theming, component CSS, dark mode, density modes.
- **Token encoding:** semantic tokens become `--color-text-primary` etc.; modes switch via `[data-theme]` or `@media (prefers-color-scheme)`; forced-colors overrides map roles to system colors [S-L10-031] [inferred for naming].
- **Platform notes:** Electron and web-view desktop apps reuse this layer [S-L10-078] [inferred].
- **Accessibility constraints:** forced-colors removes shadows [S-L10-031]; rem for font size [S-L10-074].
- **Default + heuristic:** Default to CSS custom properties for semantic tokens, media queries for preferences, container queries for component responsiveness, viewport breakpoints only for page layout. Rule of thumb: components query containers, pages query viewports.
- **Evidence:** [S-L10-031, S-L10-032, S-L10-033, S-L10-034, S-L10-035, S-L10-052, S-L10-056, S-L10-073, S-L10-074, S-L10-078]

### DC-L10-19: Component implementation technology (web components vs framework components)
- **Block path:** Components > Implementation > Technology
- **Questions the designer answers:** Do we ship components as framework components (React, Vue, Angular) or as framework-agnostic web components? Can one component API serve several host surfaces?
- **Options:**
  - **Framework components (React etc.).** The historical default; Polaris React is now deprecated [S-L10-047] (archive noted by L03 [S-L03-005]). Base Web is Uber's React implementation (one of 7 stacks) [S-L10-046].
  - **Web components.** Shopify moved Polaris to web components in 2025 because "Shopify's platform is the web platform"; they are CDN-delivered, framework-agnostic and smaller than the React runtime [S-L10-047]. Salesforce builds on Lightning Web Components with CSS custom property styling hooks [S-L10-052].
  - **Host-rendered component contracts.** The same Polaris tag renders as native UI in the POS app on iOS and Android [S-L10-048]. This is the closest thing to "write once, native everywhere" in a published system [inferred].
  - **Caution on vendor-maintained web component libraries.** Material Web Components entered maintenance mode in June 2024 when Google reassigned engineers to its internal Wiz framework [S-L10-079].
- **Visual effect:** None directly; the effect is on consistency across products using different frameworks and on how fast design updates propagate (CDN delivery updates every consumer at once) [S-L10-047].
- **Depends on (upstream):** DC-L10-01, DC-L10-03; engineering landscape.
- **Affects (downstream):** theming mechanism (CSS custom properties pierce shadow DOM; class names don't) [inferred], docs, code generation targets.
- **Token encoding:** web components consume tokens as CSS custom properties [S-L10-052] [inferred for general case].
- **Platform notes:** web components run in Electron and web views, not in native SwiftUI/Compose, unless a host maps them to native components as Shopify POS does [S-L10-048].
- **Accessibility constraints:** shadow DOM complicates ARIA references across boundaries [inferred; L08 should verify].
- **Default + heuristic:** Default to framework components when one framework dominates; choose web components when several frameworks or third-party developers must consume the system. Rule of thumb: the more heterogeneous your consumers, the lower in the stack the component contract should live.
- **Evidence:** [S-L10-046, S-L10-047, S-L10-048, S-L10-052, S-L10-079]

### DC-L10-20: Native toolkit per platform (SwiftUI/UIKit, Compose/Views, WinUI)
- **Block path:** Platforms > Implementation > Native toolkit
- **Questions the designer answers:** Which native UI toolkit does each app use, and does the design system target the modern one only?
- **Options:**
  - **Apple: SwiftUI and/or UIKit/AppKit.** All three adopt Liquid Glass by rebuilding; glass APIs exist in each (`glassEffect`, `UIGlassEffect`, `NSGlassEffectView`) [S-L10-075]. Uber still ships both UIKit and SwiftUI implementations [S-L10-046]. Semantic colors (`label`, `secondaryLabel`, `systemBackground`, grouped backgrounds) and text styles are the native token layer [S-L10-010, S-L10-011].
  - **Android: Compose (Views in maintenance).** "Android is now Compose First; Views are now in maintenance mode" [S-L10-002]. Theming is `MaterialTheme(colorScheme, typography, shapes)` plus `motionScheme` [S-L10-019, S-L10-018]. An experimental Styles API adds state-based styleable properties, with Material adoption planned after it stabilizes [S-L10-080]. Wear OS uses Wear Compose Material 3 [S-L10-018, S-L10-026].
  - **Windows: WinUI / Windows App SDK.** Global resources like `ControlCornerRadius` and `OverlayCornerRadius`; epx units [S-L10-067, S-L10-069].
- **Visual effect:** Modern toolkits get new platform visuals first: M3 Expressive components ship in Compose, and MDC-Android has the motion physics system but not yet in its components [S-L10-024, S-L10-018]. Legacy toolkits lag [inferred].
- **Depends on (upstream):** DC-L10-01; existing codebase.
- **Affects (downstream):** DC-L10-22 output formats (`ios-swift/*`, `compose/object`, `android/resources`) [S-L10-056].
- **Token encoding:** map semantic tokens to native semantics where they exist (iOS semantic colors, Material color roles) and to generated constants where they don't [inferred from S-L10-010, S-L10-019].
- **Platform notes:** Compose Material 3's latest stable is 1.4.0 (2025-09-24); the 1.5.0 alphas (alpha28 on 2026-09-09) carry the expressive promotions, with MotionScheme still experimental and MaterialShapes/LoadingIndicator reverted to experimental [S-L10-018].
- **Accessibility constraints:** native semantics give screen-reader roles for free [S-L10-072].
- **Default + heuristic:** Default to SwiftUI (UIKit where needed) and Compose for new work. Rule of thumb: target the toolkit where the platform owner ships its new design language first.
- **Evidence:** [S-L10-002, S-L10-010, S-L10-011, S-L10-018, S-L10-019, S-L10-024, S-L10-026, S-L10-046, S-L10-056, S-L10-067, S-L10-069, S-L10-072, S-L10-075, S-L10-080]

### DC-L10-21: Cross-platform framework and how it themes
- **Block path:** Platforms > Implementation > Cross-platform framework
- **Questions the designer answers:** Do we build once with React Native, Flutter, Compose Multiplatform or .NET MAUI? If so, do we render platform-native widgets or our own? Which theming library?
- **Options:**
  - **React Native.** Renders native views; `PlatformColor` reads native semantic colors (iOS UIColor names, Android attributes) and follows theme and high-contrast changes [S-L10-063]. Text respects Dynamic Type and Android font scale by default (`allowFontScaling`), capped with `maxFontSizeMultiplier` [S-L10-064]. Docs are at v0.87 [S-L10-063]. Theming libraries:
    - **React Native Paper 5.x**: Material 3 by default (`MD3LightTheme`, `MD3DarkTheme`); dynamic color via a community Expo library [S-L10-065].
    - **Tamagui 2**: same style API on web and native, optimizing compiler, tokens and themes; Tamagui 2 was a release candidate at its Dec 2025 announcement [S-L10-061].
    - **NativeWind**: Tailwind classes for RN; v5 (Tailwind v4.1+) is pre-release, v4 remains stable [S-L10-060].
    - **Unistyles 3**: C++ core via Nitro modules, requires RN 0.78+ New Architecture; adaptive light/dark themes and breakpoints [S-L10-062].
  - **Flutter.** Draws its own widgets. Material and Cupertino were released as standalone packages (`material_ui`, `cupertino_ui` 1.0.0, Aug 2026) with removal from the framework planned later; official Liquid Glass and M3 Expressive implementations are "underway" [S-L10-055]. The M3 motion physics system is unavailable in Flutter [S-L10-024]. Theming: `ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: ...), textTheme: TextTheme(displayLarge..., bodyMedium...))`, read with `Theme.of(context)`, overridden per subtree with a `Theme` widget and `copyWith` [S-L10-091]. Brand tokens that Material doesn't model go in a `ThemeExtension` (implement `copyWith` and `lerp`, register in `ThemeData.extensions`, read with `Theme.of(context).extension<T>()`); `lerp` lets custom tokens animate during theme switches [S-L10-092].
  - **Compose Multiplatform.** Stable for iOS since 1.8.0 (May 2025); native iOS scroll physics, text selection, VoiceOver, AssistiveTouch, Full Keyboard Access, font size and contrast settings; Material widgets by default [S-L10-059].
  - **.NET MAUI.** Wraps native controls; `AppThemeBinding` and `SetAppThemeColor` switch resources on system theme (iOS 13+, Android 10+, macOS 10.14+, Windows 10+) [S-L10-077].
- **Visual effect:** RN and MAUI apps look native by default because they use native views [S-L10-063, S-L10-077]. Flutter and CMP draw their own pixels, so they look identical everywhere unless the team builds platform variants; they lag OS design changes until the framework ships them (Flutter's Liquid Glass is still in progress) [S-L10-055, S-L10-059].
- **Depends on (upstream):** DC-L10-02 (posture), DC-L10-03 (sharing layer), team skills.
- **Affects (downstream):** DC-L10-22 (token output: `react-native` and `flutter` transform groups, `flutter/class.dart`) [S-L10-056, S-L10-057]; how quickly OS updates reach users.
- **Token encoding:** RN: JS/TS objects (`javascript/es6`, `typescript/es6-declarations`) [S-L10-056]; Flutter: `flutter/class.dart` [S-L10-056]; CMP: Kotlin objects (`compose/object`) [S-L10-056].
- **Platform notes:** a brand-first posture pairs naturally with Flutter/CMP; a native-first posture pairs with RN, MAUI or fully native apps [inferred].
- **Accessibility constraints:** check each framework's support for Dynamic Type, font scale and screen readers before committing (RN and CMP document it) [S-L10-064, S-L10-059].
- **Default + heuristic:** Default to native (SwiftUI + Compose) or React Native for native-first products; Flutter or CMP for brand-first products that accept a lag on OS visual changes. Rule of thumb: if the product must look like iOS 27 the week iOS 27 ships, don't draw your own widgets.
- **Evidence:** [S-L10-024, S-L10-055, S-L10-056, S-L10-057, S-L10-059, S-L10-060, S-L10-061, S-L10-062, S-L10-063, S-L10-064, S-L10-065, S-L10-077, S-L10-091, S-L10-092]

### DC-L10-22: Token pipeline to platforms
- **Block path:** Tokens > Delivery > Multi-platform build
- **Questions the designer answers:** What files does each platform need? Who converts units and colors? Do platform overrides live in the source or in the build?
- **Options (Style Dictionary v5 built-ins):**
  - **Web:** `css/variables`, `scss/variables`, `javascript/es6`, `typescript/es6-declarations` [S-L10-056]; transform groups `css`, `scss`, `js`, `web` (sizes to rem) [S-L10-057].
  - **iOS:** `ios-swift/class.swift`, `ios-swift/enum.swift`, `ios-swift/any.swift` (plus Objective-C formats); transform group `ios-swift` uses `color/UIColorSwift` and `size/swift/remToCGFloat` [S-L10-056, S-L10-057].
  - **Android:** `android/resources`, `android/colors`, `android/dimens`, `android/fontDimens`; transform group `android` uses `size/remToSp`, `size/remToDp`, `color/hex8android` [S-L10-056, S-L10-057].
  - **Compose:** `compose/object`; transforms `size/compose/remToSp` and `size/compose/remToDp` [S-L10-056, S-L10-057].
  - **Flutter:** `flutter/class.dart`; `color/hex8flutter`, `size/flutter/remToDouble` [S-L10-056, S-L10-057].
  - **React Native:** a `react-native` transform group with camelCase names and object sizing [S-L10-057].
  - All conversions assume base font size 16 [S-L10-057]. Style Dictionary v5 reads DTCG 2025.10 JSON [S-L10-058] (L07 owns versions).
- **Visual effect:** a correct pipeline makes the same decision look the same on every platform; a lossy one (for example, rem to dp with the wrong base) silently changes sizes [inferred].
- **Depends on (upstream):** DC-L10-08 (units), DC-L10-20/21 (toolkits), L07 token tiers.
- **Affects (downstream):** every platform's theme object (SwiftUI extensions, `MaterialTheme` builders, CSS variables).
- **Token encoding:** platform overrides as modes or a platform modifier in the resolver; outputs per platform [inferred; L07 owns resolver].
- **Platform notes:** built-in iOS outputs are UIKit-flavored (`UIColor`) [S-L10-056, S-L10-057]; SwiftUI `Color` extensions and Compose `ColorScheme` builders usually need custom formats [inferred]. Mapping semantic tokens onto Apple's dynamic system colors (to inherit increased-contrast variants) also needs custom work [inferred from S-L10-010].
- **Accessibility constraints:** keep text tokens in sp/rem outputs so scaling survives the build [S-L10-057, S-L10-070].
- **Default + heuristic:** Default to Style Dictionary v5 with built-in formats for CSS, Compose, Android XML and Swift, plus custom formats for SwiftUI and Material `ColorScheme`. Rule of thumb: tokens should arrive in each codebase in the idiom that codebase already uses.
- **Evidence:** [S-L10-010, S-L10-056, S-L10-057, S-L10-058, S-L10-070]

### DC-L10-23: OS version floor and design-language generation
- **Block path:** Platforms > Scope > OS versions
- **Questions the designer answers:** Which OS versions do we support? Do we design for the new language only, or keep a fallback for older OS versions?
- **Options:**
  - **Apple 26+/27+.** Liquid Glass arrived with the 26 releases (June 2025) [S-L10-005]; the 27 releases (betas June 8, 2026) refine it [S-L10-004]. Apps built with the 27 SDKs can't keep the old look [S-L10-076]. Supporting iOS 18 and earlier means the same build shows the older design on those devices [inferred].
  - **Android 12+ for dynamic color** (`Build.VERSION_CODES.S`) [S-L10-019]; **14+** for nonlinear font scaling to 200% [S-L10-071]; **15+** edge-to-edge enforced (target 35) [S-L10-023]; **16+** predictive back default and large-screen locks ignored (target 36) [S-L10-020]; **17** (stable June 16, 2026) no opt-out from large-screen resizability (target 37) [S-L10-021, S-L10-028].
  - **Material generation.** M3 Expressive in Compose is still moving to stable in the 1.5.0 alphas [S-L10-018]; Wear OS M3 Expressive is available via Wear Compose Material 3 [S-L10-026].
  - **Web.** Choose features by Baseline status: `prefers-contrast`, `forced-colors`, `pointer` are widely available; `prefers-reduced-transparency` is not [S-L10-031, S-L10-032, S-L10-033, S-L10-073].
- **Visual effect:** a floor at the newest OS lets the system assume glass chrome, dynamic color and edge-to-edge everywhere. A lower floor forces dual designs or conservative choices [inferred].
- **Depends on (upstream):** audience device data (outside the system).
- **Affects (downstream):** DC-L10-05, DC-L10-11, DC-L10-12, DC-L10-14; QA matrix.
- **Token encoding:** version-gated values are rare; prefer runtime fallbacks (dynamic color falls back to the brand scheme below Android 12) [S-L10-019].
- **Platform notes:** Apple platforms moved to unified version numbers (26) in 2025 [S-L10-005].
- **Accessibility constraints:** older OS versions lack newer settings (e.g. nonlinear scaling before Android 14) [S-L10-071].
- **Default + heuristic:** Default to supporting the current and previous major OS, designing for the current language, and letting older OS versions degrade to their native look. Rule of thumb: design for the OS your users will have when you ship, not when you start.
- **Evidence:** [S-L10-004, S-L10-005, S-L10-018, S-L10-019, S-L10-020, S-L10-021, S-L10-023, S-L10-026, S-L10-028, S-L10-031, S-L10-032, S-L10-033, S-L10-071, S-L10-073, S-L10-076]

### DC-L10-24: Secondary form factors (watch, TV, car, XR) and desktop app shells
- **Block path:** Platforms > Scope > Secondary form factors
- **Questions the designer answers:** Does our system extend to watches, TVs, cars, headsets or glasses? For desktop, do we ship native apps or web-tech shells (Electron)?
- **Options:**
  - **Watches.** watchOS: glanceable, complications, Digital Crown, 16pt default text [S-L10-015, S-L10-011]. Wear OS: M3 Expressive with EdgeButton, arc text, black backgrounds, watch-face dynamic color [S-L10-026, S-L10-027]. Material's I/O 2026 watch guidance adds physics-based motion and edge-hugging containers [S-L10-001].
  - **TV.** tvOS focus system, 29pt text, 66pt targets, overscan safe area [S-L10-015, S-L10-011, S-L10-012, S-L10-013]. Google TV adds pointer remotes [S-L10-002]. Windows treats TVs as "small" in epx because of viewing distance [S-L10-069].
  - **Cars.** Android's Car App Library targets Android Auto and Automotive OS with templated apps [S-L10-002]. Templates limit visual customization [inferred].
  - **XR and glasses.** visionOS: windows, volumes, immersion, 60pt targets, no dark mode [S-L10-015, S-L10-012, S-L10-089]. Android XR SDK Developer Preview 4, core libraries heading to beta [S-L10-002]; Material XR guidance: spatial panels, depth-based elevation [S-L10-001]; Jetpack Compose Glimmer for display AI glasses [S-L10-001].
  - **Desktop shells.** Electron exposes native chrome options: `titleBarStyle` (hidden, hiddenInset), Window Controls Overlay, macOS vibrancy types (sidebar, menu, popover...), Windows `backgroundMaterial` (mica, acrylic, tabbed) [S-L10-078]. Native macOS expects a full menu bar and keyboard shortcuts [S-L10-015]; Windows expects Mica/Acrylic, 4/8px radii [S-L10-066, S-L10-067]. (Tauri not verified in this lane.)
- **Visual effect:** each secondary form factor strips the brand down to color, type and iconography: watches go dark and glanceable, TVs go big and focus-driven, cars go templated, XR goes glass and depth. An Electron app that ignores native chrome reads as "a website in a window" [inferred].
- **Depends on (upstream):** DC-L10-01; DC-L10-03 (only foundations travel well).
- **Affects (downstream):** extra token sets (TV type scale, watch type scale), focus-state tokens for TV, motion token variants per device class (Material spring values differ for wearables) [S-L10-024].
- **Token encoding:** device-class modes on type, target and motion tokens (`deviceClass = watch | phone | tablet | desktop | tv | xr`) [inferred from S-L10-024, S-L10-011].
- **Platform notes:** Glance widgets now span mobile, Wear OS and cars through Compose [S-L10-002].
- **Accessibility constraints:** per-platform target and text minimums above; visionOS comfort rules (no peripheral motion) [S-L10-088].
- **Default + heuristic:** Default to foundations-only support for secondary form factors (color, type roles, icons) with platform templates. Rule of thumb: the smaller or farther the screen, the fewer brand-specific components survive.
- **Evidence:** [S-L10-001, S-L10-002, S-L10-011, S-L10-012, S-L10-013, S-L10-015, S-L10-024, S-L10-026, S-L10-027, S-L10-066, S-L10-067, S-L10-069, S-L10-078, S-L10-088, S-L10-089]

### DC-L10-25: Iconography across platforms (system symbols vs one brand icon set)
- **Block path:** Foundations > Iconography > Platform mapping
- **Questions the designer answers:** Do we use SF Symbols on Apple and Material icons on Android, or one custom icon set everywhere? Which icons must stay platform-standard?
- **Options:**
  - **System icons per platform.** SF Symbols: over 7,000 symbols in 9 weights and 3 scales that align with San Francisco text, adapt to reading direction and 20+ scripts, and gain new symbols with each OS (the 27 releases) [S-L10-084]. Four rendering modes (monochrome, hierarchical, palette, multicolor), gradients since SF Symbols 7, variable color, Draw animations [S-L10-016]. Symbols scale with Dynamic Type [S-L10-011]. Apple forbids using SF Symbols (or look-alikes) in app icons or logos [S-L10-016].
  - **Standard icons for standard actions, brand icons for the rest.** Airbnb follows platform conventions for "system iconography" while staying recognizable [S-L10-044]. Apple assigns standard menu icons (Cut, Copy, Paste) from the selector automatically [S-L10-075] and asks for "standard symbols to represent common actions" [S-L10-009].
  - **One brand icon set everywhere.** Fluent treats icons as a "signature experience" that makes products "unmistakably Microsoft" [S-L10-038], and ships its own icon set across platforms [inferred; L05 owns Fluent icons].
- **Visual effect:** System symbols make toolbars and menus look native and scale perfectly with text. A brand icon set gives recognizable personality (stroke weight, corner style) but can clash with system menus, share sheets and keyboards that still use system glyphs [inferred].
- **Depends on (upstream):** DC-L10-02 (posture), L05 icon style.
- **Affects (downstream):** tab bar icons, toolbar icons, menu icons, empty-state illustrations, custom symbol production (Apple recommends custom symbols over bitmaps for sidebars) [S-L10-014].
- **Token encoding:** icon tokens map a semantic name to per-platform assets: `icon.share = { ios: "square.and.arrow.up", android: <Material name>, web: <svg> }` [inferred; the iOS name is SF Symbols' share glyph, L05 should confirm names]. Size tokens follow text styles on Apple [S-L10-011].
- **Platform notes:** share, back, more and settings glyphs differ between iOS and Android and users recognize their own platform's version [inferred]. Every icon-only control needs an accessibility label [S-L10-075].
- **Accessibility constraints:** icons must scale with text size where they carry meaning [S-L10-011]; use labels, not icons alone, for ambiguous concepts [S-L10-075].
- **Default + heuristic:** Default to platform-standard glyphs for system actions (share, back, close, more, search, settings) and a brand icon set for product-specific concepts. Rule of thumb: if the OS has a glyph for the action, use it; draw your own only for things the OS has never heard of.
- **Evidence:** [S-L10-009, S-L10-011, S-L10-014, S-L10-016, S-L10-038, S-L10-044, S-L10-075, S-L10-084]

## What should be identical vs what should adapt (synthesis)

This table summarizes where the published reasoning of multi-platform systems lands. It is a synthesis of the cards above, not a single source's rule.

| Element | Identical across platforms | Adapts per platform | Evidence |
|---|---|---|---|
| Brand color (hue, key palette) | Yes | Placement and intensity (accent-only on Apple chrome; may yield to dynamic color on Android; user accent on macOS) | [S-L10-009, S-L10-010, S-L10-019, S-L10-040] |
| Color roles (semantic names) | Yes (names and intent) | Mapping to native semantics (iOS `label`, Material `onSurface`) | [S-L10-010, S-L10-019] [inferred mapping] |
| Typography roles | Yes (role names) | Typeface for body, sizes, scaling mechanism | [S-L10-039, S-L10-011, S-L10-071] |
| Display / headline typeface | Usually yes (brand font) | Body usually system font on native | [S-L10-009, S-L10-039] |
| Spacing scale | Yes (same numbers) | Unit (pt, dp, px, epx) | [S-L10-039, S-L10-069] |
| Iconography | Brand icons for product concepts | System glyphs for system actions | [S-L10-044, S-L10-038, S-L10-075] |
| Illustration, imagery, sound | Yes (signature experiences) | Format only | [S-L10-038] |
| Voice and tone | Yes | Terminology for platform features | [S-L10-009] [inferred for terminology] |
| Motion personality (in-content) | Yes | Screen transitions, back gesture, sheet physics | [S-L10-024, S-L10-030, S-L10-040, S-L10-088] |
| Navigation | Destinations yes | Container (tab bar, nav bar, rail, sidebar, menu bar) | [S-L10-014, S-L10-025, S-L10-044] |
| Controls | Label, color, states | Shape, size, behavior, haptics | [S-L10-009, S-L10-075, S-L10-090] |
| Materials | No | Glass, Mica, tonal surfaces, solid | [S-L10-008, S-L10-066, S-L10-019] |
| Target size, text minimums | No | Per-platform minimums | [S-L10-012, S-L10-072, S-L10-036] |
| Dark mode behavior | Follow system | Watch dark-only, visionOS none | [S-L10-089, S-L10-027] |

## The platform questionnaire (for the builder)

Each question below maps to a Decision Card. "Visual consequence" is what the builder should preview when the user picks an answer.

| # | Question | Typical answers | Visual consequence | Card |
|---|---|---|---|---|
| 1 | Which platforms ship in the first release? | Web; iOS + Android; web + mobile; + desktop | Adds native chrome (glass bars, Material bars), unit sets, target minimums | DC-L10-01 |
| 2 | Do tablets, foldables and desktops matter? | No (phone only is not allowed on Android 16+ at 600dp+); yes | Rails, sidebars, 2-3 panes, list-detail layouts | DC-L10-01, DC-L10-10 |
| 3 | Native-first, brand-first, or coherent hybrid? | Three postures | Native chrome vs identical custom components everywhere | DC-L10-02 |
| 4 | What do platforms share? | Principles; tokens; component specs; component code | From "same palette, platform-shaped components" to "identical components" | DC-L10-03 |
| 5 | Where does the brand color live on each platform? | Chrome; actions only; content layer | Tinted bars vs neutral glass over colorful content | DC-L10-04 |
| 6 | Follow OS personalization (dynamic color, user accent)? | Follow; fixed; hybrid | Wallpaper-derived palettes vs constant brand screenshots | DC-L10-05 |
| 7 | System font or brand font, and where? | System; brand display + system body; brand everywhere | Native text vs strong typographic identity | DC-L10-06 |
| 8 | How far do we support text scaling? | Full; capped chrome; none | Reflowing layouts at AX sizes; stacked rows | DC-L10-07 |
| 9 | How are sizes authored and converted? | Unitless 1:1; rem-based; px-based | Identical proportions, crisp edges on fractional scales | DC-L10-08 |
| 10 | How does top-level navigation work at each size? | Tab/nav bar; rail; sidebar; menu bar | App silhouette changes by width | DC-L10-09 |
| 11 | Layout by window size or device? | Size classes; Material breakpoints; container queries | Works in split view and resizable windows | DC-L10-10 |
| 12 | Edge-to-edge and safe areas? | Always (Android mandatory) | Full-bleed content under translucent bars | DC-L10-11 |
| 13 | Platform materials or our own surfaces? | Glass/Mica/tonal; solid; custom blur | Depth and translucency vs calm solids | DC-L10-12 |
| 14 | System controls or custom-branded controls? | System; restyled; custom | Capsule glass controls vs brand-shaped controls | DC-L10-13 |
| 15 | Whose motion and back behavior? | OS transitions + brand micro-motion; one motion language | Native back gestures; bouncy vs functional feel | DC-L10-14 |
| 16 | Which inputs and densities? | Touch; pointer; keyboard; remote; spatial | Airy touch layouts vs dense pointer layouts, hover states | DC-L10-15 |
| 17 | Which OS accessibility settings do we honor? | All (recommended) | High-contrast outlines, opaque fallbacks, no parallax | DC-L10-16 |
| 18 | Dark mode per platform? | System-follow; dark-only on watch; none on visionOS | Base vs elevated dark surfaces | DC-L10-17 |
| 19 | How do tokens reach the browser? | CSS custom properties + media queries + container queries | Runtime theme switching, component-level responsiveness | DC-L10-18 |
| 20 | Framework or web components? | React etc.; web components; host-rendered | Consistency across heterogeneous stacks | DC-L10-19 |
| 21 | Which native toolkits? | SwiftUI/UIKit; Compose/Views; WinUI | Access to newest platform visuals first | DC-L10-20 |
| 22 | Cross-platform framework? | None; React Native; Flutter; CMP; MAUI | Native views vs self-drawn widgets and OS-update lag | DC-L10-21 |
| 23 | Which build outputs? | CSS, Swift, Compose, XML, Dart, JS | None directly; fidelity of values | DC-L10-22 |
| 24 | Minimum OS versions? | Current + previous major; older | Assume glass, dynamic color, edge-to-edge or not | DC-L10-23 |
| 25 | Watch, TV, car, XR, desktop shell? | None; foundations only; full | Dark glanceable, focus-driven, templated, spatial | DC-L10-24 |
| 26 | System glyphs or brand icons? | System; mixed; brand | Native menus vs recognizable icon personality | DC-L10-25 |

## Decision graph (what drives what)

Edges the builder's causality graph should encode. "A -> B" means "choosing A constrains or changes B". All edges are drawn from the cards above; edge strength is [inferred].

- Target platforms (DC-01) -> unit set (DC-08), navigation containers (DC-09), breakpoint family (DC-10), target-size tokens (DC-15), token build outputs (DC-22), accessibility test matrix (DC-16).
- Target platforms includes Android -> large-screen layouts mandatory (DC-10) [S-L10-021] -> navigation rail/sidebar components required (DC-09).
- Target platforms includes Apple, built with 27 SDKs -> Liquid Glass chrome mandatory (DC-12, DC-13) [S-L10-076] -> brand color moves to actions and content (DC-04) [S-L10-009].
- Posture (DC-02) -> sharing layer (DC-03) -> framework choice (DC-21) and component tech (DC-19).
- Posture native-first -> system fonts for body (DC-06), system controls (DC-13), OS transitions (DC-14), system glyphs (DC-25).
- Posture brand-first -> custom controls (DC-13) -> must re-implement accessibility semantics (DC-16) and OS visual updates (DC-23).
- Brand color (L01) + posture -> brand color placement (DC-04) -> button, tab indicator, badge, app bar tokens.
- Personalization policy (DC-05) -> which color roles are static vs generated -> QA matrix size.
- Typeface (DC-06) -> text scaling support effort (DC-07) -> component min-heights and list layouts.
- Unit policy (DC-08) -> every dimension token and the transforms in DC-22.
- Window-size strategy (DC-10) -> navigation swaps (DC-09), dialog vs full-screen dialog, bottom sheet vs menu [S-L10-025].
- Edge-to-edge (DC-11) + materials (DC-12) -> bar backgrounds (scroll edge effect vs scrim vs solid), hero imagery bleed.
- Accessibility settings (DC-16) -> token modes (contrast, transparency, motion) -> border and focus tokens must not rely on shadow or translucency [S-L10-031].
- OS version floor (DC-23) -> availability of dynamic color (Android 12), nonlinear scaling (Android 14), edge-to-edge (15), predictive back (16), glass (Apple 26).
- Secondary form factors (DC-24) -> device-class token modes (type, targets, motion springs) [S-L10-024].

## Baked-in platform rules (device conventions the builder should generate by default)

The schema asks the builder to bake in device conventions. These are the rules this lane can state with a source; each is a default the builder should apply unless the user overrides it.

1. Minimum hit area per platform: iOS/iPadOS/watchOS 44pt, macOS 28pt, tvOS 66pt, visionOS 60pt [S-L10-012]; Android 48dp [S-L10-072]; web 24 CSS px floor (AA), 44 recommended [S-L10-036].
2. Minimum text size per platform: iOS 11pt, macOS 10pt, watchOS/visionOS 12pt, tvOS 23pt [S-L10-011].
3. Text uses scalable units: Apple text styles, Android sp (line height in sp too), web rem [S-L10-011, S-L10-071, S-L10-074].
4. Never use sp or rem for spacing that must not scale with text on Android [S-L10-070].
5. Layout decisions use window size (size class or breakpoint), never device type or orientation [S-L10-013, S-L10-022].
6. Edge-to-edge on Android with inset-aware components; safe areas on Apple; tvOS 60/80pt overscan insets [S-L10-023, S-L10-013].
7. No touch targets under system gesture insets [S-L10-030].
8. Glass only on the functional layer (bars, controls, sheets), never on reading surfaces; clear glass over bright media gets a 35% dim layer [S-L10-008].
9. Every icon-only control gets an accessibility label [S-L10-075].
10. Focus indicators must not rely on box-shadow alone (forced colors removes shadows) [S-L10-031].
11. Follow the system appearance; don't add an app-only light/dark switch on Apple [S-L10-089].
12. Watch UIs default to dark/black backgrounds [S-L10-027, S-L10-089].
13. Swap navigation containers by width: bar at compact, rail at medium/expanded, expanded rail or sidebar at large/XL [S-L10-025].
14. Keep 40-60 characters per line at every breakpoint [S-L10-025].
15. Multiples of 4 for dimensions (crisp at Windows scale plateaus; aligns with Fluent's ramp) [S-L10-069, S-L10-039].
16. Honor Reduce Motion / Reduce Transparency / Increase Contrast / prefers-contrast / forced-colors with defined fallbacks [S-L10-012, S-L10-008, S-L10-031, S-L10-033].
17. Don't encode the brand as a logo in bars or a branded launch screen on Apple [S-L10-009].

## Community signal reconciliation (against `sources/COMMUNITY-SIGNAL.md`, read 2026-09-23 ~15:05)

- **I/O 2026 claims that L00 marked "unverified" are now confirmed by this lane.** L00 could not render m3.material.io/blog/whats-new-at-io26 [COMMUNITY-SIGNAL d]. This lane rendered it in a browser (dated May 19, 2026) and confirmed the Expressive layout system, the new 8dp spacing system, watch and XR guidance, expressive lists and menus, "Material Android is Compose-first", and a planned stable Compose release with "14 expressive components" and Styles API integration [S-L10-001]. The Android Developers Blog independently states "Android is now Compose First; Views are now in maintenance mode" [S-L10-002], and the April 2026 Compose release confirms the experimental Styles API [S-L10-080].
- **Compose Material 3 versions agree.** Both lanes found 1.4.0 stable (2025-09-24) and 1.5.0-alpha28 (2026-09-09), and both caught the WebFetch summary misdating 1.4.0 to "September 09, 2026" [S-L10-018]. Nothing in this lane claims a stable Compose release ships full M3 Expressive without opt-ins.
- **Liquid Glass timeline agrees and is extended.** L00 reports an iOS 26.1 Clear/Tinted choice (Oct 2025) and iOS 27 public release around 14 Sep 2026 [S-L00-019, S-L00-048] (L00's ids; not re-verified here). This lane adds Apple's own confirmation of the 27 betas on June 8, 2026 and the transparency slider [S-L10-004], and the decisive developer fact that the 27 SDKs ignore `UIDesignRequiresCompatibility` [S-L10-076].
- **HIG change-log dates.** L00 did not see a change-log date for HIG Materials. The DocC JSON read by this lane shows "September 9, 2025: Updated guidance for Liquid Glass" [S-L10-008]. Branding and Layout were both updated September 9, 2026 [S-L10-009, S-L10-013].
- **Disputed in the community (flag for the builder, not facts):** some users now say Apple "toned down Liquid Glass too much" in iOS 27, and some report better fluidity with Reduce Transparency on [S-L00-048]. Treat glass intensity as a user-controlled range, which DC-L10-05 and DC-L10-12 already require. iOS developers push back on porting M3 Expressive styling to iOS [S-L00-046], which supports the coherent-hybrid default in DC-L10-02.
- **Material Web.** L00 notes Material Web v2.5.0 (15 Jul 2026) [S-L00-042]. That is consistent with maintenance mode (fixes, no roadmap) announced June 2024 [S-L10-079]; M3 Expressive and the motion physics system are not offered as web components [S-L10-024].

## Cross-lane notes

- [L10 -> L01] Apple's Sept 9, 2026 branding guidance moves brand color out of chrome and into the content layer beneath Liquid Glass; accent goes on the background of prominent buttons, not glyphs [S-L10-009, S-L10-010]. macOS replaces the app accent with the user's accent unless it's "multicolor" [S-L10-010]. Both belong in L01's brand-vs-UI color cards.
- [L10 -> L02] Fluent's cross-platform ramp is the best published example of "shared role names, per-platform values": Body 1 = 14/20px (web), 17/22pt (iOS), 16/24sp (Android) [S-L10-039]. Apple's Dec 16, 2025 HIG change added "emphasized weights" to every Dynamic Type style [S-L10-011]. Android 16 ignores `elegantTextHeight` for tall scripts [S-L10-020].
- [L10 -> L03] Material says breakpoints "apply to Android and web" [S-L10-025]. Windows epx breakpoints (640/1007) put TVs in "small" because of viewing distance [S-L10-069]. Android 17 makes large-screen resizability non-optional [S-L10-021].
- [L10 -> L04] Material spring token values differ by device class (wearable, phone, tablet) [S-L10-024]. Predictive back full-screen spec: exit 100 to 90%, enter 110 to 100%, fade at 35% [S-L10-030]. Windows radii 4px controls / 8px overlays, 0 when snapped [S-L10-067]. Clear glass needs a 35% dim layer over bright content [S-L10-008].
- [L10 -> L05] SF Symbols now has 7,000+ symbols, 9 weights, 3 scales, and new symbols for the 27 releases; Apple's page no longer shows a version number [S-L10-084]. Apple forbids SF Symbols in logos and app icons [S-L10-016].
- [L10 -> L07] Style Dictionary v5 transform groups exist for android, compose, ios-swift, flutter and react-native, all assuming base font size 16 [S-L10-057]. Built-in iOS output is UIKit-flavored; SwiftUI and Material `ColorScheme` outputs need custom formats [inferred]. A `platform` axis in the resolver is needed for per-platform typeface, target and type-size values.
- [L10 -> L08] Apple renamed and restyled several components under Liquid Glass: action sheets now originate from their source control, half sheets are inset, list section headers are title case, and search is a trailing tab [S-L10-075]. Material swaps components by breakpoint (bar to rail, bottom sheet to menu, full-screen dialog to dialog) [S-L10-025]. Check whether shadow DOM affects ARIA references for web-component systems (DC-L10-19).
- [L10 -> L09] For the benchmark matrix: Uber Base ships to 7 stacks (UIKit, SwiftUI, Android XML, Compose, Web React, Go, SDUI) with one spec per component [S-L10-046]; Polaris moved from React to web components (stable 2025-10) and renders natively in POS [S-L10-047, S-L10-048]; SLDS 2 replaced design tokens with CSS custom property "styling hooks" [S-L10-052].
- [L10 -> L11] Governance consequence of OS mandates: Apple's opt-out ends with the 27 SDKs and Android's large-screen opt-out ends at API 37, so a design system needs a yearly "platform release" review each June (WWDC, Android stable now in June) [S-L10-076, S-L10-021, S-L10-028] [inferred for the process].
- [L10 -> L12] The Figma iOS 26 kit should be checked for Liquid Glass regular vs clear variants and the tab bar's minimized state [S-L10-008, S-L10-014].
- [L10 -> L00] HIG Materials change log is visible in the DocC JSON: 2025-09-09 [S-L10-008]. I/O 2026 blog claims are now verified [S-L10-001].

## Open questions / gaps

- **Tauri** window theming and native-chrome options weren't verified (WebSearch budget ran out); only Electron is covered [S-L10-078, S-L10-086].
- **Windows target minimum** isn't stated on the Microsoft Learn pages read; Fluent only gives iOS/web 44 and Android 48 [S-L10-039]. Windows accent-color API behavior wasn't checked.
- **Wear OS** minimum target and margin percentages weren't on the page read [S-L10-027].
- **Material color values for Expressive** and the M3 Expressive typography changes (emphasized styles) are owned by L01/L02 and weren't re-checked here.
- **Airbnb's current (2024-26) cross-platform stance** isn't documented publicly beyond the 2016-era Saarinen material [S-L10-043, S-L10-044]; Airbnb's 2025 redesign reasoning wasn't found.
- **Atlassian's and Salesforce's native mobile** design guidance isn't public on the pages read; their public systems are web-first [S-L10-050, S-L10-052].
- **Container size queries' Baseline date** relies on a secondary source (about Aug 2025) [S-L10-035].
- **iOS 27 details** (uniform toolbar, optional icon refraction, macOS/iPadOS menu icons) come from MacRumors reporting of the keynote and State of the Union, not from Apple docs [S-L10-003]. The HIG pages read don't yet describe the transparency slider by name; they refer to "a preferred look for Liquid Glass" [S-L10-008].
- **React Native current version**: the docs read are v0.87 [S-L10-063]; the New Architecture default and Expo specifics weren't checked.
- **Flutter `useMaterial3` default version** wasn't stated on the page read [S-L10-091].
- **Web equivalent of dynamic color**: none found; this is stated as [inferred].
- **Perplexity was unavailable** (quota) and **WebSearch hit its session cap** (200/200) near the end, so late verification used WebFetch and curl on known URLs only [S-L10-000, S-L10-086].

## Confidence

- **Confirmed from Tier A sources read today:** Apple per-platform text sizes, Dynamic Type tables, target sizes, materials guidance, branding guidance (Sept 2026), dark mode rules, `UIDesignRequiresCompatibility` being ignored at the 27 SDKs, Liquid Glass adoption guidance, iPadOS 26 windowing and menu bar; Android 15/16/17 behavior changes, window size classes, density buckets, nonlinear font scaling, predictive back specs, Compose Material 3 versions (from the raw release page), M3 motion physics and breakpoints (browser-rendered m3.material.io); Fluent principles, type ramps, spacing and token tiers; Windows materials, geometry, spacing, epx; MDN media features and units; WCAG 2.2 target sizes; Style Dictionary v5 formats and transforms; Flutter decoupling and theming; Compose Multiplatform 1.8; React Native `PlatformColor` and text scaling; Shopify Polaris unification and POS rendering; Uber Base stacks; Material Web and MDC-iOS maintenance status.
- **Tier B, corroborated:** iOS 27 Liquid Glass changes (MacRumors, consistent with Apple Newsroom); Android 17 stable date (two tech outlets); Spotify's coherence model (Figma blog by Spotify's design systems manager); Airbnb quotes (Google Design library, Saarinen's own site).
- **Snippet-level (flagged):** Salesforce SLDS 2 styling hooks and "web and native" token history; NativeWind v5 and Unistyles 3 status; Wear M3 Expressive blog; container-query Baseline date.
- **Inferred (marked [inferred] in text):** the 1:1 pt/dp/px convention as a builder rule, token-encoding shapes (platform modes, material composites, icon maps), visual-effect descriptions of brand-first vs native-first, default heuristics, and all decision-graph edge strengths.
