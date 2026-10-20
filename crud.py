"""
CRUD de vagas de estágio usando apenas SQL e o módulo sqlite3
(biblioteca padrão do Python, nada a instalar).

    C - Create -> INSERT  -> criar_vaga()
    R - Read   -> SELECT  -> listar_vagas() / buscar_vaga()
    U - Update -> UPDATE  -> atualizar_vaga()
    D - Delete -> DELETE  -> remover_vaga()

Importante: os valores NUNCA são colados no texto do SQL (f-string ou +).
Usamos o marcador ? e passamos os valores separados. Isso evita SQL injection.
"""
import sqlite3
from pathlib import Path

PASTA = Path(__file__).parent
ARQUIVO_BANCO = PASTA / 'vagas.db'
ARQUIVO_SCHEMA = PASTA / 'schema.sql'


def conectar(caminho=ARQUIVO_BANCO):
    """Abre (ou cria, se não existir) o arquivo do banco."""
    conexao = sqlite3.connect(caminho)
    # Permite acessar as colunas pelo nome: vaga['titulo']
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela(conexao):
    """Executa o schema.sql (CREATE TABLE IF NOT EXISTS ...)."""
    conexao.executescript(ARQUIVO_SCHEMA.read_text(encoding='utf-8'))


def criar_vaga(conexao, titulo, empresa, telefone):
    """INSERT: grava uma nova vaga e devolve o id gerado."""
    sql = 'INSERT INTO vaga (titulo, empresa, telefone) VALUES (?, ?, ?)'
    cursor = conexao.execute(sql, (titulo.upper(), empresa, telefone))
    conexao.commit()
    return cursor.lastrowid


def listar_vagas(conexao):
    """SELECT: devolve todas as vagas ordenadas pelo id."""
    sql = 'SELECT id, titulo, empresa, telefone FROM vaga ORDER BY id'
    return conexao.execute(sql).fetchall()


def buscar_vaga(conexao, id):
    """SELECT com WHERE: devolve uma vaga ou None se o id não existir."""
    sql = 'SELECT id, titulo, empresa, telefone FROM vaga WHERE id = ?'
    return conexao.execute(sql, (id,)).fetchone()


def atualizar_vaga(conexao, id, titulo, empresa, telefone):
    """UPDATE: altera uma vaga. Devolve quantas linhas foram alteradas (0 ou 1)."""
    sql = 'UPDATE vaga SET titulo = ?, empresa = ?, telefone = ? WHERE id = ?'
    cursor = conexao.execute(sql, (titulo.upper(), empresa, telefone, id))
    conexao.commit()
    return cursor.rowcount


def remover_vaga(conexao, id):
    """DELETE: remove uma vaga. Devolve quantas linhas foram removidas (0 ou 1)."""
    sql = 'DELETE FROM vaga WHERE id = ?'
    cursor = conexao.execute(sql, (id,))
    conexao.commit()
    return cursor.rowcount
