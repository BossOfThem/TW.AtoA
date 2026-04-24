# HANDOFF — Session Checkpoint

**Last session:** 2026-04-27 — context-window fix (doc hygiene system: archive split + CLAUDE.md trim discipline)
**Hand-off by:** Claude (Sonnet 4.6)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Problem fixed:** Bootstrap was loading ~125KB (~32K tokens) per session. API errors and context exhaustion were frequent. Root cause: append-only session log in `PROGRESS.md` (50KB) and pointer history in `CASCADE.md` (41KB) with no pruning mechanism.

**Solution:** Archive split + permanent trim discipline.

- **Created [`PROGRESS-archive.md`](PROGRESS-archive.md)** — all session log entries before 2026-04-26.
- **Created [`CASCADE-history.md`](CASCADE-history.md)** — all old pointer blocks + version history before v0.23.
- **Trimmed [`PROGRESS.md`](PROGRESS.md)** — 50KB → 23KB (kept 3 most recent session entries).
- **Trimmed [`CASCADE.md`](CASCADE.md)** — 41KB → 16KB (kept most recent pointer block only; version footer trimmed to 2 bumps).
- **Updated [`CLAUDE.md`](CLAUDE.md)** — new "Doc hygiene" section; handoff trigger step 3 now instructs Claude to trim on every handoff going forward.

Bootstrap total: **~125KB → ~78KB** (~20K tokens). `cascade-lint` clean throughout.

**Changes are NOT yet committed** — working tree has modifications to CASCADE.md, CLAUDE.md, PROGRESS.md and two new untracked files. Commit before starting next session.

---

## Commits this session

None yet — work is in the working tree. Commit all five modified/new files as a single doc-hygiene commit before the next session:

```
PROGRESS-archive.md   (new)
CASCADE-history.md    (new)
PROGRESS.md           (trimmed)
CASCADE.md            (trimmed + pointer bumped below)
CLAUDE.md             (doc-hygiene section added)
HANDOFF.md            (this file)
```

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** (last pushed state at `3f8b8c6`).
- `main` HEAD: **`3f8b8c6`** (last pushed).
- **Working tree: modified** — 3 modified files + 2 new untracked. Commit before next session.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures + native myth — 2026-04-25).
- **Phase 1 exit one-pager: FILED** (2026-04-26, Follow-up #11 CLOSED).
- **4-tier + Fusion endgame** frame live across concept/phase-3..7.md + stage 01/03/04/05/06/07 stub-banners.
- **7-type × 5-armor RPS matrix** live in [`decisions/2026-04-26-attack-type-mapping.md`](decisions/2026-04-26-attack-type-mapping.md).
- **Prototype reshape plan Proposed** — awaiting PM ratification. Prototype files frozen.
- `§2.4a` + `§5.4` [LOCKED] — untouched.

### Stage-level cascade state

- **Stub-amendment banners filed:** stages 01, 03, 04, 05, 06, 07 ✓
- **Frame-independent (no amendment owed):** stages 00, 02, 08 ✓
- **Stage body rewrites:** all deferred to dedicated reopens (stub-level only).

---

## Locked content skeleton (carry forward — unchanged)

See [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) + [`decisions/2026-04-26-phase-1-exit-one-pager.md`](decisions/2026-04-26-phase-1-exit-one-pager.md) for full tables.

- **3 civs:** Greek / Aztec / Norse.
- **3 launch commanders:** Leonidas / Montezuma II / Ragnar Lothbrok, each 1 passive + short-CD + long-CD.
- **18 T1-T3 towers** (6/civ, mundane historic labels), **15 units** (5/civ), **18 T4 Demigods & Heroes** (6/civ).
- **9 Gods via 9 locked Fusion recipes** (Zeus/Athena/Poseidon; Quetzalcoatl/Huitzilopochtli/Tezcatlipoca; Odin/Thor/Tyr).
- **Tribute + Divinity economy.** 30-wave match. 6-Divinity cap. 2 unlock Fusion menu + 1/fusion.
- **7-type × 5-armor matrix** (2026-04-26).
- **MVP validation bars:** 50%+ civilization-persistence by end of T3, 30%+ reach ≥1 Fusion per match.

---

## NEXT SESSION — primary directive

**PM has named the next-session focus: commander mechanics.** Open in **plan mode**. Goal: design how the Commander behaves in-match — specifically, the proposed shift from *persistent on-field avatar* (2026-04-20 design) to *summoned-on-cast avatar* (emerges to cast a special, animates to target, retreats).

Default cadence: **one-step-at-a-time with PM "go" gates**. HARD AUTONOMY MODE is NOT in force.

### Commander-as-summoned-ability-avatar (plan-mode design pass)

**Context (2026-04-26 prototype review):** Current "on-field Commander Avatar with 2-cell aura + Shift-click move + Q signature" design ([`decisions/2026-04-20-commander-on-field-hero.md`](decisions/2026-04-20-commander-on-field-hero.md)) **does not match PM intent**. Intended: Commander is **not present on the field by default**. The Commander **emerges only to cast an ability** (short-CD / long-CD / signature), animates to the relevant location, performs the cast (e.g., Leonidas appears to shout "This Is Sparta!"), then retreats.

**Scope of the plan-mode pass:**
1. Ratify the summoned-on-cast pattern (supersede or rebase [`decisions/2026-04-20-commander-on-field-hero.md`](decisions/2026-04-20-commander-on-field-hero.md)).
2. Resolve two open questions:
   - **Passive ability presence** — is the always-on passive (e.g., "Spartan Training" = +X% to Greek towers) invisible board-wide, or does the avatar briefly flicker on wave-start / Tribute pickup?
   - **Short-CD cast frequency** — does the avatar emerge for *every* short-CD cast (heavier animation budget, more flavorful), or only for long-CD + signature?
3. Spec the cast-emerge → cast-act → cast-retreat animation phases at the conceptual level (no engine code).
4. Update `concept/phase-4.md §4.1` commander spec.
5. Determine if this adds a 7th step to [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (or extends C4).
6. File `decisions/<next-date>-commander-as-summoned-ability-avatar.md` (Accepted once PM signs off plan; Reversibility Medium; 3x debug loop inline).

**Plan-mode deliverables:** decision draft + §4.1 diff + reshape-plan addendum. No code, no commits until PM exits plan mode with "go".

### Background candidates (parked; pick up after commander pass closes)

- **Candidate A** — Prototype reshape plan ratification + execution. Ratify [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (Proposed → Accepted), then execute C1→C6 one per turn.
- **Candidate B** — Cultural-sensitivity pass scheduling (Follow-up #5). External consultation for Aztec representation + Leonidas + Ragnar.
- **Candidate C** — Patch-1 commanders per civ (Follow-up #6).
- **Candidate D** — `admin/concept.json` migration path (rewrite / regenerate / retire).

### Prototype UX debt (not blocking)

First-time players are stuck: `menuNewGame() → commander-pick → selectCommander()` never sets `Profile.data.lastMode`, so the "Play" button never surfaces. **Workaround:** DevTools `Profile.data.lastMode = "skirmish"; Profile.save(); location.reload();`. Proper fix is part of reshape plan C2/C4.

---

## Open threads / carried debts

### Still open (priority order)

1. **Commander-as-summoned-ability-avatar** — plan-mode pass (this session's primary directive).
2. **Prototype reshape plan ratification** of [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (Proposed).
3. **Cultural-sensitivity pass** (Follow-up #5) — mandatory content-lock gate.
4. **Patch-1 commanders per civ** (Follow-up #6).
5. **Myth-creature PvE bosses** (Follow-up #3).
6. **Title lock** (Q8) — "Mud to Myth" PM-floated, not locked.
7. **Stage body rewrites** (01/03/04/05/06/07) — deferred to dedicated reopens.
8. **`admin/concept.json` full migration** — rewrite / regenerate / retire. PM picks direction.
9. **Foresight-coin cross-civ borrowing** (Follow-up #7) — parked post-launch.
10. **PvE campaign + AGES + leveling + attributes** (Follow-up #8) — parked.
11. **Non-boss enemy ontology** (Follow-up #9) — open.
12. **Styling / tone pass** (Follow-up #4) — parked.
13. **[PROPOSAL] balance-pass re-ratification** (Follow-up #13) — pending numbers.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions [LOCKED]**.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- Mechanics surface (TD / merge / debuff / magic).
- Full 2026-04-25 locked content skeleton (civs, commanders, towers, units, T4 demigods, gods, recipes, economy, match arc, cap).
- Prototype files — no edits until PM ratifies reshape plan.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **Dual-push discipline:** if autonomy re-enabled, push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** inline on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS.md session log to 3 most recent entries (archive older to PROGRESS-archive.md), trim CASCADE.md pointer to most recent block (archive older to CASCADE-history.md), trim version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — fresh session post context-window fix.

FIRST: commit any uncommitted working-tree changes before bootstrapping.
  git add CASCADE.md CLAUDE.md PROGRESS.md HANDOFF.md CASCADE-history.md PROGRESS-archive.md
  git commit -m "doc hygiene — archive split + trim discipline + HANDOFF"
  git push origin HEAD main

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs, verify local main is current:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty
  (If not, pull --ff-only before reading any doc.)

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF (2026-04-27: context-window
  fix landed; doc hygiene system in place; bootstrap now ~78KB).
- Primary open blocker: Commander-as-summoned-ability-avatar
  plan-mode design pass.
- Specific next-step proposal: open plan mode, read
  decisions/2026-04-20-commander-on-field-hero.md, present a
  design plan for the summoned-on-cast pattern.

CADENCE: default one-step-at-a-time with PM "go" gates.
Plan mode is active for the commander mechanics pass.
HARD AUTONOMY MODE is NOT in force.

PRIMARY DIRECTIVE — Commander-as-summoned-ability-avatar:
  PM intent: Commander is NOT on the field by default.
  Commander EMERGES to cast an ability (short-CD / long-CD /
  signature), animates to target, retreats. Supersedes 2026-04-20
  persistent-avatar design.
  Plan-mode scope:
    1. Ratify summoned-on-cast pattern (supersede or rebase
       decisions/2026-04-20-commander-on-field-hero.md).
    2. Resolve passive presence + short-CD frequency open Qs.
    3. Spec emerge → cast-act → retreat animation phases (concept
       level only, no engine code).
    4. Update concept/phase-4.md §4.1.
    5. Determine reshape-plan C4/step-7 impact.
    6. File decisions/<date>-commander-as-summoned-ability-avatar.md.

ACTIVE DIRECTION (locked 2026-04-25, exit one-pager 2026-04-26):
  Real cultures + native myth. Greek / Aztec / Norse.
  Commanders: Leonidas / Montezuma II / Ragnar Lothbrok.
  18 T1-T3 towers + 15 units + 18 T4 Demigods & Heroes.
  Fusion-to-Gods: 9 Gods via 9 locked 2-Demigod recipes.
  Tribute + Divinity (6 cap; 2 unlock menu + 1/fusion).
  30-wave lane-wars. 7-type × 5-armor RPS + status procs.
  MVP bars: 50%+ civ-persistence T3; 30%+ ≥1 Fusion/match.

STOP AND HANDOFF when reaching:
  - Cultural-sensitivity concern (Follow-up #5).
  - §2.4a or §5.4 touch.
  - Locked-name change without PM.
  - Mechanics surface touch.
  - Prototype execution before reshape plan Accepted.

DO NOT:
  - Touch §2.4a or §5.4 conventions.
  - Touch prototype files until reshape plan Accepted.
  - Assume HARD AUTONOMY MODE.
  - Change 2026-04-25 locked names without PM.
```

---

## Escalation triggers

Hard-stop and flag if:

- A proposed sub-decision would touch `§2.4a` or `§5.4` conventions.
- A proposed sub-decision would modify 2026-04-25 locked names without PM.
- A proposed sub-decision would touch mechanics (TD/merge/debuff/magic).
- A cultural-sensitivity concern surfaces (Follow-up #5).
- Prototype file edits proposed before PM ratifies [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.

---
