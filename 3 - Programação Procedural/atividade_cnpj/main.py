from validando import isValido

cnpj = '87.560.615/0001-50'

if isValido(cnpj):
    print(cnpj)
    print('Esse cnpj é válido!')
else:
    print(cnpj)
    print('Esse cnpj é inválido!')
