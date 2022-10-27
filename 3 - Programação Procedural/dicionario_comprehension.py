#Comprehension com dicionários.
lista = [
    ['chave1', 'valor da chave 1'],
    ['chave2', 'valor da chave 2'],
    ['chave3', 'valor da chave 3'],
    ['chave4', 'valor da chave 4'],
]

dicionarios = {x.upper(): y.title() for x, y in lista}
print(dicionarios)
