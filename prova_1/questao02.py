# 2. Faça um programa em Python que verifique se um número inteiro digitado pelo usuário é divisível por outro número inteiro digitado pelo usuário ou não.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
if(n1 % n2 != 0):
    print(f"{n1} nao e divisel por {n2}")
else:
    print(f"{n1} e divisel por {n2}")