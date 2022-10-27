def conferir_numero(valor):
    try:
        valor = int(valor)
        return valor
    except (TypeError, ValueError):
        try:
            valor = float(valor)
            return valor
        except (TypeError, ValueError):
            pass


while True:
    print('Informe 2 números para multiplicar.')
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    num1 = conferir_numero(num1)
    num2 = conferir_numero(num2)

    if num1 is not None and num2 is not None:
        print(f'Resultado: {num1 * num2}')
        break
    else:
        print('Error: DIGITE APENAS NÚMEROS!')
