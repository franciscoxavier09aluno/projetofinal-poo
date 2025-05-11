
# Sistema de Gestão Acadêmica (Simples)

Este projeto simula um sistema básico de controle acadêmico em Python com menus interativos via terminal.

## Como executar

Certifique-se de que todos os arquivos `.py` estão na mesma pasta. Depois, execute o arquivo `menus.py` com:

```
python menus.py
```

## Funcionalidades principais

- Cadastro de alunos e professores
- Criação e gerenciamento de disciplinas
- Matrícula de alunos em disciplinas
- Lançamento de notas
- Relatórios de aprovados, reprovados, estatísticas gerais

## Estrutura dos arquivos

- `menus.py` – Arquivo principal (main), exibe os menus e opções.
- `pessoa.py` – Define as classes Pessoa, Aluno e Professor.
- `cadastro.py` – Lida com o cadastro e busca de entidades.
- `disciplina.py` – Classe que representa uma disciplina.
- `relatorio.py` – Geração de relatórios diversos.
- `persistencia.py` – Salva e carrega dados em arquivos `.txt`.

## Observações

- Os dados são salvos automaticamente em arquivos `.txt`.
- O sistema usa herança e programação orientada a objetos.
- A entrada de datas deve ser no formato `AAAA-MM-DD`.

## Exemplo de uso

1. Cadastrar aluno chamado João Silva.
2. Criar disciplina "Matemática" com código MAT101.
3. Matricular João Silva em MAT101.
4. Lançar nota 8.5 para ele em Matemática.
5. Ver no relatório que ele está aprovado.

