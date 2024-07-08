#!/bin/bash

# Loop através dos arquivos mazeX.txt
for file in maze*.txt; do
    # Executa o código Python com o arquivo atual
    python main.py "$file"

    # Renomeia o arquivo maze.png gerado para mazeX.png
    mv maze.png "${file%.txt}.png"
done
