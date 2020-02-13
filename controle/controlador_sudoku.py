from entidade.sudoku import Sudoku
from random import randint
import pygame
import time


class ControladorSudoku:
    def __init__(self):
        from limite.tela_sudoku import TelaSudoku
        janela = pygame.display.set_mode((540, 600))
        self.__sudoku = Sudoku()
        self.criar_jogo()
        self.__tela_sudoku = TelaSudoku(self, 540, 540, janela)

    def encontrar_vazio(self):
        for linha in range(len(self.__sudoku.tabuleiro)):
            for coluna in range(len(self.__sudoku.tabuleiro[linha])):
                if self.__sudoku.tabuleiro[linha][coluna] == 0:
                    return linha, coluna

        return None

    def eh_valido(self, num_inserido: int, posicao: tuple):
        # Verificando se existe um número igual ao inserido na linha
        for coluna in range(len(self.__sudoku.tabuleiro)):
            if self.__sudoku.tabuleiro[posicao[0]][coluna] == num_inserido and posicao[1] != coluna:
                return False

        # Verificando se existe um número igual ao inserido na coluna
        for linha in range(len(self.__sudoku.tabuleiro)):
            if self.__sudoku.tabuleiro[linha][posicao[1]] == num_inserido and posicao[0] != linha:
                return False

        # Verificando se existe um número igual ao inserido na grade 3x3
        grade_x = posicao[1]//3
        grade_y = posicao[0]//3

        for linha in range(grade_y*3, grade_y*3 + 3):
            for coluna in range(grade_x*3, grade_x*3 + 3):
                if self.__sudoku.tabuleiro[linha][coluna] == num_inserido and (linha, coluna) != posicao:
                    return False

        return True

    def solucionar(self):
        pos_vazia = self.encontrar_vazio()
        if pos_vazia:
            linha, coluna = pos_vazia
        else:
            return True

        for tentativa in range(1, 10):
            if self.eh_valido(tentativa, (linha, coluna)):
                self.__sudoku.tabuleiro[linha][coluna] = tentativa

                if self.solucionar():
                    return True

                self.__sudoku.tabuleiro[linha][coluna] = 0

        return False

    def criar_jogo(self):
        self.solucionar()
        for c in range(70):
            linha = randint(0, 8)
            coluna = randint(0, 8)
            self.__sudoku.tabuleiro[linha][coluna] = 0

        print(self.__sudoku.tabuleiro)

        return True

    """
    def inserir_numero(self, numero: int):
        linha, coluna = self.__tela_sudoku.celula_selecionada
        if self.__sudoku.tabuleiro[linha][coluna] == 0:
            self.__tela_sudoku.celulas[linha][coluna].valor(numero)
            self.atualiza_jogo()

            if self.eh_valido(numero, (linha, coluna)) and self.solucionar():
                return True
            else:
                self.__tela_sudoku.celulas[linha][coluna].valor(0)
                self.__tela_sudoku.celulas[linha][coluna].num_esboco(0)
                self.atualiza_jogo()
                return False
    """

    def tudo_prenchido(self):
        for linha in range(9):
            for coluna in range(9):
                if self.__sudoku.tabuleiro[linha][coluna] == 0:
                    return False
        return True

    def atualiza_jogo(self):
        self.__sudoku.tabuleiro = [[self.__tela_sudoku.celulas[linha][coluna].valor
                                    for coluna in range(9)] for linha in range(9)]

    def iniciar(self):
        pygame.display.set_caption("Sudoku")
        key = None
        rodando = True
        tempo_inicial = time.time()
        erros = 0
        while rodando:

            tempo_rodando = round(time.time() - tempo_inicial)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        key = 1
                    if evento.key == pygame.K_2:
                        key = 2
                    if evento.key == pygame.K_3:
                        key = 3
                    if evento.key == pygame.K_4:
                        key = 4
                    if evento.key == pygame.K_5:
                        key = 5
                    if evento.key == pygame.K_6:
                        key = 6
                    if evento.key == pygame.K_7:
                        key = 7
                    if evento.key == pygame.K_8:
                        key = 8
                    if evento.key == pygame.K_9:
                        key = 9
                    if evento.key == pygame.K_DELETE:
                        self.__tela_sudoku.apagar_celula()
                        key = None

                    if evento.key == pygame.K_SPACE:
                        self.__tela_sudoku.mostrar_solucao()

                    if evento.key == pygame.K_RETURN:
                        linha, coluna = self.__tela_sudoku.celula_selecionada
                        if self.__tela_sudoku.celulas[linha][coluna].num_esboco != 0:
                            if self.__tela_sudoku.inserir_num(self.__tela_sudoku.celulas[linha][coluna].num_esboco):
                                print("Correto")
                            else:
                                print("Errado")
                                erros += 1
                            key = None

                            if self.tudo_prenchido():
                                print("Game over")

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicao = pygame.mouse.get_pos()
                    clicado = self.__tela_sudoku.clique(posicao)
                    if clicado:
                        self.__tela_sudoku.selecionar(clicado[0], clicado[1])
                        key = None

            if self.__tela_sudoku.celula_selecionada and key is not None:
                self.__tela_sudoku.esbocar(key)

            self.__tela_sudoku.redesenhar_tela(tempo_rodando, erros)
            pygame.display.update()

    @staticmethod
    def formatar_tempo(segundos):
        segundo = segundos % 60
        minuto = segundos // 60

        tempo = " " + str(minuto) + ":" + str(segundo)
        return tempo

    @property
    def sudoku(self):
        return self.__sudoku

    @sudoku.setter
    def sudoku(self, sudoku):
        self.__sudoku = sudoku
