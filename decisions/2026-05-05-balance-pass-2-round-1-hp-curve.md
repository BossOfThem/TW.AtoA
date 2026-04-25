# Decision — Balance-pass #2, Round 1: Runner HP curve (e) base shape + boss spikes

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (numbers-phase consumer); CONCEPT.md (pending §-new "Tower-vs-Unit math" insertion); `prototype/data/balance.json` (downstream); Follow-up #13.

---

## Decision

The runner HP curve (variable (e) per locked frame) is governed at **Easy baseline** by:

```
HP_standard(R) = 100 · 1.16^R         for R ∈ [1, 30]
HP_boss(R)     = HP_standard(R) · m(R)
   where m(R10) = 3, m(R15) = 2, m(R30) = 5; m(R) = 1 otherwise.
```

R1 = 100 is a **normalized math unit** (rescalable in prototype/data without invalidating the curve). Sample anchor values (rounded):

| R | HP_standard | HP_boss (if any) | Note |
|---|-------------|------------------|------|
| 1 | 116 | — | First-wave onboarding floor. |
| 5 | 210 | — | Modifier round (slot type, not HP spike). |
| 10 | 442 | **1,326** | Boss slot (×3). +1 Divinity drop per locked frame. |
| 15 | 919 | **1,839** | Elite slot (×2). 0 Divinity drop. |
| 20 | 1,931 | — | Modifier round. |
| 25 | 4,058 | — | Telegraph round. |
| 30 | 8,585 | **42,925** | Final Boss (×5). +2 Divinity drop. |

**Easy is the base.** Hard / Hardcore shift the **exponent** only (single-axis (k) compounding per locked frame); ratification of those exponent values is **Round 2**.

The boss-spike multiplier is an **HP overlay only** — not a slot-typology change. Slot type (Boss / Elite / Modifier / Telegraph / Standard / Swarm / Recovery) and reward shape are governed by the locked round template; this decision adds only the HP magnitude relative to standard at the same R.

## Context

Numbers-phase Follow-up #13 was unblocked end-of-day 2026-05-04 by the 12-round conceptual ratification. PM picked Numbers-phase #13 (Recommended) on the next-track gate. Round 1 of the numbers arc targets the most foundational item: the per-round HP shape that everything else (tower damage Round 5, (k) exponents Round 2, Tribute economy Round 3) stacks on top of.

The 17-item conceptual frame locks the **form** (`Σ_T [DPS×t_engaged×matchup×passive_modifiers×status_state×s]`), the **slot typology** (7 types with R5/R10/R15/R20/R25/R30 assignments), and the **boss reward shape** (lump Tribute + guaranteed Divinity at R10/R30; medium + 0 at R15). It does NOT lock the per-round HP magnitudes — those are this decision.

## Alternatives considered

### Standard HP growth ratio

- **Option A — 1.14^R (gentler).** R30 ≈ 5,047 (~50× R1). Almost exactly matches the player tier-up damage ladder (≈54×); means an on-curve player neutralizes the standard wave with minimal skill. Boredom risk; leaves more headroom for Hardcore exponent shift.
- **Option B — 1.16^R (BTD6 precedent).** (Chosen.) R30 ≈ 8,585 (~85× R1). Slightly outpaces the player ladder, leaving (g) matchup + (i) placement + (h) ability uptime as the gap-closers. Industry-tuned.
- **Option C — 1.18^R (steeper).** R30 ≈ 14,378 (~144× R1). Easy starts to feel like Hard. Less room for Hardcore exponent shift in Round 2 (compounding risk against the locked single-axis (k) rule).
- **Option D — Piecewise (linear early, exponential late, inflection R15).** Maps cleanly to the round-arc beats (gentle onboarding / steady ramp / climax) but two-knob tuning is harder, doesn't translate cleanly to Godot tick-math, and players struggle to predict the inflection. Highest authoring cost.

### Boss-spike multipliers

- **Option E — R10 ×2.5 / R15 ×2 / R30 ×4 (gentler).** R30 ≈ 34,340 — climactic but more forgiving; prevents God-rush requirement. Risk: bosses feel like "thicker standard runners" — special-slot identity dilutes; the locked R30 huge-Tribute + 2-Divinity drop loses justification.
- **Option F — R10 ×3 / R15 ×2 / R30 ×5.** (Chosen.) Asymmetric spikes give each special round distinct flavor; R30 ×5 ≈ 42,925 justifies the 2-Divinity drop and Fusion endgame climax.
- **Option G — R10 ×3.5 / R15 ×2.5 / R30 ×6 (steeper).** R30 ≈ 51,510. Effectively requires Fusion endgame play; punishing on first attempts; amplifies (k=Hardcore) compounding risk.
- **Option H — Symmetric ×3 across R10/R15/R30.** Cleaner to balance; differentiation comes from drops + slot type only. R30 only ×3 ≈ 25,755 — underwhelming as Final Boss / Fusion-endgame climax.

## Reason chosen

**3x debug loop synthesis** (run prior to surfacing options):

- *Loop 1 (critique).* Linear HP gets trivially won late — player tier-ups (T1→T2→T3→T4→God ≈ 3×3×3×2 = 54× damage) are multiplicative. Pure exponential at high b risks unwinnable R30 once (k) compounds. Polynomial outpaced by geometric tier-ups by R20+. Piecewise hides the spike but is harder to balance and communicate.
- *Loop 2 (steelman).* The real lens is **per-round ratio**: exponential = constant ratio (players parse as "steady ramp"); polynomial = decreasing ratio (parse as "trivially easy then suddenly impossible"). BTD6 settled near 1.16^R after years of live tuning. Piecewise is what players already implicitly experience in most TDs (boss spikes overlay a smooth base curve).
- *Loop 3 (synthesis).* Base curve = **smooth compound exponential** at modest growth ratio; **boss spikes overlay** at R10/R15/R30 per the locked round template. Anchor R1 standard at 100 (normalized). 1.16 is the BTD6-precedent sweet spot; player damage ladder ≈ 54× from R1→R30 via tier-ups, so HP curve at 1.16 (~85×) just slightly outpaces, leaving (g)+(h)+(i) skill axes as the gap-closers — exactly the design intent. Asymmetric boss spikes preserve special-round identity and justify the locked drop shape.

PM picked Recommended on both questions; no override notes.

## Reversibility note

**Medium.** The math form (`100 · 1.16^R` with `m(R)` overlay) is parameterized — `b = 1.16` and `m` values can be re-tuned in numbers-phase Patch-1 without invalidating the frame. A *shape* change (compound → polynomial → piecewise) would invalidate Round 2 (exponent-shift only makes sense for compound) and would require re-ratifying both rounds. The R1=100 normalization unit is rescalable freely in `balance.json` once the prototype data layer ratifies; downstream tower-damage numbers (Round 5) are normalized against this anchor.

## Cascade impact

- **Frame-consistent.** Single-axis (k) compounding rule (locked) maps to exponent shift on the `b` constant in Round 2. Boss-spike overlay does not interact with (k) — overlay multiplier `m(R)` is constant across difficulty tiers.
- **Round 2 ((k) exponents)** consumes this curve as the Easy baseline. Hardcore exponent value must keep R30 mathematically winnable under expected player skill ceiling.
- **Round 3 (Tribute economy)** consumes per-round HP totals to size kill rewards (per-runner (a) yield) such that on-curve player at expected (g)+(i) skill can afford expected tier-up cadence.
- **Round 4 (per-map (j) and speed (f))** consumes the time-to-kill implicit in this curve when sizing engagement-time integral via ε.
- **Round 5 (tower stats)** consumes this curve directly when sizing T1/T2/T3/T4/God damage/cd/range to clear standard waves at expected tier-up cadence.
- **`prototype/data/balance.json` untouched this turn** — landing the curve in prototype data is a downstream port task once enough rounds ratify to populate `BALANCE` meaningfully.
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched.

## Follow-ups

- **Round 2 — (k) exponent values** for Easy / Hard / Hardcore. Easy is the base (`b = 1.16`); Hard and Hardcore shift `b` upward. Ratification target: ensure R30 Hardcore is mathematically winnable at the skill-bar threshold (Round 9), not under it.
- **Round 3 — Tribute economy** consumes HP totals for kill-yield curve sizing.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
- **`prototype/data/balance.json`** port deferred until Round 5+ ratifies enough to make the `BALANCE` region meaningful.
