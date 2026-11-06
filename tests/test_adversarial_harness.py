"""
Adversarial Stress Harness & Fuzzer for Minecraft Server GUI Ecosystem.
Challenger 1 Empirical Verification Suite.
"""

import os
import re
import sys
import yaml

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MENUS = {
    "menu_hub": {
        "path": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "menu.yml"),
        "is_hub": True,
        "size": 54,
        "type": "deluxemenus",
    },
    "menu_minas": {
        "path": os.path.join(BASE_DIR, "plugins", "DeluxeMenus", "gui_menus", "menus", "minas.yml"),
        "is_hub": False,
        "size": 54,
        "type": "deluxemenus",
    },
    "tw_ranks": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-ranks", "menus", "ranks.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
    "tw_terrenos": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-terrenos", "menus", "terrenos.yml"),
        "is_hub": False,
        "size": 27,
        "type": "tw_custom",
    },
    "tw_maquinas": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-maquinas", "menus", "maquinas.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
    "tw_spawners": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-spawners", "menus", "spawners.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
    "tw_farms": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-farms", "menus", "farms.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
    "tw_caixas": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-caixas", "menus", "caixas.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
    "tw_minas_extra": {
        "path": os.path.join(BASE_DIR, "plugins", "tw-minas", "menus", "minas_extra.yml"),
        "is_hub": False,
        "size": 54,
        "type": "tw_custom",
    },
}

def load_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_items(menu_data):
    if "items" in menu_data and isinstance(menu_data["items"], dict):
        return menu_data["items"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("items", {})
    return {}

def get_size(menu_data):
    if "size" in menu_data:
        return menu_data["size"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("size")
    return None

def get_title(menu_data):
    if "menu_title" in menu_data:
        return menu_data["menu_title"]
    if "title" in menu_data:
        return menu_data["title"]
    if "gui" in menu_data and isinstance(menu_data["gui"], dict):
        return menu_data["gui"].get("title") or menu_data["gui"].get("menu_title")
    return None

def extract_strings(obj):
    """Recursively extracts all string values from a nested dict/list structure."""
    strings = []
    if isinstance(obj, str):
        strings.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            strings.extend(extract_strings(v))
    elif isinstance(obj, list):
        for v in obj:
            strings.extend(extract_strings(v))
    return strings

def run_stress_test():
    failures = []
    warnings = []
    passed_checks = 0

    print("=== STARTING ADVERSARIAL STRESS HARNESS ===")

    # 1. TEST ALL MENU FILES EXISTENCE AND SIZE
    for menu_key, meta in MENUS.items():
        path = meta["path"]
        if not os.path.isfile(path):
            failures.append(f"[{menu_key}] File does not exist at {path}")
            continue
        try:
            data = load_yaml(path)
        except Exception as e:
            failures.append(f"[{menu_key}] YAML parse failed: {e}")
            continue

        size = get_size(data)
        if size != meta["size"]:
            failures.append(f"[{menu_key}] Expected size {meta['size']}, got {size}")
        else:
            passed_checks += 1

        title = get_title(data)
        if not title:
            failures.append(f"[{menu_key}] Title is missing or empty")
        else:
            passed_checks += 1
            # Check title format: &8➔ or color code
            if not re.search(r"^(&8|&#[0-9a-fA-F]{6}|&x(&[0-9a-fA-F]){6})[➔»]\s*(.+)$", title):
                failures.append(f"[{menu_key}] Title '{title}' does not match prefix &8➔ or hex variant")
            else:
                passed_checks += 1

        items = get_items(data)
        if not items:
            failures.append(f"[{menu_key}] No items found")
            continue

        # 2. CHECK ALL SLOTS ARE STRICTLY INTEGERS AND WITHIN [0, size-1]
        # Also check slot collisions
        slot_assignments = {} # slot -> list of (item_id, item_cfg)

        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                failures.append(f"[{menu_key}] Item '{item_id}' is not a dict")
                continue

            slots = []
            if "slot" in item_cfg:
                raw_slot = item_cfg["slot"]
                if not isinstance(raw_slot, int) or isinstance(raw_slot, bool):
                    failures.append(f"[{menu_key}] Item '{item_id}' has non-integer slot: {raw_slot} (type {type(raw_slot)})")
                else:
                    slots.append(raw_slot)

            if "slots" in item_cfg:
                raw_slots = item_cfg["slots"]
                if not isinstance(raw_slots, list):
                    failures.append(f"[{menu_key}] Item '{item_id}' 'slots' is not a list: {raw_slots}")
                else:
                    for s in raw_slots:
                        if not isinstance(s, int) or isinstance(s, bool):
                            failures.append(f"[{menu_key}] Item '{item_id}' in 'slots' has non-integer: {s}")
                        else:
                            slots.append(s)

            if not slots:
                failures.append(f"[{menu_key}] Item '{item_id}' has no slot or slots configured")

            for s in slots:
                if s < 0 or s >= size:
                    failures.append(f"[{menu_key}] Item '{item_id}' has out-of-bounds slot {s} (size={size}, valid 0..{size-1})")
                else:
                    passed_checks += 1

                if s not in slot_assignments:
                    slot_assignments[s] = []
                slot_assignments[s].append((item_id, item_cfg))

        # Check for slot collisions
        for s, assigned in slot_assignments.items():
            if len(assigned) > 1:
                # If more than 1 item, verify if this is a valid conditional overlay
                priorities = [cfg.get("priority") for _, cfg in assigned]
                view_reqs = [cfg.get("view_requirement") for _, cfg in assigned]
                
                # If any priority is None, or priorities are duplicate, check:
                if any(p is None for p in priorities) or len(set(priorities)) != len(priorities):
                    item_names = [i[0] for i in assigned]
                    failures.append(
                        f"[{menu_key}] Slot {s} has unconditional collision between items: {item_names} (priorities: {priorities})"
                    )
                else:
                    passed_checks += 1

        # 3. VERIFY UNIVERSAL RETURN BUTTON (slot 45 in 54s, slot 18 in 27s)
        expected_ret_slot = 45 if size == 54 else 18
        if not meta["is_hub"]:
            ret_items = slot_assignments.get(expected_ret_slot, [])
            if not ret_items:
                failures.append(f"[{menu_key}] Missing required return button at slot {expected_ret_slot}")
            else:
                passed_checks += 1
                r_id, r_cfg = ret_items[0]
                mat = str(r_cfg.get("material", "")).upper()
                name = str(r_cfg.get("display_name", "") or r_cfg.get("name", ""))
                lore = r_cfg.get("lore", [])
                
                # Check material
                if not any(m in mat for m in ["ARROW", "DOOR", "BARRIER"]):
                    failures.append(f"[{menu_key}] Return item '{r_id}' at slot {expected_ret_slot} has unexpected material: '{mat}'")
                else:
                    passed_checks += 1

                # Check name
                if not any(w in name.lower() for w in ["voltar", "retornar", "menu"]):
                    failures.append(f"[{menu_key}] Return item '{r_id}' name does not indicate return: '{name}'")
                else:
                    passed_checks += 1

                # Check action / commands
                cmds = (
                    r_cfg.get("left_click_commands", [])
                    + r_cfg.get("right_click_commands", [])
                    + (r_cfg.get("commands", []) if isinstance(r_cfg.get("commands"), list) else [r_cfg.get("commands", "")])
                    + [r_cfg.get("action", "")]
                )
                cmd_blob = " ".join(str(c).lower() for c in cmds)
                if not any(tgt in cmd_blob for tgt in ["principal", "menu", "ajuda", "[openguimenu]", "back"]):
                    failures.append(f"[{menu_key}] Return button at slot {expected_ret_slot} target invalid: '{cmd_blob}'")
                else:
                    passed_checks += 1

        # 4. VERIFY UNIVERSAL CLOSE BUTTON (slot 49 in 54s, slot 22 in 27s)
        expected_close_slot = 49 if size == 54 else 22
        close_items = slot_assignments.get(expected_close_slot, [])
        if not close_items:
            failures.append(f"[{menu_key}] Missing required close button at slot {expected_close_slot}")
        else:
            passed_checks += 1
            c_id, c_cfg = close_items[0]
            mat = str(c_cfg.get("material", "")).upper()
            name = str(c_cfg.get("display_name", "") or c_cfg.get("name", ""))
            
            if "BARRIER" not in mat:
                failures.append(f"[{menu_key}] Close button '{c_id}' at slot {expected_close_slot} material is not BARRIER: '{mat}'")
            else:
                passed_checks += 1

            if not any(w in name.lower() for w in ["fechar", "sair", "close"]):
                failures.append(f"[{menu_key}] Close button '{c_id}' name does not indicate close: '{name}'")
            else:
                passed_checks += 1

            cmds = (
                c_cfg.get("left_click_commands", [])
                + c_cfg.get("right_click_commands", [])
                + (c_cfg.get("commands", []) if isinstance(c_cfg.get("commands"), list) else [c_cfg.get("commands", "")])
                + [c_cfg.get("action", "")]
            )
            cmd_blob = " ".join(str(c).lower() for c in cmds)
            if "[close]" not in cmd_blob and "close" not in cmd_blob and "fechar" not in cmd_blob:
                failures.append(f"[{menu_key}] Close button '{c_id}' does not execute [close]: '{cmd_blob}'")
            else:
                passed_checks += 1

        # 5. VERIFY 3-SECTION LORE FORMAT FOR INTERACTIVE ITEMS
        for item_id, item_cfg in items.items():
            if not isinstance(item_cfg, dict):
                continue

            material = str(item_cfg.get("material", "")).upper()
            display_name = item_cfg.get("display_name", "") or item_cfg.get("name", "")
            action_field = str(item_cfg.get("action", "")).strip().lower()
            has_action = action_field not in ["", "none", "[none]"]
            has_commands = (
                bool(item_cfg.get("left_click_commands"))
                or bool(item_cfg.get("right_click_commands"))
                or bool(item_cfg.get("commands"))
                or has_action
            )

            # Skip decorative moldura panes without display name
            if "GLASS_PANE" in material and (not display_name or display_name.strip() in ["", "' '"]):
                continue

            lore = item_cfg.get("lore", [])
            if not lore:
                # If it's an interactive item with commands but no lore, flag warning/failure
                if has_commands:
                    failures.append(f"[{menu_key}] Interactive item '{item_id}' has commands but no lore!")
                continue

            # Check 3 distinct sections separated by blank line ''
            # Count blank lines
            blank_indices = [i for i, line in enumerate(lore) if str(line).strip() in ["", "''", '""']]
            
            # For interactive buttons (has_commands), verify 3 sections:
            if has_commands and not any(kw in item_id.lower() for kw in ["borda", "painel", "divider", "info"]):
                # Should have at least 2 blank separators creating 3 sections
                if len(blank_indices) < 2:
                    warnings.append(
                        f"[{menu_key}] Item '{item_id}' has {len(blank_indices)} blank line separators (expected >= 2 for 3 distinct sections). Lore: {lore}"
                    )
                else:
                    # Section 1: lines 0..blank_indices[0]-1 (Header)
                    sec1 = lore[0:blank_indices[0]]
                    # Section 2: lines blank_indices[0]+1..blank_indices[-1]-1 (Body / Status)
                    sec2 = lore[blank_indices[0]+1:blank_indices[-1]]
                    # Section 3: lines blank_indices[-1]+1..end (Footer)
                    sec3 = lore[blank_indices[-1]+1:]

                    if not sec1:
                        failures.append(f"[{menu_key}] Item '{item_id}' Section 1 (Header) is empty")
                    if not sec2:
                        failures.append(f"[{menu_key}] Item '{item_id}' Section 2 (Body) is empty")
                    if not sec3:
                        failures.append(f"[{menu_key}] Item '{item_id}' Section 3 (Footer) is empty")

                # Check footer prompt regex
                lore_text = "\n".join(str(l) for l in lore)
                prompt_pattern = re.compile(
                    r"(&[a-f0-9]|&x(&[0-9a-fA-F]){6}|&#[0-9a-fA-F]{6})?[▶»>✕]\s*(Clique para|Bloqueado)",
                    re.IGNORECASE,
                )
                if not prompt_pattern.search(lore_text):
                    failures.append(f"[{menu_key}] Item '{item_id}' lacks required action footer '▶ Clique para...'. Lore: {lore}")
                else:
                    passed_checks += 1

        # 6. VERIFY ALL COLOR CODES AND HEX CODES
        # Extract all strings
        all_strs = extract_strings(data)
        for s in all_strs:
            # Check for invalid single-char color/format codes.
            # In Minecraft:
            # Colors: 0-9, a-f, A-F
            # Formats: k (magic), l (bold), m (strikethrough), n (underline), o (italic), r (reset)
            # Hex prefix: x
            # Invalid letters: g, h, i, j, p, q, s, t, u, v, w, y, z
            bad_codes = re.findall(r"&([g-jG-Jp-qP-Qs-wS-Wy-zY-Z])", s)
            if bad_codes:
                failures.append(f"[{menu_key}] Invalid Minecraft color code '&{bad_codes[0]}' in string: '{s}'")

            # Check for malformed hex codes like &#12345 (not 6 digits)
            malformed_hex1 = re.findall(r"&#([0-9a-fA-F]{1,5}|[0-9a-fA-F]{7,})(?![0-9a-fA-F])", s)
            if malformed_hex1:
                failures.append(f"[{menu_key}] Malformed hex code '&#{malformed_hex1[0]}' in string: '{s}'")

            # Check for malformed &x hex codes
            malformed_hex2 = re.findall(r"&x(?:&[0-9a-fA-F]){1,5}(?!&[0-9a-fA-F])", s)
            if malformed_hex2:
                failures.append(f"[{menu_key}] Malformed &x hex code '{malformed_hex2[0]}' in string: '{s}'")

            passed_checks += 1

    print(f"\nTotal empirical checks passed: {passed_checks}")
    print(f"Total failures: {len(failures)}")
    print(f"Total warnings: {len(warnings)}")

    if warnings:
        print("\n--- WARNINGS ---")
        for w in warnings:
            print(f"WARN: {w}")

    if failures:
        print("\n--- FAILURES ---")
        for f in failures:
            print(f"FAIL: {f}")
        return False
    else:
        print("\nALL ADVERSARIAL STRESS CHECKS PASSED WITH ZERO FAILURES!")
        return True

if __name__ == "__main__":
    success = run_stress_test()
    sys.exit(0 if success else 1)
