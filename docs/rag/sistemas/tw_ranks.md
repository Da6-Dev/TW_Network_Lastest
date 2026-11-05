---
title: "Sistema de Ranks e Prestígios"
aliases: ["tw-ranks", "ranks", "prestigio", "prestígios"]
tags:
  - tw/sistema
  - tw/ranks
  - tw/progressao
plugin_fonte: "tw-ranks"
arquivo_config: "plugins/tw-ranks/ranks.yml"
status: ativo
ultima_atualizacao: "2026-11-05"
---

📍 [[MOC_Geral|Início]] ➔ [[MOC_Sistemas|Sistemas]] ➔ **tw_ranks**

# 🎖️ Sistema de Ranks e Prestígios (`tw-ranks`)

> [!abstract] Resumo Operacional
> O `tw-ranks` controla toda a progressão do jogador através de **11 Ranks Natalinos** e **3 Prestígios End Game**. Além de desbloquear novas minas e comandos, alguns ranks premiam o jogador diretamente via caixa de correio virtual ([[comandos_jogadores|/correio]]).

---

## 📈 Tabela de Ranks (Progressão Linear)

| Rank | Prefixo / Tag | Próximo | Custo de Evolução ($) | Broadcast | Recompensas Especiais |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CARVAO** | `&8[Carvão]` | NEVE | R$ 0,00 *(Inicial)* | ❌ Não | Acesso à Mina Carvão, Máquina de Carvão |
| **NEVE** | `&f[Neve]` | SINO | R$ 25.000,00 | ❌ Não | Mina Neve, Spawner de Vaca, Máquina Neve |
| **SINO** | `&e[Sino]` | BISCOITO | R$ 800.000,00 | ❌ Não | Mina Sino, Spawner de Aranha, Máquina Sino |
| **BISCOITO** | `&6[Biscoito]` | DUENDE | R$ 25.000.000,00 ($2.5E7) | ❌ Não | Mina Biscoito, Spawner Zombie, Máquina Biscoito, **Correio:** 1x Diamante |
| **DUENDE** | `&a[Duende]` | RENA | R$ 500.000.000,00 ($5.0E8) | ✅ Sim | Mina Duende, Spawner Blaze, Máquina Duende, **Correio:** 5x Esmeraldas |
| **RENA** | `&c[Rena]` | TRENO | R$ 15.000.000.000,00 ($1.5E10) | ✅ Sim | Mina Rena, Spawner Iron Golem, Máquina Rena |
| **TRENO** | `&4[Trenó]` | QUEBRANOZES | R$ 500.000.000.000,00 ($5.0E11) | ✅ Sim | Mina Trenó |
| **QUEBRANOZES**| `&5[Quebra-Nozes]`| ESTRELA | R$ 20.000.000.000.000,00 ($2.0E13)| ✅ Sim | Mina Quebra-Nozes |
| **ESTRELA** | `&e&l[Estrela]` | NOEL | R$ 800.000.000.000.000,00 ($8.0E14)| ✅ Sim | Mina Estrela |
| **NOEL** | `&c&l[Noel]` | MAX | R$ 15.000.000.000.000.000,00 ($1.5E16)| ✅ Sim | Mina Noel, Máquina Noel, Farm Fungus, **Recompensa:** $1.000.000,00 |
| **MAX** | `&6&l[MAX]` | - | Nível Máximo | - | Elegível para entrar no ciclo de Prestígio |

---

## 🏆 Tabela de Prestígios (End Game)

Após atingir o rank **NOEL / MAX**, o jogador pode reiniciar seu progresso de ranks para adquirir Prestígios:

| Prestígio | Prefixo / Tag | Custo de Aquisição ($) | Multiplicador de Venda | Bônus em Caixas |
| :--- | :--- | :--- | :--- | :--- |
| **GRINCH** | `&2&l[Grinch]` | R$ 50.000.000.000.000.000,00 ($5.0E16) | **1.5x** | +25% de sorte em caixas |
| **YETI** | `&b&l[Yeti]` | R$ 200.000.000.000.000.000,00 ($2.0E17) | **2.0x** | +50% de sorte em caixas |
| **KRAMPUS** | `&4&l[Krampus]` | R$ 800.000.000.000.000.000,00 ($8.0E17) | **3.0x** | +100% de sorte (2.0x) em caixas |

---

> [!tip] Dica para Jogadores
> Use `/rankupmax` para subir múltiplos ranks de uma única vez sem precisar digitar `/rankup` repetidamente!

> [!info] Comandos Vinculados
> - `/rankup`: Evolui 1 rank.
> - `/rankupmax`: Consome todo o saldo disponível para subir o máximo de ranks possíveis.
> - `/prestigio`: Abre o menu de evolução de Prestígio.
> - `/ranks`: Exibe a lista completa de ranks no chat.

---
⬅️ [[MOC_Sistemas|Voltar a Sistemas]] | ➡️ [[tw_maquinas|Próxima Nota: tw_maquinas]]
