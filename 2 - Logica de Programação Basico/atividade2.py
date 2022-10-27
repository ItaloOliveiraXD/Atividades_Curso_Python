number = input('Digite um número inteiro para verificar se é par ou ímpar: ')

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f'{number} é par!')
    else:
        print(f'{number} é ímpar!')
else:
    print(f'{number} não é um número inteiro!')

'''
try:
    number = int(number)

    if number % 2 == 0:
        print(f'{number} é par!')
    else:
        print(f'{number} é ímpar!')
except:
    print(f'{number} não é um número inteiro!')
'''