class AnaliseRisco:
    """Risco próprio e risco efetivo de cada equipamento.

    Por enquanto devolve valores fictícios (dummy). Na próxima entrega,
    calcular() passa a montar M, v e A e resolver (I - A) x = b.
    """

    def __init__(self, inventario):
        self.inv = inventario

    def calcular(self):
        """Devolve {id_equipamento: (risco_proprio, risco_efetivo)}."""
        resultado = {}
        for e in self.inv.equipamentos:
            proprio = 5.0 * e.fator_exposicao   # dummy
            efetivo = proprio * 2               # dummy
            resultado[e.id] = (proprio, efetivo)
        return resultado