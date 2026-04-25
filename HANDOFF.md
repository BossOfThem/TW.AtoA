# HANDOFF — Session Checkpoint

**Last session:** 2026-05-01 — C5 + C7.a + C7.b LANDED (C7.b across two slices).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Four pure-additive prototype passes landed under the alongside-and-non-breaking pattern, all dual-pushed. C5 + C7.a + C7.b are now complete (C7.b across two slices).** Per PM "go" gates per step.

1. **C5 — Codex modal: 7×5 attack-type vs armor RPS matrix (commit `95165b9`).** Tutorial + match HUD each gain a 📖 Codex button → opens `.codex-modal` with `<table class="cx-grid">`: 7 attack-type rows × 5 armor-tag columns; cells colored `.strong` (+25%, green) / `.weak` (-25%, red) / `.neutral` (1.0×); status-proc legend below grid + bonus/penalty footnote. Reads inlined `ATTACK_TYPES` constant sourced verbatim from [`prototype/data/attack-types.json`](prototype/data/attack-types.json) (Piercing/Slashing/Crushing/Fire/Poison/Arcane/Divine; armor tags Unarmored/Shielded/Beast/Spirit/Colossal). `openCodex()` / `closeCodex()` + Esc handler. ~70 lines JS + 24 lines CSS, all alongside; no balance wiring, no tower-card mutation.

2. **C7.a — Gut persistent on-field commander avatar (commit `6063520`).** 12 commander-avatar surfaces commented-out (NOT deleted) with dated `// SUPERSEDED 2026-04-27 (C7.a)` markers preserving full code as raw material for C7.b/C6: `initMatch` commander state line + 5-field `game.commander` struct; KeyQ + KeyC handlers; net commander-move/-sig handlers (`if (false &&...)`); net snapshot build sets `commander: null` + apply block wrapped; `onBoardClick` Shift+click branch; `commanderAuraEffectOn` / `moveCommanderTo` / `fireCommanderSignature` function bodies; `startWave` movedThisWave reset; tick-block (cd timer + knock-back); render-block (aura + avatar). `towerStats` aura mul replaced with neutral identity values (`{damage:1, cd:1, range:1, active:false}`) so tower math stays unaffected.

3. **C7.b slice 1 — Cast-emerge pipeline (commit `ae28e1d`).** Restored minimal `commander: { castState, castTarget, castTtl }` struct in `initMatch`. Added `CAST_DURATIONS = { short: 72, long: 168, signature: 270 }` (frames @ 60Hz ~= ~1.2s/~2.8s/~4.5s per 2026-04-27 spec; `slot === "long"` → signature tier). Hook in `castAbility(slot)` sets `castState/castTarget/castTtl`. Tick decrements ttl + clears state at zero. Render: civ-paletted `renderSilhouette()` 1.4× at `game.path[0]` while cast active; signature outer pulsing ring; reduce-motion → gold ring pulse only. Net snapshot build/apply syncs all three fields.

4. **C7.b slice 2 — BuilderUnit class (commit `817d048`).** `builders: []` array added to `initMatch` state (after commander struct). Spawn hook in `placeTower` pushes `{x, y, target:{x,y}, ttl:120, totalTtl:120, civ, tier:1}` from `path[0]` toward placed cell center. Tick lerps x/y by `1 - (ttl/totalTtl)`, decrements ttl, filters out ttl<=0. Render draws small 4px dot + 7px accent ring per builder, civ-tinted via `CIV_PALETTE` or neutral slate `{primary:"#94a3b8", accent:"#cbd5e1"}` for legacy commander-a..e (no `civ` field). Snapshot build slices to 32 + applies on guest. Builder concurrency cap + 90% refund-on-cancel deferred (no cancel UI surface yet).

**Untouched everywhere:** legacy `prototype/data/ages.json` + `prototype/data/towers.json` + `prototype/index.html` boot loader; legacy `commander-a..e` entries; `silhouetteSVG()` legacy; tower buy/upgrade/sell/place/attack logic; age-up logic. §2.4a + §5.4 [LOCKED] surfaces untouched. 2026-04-25 locked content-skeleton names untouched. cascade-lint clean throughout (`next-open-step: Step 5; clean.`).

**C4-continuation deferred items** (need civ-tower placement wiring): merge-preview ghosts, Promote-to-T4 button, tower-card tier+type stamp. Queued before or alongside C6.

---

## Commits this session

- `95165b9` — C5 — Codex modal: 7×5 attack-type vs armor RPS matrix (alongside). Dual-pushed.
- `6063520` — C7.a — Gut persistent on-field commander avatar (alongside, comment-out). Dual-pushed.
- `ae28e1d` — C7.b slice 1 — cast-emerge pipeline (cast-bar → transient avatar at home anchor). Dual-pushed.
- `817d048` — C7.b slice 2 — BuilderUnit class (spawn-lerp-despawn + builders snapshot). Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS trim + CASCADE pointer/version bump v0.31 → v0.32.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `817d048` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (decision 2026-04-27; prototype implementation across C7.a + C7.b this session).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape plan: RATIFIED** (2026-04-29). Effective execution order: **C1 ✓ → C2 ✓ → C3 ✓ → C4 ✓ (slice; continuation deferred) → C5 ✓ → C7.a ✓ → C7.b ✓ → C6**.
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (C7.b combined / C7.a / C5). Prior C2/C3/C4-slice archived.
- `CASCADE.md` pointer: most recent block only (v0.32, C5+C7.a+C7.b LANDED); prior C2+C3+C4-slice block archived.
- `CASCADE.md` version footer: 2 most recent bumps (v0.32 + v0.31 reference); v0.30 archived.
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#4 — Aztec glyph styling pass.** civilizations.json has `𓁹` (Egyptian eye) for Aztec — wrong civilization. C2 sidestepped by using geometric primitives. Fix in dedicated styling pass; do not surface in silhouettes/HUD until corrected.
- **#5 — Cultural-sensitivity pass.** Hard pose-lock gate on civ silhouettes. Remains a content-lock-gate before any pose-locked / culturally-coded art ships.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 [PROPOSAL] numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts).
- **C4-continuation deferred items** — merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp. Need civ-tower placement wiring; queued before or alongside C6.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI surface. Queued for C6 or post-C6 polish.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

---

## NEXT SESSION — primary directive

**C6 — dead-code sweep.** PM "go" required before any work.

**C6 scope** (from [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) + 2026-04-27 amendment): final reshape step. Removes the alongside-discipline scaffolding now that C2-C5 + C7.a/b have all graduated:
- Delete the 12 commented-out commander-avatar surfaces (`// SUPERSEDED 2026-04-27 (C7.a)` markers).
- Delete legacy `silhouetteSVG()` (now fully replaced by `civSilhouetteSVG()` for civs).
- Delete legacy `commander-a..e` entries from `commanders.json`.
- Delete legacy `prototype/data/ages.json` + `prototype/data/towers.json` (or reshape into civ-aware data layer per the new tiers/civilizations files).
- Delete legacy boot-loader fetches for ages.json/towers.json + inline fallbacks.
- Tear down age-up logic / Knowledge resource / age-gate UI now that Tribute+Divinity is the live economy.
- Tear down 5-lineage tower buy/upgrade/sell wiring (will be replaced by civ-tower placement track — gated by C4-continuation decision).

**Critical sequencing question — surface to PM via AskUserQuestion before unilateral C6 work:**
The legacy 5-lineage tower placement system is what currently drives playable matches. Removing it requires either (a) shipping civ-tower placement first as part of C6 (or as C4-continuation interleaved with C6), or (b) accepting that the prototype is non-playable for a window. Recommend option (a): combine C6 with the C4-continuation civ-tower placement track so the prototype stays playable through the transition.

**Cadence:** propose plan → PM "go" → produce → verify (`python tools/cascade-lint.py`) → tick. Single PM-gated step per HANDOFF protocol.

### Background candidates (if PM redirects)

1. **C6** (Recommended — final step on plan order; needs sequencing AskUserQuestion).
2. **C4-continuation only** — merge-preview / Promote-T4 / tower-card stamp first, defer C6.
3. Cultural-sensitivity pass scheduling (Follow-up #5).
4. Patch-1 commanders per civ (Follow-up #6).
5. `admin/concept.json` migration direction.
6. Other follow-ups #7 / #8 / #9 / #4 / #13.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).
- C7.a comment-out markers stay as-is until C6 explicitly deletes them — do NOT silently delete or uncomment outside a C6 "go".

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM standing directive 2026-04-28).
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** when a step would break running surfaces, add new code/files alongside legacy; surface cardinality conflicts to PM via AskUserQuestion before unilateral action. C6 is the explicit graduation point — alongside scaffolding is removed only on PM go.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.
- **Context-pressure self-trim:** when context budget tightens, trim step scope to pure-additive surfaces and document deferred items as continuation work (precedent: C4 slice + C7.b two-slice split).

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — primary directive C6 (dead-code sweep).

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: C5 (95165b9) +
  C7.a (6063520) + C7.b slice 1 (ae28e1d) + C7.b slice 2
  (817d048) all dual-pushed via alongside-and-non-breaking
  pattern. Codex modal + commander-avatar gutted (12
  comment-out markers) + cast-emerge pipeline +
  BuilderUnit class all live. Legacy 5-lineage data +
  boot loader + commander-a..e + silhouetteSVG() all
  preserved alongside, awaiting C6 graduation.
- Open blockers: C6 sequencing question — removing legacy
  5-lineage tower placement breaks playability unless
  civ-tower placement (C4-continuation) ships first or
  alongside. Surface to PM via AskUserQuestion with
  Recommended option (a) C6 bundled with C4-continuation
  civ-tower placement track to preserve playability.
- Specific next-step proposal: surface C6 plan via
  AskUserQuestion with Recommended first option —
  bundled C6 + C4-continuation civ-tower placement so
  prototype stays playable through alongside-graduation.
  Alternate: C4-continuation only (defer C6); or C6
  staged in two passes (markers/silhouetteSVG/cmdr-a..e
  first, then 5-lineage placement teardown).

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.
ALONGSIDE-AND-NON-BREAKING pattern (PM-ratified 2026-04-29):
C6 is the explicit graduation point — alongside scaffolding
is removed only on PM go after sequencing question is answered.

EXECUTION ORDER on standby (one PM gate per step):
  C6 (final) — possibly bundled with C4-continuation.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- C7.a `// SUPERSEDED 2026-04-27 (C7.a)` markers stay until
  C6 explicitly deletes; do NOT silently delete/uncomment.
- Aztec glyph "𓁹" in civilizations.json is wrong (Egyptian
  eye) — Follow-up #4; do not surface until corrected.

If PM redirects off C6, fall back: C4-continuation only,
cultural-sensitivity pass scheduling (Follow-up #5),
patch-1 commanders per civ (Follow-up #6),
admin/concept.json migration direction, follow-ups #7/#8/#9/#13.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock gate on any non-abstract civ art.
- A reshape step would silently break a running surface without an alongside fallback or AskUserQuestion gate.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
