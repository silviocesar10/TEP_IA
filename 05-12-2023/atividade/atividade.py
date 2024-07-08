import nltk

GLC_ARITMETICA = """
E -> E '+' T | E '-' T | T
T -> T '*' F | T '/' F | F
F -> '(' E ')' | NUM
NUM -> NUM DIGIT | DIGIT
DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""
def parse(sentence):
    sentence = sentence.replace(" ", "")
    return " ".join(sentence)

entrada_aritmetica = "\n".join([GLC_ARITMETICA])
gramatica_aritmetica = nltk.CFG.fromstring(entrada_aritmetica)
parser_aritmetico = nltk.EarleyChartParser(gramatica_aritmetica)

expressao_aritmetica = input("Expressão aritmética: ")
expressao_aritmetica = parse(sentence=expressao_aritmetica)
try:
    for tree_aritmetica in parser_aritmetico.parse(expressao_aritmetica):
        tree_aritmetica.pretty_print()
except ValueError:
    print("Nenhuma árvore de análise sintática possível.")
