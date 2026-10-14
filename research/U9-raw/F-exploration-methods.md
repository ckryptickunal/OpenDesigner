# F: Methods and evidence for exploring, discovering and generating visual styles

Research for the OpenDesigner style lab (`skills/opendesigner/references/style-lab.md`). Every finding cites a source id from the list at the end. Every source in that list was opened during this research (paper text, publisher abstract, or the author's own page). Where only an abstract or a secondary summary could be opened, the finding says so. Anything I concluded rather than read is marked [inferred].

Date of research: 14 October 2026.

---

## 1. Generative methods

### 1.1 Morphological analysis (the Zwicky box)
- Fritz Zwicky developed general morphological analysis from the 1940s until his death in 1974. You list the parameters of a problem, give each a set of values, and treat every combination of one value per parameter as a candidate configuration [S1].
- The step that makes it usable is cross-consistency assessment: compare every pair of values, mark the pairs that cannot coexist, and drop every configuration containing such a pair. Logical and empirical judgments come first, normative ones later [S1].
- The space explodes fast. Ritchey's shelter study began with ten parameters and over 500,000 configurations [S1].
- For the tool: the 12 axes are already a Zwicky box. The lab's "repairs" table is an informal cross-consistency matrix. Making it a full pairwise matrix (value x value: fine, repair, forbidden) would make the rules complete and checkable [inferred].

### 1.2 Conceptual blending
- Fauconnier and Turner treat blending as an everyday mental operation. Structure from two input spaces is projected, selectively, into a blended space. Through completion and elaboration the blend develops structure that neither input had (emergent structure). Blending follows a set of optimality principles [S6, original abstract].
- VisiBlends applies blending to graphic design: a visual blend merges two objects into one image to carry a message. Its design pattern (Single Shape Mapping) only blends objects that share a simple 3D shape, grounded in how people recognise objects. The workflow split the work into human microtasks and computation and improved novices' ability to make blends [S7].
- For the tool: a blend works when the inputs share an anchor (Fauconnier and Turner's generic space; VisiBlends' shared shape). The lab's "bones of A, skin of B" mix is a selective projection. It should also name the shared anchor and the emergent property ("magazine bones, comic skin: reads as a zine") so the person can judge the result [inferred].

### 1.3 Style tiles, element collages and mood boards
- **Style tiles** (Samantha Warren, 2012): agree fonts, colours and interface styles before layout. Full comps make clients feel the design is finished; mood boards are too vague for a complex site; several full comps invite a "Frankencomp" that mixes parts without regard to goals [S2].
- Warren showed The Washington Examiner three tiles, one per client adjective (clean, strong, friendly). The client took the direction of one, a detail of another and the typeface of the third, and that fourth tile shaped the site [S2]. People recombine traits across directions; the tool should let them.
- **Element collages** (Dan Mall, November 2012) adapt style tiles into loose arrangements of real interface pieces. Mall found wireframes and mood boards too abstract for clients. Collages record an idea at any stage of development and later merge with the site's structure [S3].
- **Mood boards** (Lucero, DIS 2012; 14 practising designers, all but one with 10+ years' experience) play five roles: framing, aligning, paradoxing, abstracting and directing [S4].
  - Paradoxing: boards let designers explore apparently conflicting ideas, such as a brief for "organic-eco-luxury". Too much conflict between images hides the intended feeling [S4].
  - Abstracting: staying abstract keeps more directions open; going concrete narrows them to what sits next to the pictures shown [S4].
- For the tool: show directions as tiles or component sheets (buttons, input, card, type pair, colour, one chart), not full pages, and keep the person's tension words (paradoxes) as first-class input [inferred from S2, S3, S4].

### 1.4 Parallel exploration and design galleries
- Dow et al. (TOCHI 2010): novices who made several ad prototypes in parallel before feedback beat those who iterated one at a time with feedback after each. Parallel ads won on click-through and expert ratings, were judged more diverse, and their makers gained more self-efficacy [S5].
- Design Galleries (Marks and colleagues, 1997): instead of tuning parameters by hand, show the broadest automatically generated set of perceptually different results. The two hard problems are dispersion (choose inputs whose outputs spread widely) and arrangement (lay them out for browsing) [S8].
- Luminate (Suh et al., CHI 2024; 14 professional writers): the authors argue that chat interfaces push people to settle early on a narrow set of ideas. Their system asks an LLM to generate task-specific nominal and ordinal dimensions with values, then organises outputs along them [S9]. This is morphological analysis with dimensions invented per task.
- For the tool: the lab's farthest-first selection is dispersion [S8]. Luminate supports letting the lab add one or two brief-specific axes (for example "material: ceramic, paper, rubber") beyond the fixed 12 [inferred from S9].

### 1.5 Operators and provocations
- SCAMPER: Substitute, Combine, Adapt, Magnify/Modify, Put to other uses, Eliminate, Rearrange/Reverse. Osborn first suggested the principles; Eberle later arranged them as a mnemonic [S10].
- Oblique Strategies (Eno and Schmidt, 1975): short prompts and axioms printed on cards, made to get past creative blocks [S11].
- For the tool: each SCAMPER verb maps to an axis operation: substitute a value, combine two styles, adapt a trait from another domain (print, architecture, packaging), magnify or minify a dial, eliminate a trait, reverse a pairing such as dark-first to light-first [inferred]. A small deck of provocations can drive the `--wild` setting [inferred].

### 1.6 How studios present directions (safe, stretch, wild)
- I found no peer-reviewed source that establishes "two safe, one wild" as a rule. The practice evidence is Warren's three adjective-led tiles [S2] and the benefit of parallel options [S5].
- Choice research matters here. Simonson (1989): an option gains share when it becomes the compromise in a set, and the effect is stronger when people expect to justify their choice to others [S12]. A person choosing for a team or a client will tend to pick the middle direction [inferred from S12].
- For the tool: put the direction the tool actually recommends in the middle slot, flanked by a safer and a bolder one. Never add a deliberately weak decoy [inferred].

---

## 2. Decomposing a visual style into attributes

### 2.1 Semantic differential and Kansei engineering
- Osgood, Suci and Tannenbaum (1957): people rate a concept on bipolar adjective pairs, and three factors recur: evaluation (good-bad), potency (strong-weak) and activity (active-passive). Scales usually have seven points [S13]. The page also claims cross-cultural universality but cites nothing for it, so I treat that as unverified.
- Kansei engineering (Nagamachi; Schütte's model) describes a product domain from two sides. The semantic space is people's feeling words (Kansei words), derived from semantic differential ratings. The space of properties is a short list of physical attributes that drive the feeling. A synthesis step (regression, QT1, rough sets, fuzzy logic) links the two, so designers can choose properties that support an intended feeling. Mood boards are suggested as input to the domain step [S14].
- Fit with OpenDesigner: `people_say` is the semantic space, the 12 traits are the space of properties, and `engine.py feel` is a hand-built synthesis. Each recorded pick (words in, traits chosen) is training data to improve that mapping over time [inferred].
- Potency and activity are useful dials for non-designers (delicate to bold, calm to lively) [inferred from S13]. Evaluation is not: everyone wants "good".

### 2.2 Validated facets of visual aesthetics
- VisAWI (Moshagen and Thielsch, 2010; seven studies): perceived website aesthetics has four facets under one general factor [S15].
  - Simplicity: clarity, orderliness, homogeneity, grouping, balance.
  - Diversity: visual richness, dynamics, variety, creativity, novelty.
  - Colorfulness: individual colours and their composition.
  - Craftsmanship: designed with skill and care.
- In the same paper, Lavie and Tractinsky's classical aesthetics (clarity, order) correlated highly with Simplicity, and their expressive aesthetics (richness, diversity) with Diversity [S15].
- VisAWI's review table lists the aspects that earlier studies used: motion and effects; balance and symmetry; coherence and craftsmanship; colour; complexity and variety; grouping and order; homogeneity and unity; images, icons and graphics; novelty; proportion; simplicity and density; text and fonts [S15].
- Compared with that list, our axes cover materials and rendering (surface, edge, depth, texture) far better than the literature does. They are missing density or complexity, imagery as its own thing, and proportion or scale. Craftsmanship is a quality, not a style, so it belongs in preflight, not in the axes [inferred].

### 2.3 Brand personality and type
- Aaker (1997): five brand personality dimensions with 15 facets: sincerity, excitement, competence, sophistication and ruggedness [S16]. These describe how a brand feels, not how it looks, so they belong in the semantic space (people's words) and map to several traits at once [inferred].
- Henderson, Giese and Cote (2004): typeface impressions (pleasing, engaging, reassuring, prominent) can be managed through six design dimensions: elaborate, harmony, natural, flourish, weight and compressed [S17]. Weight and width (compressed) are concrete type sub-traits our `type` axis leaves out.
- O'Donovan et al. (2014): 37 font attributes, 31 relative ones gathered by crowd pairwise comparison plus 6 binary ones. The authors started with 36 relative attributes and pruned 5 that correlated highly with others ("masculine" duplicated "strong") [S18]. This is the method to apply to our axes: drop or merge values that always co-occur.

### 2.4 Media, emotion and style labels in image datasets
- BAM (Behance Artistic Media, ICCV 2017; about 65 million images) labels three separate facets: media (3D graphics, comics, oil paint, pen and ink, pencil, vector art, watercolour), emotion (calm, happy, gloomy, scary) and content [S19]. How a picture is made is kept apart from how it feels.
- Karayev et al. (BMVC 2014): 20 curated style labels on about 80K Flickr photos and 25 on about 85K paintings. Deep features trained on object labels still recognised style well [S20]. Style can be learned from examples, which supports measuring new looks from references.
- For the tool: our `ornament` axis mixes media (photo, illustration, 3D) with decoration (squiggles, stickers). BAM supports splitting them [inferred from S19].

---

## 3. Novelty versus familiarity

### 3.1 The evidence
- **MAYA.** Raymond Loewy's "Most Advanced Yet Acceptable", from his 1951 autobiography *Never Leave Well Enough Alone*: push forward, but not past what people will accept [S21].
- **Hekkert, Snelders and van Wieringen (2003).** Across three studies of consumer products, typicality and novelty explained preference jointly and about equally, but suppressed each other. Neither correlated with preference on its own; each became significant once the other was controlled [S22].
  - People liked novelty as long as it did not cost typicality.
  - Expertise did not change the balance (Study 2) [S22].
  - Typicality measured objectively, as average similarity to the rest of the category, gave the same result (Study 3) [S22].
  - A summary of the paper notes that novelty mattered more for sanders and telephones and typicality more for kettles [S23].
- **Thurgood, Hekkert and Blijlevens (2014).** They replicated the joint effect (48 participants; typicality and novelty explained 55% of preference). They proposed that a feeling of safety pushes people toward novelty and risk toward typicality, but their manipulation of safety and risk did not work, so that idea is still untested [S24]. They also report earlier work (Carbon et al.) in which innovative designs gained appreciation after repeated, elaborated evaluation [S24].
- **Tuch et al. (2012).** Website screenshots were rated after 50, 500 or 1000 ms (study 1, 59 participants) and after 17, 33 or 50 ms (study 2) [S25].
  - Visual complexity and prototypicality affected ratings even at 17 ms. Complexity acts first; prototypicality catches up with longer viewing [S25].
  - Low complexity with high prototypicality looked best. Low-prototypicality sites were judged unattractive whether simple or complex [S25].
  - Limits: company websites only, a young sample, passive viewing [S25].
- **Lindgaard et al. (2006).** Appeal ratings after 50 ms matched those after 500 ms (r = .97, as reported by Tuch et al.), and 500 ms matched unlimited viewing (r = .98) [S25, S26]. Lindgaard warned that visitors who are not impressed at first may leave before seeing the offer [S26].
- **Reber, Schwarz and Winkielman (2004).** Aesthetic pleasure rises with processing fluency. Figural goodness, contrast, repetition, symmetry and prototypicality all work by making a stimulus easier to process [S27].
- **Berlyne's inverted U** (pleasure peaks at moderate arousal from complexity and novelty) has mixed support; several studies found a straight line rather than a peak (reviewed in [S25]).
- **Reinecke et al. (2013)**, 450 sites and 548 people: perceived complexity and colourfulness, with age and education, explained about half the variance in appeal after 500 ms. High complexity cost the most appeal; low and medium complexity were liked about equally. People over 45 liked low complexity more, and people with a PhD were most put off by high colourfulness [S28].
- **Reinecke and Gajos (2014)**, 2.4 million ratings from nearly 40,000 people: the most-liked sites had medium-to-high colourfulness and low-to-medium complexity. The peak shifted by group: women liked more colour, more education lowered the taste for colour, Russians preferred less complexity [S29].
  - On age, this larger sample found that people over 41 preferred more complexity, the opposite of the 2013 result. The authors attribute the difference to their more varied, less educated sample [S29].
- **Landwehr, Wentzel and Herrmann (2013)**, cars: typical designs were liked more at low exposure and atypical designs more at high exposure. Real sales data suggested atypical cars may do better in the long run [S30].
- **NN/g on long exposure (2015).** Long exposure to weak signifiers makes users more cautious: they hover, test-click and lean on wording and placement. That extra exploration adds cognitive load, and the habits carry over to other sites [S31].

### 3.2 What this means for how far a style should push
1. **Push the skin, keep the bones typical.** First impressions form in well under a second and punish low prototypicality and high complexity [S25, S26]. Novelty helps only while typicality survives [S22]. So spend novelty on surface, colour, texture, ornament, imagery and type character. Keep layout conventions, navigation placement and interactive signifiers close to the category prototype [inferred from S22, S25, S31]. This matches the lab's existing "bones of A, skin of B" rule and NN/g's view that brutalism works when it stays out of hierarchy and navigation [S46].
2. **Measure novelty against the product's category, not only against the style catalogue.** Hekkert's typicality is distance from the category's centre [S22]. A neo-brutalist accounting tool is far from its category even if it sits close to the named style "neo-brutalism" [inferred].
3. **Complexity is the cheaper lever to get wrong.** High complexity costs more appeal than any other factor measured, and low complexity costs little [S28, S29]. When pushing novelty, hold complexity at low-to-medium [inferred from S28, S29].
4. **Audiences differ, but not in ways safe to stereotype.** Peaks differ by gender, education and country, and the age findings reverse between two large studies [S28, S29]. Experts did not weight novelty differently from non-experts [S22], though NN/g allows that designer and entertainment audiences can accept stranger visuals [S46]. The tool should ask who the audience is and offer a quick first-impression test, rather than assume [inferred].
5. **Daily-use products can afford an unusual identity, not unusual controls.** Atypical designs grow on people with exposure [S30], while weak signifiers get more costly with exposure [S31]. For B2B and enterprise tools: atypical skin is acceptable, signifiers must stay strong [inferred].
6. **High-stakes contexts (money, health) probably favour typicality.** The safety-and-risk idea is plausible but its one test failed [S24], so treat this as a default to confirm, not a finding [inferred].
7. **Repeat exposure before locking a wild direction.** Atypical options are under-rated on first sight [S30, S24]. Show the chosen experimental direction again in a later session before the person commits [inferred].

---

## 4. How new styles emerge and get named today

### 4.1 Where looks are born and named
- **Dribbble.** Neumorphism started as Alexander Plyuto's 2019 Dribbble shot of a banking app. The name came later, coined in a comment on Michal Malewicz's article about the look [S35]. Paul Adams (Intercom, 2013) argued that Dribbble rewards polished surface work that impresses peers and ignores users, business goals and the product around it, and that much of that work looks alike [S34].
- **Aesthetics Wiki.** A community encyclopedia of styles created in 2018; "-core" is its biggest and fastest-growing suffix. The Atlantic counted 125 main -core pages in February 2021, and the count was 158 less than a year later [S36]. Readymag counts 1,075 aesthetics on the wiki in 2026 [S37].
- **Archivists name looks after the fact.** CARI (Consumer Aesthetics Research Institute) builds a visual lexicon of consumer ephemera from the 1970s to now [S38]. Readymag credits archives like CARI with coining or popularising terms such as Frutiger Aero and Y2K [S37]. The names arrive years after the work was made [inferred from S37, which dates a Frutiger Aero example to 2005].
- **Labels help and harm** (Readymag, July 2026, nine designers and researchers interviewed) [S37]:
  - They give clients and designers shared shorthand.
  - Most designers treat them as descriptive, not as a place to start.
  - Rigid label rules narrow a designer's range.
  - Brands adopt popular labels, and the original creators lose control.
  - One label flattens work that has several influences.
- **Collecting tools.** Are.na organises blocks into channels and connects them across people; it is ad-free and member-supported [S39]. Cosmos describes itself as an ad-free inspiration platform with collections, search by keyword, hex colour or visual similarity, AI captions that name the original artist or source, and flags for likely AI-generated images [S40]. Both are good places to watch looks gather before they have names [inferred].
- **Trend reports.** Pinterest Predicts filters two years of search data by volume and growth, normalises for season, adds a modelled trend score and a visual check of trendlines, then narrows about 500,000 qualifying searches to about 50 candidates and about 30 published trends. It claims 8 in 10 came true, which is self-reported [S41].
- **TikTok.** I could not open a reliable source on how TikTok speeds up visual-style cycles, so I make no claim about it.

### 4.2 How fast they date
- Flat design gained traction around 2011 with Microsoft Metro and Windows 8; Apple's homepage held out until about 2013. Long shadows were prominent around 2013 and had declined by the time of NN/g's 2015 article, which treats them as decoration with no job [S42]. That is about two years for a decorative sub-trend.
- Glass returns in cycles: Readymag cites a 2005 Windows Vista wallpaper as Frutiger Aero [S37], glassmorphism appears in Apple's and Microsoft's systems as a "material" [S44], and Apple made Liquid Glass its platform style in 2025 [S45]. A revival roughly every 15 to 20 years fits this sequence, but that is a pattern I see, not a measured cycle [inferred].
- Web layouts have become more alike. Website screenshots from 2003 to 2019 became much more similar after 2007, and the average layout distance between sites fell by over 30%. Designers blamed shared code and libraries, standard colour schemes and mobile support [S32].
- AI site builders may push the same way. Shin et al. (2026) argue that "vibe coding" (making a site by describing it to an LLM) can strengthen homogenisation. They propose "productive friction": deliberate points where creators question default output [S33].

### 4.3 How the tool can keep discovering without copying identity
- Watch where labels form (Aesthetics Wiki, CARI, Are.na, Cosmos, Dribbble, Behance, Pinterest Predicts) and record the label, the date first seen and the communities using it [inferred from S36 to S41].
- Admit a look to the catalogue only when it has a community label used by at least two independent sources and a description on the axes that differs from existing entries. Never admit one creator's or one brand's signature look [inferred; consistent with the project rule that references give structure, never identity].
- Describe the look on the axes from several unrelated examples, never from one source, so the entry captures the shared structure rather than one maker's identity [inferred from S37's point that labels flatten and commercialise creators' work].
- Use productive friction against sameness [S33]: when a direction sits close to the current web default [S32], say so and offer one alternative that departs on at least one skin axis [inferred].

---

## 5. Guardrails: why experimental styles fail, and how to keep the floors

### 5.1 Failure modes, with evidence
| Failure | Evidence |
|---|---|
| Decoration over function | NN/g on Liquid Glass (Oct 2025): translucent controls over busy content lower legibility. Constant animation distracts. Floating controls compete for attention. Targets became cramped. Controls appear and vanish unpredictably [S45]. |
| Weak or missing signifiers | NN/g eyetracking (71 users, 9 sites): weak clickability cues meant about 22% longer tasks and 25% more fixations. The harm shrank only on pages with low density, conventional layout and high-contrast targets [S43]. Long exposure makes it worse [S31]. |
| Effects piled on effects | High visual complexity is the strongest negative on first impressions [S25, S28]. NN/g advises using glass sparingly, with generous blur, mainly for depth and hierarchy [S44]. |
| Novelty for its own sake | NN/g: antidesign (deliberately ugly, disorienting interfaces) works against users. The worst motive is designer boredom. It may suit designer or entertainment audiences only [S46]. |
| Looks hiding problems | The aesthetic-usability effect: in Kurosu and Kashimura's study (252 people, 26 ATM layouts), perceived ease of use tracked beauty more than actual ease. Attractive designs can hide problems during testing [S47]. |
| Illegible type | Thin or unusual fonts may need more contrast than the WCAG numbers suggest. Text over images without enough contrast is a listed failure (F83) [S50]. |
| Motion sickness | Large zooms, spinning, parallax, large multi-direction movement, big page transitions and auto-playing loops can trigger vestibular symptoms. Fades, colour changes and small scale shifts are generally safe [S60]. |
| Flashing (glitch styles) | No more than three flashes in any second, unless the flashing area is small (about 341 x 256 CSS px) [S56]. |
| Low-contrast soft styles | Neumorphism's subtle tone differences produce low contrast, and its shadow-only states can be missed by low-vision users [S35]. |

Not all decoration is waste. Embellished charts were interpreted as accurately as plain ones and remembered better two to three weeks later [S48]. Decoration that carries meaning or memory is allowed; decoration that costs legibility or signifiers is not [inferred from S48, S45].

### 5.2 Keeping the floors while experimenting
- **Text contrast** 4.5:1, or 3:1 for large text (about 24 px regular or 18.5 px bold). Thresholds are not rounded: 4.499:1 fails. Measure against what the text actually sits on, including images [S50]. Level AA [S49].
- **Non-text contrast** 3:1 for control boundaries, states and needed graphics. On a gradient, test the least-contrasting area [S51]. Level AA [S49].
- **Focus visible** (2.4.7, AA) and **focus not obscured** (2.4.11, AA): sticky bars and non-modal overlays must not fully hide the focused item. A blurred or translucent overlay can still fail non-text contrast if it washes out the focus indicator [S52, S49].
- **Focus appearance** (2.4.13, AAA): at least the area of a 2 px outline, with a 3:1 change between focused and unfocused states [S53]. It is AAA, but it is the simplest way to make a ring survive glass, glow and texture [inferred].
- **Targets** at least 24 x 24 CSS px, or spaced so a 24 px circle around each does not touch another target [S54]. Level AA [S49].
- **Motion.** Interaction-triggered motion can be turned off (2.3.3, AAA; technique: `prefers-reduced-motion`) [S55]. Anything that moves on its own for more than 5 seconds needs pause, stop or hide (2.2.2, A) [S57]. Under reduced motion, swap the moving property for a fade with the same timing rather than just deleting it [S60].
- **Transparency.** `prefers-reduced-transparency` is experimental and not Baseline [S58]. It ships in Chrome 118 and later, sits behind a flag in Firefox, and is missing from Safari [S59]. A glass style therefore must pass contrast with no query applied. Use the query as an extra, and also respond to `prefers-contrast` and `forced-colors`, which every major engine supports [S59]. NN/g recommends letting users reduce transparency or increase contrast where possible [S44].

---

## Proposed exploration protocol for the tool

This builds on the existing lab (`style search`, `explore`, `mutate`, `mix`, `define`, 3 to 7 changed traits, farthest-first). New steps are marked NEW.

1. **Frame (NEW).** Before generating, record four facts:
   - the product category;
   - the audience;
   - which screens are core UI and which are marketing;
   - whether the context is high-stakes (money, health, safety).

   These set the novelty budget (step 3). Framing is the first role of a mood board [S4].
2. **Collect words, not names.**
   - Ask for two or three feel words, one dislike, and one tension pair (for example "calm but loud", "luxury but eco"). Tension pairs are Lucero's paradoxing [S4].
   - Map the words to traits through the semantic space, as Kansei engineering does [S14]. Potency and activity become dials such as weight and energy [S13]. Brand personality words such as sincere or rugged are expanded into several traits [S16] [inferred].
3. **Set a novelty budget per layer (NEW).**
   - Split the axes into bones and skin. Bones are layout, density, type structure and signifier edges. Skin is surface, depth, colour, texture, ornament, imagery and motion character.
   - Count changed traits two ways: against the nearest named style (as now) and against a prototype of the product category, for example the centre of a set of Mobbin screens from that category [S22, S25].
   - Suggested defaults [inferred; the evidence gives a direction, not these numbers]:
     - core UI for daily-use or B2B tools: bones stay typical, 2 to 4 skin changes;
     - consumer apps: up to 5 changes, with at most 1 in the bones;
     - marketing and launch pages: 4 to 7 changes;
     - `--wild`, or designer and entertainment audiences [S46]: up to 10 changes.
4. **Build the box and check consistency (NEW).**
   - Treat the axes as a Zwicky box [S1].
   - Let the generator add up to two dimensions specific to this brief, as Luminate does [S9].
   - Replace the repairs table with a full pairwise cross-consistency matrix (fine, repair or forbidden) [S1]. Forbidden pairs are the ones that cannot meet the floors.
5. **Generate in parallel with named operators.**
   - Blend: bones of A, skin of B. Name the shared anchor and the emergent property [S6, S7].
   - Mutate with SCAMPER verbs [S10].
   - For wild directions, draw one provocation card [S11].
   - Keep the outputs dispersed, farthest-first [S8], and generate them all before asking for any feedback [S5].
6. **Show three or four directions as tiles, at real size.**
   - Make them style tiles or element collages with real components, not full pages [S2, S3].
   - Label each as safe, recommended or bold. Put the recommendation in the middle position [S12].
   - Show each in light and dark, with reduced motion and reduced transparency applied.
7. **Ask for reactions trait by trait (NEW).** For each tile, ask keep, change or drop for its loud traits. Recombine the answers into the next round, as Warren's client did [S2]. Then iterate serially from there.
8. **Gate on the floors and on complexity.**
   - Measure text contrast against the worst pixel behind it [S50, S51].
   - Check the focus ring [S52, S53], target size [S54], motion [S55, S57, S60], flashes [S56], and transparency with and without the query [S58, S59].
   - NEW: add a measured visual-complexity score of the rendered tile, as Reinecke models it [S28], next to the loud-trait count. Warn when complexity is high, because it costs the most appeal [S28, S29].
   - NEW: add a craftsmanship check for alignment and spacing consistency, because VisAWI treats craft as its own facet whatever the style [S15].
9. **Run a first-impression test (NEW, optional).** Flash each finalist for half a second next to a typical design from the category. Ask "appealing?" and "trustworthy?" [S25, S26]. This is a check against the person's own taste only; real audience tests are better [S29].
10. **Repeat exposure before locking (NEW).** For any direction past the safe slot, show it again at the start of the next session before recording it as chosen [S30, S24].
11. **Name, save and record its origin.**
    - The person names it. Store the trait vector, their words, the blend or mutation it came from, and a "tool-coined" flag. Use no brand names.
    - Following Aesthetics-Wiki practice, a tool-made name is marked as coined, not presented as a known style [inferred].
12. **Discover new styles continuously, outside sessions (NEW).**
    - Watch Aesthetics Wiki, CARI, Are.na, Cosmos, Dribbble, Behance and Pinterest Predicts [S36 to S41].
    - Admit a style when at least two independent sources use the label and it differs from catalogue entries on at least 3 axes [inferred].
    - Record the date first seen, and review each trend style after about 18 months, since decorative sub-trends have lasted about two years [S42] [inferred].
    - Apply productive friction against the homogeneous default [S32, S33].

---

## Axis changes we should make

| # | Change | Why | Confidence |
|---|---|---|---|
| 1 | **Add `density`** (airy, balanced, dense) and remove `dense` and `minimal` from `layout`. Link it to the existing Density dial. | Complexity is the strongest first-impression factor [S25, S28, S29]. Simplicity and density are a core aesthetic facet [S15]. `layout` currently mixes structure with amount. | High |
| 2 | **Split `ornament` into `imagery`** (none, photo, illustration, 3d, icon-led, type-only) **and `ornament`** (none, geometric-shapes, squiggles, stickers, ascii, ornamental, pattern). | BAM keeps how a picture is made apart from what decorates the page [S19]. Images and icons are their own aspect in the aesthetics literature [S15]. | Medium |
| 3 | **Split `color` into `palette`** (monochrome, neutral-accent, tonal, duotone, spot-inks, multi, rainbow) **and `chroma`** (muted, pastel, normal, vivid, neon). Move `metallic` to `surface`. Leave `earthy` to the Warmth dial and hue. | The current list mixes palette structure, saturation and material. Saturation drives perceived colourfulness, which is the variable that predicts appeal [S29]. Each axis should hold one kind of thing [S18]. | Medium |
| 4 | **Remove overlaps.** Keep `glow` in `depth` only. Keep `paper` in `texture` only and drop `textured` from `surface`. Express pixel shape plus pixel type as a consistency rule, not two independent picks. | Values that always co-occur should be merged or pruned [S18]. Overlaps also double-count loud traits [inferred]. | High |
| 5 | **Split `motion` into character and techniques.** Character: still, subtle, springy, bouncy, stepped, glitchy. Techniques as risk flags: parallax, kinetic-type, scroll-linked, autoplay-loop, flashing. | Parallax, large zooms and autoplay loops are vestibular triggers with their own WCAG rules; character is not [S55, S57, S56, S60]. | High |
| 6 | **Add `scale`** (even, moderate, dramatic): the size and weight jump between display and body text. Add **type sub-traits `weight` and `width`**. | Weight and compression are validated typeface impression dimensions [S17]. Proportion is a recurring aesthetic aspect [S15]. Many named looks (editorial, Swiss, brutalist) differ mainly in scale [inferred]. | Medium |
| 7 | **Clarify `contrast` as `tonal-range`** (how far apart lights and darks sit in the decoration). State that it never lowers text or control contrast. | The name invites confusion with the accessibility floors [S50, S51] [inferred]. | Medium |
| 8 | **Turn `theme` from a trait into a default.** Values: light-first, dark-first. Both modes are always built. | The engine already builds both. A style that only works in one mode is a constraint to record, not a look [inferred]. | Medium |
| 9 | **Add a `layer` tag to every axis** (bones or skin) so the novelty budget can be spent on skin. | Novelty pays only while typicality survives [S22]. Prototypicality drives first impressions [S25]. Brutalism works in visuals, not in navigation [S46]. Signifiers need to stay strong [S31, S43]. | High |
| 10 | **Add two measured, derived values (not chosen by the person).** `novelty`: distance from the category prototype. `complexity`: score of the rendered preview. | Typicality is distance from the category centre [S22]. Complexity can be computed from a screenshot [S28]. | Medium |
| 11 | **Keep feelings out of the axes.** Map Osgood's potency and activity and Aaker's personality words to traits through the semantic-space lexicon. Do not add axes for them. | Kansei separates feeling words from product properties and links them in a synthesis step [S14]. | High |

Axes the evidence supports as they are: `surface`, `edge`, `depth`, `shape` and `texture`. These rendering axes are this tool's strength. The academic facets [S15] are too coarse to describe materials.

---

## Sources (all opened during this research)

1. [S1] Ritchey, T. "General Morphological Analysis." Swedish Morphological Society. https://www.swemorph.com/ma.html
2. [S2] Warren, S. "Style Tiles and How They Work." A List Apart, 27 March 2012. https://alistapart.com/article/style-tiles-and-how-they-work/
3. [S3] Mall, D. "RIF Element Collages." 13 November 2012. https://v3.danmall.com/articles/rif-element-collages
4. [S4] Lucero, A. "Framing, Aligning, Paradoxing, Abstracting, and Directing: How Design Mood Boards Work." DIS 2012, pp. 438-447 (full text). https://users.aalto.fi/~luceroa1/publications/2012/lucero12_moodboards.pdf
5. [S5] Dow, S. et al. "Parallel Prototyping Leads to Better Design Results, More Divergence, and Increased Self-Efficacy." ACM TOCHI 17(4), 2010 (abstract via Crossref). https://doi.org/10.1145/1879831.1879836
6. [S6] Fauconnier, G. and Turner, M. "Conceptual Integration Networks." Cognitive Science 22(2), 1998 (abstract via Crossref). https://doi.org/10.1207/s15516709cog2202_1
7. [S7] Chilton, L., Petridis, S. and Agrawala, M. "VisiBlends: A Flexible Workflow for Visual Blends." CHI 2019 (full text). https://www.cs.columbia.edu/~chilton/web/my_publications/VisiBlends_CHI2019.pdf
8. [S8] Andalman, B., Ryall, K., Ruml, W., Marks, J. and Shieber, S. "Design Gallery Browsers Based on 2D and 3D Graph Drawing." MERL TR97-12, 1997 (describes the Design Galleries approach). https://www.merl.com/publications/docs/TR97-12.pdf
9. [S9] Suh, S. et al. "Luminate: Structured Generation and Exploration of Design Space with Large Language Models for Human-AI Co-Creation." CHI 2024. https://arxiv.org/abs/2310.12953 (method from https://arxiv.org/html/2310.12953v3)
10. [S10] Serrat, O. "The SCAMPER Technique." Asian Development Bank Knowledge Solutions, February 2009. https://www.adb.org/publications/scamper-technique
11. [S11] Socks Studio. "'Before and After Science' and the Eno/Schmidt collaboration." 20 September 2013. https://socks-studio.com/2013/09/20/before-and-after-sciences-and-the-enoschmidt-collaboration/
12. [S12] Simonson, I. "Choice Based on Reasons: The Case of Attraction and Compromise Effects." Journal of Consumer Research 16(2), 1989 (abstract). https://academic.oup.com/jcr/article-abstract/16/2/158/1795321
13. [S13] Simply Psychology. "Semantic Differential Scale" (on Osgood, Suci and Tannenbaum, 1957). Secondary source. https://www.simplypsychology.org/semantic-differential.html
14. [S14] Schütte, S. and Marco-Almagro, L. "Development and Application of Online Tools for Kansei Engineering Evaluations." KEER 2018 (full text). https://ep.liu.se/ecp/146/003/ecp18146003.pdf
15. [S15] Moshagen, M. and Thielsch, M. T. "Facets of Visual Aesthetics." International Journal of Human-Computer Studies 68(10), 2010 (author manuscript). https://www.uni-muenster.de/OWMS/uploads/drafts_thielsch/pdf/moshagen_2010.pdf
16. [S16] Aaker, J. L. "Dimensions of Brand Personality." Journal of Marketing Research 34(3), 1997 (full text). https://gwern.net/doc/economics/1997-aaker.pdf
17. [S17] Henderson, P. W., Giese, J. L. and Cote, J. A. "Impression Management Using Typeface Design." Journal of Marketing 68(4), 2004 (abstract via Crossref). https://doi.org/10.1509/jmkg.68.4.60.42736
18. [S18] O'Donovan, P., Lībeks, J., Agarwala, A. and Hertzmann, A. "Exploratory Font Selection Using Crowdsourced Attributes." ACM TOG 33(4), 2014 (full text). https://www.dgp.toronto.edu/~donovan/font/fontSelection.pdf
19. [S19] Wilber, M. et al. "BAM! The Behance Artistic Media Dataset for Recognition Beyond Photography." ICCV 2017 (full text). https://openaccess.thecvf.com/content_ICCV_2017/papers/Wilber_BAM_The_Behance_ICCV_2017_paper.pdf
20. [S20] Karayev, S. et al. "Recognizing Image Style." BMVC 2014 (abstract). https://arxiv.org/abs/1311.3715
21. [S21] Interaction Design Foundation. "What is The MAYA Principle?" (cites Loewy, *Never Leave Well Enough Alone*, 1951). https://ixdf.org/literature/topics/maya-principle
22. [S22] Hekkert, P., Snelders, D. and van Wieringen, P. C. W. "'Most advanced, yet acceptable': Typicality and novelty as joint predictors of aesthetic preference in industrial design." British Journal of Psychology 94(1), 2003 (PubMed abstract). https://pubmed.ncbi.nlm.nih.gov/12648393/
23. [S23] Davies, J. CogSci Summaries: Hekkert, Snelders and van Wieringen (2003). https://www.jimdavies.org/summaries/HekkertSneldersVanwieringen2003.html
24. [S24] Thurgood, C., Hekkert, P. and Blijlevens, J. "The Joint Effect of Typicality and Novelty on Aesthetic Pleasure for Product Designs: Influences of Safety and Risk." IAEA Congress 2014 (full text). https://opus.lib.uts.edu.au/bitstream/10453/36796/4/The%20joint%20effect%20of%20typicality%20and%20novelty%20on%20aesthetic%20pleasure%20for%20product%20designs.pdf
25. [S25] Tuch, A. N., Presslaber, E. E., Stöcklin, M., Opwis, K. and Bargas-Avila, J. A. "The role of visual complexity and prototypicality regarding first impression of websites." IJHCS 70(11), 2012 (author preprint). https://research.google.com/pubs/archive/38315.pdf
26. [S26] Nature News. "Web users judge sites in the blink of an eye" (on Lindgaard et al. 2006, Behaviour & Information Technology 25(2), doi:10.1080/01449290500330448), 13 January 2006. https://www.nature.com/news/2006/060109/full/news060109-13.html
27. [S27] Reber, R., Schwarz, N. and Winkielman, P. "Processing fluency and aesthetic pleasure." Personality and Social Psychology Review 8(4), 2004 (PubMed abstract). https://pubmed.ncbi.nlm.nih.gov/15582859/
28. [S28] Reinecke, K. et al. "Predicting Users' First Impressions of Website Aesthetics With a Quantification of Perceived Visual Complexity and Colorfulness." CHI 2013 (full text). https://kgajos.seas.harvard.edu/papers/reinecke13aesthetics.pdf
29. [S29] Reinecke, K. and Gajos, K. Z. "Quantifying Visual Preferences Around the World." CHI 2014 (full text). https://iis.seas.harvard.edu/papers/reinecke14visual.pdf
30. [S30] Landwehr, J. R., Wentzel, D. and Herrmann, A. "Product Design for the Long Run: Consumer Responses to Typical and Atypical Designs at Different Stages of Exposure." Journal of Marketing 77(5), 2013 (abstract via Crossref). https://doi.org/10.1509/jm.11.0286
31. [S31] Moran, K. "Long-Term Exposure to Flat Design: How the Trend Slowly Makes Users Less Efficient." NN/g, 8 November 2015. https://www.nngroup.com/articles/flat-design-long-exposure/
32. [S32] Goree, S., Doosti, B., Crandall, D. and Su, N. M. "Investigating the Homogenization of Web Design: A Mixed-Methods Approach." CHI 2021 (abstract via Semantic Scholar). https://doi.org/10.1145/3411764.3445156
33. [S33] Shin, D. et al. "Interrogating Design Homogenization in Web Vibe Coding." arXiv, March 2026. https://arxiv.org/abs/2603.13036
34. [S34] Adams, P. "The Dribbblisation of Design." Inside Intercom, 18 September 2013. https://www.intercom.com/blog/the-dribbblisation-of-design/
35. [S35] Built In. "What Is Neumorphism and Why Should Designers Care?" (updated 12 December 2023). https://builtin.com/design-ux/neumorphism
36. [S36] Friedman, N. "The Ever-More-Common '-Core'." Visual Thesaurus, 20 January 2022. https://www.visualthesaurus.com/cm/candlepwr/the-ever-more-common-core/
37. [S37] Readymag. "How aesthetic labels are changing creative work." 8 July 2026. https://blog.readymag.com/aesthetic-labels/
38. [S38] Consumer Aesthetics Research Institute (CARI), home page. https://cari.institute/
39. [S39] Are.na, About. https://www.are.na/about
40. [S40] Cosmos, llms.txt (company self-description). https://www.cosmos.so/llms.txt
41. [S41] Pinterest. "Pinterest Predicts: The science behind our future trends." https://business.pinterest.com/blog/how-we-forecast-trends-pinterest-predicts/
42. [S42] Moran, K. "Flat Design: Its Origins, Its Problems, and Why Flat 2.0 Is Better for Users." NN/g, 27 September 2015. https://www.nngroup.com/articles/flat-design/
43. [S43] Moran, K. "Flat UI Elements Attract Less Attention and Cause Uncertainty." NN/g, 3 September 2017. https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
44. [S44] Brown, M. "Glassmorphism: Definition and Best Practices." NN/g, 7 June 2024. https://www.nngroup.com/articles/glassmorphism/
45. [S45] Budiu, R. "Liquid Glass Is Cracked, and Usability Suffers in iOS 26." NN/g, 10 October 2025. https://www.nngroup.com/articles/liquid-glass/
46. [S46] Moran, K. "Brutalism and Antidesign." NN/g, 5 November 2017. https://www.nngroup.com/articles/brutalism-antidesign/
47. [S47] Moran, K. "The Aesthetic-Usability Effect." NN/g (2024 version). https://www.nngroup.com/articles/aesthetic-usability-effect/
48. [S48] Bateman, S. et al. "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." CHI 2010 (full text). https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf
49. [S49] W3C. Web Content Accessibility Guidelines (WCAG) 2.2 (success criterion levels). https://www.w3.org/TR/WCAG22/
50. [S50] W3C. Understanding SC 1.4.3 Contrast (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
51. [S51] W3C. Understanding SC 1.4.11 Non-text Contrast. https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
52. [S52] W3C. Understanding SC 2.4.11 Focus Not Obscured (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
53. [S53] W3C. Understanding SC 2.4.13 Focus Appearance. https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
54. [S54] W3C. Understanding SC 2.5.8 Target Size (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
55. [S55] W3C. Understanding SC 2.3.3 Animation from Interactions. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
56. [S56] W3C. Understanding SC 2.3.1 Three Flashes or Below Threshold. https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
57. [S57] W3C. Understanding SC 2.2.2 Pause, Stop, Hide. https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
58. [S58] MDN. "prefers-reduced-transparency." https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency
59. [S59] MDN browser-compat-data, `css/at-rules/media.json` (support for prefers-reduced-transparency, prefers-reduced-motion, prefers-contrast, forced-colors). https://github.com/mdn/browser-compat-data/blob/main/css/at-rules/media.json
60. [S60] Head, V. "Designing With Reduced Motion For Motion Sensitivities." Smashing Magazine, September 2020. https://www.smashingmagazine.com/2020/09/design-reduced-motion-sensitivities/

### Sources looked for but not used
- Imaz and Benyon, *Designing with Blends* (MIT Press, 2007): only catalogue records could be opened. Not cited.
- Lindgaard et al. 2006 full text: the publisher blocked access. The numbers come from Tuch et al.'s summary [S25] and Nature's report [S26].
- Lavie and Tractinsky 2004: cited only as described in [S15].
- No reliable, openable source on TikTok trend speed was found, so the file makes no claim about it.
