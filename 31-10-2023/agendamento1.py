from constraint import *

problem = Problem()

# adiciona as variáveis e os domínios
problem.addVariables(
    variables=["A", "B", "C", "D", "E", "F", "G"],
    domain=["Segunda", "Terca", "Quarta"]
)

# adiciona as restrições
RESTRICOES = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

# para cada restrição, adiciona uma função de restrição
# indicando que x deve ser diferente de y para as variáveis x e y
for x, y in RESTRICOES:
    problem.addConstraint(lambda x, y: x != y, [x, y])

# Solve problem
for solution in problem.getSolutions():
    print(solution)
