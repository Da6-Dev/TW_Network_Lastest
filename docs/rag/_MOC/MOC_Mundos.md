---
title: "MOC — Mundos e Topologia"
aliases: ["MOC Mundos", "Mundos"]
tags:
  - tw/moc
  - tw/mundos
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ **MOC Mundos**

# 🗺️ Central de Mundos e Topologia de Servidor

> [!info] Visão de Infraestrutura
> O servidor opera exclusivamente com ilhas no vazio através do gerador `VoidGen`, garantindo 20.0 TPS e controle fino de física e proteção por região.

---

## 🌍 Mundos Ativos

| Mundo | Alias / Propósito | Dificuldade | PVP | Fome | Gerador | Nota Atômica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `world` | `&c&lTW &f&lLOBBY` | Hard | ❌ Off | ❌ Off | VoidGen | [[mundo_lobby]] |
| `minas` | `MINAS` (Progressivo) | Peaceful | ❌ Off | ❌ Off | VoidGen | [[mundo_minas]] |
| `terrenos` | `TERRENOS` (Plots) | Peaceful | ❌ Off | ❌ Off | VoidGen + PlotSquared | [[mundo_terrenos]] |
| `mina_pvp` | `&c&lTW &f&lMINA PVP` | Hard | ✅ On | ✅ On | VoidGen | [[mundo_mina_pvp]] |

---

## 🛡️ Camadas de Segurança e Proteção

- **Proteção Anti-Void:** [[mundo_lobby|VoidSpawnPlus]] no Lobby e nas Minas salva o jogador ao cair em Y=0.
- **Proteção de Propriedade:** [[mundo_terrenos|PlotSquared]] com plots 42x42 isolados.
- **Controle de Combate:** [[mundo_mina_pvp|CombatLog]] pune desconexões em combate com morte instantânea.

---
⬅️ [[MOC_Geral|Voltar ao Mapa Geral]] | ➡️ [[mundo_lobby|Ver Mundo Lobby]]
