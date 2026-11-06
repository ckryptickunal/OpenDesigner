---
description: The search skill. A built site with five planted problems for search and answer engines (a blocked OAI-SearchBot, a missing canonical, FAQ markup the page does not show, a title too long for results, a page whose text needs JavaScript). The agent reports them with evidence, treats the GPTBot block as the owner's choice, and changes nothing.
tags: [search, audit]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

We launch Ledgerly next week. The built site is in the extra folder you were given (site/, for https://ledgerly.example). Can you check it for SEO, and whether ChatGPT and Perplexity will be able to find and use it? Don't change any files and don't go online; just tell me what's wrong and why.
