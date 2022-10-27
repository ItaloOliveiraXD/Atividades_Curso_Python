num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')

# isnumeric() isdigit() isdecimal()
# Checam se a string pode ser transformada em int
# so retorna true somente se for utilizado número inteiro e positivo.
print('Primeira forma.')
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(f'A soma dos números é = {num1 + num2}')
else:
    print('Número digitado não é inteiro!')

# Outra forma de tentar utilizando números rais e negatios é:

print('Segunda forma.')
import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)
    print(f'A soma dos números é: {num1 + num2}')
else:
    print('ERRO!')
