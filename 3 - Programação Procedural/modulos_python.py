from functools import reduce


# Criando um módulo em python para utilizar no seu código
def dobra_lista(lista):
    return [x * 2 for x in lista]


def media_lista(lista):
    total = reduce(lambda ac, l: l + ac, lista, 0)
    return total / len(lista)


# Essa condição serve para executar essas linhas de código somente na pasta principal onde ela se encontra.
if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    print(dobra_lista(numeros))
    print(media_lista(numeros))
