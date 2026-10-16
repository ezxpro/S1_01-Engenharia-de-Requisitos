from crud import CRUD
from inventario import Inventario

# SISTEMA DE CADASTRO E GERENCIAMENTO DE EQUIPAMENTOS E VULNERABILIDADES


def main():
    crud = CRUD(Inventario())

    while True:
        print("== MENU ==")
        print('''Selecione uma das seguintes opções:
        1. Cadastrar equipamento
        2. Buscar equipamento
        3. Atualizar equipamento
        4. Deletar equipamento
        5. Cadastrar vulnerabilidade
        6. Ver vulnerabilidades de um equipamento
        7. Associar equipamento a uma vulnerabilidade
        0. Sair
        ''')

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("\nERRO: digite um número inteiro.\n")
            continue

        match opcao:
            case 0:
                print("Saindo do sistema...")
                break
            case 1:
                crud.create()
            case 2:
                crud.read()
            case 3:
                crud.update()
            case 4:
                crud.delete()
            case 5:
                crud.cadastrar_vulnerabilidade()
            case 6:
                crud.ver_vulnerabilidades()
            case 7:
                crud.associar()
            case _:
                print("\nOpção inválida.\n")


if __name__ == "__main__":
    main()