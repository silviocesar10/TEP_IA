from pgmpy.inference import VariableElimination
from model_livro import model

# Fazendo inferência
infer = VariableElimination(model)

# Mapeamento de rótulos
mapa_clima = {0: 'ensolarado', 1: 'chuvoso', 2: 'nublado'}
mapa_autor = {0: 'disponível', 1: 'indisponível'}
mapa_marketing = {0: 'promoção', 1: 'sem promoção'}
mapa_critica = {0: 'positiva', 1: 'negativa'}
mapa_lancamento = {0: 'sucesso', 1: 'fracasso'}

# Consultar a probabilidade de o lançamento ser um sucesso em um dia chuvoso
result = infer.query(variables=['Lancamento'], evidence={'Clima': 1}) # 1 corresponde a "chuvoso"

# Imprimir resultados da consulta
print("Probabilidade do lançamento, em dia chuvoso, ser um:")
for index, prob in enumerate(result.values):
    print(f"{mapa_lancamento[index]}: {prob:.2f}")


result2 = infer.query(variables=['Clima'], evidence={'Lancamento': 0}) # 2
print("Probabilidades de Clima quando é sucesso:")
for index, prob in enumerate(result2.values):
    print(f"{mapa_clima[index]}: {prob:.2f}")

result3 = infer.query(variables=['Autor'], evidence={'Lancamento': 0}) # 2
print("Probabilidades de Autor quando é sucesso:")
for index, prob in enumerate(result3.values):
    print(f"{mapa_autor[index]}: {prob:.2f}")

result4 = infer.query(variables=['Marketing'], evidence={'Lancamento': 0}) # 2
print("Probabilidades de Marketing quando é sucesso:")
for index, prob in enumerate(result4.values):
    print(f"{mapa_marketing[index]}: {prob:.2f}")

result5 = infer.query(variables=['Critica'], evidence={'Lancamento': 0}) # 2
print("Probabilidades de Critica quando é sucesso:")
for index, prob in enumerate(result5.values):
    print(f"{mapa_critica[index]}: {prob:.2f}")