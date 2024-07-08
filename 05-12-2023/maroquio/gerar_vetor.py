import argparse
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import Word2Vec


# Função para preprocessar o texto
def preprocessar_texto(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        text = file.read()

    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

    return tokenized_sentences


# Função para salvar os vetores das palavras
def salvar_vetores(model, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for word in model.wv.key_to_index:
            vector = " ".join(map(str, model.wv[word]))
            file.write(f"{word} {vector}\n")


# Configuração do argparse para entrada do nome do arquivo
parser = argparse.ArgumentParser(description="Word2Vec Vetores de Palavras")
parser.add_argument("arquivo", type=str, help="Nome do arquivo de texto para processar")
args = parser.parse_args()

# Preprocessamento do texto
sentencas_tokenizadas = preprocessar_texto(args.arquivo)

# Treinamento do modelo Word2Vec
model = Word2Vec(
    sentencas_tokenizadas, vector_size=100, window=5, min_count=1, workers=4
)

# Salvando os vetores das palavras em um arquivo
arquivo_vetores = args.arquivo.replace(".txt", "_vetores_palavras.txt")
salvar_vetores(model, arquivo_vetores)

print(f"Vetores das palavras salvos em {arquivo_vetores}.")
