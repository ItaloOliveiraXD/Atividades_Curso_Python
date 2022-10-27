cpf = input('Informe seu cpf: ')
cpf_Provisorio = ''
novo_Cpf = ''

for valor in cpf:
    if valor.isnumeric():
        cpf_Provisorio += valor

novo_Cpf = cpf_Provisorio[:9]


def gerarPrimeiroDigito():
    multiplicador1 = 10
    resultadoDigito1 = 0
    for valor1 in novo_Cpf:
        valor1 = int(valor1)
        produto1 = valor1 * multiplicador1
        resultadoDigito1 += produto1
        multiplicador1 -= 1

    formula = 11 - (resultadoDigito1 % 11)
    primeiroDigito = 0 if formula > 9 else formula
    primeiroDigito = str(primeiroDigito)
    return primeiroDigito


novo_Cpf += gerarPrimeiroDigito()


def gerarSegundoDigito():
    multiplicador2 = 11
    resuldadoDigito2 = 0
    for valor2 in novo_Cpf:
        valor2 = int(valor2)
        produto2 = valor2 * multiplicador2
        resuldadoDigito2 += produto2
        multiplicador2 -= 1

    formula = 11 - (resuldadoDigito2 % 11)
    segundoDigito = 0 if formula > 9 else formula
    segundoDigito = str(segundoDigito)
    return segundoDigito


novo_Cpf += gerarSegundoDigito()

sequencia = cpf[0] * 11
cpf_Correto_comCaracter = f'{novo_Cpf[0:3]}.{novo_Cpf[3:6]}.{novo_Cpf[6:9]}-{novo_Cpf[9:12]}'
cpf_Errado_comCaracter = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:12]}'

if novo_Cpf == cpf_Provisorio and cpf_Provisorio != sequencia:
    print(cpf_Correto_comCaracter)
    print('CPF válido!')
else:
    print(cpf_Errado_comCaracter)
    print('CPF inválido!')
