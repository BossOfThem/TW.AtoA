# Decision — Round 10: PvE Multiplayer deep-dive (Accepted)

**Date:** 2026-05-04 (Round 10, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md), CONCEPT.md §-new "Game modes: PvE Multiplayer".

---

## Ratified (4 PM Recommended picks)

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Lane count | **Lanes = N (player count, 2-8)** — parameterized; no empty lanes; no AI bots required at launch. |
| 2 | Win condition | **Last alive wins; R30 highest-lives tiebreak** (then Tribute+Divinity tiebreak). No tie-break escalation needed (parallel-lanes design has low tie probability). |
| 3 | Cross-lane UX | **View-only spectate** — pan/zoom to opponent lanes to see towers/lives/currency. No interaction beyond Lane-Trade send. |
| 4 | Aux slots | **Universal + Send-Creeps PvE-MP variant (Lane-Trade) + Call-for-Help** — three families. Maze Stone NOT enabled. |

## Cascade implications

- **Send-Creeps cross-mode classification update.** After Rounds 7-10: Solo NO, Horde-A NO, Horde-B NO, PvE-MP YES (Lane-Trade), PvP-IW YES (Send-for-Interest). Round 11 PvP Maze pending. Likely-final: 3-mode mechanic (PvE-MP / PvP-IW / PvP-Maze).
- **Call-for-Help cross-mode classification confirmed.** Originally "Co-op + PvE family"; after Rounds 8 + 10: Horde-A NO, Horde-B NO, PvE-MP YES. Call-for-Help is **PvE-MP-only** at launch (likely smaller cross-mode footprint than Round 6 anticipated).
- **Spectate UI is a Phase-4 architectural concern** — needs efficient view-state replication for 7 opponent lanes plus own lane. Couples to PvP-IW spectate (same primitive, different interaction rules).
- **Lane-Trade kill-bonus refund** — numbers-phase Follow-up #13 must tune the refund such that Lane-Trade is a real economic decision (not free Tribute, not punishing). Coupled to (a) Tribute-yield curve.
- **R30 highest-lives tiebreak** — implies deterministic lives accounting per leak event. Already locked in frame; no extension needed.

## Reason chosen

PM Recommended on all 4. Parameterized N-lanes scales clean without bot-AI dev scope. Last-alive + R30 tiebreak preserves PvE-MP's competitive-survival identity vs Horde's pure-cooperative identity. View-only spectate enables strategic-info-from-leader without enabling griefing. Three aux-slot families (Universal + Lane-Trade + Call-for-Help) give PvE-MP a richer toolkit than Solo/Horde without adversarial-PvP complexity.
