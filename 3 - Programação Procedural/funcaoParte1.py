def saudacao(msg, nome):  # Função sem valores padrões.
    print(msg, nome)


saudacao('Hello', 'Italo oliveira') #Passando o parâmetro para a função


def saudacao(msg='Olá', nome='Lidiane'):  # Função com valores padrões.
    print(msg, nome)


saudacao() #Chamando a função com o valor padrão
saudacao('Oi', 'Felipe') #Chamando a função alterando o valor padrão
saudacao(nome='Sophia', msg='HI') #Outra maneira de mandar valor para a função
