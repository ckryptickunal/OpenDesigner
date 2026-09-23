# U5 usability test: three personas

Run 2026-09-24 against commit after T1 phase B. Each tester played both the person and the model, following the skills word for word and running the real engine and journey tracker in a scratch folder.

| Persona | Report | Friction points (sev 3 / 2 / 1) |
|---|---|---|
| Riya, 14, school robotics club site, plain words only | [U5-usability-student.md](U5-usability-student.md) | 34 (4 / 18 / 12) |
| Meera, senior product designer, finance app, brand font, Stripe as reference | [U5-usability-designer.md](U5-usability-designer.md) | 34 (5 / 17 / 12) |
| Arjun, backend engineer, internal admin tool, React + Tailwind, "just pick" | [U5-usability-engineer.md](U5-usability-engineer.md) | 24 (3 / 11 / 10) |

## Shared findings, in priority order
1. **Most answers never reach the tokens.** Color, direction and many defined-level answers change nothing, with no warning (all three testers).
2. **Brand color is altered even when it already passes contrast**, and feel words can push the palette to gray or monochrome, hiding the brand (student, designer, engineer).
3. **The first result doesn't look like the person's project**: sample content in the preview, a DESIGN.md whose first screen is settings, and fields shown as "not recorded" after they were answered (student, designer).
4. **Platform gaps**: no per-platform font licence, iOS gets web sizes, Tailwind export doesn't import its own variables, review misses JSX and Tailwind drift, extend can't add tokens (designer, engineer).
5. **Reference measurement errors** in the extract scripts (designer).
6. **Consent and pacing**: sharing ask too long, re-asking what was already said, free words rejected (student, engineer).

## What worked
The designer voice with real, cited systems; reference intake never copied identity; the illustration hook; both consent flows and "don't share" respected; DESIGN.md refreshed after every decision; first export in 7 messages for the engineer.

## Fixes
Applied by three agents on separate files (engine, extract scripts, skills text); see `_coordination/BOARD.md` lane U5 and `_coordination/DECISIONS.md`.
