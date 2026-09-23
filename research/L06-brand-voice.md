# L06: Brand & visual identity systems, brand-to-product translation, content / voice & tone

Lane: L06. Author: orchestrator subagent L06. Started 2026-09-23.
Status: complete (first pass) 2026-09-23. 24 Decision Cards. Source ids refer to `traces/L06-trace.md`.

## Lane overview

This lane answers the builder's "what would make it look what way" question: how a brand's personality becomes concrete visual and verbal choices inside a product design system.

Five findings shape everything below:

1. **Mature organisations run two layers, not one.** A brand/visual identity layer (logo, brand typeface, palette, graphic devices, illustration, photography, motion, sound, voice) sits above a product design system that consumes a *subset* of it. IBM makes this explicit in its site switcher, which groups IBM Brand Center and IBM Design Language under "Foundations" and Carbon Design System, Carbon for IBM Products and Carbon for IBM.com under "Implementation" [S-L06-001][S-L06-003]. Google (brand > Material), Microsoft (brand > Fluent) and Airbnb (brand > DLS) follow the same shape [S-L06-031][S-L06-043].
2. **The bridge between the layers is "expressive vs productive".** Carbon ships two type sets (productive `-01`, expressive `-02`) and two motion styles with different cubic-bezier curves [S-L06-001][S-L06-002]. Material 3 Expressive (May 2025) turned the same idea into seven "expressive tactics" and advice to limit "hero moments" to one or two per product [S-L06-009]. A builder should expose *one* brand dial that moves many tokens at once rather than asking users to set 98 variables (Linear collapsed 98 theme variables into 3 inputs: base, accent, contrast) [S-L06-012].
3. **Brand-to-visual mapping is partly evidenced, partly craft.** Google's Material research measured which style attributes users perceive (playful, energetic, friendly, creative, modern, calm) and found, for example, that big splashes of color read as playful [S-L06-011], and that expressive designs rated higher on "energetic, playful, friendly" but a strong minority preferred calmer versions and banking contexts need restraint [S-L06-010]. Google Sans Flex's official copy ties weight to loud/quiet and roundness to "personal, playful" [S-L06-031]. Most other mappings in the lever matrix are practitioner convention and are marked `[inferred]`.
4. **Signature > spread.** Every famous identity in the case-study table is recognisable from 2-4 owned levers (a custom typeface, one hero color, one graphic device, one character or illustration style), not from customising every component. Apple's 2026 HIG says the same from the platform side: use the accent color "judiciously", express brand through voice, content and custom headline type, and keep familiar components [S-L06-008]. Fluent: reuse native components "80% of the time" and spend energy on "signature experiences" [S-L06-043].
5. **Voice is a foundation, not a docs appendix.** Every major system separates constant *voice* from situational *tone* (Mailchimp, Microsoft, Atlassian, Apple, NN/g) [S-L06-014][S-L06-046][S-L06-052][S-L06-013]. The mechanics (capitalization, contractions, "we", exclamation marks, numbers, dates) genuinely differ between systems and are real questionnaire decisions, e.g. Mailchimp uses title case for headings but sentence case for buttons, while Microsoft and Atlassian use sentence case everywhere [S-L06-051][S-L06-047].

---

## 1. What a visual identity system contains, and how it differs from a product design system

| Element | Brand / identity layer (marketing, "expressive") | Product design system layer ("productive") | Overlap: what the product inherits |
|---|---|---|---|
| Logo system | Primary mark, wordmark, symbol, lockups, sub-brand marks, clear space, misuse rules (IBM: 8-bar, Rebus [S-L06-003]; Slack octothorpe built from speech bubble + lozenge [S-L06-030]) | Rarely used; app icon, favicon, splash. Apple HIG: don't repeat the logo through the app, don't brand the launch screen [S-L06-008] | App icon; logo shapes reused as graphic devices (Slack's speech bubble "will form the basis of a system of customized icons, illustrations" [S-L06-030]) |
| Color | Full brand palette incl. expressive accents, gradients, campaign colors (Dropbox 2017 "deliberately jarring" combinations [S-L06-024]; Mailchimp "yellow-heavy" [S-L06-027]) | Neutral ramps, one primary/accent, semantic status colors, surface and elevation tones, contrast-tested (Stripe rebuilt its brand palette in CIELAB for predictable contrast [S-L06-035]) | Primary/accent hue, sometimes 1-2 secondary hues; brand color moves into the content layer (Apple 2026) [S-L06-008] |
| Typography | Brand/display typeface, often custom (Cereal, Spotify Mix, Uber Move, Netflix Sans, Feather Bold, Google Sans, Plex) | UI text face and scale; often the brand face at display sizes + a system or text-optimised face for body (Apple recommends exactly this [S-L06-008]; Google ran Google Sans display + Roboto body until Google Sans Text [S-L06-031]) | Headline face, weights, sometimes the whole family if it has a text cut |
| Graphic devices / motifs | Shapes, patterns, crops, frames, gradients (Slack shapes, Dropbox diamonds [S-L06-030][S-L06-024]; Stripe's marketing gradients [inferred, not verified from a primary source]) | Mostly absent; appears in empty states, onboarding, hero moments | Shape language can leak into radius and icon style (Material 3 Expressive shape library of 35 shapes for avatars and crops [S-L06-009]) |
| Grid | Brand grid for layouts, posters, motion (IBM 2x Grid [S-L06-003]) | Responsive column grid, spacing scale, breakpoints | Base unit and proportions |
| Imagery / photography | Art direction, subject matter, color grading (IBM photography guidance [S-L06-003]) | Content images, avatars, thumbnails, aspect ratios | Crop shapes, overlay treatment |
| Illustration | Hero and campaign illustration styles (IBM line/flat/isometric/hybrid UI [S-L06-003]; Mailchimp outsider-art style [S-L06-027]) | Spot illustrations for empty states, onboarding, errors | Stroke weight and palette rules |
| Iconography | Pictograms, app icons (IBM separates UI icons, app icons, pictograms [S-L06-003]) | UI icon set with fixed grid, stroke, sizes | Stroke weight / corner style tuned to the type |
| Motion | Brand/signature animation (Collins "signature animation style" for Dropbox [S-L06-024]) | Durations, easing, choreography for components (Carbon productive vs expressive [S-L06-002]) | Easing personality; "expressive" curves reserved for key moments |
| Sonic identity / haptics | Sonic logo, notification sounds (Fluent lists sound among "signature experiences" [S-L06-043]) | System sounds, haptic patterns | Notification and success sounds |
| Voice | Brand voice, messaging, tagline, campaign tone | Voice & tone guide, microcopy rules, word list, grammar and mechanics | The whole voice; tone is modulated by UI context [S-L06-014][S-L06-060] |
| Principles | Brand values, positioning | Design principles used as tie-breakers | IBM's principles are written as question checklists for "anyone authoring or authorizing any form of design" [S-L06-004] |

**Where they differ (summary).** The identity layer optimises for recognition, memory and range: "vast expressive range from minimal elements" in Collins' own vocabulary [S-L06-024]. The product layer optimises for task completion, density, accessibility and consistency. Brad Frost boils the practical difference down to three things: marketing uses much more whitespace and jumbo sizes, bigger typography, and different components (heroes, touts, comparison tables vs tables, forms, charts). He argues these can be themes of one system rather than two systems [S-L06-053].

**Brand tokens vs product tokens.** Carbon's theming model is the cleanest statement of the boundary: a *token* and its *role* "never change across themes"; only the *value* changes [S-L06-007]. So brand expression lives in values (and in which primitive a semantic token points at), while the product's semantic vocabulary stays fixed. Linear's model shows the same thing from the generator side: 3 brand inputs produce every surface, text, icon and control alias [S-L06-012]. [inferred] A builder therefore needs (a) a small set of *brand primitives* (brand hues, brand typeface(s), shape signature, motion signature, voice traits), (b) a fixed *semantic layer* the components read, and (c) an optional *expressive layer* (display type sizes, expressive motion, illustration, gradients) that only marketing surfaces and hero moments consume.

## 2. Expressive (marketing) vs productive (app) layers: how real systems split them

| System pair | Brand / expressive layer | Product / productive layer | How the split is encoded |
|---|---|---|---|
| IBM Design Language vs Carbon | Philosophy, Plex, color, 2x Grid, 8-bar and Rebus logos, pictograms, illustration, photography, animation [S-L06-003] | Carbon components, themes (White, G10, G90, G100) [S-L06-007] | Type: productive set `-01` with fixed headings vs expressive set `-02` with responsive headings for "editorial and marketing" [S-L06-001]. Motion: productive `cubic-bezier(0.2, 0, 0.38, 0.9)` vs expressive `cubic-bezier(0.4, 0.14, 0.3, 1)` (standard easing); productive "significantly faster"; no bounce or stretch [S-L06-002]. A separate implementation, Carbon for IBM.com, serves marketing [S-L06-001]. |
| Google brand vs Material 3 / M3 Expressive | Google logo (2015), Product Sans (logo lockups), Google Sans (display, brand) [S-L06-031] | Material 3 (Roboto / Google Sans Text / now Google Sans Flex) | Google Sans for display + Roboto for body was a "dual-font system" and "a compromise", fixed with Google Sans Text (2020) and now Google Sans Flex (6 axes) [S-L06-031]. M3 Expressive adds emphasized type styles, 35 shapes with morphing, springs and seven tactics, but explicitly "isn't M4" [S-L06-009]. |
| Microsoft brand vs Fluent 2 | Microsoft brand (logo, color, sound, illustration) | Fluent 2 | Principle "Unmistakably Microsoft": energy goes into "signature experiences... from color to sound, illustration to icons" while reusing native platform components "80% of the time" [S-L06-043]. |
| Airbnb brand vs DLS | Bélo symbol (DesignStudio, 2014), Airbnb Cereal (Dalton Maag, 2018) [S-L06-021] | Design Language System | One custom typeface built to "leap from button to billboard", i.e. the same face serves both layers (secondary source snippet, [S-L06-021]) |
| Spotify brand vs Encore | Spotify Mix (Dinamo, 2024), brand color, campaign system (Wrapped) [S-L06-019] | Encore (Spotify's product design system family) | Spotify Mix replaces the previous font "in-app and desktop" and in marketing, so one variable family spans both layers [S-L06-019] |
| Stripe brand vs Stripe product UI | Brand palette and marketing visuals | Dashboard and internal interface library | product interface colors "are based on our brand color palette", re-engineered in CIELAB for uniform contrast per level [S-L06-035] |
| Linear brand vs app | Marketing site | App theme generator | Headings in Inter Display "to add more expression", body in Inter; chrome color deliberately limited for a "neutral and timeless" app [S-L06-012] |

**Rule the builder can apply** [inferred from the table above]: every brand foundation should offer a *productive* value set (default for app surfaces) and an optional *expressive* value set (display type, larger radii or shape variety, springier or longer motion, fuller color). Components pick productive by default; hero moments, onboarding, empty states and marketing pages opt into expressive. Material's guidance to "stick to one or two hero moments" gives the budget [S-L06-009].

## 3. Case studies: visual signature and the levers that produce it

Reading guide: "Signature" is what makes the brand recognisable at a glance. "Levers" are the concrete settings a builder could expose. "Product translation" is how the brand reaches the app. Hex values are given only where a primary source stated them this session; where a detail comes from trade press it carries that source's id; anything else is `[inferred]`.

| Brand | Signature (what you recognise) | Levers that produce it | Product translation | Evidence |
|---|---|---|---|---|
| **IBM** | 8-bar logo stripes, Plex, blue, 2x Grid, disciplined layouts | Custom type family (Plex Sans/Serif/Mono) whose details are borrowed from the logo (slab serif, right-angled counters, the point of the M); strict grid; two motion curves; type scale from one equation (12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 48, 54, 60, 68, 76, 84, 92 px) | Carbon: productive `-01` vs expressive `-02` type sets; productive motion faster, no bounce; 4 neutral themes; "Use primary blue for primary actions", neutral running text | [S-L06-001][S-L06-002][S-L06-003][S-L06-006] |
| **Google** | Four-color logo, geometric Google Sans | Typeface lineage from logo: Product Sans (2015 lockups) > Google Sans (2018, Colophon) > Google Sans Text (2020, taller, more condensed, more spacing, Roboto proportions) > Google Sans Flex (6 axes incl. roundness and grade, open-sourced 2025); ~120 billion font requests a month | Material 3 + M3 Expressive; dynamic color from a source color; scheme variants from grayscale to "playful" | [S-L06-031][S-L06-009][S-L06-083] |
| **Microsoft** | Four-square logo, Segoe | "Friendly and legible" Segoe (Segoe UI web, Segoe UI Variable Windows); sentence case; signature color, sound, illustration, icons | Fluent 2 defers to SF Pro on Apple platforms and Roboto on Android; brand lives in "signature experiences" and 20% custom surface | [S-L06-043][S-L06-098] |
| **Apple** | SF typeface, restraint, materials (Liquid Glass since 2025) | SF Pro 9 weights, optical sizes, 4 widths, rounded variant; Liquid Glass as a floating functional layer over content | HIG tells third parties: accent color only for primary actions and status, brand color in the content layer, custom font for headlines only, no logo repetition, no launch-screen branding | [S-L06-008][S-L06-100][S-L06-113] |
| **Airbnb** | Bélo symbol, Cereal, warm and friendly; 2025 app: "Fun, alive, and simple" | Symbol "could be drawn by anyone" (DesignStudio 2014); Cereal (Dalton Maag 2018) with tall x-height, one face "from button to billboard"; 2025: more curved edges, smooth animation, playful dimensional icons | One typeface across brand and DLS; 2025 redesign done in-house, extending to Homes/Experiences/Services | [S-L06-021][S-L06-062] |
| **Spotify** | Green, bold imagery, Wrapped energy, Spotify Mix | Variable font with Dinamo (2024) mixing geometric, grotesque and humanist traits, sound-wave counters, "sharp angles and smooth curves"; wide width/weight range | Same font in app, desktop and marketing; Encore family (Mobile + Web share one token foundation); partner artwork radius 4px/8px | [S-L06-019][S-L06-020][S-L06-085][S-L06-097] |
| **Uber** | Black and white, wordmark, Uber Move | 2018 (Wolff Olins + in-house): "let in the light, embrace black"; wordmark, not symbol; Uber Move typeface (MCKL) based on transit signage | Base design system (Base 2.0) with product voice, product tone and global writing guidance; public detail pages did not render | [S-L06-023][S-L06-081] |
| **Mailchimp** | Cavendish Yellow, Freddie, Cooper, outsider-art illustration, dry humour | Yellow-heavy palette; Cooper Light (1920s serif) for warmth and sincerity; simplified Freddie (always winking, never talks); illustration mostly black and white with yellow accents | Collins "augment" translating marketing identity into product UI; voice "plainspoken, genuine, translators, dry humor"; Freddie appears in loading, error and empty states | [S-L06-027][S-L06-028][S-L06-014][S-L06-090] |
| **Dropbox** | 2017: loud color collisions, Sharp Grotesk, art collaborations | Deliberately jarring palette pairings; one huge type family (259 Sharp Grotesk fonts) to "speak in a variety of tones"; logo from identical diamond shapes; signature motion | Brand guidelines cover "icons to illustration, logos to language"; product keeps restraint [inferred] | [S-L06-024][S-L06-115][S-L06-095] |
| **Slack** | Octothorpe, four brand colors, aubergine | Logo rebuilt on a grid from speech bubble + lozenge; palette cut from 11 colors to 4; shapes reused as graphic devices and as the basis for icons and illustration | Aubergine kept as the product accent, making the app recognisable next to white windows | [S-L06-030] |
| **Stripe** | Vibrant but precise color (its marketing gradients are widely recognised but were not verified from a primary source this session) | Brand palette re-engineered in CIELAB so every hue has equal contrast at each level | Product colors derived from brand palette; any two colors 5 levels apart pass small-text contrast, 4 levels for icons/large text | [S-L06-035] |
| **Duolingo** | Duo the owl, bright green, rounded chunky shapes, Feather Bold | Feather Bold extrapolated from Duo's wing and body curves (Johnson Banks + Fontsmith, 2019); "every aspect informed by Duo's rounded feather form"; characters | 2025-26 core-tabs refresh: tiered header sizes, minimal type styles, whitespace over containers; public brand site no longer online | [S-L06-026][S-L06-029][S-L06-080][S-L06-079] |
| **Netflix** | Red, black, Netflix Sans | Netflix Sans (Dalton Maag, 2018) replaced licensed Gotham for ownability and cost; built for billboards through subtitles | Hawkins design system with Professional (studio tools) and Consumer tracks sharing tokens, icons, illustrations | [S-L06-033][S-L06-034][S-L06-087] |
| **Linear** | Dark, dense, precise, "timeless" | Theme generated in LCH from base color, accent color, contrast; Inter Display for headings; chrome color restrained; 2026 moved defaults from cool blue-grey to warmer grey, dimmer sidebar, fewer and smaller icons, softer borders | Users build custom themes from the same 3 inputs; contrast input yields accessible high-contrast themes | [S-L06-012][S-L06-067] |
| **Notion** | Black-and-white gestural drawings (Roman Muradov), monochrome UI | Hand-drawn line illustration against a sea of vector illustration; campaign added primary color for out-of-home | Illustration carries the personality; UI stays near-monochrome [inferred from S-L06-092] | [S-L06-092] |
| **Atlassian** | Bold geometric brand shapes, product logo family | Brand shapes proved too strong in-app; product icons redrawn with 1.5px stroke on 16px, rounded to match Atlassian Sans | Explicit brand-to-product adaptation: "combined the brand's angular qualities with the rounded features of our new typeface" | [S-L06-088][S-L06-089] |
| **GOV.UK** | Crown, blue (2025), GDS Transport, plain English | 2025 refresh: blue background, floating turquoise dot, expanded palette and animation; departments share the Tudor crown and differ only by departmental color | Shipped as GOV.UK Frontend 5.10.0+, with a hard deadline (31 Dec 2025) for services to update | [S-L06-105][S-L06-106][S-L06-107] |
| **Zomato (India)** | Red, food photography, Sushi DS | Sushi DS (2019) principles: user centricity, inclusivity, simplicity, consistency; "Foundations are digital brand guidelines"; custom face Okra (modified Metropolis) per search snippet | Sushi open-sourced for Android and Compose Multiplatform | [S-L06-063][S-L06-064] |
| **Swiggy (India)** | Orange S-pin symbol | Map pin redrawn as an "S" monogram (Opposite, 2014), unchanged through the 2024 IPO; sub-brand Instamart got its own blue in May 2025 while keeping a subtle S-pin | Sub-brand pattern: parent symbol retained, color changed | [S-L06-065][S-L06-066] |
| **CRED (India)** | NeoPOP: extruded, high-contrast "pop" surfaces on dark | PopFrameLayout draws 5 surfaces (top, left, right, bottom, center), edge colors computed from the center color | NeoPOP open-sourced for Android, iOS, Flutter, Web | [S-L06-037][S-L06-112] |
| **Razorpay (India)** | Blue, fintech trust | In-house rebrand (3 months, 4 designers; undated) | Blade: one cross-platform DS; `createTheme({ brandColor })` generates a full light/dark palette for merchant-branded surfaces | [S-L06-093][S-L06-041][S-L06-094] |

**Patterns across the table** [inferred from the rows above]:
- **Own one typeface, derive it from the mark.** IBM, Google, Duolingo, Spotify, Airbnb, Netflix and Uber all commissioned a face; IBM, Google and Duolingo explicitly derived letter details from the logo or mascot.
- **Split the face when one cut can't do both jobs.** Google needed Product Sans > Google Sans > Google Sans Text; Apple recommends a custom face for headlines and system font for body; Linear uses Inter Display for headings. A builder should ask "display face" and "text face" separately and allow them to be the same.
- **One hero color, reserved.** Slack keeps aubergine for one surface, Apple limits accent to primary actions and status, Carbon uses blue only for primary actions and links. Loud multi-color palettes (Dropbox 2017, Slack's 4 brand colors, Mailchimp's supporting palette) live in marketing, not in controls.
- **Brand shapes get softened for product.** Atlassian and Slack both show a strong brand geometry being translated (thinner, rounder, smaller) before it enters UI.
- **Personality is carried by illustration, characters and voice when the UI stays neutral.** Notion, Mailchimp and Duolingo.

## 4. Brand personality to visual attributes

### 4.1 Frameworks that exist (sourced)

| Framework | What it gives the builder | Evidence |
|---|---|---|
| **Aaker brand personality (1997)**: Sincerity, Excitement, Competence, Sophistication, Ruggedness | A validated 5-dimension vocabulary for the "who are we" question | [S-L06-071] |
| **Labrecque & Milne (2012)** color-personality study | Hue maps to personality (red to excitement, blue to competence); higher saturation raises perceived excitement; higher value (lightness) lowers ruggedness | [S-L06-072] |
| **Henderson, Giese & Cote (2004)** typeface impressions | Typeface impressions (pleasing, engaging, reassuring, prominent) are driven by six design dimensions: elaborate, harmony, natural, flourish, weight, compressed | [S-L06-074] |
| **Bar & Neta (2006)** contour study | Sharp-angled contours raise threat perception; curved objects are preferred | [S-L06-073] |
| **Aarron Walter's design persona (2011)** | 5-7 brand traits written as "X, but not Y" (Mailchimp: "Fun, but not childish... Trustworthy, but not stodgy"), a personality map (friendly-unfriendly x submissive-dominant), voice, copy examples, visual lexicon, engagement methods | [S-L06-070] |
| **Style Tiles (Samantha Warren, 2012)** | Semantic-differential word pairs (e.g. modern vs old-fashioned) collected from stakeholders; adjectives ranked by frequency and mapped to styles ("patriotic" to red/white/blue, publishing heritage to slab serifs) | [S-L06-078] |
| **NN/g 4 tone dimensions (2016, rev. 2023)** | Formal-casual, serious-funny, respectful-irreverent, matter-of-fact-enthusiastic; pick target words and anti-tone words | [S-L06-013] |
| **Material "style" attributes (2024)** | Google measures UIs on hierarchy, utility and style; style attributes: modern, clean, visually appealing, energetic, emotive, positivity, playfulness, friendliness, creativity, personality, vibe. Finding: a colorful top app bar rated more playful | [S-L06-011] |
| **M3 Expressive tactics (2025)** | Seven "axes" of expressiveness: variety of shapes, rich color, emphasized type, containment, fluid motion, component flexibility, hero moments | [S-L06-009] |
| **Google Sans Flex axes (2025)** | Official mapping: weight makes text feel "calm as a whisper" or "loud and rugged"; roundness gives a "personal, playful" tone; taller styles read as more premium (3,000-reader study) | [S-L06-031] |
| **Material scheme variants (code)** | A color-personality dial: Monochrome, Neutral, TonalSpot (default, low-medium colorfulness), Vibrant (max colorfulness), Expressive (detached from source hue), Fidelity/Content (brand-faithful), Rainbow/FruitSalad ("playful") | [S-L06-083] |
| **Carbon productive vs expressive** | One switch that changes type scale behaviour and motion curves together | [S-L06-001][S-L06-002] |

Caveats worth carrying into the builder: NN/g measured real but small tone effects (0.5-1 point on a 5-point scale) [S-L06-013]; Google found a "strong minority" preferring calmer designs and warned that expressive design may not suit banking [S-L06-010]; the academic studies are abstract-level citations here (full texts were bot-walled) [S-L06-075][S-L06-076].

### 4.2 The lever matrix (adjective pair to concrete settings)

How to read: each row is a brand-attribute slider. The left and right cells give settings for each foundation at the two ends. Tags show whether a cell is sourced. Most cells are practitioner convention and are marked `[inferred]`; treat them as defaults to test, not laws. Values are starting points on a 0-100 slider, where 50 is "system default".

**Row A: Playful <-> Serious**

| Foundation | Playful end | Serious end |
|---|---|---|
| Color saturation / amount | Big areas of saturated brand color on chrome (M2 colorful top app bar rated more playful) [S-L06-011]; Vibrant / Rainbow / FruitSalad scheme variants [S-L06-083] | Neutral or Monochrome scheme, color reserved for actions and status [S-L06-083][S-L06-001] |
| Hue | Warm, multi-hue secondary palette (Mailchimp yellow + pink + green) [S-L06-028] | Blue-led, few hues (Labrecque & Milne: blue reads competent) [S-L06-072] |
| Shape / radius | Large radii, pills, mixed shapes, shape morphing (M3 Expressive shape library) [S-L06-009]; curves preferred (Bar & Neta) [S-L06-073] | Small or zero radius, consistent single shape (Carbon uses square corners on most components [inferred, see L04]) |
| Type classification | Rounded or quirky display face (Feather Bold; Google Sans Flex ROND axis "personal, playful") [S-L06-026][S-L06-031] | Neo-grotesque or humanist sans, possibly slab or serif for heritage (Plex) [S-L06-006] |
| Weight / size contrast | Heavy display weights, big size jumps (M3 emphasized type) [S-L06-009] | Moderate weights (Plex Light/Regular/SemiBold only) [S-L06-001] |
| Motion | Springs, overshoot allowed, shape morph (M3 Expressive) [S-L06-009] | Ease-out curves, no bounce, stretch or sudden stops (Carbon) [S-L06-002] |
| Illustration / characters | Mascot and characters in empty, error, success states (Freddie, Duo) [S-L06-027][S-L06-026] | Pictograms or none (IBM pictograms) [S-L06-003] |
| Voice | Casual, funny, enthusiastic (NN/g) [S-L06-013]; "wink" only in success moments (Atlassian) [S-L06-060] | Formal, serious, matter-of-fact; no exclamation marks in failures [S-L06-049][S-L06-056] |

**Row B: Friendly / warm <-> Authoritative / formal**

| Foundation | Friendly end | Authoritative end |
|---|---|---|
| Color temperature | Warm neutrals and warm accents (Linear 2026 moved defaults to "a warmer gray") [S-L06-067] | Cool greys, deep blues and black (Uber "embrace black") [S-L06-023] |
| Contrast | Softer borders and separators (Linear 2026) [S-L06-067] | High contrast, strong rules and dividers [inferred] |
| Shape | Rounded corners, curved edges (Airbnb 2025 "softer feel... more curved edges") [S-L06-062] | Tighter radii, rectilinear grid (IBM 2x Grid) [S-L06-003] |
| Type | Humanist or rounded sans; SF describes itself as a "friendly typographic voice"; Segoe "friendly and legible" [S-L06-113][S-L06-098] | Serif or grotesque, heavier headings, possibly all-caps labels [inferred] |
| Capitalization | Sentence case ("more casual" per Apple) [S-L06-052] | Title case ("generally considered formal" per Apple) [S-L06-052] |
| Contractions / pronouns | Contractions, "we/you" in errors (Atlassian, Microsoft) [S-L06-056][S-L06-046] | No negative contractions (GOV.UK "cannot"); avoid "we" (Apple) [S-L06-048][S-L06-052] |
| Imagery | People, candid photography, faces (Linear 2024 Inbox "emphasized the faces of your teammates") [S-L06-012] | Product, data and abstract imagery [inferred] |

**Row C: Minimal / quiet <-> Rich / expressive**

| Foundation | Minimal end | Rich end |
|---|---|---|
| Color | Near-monochrome UI, 1 accent (Notion, Linear) [S-L06-092][S-L06-012] | Rich primary/secondary/tertiary mixing, surface tones for hierarchy (M3 Expressive tactic 2) [S-L06-009] |
| Density / whitespace | Product density (Brad Frost: apps "compact and utilitarian") [S-L06-053] | Marketing whitespace "out the wazoo", jumbo sizes [S-L06-053] |
| Containment | Whitespace instead of containers (Duolingo tabs) [S-L06-080] | Visible containers and groupings for emphasis (M3 tactic 4) [S-L06-009] |
| Iconography | Fewer, smaller, outlined icons (Linear 2026; Atlassian 1.5px stroke) [S-L06-067][S-L06-088] | Filled, colored or dimensional icons (Airbnb 2025) [S-L06-062] |
| Decoration | No graphic devices in UI | Brand shapes and crops (Slack shapes; M3 35-shape library) [S-L06-030][S-L06-009] |
| Hero moments | None | 1-2 per product (Material's own budget) [S-L06-009] |

**Row D: Calm <-> Energetic**

| Foundation | Calm end | Energetic end |
|---|---|---|
| Motion duration and curve | Productive: shorter, subtle (Carbon standard `cubic-bezier(0.2, 0, 0.38, 0.9)`) [S-L06-002] | Expressive: `cubic-bezier(0.4, 0.14, 0.3, 1)` for "enthusiastic, vibrant, and highly visible movement" [S-L06-002]; springs [S-L06-009] |
| Weight | Lighter weights ("calm as a whisper") [S-L06-031] | Heavy weights ("loud and rugged") [S-L06-031] |
| Saturation | Low (TonalSpot, Neutral) [S-L06-083] | High (Vibrant); saturation raises perceived excitement [S-L06-083][S-L06-072] |
| Chrome brightness | Recessive navigation (Linear 2026 dimmer sidebar) [S-L06-067] | Colored app bars and FABs [S-L06-011] |

**Row E: Premium / sophisticated <-> Accessible / everyday**

| Foundation | Premium end | Everyday end |
|---|---|---|
| Type proportions | Taller, more elegant styles read as more premium (Google Sans Flex study) [S-L06-031]; light display weights [inferred] | Sturdy, tall x-height, open apertures for legibility (Cereal) [S-L06-021] |
| Color | Restrained palette, dark surfaces, one metallic or deep accent [inferred] | Bright primaries [inferred] |
| Depth / texture | Materials, glass, subtle shadows (Liquid Glass used "sparingly") [S-L06-100] | Flat fills [inferred] |
| Space | Generous whitespace, fewer elements per screen [inferred] | Denser, more items, more labels [inferred] |

**Row F: Modern / technical <-> Heritage / traditional**

| Foundation | Modern end | Heritage end |
|---|---|---|
| Type | Geometric or grotesque sans, variable fonts (Google Sans Flex, Spotify Mix) [S-L06-031][S-L06-019] | Serif or slab (Cooper for Mailchimp's sincerity; slab serifs for a publisher) [S-L06-028][S-L06-078] |
| Color space and ramps | Perceptual ramps (LCH, CIELAB) with generated themes [S-L06-012][S-L06-035] | Fixed hand-picked palette [inferred] |
| Mono / code face | A mono companion (Plex Mono, Google Sans Code) [S-L06-006][S-L06-031] | None [inferred] |

**Row G: Bold / confident <-> Deferential / content-first**

| Foundation | Bold end | Deferential end |
|---|---|---|
| Brand presence in UI | Brand color on large surfaces, custom components, logo presence | Apple HIG: accent only for primary actions and status, brand color in content layer, familiar components, no logo repetition [S-L06-008] |
| Platform conventions | Custom typeface everywhere | Native type on each platform (Fluent uses SF Pro on Apple, Roboto on Android) [S-L06-098]; reuse native components 80% of the time [S-L06-043] |
| Voice | Atlassian "Bold" dialed up for confident power users [S-L06-060] | Dialed down for new, anxious or blocked users [S-L06-060] |

**How the builder should use the matrix** [inferred]: ask 4-7 slider questions (rows A-G), then compute defaults for each foundation. Where two sliders pull the same lever in opposite directions (e.g. "playful" wants large radii but "authoritative" wants small), the design principles (section 5) decide, and the conflict should be shown to the user rather than silently averaged.

## 5. Design principles: how systems write them, and what makes them useful

### 5.1 Four kinds of principles (a taxonomy the builder should keep separate)

| Kind | Purpose | Example (verbatim names) | Evidence |
|---|---|---|---|
| Brand / design-language principles | Judge whether any artefact is "on brand" | IBM: Carefully Considered, Uniquely Unified, Expertly Executed, Positively Progressive, each written as a checklist of questions (the "cover up our logo" test (would you still identify the work as IBM?)) | [S-L06-004] |
| Product experience principles | Settle trade-offs inside product design | Fluent 2: Natural on every platform, Built for focus, One for all / all for one, Unmistakably Microsoft, each split into "what makes it functional" and "what makes it emotional". GOV.UK: 11 principles incl. Do less; This is for everyone ("If we have to sacrifice elegance - so be it"); Be consistent, not uniform; Minimise environmental impact (latest addition). Zomato Sushi: User centricity, Inclusivity, Simplicity, Consistency. Linear 2026: "not every element of the interface should carry equal visual weight" | [S-L06-043][S-L06-044][S-L06-063][S-L06-067] |
| System principles | Govern the design system as a product | Carbon: open, inclusive, modular and flexible, user first, builds consistency | [S-L06-114] |
| Content / voice principles | Govern words | Atlassian: Inform to build trust; Empower to inspire action; Encourage people along the path; Motivate by showing possibilities; Satisfy by meeting expectations; Delight with unexpectedly pleasing experiences. Uber Base files content principles under "System principles" | [S-L06-060][S-L06-081] |

Negative evidence: Atlassian's Foundations navigation no longer links a design-principles page (the old URL renders an empty shell) and Shopify's Polaris "experience values" URL now redirects to the Polaris web-components overview [S-L06-055][S-L06-057]. Principles pages are among the first things to go stale; the builder should date-stamp them.

### 5.2 What makes a principle useful (sourced criteria)

From NN/g [S-L06-077]: principles are value statements that frame trade-offs. A good one:
1. **Takes a stand**, ideally naming the value it beats ("clean vs discoverable", "power users vs casual users").
2. **Inspires empathy** by saying why the value matters to users.
3. **Is concise and memorable**; fewer than 10 in total.
4. **Doesn't conflict** with the others.
5. **Gets used**: cited when justifying decisions, published with the design system.

Observed patterns that meet these criteria:
- **Question form** turns a principle into a review checklist (IBM) [S-L06-004].
- **Functional + emotional pairs** (Fluent) connect usability to brand feeling [S-L06-043].
- **Explicit sacrifice** ("If we have to sacrifice elegance - so be it") is the clearest tie-breaker language found this session [S-L06-044].
- **Named tensions** (Duolingo: consistency vs purpose, simplicity vs clarity) [S-L06-080].
- **"X, but not Y" traits** (Walter's design persona) double as principles for tone and visual style [S-L06-070].

**Builder implication** [inferred]: principles should be stored as ordered data (rank matters), each with the value it outranks, so the builder can resolve lever-matrix conflicts automatically ("Serious beats Playful for error states") and surface them in docs.

## 6. Multi-brand and white-label systems: what stays fixed, what flexes

### 6.1 Real systems

| System | Shape of the flex | What stays fixed | What flexes | Evidence |
|---|---|---|---|---|
| Carbon themes | 4 themes (White, G10, G90, G100) + custom themes by overriding token values | Tokens and roles ("never change across themes") | Values | [S-L06-007] |
| Material 3 | Static baseline vs dynamic schemes from a source color; scheme variants | Color *roles* and their component mappings ("role mappings remain the same") | Source color, scheme variant, contrast level | [S-L06-082][S-L06-083] |
| Linear | 3-input theme generator (base, accent, contrast) for both built-in and user themes | The ~98 derived aliases and the generation operations | 3 inputs | [S-L06-012][S-L06-067] |
| Razorpay Blade | `createTheme({ brandColor })` for merchant-branded Payment Pages, Payment Button, partner dashboards | Components, API, layout, behaviour; light/dark support | One brand color, with on-color foreground chosen automatically | [S-L06-094] |
| Salesforce SLDS 2 | CSS decoupled from default visual style; global styling hooks; Cosmos default theme; admins set brand colors, logos, images with "clicks, not code"; 9 new accent options | Component structure; semantic hook vocabulary (e.g. `radius-border-4`, `font-scale-4`) | Global hook values, accent color, logo, images | [S-L06-068][S-L06-069] |
| Spotify Encore | "Family" of systems: Mobile + Web subsystems on one token foundation | Foundation tokens, button hierarchy (primary/secondary/tertiary), naming | Platform-specific components and layout themes | [S-L06-085] |
| Netflix Hawkins | Professional (studio tools) and Consumer tracks | Tokens, icons, illustrations ("look and feel like Netflix") | Component sets per audience | [S-L06-087] |
| UK government identity | Every department uses the same Tudor crown in small digital spaces | Symbol, typeface (GDS Transport), layout rules | Departmental background color | [S-L06-106][S-L06-105] |
| Swiggy > Instamart | Sub-brand spun out (May 2025) | Subtle S-pin from parent | Name and primary color (blue) | [S-L06-066] |
| Atlassian product family | 14+ product logos under one parent brand | Construction and family resemblance | Per-product symbol and color | [S-L06-089] |
| Brad Frost's model | Core tokens + brand theme + optional sub-brand layer + white-label config (possibly CMS-editable) + campaign themes + legacy vs next-gen themes | HTML, APIs, shared CSS (display, positioning), JS behaviour | Theme token values; white-label "almost always" color and typography | [S-L06-053] |

### 6.2 Fixed vs flex: a default split for the builder

| Usually fixed across brands (system contract) | Usually flexes per brand (theme) | Flexes only with care |
|---|---|---|
| Component anatomy, behaviour, states, accessibility, keyboard and focus behaviour [S-L06-053] | Primary/accent color and the palette generated from it [S-L06-094][S-L06-082] | Radius / shape family (changes silhouette of every component) [inferred] |
| Semantic token names and roles [S-L06-007] | Typeface family (display and possibly text) [S-L06-053] | Density / spacing scale (affects layout and content fit) [inferred] |
| Status colors' meaning (success, warning, danger) [inferred] | Logo, imagery, illustration set [S-L06-068] | Motion personality (curve family) [inferred] |
| Minimum contrast rules (Linear's contrast input, Blade's auto foreground) [S-L06-012][S-L06-094] | Voice traits and word list [inferred] | Iconography style [inferred] |

Community note: multi-brand and white-label setups with Figma variables and modes are a live practitioner question this month (a "50+ white-label clients" thread) [S-L06-110]. L07 owns the Figma mechanics.

## 7. Content design: voice, tone, mechanics, microcopy

### 7.1 Voice vs tone (universal agreement)

Every source this session agrees: **voice is constant, tone varies with context and with the reader's emotional state.** Mailchimp ("You have the same voice all the time, but your tone changes") [S-L06-014]; Microsoft ("our voice is constant... we adapt our tone—from serious to empathetic to lighthearted") [S-L06-046]; Atlassian (tone "should change depending on the situation the user is in") [S-L06-060]; Apple ("Determine your app's voice... Match your tone to the context") [S-L06-052]; NN/g ("Keep your brand personality consistent, but vary the tone") [S-L06-013].

**Voice definitions in the wild (3-4 traits each):**
- Mailchimp: plainspoken, genuine, translators, dry humour; "weird but not inappropriate, smart but not snobbish" [S-L06-014]
- Microsoft: warm and relaxed, crisp and clear, ready to lend a hand [S-L06-046]
- Atlassian: Bold, Optimistic, Practical with a wink [S-L06-060]
- Airbnb 2025 product attributes: "Fun, alive, and simple" [S-L06-062]

**Tone modulation is a matrix, not a slider.** Atlassian publishes when to turn each trait up or down by user emotion: be *less* bold with new users, trial users, or anyone feeling apprehension, confusion or fear; add the "wink" only when users feel success, joy, pride or relief [S-L06-060]. It maps its six voice principles to UI surfaces: flags, errors and spotlights get "Inform to build trust"; success messages and modals get "Delight" [S-L06-060]. [inferred] The builder can encode this as a table: message type (error, warning, success, empty, onboarding, marketing) x tone settings (humour, formality, enthusiasm, brevity).

### 7.2 Grammar and mechanics: where systems actually differ (real decisions)

| Decision | Option 1 (who) | Option 2 (who) | Evidence |
|---|---|---|---|
| Capitalization of UI labels and headings | Sentence case everywhere: Microsoft, Atlassian, Fluent | Title case for headings and global nav, sentence case for buttons and subnav: Mailchimp. Apple: pick per element type; "Title case is generally considered formal, while sentence case is more casual" | [S-L06-047][S-L06-056][S-L06-098][S-L06-051][S-L06-052] |
| Contractions | Use them for a friendly tone: Atlassian, Microsoft | Avoid negative contractions (cannot, not can't): GOV.UK | [S-L06-056][S-L06-046][S-L06-048] |
| "We" in errors | Allowed for friendlier tone: Atlassian ("We couldn't load your page") | Avoid "we" (unclear who it is): Apple | [S-L06-056][S-L06-052] |
| Exclamation marks | Sparingly, never in failure messages: Mailchimp; avoid in UI, max one per page: Atlassian | Interjections like "oops" "can sound insincere": Apple | [S-L06-049][S-L06-056][S-L06-052] |
| Numbers | Numerals except at sentence start; commas over 3 digits; abbreviate (1k) only when space-constrained: Mailchimp; write out one to nine in long-form, 'of' not '/': Atlassian | GOV.UK: 'one' unless a step or list point | [S-L06-049][S-L06-056][S-L06-048] |
| Ranges and times | 'to' not hyphens (10am to 11am): GOV.UK, Atlassian (except tight spaces) | Hyphen for ranges; "7 am" with space: Mailchimp | [S-L06-048][S-L06-056][S-L06-049] |
| Abbreviations | Avoid e.g., i.e., etc., & (localization, assistive tech): Atlassian; no ampersands unless in a brand name: Mailchimp | n/a | [S-L06-056][S-L06-049] |
| Emoji | Infrequent and deliberate: Mailchimp; Apple notes an encouraging brand might use "occasional exclamation marks and emoji" | n/a | [S-L06-049][S-L06-008] |
| Possessives | Use sparingly ("Favorites" not "Your Favorites"): Apple | n/a | [S-L06-052] |

### 7.3 Microcopy rules for core components (sourced)

- **Buttons and links**: use a verb; "Send" beats "Let's do it!"; no "Click here", link descriptive words instead [S-L06-052][S-L06-051].
- **Multi-step flows**: pick one progression vocabulary ("Get Started", then "Continue" or "Next", then "Done") and keep it [S-L06-052].
- **Errors**: place close to the problem, avoid blame, say how to fix ("Choose a password with at least 8 characters" beats "That password is too short") [S-L06-052]; no exclamation marks in failures [S-L06-049]; tone ladder from formal to irreverent is a brand decision (NN/g's four versions of "An error has occurred") [S-L06-013].
- **Empty states**: say what to do next and give the button or link; they can show voice but must stay useful [S-L06-052].
- **Placeholders and hints**: show the format ("name@example.com"), show errors next to the field [S-L06-052].
- **Success**: the right place for delight or a "wink" [S-L06-060].

### 7.4 Terminology, inclusive language, localization readiness

- **Word lists**: Apple advises a list of common terms to keep language consistent [S-L06-052]; Mailchimp and Microsoft maintain A-Z word lists [S-L06-014][S-L06-047].
- **Inclusive language**: no generic he/she; use role nouns or singular they; use a real person's pronouns (Microsoft) [S-L06-102]; avoid gendered terminology and jargon (Apple) [S-L06-052]; Atlassian has a dedicated inclusive-language page [S-L06-054].
- **Localization**: short strings expand most. IBM's table (via W3C): up to 10 characters 200-300%, 11-20 180-200%, 21-30 160-180%, 31-50 140-160%, over 70 about 130%; German compounds may not wrap; CJK, Thai and Devanagari need extra line height [S-L06-101]. Mailchimp: subject-verb-object, keep articles and helping verbs, check formal vs informal address (tu/usted) per language because an informal voice can offend [S-L06-050].
- **Content tokens**: the DTCG 2025.10 stable format has no string/content type (types are color, dimension, fontFamily, fontWeight, duration, cubicBezier, number and composites) [S-L06-111]. [inferred] UI strings therefore belong in the i18n pipeline (message keys, ICU plural/select), not in the token file. What a builder *can* put in tokens are the layout consequences: min/max widths, truncation and line-clamp rules, line-height bumps for tall scripts.

## 8. The brand questions to answer before building a design system

Ordered from strategy to execution. Each question names the downstream decisions it feeds.

| # | Question | Why it matters / what it drives | Evidence |
|---|---|---|---|
| 1 | Who is the primary audience, and what emotional state are they usually in when they use the product (anxious, rushed, curious, celebrating)? | Tone matrix, density, motion energy | Atlassian tone-by-emotion [S-L06-060]; Mailchimp "consider the reader's state of mind" [S-L06-014] |
| 2 | What category are you in, and what does trust look like there (money, health, government, play)? | Ceiling on expressiveness; Google says banking may not suit expressive design | [S-L06-010][S-L06-041] |
| 3 | Who are the 3-5 competitors, and what visual tropes do they share? | Differentiation target: Collins positioned Mailchimp to "break from SaaS visual tropes" | [S-L06-027] |
| 4 | What is the one thing you want to be recognised by (the "cover the logo" test)? | Signature levers: typeface, hero color, graphic device, character | IBM principle [S-L06-004] |
| 5 | Pick 5-7 brand traits written as "X, but not Y". | Lever-matrix sliders and voice | Walter [S-L06-070]; NN/g anti-tone words [S-L06-013] |
| 6 | Place the brand on 4-7 semantic-differential sliders (playful-serious, friendly-authoritative, minimal-rich, calm-energetic, premium-everyday, modern-heritage, bold-deferential). | Default token values across foundations | Style Tiles [S-L06-078]; Material style attributes [S-L06-011] |
| 7 | What existing brand assets must be honoured (logo, colors, typeface licences, illustration, mascot, sonic logo)? | Primitive tokens, font loading, licensing | Case studies (section 3) |
| 8 | Will the product use the brand typeface in UI, or system fonts for body? On which platforms? | Type tokens, platform overrides | Apple custom-headline guidance [S-L06-008]; Fluent native fonts [S-L06-098] |
| 9 | Static brand color or user/content-driven dynamic color? | Color architecture | Material static vs dynamic [S-L06-082] |
| 10 | How many brands, sub-brands, white-label clients, or campaign themes must the system carry? | Theme layers | Brad Frost [S-L06-053]; Blade [S-L06-094] |
| 11 | Where do marketing and product meet, and do they share one system with two layers? | Expressive vs productive sets | Carbon [S-L06-001]; Brad Frost [S-L06-053] |
| 12 | What are the 3-5 design principles, ranked, and what does each one beat? | Tie-breaking rules | NN/g [S-L06-077] |
| 13 | What is the voice (3-4 traits), and how does tone shift for errors, success, onboarding, empty states? | Content guidelines, microcopy | Section 7 |
| 14 | Which languages and scripts must be supported at launch and within 2 years? | Typeface coverage, line height, string expansion | Google Sans script expansion [S-L06-031]; W3C [S-L06-101] |
| 15 | What accessibility commitments are non-negotiable (WCAG level, user contrast settings, reduced motion)? | Constraints on every lever | Linear contrast input [S-L06-012]; GOV.UK [S-L06-044] |

---

## 9. Decision Cards

### DC-L06-01: Brand-to-product layering model
- **Block path:** Foundations > Brand > Layer architecture
- **Questions the designer answers:** Do marketing and product share one design system? Is there a separate brand guideline above it? Which foundations exist in both layers?
- **Options:** (a) One system, two value sets (productive + expressive) inside it: Carbon type sets `-01`/`-02` and motion styles [S-L06-001][S-L06-002]; Brad Frost's "themes of one system" [S-L06-053]. (b) Brand language above, product system below, marketing implementation beside: IBM's site switcher puts IBM Brand Center and IBM Design Language under Foundations, and Carbon, Carbon for IBM Products and Carbon for IBM.com under Implementation [S-L06-001][S-L06-003]. (c) Family of systems on one foundation: Spotify Encore (Mobile + Web) [S-L06-085], Netflix Hawkins (Professional + Consumer) [S-L06-087]. (d) Single product system, brand only in logo and color (most startups) [inferred].
- **Visual effect:** (a) keeps marketing and app visibly related (same type family, same color logic) while app stays denser; (b) gives marketing more freedom but risks drift; (c) lets platforms differ in components while tokens keep them recognisably one brand.
- **Depends on (upstream):** DC-L06-02 personality profile; number of products and surfaces; team size.
- **Affects (downstream):** every foundation gets a productive and optional expressive set; component library scope (marketing components like hero, tout, comparison table vs tables and forms [S-L06-053]).
- **Token encoding:** a `layer` or `mode` axis rather than duplicate tokens, e.g. `font.heading.productive.lg` vs `font.heading.expressive.lg` ($type typography); `motion.easing.productive.standard` = [0.2, 0, 0.38, 0.9] and `motion.easing.expressive.standard` = [0.4, 0.14, 0.3, 1] ($type cubicBezier) [S-L06-002].
- **Platform notes:** app stores and OS chrome constrain the product layer more than the web marketing layer (Apple HIG branding) [S-L06-008].
- **Accessibility constraints:** both layers must meet the same contrast and motion-reduction rules; expressive does not mean exempt [S-L06-010].
- **Default + heuristic:** default to (a): one system, productive by default, expressive opt-in. Move to (b) or (c) only when separate teams own separate surfaces. L00 flags marketing-vs-product drift as a recurring governance problem [S-L06-110].
- **Evidence:** [S-L06-001][S-L06-002][S-L06-003][S-L06-053][S-L06-085][S-L06-087][S-L06-110]

### DC-L06-02: Brand personality profile (the input that drives the lever matrix)
- **Block path:** Foundations > Brand > Personality
- **Questions the designer answers:** Which 5-7 traits describe the brand, each with its "but not"? Where does the brand sit on each slider (section 4.2 rows A-G)? What must it never feel like?
- **Options:** Trait list in "X, but not Y" form (Mailchimp: "Fun, but not childish. Funny, but not goofy. Powerful, but not complicated...") [S-L06-070]; Aaker's five dimensions as a vocabulary (Sincerity, Excitement, Competence, Sophistication, Ruggedness) [S-L06-071]; semantic-differential sliders (Style Tiles) [S-L06-078]; Material's style attributes (energetic, emotive, positive, playful, friendly, creative) [S-L06-011]; NN/g tone dimensions + anti-tone words [S-L06-013].
- **Visual effect:** none directly; it sets defaults for color saturation, radius, type classification and weight, motion energy, illustration, voice (see lever matrix).
- **Depends on (upstream):** audience, category, competitors (section 8, Q1-Q4).
- **Affects (downstream):** DC-L06-03 to DC-L06-13 (visual levers) and DC-L06-18 to DC-L06-21 (voice).
- **Token encoding:** not a design token; store as metadata, e.g. `$extensions.brand.personality = { playful: 70, friendly: 80, minimal: 40, energetic: 60 }` [inferred]. DTCG allows `$extensions` for tool-specific data [S-L06-111].
- **Platform notes:** none.
- **Accessibility constraints:** none directly; the matrix must clamp any slider output that would break contrast or motion limits [inferred].
- **Default + heuristic:** ask for traits first, sliders second, then show 2-3 generated style tiles for the user to choose from (Warren's method of presenting options rather than one comp) [S-L06-078]. Keep to 4-7 sliders; NN/g found tone effects are measurable but small, so extreme settings rarely help [S-L06-013].
- **Evidence:** [S-L06-070][S-L06-071][S-L06-078][S-L06-011][S-L06-013]

### DC-L06-03: Expressiveness level and hero-moment budget
- **Block path:** Foundations > Brand > Expression intensity
- **Questions the designer answers:** How expressive should everyday screens be? Where are the 1-2 hero moments? Does the category tolerate expressive UI?
- **Options:** Productive-only (Carbon product UI; Linear 2026 "calmer interface") [S-L06-002][S-L06-067]; productive default + expressive moments (Carbon expressive motion for "significant moments such as opening a new page, clicking the primary action button", system alerts) [S-L06-002]; expressive throughout (M3 Expressive's seven tactics) [S-L06-009].
- **Visual effect:** expressive raises perceived energy, playfulness, friendliness and modernity (+34% modernity, +32% subculture, +30% rebelliousness in Google's tests) and made key elements up to 4x faster to spot [S-L06-010]; overdone, it hurts usability (unstructured album-art playlist) and a strong minority prefers calm [S-L06-010].
- **Depends on (upstream):** DC-L06-02; category trust level (banking caution) [S-L06-010].
- **Affects (downstream):** type scale emphasis styles, shape variety, color mixing, motion curves, containment, component size.
- **Token encoding:** expressive variants as a mode or a parallel set: `font.display.emphasized` (typography), `shape.corner.expressive.*` (dimension), `motion.spring.expressive.*` [inferred naming; see L04 for spring encoding].
- **Platform notes:** M3 Expressive is Android/Compose first (alpha Compose code at launch) [S-L06-009].
- **Accessibility constraints:** respect reduced-motion; keep text labels (removing labels from email actions reduced usability) [S-L06-010].
- **Default + heuristic:** productive everywhere, plus "one or two hero moments" (Material's own rule) chosen by asking "is this interaction emotionally impactful?" and "is it a key interaction?" [S-L06-009].
- **Evidence:** [S-L06-002][S-L06-009][S-L06-010][S-L06-067]

### DC-L06-04: Role of the brand color inside the product
- **Block path:** Foundations > Color > Brand color role
- **Questions the designer answers:** Where does the brand color appear: primary actions only, navigation chrome, large surfaces, content? Is there one hero color or several?
- **Options:** (a) Reserved accent: primary actions, links, status, selected tab (Apple HIG; Carbon "Use primary blue for primary actions") [S-L06-008][S-L06-001]. (b) Signature surface: one product area carries the brand color (Slack aubergine sidebar) [S-L06-030]. (c) Brand-flooded chrome: colored app bars, FABs (M2 style, rated more playful) [S-L06-011]. (d) Content-layer color: brand color lives in content and scrolls beneath glass controls (Apple 2026) [S-L06-008][S-L06-100]. (e) Neutral-first with restrained chrome tint (Linear limited "how much chrome (blue)" was used) [S-L06-012].
- **Visual effect:** (a)/(e) calm, content-first, professional; (b) instantly recognisable app silhouette; (c) playful, energetic, louder; (d) modern, dynamic, brand shows through materials.
- **Depends on (upstream):** DC-L06-02, DC-L06-03, brand palette from identity.
- **Affects (downstream):** semantic tokens `color.action.primary`, `color.nav.background`, `color.surface.brand`; button, tab, nav, badge components.
- **Token encoding:** primitive `brand.color.primary` ($type color) > semantic `color.action.primary.background` > component `button.primary.background`. Keep one alias point so the role can move without touching components [S-L06-007].
- **Platform notes:** iOS/iPadOS/macOS 26+: Liquid Glass controls float over content; use brand color in content, not in custom glass [S-L06-100].
- **Accessibility constraints:** brand color on text must pass 4.5:1 (3:1 large); Stripe had to re-engineer brand hues in CIELAB because "none of the default text colors... (except for black) met the contrast threshold" [S-L06-035].
- **Default + heuristic:** (a) reserved accent, with (b) as an optional signature. "Using your brand color too broadly can overwhelm your interface and dilute its impact" [S-L06-008].
- **Evidence:** [S-L06-001][S-L06-008][S-L06-011][S-L06-012][S-L06-030][S-L06-035][S-L06-100]

### DC-L06-05: Color scheme source and colorfulness (static brand vs dynamic; scheme variant)
- **Block path:** Foundations > Color > Scheme strategy
- **Questions the designer answers:** Are colors fixed to the brand, or generated from the user's wallpaper/content? How colorful should generated schemes be? Must the brand hue appear exactly?
- **Options:** Static baseline ("emphasize brand and uniformity"; advised for enterprise and iOS) vs dynamic ("emphasize content or user settings") [S-L06-082]. Scheme variants (Material code): Monochrome, Neutral, TonalSpot (default, "low to medium colorfulness"), Vibrant ("maxes out colorfulness"), Expressive ("intentionally detached from the source color"), Fidelity / Content (source color kept in primaryContainer), Rainbow / FruitSalad ("playful", source hue absent) [S-L06-083].
- **Visual effect:** Monochrome/Neutral read calm, premium or technical; TonalSpot balanced; Vibrant energetic; Rainbow/FruitSalad playful; Fidelity best for strong brand hues that must be exact [S-L06-083]. Higher saturation raises perceived excitement (Labrecque & Milne) [S-L06-072].
- **Depends on (upstream):** DC-L06-02 sliders A, C, D; DC-L06-04.
- **Affects (downstream):** all color roles (primary, secondary, tertiary, containers, surfaces); illustration palette.
- **Token encoding:** generator input tokens `brand.color.source` ($type color), plus metadata `$extensions.scheme.variant = "tonalSpot"` and `contrastLevel` (number) [inferred].
- **Platform notes:** dynamic color is Android-native; iOS has no wallpaper-driven scheme, so static is recommended there [S-L06-082].
- **Accessibility constraints:** dynamic schemes come with user-controlled contrast; static loses that unless added [S-L06-082].
- **Default + heuristic:** static + TonalSpot-like colorfulness for most brands; Fidelity when the brand hue is a legal/recognition asset; Vibrant only when "energetic" > 70 [inferred].
- **Evidence:** [S-L06-082][S-L06-083][S-L06-072]

### DC-L06-06: Theme-generator inputs (how many brand knobs)
- **Block path:** Foundations > Theming > Generator inputs
- **Questions the designer answers:** What is the smallest set of brand inputs from which the whole theme can be computed? Can users or clients create themes?
- **Options:** 1 input: `brandColor` (Razorpay Blade `createTheme`) [S-L06-094]; 1 source color + variant + contrast (Material) [S-L06-082][S-L06-083]; 3 inputs: base, accent, contrast (Linear, replacing 98 per-theme variables) [S-L06-012]; admin-set accent from a curated list (Salesforce: 9 new accent options) [S-L06-068]; fully manual token values (Carbon custom theme via Sass `with`) [S-L06-007].
- **Visual effect:** fewer inputs give more consistent, always-accessible themes but less nuance; Linear's contrast input produces high-contrast themes automatically [S-L06-012].
- **Depends on (upstream):** DC-L06-05, DC-L06-16.
- **Affects (downstream):** every color alias; dark mode; white-label offering.
- **Token encoding:** input tokens at the top (`theme.input.base`, `theme.input.accent`, `theme.input.contrast`) and derived semantic tokens generated at build time; perceptual color spaces (LCH/OKLCH, CIELAB) for derivation [S-L06-012][S-L06-035]. L01 owns the color math.
- **Platform notes:** generation can run at build time (static themes) or runtime (user themes) [inferred].
- **Accessibility constraints:** auto-pick on-color foreground (Blade flips button text light/dark by brand color) [S-L06-094]; enforce contrast in the generator, not by review [S-L06-035].
- **Default + heuristic:** expose 3 inputs (brand/accent color, neutral base or temperature, contrast). Linear's move to "a warmer gray" in 2026 shows the neutral base is itself a personality lever [S-L06-067].
- **Evidence:** [S-L06-007][S-L06-012][S-L06-035][S-L06-067][S-L06-068][S-L06-082][S-L06-094]

### DC-L06-07: Brand typeface strategy
- **Block path:** Foundations > Typography > Brand typeface
- **Questions the designer answers:** Custom, licensed, open-source, or system font? Same face for display and body? Does the brand face override platform fonts on iOS/Android?
- **Options:** Custom family for brand + product (Cereal, Spotify Mix, Netflix Sans, Plex, Google Sans) [S-L06-021][S-L06-019][S-L06-033][S-L06-006][S-L06-031]; custom display face + system/text face for body (Apple's recommendation; Google Sans + Roboto until Google Sans Text) [S-L06-008][S-L06-031]; display cut + text cut of one family (Inter Display + Inter at Linear; Google Sans + Google Sans Text) [S-L06-012][S-L06-031]; open-source brand face (Plex; Google Sans Flex since 2025) [S-L06-006][S-L06-031]; native fonts per platform, brand face on web only (Fluent: Segoe on web/Windows, SF Pro on Apple, Roboto on Android) [S-L06-098].
- **Visual effect:** a custom face is the single strongest recognition lever across the case studies; system fonts feel native and neutral; a display/text split gives character in headings and legibility in body.
- **Depends on (upstream):** DC-L06-02; licences; language/script coverage (DC-L06-24); budget.
- **Affects (downstream):** type tokens, scale and line heights (L02), icon stroke matching (DC-L06-13), string length/truncation.
- **Token encoding:** `font.family.brand.display`, `font.family.brand.text`, `font.family.mono` ($type fontFamily, arrays with fallbacks, e.g. Carbon `'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif`) [S-L06-001]; platform overrides as modes.
- **Platform notes:** custom fonts on iOS must support Dynamic Type and Bold Text [S-L06-008]; Fluent defers to native fonts on non-Microsoft platforms [S-L06-098].
- **Accessibility constraints:** legible "at all sizes"; system fonts "designed for optimal legibility at small sizes" [S-L06-008]; mono faces must disambiguate a/o and similar glyphs (why Google built Google Sans Code) [S-L06-031].
- **Default + heuristic:** brand face for display, system or a text cut for body, unless the family was designed for both jobs. Google needed three iterations to make one brand face work at small sizes [S-L06-031].
- **Evidence:** [S-L06-001][S-L06-006][S-L06-008][S-L06-012][S-L06-019][S-L06-021][S-L06-031][S-L06-033][S-L06-098]

### DC-L06-08: Typeface personality (classification and axes)
- **Block path:** Foundations > Typography > Personality
- **Questions the designer answers:** Geometric, grotesque, humanist, rounded, serif or slab? How heavy, how wide, how round? Where does the face's character come from (logo, mascot, domain)?
- **Options with sourced mappings:** rounded terminals give a "personal, playful" tone; weight moves text from "calm as a whisper" to "loud and rugged"; taller styles read more premium (Google Sans Flex, 3,000-reader study) [S-L06-031]; slab serifs for publishing heritage, "friendly slab serif" (Style Tiles case) [S-L06-078]; Cooper Light chosen for a "sincere and trustworthy" personality [S-L06-028]; details lifted from the logo (Plex) or mascot (Feather Bold) [S-L06-006][S-L06-026]; hybrid geometric-grotesque-humanist for a "remix" idea (Spotify Mix) [S-L06-019]. Academic basis: typeface impressions (pleasing, engaging, reassuring, prominent) vary with elaborate, harmony, natural, flourish, weight, compressed [S-L06-074].
- **Visual effect:** as listed; plus rounder and heavier reads friendlier and louder, lighter and taller reads calmer and more premium [S-L06-031].
- **Depends on (upstream):** DC-L06-02; DC-L06-07.
- **Affects (downstream):** heading weights, tracking, icon style, radius harmony (Atlassian matched icon corners to Atlassian Sans) [S-L06-088].
- **Token encoding:** variable-font axes as tokens where supported: `font.axis.rond` / `font.axis.wdth` / `font.axis.opsz` ($type number), `font.weight.heading` ($type fontWeight) [inferred naming].
- **Platform notes:** variable axes support varies by platform and renderer [inferred]; SF Pro has rounded variant and optical sizes natively [S-L06-113].
- **Accessibility constraints:** avoid very light weights for body; x-height and aperture drive small-size legibility (Cereal's tall x-height and open apertures) [S-L06-021].
- **Default + heuristic:** pick classification from sliders F (modern-heritage) and B (friendly-authoritative); tune roundness from A (playful) and weight from D (calm-energetic).
- **Evidence:** [S-L06-006][S-L06-019][S-L06-021][S-L06-026][S-L06-028][S-L06-031][S-L06-074][S-L06-078][S-L06-088][S-L06-113]

### DC-L06-09: Shape language and signature shape
- **Block path:** Foundations > Shape > Brand shape language
- **Questions the designer answers:** Is there a shape in the logo worth carrying into UI? Rounded or angular? One consistent radius family or deliberate variety?
- **Options:** logo-derived shapes as graphic elements and icon basis (Slack speech bubble + lozenge; Dropbox diamonds) [S-L06-030][S-L06-024]; brand geometry softened for UI (Atlassian: angular brand + rounded type forms, lighter outlines) [S-L06-088]; curved, soft UI (Airbnb 2025 "more curved edges") [S-L06-062]; M3 Expressive variety: 35 shapes, mixed round and square "for tension and visual contrast", shape morph [S-L06-009]; strict rectilinear (IBM grid-led) [S-L06-003].
- **Visual effect:** curves read friendlier and are preferred; sharp angles raise threat perception (Bar & Neta) [S-L06-073]; mixed shapes draw attention to the element that breaks the pattern [S-L06-009].
- **Depends on (upstream):** DC-L06-02 (A, B); logo.
- **Affects (downstream):** radius tokens (L04), avatar and image crops, icon corners, focus-ring shape, illustration.
- **Token encoding:** `shape.corner.none/sm/md/lg/full` ($type dimension) with a brand "roundness" multiplier as generator input [inferred]; decorative shapes as SVG assets, not tokens (DTCG has no file type yet) [S-L06-111].
- **Platform notes:** platform shapes (iOS continuous corners, Android M3 shape scale) may override brand radii [inferred; L04/L10].
- **Accessibility constraints:** focus indicators must stay visible on any shape [inferred].
- **Default + heuristic:** derive one radius family from the logo's curvature; allow shape variety only in hero moments. "Smaller shapes can result in essential actions looking less important" [S-L06-009].
- **Evidence:** [S-L06-003][S-L06-009][S-L06-024][S-L06-030][S-L06-062][S-L06-073][S-L06-088][S-L06-111]

### DC-L06-10: Motion personality
- **Block path:** Foundations > Motion > Personality
- **Questions the designer answers:** Should motion be efficient and invisible, or enthusiastic and visible? Springs or curves? Is bounce allowed? Is there a signature animation?
- **Options:** Carbon productive (standard `cubic-bezier(0.2, 0, 0.38, 0.9)`, entrance `(0, 0, 0.38, 0.9)`, exit `(0.2, 0, 1, 0.9)`) vs expressive (standard `(0.4, 0.14, 0.3, 1)`, entrance `(0, 0, 0.3, 1)`, exit `(0.4, 0.14, 1, 1)`); productive "significantly faster"; duration scales with distance; no "bounce, stretch, or sudden stops" [S-L06-002]. M3 Expressive spatial and effects springs, shape morph [S-L06-009]. Brand signature animation (Collins for Dropbox) [S-L06-024]; 2025 Airbnb "smooth animated interface with subtle intensities" and animated 3D icons [S-L06-062].
- **Visual effect:** productive feels efficient and serious; expressive feels vibrant; springs feel alive and physical; bounce reads playful (and is banned in IBM's serious language).
- **Depends on (upstream):** DC-L06-02 (A, D), DC-L06-03.
- **Affects (downstream):** duration and easing tokens (L04), component transitions, loading indicators, hero moments.
- **Token encoding:** `motion.easing.productive.standard` = [0.2, 0, 0.38, 0.9] and `motion.easing.expressive.standard` = [0.4, 0.14, 0.3, 1] ($type cubicBezier); durations ($type duration); DTCG has no spring type, so springs need `$extensions` or platform code [S-L06-111][inferred].
- **Platform notes:** springs are native on iOS (SwiftUI) and Compose; CSS needs `linear()` approximations [inferred; L04].
- **Accessibility constraints:** honour reduced-motion settings; keep expressive motion for "occasional, important moments" [S-L06-002].
- **Default + heuristic:** productive curves by default; expressive or springs for page transitions, primary action, alerts, and hero moments.
- **Evidence:** [S-L06-002][S-L06-009][S-L06-024][S-L06-062][S-L06-111]

### DC-L06-11: Graphic devices, motifs and signature details
- **Block path:** Foundations > Brand > Graphic devices
- **Questions the designer answers:** Does the brand have a pattern, gradient, crop or shape system? Is it allowed inside the product, and where?
- **Options:** logo shapes as devices (Slack) [S-L06-030]; brand gradient on marketing (Stripe marketing, per L05/L09; not verified this session) [inferred]; "signature detail" / "brand-coherence logic" in identity systems (Collins' vocabulary) [S-L06-024][S-L06-027]; decorative shape library for avatars and crops (M3 Expressive) [S-L06-009]; none in product (Carbon product UI) [S-L06-001].
- **Visual effect:** adds recognisability and warmth; overuse clutters and competes with content (Apple: branding should defer to content) [S-L06-008].
- **Depends on (upstream):** identity assets; DC-L06-03.
- **Affects (downstream):** empty states, onboarding, splash-free welcome screens, marketing components, image crops.
- **Token encoding:** assets (SVG) referenced by component props; gradient tokens possible ($type gradient) [S-L06-111].
- **Platform notes:** Apple: welcome/onboarding screen, not the launch screen, is the place for brand content [S-L06-008].
- **Accessibility constraints:** decorative devices must be hidden from assistive tech and never carry meaning alone [inferred].
- **Default + heuristic:** allow devices only in expressive surfaces (marketing, onboarding, empty states, hero moments).
- **Evidence:** [S-L06-001][S-L06-008][S-L06-009][S-L06-024][S-L06-027][S-L06-030][S-L06-111]

### DC-L06-12: Illustration and character system
- **Block path:** Foundations > Illustration > Brand style and characters
- **Questions the designer answers:** Does the brand have a mascot or characters? What illustration style (line, flat, isometric, dimensional, hand-drawn)? Which product states get illustration?
- **Options:** mascot as brand asset in UI moments (Freddie in loading, error, empty states; "smiles, winks... but he does not talk") [S-L06-028][S-L06-014]; mascot-derived system (Duolingo: typeface and shapes from Duo) [S-L06-026]; hand-drawn gestural line (Notion, deliberately unlike vector norms) [S-L06-092]; outsider-art, imperfect style (Mailchimp) [S-L06-027]; multiple sanctioned styles (IBM: line, flat, isometric, hybrid UI) [S-L06-003]; dimensional 3D icons (Airbnb 2025) [S-L06-062].
- **Visual effect:** characters and hand-drawn styles add warmth and humour and let the UI itself stay neutral (Notion) [S-L06-092]; dimensional styles feel tactile and playful [S-L06-062].
- **Depends on (upstream):** DC-L06-02 (A, C); identity assets.
- **Affects (downstream):** empty-state, error, success and onboarding patterns (L08); voice rules for characters (e.g. mascot does not speak) [S-L06-014].
- **Token encoding:** illustration palette as aliases of brand primitives (`illustration.color.accent` > `brand.color.primary`); stroke weight as dimension token [inferred]. L05 owns illustration systems in depth.
- **Platform notes:** animated or video icons have format and performance costs [inferred].
- **Accessibility constraints:** decorative illustrations get empty alt; don't rely on a character's expression to communicate status [inferred].
- **Default + heuristic:** one illustration style, used in empty, error, success and onboarding states; restrict humour in errors (Atlassian: delight only after trust, "little flourishes, not humor") [S-L06-060].
- **Evidence:** [S-L06-003][S-L06-014][S-L06-026][S-L06-027][S-L06-028][S-L06-060][S-L06-062][S-L06-092]

### DC-L06-13: Iconography as brand translation
- **Block path:** Foundations > Iconography > Brand match
- **Questions the designer answers:** Should icons echo the brand geometry? What stroke and size match the UI typeface? Outline or filled, colored or mono?
- **Options:** Atlassian 2025: legacy 2px stroke on 24px felt "too heavy"; new 1.5px stroke, 16px core set, 12px downscaled for tags and bylines; brand angularity combined with the rounded features of Atlassian Sans [S-L06-088]. Linear 2026: fewer icons, smaller, no colored backgrounds [S-L06-067]. IBM: separate UI icons, app icons, pictograms [S-L06-003]. Slack: icons derived from the logo's speech bubble [S-L06-030]. Airbnb 2025: playful dimensional icons [S-L06-062].
- **Visual effect:** thin outline icons matched to text read calm and precise; heavy or colored icons add energy and noise; logo-derived icons increase brand recall.
- **Depends on (upstream):** DC-L06-07, DC-L06-08, DC-L06-09.
- **Affects (downstream):** icon grid, stroke tokens, button and tag components.
- **Token encoding:** `icon.size.sm = 12px`, `icon.size.md = 16px`, `icon.stroke = 1.5px` ($type dimension) as Atlassian-style defaults [S-L06-088].
- **Platform notes:** SF Symbols and Material Symbols carry platform identity; custom sets trade nativeness for brand [inferred; L05].
- **Accessibility constraints:** icon-only controls need labels [inferred].
- **Default + heuristic:** match icon stroke to the body text stem weight at the icon's size (Atlassian's rationale) [S-L06-088].
- **Evidence:** [S-L06-003][S-L06-030][S-L06-062][S-L06-067][S-L06-088]

### DC-L06-14: Platform deference level (brand vs native conventions)
- **Block path:** Foundations > Brand > Platform deference
- **Questions the designer answers:** How much should the product look like the platform versus like the brand? Which components can be custom?
- **Options:** high deference: familiar components, accent only, no logo repetition, standard patterns (Apple HIG 2026) [S-L06-008]; Fluent's 80/20: reuse native components 80% of the time, invest in "signature experiences" [S-L06-043]; brand-first custom UI (CRED NeoPOP extruded surfaces across Android, iOS, Flutter, Web) [S-L06-112].
- **Visual effect:** high deference feels native and trustworthy; brand-first feels distinctive but costs learnability; Spotify frames the middle path as "cohesion" rather than "consistency" [S-L06-085].
- **Depends on (upstream):** DC-L06-02 slider G; platform list.
- **Affects (downstream):** component library scope; platform token overrides (DC-L06-07).
- **Token encoding:** platform modes on semantic tokens (`platform.ios`, `platform.android`, `platform.web`) [inferred; L07/L10].
- **Platform notes:** Liquid Glass controls are picked up automatically by standard components; custom controls should use glass "sparingly" [S-L06-100].
- **Accessibility constraints:** custom components must re-implement platform accessibility (Dynamic Type, screen readers) [S-L06-008].
- **Default + heuristic:** 80% native, 20% signature. Customise appearance but keep "sizing, placement, and behavior" familiar [S-L06-008][S-L06-043].
- **Evidence:** [S-L06-008][S-L06-043][S-L06-085][S-L06-100][S-L06-112]

### DC-L06-15: Design principles (kind, count, ranking, format)
- **Block path:** Governance > Principles
- **Questions the designer answers:** Which kind of principles are we writing (brand, product, system, content)? How many? Which value beats which?
- **Options:** question checklists (IBM) [S-L06-004]; functional + emotional pairs (Fluent) [S-L06-043]; imperative statements with explicit sacrifice (GOV.UK, 11 principles, updated 2 Apr 2025) [S-L06-044]; short value words (Zomato Sushi; Carbon system principles) [S-L06-063][S-L06-114]; voice principles mapped to UI surfaces (Atlassian) [S-L06-060].
- **Visual effect:** indirect: principles decide lever conflicts (e.g. "Do less" pushes toward minimal; "Unmistakably Microsoft" pushes toward signature moments).
- **Depends on (upstream):** DC-L06-02, positioning.
- **Affects (downstream):** conflict resolution in the lever matrix; review checklists; docs.
- **Token encoding:** not tokens; store as ordered records with `beats` relationships [inferred].
- **Platform notes:** none.
- **Accessibility constraints:** at least one principle should make accessibility non-negotiable (GOV.UK "This is for everyone") [S-L06-044].
- **Default + heuristic:** 3-5 principles, fewer than 10, each naming the value it outranks, non-conflicting, and cited in decisions (NN/g) [S-L06-077].
- **Evidence:** [S-L06-004][S-L06-043][S-L06-044][S-L06-060][S-L06-063][S-L06-077][S-L06-114]

### DC-L06-16: Multi-brand architecture (what is fixed, what flexes)
- **Block path:** Tokens > Theming > Brand layers
- **Questions the designer answers:** How many brands, sub-brands, white-label clients, campaigns or legacy/next-gen looks must run on the same components? Which layers can override which?
- **Options:** single brand + modes (light/dark, contrast); brand themes over a core (Brad Frost: core tokens + brand theme + sub-brand layer + white-label config + campaign themes + legacy vs next-gen) [S-L06-053]; shared symbol, per-unit color (UK government departments; Swiggy > Instamart) [S-L06-106][S-L06-066]; family of platform subsystems (Encore, Hawkins) [S-L06-085][S-L06-087].
- **Visual effect:** products share bones (layout, behaviour) and differ in color, type, imagery; sub-brands read as related through a retained symbol or construction [S-L06-066][S-L06-089].
- **Depends on (upstream):** business model; DC-L06-01.
- **Affects (downstream):** token tier structure (L07), Figma modes/collections, build pipeline, docs.
- **Token encoding:** tokens and roles fixed, values vary (Carbon) [S-L06-007]; tiers primitive > semantic > component with brand themes swapping primitives or semantic aliases [S-L06-053]; DTCG 2025.10 covers theming/multi-brand per L00 [S-L06-110].
- **Platform notes:** runtime brand switching (white-label, multi-tenant) vs build-time themes [inferred].
- **Accessibility constraints:** every brand theme must pass the same contrast checks; generate on-colors automatically [S-L06-094].
- **Default + heuristic:** fix anatomy, behaviour, semantic names and status meanings; flex brand color, typeface, logo, imagery; treat radius, density and motion as "flex with care" (section 6.2).
- **Evidence:** [S-L06-007][S-L06-053][S-L06-066][S-L06-085][S-L06-087][S-L06-089][S-L06-094][S-L06-106][S-L06-110]

### DC-L06-17: White-label customisation surface
- **Block path:** Tokens > Theming > White-label controls
- **Questions the designer answers:** What can a client change (color, font, logo, radius)? Through code, config or an admin UI? What guardrails protect accessibility and usability?
- **Options:** one brand color in code (Blade `createTheme({ brandColor })`) [S-L06-094]; admin UI "clicks, not code" for brand colors, logos, images and curated accents (Salesforce SLDS 2 Themes and Branding) [S-L06-068]; user-facing theme builder (Linear base/accent/contrast) [S-L06-012]; CMS-editable overrides (Brad Frost) [S-L06-053].
- **Visual effect:** each tenant's UI carries its brand color (and sometimes type) on identical layouts; unconstrained options risk ugly or inaccessible results [inferred].
- **Depends on (upstream):** DC-L06-06, DC-L06-16.
- **Affects (downstream):** theme validation, preview tooling, support load.
- **Token encoding:** exposed inputs only (`tenant.color.brand`, `tenant.logo`, optionally `tenant.font.display`); everything else derived [inferred].
- **Platform notes:** SLDS 2 component-level hooks (`--slds-c-*`) are not supported under the Cosmos theme, so custom components must use global hooks [S-L06-069].
- **Accessibility constraints:** auto-contrast foregrounds; clamp lightness/chroma; keep status colors fixed [S-L06-094][inferred].
- **Default + heuristic:** expose brand color + logo; add font and radius only with previews and validation. White-label "almost always" centres on color and typography [S-L06-053].
- **Evidence:** [S-L06-012][S-L06-053][S-L06-068][S-L06-069][S-L06-094]

### DC-L06-18: Voice definition
- **Block path:** Content > Voice
- **Questions the designer answers:** If the product were a person, how would it talk? Which 3-4 traits, each with a "but not"? What is the anti-voice?
- **Options:** Mailchimp (plainspoken, genuine, translators, dry humour) [S-L06-014]; Microsoft (warm and relaxed, crisp and clear, ready to lend a hand) [S-L06-046]; Atlassian (Bold, Optimistic, Practical with a wink) [S-L06-060]; NN/g coordinates on 4 tone dimensions + anti-tone words ("authoritative" without being "pedantic") [S-L06-013].
- **Visual effect:** verbal, but voice and visuals must agree; NN/g notes visual and interaction design contribute strongly to the overall "feel" [S-L06-013]. Apple: an encouraging brand may use "plain words, occasional exclamation marks and emoji, and simple sentence structures" [S-L06-008].
- **Depends on (upstream):** DC-L06-02.
- **Affects (downstream):** DC-L06-19 to DC-L06-23; marketing copy; AI assistant persona [inferred].
- **Token encoding:** not a design token; a content guideline record with traits, anti-traits, examples [inferred].
- **Platform notes:** voice is platform-independent; mechanics may follow platform conventions (Apple capitalization) [S-L06-052].
- **Accessibility constraints:** plain language benefits everyone; avoid jargon (Microsoft, Apple, GOV.UK) [S-L06-046][S-L06-052][S-L06-048].
- **Default + heuristic:** 3-4 traits with "but not", plus 3 copy examples per trait (Walter's "copy examples") [S-L06-070].
- **Evidence:** [S-L06-008][S-L06-013][S-L06-014][S-L06-046][S-L06-060][S-L06-070]

### DC-L06-19: Tone modulation matrix
- **Block path:** Content > Tone
- **Questions the designer answers:** How does tone change for errors, warnings, success, onboarding, empty states and marketing? How does it change for new versus expert users?
- **Options:** emotion-based dial (Atlassian: less bold for new/anxious users, add the wink for success, joy, relief) [S-L06-060]; situation-based (Apple Watch examples: straightforward for serious, congratulatory for goals) [S-L06-052]; NN/g 4-dimension profile per content type [S-L06-013]; "informal usually, but clarity beats entertainment" (Mailchimp) [S-L06-014].
- **Visual effect:** pairs with visual intensity: errors get calm visuals and plain words; success can carry illustration, motion and a wink [inferred from S-L06-060 and S-L06-002].
- **Depends on (upstream):** DC-L06-18.
- **Affects (downstream):** message components (banner, toast, dialog, inline error), empty states, onboarding (L08).
- **Token encoding:** not tokens; a matrix `messageType x {humor, formality, enthusiasm, length}` [inferred].
- **Platform notes:** notifications and lock-screen copy need shorter, context-aware tone (Apple "choose the right delivery method") [S-L06-052].
- **Accessibility constraints:** errors must say how to fix; humour must not obscure meaning [S-L06-052].
- **Default + heuristic:** errors: serious, respectful, matter-of-fact; success: warmest the brand allows; "once may amuse, but a dozen times may annoy" [S-L06-060].
- **Evidence:** [S-L06-002][S-L06-013][S-L06-014][S-L06-052][S-L06-060]

### DC-L06-20: Capitalization style
- **Block path:** Content > Mechanics > Capitalization
- **Questions the designer answers:** Sentence case or title case for buttons, headings, navigation, menus, dialogs?
- **Options:** sentence case everywhere (Microsoft, Atlassian, Fluent) [S-L06-047][S-L06-056][S-L06-098]; title case for headings and global nav, sentence case for buttons and subnav (Mailchimp) [S-L06-051]; per-element choice applied consistently (Apple) [S-L06-052].
- **Visual effect:** "Title case is generally considered formal, while sentence case is more casual" [S-L06-052]; title case also lengthens visual texture of labels [inferred].
- **Depends on (upstream):** DC-L06-18, slider B; platform conventions.
- **Affects (downstream):** every label string; `text-transform` must not be used to fake case (breaks localization) [inferred].
- **Token encoding:** could be a typography token property (`textCase`) but DTCG typography composite has no text-transform property [S-L06-111]; keep as content rule [inferred].
- **Platform notes:** Microsoft reserves capitals for its 500+ product names [S-L06-047].
- **Accessibility constraints:** avoid all caps for emphasis; hard to read [S-L06-047][S-L06-098].
- **Default + heuristic:** sentence case everywhere; it is the majority choice among the systems checked and localizes cleanly [S-L06-047][S-L06-056].
- **Evidence:** [S-L06-047][S-L06-051][S-L06-052][S-L06-056][S-L06-098][S-L06-111]

### DC-L06-21: Grammar and mechanics settings
- **Block path:** Content > Mechanics
- **Questions the designer answers:** Contractions? "We" and "you"? Exclamation marks? Emoji? Numerals vs words? Date, time and range formats? Abbreviations and ampersands? Oxford comma?
- **Options:** see the comparison table in section 7.2 (Atlassian, Mailchimp, Microsoft, GOV.UK, Apple) [S-L06-049][S-L06-056][S-L06-048][S-L06-052][S-L06-046].
- **Visual effect:** friendlier (contractions, "we", occasional emoji) vs more formal and precise (no negative contractions, no exclamation marks); range and time formats change string length and scannability [S-L06-048].
- **Depends on (upstream):** DC-L06-18; locale strategy.
- **Affects (downstream):** all strings; date/time/number formatting should come from locale APIs, not hand-written patterns [inferred].
- **Token encoding:** none in DTCG; locale formatting config (e.g. CLDR-based formatters) [inferred].
- **Platform notes:** OS locale settings override hard-coded formats [inferred].
- **Accessibility constraints:** GOV.UK avoids negative contractions because users misread them [S-L06-048]; Atlassian avoids e.g./i.e./etc./& for assistive tech and localization [S-L06-056].
- **Default + heuristic:** contractions yes (except negative contractions in high-stakes flows), "you" for the user, "we" sparingly, no exclamation marks in errors, 'to' for ranges, numerals for counts [inferred synthesis of sources above].
- **Evidence:** [S-L06-046][S-L06-048][S-L06-049][S-L06-052][S-L06-056]

### DC-L06-22: Component microcopy patterns
- **Block path:** Content > Microcopy
- **Questions the designer answers:** How are buttons, links, errors, empty states, placeholders and multi-step flows worded by default?
- **Options:** verb-first buttons ("Send") vs clever labels; descriptive links vs "Click here"; blame-free fix-it errors; empty states with next step and action [S-L06-052][S-L06-051]; consistent flow vocabulary (Get Started, Continue/Next, Done) [S-L06-052].
- **Visual effect:** verb labels shorten buttons and make hierarchy clearer; empty states become a branded but useful moment [S-L06-052].
- **Depends on (upstream):** DC-L06-18 to DC-L06-21.
- **Affects (downstream):** component docs, default slot content, AI-generated copy guardrails [inferred].
- **Token encoding:** default strings as i18n keys (`button.submit.label`), not design tokens [S-L06-111][inferred].
- **Platform notes:** platform-standard labels (Cancel, OK, Done) should follow OS conventions [inferred].
- **Accessibility constraints:** errors next to the field, instructions instead of scolding [S-L06-052].
- **Default + heuristic:** every component spec ships its microcopy rules with examples.
- **Evidence:** [S-L06-051][S-L06-052][S-L06-111]

### DC-L06-23: Terminology, word list and inclusive language
- **Block path:** Content > Terminology
- **Questions the designer answers:** What do we call our core objects and actions? Which words are banned? How do we write about people?
- **Options:** maintained A-Z word list (Mailchimp, Microsoft) [S-L06-014][S-L06-047]; list of common terms referenced for consistency (Apple) [S-L06-052]; bias-free rules: role nouns or singular they, a person's own pronouns (Microsoft) [S-L06-102]; inclusive-language page (Atlassian) [S-L06-054].
- **Visual effect:** consistent terms make navigation labels, headings and empty states predictable [S-L06-060].
- **Depends on (upstream):** product domain model.
- **Affects (downstream):** navigation labels, component labels, docs, search.
- **Token encoding:** glossary data, not tokens [inferred].
- **Platform notes:** platform terms (tap vs click) differ by input method [inferred].
- **Accessibility constraints:** plain language and no jargon [S-L06-046][S-L06-052].
- **Default + heuristic:** start a 20-50 term glossary on day one and lint copy against it [inferred].
- **Evidence:** [S-L06-014][S-L06-046][S-L06-047][S-L06-052][S-L06-054][S-L06-060][S-L06-102]

### DC-L06-24: Localization readiness
- **Block path:** Content > Localization
- **Questions the designer answers:** Which languages and scripts? How much room do labels need? Formal or informal address per language?
- **Options:** design with IBM's expansion budget (short strings up to 200-300%) [S-L06-101]; Latin-first rollout (Spotify Mix began with Latin scripts + Vietnamese) [S-L06-019] vs broad script coverage (Google Sans 20+ writing systems) [S-L06-031]; formal/informal decided per locale with translators [S-L06-050].
- **Visual effect:** more generous button widths, wrapping labels, taller line heights for CJK, Thai, Devanagari [S-L06-101]; fallback fonts change the brand's look in unsupported scripts [inferred].
- **Depends on (upstream):** DC-L06-07 (script coverage of the brand face); market plan.
- **Affects (downstream):** min/max widths, truncation, line-height tokens, RTL mirroring (L03/L02).
- **Token encoding:** per-script line-height and font-family modes (`font.family.brand.text` with script overrides) ($type fontFamily, number) [inferred].
- **Platform notes:** OS supplies fallback fonts per script; test brand face against them [inferred].
- **Accessibility constraints:** text resizing plus expansion compounds; Uber Base documents text resizing alongside content [S-L06-081].
- **Default + heuristic:** never fix a label width to English length; budget 2-3x for labels under 10 characters [S-L06-101].
- **Evidence:** [S-L06-019][S-L06-031][S-L06-050][S-L06-081][S-L06-101]

---

## Cross-lane notes

- [L06 -> L01] Brand color role (DC-L06-04), scheme variants as a colorfulness dial (DC-L06-05) and theme-generator inputs (DC-L06-06) depend on L01's color math. Material's variant docstrings (Monochrome / Neutral / TonalSpot / Vibrant / Expressive / Fidelity / Content / Rainbow / FruitSalad) are in `material-color-utilities` source [S-L06-083]. Linear 2026 moved default neutrals from cool blue-grey to warmer grey [S-L06-067].
- [L06 -> L02] Brand typeface strategy: display vs text cut is a recurring decision (Google Sans > Google Sans Text; Inter Display + Inter; Apple custom-headline guidance). Google Sans Flex's official page lists **6 axes** (wght, wdth, opsz, slnt, GRAD, ROND); press reports say 5. Use the official count [S-L06-031][S-L06-032].
- [L06 -> L04] Carbon productive vs expressive easing values are in DC-L06-10 [S-L06-002]. DTCG 2025.10 has no spring type [S-L06-111]. Atlassian's icon rounding matched to its typeface is a shape-harmony data point [S-L06-088].
- [L06 -> L05] Atlassian icon system (2025-09-09): 1.5px stroke, 16px core, 12px downscaled [S-L06-088]. Airbnb 2025 dimensional icons [S-L06-062]. Notion and Mailchimp show illustration carrying personality while the UI stays neutral.
- [L06 -> L07] Content strings are not a DTCG type (2025.10) [S-L06-111]; keep them in the i18n pipeline. Brand personality sliders can live in `$extensions`. Blade `createTheme({ brandColor })` and Linear's 3-input generator are reference designs for a builder's theme input API [S-L06-094][S-L06-012].
- [L06 -> L08] Microcopy rules per component (buttons, errors, empty states, placeholders, multi-step flows) are in section 7.3 and DC-L06-22; Atlassian maps voice principles to message types (flags, errors, spotlights, success) [S-L06-060].
- [L06 -> L10] Fluent defers to SF Pro on Apple platforms and Roboto on Android [S-L06-098]; Apple's 2026 branding guidance moves brand color into the content layer under Liquid Glass [S-L06-008][S-L06-100].
- [L06 -> L11] Principles taxonomy (brand, product, system, content) in section 5.1. Atlassian's design-principles page and Polaris's experience-values/content URLs are no longer live at their old addresses [S-L06-055][S-L06-057]. GOV.UK's 2025 brand refresh shipped as a Frontend release with a hard adoption deadline (31 Dec 2025), a good governance example [S-L06-105].
- [L06 -> S1] The builder's questionnaire should start with section 8 (15 brand questions), then the 4-7 sliders in section 4.2, then compute defaults. Show slider conflicts and resolve them by ranked principles (DC-L06-15).

## Open questions / gaps

- **Primary brand sites that did not render or are gone:** Airbnb Design (airbnb.design; Medium blocked), Uber brand site and Base detail pages, Duolingo brand guidelines (offline, now redirects), Sharp Type's Dropbox page, Netflix TechBlog (Cloudflare), CRED NeoPOP docs. Details for these brands rest on agency/foundry pages or trade press (Tier B) and are marked.
- **Color values:** I did not publish brand hex values (Airbnb, Spotify, Duolingo, Netflix, Uber) because no primary source was reachable this session. L09 may have them.
- **Polaris content guidelines:** old URLs now redirect to Polaris web components on shopify.dev; I could not confirm where (or whether) Polaris voice-and-tone guidance now lives.
- **Material writing guidance** (m3 content design pages) was not read this session; Material appears here via its research blogs and color docs only.
- **Academic studies** (Aaker, Labrecque & Milne, Henderson et al., Bar & Neta) were cited at abstract level; full texts were bot-walled. Coefficients for Labrecque & Milne come from a search snippet and should be re-checked before quoting numbers.
- **Brand archetypes** (Mark & Pearson) were not verified against a primary source and are therefore not used.
- **Sonic identity and haptics** have thin evidence here (Fluent names sound as a signature experience); L04 covers sound and haptics.
- **Razorpay's rebrand** date and visuals were not confirmed; only Blade theming is solidly sourced.
- **Duolingo core-tabs article** shows "Feb 4" without a year on the page.
- **Most lever-matrix cells are practitioner inference.** The sourced anchors are listed per cell; the rest should be validated with preference testing of generated themes (Material's own method: paired comparisons on hierarchy, utility and style attributes) [S-L06-011].

## Confidence

- **Confirmed from Tier A primary sources today:** Carbon productive/expressive type sets and all six easing values; Carbon theming rule (tokens and roles fixed, values vary); IBM Design Language inventory and principles; Apple HIG branding (Sep 2026), writing and Liquid Glass guidance; M3 Expressive facts (46 studies, 18,000+ participants, 7 tactics, 1-2 hero moments); Material style-attribute research; Material static vs dynamic color and scheme-variant definitions; Google Sans history and Flex axes; Fluent principles and typography; GOV.UK principles (updated 2 Apr 2025) and 2025 brand-refresh rollout; Microsoft, Mailchimp, Atlassian and Apple content mechanics; Blade `createTheme`; SLDS 2 theming; Stripe CIELAB palette and 5/4-level contrast rule; Linear 3-input theme generator and 2026 refresh; Atlassian icon system; Spotify Mix; Notion campaign; DTCG 2025.10 type list; W3C/IBM text-expansion table.
- **Tier B (recognised practitioner or company blog, corroborated where numeric):** NN/g tone dimensions and design principles; Brad Frost theming; Walter design persona; Warren style tiles; Figma blogs (Razorpay, Spotify); Collins, Pentagram, Monotype, Dalton Maag, Opposite agency pages; It's Nice That (Airbnb 2025).
- **Snippet-level or secondary:** Uber 2018 rebrand details, Airbnb Cereal specifics, Mailchimp 2018 specifics (Cooper Light, Cavendish Yellow), Netflix Sans replacing Gotham, Hawkins structure, Zomato Okra, Instamart 2025 blue, academic findings.
- **Inferred (marked `[inferred]`):** most lever-matrix cells, the fixed-vs-flex default split, token naming proposals, default heuristics that synthesise several sources.
