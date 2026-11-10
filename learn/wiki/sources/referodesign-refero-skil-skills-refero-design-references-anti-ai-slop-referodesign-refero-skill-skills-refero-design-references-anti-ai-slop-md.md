---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/anti-ai-slop.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-anti-ai-slop
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/anti-ai-slop.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - ai-slop
  - anti-patterns
  - indigo
  - cards
  - light-mode
  - editorial-serif
  - emoji
  - token-roles
  - references
  - litmus-tests
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/anti-ai-slop.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-anti-ai-slop`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/anti-ai-slop.md

## Summary

This guide from the Refero design skill lists the patterns that make an interface look AI-generated and gives a rule for each. The nine named tells are indigo/violet accents, cards everywhere, dark mode by default, calm editorial serif on autopilot, emoji as icons, decorative left accent stripes, averaging strong references into a safe middle, changing what a style token means, and faking or dropping image-led media. It then lists generic typography, color, layout and visual symptoms, the intentional alternatives, a pre-ship checklist and six litmus tests (card, image, brand, copy, identity, editorial). For a design system it supplies defaults (light mode, no indigo, cards only for interaction) and a stance that every choice must be justified for this specific product.

## Key Ideas

- AI interfaces converge on the same patterns because models optimize for safe and average choices.
- Indigo/violet is the most recognisable fingerprint of AI-generated design; avoid it unless the brand requires it.
- Cards are justified only when the container is the thing the user interacts with.
- Light mode is the baseline unless the brief asks for dark.
- The calm editorial look (cream, big serif, one italic word, earth tones) is fine for content-led brands but slop elsewhere.
- A colored side stripe should mean something such as status, priority, owner or selection.
- Synthesis means picking one primary reference and keeping its signature traits, not averaging references.
- A token's role is part of the token; do not reuse a CTA-only accent as a background.
- Keep the media role of image-led references with real assets, simple code-native graphics or honest placeholders.
- Use one dominant color plus a sharp accent rather than an even spread of color.
- Run litmus tests before shipping, such as removing a card's border, shadow, background and radius to see if anything breaks.
- Every design choice should be explainable with a reason specific to this project.

## Entities

- [[entities/refero|Refero]] (product): Design reference library whose research the guide expects choices to be grounded in.
- [[entities/referodesign-refero-skill|referodesign/refero_skill]] (tool): The MIT-licensed agent skill repository this guide comes from.
- [[entities/tailwind-css|Tailwind CSS]] (library): Named as the reason training data is saturated with indigo.
- [[entities/lucide|Lucide]] (library): Icon library suggested instead of emoji.
- [[entities/phosphor|Phosphor]] (library): Icon library suggested instead of emoji.
- [[entities/heroicons|Heroicons]] (library): Icon library suggested instead of emoji.
- [[entities/token-role-drift|Token role drift]] (concept): Using a real style token outside the role its source assigned to it.
- [[entities/reference-averaging|Reference averaging]] (concept): Blending strong references into the least risky middle point, which erases their character.

## Topics

- [[topics/design-taste-and-judgement|Design taste and judgement]]: Names nine tells of AI-generated design and argues for intentional, project-specific choices over safe defaults.
- [[topics/ai-assisted-design|AI-assisted design]]: Explains why AI models default to indigo, cards, dark mode and calm editorial serif, and how an agent should avoid them.
- [[topics/color|Color]]: Bans indigo/violet without brand justification, warns against defaulting to warm ivory and earth tones, and asks for a dominant color plus a sharp accent.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Treats dark-by-default as an AI fingerprint; use light mode unless the brief asks for dark.
- [[topics/cards-and-sections|Cards and sections]]: Default is no cards; use sections, columns, dividers or media blocks unless the container is interactive.
- [[topics/typography|Typography]]: Warns against the decorative one-word serif/italic highlight, same weight throughout, and missing letter-spacing on all caps; asks for 3-4 hierarchy levels.
- [[topics/icons-and-imagery|Icons and imagery]]: No emoji as icons; preserve image-led media with real assets, simple code-native primitives or labelled placeholders, never weak CSS fakes.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: A token's role is part of the token; combine references by giving each source a bounded job.
- [[topics/landing-pages|Landing pages]]: Flags left-text/right-image heroes and generic section stacks; offers image, brand, identity and editorial litmus tests for the first viewport.

## Notable Claims

- AI models default to indigo/violet because training data is saturated with Tailwind's indigo and LLMs optimize for the average. Evidence: THE #1 TELL: INDIGO/VIOLET
- Cards are the second most common AI-slop pattern. Evidence: THE #2 TELL: CARDS EVERYWHERE
- Dark-by-default is an AI fingerprint just like indigo. Evidence: THE #3 TELL: DARK MODE BY DEFAULT
- Newer models avoid indigo by switching to a calm editorial template of warm ivory, oversized serif and earth tones. Evidence: THE #4 TELL: CALM EDITORIAL SERIF ON AUTOPILOT
- Standard emoji immediately signal that a design is AI-generated. Evidence: THE #5 TELL: EMOJI AS ICONS
- In shipped products the left accent stripe is reserved for callouts, alerts, active items, status and priority. Evidence: THE #6 TELL: LEFT ACCENT STRIPE
- AI models often do real research and then average strong references into the safest middle point. Evidence: THE #7 TELL: REFERENCE AVERAGING
- Agents collapse image-led references into text and CSS decoration because they cannot generate the image, losing the style's main carrier. Evidence: THE #9 TELL: FAKE GRAPHICS OR TEXT-ONLY COLLAPSE
- AI over-writes copy; real designers edit down. Evidence: Copy test

## Quotes

> A token's role is part of the token. Preserve it or do not use it.

> Serif fonts and earthy palettes are not banned. Autopilot "calm editorial" is.

> Synthesis means choosing and adapting, not finding the least risky intersection.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Written as instructions for an AI agent using Refero's MCP research; several rules assume 'Refero research' is available.
- Caveat: The claim about why AI defaults to indigo (Tailwind training data) is the authors' explanation, not a measured finding.
- Caveat: Opinionated defaults (light mode, no cards) are framed as hard rules; they are the source's stance for avoiding generic output, not universal standards.

### Rules and practices

- **must** (color, all): Do not use an indigo/violet accent unless the brand explicitly requires it; pick blue, teal or a brand color instead. Why: Indigo/violet is the universal fingerprint of AI-generated design. Values: #6366f1, #8b5cf6, #7c3aed, #2563eb, #0d9488. [RULE: NEVER use indigo/violet unless the brand explicitly requires it.]
- **must** (components, all): Default to no cards; group content with sections, columns, dividers or media blocks, and use a card only when the container is a clickable item, form or expandable panel. Why: AI wraps everything in rounded shadowed boxes because it feels safe; real designers use cards sparingly. [RULE: Default is NO cards.]
- **should** (components, all): Remove a card if taking away its border, shadow, background and radius does not hurt interaction or understanding. Why: Then it is not really a card. [Card test]
- **must** (color, all): Use light mode unless the brief explicitly asks for dark. Why: Dark mode is a deliberate brand choice, and dark-by-default is an AI fingerprint. [RULE: Unless the brief explicitly asks for dark — use light mode.]
- **must** (typography, all): Do not use the warm ivory + oversized serif + earth-tone 'calm editorial' pattern unless you can say why this product needs an editorial voice, a serif display face and earth tones, and which references support it. Why: It suits editorial, cultural, hospitality or fashion brands but is AI slop on dev tools, SaaS, fintech or dashboards. [RULE: Do not use the calm editorial serif + earth-tone pattern]
- **should** (typography, all): Do not swap one word or short phrase of a headline into a different serif, italic or color just to add 'taste'; create distinction through layout, scale, weight, media or a source-backed color role. Why: The decorative one-word treatment is now a common AI default. [Specific fingerprint to avoid]
- **must** (iconography, all): Never use emoji as icons unless the user explicitly asks; use an icon library, Unicode symbols or SVG. Why: Emoji make a design look cheap, unfinished and AI-generated. Values: →, •, ◆. [RULE: Never use emoji unless the user explicitly asks for them.]
- **must** (components, all): Use a colored side accent stripe only when it communicates status, priority, owner or selection, never as decoration. Why: If you cannot say in one word what the color means, it is decoration. Values: border-left: 4px solid <accent>. [THE #6 TELL: LEFT ACCENT STRIPE]
- **must** (process, all): When references conflict, pick one primary direction and keep its signature traits; let secondary references add only 1-2 specific details. Why: Averaging turns bold references into the same safe cream-and-clay look. Values: 1-2. [THE #7 TELL: REFERENCE AVERAGING]
- **must** (tokens, all): Keep each token in the role its source gave it: do not turn a CTA-only accent into backgrounds or badges, or code syntax colors into UI accents. Why: Changing what a token means is a failure mode; uniqueness should come from composition. [THE #8 TELL: TOKEN ROLE DRIFT]
- **must** (iconography, all): Preserve the media role of an image-led reference with a real asset, stock or generated image, a simple code-native graphic, or an intentional placeholder with fixed aspect ratio, art direction and alt/caption; never fake photos or complex art with CSS blobs. Why: Collapsing image-led styles into text and CSS loses the style's main carrier. [THE #9 TELL: FAKE GRAPHICS OR TEXT-ONLY COLLAPSE]
- **should** (typography, all): Add letter-spacing to ALL CAPS and small text. Why: Missing letter-spacing on all caps is a generic-design symptom. [ALL CAPS text has letter-spacing]
- **should** (typography, all): Build a clear type hierarchy of 3-4 distinct levels, differentiated by weight and spacing as well as size. Why: Same weight throughout and no display/body distinction look generic. Values: 3-4. [Typography with purpose]
- **should** (color, all): Use a dominant color plus one sharp accent instead of evenly distributed color. Why: Perfectly even color distribution with no accent hierarchy looks generic. [Color with meaning]
- **consider** (layout, all): Break the grid intentionally with one element, not everything. Why: Visual tension comes from intentional asymmetry; perfectly symmetrical everything looks generic. [Layout with intention]
- **should** (layout, web): If the first viewport works fine without the hero image, make the image dominant or remove it. Why: The image is too weak. [Image test]
- **should** (content, all): If deleting 30% of the copy improves the page, keep deleting. Why: AI over-writes; real designers edit down. Values: 30%. [Copy test]
- **should** (layout, web): If the brand disappears after hiding the nav, make it louder: a bigger logo, brand color in the hero, or distinctive typography. Why: Hierarchy is too weak. [Brand test]
- **should** (layout, web): If the first viewport could belong to any other company, add the one detail that makes it unmistakably this brand. Why: Branding is too weak. [Identity test]
- **should** (layout, web): If swapping the logo for a coffee shop, boutique hotel or literary magazine still leaves the hero plausible, make the visual language specific to the actual product. Why: The design is probably generic calm editorial slop. [Editorial test]
- **should** (color, all): Do not use gradients that do not serve a function, or abstract blob backgrounds and generic 3D illustrations. Why: They are listed as symptoms of generic design. [gradients that don't serve function]
- **should** (color, all): Make semantic colors actually semantic, and build the palette from references rather than defaults. Why: Colors used outside their stated role, or chosen by default, read as generic. [Make semantic colors actually semantic]

### Decisions it informs

- What accent hue should the product use when there is no brand color? (`Q-color-01`)
  - Indigo/violet: Reads as the default AI-generated look. When: Only when the brand explicitly requires it.
  - Blue #2563eb: Feels trustworthy and professional. When: A general professional product.
  - Teal #0d9488: Feels fresh and distinctive. When: You want to stand apart from generic SaaS.
  - Brand color: Feels authentic and intentional. When: A brand color exists.
  - Recommendation: Avoid indigo/violet; use a brand color, or blue or teal, because indigo is the fingerprint of AI design.
- Should the default color mode be light or dark? (`Q-theme-01`)
  - Light: The professional baseline. When: The brief says nothing about color mode.
  - Dark: A deliberate brand statement. When: The brief explicitly asks for dark.
  - Recommendation: Light unless the brief explicitly asks for dark.
- How should content be grouped: cards or open layout? (`Q-dir-04`)
  - Cards: Rounded boxes with shadows around each group. When: The container is a clickable item, form or expandable panel.
  - Sections, columns, dividers or media blocks: Calmer, less templated grouping. When: The default for everything else.
  - Recommendation: No cards by default; cards only for interaction.
- Which visual direction fits the product?
  - Calm editorial serif with earth tones: Warm ivory, oversized serif headline, olive/clay/terracotta accents, airy spacing. When: Publishing, culture, fashion, hospitality or other content-led brands.
  - A sharper product-specific direction: Technical, utilitarian, high-contrast, image-led, data-dense, playful, industrial, clinical or luxury. When: Dev tools, enterprise SaaS, fintech, dashboards and functional product UI.
  - Recommendation: Choose the editorial direction only when product context and research justify it; otherwise choose a direction grounded in research.
- When the needed image is unavailable, what should stand in for it?
  - Real or generated asset: Keeps the reference's media role intact. When: A screenshot, provided asset, stock or generated image is available.
  - Code-native primitive: Honest simple graphic. When: Simple diagrams, icons, charts, code windows, grids or geometric patterns.
  - Intentional placeholder: Fixed aspect ratio, art direction and alt/caption hold the composition honest. When: No suitable asset exists.
  - Text-only or CSS blob fake: Loses the style's main carrier and looks fake. When: Never.
  - Recommendation: Use a real asset first, a code-native primitive for simple graphics, and a placeholder only when nothing suitable exists.

### Process

1. Check for the nine tells: Review the design for indigo, default cards, dark default, autopilot editorial serif, emoji icons, decorative stripes, averaged references, token role drift and faked media.
2. Justify any editorial serif direction: Answer why the product needs an editorial voice, why a serif display face, why earth tones, and which references support it; if you cannot, pick a sharper direction.
3. Lock a primary reference: When references conflict, choose one primary direction, preserve its signature traits, and let secondary references contribute 1-2 details.
4. Assign bounded jobs to sources: Give each reference a role, for example one owns canvas and type, another the code window, another the primary CTA, and keep their rules.
5. Run the slop detector checklist: Tick each item before shipping, including accent not indigo, cards justified, light mode, ALL CAPS letter-spacing and the screenshot test next to real products.
6. Run the litmus tests: Apply the card, image, brand, copy, identity and editorial tests and fix what fails.

### Examples and visual references

- Reference averaging failure: A dark workbench, an acid-yellow docs site, a saturated orange brand and a serif editorial page all collapse into the same warm cream canvas with muted clay accents.
- Token role drift: An acid-yellow reserved for the primary CTA ends up as a section background; syntax colors leave the code window and become UI accents.
- Editorial test: Swap the logo for a coffee shop, boutique hotel or literary magazine; if the hero still feels plausible, it is generic calm editorial slop.
- Safe vs intentional pricing: 3-column pricing because everyone does it versus 2-column pricing because the product has only 2 tiers.
- Left accent stripe: A 4px colored bar on a card's left edge, acceptable only for callouts, alerts, active list items, status or priority.

### Numbers

- #6366f1, #8b5cf6, #7c3aed: The indigo/violet hexes AI models default to. [THE #1 TELL: INDIGO/VIOLET]
- 4px: Width of the typical decorative left accent stripe. [border-left: 4px solid <accent>]
- 1-2: Specific details a secondary reference may contribute. [Secondary references may contribute 1-2 specific details]
- 3-4: Distinct type hierarchy levels to create. [Create clear hierarchy (3-4 distinct levels)]
- 30%: Share of copy to try deleting in the copy test. [If deleting 30% of copy improves the page]
- #2563eb, #0d9488: Blue and teal suggested in place of indigo and violet. [Instead of / Try table]

<!-- /od:learn -->
