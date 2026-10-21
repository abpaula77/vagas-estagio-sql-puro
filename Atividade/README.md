# Atividade: Relatório do projeto CRUD de vagas

Nesta atividade você vai estudar o projeto de **CRUD de vagas com SQLite puro**
e produzir um relatório. O objetivo é mostrar que você entendeu como as peças
conversam entre si: o menu (`app.py`), as funções de banco (`crud.py`) e o SQL.

Leia o `README.md` da raiz do projeto antes de começar e rode o sistema ao menos uma vez.

## O que entregar

Entregue um documento (`relatorio.md` nesta mesma pasta, ou PDF) com as quatro
partes abaixo.

### 1. Como o projeto funciona

Explique, com suas palavras, o funcionamento geral do projeto:

- Qual é o objetivo da aplicação e o que é um CRUD.
- O caminho que um dado percorre quando o usuário cadastra uma vaga:
  do menu no terminal até o arquivo `vagas.db`.
- O papel de cada arquivo: `app.py`, `crud.py` e os scripts em `sql/`.

### 2. Exemplo de execução

Rode a aplicação (`python src/app.py`) e registre um exemplo real de uso:

- Cadastre pelo menos duas vagas, liste, atualize uma e remova outra.
- Cole no relatório a saída do terminal (ou capturas de tela) de cada passo.
- Descreva em uma frase o que cada passo fez.

### 3. Explicação de uma função

Escolha **uma** função do `crud.py` (`criar_vaga`, `listar_vagas`,
`buscar_vaga`, `atualizar_vaga` ou `remover_vaga`) e explique em detalhe:

- O comando SQL que ela executa e o que cada parte desse comando faz.
- Por que os valores são passados com o marcador `?` em vez de serem colados
  no texto do SQL.
- O que a função devolve e como `app.py` usa esse retorno.

### 4. Encontre o easter egg 🥚

Durante a aula vimos o CRUD funcionando com dados "bem-comportados".
Mas o projeto tem uma **regra escondida** que não foi comentada em aula: em
certas situações o banco simplesmente **se recusa a gravar** uma vaga.

Sua missão:

- Provoque esse comportamento. Tente cadastrar vagas com dados fora do comum
  e observe quando a gravação é recusada. (Dica: preste atenção no campo
  **empresa** e no campo **telefone**.)
- Descubra **onde** no projeto essa regra está definida e **como** ela é escrita.
- Explique **o que** exatamente é exigido de cada campo e o que acontece com a
  aplicação quando a regra é violada (qual erro aparece e de onde ele vem).
- Comente: por que vale a pena ter esse tipo de regra no próprio banco, e não
  só no código da aplicação?

## Critérios de avaliação

| Parte | Peso |
|---|---|
| 1. Como o projeto funciona | 25% |
| 2. Exemplo de execução | 25% |
| 3. Explicação de uma função | 25% |
| 4. Easter egg | 25% |

Clareza da escrita e organização contam. Prefira explicar com suas próprias
palavras a copiar os comentários do código.
