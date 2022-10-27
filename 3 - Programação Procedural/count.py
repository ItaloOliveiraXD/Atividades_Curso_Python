from itertools import count

#Exemplo na pratica
contador = count()
nomes = ['Italo', 'Sophia', 'Lidiane', 'Yuri', 'Bruno', 'Fabricio']
lista_clientes = dict(zip(contador, nomes)) #Formando um dicionário
print(lista_clientes)

# Utilizando contador padrão.
contador1 = count()  # Count é infinito
lista1 = []
for valor in contador1:
    lista1.append(valor)
    if valor >= 10:
        break
print(lista1)

# Utilizando um número inicial no count
lista2 = []
contador2 = count(start=2)
for valor2 in contador2:
    lista2.append(valor2)
    if valor2 >= 10:
        break
print(lista2)

# Contando inversamente com count
contador3 = count(start=10, step=-1) #pode ser utilizado para pular passos.
lista3 = []
for valor3 in contador3:
    lista3.append(valor3)
    if valor3 <= 0:
        break
print(lista3)
