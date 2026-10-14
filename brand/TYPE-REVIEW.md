# Type review: what went wrong, and what good type needs

You were right: the colors, layout and graphics hold up, and the type doesn't. This file has three parts: what I did wrong (measured, not guessed), what I know about typefaces, type scales and setting type, and what OpenDesigner itself should change so the next agent doesn't repeat it.

Sources: the repo's own research (`research/L02-typography.md`, cards DC-L02-01 to 28), the learning wiki (`learn/wiki/topics/typography.md`), Google Fonts' live font list (fetched 2026-10-14), Inter's published tracking formula, and MDN's browser data. Where something is my own judgment, it says so.

---

## 1. What I did wrong

I measured every text element in the 25 brand images with a script.

| Problem | Evidence | Why it hurts |
|---|---|---|
| **No type scale at all** | 45 different font sizes across 25 images. One post (x-05) uses 11 sizes and one slide (carousel-04) uses 12. Near-duplicates everywhere: 20/21/22, 26/27, 33/34, 40/41 px. Headlines are 82, 100, 106, 108, 116, 118, 136 and 150 px. | Sizes that are almost the same look like mistakes, not choices. The wiki's sources say a landing page should use at most about six sizes; Refero says 6 to 8 in a whole product. |
| **I ignored the system I made** | The engine gave me a scale: 12, 16, 21, 28, 38, 51, 67, 90 (ratio 1.333). I worked out every size as a fraction of the canvas instead, so not one size came from it. | The whole pitch is "your AI follows the system". I didn't. |
| **The one-italic-serif-word trick, on every image** | Every headline has one or two words in Playfair Display Italic. The repo's wiki already names this as an AI tell (Refero's anti-AI-slop guide: "cream, big serif, one italic word"). | It reads as a template. Done everywhere, it stops meaning anything. |
| **The two faces fight** | Geist is set at weight 600 and Playfair Italic at 400. Their x-heights are almost the same (0.53 and 0.514 of the size; I measured the font files), so size isn't the problem. Weight is: Playfair has hairline strokes, so the italic word looks pale and leaves a light patch in the middle of a dark line. | Uneven "color" (how dark a line of text looks) is the first thing a type designer notices. |
| **Tracking far too tight** | Every headline is tracked −0.052em, at 64 px and at 150 px alike. For comparison, Inter's published formula never tightens past about −0.022em. | Letters start to touch and the word turns into a blob, worst at the smaller headline sizes. Tracking should change with size. |
| **Monospace used as decoration** | Mono, uppercase, wide-tracked "eyebrows" on every image, and mono inside pills for plain words like "A recipe app". The wiki's "Designing with Claude Code" source lists mono uppercase eyebrows as part of that look. | Mono should mean code, data or a file name. Used everywhere, it's another fingerprint. |
| **A borrowed face** | Geist is a good UI face, but it's another company's house typeface (Google Fonts lists that company's founder among its designers). | Our brand reads as theirs. AGENTS.md: references give structure, never identity. |
| **One weight for every size** | Headlines are weight 600 whether they're 64 px or 150 px. | Big type looks heavier than small type at the same weight. Display sizes usually want a lighter weight, or a font with optical sizes. |
| **Leading too tight for the serif** | Headline line height is 0.94, with italic descenders (g, y) on the line above capitals. | Near-collisions between lines. |
| **Hierarchy by gray only** | Ledes are 33–42 px, weight 400, in muted gray, so they're separated from the headline only by color. | It looks washed out, especially on Paper. |

**Why OpenDesigner didn't stop me (process findings):**
- The engine's default face is `system-ui`. The sketch never asks for a typeface, so there's no brand face in the tokens.
- There's one scale with one ratio, 8 steps, stopping at 90 px. There's no separate display set for marketing, posters or social images, although the research (DC-L02-11) recommends one.
- Preflight and review don't count sizes, find near-duplicate sizes, or flag the italic-word or mono-everywhere patterns.
- The wiki already knew about two of these mistakes, but nothing in the build path sends an agent there.

---

## 2. Typefaces

### What a typeface says

| Kind | Looks like | Usually reads as | Open examples (Google Fonts) |
|---|---|---|---|
| Neo-grotesque sans | Helvetica family: even, closed shapes | neutral, efficient, corporate | Inter, Hanken Grotesk, Schibsted Grotesk |
| Grotesque (older) | quirkier, uneven widths, character in a, g, R | crafted, confident, a bit European | Bricolage Grotesque, Familjen Grotesk |
| Geometric sans | circles and straight lines | modern, friendly, fashionable; weaker in long text | Outfit, Urbanist, Syne (expressive) |
| Humanist sans | pen-stroke shapes, open | warm, legible at small sizes | Source Sans 3, Atkinson Hyperlegible Next |
| Old-style serif | soft, calligraphic | literary, warm, historic | EB Garamond, Cormorant Garamond |
| Transitional or modern serif | sharp contrast, vertical stress | fashion, luxury, editorial | Playfair (new), Bodoni Moda, Libre Caslon Display |
| Contemporary text serif | sturdy, built for screens | serious journalism, trust | Newsreader, Source Serif 4, Literata, Fraunces |
| Slab | thick, square serifs | sturdy, mechanical, friendly | Roboto Slab, Young Serif (soft) |
| Monospace | every letter the same width | code, data, technical | JetBrains Mono, IBM Plex Mono, Martian Mono |

These readings are cultural and change with time and audience (DC-L02-02). Pick from the brand's adjectives, then test.

### What to look at when choosing
- **x-height** (how tall the lowercase is). Large means legible at small sizes but less elegant at big sizes; small means elegant but needs more size.
- **Width.** Condensed type fits more words and feels urgent; wide type feels calm and luxurious. Families with a width axis give you both.
- **Contrast** (thick against thin strokes). High contrast is beautiful big and breaks up small.
- **Apertures** (how open c, e, a are). Open shapes stay readable small; closed ones feel tight and formal.
- **Character letters.** a, g, R, G, &, ? and the figures carry the personality. Test those.
- **Range.** Weights, a true italic (not a slanted roman), and ideally **optical sizes** (the font redraws itself for small or big use). Google Fonts confirms these have an optical-size axis: Fraunces (9–144), Newsreader (6–72), Bricolage Grotesque (12–96), Source Serif 4 (8–60), Literata (7–72), Bodoni Moda (6–96), Playfair (new version, 5–1200), Inter (14–32 on Google Fonts; the copy installed on this Mac doesn't have it).
- **Language coverage**, if the product needs other scripts.
- **Licence.** Open (SIL OFL or Apache) is fine everywhere. Trial and demo fonts on this Mac (several are installed) are not.

### What to avoid
- **Defaults as a brand voice:** system UI, Inter and Geist are excellent for product UI and say nothing about a brand. Fine for body text, weak for a hero.
- **Faces tied to another company:** Geist (from a hosting company), Mona Sans and Hubot Sans (from the code-hosting platform), SF and New York (licensed only for that company's platforms).
- **Overused display faces** (my judgment): Playfair Display, Montserrat, Poppins, Bebas Neue. They aren't bad, just so common that they read as a template.

---

## 3. Pairing

- **Start with one family.** Its weights, widths and optical sizes may already give enough contrast. Most shipped systems use one UI family plus a mono (DC-L02-03).
- **Add a second face only for a job:** a change of context (quotes, editorial), brand moments, or missing scripts.
- **Contrast on one axis, harmony on the others.** A serif with a sans is fine if they share proportions, x-height or era. Two similar sans faces look like a mistake.
- **Match how dark they look, not their weight numbers.** A high-contrast serif next to a 600 sans needs a heavier weight or a bigger optical size to look as dark. Check it by squinting at the line.
- **Match x-heights** with CSS `font-size-adjust` when two faces sit on one line. It's supported in Chrome 127+, Safari 16.4+ and Firefox (MDN data).
- **Italic is for emphasis inside text,** where a reader would stress a word. It isn't decoration for headlines.

Pairings worth trying (starting points to test, not rules):
- **One superfamily:** IBM Plex Sans + Plex Serif + Plex Mono, or Source Sans 3 + Source Serif 4 + Source Code Pro.
- **Editorial:** Newsreader for headlines with Schibsted Grotesk for text.
- **Crafted and warm:** Bricolage Grotesque for everything (optical size does the work), plus JetBrains Mono for real code.
- **Luxury:** Bodoni Moda (big optical size) with a quiet grotesk at small sizes.

---

## 4. Type scales

A **type scale** is a short, fixed list of sizes that every text element must pick from. Most come from a **ratio**: each step is the last one multiplied by it.

| Ratio | From 16 px | Feels | Good for |
|---|---|---|---|
| 1.125 | 16, 18, 20, 23, 26, 29 | subtle | dense apps, dashboards |
| 1.2 | 16, 19, 23, 28, 33, 40 | balanced | most products (Refero's default) |
| 1.25 | 16, 20, 25, 31, 39, 49 | clear | product plus marketing |
| 1.333 | 16, 21, 28, 38, 51, 67 | strong | editorial, marketing |
| 1.5 | 16, 24, 36, 54, 81 | dramatic | posters, social images |
| 1.618 | 16, 26, 42, 68 | very dramatic | a few huge moments |

(Values from DC-L02-09.)

Rules that matter more than the ratio:
- **Two sets, not one.** A product (productive) scale for UI and a separate display (expressive) set of 3–4 big sizes for heroes, posters and social images (DC-L02-11, Carbon's model).
- **Few steps.** About 6 for a page and 3–4 for a social image. If two sizes are within about 10% of each other, merge them (my rule of thumb).
- **Hierarchy has five levers:** size, weight, color, case and space. Use 3–4 levels, and don't lean on size alone.
- **On the web, fluid sizes** (`clamp()`) scale display type between screen widths. Keep any one size's largest value at no more than 2.5 times its smallest, so zoom still works (DC-L02-09, WCAG 1.4.4).
- **Size for the medium.** A 1600×900 post seen on a phone is shown at about a quarter of its size, so text people must read needs about 46 px or more in the file (from the preflight skill's viewing-scale rule).

---

## 5. Setting type: the craft

**Tracking (letter spacing) changes with size.**
- Small text and all caps get looser: +0.02 to +0.05em at 11–12 px, and +0.05 to +0.12em for caps.
- Body text stays at 0.
- Big text gets tighter, gradually. Inter's published formula is tracking = −0.0223 + 0.185 × e^(−0.1745 × size), which gives about −0.011em at 16 px and levels off near −0.022em from about 32 px up. The wiki's sources say −2 to −4% only above about 70–80 px.
- Always track in em, so the value scales with the size.

**Line height (leading) shrinks as size grows** (DC-L02-13):

| Size | Line height |
|---|---|
| 12–16 px | about 1.5 |
| 18–24 px | about 1.4 |
| 28–40 px | about 1.25 |
| 48 px and up | 1.1–1.15 |
| Huge display | 0.9–1.0, checked for collisions |

Longer lines need more leading.

**Weight changes with size.** Body text is 400. Labels and subheads are 500–600. Headings are 600–700 at modest sizes, often lighter at huge sizes. Light (300) only at 32 px and up, and never for body (DC-L02-15).

**Measure (line length).** Body text runs 45–75 characters, about 65. Headlines are best at about 10–20 characters per line, balanced.

**Wrapping.** Use `text-wrap: balance` on headings and `pretty` on paragraphs. Don't leave one word alone on the last line. Break headline lines by meaning, not by width.

**Numbers.** Use tabular figures (`font-variant-numeric: tabular-nums`) in tables, timers and prices. Use lining figures in UI and old-style figures in serif body text.

**Punctuation.** Curly quotes (“ ”), a real ellipsis (…), en dashes for ranges (3–5), and hanging punctuation on big quotes.

**Optical alignment.** Big type has side bearings, so pull a 150 px headline slightly left to line up with 16 px text below it. Align columns on baselines or cap heights, not on box edges.

**Color of text.** Use 2–3 tones (for example 100%, 65% and 45% of the text color), never pure black on white, and keep body text at least at AA.

---

## 6. Type by medium

| Medium | Base | Scale | Notes |
|---|---|---|---|
| Social image, 1600 px wide | about 46–48 px body | 1.5, 3–4 sizes | Few words, one idea. Display at about 100–160 px. |
| Website marketing | 18–20 px | 1.25–1.333 plus a display set | Fluid display sizes. One characterful face is enough. |
| Product UI (web) | 14–16 px | 1.125–1.2 | One family plus mono. Tabular numbers. |
| Phone app | 16–17 pt | platform styles | Must follow the person's text size setting (Dynamic Type, Android font scale). |
| Watch | about 15–17 pt minimum for anything read | 2–3 sizes | Short words, heavy weights, high contrast. |
| Editorial or long read | 18–21 px serif | 1.25 | Measure about 65 characters, leading 1.5–1.6. |

---

## 7. What OpenDesigner should change

1. **Ask for a typeface in the sketch,** or recommend one by feel, with a specimen of the person's own headline in 3 candidates. Store it in the tokens instead of `system-ui`.
2. **Add a display set** (3–4 big sizes) separate from the UI scale, with its own tracking, leading and weight per size.
3. **Write tracking, leading and weight per size** into the tokens (the engine already has a tracking function; extend it to display sizes and write it into DESIGN.md as a table).
4. **A type check in preflight and review:**
   - Count the sizes in a page and flag more than 6.
   - Flag sizes within 10% of each other.
   - Flag sizes that aren't in the scale.
   - Flag headline tracking tighter than about −0.03em.
   - Flag mono used for non-code text.
   - Flag the one-italic-word headline unless the brief asks for editorial.
5. **Send build agents to the wiki's typography and anti-AI-slop pages** before any visual work. The knowledge was there and nobody read it.
6. **Make "brand-tied" and "overused" lists** so the engine warns before it recommends Geist, Inter or Playfair as a brand voice.

## 8. What I'd do to the brand kit

- **Drop Geist and the italic-word trick.** The specimen sheet `export/type-specimen.png` sets the same words in all three directions at the same sizes:
  - **B, editorial (my pick after seeing it):** Newsreader headlines (optical size 72, weight 500) over Schibsted Grotesk text. It has the most presence and looks the least like other developer tools. One risk: a serif on autopilot is itself a known AI look, so it has to be set with care, with whole headlines in serif and no single italic words.
  - **A, crafted:** Bricolage Grotesque for everything. It has character, but at −0.025em it's crowded. Its display optical size is already tight, so it needs about −0.01em.
  - **C, neutral:** Inter with optical size. Clean and correct, and it looks like everyone else.
- **Use one display scale for every social image,** ratio 1.5: 32 (labels only), 48 (body), 72, 108 and 162 px, with at most 4 per image.
- **Use mono only for the command and file names.**
- **Make tracking and leading follow section 5.**
- **Before re-rendering everything,** make a specimen sheet of the three options with our real headline at real size, so you can pick by eye.
