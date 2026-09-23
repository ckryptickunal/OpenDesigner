# Apple Human Interface Guidelines (incl. Liquid Glass)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Apple (Human Interface Guidelines at developer.apple.com/design) | [S-L09-147] |
| Launch and major versions | HIG is a living document; origin date not checked this session. Liquid Glass design announced 2025-06-09 with unified version 26 (iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26); version 27 announced at WWDC 2026 on 2026-06-08 | [S-L09-153] [S-L09-152] |
| Current version (Sept 2026) | iOS / iPadOS / macOS / watchOS / visionOS / tvOS 27 released 2026-09-14; latest HIG change-log entry 2026-09-18 (iPhone Duo and iPhone 18 bezels) | [S-L09-164] [S-L09-147] |
| Platforms | iOS, iPadOS, macOS, watchOS, tvOS, visionOS; new "Designing for iPhone Duo" (first folding iPhone) page 2026-09-09 | [S-L09-147] |
| Open source + license | No. Proprietary guidelines; SF fonts and UI kits are free downloads from Apple Design Resources | [S-L09-149] |
| Code frameworks | SwiftUI, UIKit, AppKit. Liquid Glass APIs: `glassEffect(_:in:)`, `UIGlassEffect`, `NSGlassEffectView`, `GlassEffectContainer`; `ConcentricRectangle` (all 26.0+) | [S-L09-157] [S-L09-159] [S-L09-158] |
| Figma kit | Official Apple Design Resources: iOS and iPadOS 27 and macOS 27 UI Kits for Figma (2026-09-17) and Sketch; iOS 26 Figma kit shipped 2025-07-18; watchOS 26 and visionOS 26 Figma kits 2025-08-20; tvOS 18 kit is Sketch-only. iOS Figma kit gained Increased Contrast color modes on 2024-10-17 (modes imply Figma variables [inferred]) | [S-L09-147] [S-L09-149] [S-L09-151] |
| Token tiers + naming | No public token files. De-facto 2 layers exposed as API names: system colors (`systemBlue`, `systemGray2`) and semantic dynamic colors (`label`, `secondaryLabel`, `systemBackground`, `separator`); text styles (`.largeTitle`, `.body`); materials (`ultraThin`..`thick`); glass (`.regular`, `.clear`, `.identity`) | [S-L09-142] [S-L09-141] [S-L09-159] |
| Color model | sRGB or Display P3 profiles. 12 system hues + Gray..Gray 6, each with 4 variants: light, dark, increased-contrast light, increased-contrast dark. Blue light = 0,136,255 (#0088FF), dark 0,145,255. iOS grays are cool (blue channel +5): systemGray 142,142,147, Gray 6 light 242,242,247, Gray 6 dark 28,28,30. iOS semantic set: 8 foreground (label x4, placeholderText, separator, opaqueSeparator, link) + 6 backgrounds (system and grouped x3); macOS 31+ dynamic colors. Accent: one app accent/tint color applied by the system | [S-L09-142] |
| Typeface | San Francisco: SF Pro (iOS, iPadOS, macOS, tvOS), SF Compact (watchOS), SF Mono, SF Arabic/Armenian/Georgian/Hebrew, rounded variants; New York serif. Variable fonts with dynamic optical sizes. System, Apple-owned | [S-L09-140] [S-L09-149] |
| Type scale | 11 Dynamic Type styles. iOS at Large (size/leading pt): Large Title 34/41, Title 1 28/34, Title 2 22/28, Title 3 20/25, Headline 17/22 semibold, Body 17/22, Callout 16/21, Subhead 15/20, Footnote 13/18, Caption 1 12/16, Caption 2 11/13. macOS: Large Title 26/32, Title 1 22/26, Title 2 17/22, Title 3 15/20, Headline 13/16 bold, Body 13/16, Callout 12/15, Subheadline 11/14, Footnote 10/13, Caption 1 10/13, Caption 2 10/13 medium. Hand-tuned. 12 Dynamic Type sizes (xSmall..xxxLarge + AX1..AX5): iOS Body runs 14pt to 53pt. Emphasized weights (Bold for titles, Semibold for text) added 2025-12-16 | [S-L09-140] |
| Spacing | No published spacing scale and no 8pt grid rule in the Layout page; the 8pt grid is a community convention [inferred]. Stated values: ~12pt padding around bezeled elements, ~24pt around unbezeled; tvOS safe inset 60pt top/bottom, 80pt sides, 40pt column gap, 100pt min row gap; visionOS 60pt between control centers. Layout relies on safe areas, layout guides, size classes | [S-L09-144] [S-L09-145] |
| Radius | No numeric radius scale published. iOS 26 rule is concentricity: a corner shares its center with the container's (device, window, sheet) corner; `ConcentricRectangle` computes it. Sheets and grouped sections got increased radii in 26 | [S-L09-158] [S-L09-157] [S-L09-153] |
| Elevation | Materials, not shadows. Liquid Glass (regular, clear) is a separate functional layer for controls and navigation; content layer uses ultraThin / thin / regular (default) / thick; clear glass over bright media needs a 35% dark dimming layer; Dark Mode uses base vs elevated background sets; visionOS uses a system glass material | [S-L09-141] [S-L09-163] |
| Motion | HIG publishes no numeric durations or springs. SwiftUI defaults: `spring(duration: 0.5, bounce: 0.0)`; `.smooth` bounce 0, `.snappy` 0.15, `.bouncy` 0.3, all 0.5s; also `Spring(response:dampingRatio:)`. Reduce Motion: tighten springs, replace x/y/z moves with fades, avoid animating blur and z-depth. Liquid Glass reacts more strongly to touch than trackpad | [S-L09-143] [S-L09-154] [S-L09-155] [S-L09-156] [S-L09-145] |
| Theming + modes | Light/Dark, Increased Contrast, Reduce Transparency, Reduce Motion, Dynamic Type (>= 200%); iOS 27 adds a Liquid Glass slider from ultra-clear to fully tinted; app accent color; per-platform idioms. Switched by the OS, not by the app | [S-L09-145] [S-L09-152] [S-L09-142] |
| Component count | 64 component pages in 8 categories (Content 4, Layout 10, Menus and actions 12, Navigation and search 5, Presentation 8, Selection and input 11, Status 4, System experiences 10), counted 2026-09-23 | [S-L09-162] |
| Component doc structure | Intro, Best practices, topic sections (e.g. Style, Content, Role), Platform considerations (per OS), Resources, Change log | [S-L09-162] |
| Accessibility stance | WCAG AA contrast: 4.5:1 up to 17pt, 3:1 at 18pt+ or bold. Hit targets default/min: iOS 44x44 / 28x28 pt, macOS 28x28 / 20x20, tvOS 66x66 / 56x56, visionOS 60x60 / 28x28, watchOS 44x44 / 28x28. Min text iOS 11pt, macOS 10pt | [S-L09-145] |
| Governance / contribution | Closed, central Apple team. Cadence: big update at WWDC each June, device updates each September; dated change log on every page | [S-L09-147] |
| Notable innovation | Liquid Glass: real-time rendered, specular, content-adaptive material as its own UI layer; concentric geometry tied to hardware corners; Dynamic Type; unified "26" version numbers across 5+ OSes | [S-L09-153] [S-L09-141] [S-L09-158] |

## Visual signature: why it looks like this
- Controls float on Liquid Glass (regular = blurred, luminosity-adjusted; clear = highly translucent) above full-bleed content -> content-first screens where chrome feels like lenses, not panels [S-L09-141] [S-L09-157].
- Monochrome glyphs and text on glass, color only on the primary action background -> calm, mostly gray UI with one accent hit per screen [S-L09-142].
- Concentric corner radii derived from the device and window corners -> nested shapes that echo the hardware silhouette [S-L09-158] [S-L09-153].
- SF Pro at 17pt body with tight, hand-tuned leading (17/22) and a 34pt Large Title (Bold as the emphasized weight) -> dense but very legible text under big navigation titles [S-L09-140].
- Saturated, bright system hues (blue #0088FF, red 255,56,60) used sparingly on white, cool gray (#F2F2F7) or near-black (#1C1C1E) -> crisp, high-energy accents without colored surfaces [S-L09-142].
- Critically damped default springs (bounce 0, 0.5s) with optional snappy/bouncy -> smooth, physical motion that follows the finger [S-L09-154] [S-L09-155].

## Recent changes 2024-2026
- 2024-10-17: iOS UI Kit for Figma adds modes for Increased Contrast color values [S-L09-147].
- 2025-03-07: Accessibility guidance expanded; Dynamic Type moved to Typography; new VoiceOver page [S-L09-145].
- 2025-06-09: Liquid Glass introduced across iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26; system color values updated (blue moved to 0,136,255); Materials, Color, Layout pages rewritten [S-L09-153] [S-L09-142] [S-L09-147].
- 2025-06-09: iOS and iPadOS 26 and macOS 26 UI kits for Sketch rebuilt with Liquid Glass; Icon Composer and SF Symbols 7 beta [S-L09-147].
- 2025-07-18: iOS and iPadOS 26 kits for Figma released [S-L09-151]. 2025-08-20: watchOS and visionOS kits for Figma [S-L09-147].
- 2025-07-28: Liquid Glass guidance for tab bars; scroll edge effects added to Scroll views; menu item icons; SF Symbols 7 Draw animations [S-L09-147].
- 2025-09-09: Liquid Glass motion and materials guidance updated; iPhone 17 / iPhone Air specs [S-L09-147].
- 2025-12-16: emphasized weights added to Dynamic Type specs; color guidance updated for Liquid Glass [S-L09-140] [S-L09-142].
- 2026-06-08 (WWDC 2026): version 27 for all six OSes; Liquid Glass personalization slider (ultra-clear to fully tinted); sharper app icons; macOS regains uniform toolbar, edge-to-edge sidebars, colored sidebar icons; Icon Composer 2 beta, SF Symbols 8 beta; design principles reintroduced [S-L09-152] [S-L09-147].
- 2026-06-23: iOS/iPadOS 27 and macOS 27 kits for Figma updated during the beta cycle [S-L09-147].
- 2026-09-09: "Designing for iPhone Duo" page (poses, dual displays, vertical toolbars and tab bars); Layout and Branding refreshed [S-L09-147] [S-L09-144].
- 2026-09-14: 27 releases shipped [S-L09-164]. 2026-09-17: iOS/iPadOS 27 and macOS 27 Figma kits [S-L09-147].

## Builder takeaways
- Offer a "materials instead of shadows" elevation preset: a glass layer for navigation and controls, 4 content materials, plus base/elevated dark backgrounds [S-L09-141] [S-L09-163].
- Every color token should carry 4 values (light, dark, increased-contrast light, increased-contrast dark); Apple ships all four for every system hue [S-L09-142].
- Express motion as duration + bounce (0 / 0.15 / 0.3 presets) rather than stiffness/damping; it is easier for designers [S-L09-155].
- Offer concentric radius (child radius = parent radius minus inset) as a rule, and ask users for hit targets per platform: defaults 44 / 28 / 60 pt (iOS / macOS / visionOS), minimums 28 / 20 / 28 pt [S-L09-158] [S-L09-145] [S-L09-714].

## Gaps / unverified
- No official spacing or radius token scale exists; the 8pt grid is not an Apple rule [S-L09-144].
- Increased-contrast values exist for the 12 hues and iOS grays, but macOS dynamic color RGB values were not captured [S-L09-142].
- Liquid Glass material parameters (blur radius, refraction strength, tint opacity) are not public; only the 35% dimming guidance is [S-L09-141].
- macOS 27 has no marketing name in the newsroom posts read [S-L09-152] [S-L09-164].
- HIG origin date and pre-2024 history not verified this session.
