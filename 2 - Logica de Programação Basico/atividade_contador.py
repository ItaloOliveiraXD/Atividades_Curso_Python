contador1 = 0
contador2 = 10

while contador1 < 9 and contador2 > 0:
    print(contador1, contador2)
    contador1 += 1
    contador2 -= 1

print('----------------------------------------')

for i, valor in enumerate(range(10, 1, -1)):
    print(i, valor)

