"""
Formatando valores com modificadores:
:s - Texto (str).
:d - Inteiro (int).
:f - Número de ponto flutuante (float).
:.(NÚMERO)F - quantidade de casas decimais (float). EX:{:.2f}
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f).

> - Esquerda
< - Direita
^ - Centro
"""
# Escolhendo um tamanho para o número.
number1 = 12
print(f'{number1:0>10}')
print(f'{number1:0<10}')
print(f'{number1:0^10}')
print(f'{number1:0<10.2f}')
print('-----------------------------------------')

# Modificando String.
nome = 'Italo Oliveira'
print(f'{nome:#^30}')

nome_formatado = '{:@^30}'.format(nome)
print(nome_formatado)
nome_formatado = '{n:$^30}'.format(n=nome)
print(nome_formatado)
print('-----------------------------------------')

# Outros métodos
nome = 'Italo oliveira'
print(nome.lower())
print(nome.upper())
print(nome.swapcase())
print(nome.title())
