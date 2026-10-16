import json


def salvar_lista(arquivo, lista):
    """Grava uma lista de dicionários como um array de objetos JSON."""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


def carregar_lista(arquivo):
    """Lê o array de objetos JSON. Arquivo inexistente = lista vazia."""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []