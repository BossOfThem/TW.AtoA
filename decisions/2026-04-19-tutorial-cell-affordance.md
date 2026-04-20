# Decision — Tutorial glow affordance is too subtle; log as design-debt

**Date:** 2026-04-19
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (tutorial step 1), `CONCEPT-GAPS.md` (row: onboarding clarity), future `stages/00-session-start.md`.

---

## Decision

Record the PM playtest finding that tutorial step 1's "glowing cell" affordance is not visually strong enough to communicate where towers may be placed. File as a prototype design debt, to be addressed in the next coverage-driven prototype pass (PROGRESS.md Step 4) and captured as a requirement in the eventual `stages/00-session-start.md` spec. Do NOT hot-fix the prototype in this pass; this decision only logs the finding.

## Context

During the 2026-04-19 PM playtest over `localhost:8765`, the PM could not reliably identify which board cells accepted placement at tutorial step 1. The implemented "glow" cue is imperceptible at typical monitor brightness. This is a concrete, reproducible UX defect; it is also an instance of a broader onboarding/affordance gap captured in `CONCEPT-GAPS.md`.

## Alternatives considered

- **Option A — Hot-fix the prototype now.** Crank glow alpha / add pulse animation / outline. Rejected: prototype changes are out-of-scope for the concept-gaps pass; also risks whack-a-mole fixes before the affordance pattern is specified.
- **Option B — Discard the finding as prototype-specific.** Rejected: the affordance problem generalizes to any tutorial step that uses color-only or low-contrast cues; it is a CONCEPT-level accessibility and onboarding concern.
- **Option C — Log and defer (chosen).** Record the finding with enough detail to drive the next prototype pass and the stage-00 spec, without silently editing either now.

## Reason chosen

Consistent with guided-cadence discipline: concept-gaps pass does not touch prototype. The finding is concrete and reproducible; it survives a session clear as a dated entry. When Step 4 (prototype pass) runs, this entry is the acceptance criteria ("placement-eligible cells are unambiguously visible at default brightness, using shape/outline, not color/glow alone — passes a colorblind-sim check").

## Reversibility note

Easy. If later playtests show the glow alone is sufficient, revise the entry with a supersede link. No downstream content depends on it yet.

## Follow-ups

- Step 4 prototype pass: stronger affordance (outline + inner shape mark, not color alone). Must pass a grayscale screenshot check.
- `stages/00-session-start.md` (when drafted): include placement-affordance requirement in the accessibility subsection.
- Cross-reference: `CONCEPT-GAPS.md` row `ONBOARD-02 tutorial affordance`.
