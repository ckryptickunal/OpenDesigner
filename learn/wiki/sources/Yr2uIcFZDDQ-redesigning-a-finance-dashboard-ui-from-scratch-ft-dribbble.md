---
type: source
title: Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)
created: 2026-09-27
updated: 2026-09-27
video_id: Yr2uIcFZDDQ
url: https://www.youtube.com/watch?v=Yr2uIcFZDDQ
channel: Kole Jain
published: 2024-06-29T21:15:00Z
authority: reference
tags:
  - dashboard
  - finance-dashboard
  - redesign
  - hierarchy
  - sidebar
  - grid-layout
  - data-visualization
  - charts
  - cards
  - priority
  - dribbble
  - kole-jain
---

# Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)

## Metadata

- Video ID: `Yr2uIcFZDDQ`
- Channel: Kole Jain
- Published: 2024-06-29T21:15:00Z
- URL: https://www.youtube.com/watch?v=Yr2uIcFZDDQ

## Summary

Kole Jain takes a finance dashboard shot from Dribbble that looks polished but makes little sense up close, and rebuilds it from the ground up. He starts with a hierarchy assessment: the big header is cut to essentials and moved into a collapsible sidebar, duplicate or pointless elements are removed, and related cards are merged, taking the original 12 cards down to a smaller set of meaningful modules. Each module is then fixed so its actions and content make sense for the object (no 'receive' button on a credit card, labels on unlabeled numbers, real alerts with amount, date and place) and given a priority tier. Finally the modules are placed on a grid with the most important information higher and farther left, choosing orientations that avoid awkward gaps and filling the remaining gap with a missing line-of-credit section shown as a pie chart. For a design system, it gives a repeatable dashboard process (audit, cut, merge, tier, place) and concrete chart and card rules.

## Key Ideas

- A design that looks amazing on Dribbble can fall apart once you check whether each element makes sense.
- Start a dashboard redesign with an assessment of the hierarchy, and expect to throw elements away.
- Do not let a large header push the important content below the fold; header items can move into a sidebar that also handles navigation.
- Remove duplicates and features that do not fit the product, such as a second search bar or text dictation in a finance dashboard.
- Important content should be visible as its own section, not hidden behind a button.
- Merge related cards: a growth rate and a chart belong in the annual profits card, and the system lock belongs with the credit card.
- Every action on a widget must make sense for the real object, so a credit card gets 'lock card', not 'receive' or 'direct deposit'.
- Numbers without labels mean nothing; charts need context.
- Showing a chart and growth percentages for the same data is repetitive; keep one.
- Rank each module into a priority tier as you design it, then place higher-priority modules higher and farther left on the grid.
- Keep margins consistent across modules even if a module shows fewer items, and add a way to view all.
- Choose the data representation carefully (two-sided bars for income and expenses, a pie chart for a line of credit), because it makes or breaks a dashboard.
- Pick module orientations that do not leave gaps that are hard to fill, and fill a remaining gap with a section the product actually lacks.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Creator of the video (a guy on YouTube with 1500 subscribers at the time, by his own joke) who critiques and redesigns the dashboard.
- [[entities/dribbble|Dribbble]] (product): Design showcase site where the original finance dashboard shot was found; used as an example of looks-good-but-makes-no-sense design.
- [[entities/wise|Wise]] (company): The caption says 'the wise card'; its card design is the inspiration for the credit card visual in the redesigned widget (identified as the company Wise [inferred]).
- [[entities/figma|Figma]] (tool): The redesign file is offered as a Figma file through the creator's resources page.
- [[entities/priority-tier-list|Priority tier list]] (concept): Ranking each dashboard module as high, mid-level or low priority to decide where it sits on the grid.
- [[entities/the-fold|The fold]] (concept): The point where content gets cut off on screen; the original header wasted space above it.
- [[entities/two-sided-bar-chart|Two-sided bar chart]] (concept): Bars going up for income and down for expenses, used to visualise money in and out.
- [[entities/kebab-icon|Kebab icon]] (concept): An icon added so the removed interest payment stays reachable for anyone who does care about it.

## Topics

- [[topics/dashboards-and-data-display|Dashboards and data display]]: A full finance dashboard redesign: cut and merge cards, add labels and context, pick chart types (percentage chips, two-sided bar chart, pie chart), and place modules on a priority grid.
- [[topics/visual-hierarchy|Visual hierarchy]]: Begins with a hierarchy assessment; important information goes higher and farther left, and each module is ranked high, mid-level or low priority.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Moves the header content into a sidebar: logo at the top, then the menu icon, the team, settings at the bottom, an add-widget button, and a collapsed state.
- [[topics/cards-and-sections|Cards and sections]]: Merges related cards, removes useless ones, keeps margins consistent across modules, and turns a tasks button into a full section.
- [[topics/spacing-and-layout|Spacing and layout]]: Treats the dashboard as a grid, chooses module orientations that avoid awkward gaps, and keeps margins consistent between modules.
- [[topics/design-process|Design process]]: A step-by-step redesign: assess hierarchy, cut the header, build the sidebar, audit and merge cards, fix each module, tier it, then assemble the grid.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Warns that Dribbble-style shots can look amazing but not make sense; every element and action should be checked for real meaning.
- [[topics/buttons-and-actions|Buttons and actions]]: Replaces actions that do not fit (receive, direct deposit) with lock card, adds all-tasks, add-reminder, compare and full-screen controls, and swaps a slider for a dropdown.
- [[topics/content-and-microcopy|Content and microcopy]]: Retitles cards, replaces a monthly fee with minimum payment and due date, adds labels to numbers, and drops a redundant 'financial dashboard' heading.
- [[topics/icons-and-imagery|Icons and imagery]]: Starts the fraud alert with an icon ('every good alert starts with this icon', shown on screen only), puts a full-screen icon on chart cards, a kebab icon for hidden detail, and an enlarged low-opacity logo on the card visual.

## Notable Claims

- Many Dribbble designs look amazing but do not make much sense once you zoom in. Evidence: in common dribble fashion it looks amazing but doesn't actually make that much sense
- The original layout wastes space at the top while the important content sits below the fold. Evidence: things are going to get cut off by the fold
- A dashboard does not need to announce that it is a financial dashboard, since that should be apparent. Evidence: we definitely don't need to announce that this is a financial dashboard
- Users should not have to click a button to see their tasks. Evidence: we shouldn't have to click on the button to see our tasks
- Of the original 12 cards, many were useless and several belonged inside other cards. Evidence: there are 12 cards or elements here and many of them look pretty useless
- You cannot really receive money with a credit card, so a receive or direct deposit button there makes no sense. Evidence: you can't really receive money with a credit card
- More important information should sit higher and farther left on a dashboard grid. Evidence: the more important information should be higher and farther left
- Chart numbers without labels do not mean anything. Evidence: without any labels these numbers don't mean anything
- Having a chart along with the growth percentages is repetitive. Evidence: having a chart like this along with the growth percentages is repetitive
- Curving data lines is bad and fading the data line is worse. Evidence: curving data lines like this bad and fading of the data line worse
- A decorative diagram and tiny-circle navigation in the activity card give no useful information or usable navigation. Evidence: it's a pretty diagram but entirely useless same with this navigation
- One module orientation leaves an awkward gap that is hard to fill, while the other does not. Evidence: we have two orientations but this one leaves an awkward Gap
- Data representation will make or break the UI and UX of a dashboard. Evidence: data representation people it'll make or break the UI and ux of your dashboard

## Quotes

> the more important information should be higher and farther left
> without any labels these numbers don't mean anything
> data representation people it'll make or break the UI and ux of your dashboard

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Self-promotion: the Figma file is offered through the creator's resources page, and the line chart changes are explained in an earlier video, so the reasons for 'no curved or faded data lines' are not given here.
- Caveat: Much of the critique is the creator's opinion and humor (jokes about Bill Gates and a placeholder user 'Dwayne Tatum'), not tested results.
- Caveat: The video states no exact values: no spacing, sizes, colors, grid columns or margins, only the relative priority placement.
- Caveat: The creator says 'modals' and 'models' when he means dashboard cards or modules, not overlay dialogs.
- Caveat: Auto-caption fixes made: 'dribble' read as Dribbble, 'log go' as logo, 'questioner' as questionnaire, 'Kabab' as kebab, and 'wise card' as the Wise card.
- Caveat: The first line-of-credit layout the creator considered is shown on screen but not described in the transcript.
- Caveat: The 'big red button' for all tasks is shown without any reasoning about color, and no accessibility points (contrast, focus, chart alternatives) are discussed.
- Caveat: Published 2024-06-29; auto-generated English transcript.

### Rules and practices

- **should** (process, all): Begin a dashboard design or redesign with an assessment of the hierarchy, and expect to toss elements that add no value in the process. Why: The source calls it the first order of business after seeing that the important content would sit below the fold while space at the top was wasted. [our first order of business is to do an assessment of the hierarchy]
- **should** (layout, desktop): Do not let a large header take up the space above the fold while the important content sits below it; move the header's essentials (logo, menu, team, settings) into a sidebar. Why: Scrolling is fine, but not with all the space at the top while the important content is at the bottom; a sidebar could also be handy for navigation. [I don't want all this space up here while the important is down at the bottom]
- **consider** (components, desktop): Order a dashboard sidebar with the logo at the very top, then the menu icon, then the team (with a manage-team button), with settings at the very bottom; put an add-widget button there too and give the sidebar a collapsed state. Why: This is the layout the source builds once the header is cut to essentials; the add-widget button is a good feature that was in an awkward spot. [log go at the very top followed by the menu icon then we'll put our team next and the settings all the way at the bottom]
- **consider** (content, all): Do not label a dashboard with what it obviously is, such as a 'financial dashboard' heading. Why: That should be apparent from the content itself. [we definitely don't need to announce that this is a financial dashboard]
- **should** (components, all): Remove controls that duplicate each other, such as two search bars that do the same thing, and features that do not fit the product, such as text dictation in a finance dashboard. Why: The two search bars look like they do exactly the same thing, and the source cannot recall seeing a finance dashboard with a text dictation option. [we have two search bars that look like they do exactly the same thing]
- **should** (patterns, all): Show content people need regularly, such as tasks, as its own dashboard section instead of hiding it behind a button. Why: People should not have to click a button to see their tasks; the tasks module became the call to action. [we shouldn't have to click on the button to see our tasks]
- **should** (layout, all): Merge small or related cards into the card they belong to, for example the growth rate and a separate chart into the annual profits card, and the system lock into the credit card information. Why: Many of the 12 cards looked pretty useless on their own; integrating the system lock with the credit card lets you lock the card online. [the growth rate should definitely be part of the annual profits card]
- **should** (components, all): Give each widget only the actions that make sense for the real object it represents, for example 'lock card' on a credit card instead of 'receive' or 'direct deposit'. Why: You cannot really receive money with a credit card, so those buttons make the design nonsensical. [you can't really receive money with a credit card]
- **should** (layout, all): Place dashboard modules on a grid so that the more important information is higher and farther left. Why: Placement should follow importance. [think about this as a grid where the more important information should be higher and farther left]
- **should** (process, all): Rank every module into a priority tier (high, mid-level or low) as you design it, then place high-priority modules first, mid-level next and low-priority modules at the bottom. Why: The tier list decides the layout; frequent, day-to-day functions rank high and things you rarely need to access rank low. [let's just try ranking the importance of the modals as we make them think about this as our tier list]
- **must** (components, all): Label every chart and number so the values have context. Why: Without labels the numbers do not mean anything. [without any labels these numbers don't mean anything]
- **should** (components, all): Do not show a chart and growth percentages for the same data; keep one, such as percentage chips for each level. Why: Having both is repetitive. [having a chart like this along with the growth percentages is repetitive]
- **should** (components, all): Do not curve the data line in a line chart, and do not fade the data line. Why: The source calls curved data lines bad and a fading data line worse. [curving data lines like this bad and fading of the data line worse]
- **consider** (components, all): Give line chart cards grid lines, a time scale selector, a compare button when there may be several portfolios, and an icon that opens a full-screen version of the chart. Why: These are the additions made to the investment chart; compare covers multiple portfolios, and the full-screen icon also goes on the revenue and expenses card. [added some grid lines and a time scale selector]
- **should** (content, all): Replace decorative diagrams and tiny dot navigation that carry no meaning with content that has real context, such as an alert showing amount, date and place. Why: A pretty but useless diagram and tiny circles nobody would click give the user nothing. [it's a pretty diagram but entirely useless]
- **consider** (components, all): Start an alert card with a leading icon, then give the amount, the date and the place of the transaction. Why: The source says every good alert starts with this icon (which icon is shown on screen only), and the amount, date and place make the alert make sense. [every good alert starts with this icon]
- **should** (layout, all): Keep margins consistent across dashboard modules, even if a module then shows fewer items (two reminder cards instead of four), and add filters plus a button to view all items and one to add a new item. Why: Consistency with the other modules' margins wins over fitting more; the view-all button covers the hidden items. Values: four, two. [in keeping with the margins from the other models we'll do two cards and add some filters]
- **consider** (components, all): Give money-in and money-out data a visual, such as a two-sided bar chart with income bars extending upwards and expense bars extending downwards. Why: The income and expenses card had important information but basically no visuals to represent the data. [a two-sided bar chart with the bars that extend upwards representing income]
- **should** (layout, all): When a module can go in more than one orientation, choose the one that does not leave an awkward gap that is hard to fill. Why: One orientation left a gap that would be difficult to fill with something, while the other did not. [this one leaves an awkward Gap that will be difficult to fill]
- **consider** (components, all): Keep a secondary detail you cut from a card reachable behind a kebab icon, instead of deleting it entirely. Why: Few people care about it (interest payment), but it stays available just in case someone does. [add this Kabab icon just in case someone actually does care about it]
- **consider** (components, all): Replace an unclear icon, such as a minimize icon on a large module, with a labelled button like 'all activities'. Why: The source is not sure how the module could be made much smaller, so a minimize icon does not fit it. [replace that with an all activities button instead]
- **consider** (content, all): Retitle a card when its content changes so the title matches what it now shows, for example 'Revenue and expenses' for the income and expenses card. Why: After the credit card changes the source says the card needs a better title. [we need to retitle the card to something better]
- **consider** (content, all): Show the figures that matter for the real object, for example a minimum payment and a due date on a credit card instead of a monthly fee. Why: Part of making the credit card widget make sense once zoomed in. [replace the monthly fee with a minimum payment and add the due date]
- **consider** (components, all): When a widget can hold more than one item, such as more than one credit card, add a way to scroll to the others. Why: So more than one card can be added to the dashboard. [add a way for us to scroll to more cards]
- **consider** (components, all): Keep a good diagram that lacks context, but give it the missing data, for example turning the business plan diagram into a bank loan approval with the loan amount and repayment date. Why: The card was missing too much context to make sense, but the diagram itself was worth keeping. Values: 90°. [we're once again missing too much context to make sense of what this is]
- **consider** (components, all): Adjust a component brought in from elsewhere to match the dashboard's theme, for example a dropdown instead of a slider for the time scale. Why: The source makes these minor tweaks to match the theme of the dashboard a little better. [in an effort to match the theme of the dashboard a little better]
- **consider** (process, all): Cut elements that are not necessary or give no real value, such as the header date or a bulky questionnaire card, and add them back later only if there is room or a way to work them in. Why: The date is not entirely necessary and the questionnaire is bulky and provides no real value. [this questioner at the bottom is bulky and provides no real value to us]
- **consider** (layout, all): Fill a remaining gap in the dashboard grid with a section the product actually lacks, such as a line of credit section in a finance dashboard. Why: The dashboard was clearly lacking a line of credit section, and it slotted perfectly into the empty space. [it's clearly lacking some sort of line of credit section]
- **should** (components, all): Choose each dashboard module's data representation deliberately, and try another form when the first layout is weak, as with switching the line of credit to a pie chart. Why: The source says data representation will make or break the UI and UX of a dashboard. [data representation people it'll make or break the UI and ux of your dashboard]

### Decisions it informs

- Where should the dashboard's header content and navigation live? (`Q-layout-04`)
  - Top header bar: Takes up space above the fold and pushes the important content down (the original design). When: The source does not recommend it for this dashboard.
  - Sidebar, collapsible: Frees all the space at the top; holds logo, menu icon, team, add-widget button and settings at the bottom, and can collapse. When: Dashboards where the header crowds out important content.
  - Recommendation: Move the header into a sidebar, which also helps navigation and opens up the space at the top.
- How should modules be arranged on the dashboard?
  - Priority grid: High-priority modules go top left, mid-level next, low-priority at the bottom, so the most used information is seen first. When: Any dashboard; the source ranks each module as it designs it.
  - Original arrangement: A big header on top and important content cut off below the fold. When: Not recommended by the source.
  - Recommendation: Use a priority grid where more important information is higher and farther left.
- How should growth over time be shown in a profits card?
  - Chart plus growth percentages: Shows the same information twice. When: The source calls this repetitive.
  - Percentage chips for every level: Growth is shown compactly as chips next to each value, with no extra chart. When: When a chart would only repeat the percentages.
  - Recommendation: Drop the chart and use percentage chips, because having both is repetitive.
- How should the data line in a line chart be drawn?
  - Curved data line: The source calls it bad. When: Not recommended.
  - Faded data line: The source calls it worse than curving. When: Not recommended.
  - Line without curving or fading, with grid lines and a time scale selector: The redesigned chart from the creator's earlier video. When: The source's redesign.
  - Recommendation: Avoid curving and fading the data line; add grid lines and a time scale selector.
- What control should pick a chart's time scale?
  - Slider: Used in the earlier standalone chart redesign. When: Not stated in the source.
  - Dropdown: Matches the theme of the rest of the dashboard better. When: When the chart sits inside this dashboard.
  - Recommendation: A dropdown, to match the theme of the dashboard a little better.
- Should tasks sit behind a button or in their own module?
  - Button: People have to click before they can see their tasks. When: The source says they should not have to.
  - Wide, thin tasks module: Shows reminder cards with filters, a big red button to view all tasks and a button beside it to add a reminder. When: When tasks are the main call to action; ranked high priority.
  - Recommendation: Turn the button into a full module, since this was the dashboard's call to action.
- How should income and expenses be represented? (`Q-viz-01`)
  - Numbers only: Important information with basically no visuals to represent the data. When: The source replaces it.
  - Two-sided bar chart: Bars extend upwards for income and downwards for expenses, with the dollar values and a full-screen icon. When: Showing money coming in and going out.
  - Recommendation: A two-sided bar chart, which the source thinks is the best way to represent money coming in and out.
- How should a line of credit be shown? (`Q-viz-01`)
  - The first layout the creator considered: Shown briefly on screen; not described in the transcript. When: Abandoned by the source.
  - Pie chart: Fills the empty space in the grid, with the interest payment moved behind a kebab icon. When: The source's final choice.
  - Recommendation: A pie chart; the source stresses that data representation makes or breaks a dashboard.

### Process

1. Assess the hierarchy: Split the screen into the header and everything else, and check what gets cut off by the fold.
2. Cut the header to essentials: Remove redundant titles, duplicate search bars and features that do not fit, and pull hidden content (tasks) out of buttons.
3. Build the sidebar: Logo at the very top, then the menu icon, then the team with a manage-team button, an add-widget button, and settings at the bottom; design a collapsed version.
4. Audit the cards: Count the cards (12 in the original), remove the useless ones and merge related ones into the cards they belong to.
5. Fix each module: Make actions fit the real object, add labels and context, and replace decorative diagrams with meaningful content such as alerts or loan approvals.
6. Tier each module: As you finish each module, rank it high, mid-level or low priority; day-to-day activity and calls to action rank high, rarely accessed views rank low.
7. Assemble the grid: Place high-priority modules first with the most important at the top left, choose orientations that avoid awkward gaps, then add the mid-level and low-priority modules.
8. Fill the gaps with what is missing: Use any remaining gap for a section the product lacks (a line of credit here), and choose its data representation carefully.

### Examples and visual references

- Original finance management dashboard (Dribbble): A large header with a 'financial dashboard' title, two search bars, a dictation option and a date, above 12 cards; several are decorative (a diagram with tiny dot navigation), unclear (a '13 Days' card) or belong inside other cards, and important content falls below the fold.
- Collapsible sidebar: Logo at top, menu icon, team avatars with a manage-team button, an add-widget button and settings at the bottom, with a collapsed variant.
- Credit card widget (Card visual inspired by Wise): A real-looking card showing the card number, in the brand colors, with the logo blown up at reduced opacity; 'lock card' replaces direct deposit and receive, minimum payment and due date replace the monthly fee, and a control scrolls to more cards.
- Annual profits card: The separate chart is dropped and percentage chips show growth for every level; the numbers get labels for context.
- Investment line chart card: Grid lines, a dropdown time scale selector instead of a slider, a compare button for multiple portfolios and a full-screen icon.
- Activity manager with fraud alert: The minimize icon becomes an 'all activities' button, wallet verification stays, and a decorative diagram with tiny dot navigation becomes a fraudulent activity alert with a leading icon, amount, date and place.
- Bank loan approval: The original business plan diagram is flipped 90° and recolored, with the loan amount and repayment date added.
- Tasks module: Wide and thin, two reminder cards with filters, a big red button to view all tasks and an add-reminder button beside it.
- Revenue and expenses card: A two-sided bar chart at the bottom of the card, income bars going up and expense bars going down, with the dollar values and a full-screen icon.
- Line of credit card: A pie chart that fills the leftover gap in the grid, with the interest payment removed from view and reachable from a kebab icon.

### Numbers

- 12: Number of cards or elements in the original dashboard before the cut. [there are 12 cards or elements here]
- 90°: The business plan diagram is rotated this much to become the bank loan approval visual. [I'm going to flip this 90°]
- two: Reminder cards shown in the tasks module, down from the four originally planned, to keep margins consistent with other modules. [we'll do two cards and add some filters too]
- four: Reminders the creator first planned for the tasks module before cutting it to two to keep margins consistent. [I was originally thinking we could fit four reminders in here]

<!-- /od:learn -->
