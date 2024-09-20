# Classe ContaBancaria:
#
# Atributos: titular, numero_conta, saldo
# Métodos: depositar, sacar
# •	depositar(valor): adiciona o valor ao saldo da conta.
# •	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.
class Titular:
    def __init__(self):
        self.titular = ""
    

    def getTitular(self):
        return self.titular
    

    def setTitular(self, titular):
        self.titular = titular


class ContaBancaria:
    def __init__(self):
        self.titular = None
        self.numero_conta = 0.0
        self.saldo = 0.0
    

    def set_titular(self, titular):
        self.titular = titular
    

    def get_titular(self):
        return self.titular
    

    def set_numero_conta(self, numero_conta):
        self.numero_conta = numero_conta
    

    def get_numero_conta(self):
        return self.numero_conta
    

    def set_saldo(self, saldo):
        self.saldo = saldo
    

    def get_saldo(self):
        return self.saldo
    

    def depositar(self, valor):
        self.saldo += valor
    

    def sacar(self, valor):
        if self.saldo >= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
    

    def getNomeTitular(self):
        if self.titular == None:
            print("Titular está sem nome")
        else:
            return self.titular.getTitular()

titular = Titular()
titular.setTitular("Emanuel")    
conta_bancaria = ContaBancaria()
conta_bancaria.set_titular(titular)
print(conta_bancaria.getNomeTitular())
conta_bancaria.set_saldo(700)
print(conta_bancaria.get_saldo())
conta_bancaria.depositar(300)
print(conta_bancaria.get_saldo())
conta_bancaria.sacar(500)
print(conta_bancaria.get_saldo())
conta_bancaria.sacar(300)
print(conta_bancaria.get_saldo())
conta_bancaria.sacar(200)
print(conta_bancaria.get_saldo())
conta_bancaria.sacar(100)
