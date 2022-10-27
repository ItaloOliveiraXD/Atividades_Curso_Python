import re


def retirarCaracter(cnpj):
    return re.sub(r'\D', '', cnpj)


def colocarCaracter(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'


def retirandoDigito(cnpj):
    novo_cnpj = retirarCaracter(cnpj)
    return novo_cnpj[:-2]


def isSequencia(cnpj):
    novo_cnpj = retirarCaracter(cnpj)
    sequencia = novo_cnpj[0] * len(novo_cnpj)
    if sequencia == novo_cnpj:
        return True
    else:
        return False
