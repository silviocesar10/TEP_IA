import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Carregar os dados
df = pd.read_csv('3_dataset.csv')

# Definir as variáveis independente (X) e dependente (y)
X = df[['Area', 'DistanciaCentro']]
y = df['PrecoAluguel']

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calcular o Erro Quadrático Médio (MSE) para avaliar o desempenho
mse = mean_squared_error(y_test, y_pred)
print(f'O Erro Quadrático Médio (MSE) no conjunto de teste é: {mse}')

# Para utilizar o modelo para fazer uma previsão de aluguel individual, você pode fazer:
area = 300  # exemplo de área em m²
distancia = 5  # exemplo de distância em km até o centro
preco_predito = model.predict([[area, distancia]])
print(f'O preço de aluguel previsto é: R${preco_predito[0]:.2f}')
