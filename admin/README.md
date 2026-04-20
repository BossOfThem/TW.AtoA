# Admin — Concept Map (v2)

A single-file, zero-dependency node-graph editor for the *Ash to Altar* concept. Lives here so the MD cascade and the visual map stay side-by-side.

> **Not the game.** If you're looking for a clickable slice of how the game will feel, see the sibling [`prototype/`](../prototype/) directory (throwaway design prototype). This `admin/` tool is for editing the concept map itself.

## What you see

- [`index.html`](index.html) — the app. Double-click to open in any modern browser.
- [`concept.json`](concept.json) — the editable state. Seeded from `CONCEPT.md` on 2026-04-19.

## How to use it

### Open it

- Double-click `index.html`. It opens in your default browser.
- If the browser blocks `fetch` for `concept.json` (some do under `file://`), you'll still see the inline seed, and the app will tell you via the toast: *"Using inline seed"*. In that case use **File → Import concept.json…** and pick the file manually.

### Edit

- **Click any node** to open it in the right-side **Inspector**. Edit fields inline.
- **Drag nodes** to rearrange.
- **Scroll wheel** to zoom. **Click-drag empty canvas** (or middle-click, or space+drag) to pan.
- **+ Add ▾** — creates a new commander/lineage/hybrid/age/fork/mode/stage.
- **🔗 Connect** — toggles connect mode. Click source node, then target. Creates an edge.
- **Delete key** (or inspector → Delete) — removes the selected node and its edges.
- **Comments** — each node has a comments thread at the bottom of the Inspector. Add comments for Claude to read.
- **Session notes** — running commentary in the sidebar. Also visible to Claude on export.
- **Filters** — top-right checkboxes toggle node types on/off in the view.

### Save

- All edits auto-save to browser **localStorage**. Reopening the file restores your state.
- To give your edits back to Claude: **File → Export concept.json** → drop the downloaded file into this `admin/` folder (overwrite).
- **File → Reset from seed** restores from the disk `concept.json` (or built-in seed if disk read fails).
- **File → Copy JSON to clipboard** for a quick paste into chat.

## How Claude reads your edits

When you've exported and replaced `concept.json`, Claude reads it directly during the next session. Workflow:

1. You: edit in the UI → export → drop the file.
2. You: tell Claude "I updated concept.json — look at the commanders" (or similar).
3. Claude: reads `admin/concept.json`, diffs against memory, advises / flags / proposes.

Your **comments** and **session notes** are the cleanest way to route direct questions. Example: in a commander node's comments, write *"Is this archetype too close to LoL's Sett?"* — Claude will pick it up on the next read.

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| Click node | Select + open in Inspector |
| Click empty canvas | Deselect |
| Drag node | Move |
| Scroll wheel | Zoom |
| Space + drag / middle-click drag | Pan |
| `Esc` | Deselect / cancel connect mode |
| `Delete` | Delete selected node |

## Node types and what they mean

| Color | Type | Meaning |
|-------|------|---------|
| 🟣 Purple | Commander | Player identity. Tilts toward one lineage. [Stage 01](../stages/01-commander-pick.md). |
| 🔴 Red | Lineage | Mechanical role within a match. [CONCEPT §3.3](../CONCEPT.md). |
| 🟠 Gold | Hybrid | Cross-lineage unit unlocked by adjacency. [Stage 06](../stages/06-hybrids-fusion.md). |
| 🔵 Blue | Age | Tier of civilizational evolution. [Stage 05](../stages/05-age-evolution.md). |
| 🔷 Teal | Fork | Divergence-fork option at certain ages. |
| 🟢 Green | Mode | Game mode (Campaign, Skirmish, Horde, etc.). [Stage 02](../stages/02-mode-select.md). |
| ⚫ Gray | Stage | Player-journey stage. [stages/](../stages/). |

## Known limitations of v1

- Ugly on purpose. Functional only.
- No undo/redo — but `File → Reset from seed` is always there.
- No collision detection when auto-adding nodes; you may need to drag new ones out of a stack.
- Edges are always curves; no orthogonal routing.
- `concept.json` must be manually dropped back in; no direct-to-disk save (browser security).
- Mobile/touch not tested.

## Changelog

- **v1 (2026-04-19)** — Initial build. 7 node types, drag/drop, CRUD, comments, export/import, filters, pan/zoom.
- **v2 (2026-04-19)** — War-table reskin. Splash/title screen with "Take the Altar" CTA. Perspective toggle (Commander ⇄ Player) for live read-only audits. Soft-renames: Inspector → Dossier; Session notes → Commander's Log. Sigils per node type. `Shift+P` to flip perspective. `File → Show title screen` re-shows the splash.

## Related docs

- [CASCADE.md](../CASCADE.md) — navigation spine.
- [CONCEPT.md](../CONCEPT.md) — vision anchor.
- [prototype/](../prototype/) — throwaway design prototype (the clickable game-feel slice).
- [decisions/2026-04-19-admin-ui-v1.md](../decisions/2026-04-19-admin-ui-v1.md) — decision log entry for this tool.
