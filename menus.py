from pessoa import Pessoa
from pessoa import Aluno, Professor
from cadastro import Cadastro
from disciplina import Disciplina
from relatorio import Relatorio
from persistencia import Persistencia
from datetime import date

cadastro = Cadastro()

# Função principal que mostra o menu inicial do sistema
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Menu de Alunos")
        print("2. Menu de Professores")
        print("3. Menu de Disciplinas")
        print("4. Menu de Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_disciplinas()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "5":
            print("Salvando dados e saindo...")
            Persistencia.salvar_alunos(cadastro.alunos)
            Persistencia.salvar_professores(cadastro.professores)
            Persistencia.salvar_disciplinas(cadastro.disciplinas)
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu com opções para gerenciar alunos
def menu_alunos():
    while True:
        print("\n--- Menu de Alunos ---")
        print("1. Cadastrar novo Aluno")
        print("2. Listar Alunos")
        print("3. Buscar aluno por matrícula")
        print("4. Matricular aluno em disciplina")  
        print("5. Adicionar nota")  
        print("6. Desmatricular disciplina")  
        print("7. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data = input("Data de nascimento (AAAA-MM-DD): ")
                matricula = input("Matrícula: ")
                aluno = Aluno(nome, cpf, date.fromisoformat(data), matricula)
                cadastro.cadastrar_aluno(aluno)
            except ValueError as e:
                print(f"Erro ao cadastrar aluno: {e}")

        elif opcao == "2":
            cadastro.listar_todos(cadastro.alunos)

        elif opcao == "3":
            matricula = input("Digite a matrícula: ")
            aluno = cadastro.buscar_por_matricula(matricula)
            if aluno:
                aluno.exibir_dados()

        elif opcao == "4":  
            matricula = input("Digite a matrícula do aluno: ")
            aluno = cadastro.buscar_por_matricula(matricula)
            if aluno:
                codigo_disciplina = input("Digite o código da disciplina: ")
                disciplina = cadastro.buscar_por_codigo_disciplina(
                    codigo_disciplina)
                if disciplina:
                    aluno.matricular_em_disciplina(disciplina)
                    disciplina.adicionar_aluno(aluno)
                    Persistencia.salvar_alunos(cadastro.alunos)
                    Persistencia.salvar_disciplinas(cadastro.disciplinas)
                    print("Aluno matriculado na disciplina.")
                else:
                    print("Disciplina não encontrada.")
            else:
                print("Aluno não encontrado.")
        elif opcao == "5":  
            matricula = input("Digite a matrícula do aluno: ")
            aluno = cadastro.buscar_por_matricula(matricula)
            if aluno:
                codigo_disciplina = input("Digite o código da disciplina: ")
                disciplina = cadastro.buscar_por_codigo_disciplina(
                    codigo_disciplina)
                if disciplina in aluno.disciplinas:
                    try:
                        nota = float(input("Digite a nota: "))
                        aluno.adicionar_nota(disciplina, nota)
                        Persistencia.salvar_alunos(cadastro.alunos)
                        print("Nota adicionada.")
                    except ValueError:
                        print("Nota inválida. Digite um número.")
                else:
                    print("Aluno não matriculado nesta disciplina.")
            else:
                print("Aluno não encontrado.")

        elif opcao == "6": 
            matricula = input("Digite a matrícula do aluno: ")
            aluno = cadastro.buscar_por_matricula(matricula)
            if aluno:
                codigo_disciplina = input("Digite o código da disciplina: ")
                disciplina = cadastro.buscar_por_codigo_disciplina(
                    codigo_disciplina)
                if disciplina in aluno.disciplinas:
                    aluno.desmatricular_disciplina(disciplina)
                    disciplina.remover_aluno(aluno)
                    Persistencia.salvar_alunos(cadastro.alunos)
                    Persistencia.salvar_disciplinas(cadastro.disciplinas)
                    print("Aluno desmatriculado da disciplina.")
                else:
                    print("Aluno não matriculado nesta disciplina.")
            else:
                print("Aluno não encontrado.")

        elif opcao == "7":
            break
        else:
            print("Opção inválida.")

# Menu com opções para gerenciar professores
def menu_professores():
    while True:
        print("\n--- Menu de Professores ---")
        print("1. Cadastrar novo Professor")
        print("2. Listar Professores")
        print("3. Buscar professor por SIAPE")
        print("4. Atribuir disciplina ao professor")  
        print("5. Remover disciplina do professor")  
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data = input("Data de nascimento (AAAA-MM-DD): ")
                siape = input("SIAPE: ")
                professor = Professor(nome, cpf, date.fromisoformat(data), siape)
                cadastro.cadastrar_professor(professor)
            except ValueError as e:
                print(f"Erro ao cadastrar professor: {e}")

        elif opcao == "2":
            cadastro.listar_todos(cadastro.professores)

        elif opcao == "3":
            siape = input("Digite o SIAPE: ")
            professor = cadastro.buscar_por_siape(siape)
            if professor:
                professor.exibir_dados()

        elif opcao == "4":  
            siape = input("Digite o SIAPE do professor: ")
            professor = cadastro.buscar_por_siape(siape)
            if professor:
                codigo_disciplina = input("Digite o código da disciplina: ")
                disciplina = cadastro.buscar_por_codigo_disciplina(
                    codigo_disciplina)
                if disciplina:
                    professor.adicionar_disciplina(disciplina)
                    disciplina.adicionar_professor(professor)
                    Persistencia.salvar_professores(cadastro.professores)
                    Persistencia.salvar_disciplinas(cadastro.disciplinas)
                    print("Disciplina atribuída ao professor.")
                else:
                    print("Disciplina não encontrada.")
            else:
                print("Professor não encontrado.")

        elif opcao == "5": 
            siape = input("Digite o SIAPE do professor: ")
            professor = cadastro.buscar_por_siape(siape)
            if professor:
                codigo_disciplina = input("Digite o código da disciplina: ")
                disciplina = cadastro.buscar_por_codigo_disciplina(
                    codigo_disciplina)
                if disciplina in professor.disciplinas:
                    professor.remover_disciplina(disciplina)
                    disciplina.professor_responsavel = None
                    Persistencia.salvar_professores(cadastro.professores)
                    Persistencia.salvar_disciplinas(cadastro.disciplinas)
                    print("Disciplina removida do professor.")
                else:
                    print("Professor não leciona esta disciplina.")
            else:
                print("Professor não encontrado.")

        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

# Menu com opções para gerenciar disciplinas
def menu_disciplinas():
    while True:
        print("\n--- Menu de Disciplinas ---")
        print("1. Criar nova Disciplina")
        print("2. Listar Disciplinas")
        print("3. Buscar disciplina por código")
        print("4. Ver alunos matriculados na disciplina")  
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                codigo = input("Código da disciplina: ")
                nome = input("Nome da disciplina: ")
                disciplina = Disciplina(codigo, nome)
                cadastro.cadastrar_disciplina(disciplina)
            except ValueError as e:
                print(f"Erro ao cadastrar disciplina: {e}")

        elif opcao == "2":
            cadastro.listar_todos(cadastro.disciplinas)

        elif opcao == "3":
            codigo = input("Digite o código da disciplina: ")
            disciplina = cadastro.buscar_por_codigo_disciplina(codigo)
            if disciplina:
                disciplina.exibir_dados()

        elif opcao == "4": 
            codigo = input("Digite o código da disciplina: ")
            disciplina = cadastro.buscar_por_codigo_disciplina(codigo)
            if disciplina:
                print(f"\nAlunos matriculados em {disciplina.nome}:")
                if disciplina.alunos_matriculados:
                    for aluno in disciplina.alunos_matriculados:
                        print(f"- {aluno.nome}")
                else:
                    print("Nenhum aluno matriculado.")
            else:
                print("Disciplina não encontrada.")
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# Menu que mostra relatórios diversos sobre o sistema
def menu_relatorios():
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Alunos aprovados")
        print("2. Alunos reprovados")
        print("3. Professores com muitos alunos")
        print("4. Estatísticas gerais")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Relatorio.alunos_aprovados(cadastro.alunos)
        elif opcao == "2":
            Relatorio.alunos_reprovados(cadastro.alunos)
        elif opcao == "3":
            limite = int(input("Digite o número mínimo de alunos: "))
            Relatorio.professores_com_mais_alunos(cadastro.disciplinas, limite)
        elif opcao == "4":
            Relatorio.estatisticas_gerais(
                cadastro.alunos, cadastro.professores, cadastro.disciplinas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()