atividade = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

sequencia = 10
lista_atividade = [
    atividade[index:index + sequencia]
    for index in range(0, len(atividade), sequencia)
]
resultado = '.'.join(lista_atividade)
print(resultado)

solucao2 = []
sequencia2 = ''
for numero in atividade:
    sequencia2 += numero
    if numero == '9':
        solucao2.append(sequencia2)
        sequencia2 = ''

print(solucao2)
