from random import randint

base = '0001'
corpo = randint(00000000, 99999999)
cnpj = str(corpo) + base


def gerar_digito1():
    multiplicadores_digito1 = []
    for index in range(5, -7, -1):
        if index < 2:
            index += 8
        multiplicadores_digito1.append(index)

    soma_total = 0
    for i, valor1 in enumerate(cnpj):
        valor1 = int(valor1)
        resultado_multiplicao = valor1 * multiplicadores_digito1[i]
        soma_total += resultado_multiplicao

    formula = 11 - (soma_total % 11)
    digito1 = 0 if formula > 9 else formula
    digito1 = str(digito1)
    return digito1


cnpj += gerar_digito1()


def gerar_digito2():
    multiplicadores_digito2 = []
    for index in range(6, -7, -1):
        if index < 2:
            index += 8
        multiplicadores_digito2.append(index)

    soma_total = 0
    for i, valor2 in enumerate(cnpj):
        valor2 = int(valor2)
        resultado = valor2 * multiplicadores_digito2[i]
        soma_total += resultado

    formula = 11 - (soma_total % 11)
    digito2 = 0 if formula > 9 else formula
    digito2 = str(digito2)
    return digito2


cnpj += gerar_digito2()
sequencia = cnpj[0] * len(cnpj)
cnpj_com_caracter = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
print(cnpj_com_caracter)
