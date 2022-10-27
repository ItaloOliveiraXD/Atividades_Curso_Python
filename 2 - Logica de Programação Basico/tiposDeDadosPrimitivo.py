"""
Tipos de dados.
str - string ( Texto 'assim' e "assim")
int - inteiro ( -2, -1, 0, 1, 2)
float - real/ponto flutuante (-2.2, -1.1, 0.0, 1.1, 2.2)
bool - booleano/lógico ( true/false)
"""
print('Conferindo os tipos que estao declarados:')
print('assim',type('assim'))
print(123, type(123))
print(123.321, type(123.321))
print(10==10, type(10==10))
print(10.1 == 10, type(10.1 == 10))
# Converter str para int com typecast
print('10', type('10'), type(int('10')))
print('--------------------------------------------')

# Nome: str
print('Italo oliveira', type('Italo oliveira'))
# Idade: int
print(24, type(24))
# Altura: float
print(1.81, type(1.81))
# Maior de idade: boll
print(24 > 18, type(24 > 18))


