---
type: source
title: The 3 dashboard UI flaws that give away you've NEVER built one
created: 2026-09-27
updated: 2026-09-27
video_id: Ksx9C2-3yMo
url: https://www.youtube.com/watch?v=Ksx9C2-3yMo
channel: Kole Jain
published: 2026-06-21T16:03:37Z
authority: reference
tags:
  - dashboards
  - data-tables
  - progressive-disclosure
  - spectrum-of-explicitness
  - onboarding
  - tooltips
  - popovers
  - hidden-ui
  - data-driven-color
  - timeline
  - kole-jain
---

# The 3 dashboard UI flaws that give away you've NEVER built one

## Metadata

- Video ID: `Ksx9C2-3yMo`
- Channel: Kole Jain
- Published: 2026-06-21T16:03:37Z
- URL: https://www.youtube.com/watch?v=Ksx9C2-3yMo

## Summary

Kole Jain names three flaws that show a designer has never built a real dashboard, and how to fix each. First, the data should drive the form: columns with a fixed set of values become chips, numbers are right-aligned, long text is truncated, inactive rows are shaded, time-based data becomes a timeline, and color comes from what the data means rather than decoration. Second, hierarchy is also about what you show and hide (progressive disclosure): rarely used features go into popovers, secondary actions appear on hover, and onboarding sequences features, starting with a single tooltip, instead of explaining everything at once. Third, much of a finished product is UI you cannot see at first, such as copy chips over cells, comment indicators, hidden states and tooltips, which beginner dashboards almost always miss. For a design system, this gives rules for table and data display, a 'spectrum of explicitness' for deciding how visible an action should be, and a reminder to design hidden states and tooltips as part of every component.

## Key Ideas

- Dashboards exist to display data, so the UI should be shaped around the data it shows.
- Columns that only have a set number of values, like department or employment status, read better as chips.
- Right-aligning numbers lines digits up by place value.
- Truncating long text frees room for the other columns, and shading inactive or deactivated rows sets them apart.
- Data that is split by time may not belong in a table at all; a timeline is easier to follow than a time-sorted table.
- Landing pages can get away with a lot, but dashboard color should come from the data, such as red for an urgent action.
- Avatars let the eye link who did what faster than reading a name, and a chart can summarise data that has a time dimension.
- Progressive disclosure is a kind of hierarchy based on what you show and what you hide.
- The spectrum of explicitness runs from a global, always-visible button (high) to an icon that appears on hover (low).
- Onboarding is progressive disclosure: sequence features so the user is never overwhelmed, rather than hiding them.
- A dense design gets its extra functionality from UI you cannot immediately see, and there is a lot of it.
- New features often do not need a dedicated page; they need to be better thought through in how they are implemented.
- Putting the pieces together (spacing, sizing) is not that hard; orchestrating them, including components with hidden parts and states, takes thought.
- Tooltips are missing on nearly all beginner dashboards; assume users will not understand every icon or ambiguous label.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Presenter of the video and owner of the channel.
- [[entities/mobbin|Mobbin]] (company): Library of real app screens that sponsors the video (auto-captions spell it 'Mavin'); it also launched an MCP.
- [[entities/apple-reminders|Apple Reminders]] (product): Cited as doing progressive disclosure well: swiping left and right reveals secondary actions.
- [[entities/progressive-disclosure|Progressive disclosure]] (concept): Hierarchy based on what you show and what you hide; the second of the three flaws.
- [[entities/spectrum-of-explicitness|Spectrum of explicitness]] (concept): The presenter's scale for how visible an action is, from an always-visible global button to a hover-only icon.
- [[entities/figma|Figma]] (tool): The video's assets are offered as Figma files through a link in the description.

## Topics

- [[topics/dashboards-and-data-display|Dashboards and data display]]: Let the data drive the form: chips for fixed-value columns, right-aligned numbers, truncated long text, shaded inactive rows, timelines for time-based data, and summary charts for data with a time dimension.
- [[topics/visual-hierarchy|Visual hierarchy]]: Besides strong versus poor hierarchy in a card, there is hierarchy by what you show and hide (progressive disclosure), placed along a spectrum of explicitness.
- [[topics/onboarding|Onboarding]]: Start with a single tooltip on the most important action, then a second one or a simple checklist in a corner; avoid a login modal that explains the whole product in six bullet points.
- [[topics/modals-and-popovers|Modals and popovers]]: Put infrequent features like sharing into a popover rather than a permanent panel or a new page; put the popover's primary action (a search box) at the top and reveal secondary actions on hover.
- [[topics/color|Color]]: In dashboards, color should come from the data itself, for example a red icon in a chip to draw the eye to an urgent action, not be sprinkled in to look nice.
- [[topics/icons-and-imagery|Icons and imagery]]: Avatars in activity logs speed up recognising who did what; icons need tooltips because users will not understand all of them.
- [[topics/gestures-and-drag|Gestures and drag]]: Apple Reminders reveals secondary actions on swipe left and right, keeping the main action (checking off a reminder) primary.
- [[topics/ai-assisted-design|AI-assisted design]]: The presenter says AI struggles with the idea that UI is as much about what you cannot see as what you can.

## Notable Claims

- Building the UI around the data a dashboard needs to display gives a much more usable experience. Evidence: we end up with a much more usable experience
- Department and employment status suit chips because there is only a set number of them. Evidence: there's only a set number of departments or employment statuses
- Right-aligning numbers makes the digits align by place value. Evidence: right align the numbers so the digits align by place value
- Truncating long text gives more breathing room to the other columns. Evidence: truncating long text to give more breathing room to the other columns
- Time-delineated data is easier to follow as a timeline than as a time-sorted table. Evidence: arrange this as a timeline, it starts to become a lot easier to follow
- Landing pages can get away with a lot, but dashboard colors should come from the data itself. Evidence: Landing pages, you can get away with a lot
- An avatar lets the eye associate who did what much faster than reading a name in a column. Evidence: The avatar is there because your eye can associate who did what way faster
- A chart shows the time dimension of data instantly instead of making the user hunt through a timestamp column. Evidence: instead of making you hunt through a timestamp column
- Progressive disclosure is a type of hierarchy based on what you show and what you hide. Evidence: another type of hierarchy based on what you show and what you hide
- A modal that explains the entire product at login is forgotten the moment it is dismissed. Evidence: instantly forgetting the moment you dismiss
- AI has a hard time grasping that UI is as much about what you cannot see as what you can. Evidence: A really important concept that AI has a hard time wrapping its figurative head around
- Tooltips are missing on pretty much all beginner dashboards. Evidence: what's missing pretty much unequivocally on all beginner dashboards are tooltips
- New features or elements often do not require a dedicated page. Evidence: new features or elements often don't require a dedicated page

## Quotes

> UI is as much about what you can see as what you can't see.
> dashboard colors shouldn't just be sprinkled in to look nice.
> You're not hiding functionality, you're sequencing it so that the user is never overwhelmed.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Mobbin (auto-captions say 'Mavin'): hundreds of thousands of curated screens, a new MCP, a banking mood board made in about 2 minutes, and 20% off; excluded from rules. The advice to study real software leads directly into this read.
- Caveat: No exact values are given: no spacing, sizes, colors, row heights, hover delays or tooltip timings. The before-and-after comparisons are shown visually only; the Figma files linked in the description were not reviewed.
- Caveat: The 'three tells' framing and the claim that AI struggles with hidden UI are the presenter's opinion, not backed by evidence in the video.
- Caveat: Hover-only reveals and hover tooltips assume a pointer; the video does not discuss touch or keyboard access to hidden actions [inferred].
- Caveat: Auto-caption error: 'larger drawers, models' almost certainly means modals [inferred].

### Rules and practices

- **should** (components, all): Display table columns that have a fixed set of values, such as department or employment status, as chips. Why: There is only a set number of departments or employment statuses, and chips let the data drive the form. [turned the department and employment into chips]
- **should** (layout, all): Right-align numeric columns in tables. Why: Digits then align by place value. [right align the numbers so the digits align by place value]
- **should** (components, all): Truncate long text in table cells. Why: It gives more breathing room to the other columns. [truncating long text to give more breathing room]
- **consider** (components, all): Shade out table rows that are inactive or deactivated. Why: It lets the row's status shape how the table looks, part of letting the data drive the form. [shade out rows of the table that are inactive or deactivated]
- **should** (patterns, all): Show time-delineated data as a timeline, placed in a sidebar pop-out or as a wider second column beside the table, instead of a time-sorted table. Why: A timeline is a lot easier to follow and lets the data determine the shape of the UI. [if we were to arrange this as a timeline]
- **should** (color, all): Do not add color to a dashboard for decoration; derive it from the data, such as a red icon in a chip for an urgent action. Why: Dashboard color should come from the data itself; the red draws the eye because the action is urgent. [dashboard colors shouldn't just be sprinkled in to look nice]
- **should** (patterns, all): Show an avatar next to the actor in activity logs. Why: The eye associates who did what much faster than by reading a name in the column. [The avatar is there because your eye can associate who did what]
- **consider** (patterns, all): Add a summary chart when the data has a time dimension. Why: The chart shows the change over time instantly instead of making users hunt through a timestamp column. [adding a chart to roll up the data into a summary]
- **should** (patterns, all): Put infrequently used features, such as sharing, in a popover rather than permanently in the layout or on a separate page. Why: They are not accessed often or important enough to be always visible, and a popover avoids taking the user to an entirely different page. [we tuck it into a popover so we don't have to rip the user to an entirely different page]
- **should** (components, all): Place a popover's primary action, such as the search box in a share popover, at the top where it is immediately visible. Why: It is the primary action of the popover. [the primary action is of course the search box]
- **should** (patterns, all): When space is tight, reveal secondary actions such as removing a user as an icon on hover, with a tooltip. Why: The action is not a main one, so it is progressively revealed as soon as the user starts to look for it. [we show the remove button on hover along with a tooltip]
- **should** (patterns, all): Onboard new users with a single tooltip pointing at the most important action, then a second tooltip or a simple checklist in the corner once they have done it. Why: Sequencing features means the user is never overwhelmed, without hiding functionality. [A good onboarding might start with a single tooltip]
- **should** (patterns, all): Do not explain the entire product in a modal of bullet points the moment a user first logs in, and do not drop first-time users onto a fully loaded dashboard. Why: Users forget the modal instantly once they dismiss it, and a fully loaded dashboard leaves them wondering where to start. Values: six bullet points. [explaining the entire product in a modal with six bullet points]
- **must** (components, all): Add tooltips to icons and to ambiguous labels. Why: Assume users will not understand all of the icons, or may want more detail; tooltips are missing on nearly all beginner dashboards. [what's missing pretty much unequivocally on all beginner dashboards are tooltips]
- **should** (components, all): Design the hidden UI of dense components, such as a copy chip over table cells on hover and a small triangle indicator for comments, along with the hidden components and states of drawers and modals. Why: In a dense design, additional functionality has to come from parts of the UI you cannot immediately see, and the table needs all of it to function. [a copy chip over the cells or perhaps comment functionality with a small triangle indicator]
- **consider** (process, all): Before giving a new feature its own page, check whether it can live in existing UI through hidden components and states, such as those of a drawer or modal. Why: New features or elements often don't require a dedicated page, just to be better thought through in how they are implemented. [new features or elements often don't require a dedicated page]
- **consider** (patterns, all): Design the rarely seen moments too, such as new-feature announcements and onboarding pop-ups that explain part of the product. Why: There is a lot of hidden UI that is important for a finished product. [Think about moments in software that you almost never see]
- **should** (patterns, all): Place each action on the spectrum of explicitness by how important and frequently used it is: a global, always-visible button (such as share) sits high, and a minor action (such as copying a cell) can be an icon revealed on hover. Why: The spectrum runs from a global, always-visible share button (quite high) to an icon to copy a cell on hover (much lower); actions that are not frequently accessed or not main actions are revealed progressively. [what I've just described is called the spectrum of explicitness]
- **consider** (patterns, all): Consider revealing useful but secondary list-item actions on swipe left and right, as Apple Reminders does, keeping them apart from the primary action of checking the item off. Why: The source cites it as progressive disclosure done really well: swiping reveals useful but secondary actions compared to checking off the reminder. [On swipe left and right, it reveals useful but secondary actions]

### Decisions it informs

- How should a table column with only a few possible values, like department or status, be shown?
  - Plain text: The table looks logically laid out, but nothing is driving the form. When: Not recommended by the source for fixed-value columns.
  - Chips: The table starts to shape up around its data. When: When there is only a set number of possible values.
  - Recommendation: Chips, because there is only a set number of departments or employment statuses.
- How should data that is ordered by time be displayed?
  - Time-sorted table: Works and can be used, but is harder to follow and does not let the data shape the UI. When: The source says it works but is not the best format.
  - Timeline in a sidebar pop-out: Easier to follow, tucked away beside the main view. When: When the time-based view is secondary to the table [inferred].
  - Timeline as a wider second column beside the table: Easier to follow and shown alongside the table. When: When there is room and the timeline deserves to be visible [inferred].
  - Recommendation: A timeline, in either placement, so the data drives the UI.
- How should color be used on a dashboard?
  - Decorative color sprinkled in to look nice: Sprinkled in to look nice rather than coming from the data. When: Landing pages can get away with this; dashboards should not.
  - Color that comes from the data: Color draws the eye to what matters, such as a red icon in a chip for an urgent action. When: Dashboards and data-heavy views.
  - Recommendation: Derive color from the data itself.
- How visible should a secondary action be (where does it sit on the spectrum of explicitness)? (`Q-pattern-03`)
  - Icon revealed on hover, with a tooltip: Low on the spectrum: saves space, and the action is revealed as soon as the user starts to look for it. When: Space is tight and the action is not a main one, such as removing a user from sharing or copying a cell.
  - Icon always visible: More explicit; the action is always on screen. When: When the action should be more explicit and space allows [inferred].
  - Always visible with a full text label: Still more explicit; the action is spelled out. When: When the action should be as explicit as possible [inferred].
  - Global, always-visible button: Quite high on the spectrum, like a global, always-visible share button. When: Main, frequently used actions [inferred].
  - Recommendation: For a secondary action with little space, reveal it on hover with a tooltip.
- Where should an infrequently used feature, like sharing, live? (`Q-pattern-03`)
  - Permanently in the side of the table: Permanently ingrained in the layout for something not frequently accessed or important enough. When: The source advises against it for infrequent features.
  - A separate page: Rips the user away to an entirely different page. When: The source advises against it here.
  - A popover: Available in context without leaving the page; its primary action sits at the top. When: The feature is not frequently accessed or important enough to be always visible.
  - Recommendation: A popover, because sharing is not frequently accessed and a popover avoids a page change.
- How should first-time users be introduced to the product? (`Q-pattern-04`)
  - A fully loaded dashboard with no guidance: Users stare at it wondering where to start. When: The source advises against it.
  - A modal explaining the whole product at login: Six bullet points that are forgotten the moment the modal is dismissed. When: The source advises against it.
  - Sequenced tooltips and a checklist: A single tooltip on the most important action, then a second one or a simple checklist in the corner; the user is never overwhelmed. When: Recommended onboarding approach.
  - Recommendation: Sequence features with tooltips and a simple checklist so the user is never overwhelmed.

### Process

1. Start from the data: Focus on the data the dashboard has to display and build the UI around it, so the data drives the form.
2. Shape each column to its data: Turn fixed-value columns into chips, right-align numbers, truncate long text and shade inactive or deactivated rows.
3. Question the container: If the data is split by time, consider a timeline in a sidebar pop-out or a second column instead of a time-sorted table.
4. Add meaning, not decoration: Use color that comes from the data (red for urgent), avatars for who did what, and a summary chart when the data has a time dimension.
5. Place actions on the spectrum of explicitness: Keep main actions visible, move infrequent features into popovers with the primary action at the top, and reveal secondary actions on hover with a tooltip.
6. Design the hidden UI: Add hover copy chips, comment indicators, tooltips for icons and ambiguous labels, and the hidden states of drawers and modals; plan announcements and onboarding pop-ups.
7. Sequence onboarding: Start with one tooltip on the most important action, then a second tooltip or a simple checklist in the corner.
8. Compare before and after: Put the original and revised versions side by side to see which is letting the data drive the form.
9. Study real software: Look at a lot of real software to get a feel for progressive disclosure, the spectrum of explicitness and onboarding flows (this advice leads into the sponsor read).

### Examples and visual references

- Table with department and employment status columns, before and after: The before is a logically laid out table where nothing drives the form; the after turns department and employment status into chips, right-aligns numbers, truncates long text and shades inactive rows.
- Time-sorted table turned into a timeline: Time-delineated records shown as a timeline, either tucked into a sidebar pop-out or as a wider second column beside the table.
- Activity log with meaningful color and avatars: A red icon in a chip flags an urgent action, avatars show who did what, and a chart rolls the log up into a summary over time.
- Card with poor versus strong hierarchy: Mentioned briefly as the usual way hierarchy is shown, before introducing hierarchy by showing and hiding.
- Share popover: Sharing opens in a popover from the table; a search box sits at the top as the primary action, and a remove button appears on hover with a tooltip.
- Swipe to reveal secondary actions (Apple Reminders): Swiping left and right reveals useful but secondary actions, while checking off a reminder stays the primary action.
- Ends of the spectrum of explicitness: A global, always-visible share button is high on the spectrum; an icon to copy a cell on hover is low.
- Visible versus hidden UI of a dense table: The video overlays everything visible and then all the hidden UI (copy chip over cells, comment triangle indicator, states); the hidden part is not a small amount.
- Onboarding with a single tooltip and a checklist: A first tooltip points at the most important action, followed by a second tooltip or a simple checklist in a corner, contrasted with a login modal of six bullet points.

### Numbers

- 3: Dashboard flaws covered: data driving the form, the right things hidden until needed, and the invisible UI that makes it function. [those are the three subtle flaws]
- six bullet points: The anti-pattern onboarding modal that explains the entire product at login. [a modal with six bullet points the second you log in]

<!-- /od:learn -->
