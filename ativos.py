banco_ativos = {}

def cadastrarAtivo(ID, nome, responsável, localização, tipo):
    ativo = {
    "id": ID,
    "nome": nome,
    "responsável" : responsável,
    "localização": localização,
    "tipo": tipo,
    "vulnerabilidades": []
    }

    banco_ativos[ID] = ativo

    return ativo