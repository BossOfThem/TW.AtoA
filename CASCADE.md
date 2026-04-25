# CASCADE — navigation spine for Ash to Altar

The canonical index. Every doc links from here in the order a new reader (human or Claude) should encounter it. If you are a new session: **`README.md` → `CLAUDE.md` → this file → target doc.** Do not hunt.

Non-negotiables + naming conventions + cascade discipline live in [`README.md`](README.md) + [`CLAUDE.md`](CLAUDE.md); this doc is pure navigation.

---

## How the doc tree works

The project uses a waterfall cascade (see [`CONCEPT.md`](CONCEPT.md) Phases 1–7). It shows up in three places:

1. **Conceptual cascade** — Phases 1–7 in `CONCEPT.md`. Discovery → Analysis → Design → Specification → Implementation → Validation → Iteration. Phase N+1 does not silently edit Phase N.
2. **Player-journey cascade** — [`stages/`](stages/) dir. One doc per player-experience stage, 200–600 lines each.
3. **Research cascade** — [`research/`](research/) dir. Deep-dive market evidence feeding stage decisions. Written *before* the stage that depends on it.

Cross-link convention:
- Stage-to-stage: `[stage 03 — match setup](stages/03-match-setup.md#section)`
- Stage-to-research: `[theme-era §2.3](research/02-theme-era.md#23-pirate-signal)`
- Decisions: `[2026-04-20 <slug>](decisions/2026-04-20-<slug>.md)`
- Concept anchors: `[CONCEPT §3.3](CONCEPT.md#33-the-five-lineages-mechanical-identity-within-a-match)`

Every stage / research doc carries a **Status** (Stub | Draft | In review | Locked) and **Last reviewed** date. When in doubt about freshness, trust the date.

---

## Reading order (new session)

1. [`README.md`](README.md) — status, non-negotiables, critical context.
2. [`CLAUDE.md`](CLAUDE.md) — session conventions, cadence, 3x debug loop.
3. [`HANDOFF.md`](HANDOFF.md) — last-session checkpoint.
4. This file — the map.
5. [`PROGRESS.md`](PROGRESS.md) — step tracker; first unchecked box = next step (unless queue paused).
6. [`CONCEPT.md`](CONCEPT.md) — vision hub. Phase content lives under [`concept/phase-1..7.md`](concept/); open only what you need. Stage-level drill-downs in `stages/`.
7. [`CONCEPT-GAPS.md`](CONCEPT-GAPS.md) — ephemeral proposal layer; rows migrate into CONCEPT via ratified decisions.
8. [`admin/concept.json`](admin/concept.json) — PM's structured edits. Diff against `HANDOFF.md` state snapshot.
9. Target stage / research doc per "Current work pointer" below.

---

## Current work pointer

**2026-05-04 (latest, end-of-day) — 12-round conceptual ratification COMPLETE: balance-pass #1 frame + 6-mode ontology + auxiliary economy + frame extension all locked.** Single end-to-end session ran 12 `AskUserQuestion` rounds across two arcs. **Arc 1 (Rounds 1-5):** balance-pass #1 conceptual frame — 17-item ratification covering variable nomenclature (a)–(r), master damage equation, 7-slot round typology, single-axis (k) HP-curve compounding, 4-step sell-refund schedule, targeting AI, boss-reward shape, interim Divinity-source pattern, skill-bar axes. Filed [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) (Accepted, Medium). **Arc 2 (Rounds 6-12):** auxiliary economy + 6-mode ontology — Round 6 ratified modular-slot-system + Tribute/Divinity split + "go big, no scope cuts" doctrine + Send-Creeps broad adoption (filed [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](decisions/2026-05-04-round-6-aux-economy-ratifications.md)). Per-mode deep dives: Solo Campaign multi-mission saga / single-lane / per-mission (k) / Universal slots ([`round-7`](decisions/2026-05-04-round-7-solo-campaign-deep-dive.md)); Horde **split into 2 modes** (Horde-A lane-defense + Horde-B shared-front-N-scaling), per-player wallet, linear N-multiplier, Universal slots ([`round-8`](decisions/2026-05-04-round-8-horde-coop-deep-dive.md)); PvP Interest Wars 20s rounds, **30-leak knockout + tie-break escalation + co-victory**, free-target sends, Send-for-Interest enabled, **frame item #12 lives extended to per-mode** ([`round-9`](decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md)); PvE Multiplayer N-lanes parallel, last-alive, view-only spectate, Lane-Trade + Call-for-Help ([`round-10`](decisions/2026-05-04-round-10-pve-mp-deep-dive.md)); PvP Maze hex-grid-preserved + A* pathfinding + cheap-stone-upgradable + Send-Through-Maze ([`round-11`](decisions/2026-05-04-round-11-pvp-maze-deep-dive.md)). Round 12 final closures: in-match side-panel aux UX, **frame variable (s) first-class multiplicative**, (k) PvE-only / PvP player-driven, pre-placement gray-out maze validity ([`round-12`](decisions/2026-05-04-round-12-aux-ux-frame-extension.md)). Auxiliary-economy-scope decision advances Proposed → Accepted; all 10 axes ratified. Send-Creeps cross-mode classification finalized: 3-mode mechanic (PvE-MP / PvP-IW / PvP-Maze). Mode count expanded 5 → **6** per "go big" doctrine (Horde split). Frame item #3 master equation extended with variable (s); frame item #12 lives amended per-mode (default 10; PvP-IW 30). CONCEPT-GAPS rows ECON-04 + MODE-01 advance to RESOLVED. Numbers-phase Follow-up #13 now fully unblocked. **No code edits** — pure concept/math work. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched. 7 new decision documents this session.

*Prior pointer blocks archived to [`CASCADE-history.md`](CASCADE-history.md).*

**Next planned work:**
1. **Follow-up #13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts). Critical post-graduation: flat curve still untuned; load-bearing.
2. **`admin/concept.json` migration direction** — long-deferred. PM picks: full rewrite to 3-civ/4-tier/Fusion shape, regenerate from CONCEPT.md, or retire entirely.
3. **Follow-up #5 cultural-sensitivity pass scheduling.** Hard pose-lock + content-lock gate before any culturally-coded civ art ships. Gate on Aztec glyph re-evaluation (post #4 abstract-placeholder interim) and Greek/Norse glyph audit also rolls under this.
4. **Follow-up #6** — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.
5. **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
6. Other follow-ups #7 / #8 / #9 (Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology).

Workflow upgrade Steps 0, 1, 1.5a remain complete. `PROGRESS.md` is the live step tracker.

---

## Stages — player-journey cascade

Strict downstream order. Do not open Stage N content work until Stage N-1 is at least "In review."

| # | Stage | Status | What it covers |
|---|-------|--------|----------------|
| 00 | [Session start](stages/00-session-start.md) | Draft | App launch, splash, main menu, first-time vs returning, accessibility floor. |
| 01 | [Commander pick](stages/01-commander-pick.md) | Draft | Roster size, archetype slots, first-pick UX, change-commander policy. **Identity moment.** |
| 02 | [Mode select](stages/02-mode-select.md) | Stub | Launch modes, matchmaking, lobby UX. |
| 03 | [Match setup](stages/03-match-setup.md) | Stub | Map pick, lane assignment, starting economy, pre-wave build, commander banner. |
| 04 | [In-match core](stages/04-in-match-core.md) | Stub | Waves, tower combat, economy, send/defend, Mythium. |
| 05 | [Age evolution](stages/05-age-evolution.md) | Stub | Age Gate UX, auto-evolution, divergence forks, age-persistence callback. |
| 06 | [Hybrids & fusion](stages/06-hybrids-fusion.md) | Stub | Adjacency rules, hybrid discovery, cross-lineage rares. |
| 07 | [Match end](stages/07-match-end.md) | Stub | Victory/defeat, stats, XP, drops, next-match nudge. |
| 08 | [Meta progression](stages/08-meta-progression.md) | Stub | Commander XP, backpack, battle pass, store. |

---

## Research — deep-dive market evidence

Methodology per [`00-methodology.md`](research/00-methodology.md). Sources prefer 2024–2026 freshness. Every section ends with a "so what for this game" synthesis.

| # | Research doc | Status | Feeds into |
|---|--------------|--------|------------|
| 00 | [Methodology](research/00-methodology.md) | Draft | All research |
| 01 | [Genre pulse](research/01-genre-pulse.md) | Stub | Stage 02 (mode select) |
| 02 | [Theme & era](research/02-theme-era.md) | Stub | Stages 03, 05 — era-spine decision |
| 03 | [Commander archetypes](research/03-commander-archetypes.md) | Draft | Stage 01 |
| 04 | [Monetization & live-ops](research/04-monetization-liveops.md) | Stub | Stages 07, 08 |
| 05 | [Demographics & platform](research/05-demographics-platform.md) | Stub | Stages 00, 02 |

---

## Decisions — dated log

Every concept-constraint change + every ratified gap-resolution lives here. Format: [`TEMPLATE.md`](decisions/TEMPLATE.md).

| Date | Decision | Reversibility |
|------|----------|---------------|
| 2026-05-04 | [Round 12: Aux UX + frame variable (s) + per-mode (k) + maze validity — in-match side-panel; (s) first-class multiplicative; (k) PvE-only; pre-placement gray-out](decisions/2026-05-04-round-12-aux-ux-frame-extension.md) | Medium |
| 2026-05-04 | [Round 11: PvP Maze Lane deep-dive — hex-grid preserved, A* pathfinding, cheap stones upgradable to T1, Send-Through-Maze, lives=10](decisions/2026-05-04-round-11-pvp-maze-deep-dive.md) | Medium |
| 2026-05-04 | [Round 10: PvE Multiplayer deep-dive — N parallel lanes, last-alive, view-only spectate, Lane-Trade + Call-for-Help slots](decisions/2026-05-04-round-10-pve-mp-deep-dive.md) | Medium |
| 2026-05-04 | [Round 9: PvP Interest Wars deep-dive + frame-#12 lives extension — 20s rounds, 30-leak knockout, tie-escalation + co-victory, Send-for-Interest, lives per-mode declarable](decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md) | Medium |
| 2026-05-04 | [Round 8: Horde Co-op deep-dive + co-op mode split — Horde-A (per-player adjacent lanes + leak-bleed) + Horde-B (shared lane, N-scaling map); per-player wallet; linear N-multiplier](decisions/2026-05-04-round-8-horde-coop-deep-dive.md) | Medium |
| 2026-05-04 | [Round 7: Solo Campaign deep-dive — multi-mission saga, single-lane map-shaped paths, per-mission (k), Universal slots only](decisions/2026-05-04-round-7-solo-campaign-deep-dive.md) | Medium |
| 2026-05-04 | [Round 6: Auxiliary economy ratifications + "Go big, no scope cuts" project doctrine — modular slot system, Tribute/Divinity split, all-5-modes-at-launch (became 6 after Round 8), Send-Creeps broad adoption](decisions/2026-05-04-round-6-aux-economy-ratifications.md) | Medium |
| 2026-05-04 | [Auxiliary economy structure + game modes ontology (Accepted; advanced from Proposed via Rounds 6–12) — Squadron-TD-inspired modular auxiliary structure + 6-mode roster + all 10 axes ratified](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) | Medium |
| 2026-05-04 | [Balance-pass #1 conceptual frame: 17-item ratification of tower-vs-unit math (variable nomenclature (a)–(r) + DPS×integral master equation + 7-slot round typology + (k) single-axis compounding + sell-refund + targeting + boss/Divinity sources + skill-bar axes)](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) | Medium |
| 2026-05-04 | [Aztec glyph: abstract placeholder pending cultural-sensitivity pass (closes Follow-up #4 from 2026-04-25 ratification)](decisions/2026-05-04-aztec-glyph-abstract-placeholder.md) | Easy |
| 2026-04-28 | [§5.4 [LOCKED] amendment: delete Lineages row, add Civilizations row (closes Follow-up #10; original convention archived to CASCADE-history.md)](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) | Easy |
| 2026-04-27 | [Commander-as-summoned-ability-avatar (+ Builder unit class + historic match-arc beats, solo-only); supersedes 2026-04-20 on-field-hero; same-day amendment captures 8-Q PM refinement (Aztec pre-contact; round-30 antagonists; mixed historicity; myth-mode counterfactual)](decisions/2026-04-27-commander-as-summoned-ability-avatar.md) | Medium |
| 2026-04-26 | [Prototype reshape plan (Step C, 6 steps + 2026-04-27 amendment adds C4 Cast-bar extension + new C7 step; **Accepted 2026-04-29**)](decisions/2026-04-26-prototype-reshape-plan.md) | Medium |
| 2026-04-26 | [Phase 1 exit one-pager (formal capture: World + Commander role + Hybrid topology + Why this frame wins + What remains open; closes 2026-04-25 Follow-up #11)](decisions/2026-04-26-phase-1-exit-one-pager.md) | Easy |
| 2026-04-26 | [Attack-type mapping: 7-type taxonomy + per-tower/demigod/god map + RPS armor matrix + status-proc table](decisions/2026-04-26-attack-type-mapping.md) | Medium |
| 2026-04-25 | [Q2 ratified: real-world cultures direction (Greek / Aztec / Norse) + launch-match design skeleton](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) — supersedes Q2 draft; partially supersedes 2026-04-24 reopen (thematic direction only; structural guardrails intact) | **Hard** |
| 2026-04-25 | [Q2 world pitch draft (synthetic mythic-history braid)](decisions/2026-04-25-q2-world-pitch-draft.md) — **Superseded by 2026-04-25 real-cultures ratification** | n/a (Proposed→Superseded) |
| 2026-04-24 | [Phase 1 vision reopen: synthetic mythic-history braid](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) — supersedes 2026-04-21 + 2026-04-22 Step B; **thematic direction partially superseded by 2026-04-25 real-cultures ratification** (structural guardrails intact) | **Hard** |
| 2026-04-21 | [Concept tightening: 3/3/3 shape + dungeon cosmology + Ash-enabler hybrids](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) — **Superseded by 2026-04-24** | **Hard** |
| 2026-04-19 | [Cascade restructure: consolidate to root, create stages/research/decisions dirs](decisions/2026-04-19-cascade-restructure.md) | Medium |
| 2026-04-19 | [Admin UI v1: single-file node-graph concept map](decisions/2026-04-19-admin-ui-v1.md) | Easy |
| 2026-04-19 | [Design prototype scope: throwaway HTML/JS permitted](decisions/2026-04-19-design-prototype-scope.md) | Easy |
| 2026-04-19 | [Tutorial glow affordance too subtle — log as design-debt](decisions/2026-04-19-tutorial-cell-affordance.md) | Easy |
| 2026-04-19 | [Intro-game baseline gaps escalated to concept-gaps pass](decisions/2026-04-19-intro-baseline-gaps.md) | Easy |
| 2026-04-19 | [Concept thinness load-bearing — pause workflow queue for concept-gaps pass](decisions/2026-04-19-concept-thinness-escalation.md) | Easy |
| 2026-04-20 | [Meta-UI envelope: settings menu + pause/meta-controls bundle (SETTINGS-01 + PAUSE-01)](decisions/2026-04-20-meta-ui-envelope.md) | Easy |
| 2026-04-20 | [Audio architecture: 5-bus mixer + ducking + focus-loss (AUDIO-01)](decisions/2026-04-20-audio-architecture.md) | Easy |
| 2026-04-20 | [Accessibility floor as Phase 2 constraint (A11Y-01..04 + SETTINGS-02)](decisions/2026-04-20-accessibility-floor.md) | Hard |
| 2026-04-20 | [Commander identity floor: Phase 4 §4.1 minimum spec (CMDR-01 + CMDR-02 + AUDIO-03)](decisions/2026-04-20-commander-identity-floor.md) | Medium |
| 2026-04-20 | [First-run flow: click budget + returning-player branch + skippable tutorial (FLOW-01 + FLOW-02 + ONBOARD-01)](decisions/2026-04-20-first-run-flow.md) | Easy |
| 2026-04-20 | [Save model: mode-aware save + always-persistent commander profile (SAVE-01 + SAVE-02)](decisions/2026-04-20-save-model.md) | Medium |
| 2026-04-20 | [Prototype `hybrid.pair` is ancestry tag only (PROGRESS 1.5c cleanup)](decisions/2026-04-20-prototype-hybrid-pair-shape.md) | Easy |
| 2026-04-20 | [Prototype pivots from throwaway to playable concept-demo (Step 10 unblocks Step 5 playtest)](decisions/2026-04-20-prototype-concept-demo-pivot.md) | Medium |
| 2026-04-20 | [Prototype debug-check sweep (pre-playtest) — 6 findings resolved](decisions/2026-04-20-prototype-debug-check-sweep.md) | Easy |
| 2026-04-20 | [Prototype interaction layer — hover / right-click / sell / upgrade [PROPOSAL] / reference panel](decisions/2026-04-20-prototype-interaction-layer.md) | Medium |
| 2026-04-20 | [Prototype visuals overhaul + insight layer (silhouettes / hex+glyph / projectiles / damage numbers / status icons / threat bar / next-wave telegraph / combat feed)](decisions/2026-04-20-visuals-insight-pass.md) | Medium |
| 2026-04-20 | [Doc-cascade split: CONCEPT.md → hub + concept/phase-1..7.md (+ cascade-lint size cap and concept/ integrity checks)](decisions/2026-04-20-doc-cascade-split.md) | Easy |
| 2026-04-20 | [Meta-UI shell polish (splash glyphs / login branch / menu branch / mode-aware pause)](decisions/2026-04-20-meta-ui-shell-polish.md) | Easy |
| 2026-04-20 | [Profile panel layer — dedicated Profile scene + mode-gated writeMatchSave](decisions/2026-04-20-profile-panel-layer.md) | Easy |
| 2026-04-20 | [Options 5 tabs real — audio sliders + rebind + video/a11y/gameplay persisted](decisions/2026-04-20-options-five-tabs-real.md) | Easy |
| 2026-04-20 | [Commander-pick identity upgrade — SVG silhouettes + XP ladder + cosmetic locks + silhouette-test](decisions/2026-04-20-commander-pick-identity-upgrade.md) | Easy |
| 2026-04-20 | [First-run discoverability prompts (right-click / I-key / hover) with permanent dismiss](decisions/2026-04-20-first-run-discoverability.md) | Easy |
| 2026-04-20 | [Age-as-history flavor banner + mapmods.json data + Campaign age-gate autosave + auto-age-up toggle](decisions/2026-04-20-age-history-flavor-mapmods.md) | Medium |
| 2026-04-20 | [Spontaneity random events (events.json, 25% seeded LCG, weighted pool, additive co-op broadcast)](decisions/2026-04-20-spontaneity-random-events.md) | Easy |
| 2026-04-20 | [Commander-on-field hero — avatar + 2-cell aura + Shift-click move + Q signature + additive snapshot](decisions/2026-04-20-commander-on-field-hero.md) — **Superseded by 2026-04-27** | Medium |
| 2026-04-22 | [Step B: Prototype reshape plan — 3/3/3 cascade into prototype data + scenes + lint + docs](decisions/2026-04-22-step-b-prototype-reshape-plan.md) — **Superseded by 2026-04-24** (target shape reopened; 18 sub-steps void) | Medium |

---

## Admin UI — visual concept map

- [`admin/index.html`](admin/index.html) — single-file node-graph editor. Drag/drop, edit in sidebar, per-node comments.
- [`admin/concept.json`](admin/concept.json) — canonical editable state. Seeded from `CONCEPT.md`. Read to pick up PM visual edits.
- [`admin/README.md`](admin/README.md) — usage.
- [Decision entry](decisions/2026-04-19-admin-ui-v1.md).

**Conflict rule:** MD docs win on naming conventions; JSON wins on roster/ages/hybrids/positions/comments.

---

## Prototype — clickable design slice

- [`prototype/index.html`](prototype/index.html) — single-file prototype, data-driven over HTTP.
- [`prototype/data/*.json`](prototype/data/) — BALANCE, towers, commanders as JSON. Seed for future Godot Resources.
- [`prototype/start.bat`](prototype/start.bat) — Python `http.server` on :8765 + auto-open (data-driven mode).
- [`prototype/README.md`](prototype/README.md) — run instructions.
- [`prototype/PORT-NOTES.md`](prototype/PORT-NOTES.md) — JS→Godot idiom notes.
- [Decision entry](decisions/2026-04-19-design-prototype-scope.md).

---

## Legacy / archive

- `tw-commanders-starter/` — original starter scaffold; content was duplicated into root 2026-04-19. **Do not edit.** See `tw-commanders-starter/ARCHIVED.md`.

---

## When to update this doc

- Stage / research status changes (Stub → Draft → In review → Locked).
- New stage / research / decision file added.
- Current work pointer shifts.
- Doc renamed, moved, archived.

Treat `CASCADE.md` as single source of truth for "what exists and where." If it disagrees with the filesystem, fix one or the other — never let them drift.

---

*Document version: 0.37 — 2026-05-04 (end-of-day): 12-round conceptual ratification COMPLETE. Balance-pass #1 frame (Rounds 1-5) + auxiliary economy + 6-mode ontology + frame extension (Rounds 6-12) all locked across 7 new decision documents. Mode count expanded 5 → 6 (Horde split). Frame items #3 (master equation extended with variable (s)) and #12 (lives per-mode declarable) amended via dated decision entries. CONCEPT-GAPS rows ECON-04 + MODE-01 advanced to RESOLVED. "Go big, no scope cuts" project doctrine ratified. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched. Numbers-phase Follow-up #13 fully unblocked. Prior: 0.36 — 2026-05-04 (mid-session, archived to history): Balance-pass frame Accepted + auxiliary-economy Proposed at that point. [Older version history archived to [`CASCADE-history.md`](CASCADE-history.md).]*
