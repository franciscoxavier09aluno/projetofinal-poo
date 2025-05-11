from pessoa import Pessoa
from disciplina import Disciplina
from persistencia import Persistencia

# Classe responsável por cadastrar e buscar entidades
class Cadastro:
    def __init__(self):
        self.alunos = Persistencia.carregar_alunos()
        self.professores = Persistencia.carregar_professores()
        self.disciplinas = Persistencia.carregar_disciplinas(
            professores=self.professores)  

    def cadastrar_aluno(self, aluno):
        try:
            Pessoa.validar_cpf(aluno.cpf)
            Pessoa.validar_data(aluno.data_nascimento)
            self.alunos.append(aluno)
            Persistencia.salvar_alunos(self.alunos)
            print(f"Aluno {aluno.nome} cadastrado!")
        except ValueError as e:
            print(f"Erro ao cadastrar aluno: {e}")

    def cadastrar_professor(self, professor):
        try:
            Pessoa.validar_cpf(professor.cpf)
            Pessoa.validar_data(professor.data_nascimento)
            self.professores.append(professor)
            Persistencia.salvar_professores(self.professores)
            print(f"Professor {professor.nome} cadastrado!")
        except ValueError as e:
            print(f"Erro ao cadastrar professor: {e}")

    def cadastrar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        Persistencia.salvar_disciplinas(self.disciplinas)
        print(f"Disciplina {disciplina.nome} cadastrada!")

    # Lista todos os registros de uma entidade
    def listar_todos(self, lista_entidades):
        if not lista_entidades:
            print("Nenhum registro encontrado.")
            return
        for entidade in lista_entidades:
            entidade.exibir_dados()
            print("------")

    def buscar_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        print("Aluno não encontrado.")
        return None

    def buscar_por_siape(self, siape):
        for professor in self.professores:
            if professor.siape == siape:
                return professor
        print("Professor não encontrado.")
        return None

    def buscar_por_codigo_disciplina(self, codigo):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo:
                return disciplina
        print("Disciplina não encontrada.")
        return None