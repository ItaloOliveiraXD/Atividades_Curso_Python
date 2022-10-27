from itertools import groupby

alunos = [
    {'nome': 'Italo', 'nota': 'A'},
    {'nome': 'Lidiane', 'nota': 'D'},
    {'nome': 'Sophia', 'nota': 'B'},
    {'nome': 'Yuri', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Felipe', 'nota': 'C'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Marcos', 'nota': 'A'},
    {'nome': 'Bruno', 'nota': 'D'},
    {'nome': 'João', 'nota': 'C'},
]

#Organizar o dicionário
alunos.sort(key=lambda item: item['nota'])
grupo_alunos = groupby(alunos, key=lambda item: item['nota'])
for grupo, lista_alunos in grupo_alunos:
    print(f'Lista de notas {grupo}')
    for valores in lista_alunos:
        print(valores)
    print()
