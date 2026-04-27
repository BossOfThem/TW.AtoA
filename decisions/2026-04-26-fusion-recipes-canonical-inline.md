# Decision — Fusion recipes: inline array is canonical for prototype scope

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (FUSION_RECIPES inline), `prototype/data/fusion-recipes.json`, `prototype/PORT-NOTES.md`

---

## Decision

The inline `FUSION_RECIPES` array inside `prototype/index.html` (currently ~line 1985) is the **single source of truth** for fusion recipe data during the concept-phase prototype. The sibling file `prototype/data/fusion-recipes.json` is retained as a legacy/sketch copy but is **not loaded** by the prototype and **must not** be edited with the expectation that changes will appear in-game. A code comment on the inline array now states this explicitly. When C5/C6 lands the JSON loader, that work will reconcile the two surfaces and flip canonicality.

## Context

A divergence audit (Layer-1 swarm, hierarchical-agent review, 2026-04-26) flagged that `loadData()` fetches eight JSON files but does **not** fetch `fusion-recipes.json`. Meanwhile `FUSION_RECIPES` is defined inline and consumed directly by the fusion menu. The prior comment ("Source: prototype/data/fusion-recipes.json + civilizations.json. Update both surfaces together until C5/C6") implied dual-surface editing, but only one surface was actually wired up. This created a foreseeable footgun: a future contributor edits the JSON, sees no effect, and either gives up or duplicates the change incorrectly.

## Alternatives considered

- **Option A — Wire `fusion-recipes.json` into `loadData()` now.** Would solve the divergence, but pulls forward C5/C6 loader work into a concept-only prototype scope and risks coupling the prototype to broker-level data shape that the engine port will probably refactor. Rejected as scope creep.
- **Option B — Delete `prototype/data/fusion-recipes.json`.** Cleanest divergence kill, but the JSON is useful as a sketch artifact for the eventual C5/C6 schema and for the engine port. Deleting it loses notes. Rejected.
- **Option C — Declare inline canonical, mark JSON as legacy.** (Chosen.) Zero code churn beyond a comment swap; preserves the JSON sketch; eliminates the footgun via in-source documentation; defers the actual reconciliation to C5/C6 where it belongs.

## Reason chosen

Option C respects the concept-phase principle "Port findings, not code" (CLAUDE.md → no code yet → prototype exception). The prototype is throwaway; the JSON-loader plumbing is engine work. Re-wiring fetch now would be Phase-5 code in a Phase-3 prototype. Marking the inline as canonical via comment + a dated decisions/ entry preserves the trail for the engine port without paying engine-architecture costs today.

3x debug loop:
- **Loop 1 (attack):** "Comment-only is wishful thinking. The next contributor will still edit the JSON expecting effect." — Counter: the comment now says "do NOT edit it expecting prototype effect" and points at this decision file. That's the strongest non-code signal we can issue without enforcing it via tooling.
- **Loop 2 (steelman):** "The JSON is genuinely useful for the engine port; preserving it is correct." — Agreed; that's why deletion (Option B) is rejected.
- **Loop 3 (synthesis):** Comment + decision file is sufficient for the concept phase. When C5/C6 opens, the loader work itself will flip canonicality and this decision can be superseded.

## Reversibility note

Easy. Reverting means deleting the comment and this file. The structural reality (only one surface is loaded) is unchanged either way; the decision only documents which surface to edit.

## Follow-ups

- C5/C6 (engine port) will own reconciliation: either load `fusion-recipes.json` and remove the inline array, or generate the JSON from the inline array as a build step. That work will supersede this decision via a dated entry.
- Add to PORT-NOTES guidance row: when porting fusion data, port from the inline array, not from the JSON.
