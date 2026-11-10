# Local learnings: a private B2B landing page (maritime SaaS), 2–3 Nov 2026

Source: one real project run end to end with OpenDesigner (sketch → draft → fresh-eyes review → owner feedback → rebuild). Written about the method, not the client: no names, customers or private URLs. Status: **proposed**. Nothing here changes a standard or a default until the owner accepts it (KNOWLEDGE.md section 4). The same notes are filed as F-001 to F-010 in that project's `opendesigner/feedback.md`, each with an issue link.

## What happened

1. The sketch ran with delegated answers (feel: serious, bold, trustworthy, minimal; surface: `landing page:persuade`). It built cleanly: 0 errors, every contrast pair passing.
2. Draft 1 was static and token-correct. A fresh-context reviewer scored it about 3/5 against shipped references, and caught copy overclaims and an unrealistic sample cargo.
3. The owner's verdict on draft 1, paraphrased: too dead, too much like the lead reference (Helsing), looks AI-generated, and needs motion. He asked to rebuild on the parent company's own site system (grid, spacing, type and motion) instead.
4. Draft 2 reused the parent's motion components: per-word blur reveal on a measured spring, one shared reveal observer, Lenis smooth scroll, pinned step sections, and a magnetic primary CTA. It added a pinned five-stage product explainer, a scroll-read statement, parallax photos and a hero video with a pause control.

## Lessons, each with a proposed home

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 1 | **Persuade surfaces need a motion plan before the first draft.** A static draft that passes every check still reads as "dead" and "AI-generated". | Owner verdict on draft 1 | `making.md` section 1: for `persuade` surfaces, write the motion plan (reveal system, one signature moment, one explanatory sequence) before building. `zoom.md`: ask about motion at sketch level for persuade surfaces. |
| 2 | **One signature device from a reference is identity, not structure.** Edge ruler ticks taken from the lead reference made the whole page read as a copy of it. | Owner: "too much like [reference]"; "don't use the side grids" | `making.md` section 11, new tell: "A reference's signature device pasted on (ruler ticks, bracket indices, a crop style)". `guardrails.md` section 1 could list "signature devices" under identity. |
| 3 | **Inheriting from a parent brand needs a code route, not just tokens.** Grid and type carried over; the motion system, which mattered most, lived in the parent's components. | Draft 2 adapted five parent components | Sketch option or opendesigner-extract mode: "inherit from a parent codebase", which reads its motion components and section patterns, not just CSS values. |
| 4 | **Directions in a switcher must differ in ground and grade, not just accent.** Six directions that swapped only accent and wordmark face were judged near-identical. | Fresh-eyes review of draft 1 | `making.md` section 3: an identity direction changes at least the leading ground (light or dark), the photo grade and the accent. |
| 5 | **Review flags OpenDesigner's own export.** `tokens.css`, copied into the app, contains px gaps (12px, 14px) that STD-accessibility-motion-13 flags. | `engine.py review --project site` | Bug: emit rem in the CSS export, or have review skip files carrying the export header. |
| 6 | **Illustrative durations need a reason marker.** Marketing motion (a 700 ms line draw, a 600 ms poster-to-video crossfade, a 900 ms time-bar fill) can only pass with `od-ignore`. | Review output | Accept `/* od-reason: illustrative */` (or similar) so the intent stays visible and checkable. |
| 7 | **A hero video and STD-accessibility-motion-07 can coexist.** The fix: a visible pause control (WCAG 2.2.2), no video under reduced motion or Save-Data, and a poster that matches the first frame. | Implemented in draft 2 | Name this compromise in the standard's text. |
| 8 | **Missing feel words:** "precise" and "industrial". | `engine.py feel` | Map them (precise → serious and minimal; industrial → serious and bold?) [inferred]. |
| 9 | **Background-pane screenshots catch reveals mid-run.** Draft 2's hero looked empty in one screenshot because the reveals hadn't finished. | Browser checks | `making.md` section 5: before judging a screenshot, check `element.getAnimations()` or the revealed state. |
| 10 | **AI video provider change.** Veo 3.1 was shut down on 22 Oct 2026. Image-to-video now runs on `gemini-omni-1.1-flash` via the Interactions API (`POST /v1beta/interactions`, `response_format: {type: "video", delivery: "uri"}`). The `files/{id}` URI can return the video bytes directly. | Live API responses, 2 Nov 2026 | opendesigner-paint and any tool that calls Veo. |

## Confirmed approaches (keep doing)

- A fresh-context reviewer before the owner sees the page. It caught copy that overclaimed beyond the product's source document, a cargo too large for the stated ship size, and duplicated sections.
- Keep all page copy in one data file, with every product claim traced to a source document. Missing facts render as visible draft placeholders behind a "Notes" toggle, never as invented proof.
- Re-add every figure in sample product data and write the check next to the data.

## Round 3 (3 Nov 2026): owner feedback on draft 2

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 11 | **Dark "mission-critical" grading reads dead on a B2B landing page.** Low-key, desaturated night photos taken from a defence reference were called "very dark, very out of place, a dead vibe". Bright natural daylight, true colour and deep focus replaced them, matching DC-L05-14's enterprise guidance. | Owner, draft 2 | The imagery step should default to DC-L05-14's natural-light brief for B2B persuade surfaces. Treat cinematic dark grading as an explicit opt-in, even when a reference uses it. |
| 12 | **Show every state at once for a product overview.** A pinned explainer that stepped through five stages on scroll was replaced with a bento grid "so that anybody can see what it holds". Each card now animates its own rows when it comes into view. | Owner, draft 2 | `making.md` section 7: prefer a bento or grid over a pinned stepper when the reader needs the whole picture. Keep pinning for narratives. |
| 13 | **Smooth scrolling is a taste call, not a default.** The owner removed Lenis after trying it. | Owner, draft 2 | Never include smooth scroll in a default motion kit. Ask first. |
| 14 | **Text beside a bright photo, not over it.** A light scrim over a bright hero still left the lead running across crane structures. Moving the words onto the plain ground above a full-width photo band fixed it with no scrim. | Rendered check, draft 3 | `making.md` section 5 and DC-L05-16: for bright photography, put text beside or above the image. A scrim is the fallback. |
| 15 | **Grain is used as OpenDesigner specifies:** still `feTurbulence` noise at 6% with an overlay blend, on the hero photo only, and switched off under `prefers-contrast: more`. | `styles.md` #17 | Confirmed approach. |

## Round 4 (3 Nov 2026): owner feedback on draft 3

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 16 | **Screens on photos (the opendesigner.dev `.stage`) suit a B2B product overview.** Each stage card became an Unsplash sea photo with grain and a glass bezel around a small white product screen, which reads as premium where text-heavy cards read as ugly. | Owner asked for this pattern by name | `making.md` section 6: offer the stage pattern for product shots on persuade pages. Cite `site/static/home.css`. |
| 17 | **Numbers become small interactive figures.** The estimate became a waterfall, negotiation became converging offer lines, claims became a time-bar ring, and documents became marks. Every mark shows its value and source on hover, focus or tap. | Owner: "ugly, all numbers and text" | `making.md` section 8: on persuade pages, any panel with 3 or more figures should become a figure with marks that carry tooltips. |
| 18 | **Open-library ship photos carry other companies' names.** Unsplash bulk-carrier photos show real shipping line names on the hull. Using them would put another brand on the page. Use open-library photos for abstract scenes, and generated or commissioned photos for the subject. | Search on 3 Nov | `hooks.md` H-photo and `guardrails.md` section 1. |
| 19 | **Sample the palette from the hero photo.** Deep-sea ink, white and the hull's own antifouling red made the page cohere with its imagery (the owner's the parent brand practice). | Owner request | The colour step could offer "sample from your hero photo". |
| 20 | **Fade dark bands into white in oklab, with an eased midpoint stop.** A plain linear gradient passes through a muddy grey. | Rendered check | Snippet in `making.md` section 4, or a standard. |
| 21 | **The owner may override inherited square chrome with rounded corners.** the parent brand's radius-0 rule did not carry over: pill buttons, 16–32 px containers and nested radii were asked for. | Owner, 3 Nov | Inheriting from a parent brand should list which rules are open to change. |
| 22 | **Bug: `pathLength` dash animation breaks under `vector-effect: non-scaling-stroke`.** Use a clip-path wipe instead. | Rendered check | Motion reference. |
| 23 | **Generate AI video at maximum quality, then encode down.** The owner asked for maximum quality. Gemini Omni `resolution: "4k"` gave a 3840×2160 master (59 MB). It's kept outside the repo, and the site ships a 1920 px H.264 encode (crf 24, about 7 MB). | This run | opendesigner-paint: always ask for the top resolution, keep the master, and ship an encode. |

## Round 5 (3 Nov 2026): owner feedback on draft 4

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 24 | **Strict owner rule: no CTA moves on hover.** Magnetic, cursor-following, floating or "dancing" buttons are banned. Hover changes colour or brightness only. | Owner, in his words, in `_coordination/OWNER-FEEDBACK.md` (2026-11-03 #1) | Added as a tell in `making.md` section 11. Promote to a house standard. Never include a magnetic CTA in a motion kit, even one inherited from a parent brand. |
| 25 | **Infographics built from default shapes look cheap.** Rounded bars, plain lines and floating tooltips were called "very, very, very cheap". The fix was one figure system, taken from supermemory.ai, Cloudflare and Stripe status pages: a dot-grid canvas; hairline nodes with corner handles; dashed orthogonal wires; unit marks with a stated scale ("■ = $80,000", "▮ = 1 day"); square chart markers; one accent per figure; and a readout line under each figure in place of floating tooltips. | Owner, plus a Mobbin search for "technical system diagram" and "dot matrix bar chart" | New reference page `references/figures.md` (or a section of `making.md` section 8): the figure system above, with these references. |
| 26 | **A readout line beats floating tooltips.** Tooltips centred on marks clipped at screen edges: 8 of 14 at 375 px in an audit. A single readout under the figure, updated on hover, focus or tap, never clips and works the same on touch. | Fresh-eyes audit, draft 4 | `making.md` section 8. |
| 27 | **Look for shipped examples before drawing figures.** `making.md` section 1 already asks for this, but it wasn't done for the infographics until the owner said so. | Owner: "use the Mobbin MCP … to figure out more examples" | Make it a checked step before any figure. |

## Round 6 (3 Nov 2026): owner feedback on draft 5

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 28 | **"Soft rounded" means subtle.** 16–32 px containers and pill buttons were called too rounded. A 4/6/8/12 px scale, 6 px buttons and no superellipse corners were accepted. | Owner | Roundness dial: when a person says "rounded" for an enterprise page, start around 25, not 60. |
| 29 | **Audit every figure at every width with a measuring script, not screenshots.** `scripts/figure-audit.js` measures overflow, text overlap, truncation, text under 11 px, targets under 24 px, row heights and label-style consistency. It ran at 9 widths (320 to 1440). It caught waterfall labels colliding at 320 px, a break that unifying the label style introduced and that screenshots missed. | This round | A preflight tool, with its widths list including in-between sizes (600, 900). |
| 30 | **Consistent figures share one anatomy and two text roles.** Every figure has a head (label plus one key value), the figure itself, a scale or legend, and a readout. Text uses only an uppercase label (11 px, 0.08em) and a data value. Before this there were four small-label styles across six figures. | Style inventory script | `making.md` section 8. |
| 31 | **Stagger chart labels with a transform, not a margin, on narrow grids.** A margin inside a grid row stretches the row and leaves the labels level. A transform moves the label without changing layout. | 320 px fix | Snippet. |

## Round 7 (3 Nov 2026): owner feedback on draft 5, "nothing looks aligned"

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 32 | **Build the token file before the second draft, and make components read only from it.** Drafts 1 to 5 grew values per section; the owner saw it as "you have not made a design system". One `tokens.css` (neutrals, meaning colours, roles, type, 4px space, radii, elevation, motion, layout switches) plus a component sheet that uses only `var(--…)` fixed it; `engine.py review` then reported zero raw values. | Owner; review output | `making.md` section 2: a review-clean token file is a gate before draft 2. |
| 33 | **Figures need a fixed anatomy height, not only a shared anatomy.** Equal body heights still gave screens 37px apart because labels and readouts wrapped to different line counts. Fixed grid rows (head, body, legend, readout), single-line label/readout text with ellipsis, and short readout copy made every screen equal at every width. | Measured per part | `making.md` section 8 snippet. |
| 34 | **Size compact figures with container queries on the figure frame, not media queries.** A tile in a three-column bento at 1024px is narrower than a phone; the photo frame (Daylight) takes another 50px. `@container` on the frame handled both. | Audit at 320 and 1024 | `making.md` section 8. |
| 35 | **A direction switcher must switch design systems, not palettes.** Owner rejected colour swaps. Three systems via `data-ds` on `<html>`: each changes type families, label case, radii, elevation, hero layout (centred vs split), stage treatment and section alignment. | Owner | `making.md` section 3 (showing options). |
| 36 | **Utility state classes collide.** `.is-wait` set a bar fill and also painted a heading value amber-on-amber. Scope fill classes to the marks they colour (`:is(.bar…).is-wait`). | Rendered check | Lint idea for review. |
| 37 | **Meaning colours are a house standard:** approve green, reject red, waiting amber, Teams purple, email blue, call green, unless asked otherwise. | Owner, "across all projects" | Already PRJ-02 and making.md section 11; promote to STD. |

## Round 8 (3 Nov 2026): owner feedback on draft 6, "dull, roundish, unaligned"

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 38 | **When the owner names a reference and an option inside it, measure it, don't paraphrase it.** Opening the parent brand's draft site /ask, selecting "Direction 1", screenshotting every section and dumping its stylesheet rules gave exact values (8px shell #F3F4F5, 36px mono header, white sheet r7, 16/16/14 padding, two-cell spec footer). Draft 6 had guessed and was called dull. | Owner; docs/research/07 in the client repo | `making.md` section 1: for a named reference, read computed CSS with a script, record it in a research note, build from it. |
| 39 | **Per-card photo backgrounds break trust.** Six stages on six different photos read as six different products. Identical shells for every figure, and black-and-white grainy photos only in full-bleed bands. | Owner: "containers different colour loses respect and trust" | `making.md` section 8: figure containers are one surface. |
| 40 | **Use real third-party logos for well-known apps** (Gmail, Teams) on a neutral tile; generic mail/chat glyphs look cheap. Iconify `logos` (CC0) has both. | Owner | `hooks.md`: integration logos come from the vendor or Iconify logos, never redrawn. |
| 41 | **Items derived from one source should be drawn as a tree** (spine from the source icon's centre, elbows to each child), with the child indent equal to half the parent tile. | Owner on the enquiry card | Figure vocabulary entry. |
| 42 | **A background tab pauses IntersectionObserver and WAAPI**, so split-word headings look blurred in background-tab screenshots. Verify reveals in the visible tab before calling it a bug. | This round | Preflight note. |
| 43 | **"Alternative design system" switchers can backfire.** Daylight/Bridge/Ledger were all rejected as dull; mirroring the reference's own page modes (Mixed, Night) was safer. | Owner | `making.md` section 3: offer options the reference itself offers before inventing systems. |

## Round 9 (3 Nov 2026): owner picks from Mobbin, then mixes

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 44 | **Samples first, as a pick board.** 65 Mobbin sections grouped into four candidate directions, each image linked to Mobbin with an "I like this" tick and a copyable list. The owner ticked 24 across all four directions, which a "pick one direction" question would have hidden. | `site/public/samples/`, owner's list | `making.md` section 3: show options as a tickable sample board before building. |
| 45 | **Read the picks as a taste index:** what the picks share and what the left-outs share (here: diagrams over screenshots, two moods kept, serif voice with mono data, colour photography, texture in doses; left out: stock office photos, badge grids, loud brutalism). | `docs/research/08-taste-index.md` in the client repo | Feed into `taste.py index` as poll evidence. |
| 46 | **When the owner picks across directions, build a mix-and-match lab, not four pages:** every section in 2–5 variants (one per liked sample), page-wide dials (ground, type, accent, imagery, corners), presets for the four directions, shareable URL state, per-section switcher pills like the parent site's /ask options. | `site/public/lab/` | A reusable lab template in OpenDesigner. |
| 47 | **"Less text" must never drop content.** Every lab variant carries the full checklist in `docs/CONTENT-CORE.md`. | Owner feedback, draft 7 | Source-coverage check in preflight. |

## Round 10 (3 Nov 2026): "every variation looks shitty", fonts changed without asking

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 48 | **Never put fonts on a dial the owner didn't open.** A type switch (serif / grotesk / tight) read as changing settled decisions. One pair everywhere (Outfit + Hanken Grotesk). | Owner | `making.md` section 3: options only vary what the owner left open. |
| 49 | **Thumbnails are not references.** Variants built from Mobbin thumbnails copied layouts and lost what made them good. Opening the live sites showed 2K hero video and 150px type (Waabi) and an 18-canvas live dot field behind 160px type (Dovetail). Rebuilt heroes use a playing video, a live canvas field, a 3D product window that straightens on scroll, a typing and citing assistant, a scrolling voyage ticker, word-by-word blur reveals and self-drawing lines. | `docs/research/08-taste-index.md`, `site/public/lab/` | Extract skill: always open the live reference and measure motion, scale and effects before building. |
| 50 | **Class-name collisions hide whole components.** A product window named `.app` inherited the 36px app-icon tile style and vanished. Prefix component classes. | Rendered check | Lint idea. |

## Round 11 (3 Nov 2026): scrap and restart, mobile first, "align the hull imagery"

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 51 | **Generate imagery for the layout, not the other way round.** Landscape 1376×768 photos crop badly on a portrait phone. Five new 9:16 photos were briefed with the line placed (horizon at 60%, deck line 38%, waterline 61%, hull edge at 31% across, ship running vertically), then measured with a drawn grid. | `scripts/generate-portraits.py`, `site/public/hull/` | Paint skill: brief the line position into the prompt when the layout will align to it. |
| 52 | **Align type to the photo with code, not guesses.** `object-fit: cover` moves a fixed image percentage as the box changes, so hull.js computes where the image's line lands on screen and sets `--y-wl` / `--x-edge`; rules and headlines sit on it at every width. | Checked at 375 px and 1440 px | Snippet for `making.md`. |
| 53 | **Font licences: Palantir uses Alliance No.1/No.2 (Degarism), Rosart (Camelot Typefaces) and Apercu Mono Pro (Colophon); all commercial.** A "reference font" option uses free stand-ins (Source Serif 4, Inter Tight, DM Mono, the last by the same foundry as Apercu) and says so on screen. | palantir.com stylesheet, MyFonts listings | Extract skill: name commercial fonts, never ship their files, offer stand-ins. |

## Round 12 (3 Nov 2026): four sites, a taste index, the owner's logo

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 54 | **Pick references by kinship, then measure them live at the owner's device width.** Four physical-industry sites (Seasats, Waabi, T1 Energy, Farm Minerals) measured at 375 px gave eight shared traits; the shared traits, not any one site, became the build list. | `docs/research/09-taste-index-four-sites.md` in the client repo | Extract skill: "taste index from N sites" = shared traits plus a Never list, each trait mapped to one change. |
| 55 | **Treat a supplied logo as untouchable.** Inspect transparent PNGs on a mid-grey (white artwork is invisible otherwise), keep originals unedited, derive only recolours, trims and padded icons. The owner's mark carried a horizontal cut that matched the page's waterline concept; it was preserved, not "cleaned up". | `source-material/logo-sample-2026-11-03/`, `site/public/brand/<product>/` | Brand step: inspect on grey, never redraw. |
| 56 | **Animate the aligned still, so alignment survives motion.** Image-to-video from the measured bow still, with the prompt asking the horizon to stay level; first and later frames checked at the same height. | `media-masters/`, `site/public/media/bow-waterline.mp4` | Paint skill: when type aligns to a line in a photo, animate that photo and verify the line across frames. |
| 57 | **Hidden-pane checks lie about lazy images and reveals.** A black plate and blurred text were hidden-pane artefacts; verify those in a visible tab or force-load before calling a regression. | This round | Preflight note. |

## Round 13 (3 Nov 2026): from motion to foundations

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 58 | **Owners swing from "dead" to "jiggly".** Two rounds asked for more motion; the next called it jiggly. For enterprise trust pages, default to no scroll choreography and let structure carry the page; offer motion as an opt-in. | Draft 10 vs draft 11 | Motion dial default for B2B "enterprise" intent: hover only. |
| 59 | **"Adopt the foundations, not the system".** Take colour roles, type scale, shape, container and spacing from the parent; leave its hero, layout and signature devices. Write the adopted list down (`docs/DESIGN-FOUNDATIONS.md`). | This round | Extend skill: a "foundations import" mode. |
| 60 | **Use the vendor's current icons.** Microsoft's 2025 gradient icons (Outlook, Excel, Teams) via Iconify `thesvg-color`; ImageMagick renders them black, so preview in a browser. | This round | Asset note. |

## Round 14 (3 Nov 2026): four layouts, owner's gradients

| # | Lesson | Evidence | Proposed change |
|---|---|---|---|
| 61 | **Colour is identity, not a "foundation".** Taking the parent brand's exact blue made the child look like a cheap copy. Foundations = spacing, type scale, shape, grid. | Owner on draft 11 | Extend skill: never inherit the parent's accent unless asked. |
| 62 | **Layout variations from references: one content file, N renderers.** Content in `content.js`, each reference layout as a render function, a switch for layout and colour; content parity checked per layout by script. | `site/public/home/` | Template for "show me variations". |
| 63 | **Light-to-dark gradients need a text rule.** White text on the light top was unreadable; panels with text use the lower stops (colour into black), visual-only cards keep the full sweep. | Rendered check | Colour stage: gradient + text-contrast rule. |
