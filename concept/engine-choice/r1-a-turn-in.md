# R1-A Turn-In — Tooling-fit + 2D rendering pipeline

**Date:** 2026-04-29
**Axes:** (1) Tooling-fit — editor ergonomics, hot-reload, debugger, scene/prefab grammar, scripting language fit. (2) 2D rendering pipeline — sprite/atlas pipeline, particle systems, UI substrate, post-processing, fit for tower-defense visual grammar (many small entities, heavy projectile counts, readable silhouettes).
**Status:** R1 turn-in.
**Charter:** [`CHARTER.md`](CHARTER.md). Parent: [`../PROJECT-ARC.md`](../PROJECT-ARC.md) §C. Engines evaluated: **Godot 4, Unity, Unreal Engine 5.** Decision authority: **PM-Fork-6 only** — this turn-in does not pick.

---

## §1 — Godot 4

### Tooling-fit

Godot 4 ships a single integrated editor with a tree-of-Nodes scene grammar; "prefabs" are PackedScenes (any scene can be instanced inside another). Scripting is GDScript (first-class, idiomatic), C# (Mono/.NET 8 path, second-class but supported), and GDExtension (C++ for hot paths). The editor runs on the engine itself, which means the editor and game share rendering quirks — a pro for visual fidelity dev-time, a con when editor regressions ship together with runtime regressions. `[web-validated]`

Hot-reload: GDScript supports live script reload; scene changes pick up on save. C# hot-reload is functional but has historically been the rougher path and requires editor restarts on certain class-shape changes. `[inference-from-reputation]` Debugger: built-in step debugger, scene-tree inspector at runtime, remote-inspect of running scene. Profiler is functional but lighter than Unity's. `[inference-from-reputation]`

Scripting fit for AtoA data shapes (RPS tables, Fusion 9-recipe lock, per-civ identity-hooks): GDScript handles dictionary/array literals cleanly and is closest to the prototype's HTML/JS deliverable-logic shape; the 7-attack × 5-armor RPS matrix and 9-recipe Fusion table port as nested dicts with minimal ceremony. C# gives static typing for balance-numerics validation if PM wants compile-time checks on per-tower magnitudes. `[inference-from-reputation]`

### 2D rendering pipeline

Godot's 2D path is a dedicated renderer (not 3D-faked-as-2D), with automatic CanvasItem batching, light culling, and a 2D-native particle system (GPUParticles2D + CPUParticles2D). `[web-validated]` The common performance trap is unique-texture / custom-material proliferation breaking batches; mitigation is sprite-atlas discipline and the RenderingServer API to bypass scene-tree overhead for hundreds-of-similar-entities cases. `[web-validated]` Real-world reports show scene-tree pressure at ~500 nodes-with-sprites on commodity hardware; the RenderingServer escape hatch is the documented path past that ceiling. `[web-validated]`

UI substrate: Control nodes are first-class with anchor/margin layout; theme system is mature; same renderer as gameplay so HUD/overlay composition is direct. Post-processing: WorldEnvironment + custom shaders (Godot Shading Language, GLSL-adjacent). Tower-defense visual grammar fit: many small entities is the sweet spot if atlas discipline holds; heavy projectile counts want the RenderingServer path or pooled CPU/GPU particles. `[inference-from-reputation]`

### Load-bearing finding (Godot 4)

What genuinely matters: the **scene-tree-vs-RenderingServer split** for projectile-heavy tower-defense. AtoA's per-tower magnitudes + per-mode N-scaling will produce hundreds of simultaneous projectiles at higher rounds; scene-tree-of-Sprite2D nodes hits the ~500-node ceiling fast, and RenderingServer is the documented out. This is not an engine flaw — it is an engineering pattern Godot expects the dev to know. What is noise: GDScript-vs-C# debate is a preference axis, not a substrate-fit axis; both work. Editor-on-engine criticism is also noise at this project's scale.

---

## §2 — Unity

### Tooling-fit

Unity ships a mature editor with GameObject + Component + Prefab grammar. Prefabs are first-class with Prefab Variants (override one prefab from another) — load-bearing for AtoA's 3-civ × 6-tower × per-tier-shape variant explosion. Scripting is C# (Mono/IL2CPP); no scripting alternative. `[web-validated]`

Hot-reload: domain reload on script change is the historical pain point; Unity has invested in faster Enter Play Mode (configurable domain-reload skip) and live-reload paths, but it remains slower-than-Godot iteration in the common case. `[inference-from-reputation]` Debugger: Visual Studio / Rider integration is first-class, profiler is industry-leading (CPU, GPU, memory, frame debugger), Unity Profiler + Frame Debugger are the gold standard. `[inference-from-reputation]`

Scripting fit for AtoA: C# with ScriptableObjects is a strong fit for balance-numerics, RPS tables, Fusion recipes — ScriptableObject as data-asset means designers (or PM-as-designer) edit per-tower magnitudes in the inspector without recompiling. The 7-attack × 5-armor matrix lives cleanly as a ScriptableObject lookup. `[inference-from-reputation]`

### 2D rendering pipeline

Unity's 2D substrate is mature: SpriteRenderer + Sprite Atlas + 2D Animation + 2D Light + Tilemap + URP 2D Renderer. Unity 6.3 LTS (late 2025) added Sprite Atlas Analyzer for atlas-optimization workflow. `[web-validated]` URP 2D Renderer supports 2D lights, sprite mask shaders, native anti-aliasing for sprite edges. `[web-validated]` In 2026 Unity unified URP/HDRP under the same compiler/API, simplifying the render-pipeline picture. `[web-validated]`

Particle system: Shuriken (mature, GPU-accelerated VFX Graph also available). UI substrate: UGUI (mature, performant for HUDs) + UI Toolkit (newer, more flexible). Post-processing: URP post-process stack is comprehensive. Tower-defense visual grammar fit: heavy projectile counts handled cleanly via object pooling + Shuriken; readable silhouettes via 2D lights and sorting layers; many small entities is well-trodden ground (BTD6 reference class, though BTD6 is custom-engine). `[inference-from-reputation]`

### Load-bearing finding (Unity)

What genuinely matters: **Prefab Variants + ScriptableObject data-asset grammar** is a near-perfect match for AtoA's 3-civ × 6-tower × tier-variant + per-civ-identity-hook structure. Designer-editable balance numerics in inspector without code changes is a solo-dev velocity win directly addressing the locked per-tower magnitude matrix. What is noise: domain-reload latency is real but mitigatable; the Unity-runtime-fee history (rolled back) is a licensing-layer concern (R1-C territory), not a tooling-fit concern. Prefab Variants are the load-bearing tool fit.

---

## §3 — Unreal Engine 5

### Tooling-fit

UE5 ships a heavyweight editor with Actor + Component + Blueprint grammar. Blueprints are visual scripting; C++ is the systems-language path; Blueprints-only is viable for many indie projects. The editor itself is large (multi-GB install, multi-minute cold start) and the iteration loop carries weight. `[inference-from-reputation]`

Hot-reload: C++ Live Coding (Visual Studio integration) works but is the most fragile of the three engines — class-shape changes often require editor restart. Blueprint changes hot-reload cleanly. Debugger: Blueprint visual debugger + C++ Visual Studio debugger; Unreal Insights is a powerful profiler. `[inference-from-reputation]`

Scripting fit for AtoA: C++ + Blueprint is overkill for AtoA's data shapes. DataTable + UDataAsset can hold balance-numerics, but the ceremony cost (UCLASS reflection, header-source split, build times) is high relative to AtoA's data-shape complexity. The 7-attack RPS matrix as a DataTable works but is not idiomatic. `[inference-from-reputation]`

### 2D rendering pipeline

UE5's 2D path is **second-class.** Native Paper2D is the sprite-based system; PaperZD is the third-party extension widely cited as "the definitive answer to Unreal's lack of 2D animation support" — which is itself a tell about Paper2D alone. `[web-validated]` Particle system (Niagara) is the strongest of the three engines but built for 3D-cinematic effects; using it for 2D projectile counts is using a sledgehammer. UI substrate: UMG (Unreal Motion Graphics) is mature for menu UI; in-game HUD overlay for high-entity-count 2D scenes is workable but ergonomically heavy. Post-processing: industry-leading for 3D, less aligned to 2D readable-silhouette goals. `[inference-from-reputation]`

Tower-defense visual grammar fit: UE5 can do it, but the engine fights you. Many small entities + heavy projectile counts in pure 2D is not what UE5's runtime is optimized for at the API surface; you would either rely on Paper2D + PaperZD (third-party dependency) or render 2D-styled assets through 3D meshes (different art pipeline). `[inference-from-reputation]`

### Load-bearing finding (Unreal Engine 5)

What genuinely matters: **2D is second-class in UE5, and the workaround stack (Paper2D + PaperZD) is third-party-dependent.** AtoA's substrate (per-tower magnitudes, projectile counts at higher rounds, readable-at-glance silhouettes) is exactly the workload UE5 is least suited to among the three. What is noise: UE5's 3D ceiling and Niagara firepower are not relevant to AtoA — the project does not need them. Solo-dev velocity is the load-bearing axis the charter names; UE5's editor weight + 2D second-class status compound against velocity.

---

## §4 — Anti-cascade-violation lint

Charter §5 names the locked surfaces engine choice must honor: per-tower magnitudes (45-tower matrix), attack-type 7-type RPS + 5-armor tags, Fusion 9-recipe lock, mobile unit control 4-flag catalog, 6-mode ontology with 2 feature-complete at 1.0.

**Godot 4:** No cascade violation surfaced on the tooling-fit + 2D rendering axes. The RenderingServer escape hatch handles projectile-count pressure without re-scoping per-tower magnitudes or per-mode N-scaling. RPS matrix and Fusion recipes port as data with no structural friction.

**Unity:** No cascade violation surfaced. ScriptableObject + Prefab Variant grammar absorbs the 45-tower matrix and 9-recipe Fusion lock cleanly. 2D Renderer handles the visual-grammar load.

**Unreal Engine 5:** No cascade violation surfaced strictly on these two axes — UE5 *can* honor the locked surfaces. But the velocity cost to do so via Paper2D + PaperZD + DataTable ceremony is a soft-pressure-toward-re-scoping risk: a solo dev under runway pressure who picks UE5 may downstream propose to "simplify" per-tower magnitudes or projectile counts to fit the engine, which would be RT-2 territory. **Flagged as soft-pressure, not hard violation.**

No engine in the candidate set forces re-scoping of a locked surface on these axes. RT-2 is not triggered by R1-A evidence.

---

## §5 — Synthesis (no engine pick — PM-Fork-6 only)

On tooling-fit and 2D rendering pipeline considered together, **Godot 4 and Unity both clear the substrate-fit gate cleanly; Unreal Engine 5 clears it only with notable velocity cost.** Godot 4's strengths are integrated-editor iteration speed, dedicated 2D renderer, and GDScript proximity to the prototype's deliverable-logic shape; its weakness is the scene-tree-vs-RenderingServer pattern at projectile-heavy scale, which is an engineering-discipline cost not an engine-flaw cost. Unity's strengths are Prefab Variants + ScriptableObject grammar mapping near-perfectly to AtoA's civ/tower/variant structure, plus an industry-leading profiler and the deepest 2D toolchain across the three; its weakness is domain-reload iteration latency relative to Godot. Unreal Engine 5's strengths (3D ceiling, Niagara) are not load-bearing for AtoA, while its weaknesses (2D second-class, editor weight, ceremony cost) are directly load-bearing against solo-dev velocity. On these two axes alone the strongest fits are Godot 4 and Unity in close contention; UE5 trails. PM-Fork-6 awaits R1-B (netcode + port surface) and R1-C (hiring / royalty) before resolving.

*End of R1-A turn-in. R1-B / R1-C / R1-D run parallel. Alignment-check between R1 and R2 follows per CHARTER §3.*
