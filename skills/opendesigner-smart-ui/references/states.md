# States every part handles

Each part has one good fixture (`assets/fixtures/components/<slug>.json`). `audit.py` makes the other states from it, so every part is checked the same way and a new part gets the whole matrix for free.

## Content
| State | How the audit makes it | What a good part does |
|---|---|---|
| empty | every list emptied (`allowEmpty`) | the list says "Nothing to show yet." in the part's own type; the rest of the part still reads |
| partial data | every other property left out, rendered as streaming | missing slots show as loading blocks; nothing jumps when they fill |
| very long text | every string filled to its `maxLength` | wraps inside its box; no text cut off without a way to read it; no sideways scroll of the page |
| one item | every list cut to one | no orphaned dividers or headers |
| maximum items | every list filled to `maxItems` | scrolls inside its own box or pages; never pushes the page sideways |
| missing image | every image pointed at a photo that does not exist | a quiet block with the alt text in it, the same size |
| a 30% longer language | every word grows by 30% with no new spaces (a German stand-in) | labels wrap whole; buttons grow, never clip |
| right to left | `dir="rtl"` on the page | logical properties mirror the layout; numbers stay readable |

## Load and act
| State | How | What a good part does |
|---|---|---|
| loading skeleton | `showLoading(name)` before any answer | the part's own shape in quiet blocks, `aria-busy` |
| streaming partial node | `process(messages, {partial: true})` | as partial data, and actions are disabled until complete |
| error with retry | the `ErrorRetry` part | says what failed in plain words, one retry action |
| action pending, confirmed, failed | `setActionState(button, "pending" / "done" / "failed", note)` | pending: `aria-busy`, disabled, cursor shows progress; the note is read out by the live region |
| stale data | `@metadata.stale_since` | a quiet "Updated 10:42. It may have changed since." line above the part |
| no permission | `@metadata.permission: "denied"` | the part is not drawn; a notice says so, with the owner's note |

## Environment
| State | How the audit runs it |
|---|---|
| phone at 320 px | viewport 320 × 700 |
| 200% text size | the root font size doubled (tokens are rem) |
| dark mode | `prefers-color-scheme: dark` |
| reduced motion | `prefers-reduced-motion: reduce`; no endless animation may run |
| keyboard only | every control is focused in turn; focus must be visible (outline or ring) |
| screen reader | every control and image has a name; no two actions share one; one polite live region on the page |
| text-only fallback | `toText()` must say something for every complete answer |

## What the audit does not do
- It does not use a real screen reader. It checks names, roles and the live region, which is what a screen reader reads, not how one sounds.
- It does not judge whether a part is the right one for a question. The evals do.
- The craft checks (cut-off text, breathing room, kerning, copy) come from `opendesigner-review`. When its `probe.js` lacks them, the report says they did not run.
