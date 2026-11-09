# The engine's commands

Every command of `scripts/engine.py` and `scripts/journey.py`, with its flags. `<skill>` means the opendesigner skill's folder. SKILL.md ("The engine", "The journey log") says when to run them.

```
python3 <skill>/scripts/engine.py init [--name "Acme"]
python3 <skill>/scripts/engine.py sketch --name "Acme" --audience regular --platforms web --feel friendly,minimal [--brand "#167874"] [--logo logo.svg] [--surfaces app:operate] [--delegated feel,brand]
python3 <skill>/scripts/engine.py feel [words...]            the feel words it knows, or how it reads theirs ("fun" is playful)
python3 <skill>/scripts/engine.py style search|show|tiles|mix|mutate|explore|define ...   the style lab: find, show, blend, change or invent a look (style-lab.md)
python3 <skill>/scripts/engine.py set <path> <json-value> --why "..." [--set-by delegated] [--lock]
python3 <skill>/scripts/engine.py set <path> <json-value> --dry-run   preview a value (each token's old and new value, any check it breaks); writes nothing
python3 <skill>/scripts/engine.py resolve                    current dials and derived values, for payloads
python3 <skill>/scripts/engine.py generate                   opendesigner/tokens/ (DTCG 2025.10)
python3 <skill>/scripts/engine.py validate [--json]          contrast, targets, lint; exit 1 on errors
python3 <skill>/scripts/engine.py design-md                  DESIGN.md and PRODUCT.md at the project root
python3 <skill>/scripts/engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg|artifact|brand|all
python3 <skill>/scripts/engine.py overview [--open]          opendesigner/overview.html: the whole system, what is chosen and what is still missing
python3 <skill>/scripts/engine.py preview [--open]           opendesigner/preview.html: every token
python3 <skill>/scripts/engine.py show <template> [--open]   one visual template filled with real values (opendesigner/preview/)
python3 <skill>/scripts/engine.py build [--force]            generate and validate; exports, DESIGN.md, overview, filled templates and preview only if there are no errors
python3 <skill>/scripts/engine.py review [--project src/]    end-of-implementation check: hard-coded colors, sizes, radii, shadows, durations; stale DESIGN.md sections; code that uses no tokens; a system older than the code
python3 <skill>/scripts/engine.py feedback "..." --kind gap|bug|confusing|idea [--from-journey]
python3 <skill>/scripts/engine.py feedback "<the rule>" --kind note [--same N-01]   the owner's note on the work, counted in opendesigner/RULES.md
python3 <skill>/scripts/engine.py research plan --brief "<users line>" --tools web-search,browser,last30days   user research: what to find, searches, missing tools
python3 <skill>/scripts/engine.py research check|add <findings.json> [--accept [--only Q-aud-01,...]]   check, save (research/users.md, PRODUCT.md Users), apply on a yes
python3 <skill>/scripts/engine.py research status | skip --why "..."
python3 <skill>/scripts/engine.py research market [--json]                     the competitor table and benchmark: show it before any colour
python3 <skill>/scripts/engine.py research positioning draft | confirm --proof "..." [--for --problem --claim] | show
python3 <skill>/scripts/engine.py research directions check | board [--open] | pick <id> [--remix <axis>=<id>] --why "..."
python3 <skill>/scripts/engine.py standards [--update]       house and project standards; --update applies newer house standards (overrides stay)
python3 <skill>/scripts/engine.py standard override <id> --why "<their words>" [--path P [--value <json>]]...   only when the person explicitly asks; --path releases only that value, without it every value the standard sets
python3 <skill>/scripts/engine.py standard restore <id> [--why "..."]      undo an override
python3 <skill>/scripts/engine.py standard add --rule "..." --why "..." --source <url or "person, <date>"> [--path P --value <json>]... [--values '{...}'] [--review-pattern RE --review-message "..."] [--authority good-to-have] [--beats STD-a,STD-b]
python3 <skill>/scripts/engine.py standard remove PRJ-<nn> --why "..."   project standards only
python3 <skill>/scripts/engine.py version                    this copy's release, and whether the system here is older, newer or up to date
python3 <skill>/scripts/engine.py status [--json]           the Now line: the step, what waits for the owner and the next command; first after a context reset or in a new session
python3 <skill>/scripts/engine.py handoff [yes|no] [--why "..."]   after asking once: yes writes the OpenDesigner note into AGENTS.md and a CLAUDE.md that imports it, no writes nothing; recorded either way
```

## DESIGN.md, as `design-md` writes it
Each section shows its zoom level (sketch, broad, defined, detailed). Each decision opens with one plain sentence. Text inside `<!-- od:keep -->` blocks survives each refresh.

## Versions
**Versions.** Each system records the OpenDesigner release that made it and the one that last built it (`opendesigner` in `state.json`). At the start of work on an existing system, run `engine.py version`. It compares the system with this installed copy only. It never checks online, so it cannot know about newer releases. If the system is older, say so in one line, run `build`, and show what changed. If it is newer, tell the person before you change anything: this copy may miss features, so they should update OpenDesigner first. When they ask how to update: in Claude Code, `claude plugin marketplace update opendesigner`, then `claude plugin update opendesigner@opendesigner`, then restart Claude Code (or use `/plugin`). Elsewhere, get the new copy the way it was installed (pull the repo, or upload the new skill zip).

## The journey log
Only after a yes to the log question (`rules.md` section 11).
```
python3 <skill>/scripts/journey.py consent on|off           their answer to the log question (consent --where local|web prints it)
python3 <skill>/scripts/journey.py log step_shown --step Q-shape-01    also help, frustration, speed_mode, session_end
python3 <skill>/scripts/journey.py report                   opendesigner/journey/JOURNEY.md and a short summary
python3 <skill>/scripts/journey.py share-consent [always|ask|never] [--details]   the short sharing question, its details, or their answer
python3 <skill>/scripts/journey.py share [--dry-run] [--yes]           send the anonymous report, or show it first
```
