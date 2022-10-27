from abc import ABC, abstractmethod


class A(ABC):  # Informando ser uma classe abstrata.
    @abstractmethod
    def falar(self):
        print('A está falando...')

    @abstractmethod
    def correr(self):
        pass


"""
Como B herda de A ele precisa obrigatoriamente ter todas as funções de A
porque A é uma class abstrata.
"""


class B(A):
    def falar(self):
        print('B está falando...')

    def correr(self):
        print('B está correndo...')


"""
Como C herda de B ele pode usar todos os métodos de B e de A pois B herda A
"""


class C(B):
    def falar(self):
        A.falar(self)

    def correr(self):
        super(C, self).correr()


a = C()
a.falar()
a.correr()
