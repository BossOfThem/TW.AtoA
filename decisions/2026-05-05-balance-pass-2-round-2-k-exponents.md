# Decision — Balance-pass #2, Round 2: (k) compounding exponent values

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md`](2026-05-05-balance-pass-2-round-1-hp-curve.md) (extends Easy baseline upward); [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item 6 single-axis (k) — values now bound); CONCEPT.md (pending §-new "Tower-vs-Unit math"); `prototype/data/balance.json` (downstream); Follow-up #13 + Follow-up #9 (skill-bar thresholds Round 9 must keep Hardcore winnable).

---

## Decision

The difficulty tier (k) modifies **the HP-curve exponent only** (per locked frame item 6 — single-axis compounding). Values:

| Tier | Exponent `b` | R30 standard HP | R30 final-boss HP (×5) | Ratio over Easy R30 |
|------|--------------|------------------|------------------------|----------------------|
| **Easy** | **1.16** | 8,585 | 42,925 | 1.0× |
| **Hard** | **1.19** | 23,737 | 118,685 | 2.76× |
| **Hardcore** | **1.22** | 65,498 | 327,490 | 7.63× |

**Symmetric +0.03 exponent step per tier.** Each tier roughly **2.7× the prior at R30** for standard waves; final-boss spike (×5 overlay from Round 1) remains constant `m(R)` across (k) — only the underlying standard curve scales.

Sample trajectory at each tier (rounded):

| R | Easy std | Hard std | Hardcore std |
|---|----------|----------|---------------|
| 1 | 116 | 119 | 122 |
| 5 | 210 | 238 | 270 |
| 10 | 442 | 567 | 731 |
| 15 | 919 | 1,348 | 1,977 |
| 20 | 1,931 | 3,209 | 5,348 |
| 25 | 4,058 | 7,640 | 14,468 |
| 30 | 8,585 | 23,737 | 65,498 |

**Anti-pattern explicitly preserved:** (k) does NOT modify speed (f), tower cost (a-side), runner reward (a-side), targeting AI, sell-refund schedule (already (k)-coupled per locked frame; that coupling stays), boss-spike multiplier `m(R)` (constant across (k) per Round 1), or auxiliary slot costs.

## Context

Round 1 ratified the Easy-baseline HP curve `HP_std(R) = 100 · 1.16^R` plus boss-spike overlay (R10 ×3 / R15 ×2 / R30 ×5). The locked frame item 6 mandates that (k) shifts a single axis — the HP-curve exponent. Round 2 ratifies the specific exponent values for Hard and Hardcore.

Constraint: R30 Hardcore must be **mathematically winnable** at the skill-bar threshold (Round 9), not under it. The locked frame Round-1 anti-pattern (multi-axis (k) → geometric unwinnability) is the bound — Round 2 must stay clear of it.

Skill-stack ceiling at expert play (rough estimate consumed by Round 9 thresholds):

```
Skill multiplier S = matchup × placement × ability_uptime × status × aux(s)
                  ≈   1.25  ×    2.0     ×      1.3       ×  1.3   ×  1.2
                  ≈ 5.07× DPS over base tier-ladder
```

Player tier-ladder reach at R30 (T1→T2→T3→T4→God) ≈ 3×3×3×2 = **54×**. So expert effective damage ≈ 54 × 5 = **270×** R1 baseline. Hard-tier R30 standard HP at 237× is comfortably cleared. Hardcore at 388× requires near-ceiling skill-stack — clears with margin only when aux economy is maxed and commander cooldowns are spent on schedule.

## Alternatives considered

- **Option A — Hard 1.18 / Hardcore 1.20 (gentler).** Symmetric +0.02. R30 Hardcore = 23,737 — same as Recommended Hard. Tiers feel cosmetic; Hardcore reads as "Hard with bigger HP bars" rather than a distinct skill ceiling. Doesn't justify three separate tiers under "Go big" doctrine.
- **Option B — Hard 1.19 / Hardcore 1.22 (Recommended).** (Chosen.) Symmetric +0.03. R30 ratios over Easy: 1× / 2.76× / 7.63×. Each tier doubles-plus the prior R30 wall — clean perceived escalation; Hardcore aspirational but winnable.
- **Option C — Hard 1.20 / Hardcore 1.24 (steeper).** Symmetric +0.04. R30 Hardcore = 113,829 (1,138× R1). Brushes the Round-1 anti-pattern: would require near-optimal play across all skill axes simultaneously to clear at R30, leaving no margin for a single bad placement or a missed Fusion. Maps to Soulslike NG+ scaling — design intent here is TD-aspirational, not Souls-punitive.
- **Option D — Hard 1.19 / Hardcore 1.24 (asymmetric).** Easy+Hard mainstream, Hardcore as "different category." Same Hardcore-unwinnability concern as C. Asymmetric stepping muddies the mental model players build of difficulty.

## Reason chosen

**3x debug loop synthesis:**

- *Loop 1 (critique).* Conservative deltas (+0.02) make tiers feel cosmetic. Aggressive deltas (+0.04+) risk Hardcore unwinnability — the explicit Round 1 anti-pattern. Asymmetric deltas don't map to clean perceived-difficulty mental model.
- *Loop 2 (steelman).* Symmetric step lets players mentally model "each tier ~doubles the wall at R30." Expert skill-stack ceiling ~5× over tier-ladder leaves headroom up to ~400× HP at R30 before unwinnability — Pair B's 388× is exactly the margin the "Go big" doctrine wants (Hardcore *demands* engagement with aux economy + Fusion cadence + matchup, not coastable). Pair C's 634× (under prior assumption) or 1,138× exceeds the headroom.
- *Loop 3 (synthesis).* Pair B (Hard 1.19, Hardcore 1.22) is the BTD6/Risk-of-Rain-aligned middle path: meaningful tier separation, aspirational-but-winnable Hardcore, clean ~2.76× / ~7.63× R30 ratios over Easy. Hardcore doesn't fly off into unwinnability while still demanding mastery of every other system the locked frame ratified.

PM picked Recommended; no override notes.

## Reversibility note

**Medium.** Exponent values are single-parameter knobs in `prototype/data/balance.json` once that data layer ratifies — re-tuning Hard from 1.19 to 1.20 is a config-only change. A *shape* change ((k) becomes multi-axis, or affects speed (f) or boss-spike `m(R)`) would require re-opening the Round 1 single-axis lock and Round 1 boss-spike lock — those are frame-level changes and would invalidate the cascade.

## Cascade impact

- **Round 9 (skill-bar thresholds)** consumes these exponents directly. Hardcore threshold target: **expert player at ~80% skill-bar uptime clears R30 Hardcore standard wave + final boss with no leak**. Easy threshold target: **casual player at ~50% uptime clears R30 Easy with up to 2 leaks tolerated** (lives = 10 per locked frame, 5-life buffer for casual play).
- **Round 5 (tower stats)** — T4 Demigod and Fused-God damage values must keep Hardcore R30 final boss (327,490 HP) defeatable in ≤ ~10 seconds of focused fire by an expert tower roster + commander signature uptime; sets a floor on per-tier damage progression.
- **Round 7 (aux economy + (s) ranges)** — (s) multiplier ranges set so that maxed aux on Hardcore gives the expert ~1.2× DPS bonus that closes the Hardcore margin; without aux, Hardcore is intentionally not winnable.
- **Sell-refund (k)-coupling** (locked Round 1 frame): Easy = full schedule (100/90/80/70/60), Hard = floor at 60%, Hardcore = floor at 50% (steeper schedule). Numbers stay as locked.
- **Speed (f)** is not (k)-affected per anti-pattern; Round 4 ratifies a single speed curve across all tiers.
- **`prototype/data/balance.json` untouched this turn.**
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched (item 6 now has bound values; shape unchanged).

## Follow-ups

- **Round 3 — Tribute economy** sizes per-kill rewards against Hardcore HP totals (player must afford expected tier-up cadence even on Hardcore; (a) per-runner yield is constant across (k), so reward-pressure ratio is what shifts).
- **Round 9 — Skill-bar thresholds** sets per-(k) bars and verifies Hardcore winnability at expert-band uptime.
- **Round 5 — Tower stats** floor on T4/God damage progression to keep Hardcore final boss ≤10s clear.
- **Round 7 — (s) auxiliary multiplier ranges** must give Hardcore the ~1.2× margin closer.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
