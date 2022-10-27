lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40]

#Minha resolução
nova_lista = zip(lista1, lista2)
resultado_lista = []
for valor1, valor2 in nova_lista:
    soma = valor1 + valor2
    resultado_lista.append(soma)
print(resultado_lista)


#Resolução do professor
lista_nova = [x + y for x, y in zip(lista1, lista2)]
print(lista_nova)

#Outra atividade
from itertools import zip_longest
lista_outra_atividade = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
print(lista_outra_atividade)
