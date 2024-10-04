class Escolaridade:
    def __init__(self, escolaridade):
        self.set_escolaridade(escolaridade)
    
    
    def set_escolaridade(self, escolaridade):
        if escolaridade == None:
            print("Escolaridade está vazio")
        else:
            self.escolaridade = escolaridade
    

    def get_escolaridade(self):
        return self.escolaridade

class Funcionario:
    def __init__(self):
        self.nome = ""
        self.escolaridade = None
        self.alocacao = None
        self.filial = None
        self.departamento = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    

    def get_escolaridade(self):
        return self.escolaridade
    

    def set_alocacao(self, alocacao):
        self.alocacao = alocacao
    

    def get_alocacao(self):
        return self.alocacao
    

    def set_filial(self, filial):
        self.filial = filial
    

    def get_filial(self):
        return self.filial
    

    def set_departamento(self, departamento):
        self.departamento = departamento

    
    def get_departamento(self):
        return self.departamento
    

    def get_nome_escolaridade(self):
        return self.escolaridade.get_escolaridade()
    

    def get_nome_pais_departamento(self):
        return self.alocacao.get_nome_pais_empresa()
    

    def get_nome_estado_filial(self):
        return self.filial.get_nome_estado_cidade()

class Grupo:
    def __init__(self):
        self.presidente = None
        self.pais = None
    

    def set_presidente(self, presidente):
        self.presidente = presidente
    

    def get_presidente(self):
        return self.presidente
    

    def set_pais(self, pais):
        self.pais = pais
    

    def get_pais(self):
        return self.pais
    

    def get_nome_escolaridade_presidente(self):
        return self.presidente.get_nome_escolaridade()
    

    def get_nome_pais(self):
        return self.pais.get_nome()

class Pais:
    def __init__(self):
        self.nome = ""
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome

class Empresa:
    def __init__(self):
        self.empresa = None
        self.diretor = None
    

    def set_empresa(self, empresa):
        self.empresa = empresa
    

    def get_empresa(self):
        return self.empresa
    

    def set_diretor(self, diretor):
        self.diretor = diretor
    

    def get_diretor(self):
        return self.diretor
    

    def get_nome_pais_grupo(self):
        return self.empresa.get_nome_pais()
    

    def get_nome_diretor(self):
        return self.diretor.get_nome()

class Departamento:
    def __init__(self):
        self.chefia = None
        self.pais = None
    

    def set_chefia(self, chefia):
        self.chefia = chefia
    

    def get_chefia(self):
        return self.chefia
    

    def set_pais(self, pais):
        self.pais = pais
    

    def get_pais(self):
        return self.pais
    

    def get_nome_pais_empresa(self):
        return self.pais.get_nome_pais_grupo()
    

    def get_nome_escolaridade(self):
        return self.chefia.get_nome_escolaridade()

class Estado:
    def __init__(self):
        self.nome = ""
        self.pais = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_pais(self, pais):
        self.pais = pais
    

    def get_pais(self):
        return self.pais

class Cidade:
    def __init__(self):
        self.nome = ""
        self.estado = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_estado(self, estado):
        self.estado = estado
    

    def get_estado(self):
        return self.estado
    

    def get_nome_estado(self):
        return self.estado.get_nome()

class Filial:
    def __init__(self):
        self.filial = ""
        self.estado = None
        self.empresa = None
    

    def set_filial(self, filial):
        self.filial = filial
    

    def get_filial(self):
        return self.filial
    

    def set_estado(self, estado):
        self.estado = estado
    

    def get_estado(self):
        return self.estado
    

    def set_empresa(self, empresa):
        self.empresa = empresa
    

    def get_empresa(self):
        return self.empresa
    

    def get_nome_estado_cidade(self):
        return self.estado.get_nome_estado()
    

    def get_nome_diretor_empresa(self):
        return self.empresa.get_nome_diretor()
    
escolaridade = Escolaridade("Doutorado")
presidente = Funcionario()
presidente.set_escolaridade(escolaridade)
grupo = Grupo()
grupo.set_presidente(presidente)
print(f"1 - Qual a escolaridade do presidente de um grupo? {grupo.get_nome_escolaridade_presidente()}")
pais = Pais()
pais.set_nome("Brasil")
grupo.set_pais(pais)
empresa = Empresa()
empresa.set_empresa(grupo)
departamento = Departamento()
departamento.set_pais(empresa)
presidente.set_alocacao(departamento)
print(f"2 - Qual o pais de alocacao de um funcionario? {presidente.get_nome_pais_departamento()}")
estado = Estado()
estado.set_pais(pais)
estado.set_nome("Rio de Janeiro")
cidade = Cidade()
cidade.set_estado(estado)
filial = Filial()
filial.set_estado(cidade)
funcionario = Funcionario()
funcionario.set_filial(filial)
print(f"3 - Qual o estado da filial que um funcionario coordena? {funcionario.get_nome_estado_filial()}")
escolaridade2 = Escolaridade("Mestrado")
chefe = Funcionario()
chefe.set_departamento(departamento)
chefe.set_escolaridade(escolaridade2)
departamento.set_chefia(chefe)
print(f"4 - Qual a escolaridade do chefe de um departamento? {departamento.get_nome_escolaridade()}")
diretor = Funcionario()
diretor.set_nome("Carlos")
empresa.set_diretor(diretor)
filial.set_empresa(empresa)
print(f"5 - Qual o nome do diretor da empresa de uma filial? {filial.get_nome_diretor_empresa()}")
