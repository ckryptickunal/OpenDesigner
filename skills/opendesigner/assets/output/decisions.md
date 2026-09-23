# Design decisions: {{name}}

Append-only log written by `engine.py` (every `pick` and `set` with its `--why`) and by the interviewing model (stage summaries). A change adds a new entry that supersedes the old one; nothing is deleted. Statuses: confirmed (the owner chose it), default (nobody chose it), delegated (the owner said "you decide"), assumed (owner input not yet confirmed), locked (changes need explicit consent).

## Stage summaries
<!-- one short paragraph per stage, written for a teammate -->
### {{date}} · Stage 06 · Visual direction
{{We chose ... because ... . Rejected: ... because ... .}}

## Log
<!-- one entry per decision, newest last -->
### D{{n}} · {{title}} · {{date}}
- Question: `{{Q-id}}` · Value: `{{value}}` · Status: {{confirmed|default|delegated|assumed|locked}}
- Why: {{reason in the owner's words or the default's source}}
- Changes: {{downstream decisions or tokens that moved}}
- Source: {{person | default (levers.json) | reference <url> | designer}}
- Supersedes: {{D-id or none}}

## Open items
- Assumed owner inputs to confirm: {{list}}
- Pending assets and their briefs: {{hook ids}}
- Waived warnings and reasons: {{list}}
