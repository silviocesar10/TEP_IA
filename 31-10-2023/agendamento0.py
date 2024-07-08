"""
Busca com Backtracking sem nenhuma heurística ou inferência.
"""

VARIAVEIS = ["A", "B", "C", "D", "E", "F", "G"]
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
DOMINIO = ["Segunda", "Terca", "Quarta"]


def backtrack(solucao):
    """Executa a busca por backtracking até que a solução tenha todas as variáveis."""

    # verifica se todas as variáveis possuem um valor
    if len(solucao) == len(VARIAVEIS):
        return solucao

    # seleciona uma nova variável sem atribuição de valor
    variavel = selecionar_variavel_sem_valor(solucao)
    # para cada valor do domínio
    for valor in DOMINIO:
        # cria uma nova solução como uma cópia da solução atual
        nova_solucao = solucao.copy()
        # atribui à variável um valor do domínio
        nova_solucao[variavel] = valor
        # verifica se a nova solução é consistente
        if solucao_consistente(nova_solucao):
            # se for, executa o backtracking recursivamente com a nova solução
            resultado = backtrack(nova_solucao)
            # se o resultado for diferente de None, retorna o resultado
            if resultado is not None:
                return resultado
    # se percorreu todo o domínio e não encontrou uma solução consistente, retorna None
    return None


def selecionar_variavel_sem_valor(solucao):
    """Escolhe uma variável sem valor atribuído, em ordem."""
    for variavel in VARIAVEIS:
        if variavel not in solucao:
            return variavel
    return None


def solucao_consistente(solucao):
    """Verifica se uma solução é consistente."""
    for (x, y) in RESTRICOES:

        # considera somente arcos onde ambos possuem valor atribuído
        if x not in solucao or y not in solucao:
            continue

        # se ambas possuem o mesmo valor, não é consistente
        if solucao[x] == solucao[y]:
            return False

    # se não encontrou nada inconsistente, retorna True
    return True


solucao = backtrack(dict())
print(solucao)
