from scipy.spatial.distance import cosine

import numpy as np

with open("machado_vetores_palavras.txt") as arquivo:
    palavras = dict()
    for linha in arquivo:
        frase = linha.split()
        palavra = frase[0]
        vetor = np.array([float(x) for x in frase[1:]])
        palavras[palavra] = vetor


def distancia(w1, w2):
    return cosine(w1, w2)


def palavras_proximas(palavra):
    distancias = {p: distancia(palavra, palavras[p]) for p in palavras}
    return sorted(distancias, key=lambda w: distancias[w])[:10]


def palavra_proxima(palavra):
    return palavras_proximas(palavra)[0]


# Como usar:
# rodar no terminal: python
# >>> from vetor import *
# >>> palavras["amor"]
# >>> distancia(palavras["amor"], palavras["ódio"])
# >>> distancia(palavras["amor"], palavras["esposa"])
# >>> palavras_proximas(palavras["amor"])[:10]
# >>> palavra_proxima(palavras["amor"] - palavras["ódio"] + palavras["mulher"])
