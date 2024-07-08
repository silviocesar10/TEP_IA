#pip install hmmlearn
import numpy as np

# Definir as probabilidades iniciais
prob_inicial = np.array([0.5, 0.5])  # Inicialmente, a chance é igual para Sol e Chuva

# Definir as probabilidades de transição
prob_transicao = np.array([[0.7, 0.3],  # Sol -> Sol, Sol -> Chuva
                           [0.4, 0.6]])  # Chuva -> Sol, Chuva -> Chuva

# Definir as probabilidades de emissão (observações)
prob_emissao = np.array([[0.8, 0.2],  # Sol -> GuardaChuva(Sim), Sol -> GuardaChuva(Não)
                        [0.1, 0.9]])  # Chuva -> GuardaChuva(Sim), Chuva -> GuardaChuva(Não)

# Sequência de observações
observacoes = [1, 0, 0, 0, 0]  # GuardaChuva(Não) nos primeiros 5 dias

# Função para realizar a simulação do HMM
def simular_hmm(observacoes, prob_inicial, prob_transicao, prob_emissao):
    sequencia_oculta = []
    estado_atual = np.random.choice(2, p=prob_inicial)
    
    for observacao in observacoes:
        sequencia_oculta.append(estado_atual)
        estado_atual = np.random.choice(2, p=prob_transicao[estado_atual])
    
    return sequencia_oculta

# Simular o HMM com base nas observações
sequencia_oculta = simular_hmm(observacoes, prob_inicial, prob_transicao, prob_emissao)

# Decodificar a sequência de estados ocultos
resultado = ['Sol' if estado == 0 else 'Chuva' for estado in sequencia_oculta]

# Imprimir o resultado
for dia, clima in enumerate(resultado, start=1):
    print(f'Dia {dia}: {clima}')
