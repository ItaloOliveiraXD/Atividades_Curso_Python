from random import randint

gerarCpf = str(randint(000000000, 999999999))
novoCpf = gerarCpf

# Gerar Primeiro Digito.
i = 10
somaValor1 = 0
for elementos in gerarCpf:
    elementos = int(elementos)
    valor1 = elementos * i
    somaValor1 += valor1
    i -= 1

formula = 11 - (somaValor1 % 11)
digito1 = 0 if formula > 9 else formula
digito1 = str(digito1)
novoCpf += digito1

# Gerar Segundo Digito.
i = 11
somaValor2 = 0
for elementos in novoCpf:
    elementos = int(elementos)
    valor2 = elementos * i
    somaValor2 += valor2
    i -= 1

formula = 11 - (somaValor2 % 11)
digito2 = 0 if formula > 9 else formula
digito2 = str(digito2)
novoCpf += digito2

print(novoCpf)
