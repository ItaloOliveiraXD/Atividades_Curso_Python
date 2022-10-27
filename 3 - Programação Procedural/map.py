from dados import produtos, pessoas, lista

# Utilizando map em lista
nova_lista = map(lambda x: x * 2, lista)
print(lista)
print(list(nova_lista))
print('=' * 80)


# Utilizando map em dicionário
def aumenta_preco(p):
    p['preço'] = round(p['preço'] * (1 + 0.05), 2)
    return p


novos_precos = map(aumenta_preco, produtos)
for produto in novos_precos:
    print(produto)
print('=' * 80)


# Adicionando uma nova chave no dicionário com map
def adicionar_cidade(p):
    p['cidade'] = 'Fortaleza'
    return p


nova_lista_pessoas = map(adicionar_cidade, pessoas)
for pessoa in nova_lista_pessoas:
    print(pessoa)
