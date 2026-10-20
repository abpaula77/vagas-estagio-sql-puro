"""
Testes do CRUD usando um banco em memória (:memory:),
que é criado do zero a cada teste e some ao final.

    python -m unittest -v
"""
import sqlite3
import unittest

import crud


class CrudTest(unittest.TestCase):
    def setUp(self):
        self.conexao = crud.conectar(':memory:')
        crud.criar_tabela(self.conexao)

    def tearDown(self):
        self.conexao.close()

    def test_criar_vaga(self):
        id = crud.criar_vaga(self.conexao, 'Dev Python', 'Tech Campinas', '19 3333-1000')
        vaga = crud.buscar_vaga(self.conexao, id)
        self.assertEqual(vaga['titulo'], 'DEV PYTHON')
        self.assertEqual(vaga['empresa'], 'Tech Campinas')
        self.assertEqual(vaga['telefone'], '19 3333-1000')

    def test_listar_vazio(self):
        self.assertEqual(crud.listar_vagas(self.conexao), [])

    def test_listar_vagas(self):
        crud.criar_vaga(self.conexao, 'Vaga 1', 'Empresa A', '19 1111-1111')
        crud.criar_vaga(self.conexao, 'Vaga 2', 'Empresa B', '19 2222-2222')
        titulos = [vaga['titulo'] for vaga in crud.listar_vagas(self.conexao)]
        self.assertEqual(titulos, ['VAGA 1', 'VAGA 2'])

    def test_buscar_inexistente(self):
        self.assertIsNone(crud.buscar_vaga(self.conexao, 999))

    def test_atualizar_vaga(self):
        id = crud.criar_vaga(self.conexao, 'Vaga', 'Empresa A', '19 1111-1111')
        alteradas = crud.atualizar_vaga(self.conexao, id, 'Nova vaga', 'Empresa B', '19 2222-2222')
        self.assertEqual(alteradas, 1)
        vaga = crud.buscar_vaga(self.conexao, id)
        self.assertEqual(vaga['titulo'], 'NOVA VAGA')
        self.assertEqual(vaga['empresa'], 'Empresa B')

    def test_atualizar_inexistente(self):
        self.assertEqual(crud.atualizar_vaga(self.conexao, 999, 'X', 'Empresa', '19 0000-0000'), 0)

    def test_remover_vaga(self):
        id = crud.criar_vaga(self.conexao, 'Vaga', 'Empresa A', '19 1111-1111')
        self.assertEqual(crud.remover_vaga(self.conexao, id), 1)
        self.assertIsNone(crud.buscar_vaga(self.conexao, id))

    def test_remover_inexistente(self):
        self.assertEqual(crud.remover_vaga(self.conexao, 999), 0)

    def test_check_empresa_curta(self):
        with self.assertRaises(sqlite3.IntegrityError):
            crud.criar_vaga(self.conexao, 'Vaga', 'AB', '19 1111-1111')

    def test_check_ddd_invalido(self):
        with self.assertRaises(sqlite3.IntegrityError):
            crud.criar_vaga(self.conexao, 'Vaga', 'Empresa A', '11 1111-1111')

    def test_sql_injection_e_gravado_como_texto(self):
        titulo = "x'); DROP TABLE vaga; --"
        id = crud.criar_vaga(self.conexao, titulo, 'Empresa A', '19 1111-1111')
        self.assertEqual(crud.buscar_vaga(self.conexao, id)['titulo'], titulo.upper())


if __name__ == '__main__':
    unittest.main()
