# *args são qualquer tipo de dados que você nao sabe o tamanho que deseja passar para a função
# **kwargs são os dados com argumentos nomeados.
def func(*args, **kwargs):
    print(args)
    print(kwargs)

    #Interando os valores de args.
    for v in args:
        print(v)

    #Pegando os valores de kwargs.
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    print(nome, sobrenome)



lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
#Mandando a lista desempacotada para a função e quem recebe o valor é *args.
#Mandando argumentos com chaves e quem recebe o valor é **kwargs.
func(*lista, *lista2, nome='italo', sobrenome='oliveira')
