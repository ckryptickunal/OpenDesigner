# Product brief: the process the builder should run

Kunal's direction, 2026-09-23. Every synthesis, design and research agent reads this before starting.

## The aim
Make creating design systems, designs and visuals a beautiful, visual process for engineers and technical people, the way Figma makes it for designers. The builder does not eliminate the designer.

## The process, in Kunal's words (lightly cleaned up from voice dictation)
> "First of all [we are] defining what are the building blocks, what is needed, how these shape things going ahead. Then we do two things. We do not eliminate the need of a designer, but we keep open placeholders or open hooks or open places where we ask the person using the system: do you have this building block? Do you have this building block? For example, there could be something that we can't define, like a logo or an icon, that either only a designer can make, or the engineer would have to use a tool to make. So we'll ask them for resources like that. But for building blocks like paddings, margins, primitives, components, this should be a visual-first interactive mode, with minute details about these building blocks in it, which inherently helps the user figure out what they should use and where they should use it. It should be open in the context, where the user can also add an example website, an example resource, or something which helps the AI system or LLM that we are using figure out what the reference is using, and then build upon it. Make sure you miss nothing in this context."

## What that means as requirements
1. **Define the building blocks first.** The builder starts from a complete ontology of what a design system needs, and shows how each block shapes what comes after it (the decision graph).
2. **Designer hooks, not designer replacement.** Some blocks cannot be generated well (logo, brand mark, custom icons, illustration, photography, brand typeface, and similar). For each, the builder asks "do you have this?", accepts the resource in useful formats, and offers paths when the answer is no: commission a designer, or use a named tool, with honest caveats.
3. **Visual-first, interactive editing for generatable blocks.** Spacing, margins, primitives, tokens and components are edited visually, with fine detail about each block: what it is, where to use it, where not to, and a live preview of its effect. The interface teaches as it goes.
4. **Reference intake.** At any point the person can add an example website, screenshot, Figma file or other resource. The AI reads what the reference uses (color, type, spacing, radius, motion, components) and builds on it, copying structure and quality, never another brand's identity.
5. **Nothing missed.** Coverage is checked against the ontology, so no building block is silently skipped.

## Round trip
Designs and tokens should move between the builder, Figma and Paper, and code. Kunal has a full Figma seat.
