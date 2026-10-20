---
description: The core job. From the five sketch answers, the agent builds a whole system (tokens, exports, DESIGN.md) and keeps the brand color exactly as typed.
tags: [smoke, establish]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

I'm building Billerwick, a web app where finance teams approve supplier invoices. Accountants use it all day in desktop browsers. Our brand color is #15803D. The feel I want is precise and calm. Please set up our design system in this folder now. Don't ask me anything else: wherever you would ask, use your recommended default and tell me what you assumed.
