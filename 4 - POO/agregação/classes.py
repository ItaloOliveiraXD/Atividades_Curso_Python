class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def valor_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        print(soma)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
