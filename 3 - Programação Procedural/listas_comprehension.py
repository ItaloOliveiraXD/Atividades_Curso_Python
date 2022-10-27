# Modificando valores em conjutos(Listas, Sets, Tuplas, Dicionários) em uma linha.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [valor * 2 for valor in l1]
print(ex1)

l2 = ['Italo', 'Sophia', 'Lidiane']
ex2 = [valor.replace('a', '@') for valor in l2]
print(ex2)

l3 = (
    ('Italo', 'Programador'),
    ('Lidia', 'Vendedora'),
    ('Sophia', 'Modelo'),
)
ex3 = [(chave, valor) for chave, valor in l3]
ex3 = dict(ex3)
print(ex3)

l4 = list(range(50))
ex4 = [valor for valor in l4 if valor % 2 == 0 and valor % 5 == 0]
print(ex4)

# [           Essa parte é um operador ternário             ]       ,[essa parte é da lista comprehension]
ex5 = [v if v % 2 == 0 and v % 5 == 0 else f'{v} não esta na lista' for v in l4]
print(ex5)

lista_de_nomes = ['italo', 'lidiane', 'sophia', ]
nova_lista_de_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in lista_de_nomes]
print(nova_lista_de_nomes)
