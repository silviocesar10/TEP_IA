from pgmpy.inference import VariableElimination
from model_livro import model

# Fazendo inferência
infer = VariableElimination(model)

# Mapeamento de rótulos
mapa_da = {0: 'excelente', 1: 'bom', 2: 'ruim'}
mapa_treinamento = {0: 'intensivo', 1: 'regular', 2: 'baixo'}
mapa_financiamento = {0: 'alto', 1: 'medio', 2: 'baixo'}
mapa_sucesso = {0: 'vencedor', 1: 'nao_vencedor', 2: 'finalista'}


# T=intensivo, F=baixo
result1 = infer.query(variables=['Treinamento'], evidence={'Treinamento': 2,'Financiamento': 2})
print("Probabilidade T=intensivo, F=baixo:")
for index, prob in enumerate(result1.values):
    print(f"{mapa_treinamento[index]}: {prob:.2f}")

# DA=ruim, F=alto
result2 = infer.query(variables=['DA'], evidence={'Financiamento': 0})
print("Probabilidade DA=ruim, F=alto:")
for index, prob in enumerate(result2.values):
    print(f"{mapa_da[index]}: {prob:.2f}")

# DA=bom, T=baixo, F=alto
result3 = infer.query(variables=['DA'], evidence={'Treinamento': 2, 'Financiamento': 0}) # 2
print("Probabilidade DA=bom, T=baixo, F=alto:")
for index, prob in enumerate(result3.values):
    print(f"{mapa_da[index]}: {prob:.2f}")
