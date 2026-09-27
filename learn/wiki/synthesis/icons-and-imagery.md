---
type: synthesis
title: Icons and imagery
created: 2026-09-24
updated: 2026-09-24
sources:
  - 9WVt1CelBfg
  - AH_ugxmLeUM
  - A_Ozpb0XDuw
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - Ksx9C2-3yMo
  - Lp6ey4AyDzA
  - MZSm6MA8bww
  - NtZeYmTMuo4
  - P2ksReDwWkE
  - PDcQJOPby1k
  - RCneB_MQ7qs
  - SfX43uIubj4
  - ToJiXPTNnLY
  - V3Omp1hm0Sg
  - Yr2uIcFZDDQ
  - adev-changelog
  - eMMiLeo_UGI
  - eeN7yUcIWbw
  - ek-the-magic-of-clip-path
  - ld1zhQMXxXU
  - neE6wOuBIP8
  - pGYLZyBE32o
  - sonner-styling
  - ulSOdTgoGeY
  - xHD01_Onac0
tags:
  - od-area-shape-depth
---

# Icons and imagery

## In short

Icons are small symbols that help people scan a screen and act. Imagery is the photos, product screenshots, illustrations and 3D art that show what a product is and who it is for. The sources say to take every icon from one library so they match, keep icons simple and about as tall as the text line, and leave them uncolored unless the color shows a status. Don't use emojis as interface icons. Give unfamiliar icons a tooltip, or better, choose icons people recognize at a glance. For images, quality and relevance matter most: real product or audience images beat unrelated stock, the image's focal point should stay clear, and text on a photo needs a gradient behind it.

## House standards

- **STD-visual-details-28** (must): don't ship misaligned icons (or jittery scrolling, or layouts that break on rotation).
- **STD-visual-details-38** (should): use metaphors that are neither too literal nor too abstract (a trash can means delete) and honor their physics.
- **STD-mobile-touch-09** (must): touch targets of at least 44×44pt (iOS), 48dp (Android) or a 44px hit area (web). When an icon is smaller, grow the hit area, never the icon.
- **STD-mobile-touch-05** (must): pressed elements scale to 0.97 as a whole, so their label and icons come along.
- **STD-enter-exit-origin-09** (must): a tooltip enters and exits between `opacity: 0` with `scale(0.97)` and its resting state, from its trigger, in 125ms on the ease-out curve.
- **STD-enter-exit-origin-10** (must): delay only the first tooltip in a group, then open neighbouring tooltips instantly with no animation.
- **STD-springs-gestures-05** (must): a spring never overshoots on UI that appears without a gesture behind it, such as a popover or tooltip.
- **STD-accessibility-motion-18** (must): the picker's icon-only replay button carries `aria-label="Replay animation (R)"`. This is the only standard that names an icon-only button's label, and it is specific to the picker.
- **STD-enter-exit-origin-26** (should): reveal images with `clip-path: inset()`, from `inset(0 0 100% 0)` to `inset(0 0 0 0)` on the ease-in-out curve, not by animating width, height or an overflow wrapper. **STD-easing-duration-09** (must): nothing runs over 1s unless it is illustrative, and the 1s image reveal is that exception.
- **STD-when-to-animate-11** (must): decorative motion such as animated line drawing belongs on marketing pages and illustrations, never on functional charts.
- **STD-enter-exit-origin-38** (should): set the transform-origin of every scaled or rotated element on purpose, SVG elements included.
- **STD-process-review-taste-55** (should): give coding agents written rule files per aspect of the interface, icons among them, each rule with its reason.

## What the sources teach

### One icon library, one style
- Mismatched icons (different fill, line width and style) hurt a design. Use one library: on an icon site, filter to interface icons and sort by stroke, width and corner, and download SVG. Feather and Phosphor are the presenter's Figma plugins [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Mixed-style icon sites make it hard to find several icons in one style, so use an icon pack. Feather is the presenter's go-to [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). On such a site, searching only "interface icons" returns the clean, simple ones [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Different icon styles can live in one design only when each sits in a visually separate area with a different job, such as navbar icons versus food icons [S-L19-045].
- For isometric icons, a customizable set (Isocons) lets you choose rounded or sharp corners and the stroke weight [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).

### No emojis as interface icons
- Emojis are the first, painfully obvious giveaway of an AI-built app in one redesign. Swapping them for an interface icon library such as Phosphor or Lucide improves a card at once, though some apps like Notion use emojis well [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- When prompting an AI to build UI, tell it to use an icon library, or it uses emojis [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).

### Size, detail and color
- Most icons are too large. Match the icon to the font's line height (24px in the example), then tighten the text [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Keep icons simple. A larger icon can carry more detail and a smaller one needs less [S-L19-057].
- For the most part, icons need no color: their job is to be recognizable symbols, and color is kept for status such as the active tab [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). On a dashboard, color should come from the data, such as a red icon in a chip for an urgent action [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- Softer positions: helpful icons in dense info rows add information and "a splash of color" [S-L19-061]. On marketing sites, feature icons can be drawn in the brand's accent colors, one icon per main feature [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]), or be solid brand color rather than gradient icons, with a gradient stroke on hover [S-L19-082].
- A state can show through the icon: when a recipe is saved, the save icon fills in and a red dot appears on the save tab [S-L19-045].

### Labels, tooltips and recognizable icons
- Well-known icons (house, bookmark, user) can stand alone. Less familiar icon-only buttons get a tooltip. Avoid bizarre icons [S-L19-045].
- Tooltips are missing on nearly all beginner dashboards; assume people won't understand all your icons [S-L19-056]. Secondary actions can appear on hover as an icon with a tooltip [S-L19-056].
- When there are many icons and little room for labels, show a tooltip only after the pointer rests for a full second. The demo uses a custom easing with a little bounce [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]). The magnifying glass is called the universally accepted search icon [S-L19-079].
- A later video argues the other way. Explaining harder with labels and tooltips makes a screen harder to read, and people are left guessing until an icon's tooltip appears. Use visuals people recognize at once (icons, diagrams, chips, avatars) or placement that explains the control [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- Replace an unclear icon (a minimize icon on a large module) with a labelled button. Start an alert with a leading icon, keep cut detail behind a kebab (three-dot) icon, and add a full-screen icon to chart cards [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Pick metaphors that fit the brand: a shield felt like Google, while Apple generally uses a lock. That redesign then dropped the icon for an isometric graphic [S-L19-082].

### Where icons earn their place
- Cards with no icons force people to read more; add icons and replace short text actions such as "save" [S-L19-045].
- Icons are called the secret to a great sidebar, and they get small hover labels and state changes [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- Show a relationship such as a route with icons and alignment instead of "from" and "to" labels [S-L19-052]. Put an avatar beside each actor in an activity log, because the eye finds people faster than names [S-L19-056] [S-L19-080].
- In Sonner toasts, the default success, info, warning, error and loading icons can be replaced for the whole app (`icons` prop), set on one toast (`icon`), or removed with `null` [S-L19-090] ([[sources/sonner-styling-styling-sonner|Styling – Sonner]]).

### Image quality and resolution
- A high-quality asset makes or breaks most landing pages [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]). Image quality can make or break a site, because images make up so much of it [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- Use a large, high-resolution photo when it is blown up, or it looks pixelated [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]). When searching for photos, filter to large images only [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).

### Show the product and the audience
- Swap stock images that have little to do with the product for the product itself (its dashboard). Leaning on stock images for a page's color misses; in the better version the color comes from the dashboard [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- On a SaaS landing page, replace generic icons with graphics: an edited image of your own product screen, or even simple skewed link cards [S-L19-061].
- A site with no images at all feels robotic. Images that relate to the audience are how a site connects with its users and builds trust [S-L19-062].
- A skincare site should lead with great product photos on a bright white background, using ready-made product mockups rather than renders built from scratch [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- In a portfolio, large, bright imagery should grab attention before any text. A case study needs a visual or GIF every couple of paragraphs, so the process can be understood from the images alone [S-L19-064] ([[sources/ToJiXPTNnLY-professional-portfolio-breakdown-why-is-theirs-so-much-better|Professional Portfolio Breakdown — Why Is Theirs So Much Better?]]).
- Images help people recognize things. Photos in a navigation menu show which product is which (Rivian's truck and SUV) [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]), and an image in a card adds color and makes scanning easy [S-L19-052].

### Composition: focal point, crop and consistency
- Keep the hero image's focal point clear by placing text and stats around it, and pick an image whose background is calm next to the text [S-L19-043].
- Never put hero text over the focal point. Choose a zoomed-out photo for a full-screen hero so the subject doesn't overwhelm it. Keep a set of images consistent: don't mix a photo that has a background with a cut-out that doesn't [S-L19-065].
- Pick images for thin bands and multi-image layouts with their crop, aspect ratio and orientation in mind [S-L19-060], and choose a bento arrangement that suits the images' orientation [S-L19-065].
- When scattering image assets around text, put larger pieces below and smaller ones on top, and always keep a safe margin around the text. It should look random but be ordered [S-L19-062].

### Text on images
- Don't cover the whole image with an overlay just to make text readable. Use a linear gradient that shows the image and then fades into a text-readable background, with an optional progressive blur on top [S-L19-052].
- Put a gradient under text that sits on a photo [S-L19-060], and behind text in a full-photo lightbox card. When legibility over the photo is uncertain, move titles above the images [S-L19-065].
- If a hero photo hurts contrast, first find a better photo (right mood, nothing in the way, good light), then add a subtle overlay if it is still too bright [S-L19-049]. A little noise on image or color backgrounds adds texture and helps text contrast [S-L19-062].

### Photo treatments
- Remove the background from a photo of a single object, crop and zoom into product shots, and mask images into shapes that match the site's style. Use AI images only where they fit [S-L19-085].
- To extend a photo's sky, duplicate, flip and crop it instead of using AI [S-L19-065]. For cut-out lettering over an image, pick one with nothing important where the cut-out will remove it [S-L19-060].

### Illustration, 3D and style
- Imagery style sets the vibe: blobs and fun colors are most playful, doodles sit in the middle, and realistic imagery reads professional. Illustrations around a hero show what the product is about, but stop before the next one tips the hero into clutter [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- Hand-drawn scribbles and arrows contrast well with bold, crisp text [S-L19-050].
- The clay effect (inner shadows on opposite edges) suits isometric art and illustrations that need some depth [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- A 3D logo can start from the logo's Figma SVG, extruded and lit in Spline or Blender. Check a rotating asset for dark spots and fix the lighting [S-L19-046] ([[sources/A_Ozpb0XDuw-how-hard-is-it-to-really-make-a-no-code-3d-animated-website|How hard is it to REALLY make a no-code 3D animated website?]]). Resource picks include Burst (stock photos), Endless Tools (3D) and Handy Arrows [S-L19-073].
- animations.dev teaches its hero illustration animations from SVG basics: the coordinate system and `viewBox`, path syntax, stroke properties for path drawing, and correct transform origins [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).

### Motion on images
- Reveal an image by animating `clip-path` from `inset(0 0 100% 0)` to `inset(0 0 0 0)` over 1s with `cubic-bezier(0.77, 0, 0.175, 1)`. Trigger it once, when at least 100px is in view. Build before/after sliders by clipping the top image with `inset(0 50% 0 0)` from the drag position [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Hover effects from the practitioners, none with timings:
  - image cards zoom out and pop up a call to action [S-L19-065];
  - image cards blur, grow and show extra text [S-L19-082];
  - key words pop out an image on hover [S-L19-079];
  - photos slowly zoom in or out [S-L19-085];
  - morphing images keep each change small so the browser doesn't stutter [S-L19-050].

## Where they agree and disagree

- **One library (agree).** Four Kole Jain videos [S-L19-045] [S-L19-057] [S-L19-061] [S-L19-086] and DC-L05-01 (one icon family per product) agree. Stage 17 also warns against mixing two libraries' strokes in one toolbar, and allowing different styles only in separate areas [S-L19-045] fits that [inferred]. The named libraries partly overlap with the research: Phosphor and Lucide are in DC-L05-01's list, but Feather is not. There is also a small tension in Kole Jain's own advice: one video warns that mixed-style icon sites are hard to use [S-L19-057], while two others use such a site filtered to interface icons [S-L19-045] [S-L19-082].
- **Size to the line height (agree).** "Icon size equals the line height" [S-L19-052] is DC-L05-05's heuristic, which the research had marked [inferred]. A practitioner now backs it, though only in one video.
- **Color (mostly agree).** Uncolored icons with color only for status [S-L19-051] [S-L19-056] match DC-L05-08's default: one neutral icon color, semantic colors only on status icons, no decorative multicolor in UI chrome. Accent-colored feature icons on marketing pages [S-L19-062] [S-L19-082] fit DC-L05-11's pictogram tier, which is for marketing only [inferred]. Adding icons for "a splash of color" in product rows [S-L19-061] leans against DC-L05-08.
- **Tooltips (disagree, same presenter).** Tooltips are treated as a must [S-L19-056] and as the fallback for unfamiliar icons [S-L19-045] [S-L19-079]. The newest video says not to rely on them [S-L19-080]. The research sides with the newer view: DC-L05-07 (with NN/g) wants labels visible rather than hover-only and allows icon-only for about a dozen universal actions, and DC-L05-09 cites NN/g's 5-second rule (use a word if a good icon takes more than 5 seconds to think of). Tooltips also don't exist on touch screens [inferred].
- **Tooltip motion (conflict with house standards).** The 1-second delay [S-L19-079] fits STD-enter-exit-origin-10 (delay the first tooltip). The standard sets no delay value, so 1s is a single-video number. The demo's bouncy easing conflicts with STD-springs-gestures-05 and STD-enter-exit-origin-09 (125ms ease-out, no overshoot), and the standards win.
- **Text on images (agree, and fills a gap).** Gradient scrims [S-L19-052] [S-L19-060] [S-L19-065] are the "gradient scrim" option of DC-L05-16, which the research had marked [inferred] with no official source. Q-img-02 defaults to text beside images with a scrim only on heroes. "Move titles off the image when unsure" [S-L19-065] agrees with that default.
- **Stock versus real (agree, one tension).** Product and audience images over unrelated stock [S-L19-072] [S-L19-061] [S-L19-062] match DC-L05-14, which says to use real product and people photos where trust matters and to reject any image another company could have made. But other videos recommend more stock sites [S-L19-073] and AI images "where they fit" [S-L19-085], while the Q-img-01 hook warns that AI images show artifacts and stereotypes.
- **Illustration (agree).** Imagery style setting the vibe [S-L19-063] matches DC-L05-19 (style follows personality). "Stop before clutter" [S-L19-063] matches DC-L05-20, where overusing illustration raises cognitive load, which the research marked [inferred]. 3D as a hero or marketing centerpiece [S-L19-046] fits DC-L05-21, which keeps 3D and Lottie for onboarding, celebration and marketing.
- **Image motion (house rule applies).** The 1s clip-path reveal [S-L19-010] is allowed only because it is illustrative (STD-easing-duration-09). The practitioners' hover zooms and image morphs have no timings, so they should be checked against the house duration and frequency rules before becoming defaults [inferred].

## Decisions this informs

- **Q-icon-01** (library): one open-source set on the web, such as Phosphor or Lucide. Feather needs a licence check before it is offered [S-L19-045] [S-L19-057] [S-L19-061] [S-L19-086].
- **Q-icon-02** (outlined or filled, rounded or sharp): filter icons by stroke, width and corner [S-L19-045]. Isometric sets expose rounded or sharp corners [S-L19-073]. A fill swap marks a saved state [S-L19-045].
- **Q-icon-03** (stroke): matching line width across the set [S-L19-045], with detail scaled to size [S-L19-057].
- **Q-icon-04** (sizes): tie the icon size token to the adjacent line height [S-L19-052].
- **Q-icon-05** (labels and color): several analyses map here [S-L19-045] [S-L19-051] [S-L19-079]. Keep `labels-default` plus universal icons only. Tooltips are an addition, not a replacement for labels [S-L19-080]. Keep icons mono, with status colors only.
- **Q-icon-07** (SVG or font): download SVG [S-L19-045], in line with DC-L05-10's SVG source of truth.
- **Q-img-01** (photography): real product and audience images, a clear focal point and high resolution [S-L19-062] [S-L19-072] [S-L19-043] [S-L19-065].
- **Q-img-02** (image shapes, text on images): gradient scrim, a better photo before an overlay, titles off the image when unsure, and one consistent treatment per image set [S-L19-052] [S-L19-049] [S-L19-065] [S-L19-085].
- **Q-img-03** (avatars): show avatars wherever people are referenced [S-L19-056] [S-L19-080]. The sources say nothing about avatar shape.
- **Q-img-04** (illustration): vibe scale (blobs, doodles, realistic), hand-drawn accents, clay for isometric art, and a clutter limit [S-L19-063] [S-L19-050] [S-L19-058].
- **Q-img-05** (pictograms): accent-colored feature icons and product graphics on marketing pages [S-L19-062] [S-L19-061].
- **Q-img-06** (3D, Lottie, emoji): 3D logo workflow [S-L19-046], 3D resources [S-L19-073], and no emojis as UI icons [S-L19-061] [S-L19-086].
- **Q-brand-01 / Q-brand-08**: the imagery vibe follows the personality sliders [S-L19-063], and the asset inventory should ask for product screenshots and audience photos [S-L19-062] [S-L19-072] [inferred].

## Visual examples worth showing

- The recipe app's mismatched top icons fixed with one library. Cards gain icons, and the save icon fills with a red dot on the tab [S-L19-045].
- A file-storage app's colored tab icons, redone as uncolored icons with color only on the active tab [S-L19-051].
- A card with emojis next to the same card with Phosphor icons [S-L19-061].
- Icons sized to a 24px line height next to oversized icons [S-L19-052].
- A hero whose text and stats frame an open focal point [S-L19-043]. The EV hero with text over the car, then text tucked behind the subject [S-L19-065].
- An image card with a gradient fading into a readable area, plus a progressive blur version [S-L19-052].
- A level-one page with stock images next to a level-three page showing the product dashboard [S-L19-072].
- The restaurant site's scattered image assets, larger below and smaller on top, with a safe margin around the headline [S-L19-062].
- The vibe scale on three heroes: blobs, doodles and realistic imagery [S-L19-063].
- A clip-path image reveal and a before/after comparison slider [S-L19-010].
- Rivian's navigation with product photos [S-L19-050]. A delayed icon tooltip and a magnifying glass expanding into a search bar [S-L19-079].
- A Sonner toast with swapped and removed icons [S-L19-090]. A clay isometric illustration [S-L19-058]. A spinning 3D logo [S-L19-046].

## Open questions

- Should Q-icon-05 treat tooltips as required for icon-only controls [S-L19-056] or as a last resort [S-L19-080]? And what replaces them on touch devices?
- Feather is recommended twice but isn't in DC-L05-01's library list. Its licence and upkeep need checking before it is offered.
- What stops and opacities should a `gradient.scrim` token use? The sources show gradients but state no values.
- How should OpenDesigner treat AI-generated images, which one source allows "where they fit" [S-L19-085] and the Q-img-01 hook flags?
- Should icon color rules differ by surface: mono in the product, accent colors allowed on marketing pages [S-L19-051] [S-L19-062]?
- Should the builder derive the icon size token from the body line height automatically, as the "line height" rule suggests [S-L19-052]?
