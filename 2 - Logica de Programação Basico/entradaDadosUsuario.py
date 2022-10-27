"""
Entrada de dados pelo usuário.
input() Todo input retorna uma String
"""
nome = input('Qual seu nome? ')
ano_nascimento = int(input('Qual seu ano de nascimento? '))
idade = 2022 - ano_nascimento
print()
print(f'Usuário {nome} nasceu em {ano_nascimento} portanto tem '
      f'{idade} anos.')
print('-----------------------------------------------------------')

num_1 = int(input('Digite um número intero: '))  # cast direto no input
num_2 = input('Digite outro número inteiro: ')
num_2 = int(num_2)  # cast após o input
print('A soma dos números digitados é: ', num_1 + num_2)
