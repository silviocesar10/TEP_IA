import numpy as np

prob_clima = [0.6, 0.2, 0.2]

prob_autor_dado_clima = {
    0: [0.9, 0.1], # ensolarado
    1: [0.4, 0.6], # chuvoso
    2: [0.8, 0.2], # nublado
}

prob_marketing_dado_clima = {
    0: [0.8, 0.2], # ensolarado
    1: [0.3, 0.7], # chuvoso
    2: [0.7, 0.3], # nublado
}

prob_critica_dado_clima_autor = {
    (0, 0): [0.9, 0.1], # ensolarado, disponível
    (0, 1): [0.7, 0.3], # ensolarado, indisponível
    (1, 0): [0.8, 0.2], # chuvoso, disponível
    (1, 1): [0.6, 0.4], # chuvoso, indisponível
    (2, 0): [0.85, 0.15], # nublado, disponível
    (2, 1): [0.75, 0.25], # nublado, indisponível
}

prob_lancamento_dado_critica_marketing = {
    (0, 0): [0.95, 0.05], # positiva, com promoção
    (0, 1): [0.85, 0.15], # positiva, sem promoção
    (1, 0): [0.7, 0.3], # negativa, com promoção
    (1, 1): [0.5, 0.5], # negativa, sem promoção
}

def amostrar(qtde = 10000):
    amostras = []
    for _ in range(qtde):
        clima = np.random.choice([0, 1, 2], p=prob_clima)
        autor = np.random.choice([0, 1], p=prob_autor_dado_clima[clima])
        marketing = np.random.choice([0, 1], p=prob_marketing_dado_clima[clima])
        critica = np.random.choice([0, 1], p=prob_critica_dado_clima_autor[(clima, autor)])
        lancamento = np.random.choice([0, 1], p=prob_lancamento_dado_critica_marketing[(critica, marketing)])
        amostras.append((clima, autor, marketing, critica, lancamento))
    return amostras

qtde_amostras = 100000
amostras = amostrar(qtde_amostras)

# filtrar amostras onde Clima=chuvoso
amostras_chuvoso = [a for a in amostras if a[0]==1]
qtde_chuvoso = len(amostras_chuvoso)

# filtrar para Lançamento=sucesso
amostras_sucesso = [a for a in amostras_chuvoso if a[4]==0]
qtde_sucesso = len(amostras_sucesso)

# filtrar para Lançamento=fracasso
amostras_fracasso = [a for a in amostras_chuvoso if a[4]==1]
qtde_fracasso = len(amostras_fracasso)

# probabilidade de sucesso
prob_sucesso = qtde_sucesso / qtde_chuvoso

# probabilidade de fracasso
prob_fracasso = qtde_fracasso / qtde_chuvoso

print(f"Probabilidade do lançamento ser um sucesso, dado clima chuvoso: {prob_sucesso:.2f}")

print(f"Probabilidade do lançamento ser um fracasso, dado clima chuvoso: {prob_fracasso:.2f}")