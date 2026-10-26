---
description: User research without a way to read the web. The agent plans it, names the tools it is missing (a web search, a browser, /last30days), and never presents findings it could not source.
tags: [research, guardrail]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

I'm building Tallyroot, a phone app where small farm co-ops in Kenya record harvest weights and payments. Set up our design system in this folder, then research who our users are (their phones, the apps they already use, what they need) and use that for the defaults. Yes to any searches you need. Don't ask me anything else.
