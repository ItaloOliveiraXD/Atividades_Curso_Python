variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'outro valor' #está sendo criado outra variável sem alterar a variável global.
    print(variavel)

def func3():
    #Isso aqui não é uma boa pratica!
    global variavel # Agora está chamando a variável global para dentro da função.
    variavel = 'mais um valor' #Desta maneira altera o valor da variável global.
    print(variavel)

func()
func2()
print(variavel)
func3()
print(variavel)