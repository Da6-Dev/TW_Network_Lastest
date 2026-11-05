---
title: "Sistema de Máquinas Industriais"
aliases: ["tw-maquinas", "maquinas", "máquinas"]
tags:
  - tw/sistema
  - tw/maquinas
  - tw/economia
plugin_fonte: "tw-maquinas"
arquivo_config: "plugins/tw-maquinas/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_maquinas**

# ⚙️ Sistema de Máquinas Industriais (`tw-maquinas`)

> [!info] Visão Rápida
> Máquinas são blocos colocados nos terrenos do jogador ([[mundo_terrenos]]) que geram renda passiva em dinheiro ($) a cada ciclo de segundos enquanto possuírem combustível.

---

## ⛽ Sistema de Combustível

- **Preço de Compra:** **R$ 5.000,00**
- **Unidades Fornecidas:** **100 cargas de combustível** por compra.
- Cada ciclo de operação consome cargas das máquinas ativas.
- **Threshold de Confirmação:** Compras acima de **R$ 250.000,00** exigem confirmação gráfica no GUI.

---

## 🏭 Tabela de Máquinas e Rendimentos

| Máquina | Material do Bloco | Rank Mínimo | Custo de Aquisição | Rendimento por Ciclo | Intervalo | Rendimento / Minuto |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Carvão** | `COAL_BLOCK` | CARVAO | R$ 50.000,00 | R$ 1.200,00 | 10 seg | R$ 7.200,00 |
| **Neve** | `SNOW_BLOCK` | NEVE | R$ 1.500.000,00 | R$ 35.000,00 | 10 seg | R$ 210.000,00 |
| **Sino** | `GOLD_BLOCK` | SINO | R$ 45.000.000,00 | R$ 1.100.000,00 | 10 seg | R$ 6.600.000,00 |
| **Biscoito**| `HAY_BLOCK` | BISCOITO | R$ 800.000.000,00 | R$ 20.000.000,00 | 8 seg | R$ 150.000.000,00 |
| **Duende** | `EMERALD_BLOCK` | DUENDE | R$ 25.000.000.000,00 | R$ 650.000.000,00 | 8 seg | R$ 4.875.000.000,00 |
| **Rena** | `REDSTONE_BLOCK`| RENA | R$ 750.000.000.000,00 | R$ 22.000.000.000,00 | 6 seg | R$ 220.000.000.000,00 |
| **Noel** | `BEACON` | NOEL | R$ 25 Quadrilhões | R$ 850 Trilhões | 5 seg | R$ 10.2 Quadrilhões |

---

> [!tip] Dica de Automação
> A cada ciclo de máquina, há uma chance de **0,03% (0.0003)** de obter uma [[tw_caixas|Caixa Tecnológica]], que pode conter Certificados de Overclock e Baterias de Cargas!

> [!warning] Onde Colocar?
> As máquinas só funcionam e geram lucros quando posicionadas dentro dos seus lotes no mundo [[mundo_terrenos|terrenos]].

---
⬅️ [[tw_ranks|Nota Anterior: tw_ranks]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_spawners|Próxima Nota: tw_spawners]]
