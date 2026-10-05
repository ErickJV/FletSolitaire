# 🎴 Documento de Requisitos do Sistema: Paciência Pixelado (Estilo Balatro)

**Nome do Projeto:** Pixel Solitaire

**Stack Tecnológica:** Python 3.9+, Flet Framework, Pillow (Processamento de Assets)

**Plataformas Alvo:** Desktop (Windows, macOS, Linux) e Web (Exportação via Flet Web)

---

## 1. Visão Geral e Objetivos do Projeto

### 1.1 Objetivo

Desenvolver um jogo de paciência (*Solitaire*) para um jogador em Python utilizando o framework **Flet**. A jogabilidade principal segue as regras do Klondike Solitaire clássico, enquanto o design visual, efeitos sonoros e feedback de interface (UI) inspiram-se na estética retro em pixel art e no polimento visual (*"juice"*) do jogo *Balatro*.

### 1.2 Diferenciais Chave

* **Tema em Pixel Art:** Cartas, mesas, fontes e componentes de UI retro personalizados em estilo 8-bit/16-bit.
* **Polimento Visual ("Juice"):** Arraste suave de cartas, sombras dinâmicas, inclinação da tela, efeitos de partículas na pontuação e efeitos sonoros imersivos.
* **Arquitetura Baseada em Flet:** Construído usando extensões nativas do Flet (`ft.GestureDetector`, `ft.Stack`, `ft.Container`) para renderização limpa e multiplataforma.

---

## 2. Requisitos Visuais e Estéticos (Estilo Balatro)

| Elemento | Descrição do Requisito |
| --- | --- |
| **Arte das Cartas** | Cartas personalizadas em pixel art para as faces frontais (Naipes e Valores) e versos, renderizadas em baixa resolução (ex: 70 × 100 px) e dimensionadas com interpolação *nearest-neighbor* para manter o aspecto nítido e pixelado. |
| **Tipografia** | Fontes estilo pixel/monoespaçadas (ex: *Press Start 2P*, *Silkscreen* ou arquivos TTF personalizados). |
| **Fundo e Efeitos** | Plano de fundo animado em pixel art para a mesa de jogo (ex: padrão retro de feltro dinâmico ou efeito suave de tubo de raios catódicos - CRT). |
| **Juice / Polimento** | - Inclinação e rotação da carta ao arrastar, variando com a velocidade do mouse (delta X/Y).<br>

<br>- Sombras dinâmicas baseadas na elevação/profundidade da pilha.<br>

<br>- Efeitos de partículas e faíscas ao posicionar cartas nas Fundações. |
| **Paleta de Cores** | Paleta retro de alto contraste (vermelhos e azuis neon vibrantes, dourado e fundo escuro ambiente). |

---

## 3. Requisitos Funcionais Principais

### 3.1 Gerenciamento do Baralho e Cartas

* **Baralho Padrão:** 52 cartas de baralho (4 naipes: Espadas ♠, Copas ♥, Ouros ♦, Paus ♣; valores de Ás a Rei).
* **Estado da Carta:**
* Virada para cima vs. Virada para baixo.
* Naipe, Valor, Cor (Vermelho/Preto).
* ID Único / Z-Index da camada de renderização.


* **Embaralhamento:** Ordem aleatória das cartas gerada de forma criptográfica na inicialização ou reinício do jogo.

### 3.2 Campo de Jogo (Layout do Tabuleiro)

O campo de jogo consiste em uma área principal (`ft.Stack`) com posições específicas (**Slots**):

1. **Monte / Baralho (1):** Mantém as cartas restantes viradas para baixo. Um clique compra 1 ou 3 cartas para o Descarte.
2. **Descarte (1):** A carta do topo fica virada para cima e disponível para jogo.
3. **Fundações (4):** Construídas por naipe, em ordem crescente do Ás ao Rei.
4. **Colunas do Tabuleiro (7):** Colunas em leque contendo cartas viradas para baixo e cartas jogáveis viradas para cima. Construídas em ordem decrescente alternando as cores (Vermelho sobre Preto / Preto sobre Vermelho).

---

### 3.3 Mecânicas e Interação de Arrastar e Soltar (Drag-and-Drop)

```
[ Monte ]  [ Descarte ]        [ Fundação 1 ] [ Fundação 2 ] [ Fundação 3 ] [ Fundação 4 ]
-----------------------------------------------------------------------------------------
                                 [ Tabuleiro 1-7 (Pilhas em Leque) ]

```

* **Movimento de Arraste:**
* Cartas são movidas via `ft.GestureDetector(on_pan_update=...)`.
* Arrastar uma carta intermediária em uma coluna do Tabuleiro move todas as cartas empilhadas abaixo dela como um único grupo.


* **Reordenação de Camadas (Z-Index):**
* Quando o arraste começa (`on_pan_start`), as cartas arrastadas são movidas para o topo da lista `controls` da `Stack` para evitar renderização abaixo de outras cartas.


* **Proximidade e Encaixe:**
* Se solta dentro da distância de proximidade (`DROP_PROXIMITY`, ex: 25 px) de um slot válido, a carta se encaixa na posição.


* **Retorno Suave (Bounce-Back):**
* Se solta em um local inválido ou fora de qualquer slot, a carta retorna suavemente às suas coordenadas/slot de origem.


* **Clique Duplo / Movimento Automático:**
* Dar um clique duplo em uma carta válida envia-a automaticamente para a Fundação apropriada, se a jogada for permitida.



---

### 3.4 Lógica de Jogo e Regras

* **Posicionamento no Tabuleiro:** Cartas devem ser posicionadas em ordem decrescente com cores alternadas (ex: 9 Vermelho sobre 10 Preto).
* **Posicionamento na Fundação:** Cartas devem corresponder ao naipe e ser colocadas em ordem crescente, do Ás até o Rei.
* **Reis em Slots Vazios:** Apenas Reis (ou pilhas lideradas por um Rei) podem ser colocados em colunas vazias do Tabuleiro.
* **Revelação de Cartas:** Quando a carta superior virada para cima de uma coluna é movida, a carta virada para baixo diretamente abaixo dela é revelada automaticamente.
* **Condição de Vitória:** Detectada automaticamente quando todas as 4 Fundações contiverem 13 cartas cada (total de 52 cartas). Dispara uma animação festiva de cascata de cartas em pixel art.

---

### 3.5 Interface do Usuário (UI) e Funcionalidades

* **Barra Superior / Cabeçalho:**
* **Pontuação e Multiplicador:** Indicador estilo Balatro (ex: +100 por carta posicionada, multiplicadores bônus por jogadas rápidas/sequências).
* **Cronômetro e Contador de Movimentos.**
* **Botões:** `Novo Jogo`, `Reiniciar`, `Desfazer Movimento`, `Configurações`.


* **Sistema de Desfazer (Undo):**
* Pilha que armazena os estados do tabuleiro, permitindo reverter jogadas passo a passo.


* **Painel de Configurações:**
* Opção para ativar/desativar linhas de varredura CRT / efeito de trepidação da tela.
* Controles de áudio (Volume Principal, Efeitos Sonoros, Música Chiptune Retro).



---

## 4. Arquitetura Técnica e Estrutura de Classes em Flet

Seguindo princípios orientados a objetos compatíveis com a arquitetura de tutoriais do Flet:

```
                  ┌────────────────────────┐
                  │    ft.Page (Janela)    │
                  └───────────┬────────────┘
                              │
                  ┌───────────▼────────────┐
                  │ SolitaireGame (Stack)  │
                  └─────┬────────────┬─────┘
                        │            │
         ┌──────────────▼───┐    ┌───▼──────────────┐
         │ Slot(Container)  │    │Card(GestureDet.) │
         └──────────────────┘    └──────────────────┘

```

### 4.1 Definição da Hierarquia de Classes

1. **`Slot(ft.Container)`**
* Propriedades: `slot_type` (Monte, Descarte, Fundação, Tabuleiro), `pile` (lista de objetos `Card`), `left`, `top`.
* Métodos: `add_card()`, `remove_card()`, `get_top_card()`.


2. **`Card(ft.GestureDetector)`**
* Propriedades: `suit`, `rank`, `value`, `color`, `is_face_up`, `slot` (referência ao slot atual), `pixel_image_path`.
* Eventos: `on_pan_start`, `on_pan_update`, `on_pan_end`.
* Métodos: `flip()`, `bounce_back()`, `place(slot)`.


3. **`SolitaireGame(ft.Stack)`**
* Controla o estado do jogo, pontuação, pilha de desfazer, detecção de vitória, criação do baralho e posicionamento dos slots.



---

## 5. Requisitos Não Funcionais

| Métrica | Requisito Alvo |
| --- | --- |
| **Desempenho** | Manter **60 FPS** estáveis durante o arraste de múltiplas cartas e animações no desktop e web. |
| **Latência** | Inferior a **16 ms** de resposta no evento `on_pan_update` para evitar atraso de entrada (input lag). |
| **Tamanho dos Assets** | Spritesheets PNG otimizados e arquivos de áudio leves para manter o executável final abaixo de **15 MB**. |
| **Multiplataforma** | Suporte a UI multiplataforma sem modificações no Windows, Linux, macOS e navegadores web via Flet. |
