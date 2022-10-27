class Escritor:
    def __init__(self, nome):
        self._nome = nome
        self._ferramenta = None

    @property
    def nome(self):
        return self._nome

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self._marca = marca

    @property
    def marca(self):
        return self._marca

    def escrever(self):
        print('Caneta está escrevendo...')


class ManquinaDeEscrever:

    def teclando(self):
        print('O escritor está digitando na máquina de escrever...')
