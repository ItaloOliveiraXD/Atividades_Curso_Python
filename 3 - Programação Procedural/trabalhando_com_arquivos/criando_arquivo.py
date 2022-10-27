# Melhor maneira para criar um arquivo em python.
with open('exemplo1.txt', 'w+') as file1:
    file1.write('Linha 1\n')
    file1.write('Linha 2\n')
    file1.write('Linha 3\n')
    print('0 - Conteúdo dentro do arquivo: ')
    file1.seek(0)
    print(file1.read())
    print('=' * 80)

# Outro exemplos de criar arquivo em python.
file = open('exemplo.txt', 'w+')
file.write('Escrevendo na primeira linha do aquivo criado\n')
file.write('Escrevendo na segunda linha do aquivo criado\n')
file.write('Escrevendo na terceira linha do aquivo criado\n')

# Lendo arquivos
print('1 - Conteúdo dentro do arquivo: ')
file.seek(0, 0)  # Colocando o curso no começo do arquivo
print(file.read())
print('=' * 80)

# lendo arquivo linha por linha.
print('2 - Conteúdo dentro do arquivo: ')
file.seek(0, 0)  # Colocando o curso no começo do arquivo
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('=' * 80)

# Lendo arquivos utilizando o for
print('3 - Conteúdo dentro do arquivo: ')
file.seek(0, 0)
for conteudo in file.readlines():
    print(conteudo, end='')

file.close()
