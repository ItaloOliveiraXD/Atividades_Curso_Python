def valorTotal(valor, porcentagem):
    resultado = valor * (1 + porcentagem)
    return resultado

valorInicialCarro = 30000
imposto = 0.03

valorTotalCarro = valorTotal(valorInicialCarro, imposto)

print(valorTotalCarro)
