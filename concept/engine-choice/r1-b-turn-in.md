# R1-B Turn-in — Multiplayer netcode + port surface

**Date:** 2026-04-29
**Agent:** R1-B (Phase C engine-choice mini-arc)
**Charter:** [`concept/engine-choice/CHARTER.md`](CHARTER.md)
**Parent:** [`concept/PROJECT-ARC.md`](../PROJECT-ARC.md) §C
**Axes:** Multiplayer netcode (built-in stack, lockstep/rollback/server-auth options, matchmaking infra, PvP-Co-op latency budget tolerance) + port surface (how cleanly the prototype's preserved 50–55% deliverable-logic — state machines, balance numerics, AI scaffolds — maps to the engine's idioms).
**Engines:** Godot 4, Unity, Unreal Engine 5.
**Discipline:** evidence-quality tagged per claim (web-validated / inference-from-reputation / unverifiable). No engine pick.

**Mode-pair context:** Tower (Solo Campaign) + PvP-Co-op (Horde-A canonical) per [`decisions/2026-04-29-promise-1-scope-cut.md`](../../decisions/2026-04-29-promise-1-scope-cut.md). Horde-A is **latency-tolerant wave-survival co-op**, not competitive twitch. The PvP-Co-op label is a misnomer for netcode-fit purposes — the moment-to-moment shape is shared-PvE-against-waves with light cooperative coordination, closer to L4D / Deep Rock co-op pacing than to fighting-game rollback pacing. Tick-rate ceiling is the wave-clock + per-tower cooldown (T1 cd ≈ 1.15–1.7s per locked roster); per-frame state divergence sub-100ms is comfortable rather than load-bearing.

**Port-source context:** Per [`decisions/2026-04-29-prototype-port-source-re-supersession.md`](../../decisions/2026-04-29-prototype-port-source-re-supersession.md), port grain is **deliverable-logic, not literal code.** HTML/JS prototype is not portable as code. The portable substrate is: enum-shaped state machines (wave/round/skill-bar/combat phases), pure-numeric balance derivations (HP curve `100·1.16^R`, DPS ladder, Fusion-numerics 9-recipe lock, attack-type 7×5 RPS matrix, 45-tower magnitude matrix), AI scaffolds (target-priority + threat heuristics + 4-flag mobile unit control), data-driven configs (per-civ / per-commander / per-tower tables). The port-surface axis evaluates how cleanly these *shapes* map — entity-systems grammar, signal/event grammar, data-driven-table grammar — not how cleanly JS syntax translates.

---

## §1 — Godot 4

### Netcode

- **Built-in stack:** High-level MultiplayerAPI over `MultiplayerPeer` abstraction; ENetMultiplayerPeer (UDP, reliable + unreliable channels) is the default real-time transport; WebSocket and WebRTC peers also available; `MultiplayerSpawner` + `MultiplayerSynchronizer` nodes give scene-graph-native replication. *(web-validated)*
- **Authority model:** flexible per-node authority system; server-authoritative is supported but **you build prediction, reconciliation, interest management, and matchmaking yourself** — Godot ships none of the high-level automation. *(web-validated)*
- **Lockstep / rollback:** **no first-party rollback or deterministic-lockstep stack.** Community plugins exist (e.g. SG Physics 2D, GodotRollbackNetcode/SyncFramework lineage) but are non-Godot-team assets. *(web-validated for absence in core; inference-from-reputation for community plugin maturity)*
- **Matchmaking infra:** **none built-in.** Authentication, lobbies, matchmaking are developer responsibility. GodotSteam (community wrapper over Steamworks SDK) provides Steam Networking Sockets relay + lobbies + matchmaking; Steam's NetworkingUtils ping-to-relay table gives latency-aware matchmaking primitives. *(web-validated)*
- **PvP-Co-op (Horde-A) latency tolerance:** comfortable. MultiplayerSynchronizer scales 2–16 players cleanly per published guidance; bandwidth/CPU bottlenecks reportedly start at 32+. Horde-A's typical 2–4-player co-op shape sits well inside the comfortable band. The "no built-in client-side prediction" weakness that hurts twitch-PvP is not load-bearing for wave-clock-paced co-op. *(web-validated for player-count band; inference for Horde-A specifically)*
- **Reconnection caveat:** Godot's ENet has no built-in reconnection logic — disconnect/reconnect yields a new peer ID; session persistence is developer responsibility. *(web-validated)*

### Port surface

- **Entity systems:** Godot's node + scene grammar is a tree-of-instances, not an ECS. The 45-tower magnitude matrix + 3-civ × 5-unit roster ports cleanly to scene-instances + script-attached behavior; per-civ identity-hooks live as exported variables / resource files. *(inference-from-reputation)*
- **Signal/event grammar:** Godot signals are first-class; state-machine pattern is signal-on-enter / signal-on-exit, idiomatic across community guides. The prototype's enum-state-machine logic ports near-1:1 to GDScript `enum` + `match` or to node-based state-machine pattern. *(web-validated)*
- **Data-driven configs:** GDScript `Resource` system + `.tres`/`.json` loading is idiomatic for the per-tower / per-commander / per-civ tables. Fusion-numerics 9-recipe lock and attack-type 7×5 RPS matrix are pure-data tables that map directly. *(inference-from-reputation)*
- **Friction surface:** scripting in GDScript (or C# via Mono build) — neither matches JS exactly, but logic-port (not code-port) is the framing per re-supersession; the math/balance derivations transfer regardless of host language.

### Load-bearing finding (Godot 4)

**Netcode-fit is acceptable, port-surface-fit is high.** Godot's "you build the high-level pieces yourself" netcode posture is the load-bearing finding — it's a velocity tax for any team that wants matchmaking + prediction free, and a velocity *credit* for solo-dev who wants full control over a bounded netcode surface. Horde-A latency budget makes the missing rollback/prediction non-load-bearing. Port-surface is the strongest of the three engines for AtoA's logic shape because GDScript's signal + node + Resource grammar maps cleanly to enum-state-machines + data-tables + per-entity-script idioms.

---

## §2 — Unity

### Netcode

- **Built-in stack:** Netcode for GameObjects (NGO) is Unity's first-party framework; tightly integrated with Unity lifecycle, input, scene management. NGO is currently scoped primarily to small-scale cooperative games and pairs well with P2P in that category. *(web-validated)*
- **Third-party stacks (mature):** Mirror (open-source, UNet successor, full control); FishNet (indie/custom-server choice); **Photon Fusion** (lag compensation + client-side prediction + rollback + state-syncing first-class); **Photon Quantum 3** (deterministic lockstep, now a Unity Verified Solution — only major Unity option offering input/physics prediction + rollback at the determinism grain). *(web-validated)*
- **Lockstep / rollback:** Quantum is the deterministic-lockstep gold standard in the Unity ecosystem; Fusion provides server-authoritative + rollback. **Both are paid SaaS** with Photon's CCU-based pricing model (cost composes with paid-EA economics; relevant to R1-C scope, not R1-B). *(web-validated for capability; cost composition cross-references R1-C)*
- **Matchmaking infra:** Unity Gaming Services (Lobby, Relay, Matchmaker) is first-party; Photon Cloud is the dominant third-party matchmaker; both are mature and production-tested. *(web-validated)*
- **PvP-Co-op (Horde-A) latency tolerance:** dominant. NGO out-of-the-box covers Horde-A's coordination grain comfortably; if AtoA ever needs to add a competitive PvP mode (PvP-IW or PvP-Maze post-1.0 from the roadmap stretch), Fusion or Quantum is a drop-in upgrade path. *(inference-from-reputation; capability is web-validated)*
- **Caveat:** Netcode for Entities (NFE / DOTS-based) is targeted at RTS scale but is reportedly still maturing as of 2025–2026 community discussion. *(web-validated for status, inference-from-reputation for "maturing")*

### Port surface

- **Entity systems:** Unity's GameObject + MonoBehaviour grammar is the dominant industry idiom. The 45-tower matrix + 3-civ roster port to GameObjects + Components; per-civ identity-hooks live as ScriptableObject resources. DOTS/ECS is available if scale demands it later. *(inference-from-reputation)*
- **Signal/event grammar:** UnityEvents + C# `event`/`Action` delegates + ScriptableObject-based event-channels (a community pattern) cover the prototype's event needs. State-machine grammar ports cleanly to C# `enum` + `switch` or to behavior-tree assets. *(inference-from-reputation)*
- **Data-driven configs:** ScriptableObject is the idiomatic data-table substrate; Unity has the deepest tooling for per-entity authoring (Inspector edits, Addressables, asset pipeline). Fusion-numerics + attack-type RPS table map directly. *(inference-from-reputation)*
- **Friction surface:** scripting in C#; logic-port from JS to C# is a near-1:1 translation for pure-numeric derivations and enum-state-machines (both are C-family languages). Asset import pipeline is heaviest of the three engines but most mature.

### Load-bearing finding (Unity)

**Netcode-fit is dominant; port-surface-fit is high; cost-envelope coupling is the tax.** Unity is the only candidate where every netcode tier (P2P, server-auth, rollback, deterministic-lockstep) is available as a near-drop-in choice from a mature stack. For Horde-A specifically that ceiling is over-spec'd; for the post-1.0 PvP roadmap-stretch modes (PvP-IW, PvP-Maze) that ceiling is genuine optionality. The load-bearing risk is **runtime-fee history (2023 episode)** — under cascade discipline this is a per-PROJECT-ARC.md PM-Fork-6 reversibility consideration, but for R1-B's scope (netcode + port) Unity's technical posture is strongest-or-tied across both axes. Port-surface is high but slightly behind Godot on signal-grammar idiomatic-fit (Unity's events are not as scene-tree-native as Godot signals).

---

## §3 — Unreal Engine 5

### Netcode

- **Built-in stack:** server-authoritative replication is the engine's default model and is deeply integrated — the server has authority over game state by design; replicated UPROPERTY variables auto-sync; Network Relevance culling is built-in for bandwidth efficiency. *(web-validated)*
- **Authority model:** strict server-authoritative; client → server validation pattern is idiomatic; tower placements / upgrades / attacks pattern explicitly called out in community guidance as fit for the model. *(web-validated)*
- **Lockstep / rollback:** **no first-party deterministic-lockstep or rollback stack** in the AtoA-relevant sense. Unreal's GAS (Gameplay Ability System) has client-side prediction for ability casts but is not a general-purpose rollback netcode. *(web-validated for replication primitives; inference-from-reputation for absence of general rollback)*
- **Matchmaking infra:** Online Subsystem (Steam, EOS, etc.) is the matchmaking abstraction; Epic Online Services (EOS) is first-party-adjacent, free, and provides lobbies + matchmaking + relay. *(web-validated)*
- **PvP-Co-op (Horde-A) latency tolerance:** comfortable to over-spec'd. The replication system was built for Unreal Tournament / Fortnite / Gears of War scale; Horde-A's 2–4-player wave-survival shape is trivial relative to that ceiling. *(inference-from-reputation)*

### Port surface

- **Entity systems:** Actor + Component grammar; UPROPERTY-replicated state. The 45-tower matrix maps to AActor subclasses + DataTables. *(web-validated for DataTables idiom)*
- **Signal/event grammar:** Blueprint events + C++ delegates. State-machine grammar ports to enum + switch in C++ or to State Tree / Behavior Tree assets. Heaviest of the three engines for "set up an enum state machine quickly" because of the C++/Blueprint duality and the editor-asset overhead. *(inference-from-reputation)*
- **Data-driven configs:** DataTable / DataAsset / Curve assets are the idiomatic substrate; community tutorials exist for tower-defense data-table refactoring patterns. Fusion-numerics + RPS-matrix port to DataTables. *(web-validated for tower-defense data-table workflow)*
- **Friction surface:** **highest of the three.** Scripting is C++ (steep) + Blueprint (visual, mature but slower iteration on pure-logic shapes than text). 2D rendering is famously second-class — relevant to R1-A's axis but a port-surface adjacent concern because the AtoA visual grammar is small-entity-heavy 2D. Engine weight (project size, build times, editor footprint) is highest. For solo-dev velocity on a 2D logic-heavy port, the friction surface composes against the velocity gate.

### Load-bearing finding (Unreal Engine 5)

**Netcode-fit is over-spec'd-but-technically-sound; port-surface-fit is the lowest of the three for AtoA's specific logic shape.** Unreal's replication model is genuinely excellent for the latency-tolerant Horde-A pacing — server-authoritative is the right posture, Network Relevance handles the small-entity-count efficiency. The load-bearing concern is solo-dev velocity on the port-surface axis: porting deliverable-logic (state machines + balance numerics + AI scaffolds + data-driven configs) to a C++/Blueprint stack carries higher per-shape friction than to GDScript or C#. The 2D second-class concern (R1-A scope) compounds. For the AtoA logic shape specifically, Unreal's ceiling is irrelevant and its floor is heavier than the competing engines.

---

## §4 — Anti-cascade-violation lint vs locked surfaces

Per CHARTER §5 + PROJECT-ARC.md §3 cascade-respect block, R1-B checks each engine against the locked design substrate for any forced re-scoping:

| Locked surface | Godot 4 | Unity | Unreal 5 |
|---|---|---|---|
| 17-item conceptual frame (a)–(s) | clean | clean | clean |
| 10 Numbers-phase magnitudes (HP curve, DPS ladder, etc.) | clean (pure-data) | clean (pure-data) | clean (pure-data) |
| 6-mode ontology (2 feature-complete at 1.0 + 5 stretch) | clean | clean | clean |
| §4.7 Option C wave-variance + boss/regular pool | clean | clean | clean |
| §4.4 mobile unit control (4-flag catalog) | clean | clean | clean |
| Per-tower 45-magnitude matrix + 4 locks | clean | clean | clean |
| Per-civ 5-field profiles + 3-civ-3-equation fingerprint | clean | clean | clean |
| Attack-type 7-type RPS + 5-armor tags + status-proc | clean | clean | clean |
| Fusion-numerics 9-recipe Hard-lock | clean | clean | clean |
| §5.4 [LOCKED] naming conventions | clean (engine-internal naming separate per CHARTER §5) | clean | clean |
| §2.4a [LOCKED] accessibility floor (WCAG 2.3.1 etc.) | clean (engine-agnostic; some Unity/Unreal accessibility tooling more mature, but floor is reachable on all three) | clean | clean |
| Cosmetic-only / no-pay-to-win monetization model | clean (engine-agnostic) | clean | clean |
| Horde-A as PvP-Co-op canonical (latency-tolerant) | clean | clean | clean |
| Mobile (port-source) prototype's preserved 50–55% logic | clean (highest fit) | clean (high fit) | clean (lower fit, no hard block) |

**Zero anti-cascade flags from the netcode + port-surface axes.** No engine forces re-scoping of any locked surface from these two axes. RT-2 (PROJECT-ARC.md §8) does not fire on R1-B evidence. Differential velocity on the port-surface axis is real but is a velocity-gate concern (PM-Fork-6 deliberation), not a substrate-fit failure.

---

## §5 — Synthesis (no engine pick)

Across the netcode + port-surface axes, the three engines split along a **velocity-vs-ceiling axis** that maps cleanly onto AtoA's locked Horde-A latency-tolerant pacing and logic-heavy port shape. **Godot 4** offers the cleanest port-surface for the prototype's logic shapes (signals + nodes + Resources map near-1:1 to enum-state-machines + data-tables + per-entity behavior) and an acceptable netcode story for Horde-A pacing — the trade is that anything beyond P2P co-op (matchmaking, prediction, reconnection) is developer-built, which is a velocity tax that solo-dev may absorb cleanly given the bounded netcode surface a Horde-A + Solo-Campaign launch demands. **Unity** offers the dominant netcode ceiling — every tier from NGO P2P through Mirror server-authoritative through Photon Fusion rollback through Photon Quantum 3 deterministic-lockstep is a drop-in choice — and a high port-surface fit via ScriptableObject + C#, with the load-bearing tax being cost-envelope composition (R1-C scope) rather than technical fit. **Unreal Engine 5** offers an over-spec'd-but-sound replication model and the highest per-shape port friction (C++/Blueprint duality + 2D second-class status compounding) for AtoA's specific logic-heavy 2D-grammar shape; the cost-of-entry on this axis is the load-bearing concern.

The PvP-Co-op latency budget is **forgiving on all three engines** because Horde-A is shared-PvE-against-waves, not competitive twitch. The port surface is **differentially friction-mapped**: Godot lowest, Unity moderate-with-deepest-tooling, Unreal highest. The anti-cascade-violation lint is clean across all three from these two axes alone. PM-Fork-6 deliberation will compose R1-B findings with R1-A (tooling + 2D pipeline) and R1-C (hiring + royalty) before resolution.

---

*End of R1-B turn-in. Awaiting R1-A / R1-C / R1-D parallel completion + cross-bucket alignment-check before PM-Fork-6 brief assembly.*

## Sources

- [High-level multiplayer — Godot Engine docs](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html)
- [ENetMultiplayerPeer — Godot Engine docs](https://docs.godotengine.org/en/stable/classes/class_enetmultiplayerpeer.html)
- [SceneMultiplayer — Godot Engine docs](https://docs.godotengine.org/en/stable/classes/class_scenemultiplayer.html)
- [Multiplayer Networking in Godot 4: Authoritative Server (StraySpark)](https://www.strayspark.studio/blog/godot-4-multiplayer-networking-authoritative-server)
- [Godot Multiplayer in 2026: What Actually Works (Ziva)](https://ziva.sh/blogs/godot-multiplayer)
- [GodotSteam Networking Utils](https://godotsteam.com/classes/networking_utils/)
- [Unity Netcode vs Mirror vs Photon (uversedigital)](https://uversedigital.com/blog/unity-netcode-vs-mirror-vs-photon/)
- [Photon Quantum now a Unity Verified Solution (Photon blog)](https://blog.photonengine.com/the-evolution-of-deterministic-multiplayer-photon-quantum-now-a-unity-verified-solution/)
- [Photon Fusion product page](https://www.photonengine.com/fusion)
- [How to choose the right netcode for your game (Unity blog)](https://blog.unity.com/technology/choosing-the-right-netcode-for-your-game)
- [Multiplayer in Unity: Best Networking Solutions 2025](https://appwill.co/multiplayer-in-unity-best-networking-solutions-2025/)
- [Networking Overview for Unreal Engine 5](https://docs.unrealengine.com/5.0/en-US/networking-overview-for-unreal-engine/)
- [Multiplayer Network Compendium (Cedric Neukirchen)](https://cedric-neukirchen.net/docs/category/multiplayer-network-compendium/)
- [Tower Defense Starter Kit — refactoring tower data (Unreal forums)](https://forums.unrealengine.com/t/community-tutorial-32-refactoring-tower-data-2-lets-make-a-tower-defense-game/2275379)
- [Make a Finite State Machine in Godot 4 (GDQuest)](https://www.gdquest.com/tutorial/godot/design-patterns/finite-state-machine/)
