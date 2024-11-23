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
        self.disciplina = None
        self.alunos = []
    

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
    

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)
    

    def exibir_alunos(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome(), end=" ")
    

    def verificar_aluno_turma(self, aluno):
        if aluno not in self.alunos:
            return "Aluno não está na turma!"
        else:
            return "Aluno está na turma!"
        
    
    def remover_aluno_turma(self, aluno):
        self.alunos.remove(aluno)


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
        self.alunos = []
        self.disciplinas = []
    

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
        for i in range(len(self.turmas)):
            return self.turmas[i].exibir_alunos()
    

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)
    

    def exibir_alunos_curso(self):
        for i in range(len(self.alunos)):
            print(self.alunos[i].get_nome(), end=" ")
    

    def adicionar_disciplinas(self, disciplina):
        self.disciplinas.append(disciplina)
    

    def exibir_disciplinas_curso(self):
        for i in range(len(self.disciplinas)):
            print(self.disciplinas[i].get_nome(), end=" ")
    

    def verificar_aluno_curso(self, aluno):
        if aluno not in self.alunos:
            return f"Aluno enviado não está no curso!"
        else:
            return f"Aluno ({aluno.get_nome()}) está no curso!"
    

    def verificar_turma_curso(self, turma):
        if turma not in self.turmas:
            return f"A turma enviada não está no curso!"
        else:
            return f"A turma enviada está no curso!"


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
print(f"4) Quais os nomes dos alunos que estão em alguma turma de um curso? -", end=" ")
curso.exibir_alunos_turma()
print()
aluno7 = Aluno()
aluno7.set_nome("Jeffão")
aluno8 = Aluno()
aluno8.set_nome("Monique")
aluno9 = Aluno()
aluno9.set_nome("Richard")
curso.adicionar_alunos(aluno7)
curso.adicionar_alunos(aluno8)
curso.adicionar_alunos(aluno9)
print(f"5) Quais os nomes dos alunos que estão registrados em um curso? -", end=" ")
curso.exibir_alunos_curso()
print()
disciplina = Disciplina()
disciplina.set_nome("Programação Orientada a Objetos")
disciplina2 = Disciplina()
disciplina2.set_nome("Algoritmos")
disciplina3 = Disciplina()
disciplina3.set_nome("Estrutura de Dados")
curso.adicionar_disciplinas(disciplina)
curso.adicionar_disciplinas(disciplina2)
curso.adicionar_disciplinas(disciplina3)
print(f"6) Quais as disciplinas que estão em alguma turma de um curso? -", end=" ")
curso.exibir_disciplinas_curso()
print()
print(f"7) Verificar se um aluno está numa turma - Aluno1: {turma.verificar_aluno_turma(aluno1)} / Aluno2: {turma.verificar_aluno_turma(aluno5)}")
print(f"8) Verificar se um aluno está em um curso - Aluno7: {curso.verificar_aluno_curso(aluno7)} / Aluno3: {curso.verificar_aluno_curso(aluno3)}")
print(f"9) Verificar se uma turma está em um curso - Turma1: {curso.verificar_turma_curso(turma)} / Turma2: {curso.verificar_turma_curso(turma2)}")
print("10) Excluir um aluno de uma turma - Lista atual:", end=" ")
turma.exibir_alunos()
turma.remover_aluno_turma(aluno2)
print("/ Lista atualizada:", end=" ")
turma.exibir_alunos()