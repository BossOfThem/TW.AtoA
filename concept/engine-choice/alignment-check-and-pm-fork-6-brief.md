# Alignment-check + PM-Fork-6 fork-resolution brief — Engine-choice mini-arc

**Date:** 2026-04-29
**Status:** Alignment-check landed. R1 → PM-Fork-6 gate. Non-instructional.
**Charter:** [`CHARTER.md`](CHARTER.md). Parent: [`../PROJECT-ARC.md`](../PROJECT-ARC.md) §C.
**Inputs:** `r1-a-turn-in.md` (tooling + 2D), `r1-b-turn-in.md` (netcode + port), `r1-c-turn-in.md` (hiring + royalty), `r1-d-turn-in.md` (other-bucket).
**Authority:** R2 / PM-Fork-6 is PM-only. This brief surfaces the fork; **it does not pick.**

---

## §1 — Cross-axis consistency check

Same engine-set (Godot 4 / Unity / Unreal 5) is evaluated against the same evidence-quality bar (`web-validated` / `inference-from-reputation` / `unverifiable`) across all four R1 turn-ins. No turn-in introduces a fourth top-tier candidate or omits one of the three.

**Generosity drift check:**

| Engine | R1-A (tooling/2D) | R1-B (netcode/port) | R1-C (hiring/royalty) |
|---|---|---|---|
| Godot 4 | clears with engineering-discipline caveat (RenderingServer pattern) | strongest port-surface; acceptable netcode | structurally cheapest; thinnest hiring/asset depth |
| Unity | clears cleanly; Prefab-Variant + ScriptableObject load-bearing strength | dominant netcode ceiling; high port-surface | deepest hiring/asset/docs; runtime-fee precedent flagged |
| Unreal 5 | trails (2D second-class; editor weight) | over-spec'd-but-sound; highest port friction | weakest 2D fit on hiring/docs/assets; royalty success-scaling |

Engine-by-engine framings are **internally consistent** across buckets. No bucket is markedly more or less generous to a given engine than the others — each turn-in's verdict on each engine composes coherently with the other three. R1-A's "soft-pressure-toward-re-scoping" flag on Unreal aligns with R1-B's "highest port friction" framing and R1-C's "2D-substrate weakness on every R1-C axis." R1-A's Godot "engineering-discipline pattern" framing aligns with R1-B's "you build the high-level pieces yourself" netcode framing and R1-C's "material cost shifted from licensing to in-house build-time" framing. **No drift detected.**

---

## §2 — Evidence-quality audit

**Unity runtime-fee history (load-bearing per R1-C).** R1-C tags pre-Sept-2024 announcement, modification, and 2024-09-12 cancellation as `web-validated`; current pricing (Personal free under $200k revenue; Pro $2,200/seat/yr; Enterprise tier for $25M+) tagged `web-validated for current pricing as of late 2024 / Jan 2025; inference-with-uncertainty-flag for 'stable forward.'` Tagging is **honest and load-bearing**: the precedent-of-reversal is correctly framed as a *risk* not a *current cost*. R1-B references the 2023 episode as PM-Fork-6 reversibility consideration without claiming current cost. **Consistent across buckets.**

**Unreal royalty model.** R1-C tags `web-validated` against Epic's official licensing page + 2024-10 announcement: free-to-use; 5% lifetime gross royalty above $1M-per-product threshold; 3.5% reduced rate via "Launch Everywhere with Epic" if EGS launches at-or-before other stores (effective 2025-01-01); $1,850/seat/yr alternate non-game model (not applicable to AtoA). Threshold-application math is illustrative-projection (correctly framed) not measured. **No mis-tagged claims surfaced.**

**Godot MIT.** R1-C tags `web-validated` against `godotengine.org/license`. Zero-cost framing across small/medium/large scenarios is structural, not projection. **Clean.**

Other quantitative claims (Godot ~500-node scene-tree pressure ceiling; ZipRecruiter posting counts; Photon CCU pricing as cost-composition cross-reference) are correctly tagged `web-validated` for the source observation and `inference` where extrapolation occurs. Audit returns **no mis-tagged load-bearing claims.**

---

## §3 — Anti-cascade-violation roll-up (RT-2 trigger check)

Locked surfaces under §5 of charter + PROJECT-ARC.md §3: per-tower 45-magnitude matrix; attack-type 7-type RPS + 5-armor; Fusion 9-recipe Hard-lock; mobile unit 4-flag control catalog; 6-mode ontology with 2 feature-complete at 1.0; cosmetic-only paid-EA monetization.

| Engine | R1-A lint | R1-B lint | R1-C lint | Composite |
|---|---|---|---|---|
| Godot 4 | clean | clean (zero flags) | clean (engine-cost decoupled from monetization) | **clean** |
| Unity | clean | clean (zero flags) | clean (seat fees independent of revenue model) | **clean** |
| Unreal 5 | clean (with R1-A "soft-pressure" velocity flag, not hard violation) | clean (zero flags) | clean (5% royalty neutral to cosmetic-vs-power split) | **clean** |

**No engine forces re-scoping of any locked surface. RT-2 is not triggered by R1 evidence.** R1-A's soft-pressure flag on Unreal (a runway-pressured solo-dev who picks Unreal may downstream propose to "simplify" per-tower magnitudes or projectile counts to fit the engine) is correctly framed as a risk-of-future-RT-2-triggering, not a current trigger. PM-Fork-6 may treat this as a downstream-discipline cost on the Unreal branch.

---

## §4 — PM-Fork-6 fork-resolution brief

PM-Fork-6 is **PM-only** per CHARTER §3 + PROJECT-ARC.md §7. The brief below surfaces the three branches; it does not recommend.

### §4.1 — Godot 4

**Strongest argument:** Cleanest port-surface for the prototype's logic shapes (signals + nodes + Resources map near-1:1 to enum-state-machines + data-tables + per-entity behavior, per R1-B); royalty-free MIT collapses engine cost to structural zero across every revenue scenario (per R1-C); dedicated 2D renderer with idiomatic atlas/particle pipeline (per R1-A). The composite is **lowest cost-envelope + highest port-velocity at the prototype-logic layer.**

**Load-bearing risk:** Thinnest hiring-pool and asset-store of the three (R1-C) — material cost shifts from licensing to solo-dev build-time on anything where a Unity asset-store template would have collapsed weeks of work; scene-tree-vs-RenderingServer engineering-discipline pattern at projectile-heavy scale (R1-A) is a known engine pattern not a flaw, but it is a *pattern the dev must know*; netcode "you build matchmaking + prediction + reconnection yourself" posture (R1-B) is a velocity tax for any team but a velocity *credit* for solo-dev who wants full control over a bounded netcode surface that Horde-A's latency tolerance permits.

**Cost-envelope curve:** Flat zero across small ($50k) / medium ($500k) / large ($5M) lifetime gross. No threshold, no royalty, no seat fee. **Zero engine-licensing line item across the EA → 1.0 → post-1.0 window.**

**Solo-dev profile favored:** A solo-dev who values cost-floor certainty and prototype-logic port-velocity over asset-store leverage and pre-built netcode infrastructure; who is comfortable absorbing the engineering-discipline cost of Godot's scene-tree-vs-RenderingServer pattern; who treats the "you build the netcode pieces" posture as scope-control rather than scope-burden.

### §4.2 — Unity

**Strongest argument:** Dominant on three of the six velocity axes simultaneously — deepest hiring-pool (R1-C; load-bearing for PM-Fork-7 art-director outsource and PM-Fork-9 post-1.0 second-dev hire reversibility), deepest asset-store + tooling (R1-C; tower-defense templates, UI kits, pathfinding plugins drop-in), and only candidate where every netcode tier (NGO P2P → Mirror server-auth → Photon Fusion rollback → Photon Quantum 3 deterministic-lockstep) is a near-drop-in choice (R1-B; over-spec'd for Horde-A but genuine optionality for post-1.0 PvP roadmap-stretch). Prefab Variants + ScriptableObject grammar maps near-perfectly to AtoA's 3-civ × 6-tower × tier-variant + per-civ-identity-hook structure (R1-A load-bearing finding).

**Load-bearing risk:** Runtime-fee precedent (R1-C) — current model is favorable (Personal free under $200k; Pro $2,200/seat/yr above) but Unity has demonstrated willingness to introduce per-install fees and walk them back under pressure. Current pricing is stable as of 2026-04; the precedent is not. Across the EA → 1.0 → post-1.0 window (multi-year), a future policy shift cannot be ruled out. Secondary risks: domain-reload iteration latency relative to Godot (R1-A; mitigatable); Photon Fusion / Quantum cost-composition if the post-1.0 PvP-stretch modes adopt rollback/deterministic netcode (CCU-based SaaS pricing).

**Cost-envelope curve:** $0 at small success ($50k, under Personal $200k threshold); ~$2,200–$8,800 cumulative at medium success ($500k, Pro required after threshold breach, 1–2 seats over a 4yr horizon); ~$8,800–$17,600 cumulative at large success ($5M, 1–2 Pro seats). **Threshold-stepped; no per-copy or per-install drag; predictable.** Reversibility-risk overlay: outside this curve if runtime-fee policy returns.

**Solo-dev profile favored:** A solo-dev who values asset-store leverage and hiring-pool depth (PM-Fork-7 + PM-Fork-9 reversibility) over cost-floor certainty; who reads the runtime-fee history as a one-off corrected-under-backlash rather than a structural pattern; who values the netcode optionality as genuine post-1.0 roadmap insurance even though Horde-A under-uses it; who prefers ScriptableObject + Prefab Variant ergonomics over GDScript signal grammar for the 45-tower × 3-civ matrix authoring shape.

### §4.3 — Unreal Engine 5

**Strongest argument:** Server-authoritative replication is the engine's default model, deeply integrated; Network Relevance handles small-entity-count efficiency; for a hypothetical large-success scenario where AtoA expanded to 3D-rendered-2D or 3D mode-stretch, the ceiling is highest of the three (R1-A / R1-B). Royalty model is zero below the $1M lifetime per-product threshold (R1-C), so small/medium-success scenarios pay nothing.

**Load-bearing risk:** 2D is second-class on every R1 axis — R1-A names Paper2D + PaperZD third-party-dependent stack; R1-B names "highest per-shape port friction" on the prototype's logic shapes; R1-C names hiring-pool 2D-skew + docs 2D-sparseness + asset-store 2D-sparseness. The composite is a velocity penalty *across all axes* for AtoA's specific 2D-tower-defense substrate. Royalty success-scales: 5% on lifetime gross above $1M ($140k–$200k at $5M; $665k–$950k at $20M; 3.5% reduced via EGS launch-with). **Cost-envelope penalty at large success compounds with substrate-fit penalty at all success levels.** R1-A's soft-pressure flag (a runway-pressured dev may downstream propose to "simplify" locked surfaces to fit the engine) is the latent RT-2 risk.

**Cost-envelope curve:** $0 at small ($50k); $0 at medium ($500k); $140k–$200k at large ($5M); $665k–$950k at very-large ($20M). **Royalty success-scales; storefront cuts compose on top, not in lieu.** Velocity-tax overlay: present at every success level via 2D-substrate weakness.

**Solo-dev profile favored:** Effectively none of the AtoA-specific solo-dev profile space — Unreal's strongest arguments (3D ceiling, Niagara firepower, AAA-grade replication ceiling) are not load-bearing for AtoA's locked design substrate, while its weaknesses (2D second-class, editor weight, C++/Blueprint duality friction, royalty success-scaling) are directly load-bearing against solo-dev velocity. Unreal favors a profile where 3D ceiling and AAA-tier visual grammar are core product surfaces; AtoA's locked surface is the inverse of that profile.

### §4.4 — Decision-shape framing (no pick)

The fork resolves along three composite-axes the PM weighs together: **(a) cost-floor certainty** (Godot zero across all scenarios; Unity zero at small + threshold-stepped above; Unreal zero below $1M then success-scaling), **(b) ecosystem leverage** (Unity deepest by wide margin on hiring + assets + docs; Godot growing-but-thin; Unreal large-but-3D-skewed), and **(c) port-velocity-fit on AtoA's specific logic shape** (Godot highest, Unity high, Unreal lowest). The runtime-fee precedent is a Unity-specific reversibility-risk overlay; the 2D-second-class status is an Unreal-specific velocity-penalty overlay; the asset/hiring thinness is a Godot-specific build-time-shift overlay. PM stance favoring **cost-floor certainty + maximum scope-control** points one direction; PM stance favoring **ecosystem leverage + post-1.0 netcode optionality + reversibility insurance via deep hiring-pool** points another; the third branch (Unreal) requires a PM stance where 3D ceiling is load-bearing for product surface — a stance the locked AtoA substrate does not currently support, which is why R1-A / R1-B / R1-C all converge on Unreal trailing on AtoA-specific axes despite being the strongest engine in the abstract. PM-Fork-6 resolves under PM authority alone.

---

## §5 — Other-bucket disposition

R1-D returns **null**. Bevy / MonoGame / LÖVE / Defold / Stride / Heaps / custom-stack each fail at least one velocity gate (framework-not-engine, no first-party netcode, near-zero hiring-pool, language-niche, or pre-1.0 churn); Bevy is the only intellectually interesting outlier but Rust ECS forces re-architecting the prototype's deliverable-logic port-source, eroding the very port-velocity factor the re-supersession protects. **Bucket closes.** PM-Fork-6 does not need an "other" branch on the decision tree; the fork is three-way (Godot 4 / Unity / Unreal 5) only.

---

*End of alignment-check and PM-Fork-6 fork-resolution brief. R2 / PM-Fork-6 is PM-only; R3 spec-grammar agent + RN cross-arc audit fire after PM resolution per CHARTER §3.*
