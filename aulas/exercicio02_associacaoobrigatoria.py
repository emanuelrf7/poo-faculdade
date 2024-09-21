
# Classe ContaBancaria:
#
# Atributos: titular, numero_conta, saldo
# Métodos: depositar, sacar
# •	depositar(valor): adiciona o valor ao saldo da conta.
# •	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.

class Cliente:
    def __init__(self, nome):
        self.setNome(nome)

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        if nome == "":
            print("Nome invalido")
        self.nome = nome

class ContaBancaria:

    def __init__(self, titular):
        self.setTitular(titular)
        self.numero_conta = 0
        self.saldo = 0.0
        self.estado = "ativa"

    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        if titular == None:
            print("titular invalido")
            exit()
        else:
            self.titular = titular

    def getNumeroConta(self):
        return self.numero_conta

    def setNumeroConta(self, conta):
        self.numero_conta = conta

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        if self.estado == "ativa":
            if saldo >= 0:
                self.saldo = saldo

    def setEstado(self, estado):
        if estado == "ativa" or estado == "inativa":
            self.estado = estado

    def getEstado(self):
        return self.estado

    def ativar(self):
        self.estado = "ativa"

    def inativar(self):
        self.estado = "inativa"

    def depositar(self, valor):
        if self.estado == "ativa":
            if valor > 0:
                self.saldo += valor

    def sacar(self, valor):
        if self.estado == "ativa":
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor

    def getNomeTitular(self):
        return self.titular.getNome()

# conta = ContaBancaria()
# conta.setSaldo(500)
# conta.inativar()
# print(conta.getSaldo())
# conta.depositar(100)
# print(conta.getSaldo())
# conta.ativar()
# conta.sacar(30)
# print(conta.getSaldo())

cliente = Cliente("Monique Vitoria")
conta = ContaBancaria(cliente)
print(conta.getNomeTitular())
