from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Criar o modelo
model = BayesianNetwork([
    ('Clima', 'Autor'),
    ('Clima', 'Marketing'),
    ('Clima', 'Critica'),
    ('Autor', 'Critica'),
    ('Critica', 'Lançamento'),
    ('Marketing', 'Lançamento')])

#Definição das CPDs

#Clima
cpd_clima = TabularCPD(
    variable='Clima',
    variable_card=3,
    values=[[0.6], [0.2], [0.2]]
)

#Autor condicionado ao Clima
cpd_autor = TabularCPD(
    variable='Autor',
    variable_card=2, 
    values=[[0.9, 0.4, 0.8],
            [0.1, 0.6, 0.2]],
    evidence=['Clima'],
    evidence_card=[3] #depende de Clima 3 possibilidades ?
)

#Marketing condicionado ao Clima
cpd_marketing = TabularCPD(
    variable='Marketing',
    variable_card=2,
    values=[[0.8, 0.3, 0.7],
            [0.2, 0.7, 0.3]],
    evidence=['Clima'],
    evidence_card=[3] #depende de Clima 3 possibilidades ?
)

#Critica condicionada a Clima e Autor
cpd_critica = TabularCPD(
    variable='Critica',
    variable_card=2,
    values=[[0.9, 0.7, 0.8, 0.6, 0.85, 0.75],
            [0.1, 0.3, 0.2, 0.4, 0.15, 0.25]],
    evidence=['Clima', 'Autor'],
    evidence_card=[3, 2] #depende de Clima 3 possibilidades e Autor 2 possibilidades ?
)

#Lançamento condicionado a Critica  e Marketing
cpd_lancamento = TabularCPD(
    variable='Lançamento',
    variable_card=2,
    values=[[0.95, 0.85, 0.7, 0.5],
            [0.05, 0.15, 0.3, 0.5]],
    evidence=['Critica', 'Marketing'],
    evidence_card=[2, 2] #depende de Critica 2 possibilidades e Marketing 2 possibilidades ?
)

model.add_cpds(cpd_clima, cpd_autor, cpd_marketing, cpd_critica, cpd_lancamento)

mapa_rotulos = {
    'Clima': {0: 'ensolarado', 1: 'chuvoso', 2: 'nublado'},
    'Autor': {0: 'disponivel', 1: 'indisponivel'},
    'Marketing': {0: 'promoção', 1: 'sem promoção'},
    'Critica': {0: 'positiva', 1: 'negativa'},
    'Lançamento': {0: 'sucesso', 1: 'fracasso'},
}

# Após fazer a inferência, você pode traduzir o resultado para rótulos
infer = VariableElimination(model)

print("Se Clima='chuvoso'")
# Probabilidade fracasso ou sucesso lançamento com Clima='chuvoso'
result_a = infer.query(variables=['Lançamento'], evidence={'Clima': 1,})
for index, prob in enumerate(result_a.values):
    print(f"Probabilidade do Lançamento ser '{mapa_rotulos['Lançamento'][index]}': {prob:.2f}")