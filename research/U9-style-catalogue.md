# U9: An open style space (named styles, trait axes and a style lab)

## Lane overview

- **Why.** Kunal asked for OpenDesigner to know many more visual styles and to stay open: not limited to a fixed list, but able to explore, discover and make experimental styles. Most people have no word for the look they want, so the tool names styles for them, shows them and turns a pick into settings (U8 did this for 28 styles).
- **What this lane did.** Researched 105 more named styles in five families, checked every source twice, put every style on the same 15 trait axes, and built a style lab in the engine that searches, shows, mixes, changes and invents styles on those axes while the accessibility floors stay locked.
- **Where the results live.**
  - `synthesis/styles.json`: the catalogue (133 styles), the axes, look words and trait words. Shipped as `skills/opendesigner/references/styles.json`; listed by `tools/build_data.py` in `references/style-catalog.md`.
  - `skills/opendesigner/references/style-lab.md`: how to explore styles with a person, and the evidence behind it.
  - `skills/opendesigner/scripts/engine.py`: `engine.py style list|show|search|tiles|mix|mutate|explore|define`, the `glow` depth model, halftone and scanline textures, the type scale per style, and custom styles in `state.customStyles`.
  - `research/U9-raw/`: the research schema, the five family files, the methods research and the five verification reports, as written by the agents.
  - `traces/U9-trace.md`: every source, with what it supports and what the verifier found.
- **Authority.** Reference material. Style descriptions shape options and words; dial positions are placements [inferred]. No house standard, default or question changed.

## Method

1. **Schema.** One JSON schema for every style: plain words (at most 12), the words people say, origin, defining traits, a line of code, one value on each trait axis, where it fits (product screens, marketing, or illustration only), how it fails, its accessibility risk, related styles, at least two opened sources (one not a wiki), and examples only when a source shows them (`research/U9-raw/SCHEMA.md`).
2. **Five research agents, one per family**, each told what the others covered so nothing was repeated: art and graphic design movements (22), computing eras and platform languages (21), internet aesthetics (21), current web and brand trends (22) and material and craft techniques (22).
3. **A methods agent** researched how to explore and generate styles, how to break a style into attributes, and the evidence on novelty against familiarity (`research/U9-raw/F-exploration-methods.md`, 60 sources).
4. **Merge.** A script checked every entry (ids, trait values, sources, length of the plain line, no em dashes), folded one duplicate (the sci-fi game interface into the film one), kept generic and color words out of the look words, and marked mood words ("nostalgic", "surreal", "handmade") as suggest-only, so they list styles but never start a sketch from one.
5. **Verification.** Five fresh agents opened every source again and checked origins, defining traits, code and examples. Of 108 entries, 50 were sound, 56 needed a correction and 2 were dropped. Every correction was applied by hand from the reports.

## What the verification changed

- **Dropped:** "manga UI" (no source names it as a style) and "window light" (only one source names the trend).
- **Renamed:** "Frutiger Metro" became Vectordelia (the label is contested), and "indie web" became Handmade web (the IndieWeb is a technical movement, not a look).
- **Identity:** brand logos used as examples were replaced (a band logo, a trade-union logo), aliases that name a living brand were removed, the brat entry no longer gives the album's exact green, and code samples name open fonts instead of Apple's and Microsoft's system faces.
- **House color rule:** the neo-heritage palette, which nearly matched a fast-food brand's brown, orange and cream, became "a period palette from the brand's own archive". No style sets warmth above 45.
- **Facts:** corrected origins (Vienna Secession, Dada photomontage, supergraphics, grunge typography, classic Mac system versions, marbling, McBling), study claims (Material 3 Expressive's 4x result came from one eye-tracking study), e-ink grey levels, and code that did not do what it said (a one-direction blueprint grid, CSS that claimed to dither, a Rough.js call that never drew).

## Decisions

### The trait axes (15)
- **Decision.** Every style is one value on 15 axes. Bones (shape, type, scale, layout, density, theme) are kept typical when experimenting; skin (surface, edge, depth, color, contrast, texture, imagery, ornament, motion) is where novelty is spent. Motion techniques (parallax, moving type, scroll-linked motion, autoplay loops, flashing) are flags, not a look, because each has its own accessibility rule.
- **Changes from the first 12 axes, from the methods research:** density split out of layout; imagery split out of ornament; scale added; glow kept only in depth and paper only in texture; theme made a default (both themes are always built); motion techniques made flags. Splitting color into palette and saturation, and adding type weight and width, were left for later (medium confidence, and the 133 entries would need remapping by hand).
- **Evidence.** Typicality and novelty predict preference jointly ([Hekkert, Snelders and van Wieringen 2003](https://pubmed.ncbi.nlm.nih.gov/12648393/)); complexity and prototypicality shape first impressions within 17 ms ([Tuch et al. 2012](https://research.google.com/pubs/archive/38315.pdf)); complexity costs the most appeal ([Reinecke et al. 2013](https://kgajos.seas.harvard.edu/papers/reinecke13aesthetics.pdf)); flashing and autoplay have their own success criteria ([WCAG 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html), [2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)).

### How new styles are made
- **Decision.** The lab is a morphological box: blends cross one style's bones with another's skin, and mutations borrow one skin trait from a far style. Every candidate is repaired (one surface effect, at most 3 loud traits on product screens and 4 on marketing, no glass or texture on dense screens, neon designed dark first) and kept inside a novelty budget: 2 to 5 traits from the nearest named style for product screens with at most 1 in the bones, 4 to 7 for marketing, 3 to 10 with `--wild` [inferred numbers; the research supports the direction]. Directions are picked farthest-first and are repeatable by seed. A name made in the lab is marked as coined.
- **Evidence.** [Ritchey, General Morphological Analysis](https://www.swemorph.com/ma.html); [Fauconnier and Turner 1998](https://doi.org/10.1207/s15516709cog2202_1); one effect per surface (DC-L19-67); piled-up effects read amateur (S-L19-045); atypical designs grow on people with exposure ([Landwehr, Wentzel and Herrmann 2013](https://doi.org/10.1509/jm.11.0286)), while weak signifiers get worse ([NN/g 2015](https://www.nngroup.com/articles/flat-design-long-exposure/)).

### How a style is shown and admitted
- **Decision.** Directions are shown as tiles of real components, built for real from the person's state, in light and dark (`engine.py style tiles`, `--tiles`), with the recommendation in the middle. A new look joins the catalogue when at least two independent sources use its name and it differs from every entry on at least 3 axes; one maker's signature look never does.
- **Evidence.** Style tiles ([Warren 2012](https://alistapart.com/article/style-tiles-and-how-they-work/)) and element collages ([Mall 2012](https://v3.danmall.com/articles/rif-element-collages)); the compromise effect ([Simonson 1989](https://academic.oup.com/jcr/article-abstract/16/2/158/1795321)); web layouts growing alike ([Goree et al. 2021](https://doi.org/10.1145/3411764.3445156)).

## Open questions / gaps

- **Measured typicality.** The novelty budget counts distance from the nearest named style. The research says to count distance from the product's own category too (for example the centre of a set of Mobbin screens from that category). Not built.
- **Rendered checks.** A visual-complexity score of the rendered tiles, and text contrast measured against the worst pixels behind it (glass, glow, gradients, textures, photos), belong in preflight or the review skill. Not built.
- **Axis refinements left open:** palette versus saturation, type weight and width, and a pairwise consistency matrix in place of the rule list.
- **Not yet buildable:** gloss, chrome, holographic foil, long shadows, dithering, glitch, repeating patterns and stepped motion. They are named as assets or suggestions.
- **Trend styles date.** Current trends were named in 2024 to 2026 sources; review them after about 18 months.
- **Weakly sourced entries:** Vectordelia (low confidence), quiet luxury (one source uses the name, plus an agency release), and the radius suggestions several internet-aesthetic entries take from one design-system site.

## Confidence

- **High:** the catalogue's facts after two passes (every source opened twice, corrections applied); the trait model's direction (bones typical, skin novel), backed by peer-reviewed studies.
- **Medium:** trait placements and dial values per style [inferred], and the guard rules' thresholds.
- **Low:** the novelty budget's numbers, which are estimates in the direction the evidence points.
