# Decision — Balance-pass #2, Round 7: Aux-slot costs (Tribute + Divinity) + (s) auxiliary multiplier ranges

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (binds magnitudes for variable (s) extension), [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md) (consumes Tribute/Divinity currency split), [`decisions/2026-05-04-round-12-aux-ux-frame-extension.md`](2026-05-04-round-12-aux-ux-frame-extension.md) (binds (s) multiplier values), [`decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md`](2026-05-05-balance-pass-2-round-3-tribute-economy.md) (Tribute headroom audit), [`decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md`](2026-05-05-balance-pass-2-round-5-tower-baselines.md) (validates Hardcore-margin promise), CONCEPT.md (pending §-new "Auxiliary economy structure" magnitudes).

---

## Decision

The auxiliary economy carries six bound magnitudes for universal slot families:

| Slot family | Currency | Cost | Effect | Cap |
|---|---|---|---|---|
| **Damage Bonus ((s) headline)** | Divinity | **1 Div** | (s)=1.20 multiplicative on damage equation, all towers, rest-of-match | Max 1 active/match |
| **Economy Bonus** | Divinity | **1 Div** | +25% per-kill Tribute on yield(R) curve only (boss lumps R10/R15/R30 untouched), rest-of-match | Max 1 active/match |
| **Tower-count expansion ((j) N+)** | Divinity | **1 Div = +2 N** | Adds 2 buildable hexes per Divinity spent; slots come empty (Tribute fills them) | Cap 3 Div spend → N=24→30 (+25%) |
| **Send-Creeps tactical (universal baseline)** | Tribute | **100 T** | Universal anchor for Solo "Offensive Wave" / Horde-A/B "Reinforce-Lane" / PvE-MP "Lane-Trade" / PvP-Maze "Send-Through-Maze" variants | No cap — tempo lever |
| **Call-for-Help** | Tribute | **300 T** | One-shot soft-assist unit deployment (Co-op + PvE modes only) | No cap |
| **Maze Stone** | Tribute | **25 T** | Cheap path-shape blocker (PvP-Maze only); upgradable to T1 by +75 T (= 100 T total = T1 placement parity) | No cap |

**Send-for-Interest (PvP-IW)** stays Divinity-priced per Round 6 Q2 currency-split rule (match-arc effect: permanent recurring income unlock); cost magnitude deferred to Round 8 per-mode tuning along with all Send-Creeps mode-variant income-yields.

**Targeting overrides** are free (per-tower right-click context menu; locked Round 5). **Build-queue** is free (UX convenience). **Level/upgrade/Fusion choice** surfaces existing tier-up costs (Round 5: 100/300/900/2,500 T + Fusion 1 Div); no new cost layer.

## Variable (s) magnitude binding

Per [`decisions/2026-05-04-round-12-aux-ux-frame-extension.md`](2026-05-04-round-12-aux-ux-frame-extension.md), the master damage equation extends to:

```
Damage_dealt(R) = Σ_T [DPS(T) × t_engaged(T,R) × matchup × passive_modifiers × status_state × s(T,R)]
```

Round 7 binds **`s(T, R) = 1.20` when Damage Bonus aux active, else 1.00.** Single global tier; civ-scope and per-archetype scope variants deferred to per-commander/per-tower authoring sub-pass post-Round 10.

Stacks multiplicatively with (h) passive +15% civ-matched aura (Round 6 commander magnitudes). Combined per-tower stack on civ-matched towers within commander aura with active Damage Bonus + matchup advantage: 1.20 (s) × 1.15 (h passive) × 1.25 (matchup) = **1.725× per-tower** before placement (i) and status (q) effects. Anchors Round 5's Hardcore-margin closure ground precisely.

## Currency-budget audit

### Divinity (6-cap/match)

Sources (interim per [Round 1 frame](2026-05-04-balance-pass-1-conceptual-frame.md), full ratification Round 10):
- R10 Boss: +1
- R20 zero-leakage streak ≥ 3: +1
- R30 Final Boss: +2
- 2 escalation hooks: TBD (Round 10)

Drain catalog post-Round-7:
| Drain | Cost | Round 7 status |
|---|---|---|
| Fusion menu unlock (one-time) | 2 Div | Locked (2026-04-25 ratification) |
| Per Fusion | 1 Div | Locked (2026-04-25 ratification) |
| Damage Bonus aux | 1 Div | **NEW** |
| Economy Bonus aux | 1 Div | **NEW** |
| Tower-count expansion | 1 Div / +2 N (max 3) | **NEW** |
| Send-for-Interest (PvP-IW) | TBD | Round 8 per-mode |

**Build feasibility checks (PvE 4-Div confirmed source floor; cap 6):**
- *Aux-heavy + 1 Fusion:* 2 (unlock) + 1 (Fuse) + 1 (Dmg) + 1 (Eco) = 5 Div ✓ fits cap; 1 Div leftover for +2 N expansion if streak hits.
- *Max aux, no Fusion:* 1 (Dmg) + 1 (Eco) + 3 (N+6) = 5 Div ✓ fits cap; 1 Div leftover.
- *Max Fusion, no aux:* 2 (unlock) + 4 (4 Fusions) = 6 Div ✓ but only at cap (4 Fusions assumes streak floor; on 4-Div PvE source floor, max 2 Fusions = 4 Div spend).
- *Balanced:* 2 (unlock) + 2 (2 Fusions) + 1 (Dmg) + 1 (N+2) = 6 Div ✓ at cap with 4-Div source floor + 2 escalation drops (Round 10 dependency).

Round 10 escalation-hook magnitudes will validate the 6-cap target at exactly the design intent — currently 4 Div confirmed source, 2 escalation TBD. Round 7 magnitudes work cleanly within the confirmed 4-Div floor for any *one-strategy* build; multi-strategy hybrid demands the full 6-cap source floor.

### Tribute (~14.3K headroom from Round 5 cascade)

Round 7 aux Tribute drains (typical-play estimates):
- Send-Creeps ×10 sends/match: 1,000 T
- Call-for-Help ×3 deployments: 900 T (Co-op/PvE only; Solo and PvP modes don't access this slot)
- Maze Stone ×6 stones: 150 T (PvP-Maze only)

**Mode-by-mode revised headroom (Easy ~25K income − ~10.7K tier-ups − aux):**
- Solo: 25K − 10.7K − 1.0K (sends) = **~13.3K residual** for sell-refund cycling
- Co-op (Horde): 25K − 10.7K − 1.9K (sends + Call-for-Help) = **~12.4K residual**
- PvP-Maze: 25K − 10.7K − 1.0K − 0.15K (stones) = **~13.15K residual**

All modes preserve healthy cycling headroom. Headroom degrades meaningfully only if player spams Send-Creeps beyond ~25 sends — at which point the design intent (sends are tempo levers, not primary economy) self-limits.

## Context

Per [`decisions/2026-05-04-round-12-aux-ux-frame-extension.md`](2026-05-04-round-12-aux-ux-frame-extension.md), the master damage equation extends with multiplicative variable (s) for auxiliary-state, but Round 12 left the magnitude unbound. Round 5 Hardcore-margin ground assumed `~1.2× aux contribution` to close the skill-stack × tier-ladder × matchup math against Hardcore R30 std HP 65,498 (vs Easy 8,585). Round 7 binds the magnitude that fulfills that promise and prices the Tribute-side tactical slots against the Round 5 ~14.3K Tribute headroom.

## Alternatives considered

### Q1 — Damage Bonus magnitude + scope

- **A: 1 Div = +20% global, single tier (Recommended; chosen).** (s)=1.20 anchors Round 5 promise exactly; simplest decision space; preserves (g) RPS matchup decisions (1.25/0.75 still pays even with +20% on both sides); civ + archetype scope variants Patch-1-able.
- **B: 1 Div = +15% / 2 Div = +30% (two-tier ladder).** Cheaper entry but forces 2 Div to hit Round 5 anchor (vs 1 Div Recommended); trades against Fusion economy at exactly the wrong granularity. Rejected.
- **C: 1 Div = +25% per civ (3 separate slots).** Civ-scoped; encourages mono-civ degeneracy; double-stacks (h) commander civ-aura (clarity cost: which is which?). Authoring complexity disproportionate. Rejected.
- **D: 1 Div = +10% per archetype (5 slots).** Most surgical but smallest per-slot impact; UI legibility weak (towers don't surface archetype tags in panel UI yet). Defers naturally to per-tower authoring sub-pass. Rejected.

### Q2 — Economy Bonus magnitude

- **A: 1 Div = +25% per-kill, rest-of-match, yield(R) only (Recommended; chosen).** Excludes boss lumps so storyline anchors stay; mid-match buy at R10 ~+5.5K extra Tribute = 1 extra Fusion economically; bounded snowball.
- **B: 1 Div = +20% per-kill (matches Damage Bonus symmetry).** Loses "economy = tempo, not finality" intent; cleaner math but weaker design alignment. Rejected.
- **C: 1 Div = +15% per-kill + applies to boss lumps.** Couples economy-aux to boss-storyline rounds; muddies anchor function of boss lumps. Rejected.
- **D: 2 Div = +50% per-kill.** Massive snowball; competes hard with 2 Fusions; low decision granularity. Rejected.

### Q3 — Tribute tactical slot baseline costs

- **A: Send-Creeps 100 T / Call-for-Help 300 T / Maze Stone 25 T (Recommended; chosen).** Anchored on tier-up cost ladder (T1 = 100, T2-merge = 300, ¼ T1 = 25). Symbolic equivalence; mode-variant income-yields (Round 8) carry economic-balance load.
- **B: Send-Creeps 200 T / Call-for-Help 500 T / Maze Stone 50 T.** Higher friction; suppresses routine use in Solo/Co-op. No anchor to existing cost ladder. Rejected.
- **C: Send-Creeps 50 T / Call-for-Help 200 T / Maze Stone 10 T.** Aggressive cheap-spam; trivializes maze pathing; PvP-IW snowball risk via cheap-creep recurring-income. Rejected.
- **D: Send-Creeps 150 T / Call-for-Help 400 T / Maze Stone 30 T.** No anchor; arbitrary mid-tier. Rejected.

### Q4 — Tower-count expansion ((j) N+)

- **A: 1 Divinity = +2 N (Recommended; chosen).** Cap 3 Div → +6 N (+25%); Divinity = gateway only, Tribute (100-2,500) fills slots. Competitive vs (s) Damage Bonus on like-for-like Div spend at T2-T3 fill; bounded.
- **B: 1 Divinity = +1 N.** Miserly; dominated by (s)=1.20 unless slot filled at T3+. Discourages slot adoption. Rejected.
- **C: 1 Divinity = +3 N.** Generous; cap 3 Div → +9 N (+38%); risks crowding Fusion economy by making N-aggro the dominant Divinity strategy. Rejected.
- **D: 2 Divinity = +5 N (one expensive jump).** Bulk; less granular; forces save-up; awkward stacking with (s) on small Div budgets. Rejected.

## 3x debug loop summary (per question)

**Q1 (Damage Bonus):** L1 critique flagged flat-global as collapsing (g) matchup decisions, civ-scope as double-dipping (h) passive, multi-tier as Fusion-degenerate. L2 steelman: matchup is multiplicative (1.25/0.75 still pays); civ-scope conflict resolves via slot/aura tag separation; multi-tier creates real Div opportunity cost. L3 synthesis: keep simple, single-tier flat (s)=1.20; defer surgical variants to authoring sub-pass.

**Q2 (Economy Bonus):** L1 critique: +25% breaks Round 3's 25K projection if bought R1 = +6.25K snowball. L2 steelman: 25K is full-match; mid-match buy (post-first-Divinity-drop R10) only multiplies remaining ~22K → ~+5.5K bounded by tier-up cost scaling. L3 synthesis: 1 Div = +25% on yield(R) curve only (boss lumps untouched), max 1 active/match.

**Q3 (Tribute slots):** L1 critique: cheap = spam-meta, expensive = unused, no anchor. L2 steelman: tier-up cost ladder IS the anchor; Send-Creeps as tempo not primary spend; Maze Stone is upgrade-bridge to T1 not committed structure. L3 synthesis: Send-Creeps 100 T (= T1) / Call-for-Help 300 T (= T2-merge) / Maze Stone 25 T + 75 to T1.

**Q4 (Tower-count expansion):** L1 critique: 1 Div = +1 N is dominated by (s)=1.20 across 24 towers. L2 steelman: slots come empty; Tribute fills (100/300/900/2500) — Divinity is gateway, not full cost. L3 synthesis: 1 Div = +2 N caps at +25% map expansion; Tribute followup makes the spend competitive without dominating.

## Reason chosen

Recommended on all 4 PM `AskUserQuestion` rounds. The magnitudes anchor on existing locked structure: (s)=1.20 fulfills Round 5's exact aux-contribution promise; tactical Tribute prices anchor on the Round 5 tier-up cost ladder (100/300/900/2,500); N-expansion prices Divinity as gateway with Tribute followup to avoid dominating Fusion economy. Currency-budget audit confirms feasibility within the confirmed 4-Div PvE source floor for single-strategy builds, and within the 6-cap target under Round 10 escalation-hook completion for hybrid builds.

## Reversibility note

Medium. Magnitudes can be retuned in Patch-1 telemetry if Hardcore winnability rate diverges from target. Anchored points (Round 5 ladder, (s) frame extension shape, Round 6 currency split) stay locked.

## Cascade impact

- Variable **(s) magnitude bound** = 1.20 single tier (was unbound after Round 12).
- **Frame Round-7 closure:** Round 7 of numbers-phase complete; aux-economy magnitudes now fully bounded except per-mode tuning (Round 8) and Divinity-source escalation (Round 10).
- **CONCEPT.md amendment scope expanded:** §-new "Auxiliary economy structure" section will enumerate the 6 universal slot families with bound magnitudes from Round 7 + per-mode variants from Round 8.
- `prototype/data/balance.json` **untouched.** Numbers-phase concept-only.
- `concept/phase-5.md §5.4 [LOCKED]` + `concept/phase-2.md §2.4a [LOCKED]` untouched.
- Round 5 Hardcore-margin ground (~270× expert effective damage vs ~565× Hardcore R30 HP) now closed: 1.725× per-tower stack (s × h-passive × matchup) at expert play, plus active commander burst per Round 6 + Fusion endgame, validates the design intent.

## Follow-ups

- **Round 8** — per-mode tuning: Send-Creeps mode-variant income-yields (Solo Offensive Wave kill-bonus refund / Horde Reinforce-Lane / PvE Lane-Trade refund / PvP-Maze Send-Through income / PvP-IW Send-for-Interest Divinity cost + recurring income magnitude); per-mode N-scaling (Horde-B linear N × player_count / PvE-MP per-lane / PvP-Maze maze-cell-based); PvP-IW tie-break magnitude.
- **Round 9** — skill-bar threshold magnitudes (matchup-correctness rate / placement-coverage / ability-uptime per (k) tier).
- **Round 10** — Divinity source escalation hooks (the 2 TBD sources to fill 6-cap); validates Round 7 max-aux+1-Fusion build feasibility.
- **Per-tower authoring sub-pass (post-Round 10)** — civ-scope and per-archetype Damage Bonus variants (deferred from Q1).
- **Per-commander effect-variant authoring sub-pass (post-Round 10)** — control / summon / economy variants of (h) slots.
- **CONCEPT.md amendment** — §-new "Auxiliary economy structure" with bound magnitudes.
