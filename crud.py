import tipos
from ativos import Equipamento, Vulnerabilidade

class CRUD:
    def __init__(self, inventario):
        self._inv = inventario

    @staticmethod
    def ler_id(texto):
        '''Pede um id ate receber um válido. Devolde ID se positivo ou None se 0'''
        entrada = input(texto).strip()
        if entrada.isdecimal():
            numero = int(entrada)
            return numero if numero > 0 else None
        print("\nERRO: Digite um número inteiro positivo (ou 0 para voltar).\n")
    
    def create(self):
        while True:
            print('== CADASTRAR ATIVO ==')
            id_ativo = self.ler_id("Digite o ID do ativo (0 para voltar):")
            if id_ativo is None:
                return
            if self._inv.id_existe(id_ativo):
                print(f"\nERRO: Já existe um ativo cadastrado com ID {id_ativo}. Tente outro.\n")
                continue

            nome = input("Digite o nome do ativo: ")
            responsavel = input("Digite o nome do responsável pelo ativo: ")
            localizacao = input("Digite o setor/localização do ativo: ")

            print("Digite o tipo do ativo. Tipos disponíveis: \n")
            for t in tipos.TipoAtivo:
                print(f"Categoria do ativo {t.name} → Digite código '{t.value}'")
            print()
            try:
                tipo = tipos.TipoAtivo(int(input("Digite o código do tipo de ativo: ")))
            except ValueError as erro:
                print(f"\nERRO: {erro}\n")
                continue

            while True:
                continuar = input("Deseja cadastrar outro ativo? (s/n): ").strip().lower()
                match continuar:
                    case "s":
                        break
                    case "n":
                        print("Saindo...")
                        return
                    case _:
                        print("Valor digiado incorreto. Por favor, digite 's' ou 'n'.")

    def read(self):
        while True:
            print("== BUSCAR ATIVO ==")
            print("""
        1. Buscar por ID
        2. Buscar por nome
        3. Buscar por responsável
        0. Retornar ao menu anterior""")

            opcao = input("Entre com a opção de busca desejada: ").strip()
            if not opcao.isdecimal():
                print("\nOpção inválida, digite um valor inteiro ositivo.\n")
                continue

            match int(opcao):
                case 1:
                    id_ativo = self.ler_id("Digite o ID do ativo (0 para voltar): ")
                    if id_ativo is None:
                        continue

                    ativo = self._inv.buscar(id_ativo)
                    if ativo is None:
                        print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.")
                        continue
                    print("\nATIVO ENCONTRADO COM SUCESSO:")
                    print(ativo)

                case 2:
                    nome = input("Digite o nome a ser buscado: ").strip()
                    if nome == "":
                        print("\nERRO: Valor inválido. O nome não pode estar em branco. \n")
                        continue

                    encontrados = self._inv.buscar_por_nome(nome)
                    for ativo in encontrados:
                        print("\nATIVO ENCONTRADO: ")
                        print(ativo)
                    if not encontrados:
                        print(f"\nNenhum ativo encontrado contendo o nome '{nome}'.\n")
                
                case 3:
                    responsavel = input("Digite o responsável a ser buscado: ").strip()
                    if responsavel == "":
                        print("\nERRO: Valor inválido. O responsável não pode estar em branco.\n")
                        continue

                    encontrados = self._inv.buscar_por_responsavel(responsavel)
                    for ativo in encontrados:
                        print("\nATIVO ENCONTRADO:")
                        print(ativo)
                    if not encontrados:
                        print(f"\nNenhum ativo encontrado para o responsável '{responsavel}'.\n")

                case 0:
                    return
                case _:
                    print("\nOpção inválida. Escolha uma das opções do menu.\n")

    def update(self):
        print("== ATUALIZAR ATIVO ==")
        id_ativo = self.ler_id("Digite o ID do ativo que deseja atualizar (0 para voltar): ")
        if id_ativo is None:
            return

        ativo = self._inv.buscar(id_ativo)
        if ativo is None:
            print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
            return

        print("Deixe o campo em branco e aperte Enter para manter o valor atual.")

        novo_nome = input(f"Novo nome [{ativo.nome}]: ").strip()
        novo_responsavel = input(f"Novo responsável [{ativo.responsavel}]: ").strip()
        nova_localizacao = input(f"Nova localização [{ativo.localizacao}]: ").strip()

        print(f"Tipo atual: {ativo.tipo.name}")
        for t in tipos.TipoAtivo:
            print(f"Categoria de ativo {t.name} → Digite código '{t.value}'")
        novo_tipo_str = input("Novo código de tipo de ativo: ").strip()

        novo_tipo = None
        if novo_tipo_str:
            try:
                novo_tipo = tipos.TipoAtivo(int(novo_tipo_str))
            except ValueError:
                print("Tipo inválido. O tipo não será alterado.")

        try:
            self._inv.atualizar(
                id_ativo,
                nome=novo_nome if novo_nome else None,
                responsavel=novo_responsavel if novo_responsavel else None,
                localizacao=nova_localizacao if nova_localizacao else None,
                tipo=novo_tipo
            )
        except ValueError as erro:
            print(f"\nERRO: {erro}\nNenhuma alteração foi feita.\n")
            return
        print("\nAtivo atualizado com sucesso!\n")

    def delete(self):
        print('== DELETAR ATIVO ==')
        id_ativo = self.ler_id("Digite o ID do ativo que deseja remover (0 para voltar): ")
        if id_ativo is None:
            return

        if not self._inv.id_existe(id_ativo):
            print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
            return

        confirmacao = input(f"Tem certeza que deseja remover o ativo {id_ativo}? (s/n): ").strip().lower()
        if confirmacao == "s":
            if self._inv.deletar(id_ativo):
                print("\nAtivo removido com sucesso, incluindo todas as vulnerabilidades associadas!\n")
            else:
                print("\nOcorreu um erro ao remover o ativo.\n")
        else:
            print("\nOperação cancelada.\n")

    def cadastrar_vulnerabilidade(self):
        print('== CADASTRAR VULNERABILIDADE ==')
        id_ativo = self.ler_id("Digite o ID do ativo afetado (0 para voltar): ")
        if id_ativo is None:
            return

        if not self._inv.id_existe(id_ativo):
            print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
            return

        descricao = input("Descrição da vulnerabilidade: ")
        categoria = input("Categoria/Tipo da vulnerabilidade (ex: software desatualizado, permissão indevida): ")
        print("Severidade - Opções: baixa, média, alta, crítica")
        severidade = input("Digite a severidade: ")
        print("Status - Opções: aberta, em tratamento, corrigida, aceita")
        status = input("Digite o status de tratamento: ")

        try:
            vulnerabilidade = Vulnerabilidade(descricao, categoria, severidade, status)
        except ValueError as erro:
            print(f"\nERRO: {erro}\n")
            return

        self._inv.adicionar_vulnerabilidade(id_ativo, vulnerabilidade)
        print("\nVulnerabilidade cadastrada com sucesso!\n")

    def ver_vulnerabilidades(self):
        print('== VER VULNERABILIDADES ==')
        id_ativo = self.ler_id("Digite o ID do ativo (0 para voltar): ")
        if id_ativo is None:
            return

        ativo = self._inv.buscar(id_ativo)
        if ativo is None:
            print(f"\nERRO: Não existe ativo cadastrado com ID {id_ativo}.\n")
            return

        if not ativo.vulnerabilidades:
            print(f"\nO ativo '{ativo.nome}' (ID: {id_ativo}) está sem vulnerabilidades registradas.\n")
            return

        print(f"\nVULNERABILIDADES DO ATIVO '{ativo.nome}' (ID: {id_ativo}):")
        for i, v in enumerate(ativo.vulnerabilidades, 1):
            print(f"--- Vulnerabilidade {i} ---")
            print(v)
            print()

    def ver_risco(self):
        print('== RISCO DOS ATIVOS ==')
        equipamentos = self._inv.listar()
        if not equipamentos:
            print("\nNenhum ativo cadastrado.\n")
            return
        for e in equipamentos:
            print(f"[{e.id}] {e.nome}: risco próprio = {e.risco_proprio():.2f} | risco efetivo = {e.risco_efetivo():.2f}")
        print("\n(valores fictícios por enquanto)\n")

    def ver_risco(self):
        print('== RISCO DOS ATIVOS ==')
        if not self.inv.equipamentos:
            print("\nNenhum ativo cadastrado.\n")
            return
        for e in self.inv.equipamentos.values():
            print(f"[{e.id}] {e.nome}: risco próprio = {e.risco_proprio():.2f} | risco efetivo = {e.risco_efetivo():.2f}")
        print("\n(valores fictícios por enquanto)\n")