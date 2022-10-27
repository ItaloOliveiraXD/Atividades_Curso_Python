import json

clientes = {
    'Cliente 1': {
        'nome': 'Italo',
        'idade': 24,
        'cidade': 'Fortaleza'
    },
    'Cliente 2': {
        'nome': 'Sophia',
        'idade': 5,
        'cidade': 'Fortaleza'
    },
    'Cliente 3': {
        'nome': 'Lidiane',
        'idade': 25,
        'cidade': 'Fortaleza'
    },
}

# Guardando conteúdos do código dentro de arquivos
clientes_json = json.dumps(clientes, indent=True)  # Convertendo para json
with open('clientes.json', 'w+')as file:
    file.write(clientes_json)
