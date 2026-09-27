---
type: source
title: "emilkowalski/skills: skills/prototype/PICKER.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-prototype-picker
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/prototype/PICKER.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - prototyping
  - variant-picker
  - harness-chrome
  - glass
  - segmented-control
  - sliding-highlight
  - keyboard-shortcuts
  - reduced-motion
  - easing
  - accessibility
  - agent-skill
  - emil-kowalski
---

# emilkowalski/skills: skills/prototype/PICKER.md

## Metadata

- Video ID: `eks-skills-prototype-picker`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/prototype/PICKER.md

## Summary

PICKER.md from Emil Kowalski's skills repository is the fixed specification for the variant picker that the prototype skill puts on screen while a person flips between design directions. It gives the exact markup, CSS and JavaScript wiring for a floating dark glass pill at the bottom-center of the page, with a sliding highlight, one button per variant, an optional replay button and a fixed keyboard and URL contract. Its central point is that the picker's look is not a design decision: it is copied verbatim, never restyled with the project's tokens, and allowed exactly one change (moving to the top when a variant needs the bottom of the screen). It also shows small motion details done carefully: a 250ms strong ease-out highlight slide, no animation on first load, reduced-motion handling and instant variant swaps. For a design system it is a model for tool chrome that must stay neutral and identical across projects so it never gets confused with the design being judged [inferred].

## Key Ideas

- The picker is harness chrome, not part of the design: its appearance is a spec, not a decision, and it is copied verbatim every time.
- Only the variant names and the number of variants change from run to run; project fonts, brand colors, theming, extra shadows and borders are all forbidden.
- A dark glass pill works on top of any page, light or dark, which is why the picker is deliberately not theme-aware.
- The active highlight slides between buttons as spatial feedback (250ms, strong ease-out), but the variant being previewed swaps instantly.
- The highlight transition is switched on only after first paint, so loading the page never animates it.
- Animating the highlight's width is a deliberate, justified exception to the transform/opacity rule because the element is tiny, absolutely positioned and has no layout dependents.
- The only allowed change is moving the picker to the top when a variant (toast stack, bottom sheet, dock) occupies the bottom-center.
- The replay button appears only when some variant has motion worth re-triggering; a static comparison gets a shorter pill.
- A fixed behavior contract: number keys and arrow keys switch, R replays, typing in fields and modifier keys are ignored, and exactly one item is active at a time.
- The chosen variant survives a reload through a URL parameter, and switching re-mounts the variant so entrance animations run again.
- In a framework the same structure, class names and behavior are kept, only expressed idiomatically (state, keyed re-mounts, refs and a layout effect).

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skills repository that contains this picker spec
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills; source of PICKER.md at commit 85e8e23
- [[entities/prototype|prototype]] (tool): The agent skill that builds several UI variants and shows them behind this picker
- [[entities/the-picker-proto-picker|The Picker (proto-picker)]] (concept): Floating dark pill, bottom-center, used to switch between prototype variants; its markup, CSS and wiring are fixed
- [[entities/sliding-highlight|Sliding highlight]] (concept): Absolutely positioned 28px pill behind the active button that slides with transform and width over 250ms
- [[entities/data-ready|data-ready]] (concept): Attribute added after first paint that enables the highlight transition so page load does not animate
- [[entities/data-position-top|data-position="top"]] (concept): The single allowed modification: moves the picker to top: 24px when a variant occupies the bottom-center
- [[entities/replay-button|Replay button]] (concept): Optional button (and its divider) that re-mounts the current variant so its entrance or state animation runs again; bound to the R key
- [[entities/backdrop-filter|backdrop-filter]] (concept): CSS used for the picker's dark glass surface: blur(12px) saturate(1.4)
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Media query under which the highlight transition is turned off
- [[entities/aria-current|aria-current]] (concept): Attribute set to "true" on exactly one active picker item at all times
- [[entities/requestanimationframe|requestAnimationFrame]] (concept): Used to render the variant on the next frame after clearing the stage, and (nested twice) to add data-ready after first paint
- [[entities/history-replacestate|history.replaceState]] (concept): Used to write the selected variant into the ?v= URL parameter so it persists across reload

## Topics

- [[topics/prototyping|Prototyping]]: Defines the fixed picker used to flip between prototype variants: dark glass pill, bottom-center, number and arrow keys to switch, R to replay, selection stored in ?v=, and a re-mount on every switch so entrance animations re-run.
- [[topics/presenting-designs|Presenting designs]]: The comparison tool must stay neutral chrome, identical across projects and never styled with the project's tokens, so it never reads as part of the design being judged; it moves to the top only when a variant needs the bottom-center.
- [[topics/easing-and-timing|Easing and timing]]: The highlight slides with transform and width over 250ms cubic-bezier(0.23, 1, 0.32, 1), described as strong ease-out; item color changes use 150ms ease-out; the variant swap itself has no transition.
- [[topics/animation-performance|Animation performance]]: The highlight uses will-change: transform; animating width is called a deliberate exception to the transform/opacity rule, acceptable because the element is 28px tall, absolutely positioned and has no layout dependents.
- [[topics/reduced-motion|Reduced motion]]: Under prefers-reduced-motion: reduce the highlight transition is set to none.
- [[topics/micro-interactions|Micro-interactions]]: Picker items get press feedback of scale(0.97) on :active, a hover color lift from 0.55 to 0.85 white, and a sliding active pill as spatial feedback; the transition is enabled only after first paint so load does not animate.
- [[topics/accessibility|Accessibility]]: The picker is a nav with aria-label, decorative spans are aria-hidden, the icon replay button has an aria-label, exactly one item carries aria-current="true", focus-visible shows a 2px outline with 2px offset, and key handling ignores form fields, contenteditable and modifier keys.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: The picker is deliberately not theme-aware: dark glass works on top of any page, light or dark, and theme switching is forbidden.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: The glass pill uses a 1px inset white hairline at 0.08 plus two dark drop shadows (0 8px 24px at 0.24 and 0 2px 6px at 0.12), with no extra shadows or borders allowed.
- [[topics/shape-and-corner-radius|Shape and corner radius]]: The container, highlight and items all use border-radius 999px, making a full pill.
- [[topics/typography|Typography]]: The picker uses a system font stack (-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif) at 13px, line-height 1, antialiased, never the project's fonts; the replay glyph is 14px.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Gives the full HTML, CSS and vanilla JS wiring, and says a framework version keeps the class names, structure and behavior while using state instead of innerHTML, a keyed re-mount instead of requestAnimationFrame, and refs plus a layout effect to measure the highlight.
- [[topics/ai-assisted-design|AI-assisted design]]: The spec is written for an agent to copy verbatim, with only variant names and count changing per run, so the tool looks the same every time it is generated.

## Notable Claims

- The picker's appearance is not a design decision; it is the spec. Evidence: # The Picker, first paragraph
- Keeping the picker identical across every project makes it always read as harness chrome, never as part of the design being judged. Evidence: # The Picker: It stays identical across every project
- Dark glass works on top of any page, light or dark, which is why the picker is not theme-aware. Evidence: Dark glass works on top of any page — light or dark — which is why it is not theme-aware.
- Enabling the highlight slide only after first paint (data-ready) means page load does not animate. Evidence: Styles comment: The slide is enabled only after first paint
- The highlight's width transition has negligible paint cost because the element is 28px tall, absolutely positioned and has no layout dependents. Evidence: Rules: The highlight slides; the variant swap stays instant.
- The sliding active pill is spatial feedback on the picker itself. Evidence: Rules: The highlight slides
- Setting data-position="top" when a variant occupies the bottom-center keeps the picker from covering the work. Evidence: Rules: One allowed modification
- Clearing the stage and rendering on the next frame makes entrance animations re-run. Evidence: Reference wiring: mount()
- The behavior contract is fixed regardless of how the harness renders. Evidence: Behavior contract

## Quotes

> it always reads as harness chrome, never as part of the design being judged.
> Dark glass works on top of any page — light or dark
> The highlight slides; the variant swap stays instant.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: These values are the spec for prototype harness chrome, not house design tokens; they are meant to stay out of the project's design and should not be applied to a product's components [inferred].
- Caveat: Snapshot of the repository at commit 85e8e23; the spec may change later.
- Caveat: The 'transform/opacity rule' is referenced but not defined in this file; its definition presumably lives in Emil Kowalski's other skills [inferred].
- Caveat: The prose says to ignore key events 'when a modifier is held', but the reference code checks only metaKey, ctrlKey and altKey, not shiftKey.
- Caveat: The reference wiring is verbatim only for standalone HTML; framework versions are described in one sentence rather than given as code.
- Caveat: The spec gives no reason for most individual values (shadows, alphas, sizes); they are fixed by decree, not justified one by one.

### Rules and practices

- **must** (tooling, web): Copy the picker's markup, CSS and wiring verbatim from the spec; change only the variant names and the number of variants per run. Why: The picker's appearance is not a design decision; it is the spec. [# The Picker: Copy the markup, CSS, and wiring below verbatim]
- **must** (tooling, web): Keep the picker identical across every project. Why: So it always reads as harness chrome, never as part of the design being judged. [It stays identical across every project]
- **must** (tokens, web): Do not restyle the picker with the project's tokens, fonts or colors: no project fonts, no brand colors, no theme switching, no extra shadows or borders. Why: These values are the spec; the picker must not look like part of the design being judged. [Do not restyle it with the project's tokens, fonts, or colors; No project fonts, no brand colors, no theme switching, no extra shadows or borders.]
- **must** (components, web): Render the picker as a floating dark pill at the bottom-center of the screen, and do not make it theme-aware. Why: Dark glass works on top of any page, light or dark. Values: bottom-center. [It is a floating dark pill, bottom-center.]
- **must** (components, web): Order the picker markup as the sliding highlight span first, then one button per variant, then a hairline divider, then the replay button. Why: This is the fixed markup of the spec. Values: <nav class="proto-picker", <span class="proto-picker-highlight" aria-hidden="true"></span>, <button class="proto-picker-item">, <span class="proto-picker-divider" aria-hidden="true"></span>, <button class="proto-picker-item proto-picker-replay". [The sliding highlight span first, one button per variant, a hairline divider, then the replay button]
- **must** (accessibility, web): Make the picker a <nav> with aria-label="Prototype variants", mark the highlight and divider spans aria-hidden="true", and give the icon-only replay button (↻) aria-label="Replay animation (R)". Why: This is the fixed markup of the spec. Values: aria-label="Prototype variants", aria-hidden="true", aria-label="Replay animation (R)", ↻. [<nav class="proto-picker" aria-label="Prototype variants">]
- **must** (tooling, react): In a framework, keep the picker's class names and structure; change only the rendering syntax. Why: The markup is part of the verbatim spec. [In a framework, keep the class names and structure]
- **must** (layout, css): Position the picker fixed at bottom: 24px, centered with left: 50% and transform: translateX(-50%), at z-index 2147483647. Why: Part of the verbatim style spec for a floating bottom-center pill. Values: position: fixed, bottom: 24px, left: 50%, transform: translateX(-50%), z-index: 2147483647. [position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%); z-index: 2147483647]
- **must** (layout, css): Lay the picker out as a flex row with align-items: center, gap: 2px, padding: 4px and border-radius: 999px. Why: Part of the verbatim style spec. Values: display: flex, align-items: center, gap: 2px, padding: 4px, border-radius: 999px. [display: flex; align-items: center; gap: 2px; padding: 4px; border-radius: 999px;]
- **must** (color, css): Give the picker a dark glass surface: background rgba(10, 10, 10, 0.82) with backdrop-filter: blur(12px) saturate(1.4), including the -webkit-backdrop-filter prefix. Why: Dark glass works on top of any page, light or dark. Values: rgba(10, 10, 10, 0.82), blur(12px) saturate(1.4), -webkit-backdrop-filter. [background: rgba(10, 10, 10, 0.82); -webkit-backdrop-filter: blur(12px) saturate(1.4);]
- **must** (elevation, css): Use exactly this three-layer box-shadow on the picker: an inset 1px white hairline plus two soft dark drop shadows. Why: Part of the verbatim style spec; no extra shadows or borders are allowed. Values: 0 0 0 1px rgba(255, 255, 255, 0.08) inset, 0 8px 24px rgba(0, 0, 0, 0.24), 0 2px 6px rgba(0, 0, 0, 0.12). [0 0 0 1px rgba(255, 255, 255, 0.08) inset, 0 8px 24px rgba(0, 0, 0, 0.24), 0 2px 6px rgba(0, 0, 0, 0.12)]
- **must** (typography, css): Set the picker's type to the system stack at 13px with line-height 1 and antialiased font smoothing, never the project's fonts. Why: Part of the verbatim style spec; project fonts are forbidden. Values: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif, font-size: 13px, line-height: 1, -webkit-font-smoothing: antialiased. [font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 13px; line-height: 1;]
- **must** (components, css): Disable text selection on the picker with user-select: none and -webkit-user-select: none. Why: Part of the verbatim style spec. Values: user-select: none, -webkit-user-select: none. [user-select: none; -webkit-user-select: none;]
- **must** (components, css): Style the sliding highlight as an absolutely positioned pill: top 4px, left 0, height 28px, border-radius 999px, background rgba(255, 255, 255, 0.12), will-change: transform. Why: Part of the verbatim style spec; the highlight sits behind the active button. Values: position: absolute, top: 4px, left: 0, height: 28px, border-radius: 999px, rgba(255, 255, 255, 0.12), will-change: transform. [.proto-picker-highlight {]
- **must** (motion, css): Animate the highlight's transform and width over 250ms with cubic-bezier(0.23, 1, 0.32, 1), a strong ease-out, as it moves between buttons. Why: The sliding active pill is spatial feedback on the picker itself. Values: transform 250ms cubic-bezier(0.23, 1, 0.32, 1), width 250ms cubic-bezier(0.23, 1, 0.32, 1). [.proto-picker[data-ready] .proto-picker-highlight; Rules: The highlight slides]
- **must** (motion, web): Enable the highlight transition only after first paint, by adding data-ready to the picker after two nested requestAnimationFrame calls, so the highlight takes its initial position without animating. Why: So page load doesn't animate. Values: data-ready, requestAnimationFrame(() => requestAnimationFrame(() => picker.setAttribute('data-ready', ''))). [Enable the slide only after first paint, so load doesn't animate]
- **must** (accessibility, css): Under prefers-reduced-motion: reduce, set the highlight transition to none. Why: Part of the verbatim style spec for reduced motion. Values: @media (prefers-reduced-motion: reduce), transition: none. [@media (prefers-reduced-motion: reduce)]
- **must** (motion, all): Do not animate the variant swap: the previewed variant switches instantly, with no transition, even though the picker's highlight slides. Why: The highlight's slide is spatial feedback on the picker itself; the variant being previewed still switches with no transition. [Rules: The highlight slides; the variant swap stays instant.]
- **should** (motion, css): Animate width only as a deliberate, justified exception to the transform/opacity rule, as the picker highlight does: it is 28px tall, absolutely positioned and has no layout dependents. Why: Under those conditions the paint cost is negligible. Values: 28px. [transition is a deliberate exception to the transform/opacity rule]
- **must** (components, css): Style each variant button as a 28px-tall pill: position relative so it sits above the highlight, display flex, align-items center, padding 0 12px, border 0, border-radius 999px, transparent background, font: inherit, cursor pointer. Why: Part of the verbatim style spec. Values: height: 28px, padding: 0 12px, border: 0, border-radius: 999px, background: transparent, font: inherit, cursor: pointer, position: relative. [position: relative; /* sits above the highlight */]
- **must** (color, css): Set item text to rgba(255, 255, 255, 0.55) at rest, rgba(255, 255, 255, 0.85) on hover and #fff when active. Why: Part of the verbatim style spec. Values: rgba(255, 255, 255, 0.55), rgba(255, 255, 255, 0.85), #fff. [color: rgba(255, 255, 255, 0.55); color: rgba(255, 255, 255, 0.85); .proto-picker-item[data-active] { color: #fff;]
- **must** (motion, css): Transition item text color with color 150ms ease-out. Why: Part of the verbatim style spec. Values: color 150ms ease-out. [transition: color 150ms ease-out;]
- **must** (motion, css): Give picker items press feedback of transform: scale(0.97) on :active. Why: Part of the verbatim style spec. Values: scale(0.97). [.proto-picker-item:active]
- **must** (accessibility, css): Show keyboard focus on picker items with a :focus-visible outline of 2px solid rgba(255, 255, 255, 0.4) and outline-offset 2px. Why: Part of the verbatim style spec. Values: outline: 2px solid rgba(255, 255, 255, 0.4), outline-offset: 2px. [.proto-picker-item:focus-visible]
- **must** (components, css): Draw the divider as a 1px-wide, 16px-tall hairline with margin 0 4px and background rgba(255, 255, 255, 0.12). Why: Part of the verbatim style spec. Values: width: 1px, height: 16px, margin: 0 4px, rgba(255, 255, 255, 0.12). [.proto-picker-divider {]
- **must** (components, css): Style the replay button with padding 0 10px and font-size 14px. Why: Part of the verbatim style spec. Values: padding: 0 10px, font-size: 14px. [.proto-picker-replay {]
- **must** (layout, web): If a variant occupies the bottom-center of the screen (a toast stack, a bottom sheet, a dock), set data-position="top" on the picker, which moves it to top: 24px with bottom: auto. Why: So the picker never covers the work. Values: data-position="top", top: 24px, bottom: auto. [Rules: One allowed modification]
- **must** (tooling, web): Do not move or change anything else about the picker; top placement is the only allowed modification. Why: Nothing else about it may move or change. [Nothing else about it may move or change]
- **must** (components, web): Render the replay button and its divider only when at least one variant has an entrance or state animation worth re-triggering; give a static comparison the shorter pill without them. Why: Replay is conditional; there is nothing to replay in a static comparison. [Render the replay button and its divider only when at least one variant has an entrance or state animation worth re-triggering]
- **must** (components, web): Give the replay button both classes, proto-picker-item and proto-picker-replay, so it takes the item styles with its own padding and font-size, but leave it out of the variant list that the highlight, clicks and number keys use. Why: The reference wiring selects variant items with .proto-picker-item:not(.proto-picker-replay) and wires replay separately to re-mount the current variant. Values: class="proto-picker-item proto-picker-replay", .proto-picker-item:not(.proto-picker-replay). [picker.querySelectorAll('.proto-picker-item:not(.proto-picker-replay)')]
- **must** (accessibility, web): Bind number keys 1–N to switch straight to a variant, ← and → to step between variants, and R (lower or upper case) to replay. Why: The behavior contract is fixed regardless of how the harness renders. Values: 1–N, ←, →, R, e.key === 'r' || e.key === 'R'. [Behavior contract]
- **must** (components, web): Wrap arrow-key navigation: → on the last variant goes to the first, and ← on the first goes to the last. Why: This is how the reference wiring steps between variants. Values: (current + 1) % variants.length, (current - 1 + variants.length) % variants.length. [else if (e.key === 'ArrowRight') setActive((current + 1) % variants.length);]
- **must** (accessibility, web): Ignore picker key events when focus is in an input, textarea, select or contenteditable element, or when a modifier key is held. Why: Part of the fixed behavior contract. Values: INPUT, TEXTAREA, SELECT, isContentEditable, metaKey, ctrlKey, altKey. [Ignore key events when focus is in an input, textarea, select, or contenteditable, or when a modifier is held]
- **must** (accessibility, web): Switch variants on click, and keep exactly one item carrying data-active and aria-current="true" at all times, with the highlight sliding to it. Why: Part of the fixed behavior contract. Values: data-active, aria-current="true". [Behavior contract: exactly one item carries data-active]
- **must** (tooling, web): Persist the selected variant across reloads in a 1-based URL parameter (?v=2), written with history.replaceState, falling back to variant 1. Why: Part of the fixed behavior contract: selection persists across reload. Values: ?v=2, history.replaceState. [Selection persists across reload via a URL param]
- **must** (tooling, web): Re-mount the variant on every switch so its entrance animations re-run, and make replay re-mount the current variant without switching. Why: Part of the fixed behavior contract. [Behavior contract: Switching re-mounts the variant]
- **must** (tooling, web): In standalone HTML, clear the stage first and render the variant on the next animation frame. Why: So entrance animations re-run. Values: stage.innerHTML = '', requestAnimationFrame, document.getElementById('stage'). [Reference wiring: Clear first, render next frame]
- **must** (tooling, web): Size and place the highlight from the active item's offsetWidth and offsetLeft (width plus translateX), and re-measure on window resize. Why: This is how the reference wiring keeps the highlight under the active item. Values: offsetWidth, offsetLeft, translateX, resize. [Reference wiring: moveHighlight()]
- **should** (tooling, web): Ignore a switch request for an index outside the range of variants. Why: This is how the reference wiring guards setActive. Values: if (i < 0 || i >= variants.length) return;. [if (i < 0 || i >= variants.length) return;]
- **must** (tooling, react): In a framework, keep the same picker behavior but express it idiomatically: state instead of innerHTML, a keyed re-mount instead of requestAnimationFrame, and refs plus a layout effect to measure the highlight. Why: The contract is fixed regardless of how the harness renders; the reference wiring is verbatim only for standalone HTML. [## Reference wiring]
- **should** (tooling, web): Supply variants to the wiring as an array of render functions, one per variant, in picker order. Why: The reference wiring maps picker items to variants by index. [Reference wiring: `variants` is an array of render functions]

### Decisions it informs

- Where should the variant picker sit on screen?
  - Bottom-center (default): Floating dark pill 24px above the bottom edge, centered When: Every run, unless a variant uses the bottom-center of the screen
  - Top (data-position="top"): Same pill moved to 24px from the top so it does not cover the work When: A variant occupies the bottom-center: a toast stack, a bottom sheet, a dock
  - Recommendation: Keep it at bottom-center; switching to the top is the only allowed modification and only when a variant sits at the bottom-center.
- Should the picker include a replay button?
  - With replay: Adds a hairline divider and a ↻ button (and the R key) that re-mounts the current variant so its animation runs again When: At least one variant has an entrance or state animation worth re-triggering
  - Without replay: A shorter pill with only the variant buttons When: A static comparison
  - Recommendation: Render replay and its divider only when some variant has motion worth re-triggering.

### Process

1. Paste the markup: Copy the nav, highlight span, one button per variant, divider and replay button verbatim; change only the variant names and count, and mark the first active with data-active and aria-current="true".
2. Paste the styles: Copy the CSS verbatim, without project tokens, fonts, colors, theming, extra shadows or borders.
3. Decide replay: Keep the replay button and its divider only if at least one variant has an entrance or state animation to re-trigger.
4. Decide position: Add data-position="top" only if a variant occupies the bottom-center (toast stack, bottom sheet, dock).
5. Wire the behavior: Use the reference wiring for standalone HTML (moveHighlight, mount, setActive, click, resize and keydown listeners); in a framework, express the same contract with state, a keyed re-mount and refs plus a layout effect.
6. Set the initial state: Read ?v= from the URL (default 1), activate that variant, then add data-ready after two animation frames so the highlight does not animate on load.

### Examples and visual references

- Picker markup with three variants and replay (PICKER.md Markup section): Buttons labelled Quiet (active), Editorial and Playful, a hairline divider, then a ↻ replay button; shows that variants are named by direction.
- Floating dark glass pill (The prototype harness): Near-black translucent pill (rgba(10, 10, 10, 0.82), blur 12px) at the bottom-center with a lighter pill highlight behind the active item; it sits on light or dark pages alike.
- Variants that take the bottom-center (Toast stack, bottom sheet, dock): Cases where the picker must move to the top so it never covers the design being compared.
- Static comparison (Any variant set with no motion): The picker drops the divider and replay button, giving a shorter pill.

### Numbers

- 24px: Distance of the picker from the bottom edge (or the top edge with data-position="top") [.proto-picker bottom; [data-position="top"] top]
- 2147483647: Picker z-index [.proto-picker]
- gap: 2px: Gap between items in the pill [.proto-picker]
- padding: 4px: Padding inside the pill (the highlight also sits at top: 4px) [.proto-picker; .proto-picker-highlight]
- 999px: Border radius of the pill, highlight and items [.proto-picker, .proto-picker-highlight, .proto-picker-item]
- rgba(10, 10, 10, 0.82): Picker background [.proto-picker]
- blur(12px) saturate(1.4): Picker backdrop filter (with the -webkit- prefix too) [.proto-picker]
- 0 0 0 1px rgba(255, 255, 255, 0.08) inset: Picker box-shadow layer 1: inset white hairline [.proto-picker box-shadow]
- 0 8px 24px rgba(0, 0, 0, 0.24): Picker box-shadow layer 2: larger soft drop shadow [.proto-picker box-shadow]
- 0 2px 6px rgba(0, 0, 0, 0.12): Picker box-shadow layer 3: tight drop shadow [.proto-picker box-shadow]
- 13px: Picker font size, with line-height 1 [.proto-picker]
- 28px: Height of the highlight and of each item; also why the width transition is cheap [.proto-picker-highlight, .proto-picker-item, Rules]
- rgba(255, 255, 255, 0.12): Fill of the sliding highlight and of the divider hairline [.proto-picker-highlight; .proto-picker-divider]
- 250ms cubic-bezier(0.23, 1, 0.32, 1): Highlight slide (transform and width), a strong ease-out [.proto-picker[data-ready] .proto-picker-highlight]
- 0 12px: Horizontal padding of each variant item [.proto-picker-item]
- 150ms ease-out: Item text color transition [.proto-picker-item]
- rgba(255, 255, 255, 0.55): Item text color at rest [.proto-picker-item]
- rgba(255, 255, 255, 0.85): Item text color on hover [.proto-picker-item:hover]
- #fff: Item text color when active [.proto-picker-item[data-active]]
- scale(0.97): Item press feedback on :active [.proto-picker-item:active]
- 2px solid rgba(255, 255, 255, 0.4): Focus-visible outline on items, with outline-offset: 2px [.proto-picker-item:focus-visible]
- 16px: Divider height (1px wide, margin 0 4px) [.proto-picker-divider]
- 0 10px: Replay button horizontal padding [.proto-picker-replay]
- 14px: Replay glyph (↻) font size [.proto-picker-replay]
- ?v=2: URL parameter that stores the 1-based selected variant; falls back to variant 1 [Behavior contract]

<!-- /od:learn -->
