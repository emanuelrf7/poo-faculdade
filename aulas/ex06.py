# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.
class Funcionario():
    def __init__(self):
        self.nome = ""
        self.cargo = ""
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
funcionario.set_cargo("Estagiário Externo")
print(funcionario.get_cargo())
funcionario.set_salario(700)
print(funcionario.get_salario())
funcionario.set_departamento("QA")
print(funcionario.get_departamento())
funcionario.receber_aumento(175)
funcionario.mudar_departamento("Estagiário Interno")
funcionario.exibir_dados()
