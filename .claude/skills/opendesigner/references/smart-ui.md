# Smart UI: when to offer it

Smart UI (the `opendesigner-smart-ui` skill, in the same plugin) lets an assistant in the person's product answer with a part of their own system, like a comparison or a booking step, instead of only text. It is optional. Offer it; never build it without a yes.

## When to offer
- **Once per project**, after the system exists (the sketch is enough), at a natural pause: the end of a build round, or when they ask what's next. Never during the interview.
- **Only with a reason.** Run `python3 <smart-ui skill>/scripts/smartui.py offer --project .`. It reads the repo and prints a reason (a chat or assistant file, an AI SDK in the dependencies, an assistant in PRODUCT.md or the README) or "no reason". The person's own words count too: "our support bot", "the AI panel", "the chatbot looks off".
- **Not again after an answer.** Record it: `engine.py set profile.smart_ui '"yes"'` or `'"declined"'` `--why "<their words>"`. `offer` stays quiet once either is set. After a no, bring it up again only if they ask about their assistant's answers.

## How to say it
One message, plain words, the reason first, one question:
> Your product has an assistant (`src/SupportChat.tsx`). Its answers could show parts of your system, like a list of orders or a refund step, instead of paragraphs. Smart UI does that with your own components and checks every answer before it shows. Want me to set it up?

Then wait. On a yes, follow the `opendesigner-smart-ui` skill from its first step (scope). On a no, record it and move on.
