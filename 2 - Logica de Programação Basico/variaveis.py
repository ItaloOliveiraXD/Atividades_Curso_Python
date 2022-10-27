"""
Inicia com letras, pode conter números, separar_, letras minúsculas.
"""
nome1= 'italo'
print(nome1, type(nome1))
print('----------------------------')

nome = 'Italo oliveira'
idade = 24
altura = 1.81
peso = 85.3
eMaiorDe18 = idade > 18
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso', peso)
print('É maior de idade:', eMaiorDe18)
print(f'Meu nome é {nome} tenho {idade} anos e meu imc é %.2f' % imc)
