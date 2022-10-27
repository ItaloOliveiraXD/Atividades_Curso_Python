import re


class Produtos:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def preco_com_desconto(self, porcentagem):
        self._preco = self._preco * (1 - porcentagem)

    # Guetter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, valor):
        print('passou aqui')
        self._nome = f'Produto: {valor}, Preço: R$'

    # Guetter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(re.sub(r'\D', '', valor))

        self._preco = valor


produto1 = Produtos('Camisa', 50)
produto1.preco_com_desconto(0.10)
produto1.nome = 'blusa'
print(produto1.nome, produto1.preco)


produto2 = Produtos('Tênis', 150)
produto2.preco_com_desconto(0.15)
print(produto2.nome, produto2.preco)

produto3 = Produtos('Boné', 90)
produto3.preco_com_desconto(0.05)
print(produto3.nome, produto3.preco)
