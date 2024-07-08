# Importe as classes e funções que você já definiu
from logic import *

# Defina símbolos com nomes descritivos para as características das casas e seus ocupantes
# Utilize os valores fornecidos
cores = ["Amarelo", "Azul", "Vermelho", "Verde", "Branco"]
nacionalidades = ["Norueguês", "Dinamarquês", "Britânico", "Alemão", "Suíço"]
bebidas = ["Água", "Chá", "Leite", "Café", "Cerveja"]
cigarros = ["Dunhill", "Blends", "PallM", "Prince", "BlueM"]
animais = ["Gato", "Cavalo", "Pássaro", "Peixe", "Cachorro"]

# Crie símbolos para representar as características das casas e seus ocupantes
cor_casas = [Symbol(f'CorCasa{i}') for i in range(1, 6)]
nacionalidade_pessoas = [Symbol(f'NacionalidadePessoa{i}') for i in range(1, 6)]
bebida_casas = [Symbol(f'BebidaCasa{i}') for i in range(1, 6)]
cigarro_pessoas = [Symbol(f'CigarroPessoa{i}') for i in range(1, 6)]
animal_casas = [Symbol(f'AnimalCasa{i}') for i in range(1, 6)]

# Defina as pistas como sentenças lógicas com base nos valores fornecidos
# Por exemplo, "A casa amarela está à esquerda da casa branca."
pista_1 = Implication(nacionalidade_pessoas[2], cor_casas[2])
pista_2 = Implication(nacionalidade_pessoas[4], animal_casas[4])
pista_3 = Implication(nacionalidade_pessoas[1], bebida_casas[1])
#pista_4 = Implication(cor_casas[3], cor_casas[4])
pista_5 = Implication(cor_casas[3], bebida_casas[1])
pista_6 = Implication(cigarro_pessoas[2], animal_casas[2])
pista_7 = Implication(cor_casas[0], cigarro_pessoas[0])
#pista_8 = Implication(cor_casas[2], )
#pista_9
#pista_10 =
# Continuar com as outras pistas...

# Defina a sentença lógica que representa todas as pistas
knowledge_base = And(
    pista_1,
    pista_2,
    pista_3,
    pista_5,
    pista_6,
    pista_7,
    # Adicione as outras pistas aqui usando And, Implication, etc.
)

# Defina a pergunta que você quer responder
# Por exemplo, "Quem bebe leite?"
query = [nacionalidade_pessoas[i - 1] for i in range(1, 6) if bebidas[i - 1] == "Leite"][0]

# Verifique se a knowledge_base implica a query
result = model_check(knowledge_base, query)

# Imprima o resultado
if result:
    print(f"A knowledge_base implica que o {query} bebe leite.")
else:
    print("Não podemos deduzir quem bebe leite com base nas informações fornecidas.")
