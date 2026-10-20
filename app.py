"""
Menu de terminal para o CRUD de vagas.

    python app.py
"""
import sqlite3

import crud


def ler_id():
    texto = input('ID da vaga: ').strip()
    if not texto.isdigit():
        print('ID inválido.')
        return None
    return int(texto)


def ler_dados():
    titulo = input('Título: ').strip()
    empresa = input('Empresa: ').strip()
    telefone = input('Telefone (DDD 19): ').strip()
    return titulo, empresa, telefone


def mostrar(vaga):
    print(f"[{vaga['id']}] {vaga['titulo']} | {vaga['empresa']} | {vaga['telefone']}")


def cadastrar(conexao):
    novo_id = crud.criar_vaga(conexao, *ler_dados())
    print(f'Vaga cadastrada com o id {novo_id}.')


def listar(conexao):
    vagas = crud.listar_vagas(conexao)
    if not vagas:
        print('Nenhuma vaga cadastrada.')
    for vaga in vagas:
        mostrar(vaga)


def detalhar(conexao):
    id = ler_id()
    if id is None:
        return
    vaga = crud.buscar_vaga(conexao, id)
    if vaga is None:
        print('Vaga não encontrada.')
    else:
        mostrar(vaga)


def atualizar(conexao):
    id = ler_id()
    if id is None:
        return
    if crud.buscar_vaga(conexao, id) is None:
        print('Vaga não encontrada.')
        return
    crud.atualizar_vaga(conexao, id, *ler_dados())
    print('Vaga atualizada.')


def remover(conexao):
    id = ler_id()
    if id is None:
        return
    if crud.remover_vaga(conexao, id):
        print('Vaga removida.')
    else:
        print('Vaga não encontrada.')


OPCOES = {
    '1': ('Cadastrar', cadastrar),
    '2': ('Listar', listar),
    '3': ('Detalhar', detalhar),
    '4': ('Atualizar', atualizar),
    '5': ('Remover', remover),
}


def main():
    conexao = crud.conectar()
    crud.criar_tabela(conexao)
    while True:
        print('\n=== Vagas de Estágio ===')
        for chave, (nome, _) in OPCOES.items():
            print(f'{chave} - {nome}')
        print('0 - Sair')
        escolha = input('Opção: ').strip()
        if escolha == '0':
            break
        if escolha not in OPCOES:
            print('Opção inválida.')
            continue
        try:
            OPCOES[escolha][1](conexao)
        except sqlite3.IntegrityError as erro:
            # Disparado quando um NOT NULL ou CHECK do schema.sql é violado
            print(f'O banco recusou os dados: {erro}')
    conexao.close()


if __name__ == '__main__':
    main()
