import markovify
import sys

# Verifica se o usuário passou os argumentos corretamente
if len(sys.argv) != 2:
    sys.exit("Uso: python gerador.py machado.txt")
# Lê o texto de um arquivo passado como parâmetro
with open(sys.argv[1], encoding="utf-8") as f:
    text = f.read()
# Treina o modelo de Markov
modelo = markovify.Text(text)
# Gera as sentenças
print()
for i in range(5):
    print(modelo.make_sentence())
    print()

# Tarefa: salvar o modelo usando o pickle
