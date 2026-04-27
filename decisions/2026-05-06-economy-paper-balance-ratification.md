# Decision — Economy paper-balance ratification (§4.8 exit-gate item #7 close)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md §4.6`](../concept/phase-4.md) (Economy — two-currency shape; magnitudes locked Numbers-phase #13 R3+R7+R10), [`concept/phase-4.md §4.6a`](../concept/phase-4.md) (Auxiliary economy — universal aux-slot catalog), [`concept/phase-4.md §4.3`](../concept/phase-4.md) (Fusion-spend cadence — Divinity gating), [`concept/phase-4.md §4.8`](../concept/phase-4.md) (exit-gate item #7 ✅ ticked DONE), [`concept/phase-4.md §4.11.3`](../concept/phase-4.md) (Tribute-economy (a) — read-only), [`concept/phase-4.md §4.11.5`](../concept/phase-4.md) (Tower DPS ladder + tier-up costs (c) — read-only), [`concept/phase-4.md §4.11.7`](../concept/phase-4.md) (Per-mode tuning (g)/(p)/(q) — read-only), [`concept/phase-4.md §4.11.8`](../concept/phase-4.md) (Skill-bar thresholds — read-only), [`decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md`](2026-05-05-balance-pass-2-round-3-tribute-economy.md) (Tribute economy — read-only input), [`decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md`](2026-05-05-balance-pass-2-round-5-tower-baselines.md) (DPS ladder + tier-up costs — read-only), [`decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md`](2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) (commander (h) — read-only), [`decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md`](2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) (aux costs + (s) — read-only), [`decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md`](2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) (per-mode tuning — read-only), [`decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md`](2026-05-05-balance-pass-2-round-10-divinity-sources.md) (Divinity sources — read-only).

---

## Decision

Ratify the Economy paper-balance close. Numbers-phase #13 (Rounds 1-10, 2026-05-05) authored every magnitude underpinning the two-currency Tribute + Divinity economy; this decision is a single-doc audit verifying cross-coherence, identifying no new design surface, and ticking `§4.8` exit-gate item #7 (`Economy balanced on paper`) DONE.

The audit is single-axis (no per-property arc) because every magnitude is already locked. Three coherence checks land below: (i) Tribute spend-vs-income at Easy-on-curve, (ii) Divinity spend-vs-income across realistic / expert / theoretical-ceiling envelopes, (iii) §4.11.8 skill-bar thresholds at Hardcore-expert per-(k) realized math. Zero cascade-violations across all three checks.

Phase 4 advances to **6 of 11 exit-gate items closed** (#1 commander one-pagers / #2 per-tower spec / #3 per-civ specialization / #4 enemy direction / #5 mobile unit control / **#7 economy paper-balance**). Skipping #6 (Fusion-numerics balance-pass) is intentional — Fusion magnitudes-per-God remain a separate sub-pass; Economy ratifies the Divinity *cadence* into Fusion (2 menu + 1/Fusion) without authoring God magnitudes themselves.

## Context

The Economy two-currency shape was locked 2026-04-25 (real-cultures ratification superseded the prior Gold/Faith/Cinders three-currency frame). Numbers-phase #13 then bound magnitudes:

- **R1** — Runner HP curve (e); `HP_std(R) = 100 · 1.16^R` Easy + boss spikes.
- **R2** — (k) compounding exponents per mode; Easy 1.16 / Hard 1.19 / Hardcore 1.22.
- **R3** — Tribute economy (a); `yield(R) = 5 · 1.10^R` + boss lumps R10/R15/R30 = 250/400/1500 T.
- **R4** — Speed (f); `f_base = 50 u/s` + archetype × multipliers.
- **R5** — Tower DPS ladder T1 = 1× / T2 = 3× / T3 = 9× / T4 = 27× / God = 54× + tier-up costs T1 = 100 T / T2 = 300 T / T3 = 900 T / T4 = 2,500 T.
- **R6** — Commander (h) magnitudes; passive +15% / active 4× T3 / signature free tier-up.
- **R7** — Aux-slot costs + (s) ranges; universal aux catalog priced in Tribute or Divinity.
- **R8** — Per-mode tuning + N-scaling + PvP tie-break; R31+ HP × 1.5 / R45 co-victory.
- **R9** — Skill-bar thresholds per (k); Hardcore expert closes margin exactly.
- **R10** — Divinity source escalation; 4-Div floor + Sources 5/6 escalation.

`§4.6` + `§4.6a` consolidated R3+R7+R10 into prose. `§4.3` Fusion specifies Divinity spend cadence (2 menu + 1/Fusion). `§4.10.6` locks sell-refund. The paper-balance question is: do these magnitudes compose without contradicting each other or the §4.11.8 skill-bar gate?

## Coherence audit — 3 checks, zero cascade-violations

### Check 1 — Tribute spend-vs-income at Easy-on-curve

| Quantity | Source | Value |
|---|---|---|
| Cumulative kill yield Easy R1→R30 | §4.11.3 + boss lumps | ~25,000 T |
| On-curve placement spend | §4.11.5 (T1 100 + T2 300 + T3 900 + T4 promote 2,500) | ~10,700 T |
| Aux + cycling spend (Co-op/Maze typical) | §4.6a R7 + §4.11.7 | ~1,900 T |
| Headroom for cycling / sends / Maze stones | residual | **~12,400 T** |

**Verification:** R1+R3+R5+R7 produce coherent Tribute curves at Easy. Sell-refund schedule (§4.10.6) preserves cycling viability (refund decays per-tier, never zero). At Hard / Hardcore (k = 1.19 / 1.22 per R2) the income curve is identical (Tribute is k-invariant per R3 lock); skill-bar tightening lives in §4.11.8 realized-math, not in Tribute scarcity. **PASS.**

### Check 2 — Divinity spend-vs-income across envelopes

| Envelope | Source pattern | Total in | Spend pattern | Balance |
|---|---|---|---|---|
| Realistic Easy | 4 floor (R10 + R15 + R30 + completion) | 4 Div | 2 menu + 1 Fusion + 1 Damage Bonus | 4 / 4 ✓ |
| Realistic expert | 4 floor + 1-2 escalation (1 Perfect-Wave + 1 First-Hybrid) | 5-6 Div | 2 menu + 3 Fusions + 1 aux | 6 / 6 ✓ |
| Theoretical ceiling | 4 floor + 3 Perfect-Wave (R10 + R15 + R30) + 1 First-Hybrid | 8 Div → cap 6 | 2 menu + 3 Fusions + 1 aux + 1 second-aux | 6 / 6 (2 wasted at cap; UI indicator per R10 lock) |

**Verification:** Hard 6-cap (locked R10) is structural, not soft. Wastage-past-cap is signaled in UI per R10. Sources 5+6 are skill-bar-gated (Round 9 thresholds) — novice stacks cannot accidentally reach the ceiling, preserving the difficulty escalation reading. PvP per-side awarding (R10 lock) preserves symmetry. **PASS.**

### Check 3 — §4.11.8 skill-bar realized math at Hardcore expert

| Term | Value | Source |
|---|---|---|
| Base survival margin | 0.576 | §4.11.8 R9 anchor |
| (s) Damage Bonus aux | 1.20 | §4.6a R7 |
| (h) Commander stack | 1.15 | §4.11.6 R6 |
| Matchup multiplier (RPS-favorable) | 1.25 | §4.10 RPS armor matrix |
| Realized | 0.576 × 1.20 × 1.15 × 1.25 = **0.993 ≈ 1.0** | Composition |

**Verification:** R6+R7+R9 close the Hardcore-expert margin to within ε of 1.0 (R9 anchor was tuned against this exact composition per the R7 audit footer). Easy / Hard envelopes carry positive headroom by R2's (k)-curve construction (1.16 / 1.19 vs 1.22 = expert margin only). The four locked multipliers compose multiplicatively per §4.10.2 master damage equation — no double-counting or sequence-dependence. **PASS.**

## Spine-doc edits

§4.6 / §4.6a / §4.3 already consolidate the locked magnitudes inline; no new prose authored this round. Two minor edits land:

1. `§4.8` exit-gate item #7 flips ✅ DONE with reference to this ratification + the Numbers-phase R1-R10 chain.
2. `§4.6` "Open" carry-list trimmed: `late-game Tribute sinks past R25` flagged for per-mode authoring (already locked there), `enhanced status-proc tiers` flagged for per-tower authoring (already locked there), `"Divinity" naming` flagged for Follow-up #5 (cultural-sensitivity at Phase-4 exit). All three are downstream artifacts, not Economy paper-balance debt.

## Cascade discipline check

Hard guards verified untouched verbatim:

- §5.4 + §2.4a [LOCKED] — no name additions / renames in this audit.
- 2026-04-25 content-skeleton verbatim — no civ / tower / commander / boss content.
- 2026-04-26 attack-type lock — RPS read-only (Check 3 references RPS-favorable matchup multiplier).
- §4.10 master damage equation — read-only verbatim (Check 3 multiplicative composition).
- §4.11.* numerics floor — read-only verbatim across all three checks.
- §4.7 Option C + R11 wave-composition variance grammar (LOCKED 2026-05-06) — read-only.
- §4.4 mobile-unit-control RN (LOCKED 2026-05-06) — read-only.
- Per-commander R1-R5 / per-tower R1-RN / per-civ R1-RN — read-only.
- Cultural-sensitivity Follow-up #5 — preserved (Divinity naming flagged for Phase-4-exit consultation).

Cascade-lint expected: only carried `93-files-vs-87-rows` finding (this round adds 1 file + 1 row → 94-vs-88, structural condition unchanged).

## Reason

Numbers-phase #13 produced the magnitudes; this ratification does the cross-property coherence work that closes the paper-balance gate. Authoring the audit as a single decision (rather than a multi-round arc) is appropriate because every magnitude is already locked — the deliverable is verification, not new design. The three checks are falsifiable: any future cascade-violation against any of them would re-open this gate item.

The skipping of #6 (Fusion-numerics) is intentional and explicit: Economy ratifies the Divinity *spend cadence* into Fusion (2 menu + 1/Fusion = 5 Div across 1 menu-unlock + 3 Fusions, fits 6-cap), but the per-God magnitudes (HP / range / cd / 2-type damage interaction with RPS) are a separate Fusion-numerics sub-pass. Closing #7 now without #6 is consistent with the §4.8 list ordering — the items are independent.

## Reversibility

**Medium.** This is a ratification, not a re-authoring. Reverting requires either (a) demonstrating one of the three checks is structurally false (which would re-open the underlying Numbers-phase round, not this audit), or (b) re-opening Phase 4 exit conditions for Economy-only reasons. Both are heavy moves. Treat the tick as a Phase-boundary commitment.

## Follow-ups

None new. The three minor "Open" carry-items at §4.6 close (296) are already-tracked downstream — re-flagged here for traceability, not added.
