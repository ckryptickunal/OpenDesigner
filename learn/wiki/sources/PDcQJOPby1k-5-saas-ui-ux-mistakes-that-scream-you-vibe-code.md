---
type: source
title: 5 SaaS UI/UX mistakes that SCREAM you Vibe Code
created: 2026-09-27
updated: 2026-09-27
video_id: PDcQJOPby1k
url: https://www.youtube.com/watch?v=PDcQJOPby1k
channel: Kole Jain
published: 2026-02-12T02:29:34Z
authority: reference
tags:
  - saas
  - vibe-coding
  - ai-generated-ui
  - dashboard
  - icons
  - sidebar
  - pricing
  - landing-page
  - charts
  - redesign
---

# 5 SaaS UI/UX mistakes that SCREAM you Vibe Code

## Metadata

- Video ID: `PDcQJOPby1k`
- Channel: Kole Jain
- Published: 2026-02-12T02:29:34Z
- URL: https://www.youtube.com/watch?v=PDcQJOPby1k

## Summary

Kole Jain redesigns a real vibe-coded URL shortener to show the UI and UX mistakes that give away an AI-built SaaS app, and how to fix each one. The fixes are: replace emojis with an interface icon library, don't let AI pick colors (add color through charts instead of buttons and icons), and don't let AI pick the layout (no repeated KPIs, a focused sidebar, an account card with a popover, calmer cards). He also covers product features: a modal instead of a sparse flyout, advanced options collapsed by default, and tabs that scale as features grow. On the billing and pricing side, he removes dead cards, cuts the number of plans, makes price bigger than plan name, shows the discount and what the next plan adds. Finally he argues that landing pages need real product graphics, because presentation builds trust and conversion. For a design system this gives a checklist of anti-patterns to catch in AI-generated UI, plus concrete component and pattern choices for SaaS dashboards, pricing and marketing pages.

## Key Ideas

- Emojis in product UI are an obvious sign of AI-built software; a professional interface icon library looks better (Notion is an exception that uses emojis well).
- AI tends to pick bright colors that don't work together, so a human should choose the colors.
- Color can come from charts that carry real information rather than from colored buttons and icons.
- Repeating the same KPIs in several places of a small app is a giveaway, like too many dashes in AI-written text.
- AI is generally bad at complex layouts and cards, so reworking layout is where little time brings the largest improvement.
- The sidebar should hold navigation, not stats; detailed numbers belong on the dashboard or an analytics tab.
- Busy cards get calmer when their buttons collapse into a triple-dot menu and chips collapse to icons.
- Pick the container for a form by how much it holds: a sparse flyout with lots of empty space works better as a modal.
- AI sets up logic and features well if you tell it to, so missing options and dead cards need a human pass.
- Tabs let a settings or billing area grow: new sections like documents, integrations or AI become another tab.
- On pricing cards, size by what people care about: the plan name smaller (no one cares), the cost per month larger (people do); also show the actual discount and what the next plan adds.
- Too many plans (five) is not ideal; drop at least one.
- Cheap, low-hanging features (like splitting analytics by individual link to compare them) can make an app much better.
- Landing pages are where a vibe-coded product loses most customers; a quality bar builds trust even subconsciously.
- Landing pages are about presentation, not complexity: product imagery and simple graphics beat generic icons.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Designer and YouTuber presenting the redesign.
- [[entities/builder-io|Builder.io]] (product): Sponsor of the video (sponsor segment excluded from rules and claims); also named in the intro alongside Cursor and Replit as a tool to build a first version.
- [[entities/cursor|Cursor]] (tool): Named as a tool people use to vibe code a first version.
- [[entities/replit|Replit]] (tool): Named as a vibe-coding tool (auto-captioned as 'replet').
- [[entities/notion|Notion]] (product): Cited as an app that uses emojis successfully.
- [[entities/phosphor-icons|Phosphor Icons]] (library): The icon library the presenter prefers for replacing emojis.
- [[entities/lucide|Lucide]] (library): An alternative interface icon library he says also works well.
- [[entities/resend|Resend]] (company): Cited as a software company using the pricing pattern he recommends.
- [[entities/supabase|Supabase]] (company): Cited as using the same pricing pattern (auto-captioned as 'superbase').
- [[entities/figma|Figma]] (tool): The redesign files are shared as Figma files.
- [[entities/vibe-coding|Vibe coding]] (concept): Building software by prompting AI tools; the source of the UI mistakes discussed.
- [[entities/kpi-cards|KPI cards]] (concept): Metric tiles that AI repeats across pages; replaced with charts and two-column layouts.
- [[entities/micro-charts|Micro charts]] (concept): Small charts added to KPIs to add relevant information and color.

## Topics

- [[topics/saas-product-ui|SaaS product UI]]: The whole video is a redesign of a vibe-coded SaaS URL shortener: dashboard, sidebar, cards, create-link form, billing and usage, analytics and landing page.
- [[topics/ai-assisted-design|AI-assisted design]]: Lists tell-tale signs of AI-generated UI (emojis, bright clashing colors, repeated KPIs, gradient letter avatars, cards that do nothing) and says not to let AI choose colors or layout; AI handles logic well if told to.
- [[topics/icons-and-imagery|Icons and imagery]]: Replace emojis with an interface icon library such as Phosphor or Lucide; use icons in info rows for a splash of color; use product imagery instead of generic icons on landing pages.
- [[topics/color|Color]]: Don't let AI pick colors; the dashboard changes backgrounds from dark blue to dark green and moves color into charts rather than buttons and icons.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: Don't repeat KPIs across pages; add micro charts to KPIs; use a two-column layout with small donut charts for usage; replace a plain bar chart with a shaded region map plus the data listed beside it.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Strip stats like click counts from sidebar items, left-align and tighten spacing, replace the gradient letter avatar with an account card whose links open in a popover, and group settings with billing and usage.
- [[topics/modals-and-popovers|Modals and popovers]]: A sparse create-link flyout becomes a modal; account links are tucked into a popover opened on click.
- [[topics/cards-and-sections|Cards and sections]]: Busy link cards get calmer by collapsing buttons into a triple-dot menu, collapsing chips to icons, centering the date and moving clicks to the right; cards that do nothing are removed.
- [[topics/forms-and-inputs|Forms and inputs]]: Collapse advanced options by default in the create-link form and add the missing options (custom domain switch, description) in a layout that lets more fields slot in.
- [[topics/paywalls-and-pricing-pages|Paywalls and pricing pages]]: Cut five plans down, drop unnecessary elements, shrink plan names and enlarge monthly cost, show the actual discount, show what the next plan adds, rename the business plan to enterprise, and add billing email and payment method.
- [[topics/visual-hierarchy|Visual hierarchy]]: Size elements by what users care about: plan name smaller, cost per month larger; drop unnecessary elements.
- [[topics/landing-pages|Landing pages]]: Vibe-coded landing pages lose most customers; add graphics such as skewed link cards and edited images of the product's own screens instead of generic icons, because better presentation means better conversion.

## Notable Claims

- Swapping emojis for professional icons already makes a card look better. Evidence: already starts looking better
- AI always goes for bright colors that don't work well together. Evidence: They always go for bright colors
- The same four KPIs appear three times in a small app, which gives away that AI built it. Evidence: these four KPIs at the top
- AI loves to make gradient profile circles with letters in them. Evidence: gradient profile circles with letters
- AI sets up logic and features well if you tell it to. Evidence: AI sets up logic well if you tell it to
- Layout is where you can spend the least time and see the largest changes, because AI is generally bad at complex layouts and cards. Evidence: least amount of time and see the largest
- Cards that don't do anything are a common pattern in AI-built apps. Evidence: this card doesn't do anything
- A tabbed billing and usage layout scales: documents, integrations or AI can each become another tab. Evidence: easy to add another tab and go
- The pricing pattern of showing the discount and what the next plan adds is common in software like Resend and Supabase. Evidence: extremely common for softwares like resend
- Landing pages are where a vibe-coded product loses most of its customers. Evidence: This is where you'll lose most of your customers
- SaaS landing pages have a standard of quality that establishes trust, even subconsciously. Evidence: establishes trust, even subconsciously
- Generally, the better the presentation, the better the conversion. Evidence: the better the conversion
- On the analytics page alone, changing a few charts and adding some icons created a big change. Evidence: just by changing a few charts

## Quotes

> never let an AI choose any of your colors
> AI is generally pretty bad at putting together complex layouts and cards
> Landing pages aren't about complexity, they're about presentation.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Builder.io in the middle of the video and in the description; excluded from rules.
- Caveat: Self-promotion: points to his previous video on software color theory and to Figma files on kolejain.com.
- Caveat: Opinion from a single redesign of one URL shortener; the claims about trust and conversion are not backed by data in the video.
- Caveat: Most changes are shown on screen; the transcript does not give exact colors, sizes or spacing values.
- Caveat: He assumes the standard and team plans are discounted ('At least we're going to assume that it is').
- Caveat: Auto-caption errors: 'replet' is Replit, 'flyyou' is flyout, 'SAS' is SaaS, 'doughut' is donut, 'superbase' is Supabase.
- Caveat: Published 2026-02-12; the tools named (Cursor, Replit, Builder.io) reflect that date.

### Rules and practices

- **should** (components, all): Don't use emojis as interface icons in product UI; use an interface icon library such as Phosphor or Lucide instead. Why: Emojis are the first, painfully obvious giveaway of AI-built UI; swapping to more professional icons makes the card start looking better right away. He admits some apps, like Notion, use emojis successfully. [Get rid of the emojis]
- **must** (color, all): Never let an AI tool choose your colors; choose the palette yourself. Why: AI always goes for bright colors that don't really work well together. [never let an AI choose any of your colors]
- **consider** (color, all): Add color to a dashboard through charts that carry information (for example micro charts on KPIs) rather than through colored buttons and icons. Why: In the redesign this added much more relevant information and color at the same time. [color through charts instead of buttons and icons]
- **should** (layout, all): Don't repeat the same KPI cards on several pages of the app. Why: Just as too many dashes give away AI-written text, the same four KPIs showing up three times in a small app gives away that AI built it. [show up not once, not twice, but three]
- **must** (layout, all): Never let an AI tool choose your layout; design it yourself. Why: AI is generally pretty bad at putting together complex layouts and cards, so this is where little time gives the largest change. [Never let an AI choose your layout either]
- **should** (layout, all): Keep sidebar items to navigation labels; remove stats such as click or link counts from them. Why: In a section like custom domains or teams those numbers don't matter; if people need them they visit the dashboard or analytics tab. [the amount of clicks and links]
- **consider** (components, all): Replace a gradient initial-letter profile circle with an account card, and tuck account links into a popover that opens on click. Why: Gradient letter circles are a pattern AI loves; the account card frees the sidebar from extra links, and settings, billing and usage can be collapsed together. [swap this for an account card]
- **consider** (components, all): When list cards feel busy, collapse their action buttons into a triple-dot menu and reduce chips to icons. Why: The cards were feeling a little busy. [collapse these buttons into a triple dot menu]
- **consider** (patterns, all): Use a modal instead of a side flyout when a form has only a few fields and leaves lots of empty space. Why: The create-link flyout was sparse with fields even though there was a ton of space, so a modal was more fitting. [a modal is probably more fitting]
- **consider** (patterns, all): Collapse advanced options by default in creation forms. Why: He pairs it with giving the create-link form a more modern look; the new layout also lets more features slot in easily. [collapse down the advanced options by default]
- **should** (components, all): Don't keep cards that don't do anything; remove them. Why: Cards with no function are a pattern you see a lot with AI. [this card doesn't do anything]
- **consider** (layout, all): Organize account areas like billing and usage into tabs. Why: As things scale and you need to add documents, integrations or AI, it's easy to add another tab. [easy to add another tab and go]
- **consider** (layout, all): Present usage figures in a simple two-column layout with small donut charts instead of generic KPI cards. Why: The KPIs were very vibe-coded; the two-column layout really elevates things. [a real simple two column layout]
- **should** (patterns, all): Offer fewer than five pricing plans; drop at least one. Why: Having five plans is really not ideal. Values: five plans. [having five plans is really not ideal]
- **should** (typography, all): On pricing cards, make the plan name smaller and the cost per month larger. Why: No one cares about the name, and people do care about the cost. [Drop the size of the name]
- **should** (patterns, all): Show the actual discount the user is getting on a discounted plan. Why: It is very important; without it plan prices look out of order (standard cheaper than hobby) until you realize the plan is discounted. [Showing the actual discount the user is getting]
- **should** (patterns, all): On the pricing page, show what the next plan includes that the current plan doesn't have. Why: He presents it as part of a pricing pattern that is extremely common for software like Resend or Supabase. [what the next plan includes]
- **consider** (patterns, all): Add a billing email and payment method to the billing tab. Why: Added 'for good measure'; the source gives no other reason. [billing email and payment method]
- **consider** (patterns, all): In analytics, add a toggle that splits totals into individual items (for example individual links) so they can be compared. Why: It is super easy to implement and genuinely useful: low-hanging fruit that makes the app better. [add a toggle to split into individual links]
- **consider** (components, all): For location data, use a map with shaded regions and list the actual data beside it instead of a plain bar chart. Why: It gives a much richer experience than a boring bar chart. [show them a map with shaded regions]
- **should** (patterns, web): On SaaS landing pages, use graphics such as images of your own product screens or simple skewed cards instead of generic icons. Why: Landing pages are where you lose most customers if vibe-coded; a standard of quality establishes trust, and better presentation generally means better conversion. [what we really need are some graphics]
- **consider** (process, all): Tell the AI exactly which logic and features you need, and check for missing options, instead of expecting it to add them on its own. Why: AI sets up logic well if you tell it to, and the same is true for features; the vibe-coded create-link form was missing options like custom domain and description. [AI sets up logic well if you tell it to]
- **consider** (layout, all): In a sidebar, left-align the items and tighten the spacing. Why: Part of the sidebar cleanup in the redesign; the source gives no further reason. [align this to the left and tighten up the spacing]
- **consider** (layout, all): On pricing cards, drop unnecessary elements and use spare width to tune the hierarchy. Why: The hierarchy wasn't bad but could be tuned up with the extra width available. [drop some of the unnecessary elements]
- **consider** (patterns, all): Rename a high-volume plan to Enterprise when customers at that volume probably need more than a fixed plan. Why: Business became enterprise because if you need 50,000 links per month, you probably need more. Values: 50,000 links per month. [Business has become enterprise]
- **consider** (components, all): Add helpful icons to dense information rows so they carry more useful information and a splash of color. Why: In the analytics redesign the icons made the row more useful and also added a splash of color. [helpful icons that also add a splash of color]
- **consider** (process, all): When creating features for a SaaS app, look for low-hanging fruit: simple features that are easy to build and make the app much better. Why: Simple features like splitting analytics into individual links are super easy to implement and genuinely useful. [don't forget about the lowhanging fruit]

### Decisions it informs

- Where should the interface icons come from? (`Q-icon-01`)
  - Emojis: An obvious sign the UI was generated by AI. When: The source gives no rule; it only notes some apps, like Notion, use them successfully.
  - Interface icon library (Phosphor, Lucide or similar): Looks more professional right away. When: The source's recommendation for SaaS product UI.
  - Recommendation: Use an interface icon library; he likes Phosphor, and Lucide or others work well too.
- Should a create form open in a side flyout or a modal? (`Q-pattern-01`)
  - Side flyout: A panel that slides in; with only a few fields it looks sparse, with lots of empty space. When: Not recommended here for a form with few fields [inferred].
  - Modal: Fits a form with few fields; the new layout also lets more features slot in easily. When: When the form has few fields relative to the space a flyout gives.
  - Recommendation: Modal, because the flyout was sparse with fields even though there was a ton of space.
- How should the signed-in account show in the sidebar?
  - Gradient profile circle with a letter: A common AI-generated look. When: Not recommended.
  - Account card with a popover: A card that opens a popover on click holding account links, with settings, billing and usage grouped together. When: When the sidebar has extra account links to tidy away.
  - Recommendation: Swap the gradient letter circle for an account card and move links into a popover.
- How should actions on busy list cards be shown?
  - Separate buttons and chips on each card: The card feels busy. When: Not recommended when cards already hold a lot.
  - Triple-dot menu, chips as icons: Calmer cards: actions tucked into a menu, chips reduced to icons, date centered and clicks moved to the right. When: When cards feel busy.
  - Recommendation: Collapse the buttons into a triple-dot menu and chips to icons.
- How should usage figures be shown on a billing and usage page?
  - KPI cards: Looks vibe-coded and lame. When: Not recommended here.
  - Two-column layout with small donut charts: Simple and really elevates the page. When: For usage against limits.
  - Recommendation: A simple two-column layout with a few small donut charts.
- How should location analytics be shown?
  - Bar chart: Boring. When: Not recommended here.
  - Map with shaded regions and the data listed beside it: A much richer experience. When: When the data is about places.
  - Recommendation: A map with shaded regions and the actual data to the left.
- How should a growing account area (billing, usage and more) be structured?
  - No tabs (the AI-generated page) [inferred]: The page the redesign nuked and rebuilt from scratch. When: Not recommended here.
  - Tabs: Each area gets its own tab; new sections like documents, integrations or AI can be added as another tab. When: When the product will keep adding sections.
  - Recommendation: Tabs, because the layout scales easily.
- How many pricing plans should be offered?
  - Five plans: A bit of a mess. When: Not recommended.
  - Fewer plans, with Business renamed Enterprise: Hobby probably makes the most sense to drop; Business becomes Enterprise because anyone needing 50,000 links per month probably needs more. When: Here, where five plans is too many.
  - Recommendation: Drop at least one plan (hobby probably makes most sense to drop).
- What visuals should a SaaS landing page use?
  - Generic feature icons: Looks vibe-coded; he calls them lame. When: Not recommended.
  - Product graphics: Skewed link cards and slightly edited images of the product's own screens elevate the page. When: For feature sections on a SaaS landing page.
  - Recommendation: Use graphics made from the product itself, because presentation drives trust and conversion.
- Should advanced options in a create form show by default? (`Q-pattern-03`)
  - All options visible: The vibe-coded starting point before the redesign [inferred]. When: Not recommended here.
  - Advanced options collapsed by default: Part of giving the create-link form a more modern look. When: For creation forms with advanced options.
  - Recommendation: Collapse the advanced options by default.
- Where should a dashboard get its color?
  - Colored buttons and icons: The AI-chosen bright colors that don't really work well together. When: Not recommended.
  - Charts that carry information: Micro charts on expanded KPIs add much more relevant information and color at the same time. When: On dashboards with KPIs.
  - Recommendation: Add color through charts instead of buttons and icons.

### Process

1. Swap emojis for icons: Replace emojis with an interface icon library such as Phosphor or Lucide.
2. Take over the colors: Replace AI-chosen bright colors (the example changes backgrounds from dark blue to dark green), remove some icons, and add color through charts such as micro charts on expanded KPIs.
3. Rework the layout: Remove repeated KPIs, clean the sidebar of stats, add missing sections like analytics, left-align and tighten spacing, swap the letter avatar for an account card with a popover, and simplify busy cards.
4. Fill in the features: Tell the AI what logic and options you need; pick the right container (modal vs flyout), collapse advanced options, and add missing options like custom domain or description.
5. Rebuild billing and usage: Remove cards that do nothing, retitle, split into tabs, show usage with a two-column layout and donut charts, and fix pricing plans (fewer plans, price over name, visible discount, next plan's extras, billing email and payment method).
6. Improve analytics with low-hanging features: Remove the repeated KPIs and tabs, move actions, add a toggle to compare individual items, add icons to info rows, and replace a plain bar chart with a shaded map and the data beside it.
7. Finish the landing page: Apply the same color and layout principles and add graphics made from the product (skewed cards, edited screenshots) instead of generic icons.

### Examples and visual references

- Redesign of a vibe-coded URL shortener (The presenter's example app): Before and after of a whole SaaS app: dashboard, sidebar, link cards, create-link form, billing and usage, analytics and landing page.
- Dashboard color and KPI fix (URL shortener dashboard): Backgrounds changed from dark blue to dark green, icons removed, KPIs expanded with micro charts, so color comes from data rather than buttons.
- Emojis used well (Notion): Named as an app that successfully uses emojis, the exception to the rule.
- Account card with popover (URL shortener sidebar): Replaces a gradient letter avatar; account links open in a popover on click, with settings, billing and usage grouped.
- Calmer link cards (URL shortener links list): Buttons collapsed into a triple-dot menu, date centered, chips reduced to icons, clicks moved to the right.
- Create-link modal (URL shortener): A sparse flyout turned into a modal with advanced options collapsed and new options for switching custom domain and adding a description.
- Usage tab (URL shortener billing and usage page): Two-column layout with small donut charts in place of KPI cards.
- Pricing pattern with discount and next-plan extras (Resend, Supabase): Named as software where this pricing pattern is extremely common: showing the actual discount and what the next plan includes that the current plan doesn't.
- Location analytics map (URL shortener analytics tab): Map with shaded regions and the data listed to the left, replacing a bar chart; a toggle splits totals into individual links.
- Landing page graphics (URL shortener landing page): Skewed link cards and a slightly edited image of the analytics page (and of password protection) instead of generic icons.

### Numbers

- four KPIs: The same four KPIs appear at the top and show up three times in a small AI-built app. [these four KPIs at the top]
- three times: How often the same four KPIs appear in the small vibe-coded app. [not once, not twice, but three times]
- five plans: Number of pricing plans in the vibe-coded app; he says this is not ideal. [having five plans is really not ideal]
- 50,000 links per month: The business plan's limit, which he says means the tier should be enterprise. [if you need 50,000 links per month]

<!-- /od:learn -->
