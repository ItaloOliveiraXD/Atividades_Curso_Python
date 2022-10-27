import manipulando


def isValido(cnpj):
    listaMultiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpjSemDigito = manipulando.retirandoDigito(cnpj)
    novoCnpj = ''

    while True:
        if len(cnpjSemDigito) == 12:
            soma1 = 0
            for index, valor in enumerate(cnpjSemDigito, 1):
                valor = int(valor)
                soma1 += listaMultiplicadores[index] * valor

            formula = 11 - (soma1 % 11)
            digito1 = formula if formula <= 9 else 0
            cnpjSemDigito += str(digito1)
            novoCnpj = cnpjSemDigito

        elif len(cnpjSemDigito) == 13:
            soma2 = 0
            for index2, valor2 in enumerate(novoCnpj, 0):
                valor2 = int(valor2)
                soma2 += listaMultiplicadores[index2] * valor2

            formula = 11 - (soma2 % 11)
            digito2 = formula if formula <= 9 else 0
            novoCnpj += str(digito2)

            break

    novoCnpj = manipulando.colocarCaracter(novoCnpj)
    if novoCnpj == cnpj:
        if manipulando.isSequencia(novoCnpj):
            return False
        else:
            return True
    else:
        return False
