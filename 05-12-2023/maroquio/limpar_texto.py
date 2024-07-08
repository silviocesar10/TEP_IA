import argparse
import os

# Configurar o parser de argumentos
parser = argparse.ArgumentParser(description="Corrigir arquivo de texto")
parser.add_argument("input_file", type=str, help="Nome do arquivo de entrada")

# Analisar os argumentos da linha de comando
args = parser.parse_args()

# Verificar se o arquivo de entrada existe
if not os.path.exists(args.input_file):
    print(f'O arquivo de entrada "{args.input_file}" não existe.')
else:
    # Definir o nome do arquivo de saída com o sufixo "_ok"
    nome_arquivo_saida = os.path.splitext(args.input_file)[0] + "_ok.txt"

    # Abrir o arquivo de entrada em modo de leitura
    with open(args.input_file, "r", encoding="utf-8") as arquivo:
        # Ler o conteúdo do arquivo
        texto = arquivo.read()

    # Remover quebras de linha e espaços extras
    texto_corrigido = " ".join(texto.split())

    # Abrir o arquivo de saída em modo de escrita e salvar o texto corrigido
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_corrigido:
        arquivo_corrigido.write(texto_corrigido)

    print(f'Arquivo corrigido salvo como "{nome_arquivo_saida}"')
