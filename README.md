# CRUD com SQLite puro

O mesmo cadastro de vagas do projeto Django, agora **sem framework**: só Python e SQL.
O módulo `sqlite3` vem com o Python, então não há nada para instalar.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `schema.sql` | Cria a tabela `vaga` (`CREATE TABLE`) com as restrições `NOT NULL` e `CHECK` |
| `dados_exemplo.sql` | `INSERT`s para popular o banco |
| `crud.py` | As quatro operações do CRUD em funções Python com SQL |
| `app.py` | Menu no terminal que usa o `crud.py` |
| `test_crud.py` | Testes automatizados com banco em memória |
| `exercicios.sql` | Roteiro de consultas para praticar |

## Como rodar

```console
cd sql_puro
python app.py              # menu interativo; cria o arquivo vagas.db
python -m unittest -v      # roda os testes
```

## Vendo o banco por dentro

O banco é um único arquivo: `vagas.db`. Para abrir:

- **DB Browser for SQLite** (https://sqlitebrowser.org, gratuito): *Abrir banco de dados* → `vagas.db`.
  Na aba *Navegar dados* aparecem os registros; na aba *Executar SQL* dá para rodar
  `schema.sql`, `dados_exemplo.sql` e `exercicios.sql`.
- **Terminal**, se tiver o `sqlite3` instalado:

  ```console
  sqlite3 vagas.db
  sqlite> .read schema.sql
  sqlite> .read dados_exemplo.sql
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
- **Validação no banco**: as regras do formulário Django (empresa com 3 ou mais caracteres, DDD 19)
  viraram `CHECK` no `schema.sql`. Se forem violadas, o banco recusa a gravação com `sqlite3.IntegrityError`.
- **`WHERE` em UPDATE/DELETE**: sem ele, todas as linhas são afetadas (veja `exercicios.sql`).
- **ORM × SQL**: compare `crud.py` com `estagios/core/views.py`, onde o Django gera o mesmo SQL
  por baixo (`VagaModel.objects.create(...)` equivale a um `INSERT`).
