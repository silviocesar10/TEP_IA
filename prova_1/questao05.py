# 5. Faça um programa em Python que leia nomes e notas (0 a 10) de alunos, armazenando tudo em um dicionário em que o nome do aluno é a chave e a nota é o valor. O programa deve parar a leitura quando o nome digitado for vazio. Em seguida, use "dict comprehension" para criar um dicionário com os alunos com nota igual ou superior a 7.
nomes = []
notas = []

while(True):
    nm = input("Digite o nome do aluno: ")
    if(len(nm) <= 0):
        break
    else:
        nomes.append(nm)
    
    nt = input("Digite a nota do aluno: ")
    notas.append(nt)

d = {nme: nta for nme,nta in nomes,notas if nt >= 7 else print("nao adicionado")}
print(d)