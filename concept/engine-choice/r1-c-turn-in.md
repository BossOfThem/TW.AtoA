# R1-C Turn-in — Hiring-pool / Docs / Community + Royalty / Licensing

**Date:** 2026-04-29
**Agent:** R1-C (Phase C engine-choice mini-arc)
**Charter:** [`CHARTER.md`](CHARTER.md)
**Parent:** [`PROJECT-ARC.md`](../PROJECT-ARC.md) §C
**Scope:** Axes 4 + 5 (hiring-pool / docs / community; royalty / licensing) across Godot 4, Unity, Unreal Engine 5. Evidence-only. No engine pick.
**Discipline:** non-instructional; per-claim evidence-quality tag; per-engine load-bearing finding; anti-cascade lint; synthesis paragraph (no recommendation).

---

## §1 — Per-engine evidence

### §1.1 Godot 4

**Hiring-pool depth (current 2D talent pool; contractor plug-in feasibility).** ZipRecruiter shows ~51 Godot Developer postings ($40–$142/hr) and ~19 broader Godot postings ($44k–$220k); Upwork and Freelancer carry active 2D-Godot freelance flow including roguelike-deckbuilder and 2D-game contracts. Pool is **shallow vs. Unity but growing**; Unity's 2024 runtime-fee episode is widely cited as having accelerated Godot adoption. Contractor plug-in feasibility for a solo-dev 2D project is **realistic but narrower** — fewer drop-in specialists, more generalists who learned Godot recently. *Evidence-quality: web-validated for posting counts (snapshot-only, not time-series); inference-from-reputation for "accelerated by Unity episode."*

**Official docs depth.** Official docs at `docs.godotengine.org` are comprehensive for 2D, with a stable-channel English tree covering scripting, scene grammar, signals, multiplayer, and licensing-compliance. Reputational consensus across 2025 comparison pieces is "docs are good and improving; smaller than Unity's but high-signal." *Evidence-quality: web-validated for existence/structure; inference for "high-signal" qualitative judgment.*

**Community size.** Smaller than Unity's by a wide margin in absolute headcount, but the community is the fastest-growing of the three; GitHub repo activity is high; r/godot and the official forums are active daily. **No hard 2025 headcount number surfaced in search.** *Evidence-quality: inference-from-reputation; specific size numbers unverifiable.*

**Asset-store depth.** Godot Asset Library is **free-only and significantly smaller** than Unity's Asset Store; a paid asset store is "being developed" but not live as a peer to Unity's. For a 2D tower-defense, the gap is real — fewer drop-in tower-defense templates, fewer polished UI kits, fewer pathfinding/AI plugins ready-made. *Evidence-quality: web-validated.*

**Royalty / licensing model.** **MIT license. Zero royalty. Zero revenue threshold. No seat fee. No runtime fee.** Engine source is freely redistributable; license terms do not bind games made with it; user owns their game outright. *Evidence-quality: web-validated (official `godotengine.org/license`).*

**Cost composition with paid-EA economics (EA → 1.0 → post-1.0).**

| Scenario (lifetime gross) | EA window | 1.0 window | Post-1.0 | Total engine cost |
|---|---|---|---|---|
| Small ($50k) | $0 | $0 | $0 | **$0** |
| Medium ($500k) | $0 | $0 | $0 | **$0** |
| Large ($5M) | $0 | $0 | $0 | **$0** |

Engine cost is structurally zero across all revenue scenarios. The personal-runway depth (PM-Fork-11) carries no engine-licensing line item.

**Load-bearing finding (Godot 4):** Royalty-free MIT is the dominant cost-envelope advantage; the offsetting cost is hiring/asset-store thinness, which loads the solo-dev primary path more than it loads PM-Fork-7 (art-director outsource — art tools are mostly engine-agnostic) or PM-Fork-9 (post-1.0 second-dev hire — pool is shallow but exists and growing).

---

### §1.2 Unity

**Hiring-pool depth (current 2D talent pool; contractor plug-in feasibility).** **Largest of the three by a wide margin.** ZipRecruiter shows 1,000+ Unity Developer postings ($81k–$180k); LinkedIn/Indeed listings significantly outnumber Godot postings. **However**, the 2022–mid-2025 industry contraction (~45k jobs cut, "500 applicants per posting" cited) means the pool of *available* mid-senior talent is unusually deep on the supply side. Contractor plug-in feasibility for a 2D solo-dev project is **the highest of the three** — drop-in 2D specialists, tower-defense template authors, and UI-Toolkit contractors are abundant. *Evidence-quality: web-validated for posting volume; inference for "deepest available pool" qualitative.*

**Official docs depth.** Unity's docs and Learn portal are the most extensive of the three; tutorials, manuals, scripting API reference, and a long tail of community-authored content dwarf Godot's by absolute volume. *Evidence-quality: inference-from-reputation; not directly searched in this round.*

**Community size.** Largest absolute community across forums, Discord, YouTube, Stack Overflow tag volume. *Evidence-quality: inference-from-reputation.*

**Asset-store depth.** Unity Asset Store is "massive" with thousands of paid + free assets including complete tower-defense templates, dialogue systems, inventory plugins, and pathfinding. **Cited as the single biggest asset-availability advantage of the three engines.** *Evidence-quality: web-validated.*

**Royalty / licensing model — runtime-fee history is load-bearing and recently changed; flag uncertainty.**
- **Pre-Sept-2024:** Unity announced a per-install Runtime Fee in Sept 2023 that triggered industry backlash. Modified, then on **2024-09-12 cancelled outright** for all Unity 6 and earlier versions.
- **Current model (effective 2024-10-17 for Personal; 2025-01-01 for Pro/Enterprise):**
  - **Unity Personal:** free; eligibility ceiling raised to revenue/funding under **$200,000/yr**.
  - **Unity Pro:** $2,200/seat/yr (8% increase); applicable $200,001–$24,999,999 revenue/funding band.
  - **Unity Enterprise:** for $25M+; 25% subscription price increase.
- **No per-install or per-runtime fee currently.** Seat-based subscription only.
- **Reversibility risk:** Unity has demonstrated willingness to introduce a per-install runtime fee and walk it back under pressure. The current model is stable as of 2026-04, but the precedent exists; a future Unity policy shift cannot be ruled out across the EA→1.0→post-1.0 window. *Evidence-quality: web-validated for current pricing as of late 2024 / Jan 2025; inference-with-uncertainty-flag for "stable forward."*

**Cost composition with paid-EA economics (EA → 1.0 → post-1.0).** Paid-EA is single-product at $15–20/copy, cosmetic-only Battle Pass, no IAP for power. Solo-dev = 1 seat baseline; PM-Fork-7 art-director outsource may add 1 contractor seat for a defined window; PM-Fork-9 post-1.0 second-dev hire adds 1 seat post-1.0.

| Scenario (lifetime gross) | Tier eligibility | EA seats | 1.0 seats | Post-1.0 seats | Annual seat cost (1 → 2 seats) | Lifetime engine cost (illustrative 4yr horizon) |
|---|---|---|---|---|---|---|
| Small ($50k) | Personal (free, ≤$200k) | 1 (free) | 1 (free) | 1–2 (free) | **$0** | **$0** |
| Medium ($500k) | Pro required (>$200k threshold) | 1 free → 1 Pro after threshold breach | 1 Pro | 1–2 Pro | $2,200/seat × seats | ~$2,200–$8,800 cumulative |
| Large ($5M) | Pro required from threshold breach | 1 Pro | 1–2 Pro | 2 Pro | $2,200–$4,400/yr | ~$8,800–$17,600 cumulative |

Threshold structure means small-success projects pay nothing; medium- and large-success projects pay seat-subscription only (capped, predictable, no per-copy or per-install drag). **No revenue percentage.** *Evidence-quality: web-validated for tier mechanics; illustrative for cumulative — actual depends on threshold-breach timing and seat count.*

**Anti-cascade lint (Unity).** Seat-subscription model does not conflict with paid-EA single-product or cosmetic-only Battle Pass locks. **No cascade violation.** Runtime-fee precedent flags a *reversibility risk* but no current violation.

**Load-bearing finding (Unity):** Hiring-pool depth + asset-store depth are dominant velocity advantages; runtime-fee reversal history is the dominant *structural-risk* finding — current pricing is favorable for paid-EA single-product, but Unity has demonstrated policy-shift willingness once. Cost composition is predictable at small/medium success, modest at large success.

---

### §1.3 Unreal Engine 5

**Hiring-pool depth (current 2D talent pool; contractor plug-in feasibility).** Unreal's pool is large in absolute terms but **heavily 3D / AAA-weighted**. C++ + Unreal pathway leads to "prestigious, high-paying jobs at major AAA studios"; specialists are more demanding to hire and command higher rates. **2D contractor plug-in feasibility is the weakest of the three** — Unreal's 2D toolchain (Paper2D and successors) is a second-class citizen, and 2D-tower-defense specialists in UE5 are a thin slice of an otherwise 3D-skewed market. *Evidence-quality: inference-from-reputation; web-validated for "C++ Unreal → AAA" pattern.*

**Official docs depth.** Epic's official docs are extensive but heavily 3D-oriented; 2D-specific documentation is comparatively sparse. *Evidence-quality: inference-from-reputation.*

**Community size.** Large community; heavily AAA / 3D / cinematic / VFX-skewed. Tower-defense / 2D indie cohort is small relative to Unity's or even Godot's growing 2D contingent. *Evidence-quality: inference-from-reputation.*

**Asset-store depth.** Unreal Marketplace (now Fab) is large and high-quality but skewed to 3D assets, environments, and characters. 2D-tower-defense-specific assets are sparse. *Evidence-quality: inference-from-reputation.*

**Royalty / licensing model.**
- **Free to use** for game development.
- **5% royalty on lifetime gross revenue per product above a $1,000,000 lifetime threshold**, payable to Epic regardless of who collects the revenue (storefronts, publishers, etc.).
- **3.5% reduced rate** if the game is released on Epic Games Store at-or-before other stores ("Launch Everywhere with Epic" program), effective 2025-01-01.
- Non-game commercial users have an alternate **$1,850/seat/yr** model; not applicable to AtoA's paid-EA game SKU.
- *Evidence-quality: web-validated (official Unreal Engine licensing page; Epic 2024-10 announcement).*

**Cost composition with paid-EA economics (EA → 1.0 → post-1.0).** Paid-EA at $15–20/copy. Threshold is $1M lifetime gross *per product*. AtoA is single-product, so the threshold applies cleanly to total lifetime AtoA gross.

| Scenario (lifetime gross) | Above $1M threshold? | Royalty owed | Effective engine cost |
|---|---|---|---|
| Small ($50k) | No | $0 | **$0** |
| Medium ($500k) | No | $0 | **$0** |
| Large ($5M) | Yes; royalty on $5M − $1M = $4M | 5% × $4M = $200,000 (or 3.5% × $4M = $140,000 if EGS launch-with) | **$140k–$200k** |
| Very large ($20M) | Yes; royalty on $19M | 5% × $19M = $950,000 (or 3.5% × $19M = $665,000) | **$665k–$950k** |

**Royalty scales with success.** Small/medium-success scenarios pay zero; large-success scenarios pay six-figure royalties. The Epic Games Store launch-with discount is a 1.5pp savings — load-bearing only at large success.

**Anti-cascade lint (Unreal).** Royalty model does not conflict with paid-EA single-product or cosmetic-only Battle Pass locks (the 5% applies to all gross regardless of monetization shape, so cosmetic-only is neutral). **No cascade violation.** Note: 5% royalty composes *on top of* storefront cuts (Steam 30%, etc.) — not in lieu of.

**Load-bearing finding (Unreal):** Royalty model is **success-scaling** — zero cost at small/medium, six-figure cost at large success. 2D-tower-defense fit is the weakest of the three on tooling, hiring-pool, asset-store, and docs axes. Cost-envelope advantage at small success is offset by 2D-substrate weakness; cost-envelope disadvantage at large success compounds with 2D-substrate weakness.

---

## §2 — Anti-cascade-violation lint (cross-engine)

Checked each engine's licensing model against locked surfaces:
- **Paid-EA single-product at $15–20** ([`decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md`](../../decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md))
- **Cosmetic-only Battle Pass, no IAP for power** ([`decisions/2026-04-29-promise-3-paid-base-discipline-lock.md`](../../decisions/2026-04-29-promise-3-paid-base-discipline-lock.md))

**Godot MIT:** zero conflict — engine cost decoupled from monetization shape.
**Unity seat-subscription:** zero conflict — seat fees independent of revenue model; tier eligibility is revenue-based but does not constrain monetization design.
**Unreal 5% royalty above $1M:** zero conflict — royalty applies to gross regardless of cosmetic-vs-power monetization split; does not push toward pay-to-win.

**No cascade violations across the three licensing models.** All three are paid-EA-compatible at the licensing layer.

(Other axes — tooling, netcode, port-surface — out of R1-C scope; flagged for R1-A/R1-B/alignment-check.)

---

## §3 — Synthesis paragraph (no engine pick)

Across hiring-pool / docs / community + royalty / licensing, the three engines compose distinct cost-vs-velocity profiles for a solo-dev paid-EA single-product 2D-tower-defense. **Godot 4** is structurally cheapest (MIT, zero royalty, zero seat fee) but loads solo-dev velocity with thinner asset-store and shallower (though growing) hiring-pool — material cost is shifted from licensing to in-house/contractor build-time. **Unity** has the deepest hiring-pool, the deepest asset-store, the deepest docs, and a seat-subscription model that is currently favorable for paid-EA at small-medium success (free under $200k revenue; ~$2,200/seat/yr above), but carries a load-bearing reversibility risk from the 2023 runtime-fee episode and 2024 reversal — current pricing is stable, the precedent is not. **Unreal Engine 5** offers a clean royalty model (zero below $1M, 5% above; 3.5% with EGS launch-with) that scales with success but combines a 2D-substrate weakness on every R1-C axis (hiring-pool 2D-skew, docs 2D-sparseness, asset-store 2D-sparseness) with six-figure royalty exposure at large success — the cost-envelope penalty at large success compounds with the substrate-fit penalty at all success levels for this specific 2D-tower-defense product. R1-C produces no engine recommendation; PM-Fork-6 resolves with R1-A, R1-B, R1-D, and alignment-check evidence in scope.

---

*End of R1-C turn-in.*
