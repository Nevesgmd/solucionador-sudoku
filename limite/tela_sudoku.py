from controle.controlador_sudoku import ControladorSudoku
import pygame
pygame.font.init()


class TelaSudoku:
    class Celulas:
        def __init__(self, valor: int, linha: int, coluna: int,
                     largura: int, altura: int):
            self.__valor = valor
            self.__linha = linha
            self.__coluna = coluna
            self.__largura = largura
            self.__altura = altura
            self.__num_esboco = 0
            self.__selecionado = False

        def desenhar(self, janela):
            fonte = pygame.font.SysFont("comicsans", 40)

            tamanho_celula = self.__largura / 9
            x = self.__coluna * tamanho_celula
            y = self.__linha * tamanho_celula

            if self.__num_esboco != 0 and self.__valor == 0:
                esboco = fonte.render(str(self.__num_esboco), 1, (128, 128, 128))
                janela.blit(esboco, (x + 5, y + 5))
            elif not (self.__valor == 0):
                numero_escolhido = fonte.render(str(self.__valor), 1, (0, 0, 0))
                janela.blit(numero_escolhido, (x + (tamanho_celula / 2 - numero_escolhido.get_width() / 2),
                                               y + (tamanho_celula / 2 - numero_escolhido.get_height() / 2)))

            if self.__selecionado:
                pygame.draw.rect(janela, (255, 0, 0), (x, y, tamanho_celula, tamanho_celula), 3)

        def desenhar_mudanca(self, janela, g=True):
            fonte = pygame.font.SysFont("comicsans", 40)

            tamanho_celula = self.__largura / 9
            x = self.__coluna * tamanho_celula
            y = self.__linha * tamanho_celula

            pygame.draw.rect(janela, (255, 255, 255), (x, y, tamanho_celula, tamanho_celula), 0)

            numero_escolhido = fonte.render(str(self.__valor), 1, (0, 0, 0))
            janela.blit(numero_escolhido, (x + (tamanho_celula / 2 - numero_escolhido.get_width() / 2),
                                           y + (tamanho_celula / 2 - numero_escolhido.get_height() / 2)))
            if g:
                pygame.draw.rect(janela, (0, 255, 0), (x, y, tamanho_celula, tamanho_celula), 3)
            else:
                pygame.draw.rect(janela, (255, 0, 0), (x, y, tamanho_celula, tamanho_celula), 3)

        @property
        def valor(self):
            return self.__valor

        @valor.setter
        def valor(self, valor):
            self.__valor = valor

        @property
        def linha(self):
            return self.__linha

        @linha.setter
        def linha(self, linha):
            self.__linha = linha

        @property
        def coluna(self):
            return self.__coluna

        @coluna.setter
        def coluna(self, coluna):
            self.__coluna = coluna

        @property
        def largura(self):
            return self.__largura

        @largura.setter
        def largura(self, largura):
            self.__largura = largura

        @property
        def altura(self):
            return self.__altura

        @altura.setter
        def altura(self, altura):
            self.__altura = altura

        @property
        def num_esboco(self):
            return self.__num_esboco

        @num_esboco.setter
        def num_esboco(self, num_esboco):
            self.__num_esboco = num_esboco

        @property
        def selecionado(self):
            return self.__selecionado

        @selecionado.setter
        def selecionado(self, selecionado):
            self.__selecionado = selecionado

    def __init__(self, controlador: ControladorSudoku, largura: int,
                 altura: int, janela: pygame.Surface):
        self.__controlador = controlador
        self.__largura = largura
        self.__altura = altura
        self.__janela = janela
        self.__celulas = [[TelaSudoku.Celulas(self.__controlador.sudoku.tabuleiro[linha][coluna],
                                              linha, coluna, largura, altura)
                           for coluna in range(9)] for linha in range(9)]
        self.__celula_selecionada = None

    def desenhar(self):
        # Draw Grid Lines
        tamanho_celula = self.__largura / 9
        for i in range(10):
            if i % 3 == 0 and i != 0:
                grossura = 4
            else:
                grossura = 1
            pygame.draw.line(self.__janela, (0, 0, 0), (0, i*tamanho_celula),
                             (self.__largura, i*tamanho_celula), grossura)
            pygame.draw.line(self.__janela, (0, 0, 0), (i * tamanho_celula, 0),
                             (i * tamanho_celula, self.__altura), grossura)

        # Draw Cubes
        for linha in range(9):
            for coluna in range(9):
                self.__celulas[linha][coluna].desenhar(self.__janela)

    def inserir_num(self, valor):
        linha, coluna = self.__celula_selecionada
        if self.__celulas[linha][coluna].valor == 0:
            self.__celulas[linha][coluna].valor = valor
            self.__controlador.atualiza_jogo()

            if self.__controlador.eh_valido(valor, (linha, coluna)) and self.__controlador.solucionar():
                return True
            else:
                self.__celulas[linha][coluna].valor = 0
                self.__celulas[linha][coluna].num_esboco = 0
                self.__controlador.atualiza_jogo()
                return False

    def esbocar(self, valor):
        linha, coluna = self.__celula_selecionada
        self.__celulas[linha][coluna].num_esboco = valor

    def selecionar(self, linha, coluna):
        # Reset all other
        for i in range(9):
            for j in range(9):
                self.__celulas[i][j].selecionado = False

        self.__celulas[linha][coluna].selecionado = True
        self.__celula_selecionada = (linha, coluna)
        print(self.__celula_selecionada)

    def clique(self, posicao):
        if posicao[0] < self.__largura and posicao[1] < self.__altura:
            tamanho_celula = self.__largura / 9
            x = posicao[0] // tamanho_celula
            y = posicao[1] // tamanho_celula
            return int(y), int(x)
        else:
            return None

    def mostrar_solucao(self):
        self.__controlador.solucionar()
        for linha in range(len(self.__controlador.sudoku.tabuleiro)):
            for coluna in range(len(self.__controlador.sudoku.tabuleiro[linha])):
                self.__celulas[linha][coluna].valor = self.__controlador.sudoku.tabuleiro[linha][coluna]
                self.__celulas[linha][coluna].desenhar_mudanca(self.__janela, True)
                pygame.display.update()
                pygame.time.delay(100)

    def redesenhar_tela(self, tempo, erros):
        self.janela.fill((255, 255, 255))
        # Draw time
        fonte = pygame.font.SysFont("comicsans", 40)
        texto_tempo = fonte.render("Time: " + self.__controlador.formatar_tempo(tempo), 1, (0, 0, 0))
        self.__janela.blit(texto_tempo, (540 - 160, 560))
        # Draw Strikes
        texto_erros = fonte.render("X " * erros, 1, (255, 0, 0))
        self.__janela.blit(texto_erros, (20, 560))
        # Draw grid and board
        self.desenhar()

    @property
    def controlador(self):
        return self.__controlador

    @controlador.setter
    def controlador(self, controlador):
        self.__controlador = controlador

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura):
        self.__largura = largura

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def janela(self):
        return self.__janela

    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    @property
    def celulas(self):
        return self.__celulas

    @celulas.setter
    def celulas(self, celulas):
        self.__celulas = celulas

    @property
    def celula_selecionada(self):
        return self.__celula_selecionada

    @celula_selecionada.setter
    def celula_selecionada(self, celula_selecionada):
        self.__celula_selecionada = celula_selecionada
