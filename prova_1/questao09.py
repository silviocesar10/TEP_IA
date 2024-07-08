# 9. Faça um programa em Python que receba do usuário o nome de um arquivo e que tente ler esse arquivo. Caso o arquivo não exista, o programa deve criar um arquivo com este nome e com o conteúdo "NOVO ARQUIVO". Esse código deve possuir tratamento de exceções.
a = input("Digite o nome do arquivo: ")
try:
    f = open(a, 'r')
except FileNotFoundError:
    f = open(a, "a")
    f.write("NOVO ARQUIVO")