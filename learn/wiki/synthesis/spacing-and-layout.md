---
type: synthesis
title: Spacing and layout
created: 2026-09-24
updated: 2026-09-24
sources:
  - 9WVt1CelBfg
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - HE4rLEQpiXY
  - Lp6ey4AyDzA
  - P2ksReDwWkE
  - RCneB_MQ7qs
  - SfX43uIubj4
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Vy0KKvZJRH8
  - Yr2uIcFZDDQ
  - c1TvOcKdBVE
  - eMMiLeo_UGI
  - eeN7yUcIWbw
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-mobile-native-skill
  - gKM6b2EnW1k
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - pGYLZyBE32o
  - sonner-toaster
  - tNMAFjzapOk
  - ulSOdTgoGeY
  - xHD01_Onac0
tags:
  - od-area-layout
---
# Spacing and layout

## In short

Space is the cheapest way to show what belongs together: things that sit close read as one group, and a bigger gap starts a new one. Most sources separate content with space first and add lines, boxes or background colors only when space is not enough. Every gap should come from one small base unit (4 or 8 pixels), and on the web the house standard writes spacing in rem so the layout grows when people make text bigger. The layout itself starts from what the content has to do: familiar structures for products (top to bottom, left to right, navigation on top), strict grids for dashboards, and more varied sections for marketing pages. Space helps, but it does not fix everything: too much of it breaks groups apart, and a dense list needs clearer content, not just more room.

## House standards

- STD-visual-details-32 (should): place each control near what it affects and arrange controls to mirror what they change.
- STD-visual-details-29 (should): use order, spacing and contrast so the most important thing on a screen is the most obvious.
- STD-visual-details-27 (should): make every spacing, timing and alignment value a deliberate choice you can defend.
- STD-visual-details-26 (must): build from the project's existing spacing tokens and extend them; never a parallel set or a hand-typed value.
- STD-visual-details-28 (must): no jittery scrolling, misaligned icons or layouts that break when the device rotates.
- STD-visual-details-30 (should): aim for simplicity, not minimalism; strip what is unnecessary, but do not bury everything to look minimal.
- STD-visual-details-37 (should): break a familiar pattern only when you can prove the new one is better, and test it.
- STD-accessibility-motion-13 (must): scale layout with the user's text size; on the web write spacing in rem or em, not fixed px.
- STD-visual-details-01 (must): cap body text at about 65ch.
- STD-mobile-touch-10 (must): height 100dvh for app shells, drawers and bottom-pinned UI, min-height 100svh for marketing heroes; never 100vh or lvh.
- STD-mobile-touch-16 (must): add viewport-fit=cover and pad fixed headers, tab bars, toasts and sheets with env(safe-area-inset-*).
- STD-mobile-touch-09 (must): touch targets at least 44×44pt on iOS and 48dp on Android, and a 44px hit area for small web controls on touch; grow the hit area, not the visual.
- STD-components-toasts-drawers-29 and STD-components-toasts-drawers-30 (should): toasts default to bottom-right, 32px from the screen edges on desktop and 16px below a 600px screen width.

## What the sources teach

### Closeness shows what belongs together

- The closer two things sit, the more people link them. In one landing-page hero the subtext sits 8 px under the heading, the eyebrow 12 px above it and the buttons 32 px below, so heading and subtext read as one unit [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]. The values come from one example site, so they show the idea rather than set a rule.
- A simple section can use one gap (32 px) between items and pull pairs that belong together (announcement and heading, heading and subtext) closer; the source calls that grouping another form of visual hierarchy [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- People read distance as "not related" and closeness as "related" [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]. The apple-design skill says the same ("proximity implies relationship") and adds that a control belongs next to what it changes (STD-visual-details-32) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Hero buttons should sit at least twice as far below the subtext as the subtext sits below the heading [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]. This is one video's rule of thumb; it points the same way as the 8 px and 32 px example above [inferred].
- Too much space breaks groups apart: giant text surrounded by empty space made a car maker's page feel disjointed, and pushing elements closer together created hierarchy [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]].
- On mobile, group the contents of a card with white space instead of nesting a second card, which causes "padding on padding" [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].

### Space before lines and boxes

- Separate content with space rather than dividers and cards, especially in multi-column grids such as a store; many separators and containers make even a sparse design feel cluttered [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]].
- Lines on everything, instead of spacing things apart, recall old PowerPoint slides. Dividers are coming back, and they can have rounded edges instead of being straight lines everywhere [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]].
- For lists, drop divider lines unless lines are the product's chosen style, and space the items apart; if rows must be tight, use a subtle alternating background. Use as few elements as possible to make the point [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]. A dashboard list can be separated by space, lines or color [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].
- A shop receipt holds together with no dividers at all: text hard left, prices hard right [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Lines can also be a deliberate style. A "straight line grid" keeps visible lines between feature cells instead of floating cards [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]; vertical lines can frame a landing page and keep it responsive on very large screens [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]; a "canvas grid" of section borders adds interest when there are no custom graphics [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].

### One base unit for every gap

- Use a four-point grid: every value a multiple of four, not because it looks better but because values can always be halved. Exact 8 px spacing everywhere is a guideline, not a law [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- Keep spacing on a 4 or 8 px base, especially in small components. At large sizes the presenter rounds to the nearest 5 or 10, or, to stay on 8, lets the steps grow exponentially, because 120 versus 128 makes no visible difference [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]].
- Sign-up and login modals follow a 4 px grid "religiously" [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]].
- Bigger elements get more generous spacing: 8 px insets and gaps for feature cards, but 64 px padding around a large hero screenshot [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]. These are one designer's values.
- A chip's vertical padding can be half or a quarter of its horizontal padding (20 px gives 10 or 5) [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]; this is one video's preference.
- The house standard adds that each value must be a deliberate, defensible choice (STD-visual-details-27) and that web spacing is written in rem or em so layout grows with the user's text size (STD-accessibility-motion-13) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

### Room to breathe, but space is not a cure-all

- Beginner layouts are packed too tight. Align to column grids, add vertical space between stacked items, build cards and chips with auto layout so their spacing repeats, and give mobile screens more space than you think [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]].
- White space matters more than elaborate grids [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]. A clear grid with plenty of space around text is what makes a section feel crafted rather than crammed, and a visitor should grasp the idea in a five-second scroll [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].
- Keep good spacing around a hero message so the illustrations around it read as context, not clutter; one extra illustration tipped the example over the line [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]. Images scattered around text keep a safe margin from it [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]].
- Space has limits. Extra white space in a dense list helps a little but makes everything longer; differentiating the content (avatars, grouping by due date) works better [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]. A text-only section needs three or more lines of body text or it feels too empty [S-L19-060] [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]].
- Do not shrink type and spacing when moving a design to mobile; keep them similar to desktop or slightly larger (the source cites a 17 px iOS body font against 13 px on macOS) [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].
- Check spacing on the real screen: designing zoomed out in Figma led one designer to oversized type and spacing [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]], and a desktop hero should be judged in a real browser window of 1920 by about 1,000 px rather than a tall showcase canvas [S-L19-049] [[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]. The window size is the presenter's observation, not a measurement.

### Grids: strict for products, a guide for marketing

- Column grids (12 columns on desktop, 8 on tablet, 4 on mobile) help structured, repeating pages and guide responsive behavior; custom landing pages often sit off the columns [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- Dashboards follow the grid more strictly than landing pages because they use most or all of the screen; the demo uses a two-column, two-row grid [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].
- Align to the column grid as closely as possible, and leave an element that breaks it slightly if it still feels balanced [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]].
- On a dashboard grid, put the most important modules higher and farther left, choose module orientations that do not leave awkward gaps, and keep margins consistent between modules even if one then shows fewer items [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- Build bento sections on simple grids so developers can build them [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]. Use a bento only when there is enough content to fill every box, and expect the box sizes to change as the content plan develops [S-L19-060] [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]].
- On mobile each section moves in one direction only: a vertical stack or a horizontal scroll [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].

### Alignment and edges

- Layout is built from edges: text hard left, values hard right. In compact interfaces every element sits against at least two edges (card sides, or edges made by other elements such as an avatar), and when content has nowhere to stack you can manufacture a new edge [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Alignment is one of the three biggest fixes to AI-generated screens, with fonts and color [S-L19-086] [[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]].
- Do not center everything, which is what AI does by default. Left-align, or split the hero about 3/5 and 2/5 with the top of the supporting text level with the top of the headline; put nav links next to the logo [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- Centering still has a place: a profound statement centered, larger and with a lot of space [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]], or a centered core message with context elements around it, where off-grid elements pull toward the center and thin out further away [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]].

### Pick the layout for what the content does

- At any point there are only a handful of layout options, and the choice depends on what the content is trying to do [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]].
- People expect information to flow top to bottom and left to right, with navigation at the top. Conventional layouts are easier to extend and to make responsive, so make a layout your own with details rather than by abandoning it [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].
- Apple's utility apps share one layout: global actions on top, navigation in a sidebar, content in the centre; keep roughly the top 50 px clear because it drags the window [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]. In a dashboard the sidebar is the product's spine and the top of the main area is reserved for page actions [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].
- Fix the layout first when elements are scattered [S-L19-049] [[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]; a good layout carries a section before any animation is added [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]].

### Vary sections on marketing pages

- Variety in layout between sections is called "a must"; when stacked items line up too uniformly, flip one [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]].
- Text-left, image-right rows repeated down the page look like a template, and a stacked hero steps away from it [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]. Mixing in a full-screen section, cards and a three-column section already helps; "breaking the box" (overlaps, cards shifted up and down, a card row running past the frame) adds interest but is easy to get wrong, so start small [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- Do not reuse the same layout for two sections of one page; a row of cards running off the page edge is one way to break the box [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]. A resources roundup calls layout variety "everything" [S-L19-073] [[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]].
- The common software hero is big text, a big image and lots of space [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]; beauty sites often split the screen into two halves [S-L19-049] [[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]; stacking a two-column feature row into one column keeps attention on one feature at a time [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- Once structure is in place, break the expected pattern once in a while with one well-built surprise [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].

### Platform rules from the house standards

- Size full-height layouts with 100dvh (app shells, bottom-pinned UI) or 100svh (heroes), and pad fixed headers, tab bars, toasts and sheets with the safe-area insets (STD-mobile-touch-10, STD-mobile-touch-16) [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]].
- Toasts sit 32 px from the screen edges, 16 px below a 600 px screen width, with a gap of 14 between expanded toasts (STD-components-toasts-drawers-30, STD-components-toasts-drawers-12) [S-L19-021] [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]] [S-L19-022] [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]] [S-L19-092] [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]].

## Where they agree and disagree

- **Space first.** The practitioner sources agree that space should separate content before lines or containers ([S-L19-057], [S-L19-070], [S-L19-050], [S-L19-080]). This matches DC-L15-05 (default: space first; add a container only when content types mix, items sit in a grid or spacing cannot be controlled) and DC-L04-08 (space, then a surface change, then 1px lines).
- **Lists.** DC-L04-08 says to use lines in dense data views and DC-L15-05's default uses lines for long lists. [S-L19-070] prefers space and, when rows must be tight, alternating backgrounds instead of lines. This is an open disagreement.
- **Grouping ratio.** The only numbers are an 8 px versus 32 px hero gap [S-L19-043] (about 1:4) and "at least twice" [S-L19-062] (1:2). Both fall inside Q-space-05's options and DC-L03-24's heuristic of at least 1:2 [inferred]. Neither video states a general ratio, so these stay practitioner opinion that the existing research happens to support.
- **Base unit.** A four-point grid [S-L19-052], a 4 or 8 px base [S-L19-070] and a 4 px modal grid [S-L19-075] agree with DC-L03-01's default of 4 as the grid and 8 as the rhythm. Rounding large values to the nearest 5 or 10 [S-L19-070] does not fit a token scale and would clash with STD-visual-details-26 (no hand-typed values) [inferred]; the presenter's other option, steps that grow exponentially, matches DC-L03-02's hybrid scale.
- **Units.** STD-accessibility-motion-13 (must) asks for rem or em spacing on the web. DC-L03-26's default authors tokens in px and offers rem spacing only as a toggle, and the standards file already records that engine.py's CSS export writes spacing in px. The standard wins; the card and the export need to follow it.
- **Mobile spacing.** [S-L19-053] says mobile type and spacing stay the same as desktop or get larger, and [S-L19-045] says mobile needs more space than you think. DC-L03-24 cites Material recommending more generous spacing on desktop. The two point in different directions.
- **More space or clearer content.** [S-L19-045], [S-L19-052] and [S-L19-084] ask for more room; [S-L19-080] says extra white space is not the fix for a dense list, and [S-L19-065] shows overused space breaking groups apart. DC-L15-04 sides with [S-L19-080]: the denser the layout, the stronger the grouping and signifiers must be.
- **Grids.** [S-L19-052] and [S-L19-047] match DC-L15-07 (column grid for apps, hierarchical or bento layouts for marketing, and a grid break needs a reason) and DC-L03-15 (4, 8 and 12 columns).
- **Alignment.** [S-L19-103] (left or split, not centered) agrees with DC-L15-08 (start-aligned by default; center only single-focus moments with short text). The centered "profound statement" in [S-L19-043] fits DC-L15-08's exception.
- **Breaking patterns.** The variety and "break the box" advice ([S-L19-065], [S-L19-085], [S-L19-082], [S-L19-084]) is about marketing sections. STD-visual-details-37 asks for proof before breaking familiar patterns, and [S-L19-054] argues for convention. Read together, variety belongs between marketing sections, not in navigation or components [inferred].
- **Navigation placement.** [S-L19-067] and [S-L19-047] (a sidebar and a top area for actions on desktop) and [S-L19-053] (a bottom bar of three to five links on phones) agree with DC-L03-19 (a sidebar for desktop productivity tools, a bottom bar on compact screens).

## Decisions this informs

- **Q-space-01** (base unit): a four-point grid [S-L19-052] and a 4 or 8 px base [S-L19-070] support the `4-grid-8-rhythm` option.
- **Q-space-02** (how steps grow): large steps that grow exponentially [S-L19-070] support `hybrid`.
- **Q-space-05** (space between groups versus inside them): 8 px versus 32 px [S-L19-043] and "at least twice" [S-L19-062]; the annotated hero makes a good visual for this question.
- **Q-space-06** (spacing by job): equal insets and gaps in feature cards [S-L19-103]; the chip padding ratio [S-L19-075] is a squish inset in DC-L03-04's terms [inferred].
- **Q-space-03** (target size): spreading tab icons apart to enlarge click areas [S-L19-075]; STD-mobile-touch-09 sets the floor.
- **Q-dir-02** (density): beginner layouts are too tight [S-L19-045], dashboards are denser [S-L19-047], and dense screens need differentiated content [S-L19-080].
- **Q-dir-04** (group by space, cards or lines): space first ([S-L19-057], [S-L19-070]), cards on mobile [S-L19-053], lines as a deliberate style ([S-L19-066], [S-L19-103]).
- **Q-depth-05** (how list rows are split): space, lines or color [S-L19-047]; space or alternating rows [S-L19-070].
- **Q-dir-05** (start-aligned or centered): split or left-aligned heroes [S-L19-103]; centered only for a single statement ([S-L19-043], [S-L19-063]).
- **Q-layout-03** (reading, working or data pages): dashboards follow strict grids [S-L19-047] with priority placement [S-L19-068].
- **Q-layout-04** (navigation placement): Apple's utility layout [S-L19-067], the sidebar as spine [S-L19-047], a bottom bar or a sidebar turned home page on mobile [S-L19-053].
- **Q-layout-05** (grid and bento): 12, 8 and 4 columns [S-L19-052], simple bentos [S-L19-066], bentos only with enough content [S-L19-060].
- **Q-type-17** (layouts grow with text size): STD-accessibility-motion-13 [S-L19-020] requires web spacing that scales with text; check that the `capped-chrome` default still meets it [inferred].

## Visual examples worth showing

- The annotated hero: eyebrow 12 px, subtext 8 px, buttons 32 px (Superpower site) [S-L19-043].
- A simple hero with 32 px between items and grouped pairs [S-L19-052].
- The receipt: text hard left, prices hard right, no dividers [S-L19-080].
- One list shown three ways: with lines, with space, and tight with alternating rows [S-L19-070].
- A multi-column store with and without cards and dividers [S-L19-057].
- A split hero (3/5 and 2/5) next to a centered one [S-L19-103].
- A finance dashboard cut from 12 cards to a few modules, placed higher and farther left by priority [S-L19-068].
- A desktop layout that runs in two directions next to a mobile section that stacks or scrolls sideways [S-L19-053].
- A page of repeated text-and-image rows next to a varied one ([S-L19-085], [S-L19-072]).
- Toast placement: 32 px from the edges on desktop, 16 px under 600 px [S-L19-092].

## Open questions

- How should the engine's CSS export meet STD-accessibility-motion-13 (rem or em spacing) while DC-L03-26 keeps px authoring for iOS points and Android dp?
- Should Q-space-05's default stay at 1:2 when the only concrete example, from one site, uses about 1:4?
- When is a line grid or canvas grid the right choice rather than space? The sources give taste, not criteria.
- Should mobile spacing match desktop or be tighter? [S-L19-053] and DC-L03-24 disagree.
- No question records where dashboard modules go by priority (higher and farther left) [S-L19-068].
