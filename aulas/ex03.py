# 3.	Classe Livro:
#
# Atributos: titulo, autor, ano_publicacao, numero_paginas, genero
# Métodos: abrir, fechar, marcar_pagina, avancar_pagina, retroceder_pagina
# •	abrir(): Exibe uma mensagem indicando que o livro foi aberto.
# •	fechar(): Exibe uma mensagem indicando que o livro foi fechado.
# •	marcar_pagina(pagina): Marca a página atual do livro.
# •	avancar_pagina(): Avança uma página, se não estiver na última página.
# •	retroceder_pagina(): Retrocede uma página, se não estiver na primeira página.
class Titulo:
    def __init__(self):
        self.titulo = ""
    

    def getTitulo(self):
        return self.titulo
    

    def setTitulo(self, titulo):
        self.titulo = titulo


class Autor:
    def __init__(self):
        self.autor = ""
    

    def getAutor(self):
        return self.autor
    

    def setAutor(self, autor):
        self.autor = autor


class Genero:
    def __init__(self):
        self.genero = ""
    

    def getGenero(self):
        return self.genero
    

    def setGenero(self, genero):
        self.genero = genero


class Livro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.ano_publicacao = 0
        self.numero_paginas = 0
        self.genero = None
        self.pagina = 0
    
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    

    def get_titulo(self):
        return self.titulo
    

    def set_autor(self, autor):
        self.autor = autor
    

    def get_autor(self):
        return self.autor
    

    def set_ano_publicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao
    

    def get_ano_publicacao(self):
        return self.ano_publicacao
    

    def set_numero_paginas(self, numero_paginas):
        self.numero_paginas = numero_paginas
    

    def get_numero_paginas(self):
        return self.numero_paginas
    

    def set_genero(self, genero):
        self.genero = genero
    

    def get_genero(self):
        return self.genero
    

    def set_pagina(self, pagina):
        self.pagina = pagina
    

    def get_pagina(self):
        return self.pagina
    

    def abrir(self):
        return "O livro foi aberto!"        


    def fechar(self):
        return "O livro foi fechado!"
    

    def marcar_pagina(self):
        # self.pagina = pagina
        return print(f'Você marcou a página {self.pagina}')
    

    def avancar_pagina(self):
        if self.pagina <= self.numero_paginas:
            self.pagina += 1
        
        return print(f"Você avançou para a página {self.pagina}")
    

    def retroceder_pagina(self):
        if self.pagina <= self.numero_paginas:
            self.pagina -= 1
        
        return print(f"Você retornou para a página {self.pagina}")


    def getNomeTitulo(self):
        if self.titulo == None:
            print("Titulo está sem nome")
        else:
            return self.titulo.getTitulo()
    

    def getNomeAutor(self):
        if self.autor == None:
            print("Autor está sem nome")
        else:
            return self.autor.getAutor()
    

    def getNomeGenero(self):
        if self.genero == None:
            print("Genero está sem nome")
        else:
            return self.genero.getGenero()


titulo = Titulo()
titulo.setTitulo("Ideias que rimam mais que palavras vol. 1")
autor = Autor()
autor.setAutor("Rashid")
genero = Genero()
genero.setGenero("Biografia")
livro = Livro()
livro.set_titulo(titulo)
print(livro.getNomeTitulo())
livro.set_autor(autor)
print(livro.getNomeAutor())
livro.set_ano_publicacao(2018)
print(livro.get_ano_publicacao())
livro.set_numero_paginas(300)
print(livro.get_numero_paginas())
livro.set_genero(genero)
print(livro.getNomeGenero())
print(livro.abrir())
livro.set_pagina(50)
livro.marcar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.retroceder_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.retroceder_pagina()

# 3.	Classe Livro:
#
# Atributos: titulo, autor, ano_publicacao, numero_paginas, genero
# Métodos: abrir, fechar, marcar_pagina, avancar_pagina, retroceder_pagina
# •	abrir(): Exibe uma mensagem indicando que o livro foi aberto.
# •	fechar(): Exibe uma mensagem indicando que o livro foi fechado.
# •	marcar_pagina(pagina): Marca a página atual do livro.
# •	avancar_pagina(): Avança uma página, se não estiver na última página.
# •	retroceder_pagina(): Retrocede uma página, se não estiver na primeira página.

# class Livro:

#     def _init_(self):
#         self.titulo = ""
#         self.autor = ""
#         self.ano_publicacao = 0
#         self.numero_paginas = 0
#         self.genero = ""
#         self.aberto = False
#         self.pagina_atual = 0

#     def getTitulo(self):
#         return self.titulo

#     def setTitulo(self, titulo):
#         self.titulo = titulo

#     def getAutor(self):
#         return self.autor

#     def setAutor(self, autor):
#         self.autor = autor

#     def getAnoPublicacao(self):
#         return self.ano_publicacao

#     def setAnoPublicacao(self, ano_publicacao):
#         self.ano_publicacao = ano_publicacao

#     def getNumeroPaginas(self):
#         return self.numero_paginas

#     def setNumeroPaginas(self, numero_paginas):
#         self.numero_paginas = numero_paginas

#     def getGenero(self):
#         return self.genero

#     def setGenero(self, genero):
#         self.genero = genero

#     def getPaginaAtual(self):
#         return self.pagina_atual

#     def setPaginaAtual(self, pagina_atual):
#         self.pagina_atual = pagina_atual

#     def abrir(self):
#         if not self.aberto:
#             self.aberto = True
#             print("Livro aberto")

#     def fechar(self):
#         if self.aberto:
#             self.aberto = False
#             print("Livro fechado")

#     def marcar_pagina(self, pagina):
#         if not self.aberto:
#             print("Pagina nao pode ser marcada em livro fechado")
#         else:
#             if pagina < 1 or pagina > self.numero_paginas:
#                 print("Pagina invalida")
#             else:
#                 self.pagina_atual = pagina

#     def avancar_pagina(self):
#         if self.aberto:
#             if self.pagina_atual >= self.numero_paginas:
#                 print("Nao é possivel avancar pagina")
#             else:
#                 self.pagina_atual += 1

#     def retroceder_pagina(self):
#         if self.aberto:
#             if self.pagina_atual <= 1:
#                 print("Nao é possivel retroceder pagina")
#             else:
#                 self.pagina_atual -= 1

# livro = Livro()
# livro.abrir()
# livro.setNumeroPaginas(50)
# livro.marcar_pagina(2)
# livro.retroceder_pagina()
# livro.fechar()