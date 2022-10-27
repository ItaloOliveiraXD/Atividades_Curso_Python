# Tratando erros no python.
try:
    print(a)
except NameError as erro:
    print('Error')

print('Depois o código continua normalmente')

print('=' * 80)
try:
    a = [1, 2, 3, 4]
    print(a[6])
except NameError as erro:
    print('NameError, verifique o código novamente!')
except IndexError as erro:
    print('IndexErro, verifique o código novamente!')
except:
    print('Error inesperado!')
else:                                           # Sempre que try for executado else tbm será executado
    print('Seu código foi executado!')
finally:                                        # Sempre sera executado
    print('Sempre será executado')

print('Aqui o código continua normalmente.')
