---
type: synthesis
title: Figma and design tools
created: 2026-09-24
updated: 2026-09-28
sources:
  - AH_ugxmLeUM
  - A_Ozpb0XDuw
  - If7iCPDy2vk
  - Lp6ey4AyDzA
  - MZSm6MA8bww
  - NtZeYmTMuo4
  - P2ksReDwWkE
  - VPeTgU7la34
  - YbLF42BaoZs
  - c1TvOcKdBVE
  - eeN7yUcIWbw
  - ek-the-magic-of-clip-path
  - fL1X2Mw6s3w
  - gKM6b2EnW1k
  - jSxxAFxjxbU
  - ld1zhQMXxXU
  - lkKGQVHrXzE
  - nl8OFGdx75w
  - t7mpEDXzjCg
  - xHD01_Onac0
tags:
  - od-area-process
---

# Figma and design tools

## In short

Figma is the everyday tool in most of these sources, and the videos share many small habits that make it faster and tidier: auto layout for anything with padding, one set of styles, variables and components, a nudge amount that matches your spacing grid, layer names that let Smart Animate and multi-edit find the right layers, and prototypes checked on the real screen size. The sources also show Figma's limits, where a dedicated tool does better (mesh gradients, arrows, 3D, animation), and newer workflows where an AI writes the design in code and Figma is used only for polish or for vector graphics such as logos, or where an agent builds straight into a design file through an MCP connection (Paper in one Mobbin demo). Figma's own defaults are not always good: its preset shadow is called too harsh, and designing zoomed out made one presenter's type and spacing far too large. Everything here is practitioner opinion tied to the Figma of its date (2024 to 2026), and none of it overrides OpenDesigner's own token file, which Figma only mirrors.

## House standards

No non-negotiable source is mainly about Figma. These house standards govern the values that end up in any design tool:

- `STD-visual-details-26` (must): build from the project's existing tokens (colors, radii, spacing, fonts, easing and duration) and extend them; never add a parallel set or hand-type an approximate value.
- `STD-visual-details-27` (should): make every spacing, timing and alignment value a deliberate choice you can defend.
- `STD-visual-details-14` (should): separate surfaces with a semi-transparent shadow rather than a solid, opaque border.
- `STD-easing-duration-02` (must): use the named strong curves, or a curve from easing.dev or easings.co, never a hand-rolled one; this applies to curves set in a prototyping tool once they reach code.
- `STD-process-review-taste-33` (must): judge touch and gesture feel on real hardware; an emulated or shrunken screen never counts as verified.

Also from `skills/opendesigner/references/guardrails.md`, section 6: before writing to Figma or Paper, confirm the target file, and for Figma suggest working on a duplicate.

## What the sources teach

### Structure: auto layout, styles, variables, components

- Use layout grids and align to them, and rebuild wonky cards and chips with auto layout, turning off vertical trim for pixel-perfect control. For consistency, use styles for colors, variables for measurements and components for UI elements [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Always build a chip with auto layout: select the text, press Shift+A, then add the background, round the corners and set the padding [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). Shift+A also adds auto layout while building micro-interaction prototypes [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- Multi-edit selects matching layers across frames and changes them together; it finds them by layer name and grouping position, so consistent naming matters. Shift+A adds auto layout to several frames at once, and a section limits a multi-edit to the frames inside it [S-L19-074] ([[sources/fL1X2Mw6s3w-figma-update-everything-in-under-2-minutes|Figma Update: Everything In Under 2 Minutes]]).

### Settings and small habits

- Switch the color picker from hex to HSB to change hue, saturation and brightness separately; turn iOS corner smoothing up to the maximum to taper corners slightly; and on an 8 pixel grid, change the nudge amount in preferences from 10 to 8 so small moves stay on the grid [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]). The captions garble the grid size; 8 is inferred from the nudge change.
- Figma's preset drop shadow of 25% opacity can almost always drop to 15 to 20% [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). Another video calls the default shadow way too harsh and softens it with a light gray color and much more blur, or removes it [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Designing zoomed out in Figma led one presenter to oversized type and spacing; preview on the target screen, on desktop or by mirroring the prototype in the Figma mobile app, and leave room for the browser bar [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- The same creator lost a lot of time on one project by deleting and misplacing Figma files [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Figma recipes for visual effects

- Four effects built only from layer order, blend modes, inner shadows and blurs: a kaleidoscope, a clay look, metal (including a 20% colored fill for rose gold) and a plugin-free mesh gradient of stacked blurred circles; the kaleidoscope uses one plugin, Noise & Texture [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- A dark glass surface: a partly transparent rectangle, a subtle gradient, background blur, a one pixel border and a soft inner shadow [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).
- A cut-out image text effect is made with subtract; each section is wireframed first and then designed [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]).
- A sticker comes from the star tool with 12 points, rounded; circular text needs a text-on-path plugin [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- The dashed text in a clip-path demo is a stroke drawn in Figma and converted to SVG [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Hover effects for a layouts file are prototyped with Smart Animate, and the file is free to download [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).

### Prototyping in Figma

- Smart Animate animates layers with the same name across frames; use layer opacity rather than fill opacity; "while hovering" and "on click" triggers; custom springs set by stiffness and damping [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- The prototype panel's after-delay triggers, ease in and out, custom bezier handles, instant navigation and the flow starting point chain frames into a page-load sequence [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]).
- Figma prototypes cannot bind the Command or Shift key [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]). For more, see [[synthesis/prototyping|Prototyping synthesis]].

### Other tools around Figma

- FigJam for user flows, Figma or paper for wireframes, and Google Forms for research data [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).
- For 3D web assets, Spline runs in the browser with a Figma-like interface but exports video only on paid plans; Blender is free, the industry standard and harder. The logo starts as an SVG from Figma, and the page was built without code in Wix Studio [S-L19-046] ([[sources/A_Ozpb0XDuw-how-hard-is-it-to-really-make-a-no-code-3d-animated-website|How hard is it to REALLY make a no-code 3D animated website?]]).
- Uiverse elements paste into Figma with a Copy to Figma button; the Relume kit is a large Figma Community file; Phase animates Figma designs more easily than plugins or After Effects; Photo Gradient and Handy Arrows do what Figma's gradients and pencil tool cannot [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).

### AI output in and out of Figma

- Ask the AI for HTML and CSS, download it, and import it with the HTML to design plugin (File tab, components setting on so hover effects come across). Because it is HTML and not an image, every element stays editable. Small fixes such as a sticky sidebar or exact alignment are faster in Figma than by re-prompting [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Steve Schoger designs a whole marketing page in Claude Code and opens Figma mainly for vector graphics such as logos, exported as SVG into the project [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

### Agents working inside the design tool

- In Mobbin's demo, a fresh Claude desktop session connected to Paper through its MCP builds an onboarding flow inside a Paper file that already holds a (made-up) design system, working from an attached research report and a short brief [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]).
- An agent inside Figma, asked for iOS map and filter views, produced some broken UI; connected to Mobbin's MCP to research references first, it studied them and cited its sources [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]). The screens are only shown on video, and the comparison is the vendor's own demo.

## Where they agree and disagree

Between the sources:

- **Auto layout everywhere:** agreed across [S-L19-045] [S-L19-075] [S-L19-074] [S-L19-079].
- **Figma's defaults need adjusting:** the preset shadow is too strong [S-L19-057] [S-L19-045], and zooming out misleads you on size [S-L19-057].
- **Where the design lives:** most videos design in Figma and hand off; [S-L19-086] generates in code and polishes in Figma; [S-L19-103] designs in code and keeps Figma for vectors; [S-L19-108] has an agent build inside a design file through MCP. The work is moving toward code and agents, with Figma as one tool among several [inferred].
- **Figma versus dedicated tools:** Figma can make a mesh gradient with stacked blurred layers [S-L19-058], but [S-L19-073] says a dedicated generator does more. Both hold: the recipe is enough for a soft gradient, the generator for richer ones [inferred].

Against OpenDesigner's existing research:

- **Colors as styles conflicts with the default:** [S-L19-045] puts colors in styles and measurements in variables. DC-L07-21 defaults to "variables for values, styles for bundles": every single color, spacing, radius and opacity value is a variable, and only composites (text styles, shadows, gradients, grids) are styles, because a value that changes by mode must be a variable. Follow DC-L07-21; the video's split would break dark mode [inferred].
- **Corner smoothing:** [S-L19-070] turns iOS corner smoothing to the maximum on every shape. DC-L04-04 says Figma's iOS preset is 60% and recommends it only for iOS-targeted components, with circular arcs on the web; Q-shape-04 defaults to `circular` [inferred].
- **Figma mirrors the source of truth:** DC-L07-08 defaults to DTCG files in git with Figma as a synced, published view, and DC-L16-02 makes the builder's own model canonical with design tools as push targets. The code-first workflows of [S-L19-086] and [S-L19-103] fit that direction; the Figma-first habits in most videos fit teams where designers own the tokens [inferred]. DC-L11-16 reports that 60% of teams have no design-to-code automation at all.
- **Writing into Figma:** DC-L16-13 and DC-L18-13 write to Figma through the remote MCP when a Full seat is present, otherwise emit DTCG files Figma imports, and confirm before writing to a real file. The HTML to design plugin [S-L19-086] is another import path, for screens rather than tokens [inferred]. Mobbin's Paper demo is the same MCP route used to build screens rather than tokens, on a file set up for the purpose [S-L19-108]; `guardrails.md` section 6 still applies (confirm the target file before writing) [inferred].
- **Plan limits:** DC-L07-27 says the Figma plan decides what is possible (Starter cannot publish libraries; Code Connect, branching and analytics need Organization). None of the videos mention plan limits.
- **Shadows:** a softer, lower-opacity shadow [S-L19-057] [S-L19-045] moves toward `STD-visual-details-14`'s semi-transparent shadow.

## Decisions this informs

- **Q-tool-03** (do you use a design tool, and which Figma plan): every habit here assumes Figma; the plan answer decides whether libraries, Code Connect and analytics are available (DC-L07-27).
- **Q-tool-01** (where the master copy lives): the code-first workflows [S-L19-086] [S-L19-103] support `builder` or `token-file`, with Figma as a mirror; `design-file` suits teams whose designers own the values [inferred].
- **Q-token-07** (keeping the Figma library tidy): consistent layer names make multi-edit and Smart Animate work [S-L19-074] [S-L19-059]; DC-L07-21 settles styles versus variables (`vars-styles`).
- **Q-tool-04** (linking Figma components to code for AI tools): the HTML import path [S-L19-086] moves screens into Figma but carries no link back to code components [inferred].
- **Q-space-01** (base spacing unit): if the answer is `8`, set Figma's nudge to 8 [S-L19-070].
- **Q-shape-04** (circular or squircle corners): [S-L19-070] favors maximum smoothing; the default stays `circular` for the web.
- **Q-depth-03** (what shadows look like): start below Figma's 25% preset, at 15 to 20% [S-L19-057].
- **Q-dist-01** (planned: how the system leaves the builder, including `design-push` to Figma or Paper): the round trip in [S-L19-086] shows the reverse direction, code into Figma.
- **Q-tool-03** (which design tool): the `paper` answer (MCP read and write) is the one Mobbin's agent builds in [S-L19-108]; an agent in a design file needs the system's tokens in that file to build on, as the demo's file had [inferred].

## Visual examples worth showing

- Figma's default drop shadow beside a light-gray, high-blur version and no shadow [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Two stacked shapes, one with iOS corner smoothing and one without; the difference only shows when they overlap [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- The same chip before and after auto layout, with vertical padding at half or a quarter of the horizontal padding [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- A kaleidoscope, a clay rectangle, a metallic card with its rose-gold variant and a plugin-free mesh gradient, each with its layer stack visible [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).
- An AI-generated dashboard before and after a few minutes of fixes in Figma (fonts, alignment, color) [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- The same 3D logo made in Spline and in Blender [S-L19-046] ([[sources/A_Ozpb0XDuw-how-hard-is-it-to-really-make-a-no-code-3d-animated-website|How hard is it to REALLY make a no-code 3D animated website?]]).
- iOS map and filter views from an agent inside Figma, before research (some broken UI) and after (citing its references) [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]).

## Open questions

- Several details (the 25% shadow preset, the nudge default of 10, vertical trim, the lack of modifier keys in prototypes) describe Figma between 2024 and 2025. Which still hold?
- Should OpenDesigner's Figma export set iOS corner smoothing at all, given DC-L04-04's 60% iOS-only advice and the "maximum" habit of [S-L19-070]?
- How should a Figma spring (stiffness and damping) or a hand-dragged curve be converted into tokens that meet `STD-easing-duration-02`?
- When an agent builds screens straight into Figma or Paper [S-L19-108], how does OpenDesigner check that it used the system's variables and components rather than hand-typed values (`STD-visual-details-26`)? The source gives no values from the demo file.
