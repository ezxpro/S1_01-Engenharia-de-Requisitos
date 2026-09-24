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


def read():
    while True:
        print('== BUSCAR ATIVO ==')
        print("""
        1. Buscar por ID
        2. Buscar por nome
        3. Buscar por responsável
        0. Sair""")

        opção = input("Entre com a opção de busca desejada: ").strip().lower()
        if not opção.isdigit():
            print("Opção inválida, digite um valor inteiro positivo.\n")
            continue
        else:
            opção = int(opção)
            match opção:
                case 1:
                    try:
                        id_ativo = int(input("Digite ID do ativo: "))
                        if id_ativo == 0:
                            raise ValueError
                    except ValueError:
                        print(f"\nERRO: Opção inválida. Digite um número inteiro positivo.\n")
                        continue

                    id_ativo = str(id_ativo)

                    ativo = ativos.buscar_ativo(id_ativo)
                    if ativo is None:
                        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
                        continue
                    else:
                        print(f"ATIVO ENCONTRADO COM SUCESSO:\nID: {ativo["id"]}\nNOME: {ativo["nome"]}\n"+
                              f"RESPONSÁVEL: {ativo["responsável"]}\n"f"LOCALIZAÇÃO: {ativo["localização"]}\n"
                              +f"TIPO: {ativo["tipo"]}")
                        
                case 2:
                    nome = input("Digite o nome a ser buscado: ").lower().strip()
                    if nome == "":
                        print("\nERRO: Valor inválido. O nome não pode estar")
                        continue

                    encontrados = False
                    for ativo in ativos.banco_ativos.values():
                        if nome in ativo["nome"].lower():
                            print(f"\nATIVO ENCONTRADO:\nID: {ativo['id']}\nNOME: {ativo['nome']}\n"
                                  f"RESPONSÁVEL: {ativo['responsável']}\nLOCALIZAÇÃO: {ativo['localização']}\n"
                                  f"TIPO: {ativo['tipo']}")
                            encontrados = True

                    if not encontrados:
                        print(f"\nNenhum ativo encontrado contendo o nome '{nome}'.\n")
                case 3:
                    responsavel = input("Digite o responsável a ser buscado: ").lower().strip()
                    if responsavel == "" or responsavel.replace(" ", "").isalpha() == False:
                        print("\nERRO: Valor inválido. Digite apenas letras.\n")
                        continue
                    
                    encontrados = False
                    for ativo in ativos.banco_ativos.values():
                        if responsavel in ativo["responsável"].lower():
                            print(f"\nATIVO ENCONTRADO:\nID: {ativo['id']}\nNOME: {ativo['nome']}\n"
                                  f"RESPONSÁVEL: {ativo['responsável']}\nLOCALIZAÇÃO: {ativo['localização']}\n"
                                  f"TIPO: {ativo['tipo']}")
                            encontrados = True
                            
                    if not encontrados:
                        print(f"\nNenhum ativo encontrado para o responsável '{responsavel}'.\n")
                
                case _:
                    print("\nOpção inválida. Escolha uma das opções do menu.\n")


def update():
    print("== ATUALIZAR ATIVO ==")
    id_ativo = input("Digite o ID do ativo que deseja atualizar: ").strip()

    ativo = ativos.buscar_ativo(id_ativo)
    if not ativo:
        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
        return

    print("Deixe o campo em branco e aperte Enter para manter o valor atual.")

    novo_nome = input(f"Novo nome [{ativo['nome']}]: ").strip()
    novo_responsavel = input(f"Novo responsável [{ativo['responsável']}]: ").strip()
    nova_localizacao = input(f"Nova localização [{ativo['localização']}]: ").strip()
    
    print(f"Tipo atual: {ativo['tipo']}")
    novo_tipo_str = input("Novo código de tipo de ativo: ").strip()
    
    novo_tipo = None
    if novo_tipo_str.isdigit():
        tipo_temp = int(novo_tipo_str)
        tipos_validos = [t.value for t in tipos.TipoAtivo]
        if tipo_temp in tipos_validos:
            novo_tipo = tipo_temp
        else:
            print("Tipo inválido. O tipo não será alterado.")

    ativos.atualizar_ativo(
        id_ativo, 
        nome=novo_nome if novo_nome else None, 
        responsável=novo_responsavel if novo_responsavel else None, 
        localização=nova_localizacao if nova_localizacao else None, 
        tipo=novo_tipo
    )
    print("\nAtivo atualizado com sucesso!\n")


def delete():
    print('== DELETAR ATIVO ==')
    id_ativo = input("Digite o ID do ativo que deseja remover: ").strip()
    
    if not ativos.id_existe(id_ativo):
        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
        return
    
    confirmacao = input(f"Tem a certeza que deseja remover o ativo {id_ativo}? (s/n): ").strip().lower()
    if confirmacao == 's':
        if ativos.deletar_ativo(id_ativo):
            print("\nAtivo removido com sucesso, incluindo todas as vulnerabilidades associadas!\n")
        else:
            print("\nOcorreu um erro ao remover o ativo.\n")
    else:
        print("\nOperação cancelada.\n")


def cadastrar_vulnerabilidade():
    print('== CADASTRAR VULNERABILIDADE ==')
    id_ativo = input("Digite o ID do ativo afetado: ").strip()
    
    if not ativos.id_existe(id_ativo):
        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
        return
        
    descricao = input("Descrição da vulnerabilidade: ").strip()
    if descricao == "":
        print("A descrição não pode estar vazia.")
        return
        
    categoria = input("Categoria/Tipo da vulnerabilidade (ex: software desatualizado, permissão indevida): ").strip()
    
    print("Severidade - Opções: baixa, média, alta, crítica")
    severidade = input("Digite a severidade: ").strip().lower()
    if severidade not in ["baixa", "média", "media", "alta", "crítica", "critica"]:
        print("Severidade inválida.")
        return
        
    print("Status - Opções: aberta, em tratamento, corrigida, aceita")
    status = input("Digite o status de tratamento: ").strip().lower()
    if status not in ["aberta", "em tratamento", "corrigida", "aceita"]:
        print("Status inválido.")
        return
        
    ativos.adicionar_vulnerabilidade(id_ativo, descricao, categoria, severidade, status)
    print("\nVulnerabilidade cadastrada com sucesso!\n")


def ver_vulnerabilidades():
    print('== VER VULNERABILIDADES ==')
    id_ativo = input("Digite o ID do ativo: ").strip()
    
    ativo = ativos.buscar_ativo(id_ativo)
    if not ativo:
        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
        return
        
    vulns = ativo.get("vulnerabilidades", [])
    if not vulns:
        print(f"\nO ativo '{ativo['nome']}' (ID: {id_ativo}) está sem vulnerabilidades registadas.\n")
    else:
        print(f"\nVULNERABILIDADES DO ATIVO '{ativo['nome']}' (ID: {id_ativo}):")
        for i, v in enumerate(vulns, 1):
            print(f"--- Vulnerabilidade {i} ---")
            print(f"Descrição: {v['descricao']}")
            print(f"Categoria: {v['categoria']}")
            print(f"Severidade: {v['severidade']}")
            print(f"Status: {v['status']}\n")