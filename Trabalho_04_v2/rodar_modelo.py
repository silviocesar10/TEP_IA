import os
import sys
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

def preprocess_image(image_path):
    # Carrega a imagem em escala de cinza, redimensiona e normaliza
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    return img.reshape(1, 28, 28, 1)  # Adiciona uma dimensão para corresponder à entrada do modelo

def classify_images(model, image_folder):
    correct_predictions = 0
    total_images = 0

    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        if os.path.isfile(image_path) and image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Pré-processa a imagem
            input_image = preprocess_image(image_path)

            # Realiza a predição usando o modelo
            prediction = model.predict(input_image)

            # Converte a saída da predição para uma classe (0 ou 1)
            predicted_class = int(round(prediction[0, 0]))

            # Obtém o rótulo verdadeiro a partir do nome do arquivo
            true_class = 0 if "cat" in filename.lower() else 1  # Assumindo que os gatos têm "cat" no nome do arquivo

            # Verifica se a previsão está correta
            if predicted_class == true_class:
                correct_predictions += 1

            total_images += 1

            # Imprime o resultado para cada imagem
            print(f"Image: {filename}, Predicted Class: {predicted_class} (0: Cat, 1: Dog), True Class: {true_class}")

    # Calcula e imprime a acurácia
    accuracy = correct_predictions / total_images
    print(f"\nAccuracy on {total_images} images: {accuracy:.2%}")

if __name__ == "__main__":
    # Verifica se o caminho do modelo foi fornecido como argumento de linha de comando
    if len(sys.argv) != 2:
        print("Uso: python rodar_modelo.py /pasta_com_imagens")
        sys.exit(1)

    # Carrega o modelo treinado
    model_path = "cat_dog_model.h5"  # Substitua pelo caminho real do seu modelo
    model = load_model(model_path)

    # Obtém o caminho da pasta de imagens a serem classificadas
    image_folder = sys.argv[1]

    # Realiza a classificação das imagens na pasta especificada
    classify_images(model, image_folder)
