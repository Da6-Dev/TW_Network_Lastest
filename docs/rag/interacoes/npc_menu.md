---
title: "NPC do Menu Principal"
aliases: ["npc menu", "npc principal", "fancynpcs"]
tags:
  - tw/interacoes
  - tw/npc
plugin_fonte: "FancyNpcs"
arquivo_config: "plugins/FancyNpcs/npcs.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Interacoes|Interações]] ➔ **npc_menu**

# 🤖 NPC do Menu Principal (`FancyNpcs`)

> [!abstract] Resumo
> Entidade interativa estática posicionada no Lobby principal para recepcionar jogadores e abrir o [[gui_menu_principal|Menu Principal]] com um único clique.

---

## 📍 Coordenadas e Propriedades

- **Nome Interno:** `menu`
- **UUID:** `2ef7c583-bf01-4efc-9276-573c035f6af4`
- **Tipo:** `PLAYER`
- **Mundo:** `world` ([[mundo_lobby]])
- **Coordenadas Exatas:**
  - **X:** `306.4058`
  - **Y:** `87.0000`
  - **Z:** `248.4634`
  - **Yaw:** `0.1464` | **Pitch:** `2.1000`
- **Skin:** `nielspp` (Visual temático de Ajudante de Natal)
- **Escala Visual:** `1.5x` (50% maior que um jogador comum para destaque)
- **Comportamento:**
  - `turnToPlayer: true` (Gira a cabeça acompanhando o jogador que se aproxima)
  - `collidable: true`

---

## 👆 Ações de Interação

- **Clique com Botão Direito (`RIGHT_CLICK`):**
  - Dispara a ação `player_command` com valor `menu`.
  - Abre imediatamente a interface [[gui_menu_principal|DeluxeMenus menu.yml]].

---
⬅️ [[MOC_Interacoes|Voltar a Interações]] | ➡️ [[hologramas|Próxima Nota: Hologramas]]
