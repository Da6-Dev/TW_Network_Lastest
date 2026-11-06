# Design System & Guia de Estilo Visual (UI) — TW Network

**Versão:** 1.0.0  
**Data:** 05/11/2026  
**Status:** Definitivo / Aprovado  
**Ambiente:** Purpur 26.3 | Minecraft 1.20+ / 1.21 | DeluxeMenus & `tw-*` Native Menus  

---

## 1. Princípios Fundamentais de Design

O Design System da rede **TW Network** tem como meta unificar visualmente e funcionalmente todas as interfaces gráficas (GUIs) do servidor, eliminando a fragmentação entre plugins de terceiros (como `DeluxeMenus` e `EssentialsC`) e módulos proprietários da rede (`tw-*`).

### Pilares:
1. **Consistência Estrutural:** Todo menu segue um dos dois tamanhos canônicos: **54 slots** (menus principais, hubs, catálogos) ou **27 slots** (submenus, painéis de ação e confirmações). Tamanhos arbitrários (ex: 36 ou 45 slots) são estritamente depreciados.
2. **Previsibilidade de Navegação:** Botões universais de navegação sempre ocupam as mesmas coordenadas físicas de inventário:
   - **Retorno:** Slot **45** (em 54 slots) ou Slot **18** (em 27 slots).
   - **Fechamento:** Slot **49** (em 54 slots) ou Slot **22** (em 27 slots).
3. **Hierarquia de Informação em 3 Seções:** Nenhuma lore é livre ou desordenada. Cada item comunica de forma limpa: *o que faz* (Topo), *qual o status do jogador* (Meio) e *como interagir* (Rodapé).
4. **Identidade Cromática Coesa:** Adoção de uma paleta fixa baseada em tons frios com destaque ciano/azul claro (`&#7FB4F4`), acentos dourados (`&#F7C844` / `&e`), textos descritivos em cinza claro (`&7`), molduras em grafite (`&8`) e indicadores binários de sucesso (`&a`) e restrição (`&c`).

---

## 2. Padrões de Dimensionamento e Organização de Slots

### 2.1. Menus de 54 Slots (6 Linhas / 9x6)
Utilizado para: **Menu Principal (Hub Central)**, **Catálogos Extensos** (ex: Minas, Ranks, Máquinas, Spawners, Farms, Caixas, Loja).

#### Mapa de Slots (Matriz 9x6):
```text
Linha 1 [00 a 08]: [ B ][ B ][ B ][ B ][ P ][ B ][ B ][ B ][ B ]
Linha 2 [09 a 17]: [ B ][ C ][ C ][ C ][ C ][ C ][ C ][ C ][ B ]
Linha 3 [18 a 26]: [ B ][ C ][ C ][ C ][ C ][ C ][ C ][ C ][ B ]
Linha 4 [27 a 35]: [ B ][ C ][ C ][ C ][ C ][ C ][ C ][ C ][ B ]
Linha 5 [36 a 44]: [ D ][ D ][ D ][ D ][ D ][ D ][ D ][ D ][ D ]
Linha 6 [45 a 53]: [ R ][ B ][ B ][ I ][ B ][ X ][ B ][ B ][ S ]
```

- **Legenda:**
  - `[ B ]` Moldura Externa (`BLACK_STAINED_GLASS_PANE` ou `GRAY_STAINED_GLASS_PANE`).
  - `[ P ]` Slot 4: Cabeçalho / Perfil do Jogador (`head-%player_name%`).
  - `[ C ]` Slots de Conteúdo Ativo (linhas 2 a 4).
  - `[ D ]` Linha 5 (slots 36 a 44): Divisória de Contraste (`BLACK_STAINED_GLASS_PANE` ou painéis decorativos com nome vazio `' '`).
  - `[ R ]` **Slot 45: Botão Universal de Retorno** (`ARROW`).
  - `[ I ]` Slot 48: Informações Gerais / Ranking (`BOOK` ou `GOLD_BLOCK`).
  - `[ X ]` **Slot 49: Botão Universal de Fechamento** (`BARRIER`).
  - `[ S ]` Slot 53: Atalho de Saída / Spawn (`ENDER_PEARL` ou `COMPASS`).

---

### 2.2. Menus de 27 Slots (3 Linhas / 9x3)
Utilizado para: **Submenus de Ação Rápida**, **Painéis de Configuração/Gerenciamento de Bloco** (ex: Agência de Terrenos, Painel de Máquina, Confirmação de Transação).

#### Mapa de Slots (Matriz 9x3):
```text
Linha 1 [00 a 08]: [ B ][ B ][ B ][ B ][ T ][ B ][ B ][ B ][ B ]
Linha 2 [09 a 17]: [ B ][ C ][ C ][ C ][ C ][ C ][ C ][ C ][ B ]
Linha 3 [18 a 26]: [ R ][ B ][ B ][ B ][ X ][ B ][ B ][ B ][ H ]
```

- **Legenda:**
  - `[ B ]` Moldura (`GRAY_STAINED_GLASS_PANE` ou `BLACK_STAINED_GLASS_PANE`).
  - `[ T ]` Slot 4: Ícone Temático Centralizador ou Perfil Resumido.
  - `[ C ]` Slots de Ação e Interação (slots 10 a 16).
  - `[ R ]` **Slot 18: Botão Universal de Retorno** (`ARROW`).
  - `[ X ]` **Slot 22: Botão Universal de Fechamento** (`BARRIER`).
  - `[ H ]` Slot 26: Atalho ao Hub Central (`NETHER_STAR`).

---

## 3. Paleta Cromática e Tipografia

Todas as interfaces devem aderir rigorosamente aos seguintes códigos de cor e semântica:

| Cor / Tom | Código Minecraft | Código Hexadecimal | Propósito e Uso Recomendado |
|---|---|---|---|
| **Ciano TW Principal** | `&b` / `&3` | `&#7FB4F4` ou `&x&7&f&b&4&f&4` | Títulos principais, destaques de sistemas nobres, cabeçalhos de itens. |
| **Dourado / Valor** | `&e` / `&6` | `&#F7C844` ou `&x&f&7&c&8&4&4` | Valores monetários, preços, multiplicadores, taxas, saldo de moedas. |
| **Texto Padrão** | `&7` | `#AAAAAA` | Descrições funcionais de itens, lore padrão, contexto histórico. |
| **Destaque Claro** | `&f` | `#FFFFFF` | Nomes de jogadores, quantidades numéricas neutras, dados brutos. |
| **Moldura / Divisória** | `&8` | `#555555` | Prefixos de títulos (`&8➔`), linhas separadoras (`&8───────────────`). |
| **Sucesso / Desbloqueado** | `&a` / `&2` | `#55FF55` | Status liberado, comandos de ação positiva (`&a▶ Clique para...`), saldo positivo. |
| **Alerta / Bloqueado** | `&c` / `&4` | `#FF5555` | Status bloqueado, custo faltante, avisos de perigo, botão de fechar (`&c▶ Clique para fechar`). |
| **Especial / Almas** | `&d` / `&5` | `#FF55FF` | Moeda de Almas (`%tw_souls%`), itens místicos, prestígios e forjas. |

### Regra de Compatibilidade Hexadecimal
Em plugins compatíveis com RGB do Spigot/Paper (como DeluxeMenus 1.14+ e Purpur 26.3), utilize preferencialmente a sintaxe `&#RRGGBB` ou `&x&r&r&g&g&b&b`. Para compatibilidade universal de fallback, preserve as cores secundárias nativas (`&b`, `&e`, `&7`, `&a`, `&c`).

---

## 4. Padrão Unificado de Títulos de GUI

Todos os menus devem seguir a estrutura morfológica:
```text
&8➔ <COR_TEMA>&l<NOME_DO_MENU>
```

### Exemplos Válidos:
- **Menu Principal:** `&8➔ &#7FB4F4&lMENU PRINCIPAL` ou `&8➔ &6&lMENU PRINCIPAL`
- **Minas:** `&8➔ &b&lMINAS` ou `&8➔ &#7FB4F4&lCENTRAL DE MINAS`
- **Ranks:** `&8➔ &#7FB4F4&lTRILHA DE RANKS`
- **Terrenos:** `&8➔ &#7FB4F4&lAGÊNCIA DE TERRENOS`
- **Máquinas:** `&8➔ &#7FB4F4&lFÁBRICA DE MÁQUINAS`
- **Spawners:** `&8➔ &#7FB4F4&lMERCADO DE SPAWNERS`
- **Farms:** `&8➔ &#7FB4F4&lCENTRAL DE AGRICULTURA`
- **Caixas:** `&8➔ &#7FB4F4&lCHAVES & CAIXAS VIRTUAIS`
- **Oficina:** `&8➔ &#7FB4F4&lOFICINA & MISSÕES`
- **Confirmação:** `&8➔ &c&lCONFIRMAR AÇÃO`

---

## 5. Padrão Estruturado de Lore em 3 Seções

Todo item interativo em um menu deve conter exatamente **3 seções lógicas**, separadas por linhas em branco (`''`):

```text
┌────────────────────────────────────────────────────────┐
│ [SEÇÃO 1: TOPO] Função e descrição resumida do recurso │
├────────────────────────────────────────────────────────┤
│ [SEÇÃO 2: MEIO] Estado dinâmico do jogador / variáveis  │
├────────────────────────────────────────────────────────┤
│ [SEÇÃO 3: RODAPÉ] Instrução clara do clique e ação     │
└────────────────────────────────────────────────────────┘
```

### 5.1. Especificação de Cada Seção

1. **Seção 1: Topo (Descrição Funcional)**
   - Cor padrão: `&7`.
   - Limite recomendado: 1 a 3 linhas concisas.
   - Linguagem direta em Português Brasileiro formal/amigável ("Você", "Seu", "Acesse", "Evolua").
   
2. **Seção 2: Meio (Status Dinâmico do Jogador)**
   - Cor das chaves: `&7`.
   - Cor dos valores: `&a` (liberado/sucesso), `&c` (bloqueado/falta), `&e` (quantias/valores), `&f` (dados neutros).
   - Utilização de Placeholders da rede (`%vault_eco_balance_formatted%`, `%tw_tokens%`, `%tw_souls%`, `%tw_rank%`, etc.).
   
3. **Seção 3: Rodapé (Instrução Clara de Ação)**
   - Sempre antecedido pelo símbolo `▶` (ou `✕` para cancelamento/bloqueio).
   - Ação de abertura/teleporte: `&a▶ Clique para acessar` / `&a▶ Clique para teleportar`
   - Ação de compra/evolução: `&a▶ Clique para adquirir` / `&a▶ Clique para evoluir`
   - Ação de retorno: `&e▶ Clique para voltar`
   - Ação de fechamento: `&c▶ Clique para fechar`
   - Ação bloqueada: `&c✕ Bloqueado - Requer <requisito>`

### 5.2. Exemplos de Implementação YAML

#### Exemplo A: Item do Hub Principal (Minas)
```yaml
display_name: '&#7FB4F4&lMINAS &8• &fMineração'
lore:
  - '&7Acesse a central de mineração do servidor'
  - '&7e teleporte-se para as áreas do seu rank.'
  - ''
  - '&7Seu Rank: &a%tw_rank%'
  - '&7Status: &aDisponível'
  - ''
  - '&a▶ Clique para acessar as minas'
```

#### Exemplo B: Mina Liberada (Dual State - Prioridade 1)
```yaml
display_name: '&#7FB4F4&lMINA CARVÃO &a✔'
priority: 1
view_requirement:
  requirements:
    permission:
      type: has permission
      permission: realmines.carvao.break
lore:
  - '&7Mina inicial de recursos e minérios.'
  - '&7Colete carvão, pedra e tokens básicos.'
  - ''
  - '&7Requisito: &fRank Carvão'
  - '&7Status: &aDesbloqueada'
  - ''
  - '&a▶ Clique para teleportar'
```

#### Exemplo C: Mina Bloqueada (Dual State - Prioridade 2)
```yaml
display_name: '&c&lMINA NOEL &c✖'
priority: 2
lore:
  - '&7Mina lendária do ápice da progressão.'
  - '&7Minérios divinos com alto rendimento.'
  - ''
  - '&7Requisito: &cRank Noel'
  - '&7Status: &cBloqueada'
  - ''
  - '&c✕ Bloqueado - Requer rank Noel (/rankup)'
```

#### Exemplo D: Botão Universal de Retorno (Slot 45)
```yaml
display_name: '&e➔ &lVoltar ao Menu'
material: ARROW
slot: 45
lore:
  - '&7Retorne à central principal de navegação'
  - '&7para escolher outro subsistema.'
  - ''
  - '&7Destino: &eMenu Principal'
  - ''
  - '&e▶ Clique para voltar'
```

#### Exemplo E: Botão Universal de Fechamento (Slot 49)
```yaml
display_name: '&c➔ &lFechar'
material: BARRIER
slot: 49
lore:
  - '&7Encerre a visualização desta interface'
  - '&7e retorne à sua jogatina.'
  - ''
  - '&7Ação: &cFechar GUI'
  - ''
  - '&c▶ Clique para fechar'
```

---

## 6. Materiais Canônicos de Decoração e Molduras

Para assegurar consistência em todos os plugins (`DeluxeMenus` e classes `TWMenuFrame` do Java):

1. **Bordas Externas de Menus de 54 Slots:**
   - Material: `BLACK_STAINED_GLASS_PANE` ou `GRAY_STAINED_GLASS_PANE`.
   - Nome: `' '` (espaço vazio).
   - Sem lore.

2. **Divisória da Linha 5 (Slots 36 a 44 em 54 Slots):**
   - Material: `BLACK_STAINED_GLASS_PANE` (ou `CYAN_STAINED_GLASS_PANE` em menus de prestígio/evento).
   - Nome: `' '`.

3. **Cantos Estilizados (Opcional para Menus Especiais):**
   - Material: `LIGHT_BLUE_STAINED_GLASS_PANE` nos 4 cantos (slots 0, 8, 45, 53 em menus de confirmação ou displays nobres).

---

## 7. Diretrizes de Localização e Linguagem

1. **Língua Oficial:** Português do Brasil (pt-BR).
2. **Pronomes e Conjugações:**
   - Proibido uso de Português Europeu (*"Não tens"*, *"Clica aqui"*, *"na tua conta"*).
   - Correto: *"Você não possui"*, *"Clique aqui"*, *"em sua conta"*.
3. **Formatação Monetária:**
   - Padrão abreviado para valores grandes: `$1.5k`, `$25.0M`, `$500.0B`, `$20.0T`, `$15.0Q`.
   - Sempre utilize o placeholder formatado `%vault_eco_balance_formatted%` ou `%tw_money_formatted%`.

---
*Fim da especificação do Design System.*
