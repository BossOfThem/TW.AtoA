# Decision — Concept thinness is load-bearing; pause workflow queue for concept-gaps pass

**Date:** 2026-04-19
**Status:** Accepted
**Reversibility:** Easy (unpause workflow queue at PM's discretion)
**Affects:** `PROGRESS.md` (queue paused at Step 1.5a→complete; 1.5b–9 held), `CASCADE.md` (current work pointer), `HANDOFF.md`, `CONCEPT-GAPS.md` (new).

---

## Decision

Treat the PM's playtest statement — *"a lot of things are not complete and make it difficult to really get good a vision"* — as the current highest-priority signal. Pause the approved workflow queue (Steps 1.5b, 1.5c, 2, 3, 4…) and interpose a single concept-gaps research + synthesis pass. Resume the workflow queue only after the PM has read `CONCEPT-GAPS.md` and either (a) ratified a gap-closure sequence or (b) explicitly returned to Step 1.5b.

## Context

The approved workflow plan (`i-want-to-prioritize-validated-dewdrop.md`) prioritizes prototype-first iteration on the theory that the prototype drives the concept to near-completion. That theory assumes the CONCEPT is specified enough that the prototype is *exercising* it, not *speculating on it*. The playtest refuted that assumption: the CONCEPT has too many placeholders and missing baseline features for the prototype to be a usable vision aid. Continuing down the Step-2-through-9 path would be shaving lower-value wood while the load-bearing beam (a coherent concept) is still missing members.

## Alternatives considered

- **Option A — Proceed with Step 1.5b/1.5c.** Trim PORT-NOTES, file hybrid.pair decision, move on. Rejected: doesn't address the finding; queues another session of PM frustration.
- **Option B — Reopen CONCEPT.md directly and start filling gaps.** Rejected: cascade violation. CONCEPT is Phase 1–7 anchor; gap-filling must be staged and ratified, not cowboyed.
- **Option C — Interpose a scoped concept-gaps pass before resuming the queue (chosen).** One synthesized deliverable, industry-cited, severity-tagged, owning-phase tagged. PM then decides what to ratify and in what order.

## Reason chosen

**Loop 1 (critique):** Pausing the queue risks never resuming it. Concept-gaps work could expand indefinitely ("scope eater"). Risk real. **Loop 2 (steelman):** The queue's premise is broken until the concept is thicker; resuming without gaps-closure just defers the same PM frustration one step. Scope eater mitigated by hard cap (one synthesized doc, ~300 lines) and explicit resumption criteria. **Loop 3 (synthesis):** Interpose, cap, resume. Make the gaps pass time-boxed and deliverable-centric; write the resumption trigger into this decision entry so "when do we unpause?" has a concrete answer.

## Reversibility note

Easy. If `CONCEPT-GAPS.md` turns out to be the wrong artifact, delete it and resume Step 1.5b. No CONCEPT constraints change from this entry.

## Resumption criteria

The workflow queue (Step 1.5b onward) resumes when any of:
- PM reads `CONCEPT-GAPS.md` and names a subset of gaps to ratify (producing per-gap decision entries), and is satisfied enough with the vision to re-enable prototype work.
- PM explicitly overrides and says "resume queue anyway."
- A full working day has passed since `CONCEPT-GAPS.md` was produced and the PM has not acted — in which case Claude prompts for direction at next session start rather than self-unpausing.

## Follow-ups

- This pass produces `CONCEPT-GAPS.md`.
- Sibling entries: `2026-04-19-tutorial-cell-affordance.md`, `2026-04-19-intro-baseline-gaps.md`.
- Next session's proposal menu will be: "pick a top-5 gap to ratify" or "resume Step 1.5b."
