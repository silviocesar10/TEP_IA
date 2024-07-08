# 4. Faça um programa em Python que peça ao usuário para digitar uma frase qualquer. O programa deve verificar e mostrar quantas palavras a frase possui.
frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))