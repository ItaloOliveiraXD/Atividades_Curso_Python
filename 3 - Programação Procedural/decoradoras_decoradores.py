#  Função decoradora.
def pai(funcao):
    def filha1(*args, **kwargs):
        print('Essa função esta decorada.')
        funcao(*args, **kwargs)

    return filha1


@pai  # Isso è um decorador
def filha2():
    print('Oi')

@pai  # Isso è um decorador
def filha3(msg):
    print(msg)

# Esta chamando a funcao pai porque @pai em cima dela o torna filha da função pai.
filha2()
filha3('Olá, :D')
