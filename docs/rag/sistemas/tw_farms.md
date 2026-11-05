---
title: "Sistema Agrícola e Alquimia"
aliases: ["tw-farms", "farms", "fazendas", "alquimia"]
tags:
  - tw/sistema
  - tw/farms
  - tw/alquimia
plugin_fonte: "tw-farms"
arquivo_config: "plugins/tw-farms/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_farms**

# 🌾 Sistema Agrícola e Alquimia (`tw-farms`)

> [!info] Visão Geral
> Permite a produção agrícola automatizada nos terrenos ([[mundo_terrenos]]) com armazenamento em **Silos Inteligentes**, uso de fertilizantes químicos e transmutação por **Alquimia**.

---

## 🏬 Silos Agrícolas e Upgrades

- **Capacidade Base do Silo:** **50.000 unidades**.
- **Processamento por Ciclo:** Até 250 itens por ciclo.
- **Nível Máximo de Melhorias:** Nível 25.
- **Custos em Tokens (obtidos no [[tw_spawners]]):**
  - Upgrade de Velocidade: 1.000 tokens base.
  - Upgrade de Armazenamento: 800 tokens base.
  - Upgrade de Qualidade: 1.200 tokens base.
  - Upgrade de Auto-Venda: 5.000 tokens (vende excedente automaticamente).

---

## 🌱 Cultivos e Safras Disponíveis

| Cultivo | Produto | Rank Requerido | Custo da Semente | Valor de Venda | Ciclo Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Trigo** | `WHEAT` | CARVAO | R$ 50.000,00 | R$ 20,00 | 15 seg |
| **Cenoura** | `CARROT` | SINO | R$ 500.000,00 | R$ 80,00 | 14 seg |
| **Batata** | `POTATO` | SINO | R$ 500.000,00 | R$ 80,00 | 14 seg |
| **Cana-de-Açúcar**| `SUGAR_CANE`| BISCOITO | R$ 5.000.000,00 | R$ 350,00 | 12 seg |
| **Cacto** | `CACTUS` | RENA | R$ 50.000.000,00 | R$ 1.500,00 | 10 seg |
| **Melancia** | `MELON_SLICE`| RENA | R$ 50.000.000,00 | R$ 1.800,00 | 10 seg |
| **Fungo do Nether**|`NETHER_WART`| NOEL | R$ 500.000.000,00 | R$ 15.000,00 | 8 seg |

---

## 🧪 Fertilizantes e Alquimia

### Fertilizantes Comerciais
- **Pequeno:** $1.000,00 (100 un, Solo Nível 1, 1.0x tempo, 5% safra dourada).
- **Médio:** $9.000,00 (1.000 un, Solo Nível 2, 0.8x tempo, 10% safra dourada).
- **Industrial:** $80.000,00 (10.000 un, Solo Nível 3, 0.6x tempo, 15% safra dourada).

### Fórmulas de Alquimia
- **Transmutação por XP:** 250 XP + 8 Esmeraldas ➔ 1.000 Fertilizantes Nível 2.
- **Transmutação por Almas (Souls):** 25 Almas + 4 Diamantes ➔ 5.000 Fertilizantes Nível 3.

> [!tip] Drops Especiais
> Cada safra colhida tem **0,1% (0.001)** de chance de conceder uma [[tw_caixas|Caixa da Natureza]] (contendo Foice Dourada e Sementes Mutantes).

---
⬅️ [[tw_spawners|Nota Anterior: tw_spawners]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_caixas|Próxima Nota: tw_caixas]]
