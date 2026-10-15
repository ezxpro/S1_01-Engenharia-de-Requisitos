class Equipamento:
    '''Classe base de todos ativos do inventário'''
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