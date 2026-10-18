# 13 Ferrule: security and audit hero (B2B)

Built in round 3, after the owner's review (`brand/showcase/ROUND3-BRIEF.md`). It is one of three heroes made for the B2B product screens the owner loves. Render: `shot.png`, 1440 × 900 at 2×.

## Direction
Ferrule is the fictional data platform in `product/06-ferrule-security`. This hero is for its security page, aimed at IT and security admins at mid-size companies. The question they bring to an audit log is always the same four words, so the headline is those four words.

The page is Ferrule's plum: a flat, deep step (accent 11, #63295f) of the product's own accent ramp, with white type. The headline is "When. Who. What. Where.", and each word sits exactly over the column of the audit log below that answers it:

| Word | Column below |
|---|---|
| When. | Time |
| Who. | Actor |
| What. | Action |
| Where. | IP address |

A hairline under the words matches the log's own header rule, from 317 to 1355 px. Read together, the headline is the table's header, and the open audit row answers it:
- 13:58:07
- Amara Sjöberg
- session length 24 h → 12 h
- 198.51.100.24, Stockholm

Feel words (the product's): **secure, quiet, precise**.

What makes it Ferrule's own: the headline set as the header of its own log, and the plum page.

## References (Mobbin, cited by URL only; nothing saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/432bd327-9a31-4c91-9790-fa7177212f8b (Current) | A security hero on a dark brand field, with one action. |
| https://mobbin.com/sites/sections/4cba4337-40f7-4bc9-b877-ed1339104bd0 (Retool) | The product can take most of the hero. I avoided its bleed off the edge and its bold headline. |
| https://mobbin.com/sites/sections/ffe8e8fc-2ad0-439a-b5a4-cd3fa615cf1b (1Password) | A product screenshot on a single brand-colour field. Our field is the whole page and is flat. |
| `brand/showcase/b2b-study/site.md`, "Enterprise, security and governance" | Show the control as real UI, and name what is logged concretely. |

## System (engine)
The hero inherits the product's design system:
- I copied `state.json`, `decisions.md`, `standards-state.json` and `standards.md` from `product/06-ferrule-security/opendesigner/`.
- I ran `pick Q-brand-06 two-sets` (display sizes 42, 50 and 72), then `build`.

Faces (Red Hat Text; the screen adds Red Hat Mono), greys, the plum ramp, dials and overrides are all the product's. The page uses `data-theme="light"` tokens on a plum `--page`, with `data-density="comfortable"` on `<body>`.

## Type (hero)
| Size | Role | Where |
|---|---|---|
| 50 | display-md, 400 | The four words |
| 17 | body-lg / title-md | The sentence, the button (500), the wordmark (600) |
| 14 | label-lg | Nav, Sign in |

The column conceit caps the words at 50 px. At 72 px, "When." is about 190 px wide, more than the 157 px Time column.

The embedded screen renders at 0.9333, so its 12 and 14 px read as 11.2 and 13.1 px.

## Colour and contrast (measured on the render)
| Element | Contrast |
|---|---|
| White on plum | 10.4:1 |
| Sentence (accent-dark-12 on plum) | 7.2:1 |
| Button text (ink on white) | about 16:1 |

The hairline (accent-light-8) is decorative structure at about 2:1. The plum is flat: no glow and no gradient.

## The picture
The picture is `<iframe src="../../product/06-ferrule-security/index.html?frame=audit">`, 1440 px wide, scaled to 1344 px. At 1344 px wide its export row wraps, so I kept the 1440 layout and scaled it.

The window starts at 384 px. The 900 px fold therefore lands on the claims-archive row's bottom border (553 product px). The frame runs past the first screen and ends on a row boundary at 721 product px, so the page reads whole when scrolled.

The word positions are measured, not guessed. Each one is the product's column x plus its 12 px cell padding, times 0.9333, plus 48:

| Word | x (px) |
|---|---|
| When. | 328 |
| Who. | 485 |
| What. | 689 |
| Where. | 1167 |

A fresh audit measured each word within 2 px of its column.

## Outside the tokens, on purpose
- The nav's wordmark is 240 px wide, so with the 40 px gap the nav links start at 328 px, the same edge as the headline, sentence and button.
- The words, the rule, the sentence and the button are absolutely positioned to the product's measured columns. They are marked `od-ignore`, with the arithmetic in comments.
- Nav height is 64 px; there is no nav-height token.

## Checks
- `engine.py validate`: passes, 0 warnings, 6 notes.
- `engine.py review --project heroes/13-ferrule-security`: clean.
- `preflight.py html --medium web`: 0 errors, 0 warnings.
- `check_dates.py --year 2026`: passes. 13:58:07 UTC is 15:58:07 CEST; CEST runs until Oct 25.
- Facts: the sentence reads "Ferrule logs every change to your workspace, to the second, with who made it and from which IP." Every row on screen has an actor, an IP with its city, and a time to the second. Earlier drafts that promised before-and-after values or a sign-in method for "every event" were cut: API-key and deactivation events have neither.
  - The button says "Start a workspace". An earlier "30-day trial" and then "trial" were cut: no product document backs a trial.
- `.example` rule: the hero copy names no domain or email address. An earlier hidden caption named `larchfieldmutual.com`; that has been removed.
  - The embedded product screen still shows `larchfieldmutual.com` addresses (product/06), as noted in NAMES.md. They should become `larchfieldmutual.example` in the product page.

## Round 3 (owner review)
**What he said.** "I love the B2B product screens. They look absolutely crazy." He removed four heroes he called very ugly. He asked for one hero per B2B product, using the real screen as the picture, in the product's own system, each with its own direction, one action and real proof only.

**What I built and changed.** About sixteen rounds, each scored by a fresh-context agent:
- **Early versions (centred copy over the screen) scored 3.** I tried, in turn:
  - a white page with a four-up feature strip;
  - a mono spec row;
  - a plum panel behind the screen;
  - a pink field.

  The audits found:
  - the default SaaS template, close to 1Password;
  - copy that repeated the screen;
  - overclaims: "two-factor required for every member", an invented 30-day trial, "data" for "data access".
- **The plum page scored 3.** It was ownable, but the layout was still the template.
- **Final, scored 4.** The four-word headline set over the log's own columns, on a hairline matching its header rule. The audit's two remaining notes are fixed:
  - the sentence no longer repeats the product's subtitle;
  - the rule stops where the log's rule stops.

**Fresh score: 4.** The confirmation audit is in `brand/showcase/audit/heroes--13-ferrule-security.json`.

**What remains:**
- The word spacing follows the product's column widths, so "When. Who." sits close together and "Where." sits far right. That is the cost of the idea; check that the owner reads it as intended.
- A full plum page is a taste risk next to his "no violet" rule. It is aubergine and flat, but still a risk.

## Process findings
1. **There is no "start from an existing system" path** (gap), and **density modes don't apply on `<html>`** (bug). See heroes/12.
2. **Aligning marketing type to an embedded product needs the product's geometry** (idea). I measured the column positions with Playwright and converted them by hand: (x + padding) × scale + margin. A small "measure this element in the embed" helper in `brand/tools` would make this repeatable.
3. **Product-side issues** (outside this folder):
   - `product/06` has no `data-theme`;
   - its emails use `larchfieldmutual.com` (should be `.example`);
   - "Updated 14:02 UTC" also appears in product/04.

Findings 1 and 2 are recorded with `engine.py feedback`; nothing was posted.
