"""
Polimorfismo é o princípio que permite que classes derivadas
de uma mesma superclasse tenham métodos iguais (de mesma assinatura),
mas comportamentos deferentes.
Mesma assinatura = Mesma quantidade e mesmo tipo de parâmetros
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg): pass


class B(A):
    # isso é um polimorfismo, pois sobescreve o método falar de A
    def falar(self, msg):
        print(f'B está falando sobre {msg}')


class C(A):
    # isso é um polimorfismo, pois sobescreve o método falar de A
    def falar(self, msg):
        print(f'C está falando sobre {msg}')


b = B()
c = C()
b.falar('Carro')
c.falar('Moto')
