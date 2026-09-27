---
type: synthesis
title: Accessibility
created: 2026-09-24
updated: 2026-09-28
sources:
  - EOcY3hPMQkk
  - HE4rLEQpiXY
  - adev-changelog
  - adev-home
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-the-magic-of-clip-path
  - eks-skills-animate-expo-skill
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-api
  - eks-skills-emil-design-eng-skill
  - eks-skills-improve-animations-audit
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-prototype-picker
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - sonner-toast
  - sonner-toaster
  - vaul-api
  - vaul-other
  - xHD01_Onac0
tags:
  - od-area-accessibility
  - od-area-platforms
---

# Accessibility

## In short

Accessibility means people with different eyesight, hands, bodies, devices and settings can all use the product. The sources share a handful of habits: check that text and icons stand out enough from what is behind them, respect the settings people turn on (less motion, less transparency, more contrast, bigger text, zoom), make things big enough to tap, and build menus, dialogs and drawers on ready-made parts that already handle the keyboard and screen readers. Reduced motion means gentler motion, not none at all. Most of these rules come from Emil Kowalski's sources, which OpenDesigner treats as house standards; the color-contrast advice comes from Kole Jain's videos and matches OpenDesigner's own locked WCAG 2.2 AA floors.

## House standards

**Settings people turn on**
- **STD-accessibility-motion-01** and **-02** (must): ship the reduced-motion version with every animation that moves something; under reduced motion, remove movement and keep a short opacity cross-fade (the sources use 200ms) and the opacity and color changes that explain a state. Never remove all feedback.
- **STD-accessibility-motion-03** and **-04** (must): in JavaScript and React Native, branch motion values on the reduced-motion setting, and make native screen changes fade.
- **STD-accessibility-motion-05** and **-06** (must): check reduced motion by toggling it in DevTools; missing reduced-motion handling is a medium finding and blocks approval.
- **STD-accessibility-motion-07** to **-10** (should): no full-viewport moving backgrounds, no slow loops near 0.2 Hz, ease theme switches instead of jumping brightness, and soften large surfaces while they move.
- **STD-accessibility-motion-11** and **-12** (must): `prefers-reduced-transparency: reduce` makes translucent surfaces frostier or solid; `prefers-contrast: more` gives near-solid backgrounds with a defined, contrasting border. Each is its own signal.
- **STD-accessibility-motion-13** (must): scale layout with the user's text size; on the web, spacing in rem or em.
- **STD-accessibility-motion-27** (must): never disable pinch zoom; fix the input font size instead.

**Hands and pointers**
- **STD-mobile-touch-09** (must): targets at least 44x44pt on iOS and 48dp on Android, and a 44px hit area for small web controls; grow the hit area, not the visual.
- **STD-accessibility-motion-15** (must): every `:hover` animation sits inside `@media (hover: hover) and (pointer: fine)`, shipped with the hover; `:active` stays ungated.
- **STD-mobile-touch-17** (must): controls are unselectable; text that is content stays selectable.
- **STD-accessibility-motion-20** (must): a haptic is never the only feedback.

**Keyboard, focus and screen readers**
- **STD-accessibility-motion-16** (must): build dialogs, drawers, popovers, menus, selects and tabs on an accessible primitive (base-ui, or Radix) and command menus on cmdk; never a hand-rolled `<div>` dialog or dropdown.
- **STD-accessibility-motion-17** (should): mark a visual-only duplicate layer `aria-hidden` and give its buttons `tabIndex={-1}`.
- **STD-accessibility-motion-18** (must): the prototype picker keeps its fixed accessible markup and its 2px `:focus-visible` outline at a 2px offset.
- **STD-accessibility-motion-23** (should): keep Sonner's accessibility defaults: the "Notifications" label, the Alt+T hotkey and `dismissible: true`.
- **STD-accessibility-motion-24** (must): never trap people in an overlay; a non-dismissible drawer gets an explicit close control. **STD-accessibility-motion-25** and **-26** (should): a controlled drawer still reacts to Escape, and an overlay covers the inert page behind a modal drawer.
- **STD-visual-details-09** (must): underline only links.

**Legibility and people**
- **STD-visual-details-13** (should) and **-18** (must): over translucent surfaces use higher-contrast, slightly heavier text, and never stack a light translucent surface on another.
- **STD-visual-details-43** (should): design for the full range of age, language, expertise and ability.

No house standard sets a color contrast ratio. Contrast rests on OpenDesigner's locked accessibility floors in `guardrails.md` section 4: text 4.5:1 (large text 3:1), non-text elements and focus indicators 3:1, measured without rounding up, with WCAG 2.2 AA as the default target.

## What the sources teach

### Contrast you can check
- Colored cards and white text on brand colors often fail WCAG contrast checks, and a failing pair can't reasonably be used. If a brand color fails with white text, darken it until it passes or pick a complementary color that passes; an unimportant brand-colored surface can be lightened with black text instead [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). The same video says a light gray button with white text reads as disabled with no other cue. Its contrast values appear only on screen.
- An icon placed on a photo, such as a save icon on bright listing images, gets a circle behind it so it keeps its contrast whatever the image [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- The AI-generated screen in one video needed its chips' contrast fixed [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]), so generated screens deserve a contrast pass like any other [inferred].
- Over blurred or translucent surfaces, flat gray text loses legibility: use higher contrast, a slightly heavier weight and a small letter-spacing bump, put color on a solid layer, and never stack light translucent surfaces [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Respect the settings people turn on
- Components respond to three independent signals: `prefers-reduced-motion`, `prefers-reduced-transparency` and `prefers-contrast: more`. Reduced transparency raises background opacity and drops the blur (the sample toolbar turns solid white); more contrast gets near-solid backgrounds with a defined, contrasting border [S-L19-020].
- Reduced motion is a gentler, non-vestibular version, not zero motion: keep opacity and color changes that aid understanding, and drop slides, scale, springs, parallax, elastic and overshoot. The samples use a 200ms fade [S-L19-020] [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- In React, read `useReducedMotion` and swap moving values for static ones (`closedX = reduce ? 0 : '-100%'`) [S-L19-023] [S-L19-033]. In React Native, use `ReduceMotion.System` or `useReducedMotion()`, and make screen changes fade [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]). The prototype picker turns its highlight transition off [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- In audits and reviews, movement without reduced-motion handling is a finding, reduced-motion code that removes all feedback is also a finding, and a change is approved only when reduced motion is respected [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]).
- Motion can cause motion sickness [S-L19-023]. Avoid full-viewport moving backgrounds, slow loops near 0.2 Hz (one cycle every 5 seconds) and abrupt brightness jumps between themes; make large moving objects semi-transparent while they travel [S-L19-020].
- Respect the text-size setting by scaling layout with the text, using rem or em for spacing [S-L19-020]. In React Native never animate to a hardcoded height: text scaling is on by default, so a height measured at the default size is wrong at 200% [S-L19-016].
- Never disable zoom with `user-scalable=no` or `maximum-scale=1`; the page zooms into inputs because their text is under 16px, so fix that [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).

### Hands, fingers and pointers
- Small buttons need a 44px minimum hit area, built with a pseudo-element [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]). Native targets are 44x44pt on iOS and 48dp on Android; when the visual is smaller, add `hitSlop` instead of growing it [S-L19-016].
- Touch devices fire hover on tap, so hover motion goes behind `@media (hover: hover) and (pointer: fine)` [S-L19-023] [S-L19-025] [S-L19-032] [S-L19-033]. After removing the tap highlight, every tappable keeps its own `:active` press state [S-L19-028].
- Keep content text selectable, because people copy addresses, error messages and order numbers; `user-select: none` belongs on controls only [S-L19-028].
- Haptics are off system-wide for many people and silent on most Android hardware, so a haptic is never the only feedback [S-L19-016].

### Keyboard, focus and screen readers
- Build on accessible primitives: the Vaul drawer sits on Radix's Dialog for accessibility and focus management [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]); clip-path tabs belong on Radix Tabs in production [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]); dialogs, popovers, menus and selects come from base-ui, which handles accessibility, focus trapping and dismissal, never from a `<div>` with manual focus handling [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- A duplicated decorative layer, such as the clip-path overlay copy of tabs, is marked `aria-hidden` and its buttons get `tabIndex={-1}` [S-L19-010].
- The picker spec shows the markup in full: a `<nav>` with an `aria-label`, decorative spans `aria-hidden`, an `aria-label` on the icon-only replay button, exactly one item with `aria-current="true"`, a 2px `:focus-visible` outline at a 2px offset, and key handling that ignores form fields, editable text and modifier keys [S-L19-030].
- An example of making focus easier to see: the animations.dev changelog lists "more distinct, yellow focus states" as an improvement to the course site. It is a changelog line, not a stated rule [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).
- Toasts: the container carries an ARIA label, "Notifications" by default (`containerAriaLabel`); Alt+T moves focus to the toaster area; `dir` sets text direction (left to right by default); toasts stay dismissible unless people must not close them [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]) [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).
- Drawers: an optional Title and Description are announced when the drawer opens, and the overlay covers the inert part of the page [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]).
- Underlines are reserved for links so they stay a reliable cue; emphasize other text with weight or color [S-L19-004].

### Always a way out
- A Vaul drawer set to `dismissible: false` ignores Escape, outside clicks and dragging down; the docs demo can only be closed by refreshing the page [S-L19-097] ([[sources/vaul-other-other-vaul|Other – Vaul]]). The page doesn't frame this as accessibility; the house standard adds an explicit close control (STD-accessibility-motion-24).

### Beyond the interface
- The course site added English captions to all its videos [S-L19-001], and the course names accessibility as one of the steps that take an animation from good to great [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]).
- Design for the full range of age, language, expertise and ability [S-L19-020].

## Where they agree and disagree

- **Reduced motion (strong agreement, recorded engine conflicts).** Six Emil sources say "gentler, not zero" [S-L19-016] [S-L19-020] [S-L19-023] [S-L19-025] [S-L19-032] [S-L19-033]; the picker simply switches its highlight transition off [S-L19-030]. That matches DC-L04-25 (keep color and opacity, remove travel, treat WCAG 2.3.3 as required), the default `replace` of Q-motion-07 and `guardrails.md`. Against STD-accessibility-motion-02, `standards.json` records that `engine.py` builds its reduced transitions from a 100ms duration instead of the sources' 200ms fade, and that Q-motion-07's `remove` option turns them into 0ms, which is zero motion. Since the standards' second version, the standard's own mapping replaces those values with the 200ms cross-fade in every project, it settles Q-motion-07, and `remove` can only be refused. `engine.py` also maps Q-motion-01's `none` to a motion-off flag that makes the same transitions 0ms; that is checked in the code, and `standards.json` no longer records it.
- **Transparency and contrast settings (agree with research; engine gap).** The three signals [S-L19-020] match DC-L10-16 (honor every setting, with high contrast and reduced transparency as token modes), DC-L04-16 (every translucent token has an opaque twin) and DC-L01-20. `standards.json` records that `engine.py`'s CSS export writes no `prefers-reduced-transparency` or `prefers-contrast: more` block (STD-accessibility-motion-11, -12).
- **Color contrast (agree; brand color tension).** Checking colored cards and brand colors against WCAG [S-L19-051] and fixing low-contrast chips [S-L19-086] match DC-L01-22 (WCAG 2.2 AA for all pairs, test tokens as pairs in every mode) and the `guardrails.md` floors. Kole Jain says not to be afraid to adapt brand colors [S-L19-051], while Q-color-01 offers `keep-hex` (keep the brand color exactly) beside `contrast-targets`. The two can coexist if the exact hex stays for fills without text and a darker step carries white text [inferred].
- **Disabled by color alone (tension).** A light gray button with white text reading as disabled [S-L19-051] fits DC-L01-22's note that disabled components are exempt from contrast rules, but `guardrails.md` also says never to carry meaning by color alone [inferred].
- **Web target size (recorded conflict).** A 44px hit area for small buttons [S-L19-004] and STD-mobile-touch-09 sit above `guardrails.md`'s 24x24 CSS px web floor and `engine.py`'s 24px pointer target, and `standards.json` records the conflict. The research already reconciles them: DC-L03-12's default is a 24px visual minimum with a 44px hit area on coarse pointers, and DC-L10-15 defaults web to 44 CSS px. The source's reason ("hard to tap") is about touch, so 24px for fine pointers and 44px for touch fits both [inferred].
- **Focus rings (agree; one unchecked detail).** A 2px outline at a 2px offset [S-L19-030] and distinct focus states [S-L19-001] match DC-L04-09, DC-L08-11, Q-state-03's default `outer-2-2` and `guardrails.md`. The picker's ring is white at 40% opacity on its own dark chrome; none of the sources check it against the 3:1 focus contrast in DC-L04-09, and the picker can't be restyled (STD-process-review-taste-45) [inferred].
- **Accessible primitives (agree; one recorded conflict).** Radix [S-L19-005] [S-L19-010] and base-ui [S-L19-029] match DC-L08-20's overlay constraints (focus trapped and returned, Escape closes, `aria-modal`). `standards.json` records that Q-comp-01's React default names React Aria, which is outside the curated library list (STD-visual-details-55).
- **Dismissal (agree).** The non-dismissible drawer that needs a page refresh [S-L19-097] is the failure that `guardrails.md` ("every dialog has a way to dismiss it"), DC-L08-20 ("Escape closes") and STD-accessibility-motion-24 rule out. Sonner's `dismissible: true` default [S-L19-021] agrees.
- **Text scaling (agree; cap tension).** Scaling layout with text [S-L19-020] and measuring rather than hardcoding heights [S-L19-016] match DC-L10-07 (full scaling, test at the largest size) and `guardrails.md` (text to 200%). Q-type-17's default caps fixed chrome such as tab labels at about 1.5x (from DC-L10-07); the sources name no cap, and STD-accessibility-motion-13 is a must [inferred]. `standards.json` now has STD-accessibility-motion-13 refuse Q-type-17's `none` and Q-token-04's `unitless` options and supersede DC-L03-26, and it records that the CSS export writes spacing tokens in px while font sizes are in rem, so layouts built from the spacing tokens don't grow with the user's text size.
- **Hover and haptics (agree).** Hover gating [S-L19-023] [S-L19-028] fits DC-L13-03's warning that hover-only reveal fails keyboard and touch users. "Never only a haptic" [S-L19-016] matches DC-L04-26 (Apple: never use haptics as the only channel).
- **Drawer title (open).** Vaul calls Title and Description optional [S-L19-093]; DC-L08-20 asks for `aria-modal` dialogs, and a dialog without a name is hard to identify with a screen reader, so OpenDesigner may want the title required [inferred].
- **What the sources leave out.** None of the sources cover screen-reader testing, forced colors or color-blind themes; DC-L10-16, DC-L01-20 and Q-gov-07 cover them. Kole Jain's videos treat accessibility almost only as contrast.

## Decisions this informs

- **Q-aud-03** (WCAG level): `wcag22-aa` holds. The sources give 44px (web) and 44pt (iOS) targets [S-L19-004] [S-L19-016] without naming a WCAG level; that this equals the AAA target size (WCAG 2.5.5), part of what `wcag22-aa-plus` offers, is [inferred]. DC-L19-141 proposes dropping `wcag22-a`, which the engine already maps to AA.
- **Q-aud-04** (settings people can change): the OS signals for motion, transparency, contrast and text size are always honored (house musts) [S-L19-020]; this question then only decides extra in-app controls [inferred].
- **Q-color-17** (contrast rule): every pair passes AA, including chips and brand-colored cards [S-L19-051] [S-L19-086].
- **Q-color-01** (brand colors): when the brand color fails with white text, darken it or pair it with a passing color [S-L19-051].
- **Q-color-24** (extra themes): an increased-contrast mode with solid, bordered surfaces [S-L19-020].
- **Q-motion-07** (reduced motion): `replace`, with a 200ms fade [S-L19-020] [S-L19-023]; STD-accessibility-motion-02 settles the question and refuses `remove`.
- **Q-motion-10** (device settings to follow): all of them, baked into components [S-L19-020] [S-L19-016]; `standards.json` lists the question as settled by STD-accessibility-motion-01, -11, -12 and -13.
- **Q-type-17** (text scaling): full scaling, layouts that grow with text [S-L19-020] [S-L19-016]; `none` is refused by STD-accessibility-motion-13.
- **Q-space-03** (target size): 44px hit area for touch on the web, 44pt iOS, 48dp Android [S-L19-004] [S-L19-016].
- **Q-state-03** (focus ring): 2px at a 2px offset, clearly distinct [S-L19-030] [S-L19-001].
- **Q-state-04** (states by device): hover only for fine pointers, press states for touch [S-L19-028] [S-L19-023].
- **Q-comp-01** (component base): headless, accessible primitives (base-ui or Radix) [S-L19-029] [S-L19-005].
- **Q-pattern-01** (dialogs and sheets): always dismissible (STD-accessibility-motion-24; the non-dismissible Vaul drawer shows the failure [S-L19-097]), with a title announced on open; Vaul makes the title optional [S-L19-093], so requiring it is [inferred].
- **Q-motion-09** (haptics): semantic haptics, never alone [S-L19-016].
- **Q-type-12, Q-color-18** (emphasis, links): underline only links; emphasize with weight or color [S-L19-004].
- **Q-depth-04** (glass): every translucent surface has a solid fallback and legible text [S-L19-020].
- **Q-gov-07** (testing matrix): test reduced motion and touch on real devices (STD-accessibility-motion-05, STD-process-review-taste-33) [S-L19-028].

## Visual examples worth showing

- An orange brand button with white text failing WCAG, then a darker orange and a complementary blue that both pass [S-L19-051].
- A save icon on a bright listing photo, with and without a circle behind it [S-L19-054].
- Reduced-motion twins: a sheet sliding in beside the same sheet fading in over 200ms, and a glass toolbar beside its solid-white reduced-transparency version [S-L19-020].
- A tapped button stuck in its hover state on a phone, beside the gated version [S-L19-023] [S-L19-028].
- A small icon button whose 24px glyph sits in an outlined 44px hit area [S-L19-004] [S-L19-016].
- The prototype picker with a focused item, its 2px outline and the one `aria-current` item [S-L19-030].
- Clip-path tabs with the duplicate layer toggled on, labeled `aria-hidden` [S-L19-010].
- A React Native card at default and 200% text size: a hardcoded height clipping the text beside a measured one [S-L19-016].
- A drawer announcing its title, and a non-dismissible drawer with an explicit close button added [S-L19-093] [S-L19-097].
- The animations.dev yellow focus state [S-L19-001].

## Open questions

- For web targets, should OpenDesigner lock 44px hit areas on coarse pointers and keep 24px for fine pointers, and update `guardrails.md` and `engine.py` to say so?
- When a brand color fails contrast, should OpenDesigner darken it (Kole Jain) or keep the exact hex and add a contrast-safe step for text-bearing fills?
- Should the Vaul drawer's Title become required in OpenDesigner components?
- Should Q-type-17's 1.5x cap for fixed chrome stay, given STD-accessibility-motion-13?
- The picker's 40% white focus outline is fixed chrome. Does it pass 3:1 on its own dark background, and if not, who owns the fix?
- No question covers text direction (Sonner's `dir`) or captions for video and motion content. Should either be asked?
- When will `engine.py` emit `prefers-contrast: more` and `prefers-reduced-transparency` blocks and spacing in rem? The 200ms reduced-motion fade now comes from STD-accessibility-motion-02's mapping rather than from the engine's own values.
