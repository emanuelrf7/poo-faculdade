# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.
class Cargo:
    def __init__(self, cargo):
        self.set_cargo(cargo)
    

    def set_cargo(self, cargo):
        self.cargo = cargo


    def get_cargo(self):
        return self.cargo

class Funcionario():
    def __init__(self):
        self.nome = ""
        self.cargo = None
        self.salario = 0.0
        self.departamento = ""
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    def get_cargo(self):
        return self.cargo
    
    def set_salario(self, salario):
        self.salario = salario
    
    def get_salario(self):
        return self.salario
    
    def set_departamento(self, departamento):
        self.departamento = departamento
    
    def get_departamento(self):
        return self.departamento
    
    def receber_aumento(self, percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento
        return print(f"O seu salário com {percentual}% de aumento é {self.salario}")
    
    def mudar_departamento(self, novo_departamento):
        self.departamento = novo_departamento
        return print(f"O departamento foi alterado para {self.departamento}")
    
    def exibir_dados(self):
        print("-" * 50)
        print(f"FUNCIONÁRIO {self.get_nome()}".center(50))
        print("-" * 50)
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")
        print(f"Departamento: {self.departamento}")
        print("-" * 50)
    
funcionario = Funcionario()
funcionario.set_nome("Emanuel")
print(funcionario.get_nome())
funcionario.set_cargo("Estagiário")
print(funcionario.get_cargo())
funcionario.set_salario(700)
print(funcionario.get_salario())
funcionario.set_departamento("QA")
print(funcionario.get_departamento())
funcionario.receber_aumento(175)
funcionario.mudar_departamento("Dev")
funcionario.exibir_dados()

# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.

# class Funcionario:

#     def _init_(self):
#         self.nome = ""
#         self.cargo = ""
#         self.salario = 0.0
#         self.departamento = ""

#     def getNome(self):
#         return self.nome

#     def setNome(self, nome):
#         self.nome = nome

#     def getCargo(self):
#         return self.cargo

#     def setCargo(self, cargo):
#         self.cargo = cargo

#     def getSalario(self):
#         return self.salario

#     def setSalario(self, salario):
#         if salario < 0:
#             print("Salario invalido")
#         else:
#             self.salario = salario

#     def getDepartamento(self):
#         return self.departamento

#     def setDepartamento(self, departamento):
#         self.departamento = departamento

#     def receberAumento(self, percentual):
#         if percentual < 0:
#             print("Percentual invalido")
#         else:
#             self.salario = self.salario * (1 + (percentual / 100))

#     def mudar_departamento(self, departamento):
#         self.setDepartamento(departamento)

#     def exibirDados(self):
#         print(self.nome, self.departamento, self.salario, self.cargo)

# funcionario = Funcionario()
# funcionario.setSalario(1000)
# funcionario.receberAumento(10)
# print(funcionario.getSalario())
# funcionario.setDepartamento("TI")
# print(funcionario.getDepartamento())
# funcionario.mudar_departamento("RH")
# print(funcionario.getDepartamento())
# funcionario.setNome("Ana")
# funcionario.setCargo("Analista")
# funcionario.exibirDados()