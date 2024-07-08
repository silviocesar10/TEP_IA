import sys
import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Função para carregar as imagens e rótulos
def load_images_and_labels(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28, 28))
        img = img / 255.0
        images.append(img)
        labels.append(label)
    return np.array(images), np.array(labels)

# Carrega as imagens de gatos e cachorros
cat_folder = "imgs/cats"
dog_folder = "imgs/dogs"
x_cats, y_cats = load_images_and_labels(cat_folder, 0)
x_dogs, y_dogs = load_images_and_labels(dog_folder, 1)

# Concatena e embaralha os dados
x_data = np.concatenate((x_cats, x_dogs), axis=0)
y_data = np.concatenate((y_cats, y_dogs), axis=0)
x_data, y_data = shuffle(x_data, y_data, random_state=42)

# Divisão dos dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.20, random_state=42)

# Data augmentation
data_gen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Modelo com camadas adicionais e regularização
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilação do modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinamento do modelo com data augmentation
model.fit(data_gen.flow(x_train.reshape(-1, 28, 28, 1), y_train, batch_size=32), epochs=20)

# Avaliação do modelo
accuracy = model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test, verbose=2)[1]
print(f"Accuracy on test data: {accuracy}")

# Salvamento do modelo
model.save("cat_dog_model.h5")
