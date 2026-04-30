# Round 3 — PM-Lens (Commercial / Development-Economics)

**Agent:** R3 PM-Lens thinker | **Date:** 2026-04-28 | **Inputs read:** charter, R1 turn-in, DA pass, R2 Arguer A + B, R2 Swarmer A + B, alignment-check-2. | **Live differentiators inherited from R2:** Promise 1 (feature-completeness reachability) and Promise 2 (lobby-substrate funding mechanism). Promise 3 is convergent at 5/5 under the shared paid-base + day-1-visible-BP + cosmetic-only conditional and is not a discriminator at this lens.

---

## 1. PM-lens framing

The PM-economics lens privileges what a solo developer running a multi-year project actually has to manage day-to-day: when revenue arrives relative to when work is done, where a single human's finite focus has to be spent, where a wrong call at month 12 is recoverable and where it is terminal, and which path makes the word "no" cheaper to say to feature creep. It treats the dev as a one-person org with no payroll runway beyond personal savings, no marketing department, and no second draft on first impressions. It privileges paths that externalize commitment so the solo dev cannot lie to themselves about scope, and paths whose cash flow can absorb the natural year-six fatigue cliff that has killed more indie projects than any design decision. It cannot see fun, feel, novelty, or whether the design is actually good — the player-lens owns those. It also cannot adjudicate whether the PM has the tolerance for paid-EA's public review-velocity scrutiny vs. the patience for the two-product trunk to actually conclude — that is a temperament question this lens flags but does not answer.

---

## 2. Findings

### FINDING-3PM-1: Cash-flow arrival timing is the largest economic discriminator and it strongly favors paid-EA
- **CLAIM:** Paid-EA generates revenue from day one of the first commercial product (FINDING-2WB-6: ~20% wishlist→month-1-sale conversion median; FINDING-2WB-10: TD-adjacent solo paid-EA precedents at $20K-70K year-one). The pivot defers all revenue until MtM ships — empirically a multi-year gap whose bridge funding (personal savings) is the single most-documented modal indie failure mode in Agent 6's tombstone corpus.
- **SOURCE:** FINDING-2WB-6, FINDING-2WB-10, FINDING-2B-11; R1 DA Section A-3 (Legion TD 2 800 DAU as floor); Agent 6 tombstones; Caves of Qud postmortem (FINDING-2WB-4).
- **STRENGTH:** high
- **CONFIDENCE:** high
- **COUNTER-EVIDENCE:** FINDING-2A-2 reframes the HTML 50-55% as already-shipped Product-1 logic, which is a real time-to-first-revenue advantage if AtoA-free can be released within months rather than years. The pivot's gap is shorter than it looks if AtoA-free ships fast and the dev has runway to bridge to MtM.
- **PROMISE-1 RELEVANCE:** 4
- **PROMISE-2 RELEVANCE:** 5
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Cash-flow timing directly funds the lobby-substrate engineering Promise 2 requires; Promise 1's seven-mode polish surface is materially harder to fund from savings than from EA revenue.

### FINDING-3PM-2: The two-product pivot has two abandonable subprojects; paid-EA has one focused trunk
- **CLAIM:** The pivot decision doc Loop-1 names the trap pattern explicitly: AtoA absorbs all attention, MtM never starts. Solo-dev abandonment of a second product mid-development is a documented modal failure of the indie cohort (Arguer A concession (d), uncontested). Paid-EA collapses two abandonable surfaces into one trunk where every commit advances the only product the dev will ever ship from this design.
- **SOURCE:** Pivot decision doc Loop-1; Arguer A honest concession (d); FINDING-2WB-9 (single-roadmap EA cadence); Bay 12 / Caves of Qud / Stardew patterns are all single-trunk.
- **STRENGTH:** high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** FINDING-2A-11 reframes the two-product structure as an empirical-test affordance — AtoA-free tests the creator-coverage contradiction before MtM commits resources. That genuine optionality is real, but it is purchased at the cost of two completion events instead of one.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 4
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Promise 1's seven-mode-types completion is the highest-burnout-risk surface in the entire concept; whichever path concentrates the dev on a single trunk is structurally more likely to actually deliver the promise.

### FINDING-3PM-3: The marketing-burden split between the two paths is asymmetric and under-examined
- **CLAIM:** The pivot requires the dev to run *two* marketing campaigns, eighteen-plus months apart, with the second campaign's effectiveness depending on a wishlist-conversion rate (Arguer A concession (a)) that has no positive solo-dev TW-genre reference class (Swarmer A honest negative result: "could not surface a clean solo-dev free-then-premium two-product Steam exemplar"). Paid-EA requires one campaign whose marketing surface is the EA→1.0 roadmap itself — a free narrative arc the dev gets to ride for the duration of EA. The pivot's marketing surface is two cold starts; paid-EA's is one cold start with a built-in story.
- **SOURCE:** Arguer A concession (a); Swarmer A honest-negative section; FINDING-2WB-9 (EA cadence as marketing surface); FINDING-1-09-6 (TW creator coverage debuff applies to both cold starts).
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Swarmer A's FINDING-2WA-5/6/7 (prologue trick, free-weekend wishlist lift, Next Fest conversion) document that free-predecessor-funnel mechanics are real. The pivot's marketing surface is genuinely doubled but the second campaign is not starting from zero — it inherits AtoA-free's wishlist pool. Whether that inheritance is materially valuable is the wishlist-conversion question Arguer A concedes is empirically weak.
- **PROMISE-1 RELEVANCE:** 3
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Two campaigns is two opportunities for a solo dev with no marketing background to fumble launch optics; the marketing-surface question is a solo-dev capacity question, not a strategy question.

### FINDING-3PM-4: Decision-reversibility cost at month 6 / 12 / 24 favors paid-EA at the early checkpoints
- **CLAIM:** Paid-EA is reversible at month 6 (pause updates, refund-window stays open, scope can be cut publicly via roadmap revision) and at month 12 (graduate-to-1.0-early is a recognized escape hatch — Hades, Slay the Spire, Manor Lords all used variants). The pivot is reversible at month 6 (HTML iteration is cheap to redirect) but materially less reversible at month 12 because AtoA-free's launch event is a one-shot perception-anchor that locks in audience expectations for MtM. The free-Steam-as-trash-default prior (Arguer A concession (c)) cannot be unflipped after launch.
- **SOURCE:** FINDING-2WB-9 (EA roadmap cadence); FINDING-2WB-5 (Steam free→paid is one-way; informational even if AtoA-free is HTML-hosted); Arguer A concession (c); Hades / Slay the Spire EA→1.0 trajectories.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** At month 24, paid-EA that has gone mixed is harder to recover from than a free-AtoA that simply has low concurrent (Arguer B concession on review-velocity-guillotine; FINDING-1-06-9). The reversibility question inverts at the late checkpoint: paid-EA is more reversible early, the pivot is more forgiving late.
- **PROMISE-1 RELEVANCE:** 4
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 3
- **RELEVANCE NOTE:** The PM has to pick which checkpoint matters more — early-reversibility (paid-EA) or late-forgiveness (pivot). For Promise 1's seven-mode commitment, early-reversibility is more valuable because scope cuts at month 6-12 are how this commitment actually gets honored.

### FINDING-3PM-5: Paid-EA externalizes "no" to feature creep more aggressively than the pivot
- **CLAIM:** Paid-EA's public roadmap is a written, dated, refund-backed contract with an audience that has paid in advance — every scope addition must be either justified to that audience or rejected in public. The pivot's HTML iteration phase has no equivalent external commitment device; scope is bounded only by the dev's own discipline. R1 surfaces that solo-dev abandonment correlates with un-externalized scope (Sanctum 2 cut-don't-stack lesson, FINDING-1-03-1; Stormgate's publisher-pressure-driven incomplete-ship as the inverse failure). Paid-EA gives the dev a structural ally against feature creep that the pivot does not.
- **SOURCE:** FINDING-2WB-9; FINDING-1-03-1; Arguer B Steelman (single-roadmap honesty); Caves of Qud 9-year EA discipline as positive reference (FINDING-2WB-4).
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** Public roadmaps can themselves become commitment devices that prevent good cuts — "we promised seven mode-types" becomes the trap rather than the discipline. Stormgate's roadmap was the failure mechanism, not the discipline. The externalization is only valuable if the dev is willing to publicly cut what the roadmap promised.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Promise 1's seven-mode commitment is the single largest scope-discipline question in the project; the path that gives the dev a structural "no" surface is meaningfully more likely to honor the promise.

### FINDING-3PM-6: Risk-of-ruin asymmetry — paid-EA's worst case is a 60% Steam score, the pivot's worst case is a finished free product nobody converts
- **CLAIM:** Paid-EA's terminal failure mode is documented (FINDING-1-06-9, Stormgate, Phoenix Point): mixed reviews compound with refund rage and discoverability collapse, killing the product within months. The pivot's terminal failure mode is the wishlist-conversion bet failing — AtoA-free ships, generates real engagement, and converts wishlist→MtM at the empirically observed near-zero solo-dev rate (Swarmer A honest-negative). In that scenario the dev has shipped two products and earned the revenue of zero. Paid-EA's worst case is recoverable through scope cuts and re-launch attempts; the pivot's worst case is two completed projects with no revenue and no path to recovery because the design has already been validated and rejected.
- **SOURCE:** Arguer A concession (a); Arguer B concession on review-velocity; Swarmer A honest-negative; FINDING-1-06-9; FINDING-2B-02.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Arguer A FINDING-2A-10 correctly notes AtoA-free buffers MtM with goodwill — even if conversion is low, MtM launches into a world where the design is known-good and the audience is partially primed. Paid-EA's worst case has no equivalent buffer; the design's reception and the product's reception are the same event.
- **PROMISE-1 RELEVANCE:** 3
- **PROMISE-2 RELEVANCE:** 4
- **PROMISE-3 RELEVANCE:** 3
- **RELEVANCE NOTE:** Promise 2's lobby-substrate funding requires a path that doesn't terminate at a finished product with no revenue; the pivot's terminal scenario specifically un-funds Promise 2.

### FINDING-3PM-7: Burnout-cliff timing differs structurally — paid-EA front-loads it, pivot back-loads it
- **CLAIM:** Paid-EA's high-stress phase is the EA launch window (months 0-3) where review velocity is set; after that the dev has paying customers, validated demand, and roadmap autonomy. The pivot's high-stress phase is MtM development (months 12-24+) which is also the highest-burnout-risk phase of any indie project (Arguer A concession (f)). Paid-EA aligns its hardest moment with the dev's freshest energy; the pivot aligns its hardest moment with the dev's most-depleted state, after AtoA-free has already consumed eighteen months of focus.
- **SOURCE:** Indie postmortem corpus (Agent 3 GDC findings); Arguer A concession (f); FINDING-2WB-4 (Caves of Qud 9-year sustainability under paid-EA shape).
- **STRENGTH:** medium
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** The pivot's MtM phase inherits a validated design and a known audience, which materially lowers cognitive load relative to a from-scratch second project. The "freshest energy first" framing assumes AtoA-free does not itself burn the dev out before MtM begins — which is exactly the trap pattern Loop-1 of the pivot doc names.
- **PROMISE-1 RELEVANCE:** 4
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Promise 1 requires sustained polish work over years; the path whose hardest phase is front-loaded is more likely to actually reach the polish-complete bar.

### FINDING-3PM-8: Lobby-substrate funding is materially better-served by paid-EA than by the pivot's two-shot architecture
- **CLAIM:** R1 DA Reckoning #9 elevated lobby-substrate funding as load-bearing-unsolved. Arguer A FINDING-2A-5 proposes a two-shot operationalization (cheap substrate in AtoA-free, engineered substrate in MtM). Arguer B FINDING-2B-11 funds the substrate from EA day-one revenue. The PM-economics read: the two-shot architecture defers substrate engineering to a product whose funding is the operative bet; paid-EA funds substrate engineering from revenue that has already arrived. The pivot's substrate plan is contingent on wishlist conversion succeeding; paid-EA's is contingent only on the EA reaching the same revenue floor that Legion TD 2 and Caves of Qud reached at solo-or-small-team scale.
- **SOURCE:** R1 DA Reckoning #9; FINDING-2A-5; FINDING-2B-11; Legion TD 2 (FINDING-2WB-2); Caves of Qud (FINDING-2WB-4).
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Arguer A's two-shot framing is not refuted — if wishlist conversion does materialize, the two-shot architecture genuinely funds substrate at higher quality than paid-EA's day-one revenue can. The question is whether the PM economics tolerate the conditional structure of "fund substrate IF conversion succeeds" vs the unconditional "fund substrate from revenue that exists."
- **PROMISE-1 RELEVANCE:** 2
- **PROMISE-2 RELEVANCE:** 5
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Direct Promise-2 differentiation. The substrate-funding question is the cleanest single PM-economics discriminator on Promise 2.

### FINDING-3PM-9: Feature-completeness reachability favors paid-EA's phased delivery over the pivot's two parallel completion events
- **CLAIM:** Promise 1 requires polish-complete coverage of seven mode-types. Paid-EA's reference class (Hades, Manor Lords, Slay the Spire — FINDING-2B-08) demonstrates that solo-or-small-team devs reach feature-complete state through a public phased delivery whose pacing matches dev capacity. The pivot requires reaching feature-complete state twice — once at AtoA-free's launch (HTML-deliverable polish on seven modes) and again at MtM's (engine-deliverable polish on the same seven modes). FINDING-2A-7's claim that HTML iteration is materially cheaper is real for design validation but unbenchmarked at solo-deliverable polish across seven mode-types (Arguer A concession (e): no reference-class HTML game shipped seven mode-types at solo polish).
- **SOURCE:** FINDING-2B-08; Arguer A concession (e); FINDING-2A-7; Hades / Manor Lords / Slay the Spire trajectories.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** FINDING-2A-7 is correct that HTML iteration economics are genuinely cheaper for design validation; if the AtoA-free polish bar is read as "design-validation polish" rather than "shippable-product polish," the two completion events are not symmetric and the pivot's burden is materially lower than this finding implies. The dispute is over what HTML-deliverable polish actually means.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 2
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Direct Promise-1 differentiation. The reachability question is the cleanest single PM-economics discriminator on Promise 1.

### FINDING-3PM-10: The wishlist-conversion bet is the pivot's single point of failure and has no positive solo-dev TW-genre evidence
- **CLAIM:** Arguer A's defense rests on AtoA-free generating wishlist conversion to MtM at rates that fund engine engineering. Arguer A concession (a) names this as the pivot's load-bearing assumption. Swarmer A's honest-negative section explicitly states no clean solo-dev free-then-premium Steam exemplar was found; the cited precedents (Vampire Survivors itch.io→Steam, DotA→Dota 2, Auto Chess→TFT) are all (a) studio-scale or platform-shifted, not solo-Steam-to-Steam, (b) successful under conditions a solo dev cannot replicate (Valve hiring IceFrog, $36M-funded successors). The PM-economics read: this is a single point of failure with no positive precedent, and concentrating multi-year effort behind a load-bearing variable that has no positive precedent is the structural shape of indie-cohort modal failure.
- **SOURCE:** Arguer A concession (a); Swarmer A honest-negative; FINDING-2B-02; pivot decision doc Loop-2.
- **STRENGTH:** high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** Absence of positive precedent is not absence of possibility — first cases exist by definition. FINDING-2A-8 reframes the bet as audience-overlap rather than free-to-paid-sequel-conversion, which is a definitionally weaker bet than B-5 attacks. If the PM has independent confidence in the audience-overlap framing, the empirical absence is less damaging.
- **PROMISE-1 RELEVANCE:** 3
- **PROMISE-2 RELEVANCE:** 5
- **PROMISE-3 RELEVANCE:** 4
- **RELEVANCE NOTE:** Promise 2's funding mechanism collapses if the wishlist-conversion bet fails; Promise 3's BP storefront has no audience to monetize. This finding is the bridge between the wishlist-conversion empirical gap and both differentiated promises.

---

## 3. Path comparison matrix

| Dimension | Pivot (free AtoA → paid MtM) | Paid-EA (single product) |
|---|---|---|
| **Cash-flow arrival** | Multi-year gap; revenue at MtM launch only; bridge funded by personal savings | Day-one EA revenue; ~20% wishlist→month-1 conversion median; revenue funds development |
| **Burnout cliff** | Back-loaded onto MtM phase (months 12-24+) when dev is most depleted | Front-loaded onto EA launch window (months 0-3) when dev is freshest |
| **Marketing surface** | Two cold starts, 18+ months apart; second depends on unproven wishlist transfer | One cold start with EA→1.0 roadmap as built-in continuous narrative arc |
| **Decision-reversibility (mo 6)** | High (HTML iteration cheap to redirect) | High (roadmap revision public and accepted) |
| **Decision-reversibility (mo 12)** | Medium-low (AtoA-free launch perception locks in) | High (early-1.0 graduation is a recognized escape hatch) |
| **Decision-reversibility (mo 24)** | Medium (MtM scope still adjustable; AtoA buffers) | Low (mixed reviews compound with refund rage) |
| **Scope-discipline / "no" externalization** | Internal discipline only; HTML phase has no external commitment device | Public refund-backed roadmap forces audience-justified scope cuts |
| **Risk-of-ruin worst case** | Two products shipped, zero revenue (wishlist conversion fails) — terminal | 60% Steam score on EA — recoverable via scope cuts and re-launch |
| **Lobby-substrate funding (Promise 2)** | Conditional on wishlist conversion; two-shot operationalization if conversion succeeds | Funded from EA day-one revenue at Legion-TD-2-class floor |
| **Feature-completeness path (Promise 1)** | Two completion events at two polish bars; HTML seven-mode-polish unbenchmarked | One completion event under reference-class precedent (Hades / Manor Lords / Slay the Spire) |
| **Promise 3 conditional fit** | Honored cleanly via MtM-paid-base-day-1-BP | Honored cleanly via paid-EA-base-day-1-BP |
| **Single point of failure** | Wishlist-conversion rate (no positive solo-dev TW-genre precedent) | Review-velocity floor at EA launch (recoverable) |

---

## 4. PM-lens verdict

The PM-economics lens favors **paid-EA single-product** on the live R3 differentiators and on the lens's privileged dimensions. Cash-flow timing, single-trunk focus, externalized scope discipline, lobby-substrate funding, and feature-completeness reachability all read more cleanly under paid-EA than under the pivot's two-product architecture. The pivot's worst case is structurally terminal (two products shipped, revenue conditional on a load-bearing bet with no positive solo-dev TW-genre precedent); paid-EA's worst case is structurally recoverable (a poorly-received EA launch can be scope-cut, re-launched, or graduated early). The wishlist-conversion bet underneath the pivot is the single largest unhedged variable in the entire concept and concentrating multi-year solo effort behind it without precedent is the shape of indie-cohort modal failure.

**Blind spots this lens cannot see and should be flagged:**

The lens cannot see whether the design is actually fun — the player-lens owns that, and a path that is economically optimal but lands on a design the player-lens rejects is worse than a path with worse economics and a design that lands. The lens cannot adjudicate the temperament question — whether the PM has the stomach for paid-EA's public review-velocity scrutiny vs. the patience for two completion events, and the answer is the PM's, not this lens's. The lens cannot calibrate the *quality* of the wishlist-conversion bet's downside — Arguer A's FINDING-2A-10 (AtoA-free as goodwill-bank) is a real buffer that the pivot has and paid-EA does not, and if the PM weights that buffer highly the verdict shifts. The lens treats HTML iteration economics as cheaper for design validation but more expensive for double-completion; the *design-validation-only* read of HTML (Arguer A FINDING-2A-2's framing) is not refuted, and if the PM accepts that AtoA-free is honestly a marketing artifact rather than a shippable product, the two-completion-events critique softens materially. Finally, the lens does not weigh the *learning value* of the pivot — building two products teaches the dev things about engine work, scope discipline, and audience formation that one product does not, and that career-capital accumulation has real value the lens cannot price.

The cleanest read available at this lens: paid-EA is the path the lens recommends, but the recommendation is conditional on (a) the design being good enough to survive review-velocity scrutiny — a player-lens question, (b) the PM having genuine appetite for public-EA cadence — a temperament question, and (c) the wishlist-conversion bet being honestly weighted at the empirical evidence the swarm has surfaced rather than at the pivot's reframed audience-overlap optimism. If any of those three conditions is closer to the pivot's framing than the lens has assumed, the verdict tightens or inverts.

---

*End of PM-lens turn-in. Output: `C:\TW.AtoA\concept\atoa-vs-mtm\round-3\pm-lens.md`. Conceptual / refinement / educate / ask / repeat — no imperatives toward the human PM.*
