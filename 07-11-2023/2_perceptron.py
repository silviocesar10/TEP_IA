import numpy as np
import pandas as pd

# Ler o dataset a partir de um arquivo CSV
data = pd.read_csv('2_dataset.csv')

# Mapear as classes para valores numéricos: Diabetes -> 1, Normal -> 0
data['Classe'] = data['Classe'].map({'Diabetes': 1, 'Normal': 0})

# Preparar os dados de entrada (features) como um array Numpy (X) e os rótulos (labels) como um array Numpy (y)
X = data[['Pressao', 'Glicose']].values
y = data['Classe'].values

# Adicionar uma coluna de 1s para o termo de bias ao X (cada amostra tem um termo de bias associado)
X = np.c_[np.ones(X.shape[0]), X]

# Definindo a classe Perceptron
class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate  # Taxa na qual o modelo aprende
        self.n_iterations = n_iterations    # Número de passagens pelo dataset (épocas)
        self.weights = None                 # Inicializa os pesos como None
        self.errors_ = []                   # Lista para coletar o número de classificações erradas em cada época

    # método para treinamento do modelo
    # recebe os dados de treino (X) e os rótulos (y) e ajusta os pesos
    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])  # Inicializa os pesos com zeros
        for _ in range(self.n_iterations):   # Loop sobre o número de épocas
            errors = 0                       # Contador de erros para a época atual
            for xi, target in zip(X, y):     # Loop sobre todas as amostras e rótulos
                update = self.learning_rate * (target - self.predict(xi))  # Calcula a atualização necessária
                self.weights[1:] += update * xi[1:]  # Atualiza os pesos para as features
                self.weights[0] += update            # Atualiza o peso do bias
                errors += int(update != 0.0)         # Incrementa o contador de erros se houve atualização
            self.errors_.append(errors)              # Adiciona o contador de erros à lista de erros
        return self

    def net_input(self, X):
        # Calcula o input líquido como o produto escalar de X e os pesos
        return np.dot(X, self.weights)

    def predict(self, X):
        # Faz uma previsão da classe baseada no input líquido
        # Se net_input >= 0, retorna 1, senão retorna 0
        return np.where(self.net_input(X) >= 0.0, 1, 0)

# Criar o objeto Perceptron
perceptron = Perceptron(learning_rate=0.01, n_iterations=50)

# Treinar o Perceptron com o dataset fornecido
perceptron.fit(X, y)

# Imprimir os pesos finais após o treino
print("Pesos finais:", perceptron.weights)

# Usar o Perceptron treinado para fazer previsões no mesmo dataset (X)
predictions = perceptron.predict(X)

# Imprimir as previsões e comparar com os verdadeiros rótulos (y)
print("Predições:", predictions)
print("Verdadeiros rótulos:", y)

# Imprimir o número de erros em cada época para ver a melhora durante o treino
print("Número de erros em cada iteração:", perceptron.errors_)