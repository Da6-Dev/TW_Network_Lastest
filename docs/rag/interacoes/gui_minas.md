---
title: "Interface: GUI Central de Minas"
aliases: ["gui minas", "minas.yml", "deluxemenus minas"]
tags:
  - tw/interacoes
  - tw/gui
  - tw/deluxemenus
plugin_fonte: "DeluxeMenus"
arquivo_config: "plugins/DeluxeMenus/gui_menus/menus/minas.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Interacoes|Interações]] ➔ **gui_minas**

# ⛏️ Interface: GUI Central de Minas (`minas.yml`)

> [!info] Visão Geral
> Interface gráfica de 54 slots (6 linhas) acessada via `/minaslista` ou `/minhasminas`, exibindo a lista de todas as minas do servidor e seus requisitos de liberação.

---

## 🔒 Mecânica de Requisitos
- Cada mina é representada visualmente pelo bloco característico daquele rank (ex: Minério de Carvão no Slot 10 para a Mina Carvão, Bloco de Neve para Mina Neve, etc.).
- **Minas Liberadas:** O jogador pode clicar para ser teleportado diretamente ao ponto de spawn da mina no mundo [[mundo_minas|minas]].
- **Minas Bloqueadas:** O menu exibe em vermelho o rank necessário para desbloqueio, bloqueando o teleporte até que o jogador use [[tw_ranks|/rankup]].

---
⬅️ [[gui_menu_principal|Nota Anterior: GUI Menu Principal]] | 🔼 [[MOC_Interacoes|Voltar a Interações]] | ➡️ [[jornada_jogador|Ir para Jornada do Jogador]]
