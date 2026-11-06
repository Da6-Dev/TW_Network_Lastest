"""
Deep Adversarial Verification & Stress Harness.
Empirical Challenger 1 - TW Network GUI Standardization.
"""

import os
import re
import sys
import yaml
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MENUS = {
    "menu_hub": {
        "path": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "menu.yml"),
        "is_hub": True,
        "size": 54,
        "expected_return": None,
        "expected_close": 49,
    },
    "menu_minas": {
        "path": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "minas.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_ranks": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-ranks", "menus", "ranks.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_terrenos": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-terrenos", "menus", "terrenos.yml"),
        "is_hub": False,
        "size": 27,
        "expected_return": 18,
        "expected_close": 22,
    },
    "tw_maquinas": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-maquinas", "menus", "maquinas.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_spawners": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-spawners", "menus", "spawners.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_farms": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-farms", "menus", "farms.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_caixas": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-caixas", "menus", "caixas.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
    "tw_minas_extra": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-minas", "menus", "minas_extra.yml"),
        "is_hub": False,
        "size": 54,
        "expected_return": 45,
        "expected_close": 49,
    },
}

DELUXEMENUS_CONFIG = os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "config.yml")
COMMAND_WHITELIST = os.path.join(BASE_DIR, "plugins", "CommandWhitelist", "config.yml")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run_deep_adversarial_suite():
    failures = []
    warnings = []
    checks_count = 0

    print("=================================================================")
    print("RUNNING CHALLENGER 1 DEEP ADVERSARIAL STRESS SUITE")
    print("=================================================================")

    # -------------------------------------------------------------
    # SUITE 1: Byte-level file checks (UTF-8 BOM, Mojibake)
    # -------------------------------------------------------------
    all_target_yaml_paths = [m["path"] for m in MENUS.values()] + [DELUXEMENUS_CONFIG, COMMAND_WHITELIST]
    for p in all_target_yaml_paths:
        checks_count += 1
        with open(p, "rb") as f:
            raw = f.read()
        if raw.startswith(b"\xef\xbb\xbf"):
            failures.append(f"File {p} starts with a UTF-8 BOM, which breaks some Bukkit YAML parsers!")
        
        # Test valid utf-8 decoding
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            failures.append(f"File {p} is not valid UTF-8: {e}")
            continue

        # Check for replacement chars
        if "\ufffd" in text:
            failures.append(f"File {p} contains replacement character U+FFFD (corrupted encoding)")

        # Double UTF-8 Mojibake check
        mojibake = ["Ã£", "Ã©", "Ã§", "Ã³", "âž”", "â–¶", "âœ”", "âœ–"]
        for mb in mojibake:
            if mb in text:
                failures.append(f"File {p} contains mojibake signature '{mb}'")

    # -------------------------------------------------------------
    # SUITE 2: Command Whitelist Parity Test
    # -------------------------------------------------------------
    # Load whitelisted commands
    wl_data = load_yaml(COMMAND_WHITELIST)
    default_wl = [c.lstrip("/").lower() for c in wl_data.get("groups", {}).get("default", {}).get("commands", [])]
    print(f"[Whitelist] Found {len(default_wl)} default whitelisted commands: {default_wl}")

    # Gather all player commands executed across all menus
    player_commands_checked = 0
    for menu_key, meta in MENUS.items():
        data = load_yaml(meta["path"])
        items = data.get("items", {}) or data.get("gui", {}).get("items", {})
        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            all_cmds = []
            for k in ["left_click_commands", "right_click_commands", "commands", "action"]:
                val = item_cfg.get(k)
                if isinstance(val, list):
                    all_cmds.extend(val)
                elif isinstance(val, str) and val:
                    all_cmds.append(val)
            
            for cmd in all_cmds:
                cmd_str = str(cmd).strip()
                # Check player commands: e.g. '[player] rankup', '[player] spawn', or '/rankup'
                player_cmd = None
                if cmd_str.startswith("[player]"):
                    player_cmd = cmd_str[len("[player]"):].strip()
                elif cmd_str.startswith("/"):
                    player_cmd = cmd_str[1:].strip()

                if player_cmd:
                    player_commands_checked += 1
                    if "<delay=" in player_cmd:
                        player_cmd = player_cmd[:player_cmd.index("<delay=")].strip()
                    root_cmd = player_cmd.split()[0].lower()
                    # Whitelist ignores sub-arguments; root command must be whitelisted
                    # Core server commands might be vanilla or in whitelist
                    # Check if root command is permitted
                    checks_count += 1
                    if root_cmd not in default_wl:
                        failures.append(
                            f"[{menu_key}] Item '{item_id}' executes player command '/{player_cmd}' "
                            f"(root '{root_cmd}'). Command '{root_cmd}' is NOT permitted in CommandWhitelist default group! (Whitelisted: {sorted(list(default_wl))})"
                        )

    # -------------------------------------------------------------
    # SUITE 3: Slot Integrity, Overflows, Duplicate entries in lists
    # -------------------------------------------------------------
    for menu_key, meta in MENUS.items():
        data = load_yaml(meta["path"])
        items = data.get("items", {}) or data.get("gui", {}).get("items", {})
        size = meta["size"]

        all_mapped_slots = defaultdict(list)

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue

            item_slots = []
            if "slot" in item_cfg:
                s = item_cfg["slot"]
                if not isinstance(s, int):
                    failures.append(f"[{menu_key}] '{item_id}' slot {s} is not an integer")
                else:
                    item_slots.append(s)

            if "slots" in item_cfg:
                raw_s = item_cfg["slots"]
                if not isinstance(raw_s, list):
                    failures.append(f"[{menu_key}] '{item_id}' slots is not a list")
                else:
                    # Check for duplicates WITHIN the item's own slots list!
                    if len(raw_s) != len(set(raw_s)):
                        failures.append(f"[{menu_key}] '{item_id}' has duplicate slots in its own 'slots' list: {raw_s}")
                    for s in raw_s:
                        if not isinstance(s, int):
                            failures.append(f"[{menu_key}] '{item_id}' slots contains non-integer: {s}")
                        else:
                            item_slots.append(s)

            for s in item_slots:
                checks_count += 1
                if s < 0 or s >= size:
                    failures.append(f"[{menu_key}] '{item_id}' slot {s} is out of bounds [0, {size-1}]")
                all_mapped_slots[s].append((item_id, item_cfg))

        # Check return button slot
        if meta["expected_return"] is not None:
            checks_count += 1
            ret_slot = meta["expected_return"]
            if ret_slot not in all_mapped_slots:
                failures.append(f"[{menu_key}] Missing item at expected return slot {ret_slot}")
            else:
                items_at_ret = all_mapped_slots[ret_slot]
                # Return button should not collide with moldura glass pane!
                for i_id, i_cfg in items_at_ret:
                    if "moldura" in i_id or "borda" in i_id:
                        failures.append(f"[{menu_key}] Return slot {ret_slot} is mapped by border glass pane '{i_id}'!")

        # Check close button slot
        if meta["expected_close"] is not None:
            checks_count += 1
            close_slot = meta["expected_close"]
            if close_slot not in all_mapped_slots:
                failures.append(f"[{menu_key}] Missing item at expected close slot {close_slot}")
            else:
                items_at_close = all_mapped_slots[close_slot]
                for i_id, i_cfg in items_at_close:
                    if "moldura" in i_id or "borda" in i_id:
                        failures.append(f"[{menu_key}] Close slot {close_slot} is mapped by border glass pane '{i_id}'!")

    # -------------------------------------------------------------
    # SUITE 4: Lore 3-Section Format & Placeholders Validation
    # -------------------------------------------------------------
    placeholder_pattern = re.compile(r"%([a-zA-Z0-9_]+)%")
    dangling_placeholder_pattern = re.compile(r"%([a-zA-Z0-9_]+)(?!\w)(?!%)")

    for menu_key, meta in MENUS.items():
        data = load_yaml(meta["path"])
        items = data.get("items", {}) or data.get("gui", {}).get("items", {})

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue
            lore = item_cfg.get("lore", [])
            if not lore:
                continue

            lore_lines = [str(l) for l in lore]
            # Check for dangling unclosed placeholders like %player_name without ending %
            for l_idx, line in enumerate(lore_lines):
                checks_count += 1
                # Strip valid literal percentages like 20% or 0.1%
                line_no_literals = re.sub(r"\d+(?:\.\d+)?%", "", line)
                pct_count = line_no_literals.count("%")
                if pct_count % 2 != 0:
                    failures.append(f"[{menu_key}] Item '{item_id}' line {l_idx} has odd number of '%' signs (unclosed placeholder?): '{line}'")

            # Check 3 sections for interactive buttons
            action_field = str(item_cfg.get("action", "")).strip().lower()
            has_action = action_field not in ["", "none", "[none]"]
            has_commands = (
                bool(item_cfg.get("left_click_commands"))
                or bool(item_cfg.get("right_click_commands"))
                or bool(item_cfg.get("commands"))
                or has_action
            )

            is_interactive = has_commands and not any(kw in item_id.lower() for kw in ["borda", "painel", "divider", "info"])
            if is_interactive:
                checks_count += 1
                blank_indices = [i for i, line in enumerate(lore_lines) if line.strip() in ["", "''", '""']]
                if len(blank_indices) < 2:
                    failures.append(f"[{menu_key}] Interactive item '{item_id}' lacks 2 empty lines separating 3 sections: {lore}")
                else:
                    # Verify Section 1 Header
                    header = [lore_lines[i] for i in range(0, blank_indices[0])]
                    # Verify Section 2 Body
                    body = [lore_lines[i] for i in range(blank_indices[0] + 1, blank_indices[-1])]
                    # Verify Section 3 Footer
                    footer = [lore_lines[i] for i in range(blank_indices[-1] + 1, len(lore_lines))]

                    if not header:
                        failures.append(f"[{menu_key}] '{item_id}' Section 1 (Header) is empty")
                    if not body:
                        failures.append(f"[{menu_key}] '{item_id}' Section 2 (Body) is empty")
                    if not footer:
                        failures.append(f"[{menu_key}] '{item_id}' Section 3 (Footer) is empty")

                    # Check footer prompt
                    footer_text = " ".join(footer)
                    if not re.search(r"[▶»>✕]\s*(Clique para|Bloqueado)", footer_text, re.IGNORECASE):
                        failures.append(f"[{menu_key}] '{item_id}' Footer lacks required action prompt: '{footer_text}'")

    # -------------------------------------------------------------
    # SUITE 5: Navigation Graph & Reachability Matrix
    # -------------------------------------------------------------
    # Verify Hub reaches all submenus, and all submenus reach Hub
    hub_data = load_yaml(MENUS["menu_hub"]["path"])
    hub_items = hub_data.get("items", {})
    hub_targets = set()
    for item_id, item_cfg in hub_items.items():
        if not isinstance(item_cfg, dict):
            continue
        cmds = (
            item_cfg.get("left_click_commands", [])
            + item_cfg.get("right_click_commands", [])
            + (item_cfg.get("commands", []) if isinstance(item_cfg.get("commands"), list) else [item_cfg.get("commands", "")])
            + [item_cfg.get("action", "")]
        )
        for c in cmds:
            hub_targets.add(str(c).lower().strip())

    # Target requirements from Hub
    core_systems = {
        "Minas": ["[openguimenu] minas", "/minaslista"],
        "Ranks": ["/ranks", "[player] ranks"],
        "Terrenos": ["/terrenos", "[player] terrenos"],
        "Máquinas": ["/maquinas", "[player] maquinas"],
        "Spawners": ["/spawners", "[player] spawners"],
        "Farms": ["/farms", "[player] farms"],
        "Caixas": ["/caixas", "[player] caixas"],
        "Loja": ["/shop", "[player] shop"],
        "Kits": ["/kits", "[player] kits"],
        "Cosméticos": ["/cosmetics", "[player] cosmetics"],
    }

    hub_target_blob = " ".join(hub_targets)
    for sys_name, expected_cmds in core_systems.items():
        checks_count += 1
        found = any(ec.lower() in hub_target_blob for ec in expected_cmds)
        if not found:
            failures.append(f"Central Hub cannot reach {sys_name} via {expected_cmds}!")

    # Check Return paths from every submenu
    for menu_key, meta in MENUS.items():
        if meta["is_hub"]:
            continue
        checks_count += 1
        data = load_yaml(meta["path"])
        items = data.get("items", {}) or data.get("gui", {}).get("items", {})
        ret_slot = meta["expected_return"]
        ret_item = None
        for i_id, i_cfg in items.items():
            if isinstance(i_cfg, dict) and (i_cfg.get("slot") == ret_slot or (isinstance(i_cfg.get("slots"), list) and ret_slot in i_cfg.get("slots"))):
                ret_item = i_cfg
                break

        if not ret_item:
            failures.append(f"[{menu_key}] Could not find return item at slot {ret_slot}")
        else:
            cmds = (
                ret_item.get("left_click_commands", [])
                + ret_item.get("right_click_commands", [])
                + (ret_item.get("commands", []) if isinstance(ret_item.get("commands"), list) else [ret_item.get("commands", "")])
                + [ret_item.get("action", "")]
            )
            blob = " ".join(str(c).lower() for c in cmds)
            if not ("principal" in blob or "menu" in blob or "ajuda" in blob or "back" in blob or "[openguimenu]" in blob):
                failures.append(f"[{menu_key}] Return item at slot {ret_slot} does not navigate back to Hub/Parent: '{blob}'")

    print(f"\nCompleted Deep Adversarial Suite.")
    print(f"Total assertions & checks executed: {checks_count}")
    print(f"Total Failures: {len(failures)}")
    print(f"Total Warnings: {len(warnings)}")

    if warnings:
        print("\n--- WARNING DETAILS ---")
        for w in warnings:
            print(f"[*] {w}")

    if failures:
        print("\n--- FAILURE DETAILS ---")
        for f in failures:
            print(f"[!] {f}")
        return False
    else:
        print("\n>>> ALL DEEP ADVERSARIAL ASSERTIONS PASSED (100% GREEN) <<<")
        return True

if __name__ == "__main__":
    ok = run_deep_adversarial_suite()
    sys.exit(0 if ok else 1)
