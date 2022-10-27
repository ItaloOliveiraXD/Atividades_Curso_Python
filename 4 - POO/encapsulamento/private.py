"""
Privacidade dos dados em outra linguagem:
— private

Privacidade dos dados em python nesse momento:
— private -> __nomeVariavel

# No python utiliza _ como conversão informando que não quer que meixa no variável.
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_dados(self, id, nome):
        if 'cliente' not in self.__dados:
            self.__dados['cliente'] = {id: nome}
        else:
            self.__dados['cliente'].update({id: nome})

    def mostra_cliente(self):
        for id, nome in self.__dados['cliente'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['cliente'][id]


bd = BaseDeDados()
bd.__dados = 'lista'
bd.inserir_dados(1, 'Maria')
bd.inserir_dados(2, 'João')
bd.inserir_dados(3, 'Zezinho')
bd.apagar_cliente(1)
bd.mostra_cliente()
print(bd.__dados)
# Se utilizar __ antes da variável não tem como modificar nada dela em outro local do código
