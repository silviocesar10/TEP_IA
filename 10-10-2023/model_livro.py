from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork([('Clima', 'Autor'), 
                       ('Clima', 'Marketing'),
                       ('Clima', 'Critica'),
                       ('Autor', 'Critica'),
                       ('Critica', 'Lancamento'),
                       ('Marketing', 'Lancamento')])

# Definição das CPDs

# Clima
cpd_clima = TabularCPD(
    variable='Clima',
    variable_card=3,
    values=[[0.6], [0.2], [0.2]]
)

# Autor
cpd_autor = TabularCPD(
    variable='Autor',
    variable_card=2,
    values=[
        [0.9, 0.4, 0.8], 
        [0.1, 0.6, 0.2]],
    evidence=['Clima'],
    evidence_card=[3]
)

# Marketing
cpd_marketing = TabularCPD(
    variable='Marketing',
    variable_card=2,
    values=[
        [0.8, 0.3, 0.7], 
        [0.2, 0.7, 0.3]],
    evidence=['Clima'],
    evidence_card=[3]
)

# Critica
cpd_critica = TabularCPD(
    variable='Critica',
    variable_card=2,
    values=[
        [0.9, 0.7, 0.8, 0.6, 0.85, 0.75],
        [0.1, 0.3, 0.2, 0.4, 0.15, 0.25]
    ],
    evidence=['Clima', 'Autor'],
    evidence_card=[3, 2]
)

# Lancamento
cpd_lancamento = TabularCPD(
    variable='Lancamento',
    variable_card=2,
    values=[
        [0.95, 0.85, 0.7, 0.5], 
        [0.05, 0.15, 0.3, 0.5]
    ],
    evidence=['Critica', 'Marketing'],
    evidence_card=[2, 2]
)

# Adicionar CPDs ao modelo
model.add_cpds(cpd_clima, cpd_autor, cpd_marketing, cpd_critica, cpd_lancamento)

# Verificar se o modelo é válido
assert model.check_model()