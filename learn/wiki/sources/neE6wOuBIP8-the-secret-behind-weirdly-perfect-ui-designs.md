---
type: source
title: The secret behind weirdly perfect UI designs
created: 2026-09-27
updated: 2026-09-27
video_id: neE6wOuBIP8
url: https://www.youtube.com/watch?v=neE6wOuBIP8
channel: Kole Jain
published: 2026-09-20T15:45:15Z
authority: reference
tags:
  - layout
  - alignment
  - edges
  - scannability
  - visual-hierarchy
  - emphasis
  - density
  - cards
  - icons
  - chips
  - checklist
  - checkbox
---

# The secret behind weirdly perfect UI designs

## Metadata

- Video ID: `neE6wOuBIP8`
- Channel: Kole Jain
- Published: 2026-09-20T15:45:15Z
- URL: https://www.youtube.com/watch?v=neE6wOuBIP8

## Summary

Kole Jain uses a store receipt and a checklist UI to explain why some interfaces feel 'weirdly perfect': they are built to be scanned, not read. He argues that layout works through edges: every card gives four edges, elements in compact UIs should sit against at least two, and new edges can be manufactured when content has nowhere to stack. He then shows that a dense list is fixed by differentiating content (avatars, grouping by due date, chips, blue underlined links, icons and diagrams) rather than by adding white space, labels or tooltips. Emphasis, he says, comes from the difference between an element and its neighbours, so default values should be gray and only the thing that matters gets color. Finally, he shows that cards are optional: a single line and a column edge can do the job of card borders without stacking borders and radii. For a design system, this gives concrete layout, hierarchy and emphasis rules plus a repeatable review process for any screen.

## Key Ideas

- People do not read screens: they arrive with a question and hunt for the answer, so interfaces should be optimised for scanning.
- Alignment to shared edges holds a layout together; a receipt works with text hard left, prices hard right and no dividers.
- Every card offers four edges, and elements such as an avatar and name create extra edges that more content can stack onto.
- In compact UIs (chat inputs, Kanban cards, sidebars, checklists) nearly every element borders two or more edges.
- When content lacks an edge, manufacture one (move an edge down, add a subline) instead of hiding elements in a menu.
- Density is not the problem; undifferentiated content is. Avatars and grouping make a dense list fast to search.
- Adding white space to counter density helps a little but makes everything longer.
- Immediately recognisable visuals (icons, diagrams, chips, blue underlined links, a stop-sign shape) let people understand without reading.
- Explaining harder with comparisons, labels and tooltips adds information but makes the screen harder to read.
- Placement can carry meaning, as with a checkbox in an action bar whose job is clear because it sits above the rest.
- State is signalled by change: a checkbox is plain when off and earns fill, color and a checkmark when on.
- Emphasis is the difference between an element and its neighbours, so make defaults gray rather than making the important item louder.
- Cards are not required; a single line and a column edge can replace card borders and avoid borders on borders and stacked radii.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Presenter of the video and owner of the channel it was published on.
- [[entities/walmart|Walmart]] (company): Source of the receipt used as the opening example of edge-based alignment.
- [[entities/relume-publish|Relume Publish]] (product): AI website builder that sponsors the video (sponsor segment only).
- [[entities/vs-code|VS Code]] (tool): Example of a screen people scan for one thing (a single file) rather than read.
- [[entities/claude-code|Claude Code]] (tool): Cited for ending chats with tables, as an example of differentiating a wall of text.
- [[entities/figma|Figma]] (tool): The video's example files are shared as Figma assets.
- [[entities/edges|Edges]] (concept): The lines (card sides or other elements) that content aligns and stacks against.
- [[entities/undifferentiated-content|Undifferentiated content]] (concept): Uniform content with no visual variation, which the video names as the real cause of hard-to-read density.
- [[entities/chips|Chips]] (concept): Small labelled tags with icons used to categorise content and show values instead of telling them.
- [[entities/scannable-interface|Scannable interface]] (concept): The goal all the techniques serve: screens people can search quickly without reading everything.

## Topics

- [[topics/spacing-and-layout|Spacing and layout]]: Layout is built from edges: align text hard left and values hard right, place each element against at least two edges, manufacture edges where needed, and don't answer density with extra white space alone.
- [[topics/visual-hierarchy|Visual hierarchy]]: Screens are scanned, not read; differentiation (avatars, grouping, chips, icons) and contrast with neighbours decide what the eye finds, without telling people where to start.
- [[topics/cards-and-sections|Cards and sections]]: Cards give four edges for free, but stacking containers leads to borders on borders and three radii; a single line and column edge can dissolve cards into the interface while sections do the grouping.
- [[topics/icons-and-imagery|Icons and imagery]]: Replace plain text with immediately recognisable icons, diagrams and avatars; icons that need a tooltip to be understood leave people guessing.
- [[topics/color|Color]]: Color is the signal that something changed; keep defaults gray and give accent color only to the one element that should stand out.
- [[topics/forms-and-inputs|Forms and inputs]]: A checkbox is a thin border when off and earns fill and a checkmark when on; making it blue when off would destroy the signal.
- [[topics/buttons-and-actions|Buttons and actions]]: A profile card with too many unaligned buttons is better fixed by lining buttons up on a manufactured edge than by hiding secondary actions in a menu; action-bar icons can be ambiguous until a tooltip appears.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Warns against nesting containers until borders sit on borders; a single line can do the structural work.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Explains why some UIs feel 'weirdly perfect': the polish comes from scannability through edges, differentiation and visuals, not from prettiness.

## Notable Claims

- On a receipt, the only centred items are the parts you are not meant to read; alignment is what lets you skip them. Evidence: The only center things are the parts you're not really meant to read at all
- A receipt has no dividers and little white space; two edges hold everything together. Evidence: It's just two edges holding everything together
- Filling a card's empty space by adding more content ends up looking strange. Evidence: fill up the empty space, which ends up looking strange
- Stretching buttons and collapsing secondary buttons into a corner menu makes a card look better, but hiding elements is generally not the best fix. Evidence: hiding elements isn't generally the best way to fix this
- In almost all compact UIs, such as chat inputs, Kanban cards and sidebars, every element borders at least two edges. Evidence: everything in here borders on at least two or more edges
- A checklist looks perfectly built because every line creates a new edge for the next item to stack onto. Evidence: every line creates a new edge for the next stack onto
- Letting the checklist lines run the full width of the screen makes it feel less perfect even though every edge stays in place. Evidence: let them run the full width of the screen
- Adding white space to counter density helps a little but makes everything longer. Evidence: it's also made everything longer
- The problem with a dense list is too much undifferentiated content, not too much content. Evidence: too much undifferentiated content
- After adding avatars and grouping tasks by due date, any task can be found in about a second. Evidence: You can find any task in about a second
- Old AI chats' heavy use of bullet points and Claude Code's end-of-chat tables are explained by differentiation: they make a wall of text friendlier to read. Evidence: Claude code loves making tables at the end of its chats
- Adding comparisons, labels or tooltips makes a screen harder to read in order to make it easier to understand, a trade-off you almost never want. Evidence: harder to read in order to make it easier to understand
- Clean UIs that still convey what they need do it with visuals that are immediately recognisable. Evidence: using the right visuals that are immediately recognizable
- Chips for categories also let users swap tags directly instead of through a hidden menu. Evidence: functionality to intuitively swap tags
- Nothing on a screen is ever fully consumed; people look for one thing, such as one file or one setting. Evidence: Nothing on a screen is ever fully consumed
- Edges, differentiation and swapping text for visuals make a screen faster to scan, not prettier. Evidence: they're making it faster to scan
- Nobody designs a checkbox that is blue when off, because color is the whole signal that something changed. Evidence: the color is the whole signal that something has changed
- To make one element stand out you only need to change its surroundings, not give it more color or bolder text. Evidence: change its surroundings
- Emphasis is not a property of an element but the difference between it and its neighbours. Evidence: emphasis isn't something that an element has
- Adding containers and cards to structure an open canvas leads to borders on borders and three radii stacked, which doesn't help. Evidence: borders on borders and three radii all stacked together
- A single line can dissolve cards into the interface, with the column edge doing what the card edge did. Evidence: That column edge is doing what the card edge was doing
- A card that turns most of its plain text into diagrams and icons is easier to understand than one with more raw information. Evidence: which register the instant you look at it
- Universal visuals such as a red octagon (a stop sign) are understood without reading anything. Evidence: you didn't need to read anything to get there
- Cards hand you four edges for free, and if the content doesn't fit you can just resize them. Evidence: You get four edges handed to you for free
- Edges, differentiation and visuals make a screen faster to scan without ever telling you where to start. Evidence: without ever telling you where to start

## Quotes

> Here's the thing, nobody reads a screen.
> They're not making it prettier, they're making it faster to scan.
> emphasis isn't something that an element has, it's the difference between it and its neighbors.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Relume Publish in the middle of the video (from 'before you can create a product' to 'the very first link down below') and again in the outro; its claims (a library behind 2 million existing websites, four agents working on the live site) are advertising, not design guidance.
- Caveat: The before/after comparisons (card versions, full-width lines, 'which feels like more of a chore to read') are shown on screen and not described in the transcript, so the analysis relies on the narration only.
- Caveat: Auto-generated captions with [music] markers; 'Cloud Pro plan' is probably a mis-hearing of Claude Pro [inferred], and the phrase 'It's at every one of those tools' is garbled.
- Caveat: The rules are one practitioner's heuristics; 'about a second' is his estimate, not a measured result.
- Caveat: The description links the presenter's Figma files and resources page (self-promotion).

### Rules and practices

- **should** (layout, all): In lists and line items, align text hard left and values such as prices hard right; centre only content people are not meant to read. Why: Alignment to two edges holds everything together without dividers, and lets people skip the parts they don't need. [the text is aligned hard left, and the prices are hard right]
- **should** (layout, all): Don't fill empty space in a card by adding more content; look for the edges where content can be placed instead. Why: Adding content to fill space ends up looking strange. [Instead, try thinking about the edges where we can place content]
- **should** (layout, all): In compact components (cards, chat inputs, Kanban cards, sidebars, checklists), place every element against at least two edges, counting card sides and edges created by other elements such as an avatar and name. Why: That is what almost all compact UIs do, and it is why a checklist looks perfectly built: every line creates an edge for the next to stack onto. Values: four edges, at least two or more edges. [everything in here borders on at least two or more edges]
- **should** (components, all): Don't fix a crowded card by hiding secondary actions in a corner menu; move content to clear up edges, or manufacture a new edge that lines buttons and avatar up into a solid line for the content below. Why: Hiding elements isn't generally the best way to fix it; moving content alone can leave part of the card unresolved. [we can manufacture new edges to effectively move this top edge down]
- **consider** (layout, all): When list items get larger icons that break the bottom edge, add a subline to restore it. Why: Larger icons leave the row missing its bottom edge. [we need a subline to restore it once again]
- **consider** (layout, all): Don't treat edge alignment as enough on its own; avoid letting checklist or list lines run the full width of the screen. Why: When the lines run full width, every edge is exactly where it was, but things stop feeling perfect. [let them run the full width of the screen]
- **should** (layout, all): Don't rely on extra white space alone to fix a dense list; differentiate the content instead. Why: White space helps a little but makes everything longer, and the real problem is undifferentiated content. [you reasonably might start adding in more white space to counter the density]
- **should** (patterns, all): Differentiate dense lists: show avatars wherever people are referenced and group items by a meaningful key such as due date. Why: Then it doesn't matter how much text there is; any task can be found in about a second and density works for you. Values: about a second. [if I group based on due date]
- **should** (content, all): When something is unclear, turn plain text into immediately recognisable icons, diagrams or chips instead of adding comparisons, labels or tooltips. Why: Extra explanation makes the screen harder to read in order to make it easier to understand, a trade-off you almost never want. [the instinct when something isn't clear is to explain it harder]
- **should** (components, all): Don't depend on icon-only actions whose meaning only becomes clear once a tooltip appears; use visuals people recognise immediately, or placement that explains the control. Why: Apart from the checkbox placed above the rest, people are left guessing while they wait for the tooltip. [at least while you wait for the tooltip to pop up]
- **consider** (components, all): Highlight and underline links in blue, and use chips to categorise content. Why: They are recognisable at a glance, and chips also let users swap tags directly instead of through a hidden menu. [highlighting and underlining links in blue or using chips]
- **should** (components, all): Keep a checkbox's off state plain (thin border, no color, no icon) and give fill, color and a checkmark only to the on state. Why: Color is the whole signal that something has changed. [Off, it's a thin border and nothing else]
- **should** (color, all): Show values that are on their default state in gray so non-default values catch the eye. Why: When every chip looks equally prominent while on its default state, it isn't clear which is important. [default values are gray, so the ones that aren't find your eye]
- **should** (color, all): To make one element stand out, change its surroundings instead of giving it more color or bolder text. Why: Emphasis is the difference between an element and its neighbours, not something the element has. [all you need to do to make it stand out is change its surroundings]
- **should** (layout, all): Don't structure an open canvas by stacking containers and cards; use a single line and a column edge, with sections for grouping. Why: Stacked containers end up as borders on borders and three radii stacked together, which doesn't help. [borders on borders and three radii all stacked together]
- **consider** (content, all): Break a wall of text into differentiated structure, such as bullet points or a table, so it is easier to read. Why: It differentiates the content, which makes a wall of text a lot more friendly to read; the source notes old AI chats overdid bullet points. [makes our wall of text a lot more friendly to read]
- **should** (patterns, all): Use sections (or tabs) to group content so people never scan one long undifferentiated list. Why: Grouping and varying the content makes navigating much easier. [you're not scanning one long undifferentiated list]
- **should** (process, all): Judge a screen by how fast someone can find one thing, since people arrive with a question and hunt for the answer. Why: Nobody reads a screen, and nothing on it is ever fully consumed. [nobody reads a screen]

### Decisions it informs

- Should related content be grouped inside cards, or should cards be dissolved into the page with lines and column edges? (`Q-dir-04`)
  - Cards: Four edges come for free and the card can be resized when content doesn't fit; overused, it leads to borders on borders and three radii stacked together. When: Compact, self-contained units such as profile cards, Kanban cards or chat inputs [inferred].
  - No cards: a single line and column edges: Cards dissolve into the interface; the column edge does the card edge's job, rows stack on the row above, and sections do the grouping. When: A wide canvas where people would otherwise pile containers on containers.
  - Recommendation: Either can work, because everything should serve a scannable interface; but don't fill a wide canvas with nested containers, and use a single line to dissolve cards instead.
- A card has too many buttons that don't follow its edges. How should it be fixed?
  - Stretch buttons and hide secondary actions in a corner menu: The card does look better, but actions become hidden. When: Not recommended as a general fix.
  - Move content to clear up edges: Frees the edges but can leave the top part of the card unresolved. When: When the remaining layout still resolves cleanly [inferred].
  - Manufacture new edges: Moves the top edge down so the buttons and avatar line up into a solid line for the content below. When: When elements have no edge to stack onto [inferred].
  - Recommendation: Manufacture new edges or move content; hiding elements isn't generally the best way to fix it.
- A list feels too dense. Add white space, or differentiate the content?
  - Add more white space: Helps a little but makes everything longer. When: Not the fix the source recommends.
  - Differentiate the content: Avatars where people are referenced and grouping by due date make any task findable in about a second, so density works for you. When: Whenever a list is a wall of similar rows.
  - Recommendation: Differentiate: the problem is undifferentiated content, not too much content.
- When information isn't clear, should you explain it with more text or show it with visuals?
  - Explain harder (comparison, label, tooltip): More information on screen, but the screen becomes harder to read. When: Rarely; the source calls it a trade-off you almost never want.
  - Swap text for recognisable visuals (icons, diagrams, chips, blue underlined links): Registers the instant you look, and keeps the UI clean. When: Whenever a universally recognised visual exists.
  - Use placement: Position explains the control, as with a checkbox above an action bar. When: When a control's meaning follows from where it sits.
  - Recommendation: Use the right visuals that are immediately recognisable instead of explaining harder.
- How do you make one item stand out among many similar ones?
  - Make the item louder (more color, bolder text): Adds emphasis to the element itself. When: The source's framing is that this is the instinct, not the need.
  - Change its surroundings (defaults gray, only one accent): The item stands out by contrast, like the only blue item in a menu. When: When many elements are equally prominent, such as chips all on their default state.
  - Recommendation: Change the surroundings: emphasis is the difference between an element and its neighbours.

### Process

1. Find the edges: List the edges available: a card's four sides plus the edges created by elements inside it, such as the bottom of an avatar and name.
2. Lock every element to edges: Make sure each element borders at least two edges; where content has nowhere to stack, manufacture an edge (move an edge down, add a subline) rather than hiding elements.
3. Check widths: Edge alignment alone is not enough: don't let list lines stretch across the full width of the screen, where things stop feeling perfect even with every edge in place.
4. Differentiate the content: Add avatars where people are referenced and group items by a meaningful key such as due date, instead of adding white space.
5. Swap text for visuals: Replace plain text with recognisable icons, diagrams, chips and blue underlined links, and use placement to explain controls, before reaching for labels or tooltips.
6. Set emphasis by contrast: Keep defaults and off states plain or gray, and give color only to the element that has changed or needs attention.
7. Remove unneeded containers: Where cards are nested, dissolve them with a single line and a column edge and let sections do the grouping.
8. Test scanning: Ask whether someone arriving with one question can find the answer quickly without reading the whole screen.

### Examples and visual references

- Store receipt (Walmart): Item text hard left, prices hard right, only the codes centred; no dividers and little white space, just two edges holding it together.
- Profile card with too many buttons: Avatar and name with a row of buttons that don't follow edges; fixed by manufacturing a new edge so buttons and avatar form a solid line for content below, rather than collapsing actions into a corner menu.
- Checklist UI: Every line creates an edge for the next; larger icons need a subline; stretched to full width it feels off; improved with avatars, grouping by due date, blue underlined links and chips.
- Two versions of a card: The first has more raw text; the second turns it into diagrams and icons that register instantly. The narration later says you knew who each house belonged to before reading a name, so the card appears to show houses with owner avatars [inferred].
- Red octagon: Read as a stop sign with no text, showing how universal visuals need no reading.
- Action bar: The checkbox's meaning is clear from its placement above the rest; the other icons leave you guessing until the tooltip appears.
- Code editor (VS Code): Opening VS Code you look for one file, not the whole editor; the same goes for one setting in a settings panel. Used to show nothing on a screen is fully consumed.
- Settings panel with chips: Clean edges, tabs grouping, every value a chip with an icon; unclear because every chip is on its default state, like six checkboxes that are blue when off.
- Menu with a single blue item: The only blue component is the prompt to resubscribe to a Pro plan, showing emphasis created by contrast with neighbours.
- AI chat bullet points and Claude Code tables (Claude Code): Differentiation that makes a wall of text friendlier to read.
- Interface with cards dissolved: A single line replaces the cards; the column edge does the card edge's job, rows stack on each other, sections group, chips and icons carry meaning, and default values are gray.

### Numbers

- four edges: Every card has four edges to place content against. [On every card, we have four edges]
- at least two or more edges: In almost all compact UIs, every element borders at least this many edges. [everything in here borders on at least two or more edges]
- about a second: Time to find any task after adding avatars and grouping by due date. [You can find any task in about a second]
- six checkboxes: Analogy for six chips all on their default state yet equally prominent. [It's like having six checkboxes that are blue when they're off]
- three radii: Anti-pattern: stacked containers producing three radii stacked together. [borders on borders and three radii all stacked together]

<!-- /od:learn -->
