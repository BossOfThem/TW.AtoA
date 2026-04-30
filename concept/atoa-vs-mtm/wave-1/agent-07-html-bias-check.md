# AGENT-07 — HTML BIAS AUDIT

**Agent 7 of 10 | Wave 1 Swarm | 2026-04-27**

## THE OPTIMISM GAP

The prototype reads complete on surface but is incomplete where it matters: **Fusion = stub toast, no God spawn. Mode-select copy references obsolete "11-age arc." Five lineages hard-obsoleted to 3 civs. Commander abilities have zero targeting spec. Cosmetic unlocks are dead-ends. Reference panel crashes when civ is falsy.**

The prototype is a high-fidelity UI vehicle with playable tower-placement underneath — beyond Demigod promotion, endgame is *concept*, not *delivery*.

---

## TOP 5 FINDINGS BY NORTH-STAR RELEVANCE

### 1. FUSION EXECUTION STUBBED (5/5)
- **Source:** `index.html` ln 2378-2387
- **Issue:** Menu works, execution = `toast("[stub]")`, no God unit spawn
- **Risk:** Port assumes complete, discovers spec gap at integration

### 2. FIVE LINEAGES OBSOLETED TO 3 CIVS (5/5 + 5/5 + 2/5)
- **Source:** `civilizations.json` (3 civs only), 2026-04-25 decision
- **Issue:** No Sinew/Ember/Forge/Crown/Veil; no economy pillar mechanics
- **Risk:** Port designs for 5 lineages, discovers they're gone

### 3. COMMANDER ABILITY TARGETING UNSPECIFIED (4/5)
- **Source:** `index.html` ln 666, 2482 ("targeting TBD")
- **Issue:** Cast UI complete, no spec for where avatar appears or what it does
- **Risk:** Signature ability is a UI button that does nothing; no spec to guide implementation

### 4. COSMETICS NON-FUNCTIONAL (3/5 + 3/5 + 3/5)
- **Source:** `index.html` ln 583-587 (markup only)
- **Issue:** L5/L10/L15 unlock chips appear, clicking = no-op, no equip UI
- **Risk:** Playtester earns unlock, clicks, nothing happens; credibility damage

### 5. MODE-SELECT STALE COPY (2/5)
- **Source:** `index.html` ln 495, 507, 513
- **Issue:** "11-age arc" and "one wave per age" (retired; 4-tier ladder replaces)
- **Risk:** Player reads "11-age," presses A for age-up (mechanic doesn't exist)

---

## SHADOW MATRIX (19 features audited)

5 ✅ In (tutorial, options, HUD, input, co-op wiring)
8 🟡 Partial (fusion, 4-tier, cosmetics, events, saves, tribut/divinity, reference-panel, spawn avatar)
6 ⬜ Out (lineages, god-phase, cosmetic-store, campaign-autosave, targeting-spec, complete co-op-persist)

---

## CRITICAL BLOCKERS FOR GODOT PORT

1. **Fusion God-Phase Spec**: Unit vs. passive? Tower reset post-god? Victory condition?
2. **Ability Targeting Model**: Area / line / unit / avatar-spawn? Final before implementation.
3. **Lineage Finality**: Hard-reversed forever, or Phase-2 SKU constraint (post-launch civs)?
4. **Cosmetics Pipeline**: Implement equip UI + store, or remove unlock chips + defer?
5. **Campaign Autosave Cadence**: Every age or every 5 ages? Determines file-write volume.

---

**Output:** `/c/TW.AtoA/concept/atoa-vs-mtm/wave-1/agent-07-html-bias-check.md`
