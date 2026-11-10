# The engine's commands

Every command of `scripts/engine.py` and `scripts/journey.py`, with its flags. `<skill>` means the opendesigner skill's folder. SKILL.md ("The engine", "The journey log") says when to run them.

```
python3 <skill>/scripts/engine.py init [--name "Acme"]
python3 <skill>/scripts/engine.py sketch --name "Acme" --audience regular --platforms web --feel friendly,minimal [--brand "#167874"] [--logo logo.svg] [--surfaces app:operate] [--delegated feel,brand]
python3 <skill>/scripts/engine.py feel [words...]            the feel words it knows, or how it reads theirs ("fun" is playful)
python3 <skill>/scripts/engine.py style search|show|tiles|mix|mutate|explore|define ...   the style lab: find, show, blend, change or invent a look (style-lab.md)
python3 <skill>/scripts/engine.py set <path> <json-value> --set-by <how> --why "..." [--lock]   fonts, brand color, dials and Q-* answers must say how:
                                                             chosen --quote "<their words>", confirmed_default, delegated, assumed or reference
python3 <skill>/scripts/engine.py set <path> <json-value> --dry-run   preview a value (each token's old and new value, any check it breaks); writes nothing
python3 <skill>/scripts/engine.py resolve                    current dials and derived values, for payloads
python3 <skill>/scripts/engine.py generate                   opendesigner/tokens/ (DTCG 2025.10)
python3 <skill>/scripts/engine.py validate [--json]          contrast, targets, lint; exit 1 on errors
python3 <skill>/scripts/engine.py contrast "#767676" "#fff" [--min 4.5]   the WCAG ratio of any two colors, rounded down; exit 1 under --min
python3 <skill>/scripts/engine.py design-md                  DESIGN.md and PRODUCT.md at the project root
python3 <skill>/scripts/engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg|artifact|brand|all
python3 <skill>/scripts/engine.py overview [--open]          opendesigner/overview.html: the whole system, what is chosen and what is still missing
python3 <skill>/scripts/engine.py preview [--open]           opendesigner/preview.html: every token
python3 <skill>/scripts/engine.py show <template> [--open]   one visual template filled with real values (opendesigner/preview/)
python3 <skill>/scripts/engine.py build [--force]            generate and validate; exports, DESIGN.md, overview, filled templates and preview only if there are no errors
python3 <skill>/scripts/engine.py review [--project src/] [--strict]   end-of-implementation check: hard-coded values, broken standards, removed things that came back, od-ignore without a reason, guard problems (tokens edited by hand, a locked decision undone), validate errors, stale DESIGN.md; runs without a system too. Last line "Review: ok" or what is left to fix; --strict exits 1 unless it is ok, and always when AGENTS.md, CLAUDE.md or DESIGN.md point at a missing opendesigner/
python3 <skill>/scripts/engine.py removed add "<what>" --why "<their words>" [--instead "..."] [--pattern RE]   something the owner removed on purpose; removed list; removed restore <R-id> --why "<their words>"
python3 <skill>/scripts/engine.py guard install|no|remove|status   after asking once: a pre-commit hook that runs review --strict (git commit --no-verify skips it once); no records the answer. Never writes over another hook or into a shared core.hooksPath
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
python3 <skill>/scripts/engine.py status --hook             the same in five lines, and nothing without a system: the Claude Code plugin's start-of-session hook runs it
python3 <skill>/scripts/engine.py handoff [yes|no] [--why "..."]   after asking once: yes writes the OpenDesigner note into AGENTS.md and a CLAUDE.md that imports it, no writes nothing; recorded either way
```

## The hand-off note
`engine.py handoff yes` writes `assets/output/AGENTS-snippet.md` into AGENTS.md between `<!-- opendesigner:start -->` and `<!-- opendesigner:end -->`, matched to the system. The owner's strictness answer (Q-gov-01) decides when there is one: "loose" gets the first-version note, "strict" or "canon-expanded" the full note. With no answer, a system still a sketch (zoom 0) in every area gets the first-version note: the first paragraph becomes "This project has a first version of its design system in `opendesigner/`, and `DESIGN.md` describes it. Follow it, and suggest changes to the owner instead of making them quietly. `engine.py` below means `python3 <opendesigner skill>/scripts/engine.py`, from the OpenDesigner skill or plugin.", and every line marked `<!-- strict -->` is left out. Otherwise it writes the full note. Neither keeps the `<!-- strict -->` markers. Each later `set` or `pick` refreshes the note in place, so it becomes the full note once an area is zoomed in or the owner tightens Q-gov-01, and the lighter one again if they loosen it. It rewrites only a note the engine wrote and nobody changed: when the block between the markers matches neither variant (a line added by hand, or a note from an older engine), it is left as it is and the engine says so; `engine.py handoff yes` rewrites it.

Without the engine (a ChatGPT project), do the same by hand: copy the asset into AGENTS.md, apply the rule above, and delete the `<!-- strict -->` markers.

## Removed on purpose
Removals leave no trace in code, so a later session tends to add them back first. The day the person removes something (a control, a label, divider lines, a flow), record it: `engine.py removed add "<what>" --why "<their words>" --instead "<what replaces it>"`. Add `--pattern` when a line of code that brings it back can be found by a regular expression; `review` then flags the return, and DESIGN.md lists it under "Removed on Purpose". Only the owner brings it back: `removed restore <R-id> --why "<their words>"`. An `od-ignore` comment keeps a returned line only when it gives a reason.

A removal never takes away an accessibility floor (focus rings, labels, alt text, reduced motion, contrast, target sizes). `removed add` runs the pattern against sample lines that carry each floor and refuses one that matches; `--force` is only for a false alarm the person confirmed, and is marked in decisions.md. Review never reports a line that carries a floor as removed.

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
