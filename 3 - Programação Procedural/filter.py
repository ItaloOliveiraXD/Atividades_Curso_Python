from dados import produtos, pessoas, lista

# Filtrado todos os valores das lista que são maiores ou igual a 5.
nova_lista = filter(lambda x: x >= 5, lista)
print(list(nova_lista))
print('=' * 80)

# Filtrando todos os valores dos produtos maiores que 50 reais.
lista_produtos_caros = filter(lambda p: p['preço'] > 50, produtos)
print('Produtos acima de 50 Reais:')
for produto in lista_produtos_caros:
    for nome, preco in produto.items():
        print(nome, preco)
    print()
print('=' * 80)


# Filtrando usando uma função:
def filtra(pessoa):
    if pessoa['idade'] <= 25:
        return True


lista_pessoas_maior = filter(filtra, pessoas)

for p in lista_pessoas_maior:
    print(p)
