---
title: "Interface: GUI Menu Principal"
aliases: ["gui menu principal", "menu.yml", "deluxemenus menu"]
tags:
  - tw/interacoes
  - tw/gui
  - tw/deluxemenus
plugin_fonte: "DeluxeMenus"
arquivo_config: "plugins/DeluxeMenus/gui_menus/menus/menu.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Interacoes|Interações]] ➔ **gui_menu_principal**

# 📜 Interface: GUI Menu Principal (`menu.yml`)

> [!abstract] Central Visual
> Menu em formato de baú com 45 slots (5 linhas) aberto ao digitar `/menu`, `/ajuda` ou interagir com o [[npc_menu|NPC Menu]].

---

## 🎛️ Mapa de Slots e Funções

```text
[Slot 00-08]: Moldura em Painel de Vidro Preto
[Slot 04]:    PERFIL DO JOGADOR (head-%player_name%)
              Exibe: Nome, Saldo formatado e Grupo LuckPerms.

[Slot 20]:    IR MINERAR (DIAMOND_PICKAXE)
              Ação: Som UI_BUTTON_CLICK e comando /mina.

[Slot 22]:    KITS DA MINA PVP (CHEST)
              Ação: Som BLOCK_CHEST_OPEN e comando /kits.

[Slot 24]:    MERCADO & LOJA (EMERALD)
              Ação: Som ENTITY_EXPERIENCE_ORB_PICKUP e comando /shop.

[Slot 31]:    COSMÉTICOS (NETHER_STAR)
              Ação: Som ENTITY_PLAYER_LEVELUP e comando /cosmetics.

[Slot 40]:    FECHAR MENU (BARRIER)
```

---
⬅️ [[hologramas|Nota Anterior: Hologramas]] | 🔼 [[MOC_Interacoes|Voltar a Interações]] | ➡️ [[gui_minas|Próxima Nota: GUI Central de Minas]]
