# TEST_INFRA.md — Infrastructure & Quality Gate Specification
# Minecraft Server GUI Ecosystem Standardization

**Document Version:** 1.0.0  
**Target Environment:** Purpur 26.3 | Python 3.15+ / pytest 9+ / PyYAML 6+  
**Scope:** Automated 4-Tier Opaque-Box E2E Testing Suite for DeluxeMenus & Custom `tw-*` Plugins  

---

## 1. Testing Philosophy & Integrity Guarantees

The TW Network GUI Ecosystem represents the primary user interface layer connecting players to all 10 Tycoon gameplay systems (Minas, Terrenos, Máquinas, Spawners, Farms, Caixas, Ranks, Loja, Kits, Cosméticos). A failure in menu configuration directly degrades player experience, locks progression, or breaks game loops.

To provide absolute quality assurance, this test suite adheres to the following principles:
1. **Opaque-Box Verification**: The test suite treats YAML configurations as external artifacts, testing against formal interface contracts rather than implementation internals.
2. **Zero-Tolerance Quality Gate**: No test shortcuts, synthetic mocks, or facade passes are permitted. All tests inspect real on-disk files.
3. **Deterministic & Self-Contained Execution**: All tests execute via standard `pytest` without requiring a live Minecraft server instance, enabling rapid CI/CD validation.
4. **Actionable Diagnostics**: When an assertion fails, the error message indicates the exact file path, YAML key, item identifier, slot index, and violation category.

---

## 2. Feature Inventory & Scope Mapping

| Feature ID | Scope | Target Files | Associated Test Tier |
|---|---|---|---|
| **F1** | Design System & UI Styling | `docs/design_system.md`, All YAML menus | **Tier 2** (Slots/Sizes), **Tier 3** (Titles/Lores) |
| **F2** | Navigation Architecture & UX | `docs/navigation_architecture.md`, All YAML menus | **Tier 2** (Return/Close slots), **Tier 4** (Graph Simulation) |
| **F3** | DeluxeMenus Central Configs | `plugins/DeluxeMenus/config.yml`, `menus/menu.yml`, `menus/minas.yml`, `CommandWhitelist` | **Tier 1** (Syntax), **Tier 2** (Borders), **Tier 3** (Registration) |
| **F4** | Custom `tw-*` Menu Models | `plugins/tw-*/menus/*.yml` (7 models) | **Tier 1** (Syntax), **Tier 2** (Slots), **Tier 3** (Lores) |
| **F5** | E2E Testing Suite | `tests/e2e/test_menus.py`, `TEST_INFRA.md`, `TEST_READY.md` | All Tiers (1 through 4) |

---

## 3. 4-Tier Automated Test Architecture

```
                    ┌────────────────────────────────────────────────────────┐
                    │               4-TIER TEST ARCHITECTURE                 │
                    └────────────────────────────────────────────────────────┘
                                                 │
        ┌───────────────────┬────────────────────┼───────────────────┐
        ▼                   ▼                    ▼                   ▼
  ┌───────────┐       ┌───────────┐        ┌───────────┐       ┌───────────┐
  │  TIER 1   │       │  TIER 2   │        │  TIER 3   │       │  TIER 4   │
  │  Feature  │       │ Boundary  │        │Formatting │       │    E2E    │
  │ Coverage  │       │ & Layout  │        │ & Quality │       │Navigation │
  │ & Syntax  │       │   Rules   │        │ Standards │       │Simulation │
  └─────┬─────┘       └─────┬─────┘        └─────┬─────┘       └─────┬─────┘
        │                   │                    │                   │
        ├─ Existence        ├─ Menu Sizes        ├─ Title Prefixes   ├─ Graph Walk
        ├─ YAML Parser      ├─ Slot Range        ├─ 3-Section Lore   ├─ Hub->Minas
        └─ Schema Sanity    ├─ Collisions        ├─ Registry Check   ├─ Submenus
                            └─ Return/Close      └─ Whitelist Check  └─ Return Path
```

### Tier 1: Feature Coverage & Syntactic Integrity
- **File Existence Matrix**:
  - `docs/design_system.md`
  - `docs/navigation_architecture.md`
  - `plugins/DeluxeMenus/config.yml`
  - `plugins/DeluxeMenus/gui_menus/menus/menu.yml`
  - `plugins/DeluxeMenus/gui_menus/menus/minas.yml`
  - `plugins/CommandWhitelist/config.yml`
  - `plugins/tw-ranks/menus/ranks.yml`
  - `plugins/tw-terrenos/menus/terrenos.yml`
  - `plugins/tw-maquinas/menus/maquinas.yml`
  - `plugins/tw-spawners/menus/spawners.yml`
  - `plugins/tw-farms/menus/farms.yml`
  - `plugins/tw-caixas/menus/caixas.yml`
  - `plugins/tw-minas/menus/minas_extra.yml`
- **YAML Syntax Validation**: Each file parsed with `yaml.safe_load()` must return a valid dictionary structure without syntax errors, bad indentation, or unescaped characters.

### Tier 2: Boundary & Structural Rules
- **Menu Size Constraints**:
  - Main Hub (`menu.yml`): strictly 54 slots (6 rows).
  - Mine Catalog (`minas.yml`): strictly 54 slots (6 rows).
  - Submenu models (`tw-*`): strictly 27 slots (3 rows) or 54 slots (6 rows for extensive catalogs). Sizes must be multiples of 9.
- **Slot Boundary Invariants**:
  - For size $S$, every item slot $s$ must satisfy $0 \le s < S$.
  - Items configured outside $[0, S-1]$ trigger immediate failure.
- **Slot Collision Detection**:
  - In fixed menus without dynamic priorities, no two items may claim the same slot.
  - In conditional menus (DeluxeMenus dual-state items), items sharing a slot must define distinct `priority` levels or `view_requirement` conditions.
- **Universal Return Button Rule**:
  - Every 54-slot submenu must configure a Return button at **Slot 45**.
  - Every 27-slot submenu must configure a Return button at **Slot 18**.
  - The return button item must feature a return indicator (`ARROW` or similar) and navigate to parent (`[openguimenu] principal` or `/menu`).
- **Universal Close Button Rule**:
  - Every 54-slot menu must configure a Close button at **Slot 49** (`BARRIER` / action `[close]`).
  - Every 27-slot menu must configure a Close button at **Slot 22** (`BARRIER` / action `[close]`).

### Tier 3: Formatting & Cross-Feature Standards
- **Unified Title Formatting**:
  - All menu titles must match standard indicator formatting: `&8➔` or hex-colored variants (`&#7FB4F4➔`, `&x&7&f&b&4&f&4➔`, `&8»`).
- **3-Section Lore Structure**:
  - All interactive buttons must enforce the 3-section design:
    1. **Top Section**: Short functional description (`&7...`).
    2. **Middle Section**: Dynamic player status / placeholder tags (`%...%` or status indicators).
    3. **Action Footer**: Action prompt matching `^[&§][a-z0-9]?[▶»>]\s*Clique para\s+` (e.g., `&a▶ Clique para acessar`, `&e▶ Clique para voltar`, `&c▶ Clique para fechar`).
- **DeluxeMenus Registration Integrity**:
  - `plugins/DeluxeMenus/config.yml` must explicitly register both `principal` (`menus/menu.yml`) and `minas` (`menus/minas.yml`).
- **Command Whitelist Access**:
  - `plugins/CommandWhitelist/config.yml` must include public menu open commands (`menu`, `minaslista`, `minhasminas`, `ranks`, `terrenos`, `maquinas`, `spawners`, `farms`, `caixas`) in the `default` player group.

### Tier 4: Real-World End-to-End Navigation Simulation
- **Graph Construction**:
  - Nodes: All menus ($M = \{\text{hub}, \text{minas}, \text{ranks}, \text{terrenos}, \text{maquinas}, \text{spawners}, \text{farms}, \text{caixas}, \dots\}$).
  - Directed Edges: Configured click actions (`[openguimenu] <id>`, `[player] <command>`).
- **Navigation Invariants**:
  - **Hub Reachability**: From Hub, all 10 core gameplay systems must be reachable in 1 transition.
  - **Return Path Integrity**: From any reachable submenu, following the Universal Return Button must lead back to the parent menu or Hub.
  - **No Dead Ends**: Every submenu must have at least one return or close mechanism.
- **Simulated Walkthrough**:
  - Execute a depth-first or breadth-first journey verifying cycle-free traversal and exit paths.

---

## 4. Coverage Thresholds & Quality Gate

| Metric | Target Threshold | Quality Gate Pass Criteria |
|---|---|---|
| **Required Menu Files Present** | 100% (13/13 files) | All required YAML & Markdown files present on disk |
| **YAML Parse Success Rate** | 100% (0 errors) | Zero syntax/parsing exceptions |
| **Slot Boundary Compliance** | 100% | Zero slots outside $[0, \text{size}-1]$ |
| **Return Slot Compliance** | 100% | Submenus have Return at Slot 45 (54s) or 18 (27s) |
| **Close Slot Compliance** | 100% | Menus have Close at Slot 49 (54s) or 22 (27s) |
| **Lore Format Compliance** | 100% of interactive items | Header, dynamic body, action prompt footer |
| **Menu Registry & Whitelist** | 100% | All menus registered; all commands whitelisted |
| **Navigation Graph Connectivity** | 100% reachability & return | Zero unreachable subsystems; zero orphan submenus |

---

## 5. Execution Instructions

The test suite is executed using `pytest` from the project root:

```powershell
# Run the complete 4-Tier test suite with verbose reporting:
python -m pytest tests/e2e/test_menus.py -v --tb=short

# Run a specific Tier:
python -m pytest tests/e2e/test_menus.py -k "test_tier1" -v
python -m pytest tests/e2e/test_menus.py -k "test_tier2" -v
python -m pytest tests/e2e/test_menus.py -k "test_tier3" -v
python -m pytest tests/e2e/test_menus.py -k "test_tier4" -v
```

Upon successful execution of all tests, `TEST_READY.md` is generated and published at project root summarizing the verification results.
