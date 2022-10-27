from classes import CarrinhoDeCompra, Produto
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

carrinho = CarrinhoDeCompra()

p1 = Produto('Televisão', 2500)
p2 = Produto('Notebook', 4000)
p3 = Produto('Celular', 2000)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)

carrinho.lista_produtos()

carrinho.valor_total()
