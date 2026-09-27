---
type: source
title: "Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)"
created: 2026-09-27
updated: 2026-09-27
video_id: Gfsd8NNuD9g
url: https://www.youtube.com/watch?v=Gfsd8NNuD9g
channel: Kole Jain
published: 2026-04-18T18:18:34Z
authority: reference
tags:
  - mobile
  - navigation
  - bottom-bar
  - bottom-sheet
  - touch-targets
  - type-scale
  - cards
  - gestures
  - long-press
  - contextual-actions
  - empty-states
  - desktop-to-mobile
---

# Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)

## Metadata

- Video ID: `Gfsd8NNuD9g`
- Channel: Kole Jain
- Published: 2026-04-18T18:18:34Z
- URL: https://www.youtube.com/watch?v=Gfsd8NNuD9g

## Summary

Kole Jain walks through designing a first mobile app UI from a desktop starting point, using a notes app as the running example. He covers the two main mobile navigation choices (a bottom bar with a few icons, or turning the sidebar into a home page like Notion), and explains that type and spacing stay about the same size as desktop or get larger, citing a 17 pixel iOS base font against 13 pixels on macOS. He gives layout guidelines for small screens: one direction of content per section, cards as the main building block, no double-nested cards, and one screen doing one thing, with bottom sheets for tasks that must keep the user in context. He then covers gestures (swipe back, bottom sheet zoom, swipe up to search, long press), contextual actions that come and go, and two kinds of empty state. For a design system, this gives concrete mobile defaults for navigation limits, touch targets, type size, card nesting, sheets, transitions and empty states.

## Key Ideas

- Mobile navigation has two main options: a bottom bar with a few key icons, or turning the desktop sidebar into a whole home page.
- A bottom bar should hold at most five links, ideally three or four, which keeps every target above 44 pixels.
- Top bar and bottom bar actions are contextual and change with the page.
- Squishing a desktop design onto a phone makes it too small; mobile type and spacing stay similar to desktop or get larger.
- On mobile you usually get to show one of the many things a desktop dashboard shows at once.
- Desktop layouts can extend in two directions at once; on mobile each section moves in one direction, vertical stack or horizontal scroll.
- Apart from floating menus and actions, an app is built from four building blocks: cards, text or links, images, and inputs.
- Cards group content in place of white space, which mobile screens lack, but nesting cards inside cards creates padding on padding.
- One screen does one thing (the home screen is the exception); something new gets a new page, not a new layout.
- Bottom sheets let a user do a side task, such as picking a template, without leaving the current context.
- Gestures like swipe back and swipe down on sheets feel smooth when the background moves or zooms along with the foreground.
- Long press is the mobile right click: blur the rest of the screen, show actions, and slightly zoom the element.
- Because space is limited, actions appear and hide as needed, for example the nav bar hiding while editing a note.
- Design the empty states too: a first-use state that points at the main action, and a no-results state with help and a way out.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Designer and YouTube creator presenting the mobile UI walkthrough.
- [[entities/mobbin|Mobbin]] (product): The video's sponsor; mentioned only in the sponsor segment (see caveats), not in the design guidance.
- [[entities/notion|Notion]] (product): Example of turning the sidebar into a home page with a big search bar or action button at the bottom.
- [[entities/slack|Slack]] (product): Example of a swipe up to search gesture.
- [[entities/ios|iOS]] (product): Cited for its 17 pixel base font size and its dynamic long-press preview.
- [[entities/macos|macOS]] (product): Cited for its 13 pixel base font size, smaller than iOS.
- [[entities/figma|Figma]] (tool): The creator shares the Figma files used in the video.
- [[entities/bottom-sheet|Bottom sheet]] (concept): A panel that rises from the bottom to hold a side task while keeping the user in context.
- [[entities/bottom-bar|Bottom bar]] (concept): Mobile navigation bar, typically floating, with the important action broken out.
- [[entities/empty-state|Empty state]] (concept): What the user sees when there is no content yet or a search returns nothing.

## Topics

- [[topics/mobile-app-patterns|Mobile app patterns]]: The whole video: how mobile differs from desktop in navigation, sizing, layout direction, building blocks, sheets, gestures and contextual actions.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Replace the desktop sidebar with a floating bottom bar of three or four links (five at most), or turn the sidebar into a home page as Notion does; top-bar actions are contextual.
- [[topics/typography|Typography]]: Mobile type does not shrink with the screen; iOS has a 17 pixel base font while macOS has 13 pixels.
- [[topics/spacing-and-layout|Spacing and layout]]: Spacing stays similar to desktop; each mobile section lays out in one direction only; group with white space instead of nesting containers.
- [[topics/cards-and-sections|Cards and sections]]: Cards are the main mobile building block because they group content without needing white space; avoid double-nesting them to prevent padding on padding.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: A desktop dashboard that shows many panels at once must be reduced to one thing on mobile, with each section extending in a single direction.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Bottom sheets keep the user in context for side tasks such as template selection; they can be any height, carry a title, search, check and X, and zoom the background out as they open.
- [[topics/gestures-and-drag|Gestures and drag]]: Swipe right to go back with the background shifting about 35%, swipe down to close sheets, swipe up to search, and long press as the mobile right click; teach users the swipes before relying on them.
- [[topics/buttons-and-actions|Buttons and actions]]: Actions are contextual: the nav bar hides in the note editor to reveal formatting and sharing, and template selection shows only a confirm button and an X; the plus button opens a menu or an input.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Two empty states: first use, which highlights the main plus action with a full-screen state and an instructional popover; and no search results, which needs imagery, an acknowledgement, suggestions and an exit action.
- [[topics/onboarding|Onboarding]]: On first login, a full-screen empty state and a simple popover explain how the app works instead of cards inviting the user to add content.

## Notable Claims

- Five links in a bottom bar is pretty much the limit, and three or four is much more ideal. Evidence: Five links down here is pretty much the definite limit
- Keeping the bottom bar to a few links maintains targets over 44 pixels, because people have fat fingers. Evidence: maintain over a 44-pixel target
- Apps like Notion turn the sidebar into a home page, which frees the bottom of the screen for a big search bar or action button. Evidence: which is what apps like Notion do
- Despite the smaller screen, type scale and spacing on mobile stay similar to desktop and can get a bit larger. Evidence: the type scale and spacing remains relatively similar to desktop
- iOS has a base font size of 17 pixels, while macOS has a base of only 13 pixels. Evidence: iOS actually has a base font size of 17 pixels
- Desktop dashboards can lay out content in two directions at the same time; on mobile you choose one direction per section. Evidence: you can choose one direction to move in per section
- Ignoring floating menus and actions, an app has only four building blocks: cards, text or links, images and inputs. Evidence: only four types of building blocks for an app
- Cards let you flexibly group content in place of white space, which mobile screens do not have much of. Evidence: flexibly group content in place of white space
- Double-nesting cards creates padding on padding, which restricts space and cramps things. Evidence: it creates padding on padding
- Bottom sheets keep the user in context and are easy to navigate with gestures. Evidence: they keep the user in context
- Moving the background left by about 35% and animating it right during swipe back gives a super smooth transition. Evidence: move the background left by about 35%
- Swipes can be relied on heavily as long as the user is educated on how to use them. Evidence: as long as you educate the user on how to use them
- Slack uses a swipe up to search gesture, and Apple sort of does too. Evidence: which is used by Slack as well as sort of by Apple
- Long press is the mobile equivalent of the right click. Evidence: the mobile equivalent of the right click

## Quotes

> one screen does one thing, and that's it
> don't reach for a different layout, reach for a different page altogether
> the long press, the mobile equivalent of the right click

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Mobbin (with a 20% discount link) in the middle of the video; it is not a design rule.
- Caveat: The description links to the creator's own Figma files on kolejain.com (self-promotion).
- Caveat: Beginner-level overview built around one example notes app; the rules are the creator's guidelines, not platform specifications.
- Caveat: The source gives the iOS and macOS base font sizes and the target size in pixels; platform guidelines may state these in points [inferred].
- Caveat: Auto-generated captions; no mis-hearings that change meaning were found. Published 2026-04-18.

### Rules and practices

- **should** (components, all): Keep a mobile bottom navigation bar to three or four links, and never more than five. Why: Five is pretty much the limit and three or four is ideal; it keeps every target over 44 pixels for fat fingers. Values: Five links, three or four. [Five links down here is pretty much the definite limit]
- **should** (accessibility, all): Keep mobile tap targets, such as bottom-bar links, over 44 pixels. Why: People do have fat fingers; the source gives this as the result of keeping the bottom bar to five links or fewer. Values: 44-pixel. [maintain over a 44-pixel target]
- **consider** (components, all): Make the mobile bottom bar floating, with the most important action broken out from the other links. Why: The source describes this as how bottom bars typically look nowadays. [typically floating with the important action broken out]
- **consider** (patterns, all): When the sidebar has too many important items for a bottom bar, turn the sidebar into a home page and use the freed bottom area for a big search bar or action button. Why: It is another valid form of navigation, as Notion does, and it clears up the bottom of the screen. [turn that into a whole page that sort of becomes the home page]
- **consider** (layout, all): On a sidebar-as-home-page layout, put recent items at the top and actions and counts on the right side. Why: So it does not feel so lopsided. [actions and counts to the right side, so it doesn't feel so lopsided]
- **consider** (patterns, all): Make top-bar and bottom-bar actions contextual to the page, starting from a bell and a more menu at the top. Why: These actions can and do change depending on the context the user is in. [a bell and more menu is a good place to start]
- **should** (typography, all): Do not shrink type and spacing when moving a design to mobile; keep them similar to desktop or slightly larger. Why: Squished designs look wrong next to normal-sized apps; iOS has a 17 pixel base font while macOS has 13 pixels, so things often get larger on smaller screens. Values: 17 pixels, 13 pixels. [the type scale and spacing remains relatively similar to desktop]
- **should** (layout, all): Lay out each mobile section in one direction only: stack items vertically or scroll them horizontally off the page, not both. Why: Desktop layouts can extend in two directions at once, but on mobile you can choose one direction per section; this makes converting dashboards to mobile easier. [you can choose one direction to move in per section]
- **should** (components, all): Use cards as the main way to group content on mobile screens. Why: Cards flexibly group content in place of white space, which mobile screens do not have much of. [flexibly group content in place of white space]
- **should** (components, all): Avoid nesting a card inside another card; group the inner content with white space instead of a container. Why: Double-nesting creates padding on padding, which restricts space and cramps things. [try and avoid double-nesting them]
- **should** (patterns, all): Give each mobile screen one job, except the home screen; when you need to add something new, add a new page rather than a new layout on the same screen. Why: Mobile is space-constrained, so extras like recent notes or suggested templates become clutter. [one screen does one thing]
- **should** (components, all): Use a bottom sheet for a side task that should not pull the user away from the current screen, such as picking a template while editing a note. Why: Bottom sheets keep the user in context, can be any height, and are easy to navigate with gestures. [This is where bottom sheets become super useful]
- **consider** (components, all): Give a selection bottom sheet a title, a search bar, a check to confirm and an X to close. Why: This is the structure the source builds for the template picker sheet. [add in a title, search bar, and a check and X]
- **should** (motion, all): In a swipe-right-to-go-back transition, move the background left by about 35% and animate it right as the page is swiped away. Why: It produces a super smooth transition. Values: 35%. [move the background left by about 35%]
- **consider** (motion, all): Zoom the background out as a bottom sheet comes up, and zoom it back in when the sheet is swiped down. Why: The source presents this as the same smooth-transition idea as swipe back. [we often zoom out the background and zoom back in on swipe down]
- **should** (patterns, all): Teach users a swipe gesture before relying on it heavily. Why: Swipes are everywhere in modern apps and can be relied on as long as users are educated on how to use them. [as long as you educate the user on how to use them]
- **consider** (patterns, all): On long press, blur the rest of the screen, show the element's actions, and slightly zoom the element itself. Why: Long press is the mobile equivalent of the right click, and the source calls this the typical treatment; a dynamic preview like iOS is the step further. [It's typical to blur the rest of the screen]
- **should** (patterns, all): Show actions only when they are needed: hide the nav bar in focused views and reveal the actions specific to that task. Why: Space is limited, so actions cannot always be persistent; for example, the note editor swaps the nav bar for formatting and sharing actions. [actions need to come and go as needed]
- **should** (patterns, all): Design the first-use empty state: draw attention to the main action with a full-screen empty state and a simple popover explaining how things work. Why: The ideal full-content state is not what users see the first time they log in, and focusing on the main action simplifies things. [add in a full-screen empty state to simplify things]
- **should** (content, all): For a no-results empty state, show imagery, say that nothing matches the keywords, offer suggestions in case of a typo, and give an action to exit the empty state. Why: An instruction alone is not enough for this second type of empty state. [acknowledge that there are no notes matching the existing keywords]
- **should** (layout, all): When moving a desktop dashboard to mobile, pick one of its panels for the screen instead of fitting them all in. Why: Type and spacing do not shrink on the smaller screen, so where desktop showed an action bar, recent notes, a calendar, tasks and a scratch pad, mobile has room for one of those things. [now you can pick one of those things]
- **consider** (process, all): Check a mobile design by zooming out and comparing it side by side with normal-sized apps. Why: A squished design looks fairly normal on its own until it is compared with normal-sized apps. [show you the other normal-sized apps for comparison]
- **consider** (patterns, all): Consider a swipe up gesture to open search. Why: Swipes can be relied on heavily once users are taught them; Slack uses swipe up to search, and Apple sort of does too. [a handy swipe up to search]
- **consider** (motion, all): Animate contextual actions in and out as they appear and hide. Why: The source says how these actions animate in and out is half the fun. [how these actions animate in and out is half the fun]

### Decisions it informs

- How should the app's main navigation work on a phone? (`Q-layout-04`)
  - Bottom bar: A few key icons at the bottom, nowadays typically floating with the important action broken out; targets stay over 44 pixels. When: When the sidebar links can be consolidated to a few key icons (three or four ideal, five at most).
  - Sidebar becomes the home page: The home page lists the sections, with recent items at the top and actions and counts on the right; the bottom is free for a big search bar or action button, as in Notion. When: When there are too many important items in the sidebar to fit in a bottom bar.
  - Recommendation: The bottom bar is the typical standard; use the home-page approach when there are too many important sections to fit.
- How big should text and spacing be on mobile compared with desktop? (`Q-type-08`)
  - Squish things down to fit more: Looks normal on its own but noticeably smaller than normal-sized apps when compared side by side. When: The source does not recommend it.
  - Keep desktop sizes or go a bit larger: Matches real apps; iOS uses a 17 pixel base font while macOS uses 13 pixels. When: Default for mobile designs.
  - Recommendation: Keep type scale and spacing similar to desktop or slightly larger, because more often than not things get larger on smaller screens.
- Which direction should a mobile section lay out its items?
  - Vertical stack: Each item stacks down the page. When: When the section is the main content of the screen [inferred].
  - Horizontal scroll off the page: Items continue sideways past the screen edge. When: When the section sits among other sections and should stay compact [inferred].
  - Recommendation: Pick one direction per section; you can't have both like you reasonably could on desktop.
- How should related content be grouped on a mobile screen? (`Q-dir-04`)
  - Cards: Content is grouped in containers, which works without much white space. When: The main grouping tool on mobile.
  - White space: Content is grouped by spacing alone, with no extra padding from a container. When: Inside a card, to avoid a card within a card.
  - Recommendation: Use cards as the main building block but avoid double-nesting them; group with white space inside a card.
- Should a side task open on a new page or in a bottom sheet? (`Q-pattern-01`)
  - New page: The side task gets its own screen, keeping each screen to one job. When: When you need to add something new that does not depend on the current context.
  - Bottom sheet: A panel of any height rises over the current screen, keeping the user in context and closing with a gesture. When: When the user should not be ripped away from what they are doing, such as picking a template while editing a note.
  - Recommendation: Default to a new page rather than a new layout, but use a bottom sheet when the task must keep the user in context.
- What should the main plus button do when tapped?
  - Open a small menu: A little menu of things to create appears. When: When there are several kinds of item to add [inferred].
  - Open an input: The user can immediately start typing. When: When the main action is quick capture [inferred].
- What should a long press show?
  - Blurred screen with an action list: The rest of the screen blurs, the actions appear, and the element zooms slightly. When: The typical treatment.
  - Dynamic preview: The pressed element expands into a richer preview, like iOS. When: When you want to take it a step further.
- What should a new user see on first login when there is no content? (`Q-pattern-04`)
  - Cards inviting the user to add content: Several cards prompt the user to start adding events, tasks and notes. When: The source considers and passes over this option.
  - Full-screen empty state focused on the main action: Attention goes to the plus button, with a simple popover explaining how things work. When: The source's choice, to simplify things.
  - Recommendation: Draw attention to the plus button with a full-screen empty state and an instructional popover.

### Process

1. Choose the navigation: Consolidate the desktop sidebar into a bottom bar of three or four icons (five at most), or turn the sidebar into the home page if too many items are important.
2. Set contextual top actions: Start with a bell and a more menu at the top, then change them per page.
3. Check sizes against real apps: Zoom out and compare the design with normal-sized apps; keep type and spacing similar to desktop or larger.
4. Pick one thing per screen: From the many desktop panels, choose one per screen; convert each dashboard section to a single direction, vertical or horizontal.
5. Build from four blocks: Compose screens from cards, text or links, images and inputs, avoiding cards inside cards.
6. Keep side tasks in context: Use a new page for new things, and a bottom sheet for tasks that must not pull the user away.
7. Add gestures and transitions: Add swipe back with the background shifting about 35%, sheet background zoom, swipe up to search and long-press actions; teach users the swipes.
8. Make actions come and go: Hide the nav bar in focused views and show only the actions that view needs, animating them in and out.
9. Design the empty states: Design the first-use state and the no-results state after the ideal full-content state.

### Examples and visual references

- Floating bottom navigation bar with the important action broken out: A bottom bar of a few icons floating above the content, with the main action separated from the links; shows the typical modern bottom bar.
- Sidebar turned into a home page (Notion (the pattern's reference)): Home page listing the sidebar sections, with recent notes at the top, actions and counts on the right, and a big search bar or action button at the bottom.
- Squished mobile design next to normal apps: Zooming out shows a design that looked fine is much smaller than real apps; demonstrates that mobile type and spacing should not shrink.
- Desktop dashboard reduced to one element: A desktop screen with an action bar, recent notes gallery, full calendar, tasks and scratch pad; on mobile only one of these fits per screen.
- Two-direction versus one-direction layout: A desktop layout of two columns and three rows next to a mobile section that either stacks notes vertically or scrolls them horizontally off the page.
- Double-nested cards: A card inside a card showing padding on padding that cramps the content; fixed by grouping with white space.
- Template picker bottom sheet: A sheet over the note editor with a title, search bar, check and X, and the list of templates; shows a side task kept in context.
- Swipe back transition: The previous page starts about 35% to the left and moves right as the current page is swiped away.
- Bottom sheet background zoom: The background zooms out as the sheet rises and zooms back in when the sheet is swiped down.
- Swipe up to search (Slack (and sort of Apple)): Swiping up opens search, an example of relying on a learned gesture.
- Long-press menu and dynamic preview (iOS (dynamic preview)): The rest of the screen blurs, actions appear and the element zooms slightly; the iOS variant shows a richer preview.
- Note editor with contextual actions: Opening a note hides the nav bar and shows text formatting and sharing at the top; the template sheet shows only a confirm button and an X.
- First-use empty state: A full-screen empty state that draws attention to the plus button, plus a simple popover explaining how the app works.
- No-results search empty state: Imagery, a message that no notes match the keywords, suggestions in case of a typo, and an action to exit the empty state.

### Numbers

- Five: Maximum number of links in a bottom navigation bar. [Five links down here is pretty much the definite limit]
- three or four: Ideal number of links in a bottom navigation bar. [three or four is much more ideal]
- 44-pixel: Minimum tap target size to maintain on mobile. [maintain over a 44-pixel target]
- 17 pixels: iOS base font size. [iOS actually has a base font size of 17 pixels]
- 13 pixels: macOS base font size. [macOS has a base of only 13 pixels]
- 35%: How far left the background starts in the swipe-back transition. [move the background left by about 35%]
- four: Types of building blocks in an app: cards, text or links, images, inputs. [only four types of building blocks for an app]
- two columns and three rows: Example desktop dashboard layout that extends in two directions at once, unlike a mobile section. [this layout has two columns and three rows]

<!-- /od:learn -->
