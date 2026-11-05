---
title: "Hologramas do Spawn e Lobby"
aliases: ["hologramas", "fancyholograms", "holograma boas vindas"]
tags:
  - tw/interacoes
  - tw/hologramas
plugin_fonte: "FancyHolograms"
arquivo_config: "plugins/FancyHolograms/holograms.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Interacoes|Interações]] ➔ **hologramas**

# ✨ Hologramas do Spawn e Lobby (`FancyHolograms`)

> [!info] Visão Geral
> Textos flutuantes de alto impacto visual utilizados para orientar o jogador e exibir informações dinâmicas em tempo real.

---

## 1. 🏷️ Holograma do NPC de Menu (`npc-menu`)
- **Finalidade:** Sinalizar a existência do [[npc_menu|NPC Menu]].
- **Localização:** Mundo `world`, **X:** 306.47, **Y:** 90.36, **Z:** 248.79 (Flutuando 3 blocos acima da cabeça do NPC).
- **Escala:** 1.1x | Fundo: Transparente | Alinhamento: Centralizado.
- **Texto:**
  ```text
  ✨ MENU PRINCIPAL ✨
  Minas • Kits • Mercado
  CLIQUE PARA ABRIR (Botão Direito)
  ```

---

## 2. 👋 Holograma de Boas-Vindas (`boas-vindas`)
- **Finalidade:** Recepção inicial e exibição do status do jogador.
- **Localização:** Mundo `world`, **X:** 311.48, **Y:** 87.62, **Z:** 252.67 (Em frente ao ponto de spawn).
- **Atualização:** A cada 20 ticks (1 segundo) para manter os números em tempo real.
- **Placeholders Utilizados:**
  - `%player_name%`: Nome do jogador.
  - `%luckperms_prefix%`: Tag e Rank atual.
  - `%vault_eco_balance_formatted%`: Saldo monetário em dinheiro ($).
- **Texto:**
  ```text
  ❄️ TW NETWORK ❄️
  A sua jornada começa aqui!
  Olá, %player_name%!
  Seu Rank: %luckperms_prefix%
  Saldo: $%vault_eco_balance_formatted%
  Interaja com o NPC ou digite /menu!
  ```

---
⬅️ [[npc_menu|Nota Anterior: npc_menu]] | 🔼 [[MOC_Interacoes|Voltar a Interações]] | ➡️ [[gui_menu_principal|Próxima Nota: GUI Menu Principal]]
