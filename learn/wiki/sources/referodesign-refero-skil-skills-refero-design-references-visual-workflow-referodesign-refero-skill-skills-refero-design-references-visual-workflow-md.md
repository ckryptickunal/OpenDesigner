---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/visual-workflow.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-visual-workflow
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/visual-workflow.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - visual-qa
  - design-directions
  - image-generation
  - reference-lock
  - handoff
  - refero
  - process
---

# referodesign/refero_skill: skills/refero-design/references/visual-workflow.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-visual-workflow`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/visual-workflow.md

## Summary

A short Refero workflow reference for visual exploration, generated imagery and post-build visual QA. It says to offer three distinct reference-locked visual directions only for high-visibility or new-visual-language work, then stop and let the user pick one as the build target. Before coding it asks for an explicit visual target and a list of what must not drift, and before generating any bitmap asset it asks for a short asset lock. After building it runs a visual QA pass with P0-P3 severities and blocks handoff on unresolved P0-P2 issues. For a design system this gives a concrete gate-based process for choosing a direction and checking the result against it.

## Key Ideas

- Keep the main workflow research-first: styles for taste, screens for patterns, flows for journeys
- Image generation is optional; the workflow must still work when no image tool exists
- Offer three distinct reference-locked directions only for exploration-worthy work, not small edits
- Each direction names a primary source, traits to keep, borrowed details, media strategy and rejects
- Stop and let the user choose; the chosen direction becomes the target for build and QA
- Before coding, state the build target and what must not drift
- Generate bitmap assets only when the reference lock needs real imagery, never for icons or fake product evidence
- Write an asset lock (role, slot, art direction, avoid) before generating
- Generated assets must be placed in the build before handoff or reported as blocked
- Run a visual QA pass comparing implementation evidence with source truth per viewport and state
- Classify issues P0-P3 and do not hand off with unresolved P0, P1 or P2

## Entities

- [[entities/refero|Refero]] (company): Publisher of the refero_skill repo this workflow belongs to
- [[entities/codex-desktop|Codex Desktop]] (product): Named host whose built-in image_gen tool should be used when available
- [[entities/reference-lock|Reference lock]] (concept): A direction tied to a primary source with traits to preserve, borrowed details, media strategy and rejects
- [[entities/asset-lock|Asset lock]] (concept): A short spec of role, slot, art direction and things to avoid written before generating an image
- [[entities/visual-target-gate|Visual target gate]] (concept): The check before coding that names the build target and what must not drift

## Topics

- [[topics/design-process|Design process]]: Gate-based flow: research, three reference-locked directions, user choice, visual target, build, visual QA with severities.
- [[topics/ai-assisted-design|AI-assisted design]]: How an agent should use or skip image generation and avoid substituting screenshots, CSS drawings or SVG placeholders for real imagery.
- [[topics/presenting-designs|Presenting designs]]: Present three distinct directions in a fixed format and stop for the user to choose.
- [[topics/icons-and-imagery|Icons and imagery]]: Generate bitmap assets only for hero imagery, illustrations, textures, thumbnails and cutouts, with an asset lock first.

## Notable Claims

- Refero must still work in Claude Code, Codex, Cursor, Gemini CLI, Lovable and other MCP agents when no image tool exists. Evidence: Image Generation Capability
- Another agent cannot be assumed able to call Codex Desktop's built-in image tool just because Codex is installed locally. Evidence: Image Generation Capability: Do not assume another agent can call
- P0 issues are broken tasks, unreadable or overlapping UI, or severe accessibility issues. Evidence: Classify issues by severity
- P1 issues are major design drift or a likely user-facing usability regression. Evidence: Classify issues by severity
- P2 issues are moderate visual mismatch, a missing state, a responsive issue or asset drift. Evidence: Classify issues by severity
- P3 issues are polish that can follow after handoff. Evidence: Classify issues by severity

## Quotes

> Stop and ask the user to choose.

> Generated assets must be placed into the implementation before handoff or documented as blocked.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Written for Refero's own skill and its MCP research layers; the Codex Desktop image_gen advice is host-specific and may date quickly.
- Caveat: Severity definitions are the source's own scheme, not an external standard.

### Rules and practices

- **should** (process, all): Offer three distinct reference-locked visual directions only for variants, a new visual language, major redesigns, landing pages or other high-visibility surfaces; skip it for small edits, obvious component work or production fixes with a clear source. Why: Exploration is useful only when several plausible directions exist. Values: three. [Three Visual Directions]
- **should** (process, all): Give each of the three directions a primary source, traits to preserve, borrowed details, a media strategy and rejects; use a different count only if the user asks. Why: Makes each direction reference-locked. [Three Visual Directions step 2]
- **must** (process, all): After presenting directions, stop and ask the user to choose; use the chosen one as the visual target for build and QA. Why: The selection becomes the target. [Three Visual Directions step 4]
- **must** (process, all): Before coding substantial visual work, write down the build target and what must not drift (canvas, typography, accent roles, layout, media, density). Why: Visual Target Gate. [Visual Target Gate]
- **must** (process, all): If no target exists and the direction is material, explore options or get the user to approve one reference-locked direction before building. Why: Visual Target Gate. [If no target exists]
- **must** (tooling, all): Use image generation only when the environment exposes an image tool or the user approved a CLI/API image workflow; otherwise give written directions with implementation-ready prompts. Why: Image generation is optional and must not be assumed. [Image Generation Capability]
- **must** (process, all): Do not substitute browser screenshots, CSS drawings, inline SVG or placeholder shapes for generated bitmap assets when the reference lock calls for real imagery. Why: Stated in the image generation section. [Image Generation Capability]
- **must** (iconography, all): Do not use image generation for standard icons, editable SVG systems, code-native UI or fake product evidence. Why: Generate only bitmap media the reference lock needs. [Generated Assets]
- **should** (process, all): Before generating an asset, write an asset lock with role, slot (dimensions, aspect ratio, location), art direction and what to avoid. Why: Required before generating; its avoid list names wrong palette, extra text, brand drift and generic placeholders. [Generated Assets: asset lock]
- **must** (process, all): Place generated assets in the implementation before handoff, or document them as blocked. Why: Stated requirement. [Generated Assets]
- **must** (process, all): After substantial UI work, run visual QA comparing implementation evidence with the source truth for each viewport, route, theme and interaction state, checking typography, spacing, colors/tokens, imagery, component states and copy. Why: Visual QA pass. [Visual QA]
- **must** (process, all): Do not hand off visual work with unresolved P0, P1 or P2 findings unless blocked by missing source access, assets or tools; if blocked, say what evidence is missing and what to check next. Why: Severity gate. Values: P0, P1, P2. [Do not hand off visual work]
- **must** (tooling, all): Do not assume another agent can call Codex Desktop's built-in image tool because Codex is installed; verify the tool is exposed and user-approved first. Why: Image generation must not be assumed available. [Image Generation Capability]
- **should** (tooling, all): In Codex Desktop, use the built-in image_gen tool when available and generate each visual direction or bitmap asset as its own image result. Why: Stated for that host. Values: image_gen. [Image Generation Capability]
- **should** (process, all): During visual QA, use the relevant craft references (typography, color, motion, icons, accessibility, images, copy) to judge drift toward generic design. Why: Stated in the Visual QA section. [Visual QA]

### Decisions it informs

- Should this task get three visual directions or go straight to build?
  - Three reference-locked directions: User sees distinct options and picks a target before build When: Variants, new visual language, major redesigns, landing pages, high-visibility surfaces
  - Build directly: Faster; no exploration step When: Small edits, obvious component work, production fixes with a clear source
  - Recommendation: Explore only when several plausible directions exist.
- Generate images for each direction or describe them in writing?
  - Generated image per direction: One independent image per direction When: An image tool is available and worth the latency
  - Written directions with prompts: Reference-locked text plus implementation-ready prompts When: No image tool, or not worth the latency

### Process

1. Research: Research styles first; add screens and flows when structure or journey matters.
2. Three directions: Create three distinct reference-locked directions (primary source, traits to keep, borrowed details, media strategy, rejects).
3. Visualise: Generate one image per direction if a tool exists and it is worth it; otherwise write directions with prompts.
4. User chooses: Stop and ask the user to pick; the pick becomes the visual target.
5. Visual target gate: Write the build target and what must not drift before coding.
6. Asset lock: For needed bitmap assets, write role, slot, art direction and avoid list, then generate and place them.
7. Visual QA: Record source truth, implementation evidence, viewport/state and result; check type, spacing, color, imagery, states and copy.
8. Triage: Classify findings P0-P3; resolve P0-P2 before handoff or report what blocks them.

### Examples and visual references

- Template for three directions: '[Direction name] - [specific layout, style, product framing, and primary reference]' (Three Visual Directions): A fixed one-line format for presenting each option.
- Visual QA record: Source truth, Implementation evidence, Viewport/state, Final result (Visual QA): A four-field template that pairs a reference with a captured screenshot per state.

### Numbers

- three: Default number of visual directions to offer [Create three distinct reference-locked directions]
- P0-P3: Severity levels for visual QA findings [Classify issues by severity]

<!-- /od:learn -->
