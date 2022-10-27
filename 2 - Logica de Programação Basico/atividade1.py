nome = 'Italo Oliveira'
idade = 25
altura = 1.81
peso = 85.7
anoAtual = 2022
anoNascimento = anoAtual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, tem {altura}cm de altura e pesa {peso}kg   ')
print(f'O IMC de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em: {anoNascimento}')
