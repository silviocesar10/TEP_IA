import cv2
import numpy as np
import tensorflow as tf
import os
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

# Carrega as imagens de teste
test_dog_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/test/dog"
x_test_dog, y_test_dog = load_images_and_labels(test_dog_folder, 1)  # 1 representa cachorros

# Carrega as imagens de teste
test_cat_folder = "/home/silvio/Documentos/2023-2/TEP_IA/Trabalho_04/test/cat"
x_test_cat, y_test_cat = load_images_and_labels(test_cat_folder, 0)  # 0 representa gatos

# Concatena os dados de teste
x_test_data = np.concatenate((x_test_cat, x_test_dog), axis=0)
y_test_data = np.concatenate((y_test_cat, y_test_dog), axis=0)

# Carrega o modelo treinado
model = tf.keras.models.load_model("cat_dog_model.h5")

# Avaliação do modelo no conjunto de teste
test_accuracy = model.evaluate(x_test_data.reshape(-1, 28, 28, 1), y_test_data, verbose=2)[1]
print(f"Accuracy on test data: {test_accuracy}")
