class Carro:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.velocidade_atual = 0.0
        self.estado = ""

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_ano(self, ano):
        self.ano = ano

    def get_ano(self):
        return self.ano

    def set_velocidade(self, velocidade_atual):
        self.velocidade_atual = velocidade_atual

    def get_velocidade(self):
        return self.velocidade_atual

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def ligar(self):
        self.estado = "ligado"

    def desligar(self):
        self.estado = "desligado"

    def acelerar(self, quantidade):
        if self.estado == "ligado":
            self.velocidade_atual = self.velocidade_atual + quantidade

    def frear(self, quantidade):
        if self.estado == "ligado":
            self.velocidade_atual = self.velocidade_atual - quantidade


carro = Carro()
carro.set_marca("Jeep")
print(carro.get_marca())
carro.set_modelo("Compass")
print(carro.get_modelo())
carro.set_ano(2024)
print(carro.get_ano())
carro.set_velocidade(40.5)
print(carro.get_velocidade())
carro.set_estado("ligado")
print(carro.get_estado())
carro.frear(30.5)
print(carro.get_velocidade())
carro.frear(10)
print(carro.get_estado())
print(carro.get_velocidade())
carro.desligar()
print(carro.get_estado())
