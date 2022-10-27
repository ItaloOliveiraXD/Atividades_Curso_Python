class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def exibir_cliente(self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        for endereco in self.enderecos:
            print(f'Cidade: {endereco.cidade}/{endereco.estado}')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
