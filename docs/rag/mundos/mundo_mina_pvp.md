---
title: "Mundo Mina PvP e Arena Hostil"
aliases: ["mundo mina pvp", "mina pvp", "pvp arena"]
tags:
  - tw/mundo
  - tw/pvp
  - tw/combate
mundo_nome: "mina_pvp"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Mundos|Mundos]] ➔ **mundo_mina_pvp**

# ⚔️ Mundo Mina PvP e Arena Hostil (`mina_pvp`)

> [!danger] Zona de Alto Risco e Combate Real
> A Mina PvP é a arena de combate e extração do servidor. Itens dropam no chão ao morrer e desconectar em combate resulta em morte instantânea!

---

## ⚙️ Configurações Globais (Multiverse)

- **Alias:** `&c&lTW &f&lMINA PVP`
- **Dificuldade:** `hard`
- **PVP:** `true` (Habilitado)
- **Fome (Hunger):** `true` (Habilitada)
- **Voo (Allow Flight):** `false` (Proibido voar sob qualquer circunstância)
- **Gerador:** `VoidGen`

---

## 🛡️ Regiões WorldGuard

### 1. Zona Segura do Spawn (`spawn`) — Prioridade 10
- **Área:** Cuboide X: -12 a 12, Z: -12 a 12 (Y: -64 a 320).
- `pvp`: `deny` (Impossível bater no spawn).
- `invincible`: `allow` (Sem dano dentro da base).
- `allow-combat-entry`: `deny` *(Jogadores marcados em combate são impedidos de cruzar a barreira de volta!)*

### 2. Arena Externa (`__global__`) — Prioridade 0
- `pvp`: `allow`
- `invincible`: `deny` (Dano totalmente ativo)
- `fall-damage`: `allow` (Dano de queda ativo)
- `block-break` & `block-place`: `deny`

---

## ⏱️ Sistema de Combate (`CombatLog`)

> [!warning] Regras de Combate
> - **Tag de Combate:** Duração de **15 segundos** na ActionBar.
> - **Punição por Desconexão (Combat-Log):** Modo `kill` (Morte com drop total do inventário).
> - **Elytra & Teleporte:** Desativados durante a luta.
> - **Comandos Bloqueados:** `/tpa`, `/spawn`, `/warp`, `/warps`, `/minapvp`, `/pvp`, `/pvpsair`, `/mine`, `/mina`, `/mvtp`.

---

## 🎒 Kits de Batalha Disponíveis (Cooldown: 1 Hora)
- **Kit Básico:** Armadura e Espada de Ferro, Escudo, Arco, 24 Flechas, 24 Bifes, 2 Maçãs Douradas.
- **Kit VIP:** Espada de Diamante Sharp 1, Armadura de Ferro Prot 1, 4 Maçãs Douradas.
- **Kit Prestígio:** Espada de Diamante Sharp 2, Armadura de Diamante Prot 1, 6 Maçãs Douradas.

---
⬅️ [[mundo_terrenos|Nota Anterior: mundo_terrenos]] | 🔼 [[MOC_Mundos|Voltar a Mundos]] | ➡️ [[MOC_Comandos|Ir para Comandos]]
