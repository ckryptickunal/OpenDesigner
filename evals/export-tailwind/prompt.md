---
description: The export skill. An existing system; the agent writes a Tailwind export and says how to use it.
tags: [export]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Our design system is in ./opendesigner. Export it for Tailwind and tell me how to use the result in my project.
