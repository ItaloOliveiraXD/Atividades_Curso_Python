'''
zip -> Unindo interáveis
zip_longest -> Itertools
'''

# Zip Unindo os interáveis de duas lista.
cidades = ['Fortaleza', 'Salvador', 'Natal', 'Recife', 'São Paulo', 'Rio de Janeiro', 'Coritiba']

estados = ['CE', 'BA', 'RN', 'PE']

print('Usando zip')
cidades_estados = zip(cidades, estados) #Isso retorna um gerador.

for valor in cidades_estados:
    print(valor[0],'-', valor[1])
print('-' * 80)


#Usando zip_longest
print('Usando zip_longest')
from itertools import zip_longest


todas_cidades_estados = zip_longest(cidades, estados, fillvalue='Não informado')

for valor in todas_cidades_estados:
    print(valor[0], '-', valor[1])
