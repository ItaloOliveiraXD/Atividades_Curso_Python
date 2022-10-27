num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f'A soma dos números é = {num1 + num2}')
except:
    print('ERRO!, Digite um número inteiro válido!')
