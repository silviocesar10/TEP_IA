import os
import shutil
import random

# Caminho para a pasta original
caminho_origem = '/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/imgs/dogs'

# Caminho para a pasta de destino
caminho_destino = '/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/test/dogs'

# Lista todos os arquivos na pasta original
arquivos = os.listdir(caminho_origem)

# Filtra apenas os arquivos que têm o padrão 'dog_ (n).png'
arquivos_filtrados = [arq for arq in arquivos if arq.startswith('dog_') and arq.endswith('.png')]

# Embaralha a lista de arquivos
random.shuffle(arquivos_filtrados)

# Seleciona os primeiros 20 arquivos
arquivos_selecionados = arquivos_filtrados[:20]

# Move os arquivos selecionados para a pasta de destino
for arq in arquivos_selecionados:
    caminho_arquivo_origem = os.path.join(caminho_origem, arq)
    caminho_arquivo_destino = os.path.join(caminho_destino, arq)
    
    # Verifica se o arquivo de origem ainda existe antes de mover
    if os.path.exists(caminho_arquivo_origem):
        shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
    else:
        print(f"O arquivo {arq} não existe no caminho de origem.")

print("Arquivos movidos com sucesso.")
