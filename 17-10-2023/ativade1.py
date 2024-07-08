import numpy as n

matriz_transicao = n.array([
    [0.8, 0.2],
    [0.3, 0.7]
])

def proximo_estado(estado_atual, matriz_transicao):
    return n.random.choice([0, 1], p=matriz_transicao[estado_atual])


estados = [0]

for i in range(7):
    estados.append(proximo_estado(estados[-1], matriz_transicao))

mapa_estados ={
    0: 'Sol',
    1: 'Chuva'
}

print([mapa_estados[estado] for estado in estados])