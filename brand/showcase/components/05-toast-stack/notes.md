# 05 · Toast stack (Kinroom)

## Direction
Kinroom is a fictional team chat app. Toasts here confirm small things you just did (sent, deleted, saved), bring you a mention, or tell you an upload failed, and each one offers one way back: Undo, Retry or Reply. The mood is a soft lilac fog with white, pillowy toasts stacked in depth, ink text, one iris accent and mint for success. Built after the owner's type and colour rules, so it follows them from the start. Feel words: **soft, calm, friendly**.

## References (Mobbin, cited by link only)
- Asana deleted project, https://mobbin.com/screens/36cb9092-004d-4cfa-abc7-930e4a7ff931 : a thin time-left bar on the toast and Undo as a quiet button. Became the 3 px timer on auto-dismiss toasts.
- Coda moved doc, https://mobbin.com/screens/580abcac-fdb0-4c72-b6ea-b529d42bfa1e : one short sentence and "Undo" under it, nothing else. Taught me to keep toast copy to one line plus one action.
- Xero bill deleted, https://mobbin.com/screens/eaa61031-530a-4257-8597-19988a07959f : the toast's meaning carried by a coloured mark at the start. Became the tinted icon circles (mint, iris, rose).
- Campsite comment, https://mobbin.com/screens/30b8c544-1b7d-4d99-9ec6-7d55ef5fe5c6 : a message preview with the sender and a Reply button right there. Became the mention toast with Reply.

## System (engine)
- `sketch --name Kinroom --brand "#6F58D9" --audience regular --platforms web --feel soft,calm,friendly --theme system-light-dark --surfaces "chat:operate" --delegated all`. The brand kept its hex this time (white text passes on it).
- Dials (all `delegated`): expression 45, density 50, energy 62, roundness 78 (12 px controls, 24 px toasts), depth 72, colorfulness 55, **warmth 30** (the owner warned that high warmth turns neutrals brown; these are lilac-cool, ink is #242428).
- Answers: Q-color-09 hue-matched (lilac-tinted grays), Q-type-08 16 (to avoid the 11 px small step that operate surfaces get, see 03 and 04).
- Face: `raw.textFace Figtree` (OFL, Google Fonts). One family for the whole piece.
- The house toast standards (STD-components-toasts-drawers-07 to -18, -29, -30) gave the whole behaviour, and four of them are tokens: `component.toast.gap` 14 px, `.visible` 3, `.duration` 4000 ms, `.offset.desktop` 32 px.

## Type and colour (owner's rules)
- **One font**, Figtree, at 300, 400, 500 and 600.
- **Type scale, named roles** (web px, Material 3 names): label/caption 13 (descriptions, labels, buttons in toasts), body 16 (toast titles, chat, copy), title 20 (the "Variants" heading), headline 25 (wordmark), display 39 (page title). Five sizes, each at least 23% from the next.
- **Weight on purpose:** the display title is Figtree Light (300); its highlighted phrase is set by weight only ("Small news, **softly stacked.**" at 500, same colour, same font). The highlight was 600 at first; the left column then outweighed the toast stack, so it came down to 500. The eye goes to the fanned stack first.
- **Colour:** light fog with strong ink text and white surfaces; one iris accent for actions and the selected avatar; mint and rose only inside small icon circles. No mid-tone text on tinted surfaces.

## Build
Everything uses `--ds-*`: colours, radii, sizes, elevation, focus, the toast component tokens, `motion.duration.toast` and `motion.easing.toast` for the entrance, `motion.spring.momentum` for the stack fan-out and the swipe snap-back. Outside the tokens: the blurred fog blobs (art), and the "Bottom right" diagram.

Behaviour, following the house recipe: the newest toast is in front; older ones sit 14 px higher and 5% smaller each and share the front toast's height, with their content hidden. Hovering or focusing the stack fans it out with 14 px gaps, and a pseudo-element fills each gap so the hover holds. At most 3 show; more wait in a queue and come back as others leave. Plain toasts leave after 4 s with a visible timer, paused while hovered and while the tab is hidden; toasts with an action (Undo, Retry, Reply) stay until acted on or dismissed. Enter is 400 ms ease from below (locked); a toast can be dragged right to dismiss (past 80 px or fast), and a short drag springs back. F8 focuses the stack, Escape dismisses the focused toast. Undo really restores the deleted chat message; Retry turns the failed upload into a success toast. Only transform and opacity animate; the shared height snaps. Under reduced motion toasts only fade. The render uses `?still` to freeze timers and show the fanned-out state with a cursor.

Deviation, on purpose: the toaster is mounted inside the app frame so the sheet can show it in context. STD-components-toasts-drawers-03 asks for the document root in a real app; the diagram on the left says so.

## Checks
- First render: the fanned-out toasts overlapped (heights were measured while still collapsed to the front height). Fixed by clearing heights before measuring. Also: cursor hidden behind toasts, avatar initials clipped, Undo label not centred in its pill. Fixed.
- I had used 10.5 px initials in the small avatars; changed to one letter at 13 px before any check flagged it.
- Rendered contrast in the fanned-out state: 68 text runs, 0 below 4.5:1 (lowest 4.94:1, avatar initials on gradient).
- `preflight.py html`: 0 errors, 0 warnings.
- `engine.py validate`: no errors, no warnings.
- Computed sizes 13, 16, 20, 25, 39; one face, loaded (Figtree variable 300 to 700).
- `review`: 40 findings, mostly internal sizes; it flagged the height transition (fixed: removed) and a spinner's reduced-motion period as "over 300 ms" (a false positive, recorded).
- Playwright: collapsed transforms are translateY(-28px) scale(0.9), translateY(-14px) scale(0.95), translateY(0) scale(1); hover fans them out; the saved toast survives 4.5 s of hover and leaves 4.6 s after the pointer moves away; Undo restores the chat message; four quick fires keep 3 visible and queue the rest; F8 focuses the front toast; Escape dismisses it and a queued toast returns; a 140 px drag right dismisses.

## Process findings
1. **The standards wrote the component.** Thirteen toast rules gave stacking, timing, pausing, queueing, swipe and placement, with numbers. This is the clearest case in the set of OpenDesigner making a component better than I would have alone.
2. **"Springy" collides with locked motion.** The entrance is locked to 400 ms ease and the spatial springs are critically damped; only the momentum spring overshoots, by 1.5%. I used it where the recipe leaves room (fan-out, snap-back). Confusing, recorded.
3. **review misreads a spinner** as a slow transition and suggests the toast duration for it. Bug, recorded.
4. **Recipe numbers that are not tokens** (lift per index, scale per index, swipe threshold). Idea, recorded.
5. Honest note: this is the quietest of the five pieces. It is correct and calm, which is the brief, but it is less of a poster than 01 or 04.

## Round 3 (owner review, 2026-10-14)
**What Kunal said:** "okay, but still needs work". The earlier audit: lilac and mint fog blobs, 40 px pastel icon discs, 356 px pillow toasts with 24 px corners and pill buttons, pastel initials, and a marketing column ("Small news, softly stacked.") so the toast never appeared at product scale.

**What changed:** the toast stack now sits in its real place, the corner of a Kinroom room at 1440 x 900.
- **The app:** a small publisher's workspace (Pellwick Press) in the room launch-week, with Kinroom's own words and order ("Find ⌘K", "Inbox", "Kept for later", "Rooms" with a small filled square, "People", "Write in launch-week", a paperclip and @ only). One structure of its own: a **room brief** on the right (the book, out Thu 22 Oct; print run 3,000 with 400 held; reading 41 of 60 seats; advance copies 28 of 35; pinned call notes; a checklist with owners and due dates). The first rebuild in this round scored 3 because it read as Slack ("Jump to", Threads/Mentions/Saved, "#", "huddle") and was too empty; this one answers both.
- **The toasts:** ink, compact, one line where they can be, 288 px wide, in the window corner over the brief's empty lower half, so they never cover a message or the composer (messages are capped at 720 px). A 16 px icon, title 16, description 13, iris actions; the cards behind step lighter (#3d3d43, then neutral.light.11) so the collapsed stack reads as three cards.
- **Behaviour kept from the house standards** (STD-components-toasts-drawers-07 to -18): newest in front, 3 visible, 14 px lift and 5% smaller per layer, fan out on hover or focus, F8, Escape, drag right to dismiss. The timer bar sits on the plain toast ("Call notes saved") and not on Undo, because STD-15 keeps an action toast until the person acts (WCAG 2.2.1); the fresh auditor accepted this. Outside the tokens: the toaster sits in the brief column (right 24 px) rather than 32 px from the window edge, so it lines up with the brief's padding.
- **Story and data:** poster proofs (not the cover) back from the printer; the print run landed this morning; advance copies went out last week; the mention asks about chairs "for the 22nd"; 41/60 = 68%, 28/35 = 80%; 14 to 22 Oct is 8 days; Mon 19 Oct is the letter's due date and the Monday the last copies ship.
- **People and names:** Sana Ito (SI), Vikram Malhotra (VM) and Ruth Ashdown (RA) replace Ana Ito ("AI" read as a bot), Dev Malhotra ("DM" under Direct messages) and Ruth Halloway (one letter from a fictional detective); Thimbleweed Press became Pellwick Press (Thimbleweed recalls a game; no press by the new name found).
- **Engine:** `roundness 78 → 55`, `depth 72 → 45`, rebuilt; one face (Figtree) at 13 and 16, plus 11 px for avatar initials and file-type tiles.
- **States, one per frame:** `shot.png` (you just deleted your message; "Message deleted · Undo" in front, two tucked behind), `shot-expanded.png` (pointer over the stack, timer paused), `shot-mention.png` (a mention from another room on its own), `shot-error.png` (the corrected invite failed to upload; the failure stays on the composer chip and the toast carries the one Retry). `shot-uploading.png` was removed because its toast only repeated the chip.

**Checks:** rendered contrast: 0 visible runs below the floor (toast descriptions 6.7:1, Undo 6.9:1; the tucked toasts' hidden text is the only "failure" and is invisible). `check_dates.py`: pass. preflight: 0 errors, 2 warnings (11 px initials and file tiles, short labels). `engine.py validate`: no errors.

**Renamed (coordinator, 2026-10-15):** the app's first name belonged to two real products in the same field (a call-recording tool that plugs into team chat, and an older browser chat), so it is now **Kinroom**. Web search found no product or company called Kinroom; the old name is listed under "No longer on any page" in `brand/showcase/NAMES.md`. The `sketch` command above is shown with the current name; the system was renamed with `engine.py set name "Kinroom"` and rebuilt.

**Fresh-eyes audit:** 3/5, then 4/5 (low 4); its last notes (room icons that looked like checkboxes, a lumpy collapsed stack, states that disagreed with the brief, a wrapped label, two retries, the timing of the advance copies) were fixed. References: Asana toast with a time bar https://mobbin.com/screens/36cb9092-004d-4cfa-abc7-930e4a7ff931, Notion Mail dark one-line toast https://mobbin.com/screens/5ba89c38-f816-455e-bfa0-ad98517c7d0d, GitBook toast with a small icon https://mobbin.com/screens/9e06cd74-e5a9-4913-b907-5fc7476065be.

**Fresh score: 4.**
