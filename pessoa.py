import re
from abc import ABC, abstractmethod
from datetime import datetime, date

# Classe abstrata base para Aluno e Professor
class Pessoa(ABC):
    def __init__(self, nome, cpf, data_nascimento=date(1900, 1, 1)):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if not Pessoa.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        self.__cpf = cpf

    @abstractmethod
    def exibir_dados(self):
        pass

    @staticmethod
    def validar_cpf(cpf):
        cpf = re.sub(r'\D', '', str(cpf))
        return len(cpf) == 11

    @staticmethod
    def formatar_cpf(cpf):
        cpf = str(cpf).zfill(11)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @staticmethod
    def validar_data(data_nascimento):
        if isinstance(data_nascimento, date):
            return data_nascimento <= date.today()
        elif isinstance(data_nascimento, str):
            try:
                data_nascimento = datetime.strptime(
                    data_nascimento, "%Y-%m-%d").date()
                return data_nascimento <= date.today()
            except ValueError:
                raise ValueError("Formato de data inválido (AAAA-MM-DD)")
        else:
            raise TypeError("Tipo de data inválido")

# Representa um aluno com matrícula e notas
class Aluno(Pessoa):
    total_alunos = 0

    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = {}  
        self.disciplinas = []
        Aluno.total_alunos += 1

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    def adicionar_nota(self, disciplina, nota):
        if disciplina in self.__notas:
            self.__notas[disciplina].append(nota)
        else:
            self.__notas[disciplina] = [nota]

    def calcular_media(self, disciplina):
        if disciplina in self.__notas:
            notas = self.__notas[disciplina]
            if notas:
                return sum(notas) / len(notas)
            else:
                return 0
        else:
            return 0

    def matricular_em_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_aluno(self)

    def desmatricular_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            disciplina.remover_aluno(self)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {Pessoa.formatar_cpf(self.cpf)}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Matrícula: {self.__matricula}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome}")
        print("Notas:")
        for disciplina, notas in self.__notas.items():
            print(f"  - {disciplina.nome}: {notas}")

    @staticmethod
    def exibir_total_cadastrados():
        print(f"Total de alunos cadastrados: {Aluno.total_alunos}")

# Representa um professor com SIAPE e disciplinas
class Professor(Pessoa):
    total_professores = 0

    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []
        Professor.total_professores += 1

    @property
    def siape(self):
        return self.__siape

    @siape.setter
    def siape(self, siape):
        self.__siape = siape

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.professor_responsavel = self

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            disciplina.professor_responsavel = None

    def exibir_dados(self):
        print(f"Nome do Professor: {self.nome}")
        print(f"CPF: {Pessoa.formatar_cpf(self.cpf)}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"SIAPE: {self.__siape}")
        print("Disciplinas lecionadas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")

    @staticmethod
    def exibir_total_cadastrados():
        print(f"Total de professores cadastrados: {Professor.total_professores}")