---
type: synthesis
title: Mobile app patterns
created: 2026-09-24
updated: 2026-09-28
sources:
  - 14h1VnkQvIc
  - 9ypqs_2fAl8
  - AH_ugxmLeUM
  - E7RzEZ8GlHE
  - Gfsd8NNuD9g
  - Qsq-Sj_rojU
  - ek-building-a-drawer-component
  - eks-readme
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-mobile-native-skill
  - gKM6b2EnW1k
  - goWOAFqJHpA
  - ixUq4HM4FNg
  - jSxxAFxjxbU
  - kdRkuqu8apE
  - qK7WYCMvjUw
  - tNMAFjzapOk
  - vaul-inputs
tags:
  - od-area-platforms
---

# Mobile app patterns

## In short

A phone is small, usually held in one hand and driven by a thumb, and it has no hover. So navigation moves to a bottom bar of three to five items, the most-used controls sit low where the thumb can reach, and text and spacing stay as big as on desktop or get bigger. Each screen does one job, side tasks open in a bottom sheet so people keep their place, and gestures such as swipe back, swipe down to close and long press make an app feel native, as long as a visible button does the same thing. Consumer apps also wrap the product in phone-only screens: a short explanation before the system asks for notification permission, subscription screens after onboarding and at later moments, and sometimes no login at all; these come from practitioners' tests and still have to pass OpenDesigner's rules on ways out and design tricks. A web app on a phone also needs a short list of technical fixes (no sticky hover, no gray tap flash, 16px inputs, safe areas, the right full-height units), a native app should use the platform's own sheets, tabs and screen changes, and both are only checked for real on a real phone.

## House standards

**The web on a phone**
- **STD-mobile-touch-21** (must): ship the mobile baseline before the first component: the viewport meta with `viewport-fit=cover` and `interactive-widget=resizes-content`, one theme-color per scheme, no tap highlight, `-webkit-text-size-adjust: 100%`, `overscroll-behavior: none`, 16px inputs, `touch-action: manipulation` and `user-select: none` on buttons and links, and every `:hover` rule gated.
- **STD-mobile-touch-02** (must): decide touch behavior with capability media queries and platform features (`hover`, `pointer`, `env()`, `dvh`), never by user agent or screen width.
- **STD-accessibility-motion-15** (must): put every `:hover` style inside `@media (hover: hover) and (pointer: fine)` and leave `:active` press feedback ungated.
- **STD-mobile-touch-03** and **-06** (must): remove the tap highlight once, globally, and give every tappable element its own `:active` state; `touch-action: manipulation` on tappables removes the tap delay.
- **STD-mobile-touch-10** (must): `100dvh` for app shells, drawers and bottom-pinned UI, `100svh` for heroes, never `100vh`.
- **STD-mobile-touch-11** (must) and **-13** (should): inputs at 16px or larger, and each field opens the right software keyboard.
- **STD-mobile-touch-14** and **-15** (must): contain overscroll with `overscroll-behavior`, never with a `touchmove` listener.
- **STD-mobile-touch-16** (must): paint edge to edge and pad headers, tab bars, toasts and sheets with `env(safe-area-inset-*)`.
- **STD-mobile-touch-17** (must): controls are unselectable; text that is content stays selectable.
- **STD-mobile-touch-18** (must) and **-19** (should): set `touch-action` per gesture surface, and prefer native scroll-snap carousels.
- **STD-mobile-touch-20** (must): one theme-color per color scheme, matched to the top of the page, not the brand color.
- **STD-accessibility-motion-27** (must): never disable pinch zoom.

**Touch feel, web and native**
- **STD-mobile-touch-09** (must): targets at least 44x44pt on iOS and 48dp on Android, and a 44px hit area for small web controls; grow the hit area, never the visual.
- **STD-components-toasts-drawers-72** (must): feedback the instant the finger lands, commit on release.
- **STD-mobile-touch-05** (must): pressables scale to 0.97 for 100-160ms on the web, 100-150ms in React Native.
- **STD-mobile-touch-28** (must): once a drag starts, ignore extra fingers.
- **STD-accessibility-motion-20** (must): a haptic is never the only feedback.

**Native apps (React Native and Expo)**
- **STD-mobile-touch-30** (must): redesign every hover affordance as press, position or nothing.
- **STD-mobile-touch-41** (must): use the platform's own pieces (formSheet, NativeTabs, native menus and previews, large-title headers, RefreshControl, ReanimatedSwipeable) instead of JavaScript rebuilds.
- **STD-mobile-touch-42** and **-44** (must): screen changes stay on the native stack at the platform's duration (`modal` for a task people can abandon, `formSheet` with detents for a short interruption), and any custom animation sets `animationMatchesGesture`.
- **STD-when-to-animate-14** (must): tab switches never slide. **STD-when-to-animate-05** (must): nothing people see 100+ times a day animates.
- **STD-components-toasts-drawers-60** (must): form sheets work on both platforms: at most three detents, single-screen content, and a drag cue besides the iOS-only grabber.
- **STD-mobile-touch-61** (must) and **STD-components-toasts-drawers-45** (should): UI follows the software keyboard, frame by frame in native apps and with the Visual Viewport API in a web drawer.
- **STD-accessibility-motion-04** (must): under reduced motion, native screen changes become a fade.

**First-run, permission and subscription screens**
- **STD-visual-details-41** (should): ask for private data at the moment it is needed, only for what is needed, and say why.
- **STD-accessibility-motion-24** and **STD-visual-details-33** (must): never trap people; every screen and overlay has a way out.
- **STD-when-to-animate-09** (must): spend delight motion only on rare or first-time moments such as onboarding, first run and completion.
- **STD-visual-details-39** (should): offer choices instead of one forced path.

**Process**
- **STD-process-review-taste-33** (must): judge touch and gesture feel on a real phone; emulation, simulators, dev builds and Expo Go never count.
- **STD-visual-details-42** (should): adapt to the platform: quick touch interactions on a phone.

## What the sources teach

### Navigation moves to the bottom
- Replace the desktop sidebar with a bottom bar of three or four links, five at most, often floating with the main action broken out. Keeping to five or fewer keeps every target over 44 pixels [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]). When too many sections matter, turn the sidebar into a home page, as Notion does, and use the freed bottom for a big search bar or action button [S-L19-053].
- Put the important controls at the bottom, where they are easier to reach, even though pushing everything to the top looks good. On the mobile web, check that the browser bar does not cover bottom navigation [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- TikTok is held up as low-effort mobile UX: the main action (swipe up) covers almost the whole screen, navigation sits at the bottom, and action icons line up on the right for the 70-80% of people who are right-handed [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]). The percentage is a single-video figure.
- Tab bar polish: drop a raised, circled "add" button into line with the other icons, because it is the tab people use least; keep inactive icons clearly visible and give the active tab its own style (a good place for brand color); spread the icons a little to widen click areas; add labels when icons are obscure, dark enough to read. A dark, translucent, blurred bar is shown as an option [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Top-bar and bottom-bar actions change with the context: opening a note hides the nav bar and shows formatting and sharing instead [S-L19-053]. The gamified finance concept app uses four tabs: goals, leaderboard, spending analytics and education [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Don't shrink, simplify
- A desktop design squished onto a phone is too small. Type and spacing stay about the same as desktop or get larger; iOS's base font is 17 against macOS's 13. Zoom out and compare with real apps to check [S-L19-053]. The video says "pixels"; Apple measures these in points [inferred].
- Mobile screens need more space than designers expect, especially between stacked items [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Each mobile section runs in one direction, a vertical stack or a horizontal scroll, never both. A desktop dashboard with five panels becomes one panel per screen [S-L19-053].
- Cards are the main building block because they group content without needing white space, but a card inside a card makes "padding on padding" [S-L19-053].
- One screen does one job (the home screen is the exception). Something new gets a new page, not a new layout [S-L19-053].
- Swipeable scrolling cards are preferred to stacking the same items, with page indicators under them [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]). Arrows on content people can swipe are redundant clutter [S-L19-045].
- How much fits on a screen is partly cultural: one Mobbin video says users in Eastern markets are more comfortable with information-heavy screens, so a flow that works for one audience can't simply be copied. It gives no source for this [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).

### Sheets keep people in place
- A bottom sheet handles a side task that should not pull people away, such as picking a template while editing: a title, a search bar, a check to confirm and an X to close [S-L19-053]. Emil Kowalski prefers a drawer to a modal on mobile for a more native feel, with snap points like Apple Maps [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- In a native app: `formSheet` when the sheet is its own destination, a custom drag-to-dismiss sheet only when it must live inside a screen, `modal` for a self-contained task, and `formSheet` with detents for a picker, filter or share. Android caps detents at three and shows no grabber [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]) [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- As a sheet rises, the page behind can zoom out and move down, then reverse on dismiss [S-L19-053] [S-L19-035]. Vaul offers the same as an opt-in, `scaleBackground` [S-L19-005].
- The web drawer moves on the iOS-like curve `cubic-bezier(0.32, 0.72, 0, 1)` for 500ms. It can be dragged only when its content is scrolled to the top, blocks dragging for 100ms after reaching the top so a fast scroll doesn't close it, and ignores a second finger [S-L19-005].
- When an input in a sheet opens the keyboard, the sheet must stay usable: Vaul repositions the drawer so the keyboard doesn't push content up (`repositionInputs`) [S-L19-096] ([[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]); the drawer article sits the drawer above the keyboard with the Visual Viewport API, with a slight delay [S-L19-005]; native UI follows the keyboard's real position frame by frame [S-L19-015].

### Gestures, always with a visible way out
- Mobile swipes fall into three groups: moving within a page, moving between pages, and gestures that replace a button or reveal more [S-L19-035].
- Common gestures: swipe right to go back, with the page behind moving about 35%; swipe down to close a sheet; swipe up to search (Slack); and long press as the mobile right click, which blurs the rest of the screen, shows actions and zooms the element slightly [S-L19-053].
- Teach a swipe before relying on it [S-L19-053], and give swipe actions buttons for people who don't know them, as Gmail does for delete [S-L19-035]. The video hedges a long-press fallback as "probably" good UX; making a visible alternative a rule for every gesture comes from WCAG 2.5.7 (DC-L10-15), not from the video.
- A swipe-to-confirm slider suits high-impact or irreversible actions (Resend's send, a crypto purchase), because a slider is harder to trigger by accident than a button [S-L19-035].
- Screen changes follow the swipe's direction and keep continuity, such as an image growing into the next page's hero, rather than sliding a new page in [S-L19-035]. Direction carries meaning: tools sliding up from the bottom read as temporary, and screens sliding in from the left show progress through onboarding [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- Mechanics for native apps: decide a flick by projected momentum (a sheet dismisses when its projected position passes 40% of its height), hand the release velocity to the spring, rubber-band past edges, declare the axis of any pan inside a scroll view, and never animate a header's height [S-L19-015].

### Touch feel and the web platform layer
- Most "janky on mobile" reports are platform problems, not animation problems: sticky hover, the gray tap flash, the 100vh bug, inputs that zoom the page, a tap delay, pull-to-refresh hijacking scroll, content under the notch, long press selecting button text, carousels scrolling the wrong way and a mismatched status bar. Almost every fix is one CSS declaration or meta tag [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]) [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- Touch and mouse coexist on iPads with trackpads and laptops with touchscreens, so gate by capability, never by device [S-L19-028].
- Press feedback fires when the finger lands (`:active` or `pointerdown`, never `click`): scale 0.97 over 100-160ms with ease-out on the web [S-L19-028]; 0.97 in 100-150ms in React Native (the recipe uses 120ms), with `hitSlop` to reach 44pt and `pressRetentionOffset` so a drifting finger doesn't cancel the press [S-L19-016] [S-L19-015].
- Mobile has no hover, so every hover affordance becomes press, position or nothing [S-L19-016].
- Haptics: a selection tick when a value steps, a light impact when something snaps home, a medium impact for a heavy landing or destructive action, success or error notifications; in the same frame as the visual, once per action, never the only feedback [S-L19-016].

### First use and onboarding
- Design a first-use empty state that points at the main action with a simple explanatory popover, and a no-results state with imagery, suggestions for typos and a way out [S-L19-053].
- Onboarding is the best moment to captivate mobile users: a clean, focused UI, then a swipe animation, then a surprise, as in Craft [S-L19-084]. Show the app's value (a swipeable spending breakdown) before adding game mechanics [S-L19-078].
- A step-by-step flow can use a control that is tapped or swiped, with motion that wraps into the next slide [S-L19-035].
- Answers collected during onboarding can shape the first session: Moonly's home-screen quick-access buttons follow them [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]). The wider onboarding material is in the [[synthesis/onboarding|Onboarding synthesis]].

### Permission and account screens
- In Mobbin's sample, web onboarding is 21% shorter than iOS onboarding; the video suggests, with a "might", that phone apps simply have more permission and paywall screens built in [S-L19-107].
- Many apps show their own screen before the system notification prompt, saying what the notifications are for (Brilliant: reminders so learning becomes a habit); Center also previews the notification people would receive. The video says this "apparently" raises accept rates a lot and gives no figure [S-L19-107].
- Ask why a login is needed before copying one from other apps. Moonly, with 10 million users, has no login screen: its data already sits in the Apple keychain and follows people to a new iPhone, SMS codes don't always arrive in seconds, typing a real email adds friction, and people are used to Sign in with Apple hiding their address. On Mobbin, 12% of apps have no sign-up or login step anywhere [S-L19-111].
- Other flows postpone the account. Duolingo takes people through about 60 screens, including a finished first lesson, before sign-up, and the video says it doesn't feel long [S-L19-107]. A paywall consultant prefers creating the account before the paywall so the subscriber has a user ID, though his own tests of the order were inconclusive [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Paywalls across the app's life
- In consumer phone apps the paywall is a flow with several touch points: right after onboarding (78% of the iOS apps in Mobbin's library show one there), in front of a premium feature, in settings, when a subscriber tries to cancel (a discounted win-back offer), and a last-chance message just before someone deletes the app [S-L19-106]. A well-designed paywall shown at the wrong moment is still a bad paywall [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Sheets do the side work: extra plans sit behind a "view all plans" button that opens a sheet, and tapping cancel on a yearly offer can open an exit-intent sheet offering the monthly plan [S-L19-104].
- At Moonly, a separate paywall per feature made people think each feature was sold separately; one paywall that unlocks everything won. A soft paywall (one people can close) won globally, although its close button appears only after 5 seconds, and a hard paywall won in the US [S-L19-111].
- A one-time offer that is gone once closed is paired with animation and haptic feedback to catch attention at the moment someone considers upgrading [S-L19-104]. Focus Flight's offer is shaped like a flight ticket, and the phone vibrates as it prints [S-L19-107].
- Store and payment rules shape these screens. In early 2026 Apple began rejecting paywall patterns that relied on free-trial toggles, some of which it considered confusing or misleading [S-L19-104]; only this video reports it. With Apple's own payments, half of Moonly's cancellations came within 3 minutes of purchase because cancelling is one tap, so it added Stripe as an alternative in the US; on Android, alternative billing has to go through Google's own SDK, whose screen the founder says scares buyers away and lacks Google Pay [S-L19-111]. These are one founder's figures and platform rules that date quickly.
- Pricing by device (a higher price for a new phone on 5G, a lower one for an older phone on 3G in low-battery mode) is named as one of the last levers to test, because it is a lot of work for smaller gains [S-L19-106]. The video doesn't discuss whether it is fair.
- Plans, trials, copy and testing order are covered in the [[synthesis/paywalls-and-pricing-pages|Paywalls and pricing pages synthesis]].

### Personal data people want to share
- Many of the standout dashboards in Mobbin's review were on phones: Opal shows screen-time insights as an Instagram-style story that people swipe through like content and share, and Orbit makes tracking subscriptions enjoyable. Nearly one in five products on Mobbin use the dashboard as the home screen [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- When someone takes a screenshot in Moonly, a ready-made flow lets them share it in one tap; 23% of its users share something, because people share insights about themselves, not features [S-L19-111].

### Checking the work
- The phone is the source of truth: Chrome device emulation reproduces none of these bugs. Test an older phone, with the keyboard open, in landscape at least once, and as an installed PWA when that is a target; when something can't be verified without a device, say so [S-L19-028]. Native motion is judged on a release build on the slowest supported device [S-L19-016].

## Where they agree and disagree

- **Bottom navigation with 3-5 items (agree).** The videos [S-L19-053] [S-L19-076] [S-L19-077] match DC-L10-09 (bottom bar on phones with 3-5 destinations; controls in the middle and bottom are easier to reach), DC-L08-19, DC-L03-19 and the `adaptive-bar-rail-sidebar` default of Q-layout-04. The "sidebar becomes the home page" pattern [S-L19-053] has no matching Q-layout-04 option.
- **Target sizes (agree; units differ).** 44 "pixels" [S-L19-053], 44x44pt and 48dp with `hitSlop` [S-L19-016], and wider tab click areas [S-L19-075] agree with STD-mobile-touch-09, DC-L03-12 and DC-L10-15. The video's pixels are points on iOS and dp on Android [inferred].
- **Text size (agree, with one recorded conflict).** "Don't shrink; iOS body is 17" [S-L19-053] matches Q-type-08's `17` (iOS Body) option and DC-L14-13 (desktop dense at 13-14px, phone comfortable). Separately, `standards.json` records that Q-type-08 defaults a web app to a 14px body and that the generated preview styles its inputs with that body size, which makes iOS Safari zoom (STD-mobile-touch-11); the 16px `font.size.input` token the standard adds is not yet used by any generated style.
- **Sheets on phones (agree).** Drawers over modals [S-L19-005] and sheets for side tasks [S-L19-053] match DC-L08-20's default (bottom sheet on phones). Kole Jain's "new page by default, sheet to keep context" and the house split between `modal` and `formSheet` (STD-mobile-touch-42) fit together [inferred]. Zooming the page behind [S-L19-053] [S-L19-035] matches STD-visual-details-20 (push the background back for a modal task).
- **Custom screen changes (disagree).** Kole Jain favors custom transitions: a card that expands into a page with an elastic snap, an image that zooms into the next hero, a circle wrap [S-L19-035]. The house standards keep screen changes on the native stack at the platform's duration (STD-mobile-touch-42) and give core navigation no extra motion (STD-when-to-animate-05); DC-L10-14 likewise lets the OS own screen changes and the brand own motion inside a screen. A custom transition is still possible on the native stack with `animationMatchesGesture` (STD-mobile-touch-44), and delight motion is allowed on rare moments such as onboarding (STD-when-to-animate-09), which is where the circle wrap sits [inferred]. Q-motion-06 offers `container-transform`, and `standards.json` refuses its `fade-through` option (offered for tabs) under STD-when-to-animate-05 and -14. The 35% swipe-back parallax [S-L19-053] describes a look that the native stack provides, so building it by hand is the only conflict [inferred].
- **Bounce (agree, with a condition).** Opening up the curve so swiped cards carry momentum [S-L19-035] fits STD-mobile-touch-51, which allows overshoot only when the gesture carried momentum; a swipe does [inferred]. "Almost never a linear ease" [S-L19-035] agrees with the Expo skill, which keeps linear for constant motion such as progress bars [S-L19-016].
- **Gestures need an alternative (agree), except swipe-to-confirm (tension).** A button for every swipe [S-L19-035] and teaching swipes first [S-L19-053] match Q-plat-03 ("avoid drag-only interactions without a non-drag alternative", WCAG 2.5.7) and DC-L10-15. The swipe-to-confirm slider [S-L19-035] is itself drag-only, and the video gives it no tap alternative, so WCAG 2.5.7 would still require one [inferred].
- **Arrows on swipeable content (partial tension).** Remove them on mobile [S-L19-045], but add page indicators and a button for people who don't know the gesture [S-L19-035]. Indicators keep the "there is more" signal; arrows may still matter where there is a pointer and no swipe [inferred].
- **Tab labels (partial disagreement).** Label obscure icons [S-L19-075]; the mistakes video leaves three well-known bottom-nav icons unlabeled and suggests a tooltip pop-up during onboarding for two unclear ones [S-L19-045]. That pop-up is an onboarding hint, not a hover tooltip, so it works on a phone, but it explains the icon once and leaves it unlabeled afterwards [inferred]. Q-icon-05 defaults to labels, and DC-L10-09 asks for an accessibility label on every tab icon whether or not text shows.
- **Fewer choices (disagree with research).** The TikTok teardown says more options lead to worse decisions and names Hick's law [S-L19-077]; its analysis notes that the speed argument it gives (target size and distance) is Fitts's law. OpenDesigner's L13 law table warns that Hick's law does not justify deleting options, since novices scan lists linearly and grouping and search are the fix. The same table's Fitts's law row says screen-edge targets help mouse users but hurt touch users, which bears on the right-edge icon column [inferred].
- **Where to test (mostly agree).** All three Emil sources test on real phones [S-L19-005] [S-L19-016] [S-L19-028]. The drawer article also accepts the Xcode Simulator as an alternative [S-L19-005]; the mobile-native skill calls it a step up from emulation that still misses touch feel, with real hardware as the bar [S-L19-028], and the Expo skill never judges feel in it [S-L19-016]. STD-process-review-taste-33 settles it on the stricter side.
- **Sheet timing differs by platform (no conflict).** A web drawer runs 500ms on the iOS curve [S-L19-005] (STD-enter-exit-origin-41); a native sheet uses a spring of about 300ms perceived duration [S-L19-016] (STD-easing-duration-07). `standards.json` records that OpenDesigner's `motion.transition.expand`, which sheets use, runs `motion.duration.long` (250ms under STD-easing-duration-07) on the enter curve, which matches neither, and that the drawer duration and curve tokens STD-enter-exit-origin-41 adds are not used by any transition yet.
- **Reduced motion (gap in the videos).** None of Kole Jain's mobile videos mention it; the swipe video's analysis says so. The Emil sources ship it with the animation and turn native screen changes into a fade [S-L19-016] [S-L19-015] (STD-accessibility-motion-01, -04).
- **Notification primers (fill a recorded gap).** The first L19 cards recorded that no source covered notification permission prompts or mobile paywalls. [S-L19-107] now describes the primer screen, but only as an observation with no figure; DC-L19-129 puts a primer in its setup checklist, and DC-L19-154 covers when and how to ask. Explaining the benefit before the system prompt fits STD-visual-details-41 (ask when it is needed and say why) [inferred]; a primer shown again after "not now" would fall under DC-L13-15's check for re-prompting after a dismissal [inferred].
- **Two paywall videos, one voice.** [S-L19-104] and [S-L19-106] both interview the same consultant, Jonathan Parra, so where they agree (show two plans with yearly preselected, test radically different designs first, avoid spin-the-wheel offers) it is one practitioner's opinion, not two. [S-L19-111] also splices in clips from earlier Mobbin guests.
- **One paywall or contextual ones (apparent disagreement).** [S-L19-104] says paywalls placed at each moment of the customer's life speak more to people because they are personal; [S-L19-111] says every per-feature paywall failed Moonly's tests. The first is about when a paywall appears, the second about whether each feature gets its own offer, so one paywall that unlocks everything can still appear at several moments [inferred].
- **Ways out (tension with the standards).** A close button that appears only after 5 seconds and a hard paywall with no way past [S-L19-111] sit against STD-accessibility-motion-24 and STD-visual-details-33 (every screen and overlay has a way out) and against DC-L19-135, which says paywalls and prompts always have one [inferred]. Exit-intent sheets, cancellation win-backs and a last message before deletion [S-L19-104] [S-L19-106] come close to DC-L13-15's "repeated requests after a choice was made" [inferred]. The sources themselves reject fake urgency and spin-the-wheel paywalls for a long-term business [S-L19-104] [S-L19-106], which agrees with DC-L13-15 and Q-pattern-05's `enforced` default, and ClassPass (fewer than five screens to subscribe, 17 to cancel) [S-L19-104] is exactly the case DC-L13-15's hard-to-cancel check targets (a cancel flow with more steps than sign-up).
- **Haptics on offers (mostly agree).** Both haptic examples pair the vibration with animation [S-L19-104] [S-L19-107], so the haptic is not the only feedback (STD-accessibility-motion-20) [inferred]. The ticket vibrates while it prints, whereas DC-L19-98's rule of thumb vibrates when something catches or completes, never while it moves [inferred]. Delight on a paywall fits STD-when-to-animate-09 only while the screen is rare, such as the end of onboarding, not an offer people meet on every launch [inferred].
- **Login (sources disagree).** No login at all [S-L19-111] versus an account before the paywall [S-L19-106]; DC-L19-129's default keeps a way to log in and a skip in every sign-up. Moonly's approach relies on the Apple keychain, and the source says nothing about Android [inferred]. Duolingo's 60 screens before sign-up [S-L19-107] and Moonly's 30-screen onboarding [S-L19-111] no longer clash with DC-L19-129: its updated default accepts a long flow when each screen personalises or moves toward value, and it now offers `no-account` as an account-timing option (proposed Q-pattern-15), which DC-L19-156 extends.
- **Paywall shares don't compare.** 78% of iOS apps in Mobbin's library show a paywall after onboarding [S-L19-106]; 22% of 900-plus apps and websites show one during onboarding [S-L19-107]. The samples (iOS only against apps and websites) and the moment (after against during) differ, so the two figures are not a contradiction [inferred]. Both are Mobbin library counts, not industry measures.
- **Story-format data (agree, with the gesture rule).** Opal's swipeable story [S-L19-110] is the same one-direction horizontal pattern as Kole Jain's swipeable cards [S-L19-035], so it needs the same visible alternative to swiping (Q-plat-03, DC-L10-15) [inferred].
- **Density by culture (unsourced).** The claim that users in Eastern markets prefer information-heavy screens [S-L19-107] comes with no evidence; if true, it limits "don't shrink, simplify" [S-L19-053] to some audiences [inferred]. Q-dir-02 sets density per product, not per market.
- **OpenDesigner's own preview (recorded conflicts).** `standards.json` notes that `engine.py`'s preview page writes a viewport meta without `viewport-fit=cover` or `interactive-widget` (STD-mobile-touch-21) and ungated `:hover` rules that stick after a tap (STD-accessibility-motion-15).

## Decisions this informs

- **Q-plat-01, Q-plat-02** (phone in scope): a mobile-facing web app gets the baseline first (STD-mobile-touch-21) [S-L19-028]; a native app gets the platform's own pieces [S-L19-016]. Choosing iOS or Android also brings store and payment rules that change subscription screens (Apple rejecting some free-trial toggles, alternative billing on Android; both dated, single-source reports) [S-L19-104] [S-L19-111].
- **Q-plat-03** (what people press with): touch means 44pt / 48dp targets [S-L19-053] [S-L19-016], press feedback on press-in [S-L19-028], and a non-drag alternative for every gesture [S-L19-035].
- **Q-plat-05, Q-plat-10** (look like the platform or the brand): the sources keep behavior native (sheets, tabs, menus, screen changes, back swipe) and put the brand in content and details [S-L19-016] [S-L19-015], which fits the `hybrid` and `custom-skin` defaults [inferred].
- **Q-layout-04** (where the menu sits): bottom bar with 3-5 items [S-L19-053] [S-L19-077]; a possible new option is "the sidebar becomes the home page" [S-L19-053].
- **Q-icon-05** (labels on icons): label obscure tab icons, dark enough to read [S-L19-075]; an onboarding tooltip can introduce an unclear icon [S-L19-045], but only a label keeps explaining it afterwards [inferred].
- **Q-space-03** (target size): 44pt / 48dp, widened with `hitSlop` or spacing [S-L19-016] [S-L19-075].
- **Q-type-08** (body size): don't shrink on phones; 17pt is the iOS reference [S-L19-053]; web inputs stay at 16px or larger [S-L19-028].
- **Q-dir-02, Q-dir-04** (density, grouping): roomier than expected on mobile [S-L19-045], though density expectations may differ by market (an unsourced claim) [S-L19-107]; cards as the main mobile grouping, avoiding a card inside a card where possible [S-L19-053], even though Q-dir-04 defaults to space first.
- **Q-pattern-01** (dialog, sheet or pop-up): bottom sheets on phones [S-L19-005] [S-L19-053]; `modal` for self-contained tasks and `formSheet` with detents for short interruptions [S-L19-015]; on a paywall, a sheet for "view all plans" and for the exit-intent offer [S-L19-104].
- **Q-pattern-03** (show everything or disclose progressively): `progressive` on paywalls: two plans shown, the rest behind a "view all plans" sheet [S-L19-104] [S-L19-106].
- **Q-pattern-04** (empty screens and first use): first-use and no-results states [S-L19-053]; value-first onboarding [S-L19-078]; one captivating moment in onboarding [S-L19-084]; a custom screen before the notification prompt [S-L19-107] and a first session shaped by onboarding answers [S-L19-111], which the question's options don't name yet [inferred].
- **Q-pattern-05** (design tricks policy; planned, default `enforced`): the paywall sources reject fake urgency and spin-the-wheel offers for a long-term business [S-L19-104] [S-L19-106]; ClassPass's 17-screen cancel flow is a test case for the hard-to-cancel check [S-L19-104]; a delayed close button [S-L19-111], exit-intent sheets and offers shown before deletion [S-L19-104] [S-L19-106] are candidates for human review [inferred].
- **Q-motion-06** (screen changes): tension between custom continuity transitions [S-L19-035] and native-stack screen changes with no tab animation [S-L19-016].
- **Q-motion-09** (system or brand screen changes and vibrations): the `os-nav-brand-micro` default matches the sources; `haptics-semantic` matches the Expo haptic map [S-L19-016]; the offer examples pair a haptic with animation on a rare, high-stakes screen [S-L19-104] [S-L19-107].
- **Q-motion-07** (reduced motion): native screen changes fade [S-L19-015].
- **Q-state-04** (states by device): `per-input`: gate hover, give touch its own press state [S-L19-028].
- **Q-depth-04** (glass): the dark, translucent tab bar variant [S-L19-075]; `standards.json` refuses the question's `none` and `transient` options under STD-visual-details-16, with a solid fallback under reduced transparency (STD-accessibility-motion-11).

## Visual examples worth showing

- A floating bottom bar with the main action broken out, next to Notion's sidebar-turned-home-page with recent items on top and a big search bar at the bottom [S-L19-053].
- A squished desktop design zoomed out beside normal-sized apps, showing why mobile type and spacing don't shrink [S-L19-053].
- Double-nested cards ("padding on padding") beside the same content grouped with white space inside one card [S-L19-053].
- The template-picker bottom sheet (title, search, check, X) rising while the note editor behind zooms out [S-L19-053].
- The tab bar before and after: raised circled add button, faint inactive icons and near-identical backgrounds, then aligned icons, an active state per tab, a profile-picture tab, wider spacing, optional labels and a dark blurred variant [S-L19-075].
- TikTok's thumb zone: a full-screen swipe target, bottom navigation and a right-edge icon column [S-L19-077]. The Spotify Wrapped redesign with share and volume moved to the bottom and a chapter chip [S-L19-076].
- Cards bouncing and skewing off the screen edge like a 3D ring, with a magnetic page indicator; Resend's swipe-to-confirm slider; Gmail's delete by swipe or by button [S-L19-035].
- Craft's onboarding: tools sliding up from the bottom, screens sliding in from the left [S-L19-084].
- Platform-layer before and after: a button stuck in its hover state after a tap, a bottom button hidden under the URL bar at `100vh` and visible at `100dvh`, a header padded under the notch with `env(safe-area-inset-top)`, and light and dark status bars from two theme-color tags [S-L19-028].
- The native recipes: a drag-to-dismiss sheet whose backdrop fades as it moves, a swipe-to-delete row with the list closing the gap, a collapsing header, and a tab pill sliding to the measured tab [S-L19-015].
- A drawer with a text field kept above the on-screen keyboard [S-L19-005] [S-L19-096].
- Brilliant's and Center's screens before the system notification prompt, Center's with a preview of the notification people would get [S-L19-107].
- Focus Flight's one-time offer printing out as a flight ticket, with a marker where the phone vibrates [S-L19-107].
- A map of paywall touch points across an app's life: after onboarding, a feature gate, settings, cancellation and just before deletion [S-L19-106]; the "view all plans" sheet and the exit-intent sheet offering the monthly plan [S-L19-104].
- Moonly's paywall whose close button appears after 5 seconds, as a cautionary example [S-L19-111], and ClassPass's under-five-screen sign-up beside its 17-screen cancellation [S-L19-104].
- Opal's story-style screen-time insights that people swipe through and share [S-L19-110]; Moonly's screenshot-to-share flow and its home screen with quick-access buttons chosen from onboarding answers [S-L19-111].

## Open questions

- Should Q-layout-04 gain a "the sidebar becomes the home page" option for apps with many important sections [S-L19-053]? DC-L19-49 proposes it as `hub-home` and DC-L19-119 lists it as `sidebar-as-home`; the two names need to become one.
- When may a mobile product use a custom screen transition (a card expanding, an image zooming into a hero) given STD-mobile-touch-42? Only in onboarding and other rare moments, or also for signature navigation built on the native stack?
- A swipe-to-confirm slider is drag-only. What tap alternative keeps it safe from accidental taps and still meets WCAG 2.5.7?
- The right-hand icon column for right-handed people is one video's claim [S-L19-077]. Should layouts mirror for left-handed use, or keep frequent actions centered?
- Should OpenDesigner's CSS export and preview ship the mobile web baseline (STD-mobile-touch-21) whenever Q-plat-02 includes phones, and style inputs at 16px even when the body text is 14px?
- The videos give no values for their swipe animations (no durations, curves, spring settings or skew angles). Should those examples stay as pictures only, with the Expo tables supplying the numbers?
- The permission primer now has proposals (DC-L19-154's proposed Q-plat-16 and DC-L19-129's setup checklist, both with "Not now" sticking). Open: does any source give a figure for how much a primer raises accept rates, and what should a web product do about browser push permission, which no source covers?
- DC-L19-135 now proposes flagging a missing or delayed close control as an error and does not recommend hard paywalls; is that a reading of STD-accessibility-motion-24 and STD-visual-details-33 the owner accepts, given that Moonly reports the delayed close won [S-L19-111]?
- Where is the line between a helpful exit-intent or win-back offer and DC-L13-15's repeated requests after a choice was made?
- DC-L19-129 now offers `no-account` for account timing, and DC-L19-156 recommends it when the device can keep the data. What is the Android equivalent of carrying data over in the Apple keychain? No source says.
- Store and payment rules (free-trial toggles, alternative billing) date quickly. Should OpenDesigner cover them at all, or only point to the platform's current review rules?
