from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definição do modelo
model = BayesianNetwork([('N', 'C'), ('T', 'C')])

# Definição das CPDs
# Nublado(nublado, claro)
cpd_n = TabularCPD(variable='N', variable_card=2, values=[[0.5], [0.5]])

# Noticiário (possibilidade de chuva, tempo seco)
cpd_t = TabularCPD(variable='T', variable_card=2, values=[[0.5], [0.5]])

# Chuva (sim, não)
# sim, nublado, possibilidade = 0.1
# sim, nublado, tempo seco = 0.2
# sim, claro, possibilidade = 0.3
# sim, claro, tempo seco = 0.4
# não, nublado, possibilidade = 0.9
# não, nublado, tempo seco = 0.8
# não, claro, possibilidade = 0.7
# não, claro, tempo seco = 0.6
cpd_c = TabularCPD(variable='C', variable_card=2, 
                  values=[[0.1, 0.2, 0.3, 0.4],  # P(Chuva | Nublado , Noticiário)
                          [0.9, 0.8, 0.7, 0.6]],
                  evidence=['N', 'T'],
                  evidence_card=[2, 2])

model.add_cpds(cpd_n, cpd_t, cpd_c)

# Verificar se o modelo é consistente
assert model.check_model()

# Fazendo inferência
infer = VariableElimination(model)

# Vamos supor que está nublado, mas o noticiário mencionou tempo seco
result = infer.query(variables=['C'], evidence={'N': 1, 'T': 1})
print(result)
