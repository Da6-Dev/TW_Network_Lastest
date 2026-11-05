---
title: "Núcleo e Banco de Dados (tw-core)"
aliases: ["tw-core", "banco de dados", "postgresql", "scoreboard"]
tags:
  - tw/sistema
  - tw/core
  - tw/banco-de-dados
plugin_fonte: "tw-core"
arquivo_config: "plugins/tw-core/config.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_core**

# 🗄️ Núcleo e Banco de Dados (`tw-core`)

> [!info] Visão de Infraestrutura
> O `tw-core` é o módulo central do servidor responsável por conectar os subsistemas à camada de persistência em banco relacional **PostgreSQL**, além de sincronizar scoreboards e a ordem global de progressão.

---

## 🐘 Conexão PostgreSQL

- **Host:** `localhost:5432`
- **Banco:** `tw_network_db`
- **Variáveis de Ambiente Recomendadas (Produção):**
  - `TW_DB_USERNAME`: Usuário do banco (padrão local: `postgres`).
  - `TW_DB_PASSWORD`: Senha do banco (padrão local: `1234`).

---

## 📊 Scoreboard e Placeholders

- **Frequência de Atualização:** 20 ticks (1 segundo).
- **Mapeamento de Mundos Principais:**
  - `mines`: `minas`
  - `plots`: `terrenos` (com alias `plots`)
- **Gestão Central de Ranks e Prestígios:**
  - Define a ordem canônica dos 11 Ranks e 3 Prestígios:
    `CARVAO ➔ NEVE ➔ SINO ➔ BISCOITO ➔ DUENDE ➔ RENA ➔ TRENO ➔ QUEBRANOZES ➔ ESTRELA ➔ NOEL ➔ MAX`
  - Define multiplicadores de Prestígio: Grinch (1.5x), Yeti (2.0x), Krampus (3.0x).

---
⬅️ [[tw_minas|Nota Anterior: tw_minas]] | 🔼 [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[MOC_Economia|Ir para Economia]]
