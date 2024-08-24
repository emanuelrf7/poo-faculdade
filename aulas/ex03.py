class Livro:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano_publicacao = 0
        self.numero_paginas = 0
        self.genero = ""
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
    
    def marcar_pagina(self, pagina):
        self.pagina = pagina
    
    def avancar_pagina(self):
        if self.pagina <= self.numero_paginas:
            self.pagina += 1
        
        return print(f"Você avançou para a página {self.pagina}")
    
    def retroceder_pagina(self):
        if self.pagina <= self.numero_paginas:
            self.pagina -= 1
        
        return print(f"Você retornou para a página {self.pagina}")


livro = Livro()
livro.set_titulo("Ideias que rimam mais que palavras vol. 1")
print(livro.get_titulo())
livro.set_autor("Rashid")
print(livro.get_autor())
livro.set_ano_publicacao(2018)
print(livro.get_ano_publicacao())
livro.set_numero_paginas(300)
print(livro.get_numero_paginas())
livro.set_genero("Biografia")
print(livro.get_genero())
print(livro.abrir())
livro.set_pagina(50)
print(livro.get_pagina())
livro.avancar_pagina()
livro.avancar_pagina()
livro.retroceder_pagina()
livro.avancar_pagina()
