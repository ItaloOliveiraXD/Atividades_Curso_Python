from classes import Cliente
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

cliente1 = Cliente('Italo', 24)
cliente1.inserir_endereco('Fortaleza', 'ce')
cliente1.inserir_endereco('São paulo', 'sp')
cliente1.exibir_cliente()
