# Decision — Paid Early Access Single-Product (Supersedes 2026-05-07 Two-Product Pivot)

**Date:** 2026-04-28
**Status:** Accepted (ratified 2026-04-29 by PM autonomous-mandate go)
**Reversibility:** Hard
**Affects:** `decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md` (supersedes), `CONCEPT.md` (Promise 1 north-star edit), `concept/phase-5.md` (build-order), `concept/phase-6.md` (validation MVP), Phase 4 §4.8 exit-gate item #9 (engine lock), `CASCADE.md` (current work pointer), `decisions/2026-04-19-design-prototype-scope.md` (prototype reverts to port-source)

---

## Decision

Ship Ash to Altar as a single **paid Early Access** product on Steam at $15-20, built directly on the chosen engine substrate, with the prototype's preserved 50-55% deliverable-logic **ported across rather than re-shipped as a free Steam SKU**. Promise 1's north-star scope is cut by written precondition from seven feature-complete mode-types at launch to **two feature-complete mode-types at 1.0** (the swarm's strongest single nomination is Tower + PvP-Co-op, with the actual pair to be PM-chosen). The remaining five mode-types are framed as roadmap stretch with no public completion date. The "Mud to Myth" successor-product framing is dropped entirely; there is one product. The discipline mechanism is paid-EA's externalized refund-backed public roadmap, which operates the scope cut against revealed audience engagement in public.

This decision supersedes `decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md` (which is moved from **Proposed** to **Superseded** with this entry as the supersedor).

## Context

PM proposed the two-product free→premium pivot on 2026-05-07 to resolve the tension between (a) the HTML prototype's incompleteness and (b) the desire to ship something on Steam without engine commitment. Rather than ratify or reject the pivot directly, a 4-round superaligned agent swarm (R1: 12 agents in 3 waves; R2: 4 agents; R3: 5 agents; R4: 2 dialectic cycles; 3 inter-round alignment-checks) was run under PM autonomy mandate to test the pivot against alternatives, evidence, and converged failure modes. The swarm artifacts live in `concept/atoa-vs-mtm/`; the load-bearing output is `concept/atoa-vs-mtm/SYNTHESIS.md`.

The swarm did not converge on the originally proposed pivot. It converged on paid-EA single-product across genuinely different lenses (PM-economics, player-experience, Promise-1 reachability evidence) with different reasoning arriving at the same direction. This decision documents what the swarm found, what it could not resolve, and the recommended path with conditions.

## Alternatives considered

- **Option A — Original two-product pivot (AtoA-free → MtM-premium).** Ship AtoA as a free HTML/web-app on Steam first as concept-validation + discoverability vehicle, then ship Mud to Myth as a premium engine-built successor. Defended in `concept/atoa-vs-mtm/round-2/arguer-a-defend-pivot.md`; honest concessions present (wishlist-conversion empirical weakness, no clean solo-dev free-then-premium Steam-to-Steam case). Not chosen — see Reason chosen below.
- **Option B — Premium $15-20 single SKU with traditional 1.0 launch (no EA).** Skip the EA window; ship 1.0 directly. Strong on player-experience purity but kills the public scope-discipline mechanism that makes Promise 1's cut credible against revealed audience engagement. Not chosen.
- **Option C — Hybrid premium-base + free-benchmark-mode.** Paid base game with one mode free as audience-acquisition surface. Carries the pivot's commercial-mechanism / player-experience-mechanism anti-alignment in miniature; Promise-3 architecture cleanest under pure paid-base. Not chosen.
- **Option D — Hold the original pivot at full Promise 1 scope (no edit).** Promise-1 swarmer's reachability finding (no solo-dev shipper of seven mode-types in the surveyed evidence base; Stormgate failed at $40M with exactly the AtoA mode-spread; Battle Aces cancelled May 2025 under Tencent backing at narrower scope) makes this option's scope claim empirically indefensible. Not chosen.
- **Option E — Paid Early Access single-product at $15-20 with written Promise-1 scope cut (chosen).** Two-mode feature-complete commitment at 1.0; remaining five as roadmap stretch; paid-EA's public refund-backed roadmap as the discipline mechanism. Path is the operating layer; scope cut is the precondition.

## Reason chosen

The full 3x debug loop is enacted across the swarm's R1-R4 structure; the load-bearing synthesis lives in `concept/atoa-vs-mtm/SYNTHESIS.md` §"Why this recommendation". Compressed:

**Loop 1 — aggressive critique.** The swarm's Devil's Advocate pass (`da-pass.md`) attacked the original pivot's strongest claims: pivot-self-indictment (the pivot itself is a mid-dev pivot under Agent 6's taxonomy, the very thing player-complaint Atlas anger keys to); Stormgate-AtoA resource asymmetry inversion (a $36M studio shipped incomplete on the same scope claim); F2P-cosmetics structural anger independent of execution; paid-EA selection bias on alternative-path evidence. The Promise-1 swarmer found no solo-dev shipper of >1 mode-type in the surveyed record, making the seven-mode promise empirically indefensible regardless of product-shape.

**Loop 2 — steelman.** The R3 cycle developed both paths' strongest reads. The pivot's strongest argument is the WC3→Dota2 lineage as the historically-validated funder pattern for lobby substrate (Promise-2 swarmer Finding 10). Paid-EA's strongest arguments are cash-flow timing, single-trunk focus, externalized scope-discipline via public roadmap, reference-class match for TW-veteran target audience, storefront-narrative coherence, and Promise-3 architectural fit under DA Reckoning #8.

**Loop 3 — synthesis.** PM-lens, Player-lens, and Promise-2 swarmer converged on paid-EA from different reasoning. The WC3→Dota2 pattern survives only under preconditions the pivot violates by construction (thin substrate at free tier; distinct commercial successor) — the pivot's "MtM inherits AtoA verbatim" framing fails the second condition; AtoA's seven-mode promise at the free tier fails the first. R4 Cycle-2 Q3 surfaced the load-bearing finding neither R2 arguer fully named: the pivot's commercial mechanism (wishlist conversion needs MtM visibility) is anti-aligned with its player-experience mechanism (player integrity needs MtM invisibility); the architecture itself requires the discipline crack. Paid-EA's discipline (roadmap delivery) is incentive-aligned with its commercial mechanism (revenue from EA sales). Risk-of-ruin asymmetry tightens rather than drives the verdict; Promise 3 is convergent at 5/5 across both paths under the same conditional, removing it as a discriminator. The reachability inversion (Promise 1 unreachable on either path absent a written cut) makes the scope-cut question load-bearing on the path question, not the reverse.

The swarm's confidence is **medium-high overall**, with high confidence on lens-convergence and reachability inversion, medium confidence on the specific mode-type pair, and low confidence on PM-temperament-dependent and private-runway-dependent variables.

## Reversibility note

**Hard.** Reversing this decision after ratification would mean: undoing the supersession of the 2026-05-07 pivot; restoring the two-product framing in CONCEPT.md; reverting the Promise 1 scope edit; reopening Phase 4 exit-gate item #9 under different engine-economics assumptions; rewriting Phase 5 build-order; potentially re-architecting the prototype to ship as a free Steam SKU rather than serve as a port-source. Cascade impact is large.

**Reversal conditions are explicitly named** in `concept/atoa-vs-mtm/SYNTHESIS.md` §"Reversal conditions": (1) PM personally verifies multi-year runway and temperament for anti-monetization free-product discipline; (2) the pivot is re-architected to honor WC3→Dota2 preconditions (thin substrate, distinct successor); (3) independent evidence emerges of solo-dev Steam-to-Steam free→premium wishlist conversion in the TW genre at rates that fund engine work; (4) PM weights the WC3→Dota2 historical pattern higher than the lens convergence (a coherent priors-disagreement, not a swarm-resolvable variable).

## Follow-ups

This decision unblocks/requires the following cascade-discipline work, enumerated in `SYNTHESIS.md` §"Follow-ups if accepted" (12 items). High-priority subset:

1. Edit CONCEPT.md Promise 1 from seven feature-complete mode-types at launch to the cut commitment; reopen Phase 1's vision/promise framing under cascade discipline.
2. File `decisions/2026-04-28-promise-1-scope-cut.md` capturing the cut, rationale, chosen mode-type pair, and the residual five as roadmap stretch.
3. File `decisions/2026-04-28-promise-3-paid-base-discipline-lock.md` committing the project to never reverse paid-base + day-1-visible-BP + cosmetic-only across the EA→1.0 window.
4. Re-supersede `decisions/2026-04-19-design-prototype-scope.md` clarifying the prototype's preserved 50-55% deliverable-logic ports to engine paid-EA work rather than ships as free Steam SKU.
5. Reopen Phase 4 §4.8 exit-gate item #9 (engine lock) — engine choice (Godot 4 / Unity / Unreal) is now in scope for AtoA Phase-5 prep, no longer deferred behind a hypothetical MtM.
6. Rewrite CASCADE.md current-work-pointer to AtoA Phase-4 close + Phase-5 engine-prep with paid-EA shape; trim older pointer blocks per doc hygiene.
7. Rewrite `concept/phase-5.md` build-order to single-product paid-EA shape with the chosen mode-type pair as EA-launch feature-complete commitment.
8. Rewrite `concept/phase-6.md` validation MVP to paid-EA launch event with metrics: review velocity, EA→month-1 wishlist conversion, roadmap-trim audience response.
9. Update CONCEPT.md hub: collapse two-product framing block to single-product paid-EA shape; drop "Mud to Myth" successor-product framing.
10. Charter a Steam-page draft artifact naming the EA-launch feature-complete commitment, roadmap stretch, and discipline commitments (no F2P shift, no IAP plumbing in EA window) — the externalized refund-backed contract that operates the cut.

PM ratification is the gating event; none of the above is executed under this decision until the PM moves Status from **Proposed** to **Accepted**.
