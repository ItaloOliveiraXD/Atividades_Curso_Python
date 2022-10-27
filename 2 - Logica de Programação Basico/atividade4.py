nome = input('Informe seu primeiro nome para analisarmos: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é pequeno!')
elif tamanho_nome <= 6:
    print('Seu nome tem tamanho normal!')
else:
    print('Seu nome é grande!')
