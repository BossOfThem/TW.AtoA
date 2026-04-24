# Decision — Prototype reshape plan (Step C)

**Date:** 2026-04-26
**Status:** Proposed
**Reversibility:** Medium (shape of plan is reversible; once implementation lands, reverting costs about a week of two-dev time)
**Affects:** `prototype/index.html` BALANCE region, `prototype/commanders.json`, `prototype/ages.json` (rename candidate), `prototype/towers.json` (if exists), new `prototype/civilizations.json`, new `prototype/attack-types.json` (or inline), new `prototype/fusion-recipes.json`.
**Parent:** [`2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility Hard), [`2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (Reversibility Medium), [`2026-04-26-phase-1-exit-one-pager.md`](2026-04-26-phase-1-exit-one-pager.md).
**Supersedes:** The void left by Step B (prototype reshape) after the 2026-04-24 Phase 1 reopen froze the prototype against further concept-drifting edits. This plan is Step C — the first proper reshape plan filed since the freeze, under the live real-cultures frame.

---

## The plan (no code; shape only)

### Scope

Reshape `prototype/` from the 2026-04-21 3/3/3-era state (3 lineages Ash/Nature/Prayer, 3 tiers Dust/Form/Apotheosis, Gold/Faith/Cinders economy placeholder, 5-silhouette roster) into the 2026-04-25-ratified + 2026-04-26-cascaded state (3 civilizations Greek/Aztec/Norse, 4-tier ladder T1→T4 + Fusion, Tribute/Divinity 2-currency, 3 civ-coded silhouette roster, 7-type × 5-armor RPS matrix). Prototype remains a **throwaway harness for CONCEPT decisions per the [2026-04-19 prototype-scope decision](2026-04-19-design-prototype-scope.md)** — this plan does not port the prototype into an engine and does not produce engine code.

### Step-by-step shape

**Step C1 — Data layer reshape (inert).** Edit data files; do NOT touch visual/UI code yet. Verifies the data skeleton holds.

1. Add `prototype/civilizations.json` with 3 entries — Greek, Aztec, Norse. Per-civ fields: display name, palette hex triplet, icon glyph placeholder (SVG path or Unicode shape), 6 T1-T3 tower names + 5 unit names + 6 T4 Demigod names + 3 God names (all locked content-skeleton per ratification; do NOT rename without PM input).
2. Add `prototype/fusion-recipes.json` with 9 entries — one per God, each pointing at its 2 source T4 Demigod IDs and its 2-type damage profile per the attack-type decision.
3. Add `prototype/attack-types.json` with 7 entries (Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine) + 5 armor-tag entries (Unarmored / Shielded / Beast / Spirit / Colossal) + the RPS matrix (each type → {strong-vs, weak-vs, status-proc}). Source of truth for the combat layer.
4. Rename `prototype/ages.json` → `prototype/tiers.json` with 4 entries (T1 swarm, T2 mainline, T3 elite, T4 Demigod) + a `fusion` meta-entry for the Fusion event (not a tier; trailer beat). Migrate any surviving age-gate trigger logic by renaming fields, not rewriting.
5. Migrate `prototype/commanders.json` from its 3-lineage / 5-silhouette / Ash-Nature-Prayer state to the locked trio: Leonidas / Montezuma II / Ragnar Lothbrok. Each entry retains the identity-floor fields (portrait variant slot, silhouette variant slot, 12 voice-line bank [PROPOSAL shape], passive name, signature-ability name, long-CD-ability name, 20-level XP ladder, 3 cosmetic slots L5/L10/L15). Signature-ability names are **locked** per the 2026-04-25 ratification (Spartan Training / This Is Sparta! / The Last Stand, etc.) — do NOT rename without PM input.

**Step C2 — Silhouette 5→3 SVG migration.** Per the re-rebased [`2026-04-20-commander-pick-identity-upgrade.md`](2026-04-20-commander-pick-identity-upgrade.md). Collapse the 5 SVG silhouette paths (Sinew pike / Ember hooded / Forge anvil / Crown banner / Veil masked) to 3 civ-coded silhouettes:
- **Leonidas** — Greek phalanx / shield-and-spear iconography
- **Montezuma II** — Aztec priest-king / feathered headdress iconography
- **Ragnar Lothbrok** — Norse longship / axe / raider iconography

Specific poses are **gated by cultural-sensitivity pass** per 2026-04-25 Follow-up #5 — Aztec silhouette especially must avoid caricature; Leonidas must pass the 300-movie-ideology audit; Ragnar must route through TV-show-vs-history framing. Until the sensitivity pass completes, use **neutral-abstract placeholder silhouettes** (e.g., shield/headdress/axe icons as geometric shapes rather than figure drawings) so the silhouette-test harness (`?silhouette-test=1` + Shift+S grayscale toggle) continues to work on something grayscale-readable.

XP ladder (20 [PROPOSAL]), cosmetic tick marks at L5/L10/L15, Voice-bus caption-preview, and silhouette-test harness all **survive unchanged**.

**Step C3 — Resource bar migration.** Replace any Gold/Faith/Cinders placeholders with the **Tribute + Divinity** 2-currency HUD:
- Tribute: primary currency. Shown numerically, large. Earned from kills + passive trickle.
- Divinity: mythic token. Shown as **6 discrete pips**, not a number. Fills 1 pip per boss round (mini-boss 5/15/25 + main-boss 10/20/30). Spending 2 pips opens the Fusion menu civ-wide; 1 pip per Fusion execution.
- Mythium (PvP-only) unchanged from prior prototype state.

**Step C4 — Tier-ladder UI sketch.** The prototype does not need to fully render the ladder visually, but it should surface the tier of any tower + a merge-preview affordance:
- Tower card shows its tier (T1 / T2 / T3 / T4) and its primary attack type (1 of 7).
- On placing a duplicate T1 next to a T1 (within-civ), a merge-preview ghost shows the T2 candidate.
- On placing a duplicate T2/T2, preview the T3.
- On reaching T3 + Tribute threshold, show a "Promote to T4 Demigod" button.
- On having 2 T4 Demigods + 2+ Divinity, show the **Fusion menu** listing the 3 civ Gods and their recipes (lit if reachable, dimmed if not). Clicking a lit God + spending 1 Divinity + consuming the 2 source Demigods places the God in one board slot.

**Step C5 — 7-type × 5-armor RPS indicator.** Add a small tooltip / glyph overlay on hover: tower attack type + enemy armor tag + RPS result (strong / neutral / weak / immune). Surfaces the attack-type decision's gameplay-speed readability goal per `concept/phase-6.md §6.2`.

**Step C6 — Dead-code pass.** Remove or gate any prototype code paths that only made sense under the superseded 3-lineage / 3-tier / Ash-enabler-hybrid framing. Flag, do not delete, anything that still has reuse value under the new frame (e.g., grayscale silhouette-test mode) — the freeze-era rule of preserving as-much-as-possible still holds.

### What this plan does NOT do

- **Does not commit to engine porting.** Prototype stays a throwaway HTML/JS harness per [2026-04-19 prototype-scope](2026-04-19-design-prototype-scope.md). Engine choice is still OPEN (`concept/phase-7.md §7.1 #4`).
- **Does not lock any numbers.** All per-tower Tribute costs, per-God Divinity costs, per-tier merge thresholds, XP ladder pacing, attack-type RPS percentages (+25%/-25% placeholders), status-proc durations remain [PROPOSAL] per 2026-04-25 Follow-up #13.
- **Does not lock silhouette poses.** Placeholders until cultural-sensitivity pass clears.
- **Does not touch §2.4a accessibility floor [LOCKED].** Prototype's existing colorblind / grayscale / reduce-motion affordances stay as-is; extensions would go through `§2.4a` + `§5.4`-conformant decision entries.
- **Does not touch §5.4 naming conventions [LOCKED].** All locked names from the 2026-04-25 ratification stay verbatim.

---

## 3x debug loop

**Loop 1 — aggressive critique.**

(a) This plan is pre-mature. Cultural-sensitivity pass is a mandatory gate and hasn't happened — reshaping silhouettes / portraits / cosmetic flavor before the pass risks locking visuals the pass will reject, wasting the reshape work. (b) The data-layer reshape (Step C1) touches `commanders.json` / renames `ages.json` → `tiers.json` — if PM decides to pivot Q3 or restore some prior decision, the reshape costs rollback time. (c) The Fusion menu UI (Step C4) is novel — no existing prototype code paths handle a 2-source-into-1-slot consumption, and specifying it without prototyping it risks a fragile spec. (d) "Neutral-abstract placeholder silhouettes" in C2 sounds like a cop-out — the silhouette-test harness exists to validate pose-differentiation, and abstract geometric shapes may not meet that validation target. (e) Step C6 "dead-code pass" is under-specified — which paths, what gating mechanism, what's the rollback?

**Loop 2 — steelman.**

(a) The sensitivity-pass concern is real, but the plan explicitly defers pose-locking and uses abstract placeholders. The data layer (names, civs, recipes) is not sensitivity-gated — the ratification itself handled the naming-level sensitivity call when it locked the commander trio. What's gated is visual interpretation, not the existence of the characters. (b) The rollback cost is Medium not Hard because the pre-reshape state is in git history — revert is one commit. The reshape consumes roughly a week of two-dev time to land; reverting is hours. (c) The Fusion menu is novel in the prototype but mechanically simple — a 9-entry menu where 2 Demigod board slots are the input and 1 God slot is the output. No new data structures, just a state transition. Fragility risk is standard for a throwaway prototype. (d) Abstract-shape silhouettes meet the silhouette-test harness's purpose — the test checks *that silhouettes read at grayscale zoom*, which shield-shape / headdress-shape / axe-shape do just as well as figure drawings. Pose-differentiation as a design discipline survives the placeholder. (e) C6 is intentionally under-specified because dead-code discovery happens during Steps C1-C5 — listing paths pre-implementation would be speculation. The gating mechanism is "commented-out code with a dated `// SUPERSEDED 2026-04-26` marker" matching prior freeze-era discipline.

**Loop 3 — synthesis.**

File as Proposed. The plan is the right shape: data layer first (Step C1) because it's inert and verifies the skeleton; silhouette migration (C2) with explicit abstract-placeholder discipline because it unblocks the harness; resource bar + tier ladder + RPS indicator (C3-C5) because they're the three user-facing surfaces the real-cultures + attack-type cascade touches; dead-code pass (C6) last because it depends on what C1-C5 discovered. Cultural-sensitivity pass gates pose-lock but NOT the plan's existence. PM ratifies → execution begins; PM defers → plan stays Proposed and prototype stays frozen.

---

## Alternatives considered

- **A — Hold prototype frozen until engine choice locks** (Phase 4 exit, `concept/phase-7.md §7.1 #4`). Why not: engine choice is deferred until Phase 4 exit, which is deferred until cultural-sensitivity pass + patch-1 commanders + PvE scope all resolve. Freezing the prototype that long loses the prototype's purpose (throwaway harness for CONCEPT decisions) — the live CONCEPT diverges from the prototype state too far for the harness to re-engage without a reshape.
- **B — Full rewrite (delete `prototype/` and start fresh under real-cultures frame).** Why not: destroys the identity-floor plumbing ([`decisions/2026-04-20-commander-pick-identity-upgrade.md`](2026-04-20-commander-pick-identity-upgrade.md) SVG silhouettes / XP ladder / cosmetic tick marks / Voice-bus caption-preview / silhouette-test harness) and the `§2.4a` accessibility-floor affordances that are already wired. The re-rebase banners on the 2026-04-20 decisions exist precisely to preserve this work across the frame change.
- **C — Reshape plan in 6 steps** (C1 data layer → C2 silhouettes → C3 resource bar → C4 tier ladder → C5 RPS indicator → C6 dead-code). Chosen.

## Reason chosen

Option **C** because it preserves the identity-floor plumbing via re-rebased 2026-04-20 decisions, respects the cultural-sensitivity gate by deferring pose-lock without deferring the whole plan, reshapes in inert-first order (data before UI) to minimize rollback cost, and produces a PM-ratifiable shape without locking any numbers or sensitivity-gated visuals.

## Reversibility note

**Medium.** Rollback of the plan (pre-implementation) is free — the plan is a document. Rollback of the implementation is a git revert, hours of work, no destructive content loss. Locked-content-skeleton names from the 2026-04-25 ratification stay verbatim in rollback — the data-layer reshape does not invent new names, it just migrates which names are in which file.

## Follow-ups

- PM ratification → Step C1 starts. Sub-follow-ups per step if scope grows.
- Cultural-sensitivity pass (Follow-up #5) is a **hard gate on C2 pose-lock**, not on C2 abstract-placeholder implementation. Plan-level Medium reversibility is contingent on honoring this gate.
- If engine choice locks during reshape execution (unlikely — see Alternative A), reshape-in-progress items should be completed in the prototype before any engine-porting work begins. Engine porting is a separate Phase-5 decision track per `concept/phase-7.md §7.1 #4`.
- Number-balance [PROPOSAL] pass (2026-04-25 Follow-up #13) cross-cuts this plan's numeric placeholders (Tribute costs, Divinity earn rate, merge thresholds, RPS percentages, status-proc durations). Balance pass happens after the reshape lands, not before.
- `CASCADE.md` bump + `PROGRESS.md` session-log row on Proposed filing; second bump on PM ratification (Accepted); third bump per reshape step if scope warrants.
