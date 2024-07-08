# 3. Faça um programa em Python que imprima a tabuada de multiplicação de 1 a 10 de um número inteiro digitado pelo usuário. O número digitado pelo usuário também deve estar entre 1 e 10.
n = int(input("Digite um numero entre 1 a 10: "))
if (n > 10 or n < 0) :
    print("o numero digitado nao esta entre 1 a 10")
else:
    print(f"tabuada de 10 do numero {n}:")
    i = 0
    while( i < 11):
        print(f"{n} x {i}: {n*i}")
        i = i + 1
