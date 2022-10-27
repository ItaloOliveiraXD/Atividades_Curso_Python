'''Fazendo uma calculadora'''
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Número digitado é inválido!')
        continue

    num1 = int(num1)
    num2 = int(num2)
    operador = input('Escolha um operador para fazer o calculo.')

    if operador == '+':
        print(f'Resultado: {num1 + num2}')
    elif operador == '-':
        print(f'Resultado: {num1 - num2}')
    elif operador == '*':
        print(f'Resultado: {num1 * num2}')
    elif operador == '/':
        print(f'Resultado: {num1 / num2}')

    sair = input('Deseja sair? [s]im [n]ão ')

    if sair == 's':
        break
