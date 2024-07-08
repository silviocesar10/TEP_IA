import nltk
from GLCs import *


def formatar_terminais(terminais):
    terminais_ordenados = sorted(list(terminais))
    resultado_formatado = " | ".join(terminais_ordenados)
    return resultado_formatado


entrada = "\n".join(
    [
        GLC_FRASES_COM_ADJETIVOS,
        GLC_DETERMINANTES,
        GLC_SUBSTANTIVOS,
        GLC_ADJETIVOS,
        GLC_VERBOS,
        GLC_PREPOSICOES,
    ]
)
gramatica = nltk.CFG.fromstring(entrada)
parser = nltk.ChartParser(gramatica)
frase = input("Frase: ").split()
try:
    for tree in parser.parse(frase):
        tree.pretty_print()
except ValueError:
    print("Nenhuma árvore de análise sintática possível.")

# Tarefa: criar uma gramática para as 4 expressões aritméticas básicas e com precedência usando parênteses
