# 4.	Classe Pessoa:
#
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# •	envelhecer(): Aumenta a idade da pessoa em um ano.
# •	Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# •	Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# •	Perder_peso(quilos): Diminui o peso da pessoa em quilos.
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.altura = 0.0
        self.peso = 0.0
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_idade(self, idade):
        self.idade = idade
    
    def get_idade(self):
        return self.idade
    
    def set_altura(self, altura):
        self.altura = altura
    
    def get_altura(self):
        return self.altura
    
    def set_peso(self, peso):
        self.peso = peso
    
    def get_peso(self):
        return self.peso
    
    def envelhecer(self):
        self.idade += 1
        return print(self.idade)
    
    def crescer(self, cm):
        if self.idade < 21:
            self.altura += cm
        return print(f"A altura agora é de {self.altura:.2f}")
    
    def ganhar_peso(self, quantidade):
        self.peso += quantidade
        return print(f"{self.peso:.1f}")
    
    def perder_peso(self, quantidade):
        self.peso -= quantidade
        return print(f"{self.peso:.1f}")
    
pessoa1 = Pessoa()
pessoa1.set_nome("Emanuel")
print(pessoa1.get_nome())
pessoa1.set_idade(22)
print(pessoa1.get_idade())
pessoa1.set_altura(183)
print(pessoa1.get_altura())
pessoa1.set_peso(60.9)
print(pessoa1.get_peso())
pessoa1.envelhecer()
pessoa1.envelhecer()
pessoa1.envelhecer()
pessoa1.ganhar_peso(5)
pessoa1.perder_peso(3)
print("-" * 30)
pessoa2 = Pessoa()
pessoa2.set_nome("Davi")
print(pessoa2.get_nome())
pessoa2.set_idade(16)
print(pessoa2.get_idade())
pessoa2.set_altura(180)
print(pessoa2.get_altura())
pessoa2.set_peso(63)
print(pessoa2.get_peso())
pessoa2.crescer(0.05)
pessoa2.crescer(0.05)
pessoa2.ganhar_peso(5)
pessoa2.perder_peso(1.5)

# 4.	Classe Pessoa:
#
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# •	envelhecer(): Aumenta a idade da pessoa em um ano.
# •	Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# •	Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# •	Perder_peso(quilos): Diminui o peso da pessoa em quilos.

# class Pessoa:

#     def _init_(self):
#         self.nome = ""
#         self.idade = 0
#         self.altura = 0.0
#         self.peso = 0.0

#     def getNome(self):
#         return self.nome

#     def setNome(self, nome):
#         self.nome = nome

#     def getIdade(self):
#         return self.idade

#     def setIdade(self, idade):
#         if idade < 0:
#             print("Idade invalida")
#         else:
#             self.idade = idade

#     def getPeso(self):
#         return self.peso

#     def setPeso(self, peso):
#         if peso < 0:
#             print("Peso invalido")
#         else:
#             self.peso = peso

#     def getAltura(self):
#         return self.altura

#     def setAltura(self, altura):
#         if altura < 0:
#             print("Altura invalida")
#         else:
#             self.altura = altura

#     def envelhecer(self):
#         self.idade += 1

#     def crescer(self, centimetros):
#         if self.idade >= 21:
#             print("Maior ou igual a 21 anos")
#         else:
#             if centimetros < 0:
#                 print("Centimetros invalidos")
#             else:
#                 self.altura += centimetros

#     def ganharPeso(self, quilos):
#         if quilos < 0:
#             print("Quantidade de quilos invalida")
#         else:
#             self.peso += quilos

#     def perderPeso(self, quilos):
#         if quilos < 0:
#             print("Quantidade de quilos invalida")
#         else:
#             if quilos > self.peso:
#                 print("Nao pode perder mais quilos do que o peso atual")
#             else:
#                 self.peso -= quilos


# pessoa = Pessoa()
# pessoa.setIdade(10)
# pessoa.envelhecer()
# print(pessoa.getIdade())
# pessoa.setAltura(100)
# pessoa.crescer(1)
# print(pessoa.getAltura())
# pessoa.setPeso(80)
# pessoa.ganharPeso(5)
# print(pessoa.getPeso())
# pessoa.perderPeso(10)
# print(pessoa.getPeso())