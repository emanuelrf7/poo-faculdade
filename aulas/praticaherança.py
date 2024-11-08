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
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    

    def get_escolaridade(self):
        return self.escolaridade
    

    def get_nome_escolaridade(self):
        return self.escolaridade.get_escolaridade()


class Professor(Pessoa):
    def __init__(self):
        self.curriculo_academico = ""
    

    def set_curriculo_academico(self, curriculo_academico):
        self.curriculo_academico = curriculo_academico
    

    def get_curriculo_academico(self):
        return self.curriculo_academico


class Curso:
    def __init__(self):
        self.professor = None
        self.escola = None


    def set_professor(self, professor):
        self.professor = professor


    def get_professor(self):
        return self.professor
    

    def set_escola(self, escola):
        self.escola = escola


    def get_escola(self):
        return self.escola


    def get_nome_escolaridade(self):
        return self.professor.get_nome_escolaridade()


    def get_nome_estado_escola(self):
        return self.escola.get_nome_estado_cidade()  


class Escola:
    def __init__(self):
        self.diretor = ""
        self.professor = None
        self.cidade = None
    

    def set_diretor(self, diretor):
        self.diretor = diretor
    

    def get_diretor(self):
        return self.diretor
    

    def set_professor(self, professor):
        self.professor = professor
    

    def get_professor(self):
        return self.professor
    

    def set_cidade(self, cidade):
        self.cidade = cidade
    

    def get_cidade(self):
        return self.cidade
    

    def get_nome_escolaridade(self):
        return self.professor.get_nome_escolaridade()
    

    def get_nome_estado_cidade(self):
        return self.cidade.get_nome_estado()


class Estado:
    def __init__(self):
        self.nome = ""
        self.governador = ""

    
    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_governador(self, governador):
        self.governador = governador
    

    def get_governador(self):
        return self.governador


class Cidade:
    def __init__(self):
        self.cep = 0
        self.estado = None
    

    def set_cep(self, cep):
        self.cep = cep
    

    def get_cep(self):
        return self.cep
    

    def set_estado(self, estado):
        self.estado = estado
    

    def get_estado(self):
        return self.estado
    

    def get_nome_estado(self):
        return self.estado.get_nome()
    

class Aluno(Pessoa):
    def __init__(self):
        self.curso = None
        self.matricula = ""
    

    def set_curso(self, curso):
        self.curso = curso
    

    def get_curso(self):
        return self.curso
    

    def set_matricula(self, matricula):
        self.matricula = matricula
    

    def get_matricula(self):
        return self.matricula
    

    def get_nome_estado_curso(self):
        return self.curso.get_nome_estado_escola()

escolaridade = Escolaridade()
escolaridade.set_escolaridade("Doutorado")
professor = Professor()
professor.set_escolaridade(escolaridade)
print(f"a) Qual a escolaridade de um professor? - {professor.get_nome_escolaridade()}")
curso = Curso()
curso.set_professor(professor)
print(f"b) Qual a escolaridade do coordenador de um curso? - {curso.get_nome_escolaridade()}")
escola = Escola()
escola.set_diretor("Gregson")
escola.set_professor(professor)
print(f"c) Qual a escolaridade do diretor de uma escola? - {escola.get_diretor()}: {escola.get_nome_escolaridade()}")
estado = Estado()
estado.set_nome("Rio de Janeiro")
cidade = Cidade()
cidade.set_estado(estado)
escola.set_cidade(cidade)
curso.set_escola(escola)
aluno = Aluno()
aluno.set_curso(curso)
print(f"d) Qual o estado de naturalidade de um aluno? - {aluno.get_nome_estado_curso()}")