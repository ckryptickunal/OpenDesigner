# Figures

Illustrations for the docs, drawn in code from the brand tokens. A docs page shows one with a line of its own:

```
{{figure:design-tokens-tiers}}
```

`site/build.py` inlines `site/figures/design-tokens-tiers.html` there. The Markdown copies and `llms-full.txt` keep the caption instead.

## One file per figure

- The file is one `<figure class="fig">…</figure>` with a `<figcaption>` as its last child. The caption says what the picture shows, in one or two sentences, so it also works as the alt text.
- Inside it, one frame from `site/static/figures.css`:
  - `.fig-panel`: a dot grid for diagrams, flows and comparisons.
  - `.fig-scene` with `data-scene="<name>"`: a free Unsplash photo with film grain and a `.fig-card` floating on it, for a real piece of product UI. The build adds the photo and credits the photographer. Scenes: `blue-gradient`, `blue-waves`, `sky-trees`, `forest`, `blue-soft`, `woods-sage`, `blue-stripes`, `blue-pattern`.
  - `.dodont` with a `.do` and a `.dont` box: guidance as a comparison.
- Build with the kit's classes and inline styles that use the CSS variables (`var(--accent)`, `var(--ink-muted)`, `var(--space-16)`, `var(--radius-container)`). Inline SVG is welcome: `viewBox`, `width="100%"`, `aria-hidden="true"`, `font-family` set on text. No scripts, no `<img>`, no external links.
- Two fonts: the brand face, inherited, and Source Code Pro through `.mono`, `.num` and `.kicker`. Highlight with weight, a chip or the accent. Status colors only through `var(--ok)`, `var(--warn)`, `var(--bad)` and their `-soft` fills.
- Real content only: questions and options from `skills/opendesigner/references/questions.json`, token names and values from `brand/opendesigner/build/css/tokens.css`, commands from the docs, dial values from `brand/opendesigner/state.json`. Nothing invented, no company names or logos.
- The content column is 760 px wide. Every figure also has to work at 360 px: the kit's flows and grids stack on their own; never fix a width wider than 100%.
- Small text is 12 px or larger, and text contrast stays at 4.5:1 or better.
