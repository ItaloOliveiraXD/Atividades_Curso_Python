#Criando uma lista aparti da função range
print('Criando uma lista aparti da função range()')
lista = list(range(0,10)) #é a mesma coisa que -> lista = [0,1,2,3,4,5,6,7,8,9]
print(lista)
print('----------------------------------------------------')

listaVariada = ['texto', True, 10, -20.5]
print(listaVariada)
for elem in listaVariada:
    print(f'O tipo do elemento ({elem}) é {type(elem)}')
