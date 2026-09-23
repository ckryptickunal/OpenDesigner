@AGENTS.md

## Claude-specific
- Claude sessions on the same Mac can message each other instantly with `SendMessage` (find names with `ListAgents`). The orchestrator session is "Design system research and builder". Durable messages still go through `python3 tools/od.py send`, so sessions on other machines and other models see them.
- Figma (read through the local desktop MCP; write through the remote `plugin:design:figma` server after sign-in) and Paper (read and write through its local MCP at http://127.0.0.1:29979/mcp while Paper Desktop is open) are the visual round-trip surfaces.
