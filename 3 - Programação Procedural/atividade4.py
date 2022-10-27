def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

while True:
    numero = input('Informe um número: ')
    if numero.isnumeric():
        numero = int(numero)
        resultado = fizzBuzz(numero)
        print(resultado)
        break
    else:
        print('Isso não é um número!')
