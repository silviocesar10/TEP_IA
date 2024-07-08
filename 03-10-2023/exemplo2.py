from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Criar o modelo
model = BayesianNetwork([('Chuva', 'Manutenção'), ('Chuva', 'Trem'), ('Manutenção', 'Trem'), ('Trem', 'Compromisso')])

# CPD: Conditional Probability Distribution
# Definir CPD para Chuva (C)
cpd_c = TabularCPD(
    variable='Chuva',
    variable_card=3,
    values=[[0.7], [0.2], [0.1]]
)

# Definir CPD para Manutenção (M) baseada em Chuva (C)
cpd_m = TabularCPD(
    variable='Manutenção',
    variable_card=2,
    values=[[0.2, 0.4, 0.7], [0.8, 0.6, 0.3]],
    evidence=['Chuva'],
    evidence_card=[3]
)

# Definir CPD para Trem (T) baseada em Chuva (C) e Manutenção (M)
cpd_t = TabularCPD(
    variable='Trem',
    variable_card=2,
    values=[
        [0.8, 0.9, 0.6, 0.7, 0.4, 0.5],
        [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]
    ],
    evidence=['Chuva', 'Manutenção'],
    evidence_card=[3, 2]
)

# Definir CPD para Compromisso (A) baseada em Trem (T)
cpd_a = TabularCPD(
    variable='Compromisso',
    variable_card=2,
    values=[[0.9, 0.6], [0.1, 0.4]],
    evidence=['Trem'],
    evidence_card=[2]
)

# Adicionar CPDs ao modelo
model.add_cpds(cpd_c, cpd_m, cpd_t, cpd_a)

# Verificar se o modelo é válido
assert model.check_model()
print("Modelo criado e CPDs adicionadas com sucesso!")


infer = VariableElimination(model)

# Inferência para cada variável dada a observação de que T está "atrasado"
# print("Probabilidade para Chuva (C) dado T='atrasado':")
# print(infer.query(variables=['Chuva'], evidence={'Trem': 1}))

# print("\nProbabilidade para Manutenção (M) dado T='atrasado':")
# print(infer.query(variables=['Manutenção'], evidence={'Trem': 1}))

# print("\nProbabilidade para Compromisso (A) dado T='atrasado':")
# print(infer.query(variables=['Compromisso'], evidence={'Trem': 1}))

# Mapeamento de rótulos
mapa_rotulos = {
    'Chuva': {0: 'nula', 1: 'leve', 2: 'pesada'},
    'Manutenção': {0: 'sim', 1: 'não'},
    'Trem': {0: 'pontual', 1: 'atrasado'},
    'Compromisso': {0: 'atendido', 1: 'perdido'}
}

# Após fazer a inferência, você pode traduzir o resultado para rótulos
infer = VariableElimination(model)

#print("Se Trem='atrasado', então:")

# Probabilidade para Chuva dado Trem='atrasado'
#result_c = infer.query(variables=['Chuva'], evidence={'Trem': 1})
#for index, prob in enumerate(result_c.values):
 #   print(f"Probabilidade de Chuva ser '{mapa_rotulos['Chuva'][index]}': {prob:.2f}")

# Probabilidade para Manutenção dado Trem='atrasado'
#result_m = infer.query(variables=['Manutenção'], evidence={'Trem': 1})
#for index, prob in enumerate(result_m.values):
 #   print(f"Probabilidade de Manutenção ser '{mapa_rotulos['Manutenção'][index]}': {prob:.2f}")

# Probabilidade para Manutenção dado Trem='atrasado'
#result_a = infer.query(variables=['Compromisso'], evidence={'Trem': 1})
#for index, prob in enumerate(result_a.values):
 #   print(f"Probabilidade de Compromisso ser '{mapa_rotulos['Compromisso'][index]}': {prob:.2f}")

print("Se Trem='atrasado', Chuva='leve' e Manutenção='sim'")
# Probabilidade para Compromisso dado Trem='atrasado', Chuva='leve', Manutenção='sim'
result_a = infer.query(variables=['Compromisso'], evidence={'Trem': 1,'Chuva': 1,'Manutenção': 0})
for index, prob in enumerate(result_a.values):
    print(f"Probabilidade de Compromisso ser '{mapa_rotulos['Compromisso'][index]}': {prob:.2f}")

print("Se Trem='pontual', Chuva='leve' e Manutenção='sim'")
# Probabilidade para Compromisso dado Trem='atrasado', Chuva='leve', Manutenção='sim'
result_a = infer.query(variables=['Compromisso'], evidence={'Trem': 0,'Chuva': 2,'Manutenção': 0})
for index, prob in enumerate(result_a.values):
    print(f"Probabilidade de Compromisso ser '{mapa_rotulos['Compromisso'][index]}': {prob:.2f}")

print("Se Chuva='leve' e Manutenção='sim'")
# Probabilidade para Compromisso dado Trem='atrasado', Chuva='leve', Manutenção='sim'
result_a = infer.query(variables=['Compromisso'], evidence={'Chuva': 2,'Manutenção': 0})
for index, prob in enumerate(result_a.values):
    print(f"Probabilidade de Compromisso ser '{mapa_rotulos['Compromisso'][index]}': {prob:.2f}")