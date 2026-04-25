# Decision — Balance-pass #2, Round 5: Tower (c) DPS ladder + tier-up costs

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item (c) tower base damage, item (l) lifecycle, item (m) merge/promote/fusion — magnitudes now bound); CONCEPT.md (pending §-new "Tower-vs-Unit math"); `prototype/data/balance.json` + `prototype/data/towers.json` (downstream); Follow-up #13.

---

## Decision

### DPS ladder (multipliers off T1 base)

```
T1   = 1.0× T1_base
T2   = 3.0× T1_base   (×3 from T1)
T3   = 9.0× T1_base   (×3 from T2)
T4   = 27.0× T1_base  (×3 from T3)  — Demigod
God  = 54.0× T1_base  (×2 from T4)  — Fused
```

Ladder shape: **3 × 3 × 3 × 2 ≈ 54×.** Mirrors the player tier-ladder factor in the Round 2 winnability math (skill-stack × tier-ladder ≈ 5 × 54 ≈ 270×; sufficient to clear R30 Easy 85× HP and Hardcore 565× HP under skill-stack maxed + (s) aux + Fusion-on-schedule).

**T1 base DPS anchor:** `T1_base = 20 damage/sec` (Standard archetype). Cleared R1 std runner (116 HP) in ~5.8s engaged time; at f_base=50 u/s + ε=0.6, path-length-in-range typically 60% of full path → engagement window comfortably accommodates the kill at expected wave density (~15 std runners per wave).

Per-tower variance lives in (cd, range, archetype-bonus, status-proc) — same DPS at the tier, but specific cd/range tuned per tower identity. Per-tower magnitudes deferred to a downstream tower-authoring sub-pass (post-Round 10, pre-prototype port).

### Tier-up costs (Tribute, before sell-refund cycling)

| Step | Tribute cost | Other gates | Notes |
|------|--------------|-------------|-------|
| **T1 placement** | 100 | — | Cheapest-cost floor anchors (n) buildable-slot binding. |
| **T2-merge** (2 T1 same-civ same-tier within `CIV_MERGE_RADIUS` → 1 T2) | 300 | adjacency (m) | Consumes 2 T1 placements (200 sunk) + 300 merge fee = 500 effective T2 cost. |
| **T3-merge** (2 T2 same-civ same-tier → 1 T3) | 900 | adjacency (m) | 1,000 sunk T2 + 900 merge fee = 1,900 effective T3 cost. |
| **T4-promote** (single T3 → T4 Demigod, valid demigod mapping) | 2,500 | demigod-mapping (m) | 1,900 sunk T3 + 2,500 = 4,400 effective T4 cost. |
| **Fusion** (2 T4 Demigods same-civ → 1 God) | **0 Tribute** | 2-Divinity menu unlock + 1 Divinity per Fusion (m) + (o) | 8,800 sunk T4 cost + 1 Divinity = effective God cost. |

Geometric ×3 cost ladder (T1→T4); Fusion is **Divinity-priced**, not Tribute-priced (per locked frame item m). Costs are constant across (k) per single-axis (k) rule.

### Expected on-curve spend (Easy)

Reference roster across R1→R30:
- ~15 T1 placements early-game (1,500 Tribute)
- ~5 T2-merges through R10–R15 (1,500 Tribute) — consumes 10 of the T1s
- ~3 T3-merges through R15–R20 (2,700 Tribute) — consumes 6 of the T2s
- ~2 T4 promotes through R20–R25 (5,000 Tribute)
- ~1 Fusion through R28–R30 (0 Tribute, 1 Divinity)

**Cumulative tier-up spend ≈ 10,700 Tribute** against R1→R30 Easy cumulative income ≈ 25,000 Tribute (Round 3). Headroom **≈ 14,300 Tribute** for sell-refund cycling, mid-match re-builds, and aux-slot purchases (Round 7 sizes those). Matches Round 3 cascade-impact estimate cleanly.

## Context

Rounds 1–4 ratified HP curve (R30 Easy std = 8,585), (k) exponents (1.16/1.19/1.22), Tribute economy (yield + boss lumps; Easy cumulative ≈25K), and speed (f) + per-map (j) defaults (50 u/s × archetype mults; ε=0.6, N=24). Round 5 sizes the **tower-side** of the master equation: per-tier DPS ladder and tier-up costs. The 17-item conceptual frame locks the **shape** of (c) (per-tower per-shot damage scaled by lifecycle (l)) and the **gates** of (m) (merge / promote / Fusion adjacency rules) — Round 5 binds the magnitudes.

Round 2 winnability ground (skill-stack ~5× × tier-ladder ~54× = ~270× expert effective damage vs Easy R30 HP 85× / Hardcore R30 HP 565×) consumed the ×54 tier-ladder as a placeholder; Round 5 ratifies it as the actual ladder.

## Alternatives considered

### DPS ladder

- **Option A — 3×3×3×2 = 54×.** (Chosen.) Geometric mid-ladder + 2× Fusion top-cap. Clean tier-up dopamine; matches Round 2 winnability math; Fusion feels meaningful but not mandatory. T1/T2 phases retain agency; T3 is the natural tier where matchup (g) starts deciding outcomes.
- **Option B — 2.5×2.5×2.5×2 = 31.25×.** Gentler. R30 Easy needs ~3× skill-stack to clear (well within reach); Hardcore at 565× HP needs near-ceiling stack. Smaller per-tier dopamine; merging risks feeling marginal. Easier authoring.
- **Option C — 4×4×4×2 = 128×.** Steeper. Tier-up huge but degenerate "rush T3 ASAP" meta likely; T1/T2 throwaway; Fusion-endgame upstaged. Off-curve under design intent of multi-tier engagement.
- **Option D — 3×3×3×2.5 = 67.5×.** Same T1→T4 (27×) but bigger Fusion step. Risk: makes Fusion mandatory for Hardcore R30 clear, removing player agency on whether to spend Divinity (1-Fusion = ½ of a 2-Divinity unlock budget; if mandatory, the Divinity choice axis collapses).

### Tier-up costs

- **Option E — 100/300/900/2500 (×3 ratio).** (Chosen.) Mirrors DPS ladder ratio. Expected spend ~10.7K vs 25K income → ~14.3K aux/cycling headroom. Matches Round 3 cascade estimate.
- **Option F — 80/240/720/2000.** Tighter base. ~8.5K spend, ~16.5K headroom → max-aux trivializes Hard; cycling dominates strategy.
- **Option G — 120/400/1300/3500.** Looser late. ~13K spend, ~12K headroom → Hardcore margin shrinks; "every Tribute matters" — virtue or punishment depending on player temperament.
- **Option H — 100/250/750/2000 (×2.5 ratio).** Gentler ratio than DPS ladder. ~9K spend, ~16K headroom → late-game Tribute overflow with no sink.

## Reason chosen

**3x debug loop synthesis:**

- *Loop 1 (critique).* Linear DPS ladder loses to compound HP curve by R20+. Too-steep ladder breaks merging cadence (rush T3, throwaway early-game). Cost ratios mismatched to DPS ratios create Tribute traps (too-cheap top-tier or too-expensive low-tier; both warp building meta).
- *Loop 2 (steelman).* Geometric ×3 DPS ladder + matched ×3 cost ladder is the standard TD pattern (BTD6 Tier 1–3 ~×3, Crossroad/Squadron similar). Players parse "each merge ~triples your tower" as a clean axiom. ×2 Fusion top-cap keeps Fusion meaningful without making it mandatory; the Divinity-pricing (vs Tribute) preserves the dual-currency design intent — Fusion is a *strategic* spend, not an *economic* spend.
- *Loop 3 (synthesis).* 3×3×3×2 ladder + 100/300/900/2500 cost ladder lands the Round 2 winnability math, the Round 3 economic headroom (~14K aux budget), and the dual-currency Fusion-as-strategic-spend design intent. Per-tower variance pushed to authoring sub-pass — base ladder is the contract.

PM picked Recommended on both questions; no override notes.

## Reversibility note

**Medium.** Ladder multipliers (3, 3, 3, 2) and T1_base (20 dmg/sec) are 5 values; cost ladder is 4 values. Re-tuning any of these is a config change in `balance.json`. *Shape* changes (non-geometric ladder, non-Tribute Fusion cost, or per-(k) cost scaling) would invalidate Round 2 winnability + Round 3 economic headroom estimates and need re-ratifying.

## Cascade impact

- **Round 6 (commander (h) magnitudes)** sized as multipliers/adders against T1_base = 20 dmg/sec and the per-tier ladder (passive +X% damage means +X% of the current tier DPS; signature damage scales with tier of caster's surrounding towers).
- **Round 7 (aux economy + (s) ranges)** consumes ~14K Tribute headroom for tactical-slot pricing (Tribute-priced) and Divinity-slot pricing (Divinity-priced; Fusion competes for the same Divinity pool, cap 6/match per locked frame). (s) range tuned to give ~1.2× DPS bonus at maxed aux, closing Hardcore margin per Round 2 ground.
- **Round 8 (per-mode tuning)** Send-Creeps yields tuned against expected Tribute income at a given R; Lane-Trade refund tuned against tier-up sunk-cost; PvP-Maze stones priced against T1=100 floor (cheap stone in the [10, 30] range).
- **Round 9 (skill-bar thresholds)** placement-coverage axis consumes effective DPS-per-second-engaged math: T2 at ε=0.6 vs R10 Boss HP 1,326 → ~22s engaged-time-equivalent at T2 DPS 60. Threshold-uptime requirements use this floor.
- **Per-tower authoring (post-numbers-phase)** — concrete (cd, range, attack-type, status-proc) per tower in the locked 18-T1-T3 + 18-T4-Demigod + 9-God roster. Authoring sub-pass consumes T1_base + ladder.
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched (items (c) + (l) + (m) magnitudes now bound; shapes unchanged).
- `prototype/data/balance.json` + `prototype/data/towers.json` untouched this turn.

## Follow-ups

- **Round 6 — commander (h) magnitudes** sized against T1_base + per-tier ladder.
- **Round 7 — aux costs + (s) ranges** consume ~14K Tribute headroom + Divinity Fusion-vs-aux budget.
- **Round 8 — Send-Creeps yields** tuned against per-R income.
- **Round 9 — placement-coverage thresholds** verify R10 Boss / R15 Elite / R30 final-boss clear under expected ladder + ε bands.
- **Per-tower authoring sub-pass** (post-Round 10) — per-tower (cd, range, attack-type, status-proc) for full 18-T1-T3 + 18-T4-Demigod + 9-God roster.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
