---
title: "Jornada do Jogador e Game Loop"
aliases: ["jornada do jogador", "game loop", "progressao", "end game"]
tags:
  - tw/game-loop
  - tw/progressao
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ **jornada_jogador**

# 🔄 Jornada do Jogador e Game Loop Completo

> [!abstract] Resumo do Ciclo de Jogo
> O ciclo de jogo do TW Network foi desenhado para transitar o jogador de uma **mineração manual inicial** para uma **gestão industrial automatizada** e, finalmente, para a **disputa de domínio nos Prestígios e no Top 1 do Baltop**.

---

## 🗺️ Mapa de Fases da Jornada

```mermaid
flowchart TD
    subgraph Fase1["1. Early Game (Iniciação Manual)"]
        A1[Entrada no Spawn / Lobby] --> A2[Interação com [[npc_menu|NPC Menu]] ou /menu]
        A2 --> A3[Acesso à Mina Carvão /mina]
        A3 --> A4[Mineração Manual de Pedra e Carvão]
        A4 --> A5[Eventos: Presentes e Queda de Meteorito]
        A5 --> A6[Venda de Minérios com /sell]
    end

    subgraph Fase2["2. Mid Game (Industrialização)"]
        B1[Atinge R$ 25k ➔ [[tw_ranks|/rankup]] para Neve] --> B2[Compra de Terreno [[tw_terrenos|/terreno claim]] por R$ 50k]
        B2 --> B3[Instalação da 1ª [[tw_maquinas|Máquina de Blocos]]]
        B3 --> B4[Compra de [[tw_spawners|Geradores de Mobs]] com Tokens]
        B4 --> B5[Montagem de [[tw_farms|Fazendas com Silos e Fertilizantes]]]
        B5 --> B6[Abertura e Forja de [[tw_caixas|Caixas Misteriosas]]]
    end

    subgraph Fase3["3. Late Game (Otimização e Conflito)"]
        C1[Ranks Ricos: Rena, Trenó, Estrela, Noel] --> C2[Resgate de [[mundo_mina_pvp|Kits de Batalha]]]
        C2 --> C3[Farm de Recursos Nobres na [[mundo_mina_pvp|Mina PvP]]]
        C3 --> C4[Acúmulo de Almas (Souls) e Certificados de Overclock]
        C4 --> C5[Saturação de Lotes: 25 Spawners de Iron Golem por Plot]
    end

    subgraph Fase4["4. End Game (Domínio e Prestígio)"]
        D1[Rank Noel / MAX atingido: R$ 15 Quadrilhões] --> D2[Ativação de Prestígio [[tw_ranks|/prestigio]]]
        D2 --> D3[Prestígio 1: Grinch ➔ Multiplicador 1.5x]
        D3 --> D4[Prestígio 2: Yeti ➔ Multiplicador 2.0x]
        D4 --> D5[Prestígio 3: Krampus ➔ Multiplicador 3.0x]
        D5 --> D6[Liderança do [[comandos_economia|/baltop]] e Premiações Reais]
    end

    Fase1 --> Fase2
    Fase2 --> Fase3
    Fase3 --> Fase4
```

---
⬅️ [[MOC_Geral|Voltar ao Mapa Geral]] | ➡️ [[combate_pvp|Próxima Nota: Combate PvP]]
