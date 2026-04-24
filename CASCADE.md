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

**2026-04-21 — Concept tightening (3/3/3 + dungeon cosmology + Ash-enabler hybrids) docs pass LANDED + post-Step-A residual-drift cleanup LANDED.** PM-locked pivot ratified and cascaded across the concept tree in a docs-only pass. Step A (12 sub-steps, one file per turn): A1 filed [decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility Hard, 3x debug loop inline). A2–A5 cascaded `concept/phase-1.md §1.1`, `concept/phase-3.md §3.2/§3.3/§3.5/§3.8`, `concept/phase-4.md §4.1/§4.2/§4.3/§4.6`, `concept/phase-5.md §5.1/§5.3` — `§5.4 [LOCKED]` untouched. A6 amended `CONCEPT.md` hub + `README.md` critical-context #3. A7 stub-amended `stages/01,05,06` upstream-constraints. A8 audited `CONCEPT-GAPS.md` remaining 11 rows — zero retirements, all shape-independent. Three 2026-04-20 decisions (`commander-identity-floor`, `age-history-flavor-mapmods`, `commander-pick-identity-upgrade`) are **rebased** (not superseded). Names `Ash / Nature / Prayer / Dust / Form / Apotheosis` are prose placeholders pending a deferred naming pass. **Step B (prototype reshape) and Step C (Step 5 playtest) are downstream — NOT this session.** CONCEPT.md v0.6 → v0.7. CASCADE doc version v0.13 → v0.15.

*Post-Step-A residual-drift cleanup (8 commits, one file per turn):* `concept/phase-6.md` §6.1/§6.2/§6.3/§6.4 (tier-persistence + MVP=full roster + Post-hybrid-families milestone), `concept/phase-7.md` §7.1/§7.3/§7.4 (roster question closed at 3, Veil/Crown questions retired, Ascendant→Apotheosis), `concept/phase-3.md` §3.1/§3.4/§3.6 (Age Gate→Tier Gate, ages→tiers, Sinew/Veil refs removed), `concept/phase-4.md` §4.5 (Veil tar-pit genericized) + §4.7 (enemy direction rescoped OPEN under dungeon cosmology), `concept/phase-5.md` §5.2 (build phases rewritten for 3/3/3), `concept/phase-1.md` §1.3 (Tier persistence), `stages/05-age-evolution.md` upstream-deps link label. Post-cleanup verification: stale-lineage + ages/counts sweeps re-run, all remaining hits intentional (§5.4 [LOCKED] examples, amendment notes, historical rebase-context, retirement citations, preserved-for-traceability stage-01 body). `cascade-lint` clean throughout.

**2026-04-24 (later same day) — Phase 1 vision reopen FILED and cascading.** Reopen decision [`decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md`](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) filed (Reversibility **Hard**, 3x debug loop inline, amended once to correct supersede accounting). Thematic direction: **synthetic mythic-history braid** (history + comparative religion + mythology + philosophy braided into one invented world). Mechanics (TD/merge/debuff/magic) preserved. §2.4a + §5.4 [LOCKED] untouched. Age model deferred until world/story/background land. **Supersede cascade this pass:** [`decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md`](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) Status flipped Accepted → Superseded; [`decisions/2026-04-22-step-b-prototype-reshape-plan.md`](decisions/2026-04-22-step-b-prototype-reshape-plan.md) Status flipped Proposed → Superseded (18-sub-step 3/3/3 migration void). **Step A cascade §-edits preserved in-tree as superseded-record — NOT force-reverted.** Three 2026-04-20 decisions rebased by 2026-04-21 (commander-identity-floor / age-history-flavor-mapmods / commander-pick-identity-upgrade) are un-rebased; their rebase banners now point at a Superseded parent; reconciliation deferred to Phase 1 exit (tracked in reopen Follow-ups #7). Prototype stays frozen against concept edits until Phase 1 exits. Next: Q2 — world pitch, Socratic Q2–Q10 one per turn PM-driven. Phase 1 exit rubric: one-page answer to *what the world is / Commander's role / hybrid topology meaning*. CASCADE doc version v0.18 → v0.19.

**2026-04-24 (earlier same day) — Phase 1 vision reopen ratified by PM (no doc edits in that session).** Bootstrap + concept discussion. PM confirmed full concept rehaul: supersedes 2026-04-21. Thematic direction captured as "synthetic mythic-history braid." HANDOFF + PROGRESS updated in that commit to queue the reopen decision for the next session. That queue is the one being executed above. CASCADE doc version v0.17 → v0.18 at that time.

**2026-04-22 — follow-up drift-sweep + rebase bookkeeping + Step B plan filed (Proposed).** Earlier 2026-04-22: two residuals the 2026-04-21 sweep missed, caught and resolved — `concept/phase-2.md §2.3` risks rewritten to 3-lineage / tiers shape (commit `5c8aaa6`), and `stages/04-in-match-core.md` gained an A7-style amendment banner (commit `f99fd14`, deferred from A7 scope). Downstream cascade from the already-ratified 2026-04-21 entry; no new upstream decision. Both landed to `main` via fast-forward. `cascade-lint` clean.

*Later 2026-04-22 (session `claude/resume-ash-to-altar-ghwri`, five commits one file per turn, all fast-forwarded to main):* (1) CASCADE doc-version v0.15 → v0.16 bookkeeping for the 2026-04-22 pointer-append (`90a8588`). (2) Three rebase banners filed inline on the 2026-04-20 decisions rebased under 2026-04-21 concept tightening — [`commander-identity-floor`](decisions/2026-04-20-commander-identity-floor.md) (`8b18e6f`), [`age-history-flavor-mapmods`](decisions/2026-04-20-age-history-flavor-mapmods.md) (`f6a5220`), [`commander-pick-identity-upgrade`](decisions/2026-04-20-commander-pick-identity-upgrade.md) (`5ca6c06`). Banner pattern: rebase delta called out per decision; Accepted status preserved; identity-floor / banner-mechanic / silhouette-test surfaces survive intact. (3) [`decisions/2026-04-22-step-b-prototype-reshape-plan.md`](decisions/2026-04-22-step-b-prototype-reshape-plan.md) filed **Proposed** (Reversibility Medium, 3x debug loop inline) — 18-sub-step plan covering data migration (7 JSON files), lint relax/retighten, 4 index.html passes, 4 prototype docs, PROGRESS/HANDOFF close (`fbc01f0`). CASCADE decisions table row added. **Step B execution NOT started — awaiting PM "go".** Freeze gate: 2026-05-15.

**2026-04-20 — Meta-UI concept-fidelity + TW/HoMM/AoE/SC-WC3 DNA-injection pass LANDED.** Nine strands executed in a single autonomous window: (1) shell polish + mode-aware pause, (2) profile panel + mode-gated save, (3) Options 5 tabs real, (4) commander-pick SVG silhouettes + XP ladder + silhouette-test, (5) first-run prompts, (6) verification + click-budget audit, (7) commander-as-hero on-field with 2-cell aura / Shift-click move / Q signature, (8) age-history flavor banners + mapmods.json + Campaign age-gate autosave, (9) spontaneity random events (events.json, LCG seeded for co-op determinism). See the 9 new 2026-04-20 decision entries in the decisions table below. Step 5 playtest remains the downstream gate; freeze 2026-05-15. CASCADE doc version v0.11 → v0.12.

**2026-04-20 — Step 10 (concept-demo pivot) + pre-playtest debug sweep LANDED. Step 10 in a prior autonomous pass (four phases: data expansion → scene rebuild → PeerJS co-op → polish). Pre-playtest debug-check sweep this pass (6 findings: `</h3>` typo, guest-side cell.occupied reconciliation, broker-SLA doc note, 11-age inline fallback, cascade-lint `[~skip]` awareness, guest tower-flash one-frame skip). See [`decisions/2026-04-20-prototype-concept-demo-pivot.md`](decisions/2026-04-20-prototype-concept-demo-pivot.md) + [`decisions/2026-04-20-prototype-debug-check-sweep.md`](decisions/2026-04-20-prototype-debug-check-sweep.md). Concept-demo freeze date: 2026-05-15. Prototype is **playtest-ready**. Next: Step 5 — PM playtest with a friend → findings as dated decisions. 16 of 26 CONCEPT-GAPS rows migrated, 11 remain.**

2026-04-20 batch pass (PM-overridden cadence): filed five decision entries covering SETTINGS-01+PAUSE-01, AUDIO-01, A11Y-01..04+SETTINGS-02, CMDR-01+CMDR-02+AUDIO-03, FLOW-01+FLOW-02+ONBOARD-01. Each includes a 3x debug loop inline. CONCEPT.md amended across §2.4a (Phase 2 reopen — accessibility floor), §3.2 (identity cross-link), §3.9 (meta-UI envelope), §3.10 (audio architecture), §3.11 (first-run flow), §4.1 (commander identity floor [PROPOSAL]), §5.1 (MVP commanders honor floor), §6.4 (commander re-pick metric promoted). CONCEPT.md doc version bumped 0.3 → 0.4. CONCEPT-GAPS doc version bumped 0.1 → 0.2 with migration tracker at top.

**Next planned work (PM-gated):**
1. PM reviews the five filed decision entries + CONCEPT.md amendments; supersedes any that miss the mark.
2. PM picks direction on the remaining 13 CONCEPT-GAPS rows (ratify more, accept deferred, or reorder).
3. Workflow queue (`PROGRESS.md` Step 1.5b onward) resumes per resumption criteria in [`decisions/2026-04-19-concept-thinness-escalation.md`](decisions/2026-04-19-concept-thinness-escalation.md) once ratification pass is closed.

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
| 2026-04-24 | [Phase 1 vision reopen: synthetic mythic-history braid](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) — supersedes 2026-04-21 + 2026-04-22 Step B | **Hard** |
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
| 2026-04-20 | [Commander-on-field hero — avatar + 2-cell aura + Shift-click move + Q signature + additive snapshot](decisions/2026-04-20-commander-on-field-hero.md) | Medium |
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

*Document version: 0.19 — 2026-04-24 (later same day): Phase 1 vision reopen FILED as [`decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md`](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) (Reversibility **Hard**, 3x debug loop inline). Supersede cascade: 2026-04-21 concept tightening Status flipped Accepted → Superseded; 2026-04-22 Step B plan Status flipped Proposed → Superseded. Step A cascade §-edits preserved in-tree as superseded-record. Three 2026-04-20 decisions rebased by 2026-04-21 are un-rebased; reconciliation deferred to Phase 1 exit. Prototype frozen. Next: Q2 world pitch, Socratic Q2–Q10 one per turn PM-driven. Prior: 0.18 — 2026-04-24 (earlier same day): Phase 1 vision reopen ratified by PM. Full rehaul direction captured; no doc edits in that session. Pointer updated; HANDOFF + PROGRESS updated. Prior: 0.17 — 2026-04-22 later-same-day: rebase banners on 3 rebased 2026-04-20 decisions, Step B prototype-reshape plan filed as Proposed (`decisions/2026-04-22-step-b-prototype-reshape-plan.md`, 18 sub-steps, Reversibility Medium). Pointer section updated with later-2026-04-22 block; new decisions-table row added. Step B execution NOT started — awaiting PM "go". Prior: v0.16 — 2026-04-22 follow-up drift-sweep bookkeeping. Pointer appended 2026-04-22 (commit `cd5af55`) capturing `concept/phase-2.md §2.3` rewrite (`5c8aaa6`) + `stages/04-in-match-core.md` A7 banner (`f99fd14`); the pointer-append itself was not version-bumped at the time. This bump records the addendum without content change. Prior: v0.15 — 2026-04-21 post-Step-A residual-drift cleanup LANDED. 8 cleanup commits one file per turn — `concept/phase-1.md §1.3`, `concept/phase-3.md §3.1/§3.4/§3.6`, `concept/phase-4.md §4.5/§4.7`, `concept/phase-5.md §5.2`, `concept/phase-6.md §6.1-§6.4`, `concept/phase-7.md §7.1/§7.3/§7.4`, `stages/05-age-evolution.md` link label. Stale-lineage + ages/counts sweeps re-run; all remaining hits are intentional (§5.4 [LOCKED], amendment notes, historical rebase-context, retirement citations, preserved-for-traceability). HANDOFF + PROGRESS refreshed. Prior: v0.14 — 2026-04-21 concept-tightening docs pass LANDED. Pivot cascaded across CONCEPT hub + 4 phase files + README + 3 stage stubs + CONCEPT-GAPS audit. [2026-04-21 concept-tightening decision](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility **Hard**) added to decisions table. Three 2026-04-20 decisions rebased (not superseded): commander-identity-floor, age-history-flavor-mapmods, commander-pick-identity-upgrade. `concept/phase-5.md §5.4 [LOCKED]` untouched. Step B (prototype reshape) + Step C (playtest) remain downstream. Prior: v0.13 — 2026-04-20 handoff: **Meta-UI concept-fidelity + TW/HoMM/AoE/SC-WC3 DNA-injection pass LANDED** — 9 strands in one autonomous window (shell polish, profile layer, Options 5 real, commander-pick SVG identity, first-run prompts, verification, commander-on-field hero, age-history flavor + mapmods, spontaneity events). 7 new decision entries filed 2026-04-20. Next session: **Step 5 playtest** with PM + friend. Prior: v0.12 — 2026-04-20 handoff: next-session agenda set to **Meta-UI concept-fidelity pass** (splash/login/menu polish + profile/availability layer + Options 5-tab make-real + commander-pick identity-floor upgrade + first-run prompt surface). All research rails already filed; pass executes against existing decisions (first-run-flow / meta-UI-envelope / accessibility-floor / commander-identity-floor / audio-architecture / save-model / stages-00 / stages-01). Pointer: concept-fidelity pass is forecasted for next autonomous window; Step 5 playtest remains the downstream gate. Prior: v0.11 — 2026-04-20 visuals+insight pass + doc-cascade split. Prototype now ships silhouettes/hex+glyph/projectile shapes + damage-numbers/status-icons/threat-bar/next-wave-telegraph/combat-feed (see [visuals-insight decision](decisions/2026-04-20-visuals-insight-pass.md)). CONCEPT.md restructured into hub + [concept/phase-1..7.md](concept/) (see [doc-cascade split decision](decisions/2026-04-20-doc-cascade-split.md)). `cascade-lint` extended with 600-line soft cap, `concept/` folder integrity check, and stale §-anchor warning. Pointer unchanged — still Step 5 playtest-gate.*
