import persistencia
from equipamentos import Equipamento, criar_equipamento
from vulnerabilidades import Vulnerabilidade


class Inventario:
    """Guarda os equipamentos e as vulnerabilidades e cuida da persistência."""

    def __init__(self, arq_equipamentos="equipamentos.json",
                 arq_vulnerabilidades="vulnerabilidades.json"):
        self.arq_equipamentos = arq_equipamentos
        self.arq_vulnerabilidades = arq_vulnerabilidades
        self.equipamentos = [Equipamento.from_dict(d)
                             for d in persistencia.carregar_lista(arq_equipamentos)]
        self.vulnerabilidades = [Vulnerabilidade.from_dict(d)
                                 for d in persistencia.carregar_lista(arq_vulnerabilidades)]

    def salvar(self):
        persistencia.salvar_lista(self.arq_equipamentos,
                                  [e.to_dict() for e in self.equipamentos])
        persistencia.salvar_lista(self.arq_vulnerabilidades,
                                  [v.to_dict() for v in self.vulnerabilidades])

    # ---------- equipamentos ----------
    def id_existe(self, id_equipamento):
        return self.buscar_equipamento(id_equipamento) is not None

    def cadastrar_equipamento(self, equipamento):
        if self.id_existe(equipamento.id):
            raise ValueError(f"Já existe um equipamento com ID {equipamento.id}.")
        self.equipamentos.append(equipamento)
        self.salvar()

    def buscar_equipamento(self, id_equipamento):
        for e in self.equipamentos:
            if e.id == id_equipamento:
                return e
        return None

    def buscar_por_nome(self, trecho):
        trecho = trecho.strip().lower()
        return [e for e in self.equipamentos if trecho in e.nome.lower()]

    def buscar_por_responsavel(self, trecho):
        trecho = trecho.strip().lower()
        return [e for e in self.equipamentos if trecho in e.responsavel.lower()]

    def atualizar_equipamento(self, id_equipamento, nome=None, responsavel=None,
                              localizacao=None, tipo=None):
        e = self.buscar_equipamento(id_equipamento)
        if e is None:
            raise ValueError(f"Não existe equipamento com ID {id_equipamento}.")
        if nome:
            e.nome = nome
        if responsavel:
            e.responsavel = responsavel
        if localizacao:
            e.localizacao = localizacao
        if tipo is not None and tipo != e.tipo.value:
            # o tipo é da classe, então troca-se o objeto por outro da subclasse certa
            novo = criar_equipamento(tipo, e.id, e.nome, e.responsavel, e.localizacao)
            self.equipamentos[self.equipamentos.index(e)] = novo
        self.salvar()

    def remover_equipamento(self, id_equipamento):
        e = self.buscar_equipamento(id_equipamento)
        if e is None:
            return False
        self.equipamentos.remove(e)
        for v in self.vulnerabilidades:
            v.desassociar(id_equipamento)
        self.salvar()
        return True

    # ---------- vulnerabilidades ----------
    def proximo_id_vulnerabilidade(self):
        return max((v.id for v in self.vulnerabilidades), default=0) + 1

    def buscar_vulnerabilidade(self, id_vuln):
        for v in self.vulnerabilidades:
            if v.id == id_vuln:
                return v
        return None

    def cadastrar_vulnerabilidade(self, vulnerabilidade):
        for id_equip in vulnerabilidade.equipamentos:
            if not self.id_existe(id_equip):
                raise ValueError(f"Não existe equipamento com ID {id_equip}.")
        self.vulnerabilidades.append(vulnerabilidade)
        self.salvar()

    def associar(self, id_vuln, id_equipamento):
        v = self.buscar_vulnerabilidade(id_vuln)
        if v is None:
            raise ValueError(f"Não existe vulnerabilidade com ID {id_vuln}.")
        if not self.id_existe(id_equipamento):
            raise ValueError(f"Não existe equipamento com ID {id_equipamento}.")
        v.associar(id_equipamento)
        self.salvar()

    def vulnerabilidades_do_equipamento(self, id_equipamento):
        return [v for v in self.vulnerabilidades if v.afeta(id_equipamento)]