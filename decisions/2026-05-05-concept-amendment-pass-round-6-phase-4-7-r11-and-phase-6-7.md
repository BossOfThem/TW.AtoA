# Decision — CONCEPT amendment pass Round 6: phase-4 §4.7 R11 mandate + phase-6 §6.5 telemetry NEW + phase-7 §7.4 "Go big"

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Easy
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) §4.7, §4.6a (compression); [`concept/phase-6.md`](../concept/phase-6.md) §6.5 NEW + §6.6 renumber; [`concept/phase-7.md`](../concept/phase-7.md) §7.4

---

## Decision

Round 6 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). Three changes across three phase docs:

- **`phase-4.md §4.7`** — added `### Wave-composition variance mandate (NEW 2026-05-05 R9 close-out)` subsection at the tail of §4.7, capturing the Round-9 close-out mandate (random-seeded armor-tag mix per wave + per-map crystal-lock variance) that defends §4.11.8 skill-bar thresholds from a memorization meta. Locked content-skeleton bosses exempted (composition varies; identity stays fixed per the locked roster).
- **`phase-6.md §6.5 Skill-bar telemetry NEW`** — new section (between prior §6.4 and §6.5 exit-condition; exit-condition renumbered §6.6) binding the measurement protocol for the 3 skill-bar axes (matchup-correctness from RPS-counter kill events / placement-coverage from tower-engaged-second ratio / ability-uptime from cast/cooldown ratio with signature excluded). Resolves the §4.11.8 forward-anchor live. Phase-5 owns engine-side gathering; phase-6 owns the protocol.
- **`phase-7.md §7.4`** — appended "Go big at launch (non-negotiable)" bullet to the notes-to-future-self list. Captures the 2026-04-25 ratification spirit: MVP ships the full content skeleton (3 civs × full ladder + 3 Gods via 9 Fusion recipes); cuts go to post-launch content, never to the launch skeleton.

`phase-4.md §4.6a` "Currency-budget audit" subsection compressed from 4 bullets to 1 paragraph + "Mode availability matrix" subsection compressed to a single mode-optimization pointer sentence — frees lines to keep phase-4 under the 600-line cap after the §4.7 R11 addition. Phase-4 final: 597 lines. Last-reviewed bumps for phase-6 and phase-7 (2026-04-26 → 2026-05-05).

## Context

Pre-amendment, the 2026-05-05 R9 close-out mandate (wave-composition variance) was a free-floating note in the R9 decision file with no spine surface. §4.11.8 thresholds + §4.10.5 axes both implicitly assumed the mandate existed but it had no anchor. Round 6 lands that anchor in §4.7 (enemy-system surface) — the natural home, since wave composition is enemy-system content.

Phase-6 §6.4 success metrics referenced "civilization-persistence emerging by end of T3" + "armor-tag RPS reads at gameplay speed" but had no measurement protocol. The R9 thresholds are unmeasurable without engine-side event-logging definitions; §6.5 fills that gap.

Phase-7 §7.4 already carried 11 notes-to-future-self entries (cascade discipline / solo-first / no-pay-to-win / live-service / cultural-sensitivity / title-discipline). The "go big" doctrine was implicit in §6.1 ("Shipping the full locked content skeleton in MVP is deliberate") but never elevated to §7.4 non-negotiable status. Adding it makes the doctrine cite-able from any future scope-cut conversation.

## Alternatives considered

- **Option A — Wave-variance mandate in §4.11.8 not §4.7.** Rejected: §4.11.8 is a *threshold* table; the mandate is an *enemy-system spec* (what wave composition has to support). Wrong surface.
- **Option B — Skill-bar telemetry in phase-4 not phase-6.** Rejected: phase-4 binds *what the variables are* (§4.10) and *what their values are* (§4.11); phase-6 binds *how we measure them*. The protocol belongs to validation, not specification.
- **Option C — "Go big" doctrine as a new §7.5 not a §7.4 bullet.** Rejected: §7.4 already aggregates non-negotiables (no-pay-to-win / cultural-sensitivity). Adding a bullet matches the existing structure; new section would over-elevate one item.
- **Option D — All three changes in one decision file (chosen).** Round 6 is the smallest of the 7 amendment rounds in line-count terms (~30 lines net across three files). Splitting into three decision files would inflate the decision-log without consolidation benefit.

## Reason chosen

Option D collapses three small touches into one decision while keeping each surface change minimal. Each change is independently defensible (R11 mandate has its own §, telemetry has its own §, "go big" has its own bullet) but all three trace to the same Round 6 amendment-pass scope row, so the decision file mirrors that.

The §4.6a compression is opportunistic — pre-Round-6 phase-4 was at 600 / 600 (cap-tight after Round 5's §4.6 trim); Round 6's §4.7 R11 addition would push to 602 without compensating trim. Compressing the audit-bullets paragraph + mode-availability paragraph (both information-dense already) preserves all numbers while freeing 5 lines.

## Reversibility note

**Easy.** Reverting any of the three changes is local: §4.7 R11 subsection deletion (no cross-references depend on it yet), §6.5 telemetry deletion (re-renumber §6.6 → §6.5), §7.4 bullet deletion. The R9 mandate / R9 thresholds / 2026-04-25 ratification stay Accepted regardless — this round is the *display* of those decisions in the spine docs.

## Follow-ups

- **Round 7** — Hub CONCEPT.md version bump + phase-3 / phase-4 / phase-6 / phase-7 index row touches + cascade-lint clean run + commit + final dual-push + close arc.
- **Phase 5 engine-side telemetry implementation** consumes §6.5 protocol definitions for event-logging spec.
- **Phase 5 wave-composition implementation** consumes §4.7 R11 mandate (random-seeded armor-tag mix + per-map crystal-lock variance).
- **Per-mode authoring sub-pass** consumes §4.6a compressed audit + §4.11.7 tuning matrix for per-mode optimization paths.
