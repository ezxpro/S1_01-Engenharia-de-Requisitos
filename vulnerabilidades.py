STATUS_VALIDOS = ("aberta", "em tratamento", "corrigida", "aceita")


class Vulnerabilidade:
    """Vulnerabilidade cadastrada, com a lista dos equipamentos que ela afeta."""

    def __init__(self, id_vuln, descricao, categoria, severidade, status="aberta",
                 equipamentos=None):
        self.id = id_vuln
        self.descricao = descricao
        self.categoria = categoria
        self.severidade = severidade    # nota CVSS de 0 a 10
        self.status = status
        self.equipamentos = [] if equipamentos is None else list(equipamentos)

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("A descrição não pode estar vazia.")
        self._descricao = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("A categoria não pode estar vazia.")
        self._categoria = valor

    @property
    def severidade(self):
        return self._severidade

    @severidade.setter
    def severidade(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("Severidade inválida: digite a nota CVSS (0 a 10).")
        if not 0 <= valor <= 10:
            raise ValueError("Severidade inválida: a nota CVSS vai de 0 a 10.")
        self._severidade = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        valor = str(valor).strip().lower()
        if valor not in STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Opções: {', '.join(STATUS_VALIDOS)}.")
        self._status = valor

    @property
    def classificacao(self):
        """Rótulo textual da nota CVSS (faixas oficiais do CVSS v3)."""
        if self.severidade >= 9.0:
            return "crítica"
        if self.severidade >= 7.0:
            return "alta"
        if self.severidade >= 4.0:
            return "média"
        if self.severidade > 0:
            return "baixa"
        return "nenhuma"

    def afeta(self, id_equipamento):
        return id_equipamento in self.equipamentos

    def associar(self, id_equipamento):
        if self.afeta(id_equipamento):
            raise ValueError("Esse equipamento já está associado à vulnerabilidade.")
        self.equipamentos.append(id_equipamento)

    def desassociar(self, id_equipamento):
        if id_equipamento in self.equipamentos:
            self.equipamentos.remove(id_equipamento)

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "severidade": self.severidade,
            "status": self.status,
            "equipamentos": self.equipamentos,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["id"], d["descricao"], d["categoria"], d["severidade"],
                   d["status"], d["equipamentos"])