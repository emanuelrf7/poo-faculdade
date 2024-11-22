class Pessoa:
    def __init__(self):
        self.nome = ""
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome


class Professor(Pessoa):
    def __init__(self):
        self.pessoa = None
    

    def set_pessoa(self, pessoa):
        self.pessoa = pessoa
    

    def get_pessoa(self):
        return self.pessoa
    

    def get_nome_pessoa(self):
        return self.pessoa.get_nome()


class Turma:
    def __init__(self):
        self.professor = None
        self.alunos = []
    

    def set_professor(self, professor):
        self.professor = professor
    

    def get_professor(self):
        return self.professor
    

    def get_nome_professor(self):
        return self.professor.get_nome_pessoa()
    

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)
    

    def exibir_alunos(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome(), end=" ")


class Aluno(Pessoa):
    def __init__(self):
        self.pessoa = None
    

    def set_pessoa(self, pessoa):
        self.pessoa = pessoa
    

    def get_pessoa(self):
        return self.pessoa


class Curso:
    def __init__(self):
        self.nome = ""
        self.turmas = []
        self.professores = []
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def adicionar_professores(self, professor):
        self.professores.append(professor)
    

    def exibir_professores(self):
        for i in range(len(self.professores)):
            print(self.professores[i].get_nome(), end=" ")
    

    def adicionar_turmas(self, turma):
        self.turmas.append(turma)
    

    def exibir_alunos_turma(self):
        for k, v in enumerate(self.turmas):
            print(v[k].get_nome(), end=" ")


pessoa = Pessoa()
pessoa.set_nome("Marco Antônio")
professor = Professor()
professor.set_pessoa(pessoa)
turma = Turma()
turma.set_professor(professor)
print(f"1) Qual o nome do professor de uma turma? - {turma.get_nome_professor()}")
aluno1 = Pessoa()
aluno1.set_nome("Emanuel")
aluno2 = Pessoa()
aluno2.set_nome("Paulim")
aluno3 = Pessoa()
aluno3.set_nome("Rafael")
turma.adicionar_alunos(aluno1)
turma.adicionar_alunos(aluno2)
turma.adicionar_alunos(aluno3)
print("2) Quais os nomes de todos os alunos de uma turma? -", end=" ")
turma.exibir_alunos()
print()
professor2 = Professor()
professor2.set_nome("Tássio Auad")
professor3 = Professor()
professor3.set_nome("Fábio Gonçalves")
professor4 = Professor()
professor4.set_nome("Caio Jannuzzi")
curso = Curso()
curso.set_nome("Engenharia de Software")
curso.adicionar_professores(professor2)
curso.adicionar_professores(professor3)
curso.adicionar_professores(professor4)
print("3) Quais os nomes dos professores que lecionam em alguma turma de um curso? -", end=" ")
curso.exibir_professores()
print()
aluno4 = Aluno()
aluno4.set_nome("Bruno")
aluno5 = Aluno()
aluno5.set_nome("Irlam")
aluno6 = Aluno()
aluno6.set_nome("Gabriel")
turma2 = Turma()
turma2.adicionar_alunos(aluno4)
turma2.adicionar_alunos(aluno5)
turma2.adicionar_alunos(aluno6)
curso.adicionar_turmas(turma2)
