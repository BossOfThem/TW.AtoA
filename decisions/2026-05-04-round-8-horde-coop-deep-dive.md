# Decision — Round 8: Horde Co-op deep-dive + co-op mode split (Accepted)

**Date:** 2026-05-04 (Round 8, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md), [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md) (further narrows Send-Creeps Horde variant), CONCEPT.md §-new "Game modes: Horde Co-op (×2)".

---

## Ratified

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Lane topology | **PM scope expansion — TWO Horde Co-op modes:** **Horde-A "Lane Defense"** (per-player adjacent lanes; creeps that leak one player's lane bleed sideways into neighbor) AND **Horde-B "Shared Front"** (single shared lane; map grows in proportion to player-count N). Both modes coexist at launch per "go big" doctrine. Total mode count now **6**. |
| 2 | Economy | **Per-player wallet, no sharing** — each player accrues own Tribute + Divinity by kill-credit. No transfer mechanic at launch. Preserves identity + agency. |
| 3 | (k) × N scaling | **(k) tier + linear N-multiplier on HP-curve** — player picks (k) at lobby; HP exponent shifts per (k); HP curve multiplies by player-count factor (×1.0 N=1 → ×2.8 N=8 region, exact values numbers-phase). Clean single-axis composition with locked balance-pass-#1 frame. |
| 4 | Auxiliary slots in Horde (both A and B) | **Universal slots only** — Targeting / Build-queue / Tower-count / Lifecycle / Damage Bonus / Economy Bonus. Send-Creeps Horde variant ("Reinforce Lane") **NOT enabled**. Call-for-Help **NOT enabled**. Maze Stone **NOT enabled**. |

## Cascade implications

- **Mode count expansion 5 → 6.** Mode roster is now: Solo Campaign · Horde-A Lane Defense · Horde-B Shared Front · PvE Multiplayer · PvP Interest Wars Lane · PvP Maze Lane. Per "go big" doctrine all 6 ship at v1.0.
- **Horde-A "leakage bleed-sideways" mechanic** is a new conceptual primitive — not in any prior decision. Needs frame extension: when a creep leaks from player P's lane, it spawns at player (P+1)'s lane head with a state tag (origin_player=P, leak_count=1). Player (P+1) gets a chance to kill it; if it leaks again, lives-loss is attributed proportionally. **Open ratification** for Round 9+ on whose lives suffer (originating player only / receiving player only / split / chained).
- **Horde-B "map grows with N"** rules in procedural-or-parameterized map scaling. Hand-authored Horde-B maps would need N variants per map (8 player-count buckets × map count = high authoring cost). Likely pattern: parameterized base map with N-dependent path-length / buildable-hex extension. **Open ratification** for Round 9+ on map authoring strategy.
- **Send-Creeps narrowing pattern.** Round 7 Solo dropped Send-Creeps "Offensive Wave"; Round 8 Horde dropped Send-Creeps "Reinforce Lane". The 5-mode universal-with-variants table from Round 6 collapses further — Send-Creeps appears to be a **PvP-and-PvE-MP-only mechanic** in practice. **Flag for Round 9-11:** confirm Send-Creeps lives only in PvE-MP / PvP Interest Wars / PvP Maze. If confirmed, Round 6 Send-Creeps universal classification will be downgraded to a 3-mode mechanic in a follow-up superseding decision.
- **Call-for-Help dropped from Horde** — was originally classified "Co-op + PvE family". If Horde rejects it, Call-for-Help may be PvE-MP-only. Round 10 PvE-MP will confirm.
- **Map scaling for Horde-B** plus mission-authoring for Solo plus Horde-A's lane-bleed mechanic = significant Phase 4 engine-architecture concerns. The per-mode map pipeline must support: hand-authored single-lane (Solo), per-player adjacent lanes with bleed (Horde-A), parameterized N-scaling shared lane (Horde-B), N parallel identical lanes (PvE-MP), per-player lane (PvP-IW), per-player tower-as-path grid (PvP-Maze). Six distinct map shapes.

## Open follow-ups for Round 9+

- Horde-A leak-bleed lives-attribution rule (originating / receiving / split / chained).
- Horde-A creep-bleed wraparound (does the last player's lane bleed to the first player, or does it leak-out as lives loss?).
- Horde-B map-scaling authoring strategy (parameterized vs N-variant authored).
- Send-Creeps cross-mode classification confirmation (likely 3-mode after Round 9-11).
- Call-for-Help cross-mode classification (likely PvE-MP-only after Round 10).

## Reason chosen

PM Recommended on 3 of 4 axes. PM scope expansion on Q1 splits Horde into two flavors covering both classic co-op-tower-defense topology preferences (per-player adjacent ownership vs shared-front survival). Aligns with "go big, no scope cuts" doctrine. Per-player wallet + linear N-scaling preserves the locked balance-pass-#1 frame's single-axis (k) compounding rule. Universal-only auxiliary slots keeps Horde's tactical surface focused on placement + lifecycle.
