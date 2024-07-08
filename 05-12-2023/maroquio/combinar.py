import os
import argparse


def combinar_arquivos_txt(diretorio_entrada, arquivo_saida):
    # Verificar se o diretório de entrada existe
    if not os.path.exists(diretorio_entrada):
        print(f'O diretório de entrada "{diretorio_entrada}" não existe.')
        return

    # Verificar se o diretório de entrada é válido
    if not os.path.isdir(diretorio_entrada):
        print(f'O caminho "{diretorio_entrada}" não é um diretório válido.')
        return

    # Inicializar uma lista para armazenar o conteúdo dos arquivos
    conteudo_arquivos = []

    # Percorrer todos os arquivos no diretório de entrada
    for nome_arquivo in os.listdir(diretorio_entrada):
        if nome_arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(diretorio_entrada, nome_arquivo)
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo_arquivo = arquivo.read()
                conteudo_arquivos.append(conteudo_arquivo)

    # Verificar se existem arquivos .txt no diretório
    if not conteudo_arquivos:
        print(f'Não foram encontrados arquivos .txt em "{diretorio_entrada}".')
        return

    # Combinar o conteúdo dos arquivos em um único texto
    texto_combinado = "\n".join(conteudo_arquivos)

    # Salvar o texto combinado no arquivo de saída especificado
    with open(arquivo_saida, "w", encoding="utf-8") as arquivo_final:
        arquivo_final.write(texto_combinado)

    print(f'Todos os arquivos .txt foram combinados em "{arquivo_saida}".')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Combine arquivos .txt de um diretório em um único arquivo"
    )
    parser.add_argument(
        "diretorio_entrada",
        type=str,
        help="Diretório de entrada contendo os arquivos .txt",
    )
    parser.add_argument(
        "arquivo_saida", type=str, help="Nome do arquivo de saída combinado"
    )

    args = parser.parse_args()
    combinar_arquivos_txt(args.diretorio_entrada, args.arquivo_saida)
