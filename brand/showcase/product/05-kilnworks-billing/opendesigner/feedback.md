# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
sketch called the burnt orange #c24e14 'a brown' (DESIGN.md and sketch output). Repeat of the data-table finding; the owner's rule bans brown, so this label misleads.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20sketch%20called%20the%20burnt%20orange%20%23c24e14%20%27a%20brown%27%20%28DESIGN.md%20and%20sketch...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Asketch%20called%20the%20burnt%20orange%20%23c24e14%20%27a%20brown%27%20%28DESIGN.md%20and%20sketch%20output%29.%20Repeat%20of%20the%20data-table%20finding%3B%20the%20owner%27s%20rule%20bans%20brown%2C%20so%20this%20label%20misleads.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
No row-height tokens (P2) and no separator role lighter than border.subtle (P8): border.subtle is neutral 6 (#cfd2d8, about 1.5:1), too heavy for 36px row hairlines. All three product pieces alias neutral 4 and 5 by hand and set --row: 36px.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20No%20row-height%20tokens%20%28P2%29%20and%20no%20separator%20role%20lighter%20than%20border.su...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANo%20row-height%20tokens%20%28P2%29%20and%20no%20separator%20role%20lighter%20than%20border.subtle%20%28P8%29%3A%20border.subtle%20is%20neutral%206%20%28%23cfd2d8%2C%20about%201.5%3A1%29%2C%20too%20heavy%20for%2036px%20row%20hairlines.%20All%20three%20product%20pieces%20alias%20neutral%204%20and%205%20by%20hand%20and%20set%20--row%3A%2036px.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-003 · 2026-10-14 · idea
The P1 dense work-tool profile took 10 manual commands per piece (roundness 42, depth 10, expression 25, weightCount 3, numericStyles, Q-color-19 brand-gray, focusColor, faces). After them the engine gave exactly the evidence values (6/8/12 corners, 400/500/600, tabular numeric styles). Make it the default for --audience dense.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bidea%5D%20The%20P1%20dense%20work-tool%20profile%20took%2010%20manual%20commands%20per%20piece%20%28roun...&body=%2A%2AKind%3A%2A%2A%20idea%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AThe%20P1%20dense%20work-tool%20profile%20took%2010%20manual%20commands%20per%20piece%20%28roundness%2042%2C%20depth%2010%2C%20expression%2025%2C%20weightCount%203%2C%20numericStyles%2C%20Q-color-19%20brand-gray%2C%20focusColor%2C%20faces%29.%20After%20them%20the%20engine%20gave%20exactly%20the%20evidence%20values%20%286/8/12%20corners%2C%20400/500/600%2C%20tabular%20numeric%20styles%29.%20Make%20it%20the%20default%20for%20--audience%20dense.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=enhancement%2Cfrom-engine)

## F-004 · 2026-10-14 · gap
Feel word 'precise' is unknown (also 'quiet' maps to deferential only). P10 asks for precise, efficient, dense, quiet, trustworthy.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Feel%20word%20%27precise%27%20is%20unknown%20%28also%20%27quiet%27%20maps%20to%20deferential%20only%29...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AFeel%20word%20%27precise%27%20is%20unknown%20%28also%20%27quiet%27%20maps%20to%20deferential%20only%29.%20P10%20asks%20for%20precise%2C%20efficient%2C%20dense%2C%20quiet%2C%20trustworthy.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)
