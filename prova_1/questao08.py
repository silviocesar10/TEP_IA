# 8. Faça um programa em Python que tenha uma classe para representar uma pessoa, sendo que cada pessoa deve ter CPF, nome, renda bruta e data de nascimento. A classe também deve ter um método para mostrar a idade da pessoa em anos. Use as convenções da linguagem.
from datetime import date
class Pessoa:
    def __init__(self, nome, idade, renda_bruta, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.renda_bruta = renda_bruta
        self.data_nascimento = data_nascimento
    
    def exibir_idade(self):
        ano = date.today()
        n = ano.year  - int(self.data_nascimento.split('/')[2])
        print(n)

silvio = Pessoa("silvio", 24,10, "29/03/1999")
silvio.exibir_idade()