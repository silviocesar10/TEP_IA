import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('1_dataset.csv')

# Plotar os pontos para cada classe
for classe, cor in zip(['Grafoo', 'Tiglon'], ['blue', 'red']):
    subset = df[df['Classe'] == classe]
    plt.scatter(subset['X'], subset['Y'], c=cor, label=classe, edgecolors='k')

# Adicionar a linha de separação teórica
# m = 0.5  # Coeficiente angular que você usou para gerar os dados
# c = 0  # Interceptação que você usou para gerar os dados
# x_vals = np.array(plt.gca().get_xlim())
# y_vals = m * x_vals + c
# plt.plot(x_vals, y_vals, '--', color="green", label='Linha de separação')

# Adicionar legendas e títulos
plt.title('Distribuição dos Dados')
plt.xlabel('Tamanho do Chifre')
plt.ylabel('Tamanho da Juba')
plt.legend()

# Mostrar o gráfico
plt.show()
