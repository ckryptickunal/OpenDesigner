# Style research schema (U9)

Write a JSON array to the output path you were given. One object per style. Every field below is required unless marked optional.

```json
{
  "id": "kebab-case-id",
  "name": "the name designers use",
  "aliases": ["other names designers use"],
  "plain": "what it looks like, in at most 12 plain words a 10-year-old understands",
  "people_say": ["5-10 everyday words or short phrases a non-designer would use to ask for this look"],
  "origin": "where and when it comes from, one line, with the source id in brackets, e.g. 'Milan, 1981 [S1]'",
  "defining": ["3-5 concrete, visible traits with numbers where the sources give them"],
  "code": "one line of CSS (or platform code) that carries the look",
  "traits": {
    "surface": "solid|translucent|gradient|textured|metallic|glossy|paper|luminous",
    "edge": "none|hairline|outline|thick-outline|beveled|glow|rough",
    "depth": "flat|ring|tonal|soft-shadow|hard-offset|extruded|inner|glass|glow|long-shadow|layered",
    "shape": "sharp|subtle|rounded|pill|blob|geometric|irregular|pixel",
    "color": "monochrome|muted|neutral-accent|tonal|vivid|neon|pastel|earthy|duotone|spot-inks|metallic|rainbow",
    "contrast": "low|normal|high",
    "type": "neo-grotesque|geometric|humanist|serif|slab|rounded|mono|pixel|condensed|display|script|handwritten|blackletter",
    "texture": "none|grain|halftone|scanlines|paper|dither|pattern|glitch",
    "ornament": "none|geometric-shapes|squiggles|stickers|illustration|photo|3d-objects|ascii|ornamental",
    "layout": "grid|bento|editorial|asymmetric|collage|dense|minimal|full-bleed|layered",
    "motion": "still|subtle|springy|bouncy|stepped|glitchy|kinetic|parallax",
    "theme": "light|dark|both|dark-first"
  },
  "ui_fit": "core-ui|marketing|illustration-only",
  "fits": "one line: products and moments it suits",
  "goes_wrong": "one line: the most common way it fails",
  "accessibility": "one line: the accessibility risk and its fix (contrast 4.5:1 text, 3:1 edges, reduced motion, reduced transparency)",
  "related": ["ids of close styles, from the existing list or your own"],
  "sources": [{"id": "S1", "url": "https://...", "supports": "which claim this page supports"}],
  "examples": [{"name": "real product or site", "url": "https://...", "what": "what in it shows the style"}],
  "confidence": "high|medium|low"
}
```

Each trait takes exactly one value from its list (the strongest one). If none fits, use the closest and say so in `defining`.

## Rules
1. Open every source you cite and check that it says what `supports` claims. At least two sources per style; at least one that is not Wikipedia or an aesthetics wiki (a design publication, a museum, a platform's own documentation, a design-system site, NN/g, Smashing, Figma, Awwwards, Webflow, Behance or Dribbble articles, a book publisher page).
2. Never invent a product example. Give an example only when a source shows it. `examples` may be empty.
3. Mark any number you estimated rather than read with `[inferred]` inside the string.
4. Write in plain English. No em dashes. Never copy more than 15 words from a source.
5. References give structure, never identity: describe the look, never a brand's logo, exact brand color or proprietary typeface as something to copy.
6. Skip anything that is only a fashion or interior trend with no visual-design meaning for screens, posters or brand surfaces.
7. Do not repeat a style that is already in the catalogue (list below) or in another agent's list, unless you have a clearly distinct variant; then give it a distinct id and say what differs.

Existing catalogue ids (already covered): glassmorphism, neumorphism, claymorphism, skeuomorphism, flat, material-elevation, neo-brutalism, brutalism, comic, memphis, bauhaus, swiss, editorial, minimal-monochrome, bento, mesh-gradient, grain, duotone, risograph, art-deco, y2k, frutiger-aero, pixel-art, terminal, dark-luxe, playful, organic, isometric.
