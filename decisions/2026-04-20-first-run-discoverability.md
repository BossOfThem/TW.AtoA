# Decision — First-run prompt surface (discoverability)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (toast-card DOM, `showFirstRun`/`dismissFirstRun` JS, `placeTower` + `bindActionBarTooltips` hooks, `profile.settings.firstRun.*`)

---

## Decision

Add three one-shot first-run prompts that teach right-click, I-key reference, and hover tooltips without interrupting the game. Trigger points: (1) right-click + I-key prompts fire after the first tower placement in a non-tutorial match; (2) hover prompt fires on first hover of a tower button. Dismissible with "Don't show again" writing `profile.settings.firstRun.{key} = true`. Tutorial mode suppresses all three (its narrator covers them). 8-second auto-dismiss; toast card top-center; grayscale-readable by design (ember accent border + ink-0 text).

## Context

[tutorial-cell-affordance decision](2026-04-19-tutorial-cell-affordance.md) flagged that players outside the tutorial had no prompt for the right-click sell/upgrade menu, the I-key tier reference, or the hover tooltip layer — interaction debt from the visuals-insight pass. [first-run-flow](2026-04-20-first-run-flow.md) specifies click-budget + returning-branch but left the discoverability prompts as a downstream item.

## Alternatives considered

- **Option A — Permanent HUD hint bar.** Why not: violates the meta-UI-envelope (HUD stays lean); adds permanent clutter once the player learns.
- **Option B — Tutorial-only coverage.** Why not: players who skip the tutorial (probably most returning commanders) never learn these.
- **Option C — Dismissible one-shot toasts keyed on first-touch events, profile-persisted.** (Chosen.) Fires exactly once per profile per prompt; tutorial suppresses; players who skip still get the drip.

## Reason chosen

**Loop 1 — aggressive critique.** Two prompts stacked 8.5s apart (right-click + I-key) risk overlapping if the player is actively building. The hover prompt has a race: fast players might hover *before* placing, so they see the hover prompt before the placement prompts — fine semantically but ordering is nondeterministic.

**Loop 2 — steelman.** The 8.5s delay between prompts is deliberate — enough to read and dismiss the first before the second lands. Ordering nondeterminism doesn't matter; each prompt teaches an independent behavior. Auto-dismiss at 8s keeps the game unblocked even if the player ignores the card entirely.

**Loop 3 — synthesis.** Ship as-coded. Observe in Step 5 playtest whether the second prompt lands while the first is still visible (if so, queue rather than overlap in v2). No CONCEPT change.

## Reversibility note

Easy. Remove DOM element + JS helpers + two hook calls. `profile.settings.firstRun` is additive; existing profiles get default `{rightClick:false, iKey:false, hover:false}` via `Profile.login()` seed.

## Follow-ups

- Strand 7 (this pass): hero-on-field may add a 4th first-run prompt for the commander avatar Q-signature key.
- Port note: Godot → `FirstRunPrompt.tscn` with a singleton `FirstRunManager` reading from `ConfigFile`.
