import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as constantes do jogo
LARGURA = 300
ALTURA = 300
LINHAS = 3
COLUNAS = 3
TAMANHO_CELULA = LARGURA // COLUNAS

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Inicialize a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tic-Tac-Toe")

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(1, LINHAS):
        pygame.draw.line(tela, PRETO, (0, linha * TAMANHO_CELULA), (LARGURA, linha * TAMANHO_CELULA), 2)
        pygame.draw.line(tela, PRETO, (linha * TAMANHO_CELULA, 0), (linha * TAMANHO_CELULA, ALTURA), 2)

# Função principal do jogo
def main():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(BRANCO)
        desenhar_tabuleiro()
        pygame.display.update()

if __name__ == "__main__":
    main()
