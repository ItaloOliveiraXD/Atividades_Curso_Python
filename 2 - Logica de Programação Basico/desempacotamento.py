#Desempacotamento de lista.

lista = ['João', 'Maria', 'Sophia', 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Pegando os valores iniciais da lista.
valor1, valor2, *restoDaLista = lista
print(valor1, valor2)

#Pegando os valores finais da lista.
*_, elem1, eleme2  = lista #utiliza o (*_) para informa que não vai utilizar o resto da lista.
print(elem1, eleme2)
