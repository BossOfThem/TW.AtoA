# Decision — Promise 1 scope cut from 7 mode-types to 2 (Tower + PvP-Co-op feature-complete at 1.0; remaining 5 as roadmap stretch)

**Date:** 2026-04-29
**Status:** Accepted (autonomous-default for mode-pair; AM-flagged for PM ratification or redirect on PM-Fork-2)
**Reversibility:** Hard
**Affects:** CONCEPT.md (Promise 1 north-star scope; non-negotiables — "Go big at launch" interpretation under cut-shape), [`concept/phase-1.md`](../concept/phase-1.md) (vision/promise framing), [`concept/phase-3.md`](../concept/phase-3.md) §3.6 (6-mode ontology preserved as design substrate; commitment-scope cut), [`concept/phase-5.md`](../concept/phase-5.md) (build-order rewrite to single-product paid-EA shape), [`concept/phase-6.md`](../concept/phase-6.md) (validation MVP), [`concept/PROJECT-ARC.md`](../concept/PROJECT-ARC.md) Phase B item B.1, [`decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md`](2026-04-28-paid-ea-single-product-supersedes-pivot.md) (this decision is the operative artifact for the supersession's Promise-1 cut)

---

## Decision

Promise 1's commitment-scope is cut from **seven feature-complete mode-types at launch** to **two feature-complete mode-types at 1.0**. The chosen mode-pair under autonomous-default is **Tower (Solo Campaign) + PvP-Co-op (Horde-A and/or Horde-B)** per the 4-round superaligned product-shape swarm's strongest convergence (`concept/atoa-vs-mtm/round-3-turn-in.md` + `round-4-cycles/cycle-1-Q1-Q2.md` + `SYNTHESIS.md` §"Recommendation"). The remaining five mode-types — PvE-MP, PvP-IW (Interest Wars), PvP-Maze, and the residuals of the Horde split if only one is chosen — are framed as **roadmap stretch with no public completion date**. The 6-mode ontology itself (per [`concept/phase-3.md`](../concept/phase-3.md) §3.6, ratified Round 8-11 2026-05-04) is **preserved as design substrate**, not re-edited; only the Promise-1 commitment-scope is cut.

**Default mode-pair under autonomous-default:** Tower (Solo Campaign at the unit/tower/civ scaffolding level) + PvP-Co-op (Horde-A "wave-survival co-op" as the swarm's named strongest co-op shape; Horde-B available as substitute or as a post-launch addition).

**PM-Fork-2 status:** AM-flagged. PM may ratify the autonomous-default, redirect to **Tower + Custom** (the Promise-2 substrate-weighted alternative; Legion TD 2 reference-class pattern), or redirect to another pair entirely. Cascade impact of redirect is bounded: only Phase B work item B.1 (this decision) + Phase E work items E.4/E.5 (mode-type pair implementation) are sensitive to the choice; differentiation thesis (Phase D) and engine-choice mini-arc (Phase C) are pair-agnostic.

The cut is operationally effected through the paid-EA paid-base public refund-backed roadmap (the discipline mechanism per [`decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md`](2026-04-28-paid-ea-single-product-supersedes-pivot.md)). The contract with the audience-paying-in-advance is: launch with the chosen mode-pair feature-complete; deliver the roadmap-stretch modes if-and-when audience engagement permits; refund-eligible if material commitment is broken.

## Context

The 4-round superaligned product-shape swarm closed with a load-bearing finding now part of the supersession's substrate: **Promise 1 (seven feature-complete mode-types at launch) is not solo-reachable on either path in the surveyed evidence base.** Stormgate at $40M failed at exactly the AtoA mode-spread; Battle Aces was cancelled May 2025 under Tencent backing at narrower scope; no solo-dev shipper of more than one feature-complete mode-type appears in the surveyed record (`concept/atoa-vs-mtm/round-3/swarmer-promise-1.md`).

The supersession (Accepted 2026-04-29) authorizes the cut by direction; this decision performs it. The autonomous-default of Tower + PvP-Co-op is taken from R3+R4 strongest (PM-lens "reference-class match for TW-veteran target audience"; Player-lens "Legion TD 2 lineage anchor; 87% positive across 6,350+ reviews"; Promise-2 swarmer "co-op funder pattern reduces single-trunk risk"). The competing strongest alternative, Tower + Custom, is preserved as PM-Fork-2 redirect option per its Promise-2-substrate-weighted argument.

## Alternatives considered

- **Option A — Hold 7-mode commitment.** Empirically indefensible per Promise-1 swarmer finding; the supersession itself rejects this. Not chosen.
- **Option B — Cut to one mode (Tower only).** Strongest-possible scope discipline; simplest single-trunk product. But forfeits the swarm's converged finding that the cut should be to a *pair*, not a single — multi-mode small-launch is the pattern that survives reference-class match (Legion TD 2 / Bloons TD 6 / They Are Billions all ship multiple mode-types at launch even at smaller scope). Not chosen.
- **Option C — Cut to two: Tower + PvP-Co-op (chosen, autonomous-default).** Swarm's strongest convergence. Tower as the genre-anchor mode preserves the locked design substrate (3 civs × 6 towers × 5 units × 6 T4 Demigods × 9 Gods × 3 commanders + Fusion + attack-type RPS + economy + mobile unit control + R11 wave-variance) at launch-feature-complete grain. PvP-Co-op (Horde-A) adds the social-multiplayer reference-class match and provides a second mode that doesn't require independent design substrate (inherits from Tower's). Cost-of-second-mode is structurally minimized.
- **Option D — Cut to two: Tower + Custom (PM-Fork-2 redirect option).** Promise-2-substrate-weighted alternative. Custom mode loads the SC1/WC3 lobby + custom-game substrate (Promise 2) into Promise 1's launch commitment — substrate work that is otherwise post-launch becomes pre-launch. Trade-off: Custom is more substrate-load-bearing than PvP-Co-op (chat rooms / discoverability / map-share infrastructure) but provides longer-tail audience retention (the Legion TD 2 / SC2 Squadron TD pattern). PM-decisional fork; either choice is defensible.
- **Option E — Cut to two: Tower + PvE-MP.** Less convergence-supported than Tower + PvP-Co-op. PvE-MP shares more design substrate with Tower than PvP-Co-op does (both are wave-survival; PvP-Co-op layers in social play), but the audience reference-class match is weaker for PvE-MP at the TW-veteran target. Not chosen.

## Reason chosen

3x debug loop synthesis:

- **Loop 1 (critique):** Tower + PvP-Co-op as autonomous-default risks soft-locking PM choice. The swarm's R3+R4 strongest is genuinely strongest, but PM may have temperament or audience-priority intuitions the swarm did not surface (e.g. Custom as Promise-2 substrate-loader; e.g. PvE-MP as design-substrate-cheapest second mode). Risk of PM ratifying-by-inertia rather than choosing. Risk that PvP-Co-op multiplayer infrastructure is heavier than Tower-only and stretches Phase E past the paid-EA launch window. Risk that "PvP-Co-op" as a label obscures whether Horde-A or Horde-B is the canonical mode (if either; or both at the cost of design-substrate grain).
- **Loop 2 (steelman):** Soft-locking risk is mitigated by AM-flag plus explicit PM-Fork-2 preservation in PROJECT-ARC.md §4. The autonomous-default does not foreclose redirect; cascade impact of redirect is bounded to two work items. Multiplayer-infrastructure risk is real but is the same risk under any PvP-or-Custom choice; only Tower-only avoids it, and Option B was rejected for a different reason (multi-mode reference-class match). Horde-A vs Horde-B label resolution is handled by treating Horde-A as the swarm's named strongest under Round 8 (`decisions/2026-05-04-round-8-horde-coop-deep-dive.md`); Horde-B remains in the 6-mode ontology and is available as substitute if PM redirects.
- **Loop 3 (synthesis):** Tower + PvP-Co-op (Horde-A canonical; Horde-B available as PM-Fork-2 sub-redirect) is the autonomous-default. AM-flag preserves PM's choice authority. Cascade impact of any PM-Fork-2 redirect is bounded and reversal-cheap for the design substrate.

## Reversibility note

**Hard.** The cut itself is Hard-class because reversing requires the supersession's own reversal (which is also Hard); restoring 7 feature-complete mode-types at launch is empirically indefensible per the Promise-1 swarmer finding. The mode-pair *choice within the cut* is **Medium-class reversible** until Phase E item E.4 begins implementation; PM-Fork-2 redirect at any time before Phase E start costs a single decision-file edit + Phase 5 build-order revision.

## Follow-ups

- AM HANDOFF flags this decision's autonomous-default for PM ratify-or-redirect on PM-Fork-2.
- Phase B item B.3: edit CONCEPT.md Promise 1 north-star scope to reflect the cut (per cascade discipline; reopens Phase 1 framing under written supersession authorization).
- Phase B item B.4: drop "Mud to Myth" two-product framing from CONCEPT.md hub.
- Phase E items E.4/E.5: implement chosen mode-pair (sensitive to PM-Fork-2 outcome).
- Phase F item F.1: Steam-page draft language captures cut-vs-stretch-vs-post-1.0 trichotomy for the five roadmap-stretch modes.
- Phase H item H.1: roadmap-stretch mode-types implemented piecewise post-launch per public roadmap (cascade with discipline lock D-3, PROJECT-ARC.md §7: no mode-type added to launch commitment after Phase 5 opens).
