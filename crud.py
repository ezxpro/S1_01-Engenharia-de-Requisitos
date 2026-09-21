import tipos
import ativos


def create():
    while True:
        print('== CADASTRAR ATIVO ==')
        try:
            id_ativo = int(input("Digite ID do ativo: "))
            if id_ativo == 0:
                raise ValueError
        except ValueError:
            print(f"\nERRO: Opção inválida. Digite um número inteiro positivo.\n")
            continue

        id_ativo = str(id_ativo) # converte essa bomba em string pra evitar problema depois

        if ativos.id_existe(id_ativo):
            print(f"\nERRO: já existe um ativo cadastrado com ID {id_ativo}. Tente outro.\n")
            continue

        nome = input("Digite o nome do ativo: ").strip()
        if nome == "":
            print("Nome inválido. Não pode estar em branco.")
            continue
        elif nome.isnumeric():
            print("Inválido, não pode conter apenas números.")
            continue

        responsável = input("Digite nome do responsável pelo ativo: ").strip()
        if responsável == "" or responsável.replace(" ", "").isalpha() == False:
            print("Nome do responsável inválido. Não pode estar em branco e deve conter somente letras.")
            continue

        localização = input("Digite o setor/localização do ativo: ").strip()
        if localização == "":
            print("Localização inválida. Nâo estar em branco.")
            continue

        elif localização.isnumeric():
            print("Localização inválida. Não pode ser valor numérico.")
            continue

        print("Digite o tipo do ativo. Tipos disponíveis: \n")
        tipos_disponíveis = set()
        for t in tipos.TipoAtivo:
            tipos_disponíveis.add(t.value)
            print(f"Categoria de ativo {t.name} → Digite código '{t.value}'")
        print('\n')
        try:
            tipo = int(input("Digite o código do tipo de ativo: "))
            if tipo not in tipos_disponíveis:
                raise ValueError

        except ValueError:
            print("Código digitado inválido, digite um dos códigos fornecidos")
            continue
        else:
            print(f"Ativo cadastrado com sucesso →  TIPO: {tipo} → {tipos.TipoAtivo(tipo).name} ")

        ativos.cadastrar_ativo(id_ativo=id_ativo, nome=nome, responsável=responsável, localização=localização, tipo=tipo)
        while True:
            continuar = input("Deseja cadastrar outro ativo? (s/n): ").strip().lower()  
            match continuar:
                case "s":
                    break
                case "n":
                    print("saindo...")
                    return
                case _:
                    print("Valor digitado incorreto. Por favor, digite 's' ou 'n'.")
                    continue