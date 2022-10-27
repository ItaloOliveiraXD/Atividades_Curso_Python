from vendas.preco import aumento, reducao

preco_produto1 = 26.90
preco_produto2 = 75.50
porcentagem = 0.15

preco_com_aumento = aumento(preco_produto1, porcentagem, formatar=True)
print(preco_com_aumento)
preco_com_reducao = reducao(preco_produto2, porcentagem, formatar=True)
print(preco_com_reducao)
