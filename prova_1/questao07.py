# 7. Faça um programa em Python que crie um arquivo contendo 10 jogos da Mega-Sena, 1 por linha. Cada jogo da Mega-Sena é composto por seis números entre 1 e 60.
import random

lista_jogos = []
i =0 
while (len(lista_jogos) < 6):
    jogo  = []
    while (len(jogo) < 6):
        n = random.randrange(1,60,1)
        jogo.append(n)
    lista_jogos.append(jogo)

for i in lista_jogos:
    print(i)   