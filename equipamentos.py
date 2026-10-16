from tipos import TipoAtivo


class Equipamento:
    '''Classe base de todos ativos do inventário'''

    tipo = None # necessario porque ai cada subclasse vai ter seu proprio TipoAtivo
    fator_exposição = 1.0 # cibersegurança


    def __init__(self, id_equipamento, nome, responsavel, localizacao):
        self.id = id_equipamento
        self.nome = nome
        self.responsavel = responsavel
        self.localização = localização

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

    @nome.setter
    def nome(self, valor):
        self._nome = str(valor).strip()
        if valor == "" or valor.isnumeric():
            raise ValueError("Nome inválido: não pode ser vazio nem somente números")

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        valor = str(valor).strip()
        if valor == "" or not valor.replace(" ","").isalpha():
            raise ValueError( "Responsável inválido: somente letras"+
                             " não pode deixar em branco"  )
        self._responsavel = valor

    @property
    def localização(self):
        return self._localização

    @localização.setter
    def localização(self, valor):
        valor = str(valor).strip()
        if valor == "" or valor.isnumeric():
            raise ValueError("Localização inválida, não pode ser vázia nem só números.")
        self._localização = valor

    def to_dict(self):
        return {
            "id": self.id, 
            "nome": self.nome,
             "responsavel": self.responsavel, 
             "localização":self.responsavel, 
             "tipo": self.tipo,
        }

    @classmethod
    def from_dict(cls, dados):
        return criar_equipamento(dados["tipo"], dados["id"], dados["nome"],
                                 dados["responsavel"], dados["localizacao"])



class Desktop(Equipamento):
    tipo = TipoAtivo.DESKTOP
    fator_exposicao = 1.0


class Notebook(Equipamento):
    tipo = TipoAtivo.NOTEBOOK
    fator_exposicao = 1.1      # sai da rede da empresa


class Servidor(Equipamento):
    tipo = TipoAtivo.SERVIDOR
    fator_exposicao = 1.5


class Roteador(Equipamento):
    tipo = TipoAtivo.ROTEADOR
    fator_exposicao = 1.4


class SoftwareLicenciado(Equipamento):
    tipo = TipoAtivo.SOFTWARE_LICENCIADO
    fator_exposicao = 1.0


class SoftwareLivre(Equipamento):
    tipo = TipoAtivo.SOFTWARE_LIVRE
    fator_exposicao = 1.0


class AplicacaoWeb(Equipamento):
    tipo = TipoAtivo.APLICACAO_WEB
    fator_exposicao = 1.6      # exposta à internet


class Impressora(Equipamento):
    tipo = TipoAtivo.IMPRESSORA
    fator_exposicao = 0.8


CLASSES = {
    TipoAtivo.DESKTOP: Desktop,
    TipoAtivo.NOTEBOOK: Notebook,
    TipoAtivo.SERVIDOR: Servidor,
    TipoAtivo.ROTEADOR: Roteador,
    TipoAtivo.SOFTWARE_LICENCIADO: SoftwareLicenciado,
    TipoAtivo.SOFTWARE_LIVRE: SoftwareLivre,
    TipoAtivo.APLICACAO_WEB: AplicacaoWeb,
    TipoAtivo.IMPRESSORA: Impressora,
}


    def criar_equipamento(tipo, id_equipamento, nome, responsavel, localizacao):
        """Fábrica: escolhe a subclasse certa a partir do tipo."""
        return CLASSES[tipo](id_equipamento, nome, responsavel, localizacao)