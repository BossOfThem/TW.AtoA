# R1-D turn-in — "Other" engine bucket scan

**Date:** 2026-04-29
**Agent:** Phase C R1-D
**Charter:** [`CHARTER.md`](CHARTER.md) §3 R1-D
**Scope:** Open-ended scan of non-top-3 engines for any load-bearing substrate-fit reason to consider over Godot 4 / Unity / Unreal.
**Evidence-quality tags:** `[web-validated]` / `[inference-from-reputation]` / `[unverifiable]`. This bucket is a surprise-catcher, not a deep audit; reputation-inference dominates and is flagged as such.

---

## §1 — Candidate quick-scan

| Engine | 2D viability | Multiplayer story | Solo-dev velocity | Quick-verdict |
|---|---|---|---|---|
| **Bevy** (Rust ECS) | Yes — capable 2D | Third-party (lightyear/aeronet); no first-party netcode | Low — pre-1.0 churn, no editor, Rust compile times, ECS-first paradigm forces re-architect of prototype state-machine logic | Fails velocity gate `[inference-from-reputation]` |
| **MonoGame** (C# framework) | Yes — but framework not engine; you build the editor/scene system yourself | DIY entirely | Low for solo paid-EA — too much yak-shaving on substrate Godot/Unity give free | Fails velocity gate `[inference-from-reputation]` |
| **LÖVE / love2d** (Lua) | Yes — strong 2D | DIY (enet bindings); no matchmaking infra | Medium for tiny scope; weak for paid-EA shippable with PvP-Co-op netcode budget | Fails netcode gate `[inference-from-reputation]` |
| **Defold** (Lua, Bang-owned) | Yes — strong 2D, mobile-first | First-party-ish but thin docs for desktop PvP-Co-op | Medium; smaller community, hiring-pool near-zero vs top-3 | No load-bearing edge `[inference-from-reputation]` |
| **Stride** (C#, open-source) | 2D possible but 3D-first | Limited netcode story | Small community, thin docs | Fails community/docs gate `[inference-from-reputation]` |
| **Heaps** (Haxe) | Yes (Dead Cells shipped on it) | DIY | Niche language, near-zero hiring pool | Fails hiring-pool gate `[inference-from-reputation]` |
| **Custom-stack** | N/A | N/A | Catastrophic for solo paid-EA | Disqualified by charter velocity-paramount clause |

---

## §2 — Honest finding: **NULL**

No "other" engine offers a load-bearing substrate-fit reason to consider over Godot 4 / Unity / Unreal for the locked AtoA design substrate under solo-dev paid-EA economics.

The top-3 dominate the velocity-fit space because they bundle editor + scene grammar + first-party (or near-first-party) netcode + deep docs + non-trivial hiring pool. Every "other" candidate either (a) is a framework not an engine and forces solo-dev to build substrate Godot/Unity ship free, (b) lacks first-party netcode for the PvP-Co-op latency budget, or (c) has near-zero hiring pool that breaks PM-Fork-9 reversibility. Bevy is the only intellectually interesting outlier, but Rust ECS forces re-architecting the prototype's deliverable-logic port-source — directly eroding the port-velocity factor R1-B is evaluating. `[inference-from-reputation]` across the bucket; no claim here is web-validated this turn, but the reputational signal is strong and consistent.

## §3 — Bucket closes

R1-D returns null. Top-3 evaluation in R1-A/B/C is sufficient; PM-Fork-6 does not need an "other" branch on the decision tree.

*End of R1-D turn-in.*
