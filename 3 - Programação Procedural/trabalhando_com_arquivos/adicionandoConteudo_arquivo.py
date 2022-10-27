# Adicionando conteudo no arquivo.
with open('exemplo.txt', 'a+') as file:
    file.write('Estou adicionando uma nova linha no arquivo.\n')
    file.seek(0)
    print(file.read())
