# Solucionador Sudoku com Interface Gráfica

Sudoku é um jogo cujo objetivo é a colocação de números de 1 a 9 em cada uma das células vazias numa grade 9x9, constituída por subgrades 3x3 chamadas regiões. Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9.  
Normalmente um desafio Sudoku apresenta uma solução do tabuleiro para que os jogadores possam verificar se venceram, mas caso não apresente, o jogador pode utilizar esse código para visualizar uma solução (ou pesquisar na internet).  

O projeto foi inspirado por um vídeo que indicava seu desenvolvimento para aprendizado: http://bit.ly/sudoku-solver-video

# Instruções

Rode o arquivo 'jogo_sudoku.py' para iniciar o programa.  
O jogo abrirá um tabuleiro de sudoku vazio para ser preenchido com o tabuleiro que você está querendo resolver.  
Para inserir um número basta selecionar uma célula vazia, clicar no número desejado e teclar Enter.  
Caso você queira um jogo teste para entender melhor como o Sudoku funciona tecle C que um tabuleiro será gerado para você (ao inserir um número em uma posição inválida será adicionado um erro no canto inferior esquerdo da tela).  
Quando desejar a solução, basta teclar a barra de espaço.

# Método de solução

O programa utiliza um algoritmo de força bruta chamado Backtracking (Wikipedia Backtracking: https://pt.wikipedia.org/wiki/Backtracking).

