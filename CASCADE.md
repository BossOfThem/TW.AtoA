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

**2026-05-03 — C6 slice 2 LANDED (graduation cut: legacy 5-lineage / 11-age teardown).** Closes the multi-slice C6 + C4-continuation arc started 2026-05-02. Three sub-slices ran across this session: Slice A (commander-legacy sweep, commit `1b4fd38`, prior session); Slice B (civ-tower placement bridge + tutorial reshape, prior session bridge commits); Slice C (graduation cut, commit `2893943`, this session). Slice C dual-pushed to session branch + main. **Deleted from `prototype/index.html` (699 deletions / 131 insertions):** `AGES` global + `KNOWLEDGE_PER_AGE` balance + `baseKnowledge` derivation; collapsed age-indexed damage/cd arrays to scalars; `game.ageIdx` from initMatch/initTutorial state, snapshot.enemies, `effectiveTowerStats`, tick spawn, `archetypeFor` callers, render fallbacks, `endMatch`, `towerTipHTML`, `placementTipHTML`; stale `selectTower("sinew")`; `BALANCE.TOWERS.sinew/ember` refs in `logBalanceCurve`; `"hybrid"` feed-kind branch in `emitFeed`. **HTML/CSS:** orphan `<div id="age-banner">`; `#age-banner` block + `ageBannerIn` keyframes; `.row.hybrid` rule; `.hud .age-label` rule. **Data:** `prototype/data/ages.json` + `prototype/data/towers.json` deleted (no JS fetchers; civilizations.json + tiers.json + balance.json canonical). **Lint:** `tools/cascade-lint.py` schema rows + 11-row cross-file check dropped. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched; 2026-04-25 locked content-skeleton names untouched. **Outcome:** prototype runs on civ-tower + 4-tier ladder shape only; legacy 5-lineage / 11-age surfaces fully retired. Aztec glyph follow-up #4 still deferred.

*Prior pointer block archived to [`CASCADE-history.md`](CASCADE-history.md).*

**Next planned work:**
1. **C4-continuation deferred items** — merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp polish (the civ-tower placement UI surfaces still owed; PM gate required).
2. **Follow-up #4 — Aztec glyph styling pass.** civilizations.json has `𓁹` (Egyptian eye) for Aztec — wrong civilization. Independent track.
3. **Follow-up #13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts).
4. **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
5. Cultural-sensitivity pass scheduling (Follow-up #5).
6. Patch-1 commanders per civ (Follow-up #6).
7. `admin/concept.json` migration path.
8. Other follow-ups #7 / #8 / #9.

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

*Document version: 0.34 — 2026-05-03: C6 slice 2 LANDED (graduation cut: legacy 5-lineage / 11-age teardown). Closes the multi-slice C6 + C4-continuation arc. Slice C commit `2893943` dual-pushed. 699 deletions / 131 insertions across prototype/index.html + tools/cascade-lint.py + prototype/data/{ages,towers}.json deleted. AGES global / KNOWLEDGE_PER_AGE / game.ageIdx / lineage projectile shapes / lineageOf/lineageRole / HYBRIDS map / age-up + Knowledge UI / age-banner / hybrid feed branch / 5-lineage CSS rules and tokens — all retired. Prototype now runs on civ-tower + 4-tier ladder only. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched. Aztec glyph Follow-up #4 deferred. Prior: 0.33 — 2026-05-02: C6 slice 1 LANDED (commander-legacy sweep). [Older version history archived to [`CASCADE-history.md`](CASCADE-history.md).]*
