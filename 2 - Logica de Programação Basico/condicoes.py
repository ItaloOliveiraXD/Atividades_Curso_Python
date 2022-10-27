"""
Condições if, elif, else.
"""
salario = float(input('Informe seu salário. \n'))
aumento_salario = 0

if salario < 0:
    print("Valor do Salário inválido!")
elif salario <= 280:
    aumento_salario = 0.15
elif salario <= 700:
    aumento_salario = 0.10
elif salario <= 1500:
    aumento_salario = 0.05

if salario > 0:
    novo_salario = aumento_salario * salario + salario
    print(f'Você tera um aumento de {aumento_salario*100:.0f}%')
    print(f'Seu novo salário será {novo_salario}')
