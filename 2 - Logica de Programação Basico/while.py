# loop infinito
# while True:
#     nome = input('Qual seu nome? ')
#     print(f'Olá {nome}')
# Usamos o CONTINUE para voltar ao inicio do loop
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print('--------------------------------')

'''Usamos BREAK para sair do loop'''
i = 0
while True:
    print(i)
    i+= 1
    if i == 5:
        break
print('-------------------------------')

'''Fazendo linhas e colunas com while'''
i = 0 #representa a coluna
while i < 5:
    j = 0 #representa a linha
    while j < 3:
        print(f'({i},{j})')
        j += 1
    i += 1
print('------------------------------')
