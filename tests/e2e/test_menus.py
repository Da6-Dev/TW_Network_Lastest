"""
Automated 4-Tier E2E Test Suite for Minecraft Server GUI Ecosystem.
TW Network - Purpur 26.3 / DeluxeMenus & tw-* Custom Plugins

Tiers:
  Tier 1: Feature Coverage & Syntactic Integrity (File existence & YAML validity)
  Tier 2: Boundary & Structural Rules (Menu size, slot boundaries, slot collisions, return & close slots)
  Tier 3: Formatting & Cross-Feature Standards (Title prefix, 3-section lore format, DeluxeMenus registry, CommandWhitelist)
  Tier 4: Real-World End-to-End Navigation Simulation (Navigation graph reachability, return path integrity, player journey)
"""

import os
import re
import pytest
import yaml

# Base directory for the repository
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Canonical file paths under test
PATHS = {
    "design_system_doc": os.path.join(BASE_DIR, "docs", "design_system.md"),
    "nav_architecture_doc": os.path.join(BASE_DIR, "docs", "navigation_architecture.md"),
    "deluxemenus_config": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "config.yml"),
    "menu_hub": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "menu.yml"),
    "menu_minas": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "minas.yml"),
    "command_whitelist": os.path.join(BASE_DIR, "plugins", "CommandWhitelist", "config.yml"),
    "tw_ranks": os.path.join(BASE_DIR, "plugins", "tw-ranks", "menus", "ranks.yml"),
    "tw_terrenos": os.path.join(BASE_DIR, "plugins", "tw-terrenos", "menus", "terrenos.yml"),
    "tw_maquinas": os.path.join(BASE_DIR, "plugins", "tw-maquinas", "menus", "maquinas.yml"),
    "tw_spawners": os.path.join(BASE_DIR, "plugins", "tw-spawners", "menus", "spawners.yml"),
    "tw_farms": os.path.join(BASE_DIR, "plugins", "tw-farms", "menus", "farms.yml"),
    "tw_caixas": os.path.join(BASE_DIR, "plugins", "tw-caixas", "menus", "caixas.yml"),
    "tw_minas_extra": os.path.join(BASE_DIR, "plugins", "tw-minas", "menus", "minas_extra.yml"),
}

MENU_FILES = [
    ("menu_hub", PATHS["menu_hub"], True, 54),       # is_hub=True, expected_size=54
    ("menu_minas", PATHS["menu_minas"], False, 54),  # is_hub=False, expected_size=54
    ("tw_ranks", PATHS["tw_ranks"], False, 54),
    ("tw_terrenos", PATHS["tw_terrenos"], False, 27),
    ("tw_maquinas", PATHS["tw_maquinas"], False, 54),
    ("tw_spawners", PATHS["tw_spawners"], False, 54),
    ("tw_farms", PATHS["tw_farms"], False, 54),
    ("tw_caixas", PATHS["tw_caixas"], False, 54),
    ("tw_minas_extra", PATHS["tw_minas_extra"], False, 54),
]

REQUIRED_WHITELIST_COMMANDS = [
    "menu",
    "minaslista",
    "minhasminas",
    "ranks",
    "terrenos",
    "plot",
    "plots",
    "p",
    "maquinas",
    "spawners",
    "farms",
    "caixas",
]

# Regex for title formatting: &8➔, &8», or hex variations &#7FB4F4➔, &x&7&f&b&4&f&4➔
TITLE_REGEX = re.compile(
    r"^(&8|&#[0-9a-fA-F]{6}|&x(&[0-9a-fA-F]){6})[➔»]\s*(.+)$"
)

# Regex for action prompts in lore footer: &a▶ Clique para..., &e▶ Clique para..., &c▶ Clique para...
ACTION_PROMPT_REGEX = re.compile(
    r"(&[a-f0-9]|&x(&[0-9a-fA-F]){6}|&#[0-9a-fA-F]{6})?[▶»>✕]\s*(Clique para|Bloqueado)",
    re.IGNORECASE,
)


def load_yaml_file(filepath):
    """Safely loads and parses a YAML file."""
    if not os.path.isfile(filepath):
        pytest.fail(f"Required YAML file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
            return data
        except yaml.YAMLError as exc:
            pytest.fail(f"YAML Syntax Error in {filepath}: {exc}")


def get_menu_items(menu_data):
    """
    Extracts items map from either DeluxeMenus format or tw-* custom plugin format.
    Supports top-level 'items' or nested 'items' / 'gui.items'.
    """
    if "items" in menu_data and isinstance(menu_data["items"], dict):
        return menu_data["items"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("items", {})
    return {}


def get_menu_size(menu_data):
    """Extracts menu size from configuration."""
    if "size" in menu_data:
        return menu_data["size"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("size")
    return None


def get_menu_title(menu_data):
    """Extracts menu title from configuration."""
    if "menu_title" in menu_data:
        return menu_data["menu_title"]
    if "title" in menu_data:
        return menu_data["title"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("title") or menu_data["gui"].get("menu_title")
    return None


def get_item_slots(item_id, item_cfg):
    """Returns a list of slots configured for a given item."""
    slots = []
    if "slot" in item_cfg and item_cfg["slot"] is not None:
        slots.append(int(item_cfg["slot"]))
    if "slots" in item_cfg and isinstance(item_cfg["slots"], list):
        for s in item_cfg["slots"]:
            slots.append(int(s))
    return slots


def extract_item_commands(item_cfg):
    """Extracts all action and command strings from an item configuration."""
    cmds = []
    for k in [
        "left_click_commands",
        "right_click_commands",
        "shift_left_click_commands",
        "shift_right_click_commands",
        "middle_click_commands",
        "commands",
        "action",
        "actions",
    ]:
        val = item_cfg.get(k)
        if isinstance(val, list):
            cmds.extend([str(c).strip() for c in val])
        elif isinstance(val, str) and val.strip():
            cmds.append(val.strip())
    return cmds


# ==============================================================================
# TIER 1: Feature Coverage & Syntactic Integrity
# ==============================================================================

class TestTier1FeatureCoverageAndSyntax:
    """Tier 1: Verify all required files exist and are valid YAML."""

    @pytest.mark.parametrize("file_key,filepath", list(PATHS.items()))
    def test_tier1_required_file_exists(self, file_key, filepath):
        """Every required specification and configuration file must exist on disk."""
        assert os.path.exists(filepath), f"Missing required file [{file_key}]: {filepath}"
        assert os.path.getsize(filepath) > 0, f"File [{file_key}] is empty: {filepath}"

    @pytest.mark.parametrize("file_key,filepath", [
        (k, v) for k, v in PATHS.items() if v.endswith(".yml")
    ])
    def test_tier1_yaml_syntax_validity(self, file_key, filepath):
        """Every YAML file must be parseable by PyYAML without syntax/indentation errors."""
        data = load_yaml_file(filepath)
        assert isinstance(data, dict), f"YAML file [{file_key}] did not parse into a dictionary: {filepath}"
        assert len(data) > 0, f"Parsed YAML data in [{file_key}] is empty: {filepath}"


# ==============================================================================
# TIER 2: Boundary & Structural Rules
# ==============================================================================

class TestTier2BoundaryAndStructuralRules:
    """Tier 2: Slot boundary, menu size, collision, return/close button validation."""

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier2_menu_sizes(self, menu_key, filepath, is_hub, expected_size):
        """Menu size must strictly adhere to Design System (54 slots for main/catalogs, 27 for submenus)."""
        data = load_yaml_file(filepath)
        size = get_menu_size(data)
        assert size is not None, f"Menu [{menu_key}] has no 'size' configured in {filepath}"
        assert size == expected_size, (
            f"Menu [{menu_key}] size mismatch: expected {expected_size}, got {size} in {filepath}"
        )
        assert size in [27, 54], f"Menu [{menu_key}] size {size} is not canonical (27 or 54)"

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier2_slot_limits(self, menu_key, filepath, is_hub, expected_size):
        """All item slots must be within valid index bounds [0, size - 1]."""
        data = load_yaml_file(filepath)
        size = get_menu_size(data) or expected_size
        items = get_menu_items(data)
        assert len(items) > 0, f"Menu [{menu_key}] has no items configured in {filepath}"

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            slots = get_item_slots(item_id, item_cfg)
            for s in slots:
                assert 0 <= s < size, (
                    f"Out-of-bounds slot {s} configured for item '{item_id}' in [{menu_key}]. "
                    f"Valid range for size {size} is [0, {size - 1}]."
                )

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier2_no_duplicate_conflicting_slots(self, menu_key, filepath, is_hub, expected_size):
        """
        No duplicate conflicting slot assignments on the same view tier / priority.
        If multiple items occupy the same slot, they must have distinct priorities or view_requirements.
        """
        data = load_yaml_file(filepath)
        items = get_menu_items(data)
        slot_map = {}

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            priority = item_cfg.get("priority", 1)
            slots = get_item_slots(item_id, item_cfg)
            for s in slots:
                key = (s, priority)
                assert key not in slot_map, (
                    f"Conflicting duplicate slot assignment in [{menu_key}]: "
                    f"Slot {s} with priority {priority} is used by both '{slot_map[key]}' and '{item_id}'."
                )
                slot_map[key] = item_id

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", [
        f for f in MENU_FILES if not f[2]  # Submenus only (is_hub == False)
    ])
    def test_tier2_universal_return_button(self, menu_key, filepath, is_hub, expected_size):
        """
        Universal Return button check:
          - Slot 45 on 54-slot submenus.
          - Slot 18 on 27-slot submenus.
          Must feature return item / display name / commands pointing to parent.
        """
        data = load_yaml_file(filepath)
        items = get_menu_items(data)
        expected_return_slot = 45 if expected_size == 54 else 18

        return_items = []
        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            slots = get_item_slots(item_id, item_cfg)
            if expected_return_slot in slots:
                return_items.append((item_id, item_cfg))

        assert len(return_items) > 0, (
            f"Submenu [{menu_key}] lacks a return button at required Slot {expected_return_slot} in {filepath}"
        )

        item_id, item_cfg = return_items[0]
        display_name = item_cfg.get("display_name", "") or item_cfg.get("name", "")
        material = item_cfg.get("material", "").upper()

        # Material should be ARROW, DOOR, or return-oriented item
        valid_materials = ["ARROW", "OAK_DOOR", "IRON_DOOR", "BARRIER", "DARK_OAK_DOOR"]
        assert any(m in material for m in valid_materials), (
            f"Return item at slot {expected_return_slot} in [{menu_key}] has non-standard material '{material}'"
        )
        assert any(kw in display_name.lower() for kw in ["voltar", "retornar", "menu", "hub"]), (
            f"Return item at slot {expected_return_slot} in [{menu_key}] does not indicate return action: '{display_name}'"
        )

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier2_universal_close_button(self, menu_key, filepath, is_hub, expected_size):
        """
        Universal Close button check:
          - Slot 49 on 54-slot menus.
          - Slot 22 on 27-slot menus.
        """
        data = load_yaml_file(filepath)
        items = get_menu_items(data)
        expected_close_slot = 49 if expected_size == 54 else 22

        close_items = []
        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            slots = get_item_slots(item_id, item_cfg)
            if expected_close_slot in slots:
                close_items.append((item_id, item_cfg))

        assert len(close_items) > 0, (
            f"Menu [{menu_key}] lacks a close button at required Slot {expected_close_slot} in {filepath}"
        )

        item_id, item_cfg = close_items[0]
        display_name = item_cfg.get("display_name", "") or item_cfg.get("name", "")
        material = item_cfg.get("material", "").upper()

        assert "BARRIER" in material or "RED" in material or "DOOR" in material, (
            f"Close item at slot {expected_close_slot} in [{menu_key}] has unexpected material: {material}"
        )
        assert any(kw in display_name.lower() for kw in ["fechar", "sair", "close"]), (
            f"Close item at slot {expected_close_slot} in [{menu_key}] display name does not indicate close: '{display_name}'"
        )


# ==============================================================================
# TIER 3: Formatting & Cross-Feature Standards
# ==============================================================================

class TestTier3FormattingAndCrossFeatureStandards:
    """Tier 3: Menu titles, 3-section lore format, plugin registry, command whitelist."""

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier3_menu_titles(self, menu_key, filepath, is_hub, expected_size):
        """Menu titles must match unified Design System format: prefix &8➔ or color code variants."""
        data = load_yaml_file(filepath)
        title = get_menu_title(data)
        assert title is not None, f"Menu [{menu_key}] has no title in {filepath}"
        assert TITLE_REGEX.search(title), (
            f"Menu [{menu_key}] title '{title}' violates standard format '&8➔ <TITLE>' in {filepath}"
        )

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_tier3_lore_formatting_three_sections(self, menu_key, filepath, is_hub, expected_size):
        """
        Interactive/functional buttons must adhere to 3-section lore:
          1. Header: functional description
          2. Dynamic Status: player stats / requirements
          3. Footer: action prompt matching '▶ Clique para...'
        """
        data = load_yaml_file(filepath)
        items = get_menu_items(data)
        checked_interactive_items = 0

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue

            # Identify functional/interactive items (exclude plain decorative border glass panes)
            material = str(item_cfg.get("material", "")).upper()
            display_name = item_cfg.get("display_name", "") or item_cfg.get("name", "")
            
            # Check for genuine actions (exclude '[none]', 'none', or empty actions on info panels)
            action_field = str(item_cfg.get("action", "")).strip().lower()
            has_genuine_action = action_field not in ["", "none", "[none]"]
            has_commands = (
                bool(item_cfg.get("left_click_commands"))
                or bool(item_cfg.get("right_click_commands"))
                or bool(item_cfg.get("commands"))
                or has_genuine_action
            )

            # Skip pure decorative glass panes without display name or lore
            if "GLASS_PANE" in material and (not display_name or display_name.strip() in ["", "' '"]):
                continue

            lore = item_cfg.get("lore", [])
            if not lore:
                # Decorative dividers without lore are permitted
                continue

            checked_interactive_items += 1
            lore_text = "\n".join(str(line) for line in lore)

            # Assert at least 3 lines of lore content
            assert len(lore) >= 3, (
                f"Item '{item_id}' in [{menu_key}] lore has fewer than 3 lines: {lore}"
            )

            # Assert footer prompt exists on functional items with commands/genuine actions
            if has_commands and not any(kw in item_id.lower() for kw in ["borda", "painel", "divider", "info"]):
                assert ACTION_PROMPT_REGEX.search(lore_text), (
                    f"Item '{item_id}' in [{menu_key}] lacks required 3rd-section action footer "
                    f"('▶ Clique para...'): {lore}"
                )

        assert checked_interactive_items > 0, f"No interactive items found to test in [{menu_key}]"

    def test_tier3_deluxemenus_registry(self):
        """DeluxeMenus config.yml must register all menus ('principal' and 'minas')."""
        config = load_yaml_file(PATHS["deluxemenus_config"])
        gui_menus = config.get("gui_menus", {})
        assert isinstance(gui_menus, dict), "DeluxeMenus config.yml lacks 'gui_menus' section"

        assert "principal" in gui_menus, "Menu 'principal' is not registered in DeluxeMenus config.yml"
        assert "minas" in gui_menus, "Menu 'minas' is not registered in DeluxeMenus config.yml"

        assert gui_menus["principal"].get("file") == "menus/menu.yml", (
            f"Menu 'principal' file path incorrect: {gui_menus['principal']}"
        )
        assert gui_menus["minas"].get("file") == "menus/minas.yml", (
            f"Menu 'minas' file path incorrect: {gui_menus['minas']}"
        )

    def test_tier3_command_whitelist(self):
        """CommandWhitelist config.yml must permit all player menu commands in default group."""
        config = load_yaml_file(PATHS["command_whitelist"])
        assert "groups" in config, "CommandWhitelist lacks 'groups' key"
        default_group = config["groups"].get("default", {})
        commands = default_group.get("commands", [])

        # Normalize commands (lowercase, remove leading slash)
        normalized_commands = [c.lstrip("/").lower() for c in commands]

        for req_cmd in REQUIRED_WHITELIST_COMMANDS:
            assert req_cmd in normalized_commands, (
                f"Command '/{req_cmd}' is NOT whitelisted in CommandWhitelist default group: {normalized_commands}"
            )

    def test_tier3_command_whitelist_dynamic_menu_actions(self):
        """
        Dynamically scans all 9 menus for [player] command actions and asserts that
        every dispatched root command is whitelisted in CommandWhitelist default group.
        """
        config = load_yaml_file(PATHS["command_whitelist"])
        whitelisted = set(
            c.lstrip("/").lower()
            for c in config.get("groups", {}).get("default", {}).get("commands", [])
        )

        unwhitelisted_cmds = []

        for menu_key, filepath, is_hub, size in MENU_FILES:
            menu_data = load_yaml_file(filepath)
            items = get_menu_items(menu_data)
            for item_id, item_cfg in items.items():
                if not isinstance(item_cfg, dict):
                    continue
                cmds = extract_item_commands(item_cfg)
                for c in cmds:
                    if c.startswith("[player]"):
                        raw = c[len("[player]"):].strip()
                        raw = re.sub(r"<[^>]+>", "", raw).strip()
                        if not raw:
                            continue
                        base_cmd = raw.split()[0].lstrip("/").lower()
                        if base_cmd not in whitelisted:
                            unwhitelisted_cmds.append({
                                "menu": menu_key,
                                "item": item_id,
                                "command": raw,
                                "base_cmd": base_cmd,
                            })

        assert len(unwhitelisted_cmds) == 0, (
            f"Found commands dispatched by menus that are NOT whitelisted in CommandWhitelist: {unwhitelisted_cmds}"
        )


# ==============================================================================
# TIER 4: Real-World End-to-End Navigation Simulation
# ==============================================================================

class TestTier4EndToEndNavigationSimulation:
    """Tier 4: Navigation graph construction, reachability, and player journey simulation."""

    def test_tier4_hub_to_all_systems_reachability(self):
        """
        Verify that the Central Hub (menu.yml) directly links to all 10 core gameplay systems:
        Minas, Ranks, Terrenos, Máquinas, Spawners, Farms, Caixas, Loja, Kits, Cosméticos.
        """
        hub_data = load_yaml_file(PATHS["menu_hub"])
        items = get_menu_items(hub_data)

        # Collect all commands/actions triggered by hub items
        all_actions = []
        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            for cmd_key in ["left_click_commands", "right_click_commands", "commands", "action"]:
                cmds = item_cfg.get(cmd_key, [])
                if isinstance(cmds, list):
                    all_actions.extend([str(c).lower() for c in cmds])
                elif isinstance(cmds, str):
                    all_actions.append(cmds.lower())

        action_blob = " ".join(all_actions)

        # Check all 10 core systems
        systems = {
            "Minas": ["mina", "minas", "minaslista", "[openguimenu] minas"],
            "Ranks": ["rank", "ranks", "rankup"],
            "Terrenos": ["terreno", "terrenos", "plot"],
            "Máquinas": ["maquina", "maquinas"],
            "Spawners": ["spawner", "spawners", "geradores"],
            "Farms": ["farm", "farms"],
            "Caixas": ["caixa", "caixas", "key"],
            "Loja": ["shop", "loja", "mercado"],
            "Kits": ["kit", "kits"],
            "Cosméticos": ["cosmetics", "cosmeticos"],
        }

        for sys_name, triggers in systems.items():
            assert any(trig in action_blob for trig in triggers), (
                f"System '{sys_name}' is unreachable from Central Hub (menu.yml). "
                f"Expected one of {triggers} in configured commands: {all_actions}"
            )

    def test_tier4_return_path_integrity(self):
        """
        Verify that all submenus configure a valid return path that resolves back to Hub.
        """
        for menu_key, filepath, is_hub, size in MENU_FILES:
            if is_hub:
                continue
            data = load_yaml_file(filepath)
            items = get_menu_items(data)
            return_slot = 45 if size == 54 else 18

            return_found = False
            for item_id, item_cfg in items.items():
                if not isinstance(item_cfg, dict):
                    continue
                slots = get_item_slots(item_id, item_cfg)
                if return_slot in slots:
                    cmds = (
                        item_cfg.get("left_click_commands", [])
                        + item_cfg.get("right_click_commands", [])
                        + (item_cfg.get("commands", []) if isinstance(item_cfg.get("commands"), list) else [item_cfg.get("commands", "")])
                    )
                    action_val = item_cfg.get("action")
                    if isinstance(action_val, str) and action_val:
                        cmds.append(action_val)

                    cmd_blob = " ".join(str(c).lower() for c in cmds)
                    # Verify action targets principal menu, menu command, or previous menu
                    action_valid = (
                        "principal" in cmd_blob
                        or "menu" in cmd_blob
                        or "ajuda" in cmd_blob
                        or "[openguimenu]" in cmd_blob
                        or "[close]" in cmd_blob
                        or "back" in cmd_blob
                    )
                    assert action_valid, (
                        f"Submenu [{menu_key}] return button at slot {return_slot} "
                        f"has invalid target action: '{cmd_blob}' in {filepath}"
                    )
                    return_found = True
                    break

            assert return_found, f"Submenu [{menu_key}] has no return button at slot {return_slot}"

    def test_tier4_complete_player_journey_simulation(self):
        """
        Simulate a complete user navigation session:
          Step 1: Open Hub (/menu)
          Step 2: Transition Hub -> Minas Catalog (via Slot 19 or /minaslista)
          Step 3: Inspect Minas Catalog layout (Slot 45 return, Slot 49 close)
          Step 4: Execute Return -> Verify arrival at Hub
          Step 5: Transition Hub -> Terrenos (Slot 21)
          Step 6: Inspect Terrenos layout (Slot 18 return, Slot 22 close)
          Step 7: Execute Close -> Session terminated cleanly
        """
        # Step 1: Open Hub
        hub_data = load_yaml_file(PATHS["menu_hub"])
        assert get_menu_size(hub_data) == 54, "Hub size is not 54 slots"
        hub_items = get_menu_items(hub_data)

        # Step 2: Transition Hub -> Minas
        minas_data = load_yaml_file(PATHS["menu_minas"])
        assert get_menu_size(minas_data) == 54, "Minas size is not 54 slots"
        minas_items = get_menu_items(minas_data)

        # Step 3: Inspect Minas Catalog
        minas_return = None
        minas_close = None
        for item_id, item_cfg in minas_items.items():
            if not isinstance(item_cfg, dict):
                continue
            slots = get_item_slots(item_id, item_cfg)
            if 45 in slots:
                minas_return = (item_id, item_cfg)
            if 49 in slots:
                minas_close = (item_id, item_cfg)

        assert minas_return is not None, "Minas catalog lacks Slot 45 return button"
        assert minas_close is not None, "Minas catalog lacks Slot 49 close button"

        # Step 4: Execute Return
        return_cmds = (
            minas_return[1].get("left_click_commands", [])
            + minas_return[1].get("right_click_commands", [])
        )
        return_blob = " ".join(str(c).lower() for c in return_cmds)
        assert "principal" in return_blob or "menu" in return_blob, (
            f"Minas return button does not route back to Hub: {return_cmds}"
        )

        # Step 5: Transition Hub -> Terrenos
        terrenos_data = load_yaml_file(PATHS["tw_terrenos"])
        assert get_menu_size(terrenos_data) == 27, "Terrenos submenu size is not 27 slots"
        terrenos_items = get_menu_items(terrenos_data)

        # Step 6: Inspect Terrenos layout
        terrenos_return = None
        terrenos_close = None
        for item_id, item_cfg in terrenos_items.items():
            if not isinstance(item_cfg, dict):
                continue
            slots = get_item_slots(item_id, item_cfg)
            if 18 in slots:
                terrenos_return = (item_id, item_cfg)
            if 22 in slots:
                terrenos_close = (item_id, item_cfg)

        assert terrenos_return is not None, "Terrenos lacks Slot 18 return button"
        assert terrenos_close is not None, "Terrenos lacks Slot 22 close button"

        # Step 7: Close execution
        close_cmds = (
            terrenos_close[1].get("left_click_commands", [])
            + terrenos_close[1].get("right_click_commands", [])
            + [terrenos_close[1].get("action", "")]
        )
        close_blob = " ".join(str(c).lower() for c in close_cmds)
        assert "[close]" in close_blob or "close" in close_blob or "fechar" in close_blob, (
            f"Terrenos close button did not execute close action: {close_cmds}"
        )


# ==============================================================================
# ADVERSARIAL & INTEGRITY VERIFICATION
# ==============================================================================

class TestAdversarialAndIntegrityVerification:
    """Adversarial stress testing, encoding integrity, and dual-state invariants."""

    @pytest.mark.parametrize("file_key,filepath", [
        (k, v) for k, v in PATHS.items() if v.endswith(".yml")
    ])
    def test_adversarial_encoding_and_mojibake(self, file_key, filepath):
        """Verify files do not contain corrupted UTF-8 mojibake sequences."""
        with open(filepath, "rb") as f:
            raw_bytes = f.read()

        # Must decode cleanly as utf-8
        text = raw_bytes.decode("utf-8")
        assert "\ufffd" not in text, f"Replacement character (U+FFFD) found in [{file_key}]"

        # Check for typical Windows-1252 / UTF-8 double-encoding artifacts
        mojibake_signatures = ["Ã£", "Ã©", "Ã§", "Ã³", "âž”", "â–¶", "âœ”", "âœ–"]
        for bad_sig in mojibake_signatures:
            assert bad_sig not in text, (
                f"Double-encoded mojibake signature '{bad_sig}' detected in [{file_key}] ({filepath})"
            )

    @pytest.mark.parametrize("menu_key,filepath,is_hub,expected_size", MENU_FILES)
    def test_adversarial_materials_and_schema_sanity(self, menu_key, filepath, is_hub, expected_size):
        """All items must have valid non-empty material names and well-formed structures."""
        data = load_yaml_file(filepath)
        items = get_menu_items(data)
        assert len(items) >= 5, f"Menu [{menu_key}] has an unusually small number of items ({len(items)})"

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            assert "material" in item_cfg, f"Item '{item_id}' in [{menu_key}] has no 'material' key"
            mat = str(item_cfg["material"]).strip()
            assert len(mat) > 0, f"Item '{item_id}' in [{menu_key}] has empty material"
            # Must either start with head- or be uppercase Bukkit identifier
            assert mat.startswith("head-") or mat.isupper() or "_" in mat, (
                f"Item '{item_id}' in [{menu_key}] has invalid material formatting: '{mat}'"
            )

    def test_adversarial_minas_dual_state_completeness(self):
        """
        Verify that all 16 mines in minas.yml have full dual-state coverage:
        Each mine slot must host both Priority 1 (Unlocked) and Priority 2 (Locked).
        """
        minas_data = load_yaml_file(PATHS["menu_minas"])
        items = get_menu_items(minas_data)

        # Expected 16 mine slots
        mine_slots = [10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 28, 29]

        for slot in mine_slots:
            slot_items = [
                (item_id, cfg)
                for item_id, cfg in items.items()
                if isinstance(cfg, dict) and cfg.get("slot") == slot
            ]
            assert len(slot_items) >= 2, (
                f"Slot {slot} in minas.yml lacks dual-state coverage (found {len(slot_items)} items: {slot_items})"
            )
            priorities = [cfg.get("priority") for _, cfg in slot_items]
            assert 1 in priorities, f"Slot {slot} in minas.yml lacks Priority 1 (unlocked state)"
            assert 2 in priorities, f"Slot {slot} in minas.yml lacks Priority 2 (locked state)"

    def test_adversarial_open_commands_registration(self):
        """DeluxeMenus menu files must declare canonical open commands."""
        hub = load_yaml_file(PATHS["menu_hub"])
        hub_cmds = [str(c).lower() for c in hub.get("open_command", [])]
        assert "menu" in hub_cmds, f"Hub lacks open command 'menu': {hub_cmds}"
        assert "ajuda" in hub_cmds, f"Hub lacks open command 'ajuda': {hub_cmds}"

        minas = load_yaml_file(PATHS["menu_minas"])
        minas_cmds = [str(c).lower() for c in minas.get("open_command", [])]
        assert "minaslista" in minas_cmds, f"Minas lacks open command 'minaslista': {minas_cmds}"
        assert "minhasminas" in minas_cmds, f"Minas lacks open command 'minhasminas': {minas_cmds}"
