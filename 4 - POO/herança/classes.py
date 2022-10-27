class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__  # Saber o nome da class que esta utilizando esse atributo

    def falar(self):
        print(f'{self.nome_da_classe} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_da_classe} está comprando...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):  # Adicionando novo atributo a classe filho (sobrenome).
        super().__init__(nome, idade)  # Chamando o construtor da classe pai.
        self.sobrenome = sobrenome
        self.status = 'vip'

    def comprar(self):
        super().comprar()  # Utiliza o método da classe pai mais proxima com a palavra super().
        print(f'{self.nome} {self.sobrenome} tem prioridade porque é {self.status}!')

    def falar(self):
        Pessoa.falar(self)  # Utiliza o método da classe específica que ele deseja usar.
        print(f'{self.nome} {self.sobrenome} tem prioridade porque é {self.status}!')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_da_classe} está estudando...')
