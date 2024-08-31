# 5.	Classe Produto:
#
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# •	adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# •	remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# •	aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.
class Produto():
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.quantidade_estoque = 0
        self.categoria = ""
    
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_preco(self, preco):
        self.preco = preco

    def get_preco(self):
        return self.preco
    
    def set_quantidade_estoque(self, quantidade_estoque):
        self.quantidade_estoque = quantidade_estoque

    def get_quantidade_estoque(self):
        return self.quantidade_estoque
    
    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria
    
    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        return print(self.quantidade_estoque)
    
    def remover_estoque(self, quantidade):
        if self.quantidade_estoque - quantidade >= 0:
            self.quantidade_estoque -= quantidade
        else:
            return print('Não há quantidade suficiente para remover do estoque! Tente novamente.')
        return print(self.quantidade_estoque)
    
    def aplicar_desconto(self, percentual):
       desconto = self.preco * percentual / 100
       self.preco -= desconto
       return print(self.preco) 

produto = Produto()
produto.set_nome("Luvas")
print(produto.get_nome())
produto.set_preco(40)
print(produto.get_preco())
produto.set_quantidade_estoque(10)
print(produto.get_quantidade_estoque())
produto.set_categoria("Equipamentos")
print(produto.get_categoria())
produto.adicionar_estoque(10)
produto.adicionar_estoque(5)
produto.remover_estoque(15)
produto.remover_estoque(15)
produto.remover_estoque(5)
produto.remover_estoque(20)
produto.aplicar_desconto(50)

# 5.	Classe Produto:
#
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# •	adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# •	remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# •	aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.

# class Produto:

#     def _init_(self):
#         self.nome = ""
#         self.preco = 0.0
#         self.quantidade_estoque = 0.0
#         self.categoria = ""

#     def getNome(self):
#         return self.nome

#     def setNome(self, nome):
#         self.nome = nome

#     def getPreco(self):
#         return self.preco

#     def setPreco(self, preco):
#         if preco < 0:
#             print("Preco invalido")
#         else:
#             self.preco = preco

#     def getQuantidadeEstoque(self):
#         return self.quantidade_estoque

#     def setQuantidadeEstoque(self, quantidade_estoque):
#         if quantidade_estoque < 0:
#             print("Quantidade em estoque invalida")
#         else:
#             self.quantidade_estoque = quantidade_estoque

#     def getCategoria(self):
#         return self.categoria

#     def setCategoria(self, categoria):
#         self.categoria = categoria

#     def adicionarEstoque(self, quantidade):
#         if quantidade < 0:
#             print("Quantidade invalida")
#         else:
#             self.quantidade_estoque += quantidade

#     def removerEstoque(self, quantidade):
#         if quantidade < 0:
#             print("Quantidade invalida")
#         else:
#             if quantidade > self.quantidade_estoque:
#                 print("Nao pode retirar mais que a quantidade atual")
#             else:
#                 self.quantidade_estoque -= quantidade

#     def aplicarDesconto(self, percentual):
#         if percentual < 0 or percentual > 100:
#             print("Percentual invalido")
#         else:
#             self.preco = self.preco * (1 - (percentual / 100))

# produto = Produto()
# produto.setQuantidadeEstoque(100)
# produto.adicionarEstoque(1)
# print(produto.getQuantidadeEstoque())
# produto.removerEstoque(50)
# print(produto.getQuantidadeEstoque())
# produto.setPreco(1000)
# produto.aplicarDesconto(10)
# print(produto.getPreco())