# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
sketch --theme light-only is refused by STD-visual-details-24, and the suggested fix (standard override) fails with 'no state' until you run init first. A single-theme marketing page needs init, override, then sketch: three commands and no hint of the order.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20sketch%20--theme%20light-only%20is%20refused%20by%20STD-visual-details-24%2C%20and%20the...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Asketch%20--theme%20light-only%20is%20refused%20by%20STD-visual-details-24%2C%20and%20the%20suggested%20fix%20%28standard%20override%29%20fails%20with%20%27no%20state%27%20until%20you%20run%20init%20first.%20A%20single-theme%20marketing%20page%20needs%20init%2C%20override%2C%20then%20sketch%3A%20three%20commands%20and%20no%20hint%20of%20the%20order.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
No discoverable way to set typefaces: 'set textFace X' fails ('not a token path'); the working form is set raw.textFace '"Figtree"' (JSON-quoted), found only by reading engine.py. sketch has no --text-face/--display-face flags.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20No%20discoverable%20way%20to%20set%20typefaces%3A%20%27set%20textFace%20X%27%20fails%20%28%27not%20a%20t...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANo%20discoverable%20way%20to%20set%20typefaces%3A%20%27set%20textFace%20X%27%20fails%20%28%27not%20a%20token%20path%27%29%3B%20the%20working%20form%20is%20set%20raw.textFace%20%27%22Figtree%22%27%20%28JSON-quoted%29%2C%20found%20only%20by%20reading%20engine.py.%20sketch%20has%20no%20--text-face/--display-face%20flags.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-003 · 2026-10-14 · confusing
Feel word 'tidy' maps to minimal and raises a playful-vs-minimal macro conflict. 'set raw.feel' is accepted but changes nothing; the fix is 'set macros [...]', which no doc mentions.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bconfusing%5D%20Feel%20word%20%27tidy%27%20maps%20to%20minimal%20and%20raises%20a%20playful-vs-minimal%20macro...&body=%2A%2AKind%3A%2A%2A%20confusing%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AFeel%20word%20%27tidy%27%20maps%20to%20minimal%20and%20raises%20a%20playful-vs-minimal%20macro%20conflict.%20%27set%20raw.feel%27%20is%20accepted%20but%20changes%20nothing%3B%20the%20fix%20is%20%27set%20macros%20%5B...%5D%27%2C%20which%20no%20doc%20mentions.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=confusing%2Cfrom-engine)

## F-004 · 2026-10-14 · gap
OPEN_FONTS is a short allowlist: Fredoka (SIL OFL on Google Fonts) is reported as a 'Licence risk' in DESIGN.md. Any Google Fonts family is OFL/Apache; the engine could accept a 'google-fonts' licence source.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20OPEN_FONTS%20is%20a%20short%20allowlist%3A%20Fredoka%20%28SIL%20OFL%20on%20Google%20Fonts%29%20is%20...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AOPEN_FONTS%20is%20a%20short%20allowlist%3A%20Fredoka%20%28SIL%20OFL%20on%20Google%20Fonts%29%20is%20reported%20as%20a%20%27Licence%20risk%27%20in%20DESIGN.md.%20Any%20Google%20Fonts%20family%20is%20OFL/Apache%3B%20the%20engine%20could%20accept%20a%20%27google-fonts%27%20licence%20source.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-005 · 2026-10-14 · bug
Weight tokens ignore the face's real range: energy 75 gives font.weight.display 850 but Fredoka stops at 700, so the token silently renders as 700.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20Weight%20tokens%20ignore%20the%20face%27s%20real%20range%3A%20energy%2075%20gives%20font.weigh...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AWeight%20tokens%20ignore%20the%20face%27s%20real%20range%3A%20energy%2075%20gives%20font.weight.display%20850%20but%20Fredoka%20stops%20at%20700%2C%20so%20the%20token%20silently%20renders%20as%20700.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-006 · 2026-10-14 · gap
Type scale tops out at display-sm 90px even with surfaces 'landing page:persuade' and expression 85. Hero headlines on 1440px want 120-160px; there is no display-lg/xl step or a 'hero' reach option.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Type%20scale%20tops%20out%20at%20display-sm%2090px%20even%20with%20surfaces%20%27landing%20pag...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AType%20scale%20tops%20out%20at%20display-sm%2090px%20even%20with%20surfaces%20%27landing%20page%3Apersuade%27%20and%20expression%2085.%20Hero%20headlines%20on%201440px%20want%20120-160px%3B%20there%20is%20no%20display-lg/xl%20step%20or%20a%20%27hero%27%20reach%20option.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-007 · 2026-10-14 · gap
Yellow tints lose all chroma: raw.secondaryColors #FFC83D gives accent3 steps 3-7 #f3ebd9..#e2c68b (tan, not butter). A candy pastel palette needs high-chroma light steps for yellows; the ramp caps tint chroma the same for every hue.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Yellow%20tints%20lose%20all%20chroma%3A%20raw.secondaryColors%20%23FFC83D%20gives%20accent...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AYellow%20tints%20lose%20all%20chroma%3A%20raw.secondaryColors%20%23FFC83D%20gives%20accent3%20steps%203-7%20%23f3ebd9..%23e2c68b%20%28tan%2C%20not%20butter%29.%20A%20candy%20pastel%20palette%20needs%20high-chroma%20light%20steps%20for%20yellows%3B%20the%20ramp%20caps%20tint%20chroma%20the%20same%20for%20every%20hue.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-008 · 2026-10-14 · bug
engine.py review suggests tokens by numeric coincidence: 'height: 40px' -> space-40 (should be size-control-sm), 'box-shadow: inset 0 0 0 2px' (a border) -> elevation-raised, an organic blob 'border-radius: 280px' -> radius-overlay 32px.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20engine.py%20review%20suggests%20tokens%20by%20numeric%20coincidence%3A%20%27height%3A%2040px...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Aengine.py%20review%20suggests%20tokens%20by%20numeric%20coincidence%3A%20%27height%3A%2040px%27%20-%3E%20space-40%20%28should%20be%20size-control-sm%29%2C%20%27box-shadow%3A%20inset%200%200%200%202px%27%20%28a%20border%29%20-%3E%20elevation-raised%2C%20an%20organic%20blob%20%27border-radius%3A%20280px%27%20-%3E%20radius-overlay%2032px.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-009 · 2026-10-14 · idea
Shadows are always neutral (color.shadow.key from the neutral ramp). Playful/candy systems with colorfulness 85 and depth 70 want a tinted shadow option (brand-hued key shadow).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bidea%5D%20Shadows%20are%20always%20neutral%20%28color.shadow.key%20from%20the%20neutral%20ramp%29.%20P...&body=%2A%2AKind%3A%2A%2A%20idea%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AShadows%20are%20always%20neutral%20%28color.shadow.key%20from%20the%20neutral%20ramp%29.%20Playful/candy%20systems%20with%20colorfulness%2085%20and%20depth%2070%20want%20a%20tinted%20shadow%20option%20%28brand-hued%20key%20shadow%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=enhancement%2Cfrom-engine)

## F-010 · 2026-10-14 · bug
preflight.py html (M9) reports 'font is used but has no @font-face' as an ERROR for faces loaded with a Google Fonts <link> stylesheet, which the showcase brief allows. It should read linked font CSS (or at least downgrade to a warning when fonts.googleapis.com is linked).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20preflight.py%20html%20%28M9%29%20reports%20%27font%20is%20used%20but%20has%20no%20%40font-face%27%20as...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Apreflight.py%20html%20%28M9%29%20reports%20%27font%20is%20used%20but%20has%20no%20%40font-face%27%20as%20an%20ERROR%20for%20faces%20loaded%20with%20a%20Google%20Fonts%20%3Clink%3E%20stylesheet%2C%20which%20the%20showcase%20brief%20allows.%20It%20should%20read%20linked%20font%20CSS%20%28or%20at%20least%20downgrade%20to%20a%20warning%20when%20fonts.googleapis.com%20is%20linked%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)
