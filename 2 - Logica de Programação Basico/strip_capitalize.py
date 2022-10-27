#Função strip() retira o espaço no começo da string e no final da string

frase = 'O Brasil é o pais do futebol, o Brasil é penta campeão, o Brasil vai ser hexa campeão! '
listaDaFrase = frase.split(',') #Transformanda a frase em lista depois de cada ','.
print(listaDaFrase)
print()

print('Sem a função strip().\n')
for valor in listaDaFrase:
    print(f'{valor}')
print('------------------------------------------------------------------')

print('Com a função strip()\n')
for valor2 in listaDaFrase:
    print(f'{valor2.strip()}')
print('------------------------------------------------------------------')

#Função capitalize() deixa o inicio da frase maiúsculo.
print('Com a função strip e capitalize().\n')
for valor3 in listaDaFrase:
    print(f'{valor3.strip().capitalize()}')


