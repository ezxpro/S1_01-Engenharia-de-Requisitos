import persistencia

banco_ativos = persistencia.carregar_dados()

def id_existe(id_ativo):
    return id_ativo in banco_ativos

def cadastrar_ativo(id_ativo, nome, responsável, localização, tipo):
    ativo = {
    "id": id_ativo,
    "nome": nome,
    "responsável" : responsável,
    "localização": localização,
    "tipo": tipo,
    "vulnerabilidades": []
    }

    # atualiza estado em memória
    banco_ativos[id_ativo] = ativo

    # aciona persistência para garantir que a alteração seja gravada no disco
    persistencia.salvar_dados(banco_ativos)

    return ativo

def buscar_ativo(id_ativo):
    return banco_ativos.get(id_ativo)