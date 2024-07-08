import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import Callback


class PlotagemDePerdas(Callback):
    def on_train_begin(self, logs=None):
        self.epocas = 0
        self.figura, self.grafico = plt.subplots()
        self.perdas = []

    def on_epoch_end(self, epoch, logs=None):
        # atualiza o gráfico com os novos dados
        self.perdas.append(logs["loss"])
        self.epocas += 1
        self.grafico.clear()
        self.grafico.plot(range(self.epocas), self.perdas, label="Training Loss")
        self.grafico.set_xlabel("Épocas")
        self.grafico.set_ylabel("Perda (Loss)")
        self.grafico.set_title("Evolução da Perda de Treinamento")
        self.grafico.legend()
        # exibe os pesos e os viéses de cada camada
        #for layer in self.model.layers:
         #   weights, biases = layer.get_weights()
          #  print(f"Pesos da Camada {layer.name}: {weights}")
           # print(f"Viéses da Camada {layer.name}: {biases}")

        plt.pause(0.1)

    def on_train_end(self, logs=None):
        plt.show()
