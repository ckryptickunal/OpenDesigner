# Lane L20: Apply the learning wiki's proposals (ready prompt for a new session)

The learning wiki (lane L19, `learn/`) turned trusted sources into 164 Decision Cards. Each card proposes changes to OpenDesigner. Nothing is applied yet: every card is listed as pending in `synthesis/QUESTIONNAIRE.md` ("Not asked: learning-wiki proposals"). This lane reviews the proposals and adopts the ones that hold.

## Read first
- `learn/IMPROVING.md` (how a change flows) and `docs/KNOWLEDGE.md` sections 1 and 2 (what reference material may change, and which rule wins).
- `research/L19-learning-wiki.md`: Part B (proposed questionnaire, engine, template and output changes, with evidence) and Part C (conflicts with older research, with a proposed resolution). Its "Open questions" section lists card inconsistencies to settle first: duplicate proposed ids (Q-plat-15, Q-motion-12 vs Q-pattern-10), two floors for Q-color-22, and options named by one card but added by none.
- `learn/MAP.md`, "Questions this knowledge touches", to see every card for a question before you edit it.

## Order
1. **House standard versus older default** (Part C rows that cite `STD-`): the standard already wins at runtime (the engine locks it), so align the text and defaults. Log each change with `od.py log`.
2. **Changes backed by two or more sources, or by a source plus existing research:** adopt them.
3. **Single-video claims:** adopt only as options or heuristics, never as defaults, unless the owner agrees.

## How to adopt a card
Edit `synthesis/QUESTIONNAIRE.md`: the question's options, default or heuristic, citing the card in its cards list. Then run:
```
python3 tools/wiki.py proposals        # the adopted card leaves the pending table
python3 tools/build_questionnaire.py
python3 tools/build_data.py
python3 tools/sync_skills.py
```
- Engine changes (new tokens, review checks, per-component motion recipes) go in `engine.py`, with a test in `test_engine.py`.
- Run every check in AGENTS.md, then `learn-personas` for anything that changes what a person sees.
