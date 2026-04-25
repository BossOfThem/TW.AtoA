# Decision — CONCEPT.md amendment pass: §-placement scope + 7-round queue

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Easy
**Affects:** [`CONCEPT.md`](../CONCEPT.md), [`concept/phase-3.md`](../concept/phase-3.md), [`concept/phase-4.md`](../concept/phase-4.md), [`concept/phase-6.md`](../concept/phase-6.md), [`concept/phase-7.md`](../concept/phase-7.md)

---

## Decision

Open a **7-round CONCEPT.md amendment pass** to consolidate the 22 ratified rounds (12 conceptual 2026-05-04 + 10 numbers 2026-05-05) into the doc spine as new and rewritten §-sections. Round queue, §-placements, and downstream cascade hooks are locked below. The arc opens immediately; PM autonomy mandate from 2026-05-05 (Numbers-phase Follow-up #13 mid-arc) carries forward — surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / handoff trigger.

**§5.4 [LOCKED] / §2.4a [LOCKED] / 2026-04-25 locked content skeleton untouched.** This is a consolidation pass, not a re-ratification — every magnitude already has a superseding-eligible decision file behind it. The amendment pass binds those decisions into citable §-anchors; it does not re-open any of them.

## Context

After 22 rounds (Balance-pass #1 conceptual 6→12 on 2026-05-04 + Balance-pass #2 numbers 1→10 on 2026-05-05), the 17-item conceptual frame + extension (s) + every magnitude (HP curve / (k) exponents / Tribute yield / speed / per-map / DPS ladder / commander magnitudes / aux costs / per-mode tuning / skill-bar thresholds / Divinity sources) lives **only in `decisions/` files**. The `concept/phase-*.md` spine still reads as if 2026-04-26 — `phase-3.md §3.6` lists 5 modes (real launch is 6 + PvE-MP), `phase-4.md §4.6` says "numerics [PROPOSAL]" for the entire economy and references the deprecated Mythium (now Tribute interest mechanic in PvP-IW), there is no Tower-vs-Unit math § at all, and there is no Auxiliary-economy § at all. Every future authoring sub-pass (per-tower, per-map, per-commander, per-civ) will repeatedly cite dated decision URLs instead of stable §-anchors, and `/clear`-survivability of the spine degrades the longer it sits.

The pass is overdue. It opens now.

## Alternatives considered

- **Option A — Single mega-round.** Drop all 22 rounds into a giant edit-pass on `phase-3.md` + `phase-4.md` in one round. Rejected: ~600+ lines of new prose across 5+ §s; one cascade-lint failure rolls back hours of work; PM cannot intervene mid-edit if a §-placement decision turns out wrong; commit blast radius is enormous.
- **Option B — Per-decision-file rounds.** One amendment round per ratified decision (22 rounds). Rejected: most decisions need to land in the *same* §-section as related decisions (e.g., HP curve + k exponents + yield + speed + DPS ladder all amend a single new "Numbers floor" §). Authoring across 22 rounds creates churn — same § rewritten 5 times; lint runs 22 times; commits become noise. Wrong granularity.
- **Option C — Topical 7-round queue (chosen).** Group amendments by §-section topic, not by decision-file source. Each round lands one logical concept-spine surface; lint runs once per round; dual-push every ~3 rounds per cadence rule.

## Reason chosen

**Option C — topical 7-round queue.** §-section topic is the correct grouping unit because:

1. **Reader path** — a future reader opening `phase-4.md` for "what's the HP curve?" expects to find HP curve + (k) exponents + yield + speed all co-located in a Numbers-floor §, not scattered across 5 dated decision links inside an outdated §4.6. Topical grouping matches the read path, not the write history.
2. **Lint atomicity** — each round produces one self-consistent §-amendment that can be lint-verified standalone. If Round 4 fails lint, Rounds 1-3 are already landed and pushed; the failure isolates to the in-progress § without rolling back the rest.
3. **Cascade hook discipline** — placing the Tower-vs-Unit math § (Round 3) before Numbers floor (Round 4) means the magnitudes in Round 4 cite §-anchors from Round 3 instead of inline-defining variables. Order matters; the queue locks it.

### 3x debug loop on §-placement

**Loop 1 — aggressive critique.** Putting the entire Tower-vs-Unit math frame in `phase-4.md` makes phase-4 the longest doc in the cascade by ~2×. Phase 4 is already 322 lines; adding ~250 lines of math + numbers floor + aux economy bloats it to ~600+ and re-introduces the very problem the 2026-04-20 doc-cascade-split solved (single CONCEPT.md got too long → split into per-phase docs). Why not split phase-4 *again* into `phase-4a-systems.md` + `phase-4b-numbers.md`? Phase 6 is also a candidate home for the skill-bar thresholds (it's the Validation phase — measurement protocols belong there). And the auxiliary economy is fundamentally a *mode-coupled* system (Send-Creeps cost varies per mode per Round 8), so it could just as easily live in phase-3 §3.6 alongside the mode roster — putting it in phase-4 fragments a single concept across two phase docs.

**Loop 2 — steelman.** Phase 4 is the Specification phase. Numbers, equations, magnitudes, costs, thresholds — all of it is specification, definitionally. Splitting `phase-4.md` again would dilute that role; the precedent already says "spec lives in phase-4." The 600-line objection is real but bounded — every § amendment lands in a stable home and stops growing once the authoring sub-passes (per-tower / per-commander / per-map / per-civ) move to per-civ docs (Phase 5 territory). Skill-bar thresholds are *inputs* to the math, not *measurements* of it — they belong wherever the math is bound, not in the validation phase that *measures* whether they're hit. Aux economy is mode-coupled at the magnitude tier (Send-Creeps cost) but mode-agnostic at the *structure* tier (slot ontology, currency split, Divinity-vs-Tribute pricing rule). The structure belongs in phase-4 economy; per-mode magnitudes go in the same spot as per-mode tuning. Loop 1's "split again" objection moves the problem rather than solving it: same lines, different filename.

**Loop 3 — synthesis.** Phase 4 is the right home for all of: Tower-vs-Unit math frame, Numbers floor, Auxiliary economy (structure + magnitudes), and skill-bar threshold *values*. Phase 6 hosts skill-bar *measurement protocols* and telemetry definitions (the "how we'll know if these thresholds are hit" surface, not the values themselves). Phase 3 §3.6 absorbs the mode-roster expansion (5→6 modes; per-mode summaries with cross-references to phase-4 magnitudes). Phase 7 §7.4 absorbs the "Go big, no scope cuts" doctrine as a non-negotiable note-to-future-self. The 600-line phase-4 ceiling is acceptable because the doc role (Specification) matches the content role (specs). Re-splitting phase-4 is deferred until line-count exceeds ~800 or a clean topical seam emerges (e.g., post-authoring-sub-passes when per-civ specifics fragment naturally).

## §-placement table (locked)

| Source | Target § | Round |
|--------|----------|-------|
| 6-mode ontology + Round 7-12 deep dives (Solo Campaign / Horde-A+B / PvP-IW / PvE-MP / PvP-Maze / Round 12 aux UX) | `phase-3.md §3.6` rewrite + new `§3.6.1`–`§3.6.6` per-mode sub-blocks | 2 |
| Balance-pass #1 conceptual frame (17 items) + extension (s) + master DPS×integral equation + 7-slot round typology + (k) single-axis rule + targeting + sell-refund + boss/Divinity sources + skill-bar axes | `phase-4.md` new `§4.10` Tower-vs-Unit math | 3 |
| Round 1 HP curve + Round 2 (k) exponents + Round 3 Tribute yield + Round 4 speed + per-map + Round 5 DPS ladder + tier costs + Round 6 commander magnitudes + Round 8 per-mode tuning | `phase-4.md` new `§4.11` Numbers floor | 4 |
| 2026-05-04 Round 6 aux economy ratifications + Round 7 aux costs + (s) magnitude + Round 10 Divinity source escalation hooks + Round 12 aux UX | `phase-4.md §4.6` rewrite + new `§4.6a` Auxiliary economy | 5 |
| Round 9 skill-bar thresholds (values) + Round 11 mandate (wave-randomization + crystal-lock variance) | `phase-4.md §4.11` extension (values inline with Numbers floor) + `phase-6.md` new `§6.x` skill-bar telemetry protocols + `phase-4.md §4.7` Round-11-mandate hook | 6 |
| "Go big, no scope cuts" project doctrine + numbers-phase status closure | `phase-7.md §7.4` non-negotiable addition + `§7.5` (or `§7.x`) status note | 6 (combined) |
| Hub `CONCEPT.md` version footer + phase index row touches (modes count, Tower-vs-Unit math reference, numbers floor reference) | `CONCEPT.md` index + footer | 7 |

## Round queue (locked)

1. **Round 1 (this file)** — scope decision + §-placement table + 3x debug loop.
2. **Round 2** — `phase-3.md §3.6` mode roster 5→6 (+ PvE-MP) + per-mode summary table cross-referencing phase-4 magnitudes. Rebase `§3.4` Commander-Hero-Unit residue → §4.1 summoned-on-cast subsection (cleanup).
3. **Round 3** — `phase-4.md §4.10` Tower-vs-Unit math (NEW). Bind 17-item conceptual frame + extension (s) + master equation + variable nomenclature.
4. **Round 4** — `phase-4.md §4.11` Numbers floor (NEW). HP curve / (k) / yield / speed / per-map / DPS ladder / tier costs / commander magnitudes / per-mode tuning. Cite §4.10 anchors throughout.
5. **Round 5** — `phase-4.md §4.6` economy rewrite + `§4.6a` Auxiliary economy (NEW). Tribute curves + Divinity 4-source floor + 2-source escalation table + slot catalog + Mythium retirement note (replaced by PvP-IW Send-for-Interest mechanic).
6. **Round 6** — `phase-4.md §4.7` Round-11-mandate hook + `phase-6.md` skill-bar telemetry § + `phase-7.md §7.4` "Go big" non-negotiable + numbers-phase status footer note. Combined because each surface is small (≤30 lines).
7. **Round 7** — Hub `CONCEPT.md` version footer bump (v0.8 → v0.9) + phase index row touches + cascade-lint clean run + commit + dual-push close.

Dual-push points: after Round 3 (carries Rounds 1-3), after Round 5 (carries Rounds 4-5), after Round 7 (carries Rounds 6-7 + closes arc).

## Reversibility note

**Easy.** Each round produces a single decision file + a bounded set of §-section edits. If a §-placement turns out wrong (e.g., aux economy fits better in phase-3 after all), reverting is one round of edits + a superseding decision entry. No magnitudes change; no upstream phases reopen.

The only Hard-class risk is silently editing §5.4 [LOCKED] or §2.4a [LOCKED] — explicit guard: every round verifies untouched headers before commit.

## Follow-ups

- **Round 2 onward** runs autonomously per 2026-05-05 PM autonomy mandate.
- **Cascade-lint** after every round (per cadence rule).
- **Dual-push** at the three checkpoints above.
- **Phase-5 / phase-2 explicitly NOT touched** by this pass — both contain the [LOCKED] surfaces.
- **Phase-1 not touched** — the 2026-04-26 one-pager already serves as the Phase-1 anchor for the real-cultures frame; numbers-phase work doesn't pre-Phase-3.
- **`admin/concept.json` migration** stays deferred (separate post-arc track per Numbers-phase Follow-up #13 handoff). This pass aligns the MD spine, not the JSON mirror.
- **`research/06-tw-subgenres.md`** stays deferred (separate post-arc track). Not a CONCEPT spine surface.
