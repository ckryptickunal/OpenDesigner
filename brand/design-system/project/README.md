OpenDesigner is a free, open-source helper that builds a design system with the AI a person already uses, one plain question at a time. The brand should feel like that product: calm, exact, and generous with space. It never shouts. One thing on each screen is allowed to be loud.

## Voice

- Write plain words, outcome first, short sentences. The README's own line is the model: "Make your app look good and stay consistent, with the AI you already use."
- Say what happens, not how the machinery works: "It asks five questions," not "a zoom-0 sketch".
- Sentence case everywhere, including buttons and headings. No exclamation marks, no emoji, no hype words (revolutionary, magic, effortless).
- Never name another company or product in brand material, including the AI tools it works with. Say "the AI you already use".

## Color

Three themes, each with strong tonal contrast. Light grounds carry near-black text, and dark grounds carry near-white text. Nothing sits in the middle.

- **Light** (default): `ink` on `surface`. Use for the README, documentation images and most posts.
- **Dark**: `ink` on `surface` in the dark theme. Use it for night posts and anything that shows code.
- **Cobalt**: white `ink` on cobalt `surface`. Use it once per set (one slide in a carousel, one post in a week) for the statement you most want remembered.
- `accent` (cobalt) marks exactly one thing per screen: the primary button, the `highlight` box or the circle in the mark. Two cobalt things on one screen means one of them is wrong.
- `ink-muted` is for ledes and captions only. Never put muted text on a tinted ground.
- No gradients and no brown, cream or warm-black grounds. The neutrals are cool on purpose.

## Type

**Two fonts at most in anything you make, and usually one.** Hanken Grotesk sets every word. Source Code Pro appears only for real code: commands, file names, token names. Never use mono for labels or decoration.

- **Titles are light, not bold.** `display` and `h1` are weight 300, `h2` and `h3` are 400, and only `h4` and smaller go to 500–600. Size and space carry the hierarchy, and weight is saved for emphasis.
- Use the **Web** styles for pages, the **Social canvas** styles for 1600-wide images, and the **Code** styles for code. Never invent a size. If a size seems missing, use the nearest style and change the layout instead.
- A web page uses at most six of the styles. A post uses at most four (statement or headline, subhead, body, label).
- Tracking tightens as size grows, as each style sets it (−0.035em at 162 px, 0 at body size). Don't add more.
- Heading levels map as follows:

| HTML | Style | Size / line | Weight |
|---|---|---|---|
| hero H1 | `display` | 90 / 92 | 300 |
| h1 | `h1` | 67 / 72 | 300 |
| h2 | `h2` | 51 / 56 | 400 |
| h3 | `h3` | 38 / 44 | 400 |
| h4 | `h4` | 28 / 36 | 500 |
| h5 | `h5` | 21 / 28 | 600 |
| h6 | `h6` | 16 / 24 | 600 |
| p | `body` | 16 / 24 | 400 |

The smallest text is `caption` at 12 px, above Apple's 11 pt and Material's 11 sp minimums. Body text is 16 px.

### Highlighting a phrase

A headline may highlight one phrase, and only one. There are three ways, from loudest to quietest:

1. **Fill box** (`highlight` behind `on-highlight`). This is the strongest pull on the screen, so use it only when that phrase is the single thing to remember and nothing else on the screen is cobalt. Keep the phrase on one line and give the headline at least 1.08 line height so the box clears the line above.
2. **Weight.** The phrase is set at 650 inside a 300 headline, in the same color. It's a medium pull and works on every theme. It's the default.
3. **Color.** The phrase is set in `accent-text` at the same weight. It's the quietest, and it suits running text more than headlines.

Never use an italic serif word, and never combine two methods.

Before choosing, squint at the whole screen and find where the eye lands first. That should be the highlight. If it's a picture or a button instead, use the quieter method or drop the highlight.

## Space and layout

- Space comes from the `space-*` steps. Posts use `space-80` margins at 1600 wide and `space-64` at 1080 wide.
- Leave a lot of empty space. A post holds one idea, one headline and at most one specimen.
- Specimens (a dial, a ramp, a file tree) sit on `surface-raised` with `radius-overlay` and `shadow-raised`. Nothing else gets a shadow.
- Corners follow `radius-control` (6 px) for controls and `radius-container` (8 px) for panels. Pills use `radius-full`.

## Logo

The mark is four tiles that go from a square to a circle: a scale, which is the core of every design system. The circle is the decision, so it takes the accent. The lockup is the mark and "OpenDesigner" in Hanken Grotesk Medium, outlined.

- Use `lockup-light` on Light, `lockup-dark` on Dark and `lockup-cobalt` on Cobalt. Don't recolor them otherwise.
- When a screen already spends its one accent (a highlight box, a primary button, a cobalt tile), use the one-color `lockup-light-mono` or `lockup-dark-mono`.
- Keep a clear space of half the mark's width around the lockup. The smallest lockup is 24 px tall, and the smallest mark is 16 px.

## Imagery

- Photography is allowed when it's real and quiet: hands, paper, tools, materials and light, in black and white or cool tones. Fake customers and faces are not allowed.
- Art made in code is welcome when it comes from the tokens, such as the mark's tiles repeated as a pattern.
- Don't use stock illustrations of "people at laptops".

## Accessibility

Every text pair above passes WCAG 2.2 AA (4.5:1) in all three themes, and borders, the focus ring and the highlight box pass 3:1. Focus is a 2 px `focus-ring` with a 2 px gap. Motion respects reduced motion.
