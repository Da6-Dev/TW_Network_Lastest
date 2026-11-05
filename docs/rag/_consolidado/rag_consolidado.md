# Base de Conhecimento RAG Consolidada: TW Network (RankUP Natal)
> Arquivo compilado e unificado para ingestão direta em modelos LLM, NotebookLM e agentes autônomos.  
> Servidor: Purpur 26.3 | Modo: RankUP Natal | Banco de Dados: PostgreSQL (`tw_network_db`)

---

# PARTE 1: ARQUITETURA DO SISTEMA, ECONOMIA E FLUXOS (Core RankUP)

## 1.1. Arquitetura Geral do Servidor
O TW Network opera sob o motor Purpur 26.3 com arquitetura híbrida de alto desempenho:
- **Persistência Central:** PostgreSQL conectado pelo plugin `tw-core` (Host: `localhost:5432`, Banco: `tw_network_db`).
- **Isolamento de Vácuo:** Todos os mundos utilizam o gerador `VoidGen`, eliminando terreno comum pesado.
- **Proteção Anti-Queda no Vazio:** `VoidSpawnPlus` no Lobby e nas Minas salva o jogador ao cair na camada Y=0 sem dano.
- **Plugins Proprietários:** `tw-core`, `tw-ranks`, `tw-economia`, `tw-minas`, `tw-maquinas`, `tw-spawners`, `tw-farms`, `tw-caixas`, `tw-terrenos`.

## 1.2. Sistema de Ranks e Prestígios (`tw-ranks`)
A progressão é composta por 11 Ranks lineares e 3 Prestígios End Game:

### Tabela de Ranks
- **CARVAO:** Custo: $0.00 (Inicial) | Próximo: NEVE | Mina Carvão, Máquina de Carvão.
- **NEVE:** Custo: $25.000,00 | Próximo: SINO | Mina Neve, Spawner Vaca, Máquina Neve.
- **SINO:** Custo: $800.000,00 | Próximo: BISCOITO | Mina Sino, Spawner Aranha, Máquina Sino.
- **BISCOITO:** Custo: $25.000.000,00 ($2.5E7) | Próximo: DUENDE | Spawner Zumbi, Máquina Biscoito, Correio: 1 Diamante.
- **DUENDE:** Custo: $500.000.000,00 ($5.0E8) | Próximo: RENA | Spawner Blaze, Máquina Duende, Correio: 5 Esmeraldas, Broadcast global.
- **RENA:** Custo: $15.000.000.000,00 ($1.5E10) | Próximo: TRENO | Spawner Iron Golem, Máquina Rena, Broadcast global.
- **TRENO:** Custo: $500.000.000.000,00 ($5.0E11) | Próximo: QUEBRANOZES | Mina Trenó, Broadcast global.
- **QUEBRANOZES:** Custo: $20.000.000.000.000,00 ($2.0E13) | Próximo: ESTRELA | Mina Quebra-Nozes, Broadcast global.
- **ESTRELA:** Custo: $800.000.000.000.000,00 ($8.0E14) | Próximo: NOEL | Mina Estrela, Broadcast global.
- **NOEL:** Custo: $15.000.000.000.000.000,00 ($1.5E16) | Próximo: MAX | Mina Noel, Máquina Noel, Recompensa: $1.000.000,00.
- **MAX:** Status de nível máximo. Elegível para Prestígio.

### Tabela de Prestígios (End Game)
- **GRINCH:** Custo: $50 Quadrilhões ($5.0E16) | Multiplicador de Venda: 1.5x | Caixas: +25% de sorte.
- **YETI:** Custo: $200 Quadrilhões ($2.0E17) | Multiplicador de Venda: 2.0x | Caixas: +50% de sorte.
- **KRAMPUS:** Custo: $800 Quadrilhões ($8.0E17) | Multiplicador de Venda: 3.0x | Caixas: +100% de sorte (2.0x).

## 1.3. Mineração e Eventos Globais (`tw-minas` & `RealMines`)
- **Minas do Servidor:** Cada rank possui sua mina com reset automático em 20% de blocos restantes ou a cada 120s. Há também 3 minas VIP (`vip_festivo`, `vip_nevasca`, `vip_polar`) com minérios nobres (`NETHER_GOLD_ORE`, `NETHER_QUARTZ_ORE`, `ANCIENT_DEBRIS`).
- **Meta Comunitária:** A cada 5.000 blocos minerados globalmente, ativa o Happy Hour por 180 segundos (3 minutos) concedendo 2.0x de multiplicador de venda.
- **Presentes de Natal:** Chance de 0,3% (0.003) por bloco minerado de surgir um presente no chão (vida de 12 segundos).
- **Meteorito:** Chance de 0,005% (0.00005) por bloco. Possui 300 HP. Paga de $50 a $100 por golpe e $5.000 de recompensa final.

## 1.4. Injeção e Drenagem Econômica (`tw-economia`)
- **Injeções:** Mineração ativa (cotações de Pedra a $5.00 até Tijolos do Nether a $22B por bloco), rendimento de máquinas, abates em geradores, venda de safras em silos e caixas.
- **Drenagens:** Custo exponencial de ranks e prestígios, compra de terrenos ($50k no PlotSquared), máquinas ($50k a $25 Quadrilhões), combustível ($5k por 100 unidades), geradores ($100k a $1.5 Trilhão), fertilizantes e forja de caixas.

## 1.5. Máquinas Industriais (`tw-maquinas`)
Combustível custa $5.000 por 100 unidades. Compras acima de $250k exigem confirmação.
- Carvão: Compra $50k | Rende $1.200 a cada 10s.
- Neve: Compra $1.5M | Rende $35.000 a cada 10s.
- Sino: Compra $45M | Rende $1.100.000 a cada 10s.
- Biscoito: Compra $800M | Rende $20.000.000 a cada 8s.
- Duende: Compra $25B | Rende $650.000.000 a cada 8s.
- Rena: Compra $750B | Rende $22.000.000.000 a cada 6s.
- Noel (Beacon): Compra $25 Quadrilhões | Rende $850 Trilhões a cada 5s.

## 1.6. Geradores / Spawners (`tw-spawners`)
Operam nos plots (`terrenos`). Limites: 25 por lote, 100 por jogador, máx 32 entidades empilhadas. Upgrades até Nível 19 em Velocidade, Nível 100 em Loot e Nível 10.000 em Quantidade.
- Porco: Compra $100k | Abate $800 | 15% chance de Token.
- Vaca: Compra $2.5M | Abate $18.000 | 20% chance de Token.
- Aranha: Compra $65M | Abate $450.000 | 25% chance de Token.
- Zumbi: Compra $1.2B | Abate $9.000.000 | 30% chance de Token.
- Blaze: Compra $40B | Abate $320.000.000 | 40% chance de Token.
- Iron Golem: Compra $1.5T | Abate $12.000.000.000 | 50% chance de Token.

## 1.7. Fazendas e Alquimia (`tw-farms`)
Silo com capacidade base de 50.000 unidades. Upgrades com Tokens (Velocidade, Armazenamento, Qualidade, Auto-Venda até nível 25).
- Cultivos: Trigo ($50k / Venda $20), Cenoura/Batata ($500k / Venda $80), Cana ($5M / Venda $350), Cacto/Melancia ($50M / Venda $1.5k-$1.8k), Fungo ($500M / Venda $15k).
- Fertilizantes: Pequeno ($1k), Médio ($9k), Industrial ($80k).
- Alquimia: 250 XP + 8 Esmeraldas = 1.000 Fertilizantes Nível 2. 25 Almas + 4 Diamantes = 5.000 Fertilizantes Nível 3.

## 1.8. Caixas Misteriosas (`tw-caixas`)
- Chances por atividade: Bloco minerado (0,1%), Abate de mob (0,05%), Ciclo de máquina (0,03%), Colheita (0,1%).
- Pity System: Recompensa lendária/rara garantida a cada 50 aberturas.
- Forja: 10 caixas normais = 1 especial; 100 caixas = 1 Caixa Divina (Selo da Fortuna e Orbe de Prestígio Gratuito).

---

# PARTE 2: DICIONÁRIO DE COMANDOS E PERMISSÕES

## 2.1. Comandos Whitelisted (Jogadores - `default`)
- `/mina` ou `/mine`: Abre menu da mina do rank atual.
- `/minaslista`: Lista todas as minas do servidor.
- `/rankup`: Sobe para o próximo rank com saldo suficiente.
- `/rankupmax`: Sobe o máximo de ranks de uma vez.
- `/prestigio`: Abre a interface de evolução de Prestígio.
- `/ranks`: Exibe lista de ranks, custos e benefícios.
- `/rank`: Informações sobre o rank atual.
- `/terreno` ou `/terrenos`: Gerencia plots (compra novo por $50k).
- `/maquinas` e `/maquinas status`: Painel e status de máquinas industriais.
- `/spawners`, `/geradores` e status: Gestão e estatísticas de spawners.
- `/farms` ou `/farm`: Painel de fazendas, silos e fertilizantes.
- `/caixas` e `/key`: Central de caixas e consulta de chaves.
- `/money`, `/saldo`, `/bal`, `/balance`: Consulta de saldo próprio ou de outro jogador.
- `/pay` ou `/pagar <jogador> <quantia>`: Transfere dinheiro para outro jogador.
- `/baltop`, `/magnatas`, `/topmoney`: Exibe o ranking dos jogadores mais ricos.
- `/cheque <quantia>`: Emite cheque físico.
- `/menu` ou `/ajuda`: Abre o menu principal do servidor.
- `/spawn`: Retorna ao ponto de spawn no mundo `world`.
- `/minapvp` ou `/pvp`: Teleporta para o spawn da mina PvP.
- `/pvpsair`: Sai com segurança da mina PvP (se fora de combate).
- `/correio`: Abre caixa postal virtual do MailboxGUI.
- `/kit` e `/kits`: Consulta e resgate de kits disponíveis.
- `/msg <player> <msg>`, `/reply <msg>`, `/ignore <player>`: Mensagens privadas.
- `/discord`: Exibe o link da comunidade oficial.
- `/afk`, `/rules`, `/ping`, `/playtime`, `/list`, `/trash`: Comandos utilitários.

## 2.2. Comandos VIP, Staff e Administrativos
- `/vc [msg]`: Canal VIP (Exclusivo VIP Festivo, Nevasca, Polar).
- `/fly`: Modo de voo em áreas permitidas (VIPs e Staff).
- `/repair [hand/all]`, `/hat`, `/feed`: Benefícios de utilidade VIP/Staff.
- `/sc [msg]`: Canal de chat interno da moderação (Staff).
- `/ac [msg]`: Canal de chat exclusivo da administração (Admin).
- `/invsee`, `/endersee`, `/vanish`, `/freeze`, `/god`: Ferramentas de fiscalização e moderação.
- `/kick`, `/mute`, `/unmute`: Punições aplicadas pela moderação.
- `/ban`, `/unban`, `/ban-ip`: Punições restritas à administração.
- `/lp`: Gerenciador de permissões do LuckPerms (Admin/Dono).
- `/rg`: Gerenciador de regiões do WorldGuard (Admin).
- `/realmines`: Controle de regeneração e minas (Admin).
- `/fn`: Controle de criação e coordenadas de NPCs do FancyNpcs (Admin).

---

# PARTE 3: MAPEAMENTO DE MUNDOS E REGRAS DE AMBIENTE

## 3.1. Mundo `world` (Lobby Principal)
- **Alias:** `&c&lTW &f&lLOBBY` | **Gerador:** `VoidGen` | **Dificuldade:** `hard`.
- **Flags Multiverse:** PVP off, Fome off, Clima off, Voo on, Mobs off.
- **WorldGuard (`__global__`):** `pvp: deny`, `invincible: allow`, `fall-damage: deny`, `block-break: deny`, `block-place: deny`, `item-drop: deny`, `item-pickup: deny`.
- **Resgate VoidSpawnPlus:** Queda no Y=0 teletransporta de volta ao spawn com som de Enderman.

## 3.2. Mundo `minas` (Complexo de Mineração)
- **Gerador:** `VoidGen` | **Dificuldade:** `peaceful`.
- **Flags Multiverse:** PVP off, Fome off, Clima off, Voo on, Mobs off.
- **WorldGuard (`__global__`):** `pvp: deny`, `invincible: allow`, `fall-damage: deny`, `block-break: deny` (com liberação interna para blocos gerenciados pelo RealMines), `item-drop: allow`, `item-pickup: allow`.
- **Resgate VoidSpawnPlus:** Queda no Y=0 teletransporta ao spawn das minas.

## 3.3. Mundo `terrenos` (Lotes Industriais)
- **Gerador:** `VoidGen` + `PlotSquared 7.6.x` | **Dificuldade:** `peaceful`.
- **Dimensões do Plot:** 42x42 blocos, altura Y=62, piso em grama, estradas em bloco de quartzo com largura 7. Custo de compra: R$ 50.000,00.
- **Flags Multiverse:** PVP off, Fome off, Clima off, Voo on (para donos).
- **Regras:** Limite de 25 spawners por lote; operação contínua de máquinas e colheita de fazendas.

## 3.4. Mundo `mina_pvp` (Arena de Combate e Extração)
- **Alias:** `&c&lTW &f&lMINA PVP` | **Gerador:** `VoidGen` | **Dificuldade:** `hard`.
- **Flags Multiverse:** PVP on, Fome on, Clima off, Voo off (proibido voar), Mobs off.
- **WorldGuard:**
  - `spawn` (Cuboide X: -12 a 12, Z: -12 a 12): `pvp: deny`, `invincible: allow`, `allow-combat-entry: deny` (jogadores marcados em combate não conseguem entrar).
  - `__global__` (Arena externa): `pvp: allow`, `invincible: deny`, `fall-damage: allow`, `block-break: deny`.
- **Regras do CombatLog:**
  - Tag de combate dura **15 segundos** na ActionBar.
  - Desconexão em combate (`combat-log`) = Morte instantânea (`kill`) com perda total de itens.
  - Elytra e teleportes desativados durante a luta.
  - Comandos bloqueados: `/tpa`, `/spawn`, `/warp`, `/warps`, `/minapvp`, `/pvp`, `/pvpsair`, `/mine`, `/mina`, `/mvtp`.
- **Kits PvP:** Kit Básico (Ferro), Kit VIP (Diamante Sharp 1) e Kit Prestígio (Diamante Sharp 2), com cooldown de 1 hora.

---

# PARTE 4: ENTIDADES, NPCS E INTERAÇÕES

## 4.1. NPC Central de Menu (`FancyNpcs`)
- **Nome:** `menu` | **UUID:** `2ef7c583-bf01-4efc-9276-573c035f6af4`.
- **Localização:** Mundo `world`, **X:** 306.40, **Y:** 87.00, **Z:** 248.46 (Yaw: 0.14, Pitch: 2.10).
- **Visual:** Skin `nielspp`, Escala 1.5x, acompanha o jogador com o olhar (`turnToPlayer: true`).
- **Ação:** Clique com o Botão Direito executa `player_command: menu`, abrindo a GUI principal do DeluxeMenus.

## 4.2. Hologramas Vinculados (`FancyHolograms`)
- **`npc-menu`:** Localizado em X: 306.47, Y: 90.36, Z: 248.79 (3 blocos acima do NPC menu), indicando em cores de destaque: "MENU PRINCIPAL | Minas • Kits • Mercado | CLIQUE PARA ABRIR (Botão Direito)".
- **`boas-vindas`:** Localizado em X: 311.48, Y: 87.62, Z: 252.67 em frente ao spawn, saudando o jogador e exibindo seu Rank (`%luckperms_prefix%`) e Saldo (`%vault_eco_balance_formatted%`) com atualização a cada 1 segundo.

## 4.3. Menus Gráficos (`DeluxeMenus`)
- **Menu Principal (`menu.yml`):** 45 slots. Cabeça com Perfil (Slot 4), Ir Minerar `/mina` (Slot 20), Kits PvP `/kits` (Slot 22), Mercado `/shop` (Slot 24), Cosméticos `/cosmetics` (Slot 31), Fechar (Slot 40).
- **Central de Minas (`minas.yml`):** 54 slots. Exibe o status de cada mina do servidor de acordo com a permissão do jogador.

---

# PARTE 5: DIRETRIZES DO AGENTE DE IA (`agent.md`)

## 5.1. Perfil e Postura
O assistente atua como Especialista Técnico do TW Network RankUP Natal. Deve ser prestativo, preciso, claro e manter total conformidade com a documentação oficial.

## 5.2. Regras de Resposta
1. Proibição estrita de alucinações (cite somente mecânicas reais presentes nas partes 1 a 4).
2. Fornecer comandos exatos formatados com `/`.
3. Oferecer dicas de jogabilidade ou avisos de segurança pertinentes.

## 5.3. Protocolo de Sincronização e Atualização
Se modificações em arquivos como `config.yml`, `ranks.yml` ou `regions.yml` forem detectadas no repositório, o agente deve relatar a discrepância e propor a atualização correspondente nesta base RAG.
