"""
Privacidade dos dados em outra linguagem:
— protect

Privacidade dos dados em python nesse momento:
— protect -> _nomeVariavel

# No python utiliza _ como conversão informando que não quer que meixa no variável.
"""


class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_dados(self, id, nome):
        if 'cliente' not in self._dados:
            self._dados['cliente'] = {id: nome}
        else:
            self._dados['cliente'].update({id: nome})

    def mostra_cliente(self):
        for id, nome in self._dados['cliente'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self._dados['cliente'][id]

bd = BaseDeDados()
bd.inserir_dados(1, 'Maria')
bd.inserir_dados(2, 'João')
bd.inserir_dados(3, 'Zezinho')
bd.apagar_cliente(1)
bd.mostra_cliente()