from pgmpy.sampling import BayesianModelSampling
from model_livro import model

qtde_amostras = 10000

amostrador = BayesianModelSampling(model)
amostras = amostrador.forward_sample(qtde_amostras)

# amostras onde Clima é chuvoso
amostras_chuvoso = amostras[amostras['Clima']==1]
qtde_chuvoso = len(amostras_chuvoso)

# amostras onde Clima é chuvoso e Lançamento é sucesso
amostras_sucesso = amostras_chuvoso[amostras_chuvoso['Lancamento']==0]
qtde_sucesso = len(amostras_sucesso)

# amostras onde Clima é chuvoso e Lançamento é fracasso
amostras_fracasso = amostras_chuvoso[amostras_chuvoso['Lancamento']==1]
qtde_fracasso = len(amostras_fracasso)

# probabilidade de sucesso
prob_sucesso = qtde_sucesso / qtde_chuvoso

# probabilidade de fracasso
prob_fracasso = qtde_fracasso / qtde_chuvoso

print(f"Probabilidade do lançamento ser um sucesso, dado clima chuvoso: {prob_sucesso:.2f}")

print(f"Probabilidade do lançamento ser um fracasso, dado clima chuvoso: {prob_fracasso:.2f}")