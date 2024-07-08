import nltk
import os
import sys


def main():
    # Lê os dados dos arquivos
    if len(sys.argv) != 2:
        sys.exit("Uso: python sentimento.py comentarios")
    positivos, negativos = carregar_dados(sys.argv[1])
    # Cria um conjunto com todas as palavras
    palavras = set()
    for document in positivos:
        palavras.update(document)
    for document in negativos:
        palavras.update(document)
    # Extrai as características do texto
    treinamento = []
    treinamento.extend(gerar_caracteristicas(positivos, palavras, "Positivo"))
    treinamento.extend(gerar_caracteristicas(negativos, palavras, "Negativo"))
    # Classifica uma nova amostra
    classificador = nltk.NaiveBayesClassifier.train(treinamento)
    comentario = input("Comentário: ")
    resultado = classificar(classificador, comentario, palavras)
    for key in resultado.samples():
        print(f"{key}: {resultado.prob(key):.4f}")


def extrair_palavras(documento):
    return set(
        palavra.lower()
        for palavra in nltk.word_tokenize(documento)
        if any(c.isalpha() for c in palavra)
    )


def carregar_dados(diretorio):
    resultado = []
    for arquivo in ["positivos.txt", "negativos.txt"]:
        with open(os.path.join(diretorio, arquivo), encoding="utf-8") as arq:
            resultado.append(
                [extrair_palavras(linha) for linha in arq.read().splitlines()]
            )
    return resultado


def gerar_caracteristicas(documentos, palavras, rotulo):
    caracteristicas = []
    for documento in documentos:
        caracteristicas.append(
            ({palavra: (palavra in documento) for palavra in palavras}, rotulo)
        )
    return caracteristicas


def classificar(classificador, documento, palavras):
    palavras_no_documento = extrair_palavras(documento)
    caracteristicas = {
        palavra: (palavra in palavras_no_documento) for palavra in palavras
    }
    return classificador.prob_classify(caracteristicas)


if __name__ == "__main__":
    main()

# Tarefa: salvar o classificador treinado usando o pickle
