# HANDOFF — Session Checkpoint

**Last session:** 2026-04-30 — C2 + C3 + C4 (slice) LANDED.
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Three pure-additive prototype passes landed under the alongside-and-non-breaking pattern, all dual-pushed.** Per PM "go" gates with bypass-permissions extension through C3 and explicit handoff heads-up before C4 ("context window still getting full quickly").

1. **C2 — Silhouette 5→3 SVG migration (commit `cd376f1`).** Added `civSilhouetteSVG(civId)` + `commanderSilhouetteSVG(c)` + `commanderSilhouetteColor(c)` alongside legacy `silhouetteSVG()`; civ-aware dispatch routes civ commanders to civ silhouettes (Greek triangle / Aztec hexagon / Norse diamond) and legacy commander-a..e to legacy lineage silhouettes. `CIV_PALETTE` constant inlined (Greek blue+gold / Aztec green+red / Norse slate+light-slate). **Cultural-sensitivity gate honored** via abstract geometric primitives (no glyphs/poses); skipped using civilizations.json glyphs because the Aztec entry is "𓁹" (an Egyptian eye — flagged Follow-up #4 styling pass). 3 call sites updated: roster chip, portrait card, HUD silhouette. `?silhouette-test=1` harness still works for both 5 legacy + 3 civ silhouettes (8 tiles).

2. **C3 — Tribute + Divinity resource bar (commit `45ff858`).** Added two new HUD items in both tutorial and match scenes (Tribute + Divinity), plus a Fusion HUD button (disabled until `game.divinity >= 2`). Tribute = pure visual mirror of `game.gold` (legacy Gold + Knowledge keep running unchanged). Divinity = new state field (`game.divinity`, init 0, capped at 6 discrete pips matching the locked 30-round arc) added to both `initMatch` and `initTutorial` + Net snapshot build/apply for co-op sync. Wave-end hook on `game.wave % 5 === 0` boss rounds: increment Divinity (cap 6) + toast "+1 Divinity" + emit feed event. CSS vars `--tribute: #ca8a04; --divinity: #c084fc;` added. Legacy gold/knowledge HUD + tower buy/upgrade/sell + age-up logic untouched (C5/C6 territory).

3. **C4 (slice) — Fusion menu modal + Commander Cast bar (commit `ca2a5cf`).** Self-trimmed under context pressure to the two pure-additive surfaces. **Fusion modal:** 3 civ columns × 3 god cards reading inline `FUSION_RECIPES` (verbatim PM-locked sources/types: zeus/athena/poseidon/quetzalcoatl/huitzilopochtli/tezcatlipoca/odin/thor/tyr); click → `fusionExecute()` decrements `game.divinity` by 1 + toast stub. Opens via Fusion HUD button (gated `disabled` if divinity < 2); Esc closes. **Cast bar:** 3 buttons (cast-passive [decorative] / cast-short [8s decorative CD] / cast-long [18s decorative CD]) populated from `c.stats.passive/shortCdActive/longCdSignature` for civ commanders only via `renderCastBar()`; `castAbility(slot)` plays a random VO ability bark from `c.vo.ability` and triggers decorative CD lockout. Legacy commander-a..e show no cast bar (gracefully empty — no `civ` field).

**Untouched everywhere:** legacy `prototype/data/ages.json` + `prototype/data/towers.json` + `prototype/index.html` boot loader; legacy `commander-a..e` entries; tower buy/upgrade/sell/place/attack logic; age-up logic. §2.4a + §5.4 [LOCKED] surfaces untouched. 2026-04-25 locked content-skeleton names untouched. cascade-lint clean throughout (`next-open-step: Step 5; clean.`).

**C4-continuation deferred items** (need civ-tower placement wiring the legacy 5-lineage system lacks): merge-preview ghosts, Promote-to-T4 button, tower-card tier+type stamp. Queued either before C5 or interleaved per PM direction.

---

## Commits this session

- `cd376f1` — C2 — Silhouette 5→3 SVG migration (alongside, geometric placeholders). Dual-pushed.
- `45ff858` — C3 — Resource bar migration (Tribute + Divinity, alongside). Dual-pushed.
- `ca2a5cf` — C4 (slice) — Fusion menu modal + Commander Cast bar. Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS trim + CASCADE pointer/version bump v0.30 → v0.31.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `ca2a5cf` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape plan: RATIFIED** (2026-04-29). Effective execution order: **C1 ✓ → C2 ✓ → C3 ✓ → C4 ✓ (slice; continuation deferred) → C5 → C7.a → C7.b → C6**.
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (C4 / C3 / C2). Prior C1 LANDED + RATIFIED + §5.4 amendment archived.
- `CASCADE.md` pointer: most recent block only (v0.31, C2+C3+C4 slice LANDED); prior C1 LANDED block archived.
- `CASCADE.md` version footer: 2 most recent bumps (v0.31 + v0.30 reference); v0.29 archived.
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#4 — Aztec glyph styling pass.** civilizations.json has `𓁹` (Egyptian eye) for Aztec — wrong civilization. C2 sidestepped by using geometric primitives. Fix in dedicated styling pass; do not surface in silhouettes/HUD until corrected.
- **#5 — Cultural-sensitivity pass.** Hard pose-lock gate on civ silhouettes. C2 used abstract placeholders so this is no longer a near-term blocker, but it remains a content-lock-gate before any pose-locked / culturally-coded art ships.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 [PROPOSAL] numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations).
- **C4-continuation deferred items** — merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp. Need civ-tower placement wiring; queued before or alongside C5.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

---

## NEXT SESSION — primary directive

**C5 — 7×5 RPS indicator.** PM "go" required before any work.

**C5 scope** (from [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md)): surface the 7-attack-type × 5-armor-tag matrix from [`prototype/data/attack-types.json`](prototype/data/attack-types.json) in tooltip / codex / tower-card form so the +25%/-25% RPS layer is legible. Reads existing data; no balance changes. Pure-additive UI consistent with alongside discipline.

**Possible PM redirect: C4-continuation first.** If the PM wants the deferred Fusion-related items (merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp) before C5, those each require civ-tower placement wiring — not a strict-additive surface. Will need an AskUserQuestion gate on whether to (a) introduce a civ-tower placement track alongside the legacy 5-lineage placement, or (b) wait until the legacy placement is dismantled at C5/C6.

**Cadence:** propose plan → PM "go" → produce → verify (`python tools/cascade-lint.py`) → tick. Single PM-gated step per HANDOFF protocol.

### Background candidates (if PM redirects)

1. **C5** (Recommended — next on plan order; pure-additive read of attack-types.json).
2. **C4-continuation** — merge-preview / Promote-T4 / tower-card stamp. Needs civ-tower placement wiring decision.
3. Cultural-sensitivity pass scheduling (Follow-up #5).
4. Patch-1 commanders per civ (Follow-up #6).
5. `admin/concept.json` migration direction.
6. Other follow-ups #7 / #8 / #9 / #4 / #13.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).
- Legacy `prototype/data/ages.json`, `prototype/data/towers.json`, `prototype/index.html` boot loader — DO NOT touch until C5/C6 dismantle the age-loop UI; full removal at C6.
- Legacy `commander-a..e` entries in `commanders.json` — preserved alongside the 3 civ commanders; remove at C6 dead-code pass.
- Legacy `silhouetteSVG()` — kept alongside `civSilhouetteSVG()`; remove at C6 dead-code pass.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM standing directive 2026-04-28).
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** when a step would break running surfaces, add new code/files alongside legacy; surface cardinality conflicts to PM via AskUserQuestion before unilateral action.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.
- **Context-pressure self-trim:** when context budget tightens, trim step scope to pure-additive surfaces and document deferred items as continuation work (precedent: C4 slice this session).

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — primary directive C5 (7×5 RPS indicator).

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: C2 (cd376f1) +
  C3 (45ff858) + C4 slice (ca2a5cf) all dual-pushed via
  alongside-and-non-breaking pattern. Civ silhouettes
  (geometric placeholders) + Tribute/Divinity HUD +
  Fusion menu modal + Commander Cast bar all live.
  Legacy 5-lineage data + boot loader + commander-a..e
  + silhouetteSVG() all preserved alongside.
- Open blockers: C4-continuation items (merge-preview /
  Promote-T4 / tower-card tier+type stamp) need civ-tower
  placement wiring — surface to PM via AskUserQuestion
  before either of: (a) starting C4-continuation, or
  (b) starting C5 (which may also touch tower cards).
- Specific next-step proposal: surface C5 plan via
  AskUserQuestion with Recommended first option — read
  attack-types.json + render the 7×5 matrix in tooltip
  /codex form; pure-additive; no balance changes.
  Alternate option: C4-continuation first.

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.
ALONGSIDE-AND-NON-BREAKING pattern (PM-ratified 2026-04-29):
when a step would break a running surface, add alongside;
surface cardinality conflicts via AskUserQuestion before
unilateral action.

EXECUTION ORDER on standby (one PM gate per step):
  C5 → C7.a → C7.b → C6
  (C4-continuation can interleave per PM direction).

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- Legacy ages.json / towers.json / index.html boot loader
  / commander-a..e / silhouetteSVG() preserved alongside;
  full removal at C6 dead-code pass.
- Aztec glyph "𓁹" in civilizations.json is wrong (Egyptian
  eye) — Follow-up #4; do not surface until corrected.

If PM redirects off C5, fall back: C4-continuation,
cultural-sensitivity pass scheduling (Follow-up #5),
patch-1 commanders per civ (Follow-up #6), admin/concept.json
migration direction, follow-ups #7/#8/#9/#13.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock gate on any non-abstract civ art.
- A reshape step would silently break a running surface (use alongside pattern + AskUserQuestion instead).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
