from classes import Escritor
from classes import Caneta
from classes import ManquinaDeEscrever
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = ManquinaDeEscrever()

# Passando toda class de caneta para a ferramenta, então ela pode utilizar os métodos da classe
escritor.ferramenta = caneta
escritor.ferramenta.escrever()  # Chamando um método da class caneta

# Fazendo o mesmo procedimento com a class Máquina
escritor.ferramenta = maquina
escritor.ferramenta.teclando()  # Chamando um método da class Máquina
