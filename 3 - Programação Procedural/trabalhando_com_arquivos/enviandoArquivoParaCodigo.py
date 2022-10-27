import json

with open('clientes.json', 'r') as file:
    clientes = file.read()
    # Pegando o arquivo e colocando em uma variável
    clientes = json.loads(clientes)

# Utilizando o conteúdo do arquivo.
for key, valor in clientes.items():
    print(key)
    for k1, v1 in valor.items():
        print(f'{k1}: {v1}')
    print()
