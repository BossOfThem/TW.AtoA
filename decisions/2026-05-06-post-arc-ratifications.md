# Decision — Post-per-civ-arc ratifications (next-track + 3 doc-debt resolutions)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Mixed (see per-item below)
**Affects:** [`CASCADE.md`](../CASCADE.md) reading order + Admin UI section + pointer + decisions table + version footer; [`CLAUDE.md`](../CLAUDE.md) handoff-trigger checklist; [`tools/cascade-lint.py`](../tools/cascade-lint.py) per-file size-cap override; [`PROGRESS.md`](../PROGRESS.md) Debts-carried list. No spine-doc edits required by this decision; all four items are PM-ratified state changes recorded for cascade integrity.

---

## Decision

Post-per-civ-arc-close, four PM-ratified state changes (one batched AskUserQuestion call, all four Recommended picked):

1. **Next-track pick:** §4.7 enemy direction lock + Round 11 wave-composition variance mandate, bundled. Phase-4 OPEN exit-gate item #4 + R11 mandate from 2026-05-05 amendment-pass R6. Highest cascade-unblock at this point — per-map authoring needs §4.7 creep-roster as input (else rework); per-civ signature_creep_types per-creep-row content unlocks; defends §4.11.8 skill-bar thresholds from memorization meta. Closes 2 of 7 remaining Phase-4-exit-gate items in one arc.
2. **`admin/concept.json` retired from source-of-truth chain.** Documented `concept/phase-*.md` tree + `decisions/` files as sole truth. Removed from CASCADE reading order item #8 + CLAUDE handoff-trigger checklist. Admin UI section in CASCADE retains `admin/index.html` reference but flags `admin/concept.json` as retired-not-canonical. Eliminates dual-source-of-truth maintenance debt for rest of development.
3. **`concept/phase-4.md` soft-cap ratified 600 → 700.** Implemented in `tools/cascade-lint.py` as a per-file override (other docs retain the 600 cap). Phase-4 is the heaviest spine doc by design (entire mechanical floor lives there); 700 reflects realistic terminal size accommodating remaining §4.4 + §4.7 + Fusion-numerics + economy-numerics + monetization-stub + art-director-stub content. Eliminates the ongoing "carried soft-cap 636/600" debt note from every cascade-lint run. cascade-lint clean immediately after the bump.
4. **Cultural-sensitivity Follow-up #5 consultation timing locked: at Phase 4 exit.** Last Phase-4-exit-gate item, before any art / VFX / pose / VO / civ-flavor surface direction prose generation begins in Phase 5. Heaviest-load Aztec / secondary Norse / lightest Greek per per-commander R5 one-pagers. Per-civ + per-tower arcs deliberately used civ-neutral mechanical-content language to preserve this gate's integrity — Phase 5 content authoring starts with consultation findings already in hand.

## Reason chosen

Each item is the lowest-friction, highest-cascade-discipline option among its alternatives:

- **Next-track §4.7+R11** beats per-map (rework risk if §4.7 lands creep-archetype roster after maps), §4.4 BLOCKER (smaller downstream cascade — touches commander/builder UX, not per-map / per-civ content), and Phase 5 readiness gate (cascade-violation risk; Phase 5 should not open before Phase 4 closes).
- **Retire admin/concept.json** beats regenerate (requires generator-script authoring + ongoing maintenance) and full hand-rewrite (will go stale again as Phase 4-7 land). The 2026-04-25 ratification + 2026-04-26 one-pager + concept/phase-*.md tree already function as authoritative; admin/concept.json was a Phase-1/2 navigation artifact that has outlived its scope.
- **Cap bump 600→700 on phase-4.md only** beats trim-to-600 (burns a session on doc-hygiene that will need redoing as §4.4/§4.7/etc. land) and accept-ongoing-breach (lint findings lose meaning when the same one carries indefinitely). Per-file override preserves 600 cap on all other docs.
- **Cultural-sensitivity at Phase-4 exit** beats schedule-now (consultants need a stable target to react to; engaging before §4.7 + per-map land risks compressed back-and-forth), defer-to-art-director (art-director engagement may itself be Phase-5-adjacent, pushing consultation late), and defer-to-Phase-5-readiness-gate (compresses consultation timeline against Phase-5 content lock).

## Reversibility

- Item 1 (next-track): **Easy.** Next-track picks are operational, not concept-constraint. Reversing means picking a different next-track on subsequent ratification.
- Item 2 (admin/concept.json retire): **Easy.** Retirement is a documentation change; the file remains in repo (unmodified) and can be re-promoted to source-of-truth via decision-file supersession if a future need emerges.
- Item 3 (cap bump 600→700): **Medium.** A subsequent decision file can lower the cap once Phase 4 closes and content stabilizes; cap-as-discipline-signal is the trade-off being made. Per-file override mechanism in cascade-lint is reversible by editing the override dict.
- Item 4 (cultural-sensitivity timing): **Hard.** The 2026-04-25 ratification mandates consultation before any Phase-5 content lock; Phase-4-exit timing is the latest viable interpretation of that mandate. Earlier scheduling remains within-mandate; later scheduling would breach the 2026-04-25 lock.

## Follow-ups

1. **Next session opens §4.7 + R11 sub-arc.** Likely 3-5 round queue (R1 scope + per-archetype creep-roster authoring + per-mode wave-composition + cross-mode audit + spine-doc edits at `concept/phase-4.md §4.7` + Round 11 variance mandate body). PM autonomy mandate carries from per-civ + per-tower arcs.
2. **`admin/concept.json` left in repo unmodified** as historical artifact. CASCADE Admin UI section flags it as retired. If admin/index.html is touched in future, decide then whether to delete the JSON or leave for history.
3. **`tools/cascade-lint.py` per-file override mechanism** is now available for future per-doc cap exceptions if needed (e.g., phase-7.md if it grows a long Follow-ups roster). Generalizes the precedent.
4. **Cultural-sensitivity consultation prep work** can begin tracking now (consultant identification, scope brief, deliverable shape) without engaging consultants — the engage-gate is at Phase-4 exit, not the prep-gate.
5. **Three-civ-three-equation-form fingerprint** (locked at per-civ RN as Phase-4-spec-level invariant) carries forward as the canonical per-civ identity discipline. Future patch civs (Follow-up #6) must surface a fourth equation form with a fourth non-overlapping free-variable-set or fingerprint reopens.
