# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
raw.monoFace accepts '=textFace' (as displayFace does) but writes it into tokens.css literally: --ds-font-family-mono: =textFace, ui-monospace, ... which is invalid CSS. Either resolve the reference like displayFace or refuse it.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20raw.monoFace%20accepts%20%27%3DtextFace%27%20%28as%20displayFace%20does%29%20but%20writes%20it%20i...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Araw.monoFace%20accepts%20%27%3DtextFace%27%20%28as%20displayFace%20does%29%20but%20writes%20it%20into%20tokens.css%20literally%3A%20--ds-font-family-mono%3A%20%3DtextFace%2C%20ui-monospace%2C%20...%20which%20is%20invalid%20CSS.%20Either%20resolve%20the%20reference%20like%20displayFace%20or%20refuse%20it.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
CRM record (dense): 'focused, trustworthy' with --audience dense resolved roundness 0 and two weights; P1 profile (6/8/12 corners, borders, weight 500 labels, tabular digits) set by hand (product-ui.md P1).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20CRM%20record%20%28dense%29%3A%20%27focused%2C%20trustworthy%27%20with%20--audience%20dense%20resol...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ACRM%20record%20%28dense%29%3A%20%27focused%2C%20trustworthy%27%20with%20--audience%20dense%20resolved%20roundness%200%20and%20two%20weights%3B%20P1%20profile%20%286/8/12%20corners%2C%20borders%2C%20weight%20500%20labels%2C%20tabular%20digits%29%20set%20by%20hand%20%28product-ui.md%20P1%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-003 · 2026-10-14 · gap
No key-value row token for record detail panels (used 34 px) and no inline-edit field state (focused input inside a key-value row with a focus halo); the halo color was taken from accent ramp step 4 by hand.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20No%20key-value%20row%20token%20for%20record%20detail%20panels%20%28used%2034%20px%29%20and%20no%20in...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANo%20key-value%20row%20token%20for%20record%20detail%20panels%20%28used%2034%20px%29%20and%20no%20inline-edit%20field%20state%20%28focused%20input%20inside%20a%20key-value%20row%20with%20a%20focus%20halo%29%3B%20the%20halo%20color%20was%20taken%20from%20accent%20ramp%20step%204%20by%20hand.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-004 · 2026-10-14 · gap
Command palette has no tokens: width, offset from top, row height, keycap style, scrim blur. The overlay scrim token exists but backdrop blur does not (product-ui.md 2.7).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Command%20palette%20has%20no%20tokens%3A%20width%2C%20offset%20from%20top%2C%20row%20height%2C%20key...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ACommand%20palette%20has%20no%20tokens%3A%20width%2C%20offset%20from%20top%2C%20row%20height%2C%20keycap%20style%2C%20scrim%20blur.%20The%20overlay%20scrim%20token%20exists%20but%20backdrop%20blur%20does%20not%20%28product-ui.md%202.7%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)
