# HANDOFF — Session Checkpoint

**Last session:** 2026-04-21 (concept-pivot planning session — no docs/prototype artifacts shipped; 4 pivot questions LOCKED via PM answers; feature branch pushed to origin; stream-timeout lesson captured)
**Hand-off by:** Claude (Opus 4.7, 1M context)
**Hand-off to:** next Claude Code session (post `/clear` or cloud-session reset)

---

## TL;DR (this session)

A concept-tightening pivot was scoped in plan mode. PM answered four framing questions (all Recommended options accepted) and the pivot is now ready for Step A execution. **No concept docs or decisions were written this session** — plan mode produced the answers, not the artifacts. One repo-level action shipped: `claude/bootstrap-ata-setup-B2cJv` was pushed to origin with `-u` so cloud sessions can check it out. Multiple stream idle timeouts over-long turns forced a cadence shift: **next session executes Step A one file per turn** (no batched multi-file writes, no piggybacked reads).

**Working tree is clean at `a6c6114` = origin/main = origin/claude/bootstrap-ata-setup-B2cJv.** Nothing was committed this session.

**Next-session agenda:** Execute Step A — concept docs pivot (12 sub-steps A1..A12), one file per turn. See the fenced prompt at the bottom of this doc.

---

## Pivot — LOCKED PM answers (do NOT re-ask)

| # | Question | PM answer |
|---|----------|-----------|
| 1 | §5.4 naming conventions [LOCKED] vs. Ash / Nature / Prayer | **Defer naming pass.** Ratify structure now; §5.4 UNTOUCHED. Ash / Nature / Prayer are thematic shorthand in prose only until a later naming-pass decision. |
| 2 | Tier conceptual frame (civilization-arc vs. dungeon-cosmology) | **Dungeon cosmology.** Replace 11 civilizational ages with 3 tiers expressing an Ash→Altar arc. Placeholder tier names: **Dust / Form / Apotheosis**. |
| 3 | Hybrid mechanical model | **Ash as hybrid-enabler.** Only Ash×Nature and Ash×Prayer hybridize. Nature×Prayer does NOT hybridize. Two hybrid families. |
| 4 | Pivot timing | **Docs first, prototype after, playtest after.** Step A = concept docs pivot (this next session). Step B = prototype reshape (separate PM-gated pass). Step C = Step 5 playtest on reshaped prototype. |

**Also locked this session:** world aesthetic is **dungeon-like and mysterious** (PM direct quote). Reinforces §5.3 silhouette-forward mythic art direction — already the leading candidate; now load-bearing.

**Also implied but separate pass:** "Ash to Altar" title becomes thematically load-bearing (currently `working-title-only` per README). Not a name-lock, but the Ash↔Altar arc is now the thematic spine. Title lock stays deferred.

---

## State snapshot

### Git
- Branch in use: **`claude/bootstrap-ata-setup-B2cJv`** (pushed to origin this session; tracks `origin/claude/bootstrap-ata-setup-B2cJv`).
- Working tree clean.
- `main` local tracks `origin/main` at `a6c6114` — same SHA.
- No divergence; no unpushed commits; nothing to PR (no commits beyond main yet).

### Artifacts delta this session
- **Zero** concept-doc edits, decision entries, or prototype changes.
- One remote action: `git push -u origin claude/bootstrap-ata-setup-B2cJv`.
- One plan-file that the PM exited out of before it was written (`/root/.claude/plans/i-think-we-need-stateful-fog.md` — never created; see Follow-ups).

### Docs state (unchanged from 2026-04-20 HANDOFF)
- CONCEPT.md v0.5 (hub), concept/phase-*.md unchanged.
- CONCEPT-GAPS.md v0.3 — 11 un-migrated rows remain.
- CASCADE.md v0.13 — pointer still on "2026-04-20 Meta-UI + DNA pass LANDED."
- PROGRESS.md — Step 5 is still first unchecked.
- HANDOFF.md — this rewrite.

### Research / prototype
- Two Explore agents mapped the pivot reopen surface in depth this session (results are in this session's transcript; next session can re-run if needed — they took ~3min each). Summary carried into the A1..A12 plan below.
- Prototype untouched.
- cascade-lint still clean per prior session.

---

## Open threads / carried debts

### From prior HANDOFF (2026-04-20) — still open
- Step 5 playtest gate (now explicitly sequenced AFTER Step B prototype reshape).
- 11 CONCEPT-GAPS rows remain (separate PM-gated workstream).
- Biome-select chip UI + per-commander signature wiring — both will be re-scoped under the 3-lineage model.
- Balance watchpoint (commander aura <40% wave-6 coverage auto-widen) — reconsider under new aesthetic.
- Two-browser live co-op smoke — still deferred.
- Freeze date: **2026-05-15**.

### New from this session
- **Naming pass is deferred.** A future decision must either (a) reopen §5.4 to allow 1–2 syllable ancient nouns, or (b) pick §5.4-compliant one-syllable placeholders (e.g., Ash / Loam / Vow). Until then, Ash / Nature / Prayer live as prose shorthand only — the 3-lineage structure is what's being ratified, not the names.
- **Decision entry `2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md` is not yet filed.** Step A1 writes it.
- **3 existing decisions will be partially rebased (not superseded):**
  - `2026-04-20-commander-identity-floor.md` — floor shape survives; scope narrows 5→3 commanders.
  - `2026-04-20-age-history-flavor-mapmods.md` — age-gate logic survives; ages.json collapses 11→3.
  - `2026-04-20-commander-pick-identity-upgrade.md` — silhouette-test logic survives; roster collapses 5→3.
  - Each gets a "rebased by 2026-04-21-concept-tightening..." note, not a Superseded status.
- **Stream-timeout lesson:** long turns with multiple tool calls or large outputs time out over cellular. Cadence: one file per turn, one tool call per turn where possible.

---

## Do NOT touch in Step A (docs-only pass)

- Any `prototype/` file (that's Step B).
- `tools/cascade-lint.py` logic (current assertions still pass against current prototype data — no changes needed until Step B).
- `admin/concept.json` (PM's structured edit surface; regenerate from the editor post-Step A).
- **`concept/phase-5.md` §5.4 naming conventions [LOCKED].** This is the one locked item in the cascade and the PM explicitly deferred reopening it.

---

## Next-session prompt (copy-paste after `/clear` or fresh cloud session)

Step sequence + per-step specs now live canonically in [`PROGRESS.md`](PROGRESS.md) §Step A. This prompt only routes the session there — no duplicated list.

```
Resuming Ash to Altar concept pivot. Branch: claude/bootstrap-ata-setup-B2cJv.

Bootstrap per CLAUDE.md (README.md -> CLAUDE.md -> CASCADE.md -> HANDOFF.md
-> PROGRESS.md -> CONCEPT.md). State aloud, then wait for "go".

CADENCE: ONE FILE PER TURN. Announce the file, write it, stop. Retry on
timeout (writes idempotent). Split Edit in half if same file times out twice.

Pivot context (4 locked PM answers + aesthetic lock + do-not-touch list):
HANDOFF.md §Pivot and §Do NOT touch.

Step sequence + one-line specs: PROGRESS.md §Step A.
Execute the first unchecked row; stop after each for PM verify + tick.

After A12, stop. Do NOT start Step B. Ask PM to ratify.
```

---

## Escalation triggers

Hard-stop and flag if, during Step A:

- Any prose edit silently modifies §5.4 (the one [LOCKED] item). Flag and revert.
- `cascade-lint` fails after A11 and fix takes >10 min → stop, report, do not commit.
- Any of the 4 locked PM answers above appears to conflict with a prior [LOCKED] constraint you did not anticipate → stop, surface the conflict, do not paper over.
- You realize Step A needs a prototype-layer touch to validate the prose → stop, note it as a Step B input, do not reach into `prototype/`.
- You draft the decision entry and the 3x debug loop Loop 1 critique is devastating → stop, surface it, do not rubber-stamp.

---

*End of HANDOFF — 2026-04-21. Branch pushed to origin. Pivot answers locked. Step A ready. Next session: one file per turn.*
