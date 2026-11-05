---
title: "Sistema de Eventos de Mineração"
aliases: ["tw-minas", "minas", "eventos de mina"]
tags:
  - tw/sistema
  - tw/minas
  - tw/mineracao
  - tw/eventos
plugin_fonte: "tw-minas"
arquivo_config: "plugins/tw-minas/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_minas**

# ⛏️ Sistema de Eventos de Mineração (`tw-minas`)

> [!abstract] Resumo Operacional
> O `tw-minas` gerencia a camada dinâmica de eventos da mineração em conjunto com o plugin [[mundo_minas|RealMines]], incluindo metas comunitárias, queda de presentes e meteoritos.

---

## 🌟 Eventos Dinâmicos da Mina

### 1. 🎯 Meta Comunitária e Happy Hour
- **Meta Global:** A cada **5.000 blocos** minerados coletivamente por todos os jogadores online.
- **Efeito (Happy Hour):** Duração de **180 segundos (3 minutos)**.
- **Multiplicador:** **2.0x** em todo o ganho monetário de venda de blocos minerados.

### 2. 🎁 Queda de Presentes de Natal
- **Chance por Bloco:** **0,3% (0.003)** por quebra de bloco.
- **Comportamento:** Um pacote de presente surge no piso da mina.
- **Tempo de Coleta:** **12 segundos** antes de sumir.

### 3. ☄️ Queda de Meteorito Misterioso
- **Chance de Queda:** **0,005% (0.00005)** por bloco minerado.
- **Pontos de Vida (HP):** 300 golpes necessários para destruir.
- **Recompensa por Hit:** **$50,00 a $100,00** por golpe desferido.
- **Recompensa de Conclusão:** **$5.000,00** e drops de itens raros para quem der o golpe final.

---

## ⚔️ Integração com a Mina PvP
- O plugin também monitora as sessões da arena hostil (`mina_pvp`), salvando o estado de combate a cada 100 ticks (5 segundos) e controlando o resgate de kits de batalha:
  - Kit Básico (Cooldown: 1 hora)
  - Kit VIP (Cooldown: 1 hora)
  - Kit Prestígio (Cooldown: 1 hora)
- Veja os detalhes completos em [[mundo_mina_pvp]].

---
⬅️ [[tw_terrenos|Nota Anterior: tw_terrenos]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_core|Próxima Nota: tw_core]]
