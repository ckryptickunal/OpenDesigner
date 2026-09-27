---
type: source
title: EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)
created: 2026-09-27
updated: 2026-09-27
video_id: B7k5rOgmOGY
url: https://www.youtube.com/watch?v=B7k5rOgmOGY
channel: Kole Jain
published: 2025-08-30T14:00:26Z
authority: reference
tags:
  - dashboard
  - saas
  - sidebar
  - navigation
  - data-tables
  - charts
  - modals
  - popovers
  - toasts
  - empty-states
  - bulk-actions
  - optimistic-ui
---

# EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)

## Metadata

- Video ID: `B7k5rOgmOGY`
- Channel: Kole Jain
- Published: 2025-08-30T14:00:26Z
- URL: https://www.youtube.com/watch?v=B7k5rOgmOGY

## Summary

Kole Jain designs a dashboard for a link-tracking product from scratch and explains the reasoning behind each part. He starts with the sidebar as the spine of the product: profile management at the top, links with an icon and a short title, links grouped by relevance, rarely used links at the bottom, dropdowns as the list grows, and a clear active state. For the main area he says dashboards need smaller text styles with less spacing between sizes than landing pages, stricter grids, and a main section that shows what matters most to the user, and he warns against cramming in too much. He then covers when to use a popover, a modal or a new page, toasts for confirmations, warnings and errors, and the four building blocks he says make up almost any dashboard page: lists and tables, cards, user input and tabs. For a design system, this gives a density stance for product screens, a sidebar recipe, clear rules for choosing between overlays, and a short list of dashboard components and patterns (empty states, bulk actions, chart hover and optimistic UI).

## Key Ideas

- Most dashboards fail not because they are ugly but because they are disorganized and messy.
- The sidebar is the spine of the product and holds persistent, globally relevant elements such as navigation, profile management and search.
- Navigation is about reducing cognitive load: group links by relevance and move rarely used ones (settings, help center) to the bottom.
- Sidebar links need a recognizable icon and a short title, which also makes a collapsible sidebar and notification counts or 'new' chips work.
- A dashboard should do one thing well; if it looks like it needs a PhD to operate, it is too complex.
- Dashboards use smaller text styles with less spacing between sizes than landing pages, and follow grids more strictly because they fill most of the screen.
- The main section should show what matters most to the user, such as project status in a project tool or investments in a finance tool.
- Keep displayed data minimal, think about the empty state, and let people select many items to reveal bulk actions.
- Charts should be familiar (line and bar), with grid lines, numbers, a short summary and a date range selector.
- Use a popover for simple, non-blocking context, a modal for more complex context that stays on the same page, and a new page for permanent or very large context.
- Toasts are the dashboard's notification system: they confirm changes made in a modal and surface warnings and errors that often get missed.
- Almost any dashboard page can be built from four components: lists and tables, cards, user input and tabs.
- A good list comes down to separation by space, lines or color; a good table comes down to search, filter and sort.
- Dashboard motion is tame and user focused; charts are where hover effects can be more creative.
- Optimistic UI makes a dashboard feel snappy by updating the screen instantly on the assumption that the server request will succeed.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Creator of the video, published on his Kole Jain YouTube channel.
- [[entities/mobbin|Mobbin]] (product): Library of real app screenshots that sponsors the video (auto-captions spell it 'Mvin' and 'Mobin').
- [[entities/dub|Dub]] (company): Named as putting notifications in the empty space of its sidebar.
- [[entities/linear|Linear]] (company): Named alongside Dub as adding notifications to the sidebar.
- [[entities/github|GitHub]] (product): Cited as similar to the brief description added to each item in the link list.
- [[entities/vercel|Vercel]] (product): Example of tables with forms inside cards (auto-captions spell it 'Versel').
- [[entities/notion|Notion]] (product): Example of tabs showing different views of related tables, and of a settings modal built from lists, inputs and cards.
- [[entities/gmail|Gmail]] (product): Example of optimistic UI: a deleted email disappears instantly.
- [[entities/optimistic-ui|Optimistic UI]] (concept): Updating the interface immediately on the assumption the server request will succeed.
- [[entities/popover|Popover]] (concept): A non-blocking overlay for simple context that people can click away from.
- [[entities/modal|Modal]] (concept): A blocking overlay for more complex context that keeps the user on the same page.
- [[entities/toast|Toast]] (concept): The dashboard's notification system for confirmations, warnings and errors.
- [[entities/bulk-actions|Bulk actions]] (concept): A contextual button revealed when the user selects multiple items.

## Topics

- [[topics/dashboards-and-data-display|Dashboards and data display]]: Walks through a full dashboard: focus on one job, show what matters most in the main section, keep data minimal, use a simple grid, clear charts with grid lines and numbers, and four core components (lists and tables, cards, user input, tabs).
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: The sidebar is the product's spine: profile management at the top, icon plus short title links grouped by relevance, settings and help at the bottom, dropdowns as links grow, an active state, and optional highlighted features or notifications.
- [[topics/saas-product-ui|SaaS product UI]]: Uses a link-tracking SaaS as the demo and argues dashboards matter more as AI makes software easier to produce; covers page actions at the top, bulk actions, tabs and optimistic UI.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers suit simple, non-blocking context such as display settings; modals suit more complex, blocking context that should stay on the same page, such as creating a link; very large or permanent context gets a new page.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toasts are the notification system of a dashboard: confirm changes made in a modal, raise awareness without taking over the screen, prompt action, and surface warning and error states.
- [[topics/cards-and-sections|Cards and sections]]: Most dashboards are made of many cards; keep card margins well spaced and choose a border or background color (he prefers outlines in dark mode and fills in light mode).
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Think about the empty state for a list with no data to display; use toasts for confirmation, warning and error feedback.
- [[topics/typography|Typography]]: Dashboard text styles are much smaller than a landing page's, with less spacing between sizes, because more has to fit.
- [[topics/spacing-and-layout|Spacing and layout]]: Dashboards follow grids more strictly than landing pages because they use most or all of the screen; the demo uses a two column, two row grid.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Items and cards can be separated by their own border, dividers, background color or space; stacking items in a list gives less clutter than bordering each one.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: His personal preference is outlined cards in dark mode and background-colored cards in light mode.
- [[topics/micro-interactions|Micro-interactions]]: Selecting multiple items reveals a bulk-actions button; chart hover shows a value with a percent bubble or dims the other bars.
- [[topics/motion-principles|Motion principles]]: Animation on dashboards is tame and user focused compared with websites and landing pages; people want a snappy, fast dashboard.
- [[topics/forms-and-inputs|Forms and inputs]]: User input is one of the four core dashboard components, found in modals such as 'create link' and in settings pages.
- [[topics/portfolio-and-case-studies|Portfolio and case studies]]: Dashboards are a staple of design portfolios, but most are disorganized and messy.

## Notable Claims

- Most portfolio dashboards are bad because they are disorganized and messy, not because they are ugly. Evidence: Not because they're ugly, but because they're disorganized and messy
- The sidebar houses most of the persistent and globally relevant elements, such as navigation, profile management and search. Evidence: houses most of the persistent and globally relevant elements
- A recognizable icon with a short title helps when the sidebar is collapsible and when a notification number or 'new' chip is added. Evidence: This is especially helpful if you plan on making your sidebar collapsible
- Navigation is about reducing cognitive load, which is done by grouping links by relevance. Evidence: Navigation is all about reducing cognitive load
- Settings and help center are rarely used, so they can go to the bottom of the sidebar. Evidence: since settings and help center are rarely used
- Dub and Linear have started putting notifications in the sidebar. Evidence: Companies like Dub and Linear have already started doing this
- Dashboard features are much smaller than a landing page's because many more things must fit. Evidence: the features of a dashboard are much smaller
- Dashboards use many smaller font sizes without much spacing between sizes. Evidence: We've got a lot of smaller font sizes without much spacing in between sizes
- Grids and layouts are followed more strictly on dashboards than on landing pages because dashboards use most or all of the screen. Evidence: Grids and layouts are also much more strictly followed for dashboards
- What goes in the main section of a dashboard reflects what is most important to the user. Evidence: reflects what is most important to the user
- The very top of a dashboard is generally reserved for important page actions or simple navigation. Evidence: is generally reserved for important page actions or simple navigation
- Stacking items into a list makes it easier to add an empty state than bordering each item. Evidence: This layout also makes it easier to add an empty state
- People often forget grid lines and numbers on charts. Evidence: Add some grid lines and numbers since everyone forgets those
- A popover is best when context is simple and it is non-blocking, meaning the user can click away without consequences. Evidence: best used when the context is simple
- A modal is blocking because the user must click create or cancel before doing anything else. Evidence: A modal is considered blocking
- Because the page cannot be seen while changes are made in a modal, a toast confirming the changes is generally good practice. Evidence: a toast notification confirming the changes is generally a good practice
- Warning and error states frequently get missed, and toasts are good for them. Evidence: toasts are great for a warning or error states
- When sending the user to a new page, a back button or breadcrumb is pretty much required. Evidence: having a back button or breadcrumb is pretty much required
- There are really only four main dashboard components: lists and tables, cards, user input and tabs. Evidence: there are really only four main dashboard components
- Making a good list mostly comes down to separation, done with space, lines or dividers, or color. Evidence: Making a good list mostly comes down to separation
- Search, filter and sort transform a table into an interactive tool. Evidence: transforms it into an interactive tool
- Tabs add new pages without cluttering the sidebar. Evidence: adding new pages without cluttering the sidebar
- Animation and interaction on dashboards are tame and user focused compared with websites and landing pages. Evidence: animation and interaction on dashboards is pretty tame and user focused
- Optimistic UI removes awkward pauses by acting as if the server request will succeed. Evidence: The app is optimistic that it will succeed

## Quotes

> If your dashboard looks like it requires a PhD to operate, then it's too complex.
> Just do one thing well with your dashboard.
> Navigation is all about reducing cognitive load.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Mobbin (a 20% discount link, 'hundreds of thousands' of screenshots) in the middle and at the end of the video; excluded from rules. Auto-captions spell it 'Mvin' and 'Mobin'.
- Caveat: The description links the creator's own Figma files for the dashboard (self-promotion).
- Caveat: No exact values are given: no font sizes, spacing, radii, colors, grid measurements or animation timings. The text-style comparison and most charts are only shown on screen.
- Caveat: Several points are personal preference, not tested findings: outlines in dark mode and fills in light mode ('totally up to you'), profile at the top of the sidebar, and 'only four main dashboard components'.
- Caveat: Auto-caption fixes: 'textiles' read as 'text styles', 'Versel' as Vercel, and 'shorten link' as the shortened link. A word is missing in 'don't make weird  like this', so the kind of chart he rejects is only shown on screen.
- Caveat: It does not cover loading states, accessibility, keyboard use, responsive or mobile layouts, or chart colors.
- Caveat: Published 2025-08-30; auto-generated English transcript.

### Rules and practices

- **should** (layout, all): Put persistent, globally relevant elements (navigation, profile management, search) in the sidebar; profile management and search may instead go in the top bar. Why: The sidebar is the spine of the product. [Think about it as the spine of your product]
- **consider** (components, all): Put profile management at the top of the sidebar, with a profile picture and arrows that show it is clickable, rather than a logo. Why: The creator finds it a more convenient spot; the picture makes it easy to identify and the arrows show it can be clicked. [I find this a more convenient spot for profile management]
- **should** (components, all): Give every sidebar link a recognizable icon and a short title. Why: It is especially helpful if the sidebar is collapsible, and if you want to add a notification number or a 'new' chip. [We want to start with a recognizable icon and a short title]
- **should** (patterns, all): Group sidebar links by what is relevant to each other. Why: Navigation is about reducing cognitive load. [group our links by what's relevant]
- **should** (patterns, all): Move rarely used links such as settings and help center to the bottom of the sidebar. Why: They are rarely used. [since settings and help center are rarely used, we can send them down to the bottom]
- **should** (patterns, all): Nest sidebar links into dropdowns once the number of links grows. Why: The source gives it as the step to take as the amount of links expands. [you'll want to start nesting links into drop downs]
- **must** (components, all): Show an active state on the current sidebar link, for example a rectangle indicator. Why: The source says to make sure the active state is there. [make sure to have an active state]
- **consider** (patterns, all): Optionally use the sidebar to highlight features, search or integrations, and use its empty space for notifications. Why: Both are optional; Dub and Linear already put notifications there. [if you want to highlight features, search or integrations]
- **should** (patterns, all): Give the dashboard one clear job; if it looks like it needs a PhD to operate, cut it back. Why: A dashboard that looks like it requires a PhD to operate is too complex; the cluttered counterexample feels like someone emptied a drawer onto the screen. [Just do one thing well with your dashboard]
- **should** (typography, all): Use smaller text styles for dashboards than for landing pages, with less spacing between sizes. Why: A dashboard has to fit many more things. [We've got a lot of smaller font sizes without much spacing in between sizes]
- **should** (layout, all): Follow the grid and layout more strictly on dashboards than on landing pages. Why: Dashboards use most or all of the space on screen. [Grids and layouts are also much more strictly followed for dashboards]
- **should** (layout, all): Put what matters most to the user in the main section of the dashboard, such as project status in a project management tool or investments at the top of a financial dashboard. Why: The main section reflects what is most important to the user. [you should show investments right at the top]
- **should** (layout, all): Reserve the very top of the dashboard for important page actions or simple navigation, such as a dropdown and a primary 'create' button. Why: That area is generally reserved for them. [The very top of the dashboard is generally reserved for important page actions]
- **should** (content, all): Keep data shown on the dashboard home page to a few essential fields per item. Why: Data displayed on the homepage should be kept super simple; the demo shows only favicon, short link, full link, creation date and clicks. [you'll want to keep it super simple]
- **consider** (content, all): Add a brief description to each list item, similar to GitHub, to use the space in the middle of the row. Why: The source adds it to fill the space in the middle of each row; no other reason is given. [we can add a brief description, kind of similar to GitHub]
- **consider** (components, all): Stack items into a single list for less clutter; give each item its own border only when you want stronger visual separation. Why: A stacked list is less cluttered and makes adding an empty state easier. [But for less clutter, we'll stack them into a list]
- **should** (patterns, all): Design an empty state for lists, for when there is no data to display. Why: The source calls it important to be thinking about. [which is important to be thinking about]
- **should** (patterns, all): Let users select multiple items and reveal a contextual bulk-actions button when they do. Why: Real-world applications need to manage data efficiently. [Letting the user select multiple links which reveals a new contextual button, bulk actions]
- **should** (components, all): Do not use unfamiliar, unreadable chart shapes; start from a basic line graph. Why: Nobody can tell what the unusual charts are. [I don't know what these are, and neither does anyone else]
- **should** (components, all): Add grid lines and numbers to charts. Why: Everyone forgets them. [Add some grid lines and numbers since everyone forgets those]
- **should** (components, all): Add a short summary and a date range selector to charts. Why: With them the source calls the line chart good to go, and it gives the bar chart the same range selector. [Pop in a quick summary and date selector]
- **consider** (components, all): In a bar chart that breaks data down per item, show each item's icon (such as its favicon) beside its bar. Why: It makes each item easy to identify. [with the favicon on the side to make them easily identifiable]
- **should** (components, all): Use a popover for simple context that should not block the page, such as display settings. Why: It is non-blocking: the user can click away without any consequences. [best used when the context is simple, like these display settings]
- **should** (components, all): Use a modal for more complex context when the user should stay on the same page, such as creating an item that belongs to the list on screen. Why: The task is directly related to what is displayed; the modal is blocking, so the user must create or cancel first. [A modal is best used when the context is more complex]
- **should** (patterns, all): Show a toast confirming the changes after a modal closes. Why: The user cannot see the page while the changes are being made. [a toast notification confirming the changes is generally a good practice]
- **should** (patterns, all): Use toasts to make users aware of something or prompt them to act without taking over the screen, including warning and error states. Why: Toasts are the dashboard's notification system, and warnings and errors frequently get missed. [without taking over the entire screen or prompt them to take action]
- **consider** (patterns, all): Send the user to a new page when the context is more permanent or very large, such as opening an existing item. Why: The source calls a new page reasonable for permanent or very large context. [it's reasonable to direct the user to a new page]
- **must** (patterns, all): When you send the user from the dashboard to a new page, include a back button or breadcrumb. Why: The source says a back button or breadcrumb is pretty much required when you send the user to a new page. [having a back button or breadcrumb is pretty much required]
- **should** (components, all): Separate list items with space, lines or dividers, or color. Why: Making a good list mostly comes down to separation. [Making a good list mostly comes down to separation with three ways to do it]
- **should** (components, all): Give tables search, filter or sort controls. Why: Displaying data is only half the battle; these controls turn the table into an interactive tool. [Giving the user the options to search, filter, or sort the table]
- **should** (layout, all): Keep card margins well spaced so content is not packed too tightly. Why: So content isn't too tightly packed; most dashboards are made of many cards together. [Keep the margins well spaced so content isn't too tightly packed]
- **consider** (elevation, all): Separate cards with either a border or a background color; the source's preference is outlines in dark mode and background colors in light mode. Why: Personal preference, which the source says is totally up to you. [I prefer outlines on dark modes and background colors on light mode]
- **should** (components, all): Use tabs to add closely related views or pages without adding items to the sidebar. Why: Tabs add new pages without cluttering the sidebar and keep the user in the page's context. [These are fantastic for essentially adding new pages without cluttering the sidebar]
- **consider** (motion, all): On chart hover, show the value (for example with a bubble showing a percent) or dim all the other bars in a bar chart. Why: Charts are where dashboard motion can get a little more creative. [when we hover, all of the other bars dim out]
- **consider** (motion, all): Keep dashboard animation tame and user focused, and save more creative motion for chart hover states. Why: Dashboard animation is tame compared with websites and landing pages, and charts are where you can get more creative. [Starting with our chart animations, here is where we can get a little more creative]
- **should** (patterns, all): Use optimistic UI: update the screen immediately (for example remove a deleted item) on the assumption the server request will succeed. Why: Everyone wants a snappy, fast dashboard without awkward pauses before an item disappears. [That's where optimistic UI comes into play]

### Decisions it informs

- Where should profile management and search live: in the sidebar or in the top bar?
  - Sidebar: Profile sits at the top of the sidebar with a picture and arrows, next to navigation, as part of the product's spine. When: The creator's preferred spot for profile management.
  - Top bar: Profile management and search move out of the sidebar into the bar above the page. When: The source says this is sometimes done; no condition is given.
  - Recommendation: The creator puts profile management at the top of the sidebar because he finds it more convenient; both are accepted.
- How dense should a product dashboard's text and layout be compared with a landing page? (`Q-dir-02`)
  - Landing-page scale: Larger features and text styles, with grids and layouts followed less strictly. When: Landing pages.
  - Dashboard scale: Many smaller font sizes without much spacing between sizes, and a strictly followed grid that uses most or all of the screen. When: Dashboards, where many more things have to fit.
  - Recommendation: Use the smaller, tighter dashboard scale for dashboards because many more things must fit.
- How should items in the main list be set apart from each other?
  - Each item in its own border: Stronger visual separation between items. When: When you want visual separation.
  - Stacked into one list: Less clutter, and an empty state is easier to add. When: The default in the demo.
  - Recommendation: Stack items into a list for less clutter.
- How should the rows of a list be separated? (`Q-depth-05`)
  - Space: Rows are separated only by gaps. When: Not stated in the source.
  - Lines or dividers: A line sits between rows. When: Not stated in the source.
  - Color: Rows are separated by background color. When: Not stated in the source.
- How should cards stand out from the page: a border or a background color? (`Q-depth-01`)
  - Border (outline): Cards are outlined. When: The creator's preference in dark mode.
  - Background color: Cards are filled with a different color from the page. When: The creator's preference in light mode.
  - Recommendation: Outlines in dark mode and background colors in light mode, as a personal preference that is 'totally up to you'.
- Which chart types should the dashboard use? (`Q-viz-01`)
  - Unusual chart shapes: Nobody can tell what they show. When: Never, according to the source.
  - Line graph: A basic line with grid lines, numbers, a quick summary and a date selector. When: The starting point for the main metric in the demo.
  - Bar chart: Breaks the metric down per item, with each item's favicon on the side, a range selector and switchable metrics (signups, conversion). When: Comparing items against each other in the demo.
  - Recommendation: Use basic, familiar charts (line and bar) and add grid lines, numbers, a summary and a date range selector.
- When an action needs more UI, should it open a popover, a modal or a new page?
  - Popover: Non-blocking: the user can click away without any consequences. When: Simple context, such as display settings.
  - Modal: Blocking: the user must create or cancel before doing anything else, and the page is hidden while they work, so a confirming toast follows. When: More complex context that is directly related to the current page, such as creating a link.
  - New page: Moves the user away, so a back button or breadcrumb is needed. When: Permanent or very large context, such as opening an existing link.
  - Recommendation: Match the surface to the size and permanence of the context: popover for simple, modal for complex but same-page, new page for permanent or very large.
- Should the screen wait for the server before showing the result of an action?
  - Wait for the server: Awkward pauses before, for example, a deleted link disappears. When: The source does not recommend it.
  - Optimistic UI: The item disappears instantly, on the assumption that the request will succeed, so the dashboard feels snappy. When: When you want a snappy, fast dashboard (Gmail's delete).
  - Recommendation: Use optimistic UI so there are no awkward pauses.

### Process

1. Build the sidebar first: Treat it as the product's spine: profile management at the top, links with a recognizable icon and short title, grouped by relevance, settings and help center at the bottom, dropdowns as links grow, an active state, and optionally highlighted features or notifications.
2. Decide what matters most: Pick the one job the dashboard does well and put what matters most to the user in the main section (project status, investments and so on).
3. Set up a simple grid: Use dashboard-sized text styles and a strict grid; the demo uses a two column, two row grid with link management at the top and a few important metrics below.
4. Place page actions at the top: Reserve the very top for important page actions or simple navigation, such as a dropdown and a 'create link' button.
5. Build the main list: Show only essential fields per item, add a brief description if there is space, choose bordered items or a stacked list, and design the empty state.
6. Add bulk actions: Let the user select multiple items and reveal a contextual bulk-actions button.
7. Build clear charts: Start with a basic line graph, add grid lines, numbers, a quick summary and a date selector; add a per-item bar chart with icons, the same range selector and switchable metrics.
8. Add functionality through overlays and pages: Use popovers for simple non-blocking settings, modals for complex same-page tasks, and new pages with a back button or breadcrumb for large or permanent context; confirm modal changes with a toast.
9. Lay out other pages from four components: Compose remaining pages from lists and tables (with search, filter, sort), cards (well-spaced margins, border or fill), user input and tabs.
10. Add tame, user-focused motion: Add chart hover effects and use optimistic UI so actions feel instant.

### Examples and visual references

- Link-tracking dashboard built in the video: A sidebar plus a two column, two row grid: link management at the top and a few important metrics (charts) below.
- Collapsible sidebar with icon and short-title links: Links collapse to their icons [inferred], and can carry a notification number or a 'new' chip; the active link is marked with a rectangle indicator.
- Notifications in the sidebar's empty space (Dub, Linear): The spare space in the sidebar holds notifications.
- A cluttered dashboard: Shown as a counterexample that 'feels like someone emptied a drawer onto the screen'.
- Landing page vs dashboard text styles: Side-by-side text styles: the dashboard's are much smaller, with little spacing between sizes.
- Link list items: Each row shows a favicon, the short link, the full link, the creation date and the click count, with a brief description like GitHub's; rows can be bordered or stacked in one list.
- Bulk selection: Selecting several links reveals a new contextual 'bulk actions' button.
- Line chart and per-link bar chart: The line chart has grid lines, numbers, a quick summary and a date selector; the bar chart lists each link with its favicon, a range selector and signups and conversion options.
- Chart hover effects: Hovering the line chart shows the number and a bubble with a percent; hovering the bar chart dims all the other bars.
- Display settings popover: A non-blocking overlay for simple display settings that the user can click away from without consequences.
- Create link modal followed by a toast: A blocking modal with create and cancel; after creating, a toast confirms the change because the page was hidden.
- Link detail page: Clicking an existing link opens a new page with a back button or breadcrumb.
- Tables with forms inside cards (Vercel): Cards contain tables that include form inputs.
- Tabs for related table views and a settings modal (Notion): Tabs switch between views of related tables without leaving the page; the settings modal is mostly lists with some inputs, and cards in the connections section.
- Optimistic delete (Gmail): A deleted email disappears instantly, before the server confirms.

### Numbers

- two column, two row grid: The grid used for the demo dashboard: link management at the top, metrics below. [we'll be using a very simple two column, two row grid]
- four: Main dashboard components: lists and tables, cards, user input, tabs. [there are really only four main dashboard components]
- three: Ways to separate list items: space, lines or dividers, color. [with three ways to do it]

<!-- /od:learn -->
