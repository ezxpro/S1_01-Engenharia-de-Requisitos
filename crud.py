import tipos
from equipamentos import criar_equipamento
from vulnerabilidades import Vulnerabilidade, STATUS_VALIDOS


# ---------- funções de apoio ----------
def pedir_id(texto="Digite o ID do equipamento: "):
    """Pede um inteiro positivo. Devolve None se a entrada for inválida."""
    entrada = input(texto).strip()
    if not entrada.isdigit() or int(entrada) == 0:
        print("\nERRO: digite um número inteiro positivo.\n")
        return None
    return int(entrada)


def pedir_tipo(texto):
    for t in tipos.TipoAtivo:
        print(f"Categoria {t.name} → digite o código '{t.value}'")
    entrada = input(texto).strip()
    if entrada.isdigit() and int(entrada) in [t.value for t in tipos.TipoAtivo]:
        return int(entrada)
    return None


def mostrar(equipamento):
    print(f"\nID: {equipamento.id}\nNOME: {equipamento.nome}\n"
          f"RESPONSÁVEL: {equipamento.responsavel}\nLOCALIZAÇÃO: {equipamento.localizacao}\n"
          f"TIPO: {equipamento.tipo.name}")


# ---------- equipamentos ----------
def create(inv):
    while True:
        print('== CADASTRAR EQUIPAMENTO ==')
        id_equip = pedir_id("Digite o ID do equipamento: ")
        if id_equip is None:
            continue
        if inv.id_existe(id_equip):
            print(f"\nERRO: já existe um equipamento com ID {id_equip}.\n")
            continue
        nome = input("Digite o nome do equipamento: ")
        responsavel = input("Digite o nome do responsável: ")
        localizacao = input("Digite o setor/localização: ")
        tipo = pedir_tipo("Digite o código do tipo: ")
        if tipo is None:
            print("Código de tipo inválido.")
            continue
        try:
            equip = criar_equipamento(tipo, id_equip, nome, responsavel, localizacao)
            inv.cadastrar_equipamento(equip)
        except ValueError as erro:
            print(f"\nERRO: {erro}\n")
            continue
        print(f"Equipamento cadastrado → {equip.tipo.name}")

        while True:
            continuar = input("Deseja cadastrar outro? (s/n): ").strip().lower()
            if continuar == "s":
                break
            if continuar == "n":
                return
            print("Digite 's' ou 'n'.")


def read(inv):
    while True:
        print('== BUSCAR EQUIPAMENTO ==')
        print("1. Buscar por ID\n2. Buscar por nome\n3. Buscar por responsável\n0. Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        elif opcao == "1":
            id_equip = pedir_id()
            if id_equip is None:
                continue
            achados = [inv.buscar_equipamento(id_equip)] if inv.id_existe(id_equip) else []
        elif opcao == "2":
            achados = inv.buscar_por_nome(input("Nome (ou parte dele): "))
        elif opcao == "3":
            achados = inv.buscar_por_responsavel(input("Responsável (ou parte do nome): "))
        else:
            print("\nOpção inválida.\n")
            continue

        if not achados:
            print("\nNenhum equipamento encontrado.\n")
        for equip in achados:
            mostrar(equip)


def update(inv):
    print("== ATUALIZAR EQUIPAMENTO ==")
    id_equip = pedir_id()
    if id_equip is None:
        return
    equip = inv.buscar_equipamento(id_equip)
    if equip is None:
        print(f"\nERRO: não existe equipamento com ID {id_equip}.\n")
        return

    print("Deixe em branco e aperte Enter para manter o valor atual.")
    nome = input(f"Novo nome [{equip.nome}]: ").strip()
    responsavel = input(f"Novo responsável [{equip.responsavel}]: ").strip()
    localizacao = input(f"Nova localização [{equip.localizacao}]: ").strip()
    print(f"Tipo atual: {equip.tipo.name}")
    tipo = pedir_tipo("Novo código de tipo (Enter mantém): ")
    try:
        inv.atualizar_equipamento(id_equip, nome, responsavel, localizacao, tipo)
    except ValueError as erro:
        print(f"\nERRO: {erro}\n")
        return
    print("\nEquipamento atualizado com sucesso!\n")


def delete(inv):
    print('== DELETAR EQUIPAMENTO ==')
    id_equip = pedir_id()
    if id_equip is None:
        return
    if not inv.id_existe(id_equip):
        print(f"\nERRO: não existe equipamento com ID {id_equip}.\n")
        return
    if input(f"Tem certeza que deseja remover o equipamento {id_equip}? (s/n): ").strip().lower() == 's':
        inv.remover_equipamento(id_equip)
        print("\nEquipamento removido (e desassociado das vulnerabilidades).\n")
    else:
        print("\nOperação cancelada.\n")


# ---------- vulnerabilidades ----------
def cadastrar_vulnerabilidade(inv):
    print('== CADASTRAR VULNERABILIDADE ==')
    try:
        descricao = input("Descrição: ")
        categoria = input("Categoria (ex: software desatualizado, permissão indevida): ")
        severidade = input("Nota CVSS (0 a 10): ").replace(",", ".")
        print(f"Status - opções: {', '.join(STATUS_VALIDOS)}")
        status = input("Status: ")
        ids = input("IDs dos equipamentos afetados, separados por vírgula (Enter para nenhum): ")
        afetados = [int(x) for x in ids.split(",") if x.strip()]
        vuln = Vulnerabilidade(inv.proximo_id_vulnerabilidade(), descricao, categoria,
                               severidade, status, afetados)
        inv.cadastrar_vulnerabilidade(vuln)
    except ValueError as erro:
        print(f"\nERRO: {erro}\n")
        return
    print(f"\nVulnerabilidade {vuln.id} cadastrada com sucesso!\n")


def associar(inv):
    print('== ASSOCIAR EQUIPAMENTO A VULNERABILIDADE ==')
    id_vuln = pedir_id("ID da vulnerabilidade: ")
    id_equip = pedir_id("ID do equipamento: ")
    if id_vuln is None or id_equip is None:
        return
    try:
        inv.associar(id_vuln, id_equip)
    except ValueError as erro:
        print(f"\nERRO: {erro}\n")
        return
    print("\nAssociação feita com sucesso!\n")


def ver_vulnerabilidades(inv):
    print('== VER VULNERABILIDADES ==')
    id_equip = pedir_id()
    if id_equip is None:
        return
    equip = inv.buscar_equipamento(id_equip)
    if equip is None:
        print(f"\nERRO: não existe equipamento com ID {id_equip}.\n")
        return
    vulns = inv.vulnerabilidades_do_equipamento(id_equip)
    if not vulns:
        print(f"\n'{equip.nome}' não tem vulnerabilidades registradas.\n")
        return
    print(f"\nVULNERABILIDADES DE '{equip.nome}':")
    for v in vulns:
        print(f"  {v}")
    print()