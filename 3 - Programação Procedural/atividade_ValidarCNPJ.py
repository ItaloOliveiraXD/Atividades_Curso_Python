cnpj = '65.655.903/0001-56'
cnpj_semCaracter = ''

for valor in cnpj:
    if valor.isdigit():
        cnpj_semCaracter += valor

cnpj_teste = cnpj_semCaracter[0:-2]


def gerar_digito1():
    multiplicadores_digito1 = []
    for index in range(5, -7, -1):
        if index < 2:
            index += 8
        multiplicadores_digito1.append(index)

    soma_total = 0
    for i, valor1 in enumerate(cnpj_teste):
        valor1 = int(valor1)
        resultado_multiplicao = valor1 * multiplicadores_digito1[i]
        soma_total += resultado_multiplicao

    formula = 11 - (soma_total % 11)
    digito1 = 0 if formula > 9 else formula
    digito1 = str(digito1)
    return digito1


cnpj_teste += gerar_digito1()


def gerar_digito2():
    multiplicadores_digito2 = []
    for index in range(6, -7, -1):
        if index < 2:
            index += 8
        multiplicadores_digito2.append(index)

    soma_total = 0
    for i, valor2 in enumerate(cnpj_teste):
        valor2 = int(valor2)
        resultado = valor2 * multiplicadores_digito2[i]
        soma_total += resultado

    formula = 11 - (soma_total % 11)
    digito2 = 0 if formula > 9 else formula
    digito2 = str(digito2)
    return digito2


cnpj_teste += gerar_digito2()
sequencia = cnpj_semCaracter[0] * len(cnpj_semCaracter)
cnpj_com_caracter = f'{cnpj_teste[0:2]}.{cnpj_teste[2:5]}.{cnpj_teste[5:8]}/{cnpj_teste[8:12]}-{cnpj_teste[12:14]}'

if cnpj_teste == cnpj_semCaracter and cnpj_teste != sequencia:
    print(cnpj_com_caracter)
    print('CNPJ válido!')
else:
    print(cnpj_com_caracter)
    print('CNPJ Inválido!')
