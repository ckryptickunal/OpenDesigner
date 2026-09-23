# U4 rules: the plain-language and clutter pass

Goal (BRIEF requirements 12-15): OpenDesigner reads easily for a school student, is complete enough for a designer, and is precise enough for an engineer. Nothing feels cluttered.

## How to write
- **Lead with the point.** First sentence says what this is or what to do.
- **One idea per sentence.** Aim for 15 words; split anything over 25.
- **Short paragraphs** (3 sentences at most). Prefer a short list to a long paragraph, and a paragraph to a table when a table would have one column of prose.
- **Plain words first.** Use the glossary's `term` names (`synthesis/glossary.json`). The first time a technical term appears in a page, follow the rule in `synthesis/THREE-VOICES.md`: plain meaning in a few words; the "Designers: X · Code: Y" line only where a reader may need both.
- **Cut** filler ("simply", "just", "basically", "in order to"), hedges, repetition, marketing words, exclamation marks and em dashes.
- **Keep every fact, number, command, link, file path, source id and requirement.** Clarity must never change meaning. If a sentence is wrong, fix it only with evidence from the code or research, and note it in your report.
- **Keep structure the tools depend on.** Headings, ids, table columns, front matter, `OD:` syntax and anything a build script parses must stay parseable. Run the checks below.

## Measure
Before and after, for each file you touch: `python3 tools/readability.py <files>`. The baseline for all files is `research/U4-baseline.json`. Target: every file's grade drops, long sentences (over 25 words) drop by at least half, and prose meant for people reaches grade 8 or lower. Model-facing instructions can stay more technical, but the messages they tell the model to say to people must be plain.

## Checks that must pass after your edits
```
python3 tools/build_questionnaire.py        # if you touched synthesis/QUESTIONNAIRE.md
python3 tools/build_data.py                 # regenerates skills/*/references, data/, chatgpt-project/
python3 tools/sync_skills.py                # regenerates .claude/skills and .agents/skills
python3 -m unittest discover -s skills/opendesigner/scripts -p "test_*.py"
python3 tools/check_glossary.py --build
python3 tools/jev_nav.py check
```
Never edit generated files directly (`.claude/skills/`, `.agents/skills/`, `data/`, `skills/*/references/*.json`, `skills/opendesigner/references/stages/`, `chatgpt-project/knowledge/`, `docs/GLOSSARY.md`). Edit their sources.

## Report
Append your before/after numbers and a short list of meaning-level fixes to `research/U4-plain-language.md` under your own heading.
