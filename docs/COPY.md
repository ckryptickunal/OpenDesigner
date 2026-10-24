# Copy that reads as written by a person

For every word OpenDesigner puts in public: videos, captions, posts, the website, the changelog, the footer, README and launch pages. The goal from Kunal (2026-10-22): at most 1 in 10 readers should think a line was written by AI.

## Why this is hard for us
Our readers are designers, front-end developers, engineering leads and AI builders. Most of them write with AI every day. A 2025 study found that five people who often use ChatGPT for writing, voting together, got 299 of 300 articles right when asked "human or AI?". Paraphrasing and "humanizer" tools did not fool them. They mostly noticed AI vocabulary, sentence shapes, safe and predictable ideas, formal tone and too-neat endings (Russell et al., ACL 2025, [arXiv 2501.15654](https://arxiv.org/abs/2501.15654)).

So disguise doesn't work. What works is copy only we could have written: a fact from this repo, a number, a thing that went wrong, an opinion someone could disagree with.

## The voice
- **One person, building in public.** Kunal is the only maintainer. Posts in his name say "I". The product and the site may say "OpenDesigner" or "we" only where no team is implied. Never imply users, a team or traction that FACTS.md doesn't show.
- **Outcome first, mechanism second.** "Make everything you build look like it belongs together" comes before tokens, skills or DESIGN.md (`_coordination/OWNER-FEEDBACK.md`, website review, item 7).
- **Plain and short.** Everyday words a school student follows. Say the plain meaning before any term.
- **Specific.** Numbers, names of files, counts from the repo, dates. "82 components" beats "a rich library".
- **Honest about stage.** Shipped and planned are said apart. "No users yet" is a line we are allowed to use, and it lands better than a vague claim.
- **Kunal's own words stay his.** When he gives a phrase ("Crazy af", "it has no rules"), keep it. Don't smooth it into something tidier. For posts in his name, hand him a draft to rewrite, never a finished post.

## Ten rules
1. **Lead with the point.** No warm-up line ("In today's world...", "Let's talk about...").
2. **One idea per sentence.** Then vary the length. A short one. Then a longer one that carries the detail. AI copy runs at one even rhythm.
3. **Use a fact instead of an adjective.** Cut "powerful", "beautiful", "comprehensive". Show the number or the before and after instead.
4. **Name the real thing.** "`engine.py review` flags 14 hard-coded colours" beats "smart checks catch issues".
5. **Use the plain verb.** "Use", "help", "make", "check", "show", "fix". Not "leverage", "empower", "streamline", "elevate".
6. **Say it once.** No summary at the end of a short piece, and no repeated tagline in one video (preflight M26).
7. **Pick two, or four.** Lists of exactly three adjectives or three clauses read as AI. Use the number of items there are.
8. **Have an opinion.** "Your AI isn't bad at design. It has no rules." A safe, balanced line is forgettable and reads as generated.
9. **Let it sound spoken.** Contractions, "says" not "notes", a question someone would really ask. Read it out loud. If you wouldn't say it to a friend, rewrite it.
10. **Cut 20% before you ship.** The last pass is always shorter.

## Tells to remove
The checker (`python3 tools/copy_check.py`) finds most of these. One tell alone proves little; three in a paragraph is what readers notice.

**Words.** delve, tapestry, testament, pivotal, crucial, vibrant, showcase, landscape, realm, foster, underscore, intricate, multifaceted, holistic, robust, seamless(ly), effortless(ly), elevate, empower, unlock, unleash, supercharge, leverage, harness, streamline, revolutionize, transform(ative), game-changer, cutting-edge, next-level, world-class, best-in-class, journey, embark, navigate (not about menus), boost, enhance, ensure, meticulous, nuanced, dynamic, ever-evolving.

**Openers and closers.** "In today's fast-paced...", "In a world where...", "Imagine...", "Whether you're a X or a Y", "Look no further", "Say goodbye to", "Here's the thing", "Let's dive in", "Overall,", "In conclusion,", "Ultimately,", "The result?", "The best part?".

**Shapes.**
- "It's not X, it's Y." and "Not just X, but Y." (one per piece at most, and only when X is something people really believe)
- "No X. No Y. Just Z."
- "From X to Y" when X and Y aren't two ends of anything
- A trailing "-ing" clause that claims meaning: "..., making it easier than ever", "..., highlighting the importance of..."
- A question answered straight away in the next line
- Every paragraph the same length; every bullet starting with a bold label and a colon

**Punctuation and formatting.** No em dashes (house rule already in `synthesis/glossary/WRITING-RULES.md`). No emoji used as icons or bullets. One exclamation mark per piece at most, usually none. No Title Case In Every Heading. No hashtags in the text; at most two at the end of a post where the platform expects them.

**Content.** Invented users, quotes, logos or numbers (never; FACTS.md and its Never list decide). Praise of ourselves ("beautiful", "stunning", "premium"). Promises we can't show on screen. Generic stand-in names like Acme or Jane Doe; use the registered example names and run `brand/tools/check_names.py`.

## Before and after
| Reads as AI | Reads as a person |
|---|---|
| Unlock a seamless, consistent design system in minutes! | Five questions. Then your app's colours, type and spacing, written to files your AI reads. |
| It's not just a design system. It's a design partner. | Your AI isn't bad at design. It has no rules. |
| Whether you're a designer or a developer, OpenDesigner empowers you to build beautiful UIs. | Made for people who already built something and want it to look like one product. |
| Leverage our robust review engine to ensure quality. | `engine.py review` lists every hard-coded colour and spacing value. It changes nothing until you say yes. |
| Join thousands of happy creators! | Made by one person. No users yet. Break it. |
| Elevate your workflow with cutting-edge AI. | Works in Claude, ChatGPT, Codex, Cursor and Gemini CLI. Same answers, same tokens. (Only if E is real.) |

## By surface
- **Video on-screen text.** 3 to 7 words per card. Readable muted. One claim per card, and the screen shows the proof of it. Read every card in order, out loud, before render (preflight M26).
- **Captions.** One line and a link. Write it the way Kunal would text it to a friend. Different first words for each platform, same fact.
- **Website and docs.** Outcome, then what it does, then how. Sentences under about 20 words. `python3 tools/readability.py <file>` for grade level.
- **Changelog.** What changed for the reader, in past tense, with the file or command. "The review now flags hard-coded radii" beats "Improved review capabilities".
- **Footer and small UI.** Nouns and verbs only. No slogans.

## The check before anything ships
1. `python3 tools/copy_check.py <files>` and fix or justify every hit.
2. Read it out loud. Mark any line you stumble on or wouldn't say.
3. Cut 20%.
4. Fresh eyes: someone who didn't write it reads it cold and points at the line that sounds most like AI. Fix that line. Repeat once.
5. For the 1-in-10 bar, the judge is people, not a detector. AI detectors are unreliable and score clean human text as AI. Show 10 people (or Kunal) and ask "would you guess a person or an AI wrote this?".

Sources: Russell et al. 2025 (above); Wikipedia, "Signs of AI writing" (editors' field guide; summarised in [TechCrunch, 2025-11-20](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/) and [Beutler Ink](https://www.beutlerink.com/blog/how-to-spot-ai-writing)); house rules in `synthesis/glossary/WRITING-RULES.md`, `skills/opendesigner/references/making.md` section 11, preflight M26, `_coordination/OWNER-FEEDBACK.md` and the GTM playbook brief ("Avoid: hype words, invented users or quotes").
