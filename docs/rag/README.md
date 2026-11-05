# 💎 TW Network Vault — Memória RAG Atômica (Obsidian Ready)
**Servidor:** TW Network (RankUP Natal - Purpur 26.3)  
**Arquitetura:** Zettelkasten / Notas Atômicas Interconectadas com MOCs  
**Padrão de Sintaxe:** Wikilinks (`[[...]]`), Callouts e Frontmatter YAML

---

## 🌟 Como Visualizar no Obsidian

Para abrir esta documentação como um Vault completo e interativo:
1. Abra o **Obsidian**.
2. Clique em **"Open folder as vault"** (Abrir pasta como cofre).
3. Selecione a pasta: `TW_Network_Lastest/docs/rag`.
4. Abra o arquivo `_MOC/MOC_Geral.md` ou pressione `Ctrl + G` para abrir o **Graph View** (Grafo Interconectado).

```
                      ┌───────────────┐
                      │   MOC_Geral   │
                      └───────┬───────┘
          ┌───────────┬───────┴───────┬───────────┐
          ▼           ▼               ▼           ▼
    MOC_Sistemas  MOC_Economia    MOC_Mundos  MOC_Comandos
          │           │               │           │
          ▼           ▼               ▼           ▼
     [tw_ranks] [tabela_precos]  [mundo_lobby] [comandos_jogadores]
     [tw_maquinas] [fluxo...]    [mundo_minas] [comandos_staff]
     [tw_spawners]               [mundo_pvp]
```

---

## 📂 Mapa de Pastas do Vault

- **`_MOC/`**: Centrais de conteúdo e hubs do Grafo ([[MOC_Geral]], [[MOC_Sistemas]], [[MOC_Economia]], [[MOC_Mundos]], [[MOC_Comandos]], [[MOC_Interacoes]]).
- **`sistemas/`**: Notas atômicas de cada plugin proprietário (`tw-ranks`, `tw-maquinas`, `tw-spawners`, `tw-farms`, `tw-caixas`, `tw-terrenos`, `tw-minas`, `tw-core`).
- **`economia/`**: Cotações detalhadas de blocos, análise de drenagens e boosters.
- **`mundos/`**: Flags do WorldGuard, proteção no vácuo e topologia por mundo.
- **`comandos/`**: Dicionário de comandos segmentado por público (jogadores, economia, staff e admin).
- **`interacoes/`**: Coordenadas e scripts de NPCs, hologramas dinâmicos e menus DeluxeMenus.
- **`game_loop/`**: Guias estratégicos de progressão e combate na Mina PvP.
- **`agent.md`**: Diretrizes de IA e o protocolo obrigatório de **Document-as-you-Code**.
- **`_consolidado/`**: Arquivo consolidado único para importação em ferramentas externas (Google AI Studio, NotebookLM).

---

> [!important] Regra para Agentes de IA
> Todo agente deve consultar notas específicas de 30-100 linhas em vez de arquivos monolíticos, e deve obrigatoriamente atualizar a nota atômica caso modifique qualquer arquivo `.yml` do servidor!
