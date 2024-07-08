import numpy as np
from hmmlearn import hmm

# Definir os estados ocultos
states = ["Sol", "Chuva"]

# Definir as probabilidades iniciais
start_probs = np.array([0.6, 0.4])

# Definir as probabilidades de emissão
emission_probs = np.array([[0.8, 0.2],  # Sol -> GuardaChuva(Sim), Sol -> GuardaChuva(Não)
                           [0.1, 0.9]])  # Chuva -> GuardaChuva(Sim), Chuva -> GuardaChuva(Não)

# Definir as probabilidades de transição
trans_mat = np.array([[0.8, 0.2], [0.2, 0.8]])

# Sequência de observações
observacoes = [1, 0, 0, 0, 0]  # GuardaChuva(Não) nos primeiros 5 dias

# Converta observações para números e reshape para torná-lo bidimensional
X = np.array(observacoes).reshape(-1, 1)

# Configure o modelo HMM
model = hmm.MultinomialHMM(n_components=len(states), n_iter=50)
model.n_features = 1  # Apenas uma observação possível: 0 ou 1 (GuardaChuva Sim ou Não)
model.startprob_ = start_probs
model.transmat_ = trans_mat
model.emissionprob_ = emission_probs

# Ajuste o modelo com os dados
model.fit(X)

# Execute o algoritmo de Viterbi para encontrar a sequência mais provável de estados ocultos
sequencia_oculta = model.predict(X)

# Decodifique a sequência de estados ocultos
resultado = [states[estado] for estado in sequencia_oculta]

# Imprima o resultado
for dia, clima in enumerate(resultado, start=1):
    print(f'Dia {dia}: {clima}')
