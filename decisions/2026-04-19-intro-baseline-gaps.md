# Decision — Intro-game baseline gaps (no settings / pause / skip / audio / save / accessibility) escalated to concept-gaps pass

**Date:** 2026-04-19
**Status:** Accepted
**Reversibility:** Easy (the gap list is a proposal layer; nothing in `CONCEPT.md` changes from this entry alone).
**Affects:** `CONCEPT-GAPS.md` (new doc, this pass), `CONCEPT.md` (sections flagged for future-phase amendment, NOT edited by this entry), `PROGRESS.md § Debts carried`.

---

## Decision

Formally recognize that `CONCEPT.md` in its current state is silent on — or under-specifies — the modern intro-game baseline feature set: settings/options menu, pause/meta-controls, skippable tutorial, save-and-exit, audio-mixer channels, accessibility floor. Create `CONCEPT-GAPS.md` as a proposal layer that catalogs each missing piece with industry-baseline citations, a severity tag, and a proposed owning CONCEPT phase. Do not edit `CONCEPT.md` in this pass — cascade discipline requires that any concept-constraint change be proposed via the gaps doc and ratified by a subsequent phase-appropriate decision entry.

## Context

The 2026-04-19 PM playtest surfaced that the prototype (and the CONCEPT behind it) ships a forced linear flow: Title → Begin → Pick → Take the field → Tutorial → Match → End. There is no volume control, no pause, no skip-tutorial, no save, no accessibility floor, no options menu. Modern strategy/TD games (Kingdom Rush 5 Alliance, Bloons TD 6, Legion TD 2, They Are Billions) all ship these by default; their absence is not a stylistic choice, it is a gap. Finding #3 from the same playtest ("concept too thin to form a vision") has the same root cause.

## Alternatives considered

- **Option A — Silently add baseline sections to `CONCEPT.md`.** Rejected: violates cascade discipline. `CONCEPT.md` is the vision anchor; additions must route through the decision log and an owning phase.
- **Option B — File individual decision entries per gap (settings, pause, save, audio, accessibility…).** Rejected: premature. Each of those decisions needs industry baseline, tradeoff analysis, and a scoped resolution; filing 8+ half-formed decisions would pollute the log and race the research.
- **Option C — Create `CONCEPT-GAPS.md` as a proposal layer; file one meta-decision (this one) documenting the escalation (chosen).** One dated record of the finding, one synthesized doc as the working artifact, future decision entries filed *per gap* as the PM ratifies each resolution direction.

## Reason chosen

Preserves cascade discipline (CONCEPT untouched), collects the gap set coherently so the PM can see the full shape before ratifying individual resolutions, and avoids premature commitment. The gaps doc is ephemeral in the sense that every row should eventually migrate into `CONCEPT.md` (via per-gap decisions) or be explicitly deferred post-launch; it is a holding area, not a permanent parallel spec.

## Reversibility note

Easy. `CONCEPT-GAPS.md` is additive; nothing depends on it yet. Deleting the doc loses only the synthesized catalog; the underlying findings remain filed here and in the source web citations.

## Follow-ups

- `CONCEPT-GAPS.md` produced this pass — prioritized catalog, top-5 must-close list, per-row citations.
- Each gap that moves from catalog → resolution gets its own dated decision entry at the time of ratification.
- `CONCEPT.md §7.1 open questions` to gain entries for any gap the PM chooses to promote to blocker status (future pass, not this one).
- `PROGRESS.md § Debts carried` updated to mark this finding and `tutorial-cell-affordance` and `concept-thinness-escalation` as filed.
