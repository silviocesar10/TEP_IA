from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork([('DA', 'Treinamento'), 
                       ('DA', 'Financiamento'),
                       ('DA', 'Sucesso'),
                       ('Sucesso', 'Treinamento'),
                       ('Sucesso', 'Financiamento')])

# Definição das CPDs

# DA
cpd_da = TabularCPD(
    variable='DA',
    variable_card=3,
    values=[[0.3], [0.5], [0.2]]
)

# Treinamento
cpd_treinamento = TabularCPD(
    variable='Treinamento',
    variable_card=3,
    values=[
        [0.7, 0.5, 0.2], 
        [0.2, 0.3, 0.3],
        [0.1, 0.2, 0.5]
    ],
    evidence=['DA'],
    evidence_card=[3]
)

# Financiamento
cpd_financiamento = TabularCPD(
    variable='Financiamento',
    variable_card=3,
    values=[
        [0.8, 0.5, 0.2], 
        [0.15, 0.3, 0.4],
        [0.05, 0.2, 0.4]
    ],
    evidence=['DA'],
    evidence_card=[3]
)

# Sucesso
cpd_sucesso = TabularCPD(
    variable='Sucesso',
    variable_card=2,
    values=[
        [0.70, 0.65, 0.60, 0.60, 0.55, 0.50, 0.45, 0.40, 0.35, 0.60, 0.55, 0.50, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.45, 0.40, 0.35, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10],
        [0.25, 0.30, 0.30, 0.30, 0.30, 0.35, 0.35, 0.35, 0.40, 0.30, 0.35, 0.35, 0.35, 0.35, 0.40, 0.40, 0.45, 0.45, 0.40, 0.45, 0.45, 0.45, 0.50, 0.50, 0.50, 0.55, 0.55],
        [0.05, 0.05, 0.10, 0.10, 0.15, 0.15, 0.20, 0.25, 0.25, 0.10, 0.10, 0.15, 0.15, 0.20, 0.20, 0.25, 0.25, 0.30, 0.15, 0.15, 0.20, 0.20, 0.20, 0.25, 0.30, 0.30, 0.35]
    ],
    evidence=['DA', 'Financiamento', 'Treinamento'],
    evidence_card=[3, 3, 3]
)

# Adicionar CPDs ao modelo
model.add_cpds(cpd_da, cpd_treinamento, cpd_financiamento, cpd_sucesso)

# Verificar se o modelo é válido
assert model.check_model()