# iteráveis são apresentado todos os valores imediatamente
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # isso aqui é iterável
print('isso aqui é iterável', l1)
print('-' * 80)

# iterador são aprensetados um por um
for valor in l1:
    print('isso aqui é iterador da lista l1 ->', valor)
print('-' * 80)

# aqui também é um iterador
iterador = iter(l1)
print('Outra formar de iterador ->', next(iterador))
print('Outra formar de iterador ->', next(iterador))
print('Outra formar de iterador ->', next(iterador))
print('Outra formar de iterador ->', next(iterador))
print('-' * 80)

# Gerador não apresenta todos os valores, tem que pedir valor por valor para ser aprensentado pela funçao next() ou pelo for
l2 = (x for x in range(10))
print(next(l2), '-> esse número esta guardado pelo gerador')
print(next(l2), '-> esse número esta guardado pelo gerador')
print(next(l2), '-> esse número esta guardado pelo gerador')
print(next(l2), '-> esse número esta guardado pelo gerador')
print(next(l2), '-> esse número esta guardado pelo gerador')
print(next(l2), '-> esse número esta guardado pelo gerador')
