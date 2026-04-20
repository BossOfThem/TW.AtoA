# Decision — Design Prototype Scope (browser-only, throwaway)

**Date:** 2026-04-19
**Status:** Accepted
**Reversibility:** Easy
**Affects:** CLAUDE.md ("What Claude Code should NOT do"), CONCEPT.md §phase discipline, new `prototype/` directory

---

## Decision

Browser-based HTML/JS prototypes placed in `prototype/` are permitted as design artifacts, exempt from the "no code until Phase 5" rule. These prototypes are throwaway: when Phase 5 begins in the chosen engine (Godot 4 leaning), we port **findings** (decisions, balance numbers, UX flows, pacing) — not code. The HTML prototype is archived, not migrated.

## Context

CLAUDE.md and CONCEPT.md forbid game code before engine is locked, to prevent premature engine lock-in and wasted effort on code that will be thrown away when the real engine is chosen. The PM raised that a clickable browser prototype would:

- Accelerate concept validation (click-through is faster feedback than prose review).
- Expose UX friction that stage docs can't surface on paper.
- Let us run and debug the feel of a commander + tutorial + match loop without committing to an engine.
- Produce design decisions (numbers, flow, copy) that port cleanly to any engine.

This is standard industry practice: paper → clickable prototype → engine build. The "no code" rule was meant to block **engine** work, not design prototyping.

## Alternatives considered

- **Option A — Hold the line: no code, prose/diagrams only.** Safest against scope creep, but risks stage docs calcifying around untested assumptions. Concept decisions would remain theoretical until Phase 5, months away. Not chosen.
- **Option B — Jump straight to Godot for the prototype.** Would lock engine choice prematurely (Phase 4 hasn't exited). If a finding suggests a different engine fits better, we'd have wasted work. Not chosen.
- **Option C — Browser HTML/JS throwaway prototype (chosen).** No engine commitment, no build tooling, runs from `file://`, disposable. Findings port by decision, not by code.

## Reason chosen

3x debug loop synthesis:

- **Loop 1 (critique):** Risk of scope creep — prototype becomes the de facto game, replacing Godot. Risk of code-debt thinking where a findings-level port was intended. Risk of PM anchoring on HTML quirks (DOM rendering, CSS perf) that won't match a real engine.
- **Loop 2 (steelman):** The alternative is design stasis — writing stage docs about "how it should feel" without ever testing feel. Stage 01 (commander pick) and Stage 04 (in-match core) both have blockers that are fundamentally playtest questions. A disposable prototype is the cheapest tool to answer them. Anchoring risk is mitigated by clearly marking the prototype as throwaway and by porting findings-only, not code.
- **Loop 3 (synthesis):** Proceed, with three guardrails: (1) isolated folder, (2) in-app banner declaring throwaway status, (3) decision-log mandate that when Godot begins, we port decisions not code.

## Reversibility note

Easy. If scope creeps or the prototype becomes a distraction, delete `prototype/` and revert the CLAUDE.md amendment. No downstream doc depends on the prototype's code existing; stage docs and decisions reference the prototype only as a validation source.

## Follow-ups

- [x] Amend CLAUDE.md "What Claude Code should NOT do" with the prototype exception (this session).
- [ ] First prototype: `prototype/index.html` — title → commander pick (Ember-tilted Commander B, matches CONCEPT.md §MVP vertical slice) → 60s tutorial → Lane Wars 3-wave match → end screen (this session).
- [ ] When a prototype run produces a design finding, log it as its own `decisions/` entry with pointer back to the prototype session.
- [ ] At Phase 5 kickoff: archive `prototype/` to `prototype/_archive/` and confirm no code ports across.
