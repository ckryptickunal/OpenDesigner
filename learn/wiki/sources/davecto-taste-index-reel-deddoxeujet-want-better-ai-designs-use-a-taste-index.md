---
type: source
title: Want better AI designs? use a Taste Index
created: 2026-10-15
updated: 2026-10-15
video_id: davecto-taste-index-reel-deddoxeujet
url: https://www.instagram.com/p/DedDoxEujet/
channel: davecto (Instagram reel)
published: "2026-10-13"
authority: reference
tags:
  - taste-index
  - ai-design
  - brand-guide
  - design-md
  - reference-extraction
---

# Want better AI designs? use a Taste Index

## Metadata

- Page ID: `davecto-taste-index-reel-deddoxeujet`
- Publisher: davecto (Instagram reel)
- Published: 2026-10-13
- URL: https://www.instagram.com/p/DedDoxEujet/

## Summary

A 46-second creator reel that names a 'Taste Index': point an AI at one website you love, have it break down that site's fonts, colors, shapes, components, motion and voice, and turn them into a reusable guide the AI reads before building anything new. The on-screen prompt asks for four files (a DESIGN.md with a one-line brief, 5-7 principles and a Do / Don't list that explains why, a CSS file of variables, a motion script and a live specimen page), and asks the agent to mark what it measured versus made up. Two example cards show the same five-line format (Brief, Color, Shape, Motion, Never) holding two opposite tastes. For a design system this matters as a format: a short, plain taste summary that any agent can hold in its head. It conflicts with OpenDesigner on one point: the example copies one brand's identity wholesale.

## Key Ideas

- Generic AI output comes from the AI having no written reference for what good looks like.
- A written visual reference, read before every build, keeps new pages in one visual language.
- The guide should explain why each rule exists, so the agent can handle cases the guide did not cover.
- One fixed format can hold opposite tastes: Brief, Color, Shape, Motion, Never.
- A one-line brief written as a concrete picture says more than adjectives.
- Motion can be written as a feeling plus a test, not only as durations.
- The agent should say which values it measured and which it invented.
- A live specimen page that shows every swatch, size and component is part of the guide.
- Extracting from a single site also copies that site's identity [inferred].

## Entities

- [[entities/davecto|davecto]] (person): The presenter, who builds his website and Instagram content with AI and promotes his prompt.
- [[entities/typesafe-ai|TypeSafe AI]] (company): The site whose design the example Taste Index was extracted from (typesafe.ai; the transcript calls it the Jev website).
- [[entities/claude|Claude]] (product): The AI the presenter prompts to build and then follow the Taste Index.
- [[entities/taste-index|Taste Index]] (concept): The presenter's name for an AI-readable brand guide extracted from a website you love.
- [[entities/claude-code-codex-and-cursor|Claude Code, Codex and Cursor]] (tool): The coding agents the on-screen prompt says to paste it into.

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: Gives an AI coding agent a written visual reference so it stops producing generic pages; the reference is built by the agent from a site the person admires.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: The output is a small design system: a DESIGN.md, CSS variables for every value, a motion file and a specimen page.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Taste is captured as a one-line picture, a few named principles and a Never list, in a format that stays the same across opposite tastes.

## Notable Claims

- AI looks bad at design because people do not give it a taste reference. Evidence: [0:00] Most people think AI is terrible at design,
- Pointing the AI at the Taste Index makes new pages come out in the same style. Evidence: [0:30] I just point my AI and my taste index
- Generic AI websites share purple gradients, giant rounded cards and 2023 SaaS layouts. Evidence: Purple gradients, giant rounded cards, and layouts that look like every SaaS startup from 2023.

## Quotes

> Most people think AI is terrible at design
> — [0:00]

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Self-promotion, left out of the rules: 'comment TASTE' to receive the prompt, and a follow request (0:38 to the end, and the caption).
- Caveat: Most rules, numbers and examples were read from frames (the on-screen prompt and pages, 0:22 to 0:41), not spoken; the raw file's on-screen section was transcribed from full-resolution frames on 2026-10-15.
- Caveat: The example index copies typesafe.ai's identity (its colors and look) for the presenter's own content. OpenDesigner's identity rule forbids that: references give structure and quality, never a brand's identity. Use the format, not the copying. [inferred conflict with SPEC 5.4]
- Caveat: The 90/9/1 ratio is one person's taste card, not evidence; OpenDesigner's research keeps accent use as a soft guide (about 15% of a view, DC-L15-03) and treats 60-30-10 as weak evidence.
- Caveat: Auto-captions: 'the Jev website' refers to typesafe.ai (TypeSafe's model is named Jev, shown in the frames); 'your CTO' may be a mis-hearing of the presenter's name or handle.
- Caveat: Product tag judged here: the source shows only marketing and resource pages, but the technique is not specific to either, so rules are tagged both. [inferred]
- Caveat: A 46-second creator reel: no measured outcomes beyond the presenter's own pages.

### Rules and practices

- **should** (process, all, both products): Give the AI a written visual reference and point it at that reference whenever it builds something new, so new pages come out in the same style. Why: New pages then reuse the fonts, colors and animations already defined, instead of a look the AI makes up. [[0:30] I just point my AI and my taste index]
- **should** (process, all, both products): Open the brief with one line and 5-7 principles, then color, type, components, motion and a Do / Don't list, and write why each rule exists. Why: Explaining why lets the agent handle cases the guide did not cover. Values: 5-7 principles. [[0:40] Then build four files: 1. DESIGN.md: a one-line brief, 5-7 principles]
- **should** (process, all, both products): Mark which values were measured from the reference and which the agent made up. Why: So the person can tell evidence from guesses. [[0:41] Mark what you measured and what you made up.]
- **should** (process, all, both products): Don't invent rules the reference site does not follow. Why: The guide should describe the site, not the agent's own preferences. [[0:41] Don't invent rules the site doesn't follow.]
- **consider** (typography, all, both products): When the reference uses a commercial font, name the closest free substitute. Why: So the guide can be used without a licence the person may not have. [[0:41] If a font is commercial, name the closest free substitute.]
- **consider** (process, all, both products): Use one fixed format for every taste summary: Brief, Color, Shape, Motion, Never. Why: The format holds any taste, so opposite tastes stay comparable and complete. Values: Brief, Color, Shape, Motion, Never. [[0:38] Two Examples. Same Format, Opposite Taste.]
- **consider** (motion, all, both products): Write motion as a feeling plus a test, for example a whisper that is wrong if you notice it as an animation. Why: A felt description tells the agent how much motion is too much, beyond durations. [[0:40] Motion: A whisper. If you notice it as an animation, it's wrong.]

### Decisions it informs

- Where should an AI's visual direction for new pages come from? (both products)
  - The AI's own defaults: Generic pages: purple gradients, giant rounded cards, 2023 SaaS layouts. When: The source argues against it.
  - A Taste Index extracted from one site the person loves: New pages share that site's fonts, colors and animations. When: The source's recommendation.
  - The person's own recorded choices, with references giving structure only: Consistent pages in the person's own identity rather than another brand's. [inferred: OpenDesigner's approach, not the source's] When: When the result must not copy another brand's identity. [inferred]
  - Recommendation: The source recommends a Taste Index built from a site you love, kept as files the AI reads before every build.

### Process

1. Read the reference site: Open a few different pages, not only the home page, and read the computed styles: fonts, every color and where it is used, borders, radius, shadows, spacing and grid, repeating components, motion and easing, and how headlines, labels and buttons are written.
2. Write the guide: DESIGN.md (a one-line brief, 5-7 principles, then color, type, components, motion and a Do / Don't list, with reasons), a CSS file with every value as a variable plus component classes, a motion script with no dependencies, and a live page showing every swatch, size and component.
3. Match an earlier guide's structure: Attach an existing Taste Index as the example and match its structure and depth, not its look.
4. Report and hand off: Mark measured versus made-up values, open the live page, list what was uncertain, and add one line to CLAUDE.md so later agents read the guide first.

### Examples and visual references

- The reference site (typesafe.ai (TypeSafe AI)): 0:05-0:08: hot pink and mint green panels, a large grotesk headline ('We Took The Opposite Research Direction'), a halftone dollar-bill image, big stats ('193.6x Faster, 444.6x Cheaper') and a dark FAQ panel. Read from frames only.
- The generated Taste Index page ('Retro OS') (The presenter's own guide, extracted from typesafe.ai): 0:22-0:25: a pink page with tabs (Color, Type, Micrographics, Texture, Components, Motion, Rules, DESIGN.md) and header controls that read like dials (line weight 1px always, corner radius 0 never, 7 section colors, linear or stepped easing). A metaphor thesis ('Desktop Software, Printed On Pink Paper'), three named principles ('Color Is A Place', 'Everything Is A Window', 'Two Voices'), color swatches each named with its job, neutrals, chart accents only as chips, a page order, a usage ratio, a contrast table, and component specimens each captioned with its rule. Read from frames only.
- A page built from the index (The presenter's resources page): 0:26-0:38: full-width sections in flat colors (pink, teal, magenta, mustard, orange, blue) with 1px windowed cards, scrolled top to bottom; it repeats the index's language. Read from frames only.
- Two taste cards in one format (Retro.OS and davecto.com): 0:38-0:41: two cards side by side, each with a font pairing, a swatch strip and five lines (Brief, Color, Shape, Motion, Never). One is loud (flat pink, hard shadows, square corners), the other quiet (warm paper, one teal accent, hairlines, a 2px radius). Below them the prompt itself. Read from frames only.
- The reel's own editing (This video): Word-by-word serif captions with key words in pink, a persistent title chip, hard cuts between five or six setups every 3 to 9 seconds, and screen recordings scrolling in the upper half of the frame.

### Numbers

- 5-7: principles in the DESIGN.md brief [[0:40] a one-line brief, 5-7 principles]
- 90% paper and ink, 9% muted grey, 1% teal: the color ratio on the presenter's quiet taste card; a stated taste, not research [[0:40] Color: Roughly 90% paper and ink, 9% muted grey, 1% teal.]

<!-- /od:learn -->
