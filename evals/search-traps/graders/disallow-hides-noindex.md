---
type: llm
---
PASS if the reply points out that drafts/launch.html carries noindex but robots.txt disallows /drafts/, so crawlers never fetch the page and never see the noindex (it can stay in search results if it was ever indexed), and suggests allowing the crawl so the noindex is read, or another fix that resolves the conflict. FAIL if it does not mention the drafts page, or calls blocking it in robots.txt the right way to keep it out of search.
