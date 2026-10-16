import persistencia
from equipamentos import Equipamento
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

    def buscar_equipamento(self, id_equipamento):
        for e in self.equipamentos:
            if e.id == id_equipamento:
                return e
        return None

    def id_existe(self, id_equipamento):
        return self.buscar_equipamento(id_equipamento) is not None

    def cadastrar_equipamento(self, equipamento):
        if self.id_existe(equipamento.id):
            raise ValueError(f"Já existe um equipamento com ID {equipamento.id}.")
        self.equipamentos.append(equipamento)
        self.salvar()