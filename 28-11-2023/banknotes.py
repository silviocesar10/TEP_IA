import csv
import tensorflow as tf

from sklearn.model_selection import train_test_split

from grafico import PlotagemDePerdas

# Lê os dados do arquivo CSV
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append(
            {
                "evidence": [float(cell) for cell in row[:4]],
                "label": 1 if row[4] == "0" else 0,
            }
        )

# Separa os dados em conjuntos de treinamento e teste
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.2
)

# Cria o modelo de rede neural
model = tf.keras.models.Sequential()

# Adiciona uma camada de entrada com 4 unidades, com função de ativação relu
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

# Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Configure the model for training
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Crie uma instância do Callback
plotagem_de_perdas = PlotagemDePerdas()

# Treina o modelo com o Callback
model.fit(X_training, y_training, epochs=100, callbacks=[plotagem_de_perdas], verbose=False)

# Avalia o quão bem o modelo performou
model.evaluate(X_testing, y_testing, verbose=2)
