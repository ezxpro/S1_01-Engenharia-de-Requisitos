import json

ARQUIVO = "banco_ativos.json"


def salvar_dados(banco_ativos):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(banco_ativos, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}