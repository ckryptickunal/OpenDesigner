---
description: The review skill. A page with five planted problems; the agent reports them with evidence and does not edit the page (checks report, they never rewrite).
tags: [review, audit]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Please review the page in the extra folder you were given (page/index.html) for design and accessibility problems before we ship it. Tell me what's wrong and why. Don't change the file.
