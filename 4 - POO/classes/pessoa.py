from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando!')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar porque esta comendo!')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if self.falando:
            print(f'{self.nome} parou de falar!')
            self.falando = False
        else:
            print(f'{self.nome} não está falando nada.')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return

        if self.falando:
            print(f'{self.nome} não pode comer, porque está falando!')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer!')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo nada.')

    @classmethod  # Pode utilizar tudo da classe, mas não pode utilizar nada das instâncias.
    def ano_nascimento(cls, nome, ano_que_nasceu):
        idade = cls.ano_atual - ano_que_nasceu
        return cls(nome, idade)

    @staticmethod  # Funciona como um função fora da classe só que é utilizada dentro da classe para organização.
    def is_maior(idade):
        if idade >= 18:
            return 'Maior de idade'
        else:
            return 'Menor de idade'
