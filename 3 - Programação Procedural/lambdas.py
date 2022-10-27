#Função para somar
def somar(num1, num2):
    return num1 + num2

resultado_Funcao = somar(5, 3)
print(f'Resultado usando função def: {resultado_Funcao}')

#Funçao Anônima(lambda).
x = lambda a, b: a + b
resultado_Lambda = x(4, 3)
print(f'Resultado usando lambdas: {resultado_Lambda}')

print('---------------------------------------------------------------------------------')

lista = [
    ['c', 5],
    ['i', 23],
    ['a', 12],
    ['f', 36],
    ['b', 3]
]

print(f'Lista original: \n{lista}\n')

# #Função def.
# print(f'Organizando com a funçao def: ')
#
# def func(item):
#     return item[1]
#
# lista.sort(key=func)
# print(lista, '\n')

#Função lambdas.
print(f'Organizando com função lambda: ')

lista.sort(key=lambda item: item[1])
print(lista, '\n')

print(f'Revertendo os valores da lista: ')
lista.sort(key=lambda i: i[1], reverse=True)
print(lista)


