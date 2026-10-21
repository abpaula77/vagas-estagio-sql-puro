# CRUD de vagas com SQLite puro

Cadastro de vagas de estágio **sem framework**: só Python e SQL.
O módulo `sqlite3` já vem com o Python, então não há nada para instalar.

## Estrutura do projeto

```
.
├── src/                 # código Python
│   ├── crud.py          # as quatro operações do CRUD em funções com SQL
│   ├── app.py           # menu no terminal que usa o crud.py
│   └── test_crud.py     # testes automatizados com banco em memória
├── sql/                 # scripts SQL
│   ├── schema.sql       # cria a tabela vaga (CREATE TABLE)
│   ├── dados_exemplo.sql# INSERTs para popular o banco
│   └── exercicios.sql   # roteiro de consultas para praticar
├── Atividade/           # atividade proposta aos alunos
│   └── README.md        # enunciado do relatório
├── vagas.db             # banco gerado ao rodar a aplicação (ignorado pelo git)
└── README.md
```

## Como rodar

A partir da raiz do projeto:

```console
python src/app.py                    # menu interativo; cria o arquivo vagas.db na raiz
python -m unittest discover -v -s src   # roda os testes
```

> O `app.py` e o `test_crud.py` fazem `import crud`, então os testes precisam
> enxergar a pasta `src/`. O `discover -s src` aponta a descoberta para lá.

## Vendo o banco por dentro

O banco é um único arquivo: `vagas.db`, criado na raiz do projeto. Para abrir:

- **DB Browser for SQLite** (https://sqlitebrowser.org, gratuito): *Abrir banco de dados* → `vagas.db`.
  Na aba *Navegar dados* aparecem os registros; na aba *Executar SQL* dá para rodar
  `sql/schema.sql`, `sql/dados_exemplo.sql` e `sql/exercicios.sql`.
- **Terminal**, se tiver o `sqlite3` instalado:

  ```console
  sqlite3 vagas.db
  sqlite> .read sql/schema.sql
  sqlite> .read sql/dados_exemplo.sql
  sqlite> .headers on
  sqlite> .mode column
  sqlite> SELECT * FROM vaga;
  ```

## CRUD ↔ SQL ↔ Python

| Operação | SQL | Função em `crud.py` |
|---|---|---|
| **C**reate | `INSERT INTO vaga (...) VALUES (?, ?, ?)` | `criar_vaga()` |
| **R**ead | `SELECT ... FROM vaga` / `... WHERE id = ?` | `listar_vagas()` / `buscar_vaga()` |
| **U**pdate | `UPDATE vaga SET ... WHERE id = ?` | `atualizar_vaga()` |
| **D**elete | `DELETE FROM vaga WHERE id = ?` | `remover_vaga()` |

## Pontos para discutir em aula

- **Parâmetros `?` × SQL injection**: os valores nunca são colados no texto do SQL.
  O teste `test_sql_injection_e_gravado_como_texto` mostra que o texto malicioso é gravado
  como texto comum e não executado.
- **`commit()`**: sem ele, as alterações não ficam gravadas no arquivo.
- **`WHERE` em UPDATE/DELETE**: sem ele, todas as linhas são afetadas (veja `sql/exercicios.sql`).

## Atividade para os alunos

Há uma atividade proposta na pasta [`Atividade/`](Atividade/README.md): construir um
relatório explicando o funcionamento do projeto, registrar um exemplo de execução,
detalhar uma função do `crud.py` e investigar o comportamento do sistema. Leia o
enunciado completo em `Atividade/README.md`.
