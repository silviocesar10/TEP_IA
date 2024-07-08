import numpy as n
#da
prob_da = [0.3, 0.5, 0.2]  
#treinamento dado da
prob_treinamento = {
    0: [0.7, 0.2, 0.1],  
    1: [0.5,0.3,0.2],    
    2: [0.2,0.3,0.5]     
}
#financiamento dado da
prob_financiamento = {
    0: [0.8,0.15,0.05],  
    1: [0.5,0.3,0.2],    
    2: [0.2,0.4,0.4]     
}
# sucesso dado financiamento e treinamento e da
prob_sucesso = {
    (0,0,0): [0.70,0.25,0.05],     
    (0,0,1): [0.65,0.30,0.05],     
    (0,0,2): [0.60,0.30,0.10],     
    (0,1,0): [0.60,0.30,0.10],     
    (0,1,1): [0.55,0.30,0.15],     
    (0,1,2): [0.45,0.35,0.20],     
    (0,2,0): [0.45,0.35,0.20],     
    (0,2,1): [0.40,0.35,0.25],     
    (0,2,2): [0.35,0.40,0.25],     
    (1,0,0): [0.60,0.30,0.10],     
    (1,0,1): [0.55,0.35,0.10],     
    (1,0,2): [0.50,0.35,0.15],     
    (1,1,0): [0.50,0.35,0.15],     
    (1,1,1): [0.45,0.35,0.20],     
    (1,1,2): [0.40,0.40,0.20],     
    (1,2,0): [0.35,0.40,0.25],     
    (1,2,1): [0.30,0.45,0.25],     
    (1,2,2): [0.25,0.45,0.30],     
    (2,0,0): [0.45,0.40,0.15],     
    (2,0,1): [0.40,0.45,0.15],     
    (2,0,2): [0.35,0.45,0.20],     
    (2,1,0): [0.35,0.45,0.20],     
    (2,1,1): [0.30,0.50,0.20],     
    (2,1,2): [0.25,0.50,0.25],     
    (2,2,0): [0.20,0.50,0.30],     
    (2,2,1): [0.15,0.55,0.30],     
    (2,2,2): [0.10,0.55,0.35],     
}

ddef probabilidade_sucesso(cenario):
    prob_cenario = prob_da[cenario[0]] * prob_treinamento[cenario[0]][cenario[1]] * prob_financiamento[cenario[2]][cenario[2]]
    prob_sucesso_cenario = prob_sucesso[cenario][0]
    return prob_cenario * prob_sucesso_cenario

# Cenários a serem calculados
cenario_1 = (1, 1, 2)  # DA=Ruim, T=Baixo, F=Alto
cenario_2 = (2, 2, 1)  # DA=Bom, T=Alto, F=Moderado
cenario_3 = (0, 2, 1)  # DA=Fraco, T=Alto, F=Moderado

# Calcula as probabilidades de sucesso para os cenários
probabilidade_1 = probabilidade_sucesso(cenario_1)
probabilidade_2 = probabilidade_sucesso(cenario_2)
probabilidade_3 = probabilidade_sucesso(cenario_3)

print(f"Probabilidade de sucesso no cenário 1: {probabilidade_1:.2f}")
print(f"Probabilidade de sucesso no cenário 2: {probabilidade_2:.2f}")
print(f"Probabilidade de sucesso no cenário 3: {probabilidade_3:.2f}")

