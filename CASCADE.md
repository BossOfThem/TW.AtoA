# CASCADE — navigation spine for Ash to Altar

The canonical index. Every doc links from here in the order a new reader (human or Claude) should encounter it. If you are a new session: **`README.md` → `CLAUDE.md` → this file → target doc.** Do not hunt.

Non-negotiables + naming conventions + cascade discipline live in [`README.md`](README.md) + [`CLAUDE.md`](CLAUDE.md); this doc is pure navigation.

---

## How the doc tree works

The project uses a waterfall cascade (see [`CONCEPT.md`](CONCEPT.md) Phases 1–7). It shows up in three places:

1. **Conceptual cascade** — Phases 1–7 in `CONCEPT.md`. Discovery → Analysis → Design → Specification → Implementation → Validation → Iteration. Phase N+1 does not silently edit Phase N.
2. **Player-journey cascade** — [`stages/`](stages/) dir. One doc per player-experience stage.
3. **Research cascade** — [`research/`](research/) dir. Deep-dive market evidence feeding stage decisions.

Cross-link convention:
- Stage-to-stage: `[stage 03 — match setup](stages/03-match-setup.md#section)`
- Decisions: `[2026-04-20 <slug>](decisions/2026-04-20-<slug>.md)`
- Concept anchors: `[CONCEPT §3.3](CONCEPT.md#33-...)`

Stages + research tables (status, last-reviewed) live in [`CASCADE-tables.md`](CASCADE-tables.md) — load on demand when working on those surfaces.

---

## Reading order (new session)

1. [`README.md`](README.md) — status, non-negotiables, critical context.
2. [`CLAUDE.md`](CLAUDE.md) — session conventions, cadence, 3x debug loop.
3. [`HANDOFF.md`](HANDOFF.md) — last-session checkpoint.
4. This file — the map.
5. [`PROGRESS.md`](PROGRESS.md) — step tracker; first unchecked box = next step (unless queue paused).
6. [`CONCEPT.md`](CONCEPT.md) — vision hub. Phase content lives under [`concept/phase-1..7.md`](concept/); open only what you need.
7. [`CONCEPT-GAPS.md`](CONCEPT-GAPS.md) — ephemeral proposal layer.
8. Target stage / research / decision doc per "Current work pointer" below.

---

## Current work pointer

**2026-05-06 — Economy paper-balance ratification LANDED (§4.8 exit-gate item #7 ✅ DONE).** Single-doc audit-and-ratify; no per-property arc needed because every Economy magnitude was already locked at Numbers-phase #13 R1-R10 (2026-05-05). 3-check cross-coherence audit at zero cascade-violations: (Check 1) Tribute spend-vs-income at Easy-on-curve — ~25,000 T cumulative kill yield / ~10,700 T on-curve placement / ~1,900 T aux+cycling typical / **~12,400 T headroom** preserved; sell-refund schedule keeps cycling viable at every tier. (Check 2) Divinity spend-vs-income across three envelopes — realistic-Easy 4 Div fits 4-cap (2 menu + 1 Fusion + 1 Damage Bonus); realistic-expert 5-6 Div fits 6-cap (2 menu + 3 Fusions + 1 aux); theoretical-ceiling 8 Div clamps to 6 with wastage-past-cap UI indicator per R10 lock. Sources 5+6 skill-bar-gated per Round 9 thresholds (novice stacks cannot accidentally reach ceiling). PvP per-side awarding preserves symmetry. (Check 3) §4.11.8 Hardcore-expert realized math = 0.576 × 1.20 (s) × 1.15 (h) × 1.25 (matchup) = **0.993 ≈ 1.0** — closes margin exactly per R9 anchor; multiplicative composition per §4.10.2 master damage equation, no double-counting. Easy / Hard envelopes carry positive headroom by R2 (k)-curve construction. **Spine-doc edits**: §4.8 exit-gate item #7 ✅ ticked DONE; §4.6 "Open" carry-list left as-flagged (downstream artifacts, not Economy debt — late-game Tribute sinks → per-mode authoring, status-proc tiers → per-tower authoring, "Divinity" naming → Follow-up #5 Phase-4-exit). Phase 4 advances to **6 of 11 exit-gate items closed** (#1 commander / #2 per-tower / #3 per-civ / #4 enemy direction / #5 mobile unit control / **#7 economy paper-balance**). 5 items remaining (#6 Fusion-numerics / #8 Monetization / #9 Engine lock / #10 Art director / #11 Cultural-sensitivity Phase-4-exit). Skipping #6 intentional and explicit — Economy ratifies Divinity *spend cadence* into Fusion (locks 2 menu + 1/Fusion fits 6-cap) but per-God magnitudes are separate sub-pass; §4.8 items are independent. Hard guards verified untouched verbatim. PM autonomy mandate carries. ([`decisions/2026-05-06-economy-paper-balance-ratification.md`](decisions/2026-05-06-economy-paper-balance-ratification.md))

**Carried blockers / debt:** `49c4c54` `.accord/` 69MB blob in history (purge needs explicit PM authorization) · cultural-sensitivity Follow-up #5 (scheduled at Phase-4 exit, not currently blocking).

*Older pointers archived to [`CASCADE-history.md`](CASCADE-history.md).*

**Next planned work (Phase-4 exit):** Fusion-numerics balance-pass · Economy paper-balance ratification · Monetization specifics resolution · Engine choice lock (Godot 4 leading) · Art director engagement · Cultural-sensitivity Follow-up #5 consultation (locked to last exit-gate item) · Phase 5 readiness gate (telemetry + wave variance).

---

## Decisions — dated log

Every concept-constraint change + every ratified gap-resolution lives here. Format: [`TEMPLATE.md`](decisions/TEMPLATE.md). One-line hooks only — open the linked file for full content.

| Date | Decision | Reversibility |
|------|----------|---------------|
| 2026-05-06 | [Economy paper-balance ratification (§4.8 item #7 DONE; 3-check cross-coherence audit zero cascade-violations; Phase 4 6/11 exit-gate items closed)](decisions/2026-05-06-economy-paper-balance-ratification.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control RN — cross-arc audit + spine-doc edits + arc close (CLOSES ARC 4/4; 12-cell 3-axis audit zero cascade-violations; §4.8 item #5 DONE; Phase 4 5/11 exit-gate items closed)](decisions/2026-05-06-mobile-unit-control-rn-cross-arc-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R3 — spec-grammar authoring (speed ladder T1-T4 / pathing-mode catalog / engagement-rule catalog with per-tier §3.4 falsification / aggro tie-breaker resolution stable-sort + no-override)](decisions/2026-05-06-mobile-unit-control-r3-spec-grammars.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R2 — control-model direction lock (Option (i) waypoint + mode-flags ratified; 4-flag catalog + 3-default engagement shape + no-tier-scaling principle; civ-neutral mechanical-content)](decisions/2026-05-06-mobile-unit-control-r2-direction-lock.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R1 scope (4-round per-property axis; control-model lock + spec-grammars + RN audit; spec-level grain only)](decisions/2026-05-06-mobile-unit-control-r1-scope.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction RN — cross-arc audit + spine-doc edits + arc close (CLOSES ARC 4/4; 42-cell 3-axis audit zero cascade-violations; §4.8 item #4 DONE)](decisions/2026-05-06-enemy-direction-rn-cross-arc-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction R3 — R11 wave-composition variance grammar (5 spec-level bindings; (k) band-center + matchup-affinity overlay + diversity envelope)](decisions/2026-05-06-enemy-direction-r3-r11-variance-grammar.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction R2 — Option C ratified (civ-matched bosses + shared regular-wave pool; 5-class distribution bands)](decisions/2026-05-06-enemy-direction-r2-direction-lock.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction + R11 wave-variance R1 scope (4-round per-property axis; R11 bundled)](decisions/2026-05-06-enemy-direction-r1-scope.md) | Medium |
| 2026-05-06 | [Post-per-civ-arc ratifications (next-track §4.7+R11 / admin.json retired / phase-4 cap 600→700 / cultural-sensitivity at Phase-4 exit)](decisions/2026-05-06-post-arc-ratifications.md) | Mixed |
| 2026-05-06 | [Per-civ RN — cross-civ × cross-field audit + arc close (CLOSES ARC 4/4; 15/15 zero cascade-violations; 3-civ-3-equation-form fingerprint locked)](decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [Per-civ R4 — Norse profile (5 fields + identity_hook 3x debug + R3-prediction validated + → RN hook)](decisions/2026-05-06-per-civ-r4-norse-profile.md) | Medium |
| 2026-05-06 | [Per-civ R3 — Aztec profile (5 fields + identity_hook 3x debug + R2-prediction reconciliation + → R4 hook)](decisions/2026-05-06-per-civ-r3-aztec-profile.md) | Medium |
| 2026-05-06 | [Per-civ R2 — Greek profile (5 fields + identity_hook 3x debug + → R3 hook)](decisions/2026-05-06-per-civ-r2-greek-profile.md) | Medium |
| 2026-05-06 | [Per-civ specialization sub-pass scope (4-round queue + 5-field schema + Axis A)](decisions/2026-05-06-per-civ-specialization-scope.md) | Medium |
| 2026-05-06 | [Per-tower RN — cross-civ × cross-tier audit + arc close (45/45 zero cascade-violations; 3 orthogonal civ-magnitude axes confirmed)](decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [Per-tower R4 — Norse roster (15 towers × 7 fields; cd-1.15s fastest / range-3.5 shortest / Bleed-density 6-of-15)](decisions/2026-05-06-per-tower-r4-norse-roster.md) | Medium |
| 2026-05-06 | [Per-tower R3 — Aztec roster (15 towers × 7 fields; band-high T2-T3 / cd-1.4s / Poison-Fire-Slashing bleed)](decisions/2026-05-06-per-tower-r3-aztec-roster.md) | Medium |
| 2026-05-06 | [Per-tower R2 — Greek roster (15 towers × 7 fields; cd-1.7s / range-4.0 / Divine-density 4-of-15)](decisions/2026-05-06-per-tower-r2-greek-roster.md) | Medium |
| 2026-05-06 | [Per-tower authoring sub-pass scope (4-round queue + 7-field schema + Axis A)](decisions/2026-05-06-per-tower-authoring-scope.md) | Medium |
| 2026-05-05 | [Per-commander R5 — audit + arc close (Aztec breakpoint Lever-2 applied; aura-anchor resolved; 3 one-pagers; spine-doc edits)](decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md) | Medium |
| 2026-05-05 | [Per-commander R4 — signature variants (Last Stand / Great Sacrifice / Great Heathen Army; once-per-match free)](decisions/2026-05-05-per-commander-r4-signature-variants.md) | Medium |
| 2026-05-05 | [Per-commander R3 — short-CD active variants (This Is Sparta! / Sun Offering / Berserk; 30s base CD)](decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md) | Medium |
| 2026-05-05 | [Per-commander R2 — passive variants (Spartan Training / Blood Tribute / Sons of Ragnar; +15% benchmark)](decisions/2026-05-05-per-commander-r2-passive-variants.md) | Medium |
| 2026-05-05 | [Per-commander effect-type-variant authoring scope (5-round queue + per-ability-slot axis)](decisions/2026-05-05-per-commander-effect-type-variant-authoring-scope.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R7 — hub close (CLOSES ARC 7/7; Non-negotiables "Go big at launch" promoted; footer 0.8→0.9)](decisions/2026-05-05-concept-amendment-pass-round-7-hub-close.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass R6 — phase-4 §4.7 wave-variance R11 + phase-6 §6.5 telemetry + phase-7 §7.4 "Go big"](decisions/2026-05-05-concept-amendment-pass-round-6-phase-4-7-r11-and-phase-6-7.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass R5 — phase-4 §4.6 Economy rewrite + §4.6a Auxiliary economy NEW (7-slot catalog)](decisions/2026-05-05-concept-amendment-pass-round-5-phase-4-economy.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R4 — phase-4 §4.11 Numbers floor body populated (8 sub-sections)](decisions/2026-05-05-concept-amendment-pass-round-4-phase-4-numbers-floor.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R3 — phase-4 §4.10 Tower-vs-Unit math NEW (variable nomenclature (a)-(s))](decisions/2026-05-05-concept-amendment-pass-round-3-phase-4-tower-vs-unit-math.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R2 — phase-3 §3.6 mode roster 5→6 + per-mode summary table](decisions/2026-05-05-concept-amendment-pass-round-2-phase-3-modes.md) | Easy |
| 2026-05-05 | [CONCEPT.md amendment pass scope (7-round queue + §-placement table)](decisions/2026-05-05-concept-amendment-pass-scope.md) | Easy |
| 2026-05-05 | [Balance-pass #2 R10 — Divinity source escalation (CLOSES arc; 4-Div floor + Sources 5/6)](decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R9 — Skill-bar thresholds per (k); Hardcore expert closes margin exactly](decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R8 — Per-mode tuning + N-scaling + PvP tie-break (R31+ HP×1.5; R45 co-victory)](decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R7 — Aux-slot costs + (s) ranges](decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R6 — Commander (h) ability magnitudes (passive +15% / active 4× T3 / signature free tier-up)](decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R5 — Tower DPS ladder T1=1×/T2=3×/T3=9×/T4=27×/God=54× + tier-up costs](decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R4 — Speed (f) + per-map (j); f_base=50 u/s + archetype multipliers](decisions/2026-05-05-balance-pass-2-round-4-map-speed.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R3 — Tribute economy (a); yield(R)=5·1.10^R + boss lumps](decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R2 — (k) compounding exponents; Easy 1.16 / Hard 1.19 / Hardcore 1.22](decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R1 — Runner HP curve (e); HP_std(R)=100·1.16^R Easy + boss spikes](decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md) | Medium |
| 2026-05-04 | [Round 12 — Aux UX + frame variable (s) + per-mode (k) + maze validity](decisions/2026-05-04-round-12-aux-ux-frame-extension.md) | Medium |
| 2026-05-04 | [Round 11 — PvP Maze Lane deep-dive (hex-grid, A*, Send-Through-Maze, lives=10)](decisions/2026-05-04-round-11-pvp-maze-deep-dive.md) | Medium |
| 2026-05-04 | [Round 10 — PvE Multiplayer deep-dive (N parallel lanes, last-alive)](decisions/2026-05-04-round-10-pve-mp-deep-dive.md) | Medium |
| 2026-05-04 | [Round 9 — PvP Interest Wars deep-dive + lives extension (20s rounds, 30-leak knockout)](decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md) | Medium |
| 2026-05-04 | [Round 8 — Horde Co-op deep-dive + co-op mode split (Horde-A + Horde-B)](decisions/2026-05-04-round-8-horde-coop-deep-dive.md) | Medium |
| 2026-05-04 | [Round 7 — Solo Campaign deep-dive (multi-mission saga, single-lane)](decisions/2026-05-04-round-7-solo-campaign-deep-dive.md) | Medium |
| 2026-05-04 | [Round 6 — Aux economy ratifications + "Go big, no scope cuts" doctrine](decisions/2026-05-04-round-6-aux-economy-ratifications.md) | Medium |
| 2026-05-04 | [Auxiliary economy structure + game modes ontology (Accepted; advanced from Proposed via R6-R12)](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) | Medium |
| 2026-05-04 | [Balance-pass #1 conceptual frame (17-item ratification of tower-vs-unit math)](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) | Medium |
| 2026-05-04 | [Aztec glyph: abstract placeholder pending cultural-sensitivity pass (closes Follow-up #4)](decisions/2026-05-04-aztec-glyph-abstract-placeholder.md) | Easy |
| 2026-04-28 | [§5.4 [LOCKED] amendment: delete Lineages row, add Civilizations row (closes Follow-up #10)](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) | Easy |
| 2026-04-27 | [Commander-as-summoned-ability-avatar (+ Builder unit class; supersedes 2026-04-20 on-field-hero)](decisions/2026-04-27-commander-as-summoned-ability-avatar.md) | Medium |
| 2026-04-26 | [Prototype reshape plan (Step C, 6 steps + 2026-04-27 amendment; **Accepted 2026-04-29**)](decisions/2026-04-26-prototype-reshape-plan.md) | Medium |
| 2026-04-26 | [Phase 1 exit one-pager (closes 2026-04-25 Follow-up #11)](decisions/2026-04-26-phase-1-exit-one-pager.md) | Easy |
| 2026-04-26 | [Attack-type mapping: 7-type taxonomy + per-tower map + RPS armor matrix + status-proc table](decisions/2026-04-26-attack-type-mapping.md) | Medium |
| 2026-04-25 | [Q2 ratified: real-world cultures direction (Greek / Aztec / Norse) + launch-match design skeleton](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) | **Hard** |
| 2026-04-25 | [Q2 world pitch draft (synthetic mythic-history braid) — **Superseded by 2026-04-25 ratification**](decisions/2026-04-25-q2-world-pitch-draft.md) | n/a |
| 2026-04-24 | [Phase 1 vision reopen — supersedes 2026-04-21 + 2026-04-22; thematic direction partially superseded by 2026-04-25](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) | **Hard** |
| 2026-04-21 | [Concept tightening: 3/3/3 + dungeon cosmology + Ash-enabler hybrids — **Superseded by 2026-04-24**](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) | **Hard** |
| 2026-04-19 | [Cascade restructure: consolidate to root, create stages/research/decisions dirs](decisions/2026-04-19-cascade-restructure.md) | Medium |
| 2026-04-19 | [Admin UI v1: single-file node-graph concept map](decisions/2026-04-19-admin-ui-v1.md) | Easy |
| 2026-04-19 | [Design prototype scope: throwaway HTML/JS permitted](decisions/2026-04-19-design-prototype-scope.md) | Easy |
| 2026-04-19 | [Tutorial glow affordance too subtle — log as design-debt](decisions/2026-04-19-tutorial-cell-affordance.md) | Easy |
| 2026-04-19 | [Intro-game baseline gaps escalated to concept-gaps pass](decisions/2026-04-19-intro-baseline-gaps.md) | Easy |
| 2026-04-19 | [Concept thinness load-bearing — pause workflow queue for concept-gaps pass](decisions/2026-04-19-concept-thinness-escalation.md) | Easy |
| 2026-04-20 | [Meta-UI envelope: settings menu + pause/meta-controls bundle](decisions/2026-04-20-meta-ui-envelope.md) | Easy |
| 2026-04-20 | [Audio architecture: 5-bus mixer + ducking + focus-loss](decisions/2026-04-20-audio-architecture.md) | Easy |
| 2026-04-20 | [Accessibility floor as Phase 2 constraint](decisions/2026-04-20-accessibility-floor.md) | Hard |
| 2026-04-20 | [Commander identity floor: Phase 4 §4.1 minimum spec](decisions/2026-04-20-commander-identity-floor.md) | Medium |
| 2026-04-20 | [First-run flow: click budget + returning-player branch + skippable tutorial](decisions/2026-04-20-first-run-flow.md) | Easy |
| 2026-04-20 | [Save model: mode-aware save + always-persistent commander profile](decisions/2026-04-20-save-model.md) | Medium |
| 2026-04-20 | [Prototype `hybrid.pair` is ancestry tag only](decisions/2026-04-20-prototype-hybrid-pair-shape.md) | Easy |
| 2026-04-20 | [Prototype pivots from throwaway to playable concept-demo (Step 10 unblocks Step 5 playtest)](decisions/2026-04-20-prototype-concept-demo-pivot.md) | Medium |
| 2026-04-20 | [Prototype debug-check sweep (pre-playtest) — 6 findings resolved](decisions/2026-04-20-prototype-debug-check-sweep.md) | Easy |
| 2026-04-20 | [Prototype interaction layer — hover / right-click / sell / upgrade [PROPOSAL] / reference panel](decisions/2026-04-20-prototype-interaction-layer.md) | Medium |
| 2026-04-20 | [Prototype visuals overhaul + insight layer](decisions/2026-04-20-visuals-insight-pass.md) | Medium |
| 2026-04-20 | [Doc-cascade split: CONCEPT.md → hub + concept/phase-1..7.md (+ cascade-lint)](decisions/2026-04-20-doc-cascade-split.md) | Easy |
| 2026-04-20 | [Meta-UI shell polish (splash glyphs / login branch / menu branch / mode-aware pause)](decisions/2026-04-20-meta-ui-shell-polish.md) | Easy |
| 2026-04-20 | [Profile panel layer — dedicated Profile scene + mode-gated writeMatchSave](decisions/2026-04-20-profile-panel-layer.md) | Easy |
| 2026-04-20 | [Options 5 tabs real — audio sliders + rebind + video/a11y/gameplay persisted](decisions/2026-04-20-options-five-tabs-real.md) | Easy |
| 2026-04-20 | [Commander-pick identity upgrade — SVG silhouettes + XP ladder + cosmetic locks](decisions/2026-04-20-commander-pick-identity-upgrade.md) | Easy |
| 2026-04-20 | [First-run discoverability prompts (right-click / I-key / hover) with permanent dismiss](decisions/2026-04-20-first-run-discoverability.md) | Easy |
| 2026-04-20 | [Age-as-history flavor banner + mapmods.json data + auto-age-up toggle](decisions/2026-04-20-age-history-flavor-mapmods.md) | Medium |
| 2026-04-20 | [Spontaneity random events (events.json, 25% seeded LCG, weighted pool)](decisions/2026-04-20-spontaneity-random-events.md) | Easy |
| 2026-04-20 | [Commander-on-field hero — **Superseded by 2026-04-27**](decisions/2026-04-20-commander-on-field-hero.md) | Medium |
| 2026-04-22 | [Step B: Prototype reshape plan — **Superseded by 2026-04-24** (18 sub-steps void)](decisions/2026-04-22-step-b-prototype-reshape-plan.md) | Medium |

---

## Admin UI / Prototype / Legacy

- [`admin/index.html`](admin/index.html) — node-graph admin UI per [decision](decisions/2026-04-19-admin-ui-v1.md). **`admin/concept.json` retired 2026-05-06** from source-of-truth chain per [post-arc ratifications](decisions/2026-05-06-post-arc-ratifications.md); `concept/phase-*.md` tree + `decisions/` files are sole truth. JSON file remains in repo as historical artifact only.
- [`prototype/index.html`](prototype/index.html) + [`prototype/data/`](prototype/data/) + [`prototype/start.bat`](prototype/start.bat) (Python `http.server` :8765) + [`prototype/PORT-NOTES.md`](prototype/PORT-NOTES.md) + [decision](decisions/2026-04-19-design-prototype-scope.md).
- `tw-commanders-starter/` — original starter; archived 2026-04-19. Do not edit.

---

## When to update this doc

- Stage / research status changes (Stub → Draft → In review → Locked).
- New decision file added → add one-line row to table above.
- Current work pointer shifts.
- Doc renamed, moved, archived.

Treat `CASCADE.md` as single source of truth for "what exists and where." If it disagrees with the filesystem, fix one or the other.

---

*Document version: 0.81 — 2026-05-06: Economy paper-balance ratification LANDED (§4.8 item #7 ✅ DONE). Single-doc 3-check cross-coherence audit at zero cascade-violations: Tribute spend-vs-income at Easy-on-curve (~12,400 T headroom preserved); Divinity spend-vs-income across realistic / expert / theoretical-ceiling envelopes (4/6/8→6 with wastage UI per R10 lock); §4.11.8 Hardcore-expert realized math closes to 0.993 ≈ 1.0 exactly. No new design surface — built on locked Numbers-phase #13 R1-R10 magnitudes. Phase 4 advances to **6 of 11 exit-gate items closed**. Hard guards verified untouched verbatim. PM autonomy mandate carries. Prior 0.80 — §4.4 mobile unit control RN arc-close. Older versions archived to [`CASCADE-history.md`](CASCADE-history.md).*
