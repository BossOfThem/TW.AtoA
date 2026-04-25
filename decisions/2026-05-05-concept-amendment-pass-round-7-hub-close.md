# Decision — CONCEPT amendment pass Round 7: Hub CONCEPT.md version bump + phase index touches (CLOSES amendment-pass arc 7/7)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Easy
**Affects:** [`CONCEPT.md`](../CONCEPT.md) (phase index rows 3/4/6/7, non-negotiables list, version footer)

---

## Decision

Round 7 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). **CLOSES the arc 7/7.** Three changes to the hub CONCEPT.md:

- **Phase index rows touched** (4 rows updated to reflect new §-anchors landed in Rounds 2-6):
  - **Phase 3 row** — added "6-mode launch roster (Solo Campaign / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze)" (Round 2).
  - **Phase 4 row** — added "§4.6a auxiliary-slot catalog" (Round 5), "§4.10 Tower-vs-Unit math (17-item conceptual frame + master DPS×integral equation)" (Round 3), "§4.11 Numbers floor (HP curve / (k) exponents / DPS ladder / commander magnitudes / per-mode tuning / skill-bar thresholds)" (Round 4); "Tribute" qualified to "Tribute kill-only" + "Divinity" qualified to "Divinity 6-source roster" (Round 5).
  - **Phase 6 row** — added "§6.5 skill-bar telemetry protocol" (Round 6).
  - **Phase 7 row** — added "(incl. 'Go big at launch' non-negotiable)" (Round 6).
- **Non-negotiables list** — added "**Go big at launch.** MVP ships the full content skeleton (3 civs × full ladder + 3 Gods via 9 Fusion recipes + 6 launch modes). Cuts go to post-launch content, never to the launch skeleton." Cross-link to phase-7 §7.4. Increases visibility from §7.4 trailing bullet to canonical hub non-negotiable.
- **Version footer bumped 0.8 → 0.9** with full arc summary covering all 7 rounds + cascade-lint discipline + §2.4a + §5.4 [LOCKED] untouched-throughout reaffirmation + spine-anchor stability sentence + post-arc track backlog. Prior 0.8 / 0.7 / 0.6 / 0.5 / 0.4 history preserved per CONCEPT.md footer convention (no doc-hygiene trim — that rule applies to CASCADE.md, not CONCEPT.md).

§5.4 + §2.4a [LOCKED] surfaces UNTOUCHED. Hub vision line UNTOUCHED (already 2026-04-26 real-cultures-aligned).

## Context

After Rounds 1-6, the spine docs carried 6 new / rewritten §-surfaces (phase-3 §3.6 / phase-4 §4.6 / §4.6a / §4.7 R11 / §4.10 / §4.11 / phase-6 §6.5 / phase-7 §7.4 bullet) but the hub CONCEPT.md still presented the pre-amendment phase-row summaries. A reader booting from CONCEPT.md downward would not learn that §4.10 / §4.11 / §4.6a / §6.5 even exist — they'd have to open phase-4 / phase-6 to discover the new sections.

Round 7 closes that gap: the hub now advertises the new §-anchors in the index, and the "Go big at launch" doctrine is elevated from a §7.4 bullet to a hub-level non-negotiable so it's visible without opening phase-7.

## Alternatives considered

- **Option A — Hub version bump only; no phase-index touches.** Rejected: the index rows are the load-bearing one-liners that orient any first-time reader. Leaving them stale defeats the consolidation premise of the entire amendment pass.
- **Option B — Hub version bump + index touches; "Go big" stays §7.4-only.** Rejected: §7.4 has 13 bullets; "Go big" deserves equal hub visibility to "Solo mode must be fully great" and "Strict no-pay-to-win" since it carries equal scope-cut authority. Promoting it costs 2 lines.
- **Option C — Hub bump + index touches + non-negotiables addition (chosen).** Full surface coverage. Closes the spine-anchor stability commitment from Round 1.

## Reason chosen

Option C is the only choice that fully delivers the consolidation premise. The index rows are the one-line entry points to each phase doc; they have to be accurate or the cascade-lint discipline fails on its own discovery surface. The "Go big" promotion is a low-cost / high-visibility bind on the doctrine — one line of new content, much higher cite-ability.

The footer 0.8 → 0.9 bump (rather than 0.81 / 0.85) reflects the substantive scope of the arc: 7 new decision files, ~290 net lines of new/rewritten spine content, 4 phase docs touched, plus the hub. Prior 0.7 → 0.8 was a comparable cascade (the 2026-04-26 real-cultures frame cascade partial); this one is a peer.

## Reversibility note

**Easy.** Reverting Round 7 means re-pasting the v0.8 footer + 4 prior phase-index rows + dropping the non-negotiables bullet. The Rounds 2-6 spine §-surfaces stay regardless — Round 7 is the *display* of those rounds at the hub, not the rounds themselves.

## Follow-ups

- **Final dual-push** (carries Rounds 6-7 + closes arc) per scope-decision queue.
- **HANDOFF.md rewrite** at next "prepare for handoff" trigger — capturing arc-closed state + post-arc track backlog (per-tower authoring / per-commander authoring / per-civ specialization / per-map authoring / research/06-tw-subgenres / Phase 5 readiness gate).
- **Per-tower authoring sub-pass** is now unblocked; consumes §4.10 frame + §4.11 magnitudes + §4.6a aux catalog as the spec floor.
- **Per-commander authoring sub-pass** is now unblocked; consumes §4.11.6 damage-floor + §4.1 identity-floor for control / summon / economy effect-type variants.
- **Phase 5 readiness gate** — engine-side telemetry implementation per §6.5 protocol; wave-composition variance per §4.7 R11 mandate; both are Phase 5 owns-this items now spec-anchored.
