# Lane L19: Learning wiki (ready prompt for a new session)

You maintain OpenDesigner's learning wiki: knowledge from sources the owner trusts, turned into house standards, Decision Cards and process. Read `learn/README.md` first. It explains the three authority levels and the pipeline.

## When to run this lane
- The owner shares new links (channels, videos, sites, repos), or says a source is non-negotiable, good to have, or reference material.
- `python3 tools/wiki.py status` shows sources fetched but not analysed or ingested.

## Steps
1. `export OD_SESSION="<name>"`, `python3 tools/od.py claim L19` (or ask the holder), and read your inbox.
2. Add each link: `python3 tools/wiki.py add <url> --authority non-negotiable|good-to-have|reference [--name "..."]`. A channel means every video on it; a video means that video only. Ask the owner when the authority is unclear. Never guess it.
3. Fetch: `.venv-wiki/bin/python tools/wiki.py fetch --only "<name>"` (set-up is in `learn/README.md`). Paid, logged-in or paywalled content is out of scope: use only public pages.
4. Analyse: run the saved workflow `.claude/workflows/learn-analyze.js` with the output of `python3 tools/wiki.py pending --work-items`. Hosts without workflows: follow the two prompts in that file by hand, one source at a time, with a separate verifier pass.
5. `python3 tools/wiki.py check`, then `.venv-wiki/bin/python tools/wiki.py ingest`, then `python3 tools/wiki.py trace`.
6. Synthesise what changed:
   - **Non-negotiable sources** go into `synthesis/standards.json`: draft by theme, verify against the raw text, merge, and run a completeness critic. Every standard cites its sources.
   - **Reference sources** go into Decision Cards in `research/L19-learning-wiki.md`, the topic pages in `learn/wiki/synthesis/`, and `synthesis/impact.json`. Each card says which question it improves ("Maps to"). The cards use the next free ids in their area's block.
   - A conflict with an existing card or default is written down in Part C of the L19 file. Never override it silently. A house standard wins over reference material. Only the owner can overrule a house standard.
7. Rebuild and check: `python3 tools/build_data.py`, `python3 tools/sync_skills.py`, then every check in AGENTS.md ("Before you commit"). Then run `python3 tools/wiki.py check`.
8. Log decisions (`od.py log`), post a heartbeat, and sync (`od.py sync -m "L19: ..."`).

## Rules specific to this lane
- Third-party text never enters git. `learn/raw/` is git-ignored. Analysis and wiki pages hold summaries, rules and at most 3 quotes of 15 words or fewer per source.
- Everything traces to a source: an `S-L19-nnn` id in the Decision Cards, an analysis id in the standards. Mark your own connections `[inferred]`.
- A single video's number or "always/never" claim is opinion until another source or existing research agrees.
