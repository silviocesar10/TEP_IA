# 10. Faça um programa em Python que gere uma lista de 100 números inteiros aleatórios. Ao fim, o programa deve mostrar os números em ordem e sem repetições.
import random
num = []
while(len(num) <= 100):
    num.append(random.randrange(1, 500, 1))

num.sort()
print(num)