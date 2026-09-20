import tipos
import ativos


def create():
    while True:
        print('== CADASTRAR ATIVO ==')
        try:
            id = int(input("Digite ID do ativo: "))
        except ValueError:
            print(f"\n\n\nERRO: Opção inválida. Digite um número inteiro.\n\n\n")
            continue
        nome = input("Digite o nome do ativo: ")
        responsável = input("Digite nome do responsável pelo ativo: ")
        localização = input("Digite o setor/localização do ativo: ")
        print("Digite o tipo do ativo. Tipos disponíveis: ")
        for t in tipos.TipoAtivo:
            print(f"Categoria de ativo {t.name} → Digite código '{t.value}'")
        try:
            tipo = int(input("Digite o código do tipo de ativo: "))
        except ValueError:
            print("Código digitado inválido, digite um dos códigos fornecidos")
            continue
    

        ativos.cadastrarAtivo(ID=id, nome=nome, responsável=responsável, localização=localização, tipo=tipo)
        continuar = input("Deseja cadastrar outro ativo? (s/n): ").strip.lower()
        while True:
            match continuar:
                case "s":
                    break
                case "n":
                    print("saindo...")
                    return
                case _:
                    print("Valor digitado incorreto. Por favor, digite 's' ou 'n'.")