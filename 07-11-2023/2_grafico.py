import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('2_dataset.csv')

# Plotar os pontos para cada classe
for classe, cor in zip(['Diabetes', 'Normal'], ['blue', 'red']):
    subset = df[df['Classe'] == classe]
    plt.scatter(subset['Pressao'], subset['Glicose'], c=cor, label=classe, edgecolors='k')

# Adicionar a linha de separação teórica
m = 0.3  # Coeficiente angular que você usou para gerar os dados
c = 40  # Interceptação que você usou para gerar os dados
x_vals = np.array(plt.gca().get_xlim())
y_vals = m * x_vals + c
plt.plot(x_vals, y_vals, '--', color="green", label='Linha de separação')

# Adicionar legendas e títulos
plt.title('Distribuição dos Dados')
plt.xlabel('Glicose')
plt.ylabel('Pressão Arterial')
plt.legend()

# Mostrar o gráfico
plt.show()
