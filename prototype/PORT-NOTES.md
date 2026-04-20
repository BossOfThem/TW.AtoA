# PORT-NOTES — Prototype → Godot 4

**Status:** Draft (Step 6 sweep, 2026-04-20). Appended to as prototype patterns emerge.
**Purpose:** Map every JS pattern in `prototype/index.html` to its Godot 4 idiom. Port **findings and data**, not code (see [decisions/2026-04-19-design-prototype-scope.md](../decisions/2026-04-19-design-prototype-scope.md)).

The prototype is the de-facto spec. This file is the recipe for copying it without reinventing it.

---

## Data

| JS pattern | Godot 4 idiom | Notes |
|---|---|---|
| `prototype/data/balance.json` — flat constants + nested groups | [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html) subclass `BalanceData.tres` | One `.tres` per logical group (wave/age/economy/base) or one fat resource; preference TBD. Test hot-reload in editor. |
| `prototype/data/towers.json` — per-lineage base stats + color/label | Array of `TowerData.tres` resources at `res://data/towers/` | Each tower = one `.tres`; `@export` every field for editor visibility. |
| `prototype/data/commanders.json` — roster with `playable` flag per entry + `active` pointer | `CommanderData.tres` array at `res://data/commanders/`; `active` pointer = player-state (savegame), not data | Distinguish data (immutable) from save-state (mutable). `@export` every display field (name, epithet, lore, lineageTilt, stats.passive, stats.signature) so designers edit in-editor. `playable` gates visibility in Pick scene. |
| Derived tables (`TOWER_STATS`, `WAVE_DEFS`) rebuilt at init | Same pattern: compute on match start, cache on a singleton/autoload | Don't pre-compute at load time — lets data tweaks in editor take effect. |

## Scenes

| JS pattern | Godot 4 idiom | Notes |
|---|---|---|
| `<div class="scene">` + `goto()` swaps `.active` class | Separate `PackedScene`s per screen; `get_tree().change_scene_to_packed()` | Title / Pick / Tutorial / Match / End = 5 scenes. |
| Shared HUD markup duplicated between tutorial + match scenes | One `HUD.tscn` instanced in both match-shaped scenes | Drop the `hudPrefix` JS hack. |
| `setupBoard()` + cell grid generated at scene entry | `Board.tscn` with `TileMap` for placement cells; `Path2D` for the creep lane | Lose the per-frame cell-dist math — Godot nav handles it. |
| `renderCommanderRoster()` — filter roster by `playable`, build chip row, hide if ≤1 | `CommanderPick.tscn` with `HBoxContainer` of `Button` nodes generated from `CommanderData` array filtered by `playable`; hide container if count ≤ 1 | Chip-per-commander with `pressed` signal → `select_commander(id)`. Selected-state = `StyleBoxFlat` swap or `ButtonGroup` toggle, not class list. Card content swap mirrors existing pattern. |

## Balance / derivations

| JS pattern | Godot 4 idiom | Notes |
|---|---|---|
| `deriveTowerStats()` — base × `DAMAGE_PER_AGE ^ age` | Same math inside `Tower.gd`; exposed via `get_damage(age: int)` | Trivial port. |
| `deriveWaveDefs()` — compounding multipliers | `WaveGenerator.gd` singleton reads `BalanceData` | Keep the compounding model — it's the concept. |
| `logBalanceCurve()` — `console.table` of solvability | Editor-time tool script + `print_rich()` | Consider an in-editor dock plugin later. |

## Input

| JS pattern | Godot 4 idiom | Notes |
|---|---|---|
| `canvas.addEventListener("click", onBoardClick)` + cell hit-test | `_input(event)` on `Board.tscn` + `Area2D` per cell | Let Godot dispatch the hit-test; delete the JS math. |
| `document.getElementById(...)` + `onclick=""` on buttons | `Button` node + `pressed` signal | Standard. |
| Hover tooltip (`onBoardMove` → `showTip`) + right-click ctx menu (`onBoardContext` → `showCtxMenu`) | `_input(event)` + `MOUSE_BUTTON_RIGHT` + `PopupMenu` node; tooltips via `Control.tooltip_text` or custom `CanvasLayer` panel | Prototype uses raw DOM overlays positioned in canvas space; Godot has first-class primitives. |
| **Target priority** (First / Last / Strongest / Nearest) — **not shipped in prototype** | Per-tower enum `@export var target_priority: TargetPriority` on `Tower.gd`; radial or dropdown UI in the right-click panel | Deferred from prototype per [decisions/2026-04-20-prototype-interaction-layer.md](../decisions/2026-04-20-prototype-interaction-layer.md); owed to Godot port per CONCEPT §4.4 mobile-unit-control intersection. |

## Visuals

| JS pattern | Godot 4 idiom | Notes |
|---|---|---|
| `ctx.fillStyle` + `ctx.fillRect` / `ctx.arc` per frame | `Node2D._draw()` override or `Sprite2D` per entity | For MVP slice: `Node2D._draw()` is cheapest. Sprites come with art. |
| `requestAnimationFrame(gameLoop)` | `_process(delta)` or `_physics_process(delta)` | Use `_physics_process` for anything that interacts with collisions. |
| Hardcoded CSS colors (`--ember`, `--sinew`) | Godot `Theme` resource + per-lineage `StyleBox` | Centralize. |
| `renderSilhouette(ctx, kind, ...)` — 6 canvas-primitive archetypes keyed off `enemies.json[i].kind` | One `EnemyArchetype.tres` per kind, paired with `Polygon2D` or `AnimatedSprite2D` scene; swap art in without re-authoring code | Port the archetype *taxonomy*, not the primitive paths. The prototype's hex/triangle primitives are the spec vehicle; Godot gets real art in the same shape slots. |
| `renderTowerHex` — 6-sided polygon + unicode glyph + level-crown chevrons + dashed border for guest-owned | `Tower.tscn` with `Polygon2D` base + `Label`/`TextureRect` for glyph + `Line2D`-drawn chevrons + `StyleBoxFlat` border swap on ownership | Encode per-tower-level visuals as `AnimationPlayer` "L1/L2/L3" animations on the shared Tower scene. |
| Per-lineage projectile shapes (dart/spark+trail/hex-bolt/chevron-pair/wavy-bezier/split) | `Projectile.tscn` per lineage OR one scene with a `LineageKind` enum picking between `CPUParticles2D`/`Line2D` presets | Trail decay (`alpha *= 0.85` per frame in JS) maps to `CPUParticles2D.lifetime` + gradient. |
| Muzzle flash (3-frame radial burst on shot creation) | `CPUParticles2D` one-shot or `Sprite2D` + `Timer` on tower node | Keep cheap — it's a feedback signal, not a hero effect. |
| Floating damage numbers (white/gold/grey rise-fade per hit) | `Label` pool via object-pool autoload; `AnimationPlayer` or `Tween` for rise + alpha-fade; colors as theme variants | Respects a11y reduce-motion (skip the rise, keep the pop). |
| Enemy status-icon stack (slow / burn / armor / shield / marked, TTL-ticked) | `Control` container above enemy; one icon scene per status kind; TTL driven by a component on the enemy | Status *application* (who applies what) lives in tower scripts; this row is the visual-only deliverable. |
| HP bar + threat bar (distance-to-exit, pulses red <15%) | `ProgressBar` stack or custom `Control._draw()`; red pulse via `AnimationPlayer` on a `modulate` property | Threat bar toggleable via a gameplay option; expose as a `@export var show_threat_bar: bool`. |
| Next-wave telegraph strip (mini silhouettes + counts before Send-Wave) | `HBoxContainer` populated from `WaveData` resource; chip-scene `Control` with silhouette + `Label` count | Hide container while `wave_active`. |
| Combat feed (kill / leak / hybrid / upgrade / wave rows, 4s fade) | `VBoxContainer` + per-row scene with `Tween` for fade-out; critical events (leak/defeat/hybrid) hold 6s + bold | Reduce-motion path skips fade, just hard-dismisses. |
| Splash glyph build-in (`ASH TO ALTAR` char-by-char, 3s, skippable, reduce-motion → 300ms hard-cut) | `AnimationPlayer` on a `Control` with per-character `Label` children; reduce-motion bypasses the anim and sets `modulate.a = 1` directly | Respect `UserSettings.reduce_motion`. Click/keypress anywhere advances. |
| Mode-aware pause (Campaign=hard+save, Skirmish=hard, Horde=host-vote 10s timeout, LaneWars=read-only) | `get_tree().paused = true` for hard modes; custom overlay `Control` for LaneWars read-only; host-vote via `rpc("request_pause_vote")` + `Timer` for 10s timeout | Lane Wars overlay sets `process_mode = PROCESS_MODE_ALWAYS` on the HUD. |
| Profile scene (roster + XP + cosmetic counts + settings summary + Logout) | `Profile.tscn` with `HFlowContainer` of commander cards; `ProgressBar` per XP; `ConfigFile.save()` on Logout confirm | Local-only by SAVE-01; no multi-profile until Phase 5. |
| Options 5 tabs persisted to `Profile.settings` (Audio/Input/Video/Accessibility/Gameplay) | `TabContainer`; each tab debounces writes via `Timer` → `ConfigFile.save()`; Audio sliders map to `AudioServer.set_bus_volume_db` + `AudioEffectCompressor` for ducking; Input rebind via `InputMap.action_add_event()` | Gameplay auto-age-up toggle wires to the same age-gate signal that fires the banner. |
| SVG commander silhouettes (5 lineage primitives + grayscale silhouette-test) | `CommanderSilhouette.tscn` per lineage w/ `Polygon2D` body + `Sprite2D` accent; grayscale test via shader (`modulate` saturation=0) | `?silhouette-test=1` URL is a debug-menu toggle in Godot. |
| 20-level XP ladder + L5/L10/L15 cosmetic unlocks + 3 cosmetic slots | `CommanderProgress` Resource w/ `level`/`xp`/`xp_to_next` + `CosmeticSlots.tres` (skin/frame/map-tint); unlock toasts on `level_up` signal | Chips show lock state until unlocked. |
| First-run prompts (right-click / I-key / hover) with permanent dismiss | `Toast.tscn` bound to `Profile.settings.first_run.*` flags; 8s auto-dismiss `Timer` | Tutorial suppresses these — its narrator covers them. |
| Age-gate cinematic banner (2.5s) reading `ages.json` `eraDescriptor`/`lore`/`motif` + Campaign autosave | `AnimationPlayer` on overlay `Control`; reduce-motion path = 400ms `Tween` on `modulate.a`; `ConfigFile.save()` on Campaign age-gate signal | 2-4 min loss window floor per SAVE-01. |
| `data/mapmods.json` (6 biomes: neutral/volcanic/frostfall/verdant/coastal/ruins, passive modifiers) | `res://data/mapmods/*.tres` as `MapMod` Resource array; Skirmish `MatchConfig.biome.modifier` applied at match spawn | Skirmish chip UI wires post-Step-5 playtest. |
| `data/events.json` (8 spontaneity events — LCG seeded, 25% probability, weighted pool, no-two-in-a-row, additive co-op broadcast) | `res://data/events/*.tres` as `SpontaneityEvent` Resource; `RandomNumberGenerator.seed = match_start_unix_ms` for co-op determinism; `rpc_id(guest, "show_event_banner", id)` for host-authoritative propagation | Off-switch at `Profile.settings.gameplay.spontaneity`. Balance invariant: E[effect] ≈ neutral across boons + downsides. |
| Commander-on-Field Avatar (1.4× silhouette + 2-cell aura + Shift/C+click move 1/wave + Q signature 60s CD / 8s + non-destructible knock-back) | `CommanderAvatar.tscn` = `CharacterBody2D` + `Sprite2D` + `Area2D` aura child + `Timer` for signature CD/duration; click-to-move = `NavigationAgent2D` path; knock-back = `move_and_collide` with home-direction vector; non-destructible = collision layer excludes enemy layer | Aura passive applied via `body_entered`/`body_exited` on `Area2D` adding a `Modifier` child to each tower inside. Signature `rpc("fire_signature")` host-authoritative. Snapshot additive (`commander:{x,y,lineage,cd,sigActiveTtl,auraCells}`). Balance stop-gap: if aura covers <40% of wave-6 towers, widen to 3 cells. |

---

## How to use this file

- **Before writing any new prototype feature:** check if a Godot idiom row already exists. If yes, mirror it. If no, add a row.
- **After finishing a prototype feature:** sweep this file and add any new rows that emerged. Step 6 in the approved plan is a dedicated sweep pass.
- **When porting to Godot:** this file is the checklist. Every row should map to a concrete `.tscn` / `.gd` / `.tres` deliverable.

## Deliberately not here

- Full Godot project structure — Phase 5 territory.
- Specific node names for gameplay systems not yet in the prototype (age gate, hybrid discovery, mode select, commander hero).
- Art pipeline — Phase 4 exit gate.
- **Audio and Telemetry rows** — removed 2026-04-20 per PROGRESS Step 1.5b. The prototype has no audio or telemetry system yet; speculative Godot-idiom rows were creating false spec. Audio architecture is committed at CONCEPT §3.10 (5-bus + ducking + focus-loss); the Godot mapping gets added here *when the prototype or an engine sketch actually uses buses*. Telemetry gets added when PROGRESS Step 2 (optional telemetry dump) lands.
