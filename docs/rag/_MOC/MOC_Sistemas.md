---
title: "MOC — Sistemas e Mecânicas"
aliases: ["MOC Sistemas", "Sistemas"]
tags:
  - tw/moc
  - tw/sistemas
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ **MOC Sistemas**

# ⚙️ Central de Sistemas e Mecânicas do Jogo

> [!info] Visão Geral
> Esta central reúne todas as notas atômicas dos sistemas desenvolvidos sob a suíte proprietária `tw-*`, detalhando custos, fórmulas de rendimento e regras operacionais.

---

## 📦 Lista de Sistemas Atômicos

| Sistema / Plugin | Arquivo de Nota | Função Principal | Integrações Chave |
| :--- | :--- | :--- | :--- |
| **tw-ranks** | [[tw_ranks]] | 11 Ranks lineares, 3 Prestígios e recompensas por correio | [[tw_core]], [[MOC_Economia]] |
| **tw-maquinas** | [[tw_maquinas]] | Geração autônoma de blocos com combustível e ciclos de tempo | [[tabela_precos]], [[mundo_terrenos]] |
| **tw-spawners** | [[tw_spawners]] | Abate automático de mobs, tokens especiais e upgrades | [[tw_caixas]], [[mundo_terrenos]] |
| **tw-farms** | [[tw_farms]] | Silos agrícolas de 50k, fertilizantes e alquimia de XP/Almas | [[tw_spawners]], [[mundo_terrenos]] |
| **tw-caixas** | [[tw_caixas]] | Caixas misteriosas com pity de 50 aberturas e forja divina | [[tw_minas]], [[tw_spawners]] |
| **tw-minas** | [[tw_minas]] | Eventos de mineração, Happy Hour 2.0x, Presentes e Meteorito | [[mundo_minas]], [[tabela_precos]] |
| **tw-terrenos** | [[tw_terrenos]] | Compra de plots no PlotSquared por R$ 50k e quotas de blocos | [[mundo_terrenos]], [[tw_spawners]] |
| **tw-core** | [[tw_core]] | Conexão PostgreSQL, Scoreboard de 20 ticks e placeholders | [[MOC_Geral]] |

---

## 🔄 Interconexões entre Sistemas

```mermaid
graph LR
    tw_minas["[[tw_minas]]"] -->|Drop 0.1%| tw_caixas["[[tw_caixas]]"]
    tw_spawners["[[tw_spawners]]"] -->|Gera Almas & Tokens| tw_farms["[[tw_farms]]"]
    tw_spawners -->|Drop 0.05%| tw_caixas
    tw_maquinas["[[tw_maquinas]]"] -->|Gera Dinheiro Passivo| tw_ranks["[[tw_ranks]]"]
    tw_farms -->|Venda de Silo| tw_ranks
    tw_ranks -->|Desbloqueia Máquinas & Mobs| tw_maquinas
    tw_ranks -->|Desbloqueia| tw_spawners
    tw_terrenos["[[tw_terrenos]]"] -->|Hospeda| tw_maquinas
    tw_terrenos -->|Hospeda (máx 25)| tw_spawners
```

---
⬅️ [[MOC_Geral|Voltar ao Mapa Geral]] | ➡️ [[tw_ranks|Acessar tw_ranks]]
