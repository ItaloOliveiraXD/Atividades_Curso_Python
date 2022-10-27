cpf = input('Digite seu CPF: ')
novoCpf = ''
cpfSemCaracter = ''
for numCpf in cpf:
    if numCpf.isnumeric():
        cpfSemCaracter += numCpf

# Validação primeiro digito.
novoCpf = cpfSemCaracter[0:9]

i = 10
somaValidacao1 = 0
for valor1 in novoCpf:
    valor1 = int(valor1)
    validacao1 = valor1 * i
    somaValidacao1 += validacao1
    i -= 1

formula = 11 - (somaValidacao1 % 11)     
digito1 = 0 if formula > 9 else formula
digito1 = str(digito1)
novoCpf += digito1

# Validação segundo digito.
i = 11
somaValidacao2 = 0
for valor2 in novoCpf:
    valor2 = int(valor2)
    validacao2 = valor2 * i
    somaValidacao2 += validacao2
    i -= 1

formula = 11 - (somaValidacao2 % 11)
digito2 = 0 if formula > 9 else formula
digito2 = str(digito2)
novoCpf += digito2

# Validção do cpf digitado
sequencia = cpf[0] * len(cpf)  # Exemplo: 11111111111, 66666666666, 99999999999.
if novoCpf == cpf and novoCpf != sequencia:
    print('CPF está válido!')
else:
    print('CPF está inválido!')
