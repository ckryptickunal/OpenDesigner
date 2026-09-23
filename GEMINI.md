@AGENTS.md

## Gemini CLI notes
- Gemini CLI reads skills from `.agents/skills/`, a generated copy of `skills/`. Edit `skills/`, then run `python3 tools/sync_skills.py`.
- Gemini CLI does not render MCP Apps or HTML inline. For visual steps, run `python3 skills/opendesigner/scripts/show.py <template> <payload.json> --open` and ask the person to paste back the `OD:` lines from "Copy my choice".
- Figma's MCP catalog does not list Gemini CLI as a write client. Export `figma/variables.json` with the engine for manual import.
