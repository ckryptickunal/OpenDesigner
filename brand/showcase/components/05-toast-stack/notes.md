# 05 · Toast stack (Chorus)

## Direction
Chorus is a fictional team chat app. Toasts here confirm small things you just did (sent, deleted, saved), bring you a mention, or tell you an upload failed, and each one offers one way back: Undo, Retry or Reply. The mood is a soft lilac fog with white, pillowy toasts stacked in depth, ink text, one iris accent and mint for success. Built after the owner's type and colour rules, so it follows them from the start. Feel words: **soft, calm, friendly**.

## References (Mobbin, cited by link only)
- Asana deleted project, https://mobbin.com/screens/36cb9092-004d-4cfa-abc7-930e4a7ff931 : a thin time-left bar on the toast and Undo as a quiet button. Became the 3 px timer on auto-dismiss toasts.
- Coda moved doc, https://mobbin.com/screens/580abcac-fdb0-4c72-b6ea-b529d42bfa1e : one short sentence and "Undo" under it, nothing else. Taught me to keep toast copy to one line plus one action.
- Xero bill deleted, https://mobbin.com/screens/eaa61031-530a-4257-8597-19988a07959f : the toast's meaning carried by a coloured mark at the start. Became the tinted icon circles (mint, iris, rose).
- Campsite comment, https://mobbin.com/screens/30b8c544-1b7d-4d99-9ec6-7d55ef5fe5c6 : a message preview with the sender and a Reply button right there. Became the mention toast with Reply.

## System (engine)
- `sketch --name Chorus --brand "#6F58D9" --audience regular --platforms web --feel soft,calm,friendly --theme system-light-dark --surfaces "chat:operate" --delegated all`. The brand kept its hex this time (white text passes on it).
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
