from itertools import combinations, permutations, product

#combinations combina listas onde a ordem não importa e não combina valores ja combinados.
nomes = ['Italo', 'Felipe', 'Bruno', 'Fabricio', 'Luiz', 'Pedro']
print('Usando combinations')
for valor1, valor2 in combinations(nomes, 2):
    print(valor1, valor2)
print('-' * 80)

#permutation a ordem importa e combinam valores ja combinados
print('Usando permutation')
for valor1, valor2 in permutations(nomes, 2):
    print(valor1, valor2)
print('-' * 80)

#product faz todas as combinações possiveis e combinão valores iguais
print('Usando product')
for valor1, valor2 in product(nomes, repeat=2):
    print(valor1, valor2)
