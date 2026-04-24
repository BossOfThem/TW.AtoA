# Decision — Step B: Prototype Reshape Plan (3/3/3 cascade into prototype)

**Date:** 2026-04-22
**Status:** Superseded by [`2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md`](2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) (2026-04-24 — Phase 1 reopen voids the 3/3/3 shape this plan migrates toward; 18 sub-steps unreachable; any prototype reshape is downstream of Phase 1 exit under the new direction)
**Reversibility:** Medium
**Affects:** `prototype/data/*.json` (all 7 files), `tools/cascade-lint.py`, `prototype/index.html`, `prototype/COVERAGE.md`, `prototype/PORT-NOTES.md`, `prototype/README.md`, `prototype/CLICK-BUDGET.md`

---

## Decision

Execute a data-and-scenes reshape pass on the prototype so it reflects the ratified 3/3/3 shape (3 lineages Ash/Nature/Prayer, 3 tiers Dust/Form/Apotheosis, 3 commanders, Ash-enabler hybrids). Proceed one file per turn in the sequence below. Step B gates Step 5 (playtest). Freeze 2026-05-15.

**Does not touch:** `concept/` docs, `§5.4 [LOCKED]`, `§2.4a [LOCKED]`, `admin/concept.json`, any accessibility-floor behavior.

---

## Sub-step sequence

| Sub-step | File | Scope |
|----------|------|-------|
| B1 | `tools/cascade-lint.py` | Relax `check_prototype_data()` cardinality asserts to accept transitional state (3-tier **or** 11-age, 3-cmdr **or** 5-cmdr). Keeps lint green during migration. |
| B2 | `prototype/data/ages.json` | Repopulate 11-entry age rows → 3 tier entries (Dust / Form / Apotheosis prose placeholders). Preserve field names (`eraDescriptor`, `color`, `motif`, `lore`). Filename kept as `ages.json` — alias comment added; rename is deferred to Godot port. |
| B3 | `prototype/data/towers.json` | Collapse 5-lineage × 11-age = 55 rows → 3-lineage × 3-tier = 9 base archetypes + 2 hybrid families (Ash×Nature, Ash×Prayer per Ash-enabler model). Nature×Prayer does **not** hybridize. §5.4-compliant single-syllable placeholder names. |
| B4 | `prototype/data/commanders.json` | 5 → 3 commanders (A/B/C, one per lineage Ash/Nature/Prayer). Each must honor the identity floor: portrait, silhouette slug, 12 VO lines [PROPOSAL], signature, passive, lineage tilt, 20-level ladder, 3 cosmetic slots. Numbers remain [PROPOSAL]. |
| B5 | `prototype/data/enemies.json` | Re-tier archetypes: per-tier group (Dust / Form / Apotheosis) rather than per-age. Keep `kind` field (swarmer/infantry/heavy/ranged/elite/boss) — used by renderer. |
| B6 | `prototype/data/mapmods.json` | Re-tier biome tags from 11-age rotation to 3-tier assignment. 6 biomes [PROPOSAL] survive; re-key by tier. |
| B7 | `prototype/data/events.json` | Re-weight 8 events under 3-lineage / 3-tier shape. Remove Sinew/Ember/Forge/Crown/Veil lineage references; substitute Ash/Nature/Prayer prose placeholders. |
| B8 | `prototype/data/balance.json` | Adjust any `ages` / `tiers` / lineage-count references in sub-objects (coop / multiplayer / save / progression / accessibility). |
| B9 | `tools/cascade-lint.py` | Tighten cardinality asserts back to strict 3-tier + 3-commander after all data files migrated. |
| B10 | `prototype/index.html` — commander-pick scene | 5 roster chips → 3. Silhouette slugs match new B4 commanders. XP ladder and cosmetic ticks survive. |
| B11 | `prototype/index.html` — tower-button row | 5 lineage buttons → 3 (Ash/Nature/Prayer) + adjacent hybrid hint under Ash-enabler logic. |
| B12 | `prototype/index.html` — tier labels + age→tier terminology | `AGES_DATA` reads, age-up button, tier-gate banner, autoAgeUp toggle reference. Sweep: "age" → "tier" in UI strings only (not in `ages.json` file reference until rename). |
| B13 | `prototype/index.html` — enemy renderer + silhouette-test | `kind`-keyed silhouette switch survives; ensure 3-tier enemy lookup works. Silhouette-test Shift+S still covers 3 commanders. |
| B14 | `prototype/COVERAGE.md` | Re-matrix CONCEPT × prototype coverage under 3/3/3. Update top-5 Step-4 targets row. |
| B15 | `prototype/PORT-NOTES.md` | Remove 5-lineage / 11-age idiom rows; add 3-lineage / 3-tier Godot mapping notes where applicable. |
| B16 | `prototype/README.md` | Changelog v2 → v3. Update scene table and Co-op Horde instructions for 3-commander roster. |
| B17 | `prototype/CLICK-BUDGET.md` | Verify 4-click first-time / 2-click returning budget still holds with 3-commander roster (expect no change; document confirmation). |
| B18 | `PROGRESS.md` + `HANDOFF.md` | Session-log entry for Step B landed; HANDOFF addendum; CASCADE pointer bump + doc-version bump. |

**Estimated turns:** 18, one file per turn. Sessions can pause mid-sequence; each turn is independently committed and pushed.

---

## Context

The prototype was built against the prior 5-lineage / 11-age / 5-commander shape. The 2026-04-21 concept tightening (Reversibility Hard) ratified 3/3/3. The prototype is currently playtest-blocking because a PM playtest against mismatched data would surface false signal (wrong choices, wrong matchup, wrong economy numbers). Step B aligns the prototype to the ratified shape so Step 5 produces valid data.

`tools/cascade-lint.py check_prototype_data()` currently asserts 11-age cardinality + 5 playable commanders. B1 relaxes then B9 re-tightens — lint stays green throughout.

---

## Alternatives considered

- **Option A — Migrate all 7 data files in one turn.** Rejected: violates one-file-per-turn cadence; high stream-timeout risk given file sizes.
- **Option B — Migrate data + update index.html in one pass.** Rejected: index.html is ~3000+ lines; any pass that touches both data schema and renderer in one commit is hard to review and prone to half-finished state on timeout.
- **Option C — Sequence as above: relax lint → migrate data → retighten lint → scenes → docs.** (Chosen.) Lint green throughout; each turn is independently reviewable; index.html split into 4 targeted passes so no turn is unbounded.

---

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- Keeping `ages.json` filename is confusing — readers in 6 months won't know it holds tiers.
- Splitting index.html into 4 passes (B10–B13) still requires reading 3000+ lines per pass to find the right region — risky for partial edits.
- B18 (PROGRESS + HANDOFF) is two files, not one — violates cadence.
- Lint relaxation window (B1 through B8) masks real schema errors if a data file is malformed — the transitional tolerance could let a bad file slip through undetected until B9.

**Loop 2 — steelman.**
- `ages.json` rename is not in scope for a prototype-reshape pass; the concern is real but it belongs in PORT-NOTES as a deferred rename note (already consistent with "port findings, not code" discipline). Adding a `_comment` field is sufficient.
- Splitting index.html into 4 targeted passes is correct because each pass owns a distinct region (commander-pick scene, tower row, tier labels, enemy/silhouette) — they do not cross-contaminate. The regions are identifiable by search before editing.
- B18 two-file exception is a close-session housekeeping turn, not a content turn — PROGRESS + HANDOFF are always co-edited at close. Acceptable as one turn.
- Lint relaxation window risk is mitigated by running lint after every data-file turn (already the per-turn discipline). A malformed file shows up in JSON parse failures at data-load, not hidden by cardinality relaxation.

**Loop 3 — synthesis.**
Plan proceeds as specified. Two additions: (1) add `_comment: "file name is ages.json legacy; contents are 3 tiers pending rename at Godot port"` to `ages.json` in B2; (2) lint must be run and reported clean after every turn (already the cadence — stated explicitly here as acceptance criterion).

---

## Acceptance criteria (per sub-step)

Each turn done when:
1. Target file saved, `cascade-lint` reports `clean`, commit pushed to session branch + main.
2. Prototype loads without JS console errors (for data turns: `python -m http.server 8765` + open).
3. For index.html turns: target scene renders correctly with new data (observed in browser).

Step B complete when B18 is ticked and cascade-lint reports `clean. next-open-step: Step 5`.

---

## Reversibility note

Medium. Each data file can be restored from git. index.html edits are reversible per commit. The only irreversible aspect is that `ages.json` content is overwritten — git history preserves the 11-age shape if needed.

---

## Follow-ups

- Step 5 (playtest) is unblocked once B18 is ticked.
- `gp.autoAgeUp` → `gp.autoTierUp` identifier rename is deferred to Godot port, not this pass.
- `ages.json` → `tiers.json` file rename deferred to Godot port.
- Silhouette SVG paths for 3 commanders (replacing 5) are placeholder — final poses TBD under the deferred naming pass.
- After Step 5, the 11 remaining CONCEPT-GAPS rows become the next PM-gated workstream.
