class Escolaridade:
    def __init__(self):
        self.nome = ""
    
    
    def getNome(self):
        return self.nome
    
    
    def setNome(self, nome):
        self.nome = nome    

class Funcionario:
    def __init__(self, escolaridade):
        self.setEscolaridade(escolaridade)
        self.escolaridade = escolaridade
        self.alocacao = None
    
    
    def getEscolaridade(self):
        return self.escolaridade
    
    
    def setEscolaridade(self, escolaridade):
        if escolaridade == None:
            print("Funcionario deve ter uma escolaridade")
            exit()
        self.escolaridade = escolaridade
    
    
    def get_alocacao(self):
        return self.alocacao
    
    
    def set_alocacao(self, alocacao):
        self.alocacao = alocacao
    
    
    def getNomeEscolaridade(self):
        return self.escolaridade.getNome()

class Grupo:
    def __init__(self):
        self.presidente = None
    
    
    def getPresidente(self):
        return self.presidente
    
    
    def setPresidente(self, presidente):
        self.presidente = presidente
    
    
    def getNomeEscolaridadePresidente(self):
        if self.presidente == None:
            print("Grupo sem presidente no momento")
        else:
            return self.presidente.getNomeEscolaridade()

class Pais:
    def __init__(self):
        self.nome = ""
    
    
    def get_nome(self):
        return self.nome
    
    
    def set_nome(self, nome):
        self.nome = nome

class Empresa:
    def __init__(self):
        self.empresa = None
    
    
    def get_empresa(self):
        return self.empresa
    
    
    def set_empresa(self, empresa):
        self.empresa = empresa
        
class Departamento:
    def __init__(self):
        self.chefia = None
    
    
    def get_chefia(self):
        return self.chefia
    
    
    def set_chefia(self, chefia):
        self.chefia = chefia    
        
grupo = Grupo()
escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")
presidente = Funcionario(escolaridade)
grupo.setPresidente(presidente)
print(grupo.getNomeEscolaridadePresidente())
