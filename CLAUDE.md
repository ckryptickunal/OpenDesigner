@AGENTS.md

## Claude-specific
- **Skills:** Claude Code reads `.claude/skills/` (a generated copy). Edit `skills/`, then run `python3 tools/sync_skills.py`. Users install the plugin with `/plugin marketplace add ckryptickunal/OpenDesigner` and `/plugin install opendesigner@opendesigner`. Check the manifests with `claude plugin validate .`.
- **Visual interview in Claude:**
  - In Claude chat (web and desktop), use custom visuals or artifacts: paste a template from `skills/opendesigner/assets/templates/` with its `od-data` JSON filled in.
  - In Claude Code, publish an artifact, or write a local page with `scripts/show.py ... --open`.
  - AskUserQuestion takes up to 4 options per question.
  - The person's picks come back as `OD:` lines.
- **Sessions:** Claude sessions on the same Mac can message each other instantly with `SendMessage` (find names with `ListAgents`). The orchestrator session is "OpenDesigner orchestrator". Durable messages still go through `python3 tools/od.py send`, so sessions on other machines and other models see them.
- **Visual round trip:**
  - Figma: read through the local desktop MCP. Write through the remote `plugin:design:figma` server after sign-in.
  - Paper: read and write through its local MCP at http://127.0.0.1:29979/mcp while Paper Desktop is open.
