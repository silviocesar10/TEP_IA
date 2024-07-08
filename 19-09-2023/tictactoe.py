# main.py
import math
import os
from random import randint

def ler_tabuleiro(nome_arquivo):
    with open(nome_arquivo) as file:
        linhas = file.readlines()
    tabuleiro = [list(linha.strip()) for linha in linhas]
    return tabuleiro

def gravar_tabuleiro(nome_arquivo, tabuleiro):
    with open(nome_arquivo, "w") as file:
        for linha in tabuleiro:
            file.write("".join(linha) + "\n")

def reiniciar_tabuleiro(nome_arquivo):
    with open(nome_arquivo, "w") as file:
        for _ in range(3):
            file.write("___\n") # 3 x _

def adicionar_possibilidade(tabuleiro, pontuacao):
    with open("possibilidades.txt", "a+") as file:
        for linha in tabuleiro:
            file.write("".join(linha) + "\n")
        file.write(f"{pontuacao}\n-------\n")

def quem_joga(tabuleiro):
    qtde_x = sum(linha.count("x") for linha in tabuleiro)
    qtde_o = sum(linha.count("o") for linha in tabuleiro)
    return "x" if qtde_x <= qtde_o else "o"

def tem_espaco_vazio(tabuleiro):
    return any(tabuleiro[i][j] == "_" for i in range(3) for j in range(3))

def tabuleiro_completo(tabuleiro):
    return all(tabuleiro[i][j] != "_" for i in range(3) for j in range(3))

def tabuleiro_vazio(tabuleiro):
    return all(tabuleiro[i][j] == "_" for i in range(3) for j in range(3))

def avaliar(tabuleiro):
    # checa se tem vencedor nas linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            if tabuleiro[i][0] == jogador:
                return 10
            elif tabuleiro[i][0] == oponente:
                return -10
    
    # checa se tem vencedor nas colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j]:
            if tabuleiro[0][j] == jogador:
                return 10
            elif tabuleiro[0][j] == oponente:
                return -10
    
    # checa se tem vencedor na diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[1][1] == jogador:
            return 10
        elif tabuleiro[1][1] == oponente:
            return -10
        
    # checa se tem vencedor na diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        if tabuleiro[1][1] == jogador:
            return 10
        elif tabuleiro[1][1] == oponente:
            return -10
        
    return 0

def minimax(tabuleiro, profundidade, maximizando):
    pontuacao = avaliar(tabuleiro)
    if pontuacao == 10:
        return pontuacao - profundidade
    if pontuacao == -10:
        return pontuacao + profundidade
    if tabuleiro_completo(tabuleiro) and (pontuacao == 0):
        return 0
    
    if maximizando:
        maior_pontuacao = -math.inf
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == "_":
                    tabuleiro[i][j] = jogador
                    pontuacao_atual = minimax(tabuleiro, profundidade+1, False)
                    maior_pontuacao = max(maior_pontuacao, pontuacao_atual)
                    tabuleiro[i][j] = "_"
        return maior_pontuacao
    else:
        menor_pontuacao = math.inf
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == "_":
                    tabuleiro[i][j] = oponente
                    pontuacao_atual = minimax(tabuleiro, profundidade+1, True)
                    menor_pontuacao = min(menor_pontuacao, pontuacao_atual)
                    tabuleiro[i][j] = "_"
        return menor_pontuacao
    
def buscar_melhor_jogada(tabuleiro):
    melhor_valor = -math.inf
    melhor_jogada = (-1, -1)
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "_":
                tabuleiro[i][j] = jogador
                valor_jogada = minimax(tabuleiro, 0, False)
                adicionar_possibilidade(tabuleiro, valor_jogada)
                tabuleiro[i][j] = "_"
                if valor_jogada > melhor_valor:
                    melhor_jogada = (i,j)
                    melhor_valor = valor_jogada
    return melhor_jogada

def jogo_acabou(tabuleiro):
    if avaliar(tabuleiro) != 0:
        return True
    if tabuleiro_completo(tabuleiro):
        return True
    return False


nome_arquivo = "tabuleiro.txt"

tabuleiro = ler_tabuleiro(nome_arquivo)

jogador = quem_joga(tabuleiro)
oponente = "o" if jogador == "x" else "x"

if (jogo_acabou(tabuleiro)):
    print("O jogo anterior acabou.\nO tabuleiro foi reiniciado.")
    reiniciar_tabuleiro(nome_arquivo)
    exit()

if os.path.exists("possibilidades.txt"):
    os.remove("possibilidades.txt")

melhor_jogada = (randint(0,2), randint(0,2))

if tabuleiro_vazio(tabuleiro) == False:
    melhor_jogada = buscar_melhor_jogada(tabuleiro)

tabuleiro[melhor_jogada[0]][melhor_jogada[1]] = jogador
print(f"O jogador '{jogador}' jogou na posição {melhor_jogada}.")

gravar_tabuleiro(nome_arquivo, tabuleiro)