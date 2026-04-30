# Charter — Engine-choice mini-arc (Phase C of PROJECT-ARC.md)

**Date:** 2026-04-29
**Status:** Chartered (R1 launches under autonomous-mandate; R2 gated on PM-Fork-6; R3 gated on R2 direction-lock)
**Parent arc:** [`concept/PROJECT-ARC.md`](../PROJECT-ARC.md) Phase C
**Closes:** Phase-4 §4.8 item #9 (engine lock), advancing Phase 4 exit-gate to 10/11
**Discipline:** non-instructional throughout (conceptual / refinement / educate / ask). 3x debug loop embedded across R1/R3. PM-Fork-6 is the load-bearing decision gate; R1 produces evidence, PM picks engine, R3 specs the lock-in. AskUserQuestion deferred-to-AM under D-10.

---

## §1 — Question framing

**Top-level question:** *"Which engine maximizes solo-dev velocity for the locked AtoA design substrate (per-tower magnitudes, attack-type 7-type RPS, Fusion 9-recipe lock, mobile unit control flags, 6-mode design-substrate ontology with 2 feature-complete at 1.0) under paid-EA single-product economics, given the prototype's preserved 50–55% deliverable-logic as port-source?"*

The question is **not** "which engine is best in the abstract." It is "which engine clears the substrate-fit gate and the solo-dev-velocity gate while honoring the paid-EA cost envelope (PM-Fork-11 personal-runway depth) and the port-source framing (re-supersession 2026-04-29)."

**"Velocity" decomposes into six axes** (R1 evidence-gather scope per PROJECT-ARC.md §C.1):

1. **Tooling-fit** — editor ergonomics, hot-reload, debugger quality, scene/prefab grammar, scripting language(s) and their fit to AtoA data shapes (RPS tables, Fusion recipes, per-civ identity-hooks).
2. **Multiplayer netcode** — built-in or first-party netcode? deterministic lockstep vs rollback vs server-authoritative? matchmaking infra story? PvP-Co-op (Horde-A) latency budget tolerance?
3. **2D rendering pipeline** — sprite/atlas pipeline, particle system, UI substrate, post-processing fit for tower-defense visual grammar (lots of small entities, heavy projectile/effect counts, readable-at-glance silhouettes).
4. **Hiring-pool / docs / community** — if PM-Fork-7 art-director outsource fires, can contractors plug in? if PM-Fork-9 fires (post-1.0 second-dev hire), is the talent pool deep? official docs depth, community size, asset-store depth.
5. **Royalty / licensing model** — flat license / royalty / revenue-share / source-available / fully-open. Cost composes with paid-EA economics across the EA→1.0→post-1.0 window.
6. **Port surface** — how cleanly does the prototype's preserved 50–55% deliverable-logic (HTML/JS state-machine + balance numerics + AI scaffolds) port forward? Does the engine require re-architecting in patterns that erode the port savings?

---

## §2 — Engine candidate set

Per PROJECT-ARC.md §7 lock D-2 cross-reference + CASCADE pointer "Godot 4 leading":

1. **Godot 4** — CASCADE-cited "leading" candidate. MIT-licensed; royalty-free; GDScript + C# + GDExtension; first-party multiplayer; growing 2D community; solo-dev-friendly editor.
2. **Unity** — Largest hiring pool; mature 2D pipeline; recent runtime-fee history is a load-bearing risk per PM-Fork-6 reversibility framing.
3. **Unreal Engine 5** — Largest 3D ceiling; royalty-based; 2D second-class; tooling weight high for solo-dev; relevance gated on whether AtoA visual-direction wants 3D-rendered-to-2D path.
4. **Other** — bevy / MonoGame / love2d / custom-stack / Stride. Long tail; included as "other" bucket only if R1 surfaces a load-bearing reason to consider one.

---

## §3 — Swarm shape

**Round 1 (4 parallel evidence-gather agents):**

- **R1-A: Tooling-fit + 2D rendering pipeline** — across Godot 4, Unity, Unreal. Honest evidence-quality notes per claim (web-validated / inference / unverifiable).
- **R1-B: Multiplayer netcode + port surface** — across Godot 4, Unity, Unreal. Specific attention to PvP-Co-op (Horde-A) latency and the prototype port shape.
- **R1-C: Hiring-pool / docs / community + royalty / licensing** — across Godot 4, Unity, Unreal. Cost-envelope composition with paid-EA across EA→1.0→post-1.0.
- **R1-D: "Other" bucket scan** — open-ended check for whether any non-top-3 engine clears a substrate-fit gate the top-3 don't. If finding is null, agent reports null and bucket closes.

Each R1 agent produces:
- A per-engine evidence dossier on its assigned axes.
- One "load-bearing finding" callout per engine per axis (what genuinely matters vs what's noise).
- One "evidence-quality" honest-confidence note per claim (web-validated / inference-from-reputation / unverifiable).
- Anti-cascade-violation lint: flag any engine choice that would force re-scoping of a locked surface (per PROJECT-ARC.md §3 cascade-respect block; reversal trigger RT-2).

**Alignment-check between R1 and R2.** Cross-bucket consistency verification (same engine evaluated against same evidence-quality bar across buckets); flag drift; surface load-bearing forks for PM-Fork-6.

**Round 2 (PM-Fork-6 — PM-only):**

PM picks engine after R1 evidence presented. **This is a PM-only fork; no autonomous default.** The autonomous-mandate explicitly does not extend to engine choice per PROJECT-ARC.md §7 PM-fork list. R1 evidence is presented as a structured fork-resolution brief; PM resolves.

**Round 3 (1 spec-grammar agent):**

After R2 direction-lock, a single agent specs the build-tooling lock-in for the chosen engine: CI shape, deployment shape, asset pipeline, project structure, scripting-language commitment, multiplayer-stack commitment. Produces the engine-choice decision-file body.

**RN cross-arc audit (1 agent):**

Verifies engine choice composes with all locked surfaces (per-tower magnitudes, attack-type RPS, Fusion 9-recipe lock, mobile unit control flags, 6-mode ontology with 2 feature-complete at 1.0). Zero violations is the exit gate; any violation triggers reversal trigger RT-2 (PROJECT-ARC.md §8) — back to engine candidate set, not forward to lock.

---

## §4 — Output artifacts

1. **`research/2026-0X-XX-engine-evidence-dossier.md`** — R1 evidence as substrate, kept as research not decision. Structured per-engine × per-axis with evidence-quality notes.
2. **`research/2026-0X-XX-engine-cross-arc-audit.md`** — RN audit output verifying composition with locked surfaces.
3. **`decisions/2026-0X-XX-engine-choice-lock.md`** — Hard reversibility per PROJECT-ARC.md §C.5. Names chosen engine, build-tooling lock-in spec, cross-arc audit clearance, alternatives considered, reason chosen via 3x debug loop synthesis, reversibility note. Closes Phase-4 §4.8 item #9.

---

## §5 — Context discipline

The engine-choice mini-arc must respect the locked design substrate per PROJECT-ARC.md §3 cascade-respect block. **Engine choice is implementation-substrate decision; it does not redesign the locked product surface.** If a candidate engine cannot honor a locked surface, the engine is removed from consideration — the surface is not loosened to fit the engine. (Reversal trigger RT-2 names the narrow case under which a substrate-fit failure forces upstream re-scoping via written supersession.)

The prototype's port-source framing (per `decisions/2026-04-29-prototype-port-source-re-supersession.md`) is a **port-velocity factor, not a port-source-engine constraint.** The HTML/JS prototype is not portable as code; only the deliverable-logic is portable. R1-B's port-surface axis evaluates how cleanly the *logic* ports, not how cleanly the code ports.

EZ.BRAIN naming grammar (sub-authority per PROJECT-ARC.md §3) is **not in scope** for engine choice. Engine code paths use whatever naming convention the engine + chosen scripting language idiomate to; EZ.BRAIN consumer-facing naming applies to surfaces players see, not to engine internals.

---

## §6 — Cost estimate

Per PROJECT-ARC.md §C: 4 R1 agents + 1 alignment-check + 1 PM-Fork-6 + 1 R3 spec-grammar + 1 RN audit ≈ **5 agent-rounds + 1 PM-round.** R1 launches in parallel (4 background agents); R2 is a single PM-round (no agent compute); R3 + RN run sequentially after R2.

Engine-choice decision-file cost is small relative to Phase E implementation cost; the lock is what unlocks Phase E entry.

---

## §7 — PM authorization status

**R1 launches under PM "go" autonomous-mandate per second-night session.** R1's scope is evidence-gather only; no engine-direction commitment is made in R1.

**R2 is PM-Fork-6 — does not run under autonomous-mandate.** Engine choice is reserved for PM AM-review per PROJECT-ARC.md §7 PM-fork list. R1 turn-in produces a fork-resolution brief; PM resolves; R3 fires after PM resolution.

**R3 + RN audit fire after R2 resolution** — under continuing autonomous-mandate, they run without further PM gating; the engine-choice decision file lands as Proposed (not Accepted) pending PM AM-review of the full lock spec.

---

## §8 — Parallel-safety note

Phase C is parallel-safe with Phase D (differentiation swarm) per PROJECT-ARC.md §C "Parallel-safe with" block. Different surfaces, different agents, no overlap. Both R1 sets can run concurrently as background agents under the autonomous-mandate. R2 of either phase is the PM-fork gate; R3 of either runs after its R2.

---

*End of charter. R1 launch pending under autonomous-mandate (4 parallel background agents).*
