from pgmpy.sampling import BayesianModelSampling
from model_livro import model

qtde_amostras = 10000

amostrador = BayesianModelSampling(model)
amostras = amostrador.forward_sample(qtde_amostras)

qtde_amostras = 10000

# T = Intensivo, F = Baixo
evidence1 = {'Treinamento': 0, 'Financiamento': 0}
amostras1 = amostrador.forward_sample(qtde_amostras, evidence=evidence1)
qtde_intensivo_baixo = len(amostras1)

# DA = Ruim, F = Alto
evidence2 = {'DA': 0, 'Financiamento': 2}
amostras2 = amostrador.forward_sample(qtde_amostras, evidence=evidence2)
qtde_ruim_alto = len(amostras2)

# DA = Bom, T = Baixo, F = Alto
evidence3 = {'DA': 2, 'Treinamento': 0, 'Financiamento': 2}
amostras3 = amostrador.forward_sample(qtde_amostras, evidence=evidence3)
qtde_bom_baixo_alto = len(amostras3)

probabilidade_intensivo_baixo = qtde_intensivo_baixo / qtde_amostras
probabilidade_ruim_alto = qtde_ruim_alto / qtde_amostras
probabilidade_bom_baixo_alto = qtde_bom_baixo_alto / qtde_amostras


print(f"Probabilidade T = Intensivo, F = Baixo: {probabilidade_intensivo_baixo:.2f}")
print(f"Probabilidade DA = Ruim, F = Alto: {probabilidade_ruim_alto:.2f}")
print(f"Probabilidade DA = Bom, T = Baixo, F = Alto: {probabilidade_bom_baixo_alto:.2f}")
