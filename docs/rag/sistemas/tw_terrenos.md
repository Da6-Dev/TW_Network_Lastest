---
title: "Sistema de Terrenos e Plots"
aliases: ["tw-terrenos", "terrenos", "plots"]
tags:
  - tw/sistema
  - tw/terrenos
  - tw/construcao
plugin_fonte: "tw-terrenos"
arquivo_config: "plugins/tw-terrenos/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_terrenos**

# 🏡 Sistema de Terrenos e Plots (`tw-terrenos`)

> [!info] Visão Geral
> Gerencia a integração de compra de lotes de construção no mundo [[mundo_terrenos|terrenos]], operando em conjunto com o motor do **PlotSquared 7.6.x**.

---

## 📐 Especificações dos Lotes

- **Mundo Alvo:** `terrenos`
- **Preço de Compra por Plot:** **R$ 50.000,00**
- **Dimensões do Plot:** 42x42 blocos de área útil.
- **Altura da Superfície:** Camada Y = 62 (Blocos de Grama).
- **Subsolo:** Preenchido com Pedra até a base rochosa (Bedrock).
- **Estradas:** Largura de 7 blocos em Bloco de Quartzo (`QUARTZ_BLOCK`).

---

## ⚡ Regras de Construção e Instalação

> [!warning] Quota de Spawners
> Cada plot pode hospedar no máximo **25 geradores de monstros** ([[tw_spawners]]) para garantir a estabilidade do servidor.

> [!tip] Comandos Úteis
> - `/terreno`: Abre menu de ajuda e opções de terreno.
> - `/terreno claim`: Reivindica o lote livre onde o jogador está pisando (custo: R$ 50k).
> - `/terreno auto`: Encontra e compra automaticamente o lote vago mais próximo.
> - `/terreno home`: Teleporta o jogador de volta para o seu lote principal.

---
⬅️ [[tw_caixas|Nota Anterior: tw_caixas]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_minas|Próxima Nota: tw_minas]]
