# HANDOFF — Session Checkpoint

**Last session:** 2026-04-25 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7, post-compaction)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-tower authoring sub-pass: R1 + R2 + R3 + R4 LANDED. RN remains.** This session produced R2 (Greek), R3 (Aztec), and R4 (Norse) rosters autonomously per PM autonomy mandate; all committed and dual-pushed. R2 at `04efad6`, R3 at `abe8e9a`, R4 at `9e5b332`. All three author 15 towers × the locked 7-field schema (`attack_type` / `cd` / `range` / `status_proc` / `dps` / `aux_slot_compat` / `notes`) with civ-identity-hook prose + per-tier reading + cross-arc parity hook. **All three falsifiable per-civ magnitude signatures empirically confirmed:** Greek Control = dps-centered/cd-1.7s/range-4.0/lockdown-procs; Aztec Economy = dps-band-high-T2-T3-and-God-tier/cd-1.4s/range-4.0/Poison-stack-Fire-splash-Slashing-bleed-rich; Norse Summon = dps-centered/cd-1.15s-fastest/range-3.5-shortest/Bleed-density-6-of-15-densest. All 45 attack_types verbatim-confirm 2026-04-26 mapping; all 45 dps within ±20% of 2026-05-05 R5 baseline ladder; all lane-tags clean (`controlled_by: leonidas` × 15 / `economy_target: montezuma_ii` × 15 / `summon_anchor: ragnar` × 15). cascade-lint clean every round (pre-existing phase-4 626/600 soft-cap carried). NEXT session opens at **RN — closing audit + spine-doc edits + arc close**.

---

## NEXT SESSION — primary directive

**Produce RN — cross-civ × cross-tier audit + spine-doc edits + arc close — autonomously.** PM autonomy mandate continues to apply. RN is the largest round of the arc (audit table + multiple §4 spine-doc edits + exit-gate tick), so consider mid-round mini-handoffs if context tightens. Surface AskUserQuestion ONLY on:

- Cascade-violation discovered by audit (any of 45 towers actually outside locked bands; any lane-tag cross-civ pollution).
- Spine-doc-edit scope expansion beyond what per-commander R5 deferred (i.e., §4.1 / §4.11.6 / §4.8 are in-scope; other §4.x sections are NOT in-scope without explicit PM go).
- Cultural-sensitivity surface (Follow-up #5 — art / VFX / civ-flavor surface direction prose).
- Handoff trigger.

### RN deliverable shape

**Two artifacts:**

**Artifact 1 — `decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`** (Accepted, Medium):
1. **Cross-civ × cross-tier audit table** — 45-tower matrix (3 civs × 5 tiers, with T1/T2/T3 collapsed per merge-progression model) sanity-checking dps-ladder ±20% adherence + cd/range bands + status-proc kind locks + lane-tag distribution. One row per tower, columns: civ / tower / tier / attack_type / cd / range / status_proc kind / dps / aux compat / lane-tag.
2. **Per-civ signature confirmation summary** — explicit pass/fail audit on the three falsifiable signatures committed at R2/R3/R4. Format: predicted vs delivered, with quantitative comparison (median cd, median range, dps-cluster-direction, status-proc-density). Expected: all three pass.
3. **Cross-civ band snapshot** — final locked numbers: dps medians per tier per civ; cd medians per tier per civ; range medians per tier per civ; Slashing-Bleed source counts; Poison source counts (Aztec only); Divine source counts; type-coverage gaps per civ.
4. **3x debug loop** on the arc as a whole (does the per-tower schema legibly express three orthogonal civ-archetypes from one underlying ladder, or has the schema collapsed under the weight?).
5. **Closes the per-tower authoring arc** — followups list: per-civ specialization (next major track) / per-map authoring / Phase 4 exit-gate item #2 ticked.

**Artifact 2 — Spine-doc edits to `concept/phase-4.md`** (per per-commander R5 deferral):
- **§4.1 mechanical-content rewrite** — anointed-tower aura model + active-cast-vs-passive-aura distinction + summon-cap signature-window exception language. Source: per-commander R5 close (`decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md`) "Spine-doc edits specified" block.
- **§4.11.6 deferral removal** — slow-soft-cap section had a deferral marker pending per-commander R5; per-commander R5 closed; remove deferral marker.
- **§4.8 exit-gate item #2 tick** — per-tower spec table populated for all 45 launch towers (R2 Greek + R3 Aztec + R4 Norse rosters cumulatively); tick this item, leaving phase-4 exit gate showing items #1 + #2 closed.

**Phase 4 line-cap discipline**: file is currently 626/600 (carried soft-cap). Spine-doc edits should aim for net-neutral or net-shrink, NOT net-grow. If the §4.1 rewrite naturally extends, identify a §4.x section to compress in compensation, OR flag the line-cap breach for PM ratification before committing.

### Step-by-step procedure

1. **Bootstrap** per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.
2. `git fetch origin && git log --oneline HEAD..origin/main` (expect clean — last R4 push was `9e5b332` to both session branch + main).
3. **Read inputs** (Grep > full-file Read where possible):
   - [`decisions/2026-05-06-per-tower-authoring-scope.md`](decisions/2026-05-06-per-tower-authoring-scope.md) — round queue + schema lock + guards (R1 scope).
   - [`decisions/2026-05-06-per-tower-r2-greek-roster.md`](decisions/2026-05-06-per-tower-r2-greek-roster.md) — Greek 15-tower table + signature.
   - [`decisions/2026-05-06-per-tower-r3-aztec-roster.md`](decisions/2026-05-06-per-tower-r3-aztec-roster.md) — Aztec 15-tower table + signature.
   - [`decisions/2026-05-06-per-tower-r4-norse-roster.md`](decisions/2026-05-06-per-tower-r4-norse-roster.md) — Norse 15-tower table + signature.
   - [`decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md`](decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md) — spine-doc-edits-specified block, anointed-tower model, summon-cap exception language.
   - [`concept/phase-4.md`](concept/phase-4.md) §4.1 / §4.11.6 / §4.8 — current state for editing.
4. **Author RN audit decision file** (Artifact 1 above).
5. **Edit phase-4.md** (§4.1 rewrite / §4.11.6 deferral removal / §4.8 exit-gate tick) per per-commander R5 deferral. Watch line-cap (currently 626/600).
6. **Cascade-lint:** `python tools/cascade-lint.py` — expect clean OR reduced finding-set.
7. **Add CASCADE.md decisions-table row** for RN (lint will flag if missing).
8. **Update CASCADE.md current-work pointer** — close the per-tower authoring sub-pass; flip pointer forward to next-track pick (per-civ specialization / per-map authoring / etc.).
9. **Commit RN + spine-doc edits + CASCADE updates** in one commit. Dual-push (session branch + main).
10. **Mini-handoff and stop.** RN closes the arc; the next session is a fresh-track pick.

### Discipline (carry forward)

- **No game code edits.** Concept-only — Phase 4 hasn't exited.
- **No spine-doc edits during R2/R3/R4.** All `phase-4.md §4.x` body edits + `§4.8` exit-gate tick happen at RN.
- **3x debug loop** inline on any decision that touches CONCEPT constraints — but R2/R3/R4 are *populating* a locked schema, not deciding new constraints, so loops are unlikely to fire unless a tower deviates from the bands.
- **Dual-push every commit.** Push to session branch AND `main`.
- **Cascade-lint after every round.**

---

## What is locked (clear-safe)

### Carried forward (untouched this session)

- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure (Tribute kill-only + Divinity 6-source 4-floor+2-escalation; 6-cap discipline) — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton — Accepted.
- §5.4 [LOCKED] (Civilizations row).
- §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, Hard reversibility) — Accepted.
- Splash-fix `CODEX_DATA` rename — Accepted.
- All Phase C UI-verification-sweep fixes (`5d2f3c8` / `8f67a08` / `4964895` / `abcb398`) — Accepted.

### NEW this session (R1 scope)

- **Per-tower authoring R1 scope** LANDED via `decisions/2026-05-06-per-tower-authoring-scope.md` (Accepted, Medium). Round queue + axis + 7-field schema + hard guards locked.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit (pre-handoff): `8d8550f` (chore handoff doc-hygiene from Phase C). R1 scope file + handoff bundle staged for this turn's chore commit. Will dual-push.
- Working tree at handoff: `decisions/2026-05-06-per-tower-authoring-scope.md` new + CASCADE.md + CASCADE-history.md + PROGRESS.md + PROGRESS-archive.md + HANDOFF.md modified. `.accord/` untracked (carried).

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most-recent entries (R1 scope / Phase C / Phase B). Phase A entry archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (R1 scope LANDED). Prior pointer (Phase C LANDED) archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.66 + 0.65. 0.64 archived to `CASCADE-history.md`.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 626/600 soft-cap (carried — not introduced by this handoff).

### Two prototype findings still queued (not in scope for this arc)

These are independent of the per-tower arc and remain queued from Phase C close. Pick up on a context-budget-friendly side-pass *between* per-tower rounds if PM directs, else they wait until the per-tower arc closes.

- **(a) `openReference` CIVS_DATA bug** — `prototype/index.html` ln 3310 throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy. Pre-existing.
- **(b) Mode-select copy obsolete** — `prototype/index.html` ln 495 / 507 / 513 still references "three ages" / "11-age arc solo". Obsolete under post-2026-04-25 4-tier ladder.

### Open follow-ups (carried — UNCHANGED)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art + VFX + civ-flavor surface direction). **Hard-gates per-tower arc visual prose** (this arc is mechanical-content only).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Post-arc roadmap (preserve)

1. **Per-civ specialization** — Greek/Aztec/Norse identity profiles (matchup affinities, identity hooks, signature creep types). Intersects Follow-up #5.
2. **Per-map / Round 11** — good-cell authoring + wave-randomization + crystal-lock variance per §4.7 R11 mandate.
3. **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave variance per §4.7 R11.
4. **`research/06-tw-subgenres.md`** new stub.
5. **`admin/concept.json`** migration.
6. **Follow-ups** #5 / #6 / #7 / #8 / #9 + C7.b deferred.

### Regression-watch (carried from Phase C)

- End-screen XP persist (Phase C #8) — re-verify on a fresh skirmish if any code touches `endMatch` ln 3390-3408.
- Match keybinds (Phase C #6) — re-verify after a rebind round-trip if any code touches the `Profile.setting("input.binds")` resolver.
- Tutorial Esc dismissal (Phase B carry).
- Profile scene roster (Phase B carry).
- End-screen layout post-Highest-Age row removal (Phase B carry).
- `menu-last` resolution path (Phase B carry).

---

## Cadence rules carried forward (project-level)

- **Cadence exists to manage the context window, not to gate every step.**
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously. See `feedback_autonomy_mandate.md` in user memory.
- **AskUserQuestion is the standard interface** when gating is needed. Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3, CASCADE pointer to 1 block, footer to 2.
- **Preview MCP cadence:** prefer `preview_eval` for state probes over `preview_screenshot` (cheaper, deterministic). Screenshot only when visual layout is the question. **N/A this arc — no prototype work.**

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Per-tower authoring sub-pass OPENED on 2026-05-06.
R1 scope decision LANDED at decisions/2026-05-06-per-tower-authoring-scope.md
(Accepted, Medium). PM picked Recommended on both AskUserQuestion gates:
Axis A (per-civ across tiers) + 7-field schema lock.

4-round queue locked:
  R1 (DONE) — scope decision + 3x debug loop + schema lock
  R2       — Greek roster: 15 towers × 7 fields + civ-identity-hook prose
            + per-tier reading + Leonidas controlled_by interface bind
  R3       — Aztec roster: 15 towers × 7 fields + Montezuma II
            economy_target interface bind
  R4       — Norse roster: 15 towers × 7 fields + Ragnar summon_anchor
            interface bind
  RN       — cross-civ × cross-tier audit + phase-4.md §4.x per-tower
            spec body + §4.8 exit-gate item #2 tick

7-field schema (LOCKED for the arc):
  attack_type (verbatim-confirms 2026-04-26 mapping)
  cd          (§4.10 (g) / ±20% tier band)
  range       (§4.10 (j) / ε=0.6 default)
  status_proc (2026-04-26 status-proc table — kind locked)
  dps         (2026-05-05 R5 ladder T1=20/T2=60/T3=180/T4=540/God=1080 ±20%)
  aux_slot_compat (§4.6a 7-slot universal default)
  notes       (civ-identity hook + per-commander affinity-target tag)

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — produce R2 (Greek roster) AUTONOMOUSLY per the
PM autonomy mandate carried forward from 2026-05-05 Numbers-phase /
CONCEPT-amendment-pass / per-commander arc precedent.

Surface AskUserQuestion ONLY on:
  - Genuine forks not anticipated in R1 scope.
  - Scope expansion beyond the locked 4-round queue.
  - Cascade-violation risk (attack_type deviating from 2026-04-26;
    dps beyond ±20% of 2026-05-05 R5 baseline; per-commander
    affinity-target tag crossing civ lanes).
  - Cultural-sensitivity surface (Follow-up #5 — art / VFX / civ-
    flavor surface direction prose).
  - Handoff trigger.

R2 INPUTS (Grep > full-file Read where possible):
  decisions/2026-05-06-per-tower-authoring-scope.md
  decisions/2026-04-26-attack-type-mapping.md
  decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md
  decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md
  concept/phase-4.md  (§4.6 / §4.6a / §4.10 / §4.11)
  concept/phase-3.md  (locked Greek tower content-skeleton names)

R2 DELIVERABLE:
  decisions/2026-05-06-per-tower-r2-greek-roster.md (Accepted, Medium)
  - 15-row table (6 T1-T3 + 6 T4 Demigod + 3 God) × 7 fields
  - Civ-identity-hook prose (Greek lockdown / control archetype)
  - Per-commander affinity-target tags binding Leonidas controlled_by
  - Per-tier reading at close (T1 / T2 / T3 / T4 / God paragraphs)
  - Cross-arc parity hook → R3 Aztec / R4 Norse / RN audit

R2 PROCEDURE:
  1. Read inputs.
  2. Author 15 Greek tower rows in locked 7-field schema.
  3. Cascade-lint: python tools/cascade-lint.py
     (expect clean except pre-existing phase-4 soft-cap 626/600)
  4. Commit R2 + dual-push (session branch + main).
  5. Continue to R3 (Aztec) autonomously if context budget healthy.
     Otherwise stop after R2 and file mini-handoff.

DUAL-PUSH POINTS (locked from R1 scope):
  After R2 (carries R2)
  After R3 (carries R3)
  After RN (carries R4 + RN; CLOSES arc)

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 content-skeleton names
  verbatim untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits Accepted.
- Effect-type lane locks (Greek=Control / Aztec=Economy / Norse=Summon)
  Hard reversibility — every per-tower notes affinity-target tag
  resolves cleanly to one of these three lanes.
- 2026-04-26 attack-type lock — every attack_type column verbatim-
  confirms the locked mapping.
- 2026-05-05 R5 baseline DPS ±20% band — every per-tower dps within
  band; out-of-band magnitude requires cascade-violation flag.
- Cultural-sensitivity Follow-up #5 hard-gates non-abstract civ art /
  VFX / civ-flavor surface direction. This arc is mechanical-content
  only — civ-neutral effect-type language throughout.

NO GAME CODE EDITS. Concept-only — Phase 4 hasn't exited.
NO SPINE-DOC EDITS during R2/R3/R4. All phase-4.md §4.x body edits
  + §4.8 exit-gate tick happen at RN.

VERIFY each commit with: python tools/cascade-lint.py
  (expect clean except pre-existing phase-4 soft-cap 626/600)
DUAL-PUSH each commit: session branch + main.

POST-ARC ROADMAP (preserve, deferred until RN closes):
1. Per-civ specialization (Greek/Aztec/Norse identity profiles;
   Follow-up #5 gate).
2. Per-map / Round 11 (wave-randomization + crystal-lock + good-cell).
3. Phase 5 readiness gate (telemetry + wave variance).
4. research/06-tw-subgenres.md.
5. admin/concept.json migration.
6. Follow-ups #5/#6/#7/#8/#9 + C7.b deferred items.

TWO PROTOTYPE FINDINGS STILL QUEUED (independent of this arc;
side-pass between rounds only if PM directs):
  (a) prototype/index.html ln 3310 openReference CIVS_DATA undefined
      ReferenceError when game.commander.civ is falsy.
  (b) prototype/index.html ln 495/507/513 mode-select copy obsolete
      "three ages"/"11-age arc" — post-2026-04-25 4-tier ladder.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails new (pre-existing phase-4 soft-cap is carried).
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned.
- Any amendment-pass §-anchor would be silently edited.
- Any per-commander R1-R5 spine-doc surface would be silently edited.
- Any per-tower `attack_type` deviates from 2026-04-26 mapping.
- Any per-tower `dps` falls outside ±20% of the 2026-05-05 R5 baseline.
- Any per-commander affinity-target tag crosses civ lanes.
- A track touching CONCEPT constraints lands without 3x debug loop.
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
