# L19 Decision Cards: platforms (stages 02, 04)

Lane: L19 (learning wiki). Area: platforms, covering the topics Mobile app patterns, Desktop and macOS apps and Accessibility (OpenDesigner stages 02 audience and commitments, 04 platforms and devices). Written 2026-09-24.

Built from every verified analysis tagged with these topics in `learn/analysis/` (34 sources), checked against the raw text where a card relies on a detail (the mobile, macOS, Spotify Wrapped and TikTok transcripts, the mobile-native, animate-expo and apple-design skills, and the Raycast passage of "You Don't Need Animations"). Compared with DC-L10-01 to DC-L10-25, DC-L14-01 to DC-L14-14, DC-L03-12, DC-L03-19, DC-L06-14, DC-L08-19, DC-L08-20, DC-L11-19, DC-L13-01, DC-L13-03, DC-L13-11, DC-L13-14, DC-L13-17 and DC-L16-10, with `questions.json`, the stage 02 and 04 files, `engine.py`'s answer mapping, `synthesis/standards.json`, and the L19 cards already written for color, typography and layout. Where those cards already cover a decision (DC-L19-14 appearance set, DC-L19-15 theme-color, DC-L19-17 contrast and transparency settings, DC-L19-32 phone text size, DC-L19-49 moving a desktop screen to a phone, DC-L19-55 whole-card links), these cards point to them instead of repeating them. An adversarial check on 2026-09-27 also compared them with the L19 motion, components and patterns cards written in parallel (DC-L19-90 screen transitions, DC-L19-93 press feedback, DC-L19-96 performance budget and test device, DC-L19-97 gestures, DC-L19-101 libraries, DC-L19-103 hover, DC-L19-117 command menu, DC-L19-119 phone tab bar, DC-L19-129 onboarding) and now points to them where they already own a choice.

How to read the authority: Emil Kowalski's sources are house standards (STD-...), locked. Vaul is a recommended default. Kole Jain's videos are trusted practitioner opinion: a number or an always/never rule that only one video gives is marked "one video" unless another source or existing research agrees. Anything not stated by a source is marked [inferred].

## Sources used

- [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]] (non-negotiable)
- [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]] (non-negotiable)
- [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]] (non-negotiable)
- [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]] (non-negotiable)
- [S-L19-014] [[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]] (non-negotiable)
- [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]] (non-negotiable)
- [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]] (non-negotiable)
- [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]] (non-negotiable)
- [S-L19-021] [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]] (non-negotiable)
- [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] (non-negotiable)
- [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] (non-negotiable)
- [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]] (non-negotiable)
- [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]] (non-negotiable)
- [S-L19-029] [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]] (non-negotiable)
- [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]] (non-negotiable)
- [S-L19-034] [[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]] (non-negotiable)
- [S-L19-092] [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]] (non-negotiable)
- [S-L19-093] [[sources/vaul-api-api-reference-vaul|API Reference – Vaul]] (good-to-have)
- [S-L19-096] [[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]] (good-to-have)
- [S-L19-097] [[sources/vaul-other-other-vaul|Other – Vaul]] (good-to-have)
- [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]] (reference)
- [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you're a beginner]] (reference)
- [S-L19-051] [[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]] (reference)
- [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI's in 8 minutes (beginner friendly)]] (reference)
- [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]] (reference)
- [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]] (reference)
- [S-L19-076] [[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]] (reference)
- [S-L19-077] [[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok's UX is so GOOD it should be ILLEGAL (seriously)]] (reference)
- [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]] (reference)
- [S-L19-086] [[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]] (reference)

Synthesis pages these cards build on: [[synthesis/mobile-app-patterns|Mobile app patterns synthesis]], [[synthesis/desktop-and-macos-apps|Desktop and macOS apps synthesis]] and [[synthesis/accessibility|Accessibility synthesis]].

## Decision Cards

### DC-L19-141: Accessibility floor: WCAG 2.2 AA plus the locked house rules
- **Block path:** Foundations > Accessibility > Conformance target
- **Questions the designer answers:** Which WCAG level do we commit to? Which rules above AA are already locked, whatever we pick? What would "stricter" still add?
- **Options:**
  - **WCAG 2.2 AA plus the house locks** (the current default `wcag22-aa`, reworded): AA contrast and the 24px web target floor (guardrails), plus rules the house standards make "must" at every level. Touch targets are 44x44pt on iOS, 48dp on Android, and small web controls get a 44px hit area for touch [S-L19-016] [S-L19-004]. Pinch zoom is never disabled; inputs stay at 16px or more instead [S-L19-028]. Every animation ships its reduced-motion version, gentler rather than zero [S-L19-016] [S-L19-020]. Reduced transparency and increased contrast are handled as separate signals [S-L19-020]. Layout scales with the user's text size [S-L19-020] [S-L19-016]. Hover styles are gated to fine pointers and touch gets its own press state [S-L19-028], and a haptic is never the only feedback [S-L19-016]. Overlays sit on accessible primitives [S-L19-029] [S-L19-005] and can always be dismissed (STD-accessibility-motion-24; Vaul's non-dismissible drawer shows the failure [S-L19-097]). Visible focus is already a locked guardrail (a 2px ring at a 2px offset, `guardrails.md`); the sources add that focus states should be clearly distinct [S-L19-001] and use the same 2px outline at a 2px offset [S-L19-030].
  - **AA plus stricter rules** (`wcag22-aa-plus`, reworded): what is left once touch targets are locked: 7:1 body text and fewer mid-tone text colors (DC-L01-22), and 44px targets for mouse as well as touch (WCAG 2.5.5, AAA) [inferred]. The 44px touch target in the default is already the AAA size for touch [inferred]. Kole Jain's contrast work (checking colored cards and chips, darkening a brand color that fails with white text) [S-L19-051] [S-L19-086] checks against WCAG without naming a level; it fits AA and adds nothing AAA-specific [inferred].
  - **Level A only** (`wcag22-a`): offered today, but it contradicts the locked floor in AGENTS.md and `guardrails.md`, and `engine.py` already maps it to AA ("AA stays the floor"). The option promises something the system will not do.
- **Visual effect:** AA plus locks: roomy hit areas on touch, a visible focus ring, motion that fades instead of sliding for people who ask, glass that turns solid when transparency is reduced. AA plus stricter: darker secondary text, fewer light grays, a flatter and plainer look [inferred]. Level A: nothing different from AA, because the engine ignores it.
- **Depends on (upstream):** Q-aud-01 (who uses it), Q-aud-02 (what is at stake), Q-plat-01 and Q-plat-02 (which platform rules apply).
- **Affects (downstream):** `size.target.*`, the contrast validator target (`raw.contrastTarget`), focus ring tokens, the reduced-motion and reduced-transparency modes, input text size, `guardrails.md` and DESIGN.md's accessibility section.
- **Token encoding:** existing `size.target.pointer` and `size.target.touch` ($type dimension). The level itself is a validator setting (`raw.contrastTarget` AA or AAA), not a token.
- **Platform notes:** web: 24px pointer targets and 44px touch hit areas built with a pseudo-element [S-L19-004]; iOS 44pt with `hitSlop` when the visual is smaller [S-L19-016]; Android 48dp. Zoom and the 16px input rule are web-only (iOS Safari zooms smaller inputs) [S-L19-028]. In React Native, `allowFontScaling` is on by default, so no height may be hardcoded [S-L19-016].
- **Accessibility constraints:** WCAG 2.2 AA is the locked floor; 2.5.8 (24px), 2.5.5 (44px, AAA), 1.4.4 (resize text).
- **Default + heuristic:** Default `wcag22-aa`, presented as "AA plus the house locks". Offer `wcag22-aa-plus` for money, health and government products [inferred]. Nothing below AA. Rule of thumb: the level question only decides how strict contrast and mouse targets are; touch targets, zoom, motion, transparency, contrast signals and text scaling are not up for choice.
- **Evidence:** [S-L19-001] [S-L19-004] [S-L19-005] [S-L19-016] [S-L19-020] [S-L19-028] [S-L19-029] [S-L19-030] [S-L19-051] [S-L19-086] [S-L19-097]; compared with DC-L11-19, DC-L01-22, DC-L03-12, DC-L10-15.
- **Maps to:**
  - Q-aud-03: remove option `wcag22-a`, or show it as unavailable with the reason "AA is the locked floor", because `engine.py` maps it to AA and AGENTS.md locks AA.
  - Q-aud-03: `wcag22-aa` label becomes "WCAG 2.2 AA, with locked rules for touch targets, zoom, motion and text size" (confirms current default); `wcag22-aa-plus` label becomes "AA plus 7:1 body text and 44px targets for the mouse too" (the "bigger targets" wording is already true for touch).
  - Q-aud-03 new heuristic [inferred]: when Q-aud-02 is `high-trust`, pre-select `wcag22-aa-plus` as the recommendation.
  - Visual sample: the Show strip lists each locked rule with its standard id, for example "Touch targets 44pt / 48dp (STD-mobile-touch-09)".
- **Impact now / as it grows:**
  - *AA plus locks:* now, a little extra layout room for hit areas and one extra CSS block per animation. As it grows, components carry the locks, so new screens inherit them; the risk is a hand-rolled component that skips them, which review catches.
  - *AA plus stricter:* now, a narrower, darker palette. As it grows, every new text color, theme and brand color must pass 7:1, which gets harder with each addition.
  - *Level A:* now, no effect (mapped to AA). As it grows, it only misleads the person who picked it.
- **Standards:** STD-mobile-touch-09, STD-mobile-touch-11, STD-accessibility-motion-01, STD-accessibility-motion-02, STD-accessibility-motion-11, STD-accessibility-motion-12, STD-accessibility-motion-13, STD-accessibility-motion-15, STD-accessibility-motion-16, STD-accessibility-motion-20, STD-accessibility-motion-24, STD-accessibility-motion-27

### DC-L19-142: Device settings the product always follows, and controls inside the app
- **Block path:** Foundations > Accessibility > User settings > Device signals and in-app controls
- **Questions the designer answers:** Which device settings does the product obey without being asked? Which extra controls, if any, live inside the app? Can people rearrange or hide parts of the interface?
- **Options:**
  - **Follow every device signal (always on, not a choice):** reduced motion, reduced transparency and increased contrast as three separate signals, and the user's text size, all built into components [S-L19-020]; in React Native, `useReducedMotion()` or `reduceMotion: ReduceMotion.System`, and layouts measured rather than fixed because text can reach 200% [S-L19-016]; pinch zoom stays available [S-L19-028]; light and dark follow the system "as much as possible" [S-L19-067].
  - **Plus an appearance switch in the app:** Kole Jain's Mac app keeps light and dark settings in a settings popover [S-L19-067]. This differs from DC-L10-17 (Apple: no app-only appearance setting). DC-L19-14 already owns this choice for Q-theme-01.
  - **Plus personalization:** when no single layout fits everyone, let people rearrange controls and hide what they don't use [S-L19-020]; the same Mac app lets people choose which side the quick-save panel opens from [S-L19-067].
  - **Plus a full high-contrast theme** (7:1): an optional extra mode (DC-L19-17, DC-L01-20).
  - **Plus text-size or density controls in the app** (today's `text-size` and `density` options): no source in this area asks for them. An in-app text-size control repeats the device's own text-size setting on native platforms [inferred]; a compact/roomy switch has no device equivalent, so it stays a genuine in-app option (DC-L03-11) [inferred].
- **Visual effect:** Following the signals: people who turn them on get a solid, bordered, non-moving, larger-text version of the same screen, and nobody else sees a change. In-app controls: a settings popover or panel; more choice for people, more combinations to test.
- **Depends on (upstream):** DC-L19-141 (the floor), Q-plat-01 (macOS has no Dynamic Type, DC-L10-07), Q-theme-01.
- **Affects (downstream):** the motion, transparency and contrast token modes, rem-based spacing, a settings screen or popover, the test matrix (Q-gov-07).
- **Token encoding:** semantic-tier modes `motion: full | reduced`, `transparency: full | reduced`, `contrast: standard | more` (DC-L10-16), written on the web as `prefers-reduced-motion`, `prefers-reduced-transparency: reduce` and `prefers-contrast: more` [S-L19-020]. In-app switches reuse the engine's existing `[data-theme]` and `[data-density]` overrides; nothing new.
- **Platform notes:** web reads the three media queries [S-L19-020]; React Native reads the system setting per animation [S-L19-016]; macOS follows the system appearance [S-L19-067].
- **Accessibility constraints:** reduced motion keeps opacity and color changes and drops movement; it is never zero. Text scales to 200%; zoom is never disabled.
- **Default + heuristic:** Default: every device signal followed automatically and never asked about; no extra in-app controls unless Q-theme-01 chose a switch or the product serves groups whose needs clash (then personalization). Rule of thumb: if the device already has a switch for it, the product obeys that switch; an in-app control is only for what the device can't express.
- **Evidence:** [S-L19-016] [S-L19-020] [S-L19-028] [S-L19-067]; compared with DC-L10-16, DC-L10-17, DC-L13-14, DC-L19-14, DC-L19-17.
- **Maps to:**
  - Q-aud-04: new ask "Beyond the device's own settings, which controls should people get inside the app?"; `reduced-motion`, and the device parts of `contrast` and `text-size`, become always-on notes instead of options, because the house standards make them musts.
  - Q-aud-04: new option `personalize` (rearrange or hide controls) [S-L19-020]; new default "none beyond the device settings", replacing "text-size + reduced-motion", which are now automatic.
  - Q-aud-04 visual sample: the preview's mode switcher keeps one toggle per device signal, labeled "always followed", so people can see what each one does.
  - Q-motion-10: confirms "all of them" (the list becomes information, not a choice).
- **Impact now / as it grows:**
  - *Device signals:* now, three CSS blocks (or three runtime checks) and rem spacing. As it grows, every new translucent, moving or fixed-height component must honor them, which review can check.
  - *Appearance switch:* now, a stored preference and a control. As it grows, extra themes join the same switch (DC-L19-14).
  - *Personalization:* now, a settings model and saved layouts. As it grows, every new control needs a place in the customizable set, and support has more layouts to reason about [inferred].
  - *High-contrast theme:* now, one extra mode. As it grows, every new color needs its 7:1 value.
  - *In-app text size:* now, a duplicate control. As it grows, two text-size settings can fight each other [inferred].
  - *In-app density switch:* now, a compact/comfortable token mode. As it grows, every component needs both densities, with hit areas that never shrink (DC-L03-12).
- **Standards:** STD-accessibility-motion-01, STD-accessibility-motion-02, STD-accessibility-motion-11, STD-accessibility-motion-12, STD-accessibility-motion-13, STD-accessibility-motion-27, STD-visual-details-43, STD-visual-details-64

### DC-L19-143: Mixed input: hover is an extra, press feedback is for everyone
- **Block path:** Foundations > Interaction > Input capability > Hover and press
- **Questions the designer answers:** Will the same screen be used with a finger and a mouse, sometimes on the same device? What happens to anything that only shows on hover? When does a tap show that it landed?
- **Options:**
  - **Mixed input, gated by capability (the house rule for the web):** iPads with trackpads, laptops with touchscreens and phones with a mouse mean touch and mouse are not exclusive. Hover styles live only inside `@media (hover: hover) and (pointer: fine)`, never behind a user-agent, screen-width or JavaScript touch check [S-L19-028]. Press feedback fires when the finger lands (`:active`, or `pointerdown` in JavaScript, never `click`): scale 0.97 over 100-160ms with ease-out [S-L19-028]. Highlight on touch-down, commit on touch-up, and about 10px of hit padding so a drifting finger keeps its press [S-L19-020].
  - **Touch only (native phone app):** there is no hover, so every hover affordance moves to press, position or nothing, redesigned rather than ported [S-L19-016]. Pressables scale to 0.97 in 100-150ms (the recipe uses 120ms), with `hitSlop` to reach 44pt and `pressRetentionOffset` for drift [S-L19-016] [S-L19-015]. On mobile, a slightly darker gray on press makes it "feel like you're actually pressing into something" [S-L19-051].
  - **Pointer first (desktop):** hover may add hints, such as an arrow fading in on a card that is a link [S-L19-075] or a tooltip on an unclear icon [S-L19-045], but only as an extra with a visible or keyboard path too (DC-L13-03: never hover-only for anything essential; DC-L19-55 for card links).
  - **Device sniffing:** ruled out [S-L19-028].
- **Visual effect:** Gated hover: desktops keep hover lifts and tints; phones never show a button stuck in its hover state after a tap [S-L19-028]. Press scale: the whole button, label and icon included, gives under the finger, which reads as physical [S-L19-016]. Touch-only redesign: actions that hid behind hover become visible icons or rows [inferred], or a long-press menu, the mobile equivalent of the right click [S-L19-053].
- **Depends on (upstream):** Q-plat-01, Q-plat-02 (devices), DC-L19-141.
- **Affects (downstream):** every interactive component's state rules, tooltips (need a non-hover trigger), whole-card links, `size.target.*`, Q-state-04.
- **Token encoding:** existing `size.target.pointer` (24) and `size.target.touch` (44 or 48), $type dimension. Press feedback as motion tokens, for example `motion.press.scale` ($type number, 0.97) and `motion.press.duration` ($type duration, 100ms) [inferred names]. Hover gating is an output rule of the CSS export, not a token.
- **Platform notes:** web: remove the tap highlight globally only together with an `:active` state on every tappable, and put `touch-action: manipulation` on tappables to remove the tap delay [S-L19-028]. React Native: Pressable with a CSS transition [S-L19-016]. Android ripple only in a Material-styled app (DC-L19-147).
- **Accessibility constraints:** WCAG 1.4.13 for content shown on hover; 2.5.8 targets; whatever hover reveals must also be reachable by keyboard focus [inferred].
- **Default + heuristic:** Default for Q-plat-03: touch + pointer + keyboard, treated as possibly on the same device, on every web surface; native phone apps are touch plus the operating system's keyboard and switch access [inferred]. Rule of thumb: design the touch version first; hover can only add, never hold something people need.
- **Evidence:** [S-L19-015] [S-L19-016] [S-L19-020] [S-L19-028] [S-L19-045] [S-L19-051] [S-L19-053] [S-L19-075]; compared with DC-L10-15, DC-L14-06, DC-L03-12, DC-L13-03, DC-L19-93, DC-L19-103.
- **Maps to:**
  - Q-plat-03: new heuristic and Use/avoid line "hover never carries anything essential; gate it by capability, never by device" [S-L19-028]; the default text becomes "touch + pointer + keyboard, possibly on the same device" (confirms the current default set).
  - Q-plat-03 visual sample: a phone screen where a tapped button stays in its hover state, beside the gated version, and a button scaling to 0.97 as the finger lands [S-L19-028].
  - Q-state-04: no separate change here. Its current default (all eight states, overlays for hover and press) gains the press scale from DC-L19-93 and the gated hover from DC-L19-103; this card only adds that the same device may be used by finger and mouse, which is what the `per-input` option describes.
  - Engine: the preview's ungated `:hover` rules are already recorded as a conflict under STD-accessibility-motion-15; no new note.
- **Impact now / as it grows:**
  - *Mixed input:* now, one media query around every hover rule and an `:active` rule per control. As it grows, new devices (touch laptops, tablets with keyboards) just work, because nothing depends on the device name.
  - *Touch only:* now, hover ideas must be redesigned, not copied. As it grows, a later web or desktop version adds hover as an extra without changing the base.
  - *Pointer first:* now, richer hover hints. As it grows, every hover hint needs a touch and keyboard twin, or it becomes a trap when touch use grows.
  - *Device sniffing:* now, it seems to work on the designer's devices. As it grows, it breaks on each new mixed-input device.
- **Standards:** STD-mobile-touch-02, STD-mobile-touch-03, STD-mobile-touch-05, STD-mobile-touch-06, STD-mobile-touch-08, STD-mobile-touch-09, STD-mobile-touch-30, STD-accessibility-motion-15, STD-components-toasts-drawers-72

### DC-L19-144: Web product on phones: installed-app feel or scrolling document
- **Block path:** Platforms > Web > Mobile web posture
- **Questions the designer answers:** When people open the web product on a phone, should it feel like an installed app or like a page? Will people add it to their home screen? Does a marketing site sit next to the app?
- **Options:**
  - **App shell (feels installed):** `overscroll-behavior: none` on the root, so the page no longer rubber-bands or pull-to-refreshes, with `contain` on every inner scroller; a `100dvh` shell that tracks the visible area; control text unselectable; bottom-pinned UI padded with `env(safe-area-inset-bottom)`; `interactive-widget=resizes-content` so the Android keyboard shrinks the layout as on iOS [S-L19-028]. A drawer people drag down needs the same shell (`100dvh`, no page overscroll) [S-L19-028], and keeps its inputs above the keyboard (Visual Viewport API, or Vaul's `repositionInputs`) [S-L19-005] [S-L19-096].
  - **Scrolling document (marketing, docs, content):** keep the page's own overscroll and pull-to-refresh, which is "fine on a document"; heroes use `min-height: 100svh`, because `dvh` shifts layout mid-scroll [S-L19-028].
  - **Installed PWA:** the app shell plus `apple-mobile-web-app-status-bar-style` and the manifest's `theme_color` and `background_color`, set as one decision with `theme-color`; tested in standalone mode, which changes the viewport, safe areas and status bar [S-L19-028].
  - **Per surface:** app routes get the shell, marketing routes stay documents [inferred from the split in S-L19-028].
  - **In every option:** the mobile baseline ships before the first component: `viewport-fit=cover` and `interactive-widget=resizes-content` in the viewport meta, one `theme-color` per scheme (DC-L19-15), no tap highlight, `-webkit-text-size-adjust: 100%`, 16px inputs, `touch-action: manipulation`, gated hover [S-L19-028]. The skills README lists these as the fixes a web app needs once it runs on a phone [S-L19-014].
- **Visual effect:** App shell: the page stops bouncing as a whole, bottom bars sit above the URL bar and home indicator, and the status bar matches the header; it feels installed rather than "a website in a browser" [S-L19-028]. Document: scrolls and refreshes like the web. On the mobile web, bottom navigation must also clear the browser bar, which an app-only product never has to think about [S-L19-076].
- **Depends on (upstream):** Q-scope-01 (product app, marketing, docs), Q-plat-01 (`web`), Q-plat-02 (phone in scope), Q-theme-01.
- **Affects (downstream):** the CSS export's root rules and viewport meta, the app-shell template, drawers and sheets, bottom navigation, full-height heroes, the PWA manifest.
- **Token encoding:** none (platform-layer output of the web export). The `theme-color` values come from the header surface token (DC-L19-15). An export setting such as `mobileWeb: app-shell | document | pwa | per-surface` could live under `$extensions` [inferred].
- **Platform notes:** web only; native apps get these behaviors from the OS. iOS Safari zooms into inputs under 16px and does not zoom back out; Chrome device emulation reproduces none of these bugs [S-L19-028].
- **Accessibility constraints:** never `user-scalable=no` or `maximum-scale=1`; text that is content stays selectable; safe-area padding keeps controls out of the notch and home-indicator zones [S-L19-028].
- **Default + heuristic:** Default: derived from Q-scope-01 and shown as a confirm chip: `product-app` gives an app shell, `marketing` or `docs-content` gives a document, both give per surface; PWA only when the person says people will install it. The baseline always ships when phones are in scope. Rule of thumb from the source: own scroll areas, a drawer people drag down, or a canvas means app shell; reading top to bottom means document [S-L19-028].
- **Evidence:** [S-L19-005] [S-L19-014] [S-L19-028] [S-L19-076] [S-L19-096]; compared with DC-L10-01, DC-L10-11, DC-L10-18, DC-L19-15.
- **Maps to:**
  - New question (proposed Q-plat-12, zoom 2, show if Q-plat-01 includes `web` and Q-plat-02 includes `phone`; Q-plat-11 is already proposed by DC-L19-96): "On phones, should your web product feel like an installed app or like a page people scroll?" with options `app-shell`, `document`, `pwa`, `per-surface`; default derived from Q-scope-01.
  - Q-plat-01 `web` option text gains "on phones it ships the mobile baseline first" (STD-mobile-touch-21).
  - Engine: the CSS export and `preview.html` should write the baseline; the preview's viewport meta is already recorded as a conflict under STD-mobile-touch-21.
  - Visual sample: a bottom button hidden under the URL bar at `100vh` beside the `100dvh` version, and a header padded under the notch [S-L19-028].
- **Impact now / as it grows:**
  - *App shell:* now, a handful of root rules and one layout height. As it grows, every new scroller, sheet and bottom bar must follow them (contain, dvh, safe-area padding), and each is a one-line check.
  - *Document:* now, almost nothing beyond the baseline. As it grows, if app-like features appear (drag-down drawers, canvases), the page starts fighting pull-to-refresh and must move to per surface.
  - *PWA:* now, manifest and status-bar decisions plus standalone testing. As it grows, installed users expect offline behavior and app-like navigation [inferred].
  - *Per surface:* now, two sets of root rules. As it grows, each new route must be tagged app or document, or it inherits the wrong one.
- **Standards:** STD-mobile-touch-10, STD-mobile-touch-14, STD-mobile-touch-15, STD-mobile-touch-16, STD-mobile-touch-17, STD-mobile-touch-20, STD-mobile-touch-21, STD-accessibility-motion-27, STD-components-toasts-drawers-45

### DC-L19-145: Thumb reach: where frequent actions sit on a phone
- **Block path:** Foundations > Layout > Reach zones (phone)
- **Questions the designer answers:** On a phone, which actions sit at the bottom within easy thumb reach, and which may stay at the top? Does the main action get its own spot? Do we plan for right- or left-handed use?
- **Options:**
  - **Bottom-weighted (reach first):** the important controls go at the bottom, where they are easier to reach, even though pushing everything to the top looks good; the close X can stay at the top [S-L19-076]. TikTok's bottom navigation follows the same idea as its swipe: a large target with almost no thumb travel [S-L19-077]. A floating bottom bar of three or four links, five at most, keeps every target over 44 [S-L19-053]. This matches DC-L10-09 (controls in the middle and bottom are easier to reach).
  - **Top for rare and contextual actions:** a bell and a more menu at the top, changing with the page; while a note is being edited, the nav bar hides and formatting and sharing take the top [S-L19-053].
  - **Main action broken out of the bar:** a floating bar with "the important action broken out" is described as today's typical bottom bar [S-L19-053]. Differs from [S-L19-075]: a raised, circled add button draws attention to the tab people use least, so drop it into line with the others. The two agree when the broken-out action is the most used one, such as search or quick capture, and disagree when it is a rarely used "add" [inferred]. DC-L19-119 (the phone tab bar) already owns this choice and reaches the same reconciliation; this card only adds the reach reasoning.
  - **Side-edge action column:** TikTok lines up its action icons on the right for "the 70 to 80%" of people who are right-handed [S-L19-077]. One video's figure with no second source; the L13 law table's Fitts's law row warns that screen-edge targets help mouse users but hurt touch users (research/L13-ux-laws-heuristics.md).
  - **One huge target for the dominant action:** TikTok's swipe target is almost the whole screen [S-L19-077]. The video names Hick's law, but its argument (target size and distance) is Fitts's law, as its analysis notes.
- **Visual effect:** Bottom-weighted: a quiet top (title, close, status) and a busy bottom; one-handed use feels effortless. Top-heavy: clean in a screenshot, but every action is a stretch [S-L19-076]. An edge column: content fills the screen and controls hug one side, like a video feed [S-L19-077].
- **Depends on (upstream):** Q-plat-02 (phone first-class), Q-layout-04 (navigation container), Q-aud-04 `situational` (one hand busy), DC-L19-144 (the mobile web browser bar).
- **Affects (downstream):** bottom bar, floating action button, sheet action rows, toolbars, the phone app-shell template, safe-area padding.
- **Token encoding:** none new; the bar uses the existing `size.target.touch` and safe-area padding. A builder lint rule "frequent actions in the lower part of compact screens" is a proposal [inferred].
- **Platform notes:** mobile web: the browser bar can cover bottom navigation [S-L19-076]; use a `100dvh` shell and safe-area padding (STD-mobile-touch-10, STD-mobile-touch-16). The iOS tab bar floats and can minimize on scroll (DC-L10-09).
- **Accessibility constraints:** 44pt / 48dp targets; spreading tab icons a little widens each click area, and tab labels, when used, must be dark enough to read [S-L19-075].
- **Default + heuristic:** Default on phones: bottom-weighted, with navigation and the one or two most frequent actions at the bottom and rare or global actions (settings, notifications, close) at the top; break the main action out of the bar only when it is also the most used; no handedness-specific layout. Rule of thumb: rank actions by how often they are used; the more often, the lower (and, for the one dominant action, the bigger [inferred from S-L19-077]).
- **Evidence:** [S-L19-053] [S-L19-075] [S-L19-076] [S-L19-077]; compared with DC-L10-09, DC-L14-05, DC-L03-19, DC-L08-19, DC-L19-49, DC-L19-119.
- **Maps to:**
  - Q-layout-04: new heuristic for phones: how often an action is used decides how low it sits [S-L19-076] [S-L19-077]. The companion rule "the main action leaves the bar only if it is the most used" is DC-L19-119's heuristic for the same question; apply it once.
  - Q-aud-04 `situational` ("one hand busy"): new heuristic [inferred]: when picked, the builder applies the bottom-weighted rule and flags primary actions anchored at the top.
  - Q-plat-02 visual sample: a thumb-reach overlay on the draft phone screen, next to the Spotify Wrapped redesign with share and volume moved to the bottom [S-L19-076] and TikTok's bottom bar and right-edge column [S-L19-077].
- **Impact now / as it grows:**
  - *Bottom-weighted:* now, the bottom of the screen needs careful spacing and safe-area padding. As it grows, the bottom fills up; new actions compete for the few low slots, which forces a ranking.
  - *Top for rare actions:* now, a calm top bar. As it grows, the top becomes the place for everything that doesn't fit below, so it needs a "more" menu.
  - *Main action broken out:* now, a strong signal for one action. As it grows, it is hard to take back if the most used action changes.
  - *Side-edge column:* now, maximum content area. As it grows, left-handed and accessibility users may ask for a mirrored layout [inferred].
  - *One huge target:* now, the simplest possible screen. As it grows, it only works while the product keeps choosing well for people (see DC-L19-146).
- **Standards:** STD-mobile-touch-09, STD-mobile-touch-10, STD-mobile-touch-16, STD-visual-details-42

### DC-L19-146: New interactions: where they may appear and what backs them up
- **Block path:** Patterns > Interaction > Convention vs novelty > Gestures and signature moments
- **Questions the designer answers:** Which interactions may be new or gesture-driven, and which must work the way people already know? If an action is a swipe, what does someone do who doesn't know the swipe? Where does the product's one "surprise" go?
- **Options:**
  - **Usual behavior, your own look** (`custom-skin`, the current default): familiar controls and platform navigation, with the brand in the visuals. Break a familiar pattern only when you can prove the new one is better, then test it [S-L19-020]. Don't replace a layout people have used for years; evolve it, as with Spotify Wrapped's eight-year-old format [S-L19-076]. Lean on gestures the audience already knows, such as tap to pause for a Gen Z audience [S-L19-076].
  - **Gesture shortcuts on top of visible controls:** a swipe that replaces a button (swipe to add a friend) or reveals more, with buttons "for the uninitiated", as Gmail offers delete by swipe or by button [S-L19-035]; the video hedges the long-press fallback as "probably" good UX, so "every gesture has a visible twin" is the house reading (WCAG 2.5.7 in DC-L10-15, and DC-L19-97), not the video's rule. Teach a swipe before relying on it (swipe back, swipe up to search as in Slack, long press as the mobile right click) [S-L19-053]. Gesture mechanics (momentum, thresholds, rubber-banding) belong to DC-L19-97.
  - **One dominant gesture, other options removed:** TikTok's swipe up with auto-snap and autoplay, after an onboarding that only asks for interests and gives a very short tutorial [S-L19-077]. It only works when the product learns what people want; the L13 law table warns that Hick's law is not a reason to delete navigation (research/L13-ux-laws-heuristics.md).
  - **Signature transitions:** a card that expands into a page with an elastic snap, an image that zooms into the next page's hero, a circle wrap between onboarding slides [S-L19-035]; direction that carries meaning, with tools sliding up from the bottom as temporary and onboarding screens sliding in from the left as progress [S-L19-084]. Differs from the house standards for native apps: screen changes stay on the native stack at the platform's duration, tabs never slide, and a custom stack animation must set `animationMatchesGesture`. Delight motion belongs to rare moments such as onboarding, which is also where Kole Jain puts the captivating moment on mobile [S-L19-084].
  - **Drag-only confirmation:** a swipe-to-confirm slider for sending an email (Resend) or buying crypto, because a slider is harder to trigger by accident than a button [S-L19-035]. It is drag-only, so WCAG 2.5.7 still needs another way [inferred]. House alternatives: hold-to-confirm (a 2s linear fill while pressed, a 200ms release) for destructive actions a plain click fires too easily, or undo for slips and a confirmation only for truly destructive, irreversible actions.
- **Visual effect:** Custom skin: instantly familiar, with the brand in the look. Gesture shortcuts: faster for regulars, invisible to newcomers unless taught. One dominant gesture: almost no chrome, content fills the screen [S-L19-077]. Signature transitions: memorable continuity between screens [S-L19-035]. Swipe or hold to confirm: a deliberate, heavier action.
- **Depends on (upstream):** Q-plat-05 (posture), Q-brand-04 (how expressive), Q-aud-02 (what is at stake), Q-plat-03 (inputs).
- **Affects (downstream):** swipe rows, sheets, onboarding, confirmation patterns, motion for rare moments, the accessible alternatives for every gesture.
- **Token encoding:** none (behavior rules). Signature motion uses the existing motion tokens. A builder lint rule "every gesture-driven action names its non-gesture twin" is a proposal [inferred].
- **Platform notes:** React Native: rows that reveal actions use `ReanimatedSwipeable`; a pan inside a scroll view declares its axis (for example `activeOffsetX([-10, 10])`) [S-L19-015]. Web: `touch-action` set per gesture surface (STD-mobile-touch-18).
- **Accessibility constraints:** WCAG 2.5.7 (dragging movements) and 2.5.1 (pointer gestures) need a single-pointer alternative, such as a tap or click [inferred mapping]; Kole Jain's swipe video does not discuss assistive technology or reduced motion (its analysis says so); every signature transition ships its reduced-motion version.
- **Default + heuristic:** Default `custom-skin`: gestures only as shortcuts with a visible twin; one signature moment, in onboarding or a rare success state, never in everyday navigation. On native apps that moment lives inside one screen or uses the native stack's own options with `animationMatchesGesture`, never a JavaScript-rebuilt screen transition (STD-mobile-touch-42, STD-mobile-touch-44; DC-L19-90). Rule of thumb: if a newcomer can't find the action without being told, it needs a visible control; if people see the motion 100 or more times a day, it belongs to the platform.
- **Evidence:** [S-L19-015] [S-L19-020] [S-L19-035] [S-L19-053] [S-L19-076] [S-L19-077] [S-L19-084]; compared with DC-L13-17, DC-L10-14, DC-L10-15, DC-L19-90, DC-L19-97 and the L13 law table.
- **Maps to:**
  - Q-plat-10: new heuristic "every gesture has a visible twin; evolve familiar formats instead of replacing them" [S-L19-035] [S-L19-076]; `novel-core` text gains "backed by a visible control, proven better and tested" [S-L19-020] (confirms current default `custom-skin`).
  - Q-plat-10 visual sample: Gmail's delete by swipe and by button; Resend's swipe to send beside a hold-to-confirm button [S-L19-035].
  - Q-plat-03: confirms the WCAG 2.5.7 Use/avoid line and extends it to swipe-to-confirm.
  - Q-motion-06 (motion area): follows DC-L19-90's proposed default: `container-transform` only for occasional drill-ins on the web, and on native kept inside one screen; no separate change from this card.
- **Impact now / as it grows:**
  - *Custom skin:* now, less novelty to design and test. As it grows, the product stays learnable as features pile up.
  - *Gesture shortcuts:* now, each gesture needs its twin and a way to teach it. As it grows, regulars get faster while newcomers are never locked out.
  - *One dominant gesture:* now, a very simple main screen. As it grows, every new feature fights for a place the design has removed, and the product depends on its recommendations staying good.
  - *Signature transitions:* now, custom motion work on the native stack. As it grows, each one adds reduced-motion and back-gesture cases to maintain; keeping them in rare moments caps the cost.
  - *Drag-only confirmation:* now, safe against accidental taps. As it grows, it fails keyboard, switch and voice users unless the alternative exists.
- **Standards:** STD-visual-details-36, STD-visual-details-37, STD-visual-details-40, STD-mobile-touch-18, STD-mobile-touch-41, STD-mobile-touch-42, STD-mobile-touch-44, STD-when-to-animate-05, STD-when-to-animate-09, STD-when-to-animate-14, STD-components-toasts-drawers-77, STD-easing-duration-12, STD-accessibility-motion-01

### DC-L19-147: What stays native, whatever the look
- **Block path:** Platforms > Strategy > Platform-owned pieces
- **Questions the designer answers:** Which parts of a native app are always the platform's own, whatever our brand look? Does press feedback follow Android's ripple or our own? When the web offers the same pieces, how native must they behave?
- **Options:**
  - **The platform owns navigation and system surfaces (house rule for React Native and Expo):** native stack screen changes at the platform's duration (iOS push is 350ms), `formSheet` for a sheet that is its own screen, NativeTabs for the tab bar, `Link.Menu` and `Link.Preview` for context menus and press-and-hold previews (iOS), `headerLargeTitleEnabled` for large-title headers (iOS), RefreshControl for pull to refresh, hand-rolled only when it is a signature interaction [S-L19-016]. Form sheets differ by platform: Android caps detents at three and shows no grabber, so a sheet keeps single-screen content and a drag cue of its own [S-L19-015].
  - **The brand owns what happens inside a screen** (DC-L10-14's split, which the source's rules fit [inferred]): press feel, in-content springs and haptics mapped to moments; in a custom-designed app, iOS and Android get the same 0.97 press scale [S-L19-016].
  - **Material idiom on Android:** the ripple, only in a Material-styled app [S-L19-016].
  - **Web versions of native pieces:** they match the behavior people expect from the OS, "invisible" details included; Vaul models the iOS sheet and is built on Radix Dialog [S-L19-005]. On macOS, the system share button appears in almost every app and the window buttons sit in the app's own bar [S-L19-067]; close is always top-left [S-L19-020].
  - **JavaScript rebuilds of screen transitions, tab bars or sheets:** ruled out in React Native by the house standards, including under `brand-first`. Kole Jain's custom page transitions [S-L19-035] have to stay inside one screen or use the native stack's own options (DC-L19-146, DC-L19-90).
- **Visual effect:** Platform-owned pieces look and move like every other app on the phone and pick up OS redesigns such as Liquid Glass by rebuilding (DC-L10-02, DC-L10-13). The brand still shows in color, type, press feel and in-screen motion. The same press scale on both platforms gives one consistent feel; the ripple reads as Material.
- **Depends on (upstream):** Q-plat-05 (posture), Q-plat-08 (stack), Q-plat-06 (controls).
- **Affects (downstream):** navigation, sheets, tab bar, menus, pull to refresh, swipe rows, press feedback, haptics (Q-motion-09).
- **Token encoding:** none for platform-owned pieces (delegated to the OS, as DC-L10-14 says). Brand micro-motion as tokens: press scale ($type number) and duration ($type duration, 100-150ms), springs stored as duration and damping ratio [S-L19-016].
- **Platform notes:** `Link.Menu`, `Link.Preview` and `headerLargeTitleEnabled` are iOS-only; NativeTabs lives under `expo-router/unstable-native-tabs` and may change [S-L19-016]. The sources say nothing about Flutter, which draws its own widgets (DC-L10-21).
- **Accessibility constraints:** native pieces carry screen-reader semantics (DC-L10-13); under reduced motion, native stack changes become a fade; a haptic is never the only feedback [S-L19-016].
- **Default + heuristic:** Default for every posture in React Native: the platform owns navigation, sheets, tabs, menus and pull to refresh; the brand owns the look and the motion inside screens; one press scale on both platforms unless the app is Material-styled. This confirms DC-L10-02's hybrid rule and DC-L06-14's 80/20; in React Native it narrows `brand-first` to "brand look on native behavior" [inferred], while other stacks keep DC-L10-02's options. Rule of thumb: if people's thumbs already know it from every other app, don't rebuild it.
- **Evidence:** [S-L19-005] [S-L19-015] [S-L19-016] [S-L19-020] [S-L19-035] [S-L19-067]; compared with DC-L10-02, DC-L10-13, DC-L10-14, DC-L10-21, DC-L06-14, DC-L19-101.
- **Maps to:**
  - Q-plat-05: confirms current default `hybrid`. The `brand-first` label stays (it also serves Flutter and other stacks the house standards don't cover, DC-L10-21); when Q-plat-08 is `react-native`, it shows a note: "In React Native your look runs on the platform's own navigation, sheets and tabs; the house standards don't rebuild those (STD-mobile-touch-41, STD-mobile-touch-42)."
  - Q-plat-06: confirms current default `system`; new note under `restyled` and `custom`: "press feedback: the same scale on iOS and Android; ripple only in a Material-styled app" [S-L19-016].
  - Q-motion-09: confirms `os-nav-brand-micro`.
  - Visual sample: one screen on iOS and Android with native sheet and tab bar, both pressing to 0.97.
- **Impact now / as it grows:**
  - *Platform-owned pieces:* now, less custom code and fewer look choices in chrome. As it grows, each OS redesign arrives by rebuilding, not redesigning.
  - *Brand inside screens:* now, a small set of motion tokens. As it grows, those tokens are the brand's feel on every new screen and platform.
  - *Material idiom:* now, a native Android feel. As it grows, iOS and Android press feel drift apart.
  - *Web versions:* now, a primitive (base-ui) plus Vaul's drawer behaviours instead of custom work. As it grows, base-ui updates arrive by upgrading, but Vaul is unmaintained (its README), so the drawer behaviours become the team's own code to keep (DC-L19-101).
  - *JS rebuilds:* ruled out; they would stutter and drift from each OS update.
- **Standards:** STD-mobile-touch-41, STD-mobile-touch-42, STD-mobile-touch-44, STD-mobile-touch-51, STD-mobile-touch-67, STD-components-toasts-drawers-59, STD-components-toasts-drawers-60, STD-accessibility-motion-04, STD-accessibility-motion-20, STD-visual-details-36, STD-visual-details-50

### DC-L19-148: Build stack and the house toolkit that comes with it
- **Block path:** Platforms > Implementation > Build stack and toolkit
- **Questions the designer answers:** What will you build the UI with, and which libraries, settings and code standards come with that choice? What happens when the stack is outside what the house sources cover?
- **Options:**
  - **React on the web:** one library per job from the curated list: base-ui for dialogs, popovers, menus and selects (never a `div`-based dialog), cmdk for ⌘K menus, Sonner for toasts, motion only for springs, layout and exit animations (plain CSS for a simple hover or fade), dnd kit, Virtuoso for 1,000+ rows, zustand, clsx or cva, next-themes [S-L19-029]. Drawers are not on the curated list: build them on the dialog primitive with Vaul's behaviours as the spec [S-L19-005] [S-L19-093]; Vaul itself is unmaintained (its README), so flag that before adding it as a dependency (DC-L19-101; STD-visual-details-55 never installs an abandoned package). The mobile baseline when phones are in scope (DC-L19-144).
  - **React Native with Expo:** Reanimated 4 with react-native-worklets (New Architecture), Gesture Handler (never PanResponder), expo-router for the native stack, sheets, tabs and menus, expo-haptics, react-native-keyboard-controller with KeyboardProvider at the root, Lottie only for illustration, Skia for very large scenes; install with `npx expo install`; set `CADisableMinimumFrameDurationOnPhone` so ProMotion iPhones run at 120fps [S-L19-016] [S-L19-015].
  - **SwiftUI and Swift:** the write-swift skill sets the code standard (Swift 6.3 baseline, main actor by default for app modules, value types first, gesture animations started on the event's frame) [S-L19-034] [S-L19-014]. The design sources give nothing SwiftUI-specific for components.
  - **Vue, Angular, Svelte, web components, Flutter, Compose, .NET MAUI:** no source in this area; the curated list is React-centric and the Expo stack is React Native-only. The builder falls back to DC-L10-19, DC-L10-20 and DC-L10-21 and says it has left the curated list [S-L19-029].
- **Visual effect:** none directly. The toolkit decides how sheets, toasts and menus feel (Sonner's stacked toasts, a native `formSheet`) and whether motion runs at 120fps or drops frames on an older Android [S-L19-016].
- **Depends on (upstream):** Q-plat-01, Q-plat-05, Q-comp-01, the team's existing code (`package.json`).
- **Affects (downstream):** generated component code, Q-comp-01's base, motion implementation, which skills the AGENTS snippet points to, DESIGN.md's "built with" section, export targets (DC-L10-22).
- **Token encoding:** none (implementation). Tokens reach each stack through DC-L10-22's outputs; React Native springs are stored as duration and damping ratio [S-L19-016].
- **Platform notes:** `Link.Menu` and `Link.Preview` are iOS-only; Reanimated 4 needs the New Architecture; the library picks are pinned to one commit of the skills repository and may change (analysis caveats).
- **Accessibility constraints:** base-ui and Radix handle focus management, trapping and dismissal [S-L19-029] [S-L19-005]; Sonner keeps its "Notifications" label and the Alt+T hotkey [S-L19-021]; React Native reads reduced motion per animation [S-L19-016].
- **Default + heuristic:** Default: React gives the curated list; React Native gives the Expo stack; SwiftUI gives the write-swift standard; any other stack is recorded with a plain note that the house toolkit doesn't cover it. Rule of thumb: read `package.json` first and keep a library the project already has; name one library per job, never a menu.
- **Evidence:** [S-L19-005] [S-L19-014] [S-L19-015] [S-L19-016] [S-L19-021] [S-L19-029] [S-L19-034] [S-L19-093]; compared with DC-L10-19, DC-L10-20, DC-L10-21, DC-L10-22, DC-L19-101 (which owns the per-part library picks for React web).
- **Maps to:**
  - Q-plat-08: each option gains a one-line "comes with" note as listed above (new option text); confirms current default `react` for the web.
  - Q-comp-01: cross-reference: its React default names React Aria, which is outside the curated list (conflict already recorded under STD-visual-details-55).
  - AGENTS snippet and DESIGN.md (proposed): name the toolkit for the chosen stack so later sessions don't pick competitors [inferred].
- **Impact now / as it grows:**
  - *React:* now, fewer build-vs-buy debates. As it grows, one list keeps many contributors on the same libraries; a library's change of direction affects everything at once.
  - *React Native:* now, a fixed setup cost (root providers, New Architecture, the 120fps flag). As it grows, motion stays on the UI thread as screens multiply.
  - *SwiftUI:* now, a code standard without component guidance. As it grows, component decisions come from DC-L10-20 and the design cards, not from the toolkit.
  - *Other stacks:* now, no house toolkit. As it grows, the team maintains its own list and should record it as an owner input [inferred].
- **Standards:** STD-visual-details-55, STD-visual-details-56, STD-visual-details-57, STD-accessibility-motion-16, STD-accessibility-motion-23, STD-mobile-touch-33, STD-mobile-touch-38, STD-mobile-touch-39, STD-mobile-touch-51, STD-swift-02, STD-swift-17

### DC-L19-149: Desktop app: a window people visit, or a presence where they work
- **Block path:** Platforms > Desktop > App presence
- **Questions the designer answers:** Do people come to the desktop app's window to work, or should it also appear where they already are? What is the one thing they need while they are in another app?
- **Options:**
  - **Destination window only:** the main window holds everything and people switch to it to act [inferred effect; the source argues against this for utility apps].
  - **Main window plus a shortcut panel:** a global shortcut (Command Shift S in the example) opens a minimal panel over whatever app is in front: no window buttons, a drop area, an input, buttons with shortcut hints and a native blur; Enter turns it into a toast that leaves the screen while the save finishes in the background [S-L19-067]. Modeled on Spotlight (Command Space) and Raycast [S-L19-067].
  - **Ambient presence:** pop-ups triggered by context (Notion's meeting pop-up), a strip along a screen edge (Paste), popovers and notifications [S-L19-067].
  - **How the panel appears:** the video's panel slides in and out [S-L19-067]. Differs from the house standards: something opened hundreds of times a day, like Raycast, has no open animation at all, which Emil calls the optimal experience [S-L19-012]; keyboard-started actions change instantly. The panel appears instantly and the feedback is the state change itself; Escape closes it instantly too. On Enter the panel likewise closes at once, and the toast that confirms the save is a separate notification that may enter as toasts do [inferred reading of STD-when-to-animate-06].
- **Visual effect:** Window only: a classic app, fine for deep work. Shortcut panel: the app feels part of the Mac, "a system exactly where you need it" [S-L19-067], with a tiny glass footprint. Ambient: the most native feel, but interruptive if overused [inferred].
- **Depends on (upstream):** Q-plat-01 `desktop`, the desktop shell (DC-L10-24; the example app was built from web front-end code turned into a native Mac app [S-L19-067]), Q-scope-01.
- **Affects (downstream):** a quick-panel component, a toast that doubles as completion feedback, the keyboard layer (DC-L19-151), the blur and its solid fallback, onboarding that teaches the shortcut, optimistic saves with a failure path (DC-L13-01).
- **Token encoding:** none new; the panel uses existing surface and material tokens, and its blur needs its solid twin (`color.surface.glass-fallback`, DC-L19-17).
- **Platform notes:** macOS models: Spotlight, Raycast, Paste [S-L19-067]. Electron exposes vibrancy and hidden title bars (DC-L10-24). Windows has no source in this wiki.
- **Accessibility constraints:** the global shortcut must not override standard OS shortcuts (DC-L13-17); reduced transparency turns the blur solid; the panel also needs a non-keyboard way in, such as a menu bar or dock item [inferred].
- **Default + heuristic:** Default: a destination window [inferred; the video argues that a native-feeling utility should not be a destination, but most desktop apps are not capture utilities]; add one shortcut panel when the core task happens while people are in other apps, as with capturing inspiration mid-work [S-L19-067] (search and clipboard, after Spotlight and Paste, are [inferred] extensions); ambient pop-ups only for time-bound events such as Notion's meeting pop-up [S-L19-067] [inferred scope]. Rule of thumb: if the task starts in another app, the product should come to that app.
- **Evidence:** [S-L19-012] [S-L19-067]; compared with DC-L10-24, DC-L13-17, DC-L13-01.
- **Maps to:**
  - New question (proposed Q-plat-13, zoom 2, show if Q-plat-01 includes `desktop`): "Is your desktop app a window people go to, or should it also appear where they already work?" with options `window-only`, `shortcut-panel`, `ambient`; default `window-only` [inferred default].
  - Visual sample: a Spotlight-style quick panel over another app, turning into a toast on Enter [S-L19-067].
- **Impact now / as it grows:**
  - *Window only:* now, one surface to design. As it grows, every capture or lookup still needs a trip to the app.
  - *Shortcut panel:* now, a global shortcut, a small panel and a background save with a failure state. As it grows, the panel becomes the most-used surface, so it must stay instant and tiny while features push to join it.
  - *Ambient:* now, permission prompts and trigger rules. As it grows, each new trigger risks interrupting people; they need a way to turn them off [inferred].
- **Standards:** STD-when-to-animate-05, STD-when-to-animate-06, STD-when-to-animate-20, STD-accessibility-motion-11, STD-visual-details-16, STD-visual-details-42

### DC-L19-150: Desktop main window: title bar and layout
- **Block path:** Platforms > Desktop > Window chrome and main-window layout
- **Questions the designer answers:** Does the app keep the system title bar, or fold the window buttons into its own top bar or sidebar? How much of the top edge stays free for dragging? Does the main window need a sidebar?
- **Options:**
  - **System title bar above the app:** standard chrome, the least work; DC-L10-24 notes that a web-tech app that ignores native chrome reads as "a website in a window".
  - **Integrated title bar:** the window buttons live in the top bar or sidebar and are treated like any other element, as in Finder, Notes, Reminders, Calendar and Settings [S-L19-067]; Electron's hidden or inset title bar and Window Controls Overlay allow it (DC-L10-24). Keep roughly the top 50 pixels free of actions, because that strip drags the window [S-L19-067] (one video's estimate; no platform source in this wiki confirms it).
  - **Frameless utility window:** no window buttons at all, only for small summoned panels (DC-L19-149) [S-L19-067].
  - **Layout inside the window:** global actions in the top bar, navigation in a sidebar, content in the center (Apple's utility apps) [S-L19-067]; skip the sidebar when navigation is only browsing and searching, which frees room for content [S-L19-067]. Native macOS also expects a full menu bar with every command (DC-L10-24); the video doesn't mention it.
- **Visual effect:** Integrated: one continuous surface up to the window's top edge, with the sidebar running to the top, which reads as Apple-made. System bar: a separate stripe above the app. Frameless: a floating widget. No sidebar: the window becomes a container for the person's content [S-L19-067].
- **Depends on (upstream):** Q-plat-01 `desktop`, the desktop shell (DC-L10-24), Q-layout-04, DC-L19-149.
- **Affects (downstream):** the desktop app-shell template, top bar height and padding, sidebar, menu bar, the draggable region.
- **Token encoding:** a draggable-strip height as a layout dimension, for example `layout.window.drag-region` ($type dimension, 50px as a starting value marked "one video's estimate") [inferred name]; otherwise none.
- **Platform notes:** macOS: the window buttons stay top-left, since close is always top-left [S-L19-020]. Windows: no source in this wiki (DC-L10-24 covers Mica and 4/8px radii).
- **Accessibility constraints:** macOS pointer targets are 28pt by default and 20pt at minimum (DC-L10-15); controls placed near the drag strip keep their full hit area [inferred]; the menu bar gives keyboard access to every command (DC-L10-24).
- **Default + heuristic:** Default for macOS apps: an integrated title bar with top bar, sidebar and content, and a calm top strip; drop the sidebar when navigation is only browsing and searching [S-L19-067], which sits below DC-L08-19's range of three to five sidebar destinations [inferred]. Rule of thumb: the window's top edge belongs to the window, not to actions.
- **Evidence:** [S-L19-020] [S-L19-067]; compared with DC-L10-24, DC-L10-09, DC-L14-05, DC-L08-19, DC-L03-19.
- **Maps to:**
  - New question (proposed Q-plat-14, zoom 3, show if Q-plat-01 includes `desktop`): "Keep the system title bar, or build the window buttons into your own bar?" with options `system-titlebar`, `integrated`, `frameless-panels`; default `integrated` on macOS.
  - Q-layout-04 desktop visual sample: a Finder- or Notes-style window with the window buttons in the bar and the drag strip highlighted, shown with and without a sidebar [S-L19-067].
- **Impact now / as it grows:**
  - *System title bar:* now, no chrome work. As it grows, the app keeps looking like a web page in a frame next to native apps.
  - *Integrated:* now, drag regions and button placement to get right. As it grows, new toolbar actions compete with the drag strip and must go into the sidebar, menus or the menu bar.
  - *Frameless panels:* now, a minimal utility look. As it grows, each panel needs its own way to close and move [inferred].
  - *No sidebar:* now, maximum room for content. As it grows, a second real destination forces the sidebar back in.
- **Standards:** STD-visual-details-36, STD-visual-details-42

### DC-L19-151: Keyboard shortcuts: which actions get them, how people learn them, what they see
- **Block path:** Foundations > Interaction > Keyboard shortcuts
- **Questions the designer answers:** Which actions get keyboard shortcuts? How do people discover them? What do they see when a shortcut fires?
- **Options:**
  - **Operating-system standards only:** the video's examples of standard macOS shortcuts are Command Space (Spotlight), Command Tab (switch apps) and Command W (close) [S-L19-067]; never override standard shortcuts (DC-L13-17; the L13 heuristic table asks for a shortcut registry that refuses to override OS or browser standards).
  - **App shortcuts shown where the action lives:** shortcut hints on the buttons they trigger [S-L19-067]; in menus, alignment and type separate clickable items, non-clickable items and shortcuts, as in Linear [S-L19-084]; Sonner's Alt+T moves focus to the toasts [S-L19-021] [S-L19-092].
  - **Plus a cheat sheet:** opened by its own shortcut (Google) or kept in a settings popover [S-L19-067].
  - **Plus onboarding that teaches the main shortcut:** a modal that closes when the person performs the shortcut [S-L19-067]. Differs from DC-L13-11 (no forced tour); fits only as a short, skippable step when the shortcut is the product's core [inferred]. DC-L19-129 already owns this as `learn-by-doing` in its proposed onboarding question, so this card does not ask it again.
  - **Feedback when a shortcut fires:** "If you don't see a change, you assume that something went wrong", so the video asks for micro-animations or at least a state change [S-L19-067]. The house standards never animate keyboard-started actions or command-palette toggles [S-L19-025] [S-L19-023], and review blocks such animation [S-L19-032]. So the feedback is an instant, visible state change (the panel is there, the item is selected), the half of the video's rule that both sides accept.
- **Visual effect:** Hints make buttons and menus a little denser and more "pro"; a cheat sheet keeps the interface clean; instant feedback feels exact and fast, like Raycast [S-L19-012].
- **Depends on (upstream):** Q-plat-03 `keyboard`, Q-plat-01 (`desktop` or `web`), DC-L19-149.
- **Affects (downstream):** a shortcut slot in buttons and menu rows, a keyboard-key component, tooltips, onboarding, settings, the command menu (DC-L19-152).
- **Token encoding:** a text style for shortcut hints (a `type` role, $type typography) in the secondary text color [inferred]; no motion tokens, because the change is instant.
- **Platform notes:** Command on macOS and Ctrl elsewhere (DC-L16-10); on phones, shortcuts only matter with a hardware keyboard [inferred].
- **Accessibility constraints:** visible focus on everything the keyboard reaches (DC-L08-11); a shortcut is never the only way to an action [inferred]; toasts stay reachable by hotkey.
- **Default + heuristic:** Default for desktop and web apps: OS standards untouched; shortcuts for the most frequent actions, shown on their buttons and menu rows; a cheat sheet in settings; feedback as an instant state change, never an animation. Rule of thumb: every shortcut needs a visible result in the frame it fires and a visible place to learn it.
- **Evidence:** [S-L19-012] [S-L19-021] [S-L19-023] [S-L19-025] [S-L19-032] [S-L19-067] [S-L19-084] [S-L19-092]; compared with DC-L13-17, DC-L13-11, DC-L16-10, DC-L08-11, DC-L19-81, DC-L19-129.
- **Maps to:**
  - Q-plat-03 `keyboard`: option text becomes "Keyboard: visible focus everywhere, shortcuts shown on buttons and menus, instant feedback with no animation".
  - New question (proposed Q-plat-15, zoom 3, show if Q-plat-03 includes `keyboard` or Q-plat-01 includes `desktop`): "Which actions get keyboard shortcuts, and how do people learn them?" with options `os-only`, `shown-hints`, `hints-and-cheat-sheet`; default `hints-and-cheat-sheet` on desktop, `os-only` for phone-first products [inferred defaults]. Teaching a shortcut during onboarding stays with DC-L19-129 (`learn-by-doing`).
  - Visual sample: Linear's menu with its shortcut column [S-L19-084] and the quick-save window with shortcut hints on its buttons [S-L19-067].
  - Engine: the motion feedback token's description ("Hover, press, color changes") without a keyboard exception is already recorded under STD-when-to-animate-06.
- **Impact now / as it grows:**
  - *OS standards only:* now, nothing to design. As it grows, power users of a work tool ask for shortcuts.
  - *Shown hints:* now, one extra slot in buttons and menus. As it grows, the registry must prevent collisions as features add shortcuts.
  - *Cheat sheet:* now, one settings view. As it grows, it becomes the single list to keep in sync with the registry.
  - *Onboarding step:* now, one short modal. As it grows, it teaches only the core shortcut; others stay in hints and the cheat sheet.
  - *Instant feedback:* now, no motion work. As it grows, the product stays fast however often shortcuts are used.
- **Standards:** STD-when-to-animate-05, STD-when-to-animate-06, STD-when-to-animate-17, STD-accessibility-motion-23, STD-visual-details-49

### DC-L19-152: Search on desktop: a command palette, or search in place
- **Block path:** Patterns > Search > Desktop search surface
- **Questions the designer answers:** Is search a command palette that jumps anywhere, or a search bar that filters what is on screen? Where does it live, and how does it open?
- **Options:**
  - **Command palette (⌘K):** universal search and commands, as in Notion, Obsidian and Attio; sleek, but most items take you to an entirely new screen [S-L19-067]. Built on cmdk [S-L19-029] and opened instantly, since command-palette toggles never animate [S-L19-025].
  - **Floating search bar with a slide-out preview:** search filters in place and the app stays on one screen; a collapsed bar at the bottom expands on click or shortcut; the bar shows the result count and a clear X, and the query and a back arrow sit top left, because results look like the browse view [S-L19-067].
  - **Prominent toolbar search:** every native Mac app (Music, Shortcuts, Weather) keeps search prominent and accessible [S-L19-067]; placing it in the toolbar is [inferred], since the video names no location.
  - **Both:** a palette for commands and destinations, in-place search for content [inferred].
- **Visual effect:** Palette: a centered overlay with grouped results and shortcut hints (the L08 catalog's C51 anatomy), invisible until summoned. Floating bar: search is part of the canvas and content stays visible. Toolbar search: always in view, obvious to newcomers.
- **Depends on (upstream):** DC-L19-149 (one-screen utility or many sections), Q-layout-04, DC-L19-151.
- **Affects (downstream):** the command palette component (C51), the search field, the no-results state (imagery, suggestions for typos and a way out [S-L19-053]), the keyboard layer.
- **Token encoding:** none new (dialog and menu tokens, per C51).
- **Platform notes:** desktop and web. On phones, search tends to move to the bottom or open with a swipe up, as in Slack [S-L19-053].
- **Accessibility constraints:** a palette is a combobox and listbox inside a dialog (C51) on a primitive that manages focus; the video's bar "beautifully expands" on its shortcut [S-L19-067], but under the house standards it appears instantly.
- **Default + heuristic:** Default: prominent in-place search for one-screen and content apps; add a ⌘K palette when the product has many sections or commands that lead elsewhere. Rule of thumb: if most results are destinations, use a palette; if they are items on this screen, filter in place [S-L19-067].
- **Evidence:** [S-L19-025] [S-L19-029] [S-L19-053] [S-L19-067]; compared with DC-L16-10, DC-L19-117, the L08 catalog entry C51 and the L13 heuristic table (flexibility and efficiency of use).
- **Maps to:**
  - No new question: DC-L19-117 already maps this choice to Q-comp-02 (`none` for simple sites and phone-first apps, a cmdk menu for daily-use tools with many destinations, a floating search for one-screen utilities, always opening instantly). This card adds two things to that heuristic: the rule of thumb "destinations mean a palette, items on this screen mean filtering in place" [S-L19-067], and prominent always-visible search as an option for content apps [S-L19-067]. The "about five top-level sections" threshold is [inferred].
  - Visual sample: the collapsed floating search bar, then expanded with result count, clear X and back arrow [S-L19-067], beside a ⌘K palette.
- **Impact now / as it grows:**
  - *Palette:* now, one overlay and a command registry. As it grows, it scales to hundreds of commands and becomes the expert's main entry point.
  - *In-place search:* now, simple and visible. As it grows, it can't reach commands or other sections, so a palette joins it.
  - *Toolbar search:* now, the most discoverable. As it grows, it takes permanent toolbar space.
  - *Both:* now, two surfaces to design. As it grows, the split between "find a thing" and "do a thing" stays clear [inferred].
- **Standards:** STD-accessibility-motion-16, STD-when-to-animate-05, STD-when-to-animate-06, STD-when-to-animate-20

### DC-L19-153: Real-device check: which device counts as proof
- **Block path:** Governance > Testing > Device check floor
- **Questions the designer answers:** On which physical devices is feel and layout judged before something is called done? Does an emulator, a simulator or a dev build count? Which phone is the "slow one"?
- **Options:**
  - **Real hardware for the web:** a phone connected by cable, the dev server opened by IP, Safari's Web Inspector or `chrome://inspect`; a phone a few years old, the keyboard open, landscape at least once, and standalone mode when a PWA is a target. Chrome device emulation reproduces none of the mobile bugs [S-L19-028]; a shrunken desktop window doesn't count either [S-L19-005].
  - **Release build on the slowest supported device, for native apps:** never Expo Go, a dev build or a simulator, because a dev build's slow JavaScript thread hides the problems; wrong-thread animation drops to about 20fps on a three-year-old Android (an illustrative figure) [S-L19-016].
  - **Simulator as proof:** the drawer article accepts the Xcode Simulator as an alternative test device [S-L19-005]; the mobile-native skill calls it a step up from emulation that still misses touch feel [S-L19-028]; the house standard settles it: it never counts as verified.
  - **Honest reporting without a device:** say which fixes were verified from code and which need a phone; never claim a device-only fix is fixed [S-L19-028].
  - **Real people in real contexts** [S-L19-020] (STD-process-review-taste-34).
- **Visual effect:** none directly; the choice decides which bugs ship: sticky hover, buttons under the URL bar, input zoom, jank on older phones [S-L19-028] [S-L19-016].
- **Depends on (upstream):** Q-plat-02 (devices), Q-plat-09 (OS floor), Q-plat-08 (stack), Q-gov-07 (test matrix).
- **Affects (downstream):** the definition of done, component acceptance, QA checklists, the wording of the builder's reports.
- **Token encoding:** none (process decision).
- **Platform notes:** iOS through Safari's Develop menu, Android through `chrome://inspect` [S-L19-028]; native feel on release builds [S-L19-016]; touch interactions such as drawers and swipes on physical devices [S-L19-023].
- **Accessibility constraints:** the check includes toggling reduced motion (STD-accessibility-motion-05), plus the largest text size and one screen reader per device class (DC-L14-14).
- **Default + heuristic:** Default when phones are in scope: at least one physical iPhone and one older Android [inferred pairing; the sources say "a phone that's a few years old" and "slowest supported device"], release builds for native apps, standalone mode for PWAs; emulators only for layout sketches. Rule of thumb: if it hasn't run on a phone, say which parts are unverified instead of calling it done.
- **Evidence:** [S-L19-005] [S-L19-016] [S-L19-020] [S-L19-023] [S-L19-028]; compared with DC-L14-14, DC-L10-23, DC-L19-96.
- **Maps to:**
  - No second device question: DC-L19-96 already proposes Q-plat-11 (a Q-plat-02 follow-up, "Which is the slowest phone and computer this must feel smooth on?"). This card asks that the answer name real hardware the team will check on, including a phone a few years old, and that it is recorded in PRODUCT.md as an owner input [inferred].
  - Q-gov-07: new option `real-device-floor`, on by default when Q-plat-02 includes `phone`.
  - Engine (proposed): `engine.py review` lists "needs a real device" items when phones are in scope, instead of reporting them as passed [inferred].
- **Impact now / as it grows:**
  - *Real hardware (web):* now, a cable, a second phone and a few minutes per change. As it grows, the device shelf follows the audience's devices, and bugs are caught before users report them.
  - *Release build on the slowest device:* now, slower check cycles. As it grows, performance stays good as screens and animations multiply.
  - *Simulator as proof:* now, fast. As it grows, touch-feel bugs ship unnoticed.
  - *Honest reporting:* now, a short "unverified" list. As it grows, the list shows where the team needs devices or testers.
  - *Real people:* now, recruiting effort. As it grows, it catches the context problems no device test finds.
- **Standards:** STD-process-review-taste-29, STD-process-review-taste-33, STD-process-review-taste-34, STD-accessibility-motion-05, STD-mobile-touch-24, STD-mobile-touch-39

## Open questions / gaps

- The 50-pixel drag strip (DC-L19-150) and the 70-80% right-handed figure (DC-L19-145) come from one video each; no platform source in this wiki confirms either.
- Windows desktop apps have no practitioner or house source in this wiki; DC-L19-149 and DC-L19-150 lean on macOS only.
- Swipe-to-confirm (DC-L19-146): the sources give no tap alternative; hold-to-confirm is the house pattern, but no source compares the two for high-impact, non-destructive actions such as sending.
- Whether `brand-first` (Q-plat-05) should stay as an option for Flutter, where the React Native standards do not apply, is open; the sources are silent on Flutter.
- The proposed thresholds (a ⌘K palette above about five sections in DC-L19-152) are inferred, not sourced.
- None of the sources cover screen-reader testing, forced colors, text direction or video captions beyond one changelog line [S-L19-001]; DC-L10-16 and Q-gov-07 remain the reference.

## Confidence

- Confirmed against the raw text: the mobile sizes, bottom-bar limits and the rule that one screen does one thing [S-L19-053]; the macOS layout, drag strip, shortcut feedback, Raycast and Spotlight models and the web-tech build [S-L19-067]; reach at the bottom and the browser bar [S-L19-076]; the right-handed figure and the Fitts/Hick mix-up [S-L19-077]; the mobile-native symptom list, app-versus-document split and emulation rule [S-L19-028]; the Expo no-hover fact, native pieces table, ripple rule and 350ms push [S-L19-016]; the familiarity principle and "close is always top-left" [S-L19-020]; Raycast with no open animation [S-L19-012].
- Taken first from the verified analyses, then re-read in the raw text during the 2026-09-27 check: the Vaul, Sonner, pick-ui-library, write-swift, drawer, Expo recipes, apple-design, audit and review-animations details. That check fixed: Vaul listed as a house toolkit pick (it is unmaintained and not on the curated list), the review "block" rule cited to the wrong skill, the swipe fallback stated more firmly than the video, a hover claim attributed to the mobile video, proposed question ids that collided with DC-L19-96, and new questions that duplicated DC-L19-117, DC-L19-129 and DC-L19-96.
- Inferred and marked: the proposed question ids (Q-plat-12 to Q-plat-15; Q-plat-11 is DC-L19-96's), token names, the thresholds, the handedness and interruption effects, and each reconciliation flagged in a Default.
