---
type: source
title: Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)
created: 2026-09-27
updated: 2026-09-27
video_id: Vy0KKvZJRH8
url: https://www.youtube.com/watch?v=Vy0KKvZJRH8
channel: Kole Jain
published: 2025-12-02T13:55:31Z
authority: reference
tags:
  - macos
  - desktop-app
  - apple
  - native-feel
  - dark-mode
  - empty-state
  - progressive-disclosure
  - optimistic-ui
  - keyboard-shortcuts
  - drag-and-drop
  - search
  - onboarding
---

# Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)

## Metadata

- Video ID: `Vy0KKvZJRH8`
- Channel: Kole Jain
- Published: 2025-12-02T13:55:31Z
- URL: https://www.youtube.com/watch?v=Vy0KKvZJRH8

## Summary

Kole Jain walks through designing a macOS app so it feels native, using a design-inspiration saving app as the worked example. He starts outside the main window: the app should be a system that appears where you need it (a shortcut-triggered quick-save window, popovers, toasts) and then gets out of the way, rather than a destination. For the main window he follows Apple's utility-app layout (top bar for global actions, sidebar for navigation, content in the centre), keeps the top of the window clear for dragging, drops the sidebar when navigation is simple, and uses empty states and progressive disclosure so the content can shine. He then covers designing light and dark mode separately instead of inverting, a floating search bar, visible feedback for every keyboard shortcut, drag and drop in and out of the app, a floating action bar, and onboarding that teaches shortcuts. For a design system this gives desktop-specific layout conventions, a dark-mode stance and a set of interaction patterns for utility apps.

## Key Ideas

- A native-feeling Mac app is a system that shows up exactly where you need it, not a destination you have to visit.
- To design like Apple, first get comfortable with the UI that lives outside the main window (popovers, new windows, notifications, shortcut-triggered panels).
- Think about how the user actually works (hopping between Figma, code and Notion) and give them a keyboard shortcut to act without switching context.
- An app holds the user's own content that they add and change, so it is more user-focused than a landing page, even when the components look similar.
- Apple's utility apps share one layout: global actions on top, navigation in a sidebar, content in the centre, with the traffic lights treated like any other element.
- The top of a Mac window is used for dragging the window, so keep it uncluttered.
- Skip the sidebar when navigation is just browsing and searching, so the UI becomes a container for the user's content.
- Use empty states and progressive disclosure: show only what the user needs in that moment and hide filters until there is content to filter.
- Before adding colors or effects, find the minimum UI that lets the content shine.
- Light and dark mode are not exact opposites; they should feel different but consistent.
- Search should be prominent and accessible; a floating search bar with a slide-out preview keeps a one-screen app on one screen.
- Every keyboard shortcut needs visible feedback, a micro-animation or at least a state change, or users assume something went wrong.
- Drag and drop should work both into the app and out of it to other apps.
- Optimistic UI means processing a save in the background while assuming it will succeed, as Apple Mail does when moving email to trash.
- Even desktop apps benefit from onboarding, especially to teach keyboard shortcuts, which are powerful but easy to forget.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Presenter of the video, who designs and builds the example design-inspiration app.
- [[entities/apple|Apple]] (company): Held up as the model for native macOS app design and interaction.
- [[entities/notion|Notion]] (product): Example of a third-party app that pops up when it detects a meeting, and of a command palette.
- [[entities/paste|Paste]] (product): Example of an app that integrates at the bottom of the screen and uses a native blur.
- [[entities/spotlight|Spotlight]] (product): macOS search opened with Command Space and draggable anywhere; the pattern the quick-save window follows.
- [[entities/raycast|Raycast]] (product): Example of appearing when needed and getting out of the way, and of a very good onboarding process.
- [[entities/apple-mail|Apple Mail]] (product): Example of optimistic UI: moves an email to trash before it is deleted from the server.
- [[entities/obsidian|Obsidian]] (product): Named as having a command palette or universal search.
- [[entities/attio|Attio]] (product): Named as having a command palette (caption reads 'atio') [inferred].
- [[entities/google|Google]] (company): Has a keyboard-shortcut cheat sheet that is itself opened with a shortcut.
- [[entities/traffic-lights|Traffic lights]] (concept): The macOS window buttons, which Apple apps integrate into the top bar or sidebar like any other element.
- [[entities/optimistic-ui|Optimistic UI]] (concept): Showing an action as done immediately while it is processed in the background, assuming it will succeed.
- [[entities/progressive-disclosure|Progressive disclosure]] (concept): Only showing the user what they need to see in that moment.
- [[entities/command-palette|Command palette]] (concept): Universal search considered for the app but rejected because its items usually take you to a new screen.

## Topics

- [[topics/desktop-and-macos-apps|Desktop and macOS apps]]: The whole video: native macOS patterns such as shortcut-triggered windows, the top-bar/sidebar/content layout, the window drag area, traffic lights, search, drag and drop and the share button.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Apple utility apps put navigation in a sidebar; the example app skips it because navigation is only browsing and searching, which frees room for large images.
- [[topics/spacing-and-layout|Spacing and layout]]: Top for global actions, sidebar for navigation, content in the centre; keep roughly the top 50 pixels clear because it is used to drag the window.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Respect the system light/dark setting; do not directly invert colors, because dark mode needs more separation between colors than light mode. Light and dark should feel different but consistent.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: A simple empty state invites the first action; optimistic UI shows a save as done straight away; every shortcut needs a visible state change.
- [[topics/micro-interactions|Micro-interactions]]: The quick-save panel slides in on Command Shift S, slides away on Escape and turns into a toast on Enter; the collapsed search bar expands when clicked or triggered.
- [[topics/toasts-and-notifications|Toasts and notifications]]: After saving, the quick-save window collapses into a toast notification and slides off the screen.
- [[topics/gestures-and-drag|Gestures and drag]]: Drag and drop of anything anywhere is a must: drop content into the quick-save window and drag content out to Figma, Finder or elsewhere.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers and new windows are part of feeling native; onboarding is a modal, and a settings popover holds the shortcut cheat sheet, panel side and light/dark setting.
- [[topics/buttons-and-actions|Buttons and actions]]: Buttons in the quick-save window show keyboard shortcut reminders; a floating action bar in the preview gives copy, find and delete; Apple's universal share button is common.
- [[topics/onboarding|Onboarding]]: Desktop apps should not skip onboarding; the example uses a simple modal with micro-interactions that closes when the user performs the shortcut, and a shortcut cheat sheet.
- [[topics/design-process|Design process]]: Start with how the user will actually interact and the UI outside the main window, then the main window, and ask what minimum UI lets the content shine before adding color or effects.

## Notable Claims

- Third-party apps can feel native by living outside the main window, like Notion's meeting pop-up or Paste integrating at the bottom of the screen. Evidence: Even third party apps like Notion have pop-ups as soon as it detects a meeting
- Spotlight is hard to reach other than with Command Space and can be dragged anywhere. Evidence: Spotlight search isn't very accessible with anything other than command space
- Apple Mail moves an email to trash before it is actually deleted from the server, an example of optimistic UI. Evidence: Apple Mail and many other applications follow this pattern
- A landing page is pre-generated content that doesn't really change, while an app holds user information that is added and manipulated, so apps are more user-focused. Evidence: The Notes app and the iPhone landing page might have similar UI components
- Finder, Notes, Reminders, Calendar and Settings share a layout: top for global actions, sidebar for navigation, main content in the centre. Evidence: the top for global level actions, the sidebar for navigation
- Apple apps integrate the traffic light buttons into the top bar or sidebar, treating them like any other element. Evidence: seamlessly integrate the traffic light actions into the UI
- Roughly the top 50 pixels of Apple's apps allow window dragging. Evidence: the top roughly 50 pixels of their apps allow window dragging
- Dark mode needs colors that are more different from each other than light mode, because there is less light and less differentiation. Evidence: dark mode requires colors that are more different from each other than light mode
- Directly inverting the colors into light mode makes the contrast much higher and doesn't look stellar; collapsing the colors to be more similar looks a lot more refined. Evidence: If we collapse the colors to be more similar, it looks a lot more refined
- Every native Mac app, such as Music, Shortcuts and Weather, has prominent and accessible search. Evidence: everything has search, and it's always prominent and accessible
- Most command palette items take you to an entirely new screen. Evidence: most of those menu items take you to an entirely new screen
- If users don't see a change after a keyboard shortcut, they assume something went wrong. Evidence: If you don't see a change, you assume that something went wrong
- Onboarding is not very standard for Apple apps, but Raycast has a very good onboarding process. Evidence: This isn't super standard for Apple apps, but something like Raycast
- Keyboard shortcuts are very powerful but easy to forget; Google has a cheat sheet that is opened by another keyboard shortcut. Evidence: which is why Google has a cheat sheet

## Quotes

> the app shouldn't be a destination, but a system exactly where you need it.
> Design light and dark mode not as exact opposites.
> If you don't see a change, you assume that something went wrong.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment: Matter by JetBrains, an AI development companion used to prototype the UI from a Figma link; its claims are a paid read, not design guidance.
- Caveat: Self-promotion: the app built in the video is offered for download and its waitlist (kolejain.com/stash) is linked in the description.
- Caveat: Published 2025-12-02; macOS conventions described are as of that date.
- Caveat: Opinion framing: Apple is presented as the pinnacle of design; the patterns are the presenter's recommendations, not Apple guidelines quoted.
- Caveat: The dark-mode passage is muddled in auto-captions ('Directly inverting the colors looks okay' then 'doesn't look stellar'); the reading that dark mode needs wider color separation and light mode colors should be collapsed closer is the most consistent interpretation [inferred].
- Caveat: Auto-caption fixes: 'commandshifts' is Command Shift S, 'poll request' is pull request [inferred], 'one-sreen' is one-screen, 'atio' is probably Attio [inferred].
- Caveat: The video is visual; most on-screen examples are described only by narration, and no concrete color, size, duration or easing values are given apart from the roughly 50-pixel drag area. No media list was available.

### Rules and practices

- **should** (platforms, desktop): Design the app to appear where the user needs it (for example a window opened by a keyboard shortcut) and then get out of the way, instead of making it a destination they must visit. Why: To feel native, an app should be a system exactly where you need it, like Spotlight and Raycast. [To feel native, the app shouldn't be a destination]
- **consider** (components, desktop): Keep quick-capture windows minimal: drop the traffic lights and include only a drop area, a simple input and a few buttons. Why: The window should stay out of the way and be as minimal as possible, like widgets that slide in quietly from the side. [toss the traffic lights and just add the basics of a drop area]
- **consider** (components, desktop): Show keyboard shortcut reminders on the buttons they trigger. Why: Shortcuts are powerful but easy to forget, so users need reminders [inferred]. [I'll add in some keyboard shortcut reminders to those]
- **consider** (patterns, all): Use optimistic UI for background saves: show the action as done immediately (for example collapse into a toast) while processing continues in the background. Why: The image is processed and saved in the background while the UI assumes it will succeed; Apple Mail does the same when moving email to trash. [These are also all good examples of optimistic UI]
- **should** (layout, desktop): In a utility app, put global actions in the top bar, navigation in a sidebar and the main content in the centre. Why: Almost all of Apple's utility apps (Finder, Notes, Reminders, Calendar, Settings) use this layout because apps are user-focused. [the top for global level actions, the sidebar for navigation, and the main content in the center]
- **consider** (platforms, desktop): Integrate the traffic light window buttons into the top bar or sidebar and treat them like any other element. Why: Apple's own apps do this seamlessly. [seamlessly integrate the traffic light actions into the UI]
- **should** (layout, desktop): Do not clutter the top of a macOS window with actions; roughly the top 50 pixels is the window drag area, so let it breathe. Why: That area is used to drag the window. Values: 50 pixels. [the top roughly 50 pixels of their apps allow window dragging]
- **consider** (layout, desktop): Skip the sidebar when navigation is only browsing and searching, and use the space for the user's content. Why: It gives extra room for large images and lets the UI act as a container for the user's content. [we can skip the sidebar entirely]
- **should** (patterns, all): Show a simple empty state that invites the first action, and hide filters and other components until the user has content. Why: Progressive disclosure: only show what the user needs in that moment; filters aren't useful until there is content. [This is a form of progressive disclosure]
- **consider** (patterns, all): Show an item's full data only when the user clicks on it. Why: Another form of progressive disclosure that keeps the browsing view focused on content. [only showing all of the data when the user actually clicks on the image]
- **should** (process, all): Before adding colors or effects, decide the minimum UI needed to let the content shine. Why: The UI of a content app is a container for the user's content and should stay out of the way. [What is the minimum UI needed to really let that content shine?]
- **should** (color, desktop): Respect the system light and dark mode setting as much as possible. Why: All Macs let users switch between light and dark mode. [those settings should be respected as much as possible]
- **should** (color, all): Do not create one mode by directly inverting the other's colors; design light and dark mode as different but consistent. Why: Dark mode needs colors that are more different from each other than light mode; directly inverting into light mode makes the contrast much higher and doesn't look stellar, while collapsing the colors to be more similar looks a lot more refined. [Design light and dark mode not as exact opposites]
- **should** (patterns, desktop): Make search prominent and always accessible. Why: Every native Mac app (Music, Shortcuts, Weather) has search that is prominent and accessible. [everything has search, and it's always prominent and accessible]
- **should** (patterns, all): When search results look like the browse view, show the result count and a clear (X) button in the search bar, and the query with a back arrow in the top left. Why: The browsing and search pages look quite similar. [we'll add the search results count to the search bar and an X to clear]
- **must** (motion, all): Give every keyboard shortcut, and every interaction, immediate visible feedback: a micro-animation or at least a state change. Why: If users don't see a change, they assume something went wrong. [micro animations, or at least a state change, are instrumental]
- **consider** (components, all): Collapse a tool such as the floating search bar until the user needs it, and expand it to full size when it is clicked or its shortcut is triggered. Why: It stays out of the way until the user needs it while still giving immediate feedback. [we'll collapse it down. and clicking or triggering the shortcut beautifully expands it]
- **must** (patterns, desktop): Support drag and drop both into the app and out of it to other apps (for example into Figma or Finder). Why: It makes the experience feel effortless; Apple does this across Photos, Finder, Reminders and Shortcuts. [drag and drop of anything anywhere is a must]
- **consider** (components, all): Put frequent item actions (copy, find, delete) in a floating action bar in the preview panel. Why: Keeps common actions easy to access so they feel natural rather than like features. [we'll also have a floating action bar in the preview slide out]
- **should** (patterns, desktop): Include onboarding in desktop apps and use it to teach keyboard shortcuts, and provide a shortcut cheat sheet (for example in a settings popover). Why: Keyboard shortcuts are very powerful but easy to forget. [It's important to educate the users on keyboard shortcuts]
- **should** (process, all): Before designing screens, work out how and where the user will actually interact with the product, for example while they are working in other apps. Why: To feel native the app should be a system exactly where you need it, so how the user will actually interact with the final product is super important. [thinking about how the user will actually interact with a final product is super important]
- **should** (patterns, all): Design an app around the user's own content that they add and change, not like a landing page of pre-generated content, even when the components look similar. Why: A landing page is pre-generated content that doesn't really change, while an app holds the user's information, so apps are much more user-focused; the source calls this crucial. [an app is meant to hold the user's information]
- **consider** (process, desktop): Keep a utility app simple and good at doing one thing, so its UI can stay hyperfocused. Why: Apple's utility apps (Finder, Notes, Reminders, Calendar, Settings) are wonderfully simple and good at doing one thing, so the UI can stay hyperfocused. [wonderfully simple and good at doing one thing]
- **consider** (elevation, desktop): Give a floating quick-capture window a native blur, as Paste does. Why: The source copies Paste's native blur for its quick-save window, following apps that integrate seamlessly like native windows; it gives no other reason. [kind of like how paste has a native blur]
- **consider** (patterns, all): Let search match what is actually in the content (for example image recognition on images), not just titles. Why: A query such as 'mobile app with houses and a calendar' then returns relevant results. [search based on what's actually in the image instead of just by titles]
- **consider** (components, desktop): Offer Apple's universal share button on items alongside the app's own actions. Why: You'll find it on almost all Apple apps because sometimes it is just more convenient. [Apple's universal share button because sometimes that is just more convenient]

### Decisions it informs

- Should the app be a place people go to, or something that appears where they already are?
  - Destination app: Users must switch to the app's main window to act, breaking their flow [inferred]. When: Not recommended for utility apps in this source [inferred].
  - System that appears when needed: A shortcut-triggered window, popover or panel appears over whatever the user is doing and then gets out of the way, like Spotlight, Raycast or Paste. When: When users find or capture things while doing other work, such as moving between Figma, code and Notion.
  - Recommendation: Be a system exactly where you need it: a shortcut opens a minimal quick-save window, because that is what makes a Mac app feel native.
- Does the main window need a sidebar? (`Q-layout-04`)
  - Apple utility layout with sidebar: Top bar for global actions, sidebar for navigation, content in the centre, as in Finder, Notes, Reminders, Calendar and Settings. When: When the app has real navigation between sections [inferred].
  - No sidebar: More room for large content such as images; the UI becomes a container for the user's content. When: When navigation is really just browsing and searching.
  - Recommendation: Skip the sidebar for the example app because its navigation is only browsing and searching, which lets it stay out of the way.
- How should light and dark mode colors relate to each other? (`Q-color-16`)
  - Direct inversion: Contrast becomes much higher and it doesn't look stellar. When: Not recommended.
  - Designed separately but consistent: Dark mode colors spread further apart; light mode colors collapsed to be more similar, which looks more refined. When: Always, per the source.
  - Recommendation: Design light and dark mode not as exact opposites; they should feel different but consistent, because dark mode needs more separation between colors.
- How should search work in a mostly one-screen app?
  - Command palette or universal search: Sleek and intuitive, but most items take you to an entirely new screen. When: Powerful software such as Notion, Obsidian or Attio.
  - Floating search bar with a slide-out preview: Search happens in place; results stay on the same screen and a preview slides out from the side. When: When the goal is to remain largely a one-screen application, like most of Apple's utilities.
  - Recommendation: The source chose the floating search bar and slide-out preview to keep the app on one screen.
- How should a desktop app onboard new users? (`Q-pattern-04`)
  - No onboarding: Typical of Apple's own apps; shortcuts may go undiscovered [inferred]. When: Not recommended by the source.
  - Rich onboarding process: A fuller guided flow, like Raycast's. When: When the app has a lot to teach [inferred].
  - Simple modal with micro-interactions: A modal that closes when the user performs the key shortcut, which makes the quick-save window pop out. When: When the main thing to learn is a shortcut.
  - Recommendation: Use a simple onboarding modal that teaches the shortcut by having the user perform it, because shortcuts are powerful but easy to forget.
- Should the app follow the system light and dark mode setting? (`Q-theme-01`)
  - Light and dark, following the system setting: The app matches the light or dark mode the person chose for their Mac. When: By default: the source says those settings should be respected as much as possible.
  - Plus a light/dark setting in the app: The settings popover holds the light and dark mode settings next to the shortcut cheat sheet and the quick-save panel side. When: The source's example app includes it.
  - Recommendation: Respect the system light/dark setting as much as possible, and put the light and dark mode settings in the app's settings popover.
- Should filters and item details be visible from the start, or revealed when needed? (`Q-pattern-03`)
  - Show everything up front: Filters and full item data are on screen before they are useful [inferred]. When: Not recommended by the source [inferred].
  - Progressive disclosure: A simple empty state first; filters and other components stay hidden until the user starts saving; an item's full data shows only when it is clicked. When: When the UI is mainly a container for the user's content.
  - Recommendation: Only show the user what they need to see in that moment: hide filters until there is content and show item data on click.

### Process

1. Start outside the main window: Get comfortable with the UI that lives outside the main window (popovers, new windows, notifications) and decide how the app appears where the user needs it.
2. Map how the user actually works: Look at what the user is doing when they need the app (for example editing in Figma, then code, then Notion) and give them a keyboard shortcut to act without switching.
3. Design the quick-capture window: Keep it minimal: no traffic lights, a drop area, an input, a few buttons with shortcut reminders, and a native blur.
4. Add completion feedback: On Enter, collapse the window into a toast and slide it off screen, treating the save optimistically while it processes in the background.
5. Lay out the main window: Use top bar for global actions, sidebar for navigation and content in the centre, integrate the traffic lights, keep the top clear for dragging, and drop the sidebar if navigation is simple.
6. Design the empty state and progressive disclosure: Show a simple empty state inviting the first action; hide filters until there is content; reveal item details on click. Ask what minimum UI lets the content shine.
7. Design light and dark mode: Respect the system setting and design each mode separately rather than inverting, so they feel different but consistent.
8. Design search: Make search prominent; choose between a command palette and a floating search bar with slide-out preview; add result count, clear button, query label and back arrow.
9. Give shortcuts visible feedback: Make every shortcut produce a micro-animation or state change, for example the panel sliding in on Command Shift S and away on Escape, and the collapsed search bar expanding.
10. Support drag and drop and quick actions: Let content be dropped in and dragged out to other apps, add a floating action bar (copy, find, delete) and the share button.
11. Add onboarding and a shortcut cheat sheet: Use a simple onboarding modal that teaches the key shortcut, and put a cheat sheet, the panel side and light/dark setting in a settings popover.

### Examples and visual references

- Meeting pop-up (Notion): A pop-up appears as soon as Notion detects a meeting, showing a third-party app living outside its main window.
- Bottom-of-screen integration with native blur (Paste): Paste integrates seamlessly at the bottom of the screen, like the native top-bar window view, and has a native blur, which the example quick-save window copies.
- Shortcut-triggered, draggable search (Spotlight (macOS)): Opened with Command Space and draggable anywhere; the model for appearing when needed and getting out of the way.
- Quick-save window that becomes a toast (Kole Jain's design-inspiration app): A minimal window with a drop area, input and buttons with shortcut reminders; pressing Enter collapses it into a toast that slides off screen, showing optimistic UI and feedback.
- Delete before the server confirms (Apple Mail): The email moves to trash before it is actually deleted from the server, an example of optimistic UI.
- App versus landing page (Apple Notes and the iPhone landing page): Similar components but different jobs: static pre-generated content versus user content that is added and changed.
- Shared utility-app layout (Finder, Notes, Reminders, Calendar, Settings): Global actions on top, sidebar navigation, main content in the centre, with the traffic lights built into the top bar or sidebar.
- Empty state (Apple Notes and the example app): A clear empty state when there are no notes; the example app shows a simple invitation to start saving inspiration with all filters hidden.
- Prominent search (Music, Shortcuts, Weather (macOS)): Every native Mac app shows search prominently.
- Command palette (Notion, Obsidian, Attio): Universal search whose items usually open a new screen; considered but not used.
- Floating search bar and slide-out preview (Kole Jain's design-inspiration app): A collapsed search bar at the bottom expands on click or shortcut; search matches what is in the images, not just titles; the bar shows a results count and an X to clear, with the query and a back arrow top left. Searching by image lives in the slide-out preview, which shows a few relevant results per image and a floating action bar (copy, find, delete).
- Drag and drop everywhere (Photos, Finder, Reminders, Shortcuts): Content can be dragged in and out anywhere; the example app lets images be dragged out into Figma or Finder.
- Onboarding (Raycast): Cited as a very good onboarding process for a desktop app.
- Shortcut cheat sheet (Google): A keyboard-shortcut cheat sheet that is itself opened with a keyboard shortcut.
- Universal share button (Apple apps (almost all)): The system share button appears on almost all apps because sometimes it is just more convenient.
- Keyboard shortcut list (Reminders (macOS)): Shown as an example of how many keyboard shortcuts a native Mac app has.
- Onboarding modal that closes with the shortcut (Kole Jain's design-inspiration app): A simple modal with micro-interactions; performing the quick-save shortcut closes it and pops out the quick-save window.

### Numbers

- 50 pixels: Roughly the top 50 pixels of Apple's apps are used for window dragging, so keep them uncluttered. [the top roughly 50 pixels of their apps allow window dragging]
- Command shift S: Shortcut that opens the example app's quick-save panel (captions read 'commandshifts' once). [Command shift S slides out our quicksave panel]
- Command space: macOS Spotlight shortcut; the source also cites Command Tab to switch apps and command W to close tabs as examples of important system shortcuts. [Command space for Spotlight, Command Tab to switch apps]

<!-- /od:learn -->
