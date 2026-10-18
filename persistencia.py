import json


class Persistencia:
    def __init__(self, arquivo="banco_ativos.json"):
        self.arquivo = arquivo

    def salvar(self, lista):
        with open(self.arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []