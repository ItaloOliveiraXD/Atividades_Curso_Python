from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

cliente1 = Cliente('Itlalo', 24)
cliente1.falar()
cliente1.comprar()

print()

aluno1 = Aluno('Sophia', 5)
aluno1.falar()
aluno1.estudar()

print()

cliente_vip1 = ClienteVIP('Lidia', 25, 'macedo')
cliente_vip1.falar()
cliente_vip1.comprar()
