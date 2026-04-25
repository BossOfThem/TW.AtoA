# HANDOFF — Session Checkpoint

**Last session:** 2026-04-29 — Prototype reshape plan RATIFIED + C1 Data layer LANDED.
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Prototype reshape plan RATIFIED and C1 Data layer LANDED in two clean commits, both dual-pushed.** Per PM "go" with full bypass permissions on `session/2026-04-25-q2-world-pitch`.

1. **Ratification (commit `6afdce3`):** [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) Status flipped Proposed → **Accepted (ratified 2026-04-29)**; ratification note appended at file foot, no body rewrite (plan + 2026-04-27 amendment already ran 3x debug loops). CASCADE decisions-table annotation updated. Prototype unfreezes.

2. **C1 — Data layer reshape (commit `a433703`):** Executed via PM-ratified **alongside-and-non-breaking pattern** after I surfaced the 11→4 cardinality conflict via AskUserQuestion (rename `ages.json` → `tiers.json` would break `prototype/index.html` ageIdx model). PM picked Recommended option to add new files alongside legacy; full removal deferred to C6 dead-code pass after C3-C5 dismantle the age-loop UI. Same pattern applied unilaterally to commanders.json (3 civ commanders added alongside the 5 legacy Ash/Nature/Prayer commanders; all 8 playable).

**Files added (4 new):**
- [`prototype/data/civilizations.json`](prototype/data/civilizations.json) — 3 civs (Greek/Aztec/Norse) with locked content skeleton from 2026-04-25 ratification (6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods per civ; kebab-case slugs as IDs + verbatim labels; palette/glyph as working placeholders pending styling pass).
- [`prototype/data/fusion-recipes.json`](prototype/data/fusion-recipes.json) — 9 locked recipes (3 per civ) with 2-type damage profile per attack-type decision; Thor Slashing+Crushing dissonance reaffirmed as Follow-up #6.
- [`prototype/data/attack-types.json`](prototype/data/attack-types.json) — 7-type taxonomy + 5 armor tags + RPS matrix (+25%/-25%) + per-tower/per-demigod type assignments per 2026-04-26 attack-type-mapping decision; Poison locked stacking exception (5 stacks).
- [`prototype/data/tiers.json`](prototype/data/tiers.json) — 4-tier ladder (T1 swarm / T2 mainline / T3 elite / T4 Demigod) + Fusion meta-entry (`isATier: false`).

**File modified:** [`prototype/data/commanders.json`](prototype/data/commanders.json) — Leonidas / Montezuma II / Ragnar Lothbrok added with locked signature-ability names from 2026-04-25 (Spartan Training + This Is Sparta! + The Last Stand / Blood Tribute + Sun Offering + The Great Sacrifice / Sons of Ragnar + Berserk + The Great Heathen Army), epithets, lore, 12-line VO banks (4×3 shape: pick/victory/defeat/ability), 20-level XP ladders, 3 cosmetic slots (skin/frame/mapTint). Legacy `commander-a..e` preserved unchanged.

**Lint extended:** [`tools/cascade-lint.py`](tools/cascade-lint.py) — schema checks for civilizations/fusion-recipes/attack-types/tiers + cross-file integrity (3 civs × 6/5/6/3 cardinality; 9 recipes; 7 types + 5 armors; 4 tiers + non-tier fusion meta; god ID set match between civilizations and recipes). cascade-lint clean throughout: `next-open-step: Step 5; clean.`

**Untouched:** ages.json, towers.json, index.html boot loader (per alongside pattern — running prototype still boots cleanly off legacy data). §2.4a + §5.4 [LOCKED] surfaces untouched. Locked content-skeleton names from 2026-04-25 ratification untouched.

---

## Commits this session

- `6afdce3` — ratify prototype reshape plan — Proposed → Accepted (2026-04-29). Dual-pushed.
- `a433703` — C1 — Data layer reshape (inert) — alongside-and-non-breaking. Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS oldest-entry archive trim + CASCADE pointer/version bump.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `a433703` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27, 8 steps).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28, Follow-up #10 CLOSED).
- **Prototype reshape plan: RATIFIED** (2026-04-29). Effective execution order: **C1 ✓ → C2 → C3 → C4 (incl. Cast-bar) → C5 → C7.a → C7.b → C6**.
- **C1 Data layer: LANDED** (2026-04-29 continuation, alongside pattern).
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (2026-04-29 C1 LANDED + 2026-04-29 RATIFIED + 2026-04-28 §5.4 amendment); 2026-04-27 commander-avatar continuation entry archived this handoff.
- `CASCADE.md` pointer: most recent block only (v0.30, C1 LANDED); prior 2026-04-29 ratification block archived.
- `CASCADE.md` version footer: 2 most recent bumps only (v0.30 + v0.29 reference).
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#5 — Cultural-sensitivity pass.** Hard pose-lock gate on C2 silhouettes. Independent track; not a gate on plan execution itself. Working labels acceptable for non-pose-lock content.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1 [PROPOSAL] numbers (RPS magnitudes, tier costs, etc.).
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

---

## NEXT SESSION — primary directive

**C2 — Silhouette 5→3 SVG migration.** PM "go" required before any work.

**C2 scope** (from [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md)): migrate the 5-lineage SVG silhouettes in `prototype/index.html` to 3 civ-coded silhouettes (Greek / Aztec / Norse). **Cultural-sensitivity gate** (Follow-up #5) is a **hard pose-lock gate** on this step — abstract-placeholder geometric shapes are acceptable for the silhouette-test harness; civ-specific pose locks must wait on the cultural-sensitivity review.

**Cadence:** propose C2 plan → PM "go" → produce → verify (`python tools/cascade-lint.py`) → tick. Single PM-gated step per HANDOFF protocol.

### Background candidates (if PM redirects)

1. **C2** (Recommended — next on plan order).
2. Cultural-sensitivity pass scheduling (Follow-up #5) — would unblock C2 pose-lock.
3. Patch-1 commanders per civ (Follow-up #6).
4. `admin/concept.json` migration direction.
5. Other follow-ups #7 / #8 / #9 / #4 / #13.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).
- Legacy `prototype/data/ages.json`, `prototype/data/towers.json`, `prototype/index.html` boot loader — DO NOT touch until C3-C5 dismantle the age-loop UI; full removal at C6.
- Legacy `commander-a..e` entries in `commanders.json` — preserved alongside the 3 civ commanders; remove at C6 dead-code pass.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM standing directive 2026-04-28).
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** when a reshape step would break running surfaces, add new canonical files alongside legacy; legacy stays running until later dismantle/dead-code steps. Surface cardinality conflicts to PM via AskUserQuestion before unilateral action.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — primary directive C2 (Silhouette 5→3 SVG migration).

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: ratification commit
  6afdce3 + C1 commit a433703 both dual-pushed; reshape plan
  Accepted 2026-04-29; C1 Data layer LANDED via alongside-
  and-non-breaking pattern (4 new prototype data files +
  commanders.json migration; ages.json + towers.json +
  index.html boot loader untouched; legacy commander-a..e
  + 3 civ commanders all playable).
- Open blockers: cultural-sensitivity pass (Follow-up #5)
  is a HARD POSE-LOCK GATE on C2; abstract geometric
  placeholders acceptable for harness.
- Specific next-step proposal: surface C2 plan via
  AskUserQuestion with Recommended first option (default:
  proceed with abstract geometric placeholders for silhouette-
  test harness; defer civ-specific pose locks to post-
  cultural-sensitivity-pass).

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.
ALONGSIDE-AND-NON-BREAKING pattern (PM-ratified 2026-04-29):
when a step would break a running surface, add alongside;
surface cardinality conflicts via AskUserQuestion before
unilateral action.

EXECUTION ORDER on standby (one PM gate per step):
  C2 → C3 → C4 (incl. Cast-bar) → C5 → C7.a → C7.b → C6.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- Legacy ages.json / towers.json / index.html boot loader
  DO NOT TOUCH until C3-C5 dismantle the age-loop UI;
  full removal at C6 dead-code pass.
- Legacy commander-a..e preserved alongside the 3 civ
  commanders; remove at C6.

If PM redirects off C2, fall back to background candidates:
cultural-sensitivity pass scheduling (Follow-up #5),
patch-1 commanders per civ (Follow-up #6), admin/concept.json
migration direction, follow-ups #7/#8/#9/#4/#13.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock gate on C2.
- A reshape step would silently break a running surface (use alongside pattern + AskUserQuestion instead).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
