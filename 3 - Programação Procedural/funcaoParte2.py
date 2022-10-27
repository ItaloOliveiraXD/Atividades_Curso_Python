def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return f'Divisão inválida!'

    return n1 / n2

resultado1 = divisao(8, 2)
resultado2 = divisao(8, 0)
print(resultado1, type(resultado1))
print(resultado2, type(resultado2))

print('-----------------------------------------------------')

def imprimir(msg):
    print(msg)

def checar():
    return imprimir #Está recebendo a função imprimir mas não esta executando pq não foi colocado parênteses

var = checar()
var('Var pode imprimir coisas!')
