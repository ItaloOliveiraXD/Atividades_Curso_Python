import random

palavras = ['afobado', 'amendoim', 'caatinga', 'campeonato', 'catapora', 'perfume']
x = random.randint(0, (len(palavras) - 1))
palavraSecreta = palavras[x]
letraCerta = []
letraErrada = []
chance = 6

while True:
    letra = input('Informe uma letra: ')

    if len(letra) > 1 or letra.isnumeric():
        print('Ops! Informe uma letra válida!')
        continue

    if letra in letraCerta:
        print('Você ja informou essa letra! Informe outra.')
        print(f'A palavra é: {palavraFinal}')
        continue

    if letra in letraErrada:
        print('Você ja informou essa letra! Informe outra.')
        print(f'A palavra é: {palavraFinal}')
        continue

    if letra in palavraSecreta:
        letraCerta.append(letra)
        print(f'Parabéns! A palavra tem a letra "{letra}"')
    else:
        print(f'A palavra não tem a letra "{letra}"')
        chance -= 1
        print(f'Você ainda tem {chance} chance.')
        letraErrada.append(letra)

    palavraFinal = ''
    for palavraCerta in palavraSecreta:
        if palavraCerta in letraCerta:
            palavraFinal += palavraCerta
        else:
            palavraFinal += '*'
    print(f'A palavra é: {palavraFinal}')

    if chance <= 0:
        print('Fim de jogo! Você perdeu!')
        print(f'Palavra correta é {palavraSecreta}')
        break
    elif palavraFinal == palavraSecreta:
        print('Parabéns! Você foi demais!')
        break
