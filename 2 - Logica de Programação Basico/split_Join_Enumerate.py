
#Função Split() é para dividir uma string tornando uma lista.

frase = 'O rato roeu a roupa do rei de roma'
print(f'({frase}) -> sem a função split()')

fraseSplit = frase.split(' ') #Separou todas as letras ou frases depois do espaço em uma lista.
print(f'({fraseSplit}) -> depois de utilizar a função split() virou uma lista.')
print('-----------------------------------------------------------------------------------------------------------')


# Funçao join() é utilizado para juntar uma lista em uma string.
fraseJoin = ' '.join(fraseSplit) # vai retorna a frase original pois essa funçao junta os elementos da lista.
print(f'({fraseJoin}) -> utilizando a função join temos a junção da lista em uma string novamente.')
print('-----------------------------------------------------------------------------------------------------------')


#Função enumerate() é ultilizador para enumerar os valores dentro da lista.
print('Utilizando o enumerate() para saber o indice e o valor.')
for valor, elemento in enumerate(fraseSplit):
    print(f'valorEnumerado = {valor}, Valor do elemento = {elemento}')

