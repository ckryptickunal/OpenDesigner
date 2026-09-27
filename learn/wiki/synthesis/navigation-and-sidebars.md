---
type: synthesis
title: Navigation and sidebars
created: 2026-09-24
updated: 2026-09-28
sources:
  - 14h1VnkQvIc
  - 5JxUJ1fuyO8
  - 9WVt1CelBfg
  - B7k5rOgmOGY
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - HE4rLEQpiXY
  - NtZeYmTMuo4
  - PDcQJOPby1k
  - ToJiXPTNnLY
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Vy0KKvZJRH8
  - Yr2uIcFZDDQ
  - adev-changelog
  - d4MF6pdAZNw
  - eMMiLeo_UGI
  - ek-the-magic-of-clip-path
  - ek-train-your-judgement
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-apple-design-skill
  - eks-skills-find-animation-opportunities-skill
  - gKM6b2EnW1k
  - goWOAFqJHpA
  - ixUq4HM4FNg
  - lkKGQVHrXzE
  - nl8OFGdx75w
  - xHD01_Onac0
tags:
  - od-area-components
---
# Navigation and sidebars

## In short

Navigation tells people where they are, where they can go and how to get back. On a desktop product the sidebar is the spine: grouped links, each with an icon and a short name, a clear active state, and rarely used items such as settings at the bottom. On phones a bottom bar of three to five items, within thumb reach, is the usual pattern, and websites keep their navigation at the top. The house standards say core navigation, tab switches and anything done from the keyboard should not animate, because people use them all day.

## House standards

**Wayfinding and labels**
- `STD-visual-details-33` (must): Every screen answers wayfinding.
- `STD-visual-details-34` (should): Name navigation items for their contents.
- `STD-visual-details-36` (must): Same look, same behaviour.
- `STD-mobile-touch-09` (must): Touch targets 44pt on iOS, 48dp on Android.

**Motion**
- `STD-when-to-animate-05` (must): No motion on 100+ times-a-day actions.
- `STD-when-to-animate-06` (must): Never animate keyboard-initiated actions.
- `STD-when-to-animate-07` (must): Remove or shrink motion seen tens-of-times daily.
- `STD-when-to-animate-14` (must): Tab switches never slide.
- `STD-springs-gestures-05` (must): Bounce only after a momentum gesture.
- `STD-mobile-touch-42` (must): Screen transitions stay on the native stack.
- `STD-mobile-touch-44` (must): Back swipe mirrors custom transitions.
- `STD-enter-exit-origin-25` (must): React Native: never animate header height.

**Tabs**
- `STD-enter-exit-origin-42` (should): Tab color changes: clip a duplicate.
- `STD-accessibility-motion-16` (must): Build overlays on accessible primitives. (tabs included)
- `STD-accessibility-motion-17` (should): Hide decorative duplicate layers.
- `STD-mobile-touch-41` (must): Use native pieces instead of JS rebuilds. (NativeTabs for the tab bar)

**Bars and materials**
- `STD-visual-details-15` (should): Scroll-edge effects, not hard dividers.
- `STD-visual-details-16` (should): Translucent bars and sheets.
- `STD-visual-details-17` (should): Material weight encodes hierarchy.
- `STD-mobile-touch-16` (must): Paint edge to edge, pad the safe areas.

## What the sources teach

### The sidebar is the spine of a product

- Put persistent, global things in the sidebar: navigation, profile management and search (the last two may live in the top bar instead). Kole Jain puts profile management at the top with a picture and arrows that show it opens; gives every link a recognizable icon and a short title (which also makes a collapsed sidebar and badges work); groups links by relevance; moves settings and help to the bottom; nests links into dropdowns as they grow; and insists on a visible active state such as a rectangle indicator [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- The same video: when a link opens a new page, that page needs a back button or breadcrumb; tabs add closely related views without adding sidebar items; and the sidebar's empty space can hold notifications, as Dub and Linear do [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- A good sidebar is mostly text, dividers and icons, and the icons are where to invest. Hover highlights are rectangles that fade in behind each item, and a small options menu slides up a couple of pixels as it fades in [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- Keep sidebar items to labels, without stats such as click counts. Replace a gradient letter avatar with an account card whose links open in a popover, left-align the items and tighten the spacing [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- When a big header pushes the important content below the fold, move its essentials into a collapsible sidebar: logo at the very top, then the menu, the team with a manage button and an add-widget button, and settings at the bottom [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Cleaning up an AI-made sidebar: the person's name and icon with an arrow to switch accounts, items lined up, section labels such as "Menu" removed, settings and help moved to the bottom [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Sidebar links are ghost buttons, and highlighting the active item is a signifier that tells people what the UI does [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Apple's utility apps put global actions in the top bar, navigation in a sidebar and content in the middle; an app whose only navigation is browsing and search can drop the sidebar and give the space to content [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]). Sidebars can use darker, heavier materials to separate structure [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Phones: bottom bars and thumb reach

- Replace the desktop sidebar with a bottom bar of three or four links, five at the very most, which also keeps every target over 44px. Bottom bars often float, with the main action set apart. If too many sections matter, turn the sidebar into the home page, as Notion does. Top-bar actions change with context, and focused views such as a note editor can hide the bar altogether [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- TikTok keeps its bottom bar and a column of action icons on the right within a right-handed thumb's reach; Kole Jain cites 70-80% of people as right-handed [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]). Important controls belong at the bottom of a phone screen, though on the mobile web the browser bar can get in the way [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- A tab bar upgrade: do not raise the create button above the bar in a circle, since it is the tab people use least; keep inactive icons clearly visible; give every tab an active state (a profile picture works for the profile tab); use brand color on active states for a pop; spread icons apart to enlarge click areas; add labels when icons are obscure, and make them dark enough to read [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- In React Native, use NativeTabs, which keep the platform's own tab behavior, and give Expo Router tabs `animation: 'none'`: tabs are peers, and sliding between them suggests a depth that is not there [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]). A tab indicator pill is measured once and slides over 250ms with ease-in-out, and the haptic fires when the tab is pressed [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Screen changes stay on the native stack: the platform push for going deeper, `modal` for a self-contained task, `formSheet` for a short interruption, and `fade` when reduced motion is on. A collapsing header never animates its height [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).

### Websites: top bars, menus and mega menus

- Keep navigation at the top and let information flow top to bottom and left to right; when links run out of room, collapse them into a menu that animates in, so the motion has a purpose [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- Give the nav bar hierarchy and balance instead of a flat, right-heavy row: outline the most important buttons, center the secondary links, and add hover dropdowns or a mega menu for the key links. A mega menu should stay open and slide its content sideways when moving between items rather than closing and reopening [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Menus with pictures give context at a glance: Rivian shows each vehicle so the R1T reads as a truck and the R1S as an SUV [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]), most SaaS sites use a giant image dropdown like Intercom's, and a small image menu like Pipe's suits small sites [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]). Kole Jain says images in the nav should be normal [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- For a single-product site he puts the logo at the top and collapses the links into a hamburger [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]); for a shop he puts the logo front and center, folds favorites and notifications into a menu button, shows the cart as an icon and turns the profile link into "sign in" [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- Most modern navs are small and stay out of the way [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]). Steve Schoger left-aligns the links next to the logo, because three separately placed groups felt busy, and gives the nav's button a smaller size than the hero's [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Simple site structures work best for portfolios: two or three pages at most, or one page with links to its sections [S-L19-064] ([[sources/ToJiXPTNnLY-professional-portfolio-breakdown-why-is-theirs-so-much-better|Professional Portfolio Breakdown — Why Is Theirs So Much Better?]]). For a shop with hundreds of products that customers struggled to navigate, the real fix was better search and new categories [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- A navbar can grow from a dot into a pill as a load animation, then fade its items in one by one; the Figma prototype and the GSAP build give exact timings [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]) [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).

### Tabs and active states

- To animate an active tab whose background and text color change, duplicate the tab list, style the copy as active, clip it to the active tab, and animate the clip. The copy is hidden from screen readers and keyboard focus, and real tabs should sit on an accessible primitive such as Radix Tabs [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]). The recipe animates the clip over 250ms with ease-in-out [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]), and the animations.dev course teaches the same tabs [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).
- Tabs suit account areas that will keep growing, such as billing and usage [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). Design the content of every tab before handing it off, or the developer receives half a site [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- Thin chips can work as breadcrumb navigation [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).

### Wayfinding and labels

- Every screen should answer: where am I, where can I go, what is here, and how do I get out. Name navigation items for what they hold ("Progress", "Library"), not with a vague umbrella such as "Home" [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Instead of a 1px border under a sticky header, fade a small blur or gradient where content meets the floating bar, and build bars as translucent layers [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Motion: mostly none

- Never animate what people see more than 100 times a day, such as core navigation, keyboard shortcuts and the command palette; anything started from the keyboard never animates [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- Test a menu's animation by opening and closing it rapidly, and judge the hover on a frequently used list by running the pointer through the whole list [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). The animations.dev navigation-menu walkthrough treats easing and duration as part of building the component [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).
- Between pages, Kole Jain carries an element across (an image that zooms into the next page's hero, a card that expands to full screen) rather than sliding a new page in, and keeps a button for anyone who does not know the swipe [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- Mac apps choose between a command palette (Notion, Obsidian, Attio) and a floating search bar with a slide-out preview for one-screen apps [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).

## Where they agree and disagree

- **Bottom bar size.** Kole Jain's three to five links [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]) matches DC-L08-19 and DC-L03-19 (three to five destinations on compact screens), and his 44px targets match `STD-mobile-touch-09`.
- **Hidden navigation.** Kole Jain collapses links into a hamburger or an animated menu when room runs out [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]) [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]). DC-L13-02 says to keep primary navigation visible whenever the width allows, citing an NN/g study where hidden navigation was used far less (44% against 89%).
- **A raised main action.** Kole Jain disagrees with himself: one video floats the bottom bar with the main action set apart [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]), another says the create button should not be raised [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). The deciding factor may be how often the action is used: the note app's main action is its core job, while Instagram's create tab is the least used [inferred].
- **Page transitions.** Kole Jain prefers shared-element zooms to a page sliding in [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]). The house standards keep native apps on the platform's own stack transitions (`STD-mobile-touch-42`), so his approach only has room on the web and in custom in-page moments [inferred].
- **Brand color on active items.** Kole Jain suggests brand color on active states [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). DC-L08-14 lists a neutral, non-brand selected state as an option, reserves brand primary for actions in action-dense products [inferred there], and requires an indicator, never color alone.
- **Menu entrances.** Kole Jain's menu fades in while moving up a couple of pixels [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]); the house recipe scales menus from their trigger (`STD-enter-exit-origin-08`). Both avoid a plain fade (`STD-enter-exit-origin-02`) [inferred].
- **Hover highlights.** Kole Jain animates sidebar hover highlights [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]), while `STD-when-to-animate-07` keeps hover on things used tens of times a day near-imperceptible.
- **Counts in the sidebar.** Notification counts and "new" chips are welcome [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]), but stats that do not help navigation should go [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). The difference seems to be whether the number calls for action [inferred].
- **Tab labels.** Labels for obscure icons [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]) fit Q-icon-05's default of labels, and DC-L13-18's advice to pair key actions with text.

## Decisions this informs

- **Q-layout-04** (how many sections, and where the menu sits): a sidebar on desktop, a bottom bar of three to five on phones, and the question of hiding links on websites.
- **Q-state-05** (how the picked tab or item shows): a rectangle or pill indicator, a clip-path tab, and whether brand color is used.
- **Q-icon-05** (when icons get words): label obscure tab icons, and make labels dark enough.
- **Q-motion-06** (screen changes): native stack transitions on mobile; shared-element moments are practitioner opinion. The house standards rule out the `fade` option (`STD-enter-exit-origin-02`) and the `fade-through` option (`STD-when-to-animate-05`, `STD-when-to-animate-14`).
- **Q-motion-09** (system or brand motion): navigation follows the platform; `STD-mobile-touch-42` rules out the `one-language` option.
- **Q-motion-07** (reduced motion): stack transitions switch to a fade.
- **Q-depth-04** (glass or solid bars): translucent bars with scroll-edge effects; `STD-visual-details-16` rules out the `none` and `transient` options on the web.
- **Q-pattern-03** (show everything or tuck extras away): menus that open on demand when links run out of room.
- **Q-space-03** (tap target size): bottom-bar items over 44px.

## Visual examples worth showing

- Kole Jain's dashboard sidebar: profile at the top, grouped icon links, settings at the bottom, a rectangle active state and a collapsed version [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- The collapsible finance-dashboard sidebar [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- The Instagram-style tab bar before and after [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- A floating bottom bar, and Notion's sidebar turned into a home page [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- TikTok's thumb-zone layout [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).
- Clip-path tabs (Payments, Balances, Customers, Billing) with the clip toggled off to show the duplicate [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- A mega menu that slides between items next to one that closes and reopens [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Rivian's image menu, and Intercom's large versus Pipe's small image dropdowns [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]) [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- The pill navbar growing from a dot [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).

## Open questions

- Should marketing sites ever hide their main links behind a hamburger when there is room, given DC-L13-02's evidence?
- Should active states use the brand color or a neutral one by default?
- What are the collapsed sidebar's width and behavior? The sources show collapsed variants but give no values.
- How much hover motion may sidebar items have, given they are used many times a day?
- Should web products use shared-element page transitions, and if so on which surfaces?
