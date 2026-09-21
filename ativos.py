import persistencia

banco_ativos = persistencia.carregar_dados()

def cadastrarAtivo(id_ativo, nome, responsável, localização, tipo):
    ativo = {
    "id": id_ativo,
    "nome": nome,
    "responsável" : responsável,
    "localização": localização,
    "tipo": tipo,
    "vulnerabilidades": []
    }

    banco_ativos[id_ativo] = ativo

    return ativo