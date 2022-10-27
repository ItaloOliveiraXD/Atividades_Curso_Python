'''
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
'''

texto = 'Python'
novoTexto = ''
#Iterando o texto com for
for letra in texto:
    if letra == 't':
        novoTexto += letra.upper()
    elif letra == 'h':
        novoTexto += letra.upper()
    else:
        novoTexto += letra
print(novoTexto)

print('-----------------------')

#Função range implícito
for n in range(10):
    print(n)
print('-----------------------')

#Função range explícito
for n in range(10, 20, 1):
    print(n)
print('-----------------------')
for n in range(20, 10, -1):
    print(n)
