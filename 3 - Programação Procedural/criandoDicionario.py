# Formas de criar dicionário em python.
dicionario1 = {'chave1': 'valor da chave 1', 'chave2': 'valor da chave 2'}
dicionario2 = dict(chave1='valor da chave 1', chave2='valor da chave 2')

# Adicionar uma novo valor no dicionário.
dicionario1['chave3'] = 'valor da chave 3'  # adicionando um novo valor no dicionário 1
dicionario2['chave4'] = 'valor da chave 4'  # adicionando um novo valor no dicionário 2

# Atualizando o valor em um dicionário
dicionario2['chave4'] = 'novo valor'
print(dicionario2['chave4'])

# Manipulando dicionario
a = dicionario1['chave2']
b = 'chave1' in dicionario1 #Verificando se tem a chave dentro das chaves do dicionário
c = 'valor da chave 1' in dicionario1.values() #Verificando se tem o valor dentro dos valores do dicionário

if 'chave4' in dicionario1:
    print(dicionario1['chave4'])
else:
    dicionario1['chave4'] = 'Valor da chave 4'
    print(f'{dicionario1["chave4"]}, no dicionário 1')

# Apagando item do dicionário.
del dicionario1['chave4']
dicionario1.popitem() # apaga o ultimo valor do dicionário
print(dicionario1)

#interando com dicionários
for k, v in dicionario1.items():
    print(f'Key="{k}", Value="{v}"')

#Copiando um dicionário para outra variável
import copy

dicionario3 = copy.deepcopy(dicionario1) # Agora dicionário 3 recebe dicionário 1 e tem seu próprio lugar na memória

#Concatenando 2 dicionários
dicionario1.update(dicionario2)
print(dicionario1)

