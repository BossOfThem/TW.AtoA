# Decision — Round 7: Solo Campaign deep-dive (Accepted)

**Date:** 2026-05-04 (Round 7, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md), [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md) (narrows Send-Creeps Solo variant), CONCEPT.md §-new "Game modes: Solo Campaign", Follow-up #13 numbers (per-mission cost shape).

---

## Ratified (4 PM Recommended picks)

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Macro-arc | **Multi-mission saga** — ~12-20 missions, each its own R1-R30 match on hand-authored maps. Narrative thread between missions. Commander/civ/auxiliary-slot unlocks progress as saga advances. Replayable per (k). |
| 2 | Lane topology | **Single lane, map-shaped path complexity** — one creep path; path shape (curves, chokes, splits-that-rejoin) IS the map design. Hex placement preserved. |
| 3 | (k) surfacing | **Per-mission (k) selector at mission start** — player picks Easy/Hard/Hardcore per mission. Hardcore unlocks on mission completion at Hard. Replay at higher tiers for cosmetic/lore unlocks. |
| 4 | Auxiliary slots in Solo | **Universal slots only** — Targeting Override, Build-queue, Tower-count expansion, Lifecycle, Damage Bonus, Economy Bonus. Send-Creeps / Call-for-Help / Maze Stone **NOT enabled** in Solo. |

## Cascade implications

- **Supersedes Round 6 Send-Creeps "Solo variant" (Offensive Wave) row.** Solo does not surface Send-Creeps. The 5-mode Send-Creeps variant table in `2026-05-04-round-6-aux-economy-ratifications.md` collapses to 4 modes (Horde / PvE-MP / PvP Interest Wars / PvP Maze). Solo's pacing-decision design space is filled by Universal-slot tactics only.
- **Mission count target ~12-20** sets a bounded authoring scope. Per-civ proportional split likely (4-7 missions per civ if all 3 civs carry equal narrative weight; alternative is asymmetric weighting per narrative arc).
- **Per-mission (k) selector + replay-for-unlocks** introduces a meta-progression hook: cosmetic / lore unlocks are tied to (k)-tier completion. This couples to Follow-up #7 (Foresight-coin meta-progression) — Solo Campaign unlocks may be the first concrete consumer of Foresight-coin.
- **Hand-authored maps** rules out procedural map gen for Solo. Phase 4 engine architecture must support a map-authoring pipeline (data-driven hex layout + path spline + scripted-event hooks per round).
- **Narrative thread between missions** — story is now a load-bearing artifact. Likely a new follow-up: campaign-narrative outline (per civ + cross-civ unifying arc).

## Open follow-ups for Round 8+

- Mission-count split per civ (equal / asymmetric / arc-weighted).
- Campaign narrative outline (separate decision; Phase-1 thematic artifact).
- Cosmetic/lore unlock catalog tied to (k)-tier completion.
- Map-authoring pipeline (Phase 4 architecture concern).

## Reason chosen

PM Recommended on all 4. Multi-mission saga + per-mission (k) preserves replay value and authorial control while keeping each match within the locked balance-pass-#1 R1-R30 frame. Single-lane preserves hex grid invariant. Universal-only auxiliary slots in Solo keeps the campaign focused on tactical placement + lifecycle decisions, deferring send/help/maze mechanics to the modes where they are the design's primary intent.
