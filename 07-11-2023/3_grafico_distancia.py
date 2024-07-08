import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_csv('3_dataset.csv')

# Escolhendo 'Area' como nossa variável independente
X = df[['DistanciaCentro']]
y = df['PrecoAluguel']

# Ajustando o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Calculando os valores previstos de y para a linha de regressão
X_predict = np.linspace(X.min(), X.max()).reshape(-1, 1)  # X de predição para a linha
y_predict = model.predict(X_predict)

# Plotando os pontos de dados
plt.scatter(X, y, color='blue', alpha=0.5, label='Dados Reais')

# Plotando a linha de regressão
plt.plot(X_predict, y_predict, color='red', linewidth=2, label='Linha de Regressão')

# Títulos e labels
plt.xlabel('Distância (km)')
plt.ylabel('Preço do Aluguel (R$)')
plt.title('Regressão Linear para Preço do Aluguel baseado na Área')
plt.legend()

# Mostrando o gráfico
plt.show()
