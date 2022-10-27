#Operação ternaria.
while True:
    idade = input('Informe sua idade: ')

    if idade.isnumeric():
        idade = int(idade)
    else:
        print('Informe uma idade válida!')
        continue

    if idade <= 0 or idade >= 110:
        print('Informe uma idade válida!')
    else:
        e_maior = 'Você é maior de idade!' if idade >= 18 else 'Você é menor de idade!' #operaçao ternária
        print(e_maior)
        break
