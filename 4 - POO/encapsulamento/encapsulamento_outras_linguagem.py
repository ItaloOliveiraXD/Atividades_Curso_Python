"""
Privacidade dos dados em outra linguagem:
— public

Privacidade dos dados em python nesse momento:
— public

# isso ocorre porque tudo pode ser alterado em qualquer lugar do código
"""


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_dado(self, identificacao, nome):
        if 'cliente' not in self.dados:
            self.dados['cliente'] = {identificacao: nome}
        else:
            self.dados['cliente'].update({identificacao: nome})

    def apagar_dado(self, identificacao):
        del self.dados['cliente'][identificacao]

    def apresentar_dados(self):
        for key, nome in self.dados['cliente'].items():
            print(key, nome)


bd = BaseDeDados()
bd.inserir_dado(1, 'Italo')
bd.inserir_dado(2, 'Lidia')
bd.inserir_dado(3, 'Sophia')
bd.apagar_dado(2)
bd.apresentar_dados()
# Nessa maneira posso alterar tudo que eu quiser que estiver dentro da classe.
# EX:
# bd.dados = '12345' -> nesse momento a Variável dados da classe deixa de ser dict e passa a ser do tipo numérico.
