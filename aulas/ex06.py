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
        if cargo == "":
            print("Cargo inválido")
        self.cargo = cargo


    def get_cargo(self):
        return self.cargo


class Departamento():
    def __init__(self):
        self.cargo = ""
    

    def set_departamento(self, cargo):
        self.cargo = cargo
    

    def get_departamento(self):
        return self.cargo


class Funcionario:

    def __init__(self, cargo):
        self.nome = ""
        self.setCargo(cargo)
        self.salario = 0.0
        self.departamento = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCargo(self):
        return self.cargo

    def setCargo(self, cargo):
        if cargo == None:
            print("Cargo inválido")
            exit()
        else:
            self.cargo = cargo

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        if salario < 0:
            print("Salario invalido")
        else:
            self.salario = salario

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def receberAumento(self, percentual):
        if percentual < 0:
            print("Percentual invalido")
        else:
            self.salario = self.salario * (1 + (percentual / 100))

    def mudar_departamento(self, departamento):
        self.setDepartamento(departamento)
    

    def exibir_dados(self):
        print("-" * 50)
        print(f"FUNCIONÁRIO {self.getNome()}".center(50))
        print("-" * 50)
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.getNomeCargo()}")
        print(f"Salário: {self.salario}")
        print(f"Departamento: {self.departamento}")
        print("-" * 50)
    

    def getNomeCargo(self):
        return self.cargo.get_cargo()
    

    def getNomeDepartamento(self):
        if self.departamento == None:
            print("Departamento inválido")
        return self.departamento.get_departamento()

cargo = Cargo("Analista")
departamento = Departamento()
departamento.set_departamento("RH")
funcionario = Funcionario(cargo)
funcionario.setDepartamento(departamento)
print(funcionario.getNomeCargo())
print(funcionario.getNomeDepartamento())
