---
title: "Sistema de Geradores e Spawners"
aliases: ["tw-spawners", "spawners", "geradores"]
tags:
  - tw/sistema
  - tw/spawners
  - tw/economia
plugin_fonte: "tw-spawners"
arquivo_config: "plugins/tw-spawners/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_spawners**

# 🧟 Sistema de Geradores e Spawners (`tw-spawners`)

> [!info] Visão Geral
> Geradores de monstros operam nos lotes do mundo [[mundo_terrenos|terrenos]], gerando abates automáticos com lucros financeiros diretos e **Tokens Especiais** utilizados para melhorias.

---

## 🔒 Limitações Globais e Quotas

- **Limite por Terreno:** Máximo de **25 spawners por lote** (para preservação do TPS).
- **Limite por Jogador:** Máximo de **100 geradores próprios**.
- **Empilhamento de Mobs:** Até 32 entidades empilhadas por gerador.
- **Autosave:** A cada 60 segundos.
- **Teto de Upgrades:**
  - Velocidade: Nível 19.
  - Loot: Nível 100.
  - Quantidade: Nível 10.000.

---

## 📊 Tabela de Geradores

| Spawner | Entidade | Rank Requerido | Custo de Compra | Valor por Abate | Chance de Drop de Token |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Porcos** | `PIG` | CARVAO | R$ 100.000,00 | R$ 800,00 | 15% (0.15) |
| **Vacas** | `COW` | NEVE | R$ 2.500.000,00 | R$ 18.000,00 | 20% (0.20) |
| **Aranhas** | `SPIDER` | SINO | R$ 65.000.000,00 | R$ 450.000,00 | 25% (0.25) |
| **Zumbis** | `ZOMBIE` | BISCOITO | R$ 1.200.000.000,00 | R$ 9.000.000,00 | 30% (0.30) |
| **Blazes** | `BLAZE` | DUENDE | R$ 40.000.000.000,00 | R$ 320.000.000,00 | 40% (0.40) |
| **Iron Golem**| `IRON_GOLEM`| RENA | R$ 1.500.000.000.000,00 | R$ 12.000.000.000,00 | 50% (0.50) |

---

> [!tip] Utilidade dos Tokens e Almas
> Os tokens acumulados em abates alimentam o sistema de upgrades de silos do [[tw_farms]] e abrem oportunidades de transmutação alquímica!
> A cada abate, há uma chance de **0,05%** de dropar uma [[tw_caixas|Caixa Sanguinária]].

---
⬅️ [[tw_maquinas|Nota Anterior: tw_maquinas]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_farms|Próxima Nota: tw_farms]]
