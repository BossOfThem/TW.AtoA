# HANDOFF — Session Checkpoint

**Last session:** 2026-05-06.
**Hand-off by:** Claude (Opus 4.7, post-compaction continuation — R3 produced after summary resume).
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-civ R3 (Aztec profile) LANDED** — [`decisions/2026-05-06-per-civ-r3-aztec-profile.md`](decisions/2026-05-06-per-civ-r3-aztec-profile.md) (Accepted, Medium; commit `7c3f338`, dual-pushed). 5-field profile bound; identity_hook 3x debug ran; cross-civ parity reconciliation paragraph corrects R2's Aztec-vs-Unarmored / Aztec-vs-Shielded forward-projection (bins inverted under direct aggregation against locked 2026-04-26 RPS — Piercing is neutral, not unfavorable, vs Unarmored); pattern "Beast/Spirit specialist + Crushing-hole + kill-multiplication identity" substantively confirmed; → R4 Norse hook. Hard guards verified. Cultural-sensitivity Follow-up #5 vigilance held (Aztec heaviest cultural-load center). Cascade-lint clean except pre-existing phase-4 soft-cap (629/600, carried).

**This session also landed a doc-hygiene refactor** (commit pending) — CASCADE pointer + decisions-table + footer compressed; HANDOFF de-duplicated; PROGRESS log compressed; Stages + Research tables moved to [`CASCADE-tables.md`](CASCADE-tables.md). Bootstrap chain dropped from ~127K to ~35-40K chars without loss of fidelity (full content lives in decision files). New compression standard documented in [`CLAUDE.md`](CLAUDE.md) Doc hygiene.

**NEXT session: produce R4 Norse profile autonomously per PM autonomy mandate.**

---

## State snapshot

### Git
- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commits: doc-hygiene bundle (pending push) → `7c3f338` (R3 LANDED) → `78cba67` (cleanup: untrack `.accord/`) → `49c4c54` (R2 LANDED).
- **Carried git debt:** `49c4c54` contains 69MB `.accord/events.jsonl` blob (>50MB GitHub warning). Removing requires destructive force-push — only on explicit PM authorization.

### Doc-hygiene
- All bootstrap docs now follow new compression standard (see [`CLAUDE.md`](CLAUDE.md) Doc hygiene).
- `PROGRESS.md` session log: 3 most-recent entries; older archived to [`PROGRESS-archive.md`](PROGRESS-archive.md).
- `CASCADE.md` pointer: 1 most-recent block; older archived to [`CASCADE-history.md`](CASCADE-history.md).
- `CASCADE.md` version footer: 2 most-recent entries; older archived to [`CASCADE-history.md`](CASCADE-history.md).
- cascade-lint clean except pre-existing `concept/phase-4.md` 629/600 soft-cap (carried — not introduced by this handoff).

### Locked carry-forward (untouched this session)
- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton — Accepted.
- §5.4 [LOCKED] (Civilizations row); §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, **Hard reversibility**) — Accepted.
- All per-tower R1-RN magnitude matrix + 4 locks (45/45 zero cascade-violations) — Accepted.
- Per-civ R1 scope + R2 Greek profile + R3 Aztec profile — Accepted.

### Two prototype findings still queued (not in scope for this arc)
- **(a)** `prototype/index.html:3310` — `openReference` throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy.
- **(b)** `prototype/index.html:495,507,513` — mode-select copy still references "three ages" / "11-age arc". Obsolete under post-2026-04-25 4-tier ladder.

### Open follow-ups
- **#5** — Cultural-sensitivity pass. Hard-gates non-abstract civ art / VFX / civ-flavor surface. **High-vigilance at Aztec.**
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Post-arc roadmap (deferred until per-civ RN closes)
1. Per-map / Round 11 (good-cell + wave-randomization + crystal-lock variance per §4.7 R11).
2. §4.4 mobile unit control (Phase 4 OPEN BLOCKER).
3. §4.7 enemy direction lock (Option C hybrid leading).
4. Phase 4 numerics ratification (Fusion + §4.6 economy).
5. Monetization specifics / engine choice lock / art director scope.
6. Phase 5 readiness gate (telemetry + wave variance).
7. `research/06-tw-subgenres.md` / `admin/concept.json` migration.
8. Follow-ups #5/#6/#7/#8/#9 + C7.b deferred.

---

## Cadence rules carried forward

- Cadence exists to manage the context window, not to gate every step.
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously. See `feedback_autonomy_mandate.md` in user memory.
- AskUserQuestion is the standard interface when gating is needed. Recommended-first.
- MD-first preservation — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions.
- Dual-push discipline — push to BOTH session branch AND `main` after every commit.
- **Targeted `git add` only** — never `git add -A`.
- Local-main hygiene — `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- 3x debug loop on any CONCEPT-constraint-touching proposal.
- Doc hygiene per new compression standard in [`CLAUDE.md`](CLAUDE.md) — round summaries are 1-line hooks in CASCADE/PROGRESS; full content lives in the decision file only.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Per-civ specialization sub-pass IN PROGRESS.
R1 scope LANDED at b0d7841. R2 Greek LANDED at 49c4c54 (+ cleanup
78cba67 untracking .accord/). R3 Aztec LANDED at 7c3f338. Doc-hygiene
refactor LANDED [pending-commit-sha]. All dual-pushed.

R3 deliverable: decisions/2026-05-06-per-civ-r3-aztec-profile.md
(Accepted, Medium). 5 fields bound; identity_hook 3x debug ran; cross-
civ parity reconciliation corrects R2's Aztec-vs-Unarmored=WEAK /
Aztec-vs-Shielded=NEUTRAL forward-projection (bins invert to STRONG/
WEAK under direct aggregation against locked 2026-04-26 RPS); → R4
Norse hook embedded.

KNOWN GIT DEBT (carried): commit 49c4c54 has 69MB .accord/events.jsonl
blob in history. Cleanup 78cba67 removes from tracking + .gitignore.
Full purge needs destructive force-push — DO NOT execute without
explicit PM authorization.

4-round queue (R1+R2+R3 done):
  R4 — Norse profile: 5 fields + cross-civ parity hook → RN
  RN — cross-civ × cross-field audit + phase-4.md §4.x per-civ
       specialization body + possible §4.8 exit-gate item add

5-field schema (LOCKED):
  matchup_affinity      vs §4.10 7-attack × 5-armor RPS — AGGREGATE
                        DIRECTLY against locked 2026-04-26 RPS;
                        R3 demonstrated R2's predictions can invert
                        when re-aggregated.
  identity_hook         one-paragraph mechanical thesis; civ-neutral
                        effect-type language; falsifiable proc-shape
                        distinction held at EQUATION-FORM layer
                        (Greek deceleration × lifespan-compounding /
                        Aztec per-cast-multiplier × per-kill-bonus /
                        Norse predicted cleave-radius × propagation-
                        Bleed-stack).
  signature_creep_types armor-class grain pre-§4.7-lock.
  multi_civ_play_hook   per-tower RN type-coverage gaps; Norse:
                        no-Poison + no-Divine-T1-T3 holes filled by
                        cross-civ Aztec+Greek.
  commander_synergy     per-commander R5 lane-lock — for Norse:
                        summon_anchor: ragnar all 15 Norse rows.

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — produce R4 (Norse profile) AUTONOMOUSLY per the
PM autonomy mandate.

Surface AskUserQuestion ONLY on: genuine forks not anticipated in R1
scope / scope expansion beyond 4-round queue / cascade-violation risk
(matchup_affinity contradicting per-tower RN; signature_creep_types
crossing §4.7 archetype-grain; commander_synergy crossing civ lanes) /
cultural-sensitivity surface / handoff trigger.

R4 INPUTS (Grep > full-file Read):
  decisions/2026-05-06-per-civ-specialization-scope.md  (R1 scope)
  decisions/2026-05-06-per-civ-r2-greek-profile.md
  decisions/2026-05-06-per-civ-r3-aztec-profile.md  (study reconciliation
    paragraph + 3x debug loop pattern)
  decisions/2026-05-06-per-tower-r4-norse-roster.md
  decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md
  decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md
  decisions/2026-04-26-attack-type-mapping.md  (CRITICAL — aggregate
    Norse roster directly against this lock)
  concept/phase-4.md  (§4.10 / §4.11 — read-only)

R4 DELIVERABLE: decisions/2026-05-06-per-civ-r4-norse-profile.md
(Accepted, Medium). 5-field Norse profile; identity_hook synthesis
+ 3x debug at equation-form layer; cross-civ parity reconciliation
paragraph if direct-aggregation diverges from R3's R4 prediction
(Shielded/Unarmored specialist + Spirit-and-Divine-pre-T4 hole);
cross-civ parity hook → RN.

R4 PROCEDURE:
  1. Read inputs.
  2. Author 5-field Norse profile (aggregate matchup_affinity directly
     against locked 2026-04-26 RPS).
  3. 3x debug loop on identity_hook (equation-form layer).
  4. Cross-civ parity reconciliation if R3's R4 prediction diverges.
  5. Cross-civ parity hook to RN.
  6. cascade-lint: python tools/cascade-lint.py
     (expect clean except pre-existing phase-4 soft-cap 629/600)
  7. Commit R4 + dual-push (session branch + main).
     CRITICAL: targeted `git add <file>` only — never `git add -A`.
  8. Continue to RN autonomously if context budget healthy.
     Otherwise stop after R4 and file mini-handoff.

DOC-HYGIENE (NEW STANDARD — see CLAUDE.md):
  - CASCADE decisions-table row: ONE LINE per round (`| date | [Title
    — short hook](file) | reversibility |`). No prose summaries.
  - CASCADE current-work pointer: ~5 lines (landed / next / blockers).
  - PROGRESS session log entry: 3-5 lines per round (commit + key
    correction + cross-references). Full prose lives in decision file.
  - HANDOFF TL;DR: 3-5 sentences. Don't re-prose what's in the
    decision file.

DUAL-PUSH POINTS (locked from R1 scope):
  After RN (carries R4 + RN; CLOSES arc) — but R4 is also a natural
  push point if ending the session there before RN.

NO GAME CODE EDITS. Concept-only — Phase 4 hasn't exited.
NO SPINE-DOC EDITS during R4. All phase-4.md §4.x body edits + possible
  §4.8 exit-gate item add happen at RN.

VERIFY each commit with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.
TARGETED `git add` ONLY — never `git add -A`.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5; high-vigilance at Aztec, also at Norse).
- Local `main` stale on session start.
- `cascade-lint` fails new (pre-existing phase-4 soft-cap is carried).
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned.
- Any amendment-pass §-anchor would be silently edited.
- Any per-commander R1-R5 spine-doc surface would be silently edited.
- Any per-tower R1-RN magnitude row would be silently re-tuned out of band.
- Any per-civ R2 Greek or R3 Aztec profile field would be silently edited.
- Any per-civ matchup_affinity row contradicts the per-tower RN type-coverage audit (without a reconciliation paragraph).
- Any per-civ signature_creep_types row crosses §4.7 archetype-grain.
- Any per-civ commander_synergy row crosses civ lanes.
- A track touching CONCEPT constraints lands without 3x debug loop.
- `git add -A` is about to be invoked (use targeted staging instead).
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
