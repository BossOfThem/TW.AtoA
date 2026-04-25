# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**CONCEPT.md amendment pass — ARC CLOSED. Rounds 1–7 of 7 LANDED across 3 dual-pushed commits (`6580303` + `44ada2c` + `7cae3a4`).**

Seven topical rounds rolled all 22 ratifications from the prior two arcs (2026-05-04 Balance-pass #1 conceptual-frame 12 rounds + 2026-05-05 Numbers-phase Follow-up #13 10 rounds) into the spine docs as stable §-anchors:

1. **R1** — Scope decision + §-placement table + 7-round queue. 3x debug loop on §-placement (Option A single mega-round / Option B per-decision-file / **Option C topical 7-round queue chosen**). [`scope`](decisions/2026-05-05-concept-amendment-pass-scope.md).
2. **R2** — `phase-3.md §3.6` mode roster 5→6 (Solo Campaign / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze) + per-mode summary table + §3.4 stale Commander-Hero residue redacted + §3.8 mode-count update. [`R2`](decisions/2026-05-05-concept-amendment-pass-round-2-phase-3-modes.md).
3. **R3** — `phase-4.md §4.10 Tower-vs-Unit math NEW` (9 sub-sections: variable nomenclature (a)-(r) + extension (s) + master damage equation + 7-slot round typology + (k) single-axis rule + skill-bar axes + sell-refund + target-priority + boss/Divinity reward shape + engine-port discipline) + §4.11 placeholder. Inserted §4.9→§4.10→§4.11→§4.8 per §4.4a precedent. [`R3`](decisions/2026-05-05-concept-amendment-pass-round-3-phase-4-tower-vs-unit-math.md).
4. **R4** — `phase-4.md §4.11 Numbers floor` body populated (placeholder → 8 sub-sections binding all R1-R9 magnitudes: HP / (k) / Tribute / speed+map / DPS ladder + tier-up / commander / per-mode / skill-bar). [`R4`](decisions/2026-05-05-concept-amendment-pass-round-4-phase-4-numbers-floor.md).
5. **R5** — `phase-4.md §4.6 Economy` rewrite (Tribute kill-only + Divinity 6-source 4-floor+2-escalation + Mythium retirement note) + `§4.6a Auxiliary economy NEW` (7-slot universal catalog + currency-budget audit + 1.725× expert-stack). Phase-4 trimmed to 600 lines. [`R5`](decisions/2026-05-05-concept-amendment-pass-round-5-phase-4-economy.md).
6. **R6** — `phase-4.md §4.7` Wave-composition variance mandate (R9 close-out) + `phase-6.md §6.5 Skill-bar telemetry NEW` + `phase-7.md §7.4` "Go big at launch (non-negotiable)" bullet. §4.6a audit + mode-availability compressed for line cap (phase-4 597 lines). [`R6`](decisions/2026-05-05-concept-amendment-pass-round-6-phase-4-7-r11-and-phase-6-7.md).
7. **R7 CLOSES arc 7/7** — Hub `CONCEPT.md` phase-index rows 3/4/6/7 touched + Non-negotiables list += "Go big at launch" + version footer 0.8→0.9. [`R7`](decisions/2026-05-05-concept-amendment-pass-round-7-hub-close.md).

**Spine-anchor stability achieved.** All 22 ratifications now resolve to stable §-anchors in `CONCEPT.md` + `concept/phase-3..7.md`.

PM autonomy mandate from Numbers-phase mid-arc carried forward — **R2-R7 produced fully autonomously without per-question gates.** Three dual-push checkpoints (after R3 / R5 / R7); cascade-lint clean throughout. 7 new decision documents. CASCADE bumped 0.47 → 0.55.

**No game code edits this session.** Pure spine-doc consolidation. §5.4 + §2.4a [LOCKED] UNTOUCHED throughout entire arc; 17-item conceptual frame UNTOUCHED; 2026-04-25 locked content skeleton UNTOUCHED; hub vision line UNTOUCHED.

---

## What is locked (clear-safe)

### Carried forward (untouched this session)

- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes (HP curve / (k) / Tribute / speed / DPS ladder + tier-up / commander / aux-slot costs / per-mode tuning / skill-bar thresholds / Divinity sources) — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure (Tribute kill-only + Divinity 6-source 4-floor+2-escalation; 6-cap discipline) — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (now hub Non-negotiable).
- 2026-04-25 locked content skeleton (3 civs × full ladder + 3 Gods via 9 Fusion recipes + 6 launch modes) — Accepted.
- §5.4 [LOCKED] (Civilizations row, real-culture proper nouns).
- §2.4a [LOCKED] (accessibility floor).

### NEW spine-doc surfaces this session

| Surface | Bound by |
|---------|----------|
| `phase-3.md §3.6` 6-mode roster + summary table | R2 |
| `phase-4.md §4.10 Tower-vs-Unit math` (9 sub-sections) | R3 |
| `phase-4.md §4.11 Numbers floor` (8 sub-sections) | R4 |
| `phase-4.md §4.6 Economy` rewrite | R5 |
| `phase-4.md §4.6a Auxiliary economy` (7-slot catalog + budget audit) | R5 |
| `phase-4.md §4.7` Wave-composition variance mandate (R11 anchor) | R6 |
| `phase-6.md §6.5 Skill-bar telemetry` (3-axis protocol) | R6 |
| `phase-7.md §7.4` "Go big at launch (non-negotiable)" bullet | R6 |
| Hub `CONCEPT.md` phase-index rows 3/4/6/7 + Non-negotiables list | R7 |

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit (pre-handoff): **`7cae3a4`** — "CONCEPT amendment pass ARC CLOSED — Rounds 6-7 of 7 LANDED."
- Arc commits: `6580303` (R1-R3) + `44ada2c` (R4-R5) + `7cae3a4` (R6-R7). All dual-pushed to session branch + `main`.
- Working tree before handoff commit: only `.accord/` (untracked, untouched).
- This handoff itself will produce one additional commit (PROGRESS / CASCADE / HANDOFF doc-hygiene); will be dual-pushed.

### Phase status

- All Phase 1–4 conceptual ratification carried forward + now consolidated into spine docs.
- Numbers-phase 100% done (all 17 frame variables (a)-(r) + extension (s) bound).
- Spine-anchor stability achieved — all 22 ratifications resolve to stable §-anchors.
- **Phase 5 readiness gate** — engine-side telemetry per §6.5 protocol + wave-composition variance per §4.7 R11 mandate are now spec-anchored Phase-5 owns-this items.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (CONCEPT amendment pass arc / Numbers-phase R10 / Numbers-phase R9). R8 archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (CONCEPT amendment pass ARC CLOSED). Numbers-phase Follow-up #13 prior block archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.55 + 0.54 reference. Older (0.53 / 0.52 / 0.51 / 0.50 / 0.47 / etc.) archived to `CASCADE-history.md`.
- `CONCEPT-GAPS.md`: unchanged (11 active gaps + resolved set).
- cascade-lint clean.

### Open follow-ups (carried)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art; intersects per-civ specialization track).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape; PM picks (a) full rewrite, (b) regenerate from CONCEPT.md, or (c) retire.
- **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.

### Authoring sub-passes (post-arc, no order-of-operations locked)

- **Per-tower** — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs. **Now unblocked.** Consumes §4.10 frame + §4.11 magnitudes + §4.6a aux catalog as the spec floor.
- **Per-commander** — bind control / summon / economy effect-type variants of the 3 (h) slots, equivalent-impact to damage-floor. **Now unblocked.** Consumes §4.11.6 damage-floor + §4.1 identity-floor.
- **Per-civ** — Greek / Aztec / Norse specialization (matchup affinities, identity hooks, signature creep types). Intersects Follow-up #5 cultural-sensitivity gate.
- **Per-map / Round 11** — good-cell authoring + wave-randomization seeds + crystal-lock variance per §4.7 R11 mandate.

### Regression-watch (unchanged this session)

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.

---

## NEXT SESSION — primary directive

**No single Recommended track.** With the amendment pass closed, the post-arc forks are concrete authoring sub-passes against now-stable §-anchors. PM picks scope first.

Candidate tracks (rough design-merit order):

1. **Per-commander effect-type-variant authoring sub-pass** — control / summon / economy variants of (h) slots; needs equivalent-impact-to-damage-variant constraint per R6. **Likely Recommended** — consumes §4.11.6 damage-floor + §4.1 identity-floor cleanly; unblocks Phase 4 exit-condition test ("can a non-damage commander match damage commander match-impact").
2. **Per-tower authoring sub-pass** — most concrete "numbers becoming game" progress. 5-10 rounds binding cd / range / attack-type / status-proc across 45 towers.
3. **Per-map / Round 11 authoring sub-pass** — defends skill-bar threshold integrity per §4.7 R11 mandate. Cross-cuts all 6 modes; combines wave-randomization + crystal-lock + good-cell sets.
4. **Per-civ specialization** — Greek / Aztec / Norse identity profiles; intersects Follow-up #5 cultural-sensitivity gate (hard pose-lock + content-lock before any culturally-coded civ art ships).
5. **Phase 5 readiness gate** — engine-side telemetry implementation per §6.5 protocol; wave-composition variance per §4.7 R11.
6. `research/06-tw-subgenres.md` deep-dive.
7. `admin/concept.json` migration — long-deferred staleness debt.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]**.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton.
- 17-item conceptual frame + extension (s) — **Accepted**. All Numbers-phase magnitudes — **Accepted**. Revisions require superseding decisions.
- 6-mode ontology + auxiliary economy structure — **Accepted**.
- "Go big at launch" doctrine — **Accepted (Non-negotiable)**.
- All R1-R7 amendment-pass spine surfaces (§3.6 / §4.6 / §4.6a / §4.7 R11 / §4.10 / §4.11 / §6.5 / §7.4 bullet / hub phase-index rows + non-negotiables) — **Accepted**.

---

## Cadence rules carried forward

- **Cadence exists to manage the context window, not to gate every step.** Concrete plan = execute end-to-end; gate on genuine ambiguity only.
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously without per-question gates. Surface AskUserQuestion only on genuine forks (no clear Recommended), scope expansion, cascade-violation risk, or handoff trigger. See `feedback_autonomy_mandate.md`.
- **AskUserQuestion is the standard interface** when gating is needed. Always Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit. Commit at every ~3 rounds.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — CONCEPT.md amendment pass ARC CLOSED 2026-05-05.
All 7 of 7 rounds LANDED. All 22 prior-arc ratifications (12 Balance-pass
#1 conceptual + 10 Numbers-phase #13) now resolve to stable §-anchors in
spine docs (phase-3 §3.6 / phase-4 §4.6 / §4.6a / §4.7 R11 / §4.10 / §4.11
/ phase-6 §6.5 / phase-7 §7.4 / hub CONCEPT.md). Three commits dual-pushed
across the arc (6580303 + 44ada2c + 7cae3a4) plus handoff hygiene commit.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: CONCEPT amendment pass 7/7 COMPLETE; arc CLOSED. All 17
  conceptual-frame variables (a)-(r) + extension (s) bound + spine-anchored.
  Per-tower / per-commander / per-civ / per-map authoring sub-passes ALL
  unblocked (consume §4.10/§4.11/§4.6a + §4.1 identity-floor). Phase 5
  readiness gate items spec-anchored (§6.5 telemetry + §4.7 R11 wave
  variance). admin/concept.json staleness debt outstanding.
  research/06-tw-subgenres.md not yet written.
- Open blockers: none load-bearing.
- Specific next-step: surface AskUserQuestion — PM scopes the post-arc
  fork. Candidate tracks (rough design-merit order):
    1. Per-commander effect-type-variant authoring sub-pass (control/
       summon/economy variants of (h); equivalent-impact-to-damage
       constraint per R6; unblocks Phase 4 exit-condition test).
    2. Per-tower authoring (cd/range/attack-type/status-proc across
       45 towers).
    3. Per-map / Round 11 authoring (wave-randomization + crystal-lock
       + good-cell sets per §4.7 R11 mandate).
    4. Per-civ specialization (Greek/Aztec/Norse identity profiles;
       intersects Follow-up #5 cultural-sensitivity gate).
    5. Phase 5 readiness gate (engine-side telemetry + wave variance).
    6. research/06-tw-subgenres.md.
    7. admin/concept.json migration.

CADENCE: AskUserQuestion is standard interface when gating needed.
Recommended-first. MD-first on scope expansions. Execute end-to-end
when plan concrete; gate on genuine ambiguity only. Commit + dual-push
every ~3 rounds.

PM AUTONOMY MANDATE: once an arc establishes a stable "PM picks
Recommended" pattern, proceed autonomously within that arc. Surface
gates only on genuine forks / scope expansion / cascade-risk / handoff.
See feedback_autonomy_mandate.md.

CURRENCY REMINDER: Tribute (kill-only, k-invariant) + Divinity (6-cap;
4-floor R10/R15/R30 boss + match-completion + 2-escalation Perfect-Wave
+ First-Hybrid). Mythium RETIRED. NOT "gold."

DOCTRINE REMINDER: "Go big at launch" is now a hub Non-negotiable.
MVP ships full content skeleton (3 civs × full ladder + 3 Gods via 9
Fusion recipes + 6 launch modes). Cuts go to post-launch content,
NEVER to launch skeleton. Do NOT recommend the smallest-scope option
for dev-load reduction; recommend on design merit only.

REGRESSION-WATCH: Tutorial / match flow / merge-preview / Promote-T4
indicator / Aztec glyph ◈ / logBalanceCurve / effectiveTowerStats /
snapshot — unchanged.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 locked content skeleton
  untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 amendment-pass §-anchors Accepted (§3.6 / §4.6 / §4.6a /
  §4.7 R11 / §4.10 / §4.11 / §6.5 / §7.4 / hub).
- 6-mode ontology + auxiliary economy structure Accepted.
- "Go big at launch" doctrine Accepted (Non-negotiable).
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract civ
  art (intersects per-civ specialization track).
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned without a superseding decision entry.
- Any amendment-pass §-anchor (§3.6 / §4.6 / §4.6a / §4.7 R11 / §4.10 / §4.11 / §6.5 / §7.4 / hub phase-index rows) would be silently edited.
- A scope expansion occurs and PM has not landed it in MD before further questions.
- Any recommendation invokes "lessen dev load" without explicit PM override of the "Go big at launch" doctrine.
- An authoring-sub-pass commit lands without a `decisions/<date>-*-<slug>.md` entry capturing the bindings.
