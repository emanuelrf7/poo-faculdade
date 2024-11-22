class Aluno:
    def __init__(self):
        self.nome = ""
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome

class Curso:
    def __init__(self):
        self.nome = ""
        self.alunos = []
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def matricular(self, aluno):
        self.alunos.append(aluno)
    def exibir_alunos(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome())
    def verificar_matricula(self, aluno):
        return aluno in self.alunos
    def desmatricular_aluno(self, aluno):
        self.alunos.remove(aluno)

curso = Curso()
aluno1 = Aluno()
aluno1.set_nome("Guilherme sem hamburguer")
aluno2 = Aluno()
aluno2.set_nome("Guilherme sem guaraviton")
aluno3 = Aluno()
curso.matricular(aluno1)
curso.matricular(aluno2)
curso.exibir_alunos()
print(curso.verificar_matricula(aluno1))
print(curso.verificar_matricula(aluno3))
curso.desmatricular_aluno(aluno1)
print(curso.verificar_matricula(aluno1))