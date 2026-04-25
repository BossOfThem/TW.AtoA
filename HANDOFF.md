# HANDOFF — Session Checkpoint

**Last session:** 2026-05-04 (end-of-day, **clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

12-round end-to-end conceptual ratification of tower-vs-unit math + auxiliary economy + game-mode ontology, completed in a single session under the "Go big, no scope cuts" project doctrine.

**Two arcs ran:**

- **Arc 1 (Rounds 1–5)** — Balance-pass #1 conceptual frame RATIFIED (17 items; master damage equation; round typology; (k) compounding; sell-refund; targeting; boss reward; interim Divinity source; skill-bar axes). Filed [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) (Accepted, Medium).
- **Arc 2 (Rounds 6–12)** — Auxiliary economy + 6-mode ontology RATIFIED. 7 new decision documents. Mode count expanded 5 → **6** (Horde split into A "Lane Defense" + B "Shared Front"). Frame items #3 (master equation extended with variable (s)) and #12 (lives per-mode declarable; PvP-IW=30) amended via dated entries. Project doctrine "Go big, no scope cuts" ratified.

**No code edits.** Pure concept/math work. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched.

**Numbers-phase Follow-up #13 is now fully unblocked.**

---

## What is locked (clear-safe)

### Balance-pass #1 conceptual frame (17 items, Round 1–5)

| # | Item | Locked |
|---|------|--------|
| 1 | (k) difficulty | Easy / Hard / Hardcore (3 tiers; PvE-only — see Round 12) |
| 2 | Win condition | Lives > 0 at end of R30 (PvE); last-alive (PvP) |
| 3 | Damage form | `Σ_T [DPS(T) × t_engaged(T,R) × matchup × passive_modifiers × status_state × s(T,R)]` (variable (s) added Round 12) |
| 4 | (o) Divinity | First-class second currency; cap 6/match; drain 2 (Fusion menu) + 1×N (per fusion) |
| 5 | (l) lifecycle | Tier × Level both axes. Tier {T1,T2,T3,T4,God}; Level {1,2,3}. Stone→T1 (PvP Maze only). |
| 6 | (k) compounding | Single-axis exponent shift on HP-curve only |
| 7 | Commander (h) | 3 slots × 4 effect types (damage / control / summon / economy) |
| 8 | Status + armor | (p) 5-bucket armor + (q) 7-proc status full feedback |
| 9 | Round slot typology | 7-slot (Standard / Swarm / Elite / Modifier / Telegraph / Boss / Recovery) |
| 10 | R-assignments | R5 Modifier · R10 Boss · R15 Elite · R20 Modifier · R25 Telegraph · R30 Final Boss |
| 11 | (j) map model | Per-map (ε, N) tuple |
| 12 | Lives | **Per-mode declarable** (default 10; PvP-IW=30) — amended Round 9 |
| 13 | Sell refund | Pre-wave 100% / same-wave 90% / R+1 80% / R+2 70% / R+3+ 60% flat. T4 capped 60%. (k)-coupled. |
| 14 | Targeting | AI default First; per-tower override {First / Last / Strongest / Weakest / Closest} |
| 15 | Boss reward | R10 medium + 1 Div · R15 medium + 0 Div · R30 huge + 2 Div |
| 16 | Divinity source (interim) | R10/+1 · R20-streak/+1 · R30/+2 · 2 hooks TBD; Foresight-coin Follow-up #7 final |
| 17 | Skill bars | matchup-rate / placement-coverage / ability-uptime |

### 6-mode roster (Rounds 7–11)

| Mode | Lanes | Lives | Send-Creeps | Aux slots beyond Universal | Win | (k)? |
|------|-------|-------|-------------|----------------------------|-----|------|
| Solo Campaign | 1 (authored) | 10 | — | — | R30 alive | Per-mission |
| Horde-A Lane Defense | N adjacent + leak-bleed | 10/player | — | — | R30 alive (any) | Yes |
| Horde-B Shared Front | 1 shared, N-scaled map | 10 shared | — | — | R30 alive | Yes |
| PvE Multiplayer | N parallel | 10/player | Lane-Trade | Call-for-Help | Last alive | Yes |
| PvP Interest Wars | N (per-player, free target sends) | **30**/player | Send-for-Interest | — | Last alive (tie-escalation, co-victory possible) | **No** (player-driven) |
| PvP Maze | N (per-player, free target sends) | 10/player | Send-Through-Maze | Maze Stone | Last alive | **No** (player-driven) |

### Auxiliary economy structure (Round 6 + Round 12)

- **Architecture:** modular slot system; one universal panel/surface; mode-aware slot inventory.
- **UX:** in-match side-panel, always visible, real-time access (works for PvP-IW 20s cadence).
- **Currency split:** Tribute (tactical slots: targeting, build-queue, lifecycle, send-one-shot) + Divinity (strategic slots: tower-count, sustained Damage Bonus, sustained Economy Bonus, Send-for-Interest, fusion-choice).
- **Universal slot families (all 6 modes):** Targeting Override · Build-queue · Tower-count expansion · Lifecycle (level/upgrade/fusion choice) · Damage Bonus · Economy Bonus.
- **Send-Creeps cross-mode classification:** **3-mode mechanic** (PvE-MP Lane-Trade · PvP-IW Send-for-Interest · PvP-Maze Send-Through-Maze). NOT in Solo or Horde.
- **Co-op send-mechanics safety:** helpful-only in Co-op modes; harmful exclusive to PvP modes.

### Project doctrine — "Go big, no scope cuts" (Round 6)

PM verbatim: *"We are going big or go home, there is no 'lessen load on devs' we are VERY capable and WILL complete this project regardless of scope. I can take 3 years if i have to."*

- Every conceptually ratified system ships at v1.0; no launch-surface cuts.
- Patch-1+ reserved for additive content (new commanders/civs/modes), never v1.0 backfill.
- Three-year horizon acceptable. Schedule pressure not grounds for scope cut.
- Recommended-first options should NOT be selected for dev-load reduction; design merit only.
- Scope expansion mid-design is normal under this doctrine; MD-first preservation is the safety rail.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest pushed commit: `5a7ab29` (mid-session balance-pass-frame + aux-economy-scope, dual-pushed).
- **This session's end-of-day work uncommitted as of HANDOFF write.** Files staged for next commit:
  - 7 new decision files: `decisions/2026-05-04-round-{6,7,8,9,10,11,12}-*.md`
  - `decisions/2026-05-04-auxiliary-economy-and-modes-scope.md` (Status Proposed → Accepted)
  - `CASCADE.md` (pointer + 7 new decisions-table rows + version v0.36→v0.37)
  - `CASCADE-history.md` (2 archived pointer blocks)
  - `PROGRESS.md` (new entry + trim to 3 most recent)
  - `PROGRESS-archive.md` (2 archived entries)
  - `CONCEPT-GAPS.md` (ECON-04 + MODE-01 → RESOLVED)
  - `HANDOFF.md` (this rewrite)
- Working tree dirty pending commit + dual-push.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape arc: COMPLETE** (2026-05-04 earlier).
- **Balance-pass #1 conceptual frame: RATIFIED** (2026-05-04 mid).
- **Auxiliary economy + 6-mode ontology: RATIFIED** (2026-05-04 end-of-day).
- **Numbers-phase Follow-up #13: FULLY UNBLOCKED** — frame + extensions all locked.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (end-of-day · mid-session · earlier-2026-05-04). 2026-05-03 + 2026-05-02 archived.
- `CASCADE.md` pointer: 1 most-recent block (end-of-day). Mid-session + earlier-2026-05-04 archived.
- `CASCADE.md` version footer: v0.37 + v0.36 reference.
- `CONCEPT-GAPS.md`: 11 active gaps + 3 resolved (ECON-04 RESOLVED, MODE-01 RESOLVED, MATH-01 RESOLVED).

### Open follow-ups (carried)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art).
- **#6** — Patch-1 commanders + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes — narrowed Round 6 to Phase-3-onward meta-progression artifact only (no in-match currency role).
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **#11** — Norse round-30 boss CLOSED at Jörmungandr.
- **#13 — Numbers-phase balance-pass — FULLY UNBLOCKED.** Consumes the locked frame + extensions to produce ratified values for: (a)/(c)/(e)/(f) curves; (g) magnitudes; (h) ability magnitudes; (k) HP-curve exponent values; (j) per-map (ε, N); skill-bar thresholds; **+ aux-slot costs (Tribute + Divinity); + Send-Creeps income-yield curves per mode; + per-mode lives values; + tie-break escalation curve (PvP-IW); + (s) auxiliary multiplier ranges; + Lane-Trade refund tuning; + stone-cost / stone→T1 upgrade math (PvP Maze)**.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape.
- **CONCEPT.md amendment pending** — §-new "Game modes" (6 modes) + §-new "Auxiliary economy structure" (slot inventory + UX + currency split + per-mode enablement table) + §-amend master damage equation with (s).
- **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / Bloons TD 6 / Element TD / Line Tower Wars / Mini-TD deep dives.

### Phase 4 engine architecture concerns surfaced (load-bearing post-12-round)

- A* hex-graph pathfinding + dynamic edge updates (PvP Maze; placement-validity check; Send-Through-Maze).
- Real-time PvP netcode (PvP-IW 20s simultaneous rounds; PvP Maze).
- In-match side-panel HUD layout (universal aux UX).
- View-only spectate primitive (PvE-MP + PvP-IW share it).
- Parameterized N-scaling map authoring (Horde-B).
- Per-player adjacent-lane bleed mechanic (Horde-A).
- Hand-authored mission map pipeline (Solo Campaign; ~12-20 missions).

### Regression-watch (from prior cuts; unchanged this session)

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.

---

## NEXT SESSION — primary directive

**Pick one of these tracks** (PM choice; Recommended first):

1. **(Recommended) Numbers-phase Follow-up #13** — surface AskUserQuestion-driven number ratification rounds. Likely 5-10 rounds covering: (a)/(c)/(e)/(f) curves, (g) magnitudes, (h) abilities, (k) exponent values, per-map (ε, N), skill-bar thresholds, aux-slot costs, Send-Creeps income curves, per-mode lives, tie-break escalation curve, (s) multiplier ranges, Lane-Trade refund, stone math.
2. **CONCEPT.md amendment pass** — roll the 12-round ratifications into CONCEPT.md as §-new sections. Authoring-heavy, lower-decision-density work.
3. **Research pass** — `research/06-tw-subgenres.md` deep-dive on Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD. Validates assumptions made in the 12-round pass; rigorous but slow.
4. **`admin/concept.json` migration** — long-deferred staleness debt.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]**.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton.
- The 17-item conceptual frame (with Round 9 + Round 12 amendments) is **Accepted**. Revisions require superseding decisions.
- The 6-mode ontology + auxiliary economy structure (Rounds 6-12) is **Accepted**.
- The "Go big, no scope cuts" project doctrine is **Accepted**.

---

## Cadence rules carried forward

- **Cadence exists to manage the context window, not to gate every step.** Concrete plan = execute end-to-end; gate via AskUserQuestion only on genuine ambiguity.
- **AskUserQuestion is the standard interface** (PM 2026-05-04 directive). Almost every conceptual conversation should surface options via the tool. Always Recommended-first.
- **MD-first preservation** (PM 2026-05-04 directive) — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — 12-round conceptual ratification COMPLETE end-of-day
2026-05-04. Balance-pass #1 frame + auxiliary economy + 6-mode ontology +
frame extension (variable (s); per-mode lives) all RATIFIED across 8
decision documents. "Go big, no scope cuts" project doctrine ratified.
Numbers-phase Follow-up #13 fully unblocked.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: 12-round ratification complete; numbers-phase #13 unblocked;
  CONCEPT.md amendment pending; admin/concept.json staleness debt outstanding;
  research/06-tw-subgenres.md not yet written.
- Open blockers: none load-bearing.
- Specific next-step: surface AskUserQuestion with Recommended-first
  options for the four tracks listed in HANDOFF "NEXT SESSION" section.
  Recommended track = Numbers-phase Follow-up #13.

CADENCE: AskUserQuestion is the standard interface. Recommended-first
on every option. MD-first preservation on scope expansions. Execute
end-to-end when plan concrete; gate on genuine ambiguity.

CURRENCY REMINDER: Tribute (primary, kills) + Divinity (secondary,
cap 6/match, drain 2 + 1×N for Fusion). NOT "gold."

DOCTRINE REMINDER: "Go big, no scope cuts." Do NOT recommend the
smallest-scope option for dev-load reduction; recommend on design
merit only.

REGRESSION-WATCH: Tutorial / match flow / merge-preview / Promote-T4
indicator / Aztec glyph ◈ / logBalanceCurve / effectiveTowerStats /
snapshot — unchanged.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 locked content skeleton
  untouched.
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract civ art.
- 17-item frame (with Round 9 + Round 12 amendments) Accepted.
- 6-mode ontology + auxiliary economy structure Accepted.
- "Go big, no scope cuts" doctrine Accepted.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
- The 17-item frame would be silently edited.
- A scope expansion occurs and PM has not landed it in MD before further questions.
- Any recommendation invokes "lessen dev load" without explicit PM override of the "Go big" doctrine.
- A balance-pass numbers commit lands without a `decisions/<date>-balance-pass-N-numbers.md` entry capturing [PROPOSAL] → ratified-numbers diff.
