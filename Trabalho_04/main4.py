import sys
import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle  # Add this line for the shuffle function
from tensorflow.keras.regularizers import l2



# Função para carregar as imagens e rótulos
def load_images_and_labels(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Carrega a imagem em escala de cinza
        img = cv2.resize(img, (28, 28))  # Redimensiona para 28x28 pixels (como no exemplo)
        img = img / 255.0  # Normaliza os valores dos pixels para o intervalo [0, 1]
        images.append(img)
        labels.append(label)
    return np.array(images), np.array(labels)

# Carrega as imagens de gatos
cat_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/imgs/cats"
x_cats, y_cats = load_images_and_labels(cat_folder, 0)  # 0 representa gatos

# Carrega as imagens de cachorros
dog_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/imgs/dogs"
x_dogs, y_dogs = load_images_and_labels(dog_folder, 1)  # 1 representa cachorros

# Carrega as imagens de teste
test_dog_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/test/dog"
x_test_dog, y_test_dog = load_images_and_labels(test_dog_folder, 1)  # 1 representa cachorros

# Carrega as imagens de teste
test_cat_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/test/cat"
x_test_cat, y_test_cat = load_images_and_labels(test_cat_folder, 0)  # 1 representa cachorros

# Concatena os dados de gatos e cachorros
x_data = np.concatenate((x_cats, x_dogs), axis=0)
y_data = np.concatenate((y_cats, y_dogs), axis=0)

y_test = np.concatenate((y_test_cat, y_test_dog), axis=0)
x_test = np.concatenate((x_test_cat, x_test_dog), axis=0)


#x_data, y_data = shuffle(x_data, y_data, random_state=42)
x_data, y_data = shuffle(x_data, y_data, random_state=42)



# Divisão dos dados em treinamento e teste
#x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.20, random_state=42)

#x_train 
# Adaptação do modelo para lidar com imagens em escala de cinza (1 canal)
#model = tf.keras.models.Sequential([
#    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
#    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
#    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    #tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    #tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
#    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
#    tf.keras.layers.Flatten(),
#    tf.keras.layers.Dense(144, activation="relu"),
#    tf.keras.layers.Dense(64, activation="relu"),
#    tf.keras.layers.Dense(64, activation="relu"),
#    tf.keras.layers.Dense(64, activation="relu"),
    #tf.keras.layers.Dense(144, activation="relu"),
    #tf.keras.layers.Dropout(0.2),
#    tf.keras.layers.GaussianDropout(0.2),
#    tf.keras.layers.Dense(1, activation="sigmoid")  # Alteração para uma única unidade de saída (0 ou 1)
    #tf.keras.layers.Dense(1, activation="softmax")
#])

# Adaptação do modelo para lidar com imagens em escala de cinza (1 canal)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(200, activation="relu", kernel_regularizer=l2(0.003)),  # Adição de regularização L2
    tf.keras.layers.Dense(100, activation="relu", kernel_regularizer=l2(0.003)),  # Adição de regularização L2
    tf.keras.layers.GaussianDropout(0.2),
    #tf.keras.layers.Dense(64, activation="relu", kernel_regularizer=l2(0.003)),  # Adição de regularização L2
    #tf.keras.layers.Dense(64, activation="relu", kernel_regularizer=l2(0.003)),  # Adição de regularização L2
    tf.keras.layers.GaussianDropout(0.2),
    tf.keras.layers.Dense(32, activation="relu", kernel_regularizer=l2(0.003)),  # Adição de regularização L2
    tf.keras.layers.GaussianDropout(0.2),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


# Compilação e treinamento do modelo
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
#model.fit(x_train.reshape(-1, 28, 28, 1), y_train, epochs=20)
model.fit(x_data.reshape(-1, 28, 28, 1), y_data, epochs=50)
# Ajuste o gerador aos dados

# Avaliação do modelo
accuracy = model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test, verbose=2)[1]
print(f"Accuracy on test data: {accuracy}")

# Salvamento do modelo
model_filename = "cat_dog_model.h5"
model.save(model_filename, save_format="h5", overwrite=True, include_optimizer=True)
print(f"Model saved to {model_filename}.")
