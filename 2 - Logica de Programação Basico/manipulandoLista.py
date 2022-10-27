#Juntando duas listas
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print('l1 =', l1)
print('l2 =', l2)
print('Juntando duas listas l1 + l2: ')
print('l1 + l2 =',l3)
print('-------------------------------------------')

#Adicionando valor no final da lista .append()
print('Adicionando valor no final da lista .append()')
l3.append(7)
print(l3)

#Adicionar um valor em qualquer índice da lista .insert()
print('Adicionar um valor em qualquer índice da lista .insert()')
l3.insert(1, 1.1)
l3.insert(0, 'inicio')
print(l3)

#Removendo o último valor da lista .pop()
print('Removendo o último valor da lista .pop()')
l3.pop()
print(l3)

#Removendo valor da lista por fatiamento .del()
print('Removendo valor da lista por fatiamento del(...)')
del(l3[0:3])
print(l3)
