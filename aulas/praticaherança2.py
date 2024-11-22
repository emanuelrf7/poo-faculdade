class Escolaridade:
    def __init__(self):
        self.escolaridade = ""
    

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    

    def get_escolaridade(self):
        return self.escolaridade


class Pessoa:
    def __init__(self):
        self.nome = ""
        self.escolaridade = None
        self.naturalidade = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    

    def get_escolaridade(self):
        return self.escolaridade
    

    def set_naturalidade(self, naturalidade):
        self.naturalidade = naturalidade
    

    def get_naturalidade(self):
        return self.naturalidade
    

    def get_nome_escolaridade(self):
        return self.escolaridade.get_escolaridade()
    

    def get_nome_estado_cidade(self):
        return self.naturalidade.get_nome_estado()
    

    def get_nome_cidade(self):
        return self.naturalidade.get_nome()


class Professor(Pessoa):
    def __init__(self):
        self.pessoa = None
        self.curso = None
    

    def set_pessoa(self, pessoa):
        self.pessoa = pessoa
    

    def get_pessoa(self):
        return self.pessoa
    

    def set_curso(self, curso):
        self.curso = curso
    

    def get_curso(self):
        return self.curso
    

    def get_escolaridade(self):
        return self.pessoa.get_nome_escolaridade()
    

    def get_cidade_professor(self):
        return self.pessoa.get_nome_cidade()
    

    def get_tipo_ensino(self):
        return self.curso.get_nome_tipo_ensino()


class Curso:
    def __init__(self):
        self.nome = ""
        self.coordenador = None
        self.escola = None
        self.tipo_ensino = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_coordenador(self, coordenador):
        self.coordenador = coordenador
    

    def get_coordenador(self):
        return self.coordenador
    

    def set_escola(self, escola):
        self.escola = escola
    

    def get_escola(self):
        return self.escola
    

    def set_tipo_ensino(self, tipo_ensino):
        self.tipo_ensino = tipo_ensino
    

    def get_tipo_ensino(self):
        return self.tipo_ensino
    

    def get_escolaridade_coordenador(self):
        return self.coordenador.get_escolaridade()
    

    def get_nome_estado_escola(self):
        return self.escola.get_nome_estado_cidade()
    

    def get_nome_tipo_ensino(self):
        return self.tipo_ensino.get_nome()


class Escola:
    def __init__(self):
        self.nome = ""
        self.diretor = None
        self.cidade = None
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_diretor(self, diretor):
        self.diretor = diretor
    

    def get_diretor(self):
        return self.diretor
    

    def set_cidade(self, cidade):
        self.cidade = cidade
    

    def get_cidade(self):
        return self.cidade
    

    def get_escolaridade_diretor(self):
        return self.diretor.get_escolaridade()
    

    def get_nome_estado_cidade(self):
        return self.cidade.get_nome_estado()


class Estado:
    def __init__(self):
        self.nome = ""
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome


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


class Aluno(Pessoa):
    def __init__(self):
        self.pessoa = None
        self.curso = None
    

    def set_pessoa(self, pessoa):
        self.pessoa = pessoa
    

    def get_pessoa(self):
        return self.pessoa
    

    def set_curso(self, curso):
        self.curso = curso
    

    def get_curso(self):
        return self.curso
    

    def get_estado_aluno(self):
        return self.pessoa.get_nome_estado_cidade()
    

    def get_estado_estudo_aluno(self):
        return self.curso.get_nome_estado_escola()


class TipoEnsino:
    def __init__(self):
        self.nome = ""

    
    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome


escolaridade = Escolaridade()
escolaridade.set_escolaridade("Doutorado")
pessoa = Pessoa()
pessoa.set_nome("Marco Antônio")
pessoa.set_escolaridade(escolaridade)
professor = Professor()
professor.set_pessoa(pessoa)
print(f"a) Qual a escolaridade de um professor? - {professor.get_escolaridade()}")
escolaridade2 = Escolaridade()
escolaridade2.set_escolaridade("Mestrado")
pessoa2 = Pessoa()
pessoa2.set_nome("Carlos Vitor")
pessoa2.set_escolaridade(escolaridade2)
professor2 = Professor()
professor2.set_pessoa(pessoa2)
curso = Curso()
curso.set_nome("Engenharia de Software")
curso.set_coordenador(professor2)
print(f"b) Qual a escolaridade do coordenador de um curso? - {curso.get_escolaridade_coordenador()}")
escolaridade3 = Escolaridade()
escolaridade3.set_escolaridade("Bacharelado")
pessoa3 = Pessoa()
pessoa3.set_nome("Gregson")
pessoa3.set_escolaridade(escolaridade3)
professor3 = Professor()
professor3.set_pessoa(pessoa3)
escola = Escola()
escola.set_nome("Ciep 297 Padre Salésio Schimid")
escola.set_diretor(professor3)
print(f"c) Qual a escolaridade do diretor de uma escola? - {escola.get_escolaridade_diretor()}")
estado = Estado()
estado.set_nome("Rio de Janeiro")
cidade = Cidade()
cidade.set_nome("Vassouras")
cidade.set_estado(estado)
pessoa4 = Pessoa()
pessoa4.set_nome("Emanuel")
pessoa4.set_naturalidade(cidade)
aluno = Aluno()
aluno.set_pessoa(pessoa4)
print(f"d) Qual o estado de naturalidade de um aluno? - {aluno.get_estado_aluno()}")
cidade2 = Cidade()
cidade2.set_nome("Juiz de Fora")
pessoa5 = Pessoa()
pessoa5.set_nome("Tássio Auad")
pessoa5.set_naturalidade(cidade2)
professor4 = Professor()
professor4.set_pessoa(pessoa5)
print(f"e) Qual a cidade de nascimento de um professor? - {professor4.get_cidade_professor()}")
escola.set_cidade(cidade)
curso2 = Curso()
curso2.set_nome("Ensino Médio Regular")
curso2.set_escola(escola)
aluno.set_curso(curso2)
print(f"f) Qual o estado em que um aluno estuda? - {aluno.get_estado_estudo_aluno()}")
tipo_ensino = TipoEnsino()
tipo_ensino.set_nome("Ensino Superior")
curso.set_tipo_ensino(tipo_ensino)
professor4.set_curso(curso)
print(f"g) Qual o tipo de ensino (ensino fundamental, médio, superior) que um professor foi contratado para lecionar? - {professor4.get_tipo_ensino()}")