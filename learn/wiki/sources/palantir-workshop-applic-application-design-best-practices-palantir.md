---
type: source
title: Palantir
created: 2026-10-13
updated: 2026-10-13
video_id: palantir-workshop-applic-application-design-best-practices
url: https://www.palantir.com/docs/foundry/workshop/application-design-best-practices
channel: "Palantir Workshop: application design best practices (web)"
published: Unknown
authority: reference
tags:
  - enterprise
  - work-tools
  - dashboards
  - layout
  - visual-hierarchy
  - density
  - navigation
  - overlays
  - internal-tools
  - consistency
---

# Palantir

## Metadata

- Page ID: `palantir-workshop-applic-application-design-best-practices`
- Publisher: Palantir Workshop: application design best practices (web)
- Published: Unknown
- URL: https://www.palantir.com/docs/foundry/workshop/application-design-best-practices

## Summary

Palantir's documentation for Workshop, its builder for internal operational applications, sets out how to lay out a work tool so that people can carry out workflows efficiently. It has two core principles: component clarity over complexity, and one unified, consistent experience across every application in a suite. It then gives concrete limits and patterns: no more than five primary actions in the top navigation, no more than ten visible components in a view, 30 to 40 percent whitespace, layouts that follow an F-shaped reading pattern with filters anchored on the left, three levels of headings, padding between groups and dividers inside them, one elevated area per page, navigation pinned in a header that does not scroll, and overlays only for short secondary tasks. For a design system this is a clear statement of the enterprise side: attention and efficiency come first, nothing in it is about delight, and it never mentions animation.

## Key Ideas

- The interface exists to guide a user's actions and keep their attention so workflows are efficient, effective and logical.
- Clarity of components matters more than complexity; a clear interface is what gets an application adopted.
- Two separate failure modes: overloaded (too many actionable items) and overcrowded (too many components, too little whitespace).
- Layout follows the F-shaped reading pattern: scan across the top from the left corner, then down the left side.
- Filters and configuration sit on the left and content flows to the right; summary metric cards sit on top.
- Headings come in three levels with one job each: page purpose, section grouping, short description.
- Space separates groups; dividers separate related content inside a group. Too many nested containers add clutter.
- Elevation is a signal of importance and is used once per page, on the area where users act.
- Lighter backgrounds mark important areas; darker ones mark less critical areas such as filters and collapsible panels.
- A suite feels unified when the home page centralises navigation, the header keeps logo and global settings in the same corners, and high-use components sit in the same place everywhere.
- Navigation and tabs are pinned in the header; only content sections scroll.
- Overlays are for temporary, secondary interactions, never for analysis that needs several layers of information in view.
- Every element should have to earn being visible where it is; otherwise show it only when the user needs to act on it.
- Squinting at the screen is a quick test of whether the hierarchy works.

## Entities

- [[entities/palantir|Palantir]] (company): Publisher of the guidance; maker of Foundry and Workshop.
- [[entities/palantir-foundry|Palantir Foundry]] (product): The enterprise data platform Workshop belongs to; its default font is Source Sans Pro.
- [[entities/workshop|Workshop]] (tool): Foundry's application builder for operational, internal applications; the guidance is written for people building in it.
- [[entities/f-shaped-pattern|F-shaped pattern]] (concept): The reading pattern the layout guidance is built on: horizontal scanning from the top left, then vertical scanning down the left side.
- [[entities/metric-card|Metric Card]] (concept): A Workshop widget for a single key number, recommended for a holistic view of key data at the top of an application.
- [[entities/object-table|Object Table]] (concept): Workshop's data table widget; 'Fit columns horizontally' is the recommended way to avoid sideways scrolling.
- [[entities/source-sans-pro|Source Sans Pro]] (product): The default Foundry typeface, used when no other is selected and as the fallback for a missing custom font.

## Topics

- [[topics/visual-hierarchy|Visual hierarchy]]: Hierarchy should draw attention to the right areas of interaction. Avoid overload (limit actionable items; at most five primary actions in top navigation) and overcrowding (30 to 40 percent whitespace; at most ten visible components). Check it by squinting.
- [[topics/spacing-and-layout|Spacing and layout]]: Use grid, column, or row-and-column layouts that follow the F-shaped reading pattern, with filters anchored on the left. Use compact padding in most cases; separate groups with padding and containers, and related content with dividers; do not over-nest containers.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: Work-tool layouts: metric cards for key numbers across the top, a filter panel on the left, an object table that fits its columns to the width, and a list, table and detail panel side by side.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: A drop shadow signals that content is important and an inner shadow that it is less so; lighter backgrounds signal importance and darker ones less critical areas. Apply the elevated or shaded style once per page, on the main content or primary dialog.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: At most five primary actions in top-level navigation; a home page that centralises navigation to all modules; navigation bars and tabs pinned inside the primary header so they never scroll away.
- [[topics/modals-and-popovers|Modals and popovers]]: Overlays suit temporary, secondary interactions such as a questionnaire. Avoid them for analysis. A dialog blocks the background, so reference text needed while typing must sit beside the inputs or be repeated.
- [[topics/typography|Typography]]: The page header is the largest text and states the purpose; section headers are second largest; subheadings are descriptions. In Workshop, prefer a system font over a custom typeface because custom fonts cannot be uploaded and only render if installed on the viewer's device.
- [[topics/content-and-microcopy|Content and microcopy]]: Headings and their descriptions should be succinct and help a new user understand what the section is for.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: A unified suite standardises where high-use components go and applies the same styles to tabs, metric cards, headers and buttons across every application.
- [[topics/saas-product-ui|SaaS product UI]]: The whole page describes internal, operational work tools: dense tables, filter panels, status tags and detail panels built for efficient workflows.
- [[topics/accessibility|Accessibility]]: Avoid horizontal scrolling where possible, and keep touch targets inside scrolling sections at least 30px.
- [[topics/design-process|Design process]]: Validate as you build: squint to test hierarchy, stay close to real user workflows, and ask of every element whether it must be visible where it is.

## Notable Claims

- A well-designed interface guides a user's actions and maintains their attention so they can execute workflows efficiently, effectively and logically. Evidence: Application design best practices: 'guides a user's actions and maintains their attention'
- Designs without a clear, logical visual hierarchy that are overloaded or overcrowded confuse users, block adoption and limit the application's usefulness. Evidence: Create intuitive user interfaces: 'can confuse users, blocking their application adoption'
- Users scan content in an F shape: horizontally from the top-left corner, then vertically down the left side of a section. Evidence: Configure a logical layout structure: 'a user will scan content following an "F" shape'
- Properly spaced and aligned sections enhance readability, reduce cognitive load and create logical visual connections between related elements. Evidence: Set section spacing and alignment: 'enhance user readability, reduce cognitive load'
- A dialog prevents users from scrolling or interacting with background content. Evidence: Overlay usage best practices: 'A dialog prevents users from scrolling'
- System fonts render consistently because they are present on most devices; a custom typeface in Workshop renders only if it is installed on the viewer's device. Evidence: Set module typography: 'These render consistently because they are present on most devices'

## Quotes

> prioritize component clarity over complexity

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Enterprise focus: this is vendor documentation for people building internal, operational applications in Palantir Workshop. Its limits (ten components, five navigation actions, 30 to 40 percent whitespace, compact padding) are for desktop work tools and should not be carried over to consumer apps as they stand. The 'product' tag on each rule is this analysis's judgement: rules that depend on dense, data-heavy work screens are tagged enterprise; general hierarchy, grouping and overlay rules are tagged both.
- Caveat: Tool-specific: several instructions are about Workshop's own settings (Compact padding, the Section header toggle, Fit columns horizontally, Module Appearance typography). The font advice follows from a Workshop limit (no custom font upload) and is not general typography advice.
- Caveat: The numbers are stated without evidence or citations. Under OpenDesigner's rules a number from a single reference source is a proposal until another source or the existing research agrees.
- Caveat: The page says nothing about animation, delight, empty states or error messages; its silence on them is not a rule against them.
- Caveat: The 30px touch target is above OpenDesigner's locked 24px floor, so there is no conflict.
- Caveat: The over-nesting rule and its reason come from the text inside a Do and Don't figure, read from the image, not from the page's body text. Six of the page's twelve figures were looked at; the other six are screenshots of Workshop's settings panels.

### Rules and practices

- **should** (process, all, enterprise products): Prioritise component clarity over complexity when building a work tool. Why: An intuitive interface is what gets the application adopted. [Core design principles: 'prioritize component clarity over complexity']
- **should** (layout, all, both products): Limit the total number of actionable items per screen, such as tasks, notifications and choices. Why: Too many actionable items overload the user and confuse them. [Create intuitive user interfaces: 'To avoid overload, limit the amount of total actionable items']
- **should** (patterns, all, enterprise products): Do not show more than five primary actions in the application's top-level navigation. Why: It avoids overloading the user. Values: five. [Create intuitive user interfaces: 'avoid showing more than five primary actions']
- **should** (layout, all, enterprise products): Maintain sufficient whitespace; ideally it makes up 30 to 40 percent of the screen. Why: It avoids overcrowding. Values: 30 to 40 percent. [Create intuitive user interfaces: 'To avoid overcrowding, maintain sufficient whitespace']
- **should** (layout, all, enterprise products): Limit the number of visible components to no more than ten in a single view, counting buttons, panels and widgets. Why: It avoids overcrowding. Values: ten. [Create intuitive user interfaces: 'limit the number of visible components to no more than ten in a single view']
- **should** (layout, all, enterprise products): Lay the application out along the F-shaped reading pattern, and clearly separate configuration sections from content sections. Why: It supports natural eye tracking: users scan across the top from the left corner, then down the left side. [Configure a logical layout structure: 'following an F-shaped hierarchical design pattern']
- **should** (layout, all, enterprise products): In a row and column combination layout, anchor filters in the left-most section so the application's content flows to the right. Why: It facilitates natural reading patterns and linear eye tracking. [Configure a logical layout structure: 'Row and column combination: Anchor filters in the left-most section']
- **consider** (components, all, enterprise products): Use metric cards to give a holistic view of the key data in the application. Why: They summarise the key numbers at a glance. [Configure a logical layout structure: 'Use the Metric Card widget']
- **should** (typography, all, both products): Use three heading levels with one job each: a page header (the largest text) for the application's purpose, section headers (second largest) to group nested content, and subheadings as short descriptions where needed. Why: All other content should relate to the primary heading, and the levels organise what is nested under them. [Write descriptive headers: 'Use a page header to establish your application's overarching purpose']
- **should** (content, all, both products): Write heading descriptions that are succinct and tell a new user what the section is for. Why: A new user should understand the purpose of each section. [Write descriptive headers: 'succinct and help a new user understand the purpose']
- **should** (layout, all, enterprise products): Use compact padding in most cases in a work tool. Why: The source gives this as the default without a stated reason. Values: Compact, 80 percent height or width, 16px spacing. [Set section spacing and alignment: 'In most cases, you should use Compact padding']
- **should** (layout, all, both products): Separate distinct content groups with containers and padding between them, and use dividers only to separate related content inside a section. Do not rely on dividers alone to separate groups. Why: Padding between groups helps the user understand the separation. [Set section spacing and alignment: 'use containers to separate distinct content groups across sections and dividers to separate related content']
- **consider** (layout, all, both products): Do not over-nest section containers (stated only in the page's Do and Don't figure, not in its body text). Why: Too many containers clutter the view and impede legibility (stated in the page's Do and Don't figure). [Set section spacing and alignment: figure 'A Do and Do not comparison shows when to use padding and dividers within a section']
- **should** (elevation, all, both products): Use a drop shadow on a bordered section to signal that its content is important, and an inner shadow to signal lesser importance. Why: Elevation highlights important sections and creates spatial separation. [Apply border and elevation styles: 'you should use a drop shadow to provide an elevated appearance']
- **should** (color, all, enterprise products): Use lighter background colors for important areas and darker ones for less critical areas such as filters or collapsible panels. Why: Background lightness signals importance. [Apply border and elevation styles: 'use lighter colors to signify importance']
- **should** (elevation, all, both products): Apply the shaded or elevated style only once per page, on the main content or the primary dialog where users take action. Why: It keeps the visual hierarchy, so users can tell which element is the most important. Values: once per page. [Apply border and elevation styles: 'only apply shaded padding styles once per page']
- **should** (patterns, all, enterprise products): In a suite of applications, make the landing page centralise all navigation and give an overview of the modules with thumbnails. Why: Users can take quick action to reach exactly what they need. [Build unified applications: 'The landing or homepage centralizes all navigation activity']
- **should** (patterns, all, enterprise products): Keep one primary header across all modules, with the logo in the top-left corner and global settings in the top-right. Why: It keeps logo design and global settings control consistent across the suite. Values: top-left, top-right. [Build unified applications: 'A primary header maintains consistent logo design and global settings control']
- **should** (tokens, all, both products): Standardise where high-touch components go (for example, filters on the left side of the page) and apply the same styles to tabs, metric cards, headers and buttons everywhere. Why: Users should feel they are working within one unified suite of tools. [Build unified applications: 'Standardized layout elements ensure high-touch user components follow a consistent layout']
- **should** (layout, all, both products): Avoid horizontal scrolling wherever possible; fit table columns to the available width instead. Why: The source states this as a best practice without a reason. [Scrolling best practices: 'Avoid horizontal scrolling whenever possible']
- **should** (patterns, all, both products): Put navigation bars and tabs inside the primary header so that only content sections scroll. Why: It pins navigation and tabs in the user's view. [Scrolling best practices: 'This acts as a pinning mechanism']
- **should** (accessibility, all, enterprise products): Inside a scrolling section, make every touch target, such as a button, at least 30px. Why: The source states this as a best practice without a reason. Values: 30px. [Scrolling best practices: 'are at least 30px']
- **should** (patterns, all, both products): Use overlays for temporary and secondary interactions, such as completing a questionnaire. Why: Overlays suit short tasks that sit on top of the main work. [Overlay usage best practices: 'Use overlays for temporary and secondary interactions']
- **should** (patterns, all, enterprise products): Do not put analytical sections in overlays. Why: In analysis, users need to view several layers of information at the same time. [Overlay usage best practices: 'Avoid overlays for analytical sections']
- **should** (patterns, all, enterprise products): Design overlay workflows for users who select objects first and then perform one or several actions on them. Why: That is the order in which users work with objects. [Overlay usage best practices: 'account for users selecting objects before performing one or multiple actions']
- **should** (patterns, all, both products): If users must refer to long text while entering data, place the inputs beside the content or repeat the needed content in a non-blocking area, not in a dialog over it. Why: A dialog prevents users from scrolling or interacting with the background content. [Overlay usage best practices: 'place the inputs beside the content']
- **should** (tooling, all, enterprise products): In Workshop, prefer a system font over a custom typeface. Why: A custom font cannot be uploaded and renders only if installed on the viewer's device, so it may look different for different users. Values: Source Sans Pro, Arial, Georgia, Helvetica, Times New Roman, Verdana. [Set module typography: 'prefer a system font over a custom typeface']
- **should** (process, all, both products): Squint at the interface from time to time to see which elements stand out. Why: It shows whether the hierarchy matches the intended importance of each element. [Validate your design: 'Periodically squint at your interface']
- **should** (process, all, both products): Stay closely aligned with actual user workflows while designing. Why: You keep an understanding of what users want to accomplish in each section. [Validate your design: 'Stay closely aligned with actual user workflows']
- **should** (layout, all, both products): For every element, check whether it must be visible where it is. If not, show it only when the user needs to interact with it. Why: Elements that do not need to be visible add to overload and overcrowding [inferred]. [Validate your design: 'Validate whether or not every element must be visible from its current location']

### Decisions it informs

- How much should fit on one screen of a work tool? (`Q-dir-02`) (enterprise products)
  - Within the limits: At most ten visible components, 30 to 40 percent whitespace, compact padding; the screen reads as ordered and the main area stands out. When: The source's recommendation.
  - Overloaded: Many competing actions: several colored buttons and repeated action rows fight for attention. When: The source treats this as a failure.
  - Overcrowded: Panels, tables and scrollbars packed edge to edge with almost no whitespace. When: The source treats this as a failure.
  - Recommendation: Compact padding, but capped: no more than ten components in view and 30 to 40 percent whitespace.
- Which layout pattern should an application screen use? (enterprise products)
  - Grid: Information flows horizontally from left to right. When: Not stated.
  - Columns: Information flows vertically, with important navigation elements at the top of each panel. When: Not stated.
  - Rows and columns combined: Filters are anchored in the left-most section and content flows to the right, with metric cards for key data. When: Not stated; it is the pattern the page describes in most detail.
  - Recommendation: Any of the three, as long as it follows the F-shaped reading pattern.
- Should related things be separated by space, containers or lines? (`Q-dir-04`) (both products)
  - Padding and containers between groups: Each group is its own block with clear space around it. When: Between distinct content groups.
  - Dividers: A thin line splits content that belongs together. When: Inside a section, between related content.
  - Dividers only, or containers inside containers: Groups run together, or the view fills with boxes and becomes harder to read. When: The source's figures mark both as Don't.
  - Recommendation: Padding between groups, dividers within them, and as few nested containers as clarity needs.
- How should the most important area of a page stand out? (`Q-depth-01`) (both products)
  - Drop shadow: The area looks raised and reads as important. When: Once per page, on the main content or the primary dialog.
  - Inner shadow: The area looks recessed and reads as less important. When: For lesser content.
  - Background lightness: Lighter areas read as important; darker areas read as secondary. When: Darker for filters and collapsible panels.
  - Recommendation: One elevated area per page, where the user takes action.
- When should a task open in an overlay? (`Q-pattern-01`) (enterprise products)
  - Overlay: Sits on top of the page; a dialog blocks scrolling and interaction with what is behind it. When: Temporary, secondary interactions such as a questionnaire.
  - In the page: Inputs sit beside the content, or analysis panels sit side by side, so several things stay visible at once. When: Analysis, or data entry that needs reference text.
  - Recommendation: Overlays only for short secondary tasks; keep analysis and reference-heavy entry in the page.

### Process

1. Squint test: Periodically squint at the interface; what still stands out should be the most important elements for the intended use.
2. Stay with real workflows: Keep checking each section against what users actually want to accomplish there.
3. Visibility check: For every element, ask whether it must be visible where it is; if not, surface it only when the user needs to act on it.

### Examples and visual references

- Overloaded versus overcrowded screens (Palantir's diagram, under 'Create intuitive user interfaces'): Two laptop wireframes side by side. 'Overloaded' has red, orange, green, purple and blue buttons spread over three rows of actions, so nothing leads. 'Overcrowded' has a sidebar, a second column of controls, two large panels and two tables with their own scrollbars packed together with almost no space between them.
- Row-and-column layout (Palantir's example application, under 'Configure a logical layout structure'): A header with the title, three tabs and a search box. Below it a 'Filters' panel on the left with a two-way toggle and checkbox lists that carry counts and small bars. To the right, four metric cards in a row above a wide seven-column table. A small diagram beside it draws one arrow down the left and three arrows running right.
- Padding between groups: Do and Don't (Palantir's figure, under 'Set section spacing and alignment'): Do: three titled white cards stacked on a pale gray background with a clear gap between them. Don't: the same three groups in one continuous white block, split only by thin lines, so they read as one thing.
- Over-nested containers: Do and Don't (Palantir's figure, under 'Set section spacing and alignment'): Do: a section title on the page background, then a card split into two labelled halves by a single divider, then a second card. Don't: the title, each section and each labelled block all get their own bordered box, three levels deep, and the content ends up smaller inside rings of borders.
- Sample Claims Dashboard (Palantir's sample Workshop application): Three areas side by side: a narrow left list of four group cards, each with four counts (Unreviewed, Escalated, Pending, Resolved), the selected one outlined in blue; a table of claims with checkboxes, linked titles and small outlined status tags ('Not reviewed' gray, 'Resolved' green, 'Escalated' orange); and a detail panel for the selected claim with labelled fields, comments, and two full-width buttons pinned at the bottom, a plain 'Escalate' and a solid green 'Resolve'. Only the table-and-detail block is raised on a white card with a soft shadow; the page behind is pale gray. Dense, quiet, one accent per meaning.
- Primary header with scrolling content (Palantir's diagram, under 'Scrolling best practices'): A colored bar with the logo and a row of tabs beneath it are bracketed together as 'Primary header'. Everything below is bracketed as 'Scrollable content' with an up-and-down arrow, showing that the header and tabs stay put while only the content moves.

### Numbers

- five: Most primary actions to show in top-level navigation [Create intuitive user interfaces]
- 30 to 40 percent: Ideal share of the screen left as whitespace [Create intuitive user interfaces]
- ten: Most visible components in a single view, counting buttons, panels and widgets [Create intuitive user interfaces]
- 80 percent: Height or width for a reliable custom padding setting in Workshop, used with 16px spacing [Set section spacing and alignment]
- 16px: Spacing for the reliable custom padding setting in Workshop [Set section spacing and alignment]
- 30px: Smallest touch target inside a scrolling section [Scrolling best practices]
- once per page: How often to apply the shaded or elevated style [Apply border and elevation styles]

<!-- /od:learn -->
