# Solucionador de Sudoku

Esse projeto foi desenvolvido apenas para entender um pouco melhor o [Pygame](https://www.pygame.org/news) e me divertir, pois gosto muito de jogos lógicos e queria saber como criar um algoritmo que resolvesse qualquer sudoku.

# Sumário
1. [Como o Sudoku Funciona](#sudoku)
2. [Como Iniciar o Projeto em Sua Máquina](#howto)
3. [Método de Solução](#backtracking)
4. [Agradecimentos](#agradecimentos)


<a name="sudoku"></a>
## Como o Sudoku Funciona

Sudoku é um jogo cujo objetivo é a colocação de números de 1 a 9 em cada uma das células vazias numa grade 9x9, constituída por subgrades 3x3 chamadas regiões. Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9. Normalmente um desafio Sudoku apresenta uma solução do tabuleiro para que os jogadores possam verificar se venceram, mas caso não apresente, o jogador pode utilizar esse código para visualizar uma solução (ou pesquisar na internet).  
[Neste link](https://www.youtube.com/watch?v=t3nx8axVxlk) você pode visualizar como o jogo funciona e algumas dicas para jogá-lo.

<a name="howto"></a>
## Como Iniciar o Projeto em Sua Máquina
Para testar o programa, siga os seguintes passos:

1. Instale a biblioteca `Pygame` utilizando o terminal (macOS/Linux) ou cmd (Windows) com o seguinte comando: `pip install pygame`
2. Rode o arquivo 'jogo_sudoku.py' do diretório do projeto utilizando o terminal ou cmd com a linha `python3 jogo_sudoku.py`.
3. O jogo abrirá um tabuleiro de sudoku vazio para ser preenchido com o tabuleiro que você está querendo resolver.
4. Para inserir um número basta selecionar uma célula vazia, clicar no número desejado e teclar Enter.
Caso você queira um jogo teste para checar se tudo está funcionando tecle a letra `c` que um tabuleiro será gerado para você (ao inserir um número em uma posição inválida será adicionado um erro no canto inferior esquerdo da tela).
5. Quando desejar a solução, basta teclar a barra de espaço.

<a name="backtracking"></a>
## Método de Solução
O programa utiliza um algoritmo de força bruta chamado backtracking. Caso queira se aprofundar, disponibilizo a página sobre backtracking na [Wikipedia](https://pt.wikipedia.org/wiki/Backtracking).

<a name="agradecimentos"></a>
## Agradecimentos
O projeto foi inspirado por um [vídeo](http://bit.ly/sudoku-solver-video) que indicava uma versão reduzida desse projeto visando melhorar seu portfolio e desenvolver de novas habilidades.

