import numpy as np

matriz_transicao = np.array([
    [0.2, 0.5, 0.1, 0.1, 0.1],
    [0.4, 0.2, 0.2, 0.1, 0.1],
    [0.1, 0.1, 0.2, 0.5, 0.1],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2]
])

def proximo_estado(estado_atual, matriz_transicao):
    return np.random.choice([0, 1, 2, 3, 4], p=matriz_transicao[estado_atual])

estados = [0]

for i in range(7):
    estados.append(proximo_estado(estados[-1], matriz_transicao))

mapa_estados ={
    0: 'Arroz',
    1: 'Feijao',
    2: 'Carne',
    3: 'Ovo',
    4: 'Tomate'
}

print([mapa_estados[estado] for estado in estados])