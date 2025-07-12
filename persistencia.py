from datetime import datetime, date
from pessoa import Aluno, Professor
from disciplina import Disciplina

# Responsável por salvar e carregar dados dos arquivos
class Persistencia:

    @staticmethod
    
    def carregar_alunos(nome_arquivo="alunos.txt", disciplinas_existentes=[]):
        alunos = []
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue
                    dados = linha.split("|")
                    nome, cpf, data_nascimento, matricula, *disciplinas_e_notas = dados
                    data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
                    aluno = Aluno(nome, cpf, data_nascimento, matricula)
                    for dn in disciplinas_e_notas:
                        if dn:
                            nome_disciplina, *notas = dn.split(",")
                            notas = list(map(float, notas))
                            disciplina = next((d for d in disciplinas_existentes if d.nome == nome_disciplina), None)
                            if disciplina:
                                aluno.matricular_em_disciplina(disciplina)
                                aluno.notas[disciplina] = notas
                    alunos.append(aluno)
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar alunos: {e}")
        return alunos


    @staticmethod
    def carregar_professores(nome_arquivo="professores.txt"):
        professores = []
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue  
                    dados = linha.split("|")
                    siape, nome, cpf, data_nascimento, disciplinas = dados
                    data_nascimento = datetime.strptime(
                        data_nascimento, "%Y-%m-%d").date()
                    professor = Professor(nome, cpf, data_nascimento, siape)
                    for nome_disciplina in disciplinas.split(","):
                        if nome_disciplina:
                            disciplina = Disciplina(
                                nome_disciplina, nome_disciplina)
                            professor.adicionar_disciplina(disciplina)
                    professores.append(professor)
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar professores: {e}")
        return professores

    @staticmethod
    def carregar_disciplinas(nome_arquivo="disciplinas.txt", professores=[]):
        disciplinas = []
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue  
                    dados = linha.split("|")
                    codigo, nome, professor_nome, alunos_nomes = dados
                    disciplina = Disciplina(codigo, nome)
                    if professor_nome:
                        for professor in professores:
                            if professor.nome == professor_nome:
                                disciplina.professor_responsavel = professor
                                break  
                    for aluno_nome in alunos_nomes.split(","):
                        if aluno_nome:
                            disciplina.alunos_matriculados.append(aluno_nome)
                    disciplinas.append(disciplina)
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar disciplinas: {e}")
        return disciplinas

    @staticmethod
    def salvar_alunos(alunos, nome_arquivo="alunos.txt"):
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                for aluno in alunos:
                    disciplinas_e_notas = []
                    for disciplina, notas in aluno.notas.items():
                        notas_str = ",".join(map(str, notas))
                        disciplinas_e_notas.append(f"{disciplina.nome},{notas_str}")
                    f.write(
                        f"{aluno.nome}|{aluno.cpf}|{aluno.data_nascimento.strftime('%Y-%m-%d')}|{aluno.matricula}|"
                        f"{'|'.join(disciplinas_e_notas)}\n")
        except Exception as e:
            print(f"Erro ao salvar alunos: {e}")

    @staticmethod
    def salvar_professores(professores, nome_arquivo="professores.txt"):
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                for professor in professores:
                    disciplinas = ",".join(
                        [disciplina.nome for disciplina in professor.disciplinas])
                    f.write(
                        f"{professor.siape}|{professor.nome}|{professor.cpf}|{professor.data_nascimento.strftime('%Y-%m-%d')}|"
                        f"{disciplinas}\n")
        except Exception as e:
            print(f"Erro ao salvar professores: {e}")

    @staticmethod
    def salvar_disciplinas(disciplinas, nome_arquivo="disciplinas.txt"):
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                for disciplina in disciplinas:
                    nome_professor = disciplina.professor_responsavel.nome if disciplina.professor_responsavel else "Nenhum"
                    alunos = ",".join(
                        [aluno.nome for aluno in disciplina.alunos_matriculados])
                    f.write(
                        f"{disciplina.codigo}|{disciplina.nome}|{nome_professor}|{alunos}\n")
        except Exception as e:
            print(f"Erro ao salvar disciplinas: {e}")