---
type: source
title: "emilkowalski/skills: skills/mobile-native/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-mobile-native-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/mobile-native/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - mobile-web
  - touch
  - hover-gating
  - tap-highlight
  - viewport-units
  - safe-area
  - overscroll
  - touch-action
  - theme-color
  - inputs
  - press-feedback
  - pwa
---

# emilkowalski/skills: skills/mobile-native/SKILL.md

## Metadata

- Page ID: `eks-skills-mobile-native-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/mobile-native/SKILL.md

## Summary

Emil Kowalski's mobile-native skill is an instruction file for an AI agent that makes a web app feel installed on a phone instead of like a website in a browser. It works from a symptom table of eleven common tells (sticky hover, the gray tap flash, the 100vh bug, inputs that zoom the page, laggy taps, pull-to-refresh hijacking scroll, content stopping at the notch, long-press selecting button text, carousels scrolling the wrong way, a mismatched status bar, and bugs that only show on real phones), and gives the reason and the exact CSS or meta tag for each. It insists on capability media queries instead of device sniffing, never disabling zoom, and testing on real hardware because device emulation reproduces none of these bugs. It ends with a baseline to ship before the first component and a 'Never Ship' self-check table. For a design system it supplies platform-layer defaults (viewport meta, hover gating, press feedback timing, input font size, safe-area padding, per-scheme theme-color) that every web component inherits.

## Key Ideas

- Most 'feels janky on mobile' reports are platform-layer problems, not animation problems: a tap delay, a tap flash or a hover state that sticks.
- The user's real phone is the source of truth; Chrome device emulation reproduces none of these bugs.
- Almost every fix is one CSS declaration or one meta tag, so reaching for JavaScript is the wrong tool.
- Gate by capability with media queries such as (hover: hover) and (pointer: fine), never by user agent or screen width, because touch and mouse coexist on many devices.
- Every fix carries its reason and is applied only where that reason holds; user-select: none is right on a button and a defect on body text.
- Never disable zoom; the page zooms into inputs because their font size is under 16px, so fix the font size.
- Press feedback must happen when the finger lands (:active or pointerdown), not on click, and it lasts 100-160ms with ease-out.
- Use 100dvh for app shells and 100svh for heroes; 100vh overflows by the height of the URL bar.
- Stop overscroll with overscroll-behavior (none on the root, contain on inner scrollers), never with a touchmove listener.
- Paint edge to edge with viewport-fit=cover and pad content back with env(safe-area-inset-*).
- touch-action names what the browser may still do: pan-y on a horizontal carousel, pan-x on a vertical sheet handle, none only on surfaces that own every axis.
- Give each color scheme its own theme-color, matched to the header background at the top of the page, not the brand color.
- A small baseline of meta tags and CSS should ship before the first component of any mobile-facing app.
- When a fix cannot be verified without a device, say so instead of claiming it is fixed.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skill; its knowledge is framed as his design engineering philosophy.
- [[entities/mobile-native-skill|mobile-native skill]] (tool): The agent skill this source is; a fix-it skill for the web platform layer on phones.
- [[entities/animate-skill|animate skill]] (tool): Sibling skill for designing motion; its easing tokens should be reused for press feedback.
- [[entities/review-animations-skill|review-animations skill]] (tool): Sibling skill for reviewing motion; out of scope here.
- [[entities/animate-expo-skill|animate-expo skill]] (tool): Sibling skill for React Native; out of scope here.
- [[entities/ios-safari|iOS Safari]] (product): Browser that paints tap highlights, zooms into small inputs, rubber-bands the page and still delays taps on some elements.
- [[entities/android-chrome|Android Chrome]] (product): Browser that paints tap highlights, triggers pull-to-refresh, and needs interactive-widget=resizes-content for the keyboard to shrink the layout.
- [[entities/chrome-device-emulation|Chrome device emulation]] (tool): Desktop device toolbar that does not reproduce sticky hover, tap delay, rubber-banding, safe areas or the keyboard.
- [[entities/safari-web-inspector|Safari Web Inspector]] (tool): Remote debugging for an iOS device via Safari > Develop > the device.
- [[entities/chrome-inspect|chrome://inspect]] (tool): Remote debugging for an Android device.
- [[entities/xcode-simulator|Xcode Simulator]] (tool): A step up from emulation that still misses touch feel.
- [[entities/tailwind-css|Tailwind CSS]] (library): v4's hover: variant compiles to @media (hover: hover); v3 needs future.hoverOnlyWhenSupported.
- [[entities/next-js|Next.js]] (library): Sets theme-color through the viewport export with themeColor: [{ media, color }].
- [[entities/pwa|PWA]] (concept): Installed web app whose standalone mode changes viewport, safe areas and status bar behavior.
- [[entities/sticky-hover|Sticky hover]] (concept): Touch browsers apply a fake :hover on the first tap and leave it until the user taps elsewhere.
- [[entities/tap-highlight|Tap highlight]] (concept): Translucent gray or blue flash browsers paint over tapped elements with a click handler.
- [[entities/dynamic-and-small-viewport-units-dvh-svh-lvh|Dynamic and small viewport units (dvh, svh, lvh)]] (concept): Viewport height units that replace 100vh: dvh resizes as the URL bar shows and hides, svh is the smallest the viewport gets, lvh is the largest (the old vh).
- [[entities/safe-area-insets|Safe-area insets]] (concept): env(safe-area-inset-*) values that pad content away from the notch, Dynamic Island and home indicator.
- [[entities/overscroll-behavior|overscroll-behavior]] (concept): CSS property that stops pull-to-refresh and scroll chaining without JavaScript.
- [[entities/touch-action|touch-action]] (concept): CSS property naming which gestures the browser still handles on an element.
- [[entities/theme-color|theme-color]] (concept): Meta tag that colors the status bar and browser chrome, set per color scheme.

## Topics

- [[topics/mobile-app-patterns|Mobile app patterns]]: The whole source: eleven platform-layer fixes and a baseline that make a web app feel native on a phone, plus the rule to test on real hardware.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Exact CSS and meta tags: hover gating media query, tap highlight, dvh/svh, 16px inputs, touch-action, overscroll-behavior, viewport-fit=cover with env() insets, user-select, theme-color per scheme, and Tailwind and Next.js specifics.
- [[topics/accessibility|Accessibility]]: Never disable zoom with user-scalable=no or maximum-scale=1; keep content text selectable; keep press feedback for touch users after removing the tap highlight.
- [[topics/micro-interactions|Micro-interactions]]: Press feedback fires on pointer-down via :active, uses scale(0.97) and a background change over 100ms, and stays within 100-160ms with ease-out.
- [[topics/easing-and-timing|Easing and timing]]: Press feedback timing is 100-160ms with ease-out, reusing the animate skill's tokens instead of a new curve.
- [[topics/gestures-and-drag|Gestures and drag]]: touch-action tells the browser which axes an element owns (pan-y, pan-x, none, manipulation); native scroll-snap beats a hand-rolled spring for carousels.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Sheet content uses overscroll-behavior: contain, sheets pad the bottom with calc(1rem + env(safe-area-inset-bottom)), drag-to-dismiss surfaces use touch-action: none, and a vertical sheet handle uses pan-x.
- [[topics/forms-and-inputs|Forms and inputs]]: Inputs need a 16px minimum font size to stop iOS zoom, and the right inputmode, type, autocapitalize, autocorrect and enterkeyhint to set the keyboard.
- [[topics/buttons-and-actions|Buttons and actions]]: Buttons get touch-action: manipulation, user-select: none, an :active press state, and hover styles only behind a capability media query.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: theme-color is set once per prefers-color-scheme, matched to the header background, and updated from JavaScript when the theme switches by class.
- [[topics/spacing-and-layout|Spacing and layout]]: Full-height layouts use 100dvh (app shell) or 100svh (hero), and fixed headers, bottom bars, toasts and sheets pad with safe-area insets.
- [[topics/design-process|Design process]]: Match the symptom, apply the fix only where its reason applies, ship the baseline first, test on an older real phone with the keyboard open and in landscape, and report what still needs a device.

## Notable Claims

- Most reports that an app feels janky on mobile are not animation problems but a 300ms tap delay, a gray flash on tap, or a hover state that won't let go. Evidence: Operating Posture
- The bugs in this skill do not reproduce in Chrome's device emulation, so testing only there ships all of them. Evidence: Operating Posture: Fixing what the desktop shows you
- Emulation cannot reproduce sticky hover, tap delay, rubber-banding, safe areas, or the keyboard. Evidence: Hard Rules 5: Test on hardware
- Touch has no hover, so browsers apply :hover on the first tap and leave it until the user taps somewhere else. Evidence: 1. Hover state stuck after tap
- (pointer: fine) rules out styluses and the odd Android device that claims hover support. Evidence: 1. Hover state stuck after tap: Both conditions matter
- In Tailwind v4 the hover: variant already compiles to @media (hover: hover); in v3 it requires future.hoverOnlyWhenSupported. Evidence: 1. Hover state stuck after tap
- iOS Safari and Android Chrome paint a translucent highlight over any tapped element that has a click handler, and it is the single loudest 'this is a website' signal. Evidence: 2. Gray/blue flash on tap
- 100vh on mobile is the largest viewport, so on load a 100vh element overflows by the height of the visible URL bar and a bottom-pinned button sits under it. Evidence: 3. Layout has the wrong height
- dvh resizes as the URL bar collapses, which causes layout shifts on marketing content mid-scroll; svh is stable and never overflows; lvh is the old vh. Evidence: 3. Layout has the wrong height
- iOS Safari zooms the page when focus lands on an input with font size under 16px and does not zoom back out on blur. Evidence: 4. Page zooms into the input
- Browsers wait after a tap to see whether a double-tap zoom is coming; modern browsers skip the wait with width=device-width, but iOS Safari still delays on some elements. Evidence: 5. Tap feels laggy: The 300ms click delay
- A web button that changes only on click responds when the finger leaves, which reads as lag even at 0ms. Evidence: 5. Tap feels laggy: Feedback on release instead of press
- Scrolling past the top triggers pull-to-refresh on Android Chrome and the whole-page rubber band on iOS. Evidence: 6. Pull-to-refresh hijacks scroll
- overscroll-behavior: contain keeps a container's own bounce but stops the page behind it from moving. Evidence: 6. Pull-to-refresh hijacks scroll
- A touchmove plus preventDefault() listener blocks scrolling entirely and makes the listener non-passive, which costs frames. Evidence: 6. Pull-to-refresh hijacks scroll
- By default the browser letterboxes the page inside the safe area; without viewport-fit=cover every env() safe-area value is 0px. Evidence: 7. Content stops at the notch
- Holding a finger on a web button makes iOS select its label or pop the copy/share callout on a link, which native controls never do. Evidence: 8. Long-press selects button text
- A horizontal swipe on a carousel is ambiguous to the browser, which often jitters the page up while the carousel moves. Evidence: 9. Carousel scrolls vertically
- For a native-scroll carousel, the browser's own physics beat a hand-rolled spring. Evidence: 9. Carousel scrolls vertically: scroll-snap-type
- The status bar and browser chrome take their color from theme-color; a single value gives light mode a dark bar or dark mode a white one. Evidence: 10. Status bar color doesn't match
- Standalone (installed PWA) mode changes viewport, safe areas and status bar behavior. Evidence: 11. Right in Chrome, wrong on phone
- The Xcode Simulator is a step up from emulation but still misses touch feel. Evidence: 11. Right in Chrome, wrong on phone
- interactive-widget=resizes-content makes the software keyboard shrink the layout viewport on Android Chrome, so 100dvh and bottom-pinned inputs react as they do on iOS. Evidence: Baseline
- -webkit-text-size-adjust: 100% prevents font inflation in landscape. Evidence: Baseline

## Quotes

> a desktop browser with the device toolbar on is not a phone.
> The user's phone is the source of truth.
> Real hardware is the bar.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The source is an AI agent skill with a scripted opening line that frames its knowledge as Emil Kowalski's philosophy; the skill-behavior instructions (initial response, tone) are not design rules.
- Caveat: Pinned to commit 85e8e23; browser specifics can date: iOS Safari still delaying taps on some elements, Tailwind v4 versus v3 hover behavior, and the Next.js viewport export.
- Caveat: Scope is the web platform layer only; motion design belongs to the animate skill and React Native to animate-expo.
- Caveat: The hex values #ffffff and #0a0a0a and the token names --gray-3, --gray-4 and --ease-out are sample values from the code snippets; the rule is to match theme-color to the header background and reuse existing tokens. [inferred]
- Caveat: The Baseline applies user-select: none to every a element, while section 8 limits it to controls and says content text must stay selectable; inline links inside body text may need an exception. [inferred]
- Caveat: The Baseline sets overscroll-behavior: none on html only, while section 6 sets it on html and body. [inferred]

### Rules and practices

- **must** (process, web): Ship every mobile fix with its reason, and apply it only where that reason applies, not globally out of habit. Why: The same declaration can be correct in one place and a defect in another: user-select: none on body text is a defect, on a button it is correct. Values: user-select: none. [Hard Rules 1: Every fix ships with the reason]
- **must** (platforms, web): Detect capabilities with media queries and platform features ((hover: hover), (pointer: fine), env(), dvh); never branch on user agent strings or screen width to guess at touch. Why: The platform tells you what it can do; guessing from device identity or width is wrong. Values: (hover: hover), (pointer: fine), env(), dvh. [Hard Rules 2: Media queries over device sniffing]
- **must** (platforms, web): Write interaction styles for touch and mouse at the same time and gate them by capability, not by device. Why: Touch and mouse are not exclusive: iPads with trackpads, laptops with touchscreens, phones with a mouse. [Hard Rules 3: Touch and mouse are not exclusive]
- **must** (accessibility, web): Never disable zoom with user-scalable=no or maximum-scale=1; fix the input font size that causes the zoom instead. Why: Disabling zoom is an accessibility failure, and the real cause is inputs under 16px. Values: user-scalable=no, maximum-scale=1. [Hard Rules 4: Never disable zoom]
- **must** (process, web): Test on real hardware before calling a mobile fix done: connect the phone, open the dev server by IP, and debug with Safari's Web Inspector or Chrome remote debugging. Why: Emulation cannot reproduce sticky hover, tap delay, rubber-banding, safe areas, or the keyboard. [Hard Rules 5: Test on hardware before calling it done]
- **must** (process, web): Never declare a mobile issue fixed based on Chrome device emulation. Why: None of these bugs reproduce in device emulation; testing only there ships all of them. [Never Ship: Declaring it fixed from device emulation; Operating Posture failure mode 1]
- **must** (platforms, web): Do not reach for JavaScript when CSS or a meta tag does the job; for example, hide hover states with a media query, not a useIsTouchDevice() hook. Why: Almost every item is one declaration; JavaScript is the wrong tool. Values: useIsTouchDevice(). [Reaching for JavaScript when CSS or a meta tag does it]
- **must** (process, web): When you cannot run the app on hardware, state which fixes you verified from code and which the user must confirm on a real device; never claim a device-only fix is fixed. Why: The phone is the source of truth, and the honest answer is sometimes 'I can't verify this without a device'. [Operating Posture; Tone]
- **must** (components, css): Put every :hover style inside @media (hover: hover) and (pointer: fine). Why: Touch browsers fake hover on the first tap and leave it applied, so a button that scales up on hover stays scaled up after being tapped. Values: @media (hover: hover) and (pointer: fine), background: var(--gray-3), transform: scale(1.02). [1. Hover state stuck after tap]
- **must** (components, css): Use both conditions in the hover gate, (hover: hover) and (pointer: fine), not just one. Why: (hover: hover) means the primary input can hover; (pointer: fine) means it is precise like a mouse and rules out styluses and the odd Android device that claims hover support. Values: (hover: hover), (pointer: fine). [1. Hover state stuck after tap: Both conditions matter]
- **should** (tooling, css): In Tailwind v4 rely on the hover: variant, which already compiles to @media (hover: hover); in Tailwind v3 set future.hoverOnlyWhenSupported. Why: It gates hover by capability at the framework level. Values: @media (hover: hover), future.hoverOnlyWhenSupported. [1. Hover state stuck after tap]
- **must** (components, css): Give touch users press feedback through :active on every tappable element. Why: :active works on every input type, and touch users still need feedback once hover is gated off. Values: :active. [1. Hover state stuck after tap: Touch users still need press feedback]
- **must** (platforms, css): Remove the tap highlight once, globally, with html { -webkit-tap-highlight-color: transparent; }. Why: The translucent flash on tap is the single loudest 'this is a website' signal and fights the press feedback you designed. Values: -webkit-tap-highlight-color: transparent. [2. Gray/blue flash on tap]
- **must** (components, css): After removing the tap highlight, make sure every tappable element has its own :active state. Why: You have removed the only feedback the browser was giving. Values: :active. [2. Gray/blue flash on tap]
- **must** (layout, css): Use height: 100dvh, not 100vh, for app shells, drawers and anything bottom-pinned that should track the visible area as browser chrome shows and hides. Why: 100vh is the largest viewport, so it overflows by the URL bar's height and a bottom-pinned button sits under the bar. Values: height: 100dvh, 100vh. [3. Layout has the wrong height; Never Ship: 100vh for an app shell or bottom-pinned UI]
- **must** (layout, css): Use min-height: 100svh, not 100dvh, for marketing heroes and first screens. Why: svh is the smallest the viewport gets, so nothing is cut off, and it is stable; dvh causes layout shifts on marketing content mid-scroll. Values: min-height: 100svh, 100dvh. [3. Layout has the wrong height; Never Ship: 100dvh on a marketing hero]
- **should** (layout, css): Avoid lvh for layout heights. Why: lvh is the old vh, the largest viewport; you almost never want it. Values: lvh. [3. Layout has the wrong height]
- **consider** (layout, css): Add a 100vh fallback line above the dvh/svh declaration only if the project's support matrix demands old browsers. Why: The fallback exists only for old browsers. Values: 100vh. [3. Layout has the wrong height]
- **must** (typography, web): Set input, textarea and select font-size to 16px at the minimum. Why: iOS Safari zooms the page on focus when the input font size is under 16px and does not zoom back out on blur, leaving a cropped, drifted layout. Values: font-size: 16px, 1rem at the default root size. [4. Page zooms into the input]
- **consider** (typography, css): If the design wants smaller input text on desktop, apply the 16px input size only under @media (pointer: coarse). Why: It keeps the zoom fix where it matters without changing desktop input text. Values: @media (pointer: coarse), font-size: 16px. [4. Page zooms into the input]
- **should** (components, web): Set inputmode="numeric" on code fields and inputmode="decimal" on amount fields. Why: It sets the right software keyboard for the field. Values: inputmode="numeric", inputmode="decimal". [4. Page zooms into the input: set the keyboard]
- **should** (components, web): Use type="email" and type="tel" for email and phone fields. Why: It sets the right software keyboard for the field. Values: type="email", type="tel". [4. Page zooms into the input: set the keyboard]
- **should** (components, web): Set autocapitalize="none" and autocorrect="off" on username and code fields. Why: The source lists it under setting the keyboard for the field; that auto-capitalisation and autocorrect would alter usernames and codes is [inferred]. Values: autocapitalize="none", autocorrect="off". [4. Page zooms into the input: set the keyboard]
- **should** (components, web): Set enterkeyhint ("send", "search" or "done") so the return key says what it does. Why: The return key should describe its action. Values: enterkeyhint="send", "search", "done". [4. Page zooms into the input: set the keyboard]
- **must** (platforms, css): Apply touch-action: manipulation to button, a, [role="button"] and other tappable elements. Why: Browsers wait 300ms after a tap to see whether a second tap (double-tap zoom) is coming; modern browsers skip the wait with width=device-width, but iOS Safari still delays on some elements; manipulation says the element never double-tap-zooms, so click fires immediately. Values: touch-action: manipulation, 300ms. [5. Tap feels laggy: The 300ms click delay]
- **must** (components, web): Give press feedback on press, not release: style :active, and if JavaScript is needed listen to pointerdown, not click. Why: Native buttons respond the instant the finger lands; feedback on click arrives when the finger leaves and reads as lag even at 0ms. Values: :active, pointerdown. [5. Tap feels laggy: Feedback on release instead of press; Never Ship: Press feedback on click only]
- **should** (motion, css): For button press feedback, transition transform and background over 100ms with ease-out, and on :active scale to 0.97 and change the background to var(--gray-4). Why: It gives an immediate, native-feeling response when the finger lands. Values: transition: transform 100ms var(--ease-out), background 100ms, transform: scale(0.97), background: var(--gray-4). [5. Tap feels laggy: .button:active code]
- **must** (motion, web): Keep press feedback between 100 and 160ms with ease-out. Why: The section's reason is that native buttons respond the instant the finger lands; the source gives no separate reason for the 100–160ms range. [inferred] Values: 100–160ms, ease-out. [5. Tap feels laggy: Keep press feedback at 100–160ms]
- **should** (tokens, web): If the codebase uses the animate skill's tokens, use them for press feedback; do not fork a new curve. Why: The source gives no reason; keeping one set of curves consistent across the codebase is [inferred]. Values: var(--ease-out). [5. Tap feels laggy: don't fork a new curve]
- **must** (platforms, css): In apps with their own scroll containers, drag-down drawers or a canvas, set overscroll-behavior: none on html and body. Why: Scrolling past the top triggers pull-to-refresh on Android Chrome and the whole-page rubber band on iOS, which is wrong in an app. Values: overscroll-behavior: none. [6. Pull-to-refresh hijacks scroll]
- **should** (platforms, css): Keep pull-to-refresh (drop overscroll-behavior: none from html) when the app is a scrolling document where pull-to-refresh is welcome. Why: Page-level overscroll is fine on a document. Values: overscroll-behavior: none. [Drop `overscroll-behavior: none` from `html` if the app is a scrolling document where pull-to-refresh is welcome]
- **must** (components, css): On every inner scrollable (sheet content, chat list, sidebar) set overflow-y: auto and overscroll-behavior: contain; use none on the root and contain on children. Why: contain keeps the container's own native-feeling bounce but stops scroll from chaining to the page behind it. Values: overflow-y: auto, overscroll-behavior: contain. [6. Pull-to-refresh hijacks scroll: .sheet-content]
- **must** (platforms, web): Never stop overscroll with a touchmove listener that calls preventDefault(); use overscroll-behavior. Why: It blocks scrolling entirely and makes the listener non-passive, which costs frames. Values: touchmove, preventDefault(). [6. Pull-to-refresh hijacks scroll; Never Ship]
- **must** (platforms, web): Add viewport-fit=cover to the viewport meta tag so the page paints edge to edge under the notch. Why: By default the browser letterboxes the page inside the safe area, leaving notch, Dynamic Island and home-indicator zones in the body background; native apps paint edge to edge. Values: <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />. [7. Content stops at the notch]
- **must** (layout, css): Pad fixed headers, bottom tab bars, toasts and sheets with env(safe-area-inset-*): header padding-top env(safe-area-inset-top), bottom bar padding-bottom env(safe-area-inset-bottom), sheet padding-bottom calc(1rem + env(safe-area-inset-bottom)). Why: Native apps pad their content away from the notch and home indicator; normal page content usually gets it for free through the header's padding. Values: padding-top: env(safe-area-inset-top), padding-bottom: env(safe-area-inset-bottom), padding-bottom: calc(1rem + env(safe-area-inset-bottom)). [7. Content stops at the notch]
- **must** (platforms, web): Never use env(safe-area-inset-*) without viewport-fit=cover in the viewport meta tag. Why: Without the meta tag every env() safe-area value is 0px. Values: 0px. [7. Content stops at the notch; Never Ship]
- **should** (layout, css): Give env() a fallback, such as env(safe-area-inset-bottom, 0px), when the value is used inside calc(). Why: The calc needs a defined value where the inset is unavailable. [inferred] Values: env(safe-area-inset-bottom, 0px). [7. Content stops at the notch: Give env() a fallback]
- **must** (components, css): Make control text unselectable: on button, [role="button"], .tab, .chip and .drag-handle set user-select: none, -webkit-user-select: none and -webkit-touch-callout: none. Why: Long-press on a web button selects its label or pops the copy/share callout, which native controls never do; Safari still needs the -webkit- prefix. Values: user-select: none, -webkit-user-select: none, -webkit-touch-callout: none. [8. Long-press selects button text]
- **must** (accessibility, css): Never put user-select: none on body; apply it only to controls. Why: Text that is content must stay selectable: users copy addresses, error messages and order numbers. Values: user-select: none. [8. Long-press selects button text; Never Ship]
- **must** (components, css): On a horizontal JS-gesture carousel set touch-action: pan-y. Why: A horizontal swipe is ambiguous to the browser, which often jitters the page up while the carousel moves; pan-y keeps vertical panning with the browser and gives horizontal to the carousel. Values: touch-action: pan-y. [9. Carousel scrolls vertically]
- **must** (components, css): Use touch-action: none only on a surface whose custom gesture owns every axis, such as a drag-to-dismiss sheet or a slider. Why: none means the element handles everything; elsewhere the user cannot scroll past it. Values: touch-action: none. [9. Carousel scrolls vertically: .drag-surface]
- **should** (components, css): On a vertical sheet handle set touch-action: pan-x. Why: The sheet handles vertical drags; horizontal stays with the browser. Values: touch-action: pan-x. [9. Carousel scrolls vertically: .vertical-sheet-handle]
- **should** (components, css): Choose a touch-action value by naming what the browser may still do, not what the element handles: pan-y on a horizontal carousel, pan-x on a vertical sheet handle. Why: The values name what the browser may still do; pan-y on a horizontal carousel means the browser keeps vertical panning while the element handles horizontal. Values: pan-y, pan-x. [9. Carousel scrolls vertically: The values name what the browser may still do]
- **must** (components, css): Never put touch-action: none on something the user needs to scroll past; use pan-x or pan-y. Why: The user will not be able to scroll past it. Values: touch-action: none, pan-x, pan-y. [on something the user needs to scroll past]
- **should** (components, css): If the carousel is native scroll rather than a JS gesture, prefer scroll-snap-type: x mandatory on the track and scroll-snap-align: start on slides. Why: The browser's own physics beat a hand-rolled spring, and touch-action becomes unnecessary. Values: scroll-snap-type: x mandatory, scroll-snap-align: start. [If the carousel is native scroll rather than a JS gesture, prefer]
- **must** (color, web): Set one theme-color meta tag per prefers-color-scheme, plus <meta name="color-scheme" content="light dark">. Why: The status bar and browser chrome take their color from theme-color; one value gives light mode a dark bar or dark mode a white one. Values: <meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff" />, <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a" />, <meta name="color-scheme" content="light dark" />. [10. Status bar color doesn't match; Never Ship: One theme-color for both schemes]
- **must** (color, web): Match theme-color to the color at the very top of the page (the header background), not the brand color. Why: The source gives no reason; that the status bar should blend into the top of the page is [inferred]. [10. Status bar color doesn't match: Match the value to the color at the very top]
- **should** (tooling, react): In Next.js set theme-color through the viewport export with themeColor: [{ media, color }]. Why: That is where Next.js sets the tag. Values: themeColor: [{ media, color }]. [10. Status bar color doesn't match: In Next.js]
- **must** (color, web): If the app switches theme with a class rather than the OS setting, update the theme-color tag from JavaScript on toggle. Why: The per-scheme tags use prefers-color-scheme, which follows only the OS setting. [inferred] [If the app switches theme with a class rather than the OS setting, update the tag from JavaScript on toggle]
- **should** (platforms, web): For an installed PWA, set apple-mobile-web-app-status-bar-style and the manifest's theme_color and background_color as the same decision as theme-color. Why: They are the same decision for the status bar and chrome. Values: apple-mobile-web-app-status-bar-style, theme_color, background_color. [For an installed PWA, `apple-mobile-web-app-status-bar-style` and the manifest's `theme_color`/`background_color` are the same decision]
- **must** (tooling, web): To test on a phone, connect it over USB, run the dev server on 0.0.0.0 and open it by the machine's LAN IP; debug iOS via Safari > Develop > the device and Android via chrome://inspect. Why: Sticky hover, tap highlight, vh and the URL bar, input zoom, click delay, overscroll, safe areas and the software keyboard are all real-hardware behaviors. Values: 0.0.0.0, chrome://inspect. [11. Right in Chrome, wrong on phone]
- **should** (process, web): Test on a phone that is a few years old, not the newest one on your desk. Why: Real users are not all on the newest device. [inferred] [11. Right in Chrome, wrong on phone]
- **should** (process, web): Test with the software keyboard open, and test in landscape at least once. Why: The software keyboard is a real-hardware behavior that emulation misses; the source gives no separate reason for landscape. [11. Right in Chrome, wrong on phone]
- **should** (process, web): If installation is a target, test as an installed PWA. Why: Standalone mode changes viewport, safe areas and status bar behavior. [11. Right in Chrome, wrong on phone]
- **should** (process, web): Do not treat the Xcode Simulator as the final check; real hardware is the bar. Why: The Simulator is a step up from emulation but still misses touch feel. [The Xcode Simulator is a step up from emulation but still misses touch feel]
- **must** (process, web): Ship the mobile baseline before the first component of any mobile-facing app. Why: It is the floor for feeling native on mobile. [Baseline: this is the floor. Ship it before the first component]
- **must** (platforms, web): Use the baseline viewport meta: width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content. Why: interactive-widget=resizes-content makes the software keyboard shrink the layout viewport on Android Chrome, so 100dvh and bottom-pinned inputs react as they do on iOS. Values: <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content" />. [Baseline]
- **must** (typography, css): Set -webkit-text-size-adjust: 100% on html. Why: It prevents font inflation in landscape. Values: -webkit-text-size-adjust: 100%. [Baseline]
- **must** (components, css): In the baseline, apply touch-action: manipulation, user-select: none and -webkit-user-select: none to button, a and [role="button"], and keep all :hover rules inside @media (hover: hover) and (pointer: fine). Why: It removes tap delay, long-press selection and sticky hover from the start. Values: touch-action: manipulation, user-select: none, -webkit-user-select: none, @media (hover: hover) and (pointer: fine). [all :hover rules live here]
- **must** (process, web): Run the Never Ship table as a self-check before finishing any mobile work. Why: It lists the defects that must not ship and their replacements. [Never Ship: Self-check before you finish]
- **should** (process, all): Report mobile fixes in a few lines: what was wrong (symptom and one-line why), what changed (file and declaration), and what needs a phone; do not pad it into a report. Why: The code is the deliverable. [Output]

### Decisions it informs

- Which height unit should a full-height element use on mobile?
  - 100dvh (dynamic): Resizes as the URL bar shows and hides, tracking the visible area; causes layout shifts on marketing content mid-scroll. When: App shells, drawers and anything bottom-pinned.
  - 100svh (small): The smallest the viewport gets; stable and never overflows, so nothing is cut off. When: Heroes and first screens on marketing pages.
  - 100lvh or 100vh (large): The height with browser chrome collapsed; on load it overflows by the URL bar and bottom-pinned buttons sit under it. When: Almost never; 100vh only as a fallback line for old browsers when the support matrix demands it.
  - Recommendation: 100dvh for app shells and bottom-pinned UI, 100svh for heroes; never 100vh for an app shell and never 100dvh on a marketing hero.
- Should the page itself bounce and pull-to-refresh when scrolled past the top?
  - overscroll-behavior: none on html and body: No pull-to-refresh on Android Chrome and no whole-page rubber band on iOS; the app feels installed. When: Apps with their own scroll containers, a drawer dragged down, or a canvas.
  - Keep default page overscroll: Pull-to-refresh and page bounce stay available. When: A scrolling document where pull-to-refresh is welcome.
  - Recommendation: none on the root for apps, and overscroll-behavior: contain on every inner scrollable; drop the root rule only for scrolling documents.
- How should a horizontal carousel handle swipes?
  - Native scroll with scroll-snap: scroll-snap-type: x mandatory on the track and scroll-snap-align: start on slides; uses the browser's own physics and needs no touch-action. When: When the carousel can be native scroll.
  - JS gesture with touch-action: pan-y: The carousel handles horizontal drags while the browser keeps vertical panning, stopping the page from jittering. When: When the carousel is a custom JavaScript gesture.
  - Recommendation: If the carousel is native scroll, use scroll-snap: the browser's own physics beat a hand-rolled spring and touch-action becomes unnecessary; if it is a JS gesture, set touch-action: pan-y.
- Which touch-action value should a gesture surface get?
  - manipulation: No double-tap zoom, so click fires immediately without the 300ms delay. When: Buttons, links, [role=button] and other tappables.
  - pan-y: Browser keeps vertical panning; the element handles horizontal. When: Horizontal carousels.
  - pan-x: Browser keeps horizontal panning; the element handles vertical drags. When: Vertical sheet handles.
  - none: The element handles every axis; the user cannot scroll past it. When: Only custom gestures that own every axis, like a drag-to-dismiss sheet or a slider.
  - Recommendation: Name only what the browser may still do; use none only where the element truly handles everything.
- What font size should form inputs use when the design wants small input text on desktop?
  - 16px everywhere: iOS Safari never zooms into inputs. When: Default.
  - Smaller on desktop, 16px under @media (pointer: coarse): Desktop keeps smaller input text; touch devices get 16px so focus does not zoom the page. When: When the design calls for smaller text in inputs on desktop.
  - Disable zoom with maximum-scale=1 or user-scalable=no: Stops the zoom but is an accessibility failure. When: Never.
  - Recommendation: 16px minimum (1rem at the default root size); scale up only under pointer: coarse if desktop needs smaller text; never disable zoom.
- How should hover styles be switched off on touch devices? (`Q-state-04`)
  - Capability media query: @media (hover: hover) and (pointer: fine) applies hover only to precise hovering pointers; works for mixed devices. When: Always.
  - JavaScript touch detection hook: e.g. useIsTouchDevice(); the wrong tool for a one-line CSS job. When: Never.
  - User agent or screen width sniffing: Guesses at touch and fails on iPads with trackpads, touchscreen laptops and phones with a mouse. When: Never.
  - Recommendation: Gate every hover rule with @media (hover: hover) and (pointer: fine) and give touch users :active feedback.
- When should press feedback fire?
  - :active in CSS: Responds the instant the finger lands, on every input type. When: Default for all tappables.
  - pointerdown in JavaScript: Responds on press when script is needed. When: When the feedback needs JavaScript.
  - click: Responds when the finger leaves, which reads as lag even at 0ms. When: Never as the only press feedback.
  - Recommendation: :active, or pointerdown if JavaScript is needed, at 100-160ms with ease-out.
- How should the status bar and browser chrome color follow the theme?
  - One theme-color meta per prefers-color-scheme: Light and dark each get a matching bar. When: When the theme follows the OS setting.
  - Update theme-color from JavaScript on toggle: The bar follows an in-app theme switch. When: When the app switches theme with a class rather than the OS setting.
  - A single theme-color: Light mode gets a dark bar or dark mode gets a white one. When: Never.
  - Recommendation: One tag per scheme, valued at the header background color, not the brand color; update from JavaScript if the theme is class-driven.
- Where should mobile fixes be verified before calling them done?
  - Chrome device emulation: Reproduces none of the mobile bugs; shipping on it ships them all. When: Never as proof.
  - Xcode Simulator: A step up from emulation but still misses touch feel. When: Not as the final check; the source calls it a step up from emulation, so using it for intermediate checks is [inferred].
  - Real hardware: Shows sticky hover, tap delay, rubber-banding, safe areas and the keyboard. When: Always before done; ideally a phone a few years old, with the keyboard open, once in landscape.
  - Installed PWA on hardware: Shows standalone-mode changes to viewport, safe areas and status bar. When: When installation is a target.
  - Recommendation: Real hardware is the bar; say which fixes still need a device if you cannot test on one.

### Process

1. Match the symptom: Start from the symptom table, match what the user sees, and read that section for the reason and the exact code.
2. Apply the fix where its reason holds: Use the CSS declaration or meta tag, not JavaScript, and apply it only where the why applies (for example user-select: none on controls, never on body).
3. Gate by capability: Use (hover: hover), (pointer: fine), (pointer: coarse), env() and dvh/svh instead of user agent or width checks.
4. Ship the baseline first: For a new mobile-facing app, add the viewport and theme-color meta tags and the html, input and button CSS baseline before the first component.
5. Test on real hardware: Connect the phone over USB, run the dev server on 0.0.0.0, open by LAN IP, inspect via Safari > Develop or chrome://inspect; use an older phone, open the keyboard, try landscape once, and test as an installed PWA if that is a target.
6. Run the Never Ship self-check: Check the output against the Never Ship table before finishing.
7. Report briefly: State what was wrong (symptom and one-line why), what changed (file and declaration), and what needs a phone to confirm; the code is the deliverable.

### Examples and visual references

- Sticky hover on a button that scales up: A button with a hover scale stays scaled up after being tapped, because touch browsers apply :hover on the first tap and leave it; fixed by gating hover behind (hover: hover) and (pointer: fine).
- Gray/blue tap flash (iOS Safari and Android Chrome): A translucent highlight painted over any tapped element with a click handler; the loudest sign that a page is a website.
- 100vh overflow under the URL bar (Mobile browsers): On load the URL bar is visible, so a 100vh element overflows by its height and a bottom-pinned button sits hidden under it.
- Input focus zoom (iOS Safari): Focusing an input under 16px zooms the page and it does not zoom back on blur, leaving a cropped, drifted layout.
- Press feedback CSS: .button transitions transform 100ms var(--ease-out) and background 100ms; :active scales to 0.97 and changes background to var(--gray-4), so the button responds as the finger lands.
- Safe-area padding (Notch, Dynamic Island and home indicator zones): With viewport-fit=cover the page paints edge to edge; the header pads top by env(safe-area-inset-top), the bottom bar pads by env(safe-area-inset-bottom), and a sheet pads by calc(1rem + env(safe-area-inset-bottom)).
- Long-press selecting a button label (iOS): Holding a finger on a web button selects its text or pops the copy/share callout on a link; native controls never do this.
- Carousel jitter: A horizontal swipe makes the page jitter up while the carousel moves because the browser guesses the axis; touch-action: pan-y or native scroll-snap fixes it.
- Mismatched status bar: With a single theme-color, light mode gets a dark bar or dark mode a white one; separate tags per scheme (#ffffff light, #0a0a0a dark in the sample) fix it.
- Mixed-input devices (iPads with trackpads, laptops with touchscreens, phones with a mouse): Why touch and mouse must be handled together and gated by capability.
- Mobile baseline: Viewport meta with viewport-fit=cover and interactive-widget=resizes-content, per-scheme theme-color, html tap-highlight transparent, text-size-adjust 100%, overscroll none, 16px inputs, touch-action manipulation and user-select none on buttons and links, and all hover rules in the capability query.

### Numbers

- 300ms: Click delay browsers add after a tap while waiting for a possible double-tap zoom. [5. Tap feels laggy: The 300ms click delay]
- 16px: Minimum input, textarea and select font size to stop iOS Safari zooming on focus (1rem at the default root size). [4. Page zooms into the input]
- 100–160ms: Duration range for press feedback, with ease-out. [5. Tap feels laggy]
- 100ms: Transition duration for transform and background in the sample press-feedback CSS. [5. Tap feels laggy: .button code]
- scale(0.97): Transform on :active for press feedback. [5. Tap feels laggy: .button:active]
- scale(1.02): Sample hover transform, gated behind the hover capability query. [1. Hover state stuck after tap]
- 0ms: Even at 0ms, feedback on click (release) reads as lag. [5. Tap feels laggy: Feedback on release instead of press]
- 100vh: The largest viewport on mobile (chrome collapsed); on load it overflows by the URL bar height. Keep only as a fallback line for old browsers when the support matrix demands it. [3. Layout has the wrong height]
- 100dvh: Height for app shells, drawers and bottom-pinned UI. [3. Layout has the wrong height]
- 100svh: Minimum height for heroes and first screens. [3. Layout has the wrong height]
- 0px: Value of every env(safe-area-inset-*) without viewport-fit=cover, and the recommended env() fallback in calc. [7. Content stops at the notch]
- calc(1rem + env(safe-area-inset-bottom)): Bottom padding for sheets. [7. Content stops at the notch]
- #ffffff / #0a0a0a: Sample theme-color values for light and dark schemes. [10. Status bar color doesn't match; Baseline]
- 100%: -webkit-text-size-adjust value that prevents font inflation in landscape. [Baseline]
- 0.0.0.0: Host to run the dev server on so the phone can open it by LAN IP. [11. Right in Chrome, wrong on phone]

<!-- /od:learn -->
