---
type: source
title: The 7 UI Components to Design Like Unicorn AI Startups
created: 2026-09-27
updated: 2026-09-27
video_id: If7iCPDy2vk
url: https://www.youtube.com/watch?v=If7iCPDy2vk
channel: Kole Jain
published: 2025-08-13T02:43:33Z
authority: reference
tags:
  - ai-products
  - prompt-box
  - generation-history
  - ai-memory
  - inline-editing
  - streaming
  - skeleton-loading
  - shimmer
  - confidence-indicator
  - glassmorphism
  - progressive-disclosure
  - loading-states
---

# The 7 UI Components to Design Like Unicorn AI Startups

## Metadata

- Video ID: `If7iCPDy2vk`
- Channel: Kole Jain
- Published: 2025-08-13T02:43:33Z
- URL: https://www.youtube.com/watch?v=If7iCPDy2vk

## Summary

Kole Jain walks through the UI patterns that 'unicorn' (billion dollar) AI startups share: a large prompt box, generation history and memory, inline AI editing, showing the AI's work, streamed and skeleton loading, confidence indicators, and a dark soft glass look. For most of them he names real products that do it well (Claude, Replit, Cursor, Notion AI, Lex.page, Perplexity, Relume, Amazon Comprehend, ChatGPT), and for several he describes his own free Figma component (memory panel, inline edit selectors, research trail, skeleton shimmer, confidence pill, glass surface). The common thread is that an AI product should give feedback at every step: previews in the input, retrievable history, visible and controllable memory, fast inline revision, a visible research trail, output that streams in, and an honest signal of how sure the model is [inferred]. For someone building a design system for an AI product, it gives a checklist of components (prompt input, history list, memory panel, inline edit bar, step trail, skeleton with shimmer, confidence pill) plus a recipe for the glass surface.

## Key Ideas

- Prompt-based tools tend to open with a giant prompt box, which gets people trying the tool immediately and keeps the area above the fold clean.
- ChatGPT and Gemini dropped their landing pages entirely, so visitors land straight in the interface.
- A good prompt box previews attachments such as PDFs and images, and compresses large pastes such as code into a compact block.
- Mode chips, adding context such as code, integration buttons (Google Drive, GitHub, Figma, internal tools), an advanced-mode toggle and a token cost estimate turn the input into a control panel.
- Loading indicators in AI tools should be short, looping and fluid.
- Generation history is essential for products that output text, code or images, and its core principle is retrievability: snippets, deletion and search.
- History records what happened; memory records what matters, so persistent memory should be visible and user-controlled, not hidden in settings.
- Inline AI editing (highlight, then say what to change) feels like real-time revision rather than regeneration; keep its controls short and compact.
- Showing the steps the AI took (documents retrieved, sources cited) makes the product feel intelligent and like a collaborator, not a black box.
- Waiting is tolerable when there is feedback: streaming output word by word and skeletons with shimmer make delays part of the experience.
- Confidence indicators tell people when an AI answer may be wrong: a label such as 'high confidence' or 'unverified', with the numeric score one click away.
- The dark soft glass look (dark background, blur, striking gradients, subtle animation) is common among AI startups and simple to build in Figma.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Creator of the video; presents the AI UI patterns and gives away Figma components he built for them.
- [[entities/chatgpt|ChatGPT]] (product): Cited for dropping its landing page, organising history by session, exposing memory, and streaming responses.
- [[entities/gemini|Gemini]] (product): Cited alongside ChatGPT for dropping its landing page so visitors land in the interface.
- [[entities/claude|Claude]] (product): Cited for previewing attached PDFs and images as blocks, its rotating star loading animation, and inline AI editing.
- [[entities/replit|Replit]] (product): Cited for compressing pasted code into a clean viewable block in the prompt box.
- [[entities/cursor|Cursor]] (product): Cited for letting people add code context to the chat.
- [[entities/notion-ai|Notion AI]] (product): Cited for its three bouncing dots loader, generations tied to the original block, contextual edit buttons and streamed output.
- [[entities/lex-page|Lex.page]] (product): Writing tool cited for rephrasing a sentence inline with keyboard shortcuts.
- [[entities/perplexity|Perplexity]] (product): Cited for showing its research steps: documents retrieved, sources cited and the flow of logic.
- [[entities/relume|Relume]] (product): Cited for skeleton loading with shimmer placeholders while generating a wireframe (captions say 'Reloom').
- [[entities/amazon-comprehend|Amazon Comprehend]] (product): Cited for showing a confidence score with an answer (97% in the source's example, 61% or an 'uncertain' flag when unsure).
- [[entities/github|GitHub]] (company): Cited as a page using the dark soft glass look.
- [[entities/figma|Figma]] (tool): Tool used to build the glass effect and the free component files.
- [[entities/final-round-ai|Final Round AI]] (company): Sponsor of the video; its cover letter generator is plugged mid-video (captions say 'final rounds').
- [[entities/progressive-disclosure|Progressive disclosure]] (concept): Built right into the prompt input, for example a button that toggles advanced mode or a token cost estimate above the input.
- [[entities/retrievability|Retrievability]] (concept): The core design principle for generation history: people must be able to find past outputs again.
- [[entities/confidence-indicator|Confidence indicator]] (concept): A label or score showing how sure the AI is about an answer.
- [[entities/dark-soft-glass-effect|Dark soft glass effect]] (concept): Translucent dark surfaces with blur, gradients, a one pixel border and soft inner shadow.

## Topics

- [[topics/saas-product-ui|SaaS product UI]]: Seven recurring component patterns in AI products: prompt box, history and memory, inline editing, visible reasoning steps, loading, confidence indicators and glass styling.
- [[topics/forms-and-inputs|Forms and inputs]]: The prompt box as the main input: attachment previews, collapsing large pastes, mode chips, context and integration buttons, an advanced toggle and a token cost estimate.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Short looping loaders, streaming output word by word, skeleton placeholders with shimmer, step-by-step research trails and confidence labels all give feedback during waits.
- [[topics/micro-interactions|Micro-interactions]]: Examples of small motion: Notion AI's three bouncing dots, Claude's rotating star, research steps fading in one by one, and a shimmer running across a glass border.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: The dark soft glass recipe: a semi-transparent rectangle, subtle gradient, background blur, a one pixel border and a soft inner shadow.
- [[topics/landing-pages|Landing pages]]: ChatGPT and Gemini dropped their landing pages so visitors land in the product; a giant prompt box above the fold gets people trying the tool immediately, kind of like Google.
- [[topics/figma-and-design-tools|Figma and design tools]]: The glass effect is described as easy to build in Figma, and the components are shared as Figma files.
- [[topics/design-resources|Design resources]]: The creator gives away Figma files of the components he built for each pattern.

## Notable Claims

- Starting with a giant prompt box gets the user trying out the tool immediately and gives a cleaner aesthetic above the fold. Evidence: It gets the user trying out the tool immediately
- ChatGPT and Gemini have both ditched their landing pages entirely, so the moment you land you are in the interface. Evidence: both ditched their landing pages entirely
- Replit compresses pasted code instantly into a clean viewable block. Evidence: Pasting code instantly compresses into a clean viewable block
- Letting people add code context to the chat gives them confidence that the AI knows what they want before they say it. Evidence: gives you the confidence that the AI knows what you want
- Most AI tools still hide memory in settings or do not expose it at all. Evidence: most tools still hide memory in settings
- Inline AI editing is fast, contextual and removes friction. Evidence: It's fast, contextual, and removes friction
- Showing research steps makes the product feel intelligent because it shows the AI is referencing material rather than pulling answers from the void. Evidence: pulling answers from the void
- Streaming responses word by word turns delay into anticipation. Evidence: That trickle of output turns delay into anticipation
- Amazon Comprehend returns a confidence score with an answer, for example 97% for a confident answer, and may show 61% or flag the result as uncertain when unsure. Evidence: Amazon comprehend does this well
- Startups use the dark soft glass effect to exude technological supremacy. Evidence: trying to exude technological supremacy
- Showing the AI thinking makes even delays part of the experience; what users hate is waiting without feedback. Evidence: even delays become part of the experience
- ChatGPT has implemented user-visible memory control, but most tools still hide memory in settings or do not expose it. Evidence: Chat GBT has implemented this

## Quotes

> Actually, users hate waiting without feedback.
> memory is a record of what matters.
> turns your history into a workspace, not a waste basket.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Final Round AI's cover letter generator (a claimed 30 minutes by hand versus about one with the tool); excluded from rules.
- Caveat: The video shows components on screen but states almost no exact values: no durations, blur amounts, opacities, gradient colours or shadow settings for the glass effect beyond the one pixel border.
- Caveat: The source counts '7 UI components' in the title, but the transcript does not number them; how the patterns group into seven is the analyst's reading [inferred].
- Caveat: The patterns describe what AI startups do in 2025 (published 2025-08-13), not tested results; phrases like 'you're doing it wrong' and 'Twitter would really benefit' are opinion.
- Caveat: The confidence scores (97%, 61%) are illustrative examples, not measured values.
- Caveat: Amazon Comprehend is a text analysis service, not a question-answering tool, so the 'president in 2009' confidence example may be illustrative rather than a real Comprehend feature [inferred].
- Caveat: Auto-caption fixes: 'ChachiBT', 'CHBT' and 'Chat GBT' read as ChatGPT, 'Replet' as Replit, 'Reloom' as Relume, 'final rounds' as Final Round AI. 'context taking' is left as captioned; it may mean context tagging. [inferred]
- Caveat: The video does not discuss accessibility of shimmer or streaming (for example reduced motion or screen reader announcements) or contrast on translucent glass surfaces.
- Caveat: The timestamps in the description are cut off after 'Inlin'.

### Rules and practices

- **should** (patterns, all): In prompt-based tools, open with a large prompt box above the fold so people can try the tool straight away. Why: It gets the user trying out the tool immediately and gives a much cleaner aesthetic above the fold. [if you're not starting with a giant prompt box]
- **should** (components, all): Preview attached PDFs and images as blocks inside the prompt box. Why: A great prompt box has to feel useful, not just be an input field. [previewing PDFs or images like these blocks]
- **should** (components, all): Collapse large pasted inputs such as code into a compact, viewable block instead of showing them in full in the chat. Why: So they don't take over the chat. [grouping large inputs like code blocks]
- **consider** (components, all): When the AI has broad use cases, let people give it context in the prompt box: chips that switch the mode (for example brainstorm, data, email) or a way to add context such as code. Why: It gets better answers, and adding context (as Cursor does with code) gives people confidence the AI knows what they want before they say it. Values: brainstorm, data, email. [Think chips that change the mode]
- **consider** (components, all): Consider integration buttons in the prompt box that connect to other tools such as Google Drive, GitHub, Figma or internal tools. Why: As AI gets more capable, deep integrations are starting to appear in prompt boxes. Values: Google Drive, GitHub, Figma. [Think buttons that connect to Google Drive, GitHub, Figma]
- **consider** (components, all): Build progressive disclosure into the prompt input, such as a button that toggles advanced mode or a token cost estimate shown right above the input. Why: It turns the prompt box from just an input into the control panel for the product. [build progressive disclosure right into the input]
- **must** (motion, all): Keep AI loading indicators short, looping and fluid. Why: The prompt experience should all feel fast. Values: three bouncing dots, rotating star. [Any loading indicators need to be short, looping, and fluid]
- **must** (patterns, all): If the product outputs text, code or images, provide a generation history. Why: The source calls generation history essential for such products. [generation history is essential]
- **should** (patterns, all): In generation history, preview the first line or a short snippet of each generation, allow deleting chats, and allow search. Why: The core design principle is retrievability; search turns history into a workspace, not a waste basket. [The core design principle is retrievability]
- **must** (patterns, all): If the AI has persistent memory, show it to people and let them control it. Why: History is a record of what happened, but memory is a record of what matters; the source calls it a huge opportunity. [you absolutely need to show it and let users control it]
- **consider** (components, all): Give persistent memory a dedicated panel where people can see the storage space used, bulk delete irrelevant content and add key facts. Why: It is how the source's own component lets users see and control memory. [we're giving users a dedicated memory panel]
- **should** (patterns, all): Do not hide AI memory in settings or leave it unexposed. Why: The source calls hiding memory, as most tools do, 'wild'. [most tools still hide memory in settings]
- **should** (patterns, all): Let people highlight any part of an AI response and type what they want changed. Why: It is fast, contextual and removes friction, and feels like real-time revision, not regeneration. [inline AI editing]
- **should** (components, all): Keep the inline edit control short and compact: a few quick selectors plus keyboard shortcuts. Why: For the user it then feels like real-time revision, not regeneration. [The idea is to keep this short and compact]
- **consider** (patterns, all): Show the steps the AI took, such as documents retrieved and sources cited, fading each step in one by one. Why: It makes the product feel intelligent and the AI feel like a collaborator, not a black box. Values: searching docs, extracting quotes, drafting answer. [These fade in one by one]
- **should** (patterns, all): Don't make people wait without feedback; show the AI thinking while it works. Why: Users hate waiting without feedback, but when the AI is shown thinking, even delays become part of the experience. [users hate waiting without feedback]
- **should** (patterns, all): Stream AI responses word by word rather than showing them only when complete. Why: Users hate waiting without feedback; the trickle of output turns delay into anticipation. [stream their responses word by word]
- **should** (patterns, all): While content generates, show skeleton placeholders with a shimmer effect where the content will appear, then slot the content exactly into place. Why: The layout feels alive and the product feels like it is working alongside the user. [Skeleton loading, like in Reloom]
- **should** (components, all): Show a confidence indicator with AI answers: a label or score that flags when the result is uncertain. Why: A lot of AI outputs feel confident but aren't; the source calls confidence indicators the solution. [the solution? Confidence indicators]
- **consider** (components, all): Build the confidence indicator as a pill-shaped bar below each AI response with a label such as 'high confidence' or 'unverified', clickable to reveal the numeric confidence value. Why: It is the source's own component for flagging uncertain answers. Values: high confidence, unverified. [pill-shaped bar below each AI response]
- **consider** (elevation, all): To build a dark soft glass surface, use a rectangle with some transparency, a subtle gradient, background blur, a one pixel border and a soft inner shadow. Why: It is the look AI startups use to exude technological supremacy, and it is easy to build in Figma. Values: one pixel border. [a one pixel border and soft inner shadow]
- **consider** (motion, all): Optionally run a gentle shimmer across the border of a glass surface for a subtle animation. Why: The source adds it to its glass component for a subtle, luxury glass feel. [a gentle shimmer that runs across the border]

### Decisions it informs

- What should a first-time visitor to an AI product land on?
  - A separate landing page: Visitors read marketing before they touch the tool [inferred]. When: Not recommended by the source for prompt-based tools [inferred].
  - The interface itself, led by a giant prompt box: Visitors start trying the tool immediately, with a clean, Google-like area above the fold. When: Prompt-based tools; ChatGPT and Gemini work this way.
  - Recommendation: Start with a giant prompt box; it gets people using the tool immediately and looks cleaner above the fold.
- How should the product organise past generations?
  - By session in a vertical list: A list of previous runs, one entry per session. When: As ChatGPT does.
  - Tied to the original document block: Each generation stays attached to the place it was made. When: As Notion AI does.
  - Recommendation: Either way, design for retrievability: a snippet preview per item, deletion and search.
- How do people revise part of an AI response?
  - Regenerate the whole response: The full answer is replaced [inferred]. When: The source contrasts this with inline editing, which feels like revision instead [inferred].
  - Highlight and type the change: Fast, contextual editing of just the selected part. When: As Claude does with its responses.
  - Keyboard shortcuts for inline rephrasing: Rephrase a sentence in place with a few keys. When: As the writing tool Lex.page does.
  - Contextual buttons under each paragraph: One-click actions such as 'improve writing' or 'fix spelling'. When: As Notion AI does.
  - Recommendation: Offer inline editing and keep it short and compact: a few quick selectors and keyboard shortcuts, so it feels like real-time revision, not regeneration.
- What should people see while the AI is generating? (`Q-state-08`)
  - A short looping indicator: A small fluid loop such as three bouncing dots or a rotating star. When: Loading indicators in the prompt experience (Notion AI, Claude).
  - Streamed output word by word: A trickle of output that turns delay into anticipation. When: Text responses (Notion AI, ChatGPT and everyone else).
  - Skeleton placeholders with shimmer: Placeholder images and text boxes shimmer, then the content slots exactly into place. When: Generated layouts, as in Relume's wireframe canvas.
  - A step-by-step research trail: Steps like searching docs, extracting quotes and drafting answer fade in one by one. When: Research and retrieval, as Perplexity does.
  - Recommendation: Don't make people wait without feedback; show the AI thinking through streaming, skeletons with shimmer, or visible steps, and keep any loader short, looping and fluid.
- How should the product show how sure the AI is?
  - A numeric confidence score: A percentage such as 97% for a confident answer or 61% when unsure. When: As Amazon Comprehend does.
  - A labelled pill below each response: A pill-shaped bar reading 'high confidence' or 'unverified', clickable for the numeric value. When: The source's own component.
  - No indicator: Every output looks equally confident, though many aren't [inferred]. When: The source argues this is the problem to solve [inferred].
  - Recommendation: Use a labelled pill below each response and let people click for the numeric value.

### Process

1. Build the prompt box as a control panel: Start from a large input, then add attachment previews, collapsed blocks for large pastes, mode chips, context and integration buttons (Google Drive, GitHub, Figma), an advanced-mode toggle and a token cost estimate above the input.
2. Design the history list for retrieval: Show the first line or a short snippet of each generation, allow deleting chats, and add search.
3. Add a memory panel: Show the storage space used, allow bulk deleting irrelevant content, and let people add key facts to persistent memory.
4. Build the inline edit control: Let people highlight part of a response and type the change; keep the control short and compact with a few quick selectors and keyboard shortcuts.
5. Build the research trail: Simulate a mini research trail of three animated steps (searching docs, extracting quotes, drafting answer) that fade in one by one.
6. Build the skeleton loader: Place a simple loading animation and shimmer where the text will eventually appear; when the content is ready it slots into place (as Relume does).
7. Build the confidence pill: Put a pill-shaped bar below each AI response with a label such as 'high confidence' or 'unverified', and let people click it for the numeric confidence value.
8. Build the dark soft glass surface in Figma: Draw a rectangle with some transparency, add a subtle gradient, blur the background, add a one pixel border and a soft inner shadow; optionally run a gentle shimmer across the border.

### Examples and visual references

- Landing straight in the interface (ChatGPT and Gemini): No landing page: a giant prompt box above the fold, kind of like Google.
- Attachment previews in the prompt box (Claude): Attached PDFs and images show as preview blocks inside the input.
- Pasted code collapses into a block (Replit): Pasting code instantly compresses into a clean viewable block so it doesn't take over the chat.
- Adding code context to the chat (Cursor): People attach code context to a message, signalling the AI knows what they mean.
- Short looping loaders (Notion AI and Claude): Notion AI's three bouncing dots and Claude's rotating star animation.
- Generation history styles (ChatGPT and Notion AI): ChatGPT lists previous runs by session vertically; Notion AI ties generations to the original document block.
- Memory panel component (Kole Jain's free component (ChatGPT has a similar feature)): A dedicated panel showing storage space, bulk delete and adding key facts.
- Inline AI editing (Claude, Lex.page, Notion AI): Highlight a response and type the change (Claude); rephrase with keyboard shortcuts (Lex.page); buttons like 'improve writing' or 'fix spelling' under each paragraph (Notion AI).
- Research trail (Perplexity; Kole Jain's component): Perplexity shows documents retrieved, sources cited and a logic flow across hops; the component shows three animated steps fading in one by one.
- Skeleton loading with shimmer (Relume): While generating a wireframe, the canvas shows placeholder images and text boxes with shimmer, then content slots into place.
- Confidence score (Amazon Comprehend): Asked who was president in 2009, it returns Barack Obama with a score such as 97%; uncertain answers might show 61% or an uncertain flag.
- Confidence pill component (Kole Jain's free component): A pill-shaped bar below each AI response labelled 'high confidence' or 'unverified'; clicking it shows the numeric value.
- Dark soft glass look (GitHub): Dark backgrounds, blur, striking gradients and subtle animations; the component adds a shimmer running across the border.

### Numbers

- 97%: Example confidence score Amazon Comprehend might show for a confident answer [maybe 97%]
- 61%: Example confidence score when the model is not sure [it might show 61%]
- one pixel: Border width on the dark soft glass surface [a one pixel border and soft inner shadow]
- three: Animated steps in the research trail component (searching docs, extracting quotes, drafting answer) [three animated steps]
- 7: Number of AI startup UI components covered in the video [The 7 UI Components to Design Like Unicorn AI Startups]
- three: Notion AI's loader is three bouncing dots [Notion AI's three bouncing dots]

<!-- /od:learn -->
