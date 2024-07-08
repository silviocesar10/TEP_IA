# 1. Faça um programa em Python que peça ao usuário para digitar o preço de uma mercadoria, o percentual de desconto e de imposto. Ao fim, calcule e mostre o preço final da mercadoria.
# Preço Final = Preço Base + (Preço Base * (%Imposto / 100)) - (Preço Base * (%Desconto / 100))

preco = int(input("Digite o preco base da mercadoria: "))
imposto = int(input("Digite o percentual de imposto incidente: "))
desconto = int(input("Digite o percentual de desconto incidente: "))
preco_final = preco + (preco * (imposto / 100)) - (preco * (desconto / 100))
print(preco_final)

