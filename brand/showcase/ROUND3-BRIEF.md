# Showcase round 3: the owner's review (2026-10-14)

Kunal reviewed every piece. His verdict is in each audit file under `"owner"` (`brand/showcase/audit/<category>--<folder>.json`) and it outranks every other score. The independent auditor scored some pieces 4 that he calls "very ugly" (Maison Auberval, Kumo Kōbō). Our auditors are too kind, so judge by his eye.

## What he loves, and what that tells us
- **"I love the B2B product screens. They look absolutely crazy."** These are `brand/showcase/product/01` to `06`. Open every shot.png. They work because:
  - they are real, dense, believable product;
  - they use one accent and quiet chrome;
  - their type is small and exact;
  - their data is specific;
  - they have no decoration.
- **Orbika** (`heroes/08-y2k-retrofuture`): "good to go". One object made with care, and a confident display word.
- **Live workout** (`app-screens/04`), **boarding pass** (`app-screens/05`) and **Margin** (`components/02`), the one web component he doesn't call ugly. Also footers **Brask** (`01`), **Keystrata** (`02`) and **Rallo** (`08`).
- **What he calls ugly:** Howl Hill, Maison Auberval, Kumo Kōbō and Orvita (heroes, now removed), and most web components.
- **Specific notes:**
  - Private banking: "the fonts are not visible".
  - Recipe: "better fonts, better spacing".
  - Vigil: "needs a lot of work".
  - Quillon: "better spacing".

## The bar
Put each piece next to the B2B product screens and Orbika. If it looks weaker or more generic, it isn't done. Premium means:
- **Restraint:** one accent with one job, and type that does the work through size and weight.
- **Real content:** a structure built from shipped products, never copied.
- **Generous, exact spacing:** a 4 or 8 px rhythm, aligned edges, and room around each group.
- **Legible type:** body text at 15–17 px or more on web and 17 pt on iOS, with 4.5:1 contrast.

## Rules every piece follows
1. **Process:** follow `brand/showcase/BRIEF.md` (the engine sketch in the piece folder, tokens, render with `brand/tools/shot.py`, notes).
   - The engine knows named styles (`engine.py style search <words>`, `pick Q-dir-01 <style id>`) and a dense B2B profile (`--audience dense`).
   - Your brand color stays as you type it. If the engine changes it, set it back with `set raw.brandColor '"#hex"' --set-by chosen`.
2. **Tells:** read `skills/opendesigner/references/making.md`.
   - Section 11 lists the tells, with how often each appeared. Check every one, including a reference rebuilt too closely.
   - Section 5 covers checking the page as rendered: fresh eyes, contrast against the pixels behind the text, and comparing with shipped work.
3. **Fonts:** two typefaces at most, from open licences.
   - Use Apple or Google type-scale roles.
   - Highlight with weight, a fill or the second face.
   - Strong tonal contrast.
   - No brown with orange and cream. No violet AI glow.
4. **Dates and totals:**
   - `python3 brand/tools/check_dates.py <piece> --year 2026` must pass (or each flag must be shown to be a false positive).
   - Re-add every total from the page itself.
5. **Names:**
   - Check every invented person, company and brand against `brand/showcase/NAMES.md`. Each name belongs to one product only.
   - Web-search each new brand name.
   - Add your final names to NAMES.md: append only, never reorder.
6. **Fresh-eyes audit:** before you finish, ask a fresh-context subagent (Agent tool) to audit the render.
   - Give it this brief, the owner's note, the B2B product screens as the bar, and 3 Mobbin references (`mcp__mobbin__search_screens` or `search_sections`; `output_destination` "code"; `task_intent` "Rework showcase pieces after the owner's review").
   - Fix what it finds. Stop only when it scores 4 or more against the B2B screens.
7. **Record:**
   - Append a "Round 3 (owner review)" section to `notes.md`: what he said, what you changed, and the fresh score.
   - In the audit JSON, keep every existing field. Add `"round3": {"score": <fresh score>, "changed": [...]}` and set `"facts"` to whatever remains.
8. **Scratch:** use only your own folder, `/private/tmp/claude-501/-Users-Kunal-Desktop-Design-System/34a003df-3e22-4934-a798-b489a90e133e/scratchpad/<your-slug>/`. Write and delete only inside it.
9. **Limits:**
   - Never use real company names or logos.
   - Invented domains and email addresses end in `.example` (`nearmost.example`), and shown shell commands download before they run (see BRIEF.md hard rules).
   - Never save Mobbin images.
   - Don't commit; the orchestrator commits everything.
