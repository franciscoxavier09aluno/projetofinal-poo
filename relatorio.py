# Gera relatórios diversos sobre alunos, professores e disciplinas
class Relatorio:

    @staticmethod
    def alunos_aprovados(alunos):
        print("\n--- Alunos Aprovados (média >= 7) ---")
        for aluno in alunos:  
            for disciplina, notas in aluno.notas.items():
                if notas:
                    media = sum(notas) / len(notas)
                    if media >= 7:
                        aluno.exibir_dados()
                        print(f"Média em {disciplina.nome}: {media:.2f}")
                else:
                    print(f"Aluno {aluno.nome} não possui notas em {disciplina.nome}")

    @staticmethod
    def alunos_reprovados(alunos):
        print("\n--- Alunos Reprovados (média < 7) ---")
        for aluno in alunos:
            for disciplina, notas in aluno.notas.items():
                if notas:
                    media = sum(notas) / len(notas)
                    if media < 7:
                        aluno.exibir_dados()
                        print(f"Média em {disciplina.nome}: {media:.2f}")
                else:
                    print(f"Aluno {aluno.nome} não possui notas em {disciplina.nome}")

    @staticmethod
    def professores_com_mais_alunos(disciplinas, limite):
        print(f"\n--- Professores com mais de {limite} alunos ---")
        professores_alunos = {}
        for disciplina in disciplinas:
            if disciplina.professor_responsavel:
                nome_professor = disciplina.professor_responsavel.nome
                num_alunos = len(disciplina.alunos_matriculados)
                professores_alunos[nome_professor] = professores_alunos.get(
                    nome_professor, 0) + num_alunos

        for professor, num_alunos in professores_alunos.items():
            if num_alunos > limite:
                print(f"{professor}: {num_alunos} alunos")

    @staticmethod
    def estatisticas_gerais(alunos, professores, disciplinas):
        print("\n--- Estatísticas Gerais ---")
        print(f"Total de alunos: {len(alunos)}")
        print(f"Total de professores: {len(professores)}")
        print(f"Total de disciplinas: {len(disciplinas)}")

        total_notas = 0
        total_disciplinas_com_notas = 0
        for aluno in alunos:
            for disciplina, notas in aluno.notas.items():
                if notas:
                    total_notas += sum(notas) / len(notas)
                    total_disciplinas_com_notas += 1

        if total_disciplinas_com_notas > 0:
            media_geral = total_notas / total_disciplinas_com_notas
            print(f"Média geral de notas por disciplina: {media_geral:.2f}")
        else:
            print("Nenhuma nota registrada.")