from lark import Lark

GLC_ARITMETICA = """
    start: expr

    ?expr: term
        | expr "+" term -> add
        | expr "-" term -> sub

    ?term: factor
        | term "*" factor -> mul
        | term "/" factor -> div

    ?factor: "(" expr ")"
        | NUM

    NUM: /[0-9]/
    %import common.WS
    %ignore WS
"""

gramatica_aritmetica = Lark(GLC_ARITMETICA, start='expr', parser='lalr')

expressao_aritmetica = input("Expressão aritmética: ")
try:
    tree_aritmetica = gramatica_aritmetica.parse(expressao_aritmetica)
    print(tree_aritmetica.pretty())
except Exception as e:
    print("Erro ao analisar a expressão aritmética:", e)
