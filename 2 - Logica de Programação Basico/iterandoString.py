
frase = 'o rato roeu a roupa do rei de roma' #iterável tem índices.
tamanhoFrase = len(frase)
novaFrase = ''

print(f'Frase principal "{frase}"')

# iteração ou iterar
i = 0
while i < tamanhoFrase:
    letra = frase[i]

#Modificar todas as letras 'r' minúsculas por 'R' maiúsculas.
    if letra == 'r':
        letra = 'R'

    novaFrase += letra
    i += 1

print(f'A frase iterada é: "{novaFrase}"')
