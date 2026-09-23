# Glossary

Every term OpenDesigner uses, said three ways. Read the one that fits you.

- **Plain**: anyone can follow it, no design or coding background needed.
- **Designer**: the words designers use, and what it does to the look and feel.
- **Engineer**: how it is built: token names, formats, code.

Generated from `synthesis/glossary.json` by `python3 tools/check_glossary.py --build`. Edit the JSON, not this file.

**Sections:** [Everyday terms](#everyday-terms) · [Using OpenDesigner](#using-opendesigner) · [The eight dials](#the-eight-dials) · [Context and inputs](#context-and-inputs) · [Principles](#principles) · [Foundations](#foundations) · [Tokens](#tokens) · [Components](#components) · [Patterns and templates](#patterns-and-templates) · [Guardrails and validation](#guardrails-and-validation) · [Delivery and tooling](#delivery-and-tooling) · [Governance, docs and adoption](#governance-docs-and-adoption) · [How OpenDesigner works](#how-opendesigner-works)

## Everyday terms

### accent color

The one strong color used for main buttons and for things you pick.  
Designers: primary or brand accent · Code: `color.bg.accent`

<details><summary>Designer and engineer</summary>

**Designer:** One accent keeps a calm, focused feel and makes color mean "you can act here". Add a second accent only when it has a job, not for decoration.

**Engineer:** Roles like color.bg.accent.bold, color.text.accent and color.border.focus alias color.accent.* steps. Accent text passes 4.5:1 and accent boundaries 3:1 in every mode.

**Also called:** brand color, primary color

</details>

### alias

A name that points to another choice instead of holding a value of its own.  
Designers: linked token or reference · Code: `$value: {color.accent.light.9}`

<details><summary>Designer and engineer</summary>

**Designer:** A token that borrows another token's value, so one change flows down the chain. It is how semantic and component tokens stay linked to the palette.

**Engineer:** DTCG 2025.10: $value "{color.accent.light.9}" targets a whole token; {"$ref": JSON Pointer} reaches inside values. Chains are allowed; circular references are errors. Figma variables alias within one type.

**Also called:** reference, token reference

</details>

### anatomy

The small pieces a part is built from, like the box, the words and the icon of a button.  
Designers: labeled component parts · Code: `part in token path: button.primary.container (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The numbered parts of a component (container, label, icon) shown in its spec, so designers and engineers use the same names when discussing spacing, color and states.

**Engineer:** Named parts map to Figma layers or slots and to code sub-elements; planned component tokens name them: button.primary.container.color (proposed). EightShapes generates anatomy diagrams from layers.

**Also called:** component anatomy, parts

</details>

### asset hook

A question that asks if you have something a person must make, like a logo.  
Designers: asset request: do you have this? · Code: `data/hooks.json asset rows`

<details><summary>Designer and engineer</summary>

**Designer:** For logo, app icon, icons, illustration, photography, brand type, motion, sound and more, OpenDesigner asks "Do you have this?", lists accepted formats and offers fallbacks; placeholders are always labeled.

**Engineer:** 19 rows in data/hooks.json (14 asset, 5 tool); asset rows carry ask, accepts, does and if_no. Statuses: have, commissioning, tool, open-library, placeholder, not-needed.

**Also called:** Do you have this? question

</details>

### breakpoint

A screen width where the page changes its layout, like going to one column on a phone.  
Designers: layout breakpoint, mobile first · Code: `rem media query (not generated yet)`

<details><summary>Designer and engineer</summary>

**Designer:** Each one is a moment the layout visibly reorganizes: panes appear, navigation moves from bar to rail. Fewer breakpoints mean bigger shifts; design mobile first.

**Engineer:** Material 600/840/1200/1600dp width breakpoints (Tailwind's set for web-only), written as rem media queries. DTCG has no breakpoint type, and OpenDesigner does not generate breakpoints yet.

**Also called:** window size class

</details>

### color ramp

A row of shades of one color, from very light to very dark.  
Designers: tonal scale, 11-12 steps · Code: `color.accent.light.1 to .12`

<details><summary>Designer and engineer</summary>

**Designer:** Evenly stepped shades of one hue, usually 11 or 12 steps, so backgrounds, borders, hovers and text come from a set, not by eye.

**Engineer:** Ordered primitives like color.accent.light.1 to .12 plus a dark ramp: 12 steps generated in OKLCH as DTCG color objects with hex fallback; semantic tokens alias into them.

**Example:** Light blue for backgrounds, dark blue for text on them.

**Also called:** tonal palette, color scale, shades

</details>

### component

A ready piece of the screen, like a button, that you can use again and again.  
Designers: reusable component with variants · Code: `code component with props`

<details><summary>Designer and engineer</summary>

**Designer:** A reusable part with defined anatomy, variants, sizes and states, styled only by tokens. OpenDesigner's catalog lists 64 canonical components in 10 categories, from Button to App shell.

**Engineer:** A Figma component with properties (variant, boolean, instance swap, text, slot) mirrored by a code component with props; Code Connect links them. Docs in opendesigner/components/<name>.md are planned.

**Also called:** UI component, building block

</details>

### component token

A saved value for one part only, like the color of the main button.  
Designers: component-specific override · Code: `button.primary.bg (proposed) in component.tokens.json`

<details><summary>Designer and engineer</summary>

**Designer:** Lets one component be restyled on its own (button.primary.bg) without changing every accent in the product. Add them only when a brand must tune that component separately.

**Engineer:** Planned tier 3, not generated yet: button.primary.bg (proposed) = "{color.bg.action.primary}" in component.tokens.json, only for components restyled independently or values shared by three or more.

**Also called:** component-level token

</details>

### contrast ratio

A score for how much text stands out from what is behind it; higher is easier to read.  
Designers: contrast, 4.5:1 for body text · Code: `engine.py validate contrast check`

<details><summary>Designer and engineer</summary>

**Designer:** WCAG 2.2 AA: 4.5:1 for body text, 3:1 for large text, icons and control borders, 7:1 in high-contrast themes. Test colors as pairs, never alone.

**Engineer:** engine.py validate checks every foreground and background pair in every mode with no rounding (4.499:1 fails); APCA Lc 75 on body text is reported as an advisory note.

**Example:** 4.5:1 passes; 4.499:1 fails, because nothing is rounded.

**Also called:** color contrast

</details>

### corner radius

How round the corners of a box or button are, from sharp to fully round.  
Designers: corner radius, sharp to pill · Code: `radius.control, CSS border-radius`

<details><summary>Designer and engineer</summary>

**Designer:** The most varied visible lever across systems, from 0px to pill (median 6px). Radius should grow with component size, and nested corners stay concentric.

**Engineer:** CSS border-radius from tokens radius.0 to radius.32 (0, 2, 4, 6, 8, 12, 16, 20, 24, 28, 32) plus radius.full; the Roundness dial picks radius.control.

**Also called:** border radius, rounding

</details>

### dark mode

A dark version of the app where each color is picked with care, not flipped.  
Designers: dark theme, mapped by role · Code: `semantic.color.dark.tokens.json`

<details><summary>Designer and engineer</summary>

**Designer:** Map by role, not by value: each semantic color gets the dark step that keeps its light-mode contrast. Raised surfaces get lighter; accents soften to reduce glare.

**Engineer:** A resolver context (theme: dark) loading semantic.color.dark.tokens.json: same token names, re-pointed to other ramp steps (Atlassian 700 becomes 400). CSS scope via [data-theme] or prefers-color-scheme.

**Also called:** dark theme

</details>

### density

How tightly things are packed on the screen, from roomy to tight.  
Designers: compact, comfortable or spacious · Code: `semantic.density.{compact|comfortable|spacious}`

<details><summary>Designer and engineer</summary>

**Designer:** Dense layouts feel serious and focused and suit tables and dashboards; spacious ones feel calm and open. Density shrinks padding and row heights, never tap targets.

**Engineer:** A semantic-tier mode axis (semantic.density.compact|comfortable|spacious.tokens.json), separate from breakpoints and color; each step about 4px (Material -1 to -3). size.target.min stays fixed.

**Also called:** compactness

</details>

### DESIGN.md

A file in your project that writes down each design choice for people and AI to read.  
Designers: the living system doc · Code: `DESIGN.md via engine.py design-md`

<details><summary>Designer and engineer</summary>

**Designer:** The living, readable record of the system. Each section states the decision and its reason, a token table, use and avoid notes and its zoom level.

**Engineer:** Generated at the project root by engine.py design-md from state.json, tokens and decisions.md, in Google's DESIGN.md format plus nine OpenDesigner sections; never edited as a source.

**Also called:** DESIGN.md file

</details>

### design system

The shared rules and parts that make all the screens of an app look and work the same.  
Designers: foundations, components, patterns and governance · Code: `opendesigner/state.json plus generated tokens`

<details><summary>Designer and engineer</summary>

**Designer:** Foundations, tokens, components, patterns and the guidance and governance around them, so every team ships consistent, accessible screens without re-deciding color, type and spacing each time.

**Engineer:** OpenDesigner: opendesigner/state.json plus generated DTCG 2025.10 tokens, exports and DESIGN.md; component docs and lint rules are planned. Layers: context, principles, foundations, tokens, components, patterns, guardrails, delivery, governance.

</details>

### design to code

Turning design choices into code that makes the real app look that way.  
Designers: design handoff to code · Code: `engine.py export --format css`

<details><summary>Designer and engineer</summary>

**Designer:** The step where decisions become tokens, CSS and components. When code is generated from the same source, what ships matches the design instead of being re-measured from mockups.

**Engineer:** engine.py export --format css|tailwind|swift|compose|dtcg writes opendesigner/build/. Tokens carry code syntax so Figma binds to variables; Code Connect makes Figma's MCP emit your components.

**Also called:** handoff

</details>

### design token

A color, size or other choice with a name, kept in one place for the whole app.  
Designers: named decision, like brand blue · Code: `DTCG token with $value and $type`

<details><summary>Designer and engineer</summary>

**Designer:** A named decision (brand blue, 16px spacing, 200ms fade) that design files and code both reference, so changing it once restyles every screen and nothing drifts.

**Engineer:** A DTCG 2025.10 object with a required $value and a $type such as color, dimension or duration, named by dot path (color.bg.accent) and compiled to CSS custom properties.

**Example:** Atlassian's space.100 token equals 8px.

**Also called:** token

</details>

### designer-owned

A part that needs a real person to make it well, like a logo or photos.  
Designers: commissioned brand assets · Code: `class D, data/hooks.json asset hooks`

<details><summary>Designer and engineer</summary>

**Designer:** Only 7 blocks, but the ones people notice first: brand marks, photography, illustration, motion signature, graphic motifs, pictograms and sound. They are commissioned or supplied, never generated as final.

**Engineer:** Class D in L17: 7 ontology nodes expanding into 14 asset hooks (H-logo to H-brandbook in data/hooks.json), each with accepted formats, fallbacks and a briefed placeholder.

**Also called:** class D

</details>

### DTCG

A shared way to write design choices that both design apps and code can read.  
Designers: the open token format · Code: `DTCG 2025.10 .tokens.json files`

<details><summary>Designer and engineer</summary>

**Designer:** The open token format Figma, Penpot, Tokens Studio, Style Dictionary and Terrazzo support, so tokens move between tools without retyping. Stable since 28 Oct 2025.

**Engineer:** Design Tokens Format Module 2025.10 plus Color and Resolver modules (a Final Community Group Report). Files are .tokens.json with $value, $type, $description, $extensions; themes go in .resolver.json.

**Also called:** Design Tokens Community Group format, DTCG 2025.10

</details>

### easing curve

How a move speeds up and slows down, like a car that pulls away and then brakes.  
Designers: easing: decelerate in, accelerate out · Code: `DTCG cubicBezier, CSS cubic-bezier()`

<details><summary>Designer and engineer</summary>

**Designer:** Decelerate curves make entrances feel quick and arriving; accelerate curves get exits out of the way; linear is only for spinners and progress. Keep a small named set.

**Engineer:** DTCG cubicBezier: four numbers, x values in [0, 1] and y unbounded, so overshoot is allowed; CSS cubic-bezier(). Defaults: standard (0.2, 0, 0, 1), exit (0.3, 0, 1, 1).

**Also called:** easing, timing function, cubic-bezier

</details>

### elevation

How high a part of the screen seems to float above the part below it.  
Designers: resting, raised and overlay levels · Code: `elevation.raised to elevation.overlay`

<details><summary>Designer and engineer</summary>

**Designer:** Shows stacking order: most products visibly use three levels (resting, raised, overlay). Depending on the depth model it shows as shadow, lighter tone, border or glass.

**Engineer:** Semantic elevation.raised, .floating and .overlay: DTCG shadow arrays colored {color.shadow.key} and {color.shadow.ambient}, set by the depth model; in dark mode raised surfaces also step lighter.

**Also called:** depth, z-depth

</details>

### extractable

A part that can be read from something you already have, like your logo or site.  
Designers: taken from your existing brand · Code: `class E, value with provenance`

<details><summary>Designer and engineer</summary>

**Designer:** Blocks best taken from what exists: your brand book, live product, repo or Figma file. Each value shows where it came from; you accept, adjust or ignore it.

**Engineer:** Class E in the L17 scheme: 5 blocks primarily, 44 by any route. Read at intake; each value carries provenance (reference id, method computed|pixel|vision|file, confidence).

**Also called:** class E

</details>

### Figma variables

Named colors and sizes kept in Figma, a design app, that can switch to dark mode.  
Designers: Figma variables, collections and modes · Code: `build/figma/import/, one file per mode`

<details><summary>Designer and engineer</summary>

**Designer:** Figma's version of tokens: color, number, string, boolean, timing and easing values in collections with modes, aliasable across collections and scoped to the right property pickers.

**Engineer:** Modes: 10 per collection on Professional, 20 on Organization. Native DTCG import takes one file per mode (sRGB/HSL colors, px, seconds); composites like typography do not import.

**Also called:** variable collections

</details>

### Fitts's law

Big buttons that are close by are faster to hit than small ones far away.  
Designers: big, close targets · Code: `size.target.min plus target lint`

<details><summary>Designer and engineer</summary>

**Designer:** Size targets generously and put the primary action near the content it acts on. Label key actions with text and icon. Screen-edge targets help mouse users but hurt touch users.

**Engineer:** T = a + b·log2(2D/w) (Fitts 1954). Encoded as size.target.min, fixed across densities, plus a lint error for targets under 24x24 CSS px.

**Also called:** Fitts' law

</details>

### focus ring

The outline that shows which button or box you are on when you use the keyboard.  
Designers: focus indicator · Code: `focus.ring.* on :focus-visible`

<details><summary>Designer and engineer</summary>

**Designer:** Must show on every background: a 2px ring, 2px offset, following the control's corner, in a color with 3:1 contrast. Never remove it.

**Engineer:** CSS outline on :focus-visible from focus.ring.width, focus.ring.offset and color.border.focus (per mode); radius.focus = radius.control + offset; forced-colors uses Highlight. WCAG 2.4.7 AA.

**Also called:** focus indicator, focus outline

</details>

### font weight

How thick or thin the letters are, from very thin to very bold.  
Designers: two to four weights · Code: `fontWeight 100-900, CSS font-weight`

<details><summary>Designer and engineer</summary>

**Designer:** Most systems use two to four weights: 400 body, 500-600 labels, 600-700 headings. Light (300) only at 32px and up. Weight-led hierarchy looks punchy; size-led looks airy.

**Engineer:** DTCG fontWeight: a number 1-1000 or an alias (thin 100 to black 900, extra-black 950); CSS font-weight. Expression sets type.weightCount 2-4; Energy sets heading weight 600-750.

**Also called:** weight, boldness

</details>

### gap

The empty space between things lined up in a row, a column or a grid.  
Designers: gap, auto layout spacing · Code: `space.inline.*, space.stack.*, CSS gap`

<details><summary>Designer and engineer</summary>

**Designer:** Even spacing between siblings set once on the container, so every list, toolbar and form keeps the same rhythm without per-item margins.

**Engineer:** CSS gap on flex and grid containers, from semantic dimension tokens like space.inline.sm = "{space.8}" or space.stack.lg. Figma: number variables scoped to gap.

**Also called:** stack spacing, inline spacing

</details>

### generatable

A part the tool can work out by itself from a few of your answers.  
Designers: sensible defaults to adjust · Code: `class G, from levers.json formulas`

<details><summary>Designer and engineer</summary>

**Designer:** About two thirds of a system, such as spacing, ramps, most tokens and components, follows from a few inputs and the eight dials. These get sensible defaults you adjust visually.

**Engineer:** Class G (135 of 207 blocks in L17): computed by the synthesis/levers.json formulas from raw inputs and dials, or a sourced default. Decided silently, shown for adjustment.

**Also called:** class G

</details>

### Gestalt grouping

We see things that sit close together, or inside the same box, as one group.  
Designers: common region, proximity, similarity · Code: `innerOuterRatio in space $extensions`

<details><summary>Designer and engineer</summary>

**Designer:** The best-evidenced visual principle, with a strength order: a shared boundary beats proximity, and proximity beats similarity. Keep space within groups clearly smaller than space between them.

**Engineer:** Enforced by construction: inner spacing tokens resolve below outer ones (innerOuterRatio 2 to 3.5 by density, in the space group's $extensions.opendesigner). Planned critique: flag containers nested over two deep.

**Also called:** proximity, common region, similarity

</details>

### grid

Columns you can't see that help line things up across a page.  
Designers: columns, gutters and margins · Code: `grid.columns, grid.gutter, grid.margin (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Columns, gutters and margins that align content. 4, 8 and 12 columns suit most products; 16 suits editorial or wide dashboards. Type never hangs into the gutter; containers may.

**Engineer:** Not generated yet: grid.columns (proposed) as a number, grid.gutter and grid.margin (proposed) as dimensions per breakpoint, driving CSS grid-template-columns: 4, 8, 12 columns; 16-24px gutters.

**Also called:** column grid, layout grid

</details>

### Hick's law

The more choices you see, the longer it takes to pick, unless they are in groups or you can search.  
Designers: group and label choices · Code: `planned flat-list warning above 10-12 items`

<details><summary>Designer and engineer</summary>

**Designer:** Holds when choices are known and equally likely; newcomers scan lists one by one. Group, label, order and add search, and default one option. Never cut items to satisfy it.

**Engineer:** RT = a + b·log2(n) (Hick and Hyman 1952). Planned lint: warn on flat, ungrouped lists above roughly 10-12 items with no search, sections or typeahead (threshold inferred).

**Also called:** Hick-Hyman law

</details>

### icon

A small picture that stands for an action or thing, like a trash can for delete.  
Designers: one icon set, matched stroke · Code: `size.icon.md, icon.stroke.md`

<details><summary>Designer and engineer</summary>

**Designer:** One library, stroke matched to body text weight, corners matched to Roundness. Label key actions; a meaningful icon standing alone needs a text alternative and 3:1 contrast.

**Engineer:** SVG on the library grid; size.icon.sm/md/lg = 16/20/24px; icon.stroke.sm/md/lg = 1.5/2/2.5px, scaled by size and label weight.

**Also called:** glyph, symbol

</details>

### letter spacing

How close together or far apart the letters in a word sit.  
Designers: tracking · Code: `letter-spacing (DTCG letterSpacing)`

<details><summary>Designer and engineer</summary>

**Designer:** Zero at body sizes, slightly positive (+0.02-0.05em) for small text and all caps, slightly negative from about 32px so big headlines feel dense and designed.

**Engineer:** DTCG letterSpacing is a dimension (px or rem only) inside typography, though em is the natural unit; CSS letter-spacing. Figma letter-spacing variables are px, not %.

**Also called:** tracking

</details>

### line height

How much room each line of text gets from top to bottom, so lines don't crowd.  
Designers: leading · Code: `line-height (DTCG lineHeight)`

<details><summary>Designer and engineer</summary>

**Designer:** Tight (1.1-1.25) makes headings solid; about 1.5 keeps paragraphs easy to follow. Bigger text wants a smaller ratio, longer lines a larger one; snap to 4px.

**Engineer:** Unitless number in the DTCG typography composite (lineHeight, a multiplier of fontSize); CSS line-height. Default: ratio rounded to the nearest 4px; Carbon ships compact 14/18 beside 14/20.

**Also called:** leading

</details>

### lint rule

A check that runs by itself and flags a mistake, like too many text sizes.  
Designers: design lint: errors and warnings · Code: `engine.py validate; lint/ folder planned`

<details><summary>Designer and engineer</summary>

**Designer:** Accessibility breaks are errors to fix before export; taste rules, such as more than 10 type sizes or bounce above 0.2, are warnings you may waive with a reason.

**Engineer:** engine.py validate runs deterministic checks and exits 1 on errors; findings cite their rule; waivers sit in state.json. A stylelint config in opendesigner/lint/ is planned (spec 7.12).

**Also called:** lint check, automated check

</details>

### margin

The empty space outside a box that keeps it away from the things next to it.  
Designers: outer margin at page edges · Code: `CSS margin; space.section.* between groups`

<details><summary>Designer and engineer</summary>

**Designer:** Space around an element or page edge. Prefer padding on the parent and gap between siblings; keep margins for page edges and layout sections so spacing stays predictable.

**Engineer:** CSS margin. Components set no outer margin; space.section.* spaces groups. Material's page margin is 16 compact, 24 above; page-margin tokens like layout.margin.compact (proposed) are not generated.

**Also called:** outer spacing

</details>

### MCP

A common plug that lets an AI helper use other apps, like Figma.  
Designers: AI link to your tools · Code: `Model Context Protocol server`

<details><summary>Designer and engineer</summary>

**Designer:** Lets your AI assistant read and write in the tools you use: pull a Figma frame, push tokens to Figma variables or Paper, or show a visual picker inside chat.

**Engineer:** Model Context Protocol (spec 2026-07-28): servers expose tools, resources and prompts over stdio or remote HTTP; the MCP Apps extension renders server HTML in a sandboxed iframe.

**Also called:** Model Context Protocol

</details>

### mode

One full set of the saved values, such as the light set or the dark set.  
Designers: light, dark or compact mode · Code: `DTCG resolver context (theme: dark)`

<details><summary>Designer and engineer</summary>

**Designer:** Swaps every value at once while names stay fixed: light or dark, compact or comfortable, standard or reduced motion. Designs switch mode instead of being redrawn.

**Engineer:** DTCG keeps modes in the resolver: a context (theme: light or dark) picks one file per mode, such as semantic.color.dark.tokens.json. Figma: a column per mode.

**Also called:** token mode, context

</details>

### motion duration

How long a move on screen lasts, most of the time well under a second.  
Designers: timing, snappy to smooth · Code: `motion.duration.short, CSS transition-duration`

<details><summary>Designer and engineer</summary>

**Designer:** Most UI motion runs 100-300ms: short feels snappy, long feels smooth, past about 500ms it drags. Make exits 20-35% shorter than entrances.

**Engineer:** DTCG duration tokens. At Energy 50: motion.duration.instant 0, micro 100, short 150, medium 250, long 400, extra 700ms; Energy scales medium and longer by 0.8-1.2.

**Also called:** animation duration, timing

</details>

### native look

Making an app look at home on your phone by using the phone's own buttons and letters.  
Designers: native, system look · Code: `dials.brandPresence 0-25, nativeShare near 1.0`

<details><summary>Designer and engineer</summary>

**Designer:** System fonts and components almost everywhere, brand only in accents, content and voice. Feels at home and inherits OS updates like Liquid Glass, but looks more like other apps.

**Engineer:** At the low end, Brand presence 0-25 suggests the system font per platform and nativeShare near 1.0; below 50, a native lead platform keeps its own body size.

**Also called:** native-first, system look

</details>

### neutral

The grays for text, backgrounds and lines, at times with a faint hint of color.  
Designers: grays, pure or tinted · Code: `color.neutral.light.1 to .12`

<details><summary>Designer and engineer</summary>

**Designer:** Pure gray reads neutral and tool-like, suiting photo and data apps; a slight tint toward the brand, warm or cool sets the product's temperature.

**Engineer:** A 12-step ramp per theme: color.neutral.light.1 to .12 and color.neutral.dark.*. Tinted ramps keep OKLCH chroma about 0.01-0.03 mid-ramp, 0-0.008 at the ends.

**Also called:** gray ramp, neutrals

</details>

### OKLCH

A way to write a color by how light it is, how strong it is and which color it is.  
Designers: perceptual color space · Code: `oklch(L C H)`

<details><summary>Designer and engineer</summary>

**Designer:** A perceptual color space: blue 600 and green 600 look equally heavy, so ramps stay balanced and hue swaps keep hierarchy. HSL makes yellows wash out and blues go muddy.

**Engineer:** CSS oklch(L C H), Baseline since May 2023; Tailwind v4 uses it for its whole palette. DTCG color object: colorSpace "oklch", components [L, C, H], optional hex fallback.

**Also called:** oklch()

</details>

### owner input

A choice only your team can make, like who the app is for or which devices it runs on.  
Designers: business decisions, owner's call · Code: `class I questions`

<details><summary>Designer and engineer</summary>

**Designer:** Business decisions, not design work: scope, audience, platforms, governance, terminology. OpenDesigner asks them, pre-fills from hints in your repo or references, and never invents an answer.

**Engineer:** Class I, the fifth class L17 added (29 blocks), so business decisions are not misfiled as designer-owned or generatable; questions tagged class "I" are asked or pre-filled, never invented.

**Also called:** class I, owner decision

</details>

### padding

The empty space inside a box, between its edge and what is in it.  
Designers: inner padding or inset · Code: `space.inset.md, CSS padding`

<details><summary>Designer and engineer</summary>

**Designer:** Inner breathing room of buttons, cards and fields. Keep it smaller than the space between groups so related things read together; parents own spacing, children never add outer margins.

**Engineer:** CSS padding, fed by semantic inset tokens such as space.inset.md = "{space.12}" (dimension). Density modes shrink insets one scale step; Material uses padding and gap before margins.

**Also called:** inset

</details>

### pattern

A tried way to put parts together for a common job, like a sign-up form.  
Designers: UX pattern for a recurring task · Code: `pat.* ontology layer`

<details><summary>Designer and engineer</summary>

**Designer:** A composition of components plus behavior rules for a recurring task: forms, validation, search and filtering, empty states, onboarding. It encodes when to use it, not only how it looks.

**Engineer:** 13 patterns (L08 P1 to P13), each listing the catalog components it composes, its key decisions and evidence-backed rules; stored under the pat.* ontology layer.

**Also called:** UX pattern, design pattern

</details>

### platform convention

The way a phone or computer expects things like menus and going back to work.  
Designers: native behaviors, shared brand · Code: `behavior.navigationNative = true`

<details><summary>Designer and engineer</summary>

**Designer:** Share what users perceive as the brand (color, type personality, illustration, voice); adopt the platform's version of how the device works: navigation, back, sheets, pickers, text fields, system icons.

**Engineer:** The behavior.navigationNative param is true at every Brand presence value. Mapping tokens to platform colors, such as color.text.primary to iOS label, is planned; exports emit literal values.

**Also called:** platform guidelines

</details>

### primitive token

A raw value with a plain name, like "blue 500", that says what it is, not what it is for.  
Designers: raw palette and scales · Code: `color.accent.light.9 in primitives.tokens.json`

<details><summary>Designer and engineer</summary>

**Designer:** The raw palette and scales (blue.500, space.200) with no meaning attached. Designers pick from semantic tokens instead; primitives are the ingredients those tokens point to.

**Engineer:** Bottom tier: single-valued tokens such as color.accent.light.9 (OKLCH color object) or space.16 (dimension). Values never change per mode; semantic tokens alias them. File: primitives.tokens.json.

**Example:** blue.500 is a primitive; it knows its color but not its job.

**Also called:** base token, global token, reference token

</details>

### progressive disclosure

Showing only what you need now and keeping the rest out of sight until you ask.  
Designers: advanced options behind a trigger · Code: `pat.disclosure, WAI-ARIA disclosure pattern`

<details><summary>Designer and engineer</summary>

**Designer:** Main options up front, advanced ones behind a clearly labeled trigger such as "More options" or an accordion. Keep it to two levels, and never hide essentials behind hover.

**Engineer:** Ontology node pat.disclosure; no DTCG type, it composes components. Built from C53 Accordion or disclosure using the WAI-ARIA disclosure pattern, at most two levels deep.

**Also called:** staged disclosure, show more

</details>

### reduced motion

A setting on your phone or computer that asks apps to move less, for people who get dizzy.  
Designers: reduced motion, no travel · Code: `prefers-reduced-motion, motion.reduced.tokens.json`

<details><summary>Designer and engineer</summary>

**Designer:** Keep feedback (color and opacity changes, crossfades) and remove travel: sliding, scaling, parallax and bounce. A good reduced mode still feels polished, not broken.

**Engineer:** Web @media (prefers-reduced-motion: reduce); iOS Reduce Motion, Android Remove animations. OpenDesigner's motion mode (motion.reduced.tokens.json): short fades, movement at 0ms, no translate or scale.

**Also called:** prefers-reduced-motion, Reduce Motion

</details>

### reference intake

Looking at a site you like to learn how it is built, without copying its name or logo.  
Designers: reference for structure, not identity · Code: `opendesigner-extract skill`

<details><summary>Designer and engineer</summary>

**Designer:** Carries structure and quality, never identity: no name, logo, photos, copy or proprietary fonts. A reference's brand color lends its role and strength, not its hex.

**Engineer:** The opendesigner-extract skill reads a URL, screenshot, Figma file, repo CSS or brand book; engine.py intake runs the LEVERS formulas backwards to proposed dials, accepted with --set-by reference --source-ref.

**Also called:** reference extraction

</details>

### resolver file

A small file that says which value files to mix for each look, like light or dark.  
Designers: the recipe behind themes · Code: `opendesigner.resolver.json`

<details><summary>Designer and engineer</summary>

**Designer:** The recipe behind themes: it lists the token sets and switches (theme, brand, density) and which one wins, so tools produce every light, dark or brand combination consistently.

**Engineer:** DTCG Resolver Module 2025.10: version, sets, modifiers with contexts, and resolutionOrder (later entries win). OpenDesigner writes opendesigner.resolver.json; Terrazzo supports resolvers, Style Dictionary v5 does not.

**Also called:** .resolver.json, resolver document

</details>

### semantic token

A value named for its job, like "page background", that points to a raw value below it.  
Designers: named by role, not look · Code: `color.bg.accent.bold = {color.accent.light.9}`

<details><summary>Designer and engineer</summary>

**Designer:** Named by role, not by look: color.bg.accent, color.text.subtle. Themes, dark mode and rebrands re-point these names, so designs stay correct without touching every screen.

**Engineer:** Tier 2: $value is a reference, color.bg.accent.bold = "{color.accent.light.9}". Modes live here; each resolver context re-points it (dark: {color.accent.dark.9}).

**Example:** Page background is white in light mode and near-black in dark.

**Also called:** alias token, system token, role token

</details>

### shadow

A soft dark patch drawn under something to make it look lifted off the page.  
Designers: drop shadow, contact plus blur · Code: `DTCG shadow, CSS box-shadow`

<details><summary>Designer and engineer</summary>

**Designer:** Two layers read realistic: a sharp contact shadow for the edge and a soft blur for distance, tinted neutral rather than pure black. Shadows are decorative, so boundaries need contrast.

**Engineer:** DTCG shadow: an object or array of {color, offsetX, offsetY, blur, spread, inset}, emitted as CSS box-shadow. Alias color to {color.shadow.key} so dark mode can swap it.

**Also called:** drop shadow, box shadow

</details>

### sketch level

The first quick pass: a whole but rough design system from a few answers.  
Designers: quick sketch of the whole system · Code: `zoom0 questions in pacing.json`

<details><summary>Designer and engineer</summary>

**Designer:** A handful of questions (scope, audience, platforms, brand, color, logo) yield a complete but coarse system you can use right away, then refine area by area.

**Engineer:** Zoom level 0: the six zoom0 questions in pacing.json; every other decision keeps its auto_default, so the engine still generates a complete token set and DESIGN.md.

**Also called:** zoom 0, Level 0

</details>

### skill

A folder of instructions an AI helper reads so it knows how to do one job well.  
Designers: installable AI workflow · Code: `SKILL.md folder (Agent Skills format)`

<details><summary>Designer and engineer</summary>

**Designer:** A packaged way of working you load into your own AI tool. OpenDesigner ships as skills: install them and your assistant runs the design-system interview and writes the files.

**Engineer:** Agent Skills format: a folder with SKILL.md (name and description frontmatter) and optional scripts/, references/ and assets/. Loaded by Claude, ChatGPT and Codex, Cursor, Copilot, Gemini CLI and more.

**Also called:** Agent Skill, SKILL.md

</details>

### source of truth

The one place where you change a value; every other copy is made from it.  
Designers: single source of truth · Code: `opendesigner/state.json plus DTCG tokens`

<details><summary>Designer and engineer</summary>

**Designer:** Decide where edits happen first. Whichever side is not the source drifts unless sync is automatic, so Figma becomes a synced view, not a second master.

**Engineer:** In OpenDesigner, opendesigner/state.json plus the DTCG tokens it generates; DESIGN.md, CSS, Swift, Compose, Figma and Paper are generated views. Code-canonical remains an option for mature systems.

**Also called:** single source of truth, canonical source

</details>

### spacing scale

A short list of gap sizes the whole app picks from, like marks on a ruler.  
Designers: 4-point grid, 8-point rhythm · Code: `space.0 to space.96`

<details><summary>Designer and engineer</summary>

**Designer:** A 4px grid with an 8px rhythm, about 15 steps from 0 to 96. Steps differ enough that tight-within, loose-between grouping reads at a glance.

**Engineer:** Dimension primitives space.0 to space.96 in px, named by value (space.16 = 16px); components use semantic aliases like space.inset.md = "{space.12}", never raw steps.

**Example:** 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96.

**Also called:** space scale, spacing ladder

</details>

### spring animation

Movement that acts like a real spring, coming to rest with maybe a small bounce.  
Designers: spring motion with bounce · Code: `motion.spring.* in $extensions.opendesigner`

<details><summary>Designer and engineer</summary>

**Designer:** Defined by stiffness and damping instead of a fixed time, so motion feels natural and keeps its speed when interrupted. Use bounce for spatial hero moments; fades stay critically damped.

**Engineer:** No DTCG spring type: store dampingRatio and stiffness (M3 standard 0.9 and 700) in $extensions.opendesigner, derive duration and bounce for Apple, and sample into CSS linear() for web.

**Also called:** spring, physics-based motion

</details>

### state

How a part looks at a moment, like when you point at it, press it, or it is off.  
Designers: hover, pressed, focus, disabled · Code: `:hover, :focus-visible, :active, :disabled`

<details><summary>Designer and engineer</summary>

**Designer:** Style enabled, hover, focus-visible, pressed, selected, disabled, loading and error. States that carry meaning need 3:1 against neighbors; touch screens have no hover, so never hide essentials there.

**Engineer:** CSS :hover, :focus-visible, :active, :disabled plus aria-*. Hover and press shift one and two ramp steps (color.bg.accent.boldHover, boldPressed); opacity.state.hover covers unknown colors.

**Also called:** interaction state

</details>

### status colors

Colors that tell you how things went, like green for good and red for a problem.  
Designers: success, warning, error, info · Code: `color.bg.success.subtle, color.text.success`

<details><summary>Designer and engineer</summary>

**Designer:** Success, warning, error and info, each with subtle and bold levels. Never rely on color alone: pair with an icon and text, and put dark text on yellow fills.

**Engineer:** color.bg.<status>.subtle, .bold, .boldHover; color.text.<status>, color.border.<status>; icons use color.text.<status>. Text 4.5:1, icons and borders 3:1. Color-only meaning: planned lint error.

**Also called:** feedback colors, semantic colors

</details>

### surface

A background layer that things sit on, like a card on a page.  
Designers: background levels, sunken to overlay · Code: `color.surface.sunken, .base, .raised, .overlay`

<details><summary>Designer and engineer</summary>

**Designer:** Stacked background levels (sunken, base, raised, overlay) that separate page, cards and popovers. Light mode separates them with subtle tone plus shadow or border; dark mode with lighter tones.

**Engineer:** Role-named color tokens re-pointed per theme: color.surface.sunken, .base, .raised, .overlay, plus .nav and .tinted. Compare Material 3 surface-container-lowest to -highest and Carbon $layer-01 to 03.

**Also called:** layer, background level

</details>

### template

A ready page plan made from bigger pieces, like a settings page.  
Designers: page template · Code: `L08 template mapped to catalog ids`

<details><summary>Designer and engineer</summary>

**Designer:** A page-level arrangement of patterns and components that sets content structure before real content arrives. The catalog covers dashboard, list, detail, settings and marketing landing pages.

**Engineer:** Five templates in L08, each mapped to catalog ids: a dashboard uses C63 app shell, C33 sidebar, C52 cards and C57 table.

**Also called:** page template, page layout

</details>

### theme

A named look for the whole app, such as your brand in dark mode.  
Designers: brand plus scheme combination · Code: `[data-theme] scope per resolver context`

<details><summary>Designer and engineer</summary>

**Designer:** A named combination (Brand A, dark, high contrast) applied across the system. Keep brand, color scheme and density as separate axes so combinations need not be drawn by hand.

**Engineer:** One permutation of DTCG resolver modifiers; outputs multiply (4, 3 and 2 contexts give 24). Keep modifiers orthogonal. CSS export emits one [data-theme] scope per context.

**Also called:** brand theme

</details>

### tool-assisted

A part a coder can make with a named tool, with a few things to watch for.  
Designers: made with a named tool · Code: `class T, tool named and recorded`

<details><summary>Designer and engineer</summary>

**Designer:** Blocks an engineer can produce with a named tool, with a caveat: font sourcing, icons, voice drafting and the token pipeline. OpenDesigner recommends the tool and states the catch.

**Engineer:** Class T in L17 (31 blocks): OpenDesigner names the tool (Terrazzo, Figma MCP, Code Connect), runs or links it, states the caveat and records the choice.

**Also called:** class T

</details>

### touch target

The area you can tap to press a button, which can be bigger than what you see.  
Designers: tap or hit area · Code: `size.target.min`

<details><summary>Designer and engineer</summary>

**Designer:** Minimum hit area: 24 by 24 CSS px on web (WCAG 2.2 AA), 44pt on Apple, 48dp on Android. Visuals may shrink with density; hit areas never do.

**Engineer:** size.target.min, fixed across density modes: 24 CSS px web, 44pt iOS, 48dp Android. engine.py validate errors when a target token falls below its floor.

**Also called:** hit area, tap target

</details>

### type scale

The short list of text sizes an app uses, from small labels to big titles.  
Designers: modular scale by ratio · Code: `font.size.* from type.ratio`

<details><summary>Designer and engineer</summary>

**Designer:** Sizes grown from a base by a ratio: 1.125-1.2 feels calm and dense, 1.25 suits product plus marketing, 1.333+ feels editorial. Use three sizes or fewer per view.

**Engineer:** size(n) = base x ratio^n, rounded to whole pixels; stored as font.size.* dimension primitives. Expression sets type.ratio 1.2/1.25/1.333; Density above 66 caps it at 1.2.

**Example:** Base 16 at ratio 1.25 gives 16, 20, 25, 31, 39.

**Also called:** typescale, type ramp

</details>

### typeface

A set of letters that all share one look, like the letters on an iPhone.  
Designers: brand or system typeface · Code: `DTCG fontFamily, CSS font-family`

<details><summary>Designer and engineer</summary>

**Designer:** The main personality choice in type: system fonts feel native, open faces like Inter feel neutral, proprietary faces like Plex or Cereal feel brand-led. Check licence and script coverage early.

**Engineer:** DTCG fontFamily: a string or an array in fallback order, e.g. ["Inter", "system-ui", "sans-serif"]. Emitted as CSS font-family; Figma import accepts a single string only.

**Example:** SF Pro on Apple devices, Roboto on Android.

**Also called:** font family, font

</details>

### variant

Another look for the same part, like a bold main button and a plain second one.  
Designers: primary, secondary, tertiary, destructive · Code: `variant="primary" prop`

<details><summary>Designer and engineer</summary>

**Designer:** Styled versions of one component that signal emphasis or purpose: primary, secondary, tertiary, destructive. Keep one primary per view; a lint warning for more is planned.

**Engineer:** A Figma variant property plus code prop (variant="primary"), styled by roles like color.bg.action.primary, not yet by button.primary.bg (proposed). Variants multiply with size and state.

**Also called:** style variant, emphasis level

</details>

### visual hierarchy

The order your eye sees things on a screen, set by size, boldness, color and place.  
Designers: hierarchy and emphasis · Code: `type.ratio, emphasis.maxPrimaryPerView`

<details><summary>Designer and engineer</summary>

**Designer:** Guide attention by importance: one dominant element, three distinct levels, no more than three type sizes and one primary action per view. If everything looks the same, nothing stands out.

**Engineer:** Levers: type.ratio from Expression and emphasis.maxPrimaryPerView = 1 (recorded, not checked yet); a warning above 3 type sizes per view is planned. Role tokens stay decoupled from HTML headings.

**Also called:** emphasis order

</details>

### WCAG

The main rule book that helps apps and sites work for people who can't see, hear or move well.  
Designers: WCAG 2.2 AA · Code: `WCAG 2.2 AA in engine.py validate`

<details><summary>Designer and engineer</summary>

**Designer:** Version 2.2, level AA, is the usual target: text contrast 4.5:1, non-text contrast 3:1, visible focus, 24 by 24 CSS px minimum targets. AAA is stricter.

**Engineer:** Criteria OpenDesigner builds in: 1.4.3 and 1.4.11 contrast, 2.4.7 focus visible, 2.5.8 target size (AA), and 2.3.3 animation from interactions (AAA).

**Also called:** Web Content Accessibility Guidelines, WCAG 2.2

</details>

### zoom level

How far one part of your design has come, from a rough sketch to full detail.  
Designers: sketch, broad, defined, detailed · Code: `zoom 0-3 in references/pacing.json`

<details><summary>Designer and engineer</summary>

**Designer:** Everyone starts with a sketch of the whole system, then zooms into any area and can stop at any level with something that works. DESIGN.md shows each section's level.

**Engineer:** Levels 0 sketch, 1 broad, 2 defined, 3 detailed (references/pacing.json). Questions carry a zoom field; a stage asks only those at or below the level being worked.

**Also called:** zoom, detail level

</details>

## Using OpenDesigner

### build (engine command)

Does every making step in one go, then checks the result for problems.  
Designers: end-of-step rebuild · Code: `engine.py build`

<details><summary>Designer and engineer</summary>

**Designer:** The one command to run at the end of a step or session. It rebuilds values, exports, guides and preview, then reports any problems.

**Engineer:** engine.py build runs generate, export --format all, design-md and preview, then validate; it exits 1 if validation finds errors.

**Example:** Run build before you show the result to your team.

</details>

### design-md (engine command)

Writes two short, easy pages: one about how your app looks, and one about what it is for.  
Designers: rebuild the readable guide · Code: `engine.py design-md`

<details><summary>Designer and engineer</summary>

**Designer:** Produces the readable guide to the system and a separate product brief. Hand-written notes survive only inside keep blocks; the rest is rebuilt from decisions.

**Engineer:** engine.py design-md [--out DIR] renders DESIGN.md and PRODUCT.md at the project root from state.json, tokens and decisions.md; only <!-- od:keep --> blocks survive regeneration.

**Example:** Run it after each choice so the guide stays current.

</details>

### export (engine command)

Copies your design into the forms that websites, phone apps and design tools can read.  
Designers: hand off to every tool · Code: `engine.py export --format all`

<details><summary>Designer and engineer</summary>

**Designer:** Hands the system to each place it lives: web styles, a Tailwind theme, Figma variables, Paper, iOS and Android code, all from one source.

**Engineer:** engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg|all writes one subfolder per format in opendesigner/build/, for example css/tokens.css or swift/DesignTokens.swift.

**Example:** Export to Tailwind for the website and Swift for the iPhone app.

</details>

### feedback (engine command)

Notes a problem or idea about this tool, so you can send it to the people who make it.  
Designers: log gaps, bugs and ideas · Code: `engine.py feedback <text> --kind idea`

<details><summary>Designer and engineer</summary>

**Designer:** Captures gaps, bugs, confusing steps and ideas while you work, ready to send to the project as an issue. Nothing is posted unless you say yes.

**Engineer:** engine.py feedback "text" --kind gap|bug|confusing|idea (default idea) appends an F-nnn entry to opendesigner/feedback.md and prints a pre-filled GitHub issue link. Nothing is posted.

**Example:** A question you had to ask twice becomes a confusing note.

</details>

### generate (engine command)

Turns your saved choices into the full list of colors, sizes and spacing your app will use.  
Designers: rebuild all values · Code: `engine.py generate`

<details><summary>Designer and engineer</summary>

**Designer:** Rebuilds every design value from your decisions, including light and dark, density and reduced motion. Run it after each step that changes values.

**Engineer:** Writes opendesigner/tokens/: DTCG 2025.10 files per tier and mode (primitives, semantic, semantic.color.light.tokens.json and .dark, density, motion), opendesigner.resolver.json and opendesigner.meta.json.

**Example:** Change the brand color, then generate to see new shades.

</details>

### init (engine command)

Starts a new, blank design in your project, with safe first answers already filled in.  
Designers: start from sourced defaults · Code: `engine.py init`

<details><summary>Designer and engineer</summary>

**Designer:** The first step of a session. It opens a system on sourced defaults, so every later choice is a change from a known starting point.

**Engineer:** engine.py init [--name "Acme"] [--from path] [--force] creates ./opendesigner/state.json from levers.json defaults and opens decisions.md with entry D-0001. Refuses to overwrite without --force.

**Example:** Type init once, then answer the first question.

</details>

### intake (engine command)

Looks at the sizes in a site or file you like and turns them into first ideas for your design.  
Designers: measure a reference into dials · Code: `engine.py intake <measurements.json>`

<details><summary>Designer and engineer</summary>

**Designer:** Turns what was measured on a reference, like its corner radii or type sizes, into proposed dial positions. Nothing changes until you accept. Competitor references propose nothing.

**Engineer:** engine.py intake <measurements.json> [--accept] [--json] fits reference measurements to proposed dials and raw inputs with confidence levels; --accept records each as set --set-by reference --source-ref <ref-id>.

**Example:** A site with round buttons suggests a high roundness dial.

</details>

### lock and unlock (engine commands)

Lock keeps a choice safe so no one changes it by mistake, and unlock lets it change again.  
Designers: lock or unlock a decision · Code: `engine.py lock / unlock <path>`

<details><summary>Designer and engineer</summary>

**Designer:** Protects decisions that must not drift, such as brand colors or accessibility floors. Unlocking needs the owner's clear consent, so later sessions cannot quietly restyle them.

**Engineer:** engine.py lock <path>, engine.py unlock <path>. Sets locked on the answer or dial record, or adds the path to state.json locks; set refuses locked paths without --force.

**Example:** Lock the brand teal so no one swaps it later.

**Also called:** freeze a decision

</details>

### pick (engine command)

Saves your answer to one question in the chat, along with your reason.  
Designers: answer a question by id · Code: `engine.py pick <Q-id> <option-value>`

<details><summary>Designer and engineer</summary>

**Designer:** The shortcut for answering an interview question by its id. One answer can also move linked dials, such as corner softness setting roundness.

**Engineer:** engine.py pick <Q-id> <option-value> --why "reason". Same as set on answers.<Q-id>; mapped answers also set dials or raw inputs (Q-shape-01 subtle sets dials.roundness to 40).

**Example:** Pick subtle corners for a busy work tool.

</details>

### preview (engine command)

Makes one web page that shows every color, size and shape in your design, with a few sample parts.  
Designers: specimen page, light and dark · Code: `engine.py preview [--open]`

<details><summary>Designer and engineer</summary>

**Designer:** Builds a single specimen page of every value and a few components, light and dark side by side, so you can judge the system by eye.

**Engineer:** engine.py preview [--open] writes opendesigner/preview.html, a self-contained specimen of every token and a few components in light and dark; --open launches it in the browser.

**Example:** Open the preview to see buttons and cards in both modes.

</details>

### resolve (engine command)

Shows the exact numbers your choices lead to, like a recipe card for the whole look.  
Designers: effective dial values · Code: `engine.py resolve`

<details><summary>Designer and engineer</summary>

**Designer:** Shows the real dial positions and every value they lead to, such as type ratio or control radius, so the options you are shown use real numbers.

**Engineer:** engine.py resolve prints JSON: effective dials (explicit, then preset, coupling and macros, clamped 0-100), dialSources, macroConflicts, zoom and every derived param. Read-only; fills template payloads.

**Example:** Roundness 45 resolves to a real corner size in pixels.

</details>

### set (engine command)

Saves one choice and the reason you gave, so it is never lost or forgotten.  
Designers: record a decision and why · Code: `engine.py set <path> <json-value> --why`

<details><summary>Designer and engineer</summary>

**Designer:** Records a single decision with its rationale. Later sessions see what was chosen and why, instead of guessing from the finished look.

**Engineer:** engine.py set <path> <json-value> --why "reason" [--set-by delegated] [--lock]. Writes state.json and appends a D-nnnn entry to decisions.md; locked paths need unlock or --force.

**Example:** Set the brand color to teal because it matches the logo.

</details>

### validate (engine command)

Checks your design for problems, like text too faint to read or buttons too small to tap.  
Designers: reviewer checks: contrast, targets, naming · Code: `engine.py validate [--json]`

<details><summary>Designer and engineer</summary>

**Designer:** Runs the checks a careful reviewer would: text contrast, target sizes, naming and unused values. Fix every error before showing results; warnings are worth a look.

**Engineer:** engine.py validate [--json] checks contrast pairs per theme, that every resolver permutation resolves, target floors, DTCG structure and lint. Exits 1 on errors, 0 with warnings; findings cite rules.

**Example:** Gray text on a gray card fails and must be fixed.

</details>

### Copy my choice button

A button that copies your picks as short lines of text, ready to paste back into the chat.  
Designers: copy pick, note and lock · Code: `#copy button writing OD: lines`

<details><summary>Designer and engineer</summary>

**Designer:** Closes the loop between looking and deciding: your pick, an optional note and a lock box become text the model applies exactly, with no retyping.

**Engineer:** The #copy button in every template writes OD: lines to the clipboard (navigator.clipboard, execCommand fallback); the note field adds --why and the lock checkbox adds OD:lock lines.

**Example:** Pick soft corners, press the button, paste in chat.

</details>

### Do's and Don'ts

A list in the design guide of what to do and what to avoid, for people and AI helpers.  
Designers: do's and don'ts · Code: `DESIGN.md section 8`

<details><summary>Designer and engineer</summary>

**Designer:** The guide's rules in plain sentences: what the system guarantees, the do's (one primary action per view) and don'ts (never shrink hit areas), plus any waivers.

**Engineer:** Section 8 of DESIGN.md (## Do's and Don'ts), written by design-md: rules enforced by construction, Do and Don't bullets, current validation findings and waivers with reasons.

**Example:** Don't use motion as the only signal.

</details>

### DESIGN.md front matter

A short block of settings at the top of the design guide, set out so a computer can read it.  
Designers: machine-readable guide header · Code: `YAML front matter in DESIGN.md`

<details><summary>Designer and engineer</summary>

**Designer:** The machine-readable header of the design guide: main colors, type styles, corner radii, spacing and key components, so other AI tools pick up the look quickly.

**Engineer:** YAML front matter in DESIGN.md using only Google's DESIGN.md keys (version, name, description, colors, typography, rounded, spacing, components), filled from default-mode semantic tokens. DTCG files stay canonical.

**Example:** primary: the main brand color as a hex value.

</details>

### AGENTS.md snippet

A short note, added only if you say yes, that tells new AI helpers to read your design rules first.  
Designers: rules for later AI sessions · Code: `assets/output/AGENTS-snippet.md`

<details><summary>Designer and engineer</summary>

**Designer:** Keeps later AI sessions on-system: they read the design guide and values before touching UI, stop hard-coding values, and ask before changing locked decisions.

**Engineer:** assets/output/AGENTS-snippet.md, appended to AGENTS.md or CLAUDE.md after asking: read DESIGN.md, PRODUCT.md and tokens first, never hard-code values, run engine.py review after implementation.

**Example:** A new AI session reads it before styling a page.

**Also called:** agent pointer

</details>

### build folder

The folder with ready copies of your design for web pages, phone apps and design tools.  
Designers: exports for each tool · Code: `opendesigner/build/`

<details><summary>Designer and engineer</summary>

**Designer:** Where the exports land, one per tool the team uses: web styles, Tailwind theme, Figma import files, Paper, iOS and Android. Rebuilt, never edited by hand.

**Engineer:** opendesigner/build/, written by engine.py export: css/tokens.css, tailwind/theme.css, figma/variables.json, paper/, swift/DesignTokens.swift, compose/DesignTokens.kt, dtcg/<name>.resolver.json.

**Example:** Your web app imports the file in css.

</details>

### decisions.md

A diary of every choice made, with how it was made, when and why.  
Designers: decision history with reasons · Code: `opendesigner/decisions.md`

<details><summary>Designer and engineer</summary>

**Designer:** The running history of the system: each decision with its reason, how it was set and whether it is locked. Teammates read it to learn why.

**Engineer:** opendesigner/decisions.md is append-only, ADR-style. Each set, pick, lock and init adds a D-nnnn entry: path = value, set_by, locked, date, supersedes, source_ref and reason.

**Example:** D-0002: corners set to subtle because it is a dense tool.

**Also called:** decision log

</details>

### feedback file

A list of problems and ideas you found while using this tool, kept so you can send them in later.  
Designers: running list of gaps and ideas · Code: `opendesigner/feedback.md`

<details><summary>Designer and engineer</summary>

**Designer:** A running list of gaps, bugs, confusing steps and ideas noticed during a session, kept on your machine until you choose to send them to the project.

**Engineer:** opendesigner/feedback.md, appended by engine.py feedback: one F-nnn entry per note with date, kind and a pre-filled issue link. Stays local; the person submits the issue.

**Example:** F-001: no question about chart colors in dark mode.

</details>

### preview page

A single web page that lets you see your whole design at once, in light and dark.  
Designers: specimen sheet · Code: `opendesigner/preview.html`

<details><summary>Designer and engineer</summary>

**Designer:** A specimen sheet for judging the system as a whole: colors, type, spacing, corners, depth and sample components, light and dark side by side.

**Engineer:** opendesigner/preview.html, written by engine.py preview or build: one self-contained HTML file that uses the generated CSS variables to show every token and a few components.

**Example:** Open it in any browser, with no setup.

**Also called:** specimen page

</details>

### PRODUCT.md

A short page about your product: who it is for, what it does and where it runs.  
Designers: product brief · Code: `PRODUCT.md`

<details><summary>Designer and engineer</summary>

**Designer:** The product brief kept apart from the visual system: audience, surfaces, the memorable thing, ranked principles, constraints and scope. It changes at a different pace than the look.

**Engineer:** PRODUCT.md at the project root, rendered by engine.py design-md from state.json context. Headings: Product, Audience, Surfaces, Memorable Thing, Principles, Constraints, Scope, Team and Governance.

**Example:** An invoicing app for small shop owners, on web and iPhone.

</details>

### RATIONALE.md

A one-page note that tells your team, in plain words, why the design looks the way it does.  
Designers: one-page design rationale · Code: `opendesigner/RATIONALE.md`

<details><summary>Designer and engineer</summary>

**Designer:** A one-page case for teammates who will not read the log: the five choices that shape everything, what the rules guarantee, and what is still open.

**Engineer:** opendesigner/RATIONALE.md, written by the model (not the engine) from decisions.md using assets/output/RATIONALE.md; refreshed after each extend session; ids only in footnotes.

**Example:** We chose soft corners because the app is for families.

</details>

### state.json

The one file that holds all your answers and settings; everything else is made from it.  
Designers: the decision record · Code: `opendesigner/state.json`

<details><summary>Designer and engineer</summary>

**Designer:** The single record of every answer, dial position, brand input and asset status. Change the system by changing a decision here through the engine, never by editing outputs.

**Engineer:** opendesigner/state.json (schema opendesigner-state/1): answers {Q-id: {value, set_by, locked, decision}}, dials 0-100, raw inputs, overrides, hooks, locks, zoom, hashes. Tokens and views generate from it.

**Example:** Your brand color and corner choice both live here.

</details>

### tokens folder

The folder that holds the main list of every color, size and timing in your design.  
Designers: source of truth for values · Code: `opendesigner/tokens/`

<details><summary>Designer and engineer</summary>

**Designer:** The source of truth for every design value. Figma, CSS and app code are copies made from it, so a change here reaches all of them.

**Engineer:** opendesigner/tokens/: canonical DTCG 2025.10 files, one per tier and mode (primitives.tokens.json, semantic.color.dark.tokens.json), plus opendesigner.resolver.json. Written by generate; never hand-edited.

**Example:** The dark mode colors sit in their own file here.

</details>

### hook status

Shows where art like your logo stands: you have it, someone is making it, or it is not needed.  
Designers: asset status: have, commissioning, placeholder · Code: `hooks.<H-id>.status in state.json`

<details><summary>Designer and engineer</summary>

**Designer:** Tracks assets only a person should create, such as logo, icons or photos: have, commissioning a designer, open library, a named tool, placeholder, or not needed.

**Engineer:** hooks.<H-id>.status in state.json: pending (until asked), have, commissioning, tool, open-library, placeholder or not-needed. Set with engine.py set hooks.H-logo.status '"have"'; other values are rejected.

**Example:** Logo: commissioning, since a designer is drawing it.

</details>

### interview

The step-by-step chat where the AI asks you one big question at a time and saves your answers.  
Designers: guided design interview · Code: `opendesigner skill, questions.json, pacing.json`

<details><summary>Designer and engineer</summary>

**Designer:** A guided conversation that starts with a quick sketch of the whole system, then zooms into the areas you care about, one high-impact question per turn.

**Engineer:** Run by the opendesigner skill: questions from references/stages/, metadata in questions.json, pacing in pacing.json; each answer goes through engine.py pick or set into state.json.

**Example:** First question: what are you making?

</details>

### OD line

A short line of text that stands for one choice, which you paste back into the chat.  
Designers: choice as a one-line command · Code: `OD:set Q-id=value --why`

<details><summary>Designer and engineer</summary>

**Designer:** The one format every click and reply turns into, so a choice made in a visual picker lands in the record exactly, with an optional reason and lock.

**Engineer:** A line starting OD: (set, lock, unlock, accept, ignore, remix), such as OD:set Q-shape-01="subtle" --why "dense tool", applied with engine.py set or lock.

**Example:** OD:set dials.roundness=65 means softer corners (12px).

**Also called:** copy-back line

</details>

### question id

A short name tag for each question, so you can go back and change that answer any time.  
Designers: stable question handle · Code: `Q-<area>-<nn>`

<details><summary>Designer and engineer</summary>

**Designer:** The stable handle for a question across sessions. Say "change Q-shape-01" and any later session finds the same decision, its history and what it affects.

**Engineer:** Format Q-<area>-<nn>, such as Q-shape-01, listed in questions.json. engine.py set turns a bare Q-id into answers.<Q-id>; decisions.md entries carry it.

**Example:** Q-color-01 is the question about your brand color.

</details>

### recommendation

The answer the AI suggests, with a reason, and it only counts once you say yes.  
Designers: recommended option with a reason · Code: `--set-by confirmed_default`

<details><summary>Designer and engineer</summary>

**Designer:** Every question comes with one suggested option and a short reason tied to your answers, with sources on request. Accepting it records a confirmed default, not your own choice.

**Engineer:** Listed first among 2 to 4 options on the question card, with its reason in brackets. Accepting records --set-by confirmed_default; a recommendation is never logged as chosen.

**Example:** Subtle corners, because your app is a busy work tool.

</details>

### assumed (decision status)

A guess put in so the work can go on, marked for you to check later.  
Designers: stand-in answer, needs confirming · Code: `set_by: assumed`

<details><summary>Designer and engineer</summary>

**Designer:** A stand-in answer for something only the owner knows, like audience or brand facts. It keeps work moving but must be confirmed and never shown as decided.

**Engineer:** set_by: assumed, via --set-by assumed (a leading "pending:" in --why maps here too). DESIGN.md Open Items and the final summary list every assumed path for confirmation.

**Example:** Audience set to office workers until you confirm.

</details>

### auto default (decision status)

A safe answer left in place for you, because no one got to that question.  
Designers: untouched sourced default · Code: `set_by: auto_default`

<details><summary>Designer and engineer</summary>

**Designer:** A sourced default that stands because the question was never reached, or had one right answer. It goes in the stage summary so someone can revisit it.

**Engineer:** set_by: auto_default; unreached or mechanical questions need no command. init logs D-0001 this way; auto_default decisions logged with a value appear in DESIGN.md Open Items.

**Example:** You stopped early, so the icon size kept its default.

</details>

### chosen (decision status)

Means you picked this answer yourself.  
Designers: the owner's call · Code: `set_by: chosen`

<details><summary>Designer and engineer</summary>

**Designer:** The strongest status: the owner made this call. Treat it as intent, and raise any concern as a question rather than changing it.

**Engineer:** set_by: chosen, the default for engine.py set and pick when --set-by is omitted. Stored on the answer or dial record and in its decisions.md entry.

**Example:** You typed teal, so teal is chosen.

</details>

### confirmed default (decision status)

We gave you a suggested answer and you said yes to it.  
Designers: accepted recommendation · Code: `set_by: confirmed_default`

<details><summary>Designer and engineer</summary>

**Designer:** The owner saw the recommended default and accepted it. It counts as decided, but tells reviewers the idea came from the recommendation.

**Engineer:** set_by: confirmed_default, recorded with engine.py set <path> <value> --set-by confirmed_default. A leading "default:" in --why is read as this status too.

**Example:** The suggestion was 16px text, and you said fine.

</details>

### delegated (decision status)

You said "you decide", so the AI made this choice for you.  
Designers: the model's call, owner reviews · Code: `set_by: delegated`

<details><summary>Designer and engineer</summary>

**Designer:** The owner handed this call to the model. It still carries a reason, and it is listed at the next approval gate so the owner can review it.

**Engineer:** set_by: delegated, via engine.py set <path> <value> --set-by delegated --why "<model's reason>". Listed at the next gate and in DESIGN.md Open Items.

**Example:** You said pick any motion, so the AI chose calm motion.

</details>

### locked decision

A choice kept safe, so no one can change it without asking and unlocking it first.  
Designers: locked, must not drift · Code: `locked: true or state.json locks`

<details><summary>Designer and engineer</summary>

**Designer:** Use it for what must not drift: brand hexes, accessibility floors, anything the owner fixes. Later sessions have to ask before touching it.

**Engineer:** A path with locked: true on its answer or dial record, or listed in state.json locks. engine.py set refuses it until it is unlocked, or --force with consent.

**Example:** The logo color is locked, so a new page cannot change it.

</details>

### from reference (decision status)

Taken from a site or file you shared as an example you like.  
Designers: taken from a shared reference · Code: `set_by: reference --source-ref <ref-id>`

<details><summary>Designer and engineer</summary>

**Designer:** The value came from a reference you shared, measured for structure and quality only. Another brand's logo, exact hue or proprietary typeface is not copied.

**Engineer:** set_by: reference, with --source-ref <ref-id>; written by engine.py intake --accept or set --set-by reference. The ref id points into state.json references.

**Example:** Tight spacing taken from a site you admire.

</details>

### superseded decision

An old choice that a newer one replaced, with both kept in the diary so you can see the change.  
Designers: replaced decision, history kept · Code: `supersedes: D-nnnn`

<details><summary>Designer and engineer</summary>

**Designer:** Nothing in the history is erased. When a decision changes, the old entry stays and the new one points back to it, so you can trace how the system grew.

**Engineer:** decisions.md is append-only: a later entry for the same path supersedes the earlier one and records supersedes: D-nnnn. The newest entry per path is the effective value.

**Example:** D-0009 replaces D-0002 when corners go from subtle to soft.

</details>

### visual template

A small web page that shows each option as a real sample, so you can see it before you pick.  
Designers: live option sample · Code: `assets/templates/*.html with od-data payload`

<details><summary>Designer and engineer</summary>

**Designer:** Show, then ask: a live sample of each option on real components (palette, type scale, spacing ruler, radius, elevation, motion, component sheet, option gallery) instead of a description.

**Engineer:** One of eight self-contained HTML files in assets/templates/, fed a JSON payload in its od-data script and filled from engine.py resolve; show.py opens a local copy.

**Example:** The radius page shows buttons with four corner sizes.

</details>

### time weight

How much care a question gets: big choices get more time, and small ones get a quick yes.  
Designers: high, medium or low weight · Code: `weight field in questions.json`

<details><summary>Designer and engineer</summary>

**Designer:** Tells the model where to slow down. High-weight questions shape many others, so they get real options and a line on what else changes; low-weight ones get a quick default.

**Engineer:** The weight field (high, medium, low) in questions.json: high means fan-out 5+ or a Quick question, medium fan-out 2-4 or owner inputs, low otherwise, per pacing.json.

**Example:** Brand personality is high weight; icon stroke is low.

**Also called:** question weight

</details>

### validation report

The list of problems the checker found: ones you must fix and ones worth a look, each with its rule.  
Designers: errors block, warnings need judgment · Code: `engine.py validate --json items`

<details><summary>Designer and engineer</summary>

**Designer:** Tells you what blocks shipping (errors, like text contrast under 4.5:1 or targets under 24px) and what needs judgment (warnings), each citing its rule and source.

**Engineer:** Printed by validate or build, or JSON with --json: items with severity (error, warn, info), category, rule, where, measured, threshold, evidence and fix; plus lowest ratios and a summary.

**Example:** Error: body text on gray is 3.9 to 1, below 4.5.

</details>

### broad level

The second step of detail, with one quick screen for each main part of your design.  
Designers: one screen per foundation · Code: `zoom.<area> = broad`

<details><summary>Designer and engineer</summary>

**Designer:** Zoom level 1: one short screen per foundation (style, density, color use, text, corners, depth, motion, where files live). About 8 questions and 8 minutes.

**Engineer:** Zoom level 1: the eight questions in pacing.json zoom1. Stored as state.json zoom.<area> = "broad", or inferred from 1-2 decisions in the area.

**Example:** One screen picks corners, the next picks depth.

**Also called:** zoom level 1

</details>

### defined level

The third step of detail: you pick one part, like color, and set it with real numbers.  
Designers: one area with real values · Code: `zoom.<area> = defined`

<details><summary>Designer and engineer</summary>

**Designer:** Zoom level 2: one area at a time, such as color ramps, roles and contrast, with real values. Take only the areas that matter for your product.

**Engineer:** Zoom level 2: an area's level-2 questions in stage order, then engine.py generate. Stored as zoom.<area> = "defined", or inferred from 3-5 decisions in that area.

**Example:** Zoom into color to set exact shades and contrast.

**Also called:** zoom level 2

</details>

### detailed level

The deepest step, where every small part and button is worked out in full.  
Designers: fine print, components, patterns · Code: `zoom.<area> = detailed`

<details><summary>Designer and engineer</summary>

**Designer:** Zoom level 3: the fine print of each area plus blocks, components and patterns, built from the system's values rather than from scratch.

**Engineer:** Zoom level 3: questions tagged zoom 3, from stages/NN-*.detailed.md. Stored as zoom.<area> = "detailed", or inferred from 6 or more decisions or any override in that area.

**Example:** Every button state, such as hover and disabled, is set.

**Also called:** zoom level 3

</details>

## The eight dials

### brandPresence dial

A slider for how much the app looks like your brand, or like the phone it runs on.  
Designers: native to brand-led · Code: `dials.brandPresence`

<details><summary>Designer and engineer</summary>

**Designer:** Native (0): system font and components, brand only in accents. Brand-led (100): custom face, brand color on large surfaces, custom components. Navigation, back and sheets always stay native.

**Engineer:** Posture dial, default 50. Sets guidance params type.faceSuggestion, brand color placement, nativeShare (1.0 at 0, 0.8 at 50, 0 at 100) and content.voiceGuidance; behavior.navigationNative stays true.

**Example:** Fluent's 80/20 guidance: reuse native components most of the time.

**Also called:** Brand presence, native to brand-led

</details>

### colorfulness dial

A slider for how much color the app uses, from all gray to bright and bold.  
Designers: near-gray to vibrant palette · Code: `dials.colorfulness`

<details><summary>Designer and engineer</summary>

**Designer:** Low keeps the palette near gray with one accent; high raises accent chroma, adds secondary and tertiary accents from 60 and tints surfaces. Spend strong color on small, meaningful elements.

**Engineer:** Character dial 0-100, default 50. Accent chroma for color.accent.* (HCT 0, 10, 34, 48, max), scheme variant (monochrome to vibrant) and accent count (1, or 3 from 60).

**Example:** Material's scheme variants run from Monochrome to Vibrant along this dial.

**Also called:** Colorfulness, monochrome to vivid

</details>

### density dial

A slider for how much fits on one screen, from roomy and calm to tight and packed.  
Designers: spacious to compact · Code: `dials.density`

<details><summary>Designer and engineer</summary>

**Designer:** Spacious (0) reads calm: 16px+ body, 48px controls. Compact (100) reads serious and efficient: 14px body (13 at 90+), 32px controls. Hit areas never shrink.

**Engineer:** Posture dial 0-100. Drives type.baseSize.web (19-13), size.control.md (48/40/32), size.icon.default (24/20/16) and density context; size.target.min never changes.

**Example:** GOV.UK's 19px body sits near 0; Polaris's 13px near 90.

**Also called:** Density, spacious to compact

</details>

### depth dial

A slider for how much parts seem to lift off the page, from flat to deep.  
Designers: depth model, flat to glass · Code: `dials.depth`

<details><summary>Designer and engineer</summary>

**Designer:** Each band is a different model: borders only, ring plus faint shadow, tonal layers, shadow ladder, then glass materials with a solid fallback. Dark mode lifts raised surfaces by lightness.

**Engineer:** Character dial 0-100, default 40. The elevation model breaks at 15, 35, 55 and 80; light shadow alpha (color.shadow.key) runs 0.08-0.24; dark mode lifts raised surfaces.

**Example:** GOV.UK uses borders only; Apple's Liquid Glass sits at the deep end.

**Also called:** Depth, flat to deep

</details>

### energy dial

A slider for how lively the app feels, from calm to bouncy and bright.  
Designers: calm to energetic motion · Code: `dials.energy`

<details><summary>Designer and engineer</summary>

**Designer:** Calm (0) uses no-overshoot springs, shorter durations (0.8x), lighter headings and recessive navigation; energetic (100) adds bounce, 1.2x longer medium moves, more saturation and heavier headings.

**Engineer:** Character dial 0-100, default 50. Sets spatial spring damping ratio (1.0-0.6) and stiffness (700-380) in motion.spring.spatial.*, motion.easing.standard and a duration multiplier (0.8-1.2).

**Example:** Material 3's standard spring damps at 0.9; its expressive one at 0.8.

**Also called:** Energy, calm to energetic

</details>

### expression dial

A slider for how much the app shows off, from quiet and plain to bold and loud.  
Designers: productive to expressive · Code: `dials.expression`

<details><summary>Designer and engineer</summary>

**Designer:** Productive (0) keeps attention on the task; expressive (100) adds emphasis: a bigger type scale, more weights, hero moments, brand-colored chrome, visible containers and motion throughout.

**Engineer:** Posture dial 0-100, default 50. Drives type.ratio 1.2/1.25/1.333, type.weightCount 2-4, emphasis.heroMoments, layout.containment, brand color role and expressive motion scope (resolve params).

**Example:** Above 66, Material-style emphasized type is requested; it is not generated yet.

**Also called:** Expression, productive to expressive

</details>

### roundness dial

A slider for how round the corners are, from sharp boxes to soft pill shapes.  
Designers: corner softness, sharp to pill · Code: `dials.roundness`

<details><summary>Designer and engineer</summary>

**Designer:** Sets the default control radius and everything derived from it: container and overlay radii, nested radii, focus-ring radius, icon corners and caps. Benchmark median is 6px.

**Engineer:** Character dial 0-100, default 50. radius.control bands: 0, 2, 4, 6, 8, 12, 16px, full (pill) at 93+. Sets icon corner style and cap shape (resolve params).

**Example:** Carbon sits at 0px corners; Material 3 uses full pill buttons.

**Also called:** Roundness, sharp to soft

</details>

### warmth dial

A slider for how cool and formal or warm and friendly the grays and the wording feel.  
Designers: cool slate to warm taupe neutrals · Code: `dials.warmth`

<details><summary>Designer and engineer</summary>

**Designer:** Cool tints neutrals blue (slate) with title case and firmer borders; warm tints them toward stone or taupe, softens borders, uses sentence case and contractions. Brand hue never moves.

**Engineer:** Character dial 0-100. OKLCH neutral tint (chroma, hue) of color.neutral.*: slate (0.046, 257) at 0, gray at 50, taupe (0.021, 43) at 100; plus border and casing rules.

**Example:** Cool end: GOV.UK writes "cannot". Warm end: "can't" and "we".

**Also called:** Warmth, cool/formal to warm/friendly

</details>

## Context and inputs

### Context and inputs

The facts you gather first: who it is for, where it runs, how the brand feels, and what limits apply.  
Designers: the brief: purpose, audience, platforms · Code: `state.json: context.*, raw.*, answers`

<details><summary>Designer and engineer</summary>

**Designer:** The brief behind every visual choice: purpose, audience, platforms, devices, brand personality and hard limits. Settle these first, because they constrain more later decisions than any other input.

**Engineer:** Step-0 and step-1 inputs in the decision graph, kept in state.json (context.*, raw.*, answers), not tokens. The brand personality card alone constrains 15 later decisions.

**Example:** A calm banking app for the web, iPhone and Android.

**Also called:** project context, inputs

</details>

### Brand inputs

What the brand brings: how it feels, how it ties to its ads, and how bold the app may be.  
Designers: brand personality, layering and expression · Code: `macros, answers.Q-brand-04, raw.marketingSurfaces`

<details><summary>Designer and engineer</summary>

**Designer:** What the brand brings: its personality, how the expressive identity (logo, campaign color, display type) relates to the productive product UI, and how much expression the product allows.

**Engineer:** Not tokens: answers.Q-brand-01 sliders become macros that offset dials, answers.Q-brand-04 records expressiveness, and raw.marketingSurfaces widens display type. An expressive mode axis is planned.

</details>

### Expressiveness level and hero-moment budget

How bold the brand may get in the app, and how many showy moments it is allowed.  
Designers: hero moments, expressive budget · Code: `font.display.emphasized (proposed), motion.spring.expressive.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How much brand expression the product allows. Default, Material's rule: productive everywhere plus one or two hero moments with expressive type, shape or motion, kept for key interactions.

**Engineer:** Planned, not generated yet: expressive variants as a mode or parallel set, such as font.display.emphasized (proposed), shape.corner.expressive.* (proposed), motion.spring.expressive.* (proposed), from DC-L06-03.

**Example:** A bold, springy success screen after payment; calm screens everywhere else.

**Also called:** hero moments

</details>

### Brand-to-product layering

Whether the pages that sell the app and the app itself share one set of design rules.  
Designers: expressive marketing, productive product · Code: `layer mode axis (planned): productive | expressive`

<details><summary>Designer and engineer</summary>

**Designer:** Whether marketing (expressive) and product (productive) surfaces share one system or run separately. Default: one system, productive by default, expressive opt-in; split only when separate teams own separate surfaces.

**Engineer:** Planned, not generated yet: a layer mode axis (productive | expressive), not duplicate tokens. Today Energy picks Carbon productive (0-33) or expressive (67+) curves for motion.easing.enter and .exit.

**Also called:** expressive versus productive

</details>

### Brand personality profile

A few sliders for how the brand feels, like fun or serious, that guide most later choices.  
Designers: brand personality sliders · Code: `answers.Q-brand-01, macros`

<details><summary>Designer and engineer</summary>

**Designer:** Brand traits as slider positions, such as playful to serious; OpenDesigner uses seven. The most influential input: each pair nudges concrete foundation dials. The style screen then shows directions.

**Engineer:** Not a design token. answers.Q-brand-01 stores seven slider positions; six become macros in state.json, such as {id: playful, strength: 0.4}, that offset the dials; one sets Energy.

**Also called:** brand sliders

</details>

### Hard constraints

Limits you do not get to pick, such as the law, your design app plan, and which languages you need.  
Designers: hard limits: tool plan, legal, locales · Code: `context.constraints, exports.figmaPlan`

<details><summary>Designer and engineer</summary>

**Designer:** Limits that are not taste: the design tool plan, the legal accessibility target, supported locales and scripts. Ask for the Figma plan first; it caps modes per collection.

**Engineer:** Not tokens: context.constraints lists limits and exports.figmaPlan the Figma plan. Figma caps modes per collection (Professional 10, Organization 20); validate warns and the Figma export splits bigger collections.

</details>

### Existing UI inventory (audit)

A look through your screens today to list every button, color and size you use.  
Designers: UI inventory or interface audit · Code: `css_scan.py, engine.py review`

<details><summary>Designer and engineer</summary>

**Designer:** Screenshot every unique pattern and audit colors, type and spacing in current products. Its main value is shared vocabulary and buy-in, so do it by hand even with automated data.

**Engineer:** Not stored; audit.findings[] is proposed. css_scan.py counts declared colors, sizes and radii; engine.py review lists hard-coded values. Inventory per platform: sheet, modal and dialog differ.

**Example:** Finding many slightly different grays across your products.

**Also called:** interface inventory, UI audit

</details>

### Target platforms

The places your app must run, like the web, iPhones or Android phones.  
Designers: target platforms · Code: `raw.platforms; size.target.min`

<details><summary>Designer and engineer</summary>

**Designer:** The operating systems served. Platform choice drives units, native type, target sizes, materials and navigation. OpenDesigner defaults to web only; research suggests adding iOS and Android phones from day one.

**Engineer:** Stored as raw.platforms; no DTCG type. A platform resolver modifier is planned, not generated; today each platform gets its own export, and pointer media queries set size.target.min.

</details>

### Device classes in scope

Which kinds of screens get full care, like phones and laptops, and which get only the basics.  
Designers: device classes: phone, tablet, desktop · Code: `device-class modifier (planned); answers.Q-plat-02`

<details><summary>Designer and engineer</summary>

**Designer:** Pick which device classes get full design (phone, tablet and foldable, desktop) and which get foundations only. A class is first-class when a core task happens there.

**Engineer:** Planned, not generated: a device-class resolver modifier (handheld, wrist, desk, lean-back, vehicle, spatial), separate from platform since Android spans phones, Wear, TV and Auto. Recorded as answers.Q-plat-02.

**Also called:** form factors, device classes

</details>

### OS version floor

The oldest phone or computer software your app still has to work on.  
Designers: oldest OS and design-language generation · Code: `answers.Q-plat-09; runtime fallbacks`

<details><summary>Designer and engineer</summary>

**Designer:** The oldest OS versions supported and the design-language generation targeted. Default: support current and previous major versions, design for the current language, let older ones fall back to native.

**Engineer:** Recorded as answers.Q-plat-09; OpenDesigner emits no version-gated values. Prefer runtime fallbacks, for example dynamic color falling back to the brand scheme below Android 12.

</details>

### Platform posture (native-first, brand-first or hybrid)

How much your app should look like each phone's own style, or look the same on all of them.  
Designers: native-first, brand-first or hybrid · Code: `answers.Q-plat-05, dials.brandPresence`

<details><summary>Designer and engineer</summary>

**Designer:** Native-first, brand-first or coherent hybrid. Default hybrid: share what users see as the brand (accent, headline type, icons, voice) and use each platform's own navigation, sheets, pickers and fields.

**Engineer:** Not a token: answers.Q-plat-05 and the Brand presence dial; below 50, native platforms keep their body size. Exports emit literal colors; mapping to label or onSurface is planned.

**Example:** Brand-blue buttons, but the phone's own back gesture and date picker.

**Also called:** platform deference

</details>

### What is shared across platforms

Which parts stay the same on every device, like brand colors and names, and which parts change.  
Designers: share the what, adapt the how · Code: `answers.Q-plat-07; one token set, same names`

<details><summary>Designer and engineer</summary>

**Designer:** Choose whether platforms share tokens, component specs or only principles. Default: share the what (brand hue, role names, spacing numbers, voice); adapt the how (materials, target minimums, navigation containers).

**Engineer:** Recorded as answers.Q-plat-07. Every export shares one token set with the same names; only target sizes vary by input. Per-platform overrides and shared component specs are planned.

</details>

### Implementation stack

The coding tools your team builds the app with, which decide what form the design files take.  
Designers: tech stack or toolkit · Code: `answers.Q-plat-08; SwiftUI and Compose exports`

<details><summary>Designer and engineer</summary>

**Designer:** The toolkits products are built with. Native toolkits get new OS looks first; Flutter or Compose Multiplatform suit brand-first products that accept a lag behind OS visual changes.

**Engineer:** Recorded as answers.Q-plat-08; it does not change exports yet. build writes SwiftUI, Compose, CSS and Tailwind files; React Native objects and flutter/class.dart are not generated.

</details>

### Scope: products, audience and stack

The list of which apps and people your first version will serve, and which ones it will leave out.  
Designers: scope: products, audiences, technologies · Code: `raw.platforms, context.scope`

<details><summary>Designer and engineer</summary>

**Designer:** Name the products, audiences and technologies version 1 serves, and what it will not serve. Scope to the pilot; add platforms only when a real product needs them.

**Engineer:** Stored in state.json as raw.platforms, for example ["web", "ios"], and context.scope {in, out}. Today build writes every export (CSS, Tailwind, Figma, Paper, Swift, Compose, DTCG) regardless.

</details>

### Starting point and system posture

The choice to use a ready-made kit, change one to fit, or build your own, and how strict to be.  
Designers: adopt, adapt or create · Code: `answers.Q-scope-05, answers.Q-gov-01, components.base`

<details><summary>Designer and engineer</summary>

**Designer:** Decide whether to adopt an existing system, adapt a themeable base, or create your own, and how strict, modular and centralized it will be.

**Engineer:** Not tokens: answers.Q-scope-05 (adopt, adapt or create) and answers.Q-gov-01 (strict or loose) in state.json; components.base names a base library. Nothing acts on them yet.

**Example:** A small team adapts a headless base and puts its effort into tokens and docs.

**Also called:** adopt, adapt or create, system posture

</details>

## Principles

### Principles

The rules that say what good means, before anyone picks a color or a size.  
Designers: principles: what good means · Code: `prin.design, prin.ux, prin.visual`

<details><summary>Designer and engineer</summary>

**Designer:** Defines what good means before any value is picked: team design principles, UX behavior rules from laws and heuristics, and visual principles. It decides whether the product works.

**Engineer:** Parent of prin.design, prin.ux and prin.visual. Not tokens: principles in state.json holds ranked statements; UX and visual rules live in the formulas or engine.py validate.

</details>

### Design principles

A short, ranked list of beliefs a team uses to settle ties when two good ideas clash.  
Designers: ranked design principles · Code: `principles: ordered strings in state.json`

<details><summary>Designer and engineer</summary>

**Designer:** 3-5 ranked statements that break ties when good options conflict, each naming the value it outranks. Avoid words every product claims, like simple; test each: would this screen pass?

**Engineer:** Not tokens: principles in state.json is an ordered list of statements; order is rank, and DESIGN.md and PRODUCT.md print them as tie-breakers.

**Example:** Clarity over density: when unsure, show fewer items per screen.

</details>

### UX behavior rules

What we know about how people use apps, made into rules the tool can check.  
Designers: UX laws as checkable rules · Code: `engine.py validate; rule model (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Laws and heuristics turned into checkable rules: Fitts's law, for example, becomes no target below 24x24 CSS px, applied at the token, component or flow level.

**Engineer:** No DTCG type. Today the rules sit in engine.py: formulas set target floors and contrast; validate checks them. A rule model scoped to token, component or flow is planned.

**Example:** Fitts's law becomes: no tap target smaller than 24 by 24 pixels.

**Also called:** behavior rules

</details>

### Deceptive-pattern policy

The sneaky tricks the app must never use to push people. A computer can spot some of them.  
Designers: banned deceptive or dark patterns · Code: `answers.Q-pattern-05; deceptive-pattern lint (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Which manipulative patterns are banned, and which can be checked automatically: pre-checked consent boxes, unequal accept and reject emphasis, nagging after dismissal, fake countdowns, hard-to-cancel flows.

**Engineer:** No token. Recorded as answers.Q-pattern-05; guardrails.md forbids pre-checked consent. Planned lint would flag pre-checked boxes or cancel flows longer than signup; the rest needs human review.

**Also called:** dark patterns policy

</details>

### Convention versus novelty

How much the app works the way people already expect, versus trying new ways of doing things.  
Designers: conventional behavior, custom skin · Code: `answers.Q-plat-10; heuristic H4`

<details><summary>Designer and engineer</summary>

**Designer:** How far the product follows platform and industry conventions. Default: conventional behavior with a custom skin; be novel only where it differentiates, test it, and never override standard shortcuts.

**Engineer:** No token. Recorded as answers.Q-plat-10; DESIGN.md keeps navigation, back, sheets and pickers native on every platform. Matches heuristic H4, consistency and standards.

**Also called:** Jakob's law

</details>

### Heuristic consensus set

Eight rules of thumb that the top experts agree on, like showing people what is going on.  
Designers: usability heuristics consensus · Code: `guardrails.md rules; checks planned`

<details><summary>Designer and engineer</summary>

**Designer:** Eight principles where Nielsen, Norman, Shneiderman, Tognazzini and Laws of UX agree: status and feedback, consistency, error prevention, user control, recognition over recall, plain language, minimalism, expert efficiency.

**Engineer:** Most are partly machine-checkable, such as a dismiss path on every dialog. Today guardrails.md states them as rules for the agent; automated checks are planned.

**Also called:** usability heuristics

</details>

### Inclusive design stance

Making the app work for all kinds of people, like those who are older, see poorly or use one hand.  
Designers: inclusive design, accessibility floor · Code: `density and motion contexts, raw.contrastTarget`

<details><summary>Designer and engineer</summary>

**Designer:** The accessibility floor, WCAG 2.2 AA by default, plus constraints you design for, such as older users, low vision or one-handed use, which call for larger targets or captions.

**Engineer:** Resolver contexts cover density and reduced motion, not contrast; raw.contrastTarget AAA gives 7:1 text everywhere. CSS follows prefers-reduced-motion and uses rem type for text zoom.

</details>

### Laws of UX catalog

A list of 30 well-known rules about how people use screens, each graded by how strong the proof is.  
Designers: Laws of UX, graded for evidence · Code: `evidence grade R, R-, C, H, P`

<details><summary>Designer and engineer</summary>

**Designer:** The 30 laws on lawsofux.com, each graded for evidence. Zeigarnik and choice overload are weak, and Miller's 7 plus or minus 2 does not limit menu length.

**Engineer:** Each law carries an evidence grade: R (research-backed), R- (extrapolated to UI), C (contested), H (heuristic) or P (pop analogy). Showing the grade beside each rule is planned.

</details>

### Behavior-rule model and automation boundary

How each rule is written down, and if the tool sets it, flags it, or leaves it to a person.  
Designers: rule strictness: error, warning, judgment · Code: `validate --json finding; rule record (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Sets how hard each rule bites: a built-in default, a blocking error, a warning, or human judgment. Some rules, like a seven-item menu cap, must never be automated.

**Engineer:** Planned record: id, principle, evidence grade, scope, check kind, severity, override policy, exceptions. Today validate --json reports each finding as {rule, severity, where, measured, threshold, evidence, fix}.

**Example:** An unlabeled form field would be an error, waived only with a written reason.

</details>

### Response-time ladder

How fast the screen must answer you, from a blink that feels instant to a wait that loses you.  
Designers: response times and feedback bands · Code: `feedback.acknowledge.max (proposed) = 50ms`

<details><summary>Designer and engineer</summary>

**Designer:** How fast the interface must respond, each band with its feedback: acknowledge within 50 ms, no loader under about 1 s, skeletons to 10 s, then progress.

**Engineer:** 16 ms frame, 50 ms acknowledge, 100 ms instant, 200 ms INP, 400 ms Doherty, 1 s, 10 s. Tokens like feedback.acknowledge.max (proposed) = 50ms are not generated.

**Also called:** response-time thresholds

</details>

### Visual design principles

A set of 72 rules about what makes a screen look clear and well put together.  
Designers: hierarchy, Gestalt, type pairing, polish · Code: `principles P01 to P72`

<details><summary>Designer and engineer</summary>

**Designer:** 72 visual principles, from hierarchy and Gestalt to type pairing and polish, each graded for evidence. The stance: automate strong one-answer principles, make personality ones controls, warn on the rest.

**Engineer:** Catalog P01 to P72, each graded and given a stance: automate, warn or expose as a dial. The engine implements some, such as nested radii and text tiers.

</details>

### Aesthetics and complexity readouts

What makes a screen look good: we judge it in a blink, and a middle amount of detail works best.  
Designers: aesthetic appeal, moderate complexity · Code: `complexity and colorfulness readout (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Research on appeal: judgments form in 17-50 ms, and appeal peaks at moderate complexity and colorfulness. Beauty multiplies usability rather than replacing it, so keep a restrained default.

**Engineer:** Planned, not built: an optional complexity and colorfulness readout from screenshots (the metrics option of answers.Q-pref-01). It is never a usability signal or a pass or fail check.

</details>

### Composition, balance and alignment

How things are laid out and lined up on a screen, like on a grid of columns.  
Designers: column grid, start-aligned layout · Code: `grid.columns.* (proposed), align: start | center`

<details><summary>Designer and engineer</summary>

**Designer:** The layout model and default alignment. Column grid for app surfaces, hierarchical or bento for marketing; start-aligned everywhere, centered only for single-focus moments with short text.

**Engineer:** Not generated: grid.columns.* (proposed), grid.gutter.* (proposed) and grid.margin.* (proposed); sections use space.section.*. Alignment is a component prop using logical start and end, so RTL mirrors.

</details>

### Grouping strategy

How you show that things go together: by space, by boxes around them, or by lines.  
Designers: group by space, containers or lines · Code: `space.stack.*, color.border.subtle`

<details><summary>Designer and engineer</summary>

**Designer:** Group related items by space, containers or lines; usually a shared boundary beats proximity, which beats similarity. Default: space first, containers when content mixes, lines for long lists.

**Engineer:** space.inset.* and space.stack.* (dimension), color.surface.raised for containers, color.border.subtle with border.width.default for dividers; inner spacing at most half the outer.

</details>

### Hierarchy strength and emphasis budget

How much bigger and bolder the key things look, and how many things may shout at once.  
Designers: emphasis budget, one primary action · Code: `type.ratio, type.weightCount, emphasis.maxPrimaryPerView`

<details><summary>Designer and engineer</summary>

**Designer:** How dramatic contrast between levels is, and how many elements may claim top emphasis. At Expression 50: 1.25 size ratio, three weights, three text colors, one primary action per view.

**Engineer:** Expression sets type.ratio (1.25 at 50) and type.weightCount, feeding font.size.* and font.weight.*; validate warns above three text tiers. A one-primary-per-view lint is planned (spec 6.4).

**Example:** One filled Save button per screen; everything else is quieter.

**Also called:** emphasis budget, visual hierarchy

</details>

### Optical correction and polish

Tiny fixes that fool the eye into seeing things as even, so the screen feels done.  
Designers: optical correction, nested radii · Code: `radius.nested = max(outer - padding, smallest step)`

<details><summary>Designer and engineer</summary>

**Designer:** Optical fixes that make a UI feel finished: optical centering, overshoot, icon optical size, nested radii, one light source. OpenDesigner computes nested radii and icon strokes; optical centering stays manual.

**Engineer:** radius.nested = max(radius.container - space.inset.lg, smallest step), checked by engine.py validate. Icon keylines are guidance; icon.keyline.* (proposed) is not generated.

**Example:** A play icon nudged right so it looks centered in its circle.

**Also called:** optical correction

</details>

### Interactive signifier strength

How clearly buttons and links show that you can tap or click them.  
Designers: signifiers: clickable looks clickable · Code: `color.text.link, button.primary.background (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How clearly clickable things look clickable, via fills, underlines, borders or depth. Default: balanced, with strong signifiers forced for primary actions; minimal only in sparse, conventional layouts.

**Engineer:** Today signifiers use color.bg.action.primary, color.text.link, color.border.input. Planned component tokens: button.primary.background (proposed), link.text-decoration (proposed; no DTCG type), input.border.width (proposed).

**Also called:** affordance cues

</details>

### Visual style direction

The overall look, such as flat, glassy or bold, which sets many small details at once.  
Designers: visual style: flat, tonal, glass · Code: `preset in state.json`

<details><summary>Designer and engineer</summary>

**Designer:** An overall style (flat, tonal, glass, soft, neo-brutalist, maximal) that sets shadows, borders and radius together. Recommended: Flat 2.0; with no choice, no preset applies and dials stay at defaults.

**Engineer:** Not a DTCG type: preset (flat2, tonal, glass, neobrutal, soft, maximal) in state.json sets dial positions, which generate shadows, borders and radius.

**Also called:** style preset

</details>

## Foundations

### Foundations

The basic parts every screen is built from, like color, text, space and shape.  
Designers: foundations: the scales and roles · Code: `DTCG color, dimension and typography tokens`

<details><summary>Designer and engineer</summary>

**Designer:** The raw material of every screen: color, type, space, layout, shape, depth, motion, sound, haptics, icons, imagery, data visualization, content, accessibility and input, each a set of scales and roles.

**Engineer:** Each foundation is a family of scales and roles stored as tokens, for example DTCG color, dimension and typography types, that components consume through semantic aliases rather than raw values.

**Example:** The same blue and the same 8px gap reused on every screen.

**Also called:** design foundations, foundation

</details>

### Accessibility

Making the app work for all people, even those who can't see well, can't hear, or can't use a mouse.  
Designers: WCAG 2.2 AA target · Code: `raw.contrastTarget`

<details><summary>Designer and engineer</summary>

**Designer:** Target WCAG 2.2 AA. The system guarantees component behavior and contrast-safe color pairs; product teams own page-level criteria and content. Detailed rules live with each foundation they bound.

**Engineer:** raw.contrastTarget (AA by default, or AAA) sets text minimums; validate checks each listed color pair per theme. Of accessibility settings, only reduced motion is a resolver context today.

**Also called:** a11y, WCAG conformance

</details>

### Platform accessibility settings

The phone settings people pick, like big text or less motion, which the app has to follow.  
Designers: honor OS accessibility settings · Code: `motion modifier, prefers-reduced-motion, forced-colors`

<details><summary>Designer and engineer</summary>

**Designer:** Honor text size, bold text, increased contrast, reduced transparency, reduced motion, forced colors and screen readers. Never show a boundary or focus state by shadow or translucency alone.

**Engineer:** The resolver's motion modifier (standard, reduced) follows prefers-reduced-motion, and forced-colors maps the focus ring to Highlight. Contrast and transparency modes are not generated yet.

**Example:** With forced colors on, cards keep a border because shadows disappear.

**Also called:** OS accessibility settings, user preferences

</details>

### Color

Which colors an app uses, what job each one does, and how they switch for dark mode.  
Designers: color system: ramps and roles · Code: `color.accent.light.9, color.bg.accent.bold`

<details><summary>Designer and engineer</summary>

**Designer:** The full color system: how ramps are generated, which roles exist (surface, text, border, status), how light, dark and high-contrast modes remap them, and how contrast is guaranteed.

**Engineer:** Two tiers of DTCG color tokens: primitive ramps (color.accent.light.9) and semantic roles (color.bg.accent.bold) that alias them per theme through the resolver.

**Example:** Blue buttons, gray text and a white page that turns dark at night.

**Also called:** color system, palette

</details>

### Transparent (alpha) colors

Colors you can partly see through, so they look right on any background.  
Designers: semi-transparent fills · Code: `color.neutralAlpha.*`

<details><summary>Designer and engineer</summary>

**Designer:** Semi-transparent fills that adapt to whatever sits beneath, ideal for hover fills, borders and scrims on varied backgrounds. Use solid colors for text, where contrast must be certified.

**Engineer:** A DTCG color value with an alpha field: color.neutralAlpha.light.2 to .12 and dark twins match solid neutral steps over the page; color.overlay.scrim carries alpha too.

**Example:** A light gray hover shade that works on white and on blue.

**Also called:** alpha colors, translucent colors

</details>

### Brand and accent color

The one color that makes an app feel like its brand, often on its main button.  
Designers: brand or accent color · Code: `color.bg.brand, color.text.onBrand`

<details><summary>Designer and engineer</summary>

**Designer:** Decides how many accents exist and what the brand color does: reserved accent, signature surface or whole fields. Default is neutrals plus one accent; adapt the brand hex for contrast.

**Engineer:** The brand hex, if given, is kept exactly as a seed primitive for logos; UI roles like color.bg.brand alias an accent step, 4.5:1 with color.text.onBrand.

**Example:** The exact logo blue, moved one shade darker so white button text stays readable.

**Also called:** accent color, primary color

</details>

### Palette character (chroma and scheme variant)

How bold or how soft and calm the colors feel as a whole.  
Designers: palette saturation, muted to vivid · Code: `params in opendesigner.meta.json`

<details><summary>Designer and engineer</summary>

**Designer:** Overall palette saturation, muted to vivid, plus the scheme variant shaping it (Material's TonalSpot, Fidelity or Vibrant). Keep large surfaces calm; spend color on small, meaningful elements.

**Engineer:** No DTCG type of its own: the engine records parameters in opendesigner.meta.json, such as the scheme variant tonalSpot and the accent's HCT chroma, which feed the ramp generator.

**Example:** A calm banking app next to a loud, colorful game.

**Also called:** colorfulness, scheme variant

</details>

### Contrast and color independence

Text must stand out from what is behind it, and color must never be the only clue.  
Designers: WCAG AA contrast, never color alone · Code: `contrastPairs in opendesigner.meta.json`

<details><summary>Designer and engineer</summary>

**Designer:** WCAG 2.2 AA is the floor: 4.5:1 for text, 3:1 for large text and control boundaries. Meaning never depends on color alone; add an icon, label or underline.

**Engineer:** No DTCG contrast field: opendesigner.meta.json lists intended pairs, such as color.text.primary on color.surface.base at 4.5:1, and engine.py validate checks each per theme.

**Example:** An error field shows a red border plus an icon and message, not red alone.

**Also called:** color contrast, WCAG contrast

</details>

### Gradients and expressive color

Bold color blends for ads and pictures, kept off buttons and forms.  
Designers: brand gradients and campaign colors · Code: `$type: gradient`

<details><summary>Designer and engineer</summary>

**Designer:** Brand gradients and campaign colors that live outside core controls, on marketing and illustration surfaces. Keep them off interactive components; if a gradient carries data meaning, use a sequential palette.

**Engineer:** DTCG 2025.10 gradient type: an array of stops, each with color and position. It has no kind, angle or interpolation space, so store those in $extensions; interpolate in OKLab.

**Example:** A purple-to-orange blend on a sale banner, never on the checkout button.

**Also called:** brand gradients, campaign colors

</details>

### Color modes and appearance

Full swaps of an app's colors, like light, dark, or a sharper set that is easier to see.  
Designers: light, dark and high-contrast modes · Code: `Resolver theme modifier, [data-theme]`

<details><summary>Designer and engineer</summary>

**Designer:** The alternative color mappings a system ships: light, dark, dimmed, high contrast and colorblind-safe, and how each platform picks one. Dark mode is a separate mapping, never an inversion.

**Engineer:** The DTCG Resolver module's theme modifier: light and dark contexts point semantic tokens at different files. Web CSS uses prefers-color-scheme with a [data-theme] override.

**Example:** Your phone switches to dark at night and the app follows.

**Also called:** themes, appearance modes

</details>

### Appearance modes by platform and device

Which light or dark looks each kind of device uses, and who gets to switch between them.  
Designers: appearance by device: system or override · Code: `sketch --theme, [data-theme]`

<details><summary>Designer and engineer</summary>

**Designer:** Which appearances each device class gets and who switches: system setting, in-app override or ambient light. Phones and desktops follow the system; watches stay dark; cars switch day and night.

**Engineer:** sketch --theme (system-light-dark, light-dark-toggle, light-only, dark-only) sets which theme contexts exist; web CSS adds a [data-theme] override. Per-device availability, such as wrist dark only, is not generated yet.

**Example:** A watch app that is always dark, even at noon.

**Also called:** system appearance

</details>

### Accessibility color themes

Extra color sets for people who need text to stand out more, or who mix up colors.  
Designers: high-contrast and colorblind-safe themes · Code: `contrast and vision modifiers (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Themes for users who need more contrast or hue separation: contrast levels, high contrast, forced colors, colorblind-safe palettes. Back fills with borders or icons so they survive forced colors.

**Engineer:** Not generated yet: extra resolver modifiers beside theme, such as contrast (standard, high) and vision (protan-deutan, tritan). Material offers three contrast levels; web forced-colors mode swaps in system colors.

**Example:** Primer's colorblind theme shows success in blue instead of green.

**Also called:** high contrast mode, colorblind themes, forced colors

</details>

### Dark mode mapping

How each color is picked again for dark screens, so text stays easy to read.  
Designers: dark theme, mapped by role · Code: `prefers-color-scheme: dark`

<details><summary>Designer and engineer</summary>

**Designer:** Each role gets its own dark value, mapped by role, not flipped. The default dark base is neutral step 2, untinted at Warmth 50; accents go lighter.

**Engineer:** Semantic tokens resolve per Resolver context (light, dark); each role takes the dark step giving the same contrast relationship as in light. Web: prefers-color-scheme with a [data-theme] override.

**Example:** White text on a near-black page, with the blue lightened a step.

**Also called:** dark theme

</details>

### Neutral ramp

The set of grays, from white to near black, used for most backgrounds, lines and text.  
Designers: gray scale, tinted or pure · Code: `color.neutral.*, color.neutralAlpha.*`

<details><summary>Designer and engineer</summary>

**Designer:** The gray scale behind most surfaces, borders and text. A slight tint toward the accent hue feels branded; pure gray suits image and data tools.

**Engineer:** Primitives color.neutral.light.1 to .12 and a dark twin, tinted by the Warmth dial, plus alpha twins color.neutralAlpha.light.2 to .12. Semantic roles alias them.

**Example:** Near-white for the page, mid gray for borders, dark gray for text.

**Also called:** gray ramp, grays

</details>

### Dynamic and personalized color

Whether an app can take on colors you pick, like your wallpaper, or keeps its own.  
Designers: dynamic color or fixed brand palette · Code: `DynamicColors`

<details><summary>Designer and engineer</summary>

**Designer:** Whether the OS or user may recolor the product (Android wallpaper-based dynamic color, macOS accent, Apple icon looks) or keeps a fixed brand palette. Keep brand-critical and status colors fixed.

**Engineer:** Dynamic roles resolve at runtime, so tokens store roles plus the generator recipe (source, variant, spec version, contrast level). Android applies it via DynamicColors; brand tokens remain the fallback.

**Example:** A notes app turns green because your wallpaper is a forest.

**Also called:** dynamic color, wallpaper colors

</details>

### Ramp generation and step meaning

A row of shades of one color, from light to dark, where each step has a job.  
Designers: color ramp or tonal scale · Code: `color.accent.light.*`

<details><summary>Designer and engineer</summary>

**Designer:** What a step promises differs by system: Tailwind lightness varies by hue, Spectrum keeps equal contrast per step, Material uses HCT tone. Radix gives each step a job.

**Engineer:** Primitive color tokens per ramp and theme, such as color.accent.light.1 to .12: 12 contrast-indexed steps generated in OKLCH from a seed color.

**Example:** Pale blue for a background, deep blue for the text on it.

**Also called:** tonal ramp, color scale, tonal palette

</details>

### Semantic color roles

Color names that say the job, like page background or warning text, not the shade.  
Designers: color roles by job and emphasis · Code: `color.bg.accent.bold`

<details><summary>Designer and engineer</summary>

**Designer:** Named jobs such as background, text, border and icon, crossed with roles like accent, neutral or danger and emphasis levels (subtle, default, bold). Components use roles, never raw values.

**Engineer:** Semantic tier named property, role, emphasis, state: color.bg.accent.bold aliases {color.accent.light.9}, with .boldHover and .boldPressed. Bold fills pair with on-colors such as color.text.onAccent.

**Example:** Change the danger color once and every error message updates.

**Also called:** color roles, semantic colors

</details>

### Border, outline and focus colors

Colors for lines around things, and for the ring that shows where the keyboard is.  
Designers: border strengths and focus color · Code: `color.border.*, color.border.focus`

<details><summary>Designer and engineer</summary>

**Designer:** Subtle, default and strong border strengths plus one focus color per mode. Interactive borders and focus rings need 3:1 against adjacent colors; decorative dividers do not.

**Engineer:** color.border.subtle (dividers), .default, .strong, .input, .focus (the focus ring), .accent and one per status. In forced-colors mode browsers replace border and outline colors with system colors.

**Example:** A soft gray line between list rows, a blue ring on the active field.

**Also called:** stroke colors, divider colors

</details>

### Foreground and text colors

Colors for words and icons, from strong main text to faint hint text.  
Designers: text and icon colors by emphasis · Code: `color.text.*, color.icon.*`

<details><summary>Designer and engineer</summary>

**Designer:** Text and icon colors by emphasis: primary, secondary, placeholder, disabled and inverse, plus an on-color for each bold fill. Secondary text should still pass 4.5:1 on its lowest surface.

**Engineer:** Solid semantic tokens color.text.{primary|secondary|tertiary|disabled|inverse|onBrand} and color.icon.*, aliasing ramp steps per mode. WCAG requires 4.5:1 for normal text; disabled text is exempt.

**Example:** Black for headings, gray for hints, white text on a blue button.

**Also called:** text colors, on-colors

</details>

### Status and feedback colors

Colors that show how things went, like green for success and red for an error.  
Designers: success, warning, danger, info colors · Code: `color.bg.success.*, color.text.success`

<details><summary>Designer and engineer</summary>

**Designer:** Success, warning, danger and info, each subtle and bold, for fills, text and icons. Always pair with an icon or words; yellow fills need dark text.

**Engineer:** color.bg.success.subtle, .bold and .boldHover, color.text.success, color.border.success and color.text.onSuccess; the same for warning, danger, info. Status icons take the text token.

**Example:** A green check beside 'Saved', a red icon beside 'Payment failed'.

**Also called:** feedback colors, status colors

</details>

### Surface roles

Background colors for things that stack, like a page, a card on it, and a pop-up on top.  
Designers: background tiers: base, raised, overlay · Code: `color.surface.*`

<details><summary>Designer and engineer</summary>

**Designer:** Background tiers (base, raised, overlay, sunken) that show layering. In light mode, shadow or border plus a subtle tone separates them; in dark mode, lighter tones do.

**Engineer:** color.surface.base, .raised, .sunken, .overlay and .nav, plus .tinted at Colorfulness 50 and up, aliasing neutral or accent steps with separate light and dark values.

**Example:** A white card sitting on a light gray page.

**Also called:** background layers, surface tiers

</details>

### Color space and gamut

How colors are mixed so each step looks even, and how bold a screen's colors can get.  
Designers: perceptual color space, like OKLCH · Code: `colorSpace: oklch`

<details><summary>Designer and engineer</summary>

**Designer:** Perceptual spaces such as OKLCH or HCT make equal steps look equally heavy across hues, so hierarchy survives color swaps. Gamut decides whether vivid Display P3 accents are allowed.

**Engineer:** DTCG color values set colorSpace ('oklch', 'srgb', 'display-p3') with a hex fallback. OpenDesigner writes OKLCH ramps with hex fallbacks and P3 variants in $extensions.opendesigner.p3.

**Example:** Blue and green buttons at the same step look equally strong.

**Also called:** color model, OKLCH, Display P3

</details>

### Interaction state colors

How a button's color shifts when you point at it, press it, pick it, or can't use it.  
Designers: hover, pressed, selected, disabled colors · Code: `color.bg.accent.boldHover, opacity.state.hover`

<details><summary>Designer and engineer</summary>

**Designer:** Hover, pressed, selected and disabled colors come from stepping along the ramp; a translucent state layer covers colors unknown at design time. Selected needs a non-color cue.

**Engineer:** Ramp steps per role, such as color.bg.accent.boldHover (+1 step) and .boldPressed (+2), and state-layer numbers such as opacity.state.hover = 0.08 for colors unknown at design time.

**Example:** A blue button turns one shade darker under the mouse.

**Also called:** state colors, state layers

</details>

### Content and voice

The words in the app and the rules for writing them, so the app always sounds like itself.  
Designers: content: voice, tone, microcopy · Code: `DESIGN.md Content and Voice section`

<details><summary>Designer and engineer</summary>

**Designer:** The words layer: voice, tone by situation, mechanics, component microcopy, terminology, localization, readability and scannable structure. Voice stays the same across platforms; platform feature terms adapt.

**Engineer:** No DTCG type: content rules are text records; lint settings such as content.readingGrade.max (proposed) are not built yet. DESIGN.md has a Content and Voice section.

**Also called:** content design, UX writing

</details>

### Localization readiness

Rules so the app works in other languages, where words get longer or go right to left.  
Designers: text expansion and RTL readiness · Code: `:lang() line-height scale, CLDR formatting`

<details><summary>Designer and engineer</summary>

**Designer:** Never fix a label width to English length; budget 2-3x for labels under 10 characters. Plan right-to-left layouts, per-script line heights and local date and number formats early.

**Engineer:** CSS export scales line height per listed script via :lang(); per-script font.family modes are not generated. Use CLDR locale formatting and test the brand face against OS fallbacks.

**Example:** A short English label may need three times the room once translated.

**Also called:** i18n, internationalization, text expansion

</details>

### Grammar, mechanics and capitalization

House rules for writing, like when to use capitals, how to write dates, and when to say you.  
Designers: sentence case and grammar rules · Code: `CLDR locale formatters`

<details><summary>Designer and engineer</summary>

**Designer:** Sentence case everywhere; contractions yes, except negative ones in high-stakes flows; you for the user, we sparingly; no exclamation marks in errors; numerals for counts.

**Engineer:** No DTCG type, and the typography composite has no text-transform, so casing stays a content rule. Dates and numbers go through CLDR-based locale formatters, never hard-coded formats.

**Example:** Save changes, not Save Changes.

**Also called:** style guide, sentence case, house style

</details>

### Component microcopy

The short bits of text that come with each part, like button words and error notes.  
Designers: microcopy: verb-first labels · Code: `button.submit.label (proposed) i18n key`

<details><summary>Designer and engineer</summary>

**Designer:** Each component spec ships its wording rules with examples: verb-first button labels, useful empty states, constructive errors and confirmations that name the action.

**Engineer:** Default strings would be i18n keys such as button.submit.label (proposed), not design tokens; none are generated yet. Platform labels (Cancel, OK, Done) follow OS conventions.

**Example:** The delete dialog's button says Delete file, not OK.

**Also called:** UI copy, button labels, empty-state text

</details>

### Readability and plain language

Keeping the words short and plain so that most people can read them fast.  
Designers: plain language, grade 6-8 · Code: `content.readingGrade.max (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Aim for grade 6-8 reading level in consumer products and 10-12 in expert tools. Button labels are 2-4 words, verb first. Plain language helps everyone, experts included.

**Engineer:** Proposed lint, not built: content.readingGrade.max (proposed) and button.label.maxWords (proposed) = 4. Spec 6.4 plans a warning for button labels over 4 words; no string lint exists yet.

**Example:** Save draft, not Persist current document state.

**Also called:** reading level, plain language

</details>

### Content hierarchy for scanning

Laying out words so people can skim: clear headings, the main point first, and lists instead of long blocks.  
Designers: scannable headings and structure · Code: `h1-h6 heading elements`

<details><summary>Designer and engineer</summary>

**Designer:** A heading for every section, key points in the first two paragraphs, sparing bold, bullets for three or more items. Unformatted walls of text push readers into the F-pattern.

**Engineer:** Real heading structure (WCAG 1.3.1, 2.4.6) using type role tokens. Linting for skipped heading levels, long unheaded paragraphs and link text like click here is not built yet.

**Example:** A help page where each heading answers one question.

**Also called:** scannable content, front-loading, layer-cake

</details>

### Terminology and inclusive language

A shared word list: words to use, words to avoid, and kind ways to talk about people.  
Designers: preferred and banned terms · Code: `glossary term list`

<details><summary>Designer and engineer</summary>

**Designer:** A glossary of preferred and banned terms plus inclusive-language rules, started at 20-50 terms on day one. Consistent terms make navigation labels, headings and empty states predictable.

**Engineer:** Glossary data, not tokens: a term list. Linting copy against it for banned terms and internal jargon is not built yet. Shared strings avoid input-specific verbs like tap or click.

**Example:** Pick sign in and use it everywhere, never mixed with log in.

**Also called:** word list, content glossary, inclusive language

</details>

### Tone by situation

How the app's words change with the moment: calm for mistakes, warmer for good news.  
Designers: tone shifts by message type · Code: `tone matrix, a content rule`

<details><summary>Designer and engineer</summary>

**Designer:** Voice stays; tone shifts by message type. Errors are serious, respectful and matter-of-fact; success is as warm as the brand allows; humor is rare, since repeated jokes annoy.

**Engineer:** Not tokens: a matrix of message type against humor, formality, enthusiasm and length, kept as a content rule. Notification and lock-screen strings get tighter, context-aware limits.

**Example:** Payment failed: plain and calm. Payment sent: a little warmth.

**Also called:** tone of voice, tone matrix

</details>

### Voice

The way the app sounds in words, the same each time, like a friend you know by their voice.  
Designers: brand voice: 3-4 traits with but-nots · Code: `voice guide (H-voice), DESIGN.md Content and Voice`

<details><summary>Designer and engineer</summary>

**Designer:** The brand's lasting personality in words, set as 3-4 traits, each with a but-not and three copy examples, such as authoritative but not pedantic. Tone flexes; voice stays.

**Engineer:** Not a design token: traits, anti-traits and examples belong in a voice guide (hook H-voice). DESIGN.md's Content and Voice section records the guidance level, casing and contractions.

**Example:** Practical, but not dull, with three sample lines for each trait.

**Also called:** brand voice, voice traits

</details>

### Data visualization

Charts that match the rest of the app, with set colors, parts and rules so all can read them.  
Designers: data viz, themed to the system · Code: `color.chart.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Charts as part of the system: a small set of chart types, palettes, shared anatomy and accessibility rules, so charts look native to the product rather than pasted in.

**Engineer:** Planned via the H-dataviz hook: chart palettes as color tokens, with chrome reusing text, border and dimension tokens; no chart tokens are generated yet. DTCG has no chart-specific types.

**Also called:** charts, dataviz

</details>

### Chart accessibility

Making charts clear to people who can't tell some colors apart or who have the screen read aloud.  
Designers: insight title, labels, table view · Code: `figcaption, aria-describedby, data table`

<details><summary>Designer and engineer</summary>

**Designer:** Every chart gets a title stating the insight, direct labels or a legend with shape cues, a text summary and a view-as-table option. Color is never the only cue.

**Engineer:** Meets WCAG 1.4.1 and 1.4.11 (3:1 for essential marks). Long descriptions via figure and figcaption or aria-describedby, a data table alternative, and patterns or markers as assets.

**Example:** Title: Sales doubled in March, with a table view below.

**Also called:** accessible charts, chart alt text

</details>

### Chart anatomy and tokens

The parts of a chart, like its grid lines, labels, color key and pop-up notes, and how each looks.  
Designers: axes, gridlines, labels, legends · Code: `chart.gridline.color (proposed), color.border.subtle`

<details><summary>Designer and engineer</summary>

**Designer:** Axes, gridlines, labels, legends and tooltips reuse the UI's text and border styles to match the product. Faint gridlines keep focus on data; direct labels read cleaner than legends.

**Engineer:** Not generated yet: component aliases such as chart.gridline.color (proposed) = {color.border.subtle} and chart.tick.label.color (proposed) = {color.text.secondary}; chart-only tokens just for marks and states.

**Example:** Grid lines use the same faint grey as table borders.

**Also called:** axes, gridlines, legend, tooltip

</details>

### Data-visualization palettes

Chart colors: one per group, light to dark for how much, and two-way for above or below the middle.  
Designers: categorical, sequential, diverging palettes · Code: `color.chart.categorical (proposed), .sequential, .diverging`

<details><summary>Designer and engineer</summary>

**Designer:** One brand chart color plus grey by default; 6-8 categorical colors in fixed order for neighbor contrast; one sequential ramp per primary hue and one diverging ramp, per mode.

**Engineer:** Not generated yet: per-mode color tokens color.chart.categorical.1 (proposed) onward, color.chart.sequential (proposed) and color.chart.diverging (proposed) ramps, plus brand, neutral and status sets.

**Example:** This year in brand blue, last year in grey for context.

**Also called:** chart colors, categorical palette, sequential palette, diverging palette

</details>

### Chart scope and library

Which kinds of charts the app has, like bars and lines, and which ready-made chart kit it styles.  
Designers: 5-6 chart types plus KPI number · Code: `color.chart.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Start with 5-6 types (bar, line, area, stacked bar, donut or meter, scatter) plus a KPI big number. Fewer types stay consistent; theme a library rather than build one.

**Engineer:** Not a token: the Q-viz-01 scope answer in state.json. The themed chart library would consume color.chart.* (proposed) and existing chrome tokens, as would native chart frameworks.

**Example:** A dashboard with bars, lines and one big number, all from one library.

**Also called:** chart types, chart library

</details>

### Elevation, materials and opacity

How the app shows that some parts sit on top of others, with shadows, shades and glass.  
Designers: depth: shadows, surfaces, materials · Code: `DTCG shadow, surface and opacity tokens`

<details><summary>Designer and engineer</summary>

**Designer:** The depth family: depth model, levels, shadow recipe, surface tiers, stacking order, translucent materials, and opacity for states and scrims. Together they decide what looks flat and what floats.

**Engineer:** DTCG shadow composites (color, offsetX, offsetY, blur, spread, inset), surface color tokens and opacity number tokens; layer order is not tokenized yet. Blur and materials have no DTCG type.

**Also called:** depth, layering

</details>

### Depth model

The main way the app shows layers: with lines, shadows, shades of color, or frosted glass.  
Designers: flat, shadowed, tonal or glass · Code: `$extensions.opendesigner.model`

<details><summary>Designer and engineer</summary>

**Designer:** Pick flat with borders, shadows, tonal steps or translucent material. OpenDesigner's default (Depth 40) is tonal: surface steps for in-page containers, shadows only for floating menus and dialogs.

**Engineer:** The Depth dial picks a model (borders, ring+faint-shadow, tonal, shadow-ladder, materials), stored in the elevation group's $extensions.opendesigner.model; it decides which shadow and surface tokens are emitted.

**Example:** GOV.UK uses borders only; Material uses tonal color steps.

**Also called:** depth strategy, flat versus shadow

</details>

### Translucent materials

See-through frosted glass on bars and menus, with a solid look for people who turn it off.  
Designers: glass, blur and vibrancy · Code: `material.glass.*, backdrop-filter`

<details><summary>Designer and engineer</summary>

**Designer:** Glass, blur and vibrancy feel premium and keep context visible but cut contrast. Use them only for floating navigation and overlays, never reading surfaces; each needs an opaque fallback.

**Engineer:** No DTCG material type. The materials depth model adds material.glass.blur, a glass surface color and a solid fallback for reduced transparency. Web: backdrop-filter; iOS: glassEffect; Windows: Mica, Acrylic.

**Example:** A frosted tab bar turns solid when Reduce Transparency is on.

**Also called:** glass, blur, vibrancy, Liquid Glass, Mica, Acrylic

</details>

### Opacity, state layers and scrims

A faint tint when you press, a faded look for things you can't use, and a dim veil behind pop-ups.  
Designers: state layers and scrims · Code: `opacity.state.hover, color.overlay.scrim`

<details><summary>Designer and engineer</summary>

**Designer:** Material's state layers: 0.08 hover, 0.10 focus and press, 0.16 drag, 0.38 disabled. OpenDesigner steps the ramp first and uses these only for unknown colors. Scrims dim pages behind modals.

**Engineer:** DTCG number tokens (0-1): opacity.state.hover, opacity.disabled.content. Scrim: color.overlay.scrim, a color with alpha, 40-50% in light mode and 50-60% in dark.

**Example:** A dialog opens over the page, which dims behind a dark veil.

**Also called:** state layer, scrim, backdrop, disabled opacity

</details>

### Elevation levels

How many heights a part can sit at above the page, and which parts go at each one.  
Designers: elevation levels: sunken to overlay · Code: `elevation.raised, elevation.overlay`

<details><summary>Designer and engineer</summary>

**Designer:** Four levels (sunken, default, raised, overlay) cover most products; more levels muddy the order. Two parts at the same level should never overlap each other.

**Engineer:** Semantic shadow tokens elevation.raised, .floating and .overlay. The shadow-ladder and materials models alias a six-step primitive ladder; the tonal default writes its shadows inline.

**Example:** Code wells sunken, pages default, hover cards raised, dialogs overlay.

**Also called:** elevation scale, shadow levels

</details>

### Shadow recipe

Rules for shadows: how many, how soft, what color, and how they change on dark screens.  
Designers: two-layer soft shadow · Code: `shadow array; color.shadow.key, .ambient`

<details><summary>Designer and engineer</summary>

**Designer:** Two layers: 1px contact shadow plus a soft blur growing with height, neutral at 8-24% alpha. Dark mode doubles alpha and adds a 1px edge ring.

**Engineer:** A DTCG shadow array of layers {color, offsetX, offsetY, blur, spread, inset}. Colors reference color.shadow.key and color.shadow.ambient so dark mode swaps them; Figma stores effect styles.

**Example:** A menu gets a thin edge shadow plus a wide, soft blur.

**Also called:** box shadow, drop shadow

</details>

### Stacking order (z-index layers)

A set order for what goes on top when things pile up, so pop-ups never hide.  
Designers: layer order, z-index stack · Code: `layer.modal (proposed), z-index`

<details><summary>Designer and engineer</summary>

**Designer:** A named layer order: base, sticky, dropdown, scrim, modal, popover or tooltip, toast, skip link. It keeps tooltips above modals and toasts above everything.

**Engineer:** Not generated yet: number tokens like layer.modal (proposed), named by role, spaced by 100. Avoid hard-coded z-index; the web top layer (popover, dialog) cuts the need.

**Example:** A tooltip opened inside a dialog still shows on top.

**Also called:** z-index scale, layer order

</details>

### Surface roles for elevation

The set of background shades for each layer, where higher layers get a bit lighter on dark screens.  
Designers: surface tiers, lighter in dark mode · Code: `color.surface.sunken, .base, .raised, .overlay`

<details><summary>Designer and engineer</summary>

**Designer:** Four surface tiers (sunken, default, raised, overlay). In dark mode each higher tier is 3-5% lighter, as if lit from the front, because shadows barely show on dark backgrounds.

**Engineer:** Role-named color tokens color.surface.sunken, .base, .raised, .overlay and .nav, with light and dark values. Shadows are separate elevation.* tokens; the same tiers appear under Surface roles.

**Example:** In dark mode a menu sits on a slightly lighter grey than the page.

**Also called:** surface tiers, dark-mode elevation

</details>

### Iconography

Small signs for actions and things, like a trash can for delete, and the rules for how they look.  
Designers: icon system: style, sizes, color · Code: `size.icon.*, icon.stroke.*, color.icon.*`

<details><summary>Designer and engineer</summary>

**Designer:** The UI icon system: source, style, construction, sizes, states, color, labels, naming, larger tiers, delivery and platform symbols. Consistent icons make rows look even and actions easy to recognize.

**Engineer:** No DTCG icon type: glyphs are SVG assets, with custom ones from hook H-icons (a manifest is proposed); size.icon.*, icon.stroke.* and color.icon.* are tokens.

**Also called:** icon system, icons

</details>

### Icon color and rendering mode

The colors icons use: mostly one calm grey, with bright colors saved for warnings and errors.  
Designers: one neutral icon color · Code: `color.icon.default, fill=currentColor`

<details><summary>Designer and engineer</summary>

**Designer:** One neutral icon color matched to secondary text, status colors only on status icons, no decorative multicolor. Meaningful icons need 3:1 (WCAG); Carbon asks 4.5:1 beside body text.

**Engineer:** color.icon.default (same neutral step as color.text.secondary, not an alias), .subtle, .accent and .onAccent; status icons use color.text.danger and its siblings. Web SVG: fill=currentColor.

**Example:** Grey icons in the toolbar, and a red one only beside an error.

**Also called:** icon color, multicolor icons, hierarchical rendering

</details>

### Stroke, grid and keylines

Drawing rules for icons, like line width and a shared grid, so they all look the same size.  
Designers: stroke weight, grid and keylines · Code: `icon.stroke.sm, .md, .lg`

<details><summary>Designer and engineer</summary>

**Designer:** Stroke matches text weight: about 1.5px by 14-16px text, 2px at 24px. Material's 24px grid, 20px live area and keylines keep icons even.

**Engineer:** Mostly documented, not tokenized. The engine emits icon.stroke.sm, .md and .lg (dimension) from round_to_0.5((size/12) x (weight/400)), minimum 1. Glyphs themselves are SVG assets.

**Example:** A 24px icon with a 2px line inside a 20px live area.

**Also called:** icon grid, keyline shapes, live area

</details>

### Icon delivery

How icon files are packed and sent to each kind of app, like phone apps and websites.  
Designers: one SVG master for every platform · Code: `<name>_<size>_<style>`

<details><summary>Designer and engineer</summary>

**Designer:** One SVG master feeds every platform package, so icons match everywhere. Files are named by name, size and style; size and color come from the system, not the artwork.

**Engineer:** SVG source of truth generates framework components, Android vector drawables and iOS PDF, SVG or custom SF Symbols; web uses inline SVG with fill=currentColor. Files follow <name>_<size>_<style>.

**Example:** home_24_filled.svg becomes a React component and an Android drawable.

**Also called:** icon packages, icon export

</details>

### Icons with labels

When an icon needs words beside it, and how the icon and the words line up.  
Designers: labeled icons; icon-only with tooltip · Code: `space.icon.gap (proposed), aria-hidden`

<details><summary>Designer and engineer</summary>

**Designer:** Label everything in navigation. Icon-only suits about a dozen universal actions (search, close, more, add, delete, edit, share, settings), each with a tooltip. Center icons on the text line.

**Engineer:** space.icon.gap (proposed), 4px at 16px icons, is not generated; use space.inline.xs or .sm. Icon-only controls need an accessible name; decorative icons get aria-hidden.

**Example:** A bare magnifier for search, while Settings in the sidebar keeps its label.

**Also called:** icon and label, icon-only buttons

</details>

### Icon metaphors, naming and localization

How icons get names, what each one means, and which ones flip for writing that goes right to left.  
Designers: name icons by shape, not meaning · Code: `icon manifest (proposed): name, aliases, directionType`

<details><summary>Designer and engineer</summary>

**Designer:** Name icons by shape (shield, not security) so one glyph serves many meanings, add function aliases in the component API, note mirroring per icon, test metaphors per market.

**Engineer:** Proposed, not generated yet: an icon manifest in JSON with name, aliases, directionType (unique or mirror, as Fluent does) and categories per icon. Components expose the function-alias layer.

**Example:** The back arrow points right in Arabic and Hebrew layouts.

**Also called:** icon names, right-to-left icons, mirroring

</details>

### Icons across platforms

Using the phone's own icons for common jobs like share and back, and the brand's icons for the rest.  
Designers: platform-standard system glyphs · Code: `icon.share (proposed): { ios, android, web }`

<details><summary>Designer and engineer</summary>

**Designer:** Use platform-standard glyphs for system actions (share, back, close, more, search, settings), since people know their own platform's version. The brand set covers product-specific ideas.

**Engineer:** A semantic icon maps to per-platform assets, such as icon.share (proposed) = {ios: square.and.arrow.up, android: a Material name, web: an SVG}; no icon map is generated yet.

**Example:** Share shows Apple's box-and-arrow on iPhone and the Android share glyph elsewhere.

**Also called:** system symbols, platform glyphs

</details>

### Icon sizes and optical sizing

A few set icon sizes, each one matched to the size of the words next to it.  
Designers: icon sizes 16, 20, 24px · Code: `size.icon.sm, .md, .lg`

<details><summary>Designer and engineer</summary>

**Designer:** Ship 16, 20 and 24px (12 and 32 if needed), each paired to the adjacent text's line height: 16 with 14px text, 20 with 16, 24 with 20.

**Engineer:** Dimension tokens size.icon.sm (16), .md (20) and .lg (24), plus size.icon.default set by the Density dial. Material Symbols add an optical-size axis from 20 to 48.

**Example:** A 16px icon sits beside 14px body text in a list row.

**Also called:** icon scale, optical size

</details>

### Icon library strategy

Whether to use a ready-made set of icons, add to one, or draw your own from scratch.  
Designers: native, open-source or custom set · Code: `icon.library (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Native sets feel at home, open-source sets look neutral, custom sets carry the most brand but cost the most. Default: native on apps, one open-source set on web.

**Engineer:** A system setting, not a token: icon.library (proposed) would name sf-symbols, material-symbols-rounded, lucide or custom. Custom additions use the library's own template so stroke, radius and keylines match.

**Example:** SF Symbols on iPhone, one open-source set on the web.

**Also called:** icon set choice, adopt, extend or draw

</details>

### Icon states

How an icon changes when you pick it, press it, or can't use it.  
Designers: outline at rest, filled plus accent · Code: `color.icon.accent, icon.fill.selected (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Outline at rest, filled plus accent color when selected: two cues, so it still works for color-blind people. Hover and pressed feedback go on the container, not the glyph.

**Engineer:** Not generated yet: icon.fill.selected (proposed) = 1 and icon.grade.emphasis (proposed) = 200 for variable-font axes. Color is generated: color.icon.default at rest, color.icon.accent when selected.

**Example:** The active tab icon is filled and blue; the rest are grey outlines.

**Also called:** selected icon, active icon

</details>

### Icon style and brand match

Whether icons are drawn as lines or filled in, with round or sharp corners, to fit the brand.  
Designers: outlined at rest, filled when selected · Code: `rest style param, icon.fill.selected (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Outlined at rest, filled when selected. Match corners to the radius family (rounded icons with pill buttons, sharp icons with 0-2px corners) and stroke to body text weight.

**Engineer:** Not tokens: the rest style, outline by default, is a param in opendesigner.meta.json. With Material Symbols, icon.fill.selected (proposed) = 1 would drive the FILL axis.

**Example:** A home tab icon is an outline, then fills in when tapped.

**Also called:** outline or filled, icon family

</details>

### Icon tiers beyond UI icons

Big icons with more detail for welcome screens and ads, in the same style as the small ones.  
Designers: pictograms and spot icons · Code: `icon.size.pictogram (proposed), icon.size.spot (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Pictograms and spot icons bridge UI icons and full illustration in feature grids and onboarding. Add them only with marketing surfaces, drawn with the UI icon's stroke logic scaled up.

**Engineer:** Not generated yet: larger dimension tokens such as icon.size.pictogram (proposed) = 64px and icon.size.spot (proposed) = 120px. The drawings are SVG assets beside the UI set.

**Example:** A 64px pictogram above each item in a feature grid.

**Also called:** pictograms, spot icons

</details>

### Imagery, illustration and brand marks

Rules for the photos, drawings, logo and app icon you see in the app.  
Designers: imagery, illustration and brand marks · Code: `asset manifest (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The picture layer: photo direction, aspect ratios, text on images, loading, illustration, rich media, graphic motifs and brand marks. It sets mood and brand without competing with content.

**Engineer:** No DTCG type for images or aspect ratios. An asset manifest (proposed) would list files for components; none is generated. Of the related tokens, only color.overlay.scrim exists today.

**Also called:** imagery, visual assets

</details>

### App icon, logo and favicon

The app's icon on your home screen, its logo inside, and the tiny icon on a web page tab.  
Designers: app icon, logo and favicon · Code: `SVG master, favicon.ico`

<details><summary>Designer and engineer</summary>

**Designer:** App icon: 1-3 filled shapes, checked in tinted and monochrome first. In product, a 24-32px symbol-only logo in the app bar; the full lockup on sign-in.

**Engineer:** Assets, not tokens: Apple layered icons, Android adaptive foreground, background and monochrome layers, a maskable PWA icon, and favicons from one SVG master (an SVG favicon plus favicon.ico).

**Example:** A 32px symbol in the app bar, the full wordmark on sign-in.

**Also called:** app icon, logo, favicon, brand marks

</details>

### Illustration style and tiers

How the app's drawings look, and where they show up, like on an empty page or a welcome screen.  
Designers: illustration style and tiers · Code: `illustration.color.* (proposed), illustration.size.spot (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** One style drawn from icon stroke, radius and palette, used in empty, error, success and onboarding states. Neutral spots for routine states, colorful for first run; little humor in errors.

**Engineer:** Mostly guidance; no illustration tokens are generated yet: illustration.color.* (proposed) aliasing brand primitives, illustration.stroke.width (proposed), illustration.size.spot (proposed). Drawings come through the H-illus hook.

**Example:** A calm grey drawing on an empty inbox, a colorful one after sign-up.

**Also called:** illustration system, spot illustration, hero illustration

</details>

### Image loading and placeholders

What you see while a picture is still loading or fails to load, so the page does not jump.  
Designers: reserved box, neutral placeholder · Code: `aspect-ratio, duration.skeleton.pulse (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Always reserve the final box so layout stays still. Use a neutral placeholder fill for images, skeletons only for container components, and a fallback image when the source fails.

**Engineer:** Reserve space with width and height or CSS aspect-ratio so CLS stays at or below 0.1 for 75% of visits. Placeholder fill: a color token; pulse: duration.skeleton.pulse (proposed).

**Example:** A grey box the size of the photo holds its place until it loads.

**Also called:** placeholder, image fallback, skeleton

</details>

### Graphic devices and motifs

Shapes and patterns that belong to the brand, used here and there to make the app feel like its own.  
Designers: brand motifs and graphic devices · Code: `SVG assets, $type: gradient`

<details><summary>Designer and engineer</summary>

**Designer:** Signature shapes, patterns, crops, frames and gradients from the brand identity. Use them only on expressive surfaces (marketing, onboarding, empty states, hero moments) so they never compete with content.

**Engineer:** SVG assets referenced by component props rather than tokens; gradients can be DTCG gradient tokens. On Apple platforms, brand content belongs on onboarding, not the launch screen.

**Example:** Dropbox's diamond shapes on a welcome screen, not in file lists.

**Also called:** brand motifs, graphic devices, signature details

</details>

### Photography art direction

Rules for which photos to use: who is in them, the angle, the light, and the colors.  
Designers: photo art direction brief · Code: `image.overlay.color (proposed), image.overlay.opacity (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** A one-paragraph brief (subjects, perspective, light, color treatment, casting) written before shooting or buying stock. Natural light reads factual; warm, graded color reads aspirational.

**Engineer:** Mostly guidance, not tokens. A color treatment would become image.overlay.color (proposed) and image.overlay.opacity (proposed). Apple platforms take JPEG or HEIC with an embedded color profile.

**Example:** Real customers at eye level in natural light, with ungraded color.

**Also called:** photo brief, photo style

</details>

### Aspect ratios and cropping

A short list of photo shapes, like wide or square, and where on the screen each one goes.  
Designers: aspect ratios and cropping · Code: `aspect-ratio, aspect.video (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Allow 3-5 ratios (16:9, 3:2, 4:3, 1:1, optionally 2:1), one per component slot. A small set keeps grids calm; wide feels cinematic, square product-focused.

**Engineer:** No DTCG ratio type: store a number (aspect.video (proposed) = 1.7778) or a 16 / 9 string in $extensions for CSS aspect-ratio. iOS bitmaps need @2x and @3x.

**Example:** 16:9 for heroes, 4:3 for card media, 1:1 for avatars.

**Also called:** image ratios, crops

</details>

### Emoji, 3D, animated icons and Lottie

Moving icons, emoji and 3D art, kept for big moments like a first visit.  
Designers: Lottie, 3D and animated icons · Code: `dotLottie, duration and cubicBezier tokens`

<details><summary>Designer and engineer</summary>

**Designer:** Animate icons only to confirm an action or show ongoing status. Keep 3D and Lottie for onboarding, celebration and marketing; they feel alive but are heavy and can distract.

**Engineer:** Timing uses motion tokens (duration, cubicBezier) and obeys reduced motion; the files themselves are assets, not tokens. dotLottie v2.0 packs animations, themes and state machines into one file.

**Example:** A checkmark that draws itself once when an upload finishes.

**Also called:** rich media, animated icons, Lottie

</details>

### Text and UI on images

Ways to keep words easy to read when they sit on a photo, like a dark fade behind them.  
Designers: scrim or protection gradient · Code: `color.overlay.scrim, gradient.scrim.bottom (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Put text beside images by default. When a hero needs text on top, add a scrim or protection gradient and test contrast against the image's worst-case region.

**Engineer:** Scrim tokens: color.overlay.scrim (color with alpha), or gradient.scrim.bottom (proposed). Text must keep 4.5:1, or 3:1 when large, over the lightest region behind it.

**Example:** A white headline on a beach photo gets a dark fade at the bottom.

**Also called:** scrim, protection gradient, image overlay

</details>

### Interaction and input

All the ways people control an app, like touch, mouse, keyboard, TV remote or voice.  
Designers: input modes, targets and focus · Code: `size.target.min, space.target.gap`

<details><summary>Designer and engineer</summary>

**Designer:** The inputs the system supports (touch, pointer, keyboard, remote, gaze, voice, rotary) and what depends on them: target sizes, target spacing and focus. These follow input precision, not device.

**Engineer:** Dimension tokens for target size and spacing (size.target.min, space.target.gap) plus focus-ring tokens, keyed to input mode such as pointer, touch or remote rather than device type.

**Example:** A laptop with a touchscreen gets finger-sized targets on its touch surfaces.

**Also called:** input methods

</details>

### Focus indicator

The outline that shows where you are when you move with the keyboard or a TV remote.  
Designers: focus ring, 2px at 2px offset · Code: `focus.ring.*, :focus-visible`

<details><summary>Designer and engineer</summary>

**Designer:** The visible ring showing keyboard, remote or switch focus. Default: 2px solid ring at 2px offset, following the component's radius, with 3:1 contrast against every surface.

**Engineer:** focus.ring.width and focus.ring.offset (dimension), color.border.focus (color) and radius.focus (control radius + offset); DTCG has no outline type. Web: :focus-visible with outline and outline-offset.

**Example:** Pressing Tab puts a ring around the next link.

**Also called:** focus ring, focus-visible

</details>

### Input modalities

Which ways of using the app each screen must handle, like tap, click or type.  
Designers: touch, pointer, keyboard, remote input · Code: `size.target.min, .pointer, .touch`

<details><summary>Designer and engineer</summary>

**Designer:** Which inputs each surface must support, and how density and targets switch between them. Default: touch-size targets on mobile and web, a pointer density mode for desktop.

**Engineer:** size.target.min matches the main input, from size.target.pointer or .touch. Floors: 44 iOS, 48 Android, 24 or 44 web, 28 macOS, 66 tvOS, 60 visionOS.

**Example:** A web app uses 44px targets for touch, even though 24px passes.

**Also called:** input modes

</details>

### Target size and spacing

How big and how far apart buttons must be so fingers don't hit the wrong one.  
Designers: minimum hit area and target spacing · Code: `size.target.min, space.target.gap`

<details><summary>Designer and engineer</summary>

**Designer:** Minimum hit area and target spacing by input precision: pointer 24px, finger 44-48, remote and gaze 56-66. Visuals may shrink with density; hit areas never do.

**Engineer:** Fixed tokens: size.target.min (24px web AA floor, 44pt iOS, 48dp Android) and space.target.gap (8 pointer, 12 touch). Web detects via pointer: coarse | fine.

**Example:** A small close icon still gets a 44-point tap area on iPhone.

**Also called:** touch target, hit area, tap target

</details>

### Layout

How a screen is split into areas, and how those areas move when the screen size changes.  
Designers: grids, breakpoints and max widths · Code: `grid.*, layout.*, breakpoint.* (all proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How screens divide and adapt: breakpoints, column grids, containers and maximum widths, reflowing and switching layouts, and safe areas. App shells and canonical layouts live with patterns.

**Engineer:** Not generated yet: dimension and number tokens for grids, margins and max widths. DTCG has no breakpoint or media-condition type, so breakpoints compile to build-time variables or resolver contexts.

**Example:** One column on a phone, a sidebar and content on a laptop.

**Also called:** page layout

</details>

### Responsive and adaptive strategy

How a layout fits different screen sizes, by stretching or by changing to a new layout.  
Designers: responsive reflow, adaptive layout switch · Code: `@media and @container queries`

<details><summary>Designer and engineer</summary>

**Designer:** Responsive means reflowing within a layout; adaptive means switching layouts at breakpoints, such as pane count or navigation type. Default: responsive inside panes, adaptive between breakpoints.

**Engineer:** Page layout uses viewport media queries; components use CSS container queries, with sizes like container.sm (proposed) = 24rem. Variant switching lives in code, not tokens.

**Example:** A list becomes a list plus detail view on a wide tablet.

**Also called:** responsive design, adaptive design, container queries

</details>

### Breakpoints

The window widths where the layout switches, like when a phone view turns into a tablet view.  
Designers: width breakpoints, mobile first · Code: `breakpoint.md (proposed), WindowSizeClass`

<details><summary>Designer and engineer</summary>

**Designer:** Window widths where the layout changes. Adopt Material's five width breakpoints for cross-platform work or Tailwind's set for web-only; design mobile first, then reveal, divide, resize, reposition or swap.

**Engineer:** Dimension tokens such as breakpoint.md (proposed) = 48rem are not generated yet. Media queries cannot read custom properties, so compile at build time. Android: WindowSizeClass; iOS: size classes.

**Example:** At 48rem the single column splits into two.

**Also called:** window size classes, media queries

</details>

### Containers and maximum content width

How wide the main content may get, so lines of text don't stretch across a huge screen.  
Designers: max content width and reading column · Code: `layout.container.max (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How content is framed: centered reading columns (max about 1280px, text 40-80 characters), navigation plus left-aligned content, or fluid data surfaces. Ask: reading, working or monitoring?

**Engineer:** A dimension token, layout.container.max (proposed) = 80rem, not generated yet. 65ch is not a valid DTCG dimension (px or rem only), so keep it in CSS.

**Example:** A blog post stays in a centered column even on a wide monitor.

**Also called:** max width, content width

</details>

### Column grid

Hidden columns that line things up on a page, like the lines on graph paper.  
Designers: column grid: columns, gutters, margins · Code: `grid.columns, .gutter, .margin (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Columns, gutters and margins: 4, 8 or 12 columns as width grows, 16-24px gutters, 16px margins on compact, 24px above. Type never hangs into the gutter.

**Engineer:** Not generated yet: grid.columns.* (proposed) as number tokens, grid.gutter.* and grid.margin.* (proposed) as dimensions, one value per breakpoint. Native mobile uses panes and layout guides.

**Example:** Cards spanning 4 of 12 columns, three to a row.

**Also called:** layout grid, gutters

</details>

### Safe areas, insets and edge policy

Keeping buttons and text away from notches, screen edges and folds where they get cut off.  
Designers: safe areas and edge-to-edge · Code: `viewport-fit=cover, env(safe-area-inset-*)`

<details><summary>Designer and engineer</summary>

**Designer:** Backgrounds run edge to edge; interactive content stays inside the safe area, clear of notches, system bars and hinges. TVs keep the outer 5% clear.

**Engineer:** Insets are runtime values from the platform, not tokens; tokens add padding on top, such as layout.safe.extra (proposed) = 16. Web needs viewport-fit=cover plus env(safe-area-inset-*).

**Example:** A video fills the whole screen, but its buttons stay clear of the notch.

**Also called:** safe area, insets, edge-to-edge

</details>

### Motion

How things in the app move: how fast, how they speed up or slow down, and when they stay still.  
Designers: motion system: duration, easing, springs · Code: `motion.duration.*, motion.easing.*`

<details><summary>Designer and engineer</summary>

**Designer:** The motion family: personality, duration ladder, easing curves, springs, enter and exit rules, reduced motion, and budgets per platform and device. Core durations sit between 100 and 300ms.

**Engineer:** DTCG duration, cubicBezier and transition tokens under motion.*. Springs have no DTCG type (issue #429), so they live in $extensions with a sampled CSS linear() fallback.

**Also called:** animation, transitions

</details>

### Duration scale

A few set times for how long each move takes, from instant to under a second.  
Designers: duration ladder, 100 to 300ms core · Code: `motion.duration.short`

<details><summary>Designer and engineer</summary>

**Designer:** Steps: instant 0, micro 100, short 150-200, medium 250-300, long 400-500, extra 700ms. Exits are 20-35% shorter; much past 500ms feels sluggish.

**Engineer:** DTCG duration tokens such as motion.duration.short = 150ms, on a ladder from .instant to .extra plus shorter exit steps. Figma variables import seconds only.

**Example:** A hover color changes in 100ms; full-screen dimming takes 700ms.

**Also called:** duration ladder, timing

</details>

### Easing set

How a move speeds up or slows down, like a car easing to a stop instead of braking hard.  
Designers: easing curves: standard, decelerate, accelerate · Code: `motion.easing.standard, cubic-bezier()`

<details><summary>Designer and engineer</summary>

**Designer:** Four curves: standard for moves on screen, enter (decelerate) to arrive fast and settle, exit (accelerate) to get out of the way, linear only for spinners and progress.

**Engineer:** DTCG cubicBezier arrays: motion.easing.standard [0.2, 0, 0, 1], .enter [0, 0, 0, 1], .exit [0.3, 0, 1, 1], .linear. CSS gets cubic-bezier(); x stays within 0-1.

**Example:** A menu drops in fast and settles, then speeds away when closed.

**Also called:** timing curves, cubic bezier

</details>

### Enter and exit asymmetry and interruptibility

Things leave faster than they arrive, and if you act mid-move, the app responds at once.  
Designers: shorter exits, interruptible transitions · Code: `motion.transition.enter, .exit`

<details><summary>Designer and engineer</summary>

**Designer:** Exits take about 70-80% of the entrance time and use an accelerate curve. Keep transitions interruptible, and never block input during a transition longer than about 100ms.

**Engineer:** Separate transition tokens, motion.transition.enter and motion.transition.exit. CSS transitions reverse from their current value while keyframe animations do not; SwiftUI springs retarget natively.

**Example:** Close a menu while it is still opening and it reverses at once.

**Also called:** enter and exit, interruptible motion

</details>

### Motion personality and model

Whether things move in a quick, calm way or a bouncy, fun way, and where fun is allowed.  
Designers: productive or expressive motion · Code: `Energy dial, motion.spring.*`

<details><summary>Designer and engineer</summary>

**Designer:** Productive motion (short, strong ease-out, no overshoot) for about 90% of interactions; expressive motion for 1-3 hero moments per flow. Keep bounce at or below 0.2.

**Engineer:** No motion-scheme mode: the Energy dial scales durations and springs, unlike Material 3's MotionScheme (standard, expressive). Bounce at or below 0.2 equals a damping ratio of 0.8 or higher.

**Example:** Menus fade in quickly; only the success screen gets a small bounce.

**Also called:** productive and expressive motion, motion scheme

</details>

### Motion by platform and device class

The phone runs its own screen changes, the brand styles small moves, and cars and watches move less.  
Designers: motion budget by device class · Code: `motion context modifier (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The OS owns screen transitions, back and sheets; the brand owns how things inside a screen react. The motion budget shrinks as attention narrows, to little or none in cars.

**Engineer:** OS transitions (navigation, back, sheets) are not tokenized. Not generated yet: a motion context modifier mapping device classes, such as handheld full, wrist minimal, vehicle none, to duration multipliers.

**Example:** Back swipes use the phone's own slide; the brand animates only in-screen controls.

**Also called:** motion budget, system transitions

</details>

### Reduced motion

If you ask your phone for less motion, things fade in place instead of sliding or zooming.  
Designers: reduced motion: fades, no travel · Code: `prefers-reduced-motion: reduce`

<details><summary>Designer and engineer</summary>

**Designer:** Treat WCAG 2.3.3 as required even though it is AAA. Keep feedback such as color and opacity changes; remove travel like slide, scale and parallax, and use crossfades instead.

**Engineer:** A reduced motion mode (motion.reduced.tokens.json) points transitions at short fades with zero travel. Web reads @media (prefers-reduced-motion: reduce); each major OS has a matching setting.

**Example:** With Reduce Motion on, a sliding panel fades in place.

**Also called:** Reduce Motion, prefers-reduced-motion

</details>

### Springs and physics

Moves that act like a real spring, slowing to a stop on their own.  
Designers: spring physics, critically damped · Code: `dampingRatio, stiffness in $extensions`

<details><summary>Designer and engineer</summary>

**Designer:** Springs feel natural and keep their momentum when interrupted, unlike fixed curves. Use critically damped springs for UI transitions and a little bounce only for spatial hero motion.

**Engineer:** No DTCG spring type: store dampingRatio and stiffness in $extensions, derive duration and bounce for SwiftUI Spring(duration:bounce:), use Compose spring(), and pre-sample CSS linear().

**Example:** A sheet dragged halfway and let go springs back smoothly into place.

**Also called:** spring animation, damping, stiffness

</details>

### Sound and haptics

Feedback you feel or hear instead of see, like a small buzz or a soft click.  
Designers: haptics and UI sounds (earcons) · Code: `haptics.intensity param, H-sound, H-haptic hooks`

<details><summary>Designer and engineer</summary>

**Designer:** Non-visual feedback: haptic patterns and UI sounds (earcons). Used sparingly, they confirm actions and make the UI feel physical; overused, they annoy and feel cheap.

**Engineer:** No DTCG type for haptics or sound, and none generated: OpenDesigner records the haptics.intensity parameter and sends sounds and custom haptics to the H-sound and H-haptic hooks.

**Example:** A light tap on the wrist when a payment goes through.

**Also called:** non-visual feedback, earcons, vibration

</details>

### Haptic vocabulary

A small set of buzzes the phone makes for things like a win, a warning, or flipping a switch.  
Designers: haptic vocabulary: success, warning, selection · Code: `haptic.feedback.success (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** About six semantic events (success, warning, error, selection, toggle, impact), used sparingly. Crisp, short haptics feel premium; long buzzy vibrations feel cheap. Standard controls already play their own.

**Engineer:** Not generated yet: string tokens such as haptic.feedback.success (proposed), mapped to iOS UIFeedbackGenerator .success and Android HapticFeedbackConstants.CONFIRM. Only haptics.intensity exists. Never store raw vibration durations.

**Example:** A crisp tick each time a picker wheel moves to the next item.

**Also called:** haptic feedback, vibration patterns

</details>

### UI sounds

Whether the app makes little sounds when things happen, like a chime when a message is sent.  
Designers: earcons, silent by default · Code: `H-sound hook; file reference (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Silent by default on web and productivity apps. Earcons only for rare, meaningful events on mobile, games or spatial platforms, always with a mute option, never as the only signal.

**Engineer:** No DTCG type and none generated: sounds would be file references plus a volume (proposed), requested through hook H-sound. On iOS, the audio session category should respect the silent switch.

**Example:** A payment app plays one short sound on success and stays silent otherwise.

**Also called:** earcons, UI audio

</details>

### Shape and borders

How round the corners are, and the lines that outline and split things on screen.  
Designers: corner radius and borders · Code: `radius.*, border.width.*`

<details><summary>Designer and engineer</summary>

**Designer:** Corner radius (scale, personality, per-component roles, nesting, expressive shapes) plus borders, strokes and dividers. Radius is where systems diverge most, from square to pill; every 2025-2026 revision got rounder.

**Engineer:** Radius primitives are DTCG dimensions (radius.4 = 4px, radius.full), aliased by roles such as radius.control and radius.container. Strokes use border.width.* and color.border.*.

**Example:** A card with 12px corners and a thin gray outline.

**Also called:** corner radius, borders

</details>

### Border widths and dividers

How thick the outlines are, and when a thin line splits one part of the screen from the next.  
Designers: border widths 1, 2, 4px · Code: `border.width.default, .selected, .emphasis`

<details><summary>Designer and engineer</summary>

**Designer:** Widths 1, 2, 4px: 1 by default, 2 for selected and focus, 4 for emphasis. Separate with space or a surface change before lines; lines suit dense data views.

**Engineer:** Dimension tokens border.width.1, .2 and .4, aliased by border.width.default, .selected and .emphasis; DTCG border composites bundle color, width and style. Width changes use inset box-shadow.

**Example:** A 2px outline marks the selected card while the others keep 1px.

**Also called:** stroke width, separator, hairline

</details>

### Full-round and expressive shapes

Pill shapes and fun shapes like flowers, kept for a few spots where they count.  
Designers: pills and signature shapes · Code: `radius.full, RoundedPolygon, clip-path`

<details><summary>Designer and engineer</summary>

**Designer:** Pills read tappable and friendly. Expressive shapes and shape morphing add play; use them for avatars, loaders, image masks or FABs, and limit them to 1-3 signature uses.

**Engineer:** radius.full is a dimension token. Material 3 Expressive has 35 MaterialShapes as Compose RoundedPolygon objects; web needs SVG clip-path: path() or masks. Arbitrary shapes have no DTCG type.

**Example:** A flower-shaped photo frame for profile pictures in a playful Android app.

**Also called:** pill, shape library, shape morphing

</details>

### Corner geometry and nesting

The kind of curve a corner has, and how a box inside a box gets corners that fit.  
Designers: squircle corners, concentric nesting · Code: `radius.nested`

<details><summary>Designer and engineer</summary>

**Designer:** Circular arcs or continuous squircle corners, which look softer and more Apple-like. Nested shapes stay concentric: inner radius is outer radius minus padding, so the gap stays even.

**Engineer:** Inner radius is computed at generation, max(outer - padding, smallest step), and emitted as radius.nested. The engine emits circular arcs; web corner-shape: squircle is an optional enhancement, not generated.

**Example:** Card 16px, padding 8px, so the photo inside gets 8px corners.

**Also called:** squircle, continuous corners, concentric radius, nested radius

</details>

### Roundness and brand shape language

How round the corners are all over the app, from sharp and serious to soft and friendly.  
Designers: roundness: sharp, subtle, rounded, pill · Code: `Roundness dial, radius.control`

<details><summary>Designer and engineer</summary>

**Designer:** One dial (sharp, subtle, rounded, pill) sets every corner radius. Sharp reads technical, round reads friendly. Research favors subtle; OpenDesigner starts at 8px (Roundness 50). Logo curves inspire shapes.

**Engineer:** The Roundness dial picks, at generation, which primitive radius.control aliases, from a small step to {radius.full}; there is no shape-theme mode. Signature shapes are SVG assets.

**Example:** Sharp corners for a data tool, pill buttons for a playful consumer app.

**Also called:** shape personality, roundness dial, signature shape

</details>

### Radius scale and default control radius

A short list of how round corners can be, and the usual roundness for buttons.  
Designers: corner radius scale, 8px default controls · Code: `radius.control, radius.container, border-radius`

<details><summary>Designer and engineer</summary>

**Designer:** Allowed corner radii plus the control default. Research default: 6px controls; OpenDesigner defaults to 8px controls, 12px containers at Roundness 50. Radius grows with size.

**Engineer:** DTCG dimension tokens: primitives radius.0 to radius.32 plus radius.full; roles radius.control, .container, .nested and .focus. CSS border-radius; Compose RoundedCornerShape; iOS continuous corners.

**Example:** Buttons with 8px corners inside cards with 12px corners.

**Also called:** border radius, corner radius scale

</details>

### Radius roles per component

Rules that give each kind of part its own roundness, small for tags and bigger for cards.  
Designers: radius roles per component · Code: `radius.control, radius.container, radius.person`

<details><summary>Designer and engineer</summary>

**Designer:** Named roles (detail, control, container, overlay, person) map the radius scale to component types. Radius steps up as elements get bigger, and full round is kept for avatars.

**Engineer:** Role tokens radius.detail, radius.control, radius.container, radius.overlay and radius.person alias radius primitives ($type dimension). Components use roles, never primitives; radius.person resolves to radius.full.

**Example:** Buttons 4-8px, cards 8-12px, avatars fully round.

**Also called:** semantic radius, corner roles

</details>

### Space, sizing and density

How much room goes between and inside things, how big the parts are, and how tightly they pack.  
Designers: spacing, sizing and density · Code: `space.*, size.control.*, size.icon.*`

<details><summary>Designer and engineer</summary>

**Designer:** The spacing scale and its named uses, the size ladders for controls and media, and density: how tightly the whole UI packs. Values converge; base unit and naming differ.

**Engineer:** DTCG dimension tokens in px or rem (dp and pt map to px): space.* steps, semantic space.inset.*, .stack.*, .inline.* and .section.*, size.control.*, size.icon.*, and density resolver contexts.

**Example:** The same 16px padding inside every card.

**Also called:** spacing, sizing

</details>

### Base spacing unit

The one small step that every gap and size is counted in, like the marks on a ruler.  
Designers: base unit: 4px grid, 8px rhythm · Code: `raw.spaceUnit (default 4)`

<details><summary>Designer and engineer</summary>

**Designer:** The unit every spacing and sizing value multiplies. Default: 4 as the grid, 8 as the rhythm. A pure 4 base suits dense tools; 8 suits marketing and content sites.

**Engineer:** Not a token: the unit, raw.spaceUnit (4 by default), is recorded in the space group's $extensions.opendesigner; the ladder multiplies it, so space.8 is 8px.

**Example:** Gaps of 4, 8, 16 and 24 pixels, all built from 4.

**Also called:** grid unit, 4px grid, 8pt grid

</details>

### Density

How much fits on the screen at once, packed tight or spread out, and who gets to choose.  
Designers: density: how tightly the UI packs · Code: `density: compact, comfortable, spacious`

<details><summary>Designer and engineer</summary>

**Designer:** How much content fits in an area and who controls it. Density changes layout, not only padding: body size, control height and row height.

**Engineer:** Dimension values per density resolver context (compact, comfortable, spacious), such as size.control.md at 32, 40 and 48. size.target.min sits outside the modifier and never changes.

**Example:** A spreadsheet packs rows tight; a shop page spreads things out.

**Also called:** information density

</details>

### Density by device class

How much to show at once depends on how far away you are, not how big the screen is.  
Designers: density by viewing distance · Code: `context modifier: desk, handheld, wrist (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Density follows viewing distance and input, not pixel count. A 65-inch TV is a far-away phone: phone-level density. Watches, cars and headsets stay sparse; desks can go compact.

**Engineer:** Not generated yet: density keyed to a context resolver modifier, not screen size, such as desk compact, handheld and leanback comfortable, wrist, vehicle and spatial sparse.

**Example:** A TV app shows about as much as a phone app, not a laptop.

**Also called:** device density

</details>

### Density strategy and modes

Who picks how tight things are packed, the app or you, and which parts can pack tighter.  
Designers: who sets density; compact modes · Code: `density modifier: compact, comfortable, spacious`

<details><summary>Designer and engineer</summary>

**Designer:** Who sets density (system, product or user) and which components get a compact mode. Consumer products stay comfortable; data tools offer a compact mode for tables, lists, menus and trees.

**Engineer:** The resolver's density modifier: compact, comfortable (default) or spacious. Compact drops insets, stacks and control heights about one scale step; size.target.min never changes.

**Example:** A 'Compact' option that makes table rows shorter so more fit.

**Also called:** density modes, compact mode

</details>

### Density voice and base size

Whether the whole app feels tight, cozy or roomy, and how big its text and buttons are.  
Designers: compact, comfortable or spacious · Code: `density modifier: size.control.md, space.inset.*`

<details><summary>Designer and engineer</summary>

**Designer:** The product-wide density personality: compact, comfortable or spacious, with the body size and control height that come with it. Comfortable suits apps, spacious suits marketing, compact suits data tools.

**Engineer:** The resolver's density modifier (compact, comfortable, spacious) swaps size.control.md and space.inset.*; the body size is set by the Density dial at generation, not per mode.

**Example:** An admin tool with 14px text and 32px buttons.

**Also called:** density personality

</details>

### Responsive spacing

Whether the gaps get bigger when the window gets wider.  
Designers: layout spacing grows with window · Code: `layout.margin (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Only layout spacing (page margins, pane spacers, section gaps) grows with window size. Component spacing changes only with density, never with breakpoint, so controls feel the same everywhere.

**Engineer:** Not generated yet: layout tokens with breakpoint modes, such as layout.margin (proposed) = 16 / 24 / 24; component tokens get none. Native platforms use system layout guides and window size classes.

**Example:** Page margins grow from 16px in narrow windows to 24px in wider ones.

**Also called:** adaptive spacing

</details>

### Vertical rhythm

Lining up text lines and gaps on the same steps, like the lines in a notebook.  
Designers: vertical rhythm on a 4px grid · Code: `lineHeight on 4px steps; text-box-trim`

<details><summary>Designer and engineer</summary>

**Designer:** Line heights and vertical spacing snap to a 4px grid. Measure spacing from the text box instead of a strict baseline grid, and let layouts survive user text-spacing overrides.

**Engineer:** Line-height and section-spacing tokens sit on multiples of 4px on the spacing scale. On web, CSS text-box trimming is a progressive enhancement; text boxes never get fixed heights.

**Example:** Line heights such as 20px and 24px, both multiples of 4.

**Also called:** baseline grid

</details>

### Spacing scale

The short list of gap sizes you may use, so spacing never has to be guessed.  
Designers: spacing scale, 0 to 96 · Code: `space.0 to space.96`

<details><summary>Designer and engineer</summary>

**Designer:** The ordered set of allowed gaps: about 15 steps from 0 to 96. 2px steps serve component internals; above 8px, aim for steps about 25% apart.

**Engineer:** Primitive dimension tokens named by pixel value, space.0 to space.96 (unit x 0 to 24), used through space.inset.*, .stack.*, .inline.* and .section.*. No negative steps.

**Example:** Padding of 16 and a gap of 8, never 15 or 7.

**Also called:** space scale, spacing ramp

</details>

### Semantic spacing (inset, gap, layout)

Names for what each gap is for, like room inside a button or space between cards.  
Designers: inset, gap and layout spacing · Code: `space.inset.md, space.stack.lg`

<details><summary>Designer and engineer</summary>

**Designer:** Three named jobs: inset (padding inside a component), gap (between siblings in a stack or row), and layout (margins, pane spacers, sections). Insets can be square, squished or stretched.

**Engineer:** Semantic dimension aliases space.inset.*, .stack.*, .inline.* and .section.*, swapped per density. A squish inset would need separate block and inline tokens; DTCG 2025.10 has no padding composite.

**Example:** A pill button has less padding above and below than on its sides.

**Also called:** inset, stack, gap, padding

</details>

### Size scales

A few set sizes for buttons and icons, so things placed in a row line up.  
Designers: shared size ladders · Code: `size.control.*, size.icon.*`

<details><summary>Designer and engineer</summary>

**Designer:** Shared size ladders for interactive controls and for icons and avatars, so a button, input and icon placed side by side align on the same heights.

**Engineer:** Dimension tokens size.control.sm to .lg and size.icon.sm to .lg plus .default. Avatar sizes like size.avatar.xs (proposed) and component tokens are not generated yet.

**Example:** A 40px button and a 40px input side by side.

**Also called:** sizing scale, size ladder

</details>

### Control height scale

Small, medium and large heights that buttons, text boxes and menus share, so a row lines up.  
Designers: control heights: 32, 40, 48 · Code: `size.control.sm/md/lg`

<details><summary>Designer and engineer</summary>

**Designer:** Small, medium and large heights shared by buttons, inputs and selects: 32, 40, 48 for touch-inclusive products, 24, 32, 40 for pointer-first desktop tools. Don't mix sizes in one group.

**Engineer:** Dimension tokens size.control.sm, .md and .lg; component tokens like button.height.md (proposed) are not generated yet. Hit areas keep 44pt iOS and 48dp Android minimums.

**Example:** A search box and its button, both 40px tall.

**Also called:** control sizes, component sizes

</details>

### Icon and avatar size scales

A few set sizes for icons and the small round photos of people.  
Designers: icon and avatar size ladders · Code: `size.icon.*, size.avatar.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Fixed ladders so icons and avatars stay consistent: icons 16, 20, 24, 32; avatars 16 to 64 (Primer's set). Icon size equals the body line height minus 0-4px.

**Engineer:** Dimension tokens size.icon.sm = 16, .md = 20 and .lg = 24; avatar sizes like size.avatar.xs (proposed) are not generated yet. SF and Material Symbols can scale with text.

**Example:** A 16px icon in a small button, a 40px avatar beside a comment.

**Also called:** icon sizes, avatar sizes

</details>

### Whitespace personality and grouping

How roomy or packed things feel, and how gaps show what belongs together.  
Designers: whitespace: airy or tight grouping · Code: `space.section.sm, .md, .lg`

<details><summary>Designer and engineer</summary>

**Designer:** Airy or tight feel, set by the ratio of space inside a group to space between groups: at least 1:2, or 1:3 to 1:4 for airy brands.

**Engineer:** Semantic space.section.sm, .md and .lg set outer gaps and space.stack.* inner ones; engine.py validate errors when inner exceeds half the outer in any density.

**Example:** A label sits close to its field and far from the next one.

**Also called:** white space, negative space

</details>

### Typography

How the words in an app look: which fonts, what sizes, and how much space they get.  
Designers: type system: faces, scale, roles · Code: `DTCG typography composite`

<details><summary>Designer and engineer</summary>

**Designer:** Typefaces, the type scale and its named roles, line height and spacing, text layout, and how text behaves across screens, zoom settings and non-Latin scripts.

**Engineer:** DTCG typography composite (fontFamily, fontSize, fontWeight, letterSpacing, lineHeight as a unitless multiplier), built from atomic fontFamily, fontWeight, dimension and number tokens. No slot for text case or paragraph spacing.

**Example:** Big bold headings, 16px body text for reading, small gray labels.

**Also called:** type, type system

</details>

### Scripts, fallbacks and script metrics

Making words in Hindi, Arabic and more look right, with backup fonts and room to fit.  
Designers: script coverage and fallback stacks · Code: `font.family.text, :lang() line heights`

<details><summary>Designer and engineer</summary>

**Designer:** Scripts to cover, a fallback stack for each, and script tweaks: taller line height for Indic and CJK, no italics or all caps outside Latin, right-to-left direction.

**Engineer:** Per-locale fontFamily fallback arrays, such as font.family.text for hi-IN, are not generated yet; the CSS export sets line heights for listed scripts through :lang() rules.

**Example:** Hindi text falls back to Noto Sans Devanagari with a taller line height.

**Also called:** internationalization, non-Latin scripts, font fallback

</details>

### Text metrics

Gaps between lines, letters and blocks of text, and how thick the letters are.  
Designers: line height, letter spacing, weights · Code: `lineHeight, letterSpacing, fontWeight`

<details><summary>Designer and engineer</summary>

**Designer:** Line height near 1.5 for 12-16px, tighter as text grows; letter spacing 0 at body, negative on big headings; three weights; paragraph spacing about one body size.

**Engineer:** Typography composite: lineHeight is a unitless multiplier, letterSpacing a px or rem dimension, fontWeight 1-1000 or aliases like semi-bold. Paragraph spacing has no slot; use a separate dimension token.

**Example:** 16px body text with a 24px line height and no extra letter spacing.

**Also called:** line height, letter spacing, leading

</details>

### Numerals

Giving each digit the same width, so rows of prices line up neatly.  
Designers: tabular and proportional lining figures · Code: `font-variant-numeric: tabular-nums`

<details><summary>Designer and engineer</summary>

**Designer:** Proportional lining figures in running text, tabular lining figures in tables and live-updating numbers so digits line up and do not jump. Native digits serve other scripts.

**Engineer:** No DTCG slot for font features; store $extensions such as fontFeatureSettings: 'tnum', or emit component CSS font-variant-numeric: tabular-nums lining-nums.

**Example:** A countdown timer whose digits stay put as they change.

**Also called:** tabular figures, tabular numbers

</details>

### Responsive and device-distance type

How text size changes on phones, watches and TVs, so it looks right from where you sit.  
Designers: fixed body, fluid display type · Code: `font.size.* per breakpoint (not generated)`

<details><summary>Designer and engineer</summary>

**Designer:** Body text stays fixed; display styles may go fluid on web. Farther screens need bigger numbers: body is 17pt on phone, 29pt on TV.

**Engineer:** DTCG has no fluid value like clamp(), so responsive type needs modes per breakpoint (not generated yet). Units: pt on Apple, sp on Android, epx on Windows, rem on web.

**Example:** Body text is 17 points on iPhone and 29 points on Apple TV.

**Also called:** fluid type, viewing-distance type

</details>

### Type roles and emphasis

Set text styles for each job, like big titles, reading text and small button words.  
Designers: type styles: display, headline, body, label · Code: `text.body.md`

<details><summary>Designer and engineer</summary>

**Designer:** Named styles by job (display, headline, title, body, label, code), most in large, medium and small, with one emphasized weight per style. Emphasis uses weight first, color second.

**Engineer:** Typography composites by job and size, such as text.body.md, over primitives such as font.size.14 and font.weight.body. Emphasized variants are not generated yet.

**Example:** Headline Large for a page title, Body Medium for paragraphs, Label Small for tags.

**Also called:** text styles, type styles

</details>

### Type scale

The fixed list of text sizes an app may use, from tiny labels to big headings.  
Designers: type scale: base size and ratio · Code: `font.size.14`

<details><summary>Designer and engineer</summary>

**Designer:** Body size and the ratio that generates the rest. Body runs 14px for tools, 16px for reading; ratios run 1.125-1.2 for dense apps, 1.333+ for editorial.

**Engineer:** Primitive dimension tokens named by pixel size, such as font.size.14, from round(base x ratio^n); base and ratio sit in the group's $extensions.opendesigner.

**Example:** Every heading picks from the same few sizes instead of a random one.

**Also called:** type ramp, font size scale

</details>

### Text scaling and legibility

When you turn up text size in settings, the app still fits and reads well.  
Designers: Dynamic Type and text-size support · Code: `rem, sp, UIFont.TextStyle`

<details><summary>Designer and engineer</summary>

**Designer:** Support the user's text-size setting: Dynamic Type up to AX5, Android font scale to 200%, browser zoom to 200%. Containers grow with text, and layouts survive user text-spacing overrides.

**Engineer:** Text tokens use scalable units: rem on web, sp on Android, UIFont.TextStyle on iOS. Never put sp in spacing tokens; no text container gets a fixed height.

**Example:** At the largest text setting, a button grows taller instead of cutting off its label.

**Also called:** Dynamic Type, font scale, text zoom

</details>

### Text layout (measure, alignment, casing, truncation)

How long lines of text get, which side they line up on, and what happens when words don't fit.  
Designers: line length, alignment, casing, truncation · Code: `size.measure.prose (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Keep prose near 65-70 characters per line (35-40 for CJK). Default to start alignment and sentence case; wrap first, then ellipsis with access to the full text.

**Engineer:** No DTCG type for measure, case or truncation. DTCG dimensions allow only px and rem, so size.measure.prose (proposed) would keep 65ch in $extensions; casing stays in CSS.

**Example:** A help article capped at about 70 characters per line.

**Also called:** measure, line length, truncation

</details>

### Typeface

The style of letters an app uses, like the font you pick for a school report.  
Designers: typeface or font family · Code: `font.family.*`

<details><summary>Designer and engineer</summary>

**Designer:** Which font families the system uses and why: where they come from, the personality they project, how many there are, their variable axes, and how they load.

**Engineer:** DTCG fontFamily tokens, a string or fallback array: font.family.text for UI and body, font.family.display for headings (aliases text by default) and font.family.mono.

**Example:** Inter for the whole app, plus a code font for snippets.

**Also called:** font, font family

</details>

### Variable axes and optical sizing

One font that can slide from thin to bold and reshape its letters for small or big text.  
Designers: variable font axes, optical size · Code: `font-optical-sizing: auto`

<details><summary>Designer and engineer</summary>

**Designer:** Variable fonts expose axes such as weight, optical size and grade. Default: a font with wght and opsz, with optical size tied to font size.

**Engineer:** DTCG fontWeight takes 1-1000; the typography composite has no slot for opsz, GRAD or wdth, so they live in $extensions. CSS: font-optical-sizing: auto.

**Example:** One font file covers regular, semibold and bold.

**Also called:** variable fonts, optical size

</details>

### Font licensing and loading

The rules for using a font, and how it shows up fast without text jumping.  
Designers: font licensing and loading budget · Code: `@font-face, font-display: swap`

<details><summary>Designer and engineer</summary>

**Designer:** How fonts are licensed, packaged and loaded, and what that costs in speed. Each web family adds download time, so budget two families and show a fallback first.

**Engineer:** Not tokenized beyond the fontFamily fallback array; @font-face CSS is not generated yet. Default advice: WOFF2, one variable file per family, font-display: swap, a metric-adjusted fallback and per-script subsets.

**Example:** Text appears at once in a system font, then swaps to the brand font.

**Also called:** font loading, web fonts

</details>

### Families, pairing and monospace

How many fonts an app uses, which ones pair well, and a font for code.  
Designers: one UI family plus monospace · Code: `font.family.text, .display, .mono`

<details><summary>Designer and engineer</summary>

**Designer:** Default to one UI family plus one monospace, adding a serif or display face only for marketing. Pair siblings that share x-height, contrast and width; tabular figures handle data.

**Engineer:** font.family.text, .display and .mono ($type fontFamily); the composites text.code.sm and text.code.md use mono. Numeric cells get font-variant-numeric: tabular-nums.

**Example:** One sans-serif for the app and a monospace font for code samples.

**Also called:** font pairing, monospace font

</details>

### Typeface classification and personality

The mood a font's letter shapes give, such as friendly, serious, new or old.  
Designers: type class, like neo-grotesque or humanist · Code: `type.faceSuggestion.classification`

<details><summary>Designer and engineer</summary>

**Designer:** The type class (neo-grotesque, humanist, geometric, serif, rounded) chosen from brand adjectives, then vetoed if letters get confused at 12-14px or scripts are missing.

**Engineer:** Not a token itself: it guides the value of font.family.*. The engine records the param type.faceSuggestion.classification, such as neutral-sans, in opendesigner.meta.json to drive recommendations.

**Example:** A rounded font feels playful; a serif leans toward heritage.

**Also called:** type classification, font personality

</details>

### Typeface sourcing and platform mapping

Whether an app uses the font that came with your device, a free font, or its own.  
Designers: system, open or custom brand face · Code: `font.family.text fallback array`

<details><summary>Designer and engineer</summary>

**Designer:** System stack, open neutral face (Inter, Roboto) or custom brand face, and which roles get which on each platform. Common split: brand for display and headlines, system for body.

**Engineer:** font.family.text holds one fallback array, such as system-ui, -apple-system, Segoe UI, Roboto, so each platform picks its system face. Apple's SF is system-only; custom faces must be bundled.

**Example:** SF Pro on iPhone, Roboto on Android, the brand font for headlines.

**Also called:** system font versus brand font

</details>

## Tokens

### Tokens

Saved, named choices, like a brand blue, that design apps and code can share.  
Designers: design tokens · Code: `DTCG 2025.10 plus Resolver`

<details><summary>Designer and engineer</summary>

**Designer:** Named values that store every foundation decision, such as color.bg.accent instead of a hex code. Change one token and every design and screen that uses it follows.

**Engineer:** The data layer: tiers, naming, coverage, types, modes, themes and delivery. engine.py generate writes DTCG 2025.10 files plus a Resolver; springs and P3 colors ride in $extensions.opendesigner.

**Also called:** design tokens

</details>

### Token coverage

Which choices get a saved name, and which stay as one-off numbers.  
Designers: what gets tokenized · Code: `one DTCG group per category`

<details><summary>Designer and engineer</summary>

**Designer:** Which properties become tokens. Default: everything Figma variables can bind and Check designs can lint, plus motion and focus; one-off illustration values stay out.

**Engineer:** Emitted DTCG groups: color, font, text, space, size, radius, border, elevation, opacity, motion, focus and icon. Shadow, z-index and breakpoint groups are not generated; native uses elevation and size classes.

</details>

### Platform delivery of tokens

The form design values take inside each kind of app code, like a web page or a phone app.  
Designers: tokens in platform code · Code: `build/css/tokens.css, DesignTokens.swift, DesignTokens.kt`

<details><summary>Designer and engineer</summary>

**Designer:** The form tokens take in each platform's code. On the web: CSS custom properties, media queries for user preferences, container queries for components, viewport breakpoints only for page layout.

**Engineer:** OpenDesigner writes build/css/tokens.css, tailwind/theme.css, swift/DesignTokens.swift and compose/DesignTokens.kt. Web themes follow prefers-color-scheme with a [data-theme] override; type uses rem. No Flutter output.

**Example:** --ds-color-text-primary in CSS, a DsColors class in Compose.

</details>

### Modes and theming axes

The switches that change values in one go, like light and dark, or roomy and tight.  
Designers: modes: light, dark, density, motion · Code: `resolver modifiers, Figma collection modes`

<details><summary>Designer and engineer</summary>

**Designer:** The axes along which values switch, such as color scheme, contrast, density or brand. OpenDesigner generates light and dark, three densities and reduced motion; no contrast or brand modes yet.

**Engineer:** DTCG Resolver modifiers with contexts (theme, density, motion); Figma collections and modes. Outputs multiply, so keep axes few, and orthogonal so no two set the same token. Primitives stay single-valued.

**Example:** Page background is white in light mode and near-black in dark mode.

**Also called:** theming axes

</details>

### Token naming

The rules for how saved choices get their names, so you can guess a name and find it.  
Designers: token naming convention · Code: `category.property.concept.variant(State)`

<details><summary>Designer and engineer</summary>

**Designer:** The grammar that makes token names predictable: category, property, concept, variant, state. Theme and brand never appear in semantic names, because they are modes.

**Engineer:** category.property.concept.variant, state appended in camelCase: color.bg.accent.boldHover. The export prefix (default ds) namespaces it: CSS --ds-color-bg-accent-bold-hover; Swift and Compose use camelCase.

</details>

### Primitive naming

How the basic values get named, like accent 9 for a shade or space 16 for a 16 pixel gap.  
Designers: role and numeric step · Code: `color.accent.light.9, space.16`

<details><summary>Designer and engineer</summary>

**Designer:** Research favors hue plus a numeric step for color. OpenDesigner names ramps by role and step (accent 9), space by pixel value (16), and keeps t-shirt sizes for semantic tokens.

**Engineer:** Emitted: color.accent.light.9 (color: role, mode, step) and space.16 (dimension, named by px). Hue names such as color.blue.600 (proposed) are not generated. Avoid ordinal scales.

</details>

### Themes and brands

How one design gets a new look, for a new brand or a customer, without being rebuilt.  
Designers: theming, multi-brand, white-label · Code: `tok.themes.generator, .brands, .whitelabel`

<details><summary>Designer and engineer</summary>

**Designer:** How the system is re-skinned: a few inputs generate a theme, several brands share one system, and white-label customers change a limited set of values.

**Engineer:** Parent of tok.themes.generator, .brands and .whitelabel. Today inputs such as raw.brandColor generate the theme; a re-skin overrides primitives through state.json overrides. Semantic names never change.

</details>

### Multi-brand architecture

How a few brands share one set of parts: they work the same, but colors and fonts change.  
Designers: multi-brand theming · Code: `brand modifier (planned) re-pointing color.accent.*`

<details><summary>Designer and engineer</summary>

**Designer:** Fixed across brands: anatomy, behavior, semantic names, status meanings. Flexible: brand color, typeface, logo, imagery. Radius, density and motion flex with care. Build as if a second brand will come.

**Engineer:** Planned, not generated yet: a brand resolver modifier or Figma extended collection whose contexts re-point a brandable set, such as color.accent.* and font.family.display; semantic names stay fixed.

**Also called:** multi-brand

</details>

### Theme-generator inputs

A few brand choices, like the main color, from which a whole look is worked out for you.  
Designers: theme seed: accent, base, contrast · Code: `raw.brandColor, raw.neutralBase, raw.contrastTarget`

<details><summary>Designer and engineer</summary>

**Designer:** The few brand knobs a whole theme is computed from. Default three: brand or accent color, neutral base or temperature, and contrast. A warmer gray alone shifts personality.

**Engineer:** Inputs are raw.brandColor, raw.neutralBase and raw.contrastTarget in state.json, with the Warmth dial; engine.py generate derives the color.accent.* and color.neutral.* ramps in OKLCH.

</details>

### White-label customization surface

The short list of things other companies may change to make the app their own, like logo and color.  
Designers: white-label brand color and logo · Code: `tenant.color.brand (proposed), tenant.logo (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** What external customers may change in a white-label product. Default: brand color and logo; font and radius only with previews and validation. Everything else is derived.

**Engineer:** Today the accent ramps derive from one input, raw.brandColor. Proposed tenant inputs: tenant.color.brand (proposed), tenant.logo (proposed), optionally tenant.font.display (proposed); all else derives.

**Also called:** tenant theming

</details>

### Token tiers

Layers of names, from raw values like a blue shade up to names that say what the blue is for.  
Designers: primitive, semantic, component tiers · Code: `color.bg.accent.bold = {color.accent.light.9}`

<details><summary>Designer and engineer</summary>

**Designer:** Primitives hold raw values; semantic tokens say what a value is for and are where theming happens; optional component tokens, not generated yet, let one component restyle on its own.

**Engineer:** Semantic color.bg.accent.bold = "{color.accent.light.9}", a primitive; planned component token button.primary.bg (proposed) would alias it. Aliases must share a type and never cycle.

**Example:** Accent shade 9, then accent background, then a primary button background.

**Also called:** token layers

</details>

### Token value types and encoding

The set way each kind of choice is written down, such as colors, sizes, fonts and motion.  
Designers: token value types · Code: `13 DTCG types plus $extensions`

<details><summary>Designer and engineer</summary>

**Designer:** How each kind of value is written: color, dimensions, typography, shadow and border, motion, layout. It decides what survives the trip into Figma and each platform.

**Engineer:** The 13 DTCG 2025.10 types. Gaps include springs, string, boolean, percentages and assets; springs go in $extensions on a transition token with a cubic-bezier fallback.

</details>

### Color encoding

How each color is written in the file so every tool shows the same shade.  
Designers: color space with hex fallback · Code: `$type color, colorSpace oklch`

<details><summary>Designer and engineer</summary>

**Designer:** Which color space colors are stored in, with a hex fallback. Author in OKLCH or sRGB, send sRGB to Figma, and use P3 only for vivid brand colors.

**Engineer:** $type color with colorSpace (such as oklch), components, optional alpha and a hex fallback. Figma imports sRGB and HSL only, so an OKLCH master also exports sRGB.

</details>

### Dimension units

What unit sizes are saved in, like pixels, and how they change for each kind of screen.  
Designers: units: px, pt, dp, rem · Code: `$type dimension {value, unit}`

<details><summary>Designer and engineer</summary>

**Designer:** Which unit sizes are stored in, and how they become pt on iOS, dp on Android, epx on Windows and rem on the web. Storing px keeps Figma import lossless.

**Engineer:** $type dimension {value: 16, unit: "px"}; DTCG allows only px and rem. OpenDesigner exports px 1:1 as pt and dp, and CSS font sizes as rem.

</details>

### Builder extension types

Extra things the shared file has no slot for, like bouncy motion or very bright colors, kept in side notes.  
Designers: values beyond the standard format · Code: `$extensions.opendesigner, state.json`

<details><summary>Designer and engineer</summary>

**Designer:** Values the standard format cannot hold: springs, text and yes-or-no values, icon and font references, aspect ratios and rules. OpenDesigner keeps builder settings like preset in state.json.

**Engineer:** Today $extensions.opendesigner holds springs, P3 values, provenance and evidence; builder settings (preset, macros) live in state.json and opendesigner.meta.json. String and boolean extensions are not generated.

</details>

### Layout and breakpoint encoding

How screen widths and column grids are saved, so the layout changes as the screen grows.  
Designers: breakpoints, grids and layout guides · Code: `layout.grid.columns (proposed), layout.gutter (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How breakpoints, grids and layout guides are stored. Research default: a three-mode breakpoint collection driving spacing and guides, plus grid auto layout. OpenDesigner does not generate breakpoints yet.

**Engineer:** No DTCG breakpoint type. Not generated: layout.grid.columns (proposed; 4, 8 or 12), layout.gutter (proposed), layout.margin (proposed). Figma grid auto layout maps to CSS grid.

</details>

### Motion encoding

How the speed and feel of movement on screen is saved, like how long a slide takes.  
Designers: durations, easings and springs · Code: `motion.duration.short, cubicBezier, transition`

<details><summary>Designer and engineer</summary>

**Designer:** How durations, easings and springs are stored. OpenDesigner emits eight durations and four easings, mirrored as Figma timing and easing variables with a reduced-motion mode. Research suggests 3-5 durations.

**Engineer:** DTCG duration, cubicBezier and transition, such as motion.duration.short = {value: 150, unit: "ms"}; springs stay in $extensions until DTCG adds a type.

</details>

### Shadow, border and elevation encoding

How shadows and outlines are saved so both design tools and code draw them the same.  
Designers: effect styles and strokes · Code: `elevation.* shadow arrays, border.width.*`

<details><summary>Designer and engineer</summary>

**Designer:** How shadows, borders and elevation are stored so design and code match. Figma effect styles bind color and offset to variables, so dark mode can swap the shadow color.

**Engineer:** elevation.floating is a DTCG shadow array of ring, key and ambient layers. Borders are border.width.* dimensions, not border or strokeStyle composites. Android and iOS shadows need custom transforms.

**Also called:** elevation tokens

</details>

### Typography encoding

How text settings like font, size and weight are saved: as one bundle, as single parts, or both.  
Designers: text styles bound to variables · Code: `text.body.md typography composite`

<details><summary>Designer and engineer</summary>

**Designer:** Whether type is stored as bundled styles, separate values, or both. Default both: atomic font values plus role-based composites, mirrored in Figma as text styles bound to variables.

**Engineer:** Atomic fontFamily, fontWeight and dimension tokens (line heights in px) plus composites like text.body.md. Figma lacks composite variables, so composites become text styles bound to variables.

</details>

## Components

### Components

The parts an app is made of, like buttons and menus, built once and used again.  
Designers: components: anatomy, variants, states · Code: `catalog C01-C64`

<details><summary>Designer and engineer</summary>

**Designer:** Reusable UI elements with defined anatomy, variants and states, styled from the system's tokens. OpenDesigner's catalog lists 64 canonical components in ten categories, benchmarked across 10 systems.

**Engineer:** Catalog entries C01-C64 list anatomy, props, states, the APG pattern and token families used. No component tokens are generated yet; components use semantic tokens directly.

**Example:** A Button, a Dialog and a Card are three components.

**Also called:** UI components, building blocks

</details>

### Action components

Parts you tap or click to make something happen, like buttons.  
Designers: buttons and action components · Code: `APG Button, Menu Button, Toolbar`

<details><summary>Designer and engineer</summary>

**Designer:** Components that trigger actions: button, icon button, floating action button, split button, button group, toggle button and toolbar. Their emphasis and placement signal what users should do next.

**Engineer:** APG patterns: Button (Enter and Space activate), toggle Button with aria-pressed, Menu Button with aria-haspopup, and Toolbar with a roving tabindex. Natives: SwiftUI Button, UIKit UIButton, Compose Button.

**Example:** Save, Share and a plus button that adds an item.

**Also called:** buttons

</details>

### Button hierarchy, content and destructive treatment

How many kinds of button there are, which one stands out, and how a Delete button looks.  
Designers: button hierarchy: primary to danger · Code: `color.bg.action.primary, color.bg.danger.bold`

<details><summary>Designer and engineer</summary>

**Designer:** Four emphasis levels plus danger, one primary per view, placed after the last field. Sentence-case verb labels with an optional leading icon; solid danger only in the confirmation step.

**Engineer:** Semantic tokens color.bg.action.primary with color.text.onAction, and color.bg.danger.bold for destructive; button component tokens are not generated yet. APG Button; SwiftUI destructive role.

**Example:** One filled Save button beside a plain-text Cancel button.

**Also called:** button variants, primary button, danger button

</details>

### Component API (code and Figma)

The switches and knobs on a part, like size or style, that people use to set it up.  
Designers: variants, booleans, slots, instance swap · Code: `props, compound parts like Menu.Item`

<details><summary>Designer and engineer</summary>

**Designer:** How a component is configured in Figma: variants for state, size and type, booleans for optional icons, text properties for labels, instance swap for fixed icons, slots for flexible content.

**Engineer:** Props for leaf components like Button; compound parts (Menu.Trigger, Menu.Item) for containers like Dialog. Figma slots map to React children, and booleans bind only to layer visibility.

**Example:** A Button with a size setting and an optional icon.

**Also called:** props, component properties, configuration vs composition

</details>

### Microinteraction specification

A short write-up of what starts a small action, what it does, and what you see or feel.  
Designers: microinteraction spec: trigger, rules, feedback · Code: `component state machine`

<details><summary>Designer and engineer</summary>

**Designer:** Each interactive component documents Saffer's four parts: trigger, rules, feedback, and loops and modes, plus its state list. This keeps press, hover, success and failure feedback consistent across the product.

**Engineer:** Implement the spec as a state machine, as Ark UI does; store trigger, rules, feedback, loops and modes as structured component docs. DTCG has no behavior type.

**Example:** Pull to refresh: the pull is the trigger, the spinner is the feedback.

**Also called:** microinteractions, behavior spec

</details>

### Containment components

Parts that group things, like cards, sections that open and close, and dividing lines.  
Designers: cards, accordions, dividers, carousels · Code: `APG Accordion, Disclosure, Carousel`

<details><summary>Designer and engineer</summary>

**Designer:** Components that group content: card, accordion, divider and carousel. They set how content chunks read, whether by fill, outline or shadow, and how much stays hidden until opened.

**Engineer:** APG Accordion (a heading wrapping a button with aria-expanded and aria-controls), Disclosure, and Carousel (rotation stop control first in tab order). Natives: SwiftUI DisclosureGroup; Compose Card, ElevatedCard, OutlinedCard.

**Example:** A help page where each question opens to show its answer.

**Also called:** containers

</details>

### Card and panel separation

How a card stands apart from the page: a light fill, a thin border, or a shadow.  
Designers: fill, outline or shadow card · Code: `color.surface.raised, color.border.subtle, elevation.raised`

<details><summary>Designer and engineer</summary>

**Designer:** Tinted fill feels soft and works in dark mode, outline feels crisp and flat, shadow adds depth. Use fill or outline for static cards, elevation only for floating things.

**Engineer:** Tokens: color.surface.raised, color.border.subtle, radius.container and elevation.raised. Interactive cards bounded only by a border need 3:1 contrast (WCAG 1.4.11).

**Example:** Cards on a pale gray page, each with a thin outline.

**Also called:** card style, container separation

</details>

### Data display components

Parts that show facts and people, like lists, tables and small photos of users.  
Designers: lists, tables and avatars · Code: `APG Table, Grid, Treegrid, Listbox`

<details><summary>Designer and engineer</summary>

**Designer:** Components that present data and people: list, table, avatar, and text and heading. Density, row height and type roles decide how scannable a screen of data feels.

**Engineer:** APG Table for static data, Grid for interactive or editable cells, Treegrid for nested rows, Listbox for selectable lists. Natives: SwiftUI List and Table, UIKit UITableView.

**Example:** A table of orders with a small photo of each customer.

**Also called:** data components

</details>

### Avatars

A small picture or letters that stand for a person, team or AI helper.  
Designers: circle for people, square for teams · Code: `radius.person, avatar.size.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Sizes from 16 to 64 on a 4/8 rhythm. Circle means person, square means team or organization, and a third shape marks AI agents when humans and AI mix.

**Engineer:** radius.person aliases radius.full (9999px); avatar sizes 16 to 64, avatar.size.* (proposed), are not generated yet. Add alt text when no name sits beside it.

**Example:** A round photo for a person, a square logo for a team.

**Also called:** profile picture, user image

</details>

### Device variants of components

If one set of parts fits phones and laptops, or if watches and TVs get their own.  
Designers: one component set, context modes · Code: `context modifier (proposed), color.bg.action.primary`

<details><summary>Designer and engineer</summary>

**Designer:** One component set covers phone, tablet, desktop and web through context modes; watch and TV get small separate libraries because their input changes, not only their size.

**Engineer:** Not generated yet: a context modifier so shared names like color.bg.action.primary resolve per device, and namespaces like wrist.tile.* (proposed) for device-only parts. Car uses system templates.

**Example:** Google ships separate Compose libraries for Wear and TV.

**Also called:** context modes, per-device libraries

</details>

### Feedback components

Parts that tell you what is going on, like a warning box, a loading bar or a red dot.  
Designers: alerts, toasts, progress, empty states · Code: `color.bg.danger.subtle, role=alert`

<details><summary>Designer and engineer</summary>

**Designer:** Components that report status, progress or results: alert or banner, toast, progress bar, spinner, skeleton, empty state, badge and AI indicators. Four status colors map info, success, warning and error.

**Engineer:** APG Alert (role alert, no focus move); toasts use a status live region on color.bg.inverse. Status: color.bg.danger.subtle, color.text.danger, likewise info, success, warning.

**Example:** A green banner saying your changes were saved.

**Also called:** status components, notifications

</details>

### AI surfaces module

Extra parts for AI features, like a label that says AI made this, and chat bubbles.  
Designers: AI label and AI accent · Code: `color.ai.* (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** An optional module: AI label and AI button variant first, chat components only for conversational products. A distinct AI accent aids recognition but can compete with the primary color.

**Engineer:** Not generated yet: color.ai.* (proposed) accent or gradient tokens. Examples: Carbon AI label, Spectrum 2 genai variant, shadcn Message. Stream text into polite live regions.

**Example:** A small AI tag next to a summary the app wrote.

**Also called:** AI components, AI label

</details>

### Build strategy and technology

Picking what the parts are built on: a kit with no looks, a kit with looks, or the phone's own.  
Designers: headless, styled or native base · Code: `shadcn/ui, Base UI, React Aria`

<details><summary>Designer and engineer</summary>

**Designer:** Picks the base under your components. Headless libraries leave every visual choice to your tokens, styled libraries arrive with a look to re-theme, and native controls inherit the platform's look.

**Engineer:** Suggested for React web: shadcn/ui on Base UI or React Aria; multi-framework: Ark UI or web components; mobile: SwiftUI and Compose controls themed with tokens. Recorded in components.base.

**Example:** A React app styling shadcn/ui components with its own tokens.

**Also called:** headless vs styled, web components vs framework components

</details>

### Input components

Parts where you type or pick something, like a text box, a date picker or a file upload.  
Designers: form inputs and text fields · Code: `aria-describedby, aria-invalid, APG Combobox`

<details><summary>Designer and engineer</summary>

**Designer:** Components for entering data, from text fields and selects to date pickers, file uploads and one-time codes. Field style, label placement and validation decide how easy forms feel.

**Engineer:** Native inputs plus aria-describedby for help and errors and aria-invalid; APG Combobox for suggestions, Listbox or select-only Combobox for Select, Spinbutton for number fields. Compose TextField, SwiftUI TextField.

**Example:** An email box, a country dropdown and a birthday picker.

**Also called:** form controls, text inputs

</details>

### Form field style and label placement

How a text box looks, with a full border, a shaded fill or a line, and where its name sits.  
Designers: outlined field, top label · Code: `color.border.input, text.label.md`

<details><summary>Designer and engineer</summary>

**Designer:** Outlined reads crisp, filled reads soft and app-like, underlined is minimal but low in affordance. Default: outlined fields with top labels; mark whichever of required or optional is rarer.

**Engineer:** Tokens: color.border.input (3:1), color.border.focus, color.border.danger, text.label.* for labels; input component tokens are not generated yet. Every input needs a programmatic label.

**Example:** A box with a border and its label, Email, sitting above it.

**Also called:** text field style, label position

</details>

### Component inventory scope

Choosing which parts to make first, and when to add more later.  
Designers: core set of about 25 components · Code: `button.* (proposed), APG pattern`

<details><summary>Designer and engineer</summary>

**Designer:** Version 1's library size. The default is about 25 core components (the engine starts with 22); extended ones, such as date pickers, come when two or more products ask.

**Engineer:** The list lives in components.inventory in state.json; each included component must implement its APG pattern. Per-component token namespaces such as button.* (proposed) are not generated yet.

**Example:** Buttons and checkboxes in version 1; a color picker later.

**Also called:** component scope, core and extended components

</details>

### Layout primitives and utilities

Hidden helper parts that space things out and help people who have the screen read aloud.  
Designers: box, stack and grid primitives · Code: `Box, Stack, Inline, Grid`

<details><summary>Designer and engineer</summary>

**Designer:** Box, stack and grid primitives expose spacing, color and radius as props so layouts stay on scale. The app shell and accessibility utilities, like visually hidden text, sit here too.

**Engineer:** Box, Stack, Inline and Grid take spacing tokens as props; the app shell uses APG Landmarks and Window Splitter; utilities include Radix Visually Hidden, Portal and Slot.

**Example:** A Stack that puts the same gap between every card.

**Also called:** layout primitives, Box and Stack, accessibility utilities

</details>

### Media components

Parts that show icons and pictures at the right size and shape.  
Designers: icons and images on system scales · Code: `C60 Icon, C61 Image`

<details><summary>Designer and engineer</summary>

**Designer:** Components that render icons and images, such as thumbnails. They keep icon sizes, image corners and aspect ratios on the system's scales instead of hand-set values.

**Engineer:** C60 Icon consumes icon size, stroke and color tokens; C61 Image consumes radius and surface tokens plus CSS aspect-ratio. Radix ships Accessible Icon and Aspect Ratio.

**Example:** A trash-can icon and a square product photo.

**Also called:** icons and images

</details>

### Navigation components

Parts that help you move around an app, like tabs, links and a bar of icons at the bottom.  
Designers: tabs, breadcrumbs, nav bar, sidebar · Code: `nav landmark with aria-current`

<details><summary>Designer and engineer</summary>

**Designer:** Components for moving between places: link, tabs, breadcrumbs, pagination, bottom navigation bar, navigation rail, sidebar, app bar, tree view and steps. The container follows screen size and destination count.

**Engineer:** Use links inside a nav landmark with aria-current, never the menu role. APG patterns: Tabs (tablist, tab, tabpanel), Breadcrumb, Tree View. Natives: SwiftUI TabView and NavigationSplitView, Compose NavigationBar and NavigationRail.

**Example:** Home, Search and Profile tabs along the bottom of a phone app.

**Also called:** nav components, wayfinding

</details>

### Overlay components

Parts that pop up over the page, like tips, menus and boxes that ask you something.  
Designers: dialogs, popovers, sheets, menus · Code: `APG Dialog (Modal), aria-modal`

<details><summary>Designer and engineer</summary>

**Designer:** Components that appear above the page: tooltip, popover, dialog, confirmation dialog, sheet or drawer, menu and command palette. Use modal ones only when blocking the page has a clear benefit.

**Engineer:** APG Dialog (Modal): focus moves inside and is trapped, Escape closes, focus returns to the invoker, with role dialog and aria-modal. Also Alert Dialog, Menu Button and Tooltip.

**Example:** A box asking Delete this file? with Delete and Cancel buttons.

**Also called:** popups, modals

</details>

### System controls versus custom controls

Whether an app uses the phone's own buttons in its brand color, or draws its own.  
Designers: system or custom controls · Code: `SwiftUI, UIKit and Compose controls`

<details><summary>Designer and engineer</summary>

**Designer:** System controls feel native and update with the OS, such as Liquid Glass; custom ones keep brand shape but can look out of place. Restyle color and label, not shape.

**Engineer:** Default: tint SwiftUI, UIKit and Compose controls with the accent token, custom controls on web. System controls carry VoiceOver and TalkBack roles; custom ones must supply them.

**Example:** An iOS toggle switch tinted in the brand's green.

**Also called:** native controls, custom-drawn controls

</details>

### Selection components

Parts for making a choice, like check boxes, on-off switches and sliders.  
Designers: checkbox, radio, switch, slider, chip · Code: `APG Checkbox, Radio Group, Switch, Slider`

<details><summary>Designer and engineer</summary>

**Designer:** Components for choosing among options: checkbox, radio group, switch, slider, segmented control and chip. Pick by task: switches apply instantly, radios pick one, checkboxes pick many, chips filter.

**Engineer:** APG Checkbox (aria-checked true, false or mixed), Radio Group (arrow keys move and select), Switch (role switch) and Slider (aria-valuenow). Natives: SwiftUI Toggle and Slider, Compose Checkbox, Switch, RadioButton.

**Example:** A switch that turns dark mode on or off.

**Also called:** choice controls

</details>

### Interaction states

How a part looks when you point at it, press it, pick it, or it cannot be used.  
Designers: hover, focus, pressed, selected, disabled · Code: `color.bg.action.primaryHover`

<details><summary>Designer and engineer</summary>

**Designer:** Each component's looks: enabled, hover, focus-visible, pressed, selected, disabled, loading, error. Hover and press step one or two shades along the ramp; selected and error get explicit colors.

**Engineer:** DTCG has no state semantics; states become a name suffix such as color.bg.action.primaryHover or .primaryPressed. Define all states once; each context renders the subset its inputs trigger.

**Example:** A button shows a ring around it when reached with the Tab key.

**Also called:** component states, hover, focus, pressed

</details>

### Disabled and unavailable actions

What to do with a button that cannot work right now: fade it, hide it, or explain why.  
Designers: disabled or unavailable state · Code: `aria-disabled`

<details><summary>Designer and engineer</summary>

**Designer:** Faded controls signal 'not now' but can hide why. The default never disables submit: it checks fields on blur, summarizes errors on submit, and explains when an action cannot run.

**Engineer:** Use aria-disabled, as APG recommends; it stays focusable, while disabled controls leave the tab order. Tokens: color.text.disabled, or opacity.disabled.content and .container. WCAG exempts them from contrast.

**Example:** A Save button that stays clickable and says what is missing.

**Also called:** disabled state, inactive state

</details>

### Loading state

How a part shows it is busy, like a spinning wheel or gray boxes where things will load.  
Designers: spinner, skeleton or loading button · Code: `loading.delay (proposed) = 1000ms`

<details><summary>Designer and engineer</summary>

**Designer:** Choose a spinner, a skeleton that previews the layout, or a loading button. Delay spinners about 1 s, use skeletons for first page loads, and keep loading buttons focusable.

**Engineer:** A delay token such as loading.delay (proposed) = 1000ms (DTCG duration); announce state through a 4.1.3 status message. Natives: UIKit UIActivityIndicatorView, Compose LoadingIndicator. S2 isPending keeps focus.

**Example:** A Save button showing a small spinner while it saves.

**Also called:** busy state, pending state

</details>

### Selected and active state

How the app shows which tab, row or item you picked, using a mark as well as a color.  
Designers: selected indicator plus color · Code: `aria-selected, aria-current, aria-pressed`

<details><summary>Designer and engineer</summary>

**Designer:** Mark the chosen tab, row, chip or navigation item with an indicator plus color, never color alone. In action-dense products, save brand primary for actions.

**Engineer:** Expose aria-selected, aria-current or aria-pressed per pattern. Tokens: color.bg.accent.subtle, color.text.accent and border.width.selected; the indicator needs 3:1 contrast where it conveys state.

**Example:** A pill shape behind the icon of the current tab.

**Also called:** active state, current item

</details>

### Hierarchy model and naming

How the parts are sorted from smallest to biggest, and what each one is called.  
Designers: atomic design levels and naming · Code: `comp.button (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The five levels: tokens, primitives, components, patterns and templates, with Brad Frost's atomic names kept as aliases. An alias table resolves collisions, such as Tag meaning chip in Carbon.

**Engineer:** Not a token; the chosen level and component names would become token path segments such as comp.button (proposed). Each catalog entry's Names line feeds the cross-system alias table.

**Example:** A Tag in one system is called a Chip in another.

**Also called:** atomic design, component taxonomy

</details>

## Patterns and templates

### Patterns and templates

Common ways to join parts to do a job, like a sign-up form, plus whole pages.  
Designers: UX patterns and page templates · Code: `planned lint rules (spec 6.4)`

<details><summary>Designer and engineer</summary>

**Designer:** Recurring solutions that combine components around a user goal: forms, feedback, navigation, disclosure, empty states, plus page templates and layout archetypes. Most UX behavior rules apply here.

**Engineer:** No DTCG type exists for patterns; they compose components and reference tokens. Behavior-rule lint, such as a dialog with no dismiss path, is planned (spec 6.4, 7.12), not built.

**Example:** A sign-up form: fields, labels, a button and error messages together.

**Also called:** UX patterns, page templates

</details>

### AI and conversational patterns

Rules for AI tools: say what AI made, show where facts come from, and let people fix it.  
Designers: AI labels, citations, edit and retry · Code: `color.ai.* (proposed), icon.ai (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Label AI content, place distinctly styled citations next to claims, express uncertainty, and pair every generated result with Edit, Undo and Retry. Never autoscroll streamed answers.

**Engineer:** Not generated yet: color.ai.* (proposed) or an AI accent role, and an icon.ai (proposed) glyph; streaming reuses motion tokens. Announce streamed text at completion or in chunks.

**Example:** A chat answer with numbered sources and a Retry button.

**Also called:** generative AI patterns, chat patterns

</details>

### Long collections

How a long list is split up: page numbers, a Load more button, or scrolling that never ends.  
Designers: pagination, load more, infinite scroll · Code: `APG Feed pattern`

<details><summary>Designer and engineer</summary>

**Designer:** Pagination for tables and goal-directed search, Load more for result lists, infinite scroll only for feeds. Infinite scroll hides the footer and makes items hard to find again.

**Engineer:** No new tokens; pagination reuses button and link tokens. Infinite scroll harms keyboard and footer access, so accessible feeds follow the APG Feed pattern.

**Example:** Search results with page numbers; a social feed that keeps scrolling.

**Also called:** pagination vs infinite scroll, load more

</details>

### Destructive actions: undo versus confirm

If a delete can be taken back with Undo, or if the app asks you first.  
Designers: undo versus confirm · Code: `APG Alert Dialog`

<details><summary>Designer and engineer</summary>

**Designer:** Reversible actions get undo and no confirmation; irreversible or costly ones get a dialog with verb labels like Delete file, and Cancel as the safe default. Overused confirmations breed habituation.

**Engineer:** APG Alert Dialog (role alertdialog), focus returned to the invoker. Undo toast timing is a DTCG duration and must be pausable. Planned warning: delete with neither undo nor confirm.

**Example:** Deleting an email shows Undo; deleting an account asks first.

**Also called:** undo vs confirm, delete confirmation

</details>

### Progressive disclosure

Keeping extra choices out of sight until you need them, so the screen stays clean.  
Designers: progressive disclosure, two levels max · Code: `aria-expanded, aria-controls`

<details><summary>Designer and engineer</summary>

**Designer:** Show key options first and put advanced ones behind a labeled trigger, like More options. Use at most two levels, and never hide anything essential behind hover.

**Engineer:** Triggers expose expanded or collapsed state through APG Accordion or Disclosure (aria-expanded, aria-controls). Components: accordion, toggletip, popover, sheet, tabs, steps for staged disclosure. No token; it is a pattern rule.

**Example:** An Advanced settings link that opens more choices.

**Also called:** show more, advanced options

</details>

### Empty states

What a screen shows when there is nothing in it yet, and what you can do next.  
Designers: empty states: first use, no results · Code: `Primer Blankslate, shadcn Empty`

<details><summary>Designer and engineer</summary>

**Designer:** Cover first use, user-cleared and no-results cases. Each communicates status, teaches the feature, and offers a direct next step with a call to action. Loading is not an empty state.

**Engineer:** Reuses spacing and type tokens plus illustration assets. Status must be real text, not only an image. Lint for a missing empty variant: proposed, not built. Example: Primer Blankslate.

**Example:** No projects yet, with a Create project button.

**Also called:** blank slate, zero state

</details>

### Feedback patterns

How an app tells you it is busy, that it worked, or that it went wrong.  
Designers: loading, messages and errors · Code: `aria-live regions`

<details><summary>Designer and engineer</summary>

**Designer:** How the system reports waiting, results and errors: the loading ladder, the choice of message channel, and the error message pattern. They implement the heuristic of visible status and feedback.

**Engineer:** Composes alerts, toasts, progress bars, spinners, skeletons and empty states. Announce changes through live regions (WCAG 4.1.3) without stealing focus. Duration threshold tokens are not generated yet.

**Example:** A spinner while saving, then a Saved message.

**Also called:** system status, status feedback

</details>

### Error messages

Telling people what went wrong and how to fix it, in plain words, right next to the problem.  
Designers: what happened, then how to fix · Code: `color.text.danger, color.border.danger`

<details><summary>Designer and engineer</summary>

**Designer:** Follow NN/g's 13 guidelines: shown near the source, visible without relying on color, precise, constructive and blame-free, input kept. Template: what happened, then how to fix it.

**Engineer:** Tokens: color.text.danger, color.bg.danger.subtle, color.border.danger; a status icon glyph is not generated. Message template {problem}{cause?}{remedy}. Planned lint: color-only error state (spec 6.4).

**Example:** That email is already in use. Sign in instead?

**Also called:** error copy, error states

</details>

### Loading and wait feedback

What the app shows while you wait: nothing for a blink, a filling bar for a long wait.  
Designers: loading ladder: skeleton, then progress · Code: `feedback.indicator.delay (proposed), aria-busy`

<details><summary>Designer and engineer</summary>

**Designer:** Acknowledge within 50 ms, show nothing under about 1 s, use a skeleton for 1 to 10 s page loads, and past 10 s show determinate progress with cancel.

**Engineer:** Not generated yet: DTCG duration tokens feedback.acknowledge.max (proposed) = 50ms and feedback.indicator.delay (proposed) = 1000ms. Pair aria-busy with a polite live region; indicators carry text labels.

**Example:** A page shows gray outlines of its content while it loads.

**Also called:** response-time ladder, wait feedback

</details>

### Message channel selection

Choosing where a message shows up: beside the cause, in a bar up top, or in a quick pop-up.  
Designers: inline, banner, toast or dialog · Code: `color.bg.<status>.subtle, color.text.<status>`

<details><summary>Designer and engineer</summary>

**Designer:** Put the message where the cause is, inline or in a banner by default. Toasts only for low-stakes confirmations with undo; Primer ships none. Dialogs only for blocking decisions.

**Engineer:** Four status roles, such as color.bg.danger.subtle and color.text.danger. Use live regions (WCAG 4.1.3) without moving focus; never auto-dismiss a toast holding an action.

**Example:** A Deleted, Undo toast after removing an email.

**Also called:** notification channel, toast vs banner

</details>

### Forms and field anatomy

How a form is set up: a name above each box, a tip, and a star on must-fill boxes.  
Designers: labels above fields, hints below · Code: `autocomplete, space.stack.*`

<details><summary>Designer and engineer</summary>

**Designer:** A visible label above every field, a hint below it, an asterisk at the label start with a legend, and autofill on standard inputs. Placeholder-only labels are a planned warning.

**Engineer:** Set autocomplete on personal-data inputs and expose required state to assistive tech, not only an asterisk. Unlabeled fields are a planned lint error. Label gap: a space.stack.* step.

**Example:** Email, with a star and the hint We never share it.

**Also called:** form layout, field labels

</details>

### Validation timing and error presentation

When a form checks your answers and where it shows mistakes: by each box, at the top, or both.  
Designers: inline validation and error summary · Code: `validateOn: blur | submit | change`

<details><summary>Designer and engineer</summary>

**Designer:** Sources disagree: one validates on submit, the other on blur. Both reject flagging errors mid-typing. Forms over about 5 fields show an error summary plus inline messages.

**Engineer:** A prop validateOn: blur | submit | change, with revalidateOn: change. Errors identified in text and linked to fields (WCAG 3.3.1); focus the summary on submit. GOV.UK sets novalidate.

**Example:** A phone number is checked when you leave the box, not while typing.

**Also called:** inline validation, error summary

</details>

### Glanceable surfaces

Tiny views you read in a blink without opening the app, like a watch face.  
Designers: widgets, complications, tiles, Live Activities · Code: `type.numeral.lg (proposed), ambient mode`

<details><summary>Designer and engineer</summary>

**Designer:** Widgets, complications, tiles, notifications and Live Activities. Design the complication or tile first, then the app, with one number or one status per surface. Always On dims them.

**Engineer:** Not generated yet: numeral type styles such as type.numeral.lg (proposed), compact spacing and an ambient mode that dims secondary content. Content descriptions must match exactly what is shown.

**Example:** A watch face showing the next meeting time.

**Also called:** widgets, complications and tiles

</details>

### Layout archetypes

Screen shapes many apps share, like a list on the left and details on the right.  
Designers: layout archetypes: list-detail, feed, shell · Code: `NavigationSplitView, Compose canonical scaffolds`

<details><summary>Designer and engineer</summary>

**Designer:** Named screen structures that recur across products: canonical pane layouts such as list-detail, supporting pane and feed, and the app shell that holds navigation, header and content.

**Engineer:** Compose ships canonical layout scaffolds; SwiftUI has NavigationSplitView and UIKit UISplitViewController. Pane and rail width tokens are not generated yet. Landmarks follow pane order.

**Example:** An email app: folder list, message list and open message.

**Also called:** screen archetypes

</details>

### Canonical layouts and panes

Ways to split a screen into one, two or three parts side by side, based on how wide it is.  
Designers: list-detail, supporting pane, feed · Code: `layout.pane.supporting.ratio (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Material's list-detail, supporting pane and feed layouts. One pane below 840dp, two from 840dp, three only at 1600dp and up, with the supporting pane about a third.

**Engineer:** Not generated yet: layout.pane.fixed.expanded (proposed) = 360 (dp; exported as px), layout.pane.fixed.large (proposed) = 412, layout.pane.supporting.ratio (proposed) = 0.333, a DTCG number.

**Example:** On a tablet, the inbox list and the open email side by side.

**Also called:** list-detail, supporting pane, multi-pane layout

</details>

### App shell regions

The parts of an app that stay put, like the menu and top bar, while the main content changes.  
Designers: app shell: nav, header, content · Code: `layout.sidebar.width (proposed), layout.header.height (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The persistent regions: navigation, header, content and supporting areas. Compact screens use a bottom bar with 3 to 5 destinations, medium a collapsed rail, expanded a rail or sidebar.

**Engineer:** Not generated yet: layout.rail.width.collapsed (proposed), layout.sidebar.width (proposed), layout.header.height (proposed), DTCG dimensions. Swap only functionally equivalent components. Examples: Carbon UI shell, SwiftUI NavigationSplitView.

**Example:** A sidebar and header that stay while pages change in the middle.

**Also called:** app frame, UI shell

</details>

### Transitions and choreography

How the screen moves as you go to the next one, and the order things show up in.  
Designers: container transform, shared axis, fade through · Code: `motion.transition.*`

<details><summary>Designer and engineer</summary>

**Designer:** Fade, fade through, shared axis and container transform, which visibly links an element to what it opens. Stagger items 20 to 50 ms apart, at most 500 ms total.

**Engineer:** Transitions are named by role as DTCG transition composites: motion.transition.feedback, enter, exit, move, expand. No named patterns or stagger tokens exist; reduced motion swaps movement for a fade.

**Example:** A card grows into the detail page when you tap it.

**Also called:** page transitions, stagger

</details>

### Global navigation

How an app's main menu works: how many places, how deep it goes, and if it stays in view.  
Designers: global navigation, always visible · Code: `nav.visibleItems.compact (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Keep primary navigation visible whenever width allows. Do not cap items at seven, a misuse of Miller's law; group long lists and test labels with a tree test.

**Engineer:** A pattern setting rather than a token, such as nav.visibleItems.compact (proposed) = 5, not generated yet. Expose the nav landmark and aria-current; keep placement consistent (WCAG 3.2.3).

**Example:** Five tabs that stay visible at the bottom of a phone app.

**Also called:** information architecture, primary navigation

</details>

### Navigation containers by size, platform and device

The same places to go, shown as a bottom bar on phones and a side list on laptops.  
Designers: bottom bar, rail or sidebar · Code: `nav.bar.height (proposed), NavigationRail`

<details><summary>Designer and engineer</summary>

**Designer:** 3 to 5 destinations: bottom bar on phone, rail on tablet, sidebar on desktop; more than 7 go in a grouped sidebar. Keep destinations identical and swap only the container.

**Engineer:** A rule table from context and breakpoint to container; tokens like nav.bar.height (proposed) and nav.rail.width.collapsed (proposed) are not generated yet. Natives: SwiftUI sidebarAdaptable, Compose NavigationRail.

**Example:** Tabs on the phone become a sidebar on the iPad.

**Also called:** adaptive navigation, navigation bar, rail and sidebar

</details>

### Onboarding

How new people learn an app: tips when they need them, not a tour they must sit through.  
Designers: skippable, contextual onboarding · Code: `Tooltip or Popover coachmarks`

<details><summary>Designer and engineer</summary>

**Designer:** No forced tour. Use contextual help and empty states that teach, and make everything skippable. Deck-of-cards tutorials make the interface look more complicated than it is.

**Engineer:** No tokens. Coachmarks reuse Tooltip or Popover and need dialog-style focus management, keyboard access and a dismiss control. Lint for a tour with no skip control: proposed, not built.

**Example:** A tip that appears the first time you open the editor.

**Also called:** first-run experience, product tour

</details>

### Other product patterns

More jobs apps often need, like search, filters, signing in, big tables and settings.  
Designers: search, filters, sign-in, settings · Code: `Search field, Combobox, Chips, Sheet`

<details><summary>Designer and engineer</summary>

**Designer:** Search and filtering, authentication, data tables and settings, catalogued without their own Decision Card. Their choices come from the components involved and the forms, collections and feedback patterns.

**Engineer:** Examples: filters compose Search field, Combobox, Chips and Sheet; sign-in allows paste and password managers (WCAG 3.3.8); interactive tables use APG Grid, static ones Table.

**Example:** A sign-in screen that lets a password manager fill the password.

**Also called:** search and filtering, authentication, settings

</details>

### Modality and overlays

Which pop-up to use: a center box, a panel that slides in, or a small box next to a button.  
Designers: dialog, sheet or popover choice · Code: `APG Dialog (Modal), UISheetPresentationController`

<details><summary>Designer and engineer</summary>

**Designer:** Dialog for short decisions, side sheet for editing with context, bottom sheet on phones, popover for small scoped tasks. Follow each platform's button order, and always give a way out.

**Engineer:** APG Dialog (Modal): focus trapped and returned, Escape closes, aria-modal. iOS sheets use detents and a grabber (UISheetPresentationController). A dialog with no dismiss path is a planned lint error.

**Example:** A bottom sheet with share options on a phone.

**Also called:** modals, dialogs and sheets

</details>

### Page templates

Whole pages to start from, like a dashboard, a list page, a detail page or a settings page.  
Designers: page templates: dashboard, detail, settings · Code: `Primer PageLayout, Polaris Page`

<details><summary>Designer and engineer</summary>

**Designer:** Whole-page starting points assembled from shell, components and patterns: dashboard, list or index, detail, settings, and marketing or landing page. Detail pages use a supporting pane of about one third.

**Engineer:** Product systems ship the shell as components: Primer PageLayout, Carbon UI shell and Polaris Page; marketing templates mostly live outside them. A reference site's page structure can be extracted.

**Example:** A dashboard with a sidebar, a header and a grid of cards.

**Also called:** page layouts, starter pages

</details>

## Guardrails and validation

### Guardrails and validation

The checks that keep work made by people and AI inside the rules.  
Designers: guardrails and design linting · Code: `engine.py validate, engine.py review`

<details><summary>Designer and engineer</summary>

**Designer:** The checks that keep human and agent work inside the rules: which rules run, where (editor, export, CI), how strict they are, and which device safety and accessibility tests apply.

**Engineer:** The enforcement layer for prin.ux.rules, visual principles and foundation constraints. Today engine.py validate checks tokens and engine.py review scans code; exported lint configs are planned.

**Also called:** guardrails, validation

</details>

### Check catalog

The full list of tests the tool runs, like checking text is easy to read on its background.  
Designers: contrast, target, label and limit checks · Code: `engine.py validate: contrast, targets, aliases, limits`

<details><summary>Designer and engineer</summary>

**Designer:** What engine.py validate checks: contrast pairs in every mode, target sizes, focus, reduced motion, hierarchy counts and Figma mode limits. Label, dismiss and deceptive-pattern checks are planned.

**Engineer:** validate resolves every alias without cycles, requires a $type, keeps modifiers orthogonal and warns past the Figma plan's mode cap. The Figma export warns above 5,000 variables.

</details>

### Visual critique strictness

How tough the tool is when it reviews your look: a gentle coach, a strict gate, or a score sheet.  
Designers: design critique: coach or strict · Code: `answers.Q-pref-01: coach | strict (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** How strongly the builder critiques visual choices: coaching by default; strict blocking and a metrics panel are planned. Every validate message names its rule, so users learn the vocabulary.

**Engineer:** Not tokens: answers.Q-pref-01 records silent, coach, strict or metrics, but nothing acts on it yet. validate reports errors; review --strict fails on hard-coded values or stale DESIGN.md.

</details>

### Rule enforcement and exported lint

How rules hold: you can only break one on purpose, and AI helpers must obey the same rules.  
Designers: same rules for people and agents · Code: `engine.py review, validate; lint/ (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Rules bind people and agents alike: raw values only through an explicit detach, agents limited to the same scopes as humans, and lint rules planned for every generated system.

**Engineer:** Planned: a lint/ folder with a stylelint strict-value config (spec 7.12). Today engine.py review flags hard-coded values and validate checks contrast; Figma export scopes semantic variables.

</details>

### Safety and distraction limits

Hard rules for places where a screen could put people at risk, like while they drive a car.  
Designers: safety and driver distraction limits · Code: `vehicle.animation (proposed); 76 px vehicle target`

<details><summary>Designer and engineer</summary>

**Designer:** Hard rules where a design can endanger people, such as driving or headsets. In a vehicle context they should be errors, not warnings; OpenDesigner enforces 76 px targets today.

**Engineer:** With car in raw.platforms or vehicle in raw.inputs, validate enforces a 76 px target. vehicle.animation (proposed) is planned; driving limits: 2 s glance, 12 s task.

</details>

### Accessibility test matrix by device

The smallest set of tests with helper tools, like screen readers, done on each kind of device.  
Designers: assistive tech test matrix · Code: `DESIGN.md Accessibility test matrix`

<details><summary>Designer and engineer</summary>

**Designer:** The minimum assistive-technology tests per shipped device class: one screen reader, one motor alternative and the largest text size. A first-class device means first-class assistive tech.

**Engineer:** Not tokens. DESIGN.md's Accessibility section lists the test matrix: keyboard, a screen reader per platform, 200% zoom, forced colors and reduced motion. Per-component checklists are planned.

</details>

## Delivery and tooling

### Delivery and tooling

How the finished design leaves the tool and stays in step with design apps and code.  
Designers: handoff and tooling · Code: `DTCG plus resolver, then platform code`

<details><summary>Designer and engineer</summary>

**Designer:** How the system leaves the builder and stays in sync: source of truth, interchange file, build pipeline, packaging, export channels, agent-readable outputs, and the round trip with design tools.

**Engineer:** Parent of the deliver.* nodes. engine.py generate turns state.json into DTCG 2025.10 plus a resolver; export turns that into CSS, Tailwind, Swift, Compose, Figma, Paper and DTCG.

</details>

### Agent-readable distribution

The files and links that let AI helpers read your design and follow it.  
Designers: AI-readable docs and MCP · Code: `DESIGN.md, AGENTS-snippet.md; MCP server (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** How AI agents read the system: MCP servers, llms.txt, DESIGN.md and Markdown twins of docs. Ship one live channel and one file channel, and test with evals.

**Engineer:** Today: DTCG files with $description text, DESIGN.md with a For Agents section, and an AGENTS.md snippet. An MCP server is planned (spec Phase 2).

**Also called:** agent-readable docs

</details>

### Export and handoff channels

The ways to send your design out of the tool, like copying code or sending it to a design app.  
Designers: exports: CSS, DTCG, native code, Figma · Code: `export --format all`

<details><summary>Designer and engineer</summary>

**Designer:** How a system leaves the tool. OpenDesigner writes export files and pushes to Figma or Paper through their MCP; a CLI URL and pull requests are not built.

**Engineer:** Today: DTCG (canonical), CSS custom properties, Tailwind v4 @theme, Swift, Compose, and Figma and Paper payloads. An MCP server is planned (spec Phase 2).

</details>

### Interchange format and file layout

The shared file type that tools use to pass your choices back and forth, and how it is split.  
Designers: token file format and layout · Code: `semantic.color.dark.tokens.json, resolver file`

<details><summary>Designer and engineer</summary>

**Designer:** The standard file format tokens travel in, and how the files split. Default: DTCG 2025.10, one file per tier and mode, which maps directly onto Figma's one-file-per-mode import.

**Engineer:** One file per tier and mode (semantic.color.dark.tokens.json), plus opendesigner.resolver.json with sets and modifiers. DTCG 2025.10 is stable but not a W3C Standard.

</details>

### Design-tool interop

How the tool sends your design to drawing apps like Figma and gets changes back.  
Designers: Figma and Paper as mirrors · Code: `use_figma MCP or DTCG per mode`

<details><summary>Designer and engineer</summary>

**Designer:** How the builder mirrors the system into design tools and captures changes back. No tool found does deterministic two-way token sync, so Figma and Paper are treated as mirrors.

**Engineer:** Figma: the remote MCP use_figma with a Full seat, else build/figma/import, one DTCG file per collection and mode. Paper: its local MCP. Penpot: imports the DTCG files.

</details>

### Figma

How your design shows up in Figma, an app where many people draw screens.  
Designers: Figma library: variables and styles · Code: `Figma variables; composites become styles`

<details><summary>Designer and engineer</summary>

**Designer:** How tokens and components appear in Figma: variable collections and modes, scopes and publishing, code syntax, styles versus variables, and Code Connect links to code.

**Engineer:** Figma imports color (sRGB, HSL), dimension (px), fontFamily, duration (s), number and a non-standard string. DTCG composites become styles, not variables.

</details>

### Code Connect and AI readiness

Links from each drawn part in Figma to the real code part, with notes that help AI helpers.  
Designers: Code Connect links to code · Code: `Code Connect, get_variable_defs, $description`

<details><summary>Designer and engineer</summary>

**Designer:** Links from Figma components to real code components, plus descriptions and examples Figma's AI tools read. Start with the top 20 components; describe every component and semantic variable.

**Engineer:** Code Connect needs an Organization or Enterprise plan. Descriptions go in $description; get_variable_defs returns variable names and values. The remote MCP needs a frame or layer link.

</details>

### Code syntax

The code name Figma shows next to each value, so designers and coders call it the same thing.  
Designers: code syntax in Dev Mode · Code: `codeSyntax {WEB, ANDROID, iOS}`

<details><summary>Designer and engineer</summary>

**Designer:** The code name Figma's Dev Mode shows beside each variable for Web, Android and iOS. It is the join key between canvas and code, so both sides use one name.

**Engineer:** REST codeSyntax {WEB, ANDROID, iOS}, from the CSS export's name transform: color/surface/base becomes var(--ds-color-surface-base), DS.Colors.surfaceBase on iOS. No Flutter or React Native slot.

</details>

### Styles versus variables

Which choices Figma keeps as one setting and which as a bundle, like a text style.  
Designers: variables for values, styles for bundles · Code: `text and effect styles, not variables`

<details><summary>Designer and engineer</summary>

**Designer:** Which values live as Figma variables and which as styles. Rule: variables for values, styles for bundles; any single value that changes by mode must be a variable.

**Engineer:** Colors, spacing, radius, sizes, opacity and motion become variables. OpenDesigner writes text styles bound to size, weight and family variables, and effect styles for elevation; no gradients or grids.

</details>

### Collections, modes, scopes and publishing

How Figma groups your saved choices, and hides the raw ones so no one picks them by mistake.  
Designers: variable collections, modes and scopes · Code: `hiddenFromPublishing, scopes like TEXT_FILL`

<details><summary>Designer and engineer</summary>

**Designer:** How tiers map to Figma collections and modes. Hide all primitives and scope each semantic variable to the properties its name says, so designers only see the right choices.

**Engineer:** Collections: Primitives (hidden), Color (Light, Dark), Density (Spacious, Comfortable, Compact), Motion (Standard, Reduced), Tokens. REST scopes such as TEXT_FILL; hiddenFromPublishing: true; 5,000 variables per collection.

</details>

### Paper

Paper is a design app made of web pages; it takes your colors, but light and dark need two sets.  
Designers: Paper canvas for specimens · Code: `Paper MCP write_html, create_tokens`

<details><summary>Designer and engineer</summary>

**Designer:** An HTML and CSS design canvas that agents can write to. Its tokens have no modes or libraries, so use it for specimens, not as the source of truth.

**Engineer:** A local MCP server with 34 tools, including write_html and create_tokens. Tokens are CSS variables with no modes or DTCG, so light and dark need separate sets.

</details>

### Penpot

Penpot is a free, open design app that can load and save the shared design file.  
Designers: open-source design tool, native DTCG · Code: `$themes.json and $metadata.json`

<details><summary>Designer and engineer</summary>

**Designer:** Penpot is an open-source design tool with multi-dimensional themes. It is the only tool the research found that imports and exports DTCG tokens natively.

**Engineer:** Native DTCG import and export, using $themes.json and $metadata.json alongside the token sets, with multi-dimensional themes.

</details>

### Distribution model

How coders get the kit into their app, like adding a package or pasting in the code.  
Designers: npm library, copy-in or Tailwind · Code: `CSS variables, Tailwind @theme`

<details><summary>Designer and engineer</summary>

**Designer:** How engineers consume the system: an npm library, copy-in source like shadcn, a CDN runtime, CSS and HTML only, headless primitives, or utilities like Tailwind.

**Engineer:** Generate DTCG JSON first, then emit CSS variables and a Tailwind @theme, which OpenDesigner does today. Web components work across frameworks.

</details>

### Token build pipeline

A tool that turns one design file into code that web and phone apps can use right away.  
Designers: token build pipeline · Code: `Terrazzo or Style Dictionary v5`

<details><summary>Designer and engineer</summary>

**Designer:** The build tool that turns one token source into platform code. Default: Terrazzo for web-only teams, Style Dictionary v5 when native iOS or Android outputs are needed.

**Engineer:** Consumes DTCG 2025.10 plus resolver: Terrazzo 2.x supports resolvers; Style Dictionary v5 needs each mode pre-expanded. engine.py export writes CSS, Swift and Compose; pipeline configs are planned.

**Also called:** token transformer

</details>

### Source of truth and round-trip direction

The one main copy that all other copies follow, and which way changes flow.  
Designers: canonical source, design tools mirror · Code: `state.json to tokens/ (DTCG plus resolver)`

<details><summary>Designer and engineer</summary>

**Designer:** Which copy wins and how changes flow. In OpenDesigner, state.json and the DTCG files it generates are canonical; Figma and Paper are mirrors whose edits return as recorded decisions.

**Engineer:** engine.py build compiles state.json to DTCG 2025.10 plus resolver and code; Figma variables carry matching code syntax. JSON-first keeps OKLCH and P3 values Figma import drops.

**Also called:** canonical source

</details>

## Governance, docs and adoption

### Governance, docs and adoption

How the kit is run over time: who looks after it, how it grows, and how it changes.  
Designers: governance and adoption · Code: `context.team, decisions.md, components.inventory`

<details><summary>Designer and engineer</summary>

**Designer:** How the system runs as a product over time: build order and pilots, team, contribution, decisions, status labels, versioning, deprecation, documentation, rollout and measurement.

**Engineer:** Parent of the gov.* nodes. No tokens: team notes in context.team, the decision log in decisions.md, the component list in components.inventory; status and versioning fields are proposed.

**Also called:** governance

</details>

### Rollout and communication

How the kit is brought to product teams, step by step, and how they are kept up to date.  
Designers: rollout, release notes, roadmap · Code: `extend change note; release notes (not built)`

<details><summary>Designer and engineer</summary>

**Designer:** How the system reaches product teams and keeps them informed. Default: incremental rollout led by pain points, plus release notes, a public roadmap and a support channel.

**Engineer:** opendesigner-extend ends each change with a change note: what, why, affects, validation, decision id. Release notes from token diffs and a migration checklist are not built. Native apps migrate slower.

**Also called:** rollout

</details>

### Versioning

How each new release is numbered and when releases come out.  
Designers: semantic versioning and release cadence · Code: `package.version (proposed) per artifact`

<details><summary>Designer and engineer</summary>

**Designer:** How releases are numbered and scheduled. Default: one semantic version for the whole library while small, per-package versions once there is more than one platform, on a predictable cadence.

**Engineer:** No release version is stored yet. package.version (proposed) per artifact: tokens, components-web, components-ios, figma-library. Native ships via SPM or Gradle while Figma publishes separately, so aligning versions needs automation.

**Also called:** semver

</details>

### Deprecation and migration

How old parts are phased out with warning, and how teams get help moving to new ones.  
Designers: deprecate, then remove next major · Code: `$deprecated; component.deprecated (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** Deprecate in a minor release, remove in the next major, give at least one release cycle of notice, and pair every removal with a codemod or migration guide.

**Engineer:** DTCG $deprecated (boolean or string, "Use color.bg.accent (v4)") plus $description, not emitted yet; component.deprecated {since, removeIn, replacement} is proposed. Figma variables have no deprecated flag.

</details>

### Contribution model

How people outside the core team can suggest or add new parts to the kit.  
Designers: fast lane and proposal lane · Code: `answers.Q-gov-03; governance.contribution (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How outsiders add to the system. Default: a fast lane for fixes, icons and docs, and a proposal lane for new components, gated by useful and unique.

**Engineer:** Recorded as answers.Q-gov-03 (two-lanes by default); governance.contribution {who, types, criteria} is proposed. Proposals must pass the useful-and-unique gate before any build work starts.

</details>

### Governance flow and decision records

The steps a change goes through, and how each choice and its reason are written down.  
Designers: decision records (ADRs) · Code: `decisions.md entries D-0001 onward`

<details><summary>Designer and engineer</summary>

**Designer:** The steps a change goes through and how decisions are recorded. Adopt Brad Frost's 10-step flow and log every foundation decision as an architecture decision record, as OpenDesigner does.

**Engineer:** opendesigner/decisions.md is append-only and ADR-style: each D-0001 entry records path = value, set_by, locked, date, supersedes, source_ref and reason. RFC records and status fields are proposed.

**Also called:** decision records, ADR

</details>

### Documentation platform

Where the how-to guides for the kit live, and who is allowed to write them.  
Designers: Figma plus Storybook docs · Code: `DESIGN.md; component pages (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Where documentation lives and who writes it. Small teams document in Figma plus Storybook, add a docs platform when non-engineers author, and always publish a machine-readable export.

**Engineer:** OpenDesigner generates DESIGN.md from the same data; component pages (spec 7.8) are planned. Storybook's component manifest supports React, Angular (Vite) and Vue 3 (Vite).

</details>

### Component documentation page

The fixed layout of the help page for each part, like when to use it and how.  
Designers: component usage guidelines page · Code: `opendesigner/components/<name>.md (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** The template for each component's page: usage, when not to use, anatomy, variants, states, content, accessibility, code and changelog. Docs complete is part of the definition of done.

**Engineer:** Planned (spec 7.8), not generated: opendesigner/components/<name>.md with when to use, when not, anatomy, variants, states, content, accessibility, code and changelog.

</details>

### Component status labels

Labels that show if a part is still being tried, ready to use, or on its way out.  
Designers: experimental, ready, deprecated · Code: `components.notes; component.status (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The states a component can be in. Default three, experimental, ready and deprecated, which is enough for most teams; Primer itself simplified from five to three.

**Engineer:** Recorded as answers.Q-gov-04. DESIGN.md shows each component's status from components.notes, default "planned (tokens ready)"; component.status (proposed) = experimental | ready | deprecated.

**Also called:** status labels

</details>

### Metrics and maturity

How you tell if teams use the kit and like it, and how grown-up the kit is.  
Designers: adoption metrics and maturity · Code: `answers.Q-gov-05; system.maturityStage (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** How adoption and value are measured and which maturity stage you target. Start with design adoption from Figma analytics, code adoption from a scanner, and a quarterly satisfaction survey.

**Engineer:** Recorded as answers.Q-gov-05; metrics[] {name, source, target} (proposed) and system.maturityStage (proposed), 1-4 after Sparkbox's four stages, are not stored. Native code usage needs its own scanners.

</details>

### Build order and pilot

The order you build things in, and which real app tries the kit first.  
Designers: pilot product and build order · Code: `answers.Q-gov-02; pilots[] (proposed)`

<details><summary>Designer and engineer</summary>

**Designer:** The build order and which product pilots the system. Default: minimal foundations (color roles, type, spacing, radius), then components the pilot needs, then back-fill foundations as gaps appear.

**Engineer:** No tokens. Recorded as answers.Q-gov-02; pilots[] {product, score, champion, window} is proposed. Score 2-3 candidates on Dan Mall's 8 criteria and pick one with a champion.

**Also called:** pilot

</details>

### Team model and roles

Who looks after the kit, one central team or people spread across teams, and what jobs they do.  
Designers: centralized, federated or hybrid team · Code: `answers.Q-scope-04, context.team`

<details><summary>Designer and engineer</summary>

**Designer:** Who owns the system (centralized, federated or hybrid) and which roles staff it. Default: start centralized with a named owner, even at 1-2 people; add federated contributors later.

**Engineer:** Recorded as answers.Q-scope-04 (size and model) and context.team, printed in PRODUCT.md; team.roles[] is proposed. Native platforms need iOS and Android engineers.

</details>

### Governance tooling in Figma

Tools in Figma that keep things tidy: a checker, counts of what is used, and side copies for trying changes.  
Designers: Check designs, library analytics, branching · Code: `Figma Check designs linter`

<details><summary>Designer and engineer</summary>

**Designer:** Figma's built-in governance: the Check designs linter, library analytics and branching. On Organization or Enterprise, run Check designs before Ready for dev and review analytics quarterly.

**Engineer:** Check designs lints one page at a time, caps at 25K layers and ranks partly by variable naming. OpenDesigner's validate and review lint tokens and code; no analytics.

</details>

## How OpenDesigner works

### Builder surface (meta layer)

Choices about the tool you use to make the kit, not about the kit itself.  
Designers: the builder tool itself · Code: `builder.* meta layer`

<details><summary>Designer and engineer</summary>

**Designer:** Decisions about the OpenDesigner tool rather than the system it makes: how you edit, preview, explore, review and collaborate. Today that is a chat interview with visual templates.

**Engineer:** A meta layer for decisions about the tool. Today OpenDesigner is skills, an engine script and HTML templates in the host; a standalone canvas is optional phase 3.

**Also called:** builder surface

</details>

### AI editing and generative variation

How the AI helper suggests changes you can check first, and how it shows you other options.  
Designers: reviewable agent patches, lock and shuffle · Code: `engine.py set --why; locks; patches (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Planned: agent edits as reviewable before-and-after patches, and shuffle. Today the agent shows old and new values before a change, locks protect decisions, and option-gallery compares directions.

**Engineer:** Planned: patches {op, path, from, to, rationale} and variants {seed, locked[], params}. Today each change is engine.py set with --why, logged in decisions.md; locks sit in state.json.

**Example:** Lock the brand color so later changes cannot move it.

</details>

### Canvas rendering substrate

What the work area shows: real, working web parts, a flat picture, or a scene from a design app.  
Designers: real HTML and CSS canvas · Code: `CSS custom properties, modes as selectors`

<details><summary>Designer and engineer</summary>

**Designer:** What the canvas renders: real HTML and CSS components, a flat image, or a design-tool scene graph. Default: real HTML and CSS, ideally the actual component library.

**Engineer:** preview.html is real HTML and CSS: tokens are CSS custom properties and modes are [data-theme] selectors or @media blocks. SwiftUI and Compose outputs get no preview yet.

</details>

### Multiplayer and agent presence

Whether a few people and AI helpers can work on one design at once, and how you see them.  
Designers: multiplayer and agent presence · Code: `state.json and git; CRDT operations (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Whether people and agents edit together, and how presence shows. Version 1 is single-user and local-first; agent presence is planned first, since agents are the most frequent co-editors.

**Engineer:** Version 1 keeps state in files in your repo (state.json, decisions.md), so git gives history. Planned: edits as operations (CRDT or operational transform), which also give undo.

**Also called:** multiplayer

</details>

### Controls for foundation parameters

The knobs and sliders you use to set the basics, like picking one starting color.  
Designers: generator controls: seed and targets · Code: `state.json inputs; $extensions.opendesigner.source`

<details><summary>Designer and engineer</summary>

**Designer:** The widgets that edit foundations. OpenDesigner is generator-first: seed color and contrast target, base size and ratio, space unit; raw values only through an explicit detach.

**Engineer:** Dials and raw inputs in state.json are the source; tokens are derived, with provenance in $extensions.opendesigner.source (formula or person). OKLCH values carry hex fallbacks for Figma.

</details>

### Designer hooks and resource requests

If the tool cannot make something well, like a logo, it asks whether you have one or can get one.  
Designers: designer hooks for human-made assets · Code: `hooks.<H-id>.status in state.json`

<details><summary>Designer and engineer</summary>

**Designer:** For what AI cannot make well, like logos, custom icons, illustration, photography or a brand typeface, the builder asks for yours, or suggests a designer or a named tool.

**Engineer:** state.json hooks.H-logo and 13 others store {status, files, note}; status is pending, have, commissioning, tool, open-library, placeholder or not-needed. DESIGN.md lists open ones under Open Items.

</details>

### Keyboard-first operation

Being able to do every task in the tool with the keyboard, no mouse needed.  
Designers: Cmd+K palette, keyboard-first · Code: `command palette (planned); OD: lines`

<details><summary>Designer and engineer</summary>

**Designer:** Planned for a canvas: a Cmd+K palette, single keys for toggles like light and dark, arrow-key nudging with Shift for big steps. Today everything runs by typing in chat.

**Engineer:** Planned: a palette indexing every action and token path; Cmd on macOS, Ctrl elsewhere; arrows nudge perceptual values. Today OD: lines and engine commands are the keyboard path.

**Also called:** command palette

</details>

### Reference intake

Adding a sample site or picture so the AI can learn from how it is made, without copying its brand.  
Designers: reference: structure, never brand · Code: `css_scan.py, engine.py intake`

<details><summary>Designer and engineer</summary>

**Designer:** Add a website, screenshot or Figma file at any time; the AI reads its color, type, spacing, radius, motion and components, and builds on its structure, never another brand's identity.

**Engineer:** css_scan.py or Figma's get_variable_defs and get_design_context measure values; engine.py intake fits them to dials with confidence levels, pending in state.json references.

**Also called:** reference import

</details>

### Primary interaction model

Your main way of working in the tool: sliders with a live view, a drawing space, a chat, or code.  
Designers: interaction model: chat, panels or canvas · Code: `OD:set <path>=<value>`

<details><summary>Designer and engineer</summary>

**Designer:** Research default: panels with live preview, a canvas for screens, and the agent as an accelerator, never the only path. Today OpenDesigner is agent-led: chat, visual templates and OD: lines.

**Engineer:** Each control binds to one path: a dial or raw input that derives many tokens (raw.brandColor), a question id, or a token path. Templates return OD:set lines.

</details>

### Preview surface and latency

What you see as you decide, like light and dark sample screens side by side, and how fast it updates.  
Designers: live specimens, all modes side by side · Code: `preview.html bound to semantic variables`

<details><summary>Designer and engineer</summary>

**Designer:** What you see while deciding: specimens for each scale, a component sheet and every mode side by side (engine.py preview). Live re-rendering while you drag a control is planned.

**Engineer:** preview.html binds components to semantic CSS variables, so each [data-theme] block shows a mode without code changes. The page is static; progress indicators for slow updates are planned.

</details>

### Review and visual diff

How changes get checked before they go out, ideally with before and after views side by side.  
Designers: visual diff, before and after · Code: `graph.json edges; visual diff (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** Planned: a visual diff page per change set, before and after in each mode, exported as a pull request. Today opendesigner-extend shows old and new values and git diff --stat.

**Engineer:** Planned: list changed tokens, walk the alias graph to find affected components. Today graph.json names the decisions a change moves, and engine.py review flags stale DESIGN.md sections.

</details>

### State, undo, versions and sharing

How the tool keeps your steps and saves versions, and whether you can undo or share work by a link.  
Designers: undo, versions, shareable URL · Code: `state.json plus decisions.md; URL state (planned)`

<details><summary>Designer and engineer</summary>

**Designer:** How the tool keeps history and shares work. Today: state.json and an append-only decisions.md in your repo; git gives versions and branches. Undo and state URLs are planned.

**Engineer:** state.json (schema_version 1) holds the inputs; decisions.md logs every change, and a later entry supersedes an earlier one. A compact URL encoding and coalesced undo are planned.

</details>
