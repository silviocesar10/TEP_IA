from collections import Counter




import nltk
import os
import sys
#nltk.download("punkt")

def main():
    if len(sys.argv) != 3:
        sys.exit("Uso: python ngramas.py n machado")
    print("Carregando dados...")
    n = int(sys.argv[1])
    conteudo = carregar_dados(sys.argv[2])
    # Computa os  n-gramas
    ngramas = Counter(nltk.ngrams(conteudo, n))
    # Mostra os n-gramas mais frequentes
    for ngrama, freq in ngramas.most_common(20):
        print(f"{freq}: {ngrama}")


def carregar_dados(diretorio):
    conteudos = []
    # Lê todos os arquivos e extrai as palavras
    for arquivo in os.listdir(diretorio):
        with open(os.path.join(diretorio, arquivo), encoding="utf-8") as arq:
            conteudos.extend(
                [
                    palavra.lower()
                    for palavra in nltk.word_tokenize(arq.read())
                    if any(c.isalpha() for c in palavra)
                ]
            )
    return conteudos


if __name__ == "__main__":
    main()
