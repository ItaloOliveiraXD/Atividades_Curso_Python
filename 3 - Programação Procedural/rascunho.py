lista_Atividade = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [0, 5, 6, 8, 1, 3, 4, 9, 10, 9],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
]

l0, l1, l2, l3, l4 = lista_Atividade


def valor_da_lista(lista, index):
    i = 0
    j = 1
    while i < 10:
        if lista[i] == lista_Atividade[index][j]:
            valor = lista[i]
            break
        i += 1
        j += 1
        if j == 10:
            valor = -1
            break
    return valor


numero_da_lista = valor_da_lista(l0, 0)
numero_da_lista1 = valor_da_lista(l1, 1)
numero_da_lista2 = valor_da_lista(l2, 2)
numero_da_lista3 = valor_da_lista(l3, 3)
numero_da_lista4 = valor_da_lista(l4, 4)
print(numero_da_lista, numero_da_lista1, numero_da_lista2, numero_da_lista3, numero_da_lista4)
