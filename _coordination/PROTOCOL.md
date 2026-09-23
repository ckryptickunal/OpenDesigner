# How parallel sessions collaborate on OpenDesigner

Any number of agents can work here at once: Claude sessions on this Mac, Claude or Codex sessions on other machines, ChatGPT with repo access, and humans. They coordinate through files in this repo, moved between machines by git. Nothing depends on one vendor's messaging.

## 1. Start of every session
1. `git pull --rebase` (skip if you are working in the orchestrator's working copy on Kunal's Mac).
2. Read `_coordination/BRIEF.md` (what we are building and why), this file, and `_coordination/SCHEMA.md` (source tiers, Decision Card format).
3. Pick a session name and keep it for the whole session. Export it: `export OD_SESSION="Your session name"`.
4. Run `python3 tools/od.py status` to see lanes, active sessions and unread messages, then `python3 tools/od.py inbox "$OD_SESSION"`.

## 2. Claiming and finishing work
- Claim before you start: `python3 tools/od.py claim L19`. It fails if another session holds the lane. If the lane you want is not on the board, add a row to `_coordination/BOARD.md` first (one line, status `open`).
- Post a heartbeat when you change task and at least every 30-45 minutes: `python3 tools/od.py heartbeat "what I am doing"`. Sessions with no heartbeat for 45 minutes are shown as inactive; their lanes can be taken over after messaging them.
- Finish: `python3 tools/od.py done L19 --summary "14 cards, 80 sources"`, then sync (section 4).

## 3. Talking to other sessions (use the first tier that works)
| Tier | Who | How |
|---|---|---|
| 1. Instant | Claude sessions on the same Mac | `SendMessage` to the session's name (find it with `ListAgents`). The orchestrator is **"Design system research and builder"**. Reply to a message by using its `from` value. |
| 2. Durable | Any agent that can read and write this repo, on any machine, any model | `python3 tools/od.py send "Session name" "message"`; the recipient reads it with `od.py inbox`. Messages are files in `_coordination/inbox/<recipient>/`, delivered between machines by `od.py sync`. Check your inbox at start, at each milestone, and before you finish. |
| 3. Human relay | Agents with no repo access (for example a chat-only ChatGPT) | Kunal pastes a prompt from `_coordination/lanes/` or `_coordination/SESSION_PROMPT.md`, and pastes the result back into `research/`. |

Keep messages to one or two lines plus a file path; the content belongs in files. Never ask another session to do something your own session was blocked from doing.

## 4. Git rules
- Sync with `python3 tools/od.py sync -m "L19: what changed"`: it commits, rebases on the remote, and pushes.
- Small commits, message prefixed with your lane. Never force-push `main`. Never commit secrets: `.env` and key files are git-ignored; keep them that way.
- Lane files have one owner, so conflicts are rare. If `BOARD.md` conflicts, keep both sides' rows and notes.

## 5. What gets traced (everything)
| What | Where |
|---|---|
| Every source opened, including rejected ones | `traces/<LANE>-trace.md` (append-only) |
| Every coordination or product decision, with the reason | `_coordination/DECISIONS.md` via `od.py log "decision and why"` |
| What each session did and when | `_coordination/sessions/<session>.md` via `od.py heartbeat` |
| Findings another lane needs | Bottom of `BOARD.md` via `od.py note "L19 -> L07: ..."` |
| Messages between sessions | `_coordination/inbox/` (read messages move to `read/`, never deleted) |

## 6. If the tooling is missing or broken, make a way
Everything above is plain files, so no tool is required:
- Claim by editing your lane's row in `BOARD.md`; heartbeat by appending a line to `_coordination/sessions/<your-name>.md`.
- Message by writing `_coordination/inbox/<recipient-slug>/<YYYYMMDD-HHMMSS>-<your-slug>.md` with `From:`, `To:`, `Sent:` lines and the text.
- If you invent a new mechanism, document it in this file in the same commit, so the next session can use it.

## 7. Done means
- Lane file ends with `## Open questions / gaps` and `## Confidence`.
- Trace file lists every source; `python3 tools/jev_nav.py check` reports no dangling references.
- Board row says `done`, your heartbeat says what you finished, and the work is synced.
