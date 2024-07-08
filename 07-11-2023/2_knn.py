import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Carregar os dados do arquivo CSV
df = pd.read_csv('2_dataset.csv')

# Vamos codificar as classes como números para facilitar o uso no KNN
le = LabelEncoder()
df['Classe'] = le.fit_transform(df['Classe'])

# Separar os dados em variáveis independentes (X) e variável alvo (y)
X = df[['Pressao', 'Glicose']]
y = df['Classe']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar o classificador K-NN com k=3, por exemplo
knn = KNeighborsClassifier(n_neighbors=3)

# Treinar o modelo
knn.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo K-NN: {accuracy:.2f}")

# Validação com nova amostra
# Suponha que você tenha novas amostras:
novas_amostras = [[40, 80], [130, 120]]
# Fazer previsões para novas amostras
novas_predicoes = knn.predict(novas_amostras)
novas_predicoes = le.inverse_transform(novas_predicoes)  # Transformar de volta para as etiquetas originais

# Imprimir as previsões para as novas amostras
for i, amostra in enumerate(novas_amostras):
    print(f"A nova amostra {amostra} foi classificada como '{novas_predicoes[i]}'")