---
type: synthesis
title: Dashboards and data display
created: 2026-09-24
updated: 2026-09-28
sources:
  - 66oOi9OLMCw
  - 7sUUzOCv47U
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - Ksx9C2-3yMo
  - NtZeYmTMuo4
  - PDcQJOPby1k
  - Yr2uIcFZDDQ
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-pick-ui-library-skill
  - gKM6b2EnW1k
  - goWOAFqJHpA
  - jSxxAFxjxbU
  - kdRkuqu8apE
  - t7mpEDXzjCg
  - xHD01_Onac0
tags:
  - od-area-patterns
---
# Dashboards and data display

## In short

A dashboard exists so people can read data and act on it, so the first step is deciding its one job and what matters most, then putting that highest and farthest left. Dashboards use smaller text, tighter spacing and a stricter grid than marketing pages, because much more has to fit. The data should decide the form: fixed values become chips, numbers are right-aligned, time-based records become timelines, and charts stay plain, labelled and honest. Color should come from what the data means, not from decoration, and motion stays quiet: the house standards forbid decorative motion on data people are reading. The dashboards people remember go one step further: they say what the data means and what to do next, pick a visual that fits the data, and leave things out.

## House standards

- `STD-when-to-animate-11` (must): do not move data people are reading or acting on for style; decorative motion such as mouse-tracking, spring-driven graphs and animated line drawing stays on marketing pages.
- `STD-easing-duration-13` (must): the product's personality sets how much motion there is; a crisp, professional dashboard gets fewer, subtler, faster animations.
- `STD-when-to-animate-05` (must) and `STD-when-to-animate-07` (must): no motion on actions seen 100+ times a day, and remove or shrink motion on things seen tens of times a day, such as hover effects, row selection and list navigation.
- `STD-when-to-animate-13` (must): no entrance stagger on lists people scroll past or use all day.
- `STD-visual-details-02` (must): use tabular digits (`font-variant-numeric: tabular-nums`) on price columns and on numbers that change in place.
- `STD-visual-details-59` (must): when a number animates (a counter, price or stat), use NumberFlow instead of re-rendering the text.
- `STD-visual-details-55` (must) and `STD-visual-details-56` (must): pick one library from the curated list and reuse what the project already has; for dashboards that list names recharts, Liveline and Virtuoso (see below).
- `STD-visual-details-29` (should): use order, spacing and contrast so the most important thing on a screen is the most obvious.
- `STD-visual-details-31` (should): show the common path first and put advanced options one level deeper.
- `STD-visual-details-17` (should): use darker, heavier materials to separate structural regions such as sidebars.
- `STD-visual-details-44` (should): decide what not to build, and spend people's time, attention and trust only on features that pay off.
- `STD-when-to-animate-09` (must): delight motion only on rare, high-emotion moments such as empty states and completion, never on components used many times a day.

## What the sources teach

### Start from one job and a priority order

- Give the dashboard one clear job; if it looks like it needs a PhD to operate, cut it back. The main section shows what matters most to the user, and the very top holds page actions such as a primary "create" button [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Begin a redesign with a hierarchy assessment and expect to throw elements away: the finance example merges or cuts most of its original 12 cards, ranks each module into a priority tier, and places higher tiers higher and farther left on the grid [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Do not repeat the same KPI cards on several pages, and keep stats out of the sidebar, which should hold navigation [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- On a phone, a desktop dashboard shrinks to one of its panels per screen, and each mobile section extends in one direction only (stacked or scrolled sideways, not both) [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- A click-through highlight reel is poor for checking stats at a glance; a per-chapter "view summary" screen works as a small dashboard inside a story format [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- In a money app, the analytics tab toggles saving or spending and daily, weekly or monthly views, marks overspending against a target, and adds insights about upcoming bills so people can prepare [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Go one step past the data

- Clear hierarchy, good spacing and useful charts make a dashboard fine, not memorable. The dashboards a Mobbin reviewer kept returning to, out of 2,108, were one step ahead: Faith puts key insights next to its line chart, so it shows what to do about a trend and not only what happened; Origin adds a weekly recap and a daily brief; Runner packages a run into highlights that feel like an accomplishment [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- When products do roughly the same thing, the dashboard does much of the convincing: one screenshot should say what the product does, how you are doing and what to do next. Nearly one in five products on Mobbin use the dashboard as the home screen [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- AI is filling the "why did this change?" gap, from a single prompt right under a chart to a full AI layer beside the data; on Mobbin, AI dashboards get about twice the saves and exports of the average dashboard screen, which shows what designers collect, not what users prefer [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).

### Fit the visual to the data, and leave things out

- The standout dashboards were clearly not templates; someone asked how to make the data make sense instantly. Shopify's Live View shows store visitors across the globe in real time, where every dot is a real person browsing right now; Front's heat map uses darker squares for busier hours; Visitors stands out simply by being clean when most dashboards look busy [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- Small touches show care: Cake puts a birthday cake inside its ownership donut chart, and Mercury lets people play a game instead of showing an empty table once all bills are paid [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- On mobile, personal data can be presented like content: Opal turns screen-time insights into a swipeable story that people want to share. Some products coin their own metric (streaks, a readiness score, closing rings) that users adopt in their own words [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- The reviewer's gut check is "Would I screenshot this, and why?"; the dashboards worth screenshotting were not the prettiest but the ones that knew what to leave out [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).

### Density: smaller type, stricter grid, more neutrals

- Dashboards use smaller text styles with less difference between sizes, and follow the grid more strictly than landing pages because they fill most of the screen [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- One creator gives a number: dashboard text is normally not larger than 24 px because of the information density [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). This is a single-source figure; it sits inside the productive range in the research (see below).
- A tighter type scale, the cube root of the golden ratio, suits interfaces with many font styles such as dashboards [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- Product UI needs more neutral roles than a landing page: about four background layers, one or two strokes and about three text colors before hover states, plus a slightly darker sidebar or frame as an anchor (Mercury adds about 2% blue) [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).

### Let the data drive the form

- Show fixed-value columns (department, status) as chips, right-align numbers so digits line up by place value, truncate long text, shade inactive rows, show time-based records as a timeline, put avatars next to actors in activity logs, and add a summary chart when the data has a time dimension [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- A good list comes down to separation (space, lines or color) and a good table to search, filter and sort; selecting several items should reveal bulk actions, and home-page rows should show only a few essential fields [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Every widget's actions must make sense for the real object (a credit card gets "lock card", not "receive"), every number needs a label, and an alert needs an icon, the amount, the date and the place [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Use the "completed" color only for completed work, and show an actual percentage instead of an "in progress" label [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Virtualize lists and tables of 1,000+ rows with Virtuoso before reaching for pagination hacks [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

### Charts: familiar, labelled, honest

- Prefer familiar line and bar charts and give them grid lines, numbers, a short summary and a date range selector [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Bar charts need a vertical axis, no rounded bar tops (they hide where the bar ends) and a bar count that matches the data; the counterexample shows 16 bars for 7 days [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Draw straight segments between data points instead of smoothed curves, and add horizontal and vertical grid lines, markers, a time-frame switcher, a gray previous-period line for business metrics and a legend [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). The finance redesign also rejects curved and faded data lines [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Choose each representation on purpose: a two-sided bar chart for money in and out, a pie chart for a line of credit, and never a chart plus growth percentages for the same data [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]). Location data reads better as a shaded map with the numbers listed beside it, and usage as a few small donut charts [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Give every chart a title, axis titles and a legend, and circle or annotate the part that matters [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).
- Use recharts for static or interactive dashboard charts and Liveline only for live data that scrolls with time [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

### Color from meaning

- Dashboard color should come from the data, such as a red icon in a chip for an urgent action, not be sprinkled in to look nice [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- Add color through charts that carry information, such as micro charts on KPI cards, instead of colored buttons and icons [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Always include semantic colors for success, failure and in-progress, even in a black-and-white brand; for chart series, fix lightness and chroma in OKLCH and step the hue by about 25 to 30 so every series looks equally bright [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).

### Hidden UI and progressive disclosure

- Place each action on a "spectrum of explicitness": a global share button is always visible, a minor action such as copying a cell appears on hover with a tooltip, and rarely used features live in popovers. Tooltips belong on every icon and ambiguous label, and dense tables need designed hidden UI (copy chips, comment indicators, drawer and modal states) [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- Use a popover for simple non-blocking context, a modal for complex tasks on the same page, and a new page for permanent or very large context, always with a back button or breadcrumb [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- A secondary detail cut from a card can stay reachable behind a kebab menu [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).

### Motion on dashboards

- Dashboard motion is tame and user focused; chart hover can show the value or dim the other bars, and optimistic UI (Gmail removing a deleted email at once) keeps the dashboard feeling fast [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Data the user is reading or acting on must not move for style: an animated line drawing on an analytics chart is a rejected example, and a functional banking graph is better with no animation [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- A Figma sidebar tutorial shows an integration card moving through focus, loading and success states; it is a prototype recipe, not a code spec [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).

## Where they agree and disagree

- **Plain charts beat decorative ones.** Four videos agree [S-L19-045] [S-L19-047] [S-L19-068] [S-L19-075], but all four are by one practitioner (Kole Jain), so they count as one voice. The house rule against decorative motion on data (`STD-when-to-animate-11`) points the same way. The research agrees on honesty and chart chrome: bars start at zero and gaps are never interpolated (DC-L05-22), gridlines and tick labels reuse text and border tokens, and hovering a legend dims other series (DC-L05-24), which is close to the bar dimming on chart hover in [S-L19-047].
- **"No curved lines" is one creator's view.** Both videos that say it come from the same channel [S-L19-068] [S-L19-075], and the reason is given only in one of them. The research does not rule on smoothing; its "never interpolate gaps" rule is related but different (DC-L05-22) [inferred].
- **Chart colors: a real disagreement.** [S-L19-039] calls a neutral chart dull and a single brand ramp too samey, and wants an OKLCH spectrum. The research default is one brand chart color plus gray, with a 6-8 color categorical set only when needed (DC-L05-23, DC-L01-24), and that is the current default of Q-color-19. The two sources that say color should come from the data [S-L19-056] [S-L19-061] fit either view [inferred]. Any spectrum still has to pass 3:1 against the surface and must not rely on color alone (DC-L05-25).
- **Text size.** The 24 px ceiling [S-L19-052] is a single-source number. The research describes productive type as sizes of roughly 12-32 with tight contrast (DC-L02-11), so the two point the same way but the exact cap is unconfirmed.
- **Aligning numbers.** Right-aligning numeric columns [S-L19-056] and the tabular-digit standard (`STD-visual-details-02`, DC-L02-26) work together: tabular digits make the right edge line up [inferred].
- **Hover-only actions.** [S-L19-056] reveals secondary actions on hover, and its own analysis notes it never covers touch or keyboard. The research says never hide anything essential behind hover (DC-L13-03), so hover reveals suit secondary actions only.
- **Long lists.** Virtualization [S-L19-029] and pagination (DC-L08-21, the Q-pattern-02 default) answer different questions: how to render many rows, and how people move through them [inferred]. They can be combined.
- **Density control.** The research recommends component sizes plus a user-level compact mode for data-heavy products (DC-L03-10); the sources only argue for a denser default.
- **Card separation.** Outlines in dark mode and fills in light mode is stated as personal preference [S-L19-047].
- **Say what it means.** Insights beside a chart [S-L19-110] agree with the short summary under a chart [S-L19-047] and the annotated part that matters [S-L19-083]; this is now two channels, not one. Leaving things out [S-L19-110] matches giving the dashboard one job and cutting cards [S-L19-047] [S-L19-068] and `STD-visual-details-44`.
- **Delight on a data screen.** [S-L19-110] praises a cake inside a donut chart and a game instead of an empty table, while Kole Jain's videos favour plain charts. They do not clash as long as the delight never moves the data (`STD-when-to-animate-11`): the cake is static, and Mercury's game sits in an all-done empty state, the "user-cleared" kind in DC-L13-10, where `STD-when-to-animate-09` allows delight [inferred].
- **Live data moves because it is live.** Shopify's visitor dots [S-L19-110] change with real events, which is not decorative motion; Liveline is the curated pick for live data that scrolls with time [S-L19-029] [inferred link].
- **Heat maps.** Darker-means-busier [S-L19-110] is a single-hue sequential scale. Q-color-19's `categorical-6-8` option already includes "one light-to-dark ramp", so a heat map can reuse that ramp rather than add a palette; it still needs a legend and must pass the contrast rules (DC-L05-25) [inferred].
- **AI explanations.** An AI answering "what caused this spike?" [S-L19-110] should show the data it used; DC-L19-138, following DC-L13-16, allows retrieval steps and citations but not narrated reasoning presented as an explanation [inferred application].
- **Coined metrics.** The claim that a named metric keeps users from switching [S-L19-110] has no data behind it; see the [[synthesis/retention-and-gamification|Retention and gamification synthesis]].

## Decisions this informs

- **Q-layout-03** (reading, working or data): a dashboard-heavy product answers "data".
- **Q-dir-02** (compact, comfortable, spacious): dashboards lean compact; consider "user-selectable" per DC-L03-10.
- **Q-type-09** (scale ratio): a tighter ratio for many text styles [S-L19-042].
- **Q-type-06** (numbers font and tabular digits): tabular digits are already locked for changing numbers by `STD-visual-details-02`; this question only picks the face.
- **Q-color-19** (chart colors): weigh "brand-gray" (default) against "categorical-6-8" for multi-series dashboards.
- **Q-color-15** (status colors): semantic colors are required even in a neutral brand [S-L19-039].
- **Q-viz-01** (chart kinds and kit): "core-6" plus "theme-library"; the curated library is recharts, with Liveline for live data.
- **Q-layout-04** (navigation placement): the sidebar is the product's spine [S-L19-047] [S-L19-068].
- **Q-pattern-01** (modal, panel or pop-up): popover, modal or new page by the size and permanence of the task [S-L19-047].
- **Q-pattern-02** (long lists): pagination for navigation, virtualization for rendering.
- **Q-pattern-03** (progressive disclosure): the spectrum of explicitness [S-L19-056].
- **Q-depth-01** and **Q-depth-05** (card and list separation).
- **Q-motion-01** (motion style): "productive" or "two-mode" with no hero moments on data screens.
- **Q-pattern-06** (one number without opening the app): the glanceable KPI (DC-L14-07); a coined metric is a natural candidate [S-L19-110] [inferred].
- **Q-viz-01** `by-purpose`: pick the visual that makes the data make sense at once (a live map of visitors, a heat map of busy hours) [S-L19-110].
- **Q-ai-01** (how AI work appears): a prompt under a chart or a full AI layer beside the data [S-L19-110].
- **Q-pattern-04** (empty screens): an all-done state can reward people instead of showing an empty table [S-L19-110].

## Visual examples worth showing

- A before-and-after table: plain text columns versus chips, right-aligned numbers, truncated text and shaded inactive rows [S-L19-056].
- The finance dashboard rebuild: 12 Dribbble cards cut to a priority grid, with a two-sided income and expense bar chart, a pie chart for the line of credit and a fraud alert card with amount, date and place [S-L19-068].
- A line chart fix: a small smoothed curve versus straight segments with grid lines, markers, a time-frame switcher, a gray previous-period line and a legend [S-L19-075].
- Two bar charts side by side: one with an axis, one decorative with rounded tops and 16 bars for 7 days [S-L19-045].
- The link-tracking dashboard: sidebar plus a two-by-two grid, bulk-actions button on multi-select, hover that dims the other bars [S-L19-047].
- Location analytics as a shaded map with the list beside it, KPI cards with micro charts, and a usage tab with small donuts [S-L19-061].
- A Gantt progress fix: completed color only on completed work, and a percentage instead of "in progress" [S-L19-086].
- A desktop dashboard reduced to one panel on mobile [S-L19-053].
- An OKLCH chart palette built by stepping hue by 25 to 30 at fixed lightness and chroma [S-L19-039].
- A line chart with its key insights beside it (Faith), next to the same chart alone [S-L19-110].
- Shopify's Live View with one dot per current visitor, and Front's busy-hours heat map [S-L19-110].
- Mercury's game in place of an empty table after all bills are paid, and Cake's birthday cake in a donut chart [S-L19-110].
- Opal's story-format screen-time insights on mobile [S-L19-110].

## Open questions

- Should OpenDesigner offer an OKLCH categorical palette as the dashboard default instead of brand plus gray? It would need a contrast and color-vision check (DC-L05-23).
- Where does the 24 px ceiling fit in the generated type scale, and should it be a lint or just guidance?
- What are the touch and keyboard equivalents of hover-revealed row actions? On phones the sources show swipe actions (Apple Reminders) [S-L19-056] and long-press menus [S-L19-053], but none says how a keyboard user reaches a hover-revealed action.
- Should chart tokens encode "straight segments, no smoothing" as a default, given that only one creator argues for it?
- Loading and empty states for charts and KPI tiles are barely covered by these sources; see [[synthesis/feedback-empty-and-loading-states|Feedback, empty and loading states synthesis]].
- None of the practitioner sources discuss chart accessibility (text alternatives, data tables); the research covers it (DC-L05-25) but no source here tests it.
- Should the builder offer an "insight beside the chart" slot in its chart component, and should a heat map reuse the light-to-dark ramp of Q-color-19's `categorical-6-8` option even when the product otherwise picks `brand-gray`? [S-L19-110] shows both patterns but gives no rules [inferred].
- The Mobbin reviewer's picks are opinion from screenshots; no source measures whether memorable dashboards keep users longer.
