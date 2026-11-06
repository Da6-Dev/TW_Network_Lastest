"""
Adversarial Navigation & Boundary Stress Test Suite.
Author: challenger_2 (Empirical Challenger)
Target: TW Network GUI Ecosystem Standardization
"""

import os
import re
import pytest
import yaml

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MENUS = {
    "hub": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "menu.yml"),
    "minas": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "minas.yml"),
    "ranks": os.path.join(BASE_DIR, "plugins", "tw-ranks", "menus", "ranks.yml"),
    "terrenos": os.path.join(BASE_DIR, "plugins", "tw-terrenos", "menus", "terrenos.yml"),
    "maquinas": os.path.join(BASE_DIR, "plugins", "tw-maquinas", "menus", "maquinas.yml"),
    "spawners": os.path.join(BASE_DIR, "plugins", "tw-spawners", "menus", "spawners.yml"),
    "farms": os.path.join(BASE_DIR, "plugins", "tw-farms", "menus", "farms.yml"),
    "caixas": os.path.join(BASE_DIR, "plugins", "tw-caixas", "menus", "caixas.yml"),
    "minas_extra": os.path.join(BASE_DIR, "plugins", "tw-minas", "menus", "minas_extra.yml"),
}

COMMAND_WHITELIST = os.path.join(BASE_DIR, "plugins", "CommandWhitelist", "config.yml")
DELUXEMENUS_CONFIG = os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "config.yml")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_commands(item_cfg):
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
# 1. NAVIGATION GRAPH & CONNECTIVITY STRESS TESTS
# ==============================================================================

class TestNavigationGraphAndConnectivity:
    """Stress-test navigation graph topology, reachability, and return paths."""

    def test_navigation_graph_connectivity(self):
        """
        Build directed navigation graph between menus and verify reachability:
        - Hub connects to all 10 subsystems.
        - Every submenu has a guaranteed path back to Hub.
        - Every menu has a terminal exit ([close]).
        """
        hub_data = load_yaml(MENUS["hub"])
        hub_items = hub_data.get("items", {})

        # Collect targets reachable from Hub
        hub_outgoing_actions = []
        for item_id, cfg in hub_items.items():
            if isinstance(cfg, dict):
                hub_outgoing_actions.extend(extract_commands(cfg))

        hub_action_str = " ".join(hub_outgoing_actions).lower()

        required_systems = {
            "minas": ["[openguimenu] minas", "minaslista", "minas"],
            "ranks": ["[player] ranks", "ranks"],
            "terrenos": ["[player] terrenos", "terrenos"],
            "maquinas": ["[player] maquinas", "maquinas"],
            "spawners": ["[player] spawners", "spawners"],
            "farms": ["[player] farms", "farms"],
            "caixas": ["[player] caixas", "caixas"],
            "loja": ["[player] shop", "shop"],
            "kits": ["[player] kits", "kits"],
            "cosmeticos": ["[player] cosmetics", "cosmetics"],
        }

        for system, targets in required_systems.items():
            assert any(t in hub_action_str for t in targets), (
                f"Navigation Graph Broken: Hub cannot reach system '{system}'."
            )

        # Verify Return Path for every submenu
        for menu_name, path in MENUS.items():
            if menu_name == "hub":
                continue
            data = load_yaml(path)
            size = data.get("size")
            expected_return_slot = 45 if size == 54 else 18
            expected_close_slot = 49 if size == 54 else 22

            items = data.get("items", {})
            return_cmds = []
            close_cmds = []

            for item_id, cfg in items.items():
                if not isinstance(cfg, dict):
                    continue
                slots = []
                if "slot" in cfg and cfg["slot"] is not None:
                    slots.append(int(cfg["slot"]))
                if "slots" in cfg and isinstance(cfg["slots"], list):
                    slots.extend([int(s) for s in cfg["slots"]])

                if expected_return_slot in slots:
                    return_cmds.extend(extract_commands(cfg))
                if expected_close_slot in slots:
                    close_cmds.extend(extract_commands(cfg))

            return_blob = " ".join(return_cmds).lower()
            close_blob = " ".join(close_cmds).lower()

            assert any(t in return_blob for t in ["principal", "menu", "ajuda"]), (
                f"Dead-end detected: Menu '{menu_name}' return button (slot {expected_return_slot}) "
                f"does not route back to Hub: {return_cmds}"
            )

            assert "[close]" in close_blob, (
                f"Missing terminal exit: Menu '{menu_name}' close button (slot {expected_close_slot}) "
                f"does not invoke [close]: {close_cmds}"
            )

    def test_bidirectional_cross_synergies(self):
        """
        Verify bidirectional gameplay synergy shortcuts:
        - Terrenos -> Maquinas
        - Maquinas -> Terrenos
        - Spawners -> Caixas / Forja
        """
        # Terrenos -> Maquinas
        terrenos = load_yaml(MENUS["terrenos"])
        terrenos_cmds = []
        for cfg in terrenos.get("items", {}).values():
            if isinstance(cfg, dict):
                terrenos_cmds.extend(extract_commands(cfg))
        assert any("maquinas" in c.lower() for c in terrenos_cmds), (
            "Terrenos lacks cross-shortcut to /maquinas"
        )

        # Maquinas -> Terrenos
        maquinas = load_yaml(MENUS["maquinas"])
        maquinas_cmds = []
        for cfg in maquinas.get("items", {}).values():
            if isinstance(cfg, dict):
                maquinas_cmds.extend(extract_commands(cfg))
        assert any("terrenos" in c.lower() for c in maquinas_cmds), (
            "Maquinas lacks cross-shortcut to /terrenos"
        )

        # Spawners -> Key forja
        spawners = load_yaml(MENUS["spawners"])
        spawners_cmds = []
        for cfg in spawners.get("items", {}).values():
            if isinstance(cfg, dict):
                spawners_cmds.extend(extract_commands(cfg))
        assert any("key forja" in c.lower() or "forja" in c.lower() for c in spawners_cmds), (
            "Spawners lacks cross-shortcut to key forja / caixas"
        )


# ==============================================================================
# 2. COMMAND WHITELIST COVERAGE
# ==============================================================================

class TestCommandWhitelistCoverage:
    """Verify that every command accessible by players is whitelisted in CommandWhitelist."""

    def test_all_player_commands_are_whitelisted(self):
        """
        All commands executed via [player] <cmd> across all menus must exist in
        plugins/CommandWhitelist/config.yml default group.
        """
        cw_data = load_yaml(COMMAND_WHITELIST)
        whitelisted = set(
            c.lstrip("/").lower()
            for c in cw_data.get("groups", {}).get("default", {}).get("commands", [])
        )

        unwhitelisted_cmds = []

        for menu_name, path in MENUS.items():
            data = load_yaml(path)
            items = data.get("items", {})
            for item_id, cfg in items.items():
                if not isinstance(cfg, dict):
                    continue
                cmds = extract_commands(cfg)
                for c in cmds:
                    if c.startswith("[player]"):
                        raw = c.replace("[player]", "").strip()
                        raw = re.sub(r"<[^>]+>", "", raw).strip()
                        if not raw:
                            continue
                        base_cmd = raw.split()[0].lstrip("/").lower()
                        if base_cmd not in whitelisted:
                            unwhitelisted_cmds.append({
                                "menu": menu_name,
                                "item": item_id,
                                "command": raw,
                                "base_cmd": base_cmd
                            })

        assert len(unwhitelisted_cmds) == 0, (
            f"Found commands executed in menus that are NOT whitelisted in CommandWhitelist: {unwhitelisted_cmds}"
        )

    def test_plotsquared_aliases_whitelisted(self):
        """
        Explicitly verify that all standard PlotSquared aliases ('plot', 'plots', 'p')
        are whitelisted in CommandWhitelist default group.
        """
        cw_data = load_yaml(COMMAND_WHITELIST)
        whitelisted = set(
            c.lstrip("/").lower()
            for c in cw_data.get("groups", {}).get("default", {}).get("commands", [])
        )
        for alias in ["plot", "plots", "p"]:
            assert alias in whitelisted, (
                f"PlotSquared alias '{alias}' is NOT whitelisted in CommandWhitelist default group! "
                f"Whitelisted commands: {sorted(list(whitelisted))}"
            )


# ==============================================================================
# 3. MINAS DUAL-PRIORITY & PERMISSION EDGE CASES
# ==============================================================================

class TestMinasDualPriorityAdversarial:
    """Stress-test dual-priority display items and permission fallbacks in minas.yml."""

    EXPECTED_MINES = [
        ("carvao", 10, "realmines.carvao.break"),
        ("neve", 11, "realmines.neve.break"),
        ("sino", 12, "realmines.sino.break"),
        ("biscoito", 13, "realmines.biscoito.break"),
        ("duende", 14, "realmines.duende.break"),
        ("rena", 15, "realmines.rena.break"),
        ("treno", 16, "realmines.treno.break"),
        ("quebranozes", 19, "realmines.quebranozes.break"),
        ("estrela", 20, "realmines.estrela.break"),
        ("noel", 21, "realmines.noel.break"),
        ("vip_polar", 22, "realmines.vip_polar.break"),
        ("vip_nevasca", 23, "realmines.vip_nevasca.break"),
        ("vip_festivo", 24, "realmines.vip_festivo.break"),
        ("grinch", 25, "realmines.grinch.break"),
        ("yeti", 28, "realmines.yeti.break"),
        ("krampus", 29, "realmines.krampus.break"),
    ]

    def test_dual_priority_complete_pairing(self):
        """Every mine slot must have exactly Priority 1 (with perm) and Priority 2 (fallback)."""
        minas_data = load_yaml(MENUS["minas"])
        items = minas_data.get("items", {})

        for mine_id, slot, perm in self.EXPECTED_MINES:
            slot_items = [
                (item_id, cfg)
                for item_id, cfg in items.items()
                if isinstance(cfg, dict) and cfg.get("slot") == slot
            ]
            assert len(slot_items) == 2, (
                f"Slot {slot} (Mine '{mine_id}') does not have exactly 2 states (found {len(slot_items)}: {slot_items})"
            )

            p1_items = [(iid, c) for iid, c in slot_items if c.get("priority") == 1]
            p2_items = [(iid, c) for iid, c in slot_items if c.get("priority") == 2]

            assert len(p1_items) == 1, f"Slot {slot} lacks single Priority 1 item"
            assert len(p2_items) == 1, f"Slot {slot} lacks single Priority 2 item"

            p1_id, p1_cfg = p1_items[0]
            p2_id, p2_cfg = p2_items[0]

            # Verify P1 view requirement
            vr = p1_cfg.get("view_requirement", {})
            reqs = vr.get("requirements", {})
            req_perms = [
                r.get("permission")
                for r in reqs.values()
                if isinstance(r, dict) and r.get("permission")
            ]
            assert perm in req_perms, (
                f"Slot {slot} P1 item '{p1_id}' view_requirement does not check '{perm}': {req_perms}"
            )

            # Verify P1 actions: close & mine tp
            p1_cmds = extract_commands(p1_cfg)
            assert "[close]" in p1_cmds, f"Slot {slot} P1 item lacks [close]"
            assert any(f"mine tp {mine_id}" in c.lower() for c in p1_cmds), (
                f"Slot {slot} P1 item does not teleport to '{mine_id}': {p1_cmds}"
            )

            # Verify P2 fallback: NO view requirement (unconditional fallback)
            assert "view_requirement" not in p2_cfg, (
                f"Slot {slot} P2 item '{p2_id}' has a view_requirement; fallback must be unconditional!"
            )
            assert p2_cfg.get("material") == "GRAY_DYE", (
                f"Slot {slot} P2 item '{p2_id}' material is '{p2_cfg.get('material')}', expected 'GRAY_DYE'"
            )

            # Verify P2 click action rejects with sound
            p2_cmds = extract_commands(p2_cfg)
            assert any("entity_villager_no" in c.lower() for c in p2_cmds), (
                f"Slot {slot} P2 item '{p2_id}' lacks villager deny sound: {p2_cmds}"
            )
            # Ensure P2 does NOT teleport the player!
            assert not any("tp" in c.lower() for c in p2_cmds), (
                f"Security flaw: Slot {slot} P2 item '{p2_id}' contains teleport command: {p2_cmds}"
            )

    def test_permission_edge_cases_unauthorized_clicks(self):
        """
        Adversarial test: simulate click on locked items.
        Verify that no unauthorized commands (like teleporting or purchasing) can be executed.
        """
        minas_data = load_yaml(MENUS["minas"])
        items = minas_data.get("items", {})

        for item_id, cfg in items.items():
            if not isinstance(cfg, dict):
                continue
            if cfg.get("priority") == 2:
                # Locked item
                cmds = extract_commands(cfg)
                # Must NOT contain [player] or [console] commands that grant access
                dangerous_cmds = [c for c in cmds if "[player]" in c or "[console]" in c]
                assert len(dangerous_cmds) == 0, (
                    f"Locked item '{item_id}' contains executable player/console commands: {dangerous_cmds}"
                )
