from vendas.formatar_preco.preco_formatado import real


def aumento(valor, porcentagem, formatar=False):
    retorno = valor * (1 + porcentagem)
    if formatar:
        return real(retorno)
    else:
        return retorno


def reducao(valor, porcentagem, formatar=False):
    retorno = valor * (1 - porcentagem)
    if formatar:
        return real(retorno)
    else:
        return retorno
