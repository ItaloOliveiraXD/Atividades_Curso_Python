clientes = {
    'cliente1' : {
        'nome'  : 'Italo',
        'idade' : 24,
        'cidade' : 'Fortaleza',
    },
    'cliente2' : {
        'nome'  : 'Sophia',
        'idade' : 5,
        'cidade' : 'Fortaleza',
    },
    'cliente3' : {
        'nome'  : 'Lidiane',
        'idade' : 25,
        'cidade' : 'Fortaleza',
    },
    'cliente4' : {
        'nome'  : 'Neto',
        'idade' : 50,
        'cidade' : 'Fortaleza',
    },
}

#Adicionando um cliente
clientes['cliente5'] = {
    'nome' : 'yuri',
    'idade' : '26',
    'cidade' : 'Fortaleza',
}

print(clientes)

#interando no dicionário
for clientes_key, clientes_value in clientes.items():
    print(f'Exibindo {clientes_key}')
    for k, v in clientes_value.items():
        print(f'\t {k} = {v}')
