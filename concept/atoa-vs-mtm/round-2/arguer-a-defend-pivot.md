# Round 2 — Arguer A: Defense of the AtoA-first → MtM-successor Pivot

**Agent role:** Arguer A (defends the current proposed pivot in `decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md`)
**Date:** 2026-04-28
**Inputs treated as load-bearing:** R1 turn-in (`round-1-turn-in.md`), DA pass (`da-pass.md`), pivot decision doc.
**Coherence-diff with R1:** Treats R1's reconciled HTML deliverable-logic figure (~50–55%) as load-bearing rather than the headline 65%. Treats R1 DA Reckoning #1 (substrate-pivot vs identity-pivot distinction) and #8 (Promise-3 conditional resolution) as load-bearing scaffolds for the defense. Challenges R1's implicit framing that the Stormgate resource asymmetry is primarily a *quality-bar* problem — reframes it as a *commitment-window* problem where AtoA's structural posture is asymmetrically advantaged. Does not contest the convergence-as-source-amplification downgrade on the lobby gap; accepts it and argues the defense survives even at the downgraded gap-size.

---

## 1. Steelman — strongest version of the pivot's logic

The pivot's deepest logic is that it converts the project's largest single liability — the gap between a structurally complete *concept* and an unproven *playable artifact* — into the project's largest single asset, by treating the HTML build as a public proof rather than a private prototype. Every R1 finding about underbaked launches (1-08-3 Stormgate, 1-06-2 mid-dev pivots, 1-06-9 no-recovery-from-incomplete) describes a failure mode where the *paid product* shipped before the *design* was proven at scale. The two-product sequence inverts this: AtoA-as-free is the design-proof, executed in the lowest-cost substrate where iteration is fastest and where shipping incomplete carries no monetary trust-breach with the audience. MtM-as-premium then ships *after* the design has been validated by real player behavior on a free Steam release — which is the inverse of the Stormgate posture (raise money, ship incomplete, hope) and the inverse of the Defenders-of-Ardania posture (ship paid, get reviewed, die).

The second axis of the defense is that the pivot is the only product-shape in the alternative set that *does not* require the solo dev to clear a Hades-class quality bar at first contact with the market. Alternative 1 (paid EA) and Alternative 2 (premium $15-20 launch) both load the entire commercial outcome onto a single launch event that has to clear a quality bar set by Clair Obscur, Hollow Knight Silksong, and Manor Lords — products with team sizes, art budgets, and IP-equity profiles that a solo dev has no path to match on a first IP. The pivot's free-then-premium architecture decouples *concept validation* from *quality validation*: AtoA only has to clear "the design works as a complete game" (a bar the HTML prototype is already two-thirds of the way to), while MtM only has to clear "engine-grade execution of an already-validated design" (a much narrower scope of fresh creative risk than a from-scratch premium launch). The R1 DA pass attacks the pivot as itself a mid-dev pivot, but DA Reckoning #1 already resolved this — the substrate-pivot is not the identity-pivot Agent 6's tombstone corpus describes. The dead games pivoted *what game they were*; AtoA's pivot keeps the design constant and changes the substrate from private to public.

The third axis is that the pivot is the only product-shape that operationalizes Promise 2's lobby-substrate-cost problem. The R1 DA pass (Reckoning #9) accepts that lobby-substrate funding is unsolved historically outside Blizzard subsidy. A single-product premium launch has to fund that substrate from a single revenue event; a paid-EA product has to fund it from a small high-intent cohort that may not include the SC1/WC3-recognizability audience the substrate is *for*. The free-AtoA-first architecture funds the lobby substrate from a *different* mechanism — wishlist conversion to MtM — and lets the substrate be operated at AtoA-scale (Steam Lobby APIs, P2P, no central state) before being engineered at MtM-scale. Promise 2's customizability layer gets two shippings: a cheap-substrate prototype version in AtoA where the design is validated, and a polished version in MtM where the engineering can be funded by the proven-audience-demand signal AtoA generated. No other product-shape in the alternative set affords this two-shot operationalization of the most expensive promise.

---

## 2. Findings

### FINDING-2A-1: The substrate-vs-identity pivot distinction is real and load-bearing
- **CLAIM:** R1 DA Reckoning #1 correctly distinguishes substrate-pivot (HTML→engine, design constant) from identity-pivot (OMD!U MOBA→co-op, DD2 MOBA→TD, design abandoned), and the empirical kill mechanism in Agent 6's tombstone corpus is identity-pivot, not substrate-pivot.
- **SOURCE:** R1 DA Reckoning #1; Findings 1-06-2, 1-06-9; pivot decision doc Loop-2 steelman.
- **STRENGTH:** high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** DD2 reversed an explicit no-MTX promise (1-06-7) — that is closer to a commitment-pivot than a design-pivot, and AtoA's free-no-IAP-then-paid-MtM commitment structure could be read the same way if not carefully framed.
- **PROMISE-1 RELEVANCE:** 4
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 4
- **RELEVANCE NOTE:** Defends the pivot's structure against the strongest single R1 indictment by surfacing the conceptual category mismatch in the indictment's evidence base.

### FINDING-2A-2: HTML 50-55% deliverable-logic is *more* than enough for a free-product proof
- **CLAIM:** The reconciled R1 figure (50-55% deliverable-logic preserved + 10-15% spec-blocked + 30-35% rebuild) is read in the pivot's frame as 50-55% of *Product 1's* logic already shipped, not 50-55% of a port to *Product 2*. As a free-Steam-product budget, that figure is unprecedented for solo-dev concept-validation surface.
- **SOURCE:** R1 reconciled HTML-audit number; Agent 1 + Agent 7 readings.
- **STRENGTH:** high
- **CONFIDENCE:** high
- **COUNTER-EVIDENCE:** The 30-35% rebuild surface for AtoA-as-product (rendering, transport, polish) is non-trivial and the spec-blocked 10-15% (fusion execution, ability targeting, cosmetics) requires concept-fidelity decisions that have not been made.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Reframes R1's apparent downgrade as a confirmation of the pivot's productizability calculus — the same number that hurts the port-to-engine story helps the ship-AtoA-as-product story.

### FINDING-2A-3: Stormgate's resource asymmetry runs the *wrong direction* against the pivot
- **CLAIM:** R1 DA C-1 / Reckoning #4 frames the $36M-vs-solo gap as a quality-bar gap. The pivot's frame inverts: Stormgate's resources came with publisher pressure, marketing-window commitments, and team-conflict-resolution overhead that *forced* premature ship. AtoA's solo-dev posture *cannot* be forced to ship by external capital structure. The asymmetry favors the pivot on the variable that actually killed Stormgate (commitment-window), not on the variable R1 framed (polish budget).
- **SOURCE:** R1 DA Section A-10, Reckoning #4 / #11; Finding 1-08-3.
- **STRENGTH:** high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Solo dev has no external commitment window, but also has no external accountability; "no forced ship date" can become "no ship date." Abandoned solo projects are the modal failure of the indie cohort, not the Stormgate cohort.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 3
- **RELEVANCE NOTE:** Directly addresses the R1 reckoning the synthesis flagged as load-bearing; reframes the asymmetry from a deficit to a structural advantage on the specific axis that produced Stormgate's failure mode.

### FINDING-2A-4: Promise 3's resolution is cleaner under the pivot than under the alternatives
- **CLAIM:** R1 DA Reckoning #8 resolves the 1-08-23 vs 1-06-1 contradiction with the conditional "paid-base + day-1-visible-BP + cosmetic-only." The pivot honors this conditional *more cleanly* than alternatives because (a) MtM is paid-base by construction, (b) BP is day-1-visible on MtM (not retrofitted), (c) the existing cosmetic-only ratification migrates intact, and (d) AtoA-as-free has no monetization at all, eliminating the "change-from-baseline" anger vector that 1-08-23 names as the actual failure mechanism.
- **SOURCE:** R1 DA Reckoning #8; Findings 1-08-23, 1-06-1, 1-06-7; pivot decision doc Fork A.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** The R1 brief's suggestion that "Promise 3 only resolves cleanly under paid-base" is partially correct — but the brief's claim that "the pivot has free base, which conflicts" misreads the architecture. AtoA-free is not the BP-bearing product; MtM-paid is. The two-product structure satisfies the conditional by routing each promise component to the product where it can be honored.
- **PROMISE-1 RELEVANCE:** 1
- **PROMISE-2 RELEVANCE:** 1
- **PROMISE-3 RELEVANCE:** 5
- **RELEVANCE NOTE:** The cleanest defense of Promise 3 under the pivot — addresses the brief's strongest specific challenge by surfacing that the architecture *is* what the conditional asks for, not a violation of it.

### FINDING-2A-5: The lobby-substrate funding mechanism is uniquely available under the pivot
- **CLAIM:** R1 DA Reckoning #9 names lobby-substrate funding as unsolved. The pivot's structure provides a non-Blizzard funding mechanism: AtoA's free-Steam release operates the substrate at low-cost (Steam Lobby APIs, P2P-host-driven, no central server) at a scale that proves demand; MtM's premium revenue then funds the engineered version. No other shape in the alternative set provides a two-shot operationalization of substrate cost.
- **SOURCE:** R1 DA Reckoning #9; Finding 1-06-8 (Blizzard-subsidized historical precedent); pivot decision doc Fork B.
- **STRENGTH:** medium
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Steam Lobby APIs do not solve creator IP stewardship, hostbot-equivalent infrastructure, or long-tail moderation cost. The two-shot operationalization assumes wishlist conversion from AtoA to MtM materializes — which is the operative bet, not a resolved variable.
- **PROMISE-1 RELEVANCE:** 2
- **PROMISE-2 RELEVANCE:** 5
- **PROMISE-3 RELEVANCE:** 1
- **RELEVANCE NOTE:** Promise-2-specific defense; the only operationalization in the alternative set that funds substrate cost from a non-launch-window revenue event.

### FINDING-2A-6: Paid-EA's review-velocity floor is harder to clear than free-launch's discoverability floor
- **CLAIM:** R1 Steelman B-2 surfaces that paid-EA exposes the project to review-velocity collapse the moment quality slips, with no recovery path (Finding 1-06-9). The pivot's free-AtoA shape has no review-velocity floor in the same sense — Steam free games are forgiven thin features in a way paid-EA games are not. The Hades reference class (Alt 1) is selection-confounded: those products had pre-existing dev IP equity (Supergiant's Bastion/Transistor/Pyre lineage), which a first-IP solo dev cannot inherit.
- **SOURCE:** R1 DA Section B-2; Finding 1-10-1; Finding 1-06-9; Hades reference-class context.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Free Steam games carry their own perception debuff ("low-effort default"), which the pivot decision doc Loop-1 flagged. The dichotomy "free-forgiveness vs paid-scrutiny" is real but not a free pass — AtoA still has to clear a "this is a complete game" perception bar against the free-Steam-as-trash-default prior.
- **PROMISE-1 RELEVANCE:** 4
- **PROMISE-2 RELEVANCE:** 2
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Defends the pivot against the strongest R1-nominated alternative (Alt 1 paid-EA) on the specific axis where Alt 1's reference class fails to transfer.

### FINDING-2A-7: Seven-mode-types-at-launch is structurally cheaper in HTML than in any engine
- **CLAIM:** R1 Promise-1 warnings (Sanctum 2 cut-don't-stack, Iron Marines three-tower-vocabulary) describe execution-cost ceilings inside engine-bound projects. HTML's iteration economics — no asset pipeline, no engine-recompile loop, no platform porting — make seven-mode-types materially cheaper to achieve at HTML-deliverable polish than at engine-deliverable polish. The pivot's commitment to HTML-quality (not engine-quality) for AtoA's seven mode-types is the only delivery shape in the alternative set that makes Promise-1 tractable for a solo dev.
- **SOURCE:** R1 Findings 1-03-1, 1-02-11; pivot decision doc Loop-3 guardrail #1; Finding 1-08-3 (Stormgate's incomplete-modes failure under engine constraints).
- **STRENGTH:** medium
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** R1 DA A-7 (BTD6 single-aesthetic generalization) cuts here too — HTML iteration cheapness still has to clear a polish bar, and seven-mode HTML coverage may hit a ceiling where the design is complete but the *feel* is uniformly thin across all seven modes.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 2
- **PROMISE-3 RELEVANCE:** 1
- **RELEVANCE NOTE:** Direct Promise-1 defense; reframes the R1 cut-don't-stack lesson as substrate-bound rather than universal.

### FINDING-2A-8: Wishlist-conversion bet is structurally tighter than alternative paths' equivalent bets
- **CLAIM:** R1 Steelman B-5 attacks the free-to-paid-sequel conversion rate as "empirically near-zero outside major publisher franchises." The pivot's wishlist-conversion bet is *not* the free-to-paid-sequel bet B-5 attacks — it is the audience-overlap bet, which is the same bet every alternative path makes, made earlier and with a real public artifact to anchor it. Alt 1 (paid EA) bets on wishlist→paid-EA conversion with no public artifact; Alt 2 (premium $15-20) bets on wishlist→premium with no public artifact. The pivot bets on a public-artifact-shaped wishlist→premium conversion, which is structurally a stronger conversion shape than wishlist-without-artifact.
- **SOURCE:** R1 DA Section B-5; Finding 1-10-1; pivot decision doc Loop-2 steelman.
- **STRENGTH:** medium
- **CONFIDENCE:** medium-low
- **COUNTER-EVIDENCE:** B-5's empirical claim is not refuted — the published conversion rate from free-Steam-game to paid-sequel really is low. The pivot's defense rests on framing wishlist-conversion as audience-overlap rather than sequel-conversion, which is a definitional move that may not survive scrutiny if MtM is *perceived* as a sequel rather than as an engine-replication.
- **PROMISE-1 RELEVANCE:** 2
- **PROMISE-2 RELEVANCE:** 2
- **PROMISE-3 RELEVANCE:** 4
- **RELEVANCE NOTE:** Promise-3's commercial viability depends on MtM funding. The wishlist-conversion bet is the operative variable; the defense reframes its reference class.

### FINDING-2A-9: The lobby-gap audience-size downgrade survives in the pivot's economics
- **CLAIM:** R1 accepts (Reckoning #2) that the five-agent convergence is source-amplification and the gap-size implied is overstated. The pivot's economics survive at the downgraded gap-size because AtoA-as-free does not require the gap to be a *paying* audience — it requires the gap to be a *vocal* audience that wishlist-converts to MtM. The R1 downgrade attacks the gap's size-as-paying-audience; the pivot rests on the gap's size-as-discourse-mass, which the convergence-as-source-amplification finding actually *confirms* (the discourse mass is real even if the addressable paying audience is smaller).
- **SOURCE:** R1 Reckoning #2; convergence callout (5 agents); Findings 1-09-1, 1-09-2.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Discourse mass and wishlist-conversion are not the same variable. A vocal cohort that wishlist-converts at low rates leaves MtM under-funded regardless of how loud the discourse was. The 32-42-year-old-with-90-minutes-weekly cohort (DA A-6) wishlist-converts to grand-strategy-with-narrative more reliably than to TW-with-customs.
- **PROMISE-1 RELEVANCE:** 1
- **PROMISE-2 RELEVANCE:** 5
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Reframes the R1 audience-size downgrade as compatible with the pivot's specific economics, which other shapes in the alternative set cannot do.

### FINDING-2A-10: The Player Complaint Atlas vocal-minority calibration favors the pivot's free-first posture
- **CLAIM:** R1 Reckoning #6 accepts that the Player Complaint Atlas is a complaint distribution among complainants, not a risk distribution among players. Free-AtoA exposure to atlas-derived risks (Rank 2 monetization-creep, Rank 7 customization-deficit, Rank 10 BP-FOMO, Rank 11 pricing-vs-content, Rank 12 account-deletion-IP-EULA) is structurally near-zero because AtoA has no monetization, no BP, no price, and a free-no-IAP commitment. The pivot externalizes complaint-atlas risk to MtM, where it can be addressed by ratified design (cosmetic-only, day-1-BP), with AtoA serving as a goodwill-bank that buffers MtM's launch.
- **SOURCE:** R1 Reckoning #6; Player Complaint Atlas (Agent 8); pivot decision doc Fork A.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Atlas Rank 1 (balance/power-creep), Rank 4 (endgame/content cliff), Rank 8 (bug rot), Rank 9 (UX/accessibility) all apply to *any* shipped TW including AtoA-free. Free does not exempt the product from quality-tier complaints; it exempts it from a specific subset of monetization-and-commitment-tier complaints.
- **PROMISE-1 RELEVANCE:** 3
- **PROMISE-2 RELEVANCE:** 2
- **PROMISE-3 RELEVANCE:** 5
- **RELEVANCE NOTE:** Promise-3 specifically benefits from the pivot's externalization of the vocal-minority's monetization-tier complaints away from AtoA's launch event.

### FINDING-2A-11: The creator-coverage contradiction is *less* damaging to the pivot than to alternatives
- **CLAIM:** R1 Reckoning #7 leaves the Agent-4 vs Agent-9 contradiction unresolved (creators await novelty vs creators have departed). The pivot's two-shot architecture means AtoA tests the contradiction empirically — if creators show up for AtoA-free, MtM funds creator tooling; if they don't, MtM de-prioritizes it without a sunk-cost commitment. Alternatives 1, 2, 3 must *commit* to one framing of the contradiction at launch, with no empirical test before commitment.
- **SOURCE:** R1 Reckoning #7; Findings 1-04-1, 1-09-6, 1-09-10.
- **STRENGTH:** medium
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** Creator tooling is integration work, not a flag flip — if MtM defers creator tooling pending AtoA evidence and the evidence arrives positive, MtM is then under-tooled at launch. The two-shot framing assumes MtM's design is malleable post-AtoA-launch, which the "MtM inherits AtoA verbatim" pivot-doc commitment partially contradicts.
- **PROMISE-1 RELEVANCE:** 1
- **PROMISE-2 RELEVANCE:** 4
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Reframes the R1 unresolved contradiction as the pivot's empirical-test affordance — a structural advantage no alternative path possesses.

### FINDING-2A-12: "Go big at launch" is satisfied by AtoA's launch, not deferred to MtM's
- **CLAIM:** The CONCEPT.md "Go big at launch" non-negotiable is honored by the pivot at AtoA's launch, not at MtM's. Free Steam release with full content skeleton (3 civs × full ladder × 9 Fusion Gods × 3 commanders × 6 launch modes) is structurally a "big" launch by content-surface, just as Stormgate's launch was structurally "big" by team-and-funding. The pivot's free-launch posture inverts Stormgate's failure: complete-content + free distribution + low-perception-cost-per-install vs Stormgate's incomplete-content + paid distribution + high-perception-cost-per-install.
- **SOURCE:** Pivot decision doc Context section; CONCEPT.md non-negotiables; Finding 1-08-3.
- **STRENGTH:** medium
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** "Go big at launch" historically reads as commercial-big, not content-big. A free launch may be content-big and commercial-small simultaneously, which fails to honor the spirit of the non-negotiable even if it honors the letter.
- **PROMISE-1 RELEVANCE:** 5
- **PROMISE-2 RELEVANCE:** 3
- **PROMISE-3 RELEVANCE:** 2
- **RELEVANCE NOTE:** Promise-1-coverage defense; reframes "go big" as content-completeness rather than commercial-magnitude, which the pivot satisfies and alternatives 1/2 only satisfy at higher commercial risk.

---

## 3. Honest concessions

The pivot genuinely cannot defend the following — superalignment requires naming them:

**(a) The wishlist-conversion rate from free-Steam to paid-successor is the pivot's load-bearing assumption and is empirically weak.** R1 Steelman B-5 names this honestly. The pivot's defense (Finding 2A-8) reframes the reference class but does not produce contrary evidence. If AtoA-free generates 50K wishlists and 2% convert to MtM at $15, MtM funds at $15K — inadequate for engine-build budget. The conversion-rate question is the single variable on which the entire pivot lives or dies, and the swarm has not surfaced positive empirical evidence for it specific to the TW genre.

**(b) The "MtM inherits AtoA verbatim, only Phase 5 is fresh" claim is optimistic.** Phase-1-through-Phase-4 inheritance is structural; Phase-5+ is engine-specific creative work that meaningfully reopens design questions whenever the engine substrate forces a UX or feel decision. Calling this "only Phase 5 is fresh" understates the engine-substrate-driven reopening that empirically happens.

**(c) The free-Steam perception debuff is not addressed by the pivot.** Loop-1 of the pivot doc names the risk; Loop-2 dismisses it ("AtoA-free is a marketing artifact"); Loop-3 does not engineer around it. R1 does not have a positive reference class for "first-IP solo-dev free Steam game converting to paid-successor at meaningful rates." This gap is real.

**(d) Two-product surface-area is real.** The pivot doc Loop-1 names the trap pattern (AtoA absorbs all attention, MtM never starts); Loop-3 mitigates with sequential commitment but does not eliminate. Solo-dev abandonment of the second product mid-development is a documented modal failure of the indie cohort.

**(e) The Promise-1 polish-bar at HTML-deliverable quality across seven mode-types is not externally benchmarked.** Finding 2A-7 argues the iteration economics favor HTML, but no R1 finding produces a reference-class HTML game that shipped seven mode-types at solo-deliverable polish. The closest analogs (Bloons web, Cursed Treasure, Kingdom Rush web) are single-mode-type. Cross-mode-type HTML polish at solo scope is an unbenchmarked engineering claim.

**(f) The pivot does not address the resource-budget question for whether the solo dev can complete *both* products.** The pivot decision doc treats AtoA completion as the immediate scope and MtM as future work. Whether the solo-dev career-capital can carry both products to ship is a question the pivot defers, not answers.

---

## 4. Promise-alignment self-score

**Promise 1 — feature/polish/art-complete coverage of every TW mode-type at launch: 4/5.** The pivot honors Promise 1 at AtoA's launch (full content skeleton in HTML) and at MtM's launch (engine-grade replication of the validated content). Findings 2A-2, 2A-7, 2A-12 defend the structural feasibility; concessions (e) and (f) are the held-back point. The "every mode-type at solo scope at HTML-deliverable polish" bar is structurally tractable but unbenchmarked.

**Promise 2 — SC1/WC3 customizability + recognizability: 4/5.** Findings 2A-5, 2A-9, 2A-11 defend the pivot as the only shape in the alternative set that operationalizes lobby-substrate cost in two shots and that empirically tests the creator-contradiction before committing. The held-back point: Promise 2's substrate engineering for MtM is funded by a wishlist-conversion event whose rate is the pivot's largest unhedged assumption (concession a).

**Promise 3 — optional BP + Ranked layered without compromising regular play: 5/5.** Finding 2A-4 is the cleanest single defense — the pivot's two-product architecture *is* the structural shape that R1 DA Reckoning #8 named as the conditional-clean solution. AtoA-free has no monetization (eliminates Rank 2 / Rank 10 / Rank 11 / Rank 12 atlas risks at AtoA's launch event). MtM is paid-base with day-1-visible cosmetic-only BP, which honors the conditional verbatim. Finding 2A-10 reinforces that the vocal-minority complaint atlas is structurally externalized to MtM, where it is addressed by ratified design rather than by hope. This is the strongest single promise-alignment outcome of the defense.

---

*End of Arguer A defense. Output: `C:\TW.AtoA\concept\atoa-vs-mtm\round-2\arguer-a-defend-pivot.md`.*
