# How sessions and agents collaborate on this project

Several agents work here: subagents spawned by the orchestrator, and optionally other Claude sessions that Kunal starts. They share one filesystem and can message each other.

## 1. The filesystem is the source of truth
- `_coordination/BOARD.md` is the claim board. Before starting a lane, read it. Pick an `open` lane (or one Kunal assigned you) and change its status to `claimed by <your session name>`. Change it to `done` when you finish.
- Write only to your own lane's files (`research/<LANE>-*.md`, `traces/<LANE>-trace.md`). Never overwrite another lane's file.
- Cross-lane findings go in BOARD.md under "Cross-lane notes" as one-line appends.
- Every source you open goes in your trace file, including rejected ones. That is the audit trail.
- Follow `_coordination/SCHEMA.md` for source tiers and the Decision Card format.

## 2. Messaging
- The orchestrator session is named **"Design system research and builder"**. Any local Claude session can reach it with `SendMessage` (to: that name). Use `ListAgents` to find it. Its ref at start was `332188`.
- Send a message when you claim a lane, when you finish, or when you find something that changes another lane's work. Keep messages to one line plus a file path. The content itself belongs in files.
- The orchestrator replies to the `from` attribute of your message.
- Do not ask another session to do something your own session was blocked from doing.

## 3. Detecting prior work
Before starting, check `_coordination/BOARD.md` and `traces/`. If a lane is already `done`, extend it in a new file (`research/<LANE>-addendum-<session>.md`). Do not redo it.

## 4. Done means
- Lane file ends with `## Open questions / gaps` and `## Confidence`.
- Trace file lists every source.
- BOARD.md status is `done`, and the orchestrator has been messaged.
