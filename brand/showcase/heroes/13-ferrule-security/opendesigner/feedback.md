# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
Density modes do not apply on <html> (see heroes/12 feedback): the later ':root, [data-density="compact"]' block wins; set data-density on <body>.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20Density%20modes%20do%20not%20apply%20on%20%3Chtml%3E%20%28see%20heroes/12%20feedback%29%3A%20the%20lat...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ADensity%20modes%20do%20not%20apply%20on%20%3Chtml%3E%20%28see%20heroes/12%20feedback%29%3A%20the%20later%20%27%3Aroot%2C%20%5Bdata-density%3D%22compact%22%5D%27%20block%20wins%3B%20set%20data-density%20on%20%3Cbody%3E.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
No 'start from an existing system' path for a product's marketing page; copied the product's state by hand and picked Q-brand-06 two-sets (see heroes/12 feedback).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20No%20%27start%20from%20an%20existing%20system%27%20path%20for%20a%20product%27s%20marketing%20page...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANo%20%27start%20from%20an%20existing%20system%27%20path%20for%20a%20product%27s%20marketing%20page%3B%20copied%20the%20product%27s%20state%20by%20hand%20and%20picked%20Q-brand-06%20two-sets%20%28see%20heroes/12%20feedback%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-003 · 2026-10-15 · idea
Aligning marketing type to an embedded product needs the product's geometry: I measured column x positions with Playwright and converted by hand ((x + cell padding) x scale + margin). A 'measure this element inside the embed' helper (brand/tools or the review skill's probe) would make it repeatable.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bidea%5D%20Aligning%20marketing%20type%20to%20an%20embedded%20product%20needs%20the%20product%27s%20geo...&body=%2A%2AKind%3A%2A%2A%20idea%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AAligning%20marketing%20type%20to%20an%20embedded%20product%20needs%20the%20product%27s%20geometry%3A%20I%20measured%20column%20x%20positions%20with%20Playwright%20and%20converted%20by%20hand%20%28%28x%20%2B%20cell%20padding%29%20x%20scale%20%2B%20margin%29.%20A%20%27measure%20this%20element%20inside%20the%20embed%27%20helper%20%28brand/tools%20or%20the%20review%20skill%27s%20probe%29%20would%20make%20it%20repeatable.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=enhancement%2Cfrom-engine)
