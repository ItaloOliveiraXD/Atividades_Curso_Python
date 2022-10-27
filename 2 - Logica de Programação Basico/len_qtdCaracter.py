usuario = input('Digite seu usuário: ')
qtd_caracter = len(usuario)

print(usuario, qtd_caracter, type(qtd_caracter))

if qtd_caracter >= 5 and qtd_caracter <= 10:
    print('Login efetuado com sucesso!')
else:
    print('Tamanho do usuário inválido!')

if len(usuario) >= 5 and len(usuario) <=10:
    print('Logando...')
else:
    print('Errou! Tente novamente')

'''Método len() so funciona para tipo string e
.__len__() faz a mesta funçao do len().'''
