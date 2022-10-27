lista = ['Sophia', 'Italo', 'Lidiane']
buscarLetra = input('Infome a primeira letra do nome: ')

for valor in lista:
    print(valor)
    if valor.lower().startswith(buscarLetra):
        print(f"O nome que começa com '{buscarLetra}' é {valor}")
        break
else:
    print(f"Nenhum nome começa com '{buscarLetra}'")


