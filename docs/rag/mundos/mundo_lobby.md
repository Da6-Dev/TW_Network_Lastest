---
title: "Mundo Lobby e Spawn Principal"
aliases: ["mundo lobby", "lobby", "spawn", "world"]
tags:
  - tw/mundo
  - tw/lobby
  - tw/spawn
mundo_nome: "world"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Mundos|Mundos]] ➔ **mundo_lobby**

# 🏛️ Mundo Lobby e Spawn Principal (`world`)

> [!info] Visão Geral
> Ponto de entrada, recepção e convivência social do TW Network. Área 100% protegida e imune a danos.

---

## ⚙️ Configurações do Ambiente (Multiverse)

- **Alias:** `&c&lTW &f&lLOBBY`
- **Gerador:** `VoidGen` (Ilha suspensa no vazio)
- **Dificuldade:** `hard`
- **PVP:** `false` (Desativado)
- **Fome (Hunger):** `false` (Desativada)
- **Voo (Allow Flight):** `true` (Habilitado para VIPs e Staff)
- **Clima:** `false` (Sempre limpo)
- **Spawn de Monstros:** `false`

---

## 🛡️ Flags da Região `__global__` (WorldGuard)

```yaml
flags:
  pvp: deny
  invincible: allow
  fall-damage: deny
  block-break: deny
  block-place: deny
  item-drop: deny
  item-pickup: deny
  mob-spawning: deny
  fire-spread: deny
  other-explosion: deny
  tnt: deny
  interact: allow
  use: allow
```

---

## 🕳️ Segurança de Queda (VoidSpawnPlus)

> [!tip] Resgate Automático
> Qualquer jogador que pular ou cair no vazio além da camada **Y = 0** é resgatado instantaneamente de volta ao Spawn, com o som `ENTITY_ENDERMAN_TELEPORT` e sem sofrer qualquer dano.

---

## 📍 Entidades e Pontos de Interesse
- [[npc_menu|NPC Menu Principal]]: Localizado em X: 306.40, Y: 87.00, Z: 248.46.
- [[hologramas|Hologramas]]: Holograma de Boas-Vindas e Holograma flutuante do Menu.

---
⬅️ [[MOC_Mundos|Voltar a Mundos]] | ➡️ [[mundo_minas|Próxima Nota: mundo_minas]]
