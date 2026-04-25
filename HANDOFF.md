# HANDOFF — Session Checkpoint

**Last session:** 2026-05-03 — C6 slice 2 LANDED (graduation cut: legacy 5-lineage / 11-age teardown).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**C6 slice 2 LANDED — graduation cut completing the multi-session C6 + C4-continuation arc.** Per PM "go" continuation, executed as 3 sub-slices (Bridge → Polish → Graduation). Slice C is the pure deletion pass: removes the legacy 5-lineage / 11-age surfaces from `prototype/index.html` now that civ-tower namespacing (Slice A, prior session) and the tutorial reshape (Slice B, prior session) have shipped. **Prototype now runs on civ-tower + 4-tier ladder shape only. Legacy 5-lineage / 11-age surfaces are fully retired.**

**Single commit `2893943`, dual-pushed to session branch + `main`.** 699 deletions / 131 insertions across 4 files: `prototype/index.html`, `tools/cascade-lint.py`, `prototype/data/ages.json` (deleted), `prototype/data/towers.json` (deleted). cascade-lint clean.

**Deleted from `prototype/index.html`:** `AGES` global; `KNOWLEDGE_PER_AGE` balance constant + `baseKnowledge` derivation in `deriveTowerStats`; collapsed age-indexed `damage[]` / `cd[]` arrays to scalars; `game.ageIdx` from `initMatch` / `initTutorial` state, `snapshot.enemies`, `effectiveTowerStats`, tick spawn, `archetypeFor` callers, render fallbacks, `endMatch`, `towerTipHTML`, `placementTipHTML`; stale `selectTower("sinew")` in `initMatch`; `BALANCE.TOWERS.sinew/ember` refs in `logBalanceCurve` (rebuilt as `cheapest * 2`); `"hybrid"` feed-kind branch in `emitFeed`; orphan `<div id="age-banner">`; `#age-banner` CSS block + `ageBannerIn` keyframes; `.row.hybrid` combat-feed rule; `.hud .age-label` rule.

**Deleted files:** `prototype/data/ages.json`, `prototype/data/towers.json`. No JS fetchers reference them; `civilizations.json` + `tiers.json` + `balance.json` are canonical.

**Tooling:** `tools/cascade-lint.py` — dropped `ages.json` + `towers.json` schema rows and the 11-row ages cross-file check; `civilizations.json` / `fusion-recipes.json` / `attack-types.json` / `tiers.json` checks remain authoritative.

**Untouched:** §2.4a + §5.4 [LOCKED] surfaces; 2026-04-25 locked content-skeleton names; Aztec glyph Follow-up #4 (`𓁹` Egyptian-eye in `civilizations.json` for Aztec — wrong civ; deferred to dedicated styling pass).

---

## Commits this session

- `2893943` — C6 slice 2 / Slice C — graduation cut: legacy 5-lineage / 11-age teardown. Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS trim + CASCADE pointer/version bump.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `2893943` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (decision 2026-04-27; prototype implementation across C7.a + C7.b).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape plan: COMPLETE.** Effective execution order: **C1 ✓ → C2 ✓ → C3 ✓ → C4 (slice + continuation across slices) ✓ → C5 ✓ → C7.a ✓ → C7.b ✓ → C6 slice 1 ✓ → C6 slice 2 (Bridge + Polish + Graduation) ✓**. Reshape arc closed. Polish / follow-ups remain.
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (C6 slice 2 / C6 slice 1 / C7.b). C7.a entry archived this handoff.
- `CASCADE.md` pointer: most recent block only (v0.34, C6 slice 2 LANDED); prior C6-slice-1 block archived.
- `CASCADE.md` version footer: 2 most recent bumps (v0.34 + v0.33 reference); v0.32 archived.
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#4 — Aztec glyph styling pass.** `civilizations.json` has `𓁹` (Egyptian eye) for Aztec — wrong civilization. Fix in dedicated styling pass; do not surface in silhouettes/HUD until corrected.
- **#5 — Cultural-sensitivity pass.** Hard pose-lock gate on civ silhouettes. Content-lock-gate before any pose-locked / culturally-coded art ships.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 [PROPOSAL] numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts). Especially load-bearing now that the legacy age-multiplier curve is gone — `effectiveTowerStats` collapsed to scalar `damage` / `cd`, level-only multipliers; balance-pass should validate the new flat curve.
- **C4-continuation deferred items (still owed)** — merge-preview ghosts on tower-merge hover; explicit Promote-to-T4 button surface; tower-card tier+type stamp polish. Civ-tower buy/place/attack wiring landed; UI affordances for merge/promote did not.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI surface. Queued for post-reshape polish.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

### New regression-watch (Slice C)

The graduation cut is a large surgical pass. Things to manually sanity-check next session before any new code:
- **Tutorial flow** — `TUT_TOWER_KEY = "greek_phalanx"` pin; tutorial steps 1→5 advance correctly; `selectTower` lock keeps non-phalanx unselectable until step 5.
- **Match flow** — `initMatch` no longer pre-selects a tower; verify build-set renders + tower placement still works for all 3 civs.
- **`logBalanceCurve`** — rebuilt to `80 - cheapest * 2`; verify console.table output is sane on first wave run.
- **`effectiveTowerStats`** — now reads `stat.damage` / `stat.cd` as scalars (previously `[ageIdx]`). All upgrade math should still resolve.
- **Snapshot / co-op** — `enemies[].ageIdx` field dropped from snapshot. Guests fall back to `archetypeFor(0)` for any enemy missing kind/color/accent — confirm cross-version snapshot hasn't been broken (we are pre-launch; no version compat needed, but check guest renders correctly in a quick host/guest test if PM wants).

---

## NEXT SESSION — primary directive

**No single load-bearing directive. The reshape arc is closed.** Several independent tracks are open for PM to pick from:

**Recommended option (a) — C4-continuation polish.** The merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp surfaces were deferred under `alongside-and-non-breaking` discipline and never came back. Now that legacy is gone, these UI affordances can land cleanly on the civ-tower + 4-tier shape. Smallest, most contained next step.

**Alternate (b) — Follow-up #13 balance-pass.** Slice C collapsed age-indexed damage/cd arrays to scalars. The flat curve is currently untuned. PM ratifies new [PROPOSAL] numbers; cascade-lint stays clean (no schema check); balance.json + CIV_TOWER_TIER_BASE are the editable surfaces.

**Alternate (c) — Follow-up #4 Aztec glyph fix.** Tiny scoped pass: edit `civilizations.json` to replace `𓁹` with a correct Aztec-coded glyph (or abstract placeholder pending Follow-up #5). Cultural-sensitivity gate (#5) means do NOT lock a culturally-coded glyph without PM ratification — abstract first.

**Alternate (d) — admin/concept.json migration direction.** Long-deferred. PM picks: full rewrite / regenerate / retire.

**Alternate (e) — Follow-up #6 patch-1 commanders + Thor recipe-layer dissonance.** Larger design pass.

**Cadence:** propose plan via AskUserQuestion (Recommended first) → PM "go" → produce → verify (`python tools/cascade-lint.py`) → tick. Single PM-gated step per HANDOFF protocol.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM standing directive 2026-04-28).
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** when a step would break running surfaces, add new code/files alongside legacy; surface cardinality conflicts to PM via AskUserQuestion before unilateral action. **C6 was the explicit graduation point.** Pattern remains live for any future similar reshape.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.
- **Context-pressure self-trim + scope re-gate:** when context budget tightens OR scope balloons mid-step beyond proposed delete, stop and re-gate via AskUserQuestion with slice options. Precedents: C4 slice + C7.b two-slice split + C6 two-slice split + C6 slice 2 three-sub-slice split (this multi-session arc).
- **Bias toward batched edits when context burns.** PM feedback this session: micro-step tool calls overclock the context window. Group independent edits into parallel batches when safe.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — prototype reshape arc CLOSED (C6 slice 2
graduation cut landed in commit 2893943, multi-session C6+C4-continuation
arc complete). No single primary directive — several follow-up tracks
open for PM to pick from.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: C6 slice 2 (2893943)
  dual-pushed. Legacy 5-lineage / 11-age surfaces fully retired
  (AGES global, KNOWLEDGE_PER_AGE, game.ageIdx, lineageOf/Role,
  HYBRIDS, age-banner, hybrid feed kind, --sinew/--forge/--crown/
  --veil tokens, ages.json, towers.json, lint schemas — all gone).
  Prototype runs on civ-tower + 4-tier ladder only.
- Open blockers: none load-bearing. Several independent tracks
  open: C4-continuation polish (merge-preview / Promote-T4 /
  tower-card stamp), Follow-up #13 balance-pass re-ratification
  (now critical — flat curve currently untuned post-graduation),
  Follow-up #4 Aztec glyph (𓁹 Egyptian-eye in civilizations.json
  is wrong civ; gated on cultural-sensitivity Follow-up #5),
  admin/concept.json migration direction, Follow-up #6 patch-1
  commanders + Thor recipe dissonance.
- Specific next-step proposal: surface plan via AskUserQuestion
  with Recommended first option = C4-continuation polish
  (smallest, most contained; lands cleanly on the new civ-tower
  + 4-tier shape). Alternate = Follow-up #13 balance-pass.
  Alternate = Follow-up #4 Aztec glyph (gated on #5).
  Alternate = admin/concept.json direction. Alternate =
  Follow-up #6 commanders+Thor pass.

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.
ALONGSIDE-AND-NON-BREAKING pattern remains live for any future
reshape.
BIAS toward batched edits when context burns (PM feedback
2026-05-03: micro-step tool calls overclock context window).

REGRESSION-WATCH (from Slice C graduation cut):
- Tutorial: TUT_TOWER_KEY = "greek_phalanx" pin; steps 1→5 advance.
- Match: initMatch no longer pre-selects tower; build-set renders
  + tower placement works for all 3 civs.
- logBalanceCurve: console.table output sane (rebuilt to
  cheapest*2 instead of sinew+ember refs).
- effectiveTowerStats: scalars instead of [ageIdx] arrays.
- Snapshot: enemies[].ageIdx dropped; guest renders fall back to
  archetypeFor(0) on missing kind/color/accent.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- Cultural-sensitivity Follow-up #5: hard pose-lock gate on
  any non-abstract civ art. Aztec glyph fix (Follow-up #4)
  must use abstract placeholder unless PM ratifies a culturally-
  coded replacement.
- Reshape arc is closed. Do not regress legacy lineage/age
  surfaces back into the prototype.

If PM redirects off these tracks, fall back to: cultural-
sensitivity pass scheduling (Follow-up #5), follow-ups #7/#8/#9.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock gate on any non-abstract civ art.
- A reshape step would silently break a running surface without an alongside fallback or AskUserQuestion gate.
- Scope balloons mid-step beyond the proposed delete — re-gate via AskUserQuestion with slice options before continuing.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
- Any attempt to regress the retired lineage/age surfaces (sinew/ember/forge/crown/veil; AGES; ageIdx; HYBRIDS; age-banner) back into the prototype.
