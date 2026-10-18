from tipos import TipoAtivo
import persistencia

banco_ativos = persistencia.carregar_dados()

def id_existe(id_ativo):
    return id_ativo in banco_ativos

def cadastrar_ativo(id_ativo, nome, responsável, localização, tipo):
    ativo = {
    "id": id_ativo,
    "nome": nome,
    "responsável" : responsável,
    "localização": localização,
    "tipo": tipo,
    "vulnerabilidades": []
    }

    # atualiza estado em memória
    banco_ativos[id_ativo] = ativo

    # aciona persistência para garantir que a alteração seja gravada no disco
    persistencia.salvar_dados(banco_ativos)

    return ativo

def buscar_ativo(id_ativo):
    return banco_ativos.get(id_ativo)

def buscar_ativos_por_nome(nome):
    # Corrigido: adicionado parênteses na chamada de .values()
    for ativo in banco_ativos.values():
        if nome.strip().lower() == ativo["nome"].lower():
            return ativo
    return None

def atualizar_ativo(id_ativo, nome=None, responsável=None, localização=None, tipo=None):
    if id_ativo in banco_ativos:
        if nome:
            banco_ativos[id_ativo]["nome"] = nome
        if responsável:
            banco_ativos[id_ativo]["responsável"] = responsável
        if localização:
            banco_ativos[id_ativo]["localização"] = localização
        if tipo:
            banco_ativos[id_ativo]["tipo"] = tipo
        
        persistencia.salvar_dados(banco_ativos)
        return True
    return False

def deletar_ativo(id_ativo):
    if id_ativo in banco_ativos:
        del banco_ativos[id_ativo]
        persistencia.salvar_dados(banco_ativos)
        return True
    return False

def adicionar_vulnerabilidade(id_ativo, descricao, categoria, severidade, status):
    if id_ativo in banco_ativos:
        vulnerabilidade = {
            "descricao": descricao,
            "categoria": categoria,
            "severidade": severidade,
            "status": status
        }
        banco_ativos[id_ativo]["vulnerabilidades"].append(vulnerabilidade)
        persistencia.salvar_dados(banco_ativos)
        return True
    return False

class Vulnerabilidade:
    def __init__(self, descricao, categoria, severidade, status):
        self.descricao = descricao
        self.categoria = categoria
        self.severidade = severidade
        self.status = status

        def __str__(self):
            return ( f"Descrição: {self.descricao}\n"
                f"Categoria: {self.categoria}\n"
                f"Severidade: {self.severidade}\n"
                f"Status: {self.status}"
            )

        def to_dict(self):
            return {
                "descricao": self.descricao,
                "categoria": self.categoria,
                "severidade": self.severidade,
                }
        @classmethod
        def from_dict():
            return cls(dados["descricao"], dados["categoria"],
                    dados["severidade"], dados["status"])

class Equipamento:
    def __init__(self, id_equipamento, nome, responsavel, localizacao, tipo):
        self.id = id_equipamento
        self.nome = nome
        self. responsavel = responsavel
        self. localizacao = localizacao
        self.tipo = tipo
        self.vulnerabilidades = []

def adicionar_vulnerabilidades(self, vulnerabilidade):
    self.vulnerabilidades.append(vulnerabilidade)


def __str__(self):
    return (f"ID: {self.id}"
            f"NOME: {self.nome}"
            f"RESPONSÁVEL: {self.responsavel}"
            f"LOCALIZAÇÃO: {self.localizacao}"
            f"TIPO: {self.tipo.nome}"
            )