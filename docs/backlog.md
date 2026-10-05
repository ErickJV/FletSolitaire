Roteiro de Desenvolvimento (Roadmap) e Fases

```
Fase 1: Base ──► Fase 2: Regras do Jogo ──► Fase 3: Polimento Pixel ──► Fase 4: Áudio e Deploy
(PoC de Arraste Flet)  (Lógica do Solitaire)     (Visual Estilo Balatro)     (FX, Pontuação, Executável)

```

### Fase 1: Prova de Conceito e Mecanismo de Arraste

* [ ] Configurar ambiente inicial do projeto Flet.
* [ ] Criar card e window principal.
* [ ] Implementar o arraste e soltar da `Card` (`ft.GestureDetector`) no `SolitaireGame` (`ft.Stack`).
* [ ] Implementar detecção de proximidade do `Slot` e reordenação de camadas Z-Index (`move_on_top`).

### Fase 2: Regras do Solitaire e Pilhas em Leque

* [ ] Criar estrutura de dados de 52 cartas com naipes/valores.
* [ ] Criar lógica de posicionamento em leque para pilhas do Tabuleiro.
* [ ] Implementar regras completas do Klondike (Fundação, Tabuleiro, Monte/Descarte).
* [ ] Adicionar animação de virar cartas e detecção de auto-movimento.

### Fase 3: Pixel Art Estilo Balatro e Polimento Visual

* [ ] Integrar pacote de assets em pixel art (faces, versos e fontes pixeladas).
* [ ] Aplicar escala *nearest-neighbor* nas imagens do Flet para manter os pixels definidos.
* [ ] Adicionar efeitos de inclinação ao arrastar e partículas ao posicionar cartas.
* [ ] Criar interface superior (HUD) estilo Balatro com contador de Pontos/Multiplicadores.

### Fase 4: Áudio, Estado do Jogo e Implantação

* [ ] Integrar efeitos sonoros retro (embaralhar, arrastar, deslizar, som de vitória).
* [ ] Implementar sistema de pilha para `Desfazer` e painel de `Configurações`.
* [ ] Empacotar executável standalone para desktop via PyInstaller ou `flet build`.
