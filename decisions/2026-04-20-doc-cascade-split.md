# Decision — Doc cascade split (CONCEPT → hub + phase children)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** CONCEPT.md, concept/phase-1.md … phase-7.md (new), tools/cascade-lint.py, CASCADE.md (decisions table row only)

---

## Decision

Split the oversized `CONCEPT.md` (627 lines, 2026-04-20) into a small hub + one file per phase so every MD in the cascade fits the 200–600 line readability band and a fresh session reads only the phase it needs:

- `CONCEPT.md` → hub (~120 lines): vision, phase index with 1-sentence summaries, §7 non-negotiables, §5.4 naming conventions.
- `concept/phase-1.md` … `concept/phase-7.md` → full phase content, one file each.
- `tools/cascade-lint.py` gains a 600-line soft-cap warning, a `concept/` folder integrity check (every phase file has `Status:` + `Last reviewed:` frontmatter; hub's phase index links to all seven), and a best-effort cross-reference scan that warns when a `CONCEPT.md §N.M` reference elsewhere in the repo no longer resolves.

CASCADE.md is **not** split — verification this session shows it at 153 lines, well inside band. A prior audit misreported its size; the plan is updated to match reality.

## Context

The doc cascade anchors every fresh session's bootstrap read. `CONCEPT.md` at 627 lines is the longest read on the critical path and the only root doc over the 600-line band. No size rule exists in `cascade-lint`. PM priority: "updating MDs true to 200–600 line logic cascade / folder logic using shortcuts / links that reduce Claude's read time / action time."

## Alternatives considered

- **Option A — leave CONCEPT intact until Phase 5.** Safe, but keeps the longest read on the critical path for months and creates no incentive to re-read in smaller scopes.
- **Option B — add a 600-line warning to lint only.** Lowest blast radius. Not chosen because a warning without a split is noise; the split is the fix.
- **Option C — split CONCEPT into hub + per-phase children, extend lint.** (Chosen.) Largest upfront churn but aligns CONCEPT with the band, keeps the waterfall discipline visible (phase boundary = file boundary), and makes the ceiling enforceable.

## Reason chosen

**3x debug loop:**

- **Loop 1 — critique.** Splitting CONCEPT risks scattering the waterfall-cascade discipline across seven files. A fresh session might edit `concept/phase-3.md` without noticing that `concept/phase-2.md` constraints forbid it. Hub-rot: the hub's phase index goes stale as children are edited. Cross-ref rot: every external `CONCEPT.md §N.M` link becomes a potential 404.
- **Loop 2 — steelman.** The cascade discipline already lives in the prose of `CLAUDE.md §Cascade discipline` + the decision log — not in CONCEPT's physical monolith. Per-phase files actually *reinforce* the waterfall because the phase boundary becomes a file boundary. Hub-rot is solvable via lint (enforce "hub lists all seven children"). Cross-ref rot is a one-time fixup (grep + rewrite) plus lint for future additions.
- **Loop 3 — synthesis.** Split. Keep the hub tight (vision + phase index + non-negotiables + naming). Extend lint to catch hub-child drift and stale §-anchors. File this decision before touching the files so downstream confusion traces back to a written source.

## Reversibility note

Easy. The split is copy-paste-mergeable back into a single file. Lint rules are additive. No CONCEPT constraints change. Downstream decision entries that reference `CONCEPT.md §N.M` anchors get rewritten by lint-assisted sweep; worst case is a flurry of trivial link-fix commits.

## Follow-ups

- Execute the split: create `concept/phase-1.md` … `phase-7.md`, rewrite `CONCEPT.md` as hub.
- Extend `tools/cascade-lint.py` with size-cap + concept-folder integrity + cross-ref warning.
- Run `python tools/cascade-lint.py` after each step; expect clean.
- Decisions table in CASCADE.md gains a row for this file.
- CASCADE.md version bumps v0.10 → v0.11.
- Future: when Phase 5 opens, consider a second split (phase-5 → phase-5/01-engine.md, phase-5/02-data.md, …).
