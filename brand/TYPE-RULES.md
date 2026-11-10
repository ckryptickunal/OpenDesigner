# Type rules: Apple and Google

What Apple and Google publish about type sizes, type scales, named roles and weights. Every visual we make follows these rules.

- Checked against live sources on 2026-10-14. Every number below comes from a page or file opened that day.
- **[inferred]** means our recommendation, not a platform rule. **[computed]** means arithmetic on verified numbers. **[unverified]** means it was not confirmed live.
- "Repo" means `research/L02-typography.md` (cards DC-L02-01..28) and `skills/opendesigner/references/stages/11-type-scale-and-text.md`.
- Apple's HIG pages are rendered by JavaScript, so they were read from Apple's own JSON endpoints (`developer.apple.com/tutorials/data/...`). The Material 3 site was read from the JSON its pages load (`m3.material.io/_dsm/...`). The Material token module was read with the **3p** (third-party) audience, which is the setting for products outside Google.

---

## 1. Apple text styles

### 1a. iOS and iPadOS, Dynamic Type default size (Large)

| Text style (SwiftUI name) | Size pt | Leading pt | Weight | Emphasized weight |
|---|---|---|---|---|
| Large Title (`.largeTitle`) | 34 | 41 | Regular | Bold |
| Title 1 (`.title`) | 28 | 34 | Regular | Bold |
| Title 2 (`.title2`) | 22 | 28 | Regular | Bold |
| Title 3 (`.title3`) | 20 | 25 | Regular | Semibold |
| Headline (`.headline`) | 17 | 22 | Semibold | Semibold |
| Body (`.body`) | 17 | 22 | Regular | Semibold |
| Callout (`.callout`) | 16 | 21 | Regular | Semibold |
| Subhead (`.subheadline`) | 15 | 20 | Regular | Semibold |
| Footnote (`.footnote`) | 13 | 18 | Regular | Semibold |
| Caption 1 (`.caption`) | 12 | 16 | Regular | Semibold |
| Caption 2 (`.caption2`) | 11 | 13 | Regular | Semibold |

Source: https://developer.apple.com/design/human-interface-guidelines/typography (Specifications > iOS, iPadOS Dynamic Type sizes > Large (default); read from https://developer.apple.com/tutorials/data/design/human-interface-guidelines/typography.json; latest change log entry is 2025-12-16, "Added emphasized weights"). SwiftUI names: https://developer.apple.com/documentation/swiftui/font/textstyle

- The HIG table calls the style "Subhead"; the SwiftUI API calls it `subheadline`.
- You get emphasized weights with the bold trait (`bold()` in SwiftUI, `traitBold` in UIKit). Apple says they "can be medium, semibold, bold, or heavy".
- Repo check: the sizes and leading match the repo (L02 Table 2, DC-L02-07). The repo mentions emphasized weights but doesn't list them per style. They are now in this table.

**How the styles scale (selected Dynamic Type sizes, size/leading in pt)**

| Style | xSmall | Large (default) | xxxLarge | AX5 (largest) |
|---|---|---|---|---|
| Large Title | 31/38 | 34/41 | 40/48 | 60/70 |
| Title 1 | 25/31 | 28/34 | 34/41 | 58/68 |
| Body | 14/19 | 17/22 | 23/29 | 53/62 |
| Footnote | 12/16 | 13/18 | 19/24 | 44/52 |
| Caption 2 | 11/13 | 11/13 | 17/22 | 40/48 |

Source: https://developer.apple.com/design/human-interface-guidelines/typography (Specifications, all iOS size tabs)

- Large styles grow less than body text. Body grows 3.1x from Large to AX5, Large Title only 1.8x [computed]. Repo check: matches DC-L02-21.

### 1b. macOS built-in text styles (macOS doesn't support Dynamic Type)

| Text style | Size pt | Line height pt | Weight | Emphasized weight |
|---|---|---|---|---|
| Large Title | 26 | 32 | Regular | Bold |
| Title 1 | 22 | 26 | Regular | Bold |
| Title 2 | 17 | 22 | Regular | Bold |
| Title 3 | 15 | 20 | Regular | Semibold |
| Headline | 13 | 16 | **Bold** | Heavy |
| Body | 13 | 16 | Regular | Semibold |
| Callout | 12 | 15 | Regular | Semibold |
| Subheadline | 11 | 14 | Regular | Semibold |
| Footnote | 10 | 13 | Regular | Semibold |
| Caption 1 | 10 | 13 | Regular | Medium |
| Caption 2 | 10 | 13 | Medium | Semibold |

Source: https://developer.apple.com/design/human-interface-guidelines/typography (Specifications > macOS built-in text styles)

### 1c. watchOS text styles at the default sizes for each case size

| Style | Large: default on 40, 41, 42 mm (size/leading pt) | xLarge: default on 44, 45, 49 mm (size/leading pt) | Weight | Emphasized |
|---|---|---|---|---|
| Large Title | 36/38.5 | 40/42.5 | Regular | Bold |
| Title 1 | 34/36.5 | 38/40.5 | Regular | Semibold |
| Title 2 | 28/30.5 | 30/32.5 | Regular | Semibold |
| Title 3 | 19/21.5 | 20/22.5 | Regular | Semibold |
| Headline | 16/18.5 | 17/19.5 | Semibold | Semibold |
| Body | 16/18.5 | 17/19.5 | Regular | Semibold |
| Caption 1 | 15/17.5 | 16/18.5 | Regular | Semibold |
| Caption 2 | 14/16.5 | 15/17.5 | Regular | Semibold |
| Footnote 1 | 13/15.5 | 14/16.5 | Regular | Semibold |
| Footnote 2 | 12/14.5 | 13/15.5 | Regular | Semibold |

Source: https://developer.apple.com/design/human-interface-guidelines/typography (Specifications > watchOS Dynamic Type sizes; "Small" is the default on 38 mm). The system font is SF Compact, and complications use SF Compact Rounded.

- The page names only 38, 40/41/42 and 44/45/49 mm. It lists no other case sizes.
- Repo check: the repo gives the watchOS default as 16 pt. That is right for 41 mm (Large). On 45 and 49 mm the default is xLarge, where Body is 17 pt. The repo doesn't say this.

### 1d. Apple default and minimum text sizes

| Platform | Default (body) size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Source: https://developer.apple.com/design/human-interface-guidelines/typography ("Ensuring legibility"). The same table is at https://developer.apple.com/design/human-interface-guidelines/accessibility

- The minimums apply "for both custom and system fonts". For a custom font with a thin weight, "aim for larger than the recommended sizes".
- Text enlargement: "Ideally, give people the option to enlarge text by at least 200 percent (or 140 percent in watchOS apps)" (Accessibility page).
- Repo check: the sizes match DC-L02-20. The repo's "Apple asks for at least 200%" (stage 11, Q-type-17) leaves out watchOS's 140%.

---

## 2. Apple tracking and weights

### 2a. SF Pro tracking (iOS, iPadOS, visionOS) at key sizes

| Size pt | Tracking (1/1000 em) | Tracking pt | CSS `letter-spacing` [computed] |
|---|---|---|---|
| 6 | +41 | +0.24 | 0.041em |
| 11 | +6 | +0.06 | 0.006em |
| 12 | 0 | 0 | 0 |
| 13 | -6 | -0.08 | -0.006em |
| 15 | -16 | -0.23 | -0.016em |
| 17 | -26 | -0.43 | -0.026em |
| 20 | -23 | -0.45 | -0.023em |
| 22 | -12 | -0.26 | -0.012em |
| 24 | +3 | +0.07 | 0.003em |
| 28 | +14 | +0.38 | 0.014em |
| 34 | +12 | +0.40 | 0.012em |
| 48 | +8 | +0.35 | 0.008em |
| 64 | +4 | +0.22 | 0.004em |
| 80 and up (to 96) | 0 | 0 | 0 |

Source: https://developer.apple.com/design/human-interface-guidelines/typography (Specifications > Tracking values > SF Pro)

- Tightest at 17-20 pt, positive again from 24 pt, and 0 from 80 pt.
- The macOS SF Pro table is the same, except that the 52 pt and 53 pt point values are swapped.
- Apple: "In a running app, the system font dynamically adjusts tracking at every point size." You only adjust it by hand in mockups.
- These values are for SF Pro. They don't carry over to other fonts [inferred].
- Repo check: matches DC-L02-14.

### 2b. Apple weight guidance

| Rule | Apple's words (paraphrased unless quoted) |
|---|---|
| Avoid light weights | "In general, avoid light font weights." Prefer Regular, Medium, Semibold or Bold. Avoid Ultralight, Thin and Light, "which can be difficult to see, especially when text is small." |
| Thin custom fonts | Use sizes larger than the minimums. |
| Hierarchy | Adjust weight, size and colour to show hierarchy. Keep the hierarchy when people change the text size. |
| Extra level | The bold trait "adds weight to text, letting you create another level of hierarchy." |
| Typefaces | "Minimize the number of typefaces you use." |
| Leading | Use loose leading for wide columns and long passages, and tight leading only where height is limited. "If you need to display three or more lines of text, avoid tight leading." |
| visionOS | Uses bolder versions of the body and title styles, and adds Extra Large Title 1 and 2 for editorial layouts. This page publishes no size table for visionOS. |

Source: https://developer.apple.com/design/human-interface-guidelines/typography

---

## 3. Material 3 type scale

### 3a. Baseline styles (15)

| Token (`md.sys.typescale.*`) | Size sp (= px on web) | Line height | Weight | Tracking, site 3p (Roboto) | Tracking, Compose v0_103 | Web em [computed from 3p] |
|---|---|---|---|---|---|---|
| display-large | 57 | 64 | 400 | -0.25 | -0.2 | -0.0044em |
| display-medium | 45 | 52 | 400 | 0 | 0 | 0 |
| display-small | 36 | 44 | 400 | 0 | 0 | 0 |
| headline-large | 32 | 40 | 400 | 0 | 0 | 0 |
| headline-medium | 28 | 36 | 400 | 0 | 0 | 0 |
| headline-small | 24 | 32 | 400 | 0 | 0 | 0 |
| title-large | 22 | 28 | 400 | 0 | 0 | 0 |
| title-medium | 16 | 24 | 500 | 0.15 | 0.2 | 0.0094em |
| title-small | 14 | 20 | 500 | 0.1 | 0.1 | 0.0071em |
| body-large | 16 | 24 | 400 | 0.5 | 0.5 | 0.0313em |
| body-medium | 14 | 20 | 400 | 0.25 | 0.2 | 0.0179em |
| body-small | 12 | 16 | 400 | 0.4 | 0.4 | 0.0333em |
| label-large | 14 | 20 | 500 | 0.1 | 0.1 | 0.0071em |
| label-medium | 12 | 16 | 500 | 0.5 | 0.5 | 0.0417em |
| label-small | 11 | 16 | 500 | 0.5 | 0.5 | 0.0455em |

Sources:
- Page: https://m3.material.io/styles/typography/type-scale-tokens
- Token module: https://m3.material.io/_dsm/data/dsdb-m3/2026-09-23_06-10-05/TYPOGRAPHY.20543ce18892f7d9.json (design-system revision 2026-05-27)
- Shipped code: https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens/TypeScaleTokens.kt (`VERSION: v0_103`, last commit 2026-08-05)

- **The token module has an audience setting.** Its default audience is Google's own products. There, display through title-large use Google Sans, smaller styles use Google Sans Text, and tracking is 0 except 0.1 on body-small, label-medium and label-small. With the third-party audience, every style uses Roboto with the tracking shown above. Sizes, line heights and weights are the same in every setting.
- **Repo check:**
  - The repo (DC-L02-14, "Open questions") describes only the Google Sans view and the Compose values, and asks which is canonical. The live 3p setting answers it: products outside Google use Roboto with the tracking above.
  - Compose v0_103 still differs from the site on three styles: display-large -0.2 vs -0.25, title-medium 0.2 vs 0.15, body-medium 0.2 vs 0.25.

### 3b. Emphasized styles (15, added in the M3 Expressive update, May 2025)

| Token (`md.sys.typescale.emphasized.*`) | Size / line height | Weight (site and Compose) | Tracking, site 3p | Tracking, Compose v0_103 |
|---|---|---|---|---|
| display-large / medium / small | 57/64, 45/52, 36/44 | 500 | -0.25, 0, 0 | 0, 0, 0 |
| headline-large / medium / small | 32/40, 28/36, 24/32 | 500 | 0 | 0 |
| title-large | 22/28 | 500 | 0 | 0 |
| title-medium / small | 16/24, 14/20 | 700 | 0.15, 0.1 | 0.15, 0.1 |
| body-large / medium / small | 16/24, 14/20, 12/16 | 500 | 0.5, 0.25, 0.4 | 0.15, 0.25, 0.4 |
| label-large / medium / small | 14/20, 12/16, 11/16 | 700 | 0.1, 0.5, 0.5 | 0.1, 0.5, 0.5 |

Sources: the same token module and Compose file as 3a. Usage rules: https://m3.material.io/styles/typography/type-scale-tokens

- Emphasized styles have "a higher weight and other minor adjustments", and are "best applied to bold, selection, and other areas of emphasis".
- Components don't use them by default. They suit badges, primary buttons, extended FABs, and selected list and menu items.
- The availability table lists "Web: Expressive" as **Unavailable**. Material Web has no emphasized styles.
- Repo check: matches "15 emphasized styles, heavier weights on the same sizes" (DC-L02-11). The repo doesn't list the emphasized tracking, where Compose and the site disagree on display-large and body-large.

### 3c. How Material builds its scale

| Rule | Value | Source |
|---|---|---|
| Ratio and base | "Material Design uses the Major Second type scale with 14 as its key base size." | https://m3.material.io/styles/typography/type-scale-tokens |
| Fit to the formula | 11, 12, 16, 22, 28, 32, 36 and 45 equal 14 × 1.125ⁿ rounded. 24 and 57 are 1 off (the formula gives 25 and 58). [computed] | arithmetic |
| Roles | 5 roles (display, headline, title, body, label) × 3 sizes (large, medium, small) | https://m3.material.io/styles/typography/applying-type |
| Typefaces | Brand typeface for larger styles (Headline, Display), plain typeface for smaller ones (Body, Label). "Roboto is the default for both." | https://m3.material.io/styles/typography/type-scale-tokens |
| Customizing | Change typeface, line height and letter spacing. "Avoid changing the type size; this can affect how components render and reflow." | same |
| Contrast between sizes | Aim for "impactful contrast between sizes by avoiding small differences." | same |
| Units | Android sp; web rem = sp/16. The page says browsers default to 16px. | same |
| Tracking unit | Tracking px ÷ font size, e.g. 0.2 ÷ 16 = 0.0125. The page labels the web unit "rem", but the result is size-relative, which is `em` in CSS [inferred]. | same |
| Line height | Images on the page show "larger type with a line height ratio of 1.2" and "body type with a line height ratio of 1.5". | https://m3.material.io/styles/typography/applying-type |
| Line length | 40 to 60 characters for long body text, 20 to 40 for short lines | same |
| Scaling across devices | From phone or tablet to desktop, "increase the size of display and headline." | same |
| Language height | Line height adapts by script: small (Latin and others), medium (~7% taller, e.g. Hindi, Tamil), large (~30%, e.g. Telugu), extra large (~100%, Nastaliq) | https://m3.material.io/styles/typography/type-scale-tokens (updated Aug 2026) |

- Apple states no ratio for its scale.

---

## 4. Mapping to web H1-H6, body, small and caption

### 4a. What the sources themselves say

| Source | What it says about heading levels |
|---|---|
| Apple SwiftUI `Font.TextStyle` | `title` is "the font used for first level hierarchical headings", `title2` for second level and `title3` for third level. `headline` is "the font used for headings", `subheadline` "for subheadings". https://developer.apple.com/documentation/swiftui/font/textstyle |
| Apple accessibility | Heading level is set apart from the visual style, with `AccessibilityHeadingLevel` `.h1` to `.h6` (or `.unspecified`). Every levelled heading except h1 must come after a heading one level higher. https://developer.apple.com/documentation/swiftui/accessibilityheadinglevel. The HIG says "use accurate section headings". https://developer.apple.com/design/human-interface-guidelines/voiceover |
| Google, Material 2 to 3 migration | Official mapping from M2's H-named styles: h1 → displayLarge, h2 → displayMedium, h3 → displaySmall, (none) → headlineLarge, h4 → headlineMedium, h5 → headlineSmall, h6 → titleLarge, subtitle1 → titleMedium, subtitle2 → titleSmall, body1 → bodyLarge, body2 → bodyMedium, caption → bodySmall, button → labelLarge, (none) → labelMedium, overline → labelSmall. https://developer.android.com/develop/ui/compose/designsystems/material2-material3 (last updated 2026-10-01) |
| Material Web | Its code example is `<h1 class="md-typescale-display-large">` with `<p class="md-typescale-body-medium">`. https://github.com/material-components/material-web/blob/main/docs/theming/typography.md |
| Material roles | Label is for text inside components and "very small text in the content body, such as captions". Buttons use label-large. https://m3.material.io/styles/typography/applying-type |
| W3C WAI | Rank 1 (`<h1>`) is the most important and rank 6 the least. "Skipping heading ranks can be confusing and should be avoided where possible", e.g. no `<h2>` followed directly by `<h4>`. https://www.w3.org/WAI/tutorials/page-structure/headings/ |

**Browser default heading styles (HTML Standard)**

| Element | Default size | At a 16px root [computed] | Weight |
|---|---|---|---|
| h1 | 2.00em | 32px | bold |
| h2 | 1.50em | 24px | bold |
| h3 | 1.17em | 18.72px | bold |
| h4 | 1.00em | 16px | bold |
| h5 | 0.83em | 13.28px | bold |
| h6 | 0.67em | 10.72px | bold |
| small | `font-size: smaller` | - | - |

Source: https://html.spec.whatwg.org/multipage/rendering.html#sections-and-headings (§15.3.6; `:heading { font-weight: bold; }`)

- The default h6 (10.72px) is below the 12px legibility line in section 5. Always restyle headings.

### 4b. Recommended mapping for a marketing website [inferred]

| HTML | Desktop (M3 token, size/line height px, weight) | Mobile | Why |
|---|---|---|---|
| H1 (hero) | display-large 57/64, 400 | display-small 36/44, 400 | Display is for "short, important text"; Material scales display up on desktop |
| H2 (section) | display-small 36/44, 400 | headline-medium 28/36, 400 | |
| H3 | headline-small 24/32, 400 | title-large 22/28, 400 | |
| H4 | title-large 22/28, 400 | title-large 22/28, 400 | |
| H5 | title-medium 16/24, 500 | same | Rare on marketing pages |
| H6 | title-small 14/20, 500 | same | Avoid if possible |
| Lead paragraph | No M3 token. Apple Title 3 (20/25, Regular) is the nearest platform size | 18/28 | |
| Body | body-large 16/24, 400 | 16/24 | 16px floor (section 5) |
| Small | body-medium 14/20, 400 | same | |
| Caption | body-small 12/16, 400 | same | |
| Eyebrow / overline | label-medium 12/16, 500, +0.5 tracking | same | M2 overline maps to label-small (11), but 12 keeps marketing copy above the 12px line |
| Button | label-large 14/20, 500 | same | Material: buttons use label-large |

### 4c. Recommended mapping for a product UI [inferred]

| HTML | Web app (M3 token, px) | iOS (Apple text style, pt) | Why |
|---|---|---|---|
| H1 (page title) | headline-small 24/32, 400 | Title 1 28/34 Regular (Large Title 34/41 for a top-level screen) | Apple: `title` = first-level heading |
| H2 | title-large 22/28, 400 | Title 2 22/28 Regular | Apple: `title2` = second level |
| H3 | title-medium 16/24, 500 | Title 3 20/25 Regular | Apple: `title3` = third level |
| H4 | title-small 14/20, 500 | Headline 17/22 Semibold | Apple: `headline` = headings |
| H5-H6 | Don't use. Flatten the structure. | Subheadline 15/20 | Fewer levels read better in dense UI |
| Body | body-medium 14/20 (dense) or body-large 16/24 (reading) | Body 17/22 | Material's key size is 14; Apple's default is 17 |
| Small | body-small 12/16 | Footnote 13/18 | |
| Caption | body-small 12/16; label-small 11/16 is the floor | Caption 1 12/16; Caption 2 11/13 is the floor | 11 is the iOS minimum and Material's smallest style |
| Button / control | label-large 14/20, 500 | Body or Headline 17 | |

---

## 5. Minimum sizes

| Source | Rule | Source URL |
|---|---|---|
| Apple | iOS/iPadOS min 11 pt (default 17), macOS 10 (13), tvOS 23 (29), visionOS 12 (17), watchOS 12 (16). Go larger for thin weights. | https://developer.apple.com/design/human-interface-guidelines/typography |
| Apple | Let people enlarge text by at least 200% (140% on watchOS) | https://developer.apple.com/design/human-interface-guidelines/accessibility |
| Material 3 | Smallest style is label-small 11sp. Smallest body is body-small 12sp. Key body size is 14. The pages read state no explicit minimum. | https://m3.material.io/styles/typography/type-scale-tokens |
| WCAG 2.2 SC 1.4.4 Resize Text (AA) | "Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality." The SC sets no pixel minimum. Using viewport units to size text is a listed failure (F94). | https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html (updated 06 Sep 2026) |
| WCAG 2.2 SC 1.4.12 Text Spacing (AA) | Nothing may break when users set line height to 1.5× the font size, paragraph spacing to 2×, letter spacing to 0.12× and word spacing to 0.16× | https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html (updated 01 Oct 2025) |
| Browser default | The default font size is "usually 16px" | https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size |
| USWDS (US government design system) | "For most text, including body copy, use at least an effective size of 16px." Lines of 45-90 characters. Line height 1.5 or more for long text. | https://designsystem.digital.gov/components/typography/ |
| WebKit (iOS Safari) | When a field is focused, the zoom is `16 / field font size` (`webViewStandardFontSize = 16`), so fields under 16px zoom in. Input text must be at least 16px. | https://github.com/WebKit/WebKit/blob/main/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm (`_zoomToFocusRect`) |
| Lighthouse (legacy) | Flagged pages where 40% or more of the text is under 12px; advised "at least 12 px on at least 60% of the text". The audit was **removed in Lighthouse 13**. | https://developer.chrome.com/docs/lighthouse/seo/font-size |

- Repo check: the repo marks the 16px web rule and the iOS Safari input zoom as unverified (DC-L02-20, S-L02-064). Both are now confirmed: WebKit's source code, USWDS and MDN. The repo doesn't mention that the Lighthouse audit was removed.
- Our floor [inferred]: 16px body on the web, 16px in form fields, nothing anyone must read below 12px on the web or 11pt on iOS.

**Related contrast thresholds (text size decides which applies)**

| Source | Small text | Large text |
|---|---|---|
| Apple (Accessibility Inspector, WCAG AA) | Up to 17 pt: 4.5:1 | 18 pt and up, or any bold text: 3:1 |
| Material 3 | 4.5:1 | 3:1 |

Sources: https://developer.apple.com/design/human-interface-guidelines/accessibility and https://m3.material.io/styles/typography/applying-type

---

## 6. Weight usage: regular vs bold titles

| System | Titles and headings | Body | Bold or emphasis | Source |
|---|---|---|---|---|
| Apple iOS | Large Title and Title 1-3 are **Regular**. Only Headline is Semibold. | Regular | Bold trait: Bold for Large Title, Title 1 and 2; Semibold for the rest | https://developer.apple.com/design/human-interface-guidelines/typography |
| Apple macOS | Large Title and Title 1-3 are Regular. Headline is **Bold** (emphasized: Heavy). | Regular | Semibold mostly; Caption 2 is Medium by default | same |
| Apple tvOS | Title 1-3 and Headline are **Medium** | Medium | Bold | same |
| Apple watchOS | Titles are Regular. Headline is Semibold. | Regular | Bold or Semibold | same |
| Material 3 baseline | display, headline and title-large are **400 Regular**. title-medium and title-small are 500. | 400 | label 500 | https://m3.material.io/styles/typography/type-scale-tokens |
| Material 3 emphasized | display to title-large 500; title-medium and title-small 700 | 500 | label 700 | same |
| Material Web | Each typeface needs 400, 500 and 700 loaded | - | - | https://github.com/material-components/material-web/blob/main/docs/theming/typography.md |
| Browser default | h1-h6 are **bold** | normal | - | https://html.spec.whatwg.org/multipage/rendering.html |

What this means for light, non-bold titles:
- Both Apple and Material set their large titles in **Regular (400)**. Bold is an opt-in emphasis on top. The browser's default bold headings are the outlier, so reset `font-weight` on `h1` to `h6`.
- **Light (300) and thinner** is where the rules diverge. Apple says "in general, avoid light font weights", especially at small sizes. Material allows it only in editorial treatments ("a narrow, thin style for serenity"). Our rule [inferred]: 400 for all titles. 300 only at display sizes (32px and up), never for body, labels or anything near the minimum size.

---

## 7. Reference sites

I measured both sites' computed text styles on the live pages on 2026-10-14, at 1440 wide, with a script that read every text element.

| | Anduril (anduril.com) | Palantir (palantir.com) |
|---|---|---|
| Families | One: a Helvetica-style display family | Two cuts of one family (No.1 and No.2), plus a mono |
| Largest text | 56 px, weight 700, −0.02em, line 1.1 (product names) | 80 px, **weight 400**, −0.05em, line 1.0 |
| Section titles | 40 px, **weight 400**, −0.02em | 46–50 px, **weight 400**, −0.02 to −0.025em |
| Body | 18 px, 400 | 16–18 px, 400 |
| Labels | 12 px, 500, uppercase, +0.04em | 10–12 px, 400, uppercase |
| Color | white on pure black | near-black (#1e1f2b) on pure white, grey #666 secondary |
| Imagery | full-bleed cinematic photography | full-bleed black-and-white photography |

What to take from them:
- One family, with the hierarchy carried by size and space, not boldness.
- Tight tracking works because the weight is regular.
- Strong tonal contrast: pure black or pure white grounds.
- Photography does the emotional work, so the type stays quiet.

## Summary of disagreements with the repo

1. **Material tracking.** The repo doesn't know which values are canonical. The live token module's third-party setting gives Roboto with display-large -0.25, title-medium 0.15 and body-medium 0.25. Compose v0_103 ships -0.2, 0.2 and 0.2. Emphasized body-large is 0.5 on the site and 0.15 in Compose.
2. **16px on the web.** The repo marks it unverified. It is now confirmed by WebKit's source code (input focus zoom), USWDS and MDN.
3. **watchOS default.** The repo says 16 pt. That is right only for 40/41/42 mm. The 44/45/49 mm default (xLarge) has a 17 pt body.
4. **Text enlargement.** The repo says Apple asks for 200%. Apple says 200%, or 140% on watchOS.
5. **Lighthouse 12px audit.** It was removed in Lighthouse 13. The repo doesn't mention this.
6. **Material Web.** It has no emphasized (Expressive) styles. The repo doesn't mention this.

Everything else checked (Apple sizes, leading, minimums and tracking; Material sizes, line heights, weights, the Major Second ratio and the language-height groups) matches the repo.
