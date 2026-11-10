## What this changes

<!-- One or two sentences. Link the issue: "Closes #123". -->

## Type of change

- [ ] Research correction or new source
- [ ] New building block or Decision Card
- [ ] Skill or interview change
- [ ] Engine, export or tooling
- [ ] Host support (a new AI tool)
- [ ] Docs or translation
- [ ] Example

## Evidence

<!-- Research: the source ids you added and their trace rows. Skills or engine: test output, a short transcript or a screenshot of the visual. -->

## Checklist

- [ ] Every new claim cites a source id (`[S-Lxx-nnn]`) or is marked `[inferred]`, and new sources are logged in `traces/`.
- [ ] `python3 tools/jev_nav.py check` reports 0 files with dangling references.
- [ ] Every JSON file still parses, and `python3 tools/check_links.py` passes.
- [ ] I edited source files (`research/`, `synthesis/`, `skills/`, `tools/`), not generated copies; if I changed them, I ran `python3 tools/build_data.py` and `python3 tools/sync_skills.py`, and the engine tests.
- [ ] If this changes what the engine writes, I ran `python3 tools/build_examples.py`, and `python3 tools/build_examples.py --check` passes.
- [ ] Nothing copies another brand's identity (logo, name, typeface files, illustrations).
- [ ] `CHANGELOG.md` has one short, dated entry per change, and `python3 tools/changelog_check.py` passes.
- [ ] If this changes the website's header, footer or navigation, no link that search engines or AI answer engines follow was dropped.
- [ ] No secrets, keys or `.env` files are included.
- [ ] If this changes a product decision, I added a line to `_coordination/DECISIONS.md` with `python3 tools/od.py log`.
