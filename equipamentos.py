class Equipamento:

"""Classe base de todos ativos do inventário"""

def __init__(self, id_equipamento, nome, responsavel, localizacao):
    self.id = id_equipamento
    self.nome = nome
    self.responsavel = responsavel
    self.localizacao = localizacao

# Cada atributo é validado no setter: não existe objeto inválido.
@property
def id(self):
    return self._id

@id.setter
def id(self, valor):
    if not isinstance(valor, int) or valor <= 0:
        raise ValueError("ID inválido: digite um número inteiro positivo.")
    self._id = valor

@property
def nome(self):
    return self._nome