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
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

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
        self.professores = []
        self.disciplina = None
    
    
    def set_professor(self, professor):
        self.professor = professor
    

    def get_professor(self):
        return self.professor
    

    def set_disciplina(self, disciplina):
        self.disciplina = disciplina
    

    def get_disciplina(self):
        return self.disciplina
    

    def get_nome_professor(self):
        return self.professor.get_nome_pessoa()
    

    def matricular(self, aluno):
        self.alunos.append(aluno)
    

    def adicionar_professor(self, professor):
        self.professores.append(professor)
    

    def exibir_alunos(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome_aluno(), end=" ")
    

    def exibir_professores(self):
        for i in range(len(self.professores)):
            print(self.professores[i].get_nome_pessoa(), end=" ")
    

    def exibir_disciplina(self):
        return self.disciplina.get_nome()
    

    def verificar_aluno(self, aluno):
        if aluno in self.alunos:
            return True
        else:
            return False


class Aluno(Pessoa):
    def __init__(self):
        self.turma = None
    

    def set_turma(self, turma):
        self.turma = turma
    

    def get_turma(self):
        return self.turma
    

    def get_nome_aluno(self):
        return self.nome.get_nome()


class Curso:
    def __init__(self):
        self.nome = ""
        self.turma = None
        self.alunos = []
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome
    

    def set_turma(self, turma):
        self.turma = turma
    

    def get_nome_alunos_turma(self):
        return self.turma.exibir_alunos()
    

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)
    

    def get_nome_alunos_curso(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome_aluno(), end=" ")


class Disciplina:
    def __init__(self):
        self.nome = ""
    

    def set_nome(self, nome):
        self.nome = nome
    

    def get_nome(self):
        return self.nome

pessoa = Pessoa()
pessoa.set_nome("Marco Antônio")
professor = Professor()
professor.set_pessoa(pessoa)
turma = Turma()
turma.set_professor(professor)
print(f"1) Qual o nome do professor de uma turma? - {turma.get_nome_professor()}")
pessoa_aluno1 = Pessoa()
pessoa_aluno1.set_nome("Emanuel")
aluno1 = Aluno()
aluno1.set_nome(pessoa_aluno1)
pessoa_aluno2 = Pessoa()
pessoa_aluno2.set_nome("Paulim")
aluno2 = Aluno()
aluno2.set_nome(pessoa_aluno2)
pessoa_aluno3 = Pessoa()
pessoa_aluno3.set_nome("Rafael")
aluno3 = Aluno()
aluno3.set_nome(pessoa_aluno3)
turma.matricular(aluno1)
turma.matricular(aluno2)
turma.matricular(aluno3)
print(f"2) Quais os nomes de todos os alunos de uma turma? - ", end="")
turma.exibir_alunos()
curso = Curso()
curso.set_nome("Engenharia de Software")
curso.set_turma(turma)
pessoa2 = Pessoa()
pessoa2.set_nome("Tassio Auad")
professor2 = Professor()
professor2.set_pessoa(pessoa2)
pessoa3 = Pessoa()
pessoa3.set_nome("Fabio")
professor3 = Professor()
professor3.set_pessoa(pessoa3)
turma.adicionar_professor(professor)
turma.adicionar_professor(professor2)
turma.adicionar_professor(professor3)
print()
print(f"3) Quais os nomes dos professores que lecionam em alguma turma de um curso? - ", end="")
turma.exibir_professores()
print()
print(f"4) Quais os nomes dos alunos que estão em alguma turma de um curso? - ", end="")
curso.get_nome_alunos_turma()
pessoa_aluno4 = Pessoa()
pessoa_aluno4.set_nome("Gabriel Lopes")
aluno4 = Aluno()
aluno4.set_nome(pessoa_aluno4)
pessoa_aluno5 = Pessoa()
pessoa_aluno5.set_nome("Nathan")
aluno5 = Aluno()
aluno5.set_nome(pessoa_aluno5)
pessoa_aluno6 = Pessoa()
pessoa_aluno6.set_nome("Rafael Antunes")
aluno6 = Aluno()
aluno6.set_nome(pessoa_aluno6)
curso.adicionar_alunos(aluno4)
curso.adicionar_alunos(aluno5)
curso.adicionar_alunos(aluno6)
print()
print(f"5) Quais os nomes dos alunos que estão registrados em um curso? - ", end="")
curso.get_nome_alunos_curso()
disciplina1 = Disciplina()
disciplina1.set_nome("Programação Orientada a Objetos")
turma.set_disciplina(disciplina1)
print()
print(f"6) Quais as disciplinas que estão em alguma turma de um curso? - {turma.exibir_disciplina()}")
print(f"7) Verificar se um aluno está numa turma - Aluno 2: {turma.verificar_aluno(aluno2)} / Aluno 5: {turma.verificar_aluno(aluno5)}")