# Representa uma disciplina que pode ter alunos e um professor
class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel=None):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_matriculados:
            self.alunos_matriculados.append(aluno)
        if self not in aluno.disciplinas:
            aluno.disciplinas.append(self)

    def remover_aluno(self, aluno):
        if aluno in self.alunos_matriculados:
            self.alunos_matriculados.remove(aluno)

    def adicionar_professor(self, professor): 
        self.professor_responsavel = professor
        if self not in professor.disciplinas:
            professor.disciplinas.append(self)

    def exibir_dados(self):
        print(f"Disciplina: {self.nome} ({self.codigo})")
        if self.professor_responsavel:
            print(f"Professor Responsável: {self.professor_responsavel.nome}")
        else:
            print("Professor Responsável: Não atribuído")

        print("Alunos Matriculados:")
        if self.alunos_matriculados:
            for aluno in self.alunos_matriculados:
                print(f"  - {aluno.nome}")
        else:
            print("Nenhum aluno matriculado.")