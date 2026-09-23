# Writing rules for the three-voice glossary

OpenDesigner must be easy enough for a school student, useful to a designer, and precise for an engineer (`_coordination/BRIEF.md`, requirements 12-13). Every term gets three short explanations. `tools/check_glossary.py` enforces the limits below.

## Entry format (JSON)
```json
{
  "id": "found.color.ramp",
  "term": "Color ramp",
  "aka": ["tonal palette", "color scale"],
  "plain": "A row of shades of one color, from very light to very dark.",
  "designer": "A tonal scale of one hue with evenly stepped lightness, used to pick tints and shades consistently instead of by eye.",
  "engineer": "An ordered set of primitive color tokens, such as color.blue.100 to color.blue.900, generated in OKLCH; semantic tokens alias into it.",
  "example": "Light blue for backgrounds, dark blue for text on them.",
  "source": ["found.color.ramp", "DC-L01-02"]
}
```
Keep `id` and `term` exactly as given in your input batch. `aka` (or `aliases`: names other systems use, e.g. Snackbar = Toast), `see_also` (related term ids) and `example` are optional but welcome.

## The three voices
| Voice | Reader | Limit | Rules |
|---|---|---|---|
| **plain** | A 12-year-old, or anyone with no design or coding background | 20 words, one sentence | Everyday words. No acronyms (OK, TV, AI and UI are allowed). None of the jargon words the checker lists; explain the idea instead of naming it. An everyday comparison is welcome ("like the ruler marks on a ruler"). Say what it is or what it does for the person, not how it is built. |
| **designer** | A product or visual designer | 30 words | Design vocabulary is fine. Say what it changes in the look, feel or usability, and when to reach for it. |
| **engineer** | A software engineer | 30 words | How it is represented and built: token names and tiers, DTCG 2025.10 types, CSS properties, platform APIs, file names. Be exact. |

## Accuracy
- Take meanings from your batch's `context` and `source`, and from the files they point to (`synthesis/ONTOLOGY.md`, `synthesis/cards.json`, `research/*.md`). `python3 tools/jev_nav.py find "question"` searches all the research.
- Never invent numbers, names or standards. A number in any voice must come from the sources (for example 4.5:1 contrast, 24 CSS px targets, DTCG 2025.10).
- If a building block is about a decision rather than a thing (for example "Starting point and system posture"), explain the decision: what is being chosen and why it matters.
- The three voices must say the same thing at three depths. They must not contradict each other.

## Tone
Short sentences. No filler ("simply", "just", "basically"), no marketing words, no exclamation marks, no em dashes. Complete sentences are fine without a final period only in `aka`.

## Check before you finish
```
python3 tools/check_glossary.py synthesis/glossary/shard-<x>.json
```
It must print `0 errors`. Fix every error, especially plain-voice grade, jargon and acronyms.
