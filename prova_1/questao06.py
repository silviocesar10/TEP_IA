# 6. Faça um programa em Python que tenha uma função chamada "aplicar_formula" que possui dois parâmetros: "formula", que é uma função; e "valor", que é um inteiro. No corpo da função "aplicar_formula", você deve chamar a função "formula" passando "valor" como argumento. Em seguida, faça uma chamada para "aplicar_formula" passando como primeiro argumento uma função lambda que dobre o valor de um parâmetro "x", e, como segundo argumento, o valor 10.
def aplicar_formula(formula, valor):
    return formula(valor)
               
res=aplicar_formula(lambda x: x * 2, 10)

print(res)