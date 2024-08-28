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
