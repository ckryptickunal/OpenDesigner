# Prompts for extra sessions

Paste one of these into a new session. Works in Claude Code, Codex, or any agent that can read and write the repo.

---

## Prompt A: join the project (any agent with repo access)

```
You are joining OpenDesigner, an open-source, AI-first resource for creating design systems. Many sessions (Claude, Codex, others) work on it in parallel and coordinate through files in the repo.

Setup: if you are not already in the repo, clone https://github.com/ckryptickunal/OpenDesigner (on Kunal's Mac the working copy is /Users/Kunal/Desktop/Design-System). Then:
1. Read _coordination/BRIEF.md, _coordination/PROTOCOL.md and _coordination/SCHEMA.md, in that order.
2. Choose a session name, export OD_SESSION="<name>", run `python3 tools/od.py status`, and read your inbox with `python3 tools/od.py inbox "$OD_SESSION"`.
3. Claim the lane I name below with `python3 tools/od.py claim <LANE>` (or the first `open` lane if I name none). Tell the orchestrator: `python3 tools/od.py send "OpenDesigner orchestrator" "claimed <LANE>"` (Claude sessions on the same Mac can also use SendMessage to that name).
4. Work per SCHEMA.md: official sources first, log every source in traces/<LANE>-trace.md, write Decision Cards in research/<LANE>-<slug>.md, tag every claim with a source id or [inferred]. Post `od.py heartbeat` updates as you go.
5. Finish with `python3 tools/od.py done <LANE> --summary "..."`, `python3 tools/jev_nav.py check`, and `python3 tools/od.py sync -m "<LANE>: ..."`, then message the orchestrator your top 5 findings.
Never edit another lane's files and never commit secrets. Verify anything from 2025-2026 against live sources.

Lane: <fill in, or leave blank>
```

---

## Prompt B: agents without repo access (for example chat-only ChatGPT)

```
You are helping research OpenDesigner, an open-source, AI-first resource for creating design systems. I will paste a lane prompt below. Follow it, but instead of writing files, reply with: (1) the full lane document in Markdown, using Decision Cards in this format: "### DC-<LANE>-<nn>: <title>" followed by bullet fields Block path, Questions the designer answers, Options, Visual effect, Depends on, Affects, Token encoding, Platform notes, Accessibility constraints, Default + heuristic, Evidence; and (2) a source table with URL, publisher, date, and what you took from it. Cite a source for every claim or mark it [inferred]. I will paste your answer into the repo.

<paste a lane prompt from _coordination/lanes/ here>
```

---

## Prompt C: the Figma MCP hands-on lane (L12)

Before using this prompt, open the kits you want inspected in the Figma desktop app (its local MCP reads the open file): Figma's "Simple Design System", Google's "Material 3 Design Kit", Apple's iOS/iPadOS UI kit, and optionally Microsoft's "Fluent 2 Web".

```
You are taking lane L12 (Figma MCP hands-on) in OpenDesigner. Follow Prompt A's setup and claim L12.

Goal: inspect real design-system files through the Figma MCP tools (get_metadata, get_variable_defs, get_design_context, get_screenshot) and record how professional systems are structured inside Figma. For each open file, document: variable collections, modes, variable types and counts, naming conventions, aliasing chains (primitive to semantic to component), scoping and code syntax; styles still used alongside variables; how Button, Text field, Checkbox, Dialog and Navigation use variants and component properties (boolean, instance swap, text, variant) and model states; page and file organization. Save key screenshots to research/L12-assets/, write research/L12-figma-mcp-handson.md (Decision Cards where they fit), log every file and node inspected in traces/L12-trace.md, then finish per Prompt A.
```
