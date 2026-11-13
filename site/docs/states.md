---
title: Empty, loading and error states
seo_title: Empty, loading and error states: 404, skeletons, toasts
description: What a screen shows before, between and after its data: 404 and error pages, empty states, skeletons that don't jump, spinners, progress, banners and toasts.
section: Craft
order: 5
updated: 2026-11-13
---

Most screens spend part of their life without their data. They're empty before the first item, loading while it arrives, or broken when a request fails. These in-between states are where people get stuck, so each one needs a design of its own.

The [component library](/library/) has 22 finished parts for them, in its **States** aisle. Like every library part, they use only your design tokens, so they take your colours, type and spacing.

## Every state answers three questions

1. **What happened?** In plain words, without blaming the person. "We can't find that page", not "Invalid URL".
2. **Is my work safe?** Say so when it is: "Your text is kept on this page".
3. **What can I do now?** One clear next step: search, try again, ask for access or clear the filters.

{{figure:states-words}}

The words follow the house [copy rules](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/COPY.md): sentence case, no "Oops" and no joke when something failed.

## Pages for when the whole screen can't show

| Page | When | It offers |
|---|---|---|
| [Page not found](/library/page-not-found/) (404) | The link is old or the page moved | A search, Go to home and Go back |
| [Something went wrong](/library/page-error/) (500) | The server failed | Try again, and a reference code for support |
| [Offline](/library/page-offline/) | No connection | What still works on this device, and what waits |
| [Maintenance](/library/page-maintenance/) | Planned downtime | What's paused, that nothing is lost, and when it's back |
| [No access](/library/page-no-access/) (403) | Signed in, but not allowed | Who owns it, and a way to ask for access |
| [Session expired](/library/session-expired/) | Signed out mid-task | Sign in again, with the draft kept |

## Empty is not one state

A list can be empty for four different reasons, and each needs different words.

| Why it's empty | Part | Says |
|---|---|---|
| Nothing has been made yet | [First use](/library/empty-first-use/) | What this area is for, and the one action that starts it |
| A search found nothing | [No results](/library/empty-no-results/) | What was searched and where, and ways to widen it |
| Everything is done | [All done](/library/empty-all-done/) | That nothing is waiting, and when new items will show up |
| Filters hide everything | [Filtered to nothing](/library/empty-filtered/) | Which filters are on, and a button to clear them |

## Loading: match the wait

{{figure:states-wait}}

The inline spinner waits about a second before it shows, so a quick answer never flashes. A system made with OpenDesigner can set these limits with its `--ds-state-wait-*` tokens; the parts fall back to 1 second where a system doesn't have them.

### Skeletons that don't jump

{{figure:states-skeleton}}

The five skeleton parts ([text](/library/skeleton-text/), [card](/library/skeleton-card/), [list](/library/skeleton-list/), [table](/library/skeleton-table/) and [media](/library/skeleton-media/)) are the loaded layout itself, greyed out. Each line keeps its font and line height and stays on one line, and each picture keeps its frame. Each was measured in a browser at 1440 and 375 px wide, and none of the five moved by a single pixel when its data arrived. While your data loads, fill the part with placeholder text of a typical length. Each line is held to one line, so the real text can be longer or shorter without changing the height.

While loading, the area is marked busy for screen readers and can't be tabbed into. A short status says when it starts and when it's done. With reduced motion turned on, the grey bars stay still instead of shimmering.

### Short waits and long tasks

- **[Inline spinner](/library/inline-spinner/)**: inside the button or beside the field that's working. The button stays focused and can't be pressed twice.
- **[Progress with steps](/library/progress-steps/)**: for imports, exports and uploads. It announces each new step, not every percent.
- **[Optimistic update](/library/optimistic-update/)**: shows a small change at once. If the save fails, it puts things back and says why, with a retry.

## Feedback after an action

| Part | Use it for |
|---|---|
| [Page banners](/library/page-banners/) | News about the whole page or account: info, success, warning and error. The error banner stays until it's fixed |
| [Toast with undo](/library/toast-undo/) | A reversible action such as archive. Undo puts the item back where it was, and the toast has no timer |
| [Inline field error](/library/field-error/) | One field that can't be accepted. The message sits under the field and clears once the value is right |
| [Success confirmation](/library/success-confirmation/) | The end of a task people want proof of: what happened, the details to keep, and what happens next |

:::dev
Each part's `meta.json` lists when to use it and when not, its keyboard behaviour and how it handles seven edge cases: empty, loading, error, disabled, overflow, long text and a missing image. A `fixture.json` beside it holds its sample data. `python3 skills/opendesigner/scripts/library.py list --type states` lists all 22. Where a system has the `--ds-state-*` tokens, the parts use them; every use falls back to a token every system has, and `library.py check` enforces that.
:::
