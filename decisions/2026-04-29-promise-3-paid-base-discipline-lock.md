# Decision — Promise 3 paid-base discipline-lock (paid-base + day-1-visible-BP + cosmetic-only across EA→1.0; never reverse)

**Date:** 2026-04-29
**Status:** Accepted
**Reversibility:** Hard
**Affects:** CONCEPT.md (Promise 3 architecture), [`decisions/2026-05-06-monetization-specifics-ratification.md`](2026-05-06-monetization-specifics-ratification.md) (extends Hard-class lock), [`decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md`](2026-04-28-paid-ea-single-product-supersedes-pivot.md) (operational artifact), [`concept/PROJECT-ARC.md`](../concept/PROJECT-ARC.md) §7 lock D-1, [`concept/atoa-vs-mtm/SYNTHESIS.md`](../concept/atoa-vs-mtm/SYNTHESIS.md) §"DA Reckoning #8 conditional"

---

## Decision

The paid-EA single-product is committed across the entire EA→1.0 window to the following monetization architecture, with no reversal permitted:

1. **Paid base.** The product is purchased once at $15-20 (PM-Fork-8 resolves specific tier). No transition to free-to-play during the EA→1.0 window. No demo-tier-becomes-product conversion. The base price is the access transaction.
2. **Day-1-visible Battle Pass.** The Battle Pass architecture lives in code from EA day 1. Players see the BP track from launch; cosmetics flow through it. The BP is not added later "when the audience is ready" — adding it later is what triggers the F2P-cosmetics anger pattern Player Complaint Atlas catalogued.
3. **Cosmetic-only.** Battle Pass content is cosmetic only: skins, voice-overs, particle styles, banner art, end-of-match flourishes, optional commander-portrait variants. No stat changes. No power purchasable. No commander unlocks behind paywall (commanders unlock through gameplay or are owned at base purchase). No towers / units / Demigods / Gods / Fusion recipes purchasable. No mode-types purchasable. No PvE difficulty / PvP rank / leaderboard entry purchasable.

These three commitments compose: paid-base + day-1-visible-BP + cosmetic-only is one architecture, not three independent ones. Reversing any of the three collapses the architecture into a different shape (paid+BP-without-cosmetic = pay-to-win; paid+cosmetic-only-no-BP = forfeits Promise 3 entirely; F2P+BP+cosmetic = re-introduces the F2P anger pattern). The lock preserves all three together.

## Context

The 4-round superaligned product-shape swarm's Devil's Advocate Reckoning #8 surfaced the load-bearing conditional: **Promise 3 collapses to convergent 5/5 across both paths under same conditional** — paid-base + day-1-visible-BP + cosmetic-only. Both the original 2026-05-07 pivot and the 2026-04-28 supersession converge on Promise 3 reaching its rated quality only when this architecture holds. (`concept/atoa-vs-mtm/round-3-turn-in.md` + `round-4-cycles/cycle-2-Q3-Q4.md` Q3 dialectic.)

The supersession (Accepted 2026-04-29) chose the paid-base path. This decision **operationally locks the architecture** so the path's Promise-3 quality cannot be silently reverted under in-EA pressure (e.g. revenue stress, audience-expansion temptation, BP-revenue-lift temptation through stat-tier addition). The discipline-lock is the structural defense against the same anti-alignment the swarm found in the 2026-05-07 pivot: commercial-mechanism (revenue) opposing player-experience-mechanism (player integrity).

The 2026-05-06 monetization-specifics-ratification (Hard-class) is the upstream source for the cosmetic-only / no-pay-to-win model-shape. This decision **extends that lock from the 1.0+ steady state into the EA window** — under the supersession, the BP is now day-1-visible, which the prior monetization decision did not specify because the prior product-shape (engine MVP, no EA window) did not have an EA window to specify.

## Alternatives considered

- **Option A — No discipline-lock; trust scope-discipline emergence in EA.** Avoids Hard-class additional lock. But the 4-round swarm Q3 dialectic explicitly named that paid-EA's discipline-mechanism is incentive-aligned only when the architecture is locked; without the lock, EA-revenue pressure can rationalize a free-trial-period-then-F2P shift, reverting to the F2P anger pattern. Not chosen.
- **Option B — Lock paid-base + cosmetic-only; defer BP-visibility to post-launch.** Cleaner against the prior monetization-specifics-ratification but breaks the swarm's Q3 finding that day-1-visible-BP is structural to Promise 3's 5/5 rating. Adding BP later is what generates the anger pattern; locking it as day-1 architecture is the structural defense. Not chosen.
- **Option C — Full architectural discipline-lock across EA→1.0 (chosen).** All three commitments locked together as one architecture. Reversing any requires written supersession; cascade-discipline tripwires fire on attempted silent edit.
- **Option D — Lock only through 1.0 ship; allow post-1.0 evolution.** Plausible but the load-bearing finding is that the architecture's quality compounds across the EA→1.0 window's audience-trust accumulation. Reversing post-1.0 erodes that accumulated trust by signaling "the discipline was a launch posture, not a product principle." Not chosen.

## Reason chosen

3x debug loop synthesis:

- **Loop 1 (critique):** Discipline-lock at this severity (Hard-class, no reversal) might be over-constraint. Real product evolution cases exist where post-launch monetization adjustments are right (e.g. cosmetic-only product later adds non-power QoL convenience that audience asked for). Risk that the lock prevents legitimate evolution. Risk that "cosmetic-only" is fuzzily defined at edges (e.g. is a cosmetic skin that has slightly-different audio cues a stat change? Is a banner-art unlock that displays match-history-stats a cosmetic or a UI-feature?). Risk that day-1-visible BP architecture in code from launch represents engine engineering work that compounds Phase E cost without obvious EA-revenue benefit.
- **Loop 2 (steelman):** The over-constraint risk is overweighted. The audience-trust accumulation argument is real and load-bearing per the swarm Q3 finding; reversibility softer than Hard would invite the kind of EA-revenue-pressure rationalization the lock structurally defends against. Edge-cases on "cosmetic-only" are real but addressable case-by-case under cascade discipline (each new addition is a written decision-file event; "is this still cosmetic-only" is a reviewable question per addition). The day-1-visible BP engineering cost is real but bounded — BP architecture is largely a UI surface plus a content-flow pipeline plus a season-rotation scheduler; engine-substrate work is one-time and small relative to the full Phase E implementation. Locking it day-1 in code prevents the "we'll add it later" trap that becomes the F2P anger pattern's source.
- **Loop 3 (synthesis):** Hard-class discipline-lock holds. Reversibility note acknowledges what reversal would cost; the lock preserves the architecture as one unit. Edge-case discipline (case-by-case "is this still cosmetic-only") becomes a continuous discipline rather than a one-time question.

## Reversibility note

**Hard.** Reversing any of the three commitments individually requires a written supersession decision per CLAUDE.md cascade rules. The supersession would need to articulate why the F2P anger pattern (Player Complaint Atlas catalogued) is no longer a structural risk; why the day-1-visible-BP architecture is mid-stream-replaceable without erosion of audience-trust; why the cosmetic-only / no-pay-to-win model-shape (already Hard-class per 2026-05-06 monetization-specifics-ratification) can be selectively relaxed. Cumulative cascade impact is large.

## Follow-ups

- Phase F item F.3 (PROJECT-ARC.md §5): Day-1-visible Battle Pass architecture lives in code from EA day 1. Engine implementation budgeted into Phase E.
- Phase F item F.4: Public refund-backed roadmap names the discipline-lock commitments as written contract with the audience-paying-in-advance.
- Phase J item J.1 + J.4 + J.5: post-1.0 monetization evolution must respect this lock; any attempted relaxation is a Hard-class supersession event, not a steady-state product decision.
- Steam-page draft (Phase F item F.1): names the discipline-lock commitments under "what we will not do" language — explicit "no F2P shift, no IAP plumbing for power, no pay-to-win, ever" framing.
