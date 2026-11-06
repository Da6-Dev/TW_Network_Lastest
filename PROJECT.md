# Project: Minecraft Server GUI Ecosystem Standardization

## Architecture
- **Ecosystem Goal**: Restructure, standardize, and interconnect all server GUIs (DeluxeMenus and custom `tw-*` plugins) into a unified, native presentation layer with consistent UX, styling, lore formatting, and bidirectional navigation.
- **Visual Design Standard (R1)**:
  - 54 slots (6 rows) for Main Menus, Hubs, and Catalogs.
  - 27 slots (3 rows) for Action Panels, Submenus, and Management views.
  - Consistent Stained Glass Pane borders and column dividers (`GRAY_STAINED_GLASS_PANE` / `BLACK_STAINED_GLASS_PANE` / accent panes).
  - Hex & Minecraft color palette: Primary hex highlight `&#7FB4F4` (or `&x&7&f&b&4&f&4`), secondary value `&e` / `&#F7C844`, description text `&7`, dark gray accents `&8`, success `&a`, alert/closed `&c`.
  - Unified Title Format: `&8➔ &b&lTÍTULO` (or hex variant).
  - 3-Section Item Lore:
    1. Header: Short functional description.
    2. Body: Dynamic status / variables (`%player_name%`, `%vault_eco_balance_formatted%`, `%tw_tokens%`, `%tw_rank%`, etc.).
    3. Footer: Clear click action prompt (`&a▶ Clique para acessar`, `&e▶ Clique para voltar`, `&c▶ Clique para fechar`).
- **Navigation Architecture (R2)**:
  - Central Hub (`menu.yml`, 54 slots) acting as the main gateway to all 10 core systems.
  - Universal Return Button: Slot 45 in 54-slot menus; Slot 18 in 27-slot menus.
  - Universal Close Button: Slot 49 in 54-slot menus; Slot 22 in 27-slot menus.
  - Cross-linking between related subsystems (Minas ↔ Loja, Terrenos ↔ Máquinas/Spawners, Spawners ↔ Forja).
- **Configuration & Integration (R3)**:
  - DeluxeMenus: Fully configured and registered `menu.yml`, `minas.yml`, and `config.yml`.
  - Whitelist: `plugins/CommandWhitelist/config.yml` allowing public menu commands.
  - Custom `tw-*` Plugins: Declarative YAML configuration structures and models for all custom modules (`tw-ranks`, `tw-terrenos`, `tw-maquinas`, `tw-spawners`, `tw-farms`, `tw-caixas`, `tw-minas`).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | F1: Design System & Style Guide (R1) | Complete UI specification: slots, palette, titles, 3-section lore standard | M1 | Survey / R1 |
| 2 | F2: Navigation Architecture & UX Flow (R2) | Full UX navigation map, bidirectional links, universal return (45/18) and close slots | M2 | Survey / R2 |
| 3 | F3: DeluxeMenus Central Configurations (R3) | 54-slot `menu.yml`, fixed `minas.yml`, registration in `config.yml`, command whitelist | M3 | Survey / R3 |
| 4 | F4: Custom `tw-*` Plugins Menu Models (R3) | Standardized YAML configuration models for all 7 custom menu-bearing modules | M4 | Survey / R3 |
| 5 | F5: E2E Test Suite & Hardening | Automated YAML syntax validator, slot/lore/title rules tester (Tiers 1-5) | M5 | Dual Track |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Design System & Visual UI Style Guide | Define and document definitive Design System specification (R1) | Survey | DONE |
| M2 | Navigation Architecture & UX Flow Map | Map full navigation hierarchy, routes, cross-system links, universal slots (R2) | M1 | DONE |
| M3 | DeluxeMenus Central Ecosystem Implementation | Implement 54-slot `menu.yml`, fixed `minas.yml`, `config.yml`, `CommandWhitelist` (R3) | M1, M2 | DONE |
| M4 | Custom `tw-*` Standardized Menu YAML Models | Create standardized YAML configuration files/templates for `tw-*` plugin menus (R3) | M1, M2 | DONE |
| M5 | E2E Testing Suite & Quality Gate | Validate YAML syntax, slot placement, lores, and cross-linking (Tiers 1-5) | M3, M4 | DONE |

## Interface Contracts
### DeluxeMenus ↔ Central Hub (`menu.yml`)
- Open commands: `/menu`, `/ajuda`
- GUI registration: `plugins/DeluxeMenus/config.yml` entry `principal: file: menus/menu.yml`
- Slots: 54 total (6 rows)
- Shortcuts:
  - Slot 4: Perfil (`head-%player_name%`)
  - Slot 19: Minas (`/minaslista` / `[openguimenu] minas`)
  - Slot 20: Ranks (`/ranks`)
  - Slot 21: Terrenos (`/terrenos`)
  - Slot 22: Máquinas (`/maquinas`)
  - Slot 23: Spawners (`/spawners`)
  - Slot 24: Farms (`/farms`)
  - Slot 25: Caixas (`/caixas`)
  - Slot 30: Loja (`/shop`)
  - Slot 31: Kits (`/kits`)
  - Slot 32: Cosméticos (`/cosmetics`)
  - Slot 49: Fechar (`BARRIER`, `[close]`)

### DeluxeMenus ↔ Minas Submenu (`minas.yml`)
- Open commands: `/minaslista`, `/minhasminas`
- GUI registration: `plugins/DeluxeMenus/config.yml` entry `minas: file: menus/minas.yml`
- Slots: 54 total (6 rows)
- Universal Return: Slot 45 (`ARROW`, `[openguimenu] principal`, display `&e&lVoltar ao Menu`)
- Universal Close: Slot 49 (`BARRIER`, `[close]`, display `&c&lFechar`)
- Mine items: Slots 10-16, 19-25, 28-34 with dual state (unlocked vs locked)

### Custom `tw-*` Menu Schema Standard
- YAML format per menu:
  - `title`: String matching `&8➔ &b&lTÍTULO`
  - `size`: Integer, strictly `54` (main) or `27` (submenu)
  - `items`: Map of item configurations
    - `slot`: Integer
    - `material`: Valid Bukkit material name
    - `name`: String with formatted title
    - `lore`: Array of strings adhering to 3 sections (Header, Dynamic Status, Action Footer)
  - Universal return: Slot 45 (size 54) or Slot 18 (size 27)
  - Universal close: Slot 49 (size 54) or Slot 22 (size 27)

## Code Layout
- Documentation:
  - `docs/design_system.md`: Comprehensive Visual UI Style Guide (R1)
  - `docs/navigation_architecture.md`: UX Navigation Map & Ecosystem Flow (R2)
- DeluxeMenus Configurations:
  - `plugins/DeluxeMenus/config.yml`: Menu registry
  - `plugins/DeluxeMenus/gui_menus/menus/menu.yml`: 54-slot Central Hub
  - `plugins/DeluxeMenus/gui_menus/menus/minas.yml`: 54-slot Minas menu with fixed slot 45 return
- Custom Plugin YAML Models:
  - `plugins/tw-ranks/menus/ranks.yml`: Standardized Ranks menu model
  - `plugins/tw-terrenos/menus/terrenos.yml`: Standardized Terrenos menu model
  - `plugins/tw-maquinas/menus/maquinas.yml`: Standardized Máquinas shop & panel models
  - `plugins/tw-spawners/menus/spawners.yml`: Standardized Spawners shop & panel models
  - `plugins/tw-farms/menus/farms.yml`: Standardized Farms panel & storage models
  - `plugins/tw-caixas/menus/caixas.yml`: Standardized Caixas & Key forge models
  - `plugins/tw-minas/menus/minas_extra.yml`: Standardized Oficina & Cartinhas models
- Command Whitelist:
  - `plugins/CommandWhitelist/config.yml`: Player command access
- Testing & Verification Suite:
  - `tests/e2e/test_menus.py`: Automated validator verifying YAML syntax, slot counts, return button slots, close button slots, and lore formatting.
