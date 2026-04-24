# HANDOFF — Session Checkpoint

**Last session:** 2026-04-26 (later, continuation-2 — stages 03/07 stub-amendments + admin/concept.json staleness banner landed after HANDOFF rewrite; Phase 1 exit one-pager + stages 01/04/05/06 + CONCEPT-GAPS v0.5 + prototype reshape plan Proposed from the prior sub-pass)
**Hand-off by:** Claude (Opus 4.7, 1M context)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Directive executed under HARD AUTONOMY MODE** after PM authorized "Full autonomy-safe queue + PM-gated answers" on a 4-question upfront gate. Scope cap: autonomy-safe items only; patch-1 commanders parked; working-title stays "Ash to Altar" ("Mud to Myth" floated); prototype reshape is plan-only-Proposed, no code.

**13 commits total** (9 from the earlier sub-pass + 4 from a continuation after HANDOFF was first rewritten), one file per turn, all dual-pushed to `session/2026-04-25-q2-world-pitch` + `main`:

**Continuation-2 (4 commits after HANDOFF rewrite, user-triggered "continue till or prompt me"):**
- `stages/03-match-setup.md` stub-amendment banner (Tribute+Divinity supersede gold/knowledge/influence; starting-age → starting-tier; civ-coded map + tone).
- `stages/07-match-end.md` stub-amendment banner (MVP civilization + final-tier + Fusion count + named Gods + Tribute/Divinity stats; commander voice-line cultural-sensitivity gate).
- `admin/concept.json` `meta.staleNotice` banner (file still on pre-2026-04-21 5-lineage/11-age shape; NOT migrated; migration tracked as PROGRESS debt pending PM).
- `CASCADE.md` v0.23 → v0.24 + PROGRESS session-log continuation entry.

Stages 00/02/08 scan-verified frame-independent — no amendments owed. All real-cultures cascade across stage tree now complete at stub-level (stages 01/03/04/05/06/07).

**Earlier sub-pass (9 commits) originally captured here:**

1. **Phase 1 exit one-pager filed** — [`decisions/2026-04-26-phase-1-exit-one-pager.md`](decisions/2026-04-26-phase-1-exit-one-pager.md) (Accepted; Reversibility Easy; 3x debug loop inline). Formal capture closing Follow-up #11. Structure: The one page (World / Commander role / Hybrid topology / Why this frame wins / What remains open) + Alternatives + Reason + Follow-ups. MVP validation bars restated: 50%+ civ-persistence, 30%+ Fusion-reach.

2. **`concept/phase-2.md §2.3` residual rewritten** — "Content explosion" now cites 3-civ locked skeleton; "Lineage balance" → "Civilization balance" citing attack-type-coverage gaps; onboarding-cliff surface list expanded + mundane-outside/myth-inside cited as load-bearing.

3. **Stages 01/04/05/06 stub-amendments** — 2026-04-26 amendment banners added to [`stages/01-commander-pick.md`](stages/01-commander-pick.md), [`stages/04-in-match-core.md`](stages/04-in-match-core.md), [`stages/05-age-evolution.md`](stages/05-age-evolution.md), [`stages/06-hybrids-fusion.md`](stages/06-hybrids-fusion.md) pointing at 2026-04-25 ratification + 2026-04-26 one-pager. Stage 06 **OPEN BLOCKER discovery-mechanic CLOSED** (menu-driven + codex-visible; 9 locked recipes enumerated inline). Stage 05 "age evolution" subject reframed to tier-evolution + Fusion event. §5.4 + §2.4a [LOCKED] untouched across all four; body rewrites deferred to dedicated reopens.

4. **CONCEPT-GAPS v0.4 → v0.5** — shape-audit re-pass; all 11 remaining rows confirmed shape-independent under real-cultures + 7-type × 5-armor frame. Cultural-sensitivity pass flagged as game-wide mandatory gate.

5. **Prototype reshape plan filed Proposed** — [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (**Proposed**; Reversibility Medium). 6-step: C1 data layer → C2 silhouette 5→3 SVG migration → C3 Tribute+Divinity resource bar → C4 tier-ladder + Fusion menu → C5 7-type × 5-armor RPS indicator → C6 dead-code. No code touched, no number locks, no pose locks. **Awaiting PM ratification before execution.**

6. **CASCADE v0.22 → v0.23** + PROGRESS session-log row.

Autonomy stopped at the scope cap. Remaining items (cultural-sensitivity pass, patch-1 commanders, myth-creature PvE, playtest, prototype reshape execution, title) are PM-gated.

---

## Commits this session (all dual-pushed; `main` at `fbd6e7e`)

### Continuation-2 commits (after first HANDOFF rewrite)

| # | Commit | Scope |
|---|--------|-------|
| 11 | `aa1e750` | `admin/concept.json` `meta.staleNotice` + PROGRESS debt line |
| 12 | `8f2efb5` | `stages/03-match-setup.md` stub-amendment |
| 13 | `6e4e3ca` | `stages/07-match-end.md` stub-amendment |
| 14 | `fbd6e7e` | CASCADE v0.23 → v0.24 + PROGRESS continuation-2 entry |
| 15 | (this) | HANDOFF rewrite for continuation-2 |

### Earlier sub-pass commits

| # | Commit | Scope |
|---|--------|-------|
| 1 | `be00471` | `decisions/2026-04-26-phase-1-exit-one-pager.md` filed Accepted |
| 2 | `d59c981` | `concept/phase-2.md §2.3` residual rewrite + banner |
| 3 | `2eafd41` | `stages/01-commander-pick.md` stub-amendment |
| 4 | `d6838e2` | `stages/04-in-match-core.md` stub-amendment (Tribute+Divinity + 7×5 matrix) |
| 5 | `9c9e5f2` | `stages/05-age-evolution.md` stub-amendment (4-tier + Fusion) |
| 6 | `e3c00f9` | `stages/06-hybrids-fusion.md` stub-amendment (OPEN BLOCKER CLOSED) |
| 7 | `d4745a8` | `CONCEPT-GAPS.md` v0.4 → v0.5 shape-audit |
| 8 | `c1edee1` | `decisions/2026-04-26-prototype-reshape-plan.md` filed Proposed |
| 9 | `d1a6394` | `CASCADE.md` v0.22 → v0.23 + seventh-pass pointer + 2 decision rows |
| 10 | `acb01ca` | PROGRESS — 2026-04-26 (later) session-log entry |

---

## State snapshot

### Git

- Branch pushed: **`session/2026-04-25-q2-world-pitch`** (tracking origin, clean).
- `main` HEAD: **`fbd6e7e`** (local + origin/main in sync) pre-this-commit; will be the HANDOFF-rewrite commit after push.
- Working tree clean. Dual-push cadence honored every commit.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: ratified** (real-world cultures + native myth — 2026-04-25).
- **Phase 1 exit one-pager: FILED** (2026-04-26, Follow-up #11 CLOSED).
- **4-tier + Fusion endgame** frame lives across concept/phase-3..7.md + stages 01/04/05/06 stub-banners.
- **7-type × 5-armor RPS matrix** live in [`decisions/2026-04-26-attack-type-mapping.md`](decisions/2026-04-26-attack-type-mapping.md).
- **Prototype reshape plan Proposed** — awaiting PM ratification. Prototype files frozen.
- `§2.4a` + `§5.4` [LOCKED] — untouched.

### Stage-level cascade state (updated continuation-2)

- **Stub-amendment banners filed:** stages 01, 03, 04, 05, 06, 07 ✓
- **Frame-independent (no amendment owed):** stages 00, 02, 08 ✓
- **Stage body rewrites:** all six still deferred to dedicated reopens (stub-level only).

### Not touched this pass (still owed)

- **Cultural-sensitivity pass** (Follow-up #5) — mandatory gate before content-lock. External consultation needed.
- **Patch-1 commanders per civ** (Follow-up #6) — PM-directed.
- **Myth-creature PvE boss roster** (Follow-up #3).
- **Title lock** (Q8) — "Mud to Myth" floated but not locked.
- **Prototype reshape plan execution** — awaiting PM ratification of [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md).
- **`concept/phase-1.md §1.1`** — verified continuation-2: already rewritten in earlier 2026-04-26 pass (real-cultures framing + framing-note). No further work owed.
- Stage body rewrites (01/03/04/05/06/07) — deferred to dedicated reopens; banners only.
- `admin/concept.json` — staleness banner added continuation-2; full migration pending PM direction (new debt in PROGRESS).

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

**Default cadence: one-step-at-a-time with PM "go" gates.** HARD AUTONOMY MODE is NOT in force unless PM re-enables.

### Two candidate directives (PM picks)

**Candidate A — Prototype reshape plan ratification + execution (if PM ratifies).**
- PM reviews [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md), flips Proposed → Accepted (or revises).
- If Accepted: execute 6 steps C1→C6 one per turn. Data layer first (civilizations.json / fusion-recipes.json / attack-types.json; tiers.json rename; commander migration), then silhouette SVG migration, then Tribute+Divinity bar, then tier-ladder + Fusion menu UI, then RPS indicator, then dead-code pass.
- Prototype freeze lifts for this work. Concept docs stay untouched.

**Candidate B — Cultural-sensitivity pass scheduling (Follow-up #5).**
- PM decides external-consultation plan: Aztec representation review, 300-ideology audit for Leonidas framing, TV-show-vs-history framing for Ragnar. Output is a dated decision entry defining the process + gate criteria + who consults. Blocks content-lock.

**Candidate C — Patch-1 commanders per civ (Follow-up #6).**
- PM selects candidate rosters for the +1-per-civ patch-1 commander. Per 2026-04-25 ratification these are TBD post-playtest, but PM can pre-seed the candidate pool.

### Scope that STOPS autonomy (HANDOFF when reached)

- Anything touching `§2.4a` or `§5.4` conventions.
- Anything modifying 2026-04-25 locked names.
- Anything touching mechanics (TD/merge/debuff/magic).
- Cultural-sensitivity concerns surfacing.
- Prototype execution before PM ratification.

---

## Open threads / carried debts

### CLOSED this pass

- **Follow-up #11** (Phase 1 exit formal one-page write-up) — CLOSED via [`decisions/2026-04-26-phase-1-exit-one-pager.md`](decisions/2026-04-26-phase-1-exit-one-pager.md).
- **Stages 01/03/04/05/06/07 stub-amendments** — CLOSED (banners filed; body rewrites deferred). Stages 00/02/08 frame-independent.
- **`admin/concept.json` staleness visibility** — CLOSED at banner-level (file carries `meta.staleNotice`); full migration is a new open debt.
- **CONCEPT-GAPS audit against real-cultures frame** — CLOSED (v0.5 shape-audit re-pass).
- **Stage 06 OPEN BLOCKER** (hybrid discovery mechanic) — CLOSED (menu-driven + codex-visible).

### Still open (priority order)

1. **Prototype reshape plan — PM ratification** of [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (Proposed).
2. **Cultural-sensitivity pass** (Follow-up #5) — mandatory content-lock gate.
3. **Patch-1 commanders per civ** (Follow-up #6).
4. **Myth-creature PvE bosses** (Follow-up #3).
5. **Title lock** (Q8) — "Mud to Myth" PM-floated, not locked.
6. **`concept/phase-1.md §1.1` + `concept/phase-2.md` body** deep rewrites — upstream closure, downstream of one-pager.
7. **Stage body rewrites** (01/03/04/05/06/07) — deferred to dedicated reopens.
7a. **`admin/concept.json` full migration** — rewrite to real-cultures shape, regenerate from CONCEPT.md tree via extended admin/ tooling, or retire in favor of concept/phase-*.md as sole source of truth. PM picks.
8. **Foresight-coin cross-civ borrowing** (Follow-up #7) — parked post-launch.
9. **PvE campaign + AGES + leveling + attributes** (Follow-up #8) — parked.
10. **Non-boss enemy ontology** (Follow-up #9) — open.
11. **Styling / tone pass** (Follow-up #4) — parked.
12. **[PROPOSAL] balance-pass re-ratification** (Follow-up #13) — pending numbers.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions [LOCKED]** (conventions, not specific names).
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- Mechanics surface (TD / merge / debuff / magic).
- Full 2026-04-25 locked content skeleton (civs, commanders, towers, units, T4 demigods, gods, recipes, economy, match arc, cap).
- Prototype files — no edits until PM ratifies reshape plan.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`. HARD AUTONOMY is a session override — do NOT assume it's in force unless PM re-enables.
- **Dual-push discipline:** if autonomy re-enabled, push to BOTH session branch AND `main` after every commit (fast-forward only).
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs. Pull --ff-only if stale.
- **3x debug loop** inline on any CONCEPT-constraint-touching proposal.
- **Placeholder flagging:** every name placeholder unless `[LOCKED]`. 2026-04-25 launch-skeleton names are PM-protected.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. 2026-04-27+ session.

BOOTSTRAP per CLAUDE.md:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE bootstrapping, verify local main is current:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty
  (If not, pull --ff-only before reading any doc.)

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF (2026-04-26 later: Phase 1
  exit one-pager FILED; stages 01/04/05/06 stub-amended; CONCEPT-GAPS
  v0.5 shape-audit clean; prototype reshape plan filed Proposed
  awaiting PM ratification).
- Open blockers for forward motion: PM picks the directive.
  Candidate A = prototype reshape plan ratification + execution
  (ratifies 2026-04-26-prototype-reshape-plan.md, then C1→C6 one
  per turn, prototype freeze lifts). Candidate B = cultural-sensitivity
  pass scheduling (Follow-up #5). Candidate C = patch-1 commanders
  pre-seed (Follow-up #6).
- Specific next-step proposal: await PM selection among A/B/C.

CADENCE: default one-step-at-a-time with PM "go" gates per CLAUDE.md.
HARD AUTONOMY MODE is NOT in force unless PM re-enables.

ACTIVE DIRECTION (ratified 2026-04-25, cascaded 2026-04-26,
Phase 1 exit one-pager filed 2026-04-26):
- Real cultures + native myth. Greek / Aztec / Norse launch.
- Commanders: Leonidas / Montezuma II / Ragnar Lothbrok.
- 18 T1-T3 towers + 15 units + 18 T4 Demigods & Heroes.
- Fusion-to-Gods endgame: 9 Gods via 9 locked 2-Demigod recipes.
- Tribute + Divinity 2-currency (6 cap; 2 unlock menu + 1/fusion).
- 30-wave lane-wars match. Boss at 5/10/15/20/25/30 (mini/main alt).
- 7-attack-type × 5-armor-tag RPS with per-type light status procs.
- "High-school recognizable" naming + "mundane outside, myth inside"
  tower heuristic.
- MVP bars: 50%+ civ-persistence by T3; 30%+ reach ≥1 Fusion/match.

STOP AND HANDOFF when reaching any of these:
- Cultural-sensitivity concern surfaces (Follow-up #5).
- §2.4a or §5.4 convention touch.
- 2026-04-25 locked-name change without PM.
- Mechanics surface touch.
- Prototype execution before PM ratifies reshape plan.

DO NOT:
- Touch §2.4a or §5.4 conventions.
- Touch any prototype file until reshape plan Accepted.
- Force-revert 2026-04-21 Step A §-edits.
- Re-open Follow-up #10 or #11.
- Change locked names without PM.
- Drift from "high-school recognizable" naming.

LOCKED (do NOT modify):
- §2.4a + §5.4 [LOCKED].
- Mechanics: TD/merge/debuff/magic.
- Full 2026-04-25 launch-match design skeleton.
- 7-type × 5-armor matrix (Reversibility Medium; new decision to
  amend).
- Phase 1 exit one-pager (Reversibility Easy but formal-capture;
  don't silently edit, new decision if revision needed).

WORKING TITLE: "Ash to Altar" stays. "Mud to Myth" is PM-floated
candidate; no action needed.
```

---

## Escalation triggers

Hard-stop and flag if:

- A proposed sub-decision would touch `§2.4a` or `§5.4` conventions.
- A proposed sub-decision would modify 2026-04-25 locked names without PM input.
- A proposed sub-decision would touch mechanics (TD/merge/debuff/magic).
- A proposed sub-decision would silently revise the 7-type × 5-armor matrix (new decision required).
- A cultural-sensitivity concern surfaces — STOP and flag for PM + external consultation per Follow-up #5.
- Prototype file edits proposed before PM ratifies [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md).
- Local `main` stale on session start — resync before reading docs.
- `cascade-lint` fails and fix > 5min.

---

*End of HANDOFF — 2026-04-26 later. Phase 1 exit one-pager filed; stages 01/04/05/06 stub-amended; CONCEPT-GAPS v0.5; prototype reshape plan Proposed. Next session: PM picks directive A/B/C under default PM-gated cadence.*
