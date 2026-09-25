# Global and project-local preferences

Design proposal for review, September 25, 2026. Source: Kunal's September 25 voice note and public `ckryptickunal/OpenDesigner` at `30f0429`. This workstream concerns scope and persistence, not the journey tracker or the visual tree.

## What exists

- `skills/opendesigner/scripts/engine.py:486-516` creates `opendesigner/state.json` per project. It includes `profile.voice`, project `context`, `answers`, `dials`, `references`, `taste`, `hooks`, and `locks`.
- `engine.py:3141-3143, 3807-3874` accepts `profile.voice` via `set`, writes project state and an append-only `decisions.md`. It does not represent a user-wide workflow profile or distinguish a reusable preference from a local design decision.
- `journey.py:232-260` stores tracking and report-sharing choices in the same project's `profile`; those choices are privacy permissions, not evidence of a cross-project preference.
- `skills/opendesigner-extend/SKILL.md` reads the local `DESIGN.md`, state, decisions, and tokens before changing that project. The `chatgpt-project` bundle has no cross-project store. The generated `.agents/skills` and `.claude/skills` folders copy `skills/` and must not be edited by hand.

## Gap and risk

A designer may prefer short questions everywhere, but a project's brand color, audience, license, or pattern choice does not belong to every project. Currently `profile.voice` is local even though the wording can sound personal. Automatically importing choices from another repo would leak context and quietly overwrite the new project's actual requirements. `profile.tracking` and `share_reports` must never be inherited as blanket consent. Host capabilities also differ: a path on one machine does not imply access in a web chat.

## Proposed contract

Keep `opendesigner/state.json` the canonical project record. Define a separate optional *user workflow preference* file outside any individual project, supplied explicitly by the user or their host. First version should contain only portable process choices, such as preferred explanation voice and whether to show an example before asking. No names, source links, product context, design tokens, prior answers, or tracking/sharing permission. The user should see and edit each entry, its scope, when it was set, and the last time it was used. No file is created or read beyond the current project without an explicit opt-in and a host-specific location chosen by the user.

At start: read project files first; ask whether an explicitly supplied workflow preference should apply. Project-specific constraints and locked decisions win. If the reusable preference conflicts with a project constraint, display both and ask; do not silently choose. During work: a repeated request to shorten a prompt becomes a candidate, not a global change. Ask whether to keep it in this project only or save it for future projects. On export: include only project state in project deliverables. Separate consent to keep the local journey log from consent to share it; neither crosses projects.

Suggested schema (proposal, not implemented):

```json
{
  "version": 1,
  "preferences": [
    {"key": "explanation_voice", "value": "plain", "scope": "user-workflow", "approved_at": "<timestamp>", "source": "explicit-user-choice"}
  ]
}
```

`approved_at` records a specific approval rather than pretending habit is permission. The host must own path discovery and access. Invalid schema or missing file should fail safely back to the project's defaults, not wipe local state. Do not blend this file into `state.json` during generation; resolve precedence in memory and show the source of each applied preference.

## Implementation slices and acceptance

1. Document the two scopes and a small allowlist of portable keys. Review the key list with Kunal before code that persists user-wide preferences. Kunal clarified that user-wide taste should follow across projects and product improvements should reach the repo as a separate reviewed contribution. Ask only which storage and sync mechanism he wants across hosts or devices; these imply different privacy designs.
2. Add a pure resolver with tests: project override wins; locked local decision cannot be overridden; absent/malformed external profile is non-destructive; tracking/sharing never inherit; no project facts are copied. Avoid a new dependency or server.
3. Add an opt-in import/export path and plain confirmation text for compatible local hosts; keep web-only hosts local until there is a safe supported persistence route. Test two unrelated projects plus a second session and verify no cross-project tokens, names or references appear.

## Decision needed

Resolved: Kunal means both user-wide preferences across projects and a separate path for improvements to the OpenDesigner repo. The unresolved implementation choice is the storage/sync mechanism across hosts. Do not confuse either path with a whole-repo design default.

## Founder clarification (September 25, 2:39 PM IST)

Kunal confirmed both: a user's taste that follows them across projects, **and** improvements that should flow back to the OpenDesigner repository. These are different paths, not one global store. A user's portable taste remains their own opt-in preference; proposed changes to the open-source product become a separately reviewed contribution. A local decision or journey event must never automatically be published as a repo issue or PR. The first implementation can use an explicit export/review action for a sanitized improvement proposal, with the existing feedback mechanism as the starting point. Its contents and destination are reviewed before publishing. Keep the project answer, user-wide taste, and shared product improvement distinct in data and UI.

The remaining design question is *how* a user-wide profile follows a person across devices and hosts (local explicit import/export first versus hosted sync), not whether it should span projects. No cloud sync or cross-device disclosure is assumed.
