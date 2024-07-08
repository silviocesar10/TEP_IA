from constraint import Problem 
 
# Criando o problema 
problema = Problem() 
 
# Definindo as variáveis e seus domínios 
palestrantes = ["A", "B", "C", "D", "E"] 
salas = [1, 2, 3] 
problema.addVariables(palestrantes, salas) 
 
# Adicionando as restrições 
problema.addConstraint(lambda a: a != 1, ["A"]) 
problema.addConstraint(lambda b, d: b != d, ["B", "D"]) 
problema.addConstraint(lambda c, d: c != d, ["C", "D"]) 
problema.addConstraint(lambda e: e == 3, ["E"]) 
 
solucoes = problema.getSolutions() 
for s in solucoes:
    print(s)