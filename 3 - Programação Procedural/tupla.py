tupla1 = (1, 2, 3, 4) #Criando uma tupla.
tupla2 = 5, 6, 7, 8   #Outra maneira de criar tupla.
tupla3 = tupla1 + tupla2 #Concatenando tubla

tupla4 = tupla3[2:7] #Fatiando tupla.

v1, v2, v3, *_, vFinal1, vFinal2 = tupla3 #Desempacotando uma tupla

lista1 = list(tupla3)
print('Isso é uma tupla', tupla3)
print('Isso é uma lista', lista1)