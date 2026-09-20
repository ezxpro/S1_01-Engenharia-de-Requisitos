from tipos import TipoAtivo
import ativos
import persistencia
import crud


def main():

    while True:
        print("Bem vindo ao Sistema de Cadastro e Gerenciamento de Ativos de TI")
        print("== MENU ==")
        print('''Selecione uma das seguintes opções:
        1. Cadastrar ativo
        2. Buscar ativo
        3. Atualizar ativo
        4. Deletar ativo
        5. Cadastrar vulnerabilidades
        6. Ver vulnerabilidades de um ativo
        0. Sair
        ''')
        
        try:
            opção = int(input("Digite sua opção: "))
        except ValueError:
            print(f"\n\n\nERRO: Opção inválida. Digite um número inteiro.\n\n\n")
        else:
            match opção:
                case 1:
                    crud.create()
                case _:
                    break
                    



                    



if __name__ == "__main__":
    main()
