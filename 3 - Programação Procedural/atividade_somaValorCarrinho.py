carrinho = []

carrinho.append(('Produto 1', 25))
carrinho.append(('Produto 2', 5))
carrinho.append(('Produto 3', 60))
carrinho.append(('Produto 4', 90))
carrinho.append(('Produto 5', 20))


total = sum([valor[1] for valor in carrinho])
print(total)

# resultado = 0
# for valor in carrinho:
#     resultado += valor[1]
# print(resultado)