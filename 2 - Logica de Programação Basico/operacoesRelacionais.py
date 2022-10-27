"""
Operadores relacionais
== igualdade
< menor que
<= menor que ou igual a
> maior que
>= maior que ou igual a
!= diferente
"""
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
# Idade mínima para fazer Empréstimo.
idade_minima = 18

print("'Análise 1'")
if idade >= idade_minima:
    print(f'{nome} está apto para fazer empréstimo. ')
else:
    print(f'{nome} NÃO está apto para fazer empréstimo')

print('----------------------------------------------------')

# Faixa de idade para fazer empréstimo
idade_menor = 20
idade_maior = 30
print("'Análise 2'")
if idade < idade_menor:
    print(f'{nome} NÃO está apto para fazer empréstimo')
elif idade > idade_maior:
    print(f'{nome} NÃO está apto para fazer empréstimo')
else:
    print(f'{nome} está apto para fazer empréstimo. ')
print('---------------------------------------------------')

# Faixa de idade para fazer empréstimo
idade_menor1 = 40
idade_maior1 = 50

print("'Análise 3'")
if idade >= idade_menor1 and idade <= idade_maior1:
    print(f'{nome} está apto para fazer empréstimo. ')
else:
    print(f'{nome} NÃO está apto para fazer empréstimo')
