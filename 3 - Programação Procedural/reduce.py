from dados import pessoas, produtos, lista
from functools import reduce

# Somando todo os valore da lista.
total = reduce(lambda ac, i: i + ac, lista, 0)
print(total)

# Somando todos os valores dos produtos
total_preco_produtos = reduce(lambda ac, i: i['preço'] + ac, produtos, 0)
print(round(total_preco_produtos, 2))

# Tirando a media de idade das pessoas
idade_total = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
media_idade = idade_total / len(pessoas)
print(media_idade)
